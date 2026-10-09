#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master generator for Kingdom of Serbia (SER) WW1 National Focus Tree (1911-1918).
Generates exactly 94 substantive focuses across 5 non-colliding visual wings:
- Sector 1: Economy, Infrastructure & Kragujevac (12 focuses, x=1..5, y=0..5)
- Sector 2: Royal Army & General Staff (16 focuses, x=8..14, y=0..6)
- Sector 3: Internal Politics & The Black Hand (20 focuses, x=16..22, y=0..8)
- Sector 4: Balkan Diplomacy & South Slav Question (20 focuses, x=24..30, y=0..6)
- Sector 5: 1914 Crisis, War, Exile & Liberation (26 focuses, x=33..41, y=0..11)
Total = 94 focuses.
"""

from pathlib import Path

FOCI = []

def add_f(fid, x, y, cost, icon=None, prereqs=None, mut_excl=None, available=None, bypass=None, rewards=None, filters=None):
    if icon is None:
        icon = f"GFX_{fid}"
    FOCI.append({
        'id': fid,
        'x': x,
        'y': y,
        'cost': cost,
        'icon': icon,
        'prereqs': prereqs or [],
        'mut_excl': mut_excl or [],
        'available': available,
        'bypass': bypass,
        'rewards': rewards or [],
        'filters': filters or ['FOCUS_FILTER_POLITICAL']
    })

# ==============================================================================
# SECTOR 1: ECONOMY, INFRASTRUCTURE & KRAGUJEVAC (12 FOCUSES | x: 1 to 5)
# ==============================================================================

# Root (y=0)
add_f("SER_agrarian_kingdom_finances", 3, 0, 5,
      rewards=["add_political_power = 60", "add_stability = 0.05", "add_to_variable = { ser_national_cohesion = 5 }", "set_country_flag = SER_agrarian_finances_settled"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Rural branches (x=1)
add_f("SER_zadruga_cooperative_network", 1, 1, 5,
      prereqs=["SER_agrarian_kingdom_finances"],
      rewards=["add_stability = 0.05", "add_political_power = 40", "add_to_variable = { ser_national_cohesion = 5 }", "107 = { add_extra_state_shared_building_slots = 1 }"],
      filters=["FOCUS_FILTER_INDUSTRY", "FOCUS_FILTER_STABILITY"])

add_f("SER_expand_livestock_and_grain_trade", 1, 2, 5,
      prereqs=["SER_zadruga_cooperative_network"],
      rewards=["add_political_power = 50", "add_to_variable = { ser_national_cohesion = 5 }", "108 = { add_extra_state_shared_building_slots = 1 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Railroad artery (x=3)
add_f("SER_belgrade_nis_rail_artery", 3, 1, 5,
      prereqs=["SER_agrarian_kingdom_finances"],
      rewards=["107 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
               "108 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
               "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_morava_valley_logistics", 3, 2, 5,
      prereqs=["SER_belgrade_nis_rail_artery"],
      rewards=["107 = { add_building_construction = { type = supply_node province = 11586 instant_build = yes } }",
               "add_command_power = 15", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Mining & Resources (x=5)
add_f("SER_bor_copper_and_rudnik_mines", 5, 1, 5,
      prereqs=["SER_agrarian_kingdom_finances"],
      rewards=["108 = { add_resource = { type = steel amount = 4 } }", "add_political_power = 30"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_modernize_trepca_prospects", 5, 2, 5,
      prereqs=["SER_bor_copper_and_rudnik_mines"],
      rewards=["108 = { add_resource = { type = tungsten amount = 3 } }", "add_stability = 0.03"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Industrial consolidation at Kragujevac
add_f("SER_kragujevac_military_workshops", 2, 3, 6,
      prereqs=["SER_expand_livestock_and_grain_trade", "SER_morava_valley_logistics"],
      rewards=["107 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
               "107 = { add_extra_state_shared_building_slots = 1 }",
               "add_to_variable = { ser_army_readiness = 5 }",
               "if = { limit = { has_idea = SER_underdeveloped_agrarian_economy } remove_ideas = SER_underdeveloped_agrarian_economy add_ideas = SER_kragujevac_arsenal_expansion }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_domestic_ammunition_lines", 1, 4, 6,
      prereqs=["SER_kragujevac_military_workshops"],
      rewards=["107 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
               "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2500 producer = SER }",
               "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_creusot_schneider_contracts", 3, 4, 6,
      prereqs=["SER_kragujevac_military_workshops"],
      rewards=["add_tech_bonus = { name = artillery_bonus bonus = 1.0 uses = 1 category = artillery }",
               "add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 60 producer = SER }",
               "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_national_bank_monetary_stability", 5, 3, 5,
      prereqs=["SER_modernize_trepca_prospects"],
      rewards=["add_political_power = 80", "add_stability = 0.05", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_diversified_national_industry", 2, 5, 7,
      prereqs=["SER_domestic_ammunition_lines", "SER_creusot_schneider_contracts", "SER_national_bank_monetary_stability"],
      rewards=["107 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
               "108 = { add_extra_state_shared_building_slots = 1 }",
               "add_to_variable = { ser_national_cohesion = 10 }",
               "if = { limit = { has_idea = SER_kragujevac_arsenal_expansion } remove_ideas = SER_kragujevac_arsenal_expansion add_ideas = SER_diversified_national_industry }"],
      filters=["FOCUS_FILTER_INDUSTRY"])


# ==============================================================================
# SECTOR 2: ROYAL ARMY & GENERAL STAFF (16 FOCUSES | x: 8 to 14)
# ==============================================================================

# General Staff Root (y=0)
add_f("SER_radomir_putnik_doctrine", 11, 0, 5,
      rewards=["army_experience = 25", "add_command_power = 20", "add_to_variable = { ser_army_readiness = 10 }", "set_country_flag = SER_putnik_doctrine_established"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Conscription & Mobilization (x=9)
add_f("SER_three_ban_conscription_system", 9, 1, 5,
      prereqs=["SER_radomir_putnik_doctrine"],
      rewards=["add_manpower = 25000", "add_war_support = 0.05", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("SER_mobilization_timetables", 9, 2, 5,
      prereqs=["SER_three_ban_conscription_system"],
      rewards=["add_command_power = 20", "army_experience = 10", "add_to_variable = { ser_army_readiness = 5 }",
               "add_tech_bonus = { name = land_doc bonus = 1.0 uses = 1 category = land_doctrine }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_peacetime_infantry_cadre", 9, 3, 5,
      prereqs=["SER_mobilization_timetables"],
      rewards=["107 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
               "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 4000 producer = SER }",
               "army_experience = 15", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_MANPOWER", "FOCUS_FILTER_INDUSTRY"])

# Artillery & Firepower (x=13)
add_f("SER_artillery_park_reorganization", 13, 1, 5,
      prereqs=["SER_radomir_putnik_doctrine"],
      rewards=["army_experience = 20", "add_to_variable = { ser_army_readiness = 5 }",
               "add_tech_bonus = { name = artillery_bonus bonus = 1.0 uses = 1 category = artillery }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_rapid_fire_field_guns", 13, 2, 5,
      prereqs=["SER_artillery_park_reorganization"],
      rewards=["add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 40 producer = SER }",
               "army_experience = 10", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Fortification & Topography (x=11)
add_f("SER_drina_defensive_survey", 11, 2, 5,
      prereqs=["SER_radomir_putnik_doctrine"],
      rewards=["107 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = 3609 } }",
               "107 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = 11586 } }",
               "add_command_power = 10", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_DEFENSE"])

add_f("SER_danubian_flotilla_watch", 11, 3, 4,
      prereqs=["SER_drina_defensive_survey"],
      rewards=["107 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = 11586 } }",
               "add_stability = 0.03", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_DEFENSE"])

# Specialized Infantry (x=8, 10, 12, 14)
add_f("SER_mountain_warfare_detachments", 8, 4, 5,
      prereqs=["SER_peacetime_infantry_cadre"],
      rewards=["add_tech_bonus = { name = special_forces_bonus bonus = 1.0 uses = 1 category = mountaineers }",
               "army_experience = 15", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_entrenchment_and_counterstroke", 10, 4, 5,
      prereqs=["SER_peacetime_infantry_cadre", "SER_danubian_flotilla_watch"],
      rewards=["army_experience = 20", "add_to_variable = { ser_army_readiness = 5 }",
               "add_tech_bonus = { name = land_doc bonus = 1.0 uses = 1 category = land_doctrine }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_officer_corps_meritocracy", 12, 4, 5,
      prereqs=["SER_rapid_fire_field_guns", "SER_danubian_flotilla_watch"],
      rewards=["add_command_power = 25", "army_experience = 15", "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("SER_military_telegraph_corps", 14, 4, 4,
      prereqs=["SER_rapid_fire_field_guns"],
      rewards=["add_tech_bonus = { name = radio_bonus bonus = 1.0 uses = 1 category = electronics }",
               "add_political_power = 30", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

# Medical & Veteran Staff (y=5)
add_f("SER_field_medical_directorate", 9, 5, 5,
      prereqs=["SER_mountain_warfare_detachments", "SER_entrenchment_and_counterstroke"],
      rewards=["add_tech_bonus = { name = hospital_bonus bonus = 1.0 uses = 1 category = support_tech }",
               "add_stability = 0.03", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("SER_foreign_medical_missions", 11, 5, 5,
      prereqs=["SER_entrenchment_and_counterstroke", "SER_officer_corps_meritocracy"],
      rewards=["add_stability = 0.05", "add_political_power = 40", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_veteran_serbian_soldier", 13, 5, 6,
      prereqs=["SER_officer_corps_meritocracy", "SER_military_telegraph_corps"],
      rewards=["army_experience = 25", "add_war_support = 0.05", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Supreme Command (y=6)
add_f("SER_supreme_command_preparedness", 11, 6, 5,
      prereqs=["SER_field_medical_directorate", "SER_foreign_medical_missions", "SER_veteran_serbian_soldier"],
      rewards=["add_command_power = 30", "army_experience = 30", "add_war_support = 0.05", "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])


# ==============================================================================
# SECTOR 3: INTERNAL POLITICS & THE BLACK HAND (20 FOCUSES | x: 16 to 22)
# ==============================================================================

# Peter I Reign Root (y=0)
add_f("SER_reign_of_peter_i", 19, 0, 5,
      rewards=["country_event = { id = ww1_serbia.1 }", "add_political_power = 80", "add_stability = 0.05",
               "add_to_variable = { ser_civil_military_balance = 5 }", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

# Constitutional & Radical Party path (x=16..17)
add_f("SER_radical_party_cabinet", 17, 1, 5,
      prereqs=["SER_reign_of_peter_i"],
      rewards=["add_political_power = 100", "add_popularity = { ideology = democratic popularity = 0.10 }",
               "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_independent_radicals_dialogue", 16, 2, 5,
      prereqs=["SER_radical_party_cabinet"],
      rewards=["add_stability = 0.05", "add_political_power = 50", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_strengthen_narodna_skupstina", 17, 3, 5,
      prereqs=["SER_independent_radicals_dialogue"],
      rewards=["add_political_power = 75", "add_stability = 0.05", "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_constitutional_liberties_bill", 17, 4, 5,
      prereqs=["SER_strengthen_narodna_skupstina"],
      rewards=["add_stability = 0.08", "add_political_power = 60", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

# Crown Prince Regency & Conspiracies (x=18..19)
add_f("SER_crown_prince_regency_prep", 19, 1, 5,
      prereqs=["SER_reign_of_peter_i"],
      rewards=["add_political_power = 60", "add_command_power = 15", "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_investigate_officer_conspiracies", 19, 2, 5,
      prereqs=["SER_crown_prince_regency_prep"],
      rewards=["country_event = { id = ww1_serbia.2 }", "add_political_power = 50", "add_stability = -0.03",
               "add_to_variable = { ser_civil_military_balance = -5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# The Black Hand & Military Nationalist Network (x=21..22)
add_f("SER_the_shadow_of_apis", 21, 1, 5,
      prereqs=["SER_reign_of_peter_i"],
      rewards=["country_event = { id = ww1_serbia.2 }", "add_war_support = 0.08", "add_command_power = 20",
               "add_to_variable = { ser_civil_military_balance = -10 }", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_narodna_odbrana_patronage", 21, 2, 5,
      prereqs=["SER_the_shadow_of_apis"],
      rewards=["add_war_support = 0.05", "add_manpower = 10000", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("SER_military_intelligence_network", 22, 3, 5,
      prereqs=["SER_the_shadow_of_apis"],
      rewards=["add_command_power = 25", "army_experience = 15", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Civil vs Military Climax (y=5)
add_f("SER_civilian_supremacy_charter", 17, 5, 6,
      prereqs=["SER_constitutional_liberties_bill", "SER_investigate_officer_conspiracies"],
      mut_excl=["SER_officer_corps_ascendancy"],
      rewards=["remove_ideas = SER_civil_military_rivalry",
               "add_ideas = SER_civilian_supremacy_established",
               "add_political_power = 120", "add_stability = 0.10",
               "add_to_variable = { ser_civil_military_balance = 25 }", "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

add_f("SER_curb_secret_societies", 17, 6, 5,
      prereqs=["SER_civilian_supremacy_charter"],
      rewards=["add_stability = 0.08", "add_command_power = -15", "add_political_power = 60",
               "add_to_variable = { ser_civil_military_balance = 10 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_officer_corps_ascendancy", 21, 5, 6,
      prereqs=["SER_narodna_odbrana_patronage", "SER_military_intelligence_network"],
      mut_excl=["SER_civilian_supremacy_charter"],
      rewards=["remove_ideas = SER_civil_military_rivalry",
               "add_ideas = SER_military_officer_ascendancy",
               "add_war_support = 0.15", "army_experience = 25",
               "add_to_variable = { ser_civil_military_balance = -25 }", "add_to_variable = { ser_army_readiness = 15 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_clandestine_national_action", 21, 6, 5,
      prereqs=["SER_officer_corps_ascendancy"],
      rewards=["add_command_power = 30", "add_war_support = 0.05", "add_manpower = 15000",
               "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Monarchic Arbitration (x=19)
add_f("SER_monarchic_arbiter", 19, 4, 5,
      prereqs=["SER_investigate_officer_conspiracies"],
      rewards=["add_stability = 0.05", "add_political_power = 50", "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_patriotic_press_censorship", 19, 5, 4,
      prereqs=["SER_monarchic_arbiter"],
      rewards=["add_war_support = 0.05", "add_stability = 0.03", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_anticorruption_procurement", 16, 6, 5,
      prereqs=["SER_civilian_supremacy_charter"],
      rewards=["add_political_power = 60", "add_stability = 0.05", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_professional_civil_service", 16, 7, 5,
      prereqs=["SER_anticorruption_procurement"],
      rewards=["add_political_power = 80", "add_stability = 0.05", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Sacred National Union (y=7, 8)
add_f("SER_national_unity_covenant", 19, 7, 6,
      prereqs=["SER_curb_secret_societies", "SER_patriotic_press_censorship"],
      rewards=["add_stability = 0.10", "add_war_support = 0.10", "add_political_power = 80",
               "add_to_variable = { ser_national_cohesion = 15 }"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_regency_of_alexander", 19, 8, 5,
      prereqs=["SER_national_unity_covenant"],
      available="date > 1914.6.1",
      rewards=["country_event = { id = ww1_serbia.6 }",
               "add_political_power = 100", "add_command_power = 25",
               "add_to_variable = { ser_civil_military_balance = 10 }"],
      filters=["FOCUS_FILTER_POLITICAL"])


# ==============================================================================
# SECTOR 4: BALKAN DIPLOMACY & SOUTH SLAV QUESTION (20 FOCUSES | x: 24 to 30)
# ==============================================================================

# Diplomatic Root (y=0)
add_f("SER_balkan_diplomatic_initiatives", 27, 0, 5,
      rewards=["add_political_power = 80", "add_to_variable = { ser_balkan_influence = 10 }", "set_country_flag = SER_balkan_diplomacy_opened"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Serbo-Bulgarian & Macedonia dialogue (x=24..25)
add_f("SER_serbo_bulgarian_dialogue", 25, 1, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["country_event = { id = ww1_serbia.4 }", "add_opinion_modifier = { target = BUL modifier = positive_50 }",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_macedonian_autonomy_proposal", 25, 2, 5,
      prereqs=["SER_serbo_bulgarian_dialogue"],
      rewards=["add_political_power = 50", "BUL = { add_opinion_modifier = { target = SER modifier = positive_25 } }",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_bulgarian_non_aggression_pact", 25, 3, 6,
      prereqs=["SER_macedonian_autonomy_proposal"],
      rewards=["give_guarantee = BUL", "BUL = { give_guarantee = SER }", "add_political_power = 60",
               "add_to_variable = { ser_balkan_influence = 10 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Montenegro Dynastic Accord (x=26)
add_f("SER_montenegrin_dynastic_ties", 26, 1, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["country_event = { id = ww1_serbia.5 }", "add_stability = 0.05", "add_political_power = 50",
               "add_to_variable = { ser_balkan_influence = 5 }", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_cetinje_military_convention", 26, 2, 5,
      prereqs=["SER_montenegrin_dynastic_ties"],
      rewards=["add_command_power = 20", "army_experience = 15", "add_manpower = 10000",
               "add_to_variable = { ser_balkan_influence = 5 }", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_MANPOWER"])

# Greece & Romania (x=28)
add_f("SER_greek_commercial_transit", 28, 1, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["add_opinion_modifier = { target = GRE modifier = positive_50 }", "add_political_power = 50",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_romanian_danube_understanding", 28, 2, 5,
      prereqs=["SER_greek_commercial_transit"],
      rewards=["add_opinion_modifier = { target = ROM modifier = positive_50 }", "add_stability = 0.05",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Sublime Porte Normalization (x=30)
add_f("SER_sublime_porte_normalization", 30, 1, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["add_opinion_modifier = { target = TUR modifier = positive_25 }", "add_political_power = 60",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Balkan Accord (y=4)
add_f("SER_balkan_equilibrium_accord", 26, 4, 6,
      prereqs=["SER_bulgarian_non_aggression_pact", "SER_cetinje_military_convention", "SER_romanian_danube_understanding"],
      rewards=["add_political_power = 100", "add_stability = 0.08",
               "add_to_variable = { ser_balkan_influence = 15 }", "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_STABILITY"])

# Russian & French Patronage (x=24..25, y=4..6)
add_f("SER_traditional_russian_patronage", 24, 4, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["add_opinion_modifier = { target = RUS modifier = positive_100 }", "add_political_power = 60",
               "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_saint_petersburg_arms_loans", 24, 5, 5,
      prereqs=["SER_traditional_russian_patronage"],
      rewards=["add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 5000 producer = RUS }",
               "add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 40 producer = RUS }",
               "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_banque_franco_serbe_credits", 25, 5, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["country_event = { id = ww1_serbia.3 }",
               "if = { limit = { has_idea = SER_underdeveloped_agrarian_economy } remove_ideas = SER_underdeveloped_agrarian_economy }",
               "add_ideas = SER_french_serbian_trade_accord", "add_political_power = 80",
               "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_entente_diplomatic_shield", 24, 6, 6,
      prereqs=["SER_saint_petersburg_arms_loans", "SER_banque_franco_serbe_credits"],
      rewards=["RUS = { give_guarantee = SER }", "FRA = { give_guarantee = SER }", "add_war_support = 0.10",
               "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Austrian Détente Alternative (x=29..30, y=4..6)
add_f("SER_austrian_border_accommodation", 29, 4, 5,
      prereqs=["SER_balkan_diplomatic_initiatives"],
      rewards=["add_opinion_modifier = { target = AUS modifier = positive_50 }", "add_political_power = 60",
               "add_to_variable = { ser_balkan_influence = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_serbo_austrian_trade_treaty", 30, 5, 6,
      prereqs=["SER_austrian_border_accommodation"],
      rewards=["if = { limit = { has_idea = SER_underdeveloped_agrarian_economy } remove_ideas = SER_underdeveloped_agrarian_economy }",
               "add_ideas = SER_serbo_austrian_economic_pact", "add_political_power = 80", "add_stability = 0.05",
               "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_suppress_anti_habsburg_agitation", 29, 6, 5,
      prereqs=["SER_serbo_austrian_trade_treaty"],
      rewards=["add_opinion_modifier = { target = AUS modifier = positive_75 }", "add_stability = 0.05", "add_war_support = -0.05",
               "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

# South Slav Cultural & Strategy (x=27..28, y=5..6)
add_f("SER_south_slav_cultural_links", 27, 5, 5,
      prereqs=["SER_balkan_equilibrium_accord"],
      rewards=["add_political_power = 75", "add_stability = 0.05",
               "add_to_variable = { ser_balkan_influence = 5 }", "add_to_variable = { ser_national_cohesion = 5 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_greater_serbian_strategy", 27, 6, 6,
      prereqs=["SER_south_slav_cultural_links"],
      mut_excl=["SER_yugoslav_federal_ideal"],
      rewards=["if = { limit = { has_idea = SER_balkan_defiance } remove_ideas = SER_balkan_defiance }",
               "add_ideas = SER_greater_serbia_ideal", "add_war_support = 0.15",
               "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_yugoslav_federal_ideal", 28, 6, 6,
      prereqs=["SER_south_slav_cultural_links"],
      mut_excl=["SER_greater_serbian_strategy"],
      rewards=["if = { limit = { has_idea = SER_balkan_defiance } remove_ideas = SER_balkan_defiance }",
               "add_ideas = SER_yugoslav_brotherhood_charter", "add_stability = 0.10",
               "add_to_variable = { ser_balkan_influence = 15 }"],
      filters=["FOCUS_FILTER_STABILITY"])


# ==============================================================================
# SECTOR 5: 1914 CRISIS, WAR, EXILE & LIBERATION (26 FOCUSES | x: 33 to 41)
# ==============================================================================

# Sub-branch 5.1: July Crisis 1914 & Mobilization (8 Focuses | x=34..37, y=0..4)
add_f("SER_sarajevo_aftermath_crisis", 36, 0, 3,
      available="OR = { date > 1914.6.28 has_global_flag = ww1_sarajevo_assassination has_war = yes }",
      rewards=["country_event = { id = ww1_serbia.7 }", "add_political_power = 50", "add_war_support = 0.10",
               "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_internal_inquiry_on_conspirators", 34, 1, 3,
      prereqs=["SER_sarajevo_aftermath_crisis"],
      rewards=["add_stability = 0.05", "add_political_power = 40", "add_to_variable = { ser_civil_military_balance = 5 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_face_austrian_ultimatum", 36, 1, 4,
      prereqs=["SER_sarajevo_aftermath_crisis"],
      rewards=["country_event = { id = ww1_serbia.8 }", "add_political_power = 60", "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_appeal_to_tsar_nicholas", 35, 2, 3,
      prereqs=["SER_face_austrian_ultimatum"],
      rewards=["RUS = { country_event = { id = ww1_russia.12 } }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_general_mobilization_order", 37, 2, 4,
      prereqs=["SER_face_austrian_ultimatum"],
      rewards=["country_event = { id = ww1_serbia.9 }", "add_manpower = 45000", "add_war_support = 0.15",
               "add_to_variable = { ser_army_readiness = 20 }"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("SER_defend_belgrade_perimeter", 35, 3, 4,
      prereqs=["SER_appeal_to_tsar_nicholas", "SER_general_mobilization_order"],
      rewards=["107 = { add_building_construction = { type = bunker level = 2 instant_build = yes province = 11586 } }",
               "add_command_power = 20", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_DEFENSE"])

add_f("SER_drina_valley_ambush_lines", 37, 3, 4,
      prereqs=["SER_general_mobilization_order"],
      rewards=["107 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = 3609 } }",
               "army_experience = 20", "add_to_variable = { ser_army_readiness = 5 }"],
      filters=["FOCUS_FILTER_DEFENSE"])

add_f("SER_total_defensive_war", 36, 4, 5,
      prereqs=["SER_defend_belgrade_perimeter", "SER_drina_valley_ambush_lines"],
      available="has_war = yes",
      rewards=["add_war_support = 0.15", "add_stability = 0.10", "add_command_power = 30",
               "add_to_variable = { ser_army_readiness = 15 }", "add_to_variable = { ser_national_cohesion = 15 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Sub-branch 5.2: Decisive Battles of 1914 (3 Focuses | x=35..37, y=5..6)
add_f("SER_battle_of_cer_heroism", 35, 5, 3,
      prereqs=["SER_total_defensive_war"],
      rewards=["add_timed_idea = { idea = SER_cer_counterstroke_glory days = 28 }",
               "army_experience = 25", "add_war_support = 0.10", "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("SER_misic_kolubara_counteroffensive", 37, 5, 4,
      prereqs=["SER_total_defensive_war"],
      rewards=["country_event = { id = ww1_serbia.10 }",
               "add_timed_idea = { idea = SER_kolubara_maneuver_mastery days = 21 }",
               "army_experience = 30", "add_command_power = 25", "add_to_variable = { ser_army_readiness = 15 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("SER_typhus_epidemic_containment", 36, 6, 4,
      prereqs=["SER_battle_of_cer_heroism", "SER_misic_kolubara_counteroffensive"],
      rewards=["add_timed_idea = { idea = SER_typhus_epidemic_crisis days = 180 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

# Sub-branch 5.3: The Great Albanian Retreat (3 Focuses | x=33, y=7..9)
add_f("SER_the_albanian_golgotha", 33, 7, 4,
      prereqs=["SER_typhus_epidemic_containment"],
      available="OR = { NOT = { controls_state = 107 } surrender_progress > 0.30 }",
      rewards=["country_event = { id = ww1_serbia.11 }", "add_war_support = 0.15", "add_command_power = 25",
               "add_to_variable = { ser_national_cohesion = 15 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("SER_evacuation_of_military_cadres", 33, 8, 4,
      prereqs=["SER_the_albanian_golgotha"],
      rewards=["add_manpower = 20000", "army_experience = 20", "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("SER_montenegrin_rearguard_stand", 33, 9, 3,
      prereqs=["SER_evacuation_of_military_cadres"],
      rewards=["add_timed_idea = { idea = SER_cer_counterstroke_glory days = 21 }",
               "add_war_support = 0.10", "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Sub-branch 5.4: Government in Exile at Corfu & Salonika Front (6 Focuses | x=35..37, y=7..11)
add_f("SER_government_in_exile_corfu", 36, 7, 4,
      prereqs=["SER_typhus_epidemic_containment"],
      available="OR = { NOT = { controls_state = 107 } has_war = yes }",
      rewards=["country_event = { id = ww1_serbia.12 }", "add_political_power = 100", "add_stability = 0.10",
               "add_to_variable = { ser_national_cohesion = 10 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_rebuild_army_in_salonika", 36, 8, 6,
      prereqs=["SER_government_in_exile_corfu"],
      rewards=["if = { limit = { has_idea = SER_balkan_defiance } remove_ideas = SER_balkan_defiance }",
               "add_ideas = SER_rebuilt_salonika_corps",
               "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 8000 producer = FRA }",
               "army_experience = 30", "add_to_variable = { ser_army_readiness = 20 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("SER_french_chauchats_and_75mm", 35, 9, 5,
      prereqs=["SER_rebuild_army_in_salonika"],
      rewards=["add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 60 producer = FRA }",
               "add_tech_bonus = { name = infantry_weapons bonus = 1.0 uses = 1 category = infantry_weapons }",
               "add_to_variable = { ser_army_readiness = 10 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("SER_salonika_trial_of_apis", 37, 9, 5,
      prereqs=["SER_rebuild_army_in_salonika"],
      available="date > 1917.1.1",
      rewards=["country_event = { id = ww1_serbia.13 }",
               "add_stability = 0.12", "add_political_power = 80",
               "add_to_variable = { ser_civil_military_balance = 20 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_corfu_declaration_accord", 36, 10, 5,
      prereqs=["SER_french_chauchats_and_75mm", "SER_salonika_trial_of_apis"],
      available="date > 1917.1.1",
      rewards=["country_event = { id = ww1_serbia.14 }", "add_political_power = 120", "add_stability = 0.10",
               "add_to_variable = { ser_national_cohesion = 15 }", "add_to_variable = { ser_balkan_influence = 15 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_allied_balkan_coordination", 36, 11, 4,
      prereqs=["SER_corfu_declaration_accord"],
      rewards=["army_experience = 25", "add_command_power = 25", "add_war_support = 0.10",
               "add_to_variable = { ser_army_readiness = 15 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Sub-branch 5.5: 1918 Breakthrough & Liberation (6 Focuses | x=38..41, y=7..11)
add_f("SER_breakthrough_at_dobro_pole", 39, 7, 4,
      prereqs=["SER_typhus_epidemic_containment"],
      available="AND = { date > 1918.6.1 has_war = yes }",
      rewards=["country_event = { id = ww1_serbia.15 }",
               "add_timed_idea = { idea = SER_dobro_pole_breakthrough days = 30 }",
               "army_experience = 35", "add_command_power = 30", "add_to_variable = { ser_army_readiness = 20 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("SER_liberation_of_the_homeland", 39, 8, 4,
      prereqs=["SER_breakthrough_at_dobro_pole"],
      available="controls_state = 107",
      rewards=["add_stability = 0.20", "add_war_support = 0.15", "add_political_power = 100",
               "add_to_variable = { ser_national_cohesion = 20 }", "add_to_variable = { ser_army_readiness = 15 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_armistice_on_the_danube", 39, 9, 3,
      prereqs=["SER_liberation_of_the_homeland"],
      rewards=["add_political_power = 120", "add_stability = 0.15",
               "add_to_variable = { ser_national_cohesion = 15 }", "add_to_variable = { ser_balkan_influence = 20 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("SER_podgorica_assembly_unification", 38, 10, 4,
      prereqs=["SER_armistice_on_the_danube"],
      rewards=["add_stability = 0.10", "add_manpower = 15000", "add_political_power = 80",
               "add_to_variable = { ser_national_cohesion = 15 }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("SER_proclamation_of_yugoslavia", 39, 11, 5,
      prereqs=["SER_armistice_on_the_danube", "SER_podgorica_assembly_unification"],
      mut_excl=["SER_restored_sovereign_serbia"],
      rewards=["country_event = { id = ww1_serbia.16 }",
               "set_cosmetic_tag = YUG", "add_stability = 0.15", "add_political_power = 150",
               "add_to_variable = { ser_national_cohesion = 25 }", "add_to_variable = { ser_balkan_influence = 30 }"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

add_f("SER_restored_sovereign_serbia", 41, 11, 5,
      prereqs=["SER_armistice_on_the_danube"],
      mut_excl=["SER_proclamation_of_yugoslavia"],
      rewards=["add_stability = 0.15", "add_war_support = 0.15", "add_political_power = 150",
               "107 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
               "add_to_variable = { ser_national_cohesion = 25 }"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_INDUSTRY"])

# ==============================================================================
# COMPILER & FILE WRITER
# ==============================================================================

def generate_focus_tree_code():
    print(f"Total Serbian focuses defined: {len(FOCI)}")
    assert len(FOCI) == 94, f"Expected exactly 94 focuses, got {len(FOCI)}"

    # Check for coordinate collisions and dy >= 1
    coords = {}
    foci_by_id = {f['id']: f for f in FOCI}

    for f in FOCI:
        c = (f['x'], f['y'])
        if c in coords:
            raise ValueError(f"Coordinate collision at {c}: {f['id']} and {coords[c]}")
        coords[c] = f['id']

        for p in f['prereqs']:
            if p not in foci_by_id:
                raise ValueError(f"Prerequisite '{p}' not found for focus '{f['id']}'")
            parent = foci_by_id[p]
            if f['y'] <= parent['y']:
                raise ValueError(f"dy <= 0 violation: child {f['id']} (y={f['y']}) <= parent {p} (y={parent['y']})")

    out = []
    out.append("focus_tree = {")
    out.append("\tid = serbian_focus")
    out.append("\tcountry = {")
    out.append("\t\tfactor = 0")
    out.append("\t\tmodifier = {")
    out.append("\t\t\tadd = 10")
    out.append("\t\t\ttag = SER")
    out.append("\t\t}")
    out.append("\t}")
    out.append("\tdefault = no")
    out.append("")

    for f in FOCI:
        out.append("\tfocus = {")
        out.append(f"\t\tid = {f['id']}")
        out.append(f"\t\ticon = {f['icon']}")
        out.append(f"\t\tx = {f['x']}")
        out.append(f"\t\ty = {f['y']}")
        out.append(f"\t\tcost = {f['cost']}")
        out.append("")

        if f['prereqs']:
            for p in f['prereqs']:
                out.append(f"\t\tprerequisite = {{ focus = {p} }}")
        
        if f['mut_excl']:
            for m in f['mut_excl']:
                out.append(f"\t\tmutually_exclusive = {{ focus = {m} }}")

        if f['available']:
            out.append(f"\t\tavailable = {{ {f['available']} }}")

        if f['bypass']:
            out.append(f"\t\tbypass = {{ {f['bypass']} }}")

        if f['filters']:
            filters_str = " ".join(f['filters'])
            out.append(f"\t\tsearch_filters = {{ {filters_str} }}")

        out.append("\t\tcompletion_reward = {")
        for r in f['rewards']:
            out.append(f"\t\t\t{r}")
        out.append("\t\t}")
        out.append("\t}")
        out.append("")

    out.append("}")
    out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    tree_code = generate_focus_tree_code()
    out_file = Path(__file__).resolve().parent.parent / "common" / "national_focus" / "serbia.txt"
    out_file.write_text(tree_code, encoding="utf-8")
    print(f"Successfully generated {out_file} with {len(FOCI)} focuses!")
