"""Structural check of docs/italy_focus_outline.txt (Italy focus tree, slice 0).

Run from WW1/:  python -B -X utf8 scripts/check_italy_outline.py
Checks ids, parents, cycles, exclusive symmetry, chronology, bilingual titles and
reports per-wing shape (size, depth, forks, merges, longest straight chain).
"""
import sys
from collections import defaultdict
from pathlib import Path

OUTLINE = Path(__file__).resolve().parents[1] / "docs" / "italy_focus_outline.txt"
TARGET = 200


def load():
    rows = []
    for n, line in enumerate(OUTLINE.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        p = line.split("|")
        if len(p) != 7:
            sys.exit(f"line {n}: expected 7 fields, got {len(p)}")
        wing, fid, year, par, exc, en, pt = [x.strip() for x in p]
        rows.append(dict(wing=wing, id=fid, year=int(year), raw=par, en=en, pt=pt, line=n,
                         parents=[] if par == "-" else [a for a in par.replace("/", ",").split(",")],
                         mode="root" if par == "-" else ("OR" if "/" in par else "AND"),
                         excl=[] if exc == "-" else exc.split(",")))
    return rows


def main():
    rows = load()
    ids = {r["id"]: r for r in rows}
    bad = []
    if len(ids) != len(rows):
        dup = {r["id"] for r in rows if sum(1 for q in rows if q["id"] == r["id"]) > 1}
        bad.append(f"duplicate ids: {sorted(dup)}")
    for r in rows:
        for p in r["parents"]:
            if p not in ids:
                bad.append(f"{r['id']}: unknown parent {p}")
        for e in r["excl"]:
            if e not in ids:
                bad.append(f"{r['id']}: unknown exclusive {e}")
            elif r["id"] not in ids[e]["excl"]:
                bad.append(f"{r['id']} excludes {e} but not the reverse")
        if not r["en"] or not r["pt"]:
            bad.append(f"{r['id']}: missing EN/PT title")
        if "," in r["raw"] and "/" in r["raw"]:
            bad.append(f"{r['id']}: mixed AND/OR parents")
    # cycles / depth
    depth, state = {}, {}

    def dfs(i):
        if state.get(i) == 1:
            bad.append(f"cycle at {i}")
            return 0
        if i in depth:
            return depth[i]
        state[i] = 1
        d = 0 if not ids[i]["parents"] else 1 + max(dfs(p) for p in ids[i]["parents"] if p in ids)
        state[i] = 2
        depth[i] = d
        return d

    for i in ids:
        dfs(i)
    warn = []
    for r in rows:
        for p in r["parents"]:
            if p in ids and ids[p]["year"] > r["year"]:
                warn.append(f"{r['id']} ({r['year']}) comes before parent {p} ({ids[p]['year']})")
    kids = defaultdict(list)
    for r in rows:
        for p in r["parents"]:
            kids[p].append(r["id"])
    print(f"focuses: {len(rows)} (target {TARGET})  unique ids: {len(ids)}")
    print(f"{'wing':5}{'n':>4}{'depth':>7}{'roots':>7}{'forks':>7}{'merges':>8}{'excl.pairs':>11}{'longest straight chain':>24}")
    for w in dict.fromkeys(r["wing"] for r in rows):
        ws = [r for r in rows if r["wing"] == w]
        forks = sum(1 for r in ws if len(kids[r["id"]]) >= 2)
        merges = sum(1 for r in ws if len(r["parents"]) >= 2)
        pairs = sum(len(r["excl"]) for r in ws) // 2
        best = 0
        for r in ws:  # chain start = node whose parent is not a single-child straight link
            if len(r["parents"]) == 1 and len(kids[r["parents"][0]]) == 1:
                continue
            n, cur = 1, r["id"]
            while len(kids[cur]) == 1 and len(ids[kids[cur][0]]["parents"]) == 1:
                cur = kids[cur][0]
                n += 1
            best = max(best, n)
        print(f"{w:5}{len(ws):4}{max(depth[r['id']] for r in ws):7}{sum(1 for r in ws if r['mode']=='root'):7}"
              f"{forks:7}{merges:8}{pairs:11}{best:24}")
    if len(rows) != TARGET:
        bad.append(f"expected {TARGET} focuses, found {len(rows)}")
    for w in warn:
        print("WARN chronology:", w)
    for b in bad:
        print("ERROR:", b)
    print("RESULT:", "OK" if not bad else f"{len(bad)} error(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
