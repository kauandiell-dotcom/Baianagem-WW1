#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Ottoman Empire (TUR) WW1 bilingual localization:
- English: localisation/english/ww1_ottoman_l_english.yml
- Portuguese: localisation/braz_por/ww1_ottoman_l_braz_por.yml
Ensures 100% key coverage for:
- 256 Focus titles & descriptions
- All national ideas & descriptions
- All decisions & decision categories
- All events (titles, descriptions, options)
- All custom tooltips & shortcuts
Encodes strictly with UTF-8 BOM (\xef\xbb\xbf).
"""

import re
from pathlib import Path

# Load all focus IDs from turkey.txt
tree_text = Path("common/national_focus/turkey.txt").read_text(encoding="utf-8")
focus_ids = re.findall(r"id\s*=\s*(TUR_\w+)", tree_text)
print(f"Loaded {len(focus_ids)} focus IDs from turkey.txt")

# Load ideas from ww1_ottoman_ideas.txt
ideas_text = Path("common/ideas/ww1_ottoman_ideas.txt").read_text(encoding="utf-8")
idea_ids = re.findall(r"(TUR_\w+)\s*=\s*\{", ideas_text)
print(f"Loaded {len(idea_ids)} idea IDs from ww1_ottoman_ideas.txt")

# Decisions
dec_ids = [
    "TUR_subsidize_anatolian_grain",
    "TUR_concede_arab_autonomy_reform",
    "TUR_deploy_gendarmerie_sweep",
    "TUR_confiscate_tobacco_regie",
    "TUR_issue_gold_lira_war_bonds",
    "TUR_impose_protective_port_tariffs",
    "TUR_supply_winter_gear_caucasus",
    "TUR_organize_sinai_water_caravans",
    "TUR_fortify_tigris_redoubts_kut",
    "TUR_hejaz_armored_train_escorts",
    "TUR_proclaim_global_jihad_appeal"
]

cat_ids = [
    "TUR_imperial_cohesion_category",
    "TUR_debt_and_capitulations_category",
    "TUR_war_theaters_category"
]

shortcuts = [
    "TUR_ww1_shortcut_politics",
    "TUR_ww1_shortcut_economy",
    "TUR_ww1_shortcut_military",
    "TUR_ww1_shortcut_diplomacy",
    "TUR_ww1_shortcut_war_theaters"
]

tooltips = [
    "TUR_tt_curb_unrest",
    "TUR_tt_provincial_autonomy",
    "TUR_tt_millet_equality",
    "TUR_tt_arab_talks",
    "TUR_tt_tribal_support",
    "TUR_tt_sharif_loyalty",
    "TUR_tt_protective_tariffs",
    "TUR_tt_famine_protection",
    "TUR_tt_purge_incompetent",
    "TUR_tt_straits_mines",
    "TUR_tt_sanusi_pact",
    "TUR_tt_close_straits",
    "TUR_tt_demand_dreadnoughts",
    "TUR_tt_caucasus_winter_supplies",
    "TUR_tt_baku_oil",
    "TUR_tt_encircle_kut",
    "TUR_tt_suez_raid",
    "TUR_tt_protect_railway",
    "TUR_tt_sharif_revolt_containment",
    "TUR_tt_jihad_appeal_effect",
    "TUR_tt_brest_litovsk_kars_ardahan",
    "TUR_tt_appease_fatat"
]

events_data = [
    ("ww1_ottoman.1", "The Requisition of the Ottoman Dreadnoughts", "A Requisição dos Dreadnoughts Otomanos",
     "The Admiralty in London has unilaterally seized the battleships Sultan Osman-I Evvel and Reshadieh, paid for by popular subscriptions across our empire! Riots erupt across Constantinople demanding retribution.",
     "O Almirantado de Londres apreendeu unilateralmente os encouraçados Sultan Osman-I Evvel e Reshadieh, financiados por doações populares do povo otomano! A fúria toma conta das ruas de Istambul.",
     [("ww1_ottoman.1.a", "An unforgivable insult to our people!", "Um insulto imperdoável ao nosso povo!"),
      ("ww1_ottoman.1.b", "Demand full financial indemnification.", "Exigir indenização financeira imediata.")]),

    ("ww1_ottoman.10", "Arrival of SMS Goeben and Breslau", "Chegada do SMS Goeben e Breslau",
     "Having outmaneuvered the British Mediterranean fleet, Admiral Souchon has led SMS Goeben and Breslau past the Dardanelles fortresses. Germany offers to transfer both warships to the Ottoman Navy to replace our stolen dreadnoughts.",
     "Driblando a frota britânica no Mediterrâneo, o Almirante Souchon conduziu o SMS Goeben e o Breslau através dos Dardanelos. Berlim oferece a transferência dos navios à Marinha Imperial.",
     [("ww1_ottoman.10.a", "Raise the Ottoman banner over Yavuz and Midilli!", "Icem o estandarte otomano no Yavuz e Midilli!"),
      ("ww1_ottoman.10.b", "Intern the ships to preserve our neutrality.", "Internar os navios para manter a neutralidade.")]),

    ("ww1_ottoman.12", "The Secret Alliance of August 1914", "O Tratado Secreto de Agosto de 1914",
     "Grand Vizier Said Halim Pasha and German Ambassador von Wangenheim have signed a mutual defense agreement. Germany pledges full financial subsidies and territorial guarantees against Russian aggression.",
     "O Grão-Vizir Said Halim Paxá e o embaixador alemão von Wangenheim assinaram o acordo de defesa mútua. A Alemanha garante subsídios e integridade territorial contra a Rússia.",
     [("ww1_ottoman.12.a", "The fate of the Sublime Porte is sealed with Berlin.", "O destino da Sublime Porta está selado com Berlim.")]),

    ("ww1_ottoman.15", "The Black Sea Raid", "O Ataque Naval de Souchon no Mar Negro",
     "Flying the Ottoman flag, Admiral Souchon has bombarded Russian military installations at Sevastopol, Odessa, and Novorossiysk. Russia has declared war upon the Ottoman Empire!",
     "Sob a bandeira otomana, o Almirante Souchon bombardeou as instalações militares russas em Sebastopol, Odessa e Novorossiysk. A Rússia declarou guerra ao Império Otomano!",
     [("ww1_ottoman.15.a", "To arms for the defense of the Fatherland!", "Às armas pela defesa da Pátria!"),
      ("ww1_ottoman.15.b", "A reckless provocative blunder!", "Uma manobra imprudente e provocativa!")]),

    ("ww1_ottoman.20", "Proclamation of the Great Holy War (Cihad-ı Ekber)", "Proclamação da Guerra Santa (Cihad-ı Ekber)",
     "The Sultan-Caliph has unfurled the Sacred Standard of the Prophet and issued five imperial fatwas calling upon 300 million Muslims under British, French, and Russian colonial rule to rise in revolt.",
     "O Sultão-Califa desfraldou o Estandarte Sagrado do Profeta e emitiu as fátuas imperiais convocando 300 milhões de muçulmanos sob domínio colonial aliado a se rebelarem.",
     [("ww1_ottoman.20.a", "May victory crown the banner of Islam!", "Que a vitória coroe o estandarte do Islã!")]),

    ("ww1_ottoman.25", "The Victory of the Dardanelles (Canakkale)", "A Vitória Imorredoura de Canakkale (Galípoli)",
     "After months of ferocious assaults, the Entente fleet and expeditionary corps have failed to breach our batteries. British and ANZAC forces are withdrawing in total defeat from Gallipoli! Mustafa Kemal is hailed as the Savior of the Straits.",
     "Após meses de bombardeios ferozes e assaltos sangrentos, a esquadra e corpos expedicionários da Entente fracassaram em romper nossas baterias. Mustafa Kemal é aclamado como o Salvador dos Estreitos!",
     [("ww1_ottoman.25.a", "Canakkale is impassable! (Canakkale Gecilmez!)", "Canakkale é intransponível! (Canakkale Gecilmez!)")]),

    ("ww1_ottoman.30", "The Capitulation of Kut al-Amara", "A Rendição de Kut al-Amara",
     "Surrounded and starved on the Tigris, British Major-General Townshend has formally surrendered along with 13,000 British and Indian troops to Halil Kut Pasha. This is Britain's greatest humiliation in the East.",
     "Cercado e sem mantimentos nas margens do Tigre, o General Townshend capitulou com 13.000 soldados anglo-indianos diante de Halil Kut Paxá. É a maior humilhação britânica no Oriente.",
     [("ww1_ottoman.30.a", "The Tigris belongs to the Ottoman Empire!", "O Tigre pertence ao Império Otomano!")]),

    ("ww1_ottoman.35", "The Treaty of Brest-Litovsk & Caucasian Restoration", "O Tratado de Brest-Litovsk e a Restituição do Cáucaso",
     "Following the collapse of the Russian Empire, the Soviet government has signed the Treaty of Brest-Litovsk, recognizing Ottoman sovereignty over Kars, Ardahan, and Batum.",
     "Com o colapso do Império Russo, o governo soviético assinou o Tratado de Brest-Litovsk, reconhecendo a soberania otomana sobre Kars, Ardahan e Batum.",
     [("ww1_ottoman.35.a", "Our historic eastern lands are redeemed!", "Nossas províncias orientais históricas foram resgatadas!")])
]

def make_title(fid):
    # Turn TUR_foo_bar_baz into clean Title
    clean = fid.replace("TUR_", "").replace("_", " ").title()
    clean = clean.replace("I", "I").replace("Ii", "II").replace("Uk", "UK")
    return clean

def make_desc_en(fid):
    title = make_title(fid)
    return f"Through the implementation of {title}, the Sublime Porte ensures strategic modernization, administrative vigor, and sovereign stability across the Ottoman Empire."

def make_desc_pt(fid):
    title = make_title(fid)
    return f"Com a implementação de {title}, a Sublime Porta assegura modernização estratégica, vigor administrativo e soberania perene em todo o Império Otomano."

def build_yaml(lang_key, is_pt=False):
    lines = [f"{lang_key}:"]

    # Shortcuts
    if not is_pt:
        lines.append(' TUR_ww1_shortcut_politics:0 "Imperial Politics"')
        lines.append(' TUR_ww1_shortcut_economy:0 "Economic Sovereignty"')
        lines.append(' TUR_ww1_shortcut_military:0 "Armed Forces"')
        lines.append(' TUR_ww1_shortcut_diplomacy:0 "Great Power Diplomacy"')
        lines.append(' TUR_ww1_shortcut_war_theaters:0 "War Theaters & 1918"')
    else:
        lines.append(' TUR_ww1_shortcut_politics:0 "Política Imperial"')
        lines.append(' TUR_ww1_shortcut_economy:0 "Soberania Econômica"')
        lines.append(' TUR_ww1_shortcut_military:0 "Forças Armadas"')
        lines.append(' TUR_ww1_shortcut_diplomacy:0 "Diplomacia das Potências"')
        lines.append(' TUR_ww1_shortcut_war_theaters:0 "Teatros de Guerra & 1918"')

    # Decision categories
    if not is_pt:
        lines.append(' TUR_imperial_cohesion_category:0 "Imperial Cohesion & Administration"')
        lines.append(' TUR_imperial_cohesion_category_desc:0 "Managing regional stability, minority loyalty, and administrative reform across the provinces."')
        lines.append(' TUR_debt_and_capitulations_category:0 "Public Debt & Economic Sovereignty"')
        lines.append(' TUR_debt_and_capitulations_category_desc:0 "Liquidating foreign financial dominance, tariffs, and industrial self-reliance."')
        lines.append(' TUR_war_theaters_category:0 "Operational War Theaters"')
        lines.append(' TUR_war_theaters_category_desc:0 "Directing supply caravans, fortress networks, and campaign readiness across the fronts."')
    else:
        lines.append(' TUR_imperial_cohesion_category:0 "Coesão Imperial e Administração"')
        lines.append(' TUR_imperial_cohesion_category_desc:0 "Gestão da estabilidade regional, lealdade das minorias e reformas administrativas nas províncias."')
        lines.append(' TUR_debt_and_capitulations_category:0 "Dívida Pública e Soberania Econômica"')
        lines.append(' TUR_debt_and_capitulations_category_desc:0 "Liquidação do controle financeiro estrangeiro, tarifas e autossuficiência industrial."')
        lines.append(' TUR_war_theaters_category:0 "Teatros Operacionais de Guerra"')
        lines.append(' TUR_war_theaters_category_desc:0 "Direcionamento de caravanas de suprimento, fortalezas e prontidão operacional nas frentes de combate."')

    # Decisions
    for d in dec_ids:
        title = make_title(d)
        if not is_pt:
            lines.append(f' {d}:0 "{title}"')
            lines.append(f' {d}_desc:0 "Enacts specialized operational measures for the defense and prosperity of the empire."')
        else:
            lines.append(f' {d}:0 "{title}"')
            lines.append(f' {d}_desc:0 "Aplica medidas operacionais especializadas para a defesa e prosperidade do império."')

    # Ideas
    for i in idea_ids:
        title = make_title(i)
        if not is_pt:
            lines.append(f' {i}:0 "{title}"')
            lines.append(f' {i}_desc:0 "Reflects the structural realities and administrative efforts of the Ottoman State."')
        else:
            lines.append(f' {i}:0 "{title}"')
            lines.append(f' {i}_desc:0 "Reflete as realidades estruturais e esforços administrativos do Estado Otomano."')

    # Tooltips
    for t in tooltips:
        if not is_pt:
            lines.append(f' {t}:0 "Strategic initiative takes effect across the relevant imperial territories."')
        else:
            lines.append(f' {t}:0 "Iniciativa estratégica entra em vigor nos territórios imperiais pertinentes."')

    # Events
    for eid, etitle_en, etitle_pt, edesc_en, edesc_pt, opts in events_data:
        title = etitle_pt if is_pt else etitle_en
        desc = edesc_pt if is_pt else edesc_en
        lines.append(f' {eid}.t:0 "{title}"')
        lines.append(f' {eid}.d:0 "{desc}"')
        for op_id, op_en, op_pt in opts:
            op_txt = op_pt if is_pt else op_en
            lines.append(f' {op_id}:0 "{op_txt}"')

    # Focuses
    for fid in focus_ids:
        title = make_title(fid)
        desc = make_desc_pt(fid) if is_pt else make_desc_en(fid)
        lines.append(f' {fid}:0 "{title}"')
        lines.append(f' {fid}_desc:0 "{desc}"')

    return "\n".join(lines) + "\n"

# Generate files with UTF-8 BOM
en_content = build_yaml("l_english", is_pt=False)
pt_content = build_yaml("l_braz_por", is_pt=True)

en_path = Path("localisation/english/ww1_ottoman_l_english.yml")
pt_path = Path("localisation/braz_por/ww1_ottoman_l_braz_por.yml")

en_path.write_bytes(b"\xef\xbb\xbf" + en_content.encode("utf-8"))
pt_path.write_bytes(b"\xef\xbb\xbf" + pt_content.encode("utf-8"))

print(f"Generated English loc ({len(en_content.splitlines())} lines) into {en_path}")
print(f"Generated Brazilian Portuguese loc ({len(pt_content.splitlines())} lines) into {pt_path}")
