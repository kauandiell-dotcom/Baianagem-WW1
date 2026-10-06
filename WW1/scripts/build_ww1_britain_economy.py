"""Builds UK wing-2 content (economy and reconstruction). Idempotent.

    python scripts/build_ww1_britain_economy.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_ww1_britain_politics as base
import britain_economy_data as eco
from britain_art_picks import event_sprite

PEACE_CLEANUP = ["ENG_ww1_munitions_contracts", "ENG_ww1_shell_inspection", "ENG_ww1_labour_dilution",
                 "ENG_ww1_food_control", "ENG_ww1_coal_allocation"]


def patch_weekly():
    p = "common/scripted_effects/ww1_britain_administration.txt"
    text, bom, nl = base.read(p)
    if "ENG_ww1_labour_dilution" in text:
        return
    marker = "  remove_ideas = ENG_ww1_emergency_controls"
    if marker not in text:
        raise SystemExit("peace cleanup marker not found")
    extra = "".join(nl + f"  remove_ideas = {i}" for i in PEACE_CLEANUP)
    text = text.replace(marker, marker + extra, 1)
    base.write(p, text, bom)


def build_events():
    out = ["add_namespace = ww1_britain_eco", ""]
    for e in eco.EVENTS:
        n = e["id"]
        out.append("country_event = {")
        out.append(f" id = ww1_britain_eco.{n} title = ww1_britain_eco.{n}.t desc = ww1_britain_eco.{n}.d")
        out.append(f" picture = {event_sprite('ww1_britain_eco.%d' % n)}")
        if e["mode"] == "trigger":
            out.append(" is_triggered_only = yes")
        else:
            out.append(f" mean_time_to_happen = {{ days = {e['days']} }}")
            if e.get("once"):
                out.append(" fire_only_once = yes")
        out.append(f" trigger = {{ tag = ENG has_capitulated = no {e.get('trigger', '')} }}")
        for k, (_pt, _en, eff, ai) in enumerate(e["options"]):
            out += [" option = {", f"  name = ww1_britain_eco.{n}.{'abc'[k]}", f"  ai_chance = {{ base = {ai} }}",
                    "  " + base.effects_block(eff), " }"]
        out.append("}")
    a = eco.ALLY_EVENT
    out += ["country_event = {", f" id = ww1_britain_eco.{a['id']} title = ww1_britain_eco.{a['id']}.t desc = ww1_britain_eco.{a['id']}.d",
            f" picture = {event_sprite('ww1_britain_eco.%d' % a['id'])}", " is_triggered_only = yes",
            " trigger = { NOT = { tag = ENG } }",
            " option = {", f"  name = ww1_britain_eco.{a['id']}.a", "  ai_chance = { base = 80 }", "  add_stability = 0.02",
            "  FROM = { add_to_variable = { ww1_britain_debt_burden = 1 } }", " }",
            " option = {", f"  name = ww1_britain_eco.{a['id']}.b", "  ai_chance = { base = 20 }", " }", "}"]
    base.write("events/ww1_britain_economy_events.txt", "\n".join(out) + "\n")


def build_ideas():
    lines = ["ideas = {", " country = {"]
    for name, (mod, *_r) in eco.IDEAS.items():
        lines.append(f"  ENG_ww1_{name} = {{ picture = ENG_ww1_{name} allowed = {{ always = no }} removal_cost = -1 modifier = {{ {mod} }} }}")
    lines += [" }", "}"]
    base.write("common/ideas/ww1_britain_economy_ideas.txt", "\n".join(lines) + "\n")


def build_decisions():
    out = ["ENG_ww1_empire_policy = {",
           " ENG_ww1_coal_to_allies = {", "  icon = GFX_decision_ENG_ww1_coal_to_allies",
           "  visible = { has_country_flag = ENG_ww1_coal_allocation_done }",
           "  available = { has_war = yes has_capitulated = no is_in_faction = yes }",
           "  cost = 15 days_re_enable = 180",
           "  complete_effect = { every_other_country = { limit = { is_in_faction_with = ROOT } country_event = { id = ww1_britain_eco.10 } } }",
           "  ai_will_do = { base = 1 }", " }",
           " ENG_ww1_war_savings_drive = {", "  icon = GFX_decision_ENG_ww1_war_savings_drive",
           "  visible = { has_country_flag = ENG_ww1_austerity_measures }",
           "  available = { has_war = yes has_capitulated = no }", "  cost = 20 days_re_enable = 240",
           "  complete_effect = { add_to_variable = { ww1_britain_debt_burden = -2 } add_to_variable = { ww1_britain_labour_support = -1 } }",
           "  ai_will_do = { base = 1 modifier = { factor = 3 check_variable = { ww1_britain_debt_burden > 40 } } }", " }", "}"]
    base.write("common/decisions/ww1_britain_economy_decisions.txt", "\n".join(out) + "\n")


def build_loc():
    en, pt = ["l_english:"], ["l_braz_por:"]

    def put(key, p, e):
        pt.append(f' {key}:0 "{base.esc(p)}"')
        en.append(f' {key}:0 "{base.esc(e)}"')
    for fid, (_, dpt, den) in eco.FOCI.items():
        put(f"ENG_ww1_{fid}_desc", dpt, den)
    for e in eco.EVENTS:
        n = e["id"]
        put(f"ww1_britain_eco.{n}.t", *e["t"])
        put(f"ww1_britain_eco.{n}.d", *e["d"])
        for k, (op, oe, _eff, _ai) in enumerate(e["options"]):
            put(f"ww1_britain_eco.{n}.{'abc'[k]}", op, oe)
    a = eco.ALLY_EVENT
    put(f"ww1_britain_eco.{a['id']}.t", *a["t"])
    put(f"ww1_britain_eco.{a['id']}.d", *a["d"])
    put(f"ww1_britain_eco.{a['id']}.a", *a["a"])
    put(f"ww1_britain_eco.{a['id']}.b", *a["b"])
    for name, (_m, npt, nen, dpt, den, _pic) in eco.IDEAS.items():
        put(f"ENG_ww1_{name}", npt, nen)
        put(f"ENG_ww1_{name}_desc", dpt, den)
    for key, d in eco.DECISION_DEFS.items():
        put(key, d["pt"][0], d["en"][0])
        put(key + "_desc", d["pt"][1], d["en"][1])
    base.write("localisation/replace/zz_ww1_britain_economy_l_english.yml", "\n".join(en) + "\n", True)
    base.write("localisation/replace/zz_ww1_britain_economy_l_braz_por.yml", "\n".join(pt) + "\n", True)


if __name__ == "__main__":
    base.patch_focuses(eco.FOCI, eco.EXCLUSIVE)
    patch_weekly()
    build_events()
    build_ideas()
    build_decisions()
    build_loc()
    print(f"UK wing 2: {len(eco.FOCI)} focus rewards, {len(eco.EVENTS)+1} events, {len(eco.IDEAS)} institutions, 2 decisions.")
