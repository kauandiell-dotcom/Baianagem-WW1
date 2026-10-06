"""Relayout an existing HOI4 focus-tree file in place (prerequisites + x/y only).

Reads a national_focus .txt, optionally joins groups with extra links, reshapes long
straight ladders into fork/merge diamonds and recomputes positions with
scripts/focus_layout.py. Rewards, costs, icons and conditions are never touched.

    python scripts/relayout_focus_tree.py common/national_focus/uk.txt \
        --link ENG_ww1_the_imperial_conference=ENG_ww1_the_liberal_cabinet [--dry-run]

--link CHILD=PARENT adds PARENT as an extra ANY-OF parent of CHILD (use it to join
groups into one wing). --dry-run only prints the report.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import focus_layout as fl


def blocks(text):
    """Yield (start, end) of each top-level ' focus = { ... }' block."""
    for m in re.finditer(r"(?m)^ focus = \{", text):
        depth, i = 1, m.end()
        while depth and i < len(text):
            c = text[i]
            if c == "#":
                i = text.find("\n", i)
                continue
            depth += (c == "{") - (c == "}")
            i += 1
        yield m.start(), i


def parse(text):
    nodes, spans = [], []
    for s, e in blocks(text):
        b = text[s:e]
        fid = re.search(r"(?m)^  id = (\S+)", b).group(1)
        pre = re.findall(r"(?m)^  prerequisite = \{([^}]*)\}", b)
        groups = [re.findall(r"focus = (\S+)", p) for p in pre]
        mx = re.findall(r"(?m)^  mutually_exclusive = \{([^}]*)\}", b)
        excl = [f for blk in mx for f in re.findall(r"focus = (\S+)", blk)]
        x = int(re.search(r"(?m)^  x = (-?\d+)", b).group(1))
        y = int(re.search(r"(?m)^  y = (-?\d+)", b).group(1))
        # first block = ANY-OF parents; each further block is a required (AND) parent group
        parents = groups[0] if groups else []
        also = [g[0] for g in groups[1:] if len(g) == 1]
        if any(len(g) != 1 for g in groups[1:]):
            raise SystemExit(f"{fid}: complex AND-of-OR prerequisites are not supported")
        nodes.append(dict(id=fid, parents=parents, also=also, excl=excl, x=x, y=y))
        spans.append((s, e))
    return nodes, spans


def rewrite(text, nodes, spans, before, nl="\n"):
    out, last = [], 0
    for n, (s, e) in zip(nodes, spans):
        b = text[s:e]
        b = re.sub(r"(?m)^  x = -?\d+", f"  x = {n['x']}", b, count=1)
        b = re.sub(r"(?m)^  y = -?\d+", f"  y = {n['y']}", b, count=1)
        old = before[n["id"]]
        if (old["parents"], old["also"]) != (n["parents"], n["also"]):
            b = re.sub(r"(?m)^  prerequisite = \{[^}]*\}\r?\n", "", b)
            new = ""
            if n["parents"]:
                new += "  prerequisite = { " + " ".join("focus = " + p for p in n["parents"]) + " }" + nl
            for q in n["also"]:
                new += f"  prerequisite = {{ focus = {q} }}{nl}"
            b = re.sub(r"(?m)^(  y = -?\d+\r?\n)", lambda m: m.group(1) + new, b, count=1)
        out += [text[last:s], b]
        last = e
    out.append(text[last:])
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tree")
    ap.add_argument("--link", action="append", default=[], help="CHILD=PARENT extra ANY-OF parent")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-diamonds", action="store_true")
    a = ap.parse_args()
    path = Path(a.tree)
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    nodes, spans = parse(text)
    ids = {n["id"]: n for n in nodes}
    before = {n["id"]: dict(parents=list(n["parents"]), also=list(n["also"])) for n in nodes}
    for l in a.link:
        c, p = l.split("=")
        if c not in ids or p not in ids:
            raise SystemExit(f"unknown id in --link {l}")
        if p not in ids[c]["parents"]:
            ids[c]["parents"].append(p)
    print("before:")
    fl.print_report(nodes, {n["id"]: (n["x"], n["y"]) for n in nodes})
    changed = 0 if a.no_diamonds else fl.diamondize(nodes)
    pos = fl.layout(nodes)
    for n in nodes:
        n["x"], n["y"] = pos[n["id"]]
    print(f"after (re-parented {changed} focuses):")
    fl.print_report(nodes, pos)
    if a.dry_run:
        return
    new = rewrite(text, nodes, spans, before, "\r\n" if b"\r\n" in raw else "\n")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + new.encode("utf-8"))
    print("written", path)


if __name__ == "__main__":
    main()
