"""Read-only WW1 checks against the installed game's effective content overlay.

Default: engine/fairness foundation. --content: scripts, focus graphs, localisation,
event/OOB references and referenced GFX. Optional --content-root directories model
unpacked DLC/other content; missing DLC archives are not silently assumed loaded.
This is static evidence, not proof of runtime scope or campaign balance.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Iterator


@dataclass
class Node:
    key: str
    value: str | list["Node"] | None
    line: int
    operator: str = ""

    def get(self, key: str, default=None):
        if isinstance(self.value, list):
            return next((n.value for n in self.value if n.key == key), default)
        return default


@dataclass(frozen=True)
class Issue:
    code: str
    file: str
    line: int
    detail: str
    severity: str = "error"


TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}]|[=<>!]+|[^\s{}=<>!#"]+')


def parse(text: str) -> list[Node]:
    tokens = []
    line, position = 1, 0
    for match in TOKEN.finditer(text):
        if text[position:match.start()].strip():
            raise ValueError(f"Unterminated string near line {line}")
        line += text.count("\n", position, match.start())
        if not match.group().startswith("#"):
            tokens.append((match.group(), line))
        line += match.group().count("\n")
        position = match.end()
    if text[position:].strip():
        raise ValueError(f"Unterminated string near line {line}")

    def block(index: int, nested: bool = False):
        out = []
        while index < len(tokens):
            key, lineno = tokens[index]
            index += 1
            if key == "}":
                if not nested:
                    raise ValueError(f"Unexpected closing brace at line {lineno}")
                return out, index
            if key == "{":
                # Lists such as optional_assets contain anonymous blocks.
                value, index = block(index, True)
                out.append(Node("", value, lineno))
                continue
            operator = ""
            value = None
            if index < len(tokens) and tokens[index][0] in ("=", ">", "<", ">=", "<=", "!=", "=="):
                operator = tokens[index][0]
                index += 1
                if index == len(tokens) or tokens[index][0] == "}":
                    raise ValueError(f"Missing value at line {lineno}")
                value = tokens[index][0]
                index += 1
                if value == "{":
                    value, index = block(index, True)
                elif value in ("rgb", "hsv", "hsv360") and index < len(tokens) and tokens[index][0] == "{":
                    # Native country colours use typed lists: color = rgb { ... }.
                    index += 1
                    value, index = block(index, True)
                else:
                    value = value.strip('"')
            out.append(Node(key.strip('"'), value, lineno, operator))
        if nested:
            raise ValueError("Unclosed block at end of file")
        return out, index

    return block(0)[0]


def walk(nodes: list[Node]) -> Iterator[Node]:
    for node in nodes:
        yield node
        if isinstance(node.value, list):
            yield from walk(node.value)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def lua_native_keys(text: str) -> set[str]:
    """Extract root.namespace.key without mistaking colour tables for namespaces."""
    text = re.sub(r"--\[\[[\s\S]*?\]\]|--[^\n]*", "", text)
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|[A-Za-z_]\w*|[{}=]|[^\s]', text)
    stack: list[str | None] = []
    result = set()
    for i, token in enumerate(tokens):
        if token == "{":
            key = tokens[i - 2] if i >= 2 and tokens[i - 1] == "=" else None
            stack.append(key)
        elif token == "}":
            if stack:
                stack.pop()
        elif i + 1 < len(tokens) and tokens[i + 1] == "=" and len(stack) == 2:
            if stack[0] in ("NDefines", "NDefines_Graphics") and stack[1]:
                result.add(".".join([str(stack[0]), str(stack[1]), token]))
    return result


def defines(path: Path):
    text = re.sub(r"--\[\[[\s\S]*?\]\]", "", read(path))
    for lineno, line in enumerate(text.splitlines(), 1):
        match = re.match(r"\s*(NDefines(?:_Graphics)?\.\w+\.\w+)\s*=\s*(.*?)(?:\s*--.*)?$", line)
        if match:
            yield match[1], match[2].strip(), lineno


def effective_files(mod: Path, roots: list[Path], directory: str, suffix: str) -> dict[str, Path]:
    replace = []
    descriptor = mod / "descriptor.mod"
    if descriptor.exists():
        replace = [n.value.rstrip("/") for n in parse(read(descriptor))
                   if n.key == "replace_path" and isinstance(n.value, str)]
    result = {}
    for root in roots:
        for path in sorted((root / directory).rglob("*")):
            if path.is_file() and path.suffix.lower() == suffix:
                relative = path.relative_to(root).as_posix()
                if not any(relative == p or relative.startswith(p + "/") for p in replace):
                    result[relative] = path
    for path in sorted((mod / directory).rglob("*")):
        if path.is_file() and path.suffix.lower() == suffix:
            result[path.relative_to(mod).as_posix()] = path
    return result


def foundation(mod: Path, game: Path) -> list[Issue]:
    issues = []
    native = set()
    for path in (game / "common/defines").glob("*.lua"):
        native.update(lua_native_keys(read(path)))
    if not native:
        return [Issue("missing_native_defines", str(game), 0, "No native define registry found")]
    effective = {}
    for path in sorted((mod / "common/defines").glob("*.lua")):
        for key, value, line in defines(path):
            if key not in native:
                issues.append(Issue("unknown_define", path.relative_to(mod).as_posix(), line, key))
            effective[key] = (value, path, line)
    for key in ("WEATHER_DISTANCE_CUTOFF", "DRAW_FOW_CUTOFF", "POSTEFFECT_PER_PROVINCE_MAX_SNOW", "POSTEFFECT_TOTAL_MAX_SNOW"):
        full = "NDefines_Graphics.NGraphics." + key
        if full in effective and float(effective[full][0]) <= 0:
            _, path, line = effective[full]
            issues.append(Issue("hidden_weather", path.relative_to(mod).as_posix(), line, full))
    for filename, forbidden in (
        ("baianagem_player_on_actions.txt", {"set_research_slots", "army_experience", "navy_experience", "air_experience"}),
        ("Sv_core_claim.txt", {"add_core_of"}),
    ):
        path = mod / "common/on_actions" / filename
        if path.exists():
            for node in walk(parse(read(path))):
                if node.key in forbidden:
                    issues.append(Issue("campaign_fairness", path.relative_to(mod).as_posix(), node.line, node.key))
    for path in (mod / "common/units").glob("*.txt"):
        for wrapper in parse(read(path)):
            if wrapper.key != "sub_units" or not isinstance(wrapper.value, list):
                continue
            for unit in wrapper.value:
                categories = unit.get("categories", [])
                if isinstance(categories, list) and any(n.key == "category_special_forces" for n in categories):
                    if unit.get("special_forces") != "yes":
                        issues.append(Issue("uncapped_special_unit", path.relative_to(mod).as_posix(), unit.line, unit.key))
    return issues


def localisation(mod: Path, roots: list[Path]):
    registry = {"english": set(), "braz_por": set()}
    issues = []
    for path in effective_files(mod, roots, "localisation", ".yml").values():
        raw = path.read_bytes()
        # Header determines language even for localisation/replace files.
        # Avoid decoding unrelated native languages just to build EN/PT registries.
        header = next((l.strip() for l in raw[:4096].decode("utf-8-sig", errors="replace").splitlines()
                       if l.strip() and not l.lstrip().startswith("#")), "")
        language = re.fullmatch(r"l_(\w+):", header)
        own = path.is_relative_to(mod)
        if own and not raw.startswith(b"\xef\xbb\xbf"):
            issues.append(Issue("localisation_bom", path.relative_to(mod).as_posix(), 1, "UTF-8 BOM required"))
        if not language:
            if own:
                issues.append(Issue("localisation_header", path.relative_to(mod).as_posix(), 1, header))
            continue
        if language[1] not in registry and not own:
            continue
        try:
            source = raw.decode("utf-8-sig")
        except UnicodeDecodeError as error:
            issues.append(Issue("localisation_encoding", str(path), 0, str(error), "error" if own else "warning"))
            source = raw.decode("utf-8-sig", errors="replace")
        keys = registry.setdefault(language[1], set())
        for line in source.splitlines():
            match = re.match(r'\s*([^\s:#]+):\d*\s+"', line)
            if match:
                keys.add(match[1])
    return registry, issues


def content(mod: Path, roots: list[Path]) -> list[Issue]:
    issues = []
    own = {}

    def registry_parse(path):
        relative = path.relative_to(mod).as_posix() if path.is_relative_to(mod) else str(path)
        if relative in own:
            return own[relative]
        try:
            return parse(read(path))
        except (ValueError, UnicodeError) as error:
            issues.append(Issue("registry_source_syntax", relative, 0, str(error), "error" if path.is_relative_to(mod) else "warning"))
            return []

    for directory in ("common", "events", "history", "interface"):
        for path in sorted((mod / directory).rglob("*")):
            if path.is_file() and path.suffix in (".txt", ".gfx", ".gui"):
                try:
                    own[path.relative_to(mod).as_posix()] = parse(read(path))
                except (ValueError, UnicodeError) as error:
                    issues.append(Issue("script_syntax", path.relative_to(mod).as_posix(), 0, str(error)))
    loc, loc_issues = localisation(mod, roots)
    issues.extend(loc_issues)
    sprites = {}
    for path in effective_files(mod, roots, "interface", ".gfx").values():
        for node in walk(registry_parse(path)):
            if node.key.lower() == "spritetype":
                name = node.get("name")
                texture = node.get("texturefile", node.get("textureFile"))
                if isinstance(name, str):
                    sprites[name] = texture
    event_ids = set()
    for path in effective_files(mod, roots, "events", ".txt").values():
        for node in registry_parse(path):
            if node.key in ("country_event", "news_event", "state_event"):
                event_ids.add(node.get("id"))
    oobs = {Path(rel).stem for rel in effective_files(mod, roots, "history/units", ".txt")}
    referenced = []

    def loc_check(key, filename, line):
        if not isinstance(key, str):
            return
        for language in ("english", "braz_por"):
            if key not in loc[language]:
                issues.append(Issue("missing_localisation", filename, line, language + ": " + key))

    def gfx_check(key, filename, line):
        if not isinstance(key, str) or key.startswith("$"):
            return
        if not key.startswith("GFX_"):
            key = "GFX_" + key
        if key not in sprites:
            issues.append(Issue("missing_sprite", filename, line, key))
            return
        texture = sprites[key]
        if not isinstance(texture, str):
            issues.append(Issue("missing_sprite_texture", filename, line, key))
            return
        texture = texture.replace("\\", "/")
        path = next((root / texture for root in [mod, *reversed(roots)] if (root / texture).is_file()), None)
        if path is None:
            issues.append(Issue("missing_texture", filename, line, key + " -> " + texture))
        else:
            referenced.append((filename, line, key, path))

    for filename, nodes in own.items():
        if filename.startswith("common/national_focus/"):
            for tree in (n for n in nodes if n.key == "focus_tree" and isinstance(n.value, list)):
                focuses = {n.get("id"): n for n in tree.value if n.key == "focus" and isinstance(n.value, list)}
                graph = {}
                for ident, focus in focuses.items():
                    loc_check(ident, filename, focus.line)
                    loc_check(str(ident) + "_desc", filename, focus.line)
                    icon = focus.get("icon")
                    if isinstance(icon, list):
                        for n in walk(icon):
                            if n.key == "value":
                                gfx_check(n.value, filename, n.line)
                    else:
                        gfx_check(icon, filename, focus.line)
                    dependencies = [n.value for n in walk(focus.value) if n.key == "focus" and isinstance(n.value, str)]
                    prerequisites = [n.value for section in focus.value if section.key == "prerequisite" and isinstance(section.value, list)
                                     for n in walk(section.value) if n.key == "focus" and isinstance(n.value, str)]
                    graph[ident] = prerequisites
                    for dep in dependencies:
                        if dep not in focuses:
                            issues.append(Issue("missing_focus_reference", filename, focus.line, str(ident) + " -> " + dep))
                visiting, done = set(), set()
                def visit(key):
                    if key in visiting:
                        issues.append(Issue("focus_cycle", filename, focuses[key].line, str(key)))
                        return
                    if key in done or key not in focuses:
                        return
                    visiting.add(key)
                    for dep in graph[key]:
                        visit(dep)
                    visiting.remove(key)
                    done.add(key)
                for ident in focuses:
                    visit(ident)
        for node in walk(nodes):
            if node.key in ("country_event", "news_event", "state_event") and isinstance(node.value, list):
                ident = node.get("id")
                # Definitions have title/immediate/option; calls contain only scheduling data.
                definition = any(n.key in ("title", "desc", "option", "immediate", "trigger", "is_triggered_only", "hidden") for n in node.value)
                if ident and not definition and ident not in event_ids:
                    issues.append(Issue("missing_event_reference", filename, node.line, str(ident)))
                if definition:
                    for key in ("title", "desc"):
                        loc_check(node.get(key), filename, node.line)
                    gfx_check(node.get("picture"), filename, node.line)
                    for option in (n for n in node.value if n.key == "option"):
                        loc_check(option.get("name"), filename, option.line)
            if node.key in ("load_oob", "load_oob_dlc", "oob") and isinstance(node.value, str):
                if node.value not in oobs:
                    issues.append(Issue("missing_oob_reference", filename, node.line, node.value))
    # Byte equality reveals actual artwork reuse even when sprite names differ.
    hashes = {}
    for filename, line, key, path in referenced:
        if filename.startswith("common/national_focus/"):
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            hashes.setdefault((filename, digest), []).append((line, key))
    for (filename, _), uses in hashes.items():
        if len(uses) > 1:
            issues.append(Issue("repeated_focus_art", filename, uses[0][0], f"{len(uses)} focuses share artwork: " + ", ".join(k for _, k in uses[:5]), "warning"))
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mod", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--game", type=Path, required=True)
    parser.add_argument("--content-root", type=Path, action="append", default=[])
    parser.add_argument("--content", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    issues = foundation(args.mod, args.game)
    if args.content:
        issues += content(args.mod, [args.game, *args.content_root])
    if args.json:
        print(json.dumps([vars(i) for i in issues], ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print(f"{issue.severity.upper()} {issue.code} {issue.file}:{issue.line} {issue.detail}")
        errors = sum(i.severity == "error" for i in issues)
        print(f"Static checks: {errors} errors, {len(issues) - errors} warnings. Runtime validation still required.")
    return int(any(i.severity == "error" for i in issues))


if __name__ == "__main__":
    raise SystemExit(main())
