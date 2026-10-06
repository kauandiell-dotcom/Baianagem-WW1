"""Audit panel for Italy (ITA) WW1 content in Baianagem WW1.

Prints a formatted markdown table comparing targets against actual numbers.
Run from WW1/: python -B -X utf8 scripts/italy_audit.py
"""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ww1_foundation import parse, read, walk

FOCUS_FILE = ROOT / "common" / "national_focus" / "italy.txt"
EFFECTS_FILE = ROOT / "common" / "scripted_effects" / "ww1_italy_effects.txt"
GFX_FILE = ROOT / "interface" / "ww1_italy_goals.gfx"
EN_LOC = ROOT / "localisation" / "english" / "ww1_italy_l_english.yml"
PT_LOC = ROOT / "localisation" / "braz_por" / "ww1_italy_l_braz_por.yml"


def audit():
    results = {}

    # 1. Focuses
    foci = []
    if FOCUS_FILE.is_file():
        nodes = parse(read(FOCUS_FILE))
        trees = [n for n in nodes if n.key == "focus_tree"]
        if trees:
            foci = [n for n in trees[0].value if n.key == "focus"]
    results["focuses"] = len(foci)

    # Focus real reward & ai_will_do & descriptions
    real_rewards = 0
    ai_will_do_count = 0
    en_desc_count = 0
    pt_desc_count = 0
    tot_stab = 0.0
    tot_ws = 0.0
    max_pp = 0.0

    en_text = read(EN_LOC) if EN_LOC.is_file() else ""
    pt_text = read(PT_LOC) if PT_LOC.is_file() else ""

    REAL_EFFECTS = {
        "country_event", "add_political_power", "add_stability", "add_war_support",
        "army_experience", "navy_experience", "air_experience", "add_tech_bonus",
        "add_to_variable", "add_ideas", "remove_ideas", "custom_effect_tooltip",
        "declare_war_on", "create_wargoal", "add_opinion_modifier", "transfer_state",
        "add_building_construction", "build_railway", "set_technology", "give_guarantee"
    }

    for f in foci:
        fid = f.get("id")
        reward = f.get("completion_reward")
        if reward:
            keys = {x.key for x in walk(reward)}
            if (keys & REAL_EFFECTS) or any(k.startswith("ita_ww1_") or k.startswith("ww1_ITA_") for k in keys):
                real_rewards += 1
            for x in walk(reward):
                if x.key == "add_stability" and float(x.value) > 0:
                    tot_stab += float(x.value)
                elif x.key == "add_war_support" and float(x.value) > 0:
                    tot_ws += float(x.value)
                elif x.key == "add_political_power":
                    max_pp = max(max_pp, float(x.value))
        if any(x.key == "ai_will_do" for x in f.value):
            ai_will_do_count += 1
        if f" {fid}_desc:0 " in en_text and ("Immediate effect:" in en_text or "Efeito imediato:" in en_text):
            en_desc_count += 1
        if f" {fid}_desc:0 " in pt_text and ("Immediate effect:" in pt_text or "Efeito imediato:" in pt_text):
            pt_desc_count += 1

    results["real_rewards"] = real_rewards
    results["ai_will_do"] = ai_will_do_count
    results["desc_with_effect"] = min(en_desc_count, pt_desc_count)
    results["tot_stab"] = tot_stab
    results["tot_ws"] = tot_ws
    results["max_pp"] = max_pp

    # 2. Events
    event_files = sorted(ROOT.glob("events/ww1_italy_*.txt"))
    events = []
    for ef in event_files:
        for n in parse(read(ef)):
            if n.key == "country_event":
                events.append(n)
    results["events"] = len(events)

    spontaneous = 0
    multi_opt = 0
    third_party = 0
    for ev in events:
        opts = [x for x in ev.value if x.key == "option"]
        if len(opts) >= 2:
            multi_opt += 1
        keys = {x.key for x in ev.value}
        if ("trigger" in keys or "mean_time_to_happen" in keys) and (ev.get("is_triggered_only") != "yes" or "trigger" in keys):
            spontaneous += 1
        for opt in opts:
            opt_nodes = opt.value if isinstance(opt.value, list) else [opt]
            opt_keys = {x.key for x in walk(opt_nodes)}
            if any(k in ["GER", "AUS", "ENG", "FRA", "TUR", "SER", "GRE"] for k in opt_keys):
                third_party += 1
                break

    results["spontaneous_events"] = spontaneous
    results["multi_opt_events"] = multi_opt
    results["third_party_events"] = third_party

    # 3. Decisions
    dec_files = sorted(ROOT.glob("common/decisions/ww1_italy_*.txt"))
    decisions = []
    for df in dec_files:
        for cat in parse(read(df)):
            for d in cat.value:
                if isinstance(d.value, list):
                    decisions.append(d)
    results["decisions"] = len(decisions)

    cat_file = ROOT / "common" / "decisions" / "categories" / "ww1_italy_categories.txt"
    cats = parse(read(cat_file)) if cat_file.is_file() else []
    results["decision_categories"] = len(cats)

    # 4. Ideas
    ideas_file = ROOT / "common" / "ideas" / "ww1_italy_ideas.txt"
    ideas = []
    if ideas_file.is_file():
        for n in parse(read(ideas_file)):
            if n.key == "ideas":
                for cat in n.value:
                    for idea in cat.value:
                        if isinstance(idea.value, list):
                            ideas.append(idea)
    results["ideas"] = len(ideas)

    # 5. Gauges
    gauges_count = 0
    if EFFECTS_FILE.is_file():
        eff_text = read(EFFECTS_FILE)
        for g in ["ita_ww1_interventionism", "ita_ww1_social_tension", "ita_ww1_army_morale", "ita_ww1_southern_gap", "ita_ww1_irredentism"]:
            if g in eff_text:
                gauges_count += 1
    results["gauges"] = gauges_count

    # 6. Opinion modifiers
    op_files = sorted(ROOT.glob("common/opinion_modifiers/ww1_italy_*.txt"))
    ops = []
    for of in op_files:
        for n in parse(read(of)):
            if n.key == "opinion_modifiers":
                for op in n.value:
                    ops.append(op.key)
    results["opinion_modifiers"] = len(ops)

    # 7. Localisation
    en_keys = set(re.findall(r"^ ([\w.]+):0 ", en_text, re.M))
    pt_keys = set(re.findall(r"^ ([\w.]+):0 ", pt_text, re.M))
    results["loc_keys_en"] = len(en_keys)
    results["loc_keys_pt"] = len(pt_keys)
    results["loc_parity"] = (en_keys == pt_keys and len(en_keys) > 0)
    results["en_bom"] = EN_LOC.is_file() and EN_LOC.read_bytes().startswith(b"\xef\xbb\xbf")
    results["pt_bom"] = PT_LOC.is_file() and PT_LOC.read_bytes().startswith(b"\xef\xbb\xbf")

    # 8. GFX Focus Icons
    gfx_text = read(GFX_FILE) if GFX_FILE.is_file() else ""
    shine_count = len(re.findall(r'name = "GFX_goal_ww1_ITA_ww1_\w+_shine"', gfx_text))
    results["shine_count"] = shine_count

    # Print Report
    print("=" * 70)
    print("PAINEL DE AUDITORIA — ITÁLIA WW1 (ITA)")
    print("=" * 70)
    print(f"{'Item':<35} | {'Meta':<12} | {'Atual':<10} | {'Status'}")
    print("-" * 70)

    rows = [
        ("Focos na Árvore", "200", str(results["focuses"]), "OK" if results["focuses"] == 200 else "FALHA"),
        ("Focos com Efeito Real", "200", str(results["real_rewards"]), "OK" if results["real_rewards"] == 200 else "FALHA"),
        ("ai_will_do em Focos", "200", str(results["ai_will_do"]), "OK" if results["ai_will_do"] == 200 else "FALHA"),
        ("Focos com Efeito no Desc", ">= 180", str(results["desc_with_effect"]), "OK" if results["desc_with_effect"] >= 180 else "FALHA"),
        ("Teto Estabilidade Positiva", "<= 0.15", f"{results['tot_stab']:.2f}", "OK" if results["tot_stab"] <= 0.151 else "EXCEDIDO"),
        ("Teto Apoio Guerra Positivo", "<= 0.20", f"{results['tot_ws']:.2f}", "OK" if results["tot_ws"] <= 0.201 else "EXCEDIDO"),
        ("Teto Poder Político Foco", "<= 60", f"{results['max_pp']:.0f}", "OK" if results["max_pp"] <= 60 else "EXCEDIDO"),
        ("Eventos Novos", ">= 70", str(results["events"]), "OK" if results["events"] >= 70 else "FALHA"),
        ("Eventos Espontâneos", ">= 35", str(results["spontaneous_events"]), "OK" if results["spontaneous_events"] >= 35 else "FALHA"),
        ("Eventos c/ >= 2 Opções", ">= 70", str(results["multi_opt_events"]), "OK" if results["multi_opt_events"] >= 70 else "FALHA"),
        ("Eventos Enviados a 3ºs", ">= 6", str(results["third_party_events"]), "OK" if results["third_party_events"] >= 6 else "FALHA"),
        ("Decisões", ">= 24", str(results["decisions"]), "OK" if results["decisions"] >= 24 else "FALHA"),
        ("Categorias de Decisão", ">= 4", str(results["decision_categories"]), "OK" if results["decision_categories"] >= 4 else "FALHA"),
        ("Ideias/Espíritos", ">= 24", str(results["ideas"]), "OK" if results["ideas"] >= 24 else "FALHA"),
        ("Medidores Internos", "5", str(results["gauges"]), "OK" if results["gauges"] == 5 else "FALHA"),
        ("Modificadores de Opinião", ">= 6", str(results["opinion_modifiers"]), "OK" if results["opinion_modifiers"] >= 6 else "FALHA"),
        ("Ícones c/ _shine", "200", str(results["shine_count"]), "OK" if results["shine_count"] == 200 else "FALHA"),
        ("Paridade Loc EN / PT", "100%", "SIM" if results["loc_parity"] else "NÃO", "OK" if results["loc_parity"] else "FALHA"),
        ("UTF-8 BOM nos .yml", "SIM", "SIM" if results["en_bom"] and results["pt_bom"] else "NÃO", "OK" if results["en_bom"] and results["pt_bom"] else "FALHA"),
    ]

    for item, meta, atual, status in rows:
        print(f"{item:<35} | {meta:<12} | {atual:<10} | {status}")
    print("=" * 70)


if __name__ == "__main__":
    audit()
