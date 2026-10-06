"""Generic builder for UK wings 3+ (data module britain_<slug>_data.py). Idempotent.

    python scripts/build_ww1_britain_wing.py diplomacy

Module contract: NS (event namespace), FOCI, EXCLUSIVE, IDEAS, EVENTS, DECISIONS, optional PEACE_CLEANUP.
Event dict: id, mode ('trigger'|'mtth'), t, d, options [(pt, en, effects, ai)],
            optional trigger (extra ENG conditions) or trigger_full (replaces the ENG default).
"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_ww1_britain_politics as base
from britain_art_picks import event_sprite


def patch_peace_cleanup(ideas):
    """Add remove_ideas lines for wartime institutions to the weekly peace branch (idempotent)."""
    if not ideas:
        return
    p = "common/scripted_effects/ww1_britain_administration.txt"
    text, bom, nl = base.read(p)
    marker = "  remove_ideas = ENG_ww1_emergency_controls"
    if marker not in text:
        raise SystemExit("peace cleanup marker not found")
    extra = "".join(nl + f"  remove_ideas = {i}" for i in ideas if f"remove_ideas = {i}" not in text)
    if extra:
        text = text.replace(marker, marker + extra, 1)
        base.write(p, text, bom)


def build(slug):
    m = importlib.import_module(f"britain_{slug}_data")
    ns = m.NS
    out = [f"add_namespace = {ns}", ""]
    for e in m.EVENTS:
        n, eid = e["id"], f"{ns}.{e['id']}"
        out += ["country_event = {", f" id = {eid} title = {eid}.t desc = {eid}.d", f" picture = {event_sprite(eid)}"]
        if e["mode"] == "trigger":
            out.append(" is_triggered_only = yes")
        else:
            out.append(f" mean_time_to_happen = {{ days = {e['days']} }}")
            if e.get("once"):
                out.append(" fire_only_once = yes")
        trig = e.get("trigger_full") or f"tag = ENG has_capitulated = no {e.get('trigger', '')}"
        out.append(f" trigger = {{ {trig} }}")
        for k, (_pt, _en, eff, ai) in enumerate(e["options"]):
            out += [" option = {", f"  name = {eid}.{'abc'[k]}", f"  ai_chance = {{ base = {ai} }}"]
            if eff:
                out.append("  " + base.effects_block(eff))
            out.append(" }")
        out.append("}")
    base.write(f"events/ww1_britain_{slug}_events.txt", "\n".join(out) + "\n")

    lines = ["ideas = {", " country = {"]
    for name, (mod, *_r) in m.IDEAS.items():
        lines.append(f"  ENG_ww1_{name} = {{ picture = ENG_ww1_{name} allowed = {{ always = no }} removal_cost = -1 modifier = {{ {mod} }} }}")
    lines += [" }", "}"]
    base.write(f"common/ideas/ww1_britain_{slug}_ideas.txt", "\n".join(lines) + "\n")

    cat = getattr(m, "CATEGORY", "ENG_ww1_empire_policy")
    if getattr(m, "CATEGORY_DEF", False):
        base.write(f"common/decisions/categories/ww1_britain_{slug}_categories.txt",
                   f"{cat} = {{\n icon = GFX_decision_{cat}\n allowed = {{ tag = ENG }}\n"
                   " visible = { has_country_flag = ww1_britain_initialised }\n}\n")
    dec = [f"{cat} = {{"]
    for d in m.DECISIONS:
        dec += [f" {d['id']} = {{", f"  icon = GFX_decision_{d['id']}"] + d["lines"] + [" }"]
    dec.append("}")
    base.write(f"common/decisions/ww1_britain_{slug}_decisions.txt", "\n".join(dec) + "\n")

    en, pt = ["l_english:"], ["l_braz_por:"]

    def put(key, p, e):
        pt.append(f' {key}:0 "{base.esc(p)}"')
        en.append(f' {key}:0 "{base.esc(e)}"')
    for fid, (_, dpt, den) in m.FOCI.items():
        put(f"ENG_ww1_{fid}_desc", dpt, den)
    for e in m.EVENTS:
        eid = f"{ns}.{e['id']}"
        put(eid + ".t", *e["t"])
        put(eid + ".d", *e["d"])
        for k, (op, oe, _eff, _ai) in enumerate(e["options"]):
            put(f"{eid}.{'abc'[k]}", op, oe)
    for name, (_m, npt, nen, dpt, den, _pic) in m.IDEAS.items():
        put(f"ENG_ww1_{name}", npt, nen)
        put(f"ENG_ww1_{name}_desc", dpt, den)
    for d in m.DECISIONS:
        put(d["id"], d["pt"][0], d["en"][0])
        put(d["id"] + "_desc", d["pt"][1], d["en"][1])
    if getattr(m, "CATEGORY_DEF", False):
        put(m.CATEGORY, m.CATEGORY_LOC[0], m.CATEGORY_LOC[1])
        put(m.CATEGORY + "_desc", m.CATEGORY_LOC[2], m.CATEGORY_LOC[3])
    base.write(f"localisation/replace/zz_ww1_britain_{slug}_l_english.yml", "\n".join(en) + "\n", True)
    base.write(f"localisation/replace/zz_ww1_britain_{slug}_l_braz_por.yml", "\n".join(pt) + "\n", True)
    base.patch_focuses(m.FOCI, m.EXCLUSIVE)
    patch_peace_cleanup(getattr(m, "PEACE_CLEANUP", []))
    print(f"UK {slug}: {len(m.FOCI)} rewards, {len(m.EVENTS)} events, {len(m.IDEAS)} institutions, {len(m.DECISIONS)} decisions.")


if __name__ == "__main__":
    build(sys.argv[1])
