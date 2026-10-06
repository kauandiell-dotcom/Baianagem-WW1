"""Reorganiza as arvores de foco da Alemanha e da Russia no molde Austria/Reino Unido/Franca.

Nao cria, apaga nem renomeia foco; nao mexe em efeitos, custos nem icones. So altera:
  * x / y de cada foco (asas lado a lado, bifurcacoes e juncoes, 1 linha por passo);
  * prerequisite de corredores retos longos (viram losangos: bifurca e junta de novo, com E);
  * cabecalho: initial_show_position e um shortcut por asa;
  * search_filters (ausentes) e tokens de filtro invalidos (ARMY/NAVY/AIRFORCE).

    python scripts/relayout_wings.py germany [--dry-run]
    python scripts/relayout_wings.py soviet  [--dry-run]
"""
import argparse
import copy
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import focus_layout as fl
import relayout_tabbed_tree as rt

ROOT = HERE.parent

SPECS = {
    "germany": dict(
        file="common/national_focus/germany.txt", prefix="GER_ww1_shortcut_",
        claim=[
            ("politics", ["GER_kaiser_wilhelm_personal_rule"]),
            ("economy", ["GER_agadir_crisis_gambit"]),
            ("navy_air", ["GER_tirpitz_fourth_naval_bill"]),
            ("global_war", ["GER_mittelafrika_colonial_vision", "GER_hajj_wilhelm_pan_islamic_crusade",
                            "GER_asienkorps_palestine_expedition"]),
            ("diplomacy", ["GER_austro_hungarian_staff_coordination", "GER_willy_nicky_telegrams_bjorko",
                           "GER_emergency_danubian_annexation"]),
            ("endgame", ["GER_the_kaiserschlacht_1918"]),
            ("army", ["GER_army_bill_1912"]),
        ],
        order=["politics", "economy", "navy_air", "global_war", "diplomacy", "army", "endgame"],
        show="politics",
        names={
            "politics": ("Go to: Politics & Society", "Ir para: Política e Sociedade"),
            "economy": ("Go to: Economy & Total War", "Ir para: Economia e Guerra Total"),
            "navy_air": ("Go to: Navy & Air Service", "Ir para: Marinha e Aviação"),
            "global_war": ("Go to: Colonies & the Orient", "Ir para: Colônias e Oriente"),
            "diplomacy": ("Go to: Alliances & the East", "Ir para: Alianças e Leste"),
            "army": ("Go to: Army & Western Front", "Ir para: Exército e Frente Ocidental"),
            "endgame": ("Go to: 1918 Offensives & Collapse", "Ir para: Ofensivas de 1918 e Colapso"),
        }),
    "soviet": dict(
        file="common/national_focus/soviet.txt", prefix="SOV_ww1_shortcut_",
        claim=[
            ("revolution", ["SOV_february_bread_riots_1917"]),
            ("politics", ["SOV_the_empire_of_nicholas_ii"]),
            ("economy", ["SOV_modernizing_the_colossus"]),
            ("navy_air", ["SOV_rebuilding_the_empires_shields"]),
            ("army", ["SOV_the_great_military_program"]),
            ("foreign", ["SOV_third_rome_foreign_policy"]),
        ],
        order=["politics", "revolution", "economy", "army", "navy_air", "foreign"],
        show="politics",
        names={
            "politics": ("Go to: Autocracy & the Duma", "Ir para: Autocracia e Duma"),
            "revolution": ("Go to: Revolution & Civil War", "Ir para: Revolução e Guerra Civil"),
            "economy": ("Go to: Economy, Railways & War Production", "Ir para: Economia, Ferrovias e Produção de Guerra"),
            "army": ("Go to: Army & the General Staff", "Ir para: Exército e Estado-Maior"),
            "navy_air": ("Go to: Fleets & Air Service", "Ir para: Frotas e Serviço Aéreo"),
            "foreign": ("Go to: Diplomacy & War Aims", "Ir para: Diplomacia e Objetivos de Guerra"),
        }),
}

FILTER_FIX = {"FOCUS_FILTER_ARMY": "FOCUS_FILTER_ARMY_XP", "FOCUS_FILTER_NAVY": "FOCUS_FILTER_NAVY_XP",
              "FOCUS_FILTER_AIRFORCE": "FOCUS_FILTER_AIR_XP"}


def links(n):
    return list(n["parents"]) + list(n["also"])


def descendants(by_id, kids, roots, taken):
    out, stack = [], [r for r in roots if r not in taken]
    seen = set()
    while stack:
        i = stack.pop()
        if i in seen or i in taken:
            continue
        seen.add(i)
        out.append(i)
        stack.extend(kids.get(i, []))
    return out


def plan(nodes, spec):
    by_id = {n["id"]: n for n in nodes}
    kids = defaultdict(list)
    for n in nodes:
        for p in links(n):
            kids[p].append(n["id"])
    wing_of, taken = {}, set()
    for key, roots in spec["claim"]:
        for r in roots:
            if r not in by_id:
                raise SystemExit("raiz desconhecida: " + r)
        got = descendants(by_id, kids, roots, taken)
        for i in got:
            wing_of[i] = key
        taken.update(got)
    missing = [i for i in by_id if i not in wing_of]
    if missing:
        raise SystemExit("focos sem asa: %s" % missing[:10])
    return wing_of


def layout_wings(nodes, spec, wing_of, min_run=4, wing_gap=5):
    by_id = {n["id"]: n for n in nodes}
    pos, cursor, changed = {}, 0, {}
    wing_info = {}
    for key in spec["order"]:
        ids = [i for i in by_id if wing_of[i] == key]
        sub = []
        for i in ids:
            n = by_id[i]
            cross = any(wing_of.get(p) != key for p in links(n))
            s = dict(id=i, parents=[p for p in n["parents"] if wing_of.get(p) == key],
                     also=[p for p in n["also"] if wing_of.get(p) == key],
                     excl=list(n["excl"]) + (["__locked__"] if cross else []), x=n["x"], y=n["y"])
            sub.append(s)
        before = {s["id"]: (list(s["parents"]), list(s["also"])) for s in sub}
        fl.diamondize(sub, min_run=min_run)
        for s in sub:
            if (s["parents"], s["also"]) != before[s["id"]]:
                changed[s["id"]] = (list(s["parents"]), list(s["also"]))
        p = fl.layout(sub)
        width = 0
        for i, (x, y) in p.items():
            pos[i] = (x + cursor, y)
            width = max(width, x)
        wing_info[key] = dict(x0=cursor, width=width + 1, ids=ids)
        cursor += width + 1 + wing_gap
    # cross-wing parents must sit above their children: push whole wings down when needed
    for _ in range(10):
        moved = False
        for key in spec["order"]:
            need = 0
            for i in wing_info[key]["ids"]:
                for p in links(by_id[i]):
                    if wing_of[p] != key:
                        need = max(need, pos[p][1] + 1 - pos[i][1])
            if need > 0:
                for i in wing_info[key]["ids"]:
                    pos[i] = (pos[i][0], pos[i][1] + need)
                moved = True
        if not moved:
            break
    return pos, changed, wing_info


def apply_changes(by_id, changed):
    for i, (par, also) in changed.items():
        n = by_id[i]
        cross_keep = [p for p in n["parents"] if p not in par and False]
        n["new_parents"], n["new_also"] = par, also


def rewrite(text, nodes, spans, pos, changed, filters, nl):
    out, last = [], 0
    for n, (s, e) in zip(nodes, spans):
        b = text[s:e]
        i = n["id"]
        x, y = pos[i]
        new_pre = None
        if i in changed:
            par, also = changed[i]
            lines = []
            if par:
                lines.append("prerequisite = { " + " ".join("focus = " + p for p in par) + " }")
            for q in also:
                lines.append("prerequisite = { focus = " + q + " }")
            new_pre = lines
        flt = filters.get(i)
        res, depth, skip = [], 0, 0
        for line in b.splitlines(keepends=True):
            clean = rt._strip(line)
            if skip:
                skip += clean.count("{") - clean.count("}")
                if skip <= 0:
                    skip = 0
                continue
            if depth == 1:
                if re.match(r"\s*x\s*=", clean):
                    line = re.sub(r"(x\s*=\s*)-?\d+", lambda m: m.group(1) + str(x), line, count=1)
                elif re.match(r"\s*y\s*=", clean):
                    line = re.sub(r"(y\s*=\s*)-?\d+", lambda m: m.group(1) + str(y), line, count=1)
                    ind = re.match(r"\s*", line).group(0)
                    if flt:
                        line += ind + "search_filters = { " + " ".join(flt) + " }" + nl
                    if new_pre is not None:
                        line += "".join(ind + l + nl for l in new_pre)
                elif new_pre is not None and re.match(r"\s*prerequisite\s*=\s*\{", clean):
                    bal = clean.count("{") - clean.count("}")
                    if bal > 0:
                        skip = bal
                    continue
            depth += clean.count("{") - clean.count("}")
            res.append(line)
        out += [text[last:s], "".join(res)]
        last = e
    out.append(text[last:])
    return "".join(out)


def infer_filters(text, nodes, spans):
    """Filter list for focuses that have none, based on what their reward does."""
    res = {}
    for n, (s, e) in zip(nodes, spans):
        b = text[s:e]
        if re.search(r"(?m)^\s*search_filters\s*=", b):
            continue
        rew = b[b.find("completion_reward"):] if "completion_reward" in b else ""
        f = []
        rules = [("army_experience", "FOCUS_FILTER_ARMY_XP"), ("navy_experience", "FOCUS_FILTER_NAVY_XP"),
                 ("air_experience", "FOCUS_FILTER_AIR_XP"), ("add_building_construction", "FOCUS_FILTER_INDUSTRY"),
                 ("add_tech_bonus", "FOCUS_FILTER_RESEARCH"), ("add_manpower", "FOCUS_FILTER_MANPOWER"),
                 ("set_politics", "FOCUS_FILTER_POLITICAL"), ("add_stability", "FOCUS_FILTER_STABILITY"),
                 ("add_war_support", "FOCUS_FILTER_WAR_SUPPORT"), ("add_opinion_modifier", "FOCUS_FILTER_ANNEXATION"),
                 ("country_event", "FOCUS_FILTER_POLITICAL"), ("add_ideas", "FOCUS_FILTER_POLITICAL")]
        for key, flt in rules:
            if key in rew and flt not in f:
                f.append(flt)
        res[n["id"]] = (f or ["FOCUS_FILTER_POLITICAL"])[:2]
    return res


def header(text, spec, roots, nl, xs):
    if "initial_show_position" in text[:text.find("focus = {")] and "shortcut" in text[:text.find("focus = {")]:
        return text
    m = re.search(r"(?m)^(\s*)continuous_focus_position\s*=.*$", text)
    if not m:
        raise SystemExit("continuous_focus_position nao encontrado")
    ind = m.group(1)
    add = []
    sx = xs[spec["show"]]
    add.append("%sinitial_show_position = { x = %d y = 0 }" % (ind, sx))
    for key in spec["order"]:
        add.append("%sshortcut = {" % ind)
        add.append("%s\tname = %s%s" % (ind, spec["prefix"], key))
        add.append("%s\ttarget = %s" % (ind, roots[key]))
        add.append("%s\tscroll_wheel_factor = 0.5" % ind)
        add.append("%s}" % ind)
    return text[:m.end()] + nl + nl.join(add) + text[m.end():]


def write_loc(spec, root):
    for lang, idx, fn, head in (("english", 0, "ww1_%s_wings_l_english.yml", "l_english:"),
                                ("braz_por", 1, "ww1_%s_wings_l_braz_por.yml", "l_braz_por:")):
        tag = spec["prefix"].split("_")[0].lower()
        d = root / "localisation" / lang
        d.mkdir(parents=True, exist_ok=True)
        lines = [head]
        for key in spec["order"]:
            lines.append(' %s%s:0 "%s"' % (spec["prefix"], key, spec["names"][key][idx]))
        (d / (fn % tag)).write_bytes(("\ufeff" + "\n".join(lines) + "\n").encode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tree", choices=sorted(SPECS))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-run", type=int, default=4)
    a = ap.parse_args()
    spec = SPECS[a.tree]
    path = ROOT / spec["file"]
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in text else "\n"
    for bad, good in FILTER_FIX.items():
        text = re.sub(re.escape(bad) + r"\b(?!_)", good, text)
    nodes, spans = rt.parse(text)
    rt.resolve_absolute(nodes)
    ln = rt.to_layout_nodes(nodes)
    if any(n["degraded"] for n in ln):
        raise SystemExit("prerequisitos E-de-OU nao suportados")
    wing_of = plan(ln, spec)
    print("antes:")
    fl.print_report(ln, {n["id"]: (n["x"], n["y"]) for n in ln})
    pos, changed, info = layout_wings(ln, spec, wing_of, a.min_run)
    by_id = {n["id"]: n for n in ln}
    for key in spec["order"]:
        sub = [by_id[i] for i in info[key]["ids"]]
        for s in sub:
            if s["id"] in changed:
                s["parents"], s["also"] = changed[s["id"]]
    # keep cross-wing parents on untouched nodes (never changed because locked)
    print("depois (%d focos reparentados):" % len(changed))
    fl.print_report(ln, pos)
    for key in spec["order"]:
        ids = info[key]["ids"]
        print("  asa %-11s %3d focos  x=%d..%d  y=%d..%d" % (
            key, len(ids), min(pos[i][0] for i in ids), max(pos[i][0] for i in ids),
            min(pos[i][1] for i in ids), max(pos[i][1] for i in ids)))
    print("sobreposicoes:", len(pos) - len(set(pos.values())))
    if a.dry_run:
        return
    # roots of each wing: smallest y then x among nodes without an intra-wing parent
    roots, xs = {}, {}
    for key in spec["order"]:
        cand = [i for i in info[key]["ids"]
                if not any(wing_of[p] == key for p in links(by_id[i]))]
        cand.sort(key=lambda i: (pos[i][1], pos[i][0]))
        roots[key] = cand[0]
        xs[key] = pos[cand[0]][0]
    filters = infer_filters(text, nodes, spans)
    new = rewrite(text, nodes, spans, pos, changed, filters, nl)
    new = header(new, spec, roots, nl, xs)
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + new.encode("utf-8"))
    write_loc(spec, ROOT)
    print("escrito", path, "| filtros adicionados:", len(filters))


if __name__ == "__main__":
    main()
