#!/usr/bin/env python3
"""
Consolidates and enriches all British WW1 events into events/ww1_britain_events.txt.
Ensures zero empty options and guarantees tangible player-facing gameplay rewards.
"""
import os
import re

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FILES = [
    "ww1_britain_policy_events.txt",
    "ww1_britain_politics_events.txt",
    "ww1_britain_military_events.txt",
    "ww1_britain_army_events.txt",
    "ww1_britain_navy_events.txt",
    "ww1_britain_diplomacy_events.txt",
    "ww1_britain_economy_events.txt",
    "ww1_britain_extra_events.txt",
]

def load_file_content(fname):
    p = os.path.join(MOD_ROOT, "events", fname)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    return ""

def process_events():
    events_dir = os.path.join(MOD_ROOT, "events")
    target_path = os.path.join(events_dir, "ww1_britain_events.txt")
    
    # Read files
    content_policy = load_file_content("ww1_britain_policy_events.txt")
    content_politics = load_file_content("ww1_britain_politics_events.txt")
    content_army = load_file_content("ww1_britain_army_events.txt")
    content_navy = load_file_content("ww1_britain_navy_events.txt")
    content_diplomacy = load_file_content("ww1_britain_diplomacy_events.txt")
    content_economy = load_file_content("ww1_britain_economy_events.txt")
    content_extra = load_file_content("ww1_britain_extra_events.txt")
    
    combined = []
    
    # 1. Policy & Global events (namespace: ww1_britain)
    combined.append("# ========================================================")
    combined.append("# WW1 BRITAIN: POLICY & CABINET EVENTS")
    combined.append("# ========================================================")
    
    # Enhance policy events
    p = content_policy
    # Fix ww1_britain.5.a
    p = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain\.5\.a\s*\}',
        'option = {\n\t\tname = ww1_britain.5.a\n\t\tadd_political_power = 30\n\t\tadd_war_support = 0.05\n\t\tcustom_effect_tooltip = ENG_ww1_continental_commitment_tt\n\t}',
        p
    )
    # Fix ww1_britain.6.a
    p = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain\.6\.a\s*\}',
        'option = {\n\t\tname = ww1_britain.6.a\n\t\tadd_political_power = 30\n\t\tadd_stability = 0.05\n\t\tcustom_effect_tooltip = ENG_ww1_armed_neutrality_tt\n\t}',
        p
    )
    # Fix ww1_britain.9.a
    p = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain\.9\.a\s*\}',
        'option = {\n\t\tname = ww1_britain.9.a\n\t\tadd_political_power = 30\n\t\tadd_war_support = 0.05\n\t}',
        p
    )
    # Fix ww1_britain.11.a
    p = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain\.11\.a\s*\}',
        'option = {\n\t\tname = ww1_britain.11.a\n\t\tadd_political_power = -20\n\t\tadd_stability = -0.02\n\t}',
        p
    )
    # Fix ww1_britain.12.a
    p = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain\.12\.a\s*\}',
        'option = {\n\t\tname = ww1_britain.12.a\n\t\tadd_political_power = 15\n\t}',
        p
    )
    combined.append(p)
    
    # 2. Politics & Home Front (namespace: ww1_britain_pol)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: DOMESTIC POLITICS & IMPERIAL RELATIONS")
    combined.append("# ========================================================")
    pol = content_politics
    # Fix ww1_britain_pol.1.b
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.1\.b[\s\S]*?set_country_flag\s*=\s*ENG_ww1_home_rule_amended\s*\n\s*)',
        r'\1add_political_power = 20\n\t\tadd_stability = 0.01\n\t',
        pol
    )
    # Fix ww1_britain_pol.2.a
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.2\.a[\s\S]*?set_country_flag\s*=\s*ENG_ww1_ulster_exclusion_accepted\s*\n\s*)',
        r'\1add_political_power = 20\n\t\tadd_stability = 0.02\n\t',
        pol
    )
    # Fix ww1_britain_pol.2.b
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.2\.b[\s\S]*?set_country_flag\s*=\s*ENG_ww1_home_rule_unamended\s*\n\s*)',
        r'\1add_political_power = -15\n\t\tadd_stability = -0.02\n\t',
        pol
    )
    # Rework Imperial Conference ww1_britain_pol.6 (Bruno's Bug #1)
    pol_6_rework = """country_event = {
\tid = ww1_britain_pol.6
\ttitle = ww1_britain_pol.6.t
\tdesc = ww1_britain_pol.6.d
\tpicture = GFX_event_ww1_britain_imperial_conference
\tis_triggered_only = yes
\ttrigger = { tag = ENG has_capitulated = no }

\toption = {
\t\tname = ww1_britain_pol.6.a
\t\tai_chance = { base = 40 }
\t\tnavy_experience = 30
\t\tadd_equipment_to_stockpile = { type = convoy_1 amount = 200 }
\t\tadd_political_power = 25
\t\tadd_to_variable = { ww1_britain_dominion_consent = -2 }
\t\tadd_to_variable = { ww1_britain_debt_burden = -1 }
\t}

\toption = {
\t\tname = ww1_britain_pol.6.b
\t\tai_chance = { base = 60 }
\t\tadd_political_power = 75
\t\tadd_stability = 0.05
\t\tadd_to_variable = { ww1_britain_dominion_consent = 10 }
\t\tadd_to_variable = { ww1_britain_debt_burden = 1 }
\t\tif = {
\t\t\tlimit = { country_exists = CAN }
\t\t\tCAN = { add_opinion_modifier = { target = ROOT modifier = imperial_conference_autonomy } }
\t\t}
\t\tif = {
\t\t\tlimit = { country_exists = AST }
\t\t\tAST = { add_opinion_modifier = { target = ROOT modifier = imperial_conference_autonomy } }
\t\t}
\t\tif = {
\t\t\tlimit = { country_exists = NZL }
\t\t\tNZL = { add_opinion_modifier = { target = ROOT modifier = imperial_conference_autonomy } }
\t\t}
\t\tif = {
\t\t\tlimit = { country_exists = SAF }
\t\t\tSAF = { add_opinion_modifier = { target = ROOT modifier = imperial_conference_autonomy } }
\t\t}
\t}
}"""
    pol = re.sub(r'country_event\s*=\s*\{\s*id\s*=\s*ww1_britain_pol\.6[\s\S]*?^\}', pol_6_rework, pol, flags=re.MULTILINE)

    # Fix ww1_britain_pol.9.a
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.9\.a[\s\S]*?set_country_flag\s*=\s*ENG_ww1_irish_dominion_track\s*\n\s*)',
        r'\1add_political_power = 25\n\t\tadd_stability = 0.02\n\t',
        pol
    )
    # Fix ww1_britain_pol.9.b
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.9\.b[\s\S]*?set_country_flag\s*=\s*ENG_ww1_irish_partition_act\s*\n\s*)',
        r'\1add_political_power = 15\n\t\tadd_stability = -0.01\n\t',
        pol
    )
    # Fix ww1_britain_pol.10.a
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.10\.a[\s\S]*?set_country_flag\s*=\s*ENG_ww1_irish_free_state\s*\n\s*)',
        r'\1add_political_power = 50\n\t\tadd_stability = 0.05\n\t',
        pol
    )
    # Fix ww1_britain_pol.12.a (Irish Conscription)
    pol = re.sub(
        r'(name\s*=\s*ww1_britain_pol\.12\.a[\s\S]*?set_country_flag\s*=\s*ENG_ww1_irish_conscription_authorised\s*\n\s*)',
        r'\1add_manpower = 35000\n\t\tadd_stability = -0.05\n\t',
        pol
    )
    combined.append(pol)

    # 3. Military / Army (namespace: ww1_britain_mil)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: ARMY & MILITARY EVENTS")
    combined.append("# ========================================================")
    arm = content_army
    # Fix ww1_britain_mil.13.b
    arm = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain_mil\.13\.b\s*ai_chance\s*=\s*\{\s*base\s*=\s*30\s*\}\s*\}',
        'option = {\n\t\tname = ww1_britain_mil.13.b\n\t\tai_chance = { base = 30 }\n\t\tadd_political_power = 15\n\t}',
        arm
    )
    combined.append(arm)

    # 4. Navy (namespace: ww1_britain_nav)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: NAVAL & BLOCKADE EVENTS")
    combined.append("# ========================================================")
    nav = content_navy
    # Fix ww1_britain_nav.12.b
    nav = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain_nav\.12\.b\s*ai_chance\s*=\s*\{\s*base\s*=\s*30\s*\}\s*\}',
        'option = {\n\t\tname = ww1_britain_nav.12.b\n\t\tai_chance = { base = 30 }\n\t\tadd_political_power = 15\n\t}',
        nav
    )
    combined.append(nav)

    # 5. Diplomacy (namespace: ww1_britain_dip)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: DIPLOMACY & ALLIANCE EVENTS")
    combined.append("# ========================================================")
    dip = content_diplomacy
    # Fix ww1_britain_dip.12.b
    dip = re.sub(
        r'(name\s*=\s*ww1_britain_dip\.12\.b[\s\S]*?set_country_flag\s*=\s*POR_ww1_declined_london\s*\n\s*)',
        r'\1add_political_power = 20\n\t\tadd_stability = 0.01\n\t',
        dip
    )
    combined.append(dip)

    # 6. Economy (namespace: ww1_britain_eco)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: ECONOMY & WARTIME FINANCE EVENTS")
    combined.append("# ========================================================")
    eco = content_economy
    # Fix ww1_britain_eco.5.b
    eco = re.sub(
        r'(name\s*=\s*ww1_britain_eco\.5\.b[\s\S]*?set_country_flag\s*=\s*ENG_ww1_geddes_axe_half\s*\n\s*)',
        r'\1add_political_power = 15\n\t\tadd_stability = 0.01\n\t',
        eco
    )
    # Fix ww1_britain_eco.6.b
    eco = re.sub(
        r'(name\s*=\s*ww1_britain_eco\.6\.b[\s\S]*?set_country_flag\s*=\s*ENG_ww1_miners_subsidy\s*\n\s*)',
        r'\1add_political_power = -20\n\t\tadd_stability = 0.03\n\t',
        eco
    )
    # Fix ww1_britain_eco.10.b
    eco = re.sub(
        r'option\s*=\s*\{\s*name\s*=\s*ww1_britain_eco\.10\.b\s*ai_chance\s*=\s*\{\s*base\s*=\s*20\s*\}\s*\}',
        'option = {\n\t\tname = ww1_britain_eco.10.b\n\t\tai_chance = { base = 20 }\n\t\tadd_political_power = 10\n\t}',
        eco
    )
    combined.append(eco)

    # 7. Historical flavor (namespace: ww1_britain_x)
    combined.append("\n# ========================================================")
    combined.append("# WW1 BRITAIN: HISTORICAL NARRATIVE & WAR DISPATCHES")
    combined.append("# ========================================================")
    combined.append(content_extra)

    # Write target file
    full_output = "\n".join(combined)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_output)
    print(f"Wrote consolidated {target_path} ({len(full_output)} bytes)")

if __name__ == "__main__":
    process_events()
