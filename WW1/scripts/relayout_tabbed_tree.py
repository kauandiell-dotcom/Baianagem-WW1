"""Relayout de arvores de foco no formato do mod (tabs ou espacos), ao estilo Austria/UK/Franca.

Nao cria, apaga nem renomeia foco. Mexe so em: prerequisite (juncoes/bifurcacoes), x, y e,
opcionalmente, insere initial_show_position e shortcut ausentes.

    python scripts/relayout_tabbed_tree.py common/national_focus/soviet.txt --dry-run
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import focus_layout as fl


def _strip(line):
    i = line.find("#")
    return line if i < 0 else line[:i]


def split_blocks(text):
    """(start, end) of every 'focus = {' block that sits directly inside the focus_tree block."""
    depth, i, n, line_start = 0, 0, len(text), 0
    opens, spans = [], []
    while i < n:
        c = text[i]
        if c == "#":
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == '"':
            j = text.find('"', i + 1)
            i = n if j < 0 else j + 1
            continue
        if c == "{":
            depth += 1
            if depth == 2 and re.search(r"(?:^|\s)focus\s*=\s*$", text[line_start:i]):
                opens.append(line_start)
            else:
                opens.append(None) if depth == 2 else None
        elif c == "}":
            if depth == 2 and opens:
                s = opens.pop()
                if s is not None:
                    spans.append((s, i + 1))
            depth -= 1
        elif c == "\n":
            line_start = i + 1
        i += 1
    return spans


def parse(text):
    nodes, spans = [], []
    for s, e in split_blocks(text):
        b = text[s:e]
        d = dict(id=None, rawx=None, rawy=None, rel=None, groups=[], excl=[])
        depth, cur, buf = 0, None, ""
        for line in b.splitlines():
            clean = _strip(line)
            if depth == 1 and cur is None:
                for key, pat in (("id", r"id"), ("rawx", r"x"), ("rawy", r"y"), ("rel", r"relative_position_id")):
                    m = re.match(r"\s*" + pat + r"\s*=\s*(\S+)", clean)
                    if m and (key != "id" or d["id"] is None):
                        d[key] = int(m.group(1)) if key in ("rawx", "rawy") else m.group(1)
                m = re.match(r"\s*(prerequisite|mutually_exclusive)\s*=\s*\{", clean)
                if m:
                    cur, buf = m.group(1), ""
            if cur:
                buf += " " + clean
                if buf.count("{") <= buf.count("}"):
                    found = re.findall(r"focus\s*=\s*([^\s}]+)", buf)
                    if cur == "prerequisite":
                        d["groups"].append(found)
                    else:
                        d["excl"].extend(found)
                    cur = None
            depth += clean.count("{") - clean.count("}")
        d["x"], d["y"] = d["rawx"], d["rawy"]
        nodes.append(d)
        spans.append((s, e))
    return nodes, spans


def resolve_absolute(nodes):
    byid = {n["id"]: n for n in nodes}
    memo = {}

    def ab(i):
        if i in memo:
            return memo[i]
        n = byid[i]
        if n["rel"] and n["rel"] in byid:
            px, py = ab(n["rel"])
            memo[i] = (px + (n["rawx"] or 0), py + (n["rawy"] or 0))
        else:
            memo[i] = (n["rawx"] or 0, n["rawy"] or 0)
        return memo[i]

    for n in nodes:
        n["x"], n["y"] = ab(n["id"])


def to_layout_nodes(nodes):
    out = []
    for n in nodes:
        gs = n["groups"]
        parents = list(gs[0]) if gs else []
        also = []
        degraded = False
        for g in gs[1:]:
            if len(g) == 1:
                also.append(g[0])
            else:
                degraded = True
                parents += [p for p in g if p not in parents]
        out.append(dict(id=n["id"], parents=parents, also=also, excl=list(n["excl"]),
                        x=n["x"], y=n["y"], degraded=degraded))
    return out


