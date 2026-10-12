"""
Clean Rework Script for British Empire Focus Tree (ENG).
Converts all 106 separate add_ideas calls into:
1. Canonical swap_ideas for the 5 Core National Pillars.
2. Tangible, balanced material rewards (factories, dockyards, equipment, valid tech bonuses, XP).
"""
import sys
import os
import re

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MOD_ROOT)

from scripts.eng_data_politics import POLITICS_DATA
from scripts.eng_data_economy import ECONOMY_DATA
from scripts.eng_data_diplomacy import DIPLOMACY_DATA
from scripts.eng_data_military import MILITARY_DATA
from scripts.eng_data_navy_air import NAVY_AIR_DATA
from scripts.eng_data_tech_intel import TECH_INTEL_DATA

# -----------------------------------------------------------------------------
# 1. POLITICS REWARDS CLEANUP
# -----------------------------------------------------------------------------
POLITICS_REPLACEMENTS = {
    "ENG_ww1_national_insurance": """add_stability = 0.05
add_political_power = 60""",
    "ENG_ww1_the_defence_of_the_realm": """swap_ideas = {
    remove_idea = ENG_irish_home_rule_tension
    add_idea = ENG_irish_home_rule_suspended
}
add_stability = 0.05
add_war_support = 0.05""",
    "ENG_ww1_the_military_service_act": """add_manpower = 100000
add_war_support = 0.05
add_political_power = 40""",
    "ENG_ww1_reserved_civilian_occupations": """128 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.03""",
    "ENG_ww1_the_war_cabinet": """add_political_power = 100
add_war_support = 0.05
army_experience = 15
navy_experience = 15""",
    "ENG_ww1_representation_of_the_people": """swap_ideas = {
    remove_idea = ENG_irish_home_rule_suspended
    add_idea = ENG_irish_home_rule_compromise
}
add_stability = 0.08
add_political_power = 75""",
    "ENG_ww1_liberal_reconstruction": """126 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 2
        instant_build = yes
    }
}
add_stability = 0.05""",
    "ENG_ww1_the_imperial_conference": """country_event = { id = ww1_britain_pol.6 }
add_political_power = 50
set_country_flag = ENG_ww1_imperial_conference_held""",
    "ENG_ww1_dominion_procurement_offices": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 5000
    producer = ENG
}
add_political_power = 40""",
    "ENG_ww1_imperial_troop_transport": """swap_ideas = {
    remove_idea = ENG_the_imperial_web
    add_idea = ENG_the_imperial_web_t2
}
add_equipment_to_stockpile = {
    type = convoy
    amount = 100
    producer = ENG
}
add_war_support = 0.05""",
    "ENG_ww1_dominion_war_cabinet_delegates": """swap_ideas = {
    remove_idea = ENG_the_imperial_web_t2
    add_idea = ENG_the_imperial_web_t3
}
add_political_power = 75
add_stability = 0.05"""
}

# -----------------------------------------------------------------------------
# 2. ECONOMY REWARDS CLEANUP
# -----------------------------------------------------------------------------
ECONOMY_REPLACEMENTS = {
    "ENG_ww1_the_city_credit_market": """add_political_power = 75
add_stability = 0.05""",
    "ENG_ww1_railway_freight_coordination": """128 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
129 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}""",
    "ENG_ww1_domestic_coal_allocation": """131 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_political_power = 40""",
    "ENG_ww1_the_ministry_of_munitions": """swap_ideas = {
    remove_idea = ENG_city_of_london_credit
    add_idea = ENG_city_of_london_credit_t2
}
128 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}""",
    "ENG_ww1_shell_inspection_boards": """130 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 120
    producer = ENG
}""",
    "ENG_ww1_wartime_labour_dilution": """add_manpower = 60000
add_war_support = 0.05""",
    "ENG_ww1_emergency_factory_controls": """swap_ideas = {
    remove_idea = ENG_city_of_london_credit_t2
    add_idea = ENG_city_of_london_credit_t3
}
129 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}""",
    "ENG_ww1_the_ministry_of_food": """add_stability = 0.05
add_political_power = 50""",
    "ENG_ww1_housing_and_civilian_employment": """126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.05""",
    "ENG_ww1_military_demobilisation_planning": """add_manpower = 50000
add_stability = 0.05""",
    "ENG_ww1_disability_pension_administration": """add_stability = 0.08
add_political_power = 50""",
    "ENG_ww1_industrial_conversion_planning": """130 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 2
        instant_build = yes
    }
}""",
    "ENG_ww1_public_debt_repayment": """add_political_power = 75
add_stability = 0.05""",
    "ENG_ww1_the_public_health_settlement": """add_stability = 0.08
add_manpower = 40000""",
    "ENG_ww1_the_education_reconstruction_programme": """add_tech_bonus = {
    name = education_science_bonus
    bonus = 1.0
    uses = 2
    category = electronics
}
add_political_power = 50""",
    "ENG_ww1_the_industrial_relations_conference": """add_stability = 0.08
add_political_power = 50""",
    "ENG_ww1_the_nineteen_twenty_three_settlement": """add_stability = 0.10
add_political_power = 100"""
}

# -----------------------------------------------------------------------------
# 3. DIPLOMACY REWARDS CLEANUP
# -----------------------------------------------------------------------------
DIPLOMACY_REPLACEMENTS = {
    "ENG_ww1_the_french_naval_understanding": """navy_experience = 25
add_political_power = 50
FRA = {
    add_opinion_modifier = {
        target = ENG
        modifier = entente_naval_understanding
    }
}""",
    "ENG_ww1_french_staff_conversations": """army_experience = 20
add_political_power = 40""",
    "ENG_ww1_continental_commitment": """add_war_support = 0.08
add_political_power = 50""",
    "ENG_ww1_armed_neutrality": """add_stability = 0.08
add_war_support = 0.05""",
    "ENG_ww1_channel_expeditionary_coordination": """123 = {
    add_building_construction = {
        type = naval_base
        level = 1
        instant_build = yes
    }
}
navy_experience = 15""",
    "ENG_ww1_russian_procurement_liaison": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 3000
    producer = ENG
}
add_political_power = 40""",
    "ENG_ww1_neutral_shipping_assurances": """add_equipment_to_stockpile = {
    type = convoy
    amount = 50
    producer = ENG
}
add_political_power = 50""",
    "ENG_ww1_american_credit_negotiations": """add_political_power = 100
add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 200
    producer = ENG
}""",
    "ENG_ww1_balkan_allied_coordination": """add_political_power = 50
army_experience = 15""",
    "ENG_ww1_coalition_shipping_priorities": """add_equipment_to_stockpile = {
    type = convoy
    amount = 75
    producer = ENG
}
navy_experience = 15""",
    "ENG_ww1_the_supreme_war_council": """army_experience = 25
navy_experience = 20
add_political_power = 50""",
    "ENG_ww1_reconstruction_credit_negotiations": """126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_political_power = 50""",
    "ENG_ww1_the_naval_disarmament_conference": """add_stability = 0.08
add_political_power = 60""",
    "ENG_ww1_a_european_security_settlement": """add_stability = 0.10
add_political_power = 80"""
}

# -----------------------------------------------------------------------------
# 4. MILITARY REWARDS CLEANUP
# -----------------------------------------------------------------------------
MILITARY_REPLACEMENTS = {
    "ENG_ww1_the_haldane_establishment": """army_experience = 25
add_political_power = 60""",
    "ENG_ww1_officer_training_corps": """army_experience = 20
add_command_power = 30
add_manpower = 25000""",
    "ENG_ww1_army_service_corps_offices": """add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 150
    producer = ENG
}
add_tech_bonus = {
    name = motorized_bonus
    bonus = 1.0
    uses = 1
    category = motorized_equipment
}""",
    "ENG_ww1_the_expeditionary_establishment": """army_experience = 25
add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 4000
    producer = ENG
}""",
    "ENG_ww1_kitchener_new_armies": """swap_ideas = {
    remove_idea = ENG_professional_bef
    add_idea = ENG_professional_bef_t2
}
add_manpower = 150000
add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 10000
    producer = ENG
}""",
    "ENG_ww1_the_pals_battalion_system": """add_manpower = 80000
add_war_support = 0.05""",
    "ENG_ww1_field_medical_organisation": """add_tech_bonus = {
    name = medical_bonus
    bonus = 1.0
    uses = 2
    category = support_tech
}
add_manpower = 20000""",
    "ENG_ww1_machine_gun_corps_formation": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 5000
    producer = ENG
}
army_experience = 25""",
    "ENG_ww1_trench_mortar_sections": """add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 100
    producer = ENG
}
add_tech_bonus = {
    name = mortar_bonus
    bonus = 1.0
    uses = 1
    category = artillery
}""",
    "ENG_ww1_gas_protection_training": """add_tech_bonus = {
    name = support_bonus
    bonus = 1.0
    uses = 1
    category = support_tech
}
army_experience = 15""",
    "ENG_ww1_combined_arms_staff_courses": """army_experience = 30
add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}""",
    "ENG_ww1_a_smaller_professional_force": """army_experience = 25
add_stability = 0.05""",
    "ENG_ww1_territorial_defence_renewal": """add_manpower = 40000
army_experience = 15""",
    "ENG_ww1_the_channel_mobilisation_timetable": """add_equipment_to_stockpile = {
    type = convoy
    amount = 50
    producer = ENG
}
navy_experience = 15""",
    "ENG_ww1_the_bef_deployment_plan": """army_experience = 25
add_war_support = 0.05""",
    "ENG_ww1_the_flanders_supply_organisation": """123 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 100
    producer = ENG
}""",
    "ENG_ww1_holding_the_continental_line": """army_experience = 20
add_manpower = 50000""",
    "ENG_ww1_mediterranean_landing_preparation": """add_tech_bonus = {
    name = marine_bonus
    bonus = 1.0
    uses = 1
    category = marine_tech
}
navy_experience = 20""",
    "ENG_ww1_mesopotamian_supply_review": """add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 120
    producer = ENG
}
army_experience = 15""",
    "ENG_ww1_the_creeping_barrage_school": """add_tech_bonus = {
    name = artillery_doctrine
    bonus = 1.0
    uses = 1
    category = artillery
}
army_experience = 25""",
    "ENG_ww1_tank_committee_experiments": """swap_ideas = {
    remove_idea = ENG_professional_bef_t2
    add_idea = ENG_professional_bef_t3
}
add_tech_bonus = {
    name = armor_bonus
    bonus = 1.0
    uses = 2
    category = armor
}
army_experience = 30""",
    "ENG_ww1_assault_coordination_exercises": """add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 1
    category = land_doctrine
}
army_experience = 20""",
    "ENG_ww1_palestine_railway_liaison": """130 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
army_experience = 15""",
    "ENG_ww1_the_spring_defence_plan": """add_manpower = 75000
add_war_support = 0.08
army_experience = 20""",
    "ENG_ww1_the_allied_counteroffensive_plan": """army_experience = 35
add_war_support = 0.10""",
    "ENG_ww1_operational_reserve_restoration": """add_manpower = 50000
army_experience = 15""",
    "ENG_ww1_lessons_for_the_general_staff": """army_experience = 40
add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}"""
}

# -----------------------------------------------------------------------------
# 5. NAVY & AIR REWARDS CLEANUP
# -----------------------------------------------------------------------------
NAVY_AIR_REPLACEMENTS = {
    "ENG_ww1_admiralty_fleet_survey": """navy_experience = 30
add_political_power = 60""",
    "ENG_ww1_submarine_service_development": """add_tech_bonus = {
    name = sub_bonus
    bonus = 1.0
    uses = 2
    category = ss_tech
}
navy_experience = 25
126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}""",
    "ENG_ww1_naval_gunnery_calibration": """add_tech_bonus = {
    name = naval_gunnery_bonus
    bonus = 1.0
    uses = 1
    category = naval_equipment
}
navy_experience = 20""",
    "ENG_ww1_the_north_sea_watch": """navy_experience = 25
add_war_support = 0.05""",
    "ENG_ww1_grand_fleet_maintenance": """swap_ideas = {
    remove_idea = ENG_two_power_standard
    add_idea = ENG_two_power_standard_t2
}
125 = {
    add_building_construction = {
        type = naval_base
        level = 1
        instant_build = yes
    }
}
navy_experience = 25""",
    "ENG_ww1_maritime_blockade_coordination": """navy_experience = 30
add_equipment_to_stockpile = {
    type = convoy
    amount = 80
    producer = ENG
}""",
    "ENG_ww1_depth_charge_trials": """add_tech_bonus = {
    name = asw_bonus
    bonus = 1.0
    uses = 1
    category = dd_tech
}
navy_experience = 20""",
    "ENG_ww1_convoy_system_organisation": """add_equipment_to_stockpile = {
    type = convoy
    amount = 100
    producer = ENG
}
navy_experience = 25""",
    "ENG_ww1_naval_signals_and_direction_finding": """add_tech_bonus = {
    name = signals_bonus
    bonus = 1.0
    uses = 1
    category = electronics
}
navy_experience = 20""",
    "ENG_ww1_mediterranean_convoy_liaison": """add_equipment_to_stockpile = {
    type = convoy
    amount = 60
    producer = ENG
}
navy_experience = 15""",
    "ENG_ww1_naval_budget_retrenchment": """123 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}
add_political_power = 60""",
    "ENG_ww1_royal_flying_corps_organisation": """air_experience = 25
add_tech_bonus = {
    name = rfc_bonus
    bonus = 1.0
    uses = 2
    category = air_equipment
}""",
    "ENG_ww1_military_pilot_instruction": """air_experience = 20
add_command_power = 20""",
    "ENG_ww1_royal_naval_air_service_organisation": """navy_experience = 20
air_experience = 20
add_tech_bonus = {
    name = rnas_bonus
    bonus = 1.0
    uses = 2
    category = air_equipment
}""",
    "ENG_ww1_fighter_squadron_instruction": """air_experience = 25
add_tech_bonus = {
    name = fighter_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}""",
    "ENG_ww1_artillery_spotting_liaison": """air_experience = 15
army_experience = 15""",
    "ENG_ww1_aircraft_engine_reliability": """add_tech_bonus = {
    name = engine_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}
air_experience = 15""",
    "ENG_ww1_home_air_defence_coordination": """air_experience = 20
add_stability = 0.05""",
    "ENG_ww1_the_independent_air_service_debate": """air_experience = 25
add_political_power = 40""",
    "ENG_ww1_royal_air_force_unification": """air_experience = 35
add_tech_bonus = {
    name = raf_bonus
    bonus = 1.0
    uses = 2
    category = air_doctrine
}""",
    "ENG_ww1_civil_aviation_research": """add_tech_bonus = {
    name = aviation_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}
add_political_power = 40""",
    "ENG_ww1_a_sustainable_air_establishment": """air_experience = 25
add_stability = 0.05"""
}

# -----------------------------------------------------------------------------
# 6. TECH & INTEL REWARDS CLEANUP
# -----------------------------------------------------------------------------
TECH_INTEL_REPLACEMENTS = {
    "ENG_ww1_the_national_physical_laboratory": """add_tech_bonus = {
    name = npl_standards
    bonus = 1.0
    uses = 2
    category = industry
}
add_political_power = 30""",
    "ENG_ww1_university_military_contracts": """add_tech_bonus = {
    name = university_science
    bonus = 1.0
    uses = 2
    category = electronics
}
add_political_power = 40""",
    "ENG_ww1_ordnance_metallurgy_research": """add_tech_bonus = {
    name = metallurgy_bonus
    bonus = 1.0
    uses = 2
    category = artillery
}
army_experience = 15""",
    "ENG_ww1_machine_tool_standards": """add_tech_bonus = {
    name = machine_tools_bonus
    bonus = 1.0
    uses = 2
    category = industry
}""",
    "ENG_ww1_field_wireless_research": """add_tech_bonus = {
    name = wireless_bonus
    bonus = 1.0
    uses = 2
    category = electronics
}
army_experience = 15""",
    "ENG_ww1_signals_intelligence_organisation": """add_tech_bonus = {
    name = sigint_bonus
    bonus = 1.0
    uses = 2
    category = electronics
}
navy_experience = 20
army_experience = 20""",
    "ENG_ww1_the_room_forty_office": """add_tech_bonus = {
    name = room_forty_crypto
    bonus = 1.0
    uses = 2
    category = electronics
}
navy_experience = 25
add_political_power = 50""",
    "ENG_ww1_artillery_survey_mathematics": """add_tech_bonus = {
    name = artillery_math_bonus
    bonus = 1.0
    uses = 2
    category = artillery
}
army_experience = 20""",
    "ENG_ww1_chemical_protection_research": """add_tech_bonus = {
    name = chemical_protection
    bonus = 1.0
    uses = 1
    category = support_tech
}
army_experience = 15""",
    "ENG_ww1_the_landships_technical_committee": """add_tech_bonus = {
    name = tank_bonus
    bonus = 1.0
    uses = 2
    category = armor
}
army_experience = 25
130 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}""",
    "ENG_ww1_hydrophone_analysis_laboratory": """swap_ideas = {
    remove_idea = ENG_two_power_standard_t2
    add_idea = ENG_two_power_standard_t3
}
add_tech_bonus = {
    name = asdic_bonus
    bonus = 1.0
    uses = 2
    category = dd_tech
}
navy_experience = 30""",
    "ENG_ww1_production_quality_standards": """add_tech_bonus = {
    name = quality_standards
    bonus = 1.0
    uses = 2
    category = industry
}
128 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}""",
    "ENG_ww1_the_postwar_research_council": """add_tech_bonus = {
    name = postwar_science
    bonus = 1.0
    uses = 2
    category = electronics
}
add_political_power = 50""",
    "ENG_ww1_industrial_patent_exchanges": """add_tech_bonus = {
    name = patent_industry
    bonus = 1.0
    uses = 2
    category = industry
}
add_political_power = 40""",
    "ENG_ww1_technical_education_for_reconstruction": """add_tech_bonus = {
    name = technical_edu
    bonus = 1.0
    uses = 2
    category = electronics
}
add_stability = 0.05"""
}

# Combine all clean replacements
ALL_REPLACEMENTS = {}
ALL_REPLACEMENTS.update(POLITICS_REPLACEMENTS)
ALL_REPLACEMENTS.update(ECONOMY_REPLACEMENTS)
ALL_REPLACEMENTS.update(DIPLOMACY_REPLACEMENTS)
ALL_REPLACEMENTS.update(MILITARY_REPLACEMENTS)
ALL_REPLACEMENTS.update(NAVY_AIR_REPLACEMENTS)
ALL_REPLACEMENTS.update(TECH_INTEL_REPLACEMENTS)

print(f"Total targeted focus reward replacements: {len(ALL_REPLACEMENTS)}")

# Now apply to scripts/eng_data_*.py
def update_data_file(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified_count = 0
    for fid, new_rew in replacements.items():
        # Find entry for fid in file
        pattern = rf'("{re.escape(fid)}":\s*\{{.*?reward":\s*""")(.*?)(""".*?\}})'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            content = content[:m.start(2)] + new_rew + content[m.end(2):]
            modified_count += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {modified_count} rewards in {filepath}")

update_data_file("scripts/eng_data_politics.py", POLITICS_REPLACEMENTS)
update_data_file("scripts/eng_data_economy.py", ECONOMY_REPLACEMENTS)
update_data_file("scripts/eng_data_diplomacy.py", DIPLOMACY_REPLACEMENTS)
update_data_file("scripts/eng_data_military.py", MILITARY_REPLACEMENTS)
update_data_file("scripts/eng_data_navy_air.py", NAVY_AIR_REPLACEMENTS)
update_data_file("scripts/eng_data_tech_intel.py", TECH_INTEL_REPLACEMENTS)

print("All eng_data_*.py files updated successfully!")
