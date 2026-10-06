"""Apply reviewed picture/icon bindings while preserving gameplay byte-for-byte.

Run after visual_asset_pipeline.py. Only top-level event/focus header graphics change.
"""
from pathlib import Path
from collections import defaultdict
import argparse
import json
import re
from visual_asset_pipeline import ROOT

def spans(text):
    token = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}]')
    for start in re.finditer(r'(?m)^\s*(country_event|news_event|focus)\s*=\s*\{', text):
        depth = 1
        for match in token.finditer(text, start.end()):
            if match[0] == "{":
                depth += 1
            elif match[0] == "}":
                depth -= 1
            if depth == 0:
                yield start.group(1), start.end(), match.start()
                break

def apply():
    requests = json.loads((ROOT / "docs/visual_asset_requests.json").read_text(encoding="utf-8"))
    grouped = defaultdict(list)
    for record in requests:
        if "bind_file" in record:
            grouped[record["bind_file"]].append(record)
    applied = []
    for relative, records in grouped.items():
        path = ROOT / relative
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")
        replacements = []
        for record in records:
            identity = record.get("bind_event", record.get("bind_focus"))
            property_name = "picture" if "bind_event" in record else "icon"
            found = []
            for block_type, left, right in spans(text):
                header = text[left:right].split("trigger", 1)[0].split("completion_reward", 1)[0]
                identifier = re.search(r'(?m)^\s*id\s*=\s*([^\s{}]+)', header)
                graphic = re.search(r'(?m)^\s*' + property_name + r'\s*=\s*([^\s{}]+)', header)
                if identifier and identifier[1] == identity and graphic:
                    found.append((left + graphic.start(1), left + graphic.end(1), graphic[1]))
            if len(found) != 1:
                raise ValueError(f"Expected one graphics header for {relative}:{identity}, found {len(found)}")
            left, right, old = found[0]
            replacements.append((left, right, record["sprite"]))
            applied.append({"file": relative, "id": identity, "old_sprite": old, "sprite": record["sprite"],
                            "source_relative": record.get("source_relative", record.get("source_project"))})
        edited = text
        for left, right, new in sorted(replacements, reverse=True):
            edited = edited[:left] + new + edited[right:]
        scrub = lambda s: re.sub(r'(?m)^(\s*(?:picture|icon)\s*=\s*)[^\r\n]+', r'\1[ART]', s)
        if scrub(edited) != scrub(text):
            raise AssertionError(f"A non-graphics line changed in {relative}")
        if edited != text:
            prefix = b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b""
            path.write_bytes(prefix + edited.encode("utf-8"))
    (ROOT / "docs/visual_binding_manifest.json").write_text(json.dumps(applied, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Applied {len(applied)} individual graphics bindings. Gameplay text preserved.")

if __name__ == "__main__":
    apply()
