"""Generic focus-tree layout tool (HOI4 1.19): wings, diamonds, tidy positions, report.

Used by the country builders (Austria-Hungary now; UK and Italy next). It never
creates, renames or deletes a focus. It only (a) reshapes long straight ladders
into fork/merge "diamonds" and (b) computes x/y so a tree reads like the vanilla
German tree: one wing per connected group, forks spread under their parent,
merges centred under their parents, wings side by side.

Node format (plain dicts, ids already fully qualified):
    {"id": str, "parents": [ids, any-one-of (OR)], "also": [ids, all required (AND)],
     "excl": [ids], "x": seed_x, "y": seed_y}

API
    diamondize(nodes, min_run=4) -> number of nodes re-parented
    layout(nodes, gap_x=2, wing_gap=4) -> {id: (x, y)}
    report(nodes, pos) -> list of per-wing dicts
    print_report(nodes, pos)
"""
from collections import defaultdict


def _links(n):
    return list(n["parents"]) + list(n.get("also", []))


def _maps(nodes):
    ids = {n["id"]: n for n in nodes}
    kids = defaultdict(list)
    for n in nodes:
        for p in _links(n):
            kids[p].append(n["id"])
    return ids, kids


def diamondize(nodes, min_run=4):
    """Turn straight ladders into anchor -> (a | b) -> merge -> (a | b) ... patterns.

    A run is a maximal chain of nodes with exactly one parent and (except the
    last) exactly one child. Nodes with mutually exclusive partners never move.
    Returns how many nodes got a new prerequisite.
    """
    ids, kids = _maps(nodes)
    seen, changed = set(), 0

    def plain(n):
        return len(n["parents"]) == 1 and not n.get("also") and not n["excl"]

    for n in nodes:
        if n["id"] in seen or not plain(n):
            continue
        p = ids.get(n["parents"][0])
        # start of a run: parent is absent/forking/not plain-single-child
        if p is not None and plain(p) and len(kids[p["id"]]) == 1:
            continue
        run, cur = [n], n
        while len(kids[cur["id"]]) == 1:
            nxt = ids[kids[cur["id"]][0]]
            if not plain(nxt) or nxt["id"] in seen:
                break
            run.append(nxt)
            cur = nxt
        seen.update(x["id"] for x in run)
        if len(run) < min_run:
            continue
        anchor, i = run[0], 1
        while i + 2 < len(run):
            a, b, m = run[i], run[i + 1], run[i + 2]
            b["parents"] = [anchor["id"]]
            m["parents"] = [a["id"]]
            m["also"] = [b["id"]]
            changed += 2
            anchor, i = m, i + 3
        if i < len(run) - 1:  # two leftovers: make them siblings of the anchor
            run[i + 1]["parents"] = [anchor["id"]]
            changed += 1
    return changed


def _components(nodes):
    ids = {n["id"]: n for n in nodes}
    parent = {i: i for i in ids}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for n in nodes:
        for p in _links(n):
            if p in ids:
                parent[find(n["id"])] = find(p)
    groups = defaultdict(list)
    for n in nodes:
        groups[find(n["id"])].append(n)
    return sorted(groups.values(), key=lambda g: min(n["x"] for n in g))


def _depths(nodes):
    ids = {n["id"]: n for n in nodes}
    memo = {}

    def d(i):
        if i not in memo:
            memo[i] = 0
            ps = [p for p in _links(ids[i]) if p in ids]
            memo[i] = 0 if not ps else 1 + max(d(p) for p in ps)
        return memo[i]

    return {i: d(i) for i in ids}


def _pack(layer, target, seed, gap):
    order = sorted(layer, key=lambda i: (target[i], seed[i]))
    xs, prev = {}, None
    for i in order:
        xs[i] = target[i] if prev is None else max(target[i], xs[prev] + gap)
        prev = i
    shift = sum(target[i] - xs[i] for i in order) / len(order)
    return {i: xs[i] + shift for i in order}


def layout(nodes, gap_x=2, wing_gap=4, step_y=1, rounds=6):
    depth = _depths(nodes)
    out, cursor = {}, 0
    for comp in _components(nodes):
        ids = {n["id"]: n for n in comp}
        kids = defaultdict(list)
        for n in comp:
            for p in _links(n):
                kids[p].append(n["id"])
        seed = {n["id"]: n["x"] * 1000 + n["y"] for n in comp}
        x = {n["id"]: float(n["x"]) for n in comp}
        layers = defaultdict(list)
        for i in ids:
            layers[depth[i]].append(i)
        top = min(layers)
        for r in range(rounds):
            for d in sorted(layers):  # top-down: centre under parents
                tgt = {}
                for i in layers[d]:
                    ps = [p for p in _links(ids[i]) if p in x]
                    tgt[i] = sum(x[p] for p in ps) / len(ps) if ps else x[i]
                x.update(_pack(layers[d], tgt, seed, gap_x))
            if r == rounds - 1:
                break
            for d in sorted(layers, reverse=True):  # bottom-up: centre over children
                tgt = {}
                for i in layers[d]:
                    cs = [c for c in kids[i] if c in x]
                    tgt[i] = (sum(x[c] for c in cs) / len(cs)) if cs else x[i]
                x.update(_pack(layers[d], tgt, seed, gap_x))
        lo = min(x.values())
        width = 0
        for i in ids:
            px = int(round(x[i] - lo)) + cursor
            out[i] = (px, (depth[i] - top) * step_y)
            width = max(width, px - cursor)
        cursor += width + gap_x + wing_gap
    return out


def _crossings(edges, pos):
    n = 0
    for (a, b), (c, d) in ((e1, e2) for k, e1 in enumerate(edges) for e2 in edges[k + 1:]):
        if pos[a][1] == pos[c][1] and pos[b][1] == pos[d][1] and len({a, b, c, d}) == 4:
            if (pos[a][0] - pos[c][0]) * (pos[b][0] - pos[d][0]) < 0:
                n += 1
    return n


def report(nodes, pos):
    ids, kids = _maps(nodes)
    rows = []
    for comp in _components(nodes):
        cid = {n["id"] for n in comp}
        xs = [pos[i][0] for i in cid]
        ys = [pos[i][1] for i in cid]
        forks = sum(1 for i in cid if len(kids[i]) >= 2)
        merges = sum(1 for i in cid if len(_links(ids[i])) >= 2)
        edges = [(p, i) for i in cid for p in _links(ids[i]) if p in cid]
        long_edges = sum(1 for p, i in edges
                         if abs(pos[p][0] - pos[i][0]) + abs(pos[p][1] - pos[i][1]) > 12)
        straight, best = set(), 0
        for i in cid:
            n = ids[i]
            ps = _links(n)
            if len(ps) == 1 and len(kids[ps[0]]) == 1 and len(_links(ids[ps[0]])) <= 1:
                continue
            length, cur = 1, i
            while len(kids[cur]) == 1 and len(_links(ids[kids[cur][0]])) == 1:
                cur = kids[cur][0]
                length += 1
            best = max(best, length)
        overlaps = len(cid) - len({pos[i] for i in cid})
        rows.append(dict(n=len(cid), width=max(xs) - min(xs) + 2, depth=max(ys) + 1,
                         forks=forks, merges=merges, longest_straight=best,
                         long_edges=long_edges, overlaps=overlaps,
                         crossings=_crossings(edges, pos), x0=min(xs)))
    return rows


def print_report(nodes, pos):
    print(f"{'wing':>4}{'n':>5}{'width':>7}{'depth':>7}{'forks':>7}{'merges':>8}"
          f"{'straight':>9}{'longE':>7}{'cross':>7}{'overlap':>8}")
    for k, r in enumerate(report(nodes, pos), 1):
        print(f"{k:>4}{r['n']:>5}{r['width']:>7}{r['depth']:>7}{r['forks']:>7}{r['merges']:>8}"
              f"{r['longest_straight']:>9}{r['long_edges']:>7}{r['crossings']:>7}{r['overlaps']:>8}")
