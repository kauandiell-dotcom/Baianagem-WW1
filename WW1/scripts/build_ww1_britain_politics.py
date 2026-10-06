"""Builds UK wing-1 content (politics, empire, Ireland) into the mod. Idempotent.

    python scripts/build_ww1_britain_politics.py

Touches only UK-owned files: common/national_focus/uk.txt (rewards + two exclusions),
common/scripted_effects/ww1_britain_administration.txt (two new variables),
and generated files named ww1_britain_politics_* (events, ideas, decisions, localisation).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from britain_politics_data import FOCI, EXCLUSIVE
import britain_politics_events as ev
from britain_art_picks import event_sprite

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ENG_ww1_"


def read(p):
    raw = (ROOT / p).read_bytes()
    return raw.decode("utf-8-sig"), raw.startswith(b"\xef\xbb\xbf"), "\r\n" if b"\r\n" in raw else "\n"


def write(p, text, bom=False):
    path = ROOT / p
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8"))


def find_block(text, fid):
    m = re.search(r"(?m)^ focus = \{\r?\n  id = " + re.escape(PREFIX + fid) + r"\r?\n", text)
    if not m:
        raise SystemExit(f"focus {fid} not found")
    depth, i = 1, m.end()
    while depth:
        c = text[i]
        depth += (c == "{") - (c == "}")
        i += 1
    return m.start(), i


def patch_focuses(foci=None, exclusive=None):
    foci = FOCI if foci is None else foci
    exclusive = EXCLUSIVE if exclusive is None else exclusive
    text, bom, nl = read("common/national_focus/uk.txt")
    for fid, (effects, _, _) in foci.items():
        s, e = find_block(text, fid)
        block = text[s:e]
        r = re.search(r"(?m)^  completion_reward = \{", block)
        depth, i = 1, r.end()
        while depth:
            depth += (block[i] == "{") - (block[i] == "}")
            i += 1
        body = (nl + "   ").join(effects)
        new_reward = "  completion_reward = {" + nl + "   " + body + nl + "  }"
        block = block[:r.start()] + new_reward + block[i:]
        text = text[:s] + block + text[e:]
    for a, b in exclusive:
        for x, y in ((a, b), (b, a)):
            s, e = find_block(text, x)
            block = text[s:e]
            line = f"  mutually_exclusive = {{ focus = {PREFIX}{y} }}"
            if line not in block:
                block = re.sub(r"(?m)^(  y = -?\d+\r?\n)", lambda m: m.group(1) + line + nl, block, count=1)
                text = text[:s] + block + text[e:]
    write("common/national_focus/uk.txt", text, bom)


def patch_scripted_effects():
    p = "common/scripted_effects/ww1_britain_administration.txt"
    text, bom, nl = read(p)
    if "ww1_britain_dominion_consent" in text:
        return
    marker = " set_variable = { ww1_britain_irish_exemption_factor = 0 }" + nl + " remove_ideas = ENG_professional_bef"
    if marker not in text:
        raise SystemExit("initialise marker not found")
    add = (" set_variable = { ww1_britain_irish_exemption_factor = 0 }" + nl +
           " set_variable = { ww1_britain_ulster_tension = 10 }" + nl +
           " set_variable = { ww1_britain_dominion_consent = 50 }" + nl + " remove_ideas = ENG_professional_bef")
    text = text.replace(marker, add)
    clamp = " clamp_variable = { var = ww1_britain_labour_support min = 0 max = 100 }"
    if clamp not in text:
        raise SystemExit("clamp marker not found")
    extra = (clamp + nl + " clamp_variable = { var = ww1_britain_ulster_tension min = 0 max = 100 }" + nl +
             " clamp_variable = { var = ww1_britain_dominion_consent min = 0 max = 100 }" + nl +
             " if = { limit = { check_variable = { ww1_britain_ulster_tension > 69 } } add_to_variable = { ww1_britain_irish_tension = .2 } }")
    text = text.replace(clamp, extra, 1)
    write(p, text, bom)


def effects_block(effects, indent="  "):
    return ("\n" + indent).join(effects)


def build_events():
    out = ["add_namespace = ww1_britain_pol", ""]
    for e in ev.EVENTS:
        n = e["id"]
        out.append("country_event = {")
        out.append(f" id = ww1_britain_pol.{n} title = ww1_britain_pol.{n}.t desc = ww1_britain_pol.{n}.d")
        out.append(f" picture = {event_sprite('ww1_britain_pol.%d' % n)}")
        if e["mode"] == "trigger":
            out.append(" is_triggered_only = yes")
        else:
            out.append(f" mean_time_to_happen = {{ days = {e['days']} }}")
            if e.get("once"):
                out.append(" fire_only_once = yes")
        extra = e.get("trigger", "")
        out.append(f" trigger = {{ tag = ENG has_capitulated = no {extra} }}")
        for k, (pt, en, eff, ai) in enumerate(e["options"]):
            out.append(" option = {")
            out.append(f"  name = ww1_britain_pol.{n}.{'abc'[k]}")
            out.append(f"  ai_chance = {{ base = {ai} }}")
            out.append("  " + effects_block(eff))
            out.append(" }")
        out.append("}")
    d = ev.DOMINION_EVENT
    out += ["country_event = {",
            f" id = ww1_britain_pol.{d['id']} title = ww1_britain_pol.{d['id']}.t desc = ww1_britain_pol.{d['id']}.d",
            f" picture = {event_sprite('ww1_britain_pol.20')}", " is_triggered_only = yes",
            " trigger = { OR = { tag = CAN tag = AST tag = NZL tag = SAF } }",
            " option = {", f"  name = ww1_britain_pol.{d['id']}.a", "  ai_chance = { base = 60 }",
            "  add_manpower = -15000",
            "  FROM = { add_manpower = 15000 add_to_variable = { ww1_britain_dominion_consent = 2 } }",
            " }",
            " option = {", f"  name = ww1_britain_pol.{d['id']}.b", "  ai_chance = { base = 40 }",
            "  FROM = { add_to_variable = { ww1_britain_dominion_consent = -3 } }",
            "  add_stability = 0.01",
            " }", "}"]
    c = ev.IRISH_CRISIS
    out += ["add_namespace = ww1_britain", "country_event = {", f" id = {c['id']} title = {c['id']}.t desc = {c['id']}.d",
            f" picture = {event_sprite('ww1_britain.3')}", " is_triggered_only = yes", " trigger = { tag = ENG has_capitulated = no }"]
    for k, (pt, en, eff, ai) in enumerate(c["options"]):
        out += [" option = {", f"  name = {c['id']}.{'abc'[k]}", f"  ai_chance = {{ base = {ai} }}", "  " + effects_block(eff), " }"]
    out.append("}")
    write("events/ww1_britain_politics_events.txt", "\n".join(out) + "\n")


def build_ideas():
    lines = ["ideas = {", " country = {"]
    for name, (mod, _npt, _nen, _dpt, _den, _picture) in ev.IDEAS.items():
        lines.append(f"  ENG_ww1_{name} = {{ picture = ENG_ww1_{name} allowed = {{ always = no }} removal_cost = -1 modifier = {{ {mod} }} }}")
    lines += [" }", "}"]
    write("common/ideas/ww1_britain_politics_ideas.txt", "\n".join(lines) + "\n")


def build_decisions():
    cat = ("ENG_ww1_empire_policy = {\n icon = GFX_decision_ENG_ww1_empire_policy\n allowed = { tag = ENG }\n"
           " visible = { has_country_flag = ww1_britain_initialised }\n}\n")
    write("common/decisions/categories/ww1_britain_politics_categories.txt", cat)
    out = ["ENG_ww1_empire_policy = {"]
    for tag, (slug, pt_name, en_name) in ev.TAGS.items():
        key = f"ENG_ww1_request_dominion_contingent_{tag}"
        out += [f" {key} = {{", f"  icon = GFX_decision_{key}",
                f"  visible = {{ has_country_flag = ENG_ww1_consulted_{slug} }}",
                f"  available = {{ has_war = yes has_capitulated = no country_exists = {tag} check_variable = {{ ww1_britain_dominion_consent > 29 }} }}",
                "  cost = 20 days_re_enable = 270",
                f"  complete_effect = {{ {tag} = {{ country_event = {{ id = ww1_britain_pol.20 }} }} }}",
                "  ai_will_do = { base = 2 modifier = { factor = 0 check_variable = { ww1_britain_dominion_consent < 40 } } }", " }"]
    out += [" ENG_ww1_reconvene_imperial_conference = {", "  icon = GFX_decision_ENG_ww1_reconvene_imperial_conference",
            "  visible = { has_country_flag = ENG_ww1_imperial_conference_held }",
            "  available = { has_capitulated = no }", "  cost = 30 days_re_enable = 365",
            "  complete_effect = { add_to_variable = { ww1_britain_dominion_consent = 6 } add_to_variable = { ww1_britain_debt_burden = 1 } }",
            "  ai_will_do = { base = 1 modifier = { factor = 0 check_variable = { ww1_britain_dominion_consent > 70 } } }", " }",
            " ENG_ww1_release_irish_prisoners = {", "  icon = GFX_decision_ENG_ww1_release_irish_prisoners",
            "  visible = { check_variable = { ww1_britain_irish_tension > 30 } }",
            "  available = { has_capitulated = no check_variable = { ww1_britain_irish_tension > 40 } }",
            "  cost = 20 days_re_enable = 150",
            "  complete_effect = { add_to_variable = { ww1_britain_irish_tension = -8 } add_to_variable = { ww1_britain_ulster_tension = 4 } }",
            "  ai_will_do = { base = 1 modifier = { factor = 3 check_variable = { ww1_britain_irish_tension > 60 } } }", " }",
            " ENG_ww1_emergency_suppression = {", "  icon = GFX_decision_ENG_ww1_emergency_suppression",
            "  visible = { check_variable = { ww1_britain_irish_tension > 40 } }",
            "  available = { has_capitulated = no check_variable = { ww1_britain_irish_tension > 50 } }",
            "  cost = 15 days_re_enable = 120",
            "  complete_effect = { add_to_variable = { ww1_britain_irish_tension = -5 } add_to_variable = { ww1_britain_ulster_tension = -3 } add_stability = -0.01 }",
            "  ai_will_do = { base = 1 modifier = { factor = 2 check_variable = { ww1_britain_irish_tension > 75 } } }", " }", "}"]
    write("common/decisions/ww1_britain_politics_decisions.txt", "\n".join(out) + "\n")


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_loc():
    en, pt = ["l_english:"], ["l_braz_por:"]

    def put(key, p, e):
        pt.append(f' {key}:0 "{esc(p)}"')
        en.append(f' {key}:0 "{esc(e)}"')
    for fid, (_, dpt, den) in FOCI.items():
        put(f"{PREFIX}{fid}_desc", dpt, den)
    for e in ev.EVENTS:
        n = e["id"]
        put(f"ww1_britain_pol.{n}.t", *e["t"])
        put(f"ww1_britain_pol.{n}.d", *e["d"])
        for k, (op, oe, _eff, _ai) in enumerate(e["options"]):
            put(f"ww1_britain_pol.{n}.{'abc'[k]}", op, oe)
    d = ev.DOMINION_EVENT
    put(f"ww1_britain_pol.{d['id']}.t", *d["t"])
    put(f"ww1_britain_pol.{d['id']}.d", *d["d"])
    put(f"ww1_britain_pol.{d['id']}.a", *d["a"])
    put(f"ww1_britain_pol.{d['id']}.b", *d["b"])
    for name, (_m, npt, nen, dpt, den, _pic) in ev.IDEAS.items():
        put(f"ENG_ww1_{name}", npt, nen)
        put(f"ENG_ww1_{name}_desc", dpt, den)
    put("ENG_ww1_empire_policy", "Política imperial e irlandesa", "Imperial and Irish Policy")
    put("ENG_ww1_empire_policy_desc", "Consultas aos domínios e medidas de emergência na Irlanda. Consentimento dos domínios: [?ww1_britain_dominion_consent|0]. Tensão irlandesa: [?ww1_britain_irish_tension|0]. Tensão no Ulster: [?ww1_britain_ulster_tension|0].",
        "Dominion consultations and emergency measures in Ireland. Dominion consent: [?ww1_britain_dominion_consent|0]. Irish tension: [?ww1_britain_irish_tension|0]. Ulster tension: [?ww1_britain_ulster_tension|0].")
    for tag, (slug, npt, nen) in ev.TAGS.items():
        put(f"ENG_ww1_request_dominion_contingent_{tag}", f"Pedir voluntários a {npt}", f"Request Volunteers from {nen}")
        put(f"ENG_ww1_request_dominion_contingent_{tag}_desc",
            f"Gasta 20 de poder político. Em guerra, pede a {npt} que envie 15.000 de mão de obra. Exige a consulta prévia e consentimento acima de 29. O domínio decide; nada é criado, a mão de obra passa de um país ao outro.",
            f"Spend 20 political power. At war, ask {nen} to send 15,000 manpower. Requires the earlier consultation and consent above 29. The Dominion decides; nothing is created, manpower moves from one country to the other.")
    put("ENG_ww1_reconvene_imperial_conference", "Reunir nova conferência imperial", "Reconvene the Imperial Conference")
    put("ENG_ww1_reconvene_imperial_conference_desc", "Gasta 30 de poder político. Consentimento dos domínios +6 e dívida +1. Disponível a cada ano depois da primeira conferência.",
        "Spend 30 political power. Dominion consent +6 and debt +1. Available once a year after the first conference.")
    put("ENG_ww1_release_irish_prisoners", "Libertar presos irlandeses", "Release Irish Prisoners")
    put("ENG_ww1_release_irish_prisoners_desc", "Gasta 20 de poder político. A tensão irlandesa cai 8 e a tensão no Ulster sobe 4. Exige tensão irlandesa acima de 40.",
        "Spend 20 political power. Irish tension falls by 8 and Ulster tension rises by 4. Requires Irish tension above 40.")
    put("ENG_ww1_emergency_suppression", "Reprimir a agitação", "Suppress the Agitation")
    put("ENG_ww1_emergency_suppression_desc", "Gasta 15 de poder político. A tensão irlandesa cai 5, a do Ulster cai 3 e a estabilidade cai 1%. Exige tensão irlandesa acima de 50.",
        "Spend 15 political power. Irish tension falls by 5, Ulster tension falls by 3 and stability falls by 1%. Requires Irish tension above 50.")
    put("ENG_ww1_autonomy_consultation", "Consulta imperial", "Imperial consultation")
    c = ev.IRISH_CRISIS
    put(c["id"] + ".t", *c["t"])
    put(c["id"] + ".d", *c["d"])
    for k, (op, oe, _eff, _ai) in enumerate(c["options"]):
        put(f"{c['id']}.{'abc'[k]}", op, oe)
    for key, (p_, e_) in ev.LOC_FIXES.items():
        put(key, p_, e_)
    write("localisation/replace/zz_ww1_britain_politics_l_english.yml", "\n".join(en) + "\n", True)
    write("localisation/replace/zz_ww1_britain_politics_l_braz_por.yml", "\n".join(pt) + "\n", True)


if __name__ == "__main__":
    patch_focuses()
    patch_scripted_effects()
    build_events()
    build_ideas()
    build_decisions()
    build_loc()
    print(f"UK wing 1: {len(FOCI)} focus rewards, {len(ev.EVENTS)+2} events, {len(ev.IDEAS)} institutions, 7 decisions.")
