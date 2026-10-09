#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Rework Engine for Ottoman Empire (TUR) WW1 National Focus Tree.
Reconstructs scripts/generate_full_ottoman_tree.py with high-substance rewards,
Clausewitz syntax compliance, variable integration, event hooks, and factory placement.
ENFORCES STRICT ANTI-STACKING & CLEAN SPIRIT UPGRADES:
- No idea is duplicated across multiple focuses.
- Focuses upgrade starting spirits by removing earlier tiers (remove_ideas / add_ideas).
- Short-term crisis moments use add_timed_idea (365/720 days).
- Topbar active spirits are kept strictly between 5 and 6 at any given time.
"""

from pathlib import Path
import re
import sys

# Map of upgraded rewards for focuses across all 5 wings
REWARDS_MAP = {
    # -------------------------------------------------------------------------
    # WING 1: POLITICS & GOVERNMENT
    # -------------------------------------------------------------------------
    "TUR_second_constitutional_era_politics": [
        "add_political_power = 100",
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }",
        "set_country_flag = TUR_constitutional_reforms_begun"
    ],
    "TUR_cup_vanguard": [
        "country_event = { id = ww1_ottoman.2 }",
        "remove_ideas = TUR_second_constitutional_era",
        "add_ideas = TUR_cup_vanguard_centralization",
        "add_to_variable = { tur_imperial_cohesion = 5 }",
        "add_to_variable = { tur_arab_unrest = 5 }",
        "add_popularity = { ideology = fascism popularity = 0.15 }"
    ],
    "TUR_talat_interior_ministry": [
        "add_political_power = 75",
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_enver_military_drive": [
        "add_war_support = 0.10",
        "army_experience = 25",
        "add_command_power = 20"
    ],
    "TUR_cemal_public_order": [
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }",
        "add_to_variable = { tur_arab_unrest = -5 }"
    ],
    "TUR_bab_i_ali_consolidation": [
        "country_event = { id = ww1_ottoman.3 }",
        "set_politics = { ruling_party = fascism elections_allowed = no }",
        "add_political_power = 120",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_teskilat_i_mahsusa": [
        "add_timed_idea = { idea = TUR_teskilat_i_mahsusa_network days = 720 }",
        "add_political_power = 60",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_centralist_provincial_governors": [
        "add_stability = 0.05",
        "add_political_power = 60",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_to_variable = { tur_arab_unrest = 5 }"
    ],
    "TUR_paramilitary_youth_unions": [
        "add_manpower = 25000",
        "add_war_support = 0.08"
    ],
    "TUR_national_bourgeoisie_creation": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_secular_law_codes": [
        "add_research_slot = 1",
        "add_stability = -0.03",
        "add_political_power = 50"
    ],
    "TUR_turkification_of_trade": [
        "add_political_power = 75",
        "add_to_variable = { tur_foreign_influence = -15 }",
        "add_to_variable = { tur_public_debt = -5 }",
        "add_tech_bonus = { name = TUR_milli_iktisat bonus = 1.0 ahead_reduction = 1 category = industry }",
        "797 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_milli_iktisat_policies": [
        "340 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.05",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_state_controlled_newspapers": [
        "add_war_support = 0.10",
        "add_political_power = 50",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_sublime_porte_war_council": [
        "army_experience = 30",
        "add_command_power = 25",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],

    # Branch 1.2: Entente Libérale / Decentralization
    "TUR_hurriyet_ve_itilaf_victory": [
        "remove_ideas = TUR_second_constitutional_era",
        "add_ideas = TUR_hurriyet_ve_itilaf_governance",
        "add_popularity = { ideology = democratic popularity = 0.20 }",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_prince_sabahaddin_doctrine": [
        "add_political_power = 80",
        "add_stability = 0.05",
        "add_to_variable = { tur_foreign_influence = 5 }"
    ],
    "TUR_provincial_self_governance": [
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_to_variable = { tur_arab_unrest = -15 }"
    ],
    "TUR_empower_minority_bourgeoisie": [
        "339 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_anglo_french_constitutionalism": [
        "add_opinion_modifier = { target = ENG modifier = positive_50 }",
        "add_opinion_modifier = { target = FRA modifier = positive_50 }",
        "add_to_variable = { tur_foreign_influence = 5 }"
    ],
    "TUR_pluralistic_parliament": [
        "set_politics = { ruling_party = democratic elections_allowed = yes }",
        "add_stability = 0.10",
        "add_research_slot = 1"
    ],
    "TUR_judicial_and_press_liberties": [
        "add_political_power = 60",
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_millet_equality_charter": [
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_civic_ottomanism_restored": [
        "add_stability = 0.10",
        "add_political_power = 75",
        "add_to_variable = { tur_imperial_cohesion = 15 }",
        "add_to_variable = { tur_arab_unrest = -15 }"
    ],
    "TUR_decentralized_tax_farming_abolition": [
        "add_political_power = 80",
        "add_to_variable = { tur_public_debt = -15 }",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_stability = 0.05",
        "343 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_liberal_parliamentary_hegemony": [
        "add_political_power = 100",
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],

    # Branch 1.3: Palace Autocracy
    "TUR_imperial_prerogative_of_mehmed_v": [
        "remove_ideas = TUR_second_constitutional_era",
        "add_ideas = TUR_palace_autocracy_restored",
        "add_popularity = { ideology = neutrality popularity = 0.25 }",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_loyal_viziers_cabinet": [
        "add_political_power = 80",
        "add_stability = 0.05"
    ],
    "TUR_traditional_ulema_alliance": [
        "add_stability = 0.10",
        "add_war_support = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_dissolve_fractious_assembly": [
        "set_politics = { ruling_party = neutrality elections_allowed = no }",
        "add_political_power = 120",
        "add_stability = -0.05"
    ],
    "TUR_imperial_bodyguard_regiments": [
        "add_manpower = 15000",
        "army_experience = 20"
    ],
    "TUR_reinforce_the_porte": [
        "add_stability = 0.08",
        "add_political_power = 60",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_sultans_decree_prerogatives": [
        "add_political_power = 100",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_court_appointed_valis": [
        "add_stability = 0.05",
        "add_political_power = 50",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_divan_council_restored": [
        "add_political_power = 90",
        "add_stability = 0.08"
    ],
    "TUR_absolute_caliphal_authority": [
        "add_stability = 0.15",
        "add_war_support = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],

    # Branch 1.4: Arab Provinces & Caliphate
    "TUR_arab_congress_dialogue": [
        "country_event = { id = ww1_ottoman.4 }",
        "add_political_power = 50",
        "add_to_variable = { tur_arab_unrest = -10 }",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_beirut_and_damascus_charters": [
        "553 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.05",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_dual_monarchy_protocol": [
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 15 }",
        "add_to_variable = { tur_arab_unrest = -20 }"
    ],
    "TUR_guaranteed_arab_cabinet_seats": [
        "add_political_power = 60",
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_loyal_tribal_federation": [
        "add_manpower = 20000",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_caliphate_and_arab_solidarity": [
        "add_war_support = 0.10",
        "add_stability = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_bilingual_imperial_administration": [
        "add_stability = 0.08",
        "add_political_power = 50",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_sharifian_protectorate_accord": [
        "add_stability = 0.08",
        "add_to_variable = { tur_arab_unrest = -15 }",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_mesopotamian_notables_council": [
        "291 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_syrian_economic_integration": [
        "554 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_pan_islamic_imperial_brotherhood": [
        "add_war_support = 0.10",
        "add_manpower = 30000",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_shrine_of_eyup_pilgrimage": [
        "add_stability = 0.08",
        "add_political_power = 50"
    ],
    "TUR_mobilize_sufi_brotherhoods": [
        "add_manpower = 25000",
        "add_war_support = 0.05"
    ],
    "TUR_holy_cities_custodianship": [
        "add_political_power = 75",
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_proclamation_of_jihad_readiness": [
        "country_event = { id = ww1_ottoman.14 }",
        "add_war_support = 0.15",
        "add_manpower = 35000",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_imperial_cohesion_ascendant": [
        "add_stability = 0.15",
        "add_political_power = 100",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_legacy_of_osman_eternal": [
        "add_stability = 0.20",
        "add_war_support = 0.15",
        "add_political_power = 150",
        "add_to_variable = { tur_imperial_cohesion = 25 }"
    ],

    # -------------------------------------------------------------------------
    # WING 2: ECONOMY, PUBLIC DEBT, RAILWAYS & INDUSTRY
    # -------------------------------------------------------------------------
    "TUR_economic_sovereignty_drive": [
        "add_political_power = 60",
        "add_to_variable = { tur_public_debt = -5 }",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_audit_opda_administration": [
        "add_political_power = 60",
        "add_to_variable = { tur_public_debt = -5 }",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_renegotiate_creditor_coupons": [
        "country_event = { id = ww1_ottoman.7 }",
        "remove_ideas = TUR_sick_man_debt",
        "add_ideas = TUR_debt_renegotiated",
        "add_to_variable = { tur_public_debt = -15 }",
        "add_to_variable = { tur_foreign_influence = -10 }"
    ],
    "TUR_unilateral_abrogation_of_capitulations": [
        "country_event = { id = ww1_ottoman.8 }",
        "remove_ideas = TUR_debt_renegotiated",
        "add_ideas = TUR_capitulations_abrogated",
        "add_to_variable = { tur_foreign_influence = -25 }",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_protective_tariff_code": [
        "add_political_power = 50",
        "341 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_foreign_influence = -5 }"
    ],
    "TUR_national_bank_osmanli_itibar": [
        "country_event = { id = ww1_ottoman.24 }",
        "add_political_power = 60",
        "add_to_variable = { tur_public_debt = -10 }",
        "add_to_variable = { tur_foreign_influence = -15 }"
    ],
    "TUR_confiscate_foreign_monopolies": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_foreign_influence = -15 }"
    ],
    "TUR_monetary_autonomy_and_gold_lira": [
        "add_political_power = 75",
        "add_to_variable = { tur_public_debt = -15 }",
        "add_to_variable = { tur_foreign_influence = -10 }",
        "add_stability = 0.05",
        "add_tech_bonus = { name = TUR_gold_lira bonus = 1.0 ahead_reduction = 1 category = industry }"
    ],
    "TUR_tobacco_regie_liquidation": [
        "340 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_foreign_influence = -10 }"
    ],
    "TUR_salt_monopoly_nationalization": [
        "346 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_public_debt = -10 }"
    ],
    "TUR_complete_fiscal_liberation": [
        "remove_ideas = TUR_capitulations_abrogated",
        "add_ideas = TUR_financial_sovereignty",
        "add_political_power = 100",
        "add_to_variable = { tur_public_debt = -20 }",
        "add_to_variable = { tur_foreign_influence = -20 }"
    ],
    "TUR_taurus_and_amanus_tunnels": [
        "country_event = { id = ww1_ottoman.9 }",
        "344 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_konya_aleppo_trunk_line": [
        "346 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"
    ],
    "TUR_aleppo_to_mosul_extension": [
        "676 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "add_to_variable = { tur_arab_unrest = -5 }"
    ],
    "TUR_mosul_baghdad_railhead": [
        "291 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_basra_terminus_settlement": [
        "811 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_political_power = 40"
    ],
    "TUR_hejaz_railway_expansion": [
        "551 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "550 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_to_variable = { tur_arab_unrest = -10 }",
        "add_stability = 0.05"
    ],
    "TUR_syrian_feeder_lines": [
        "553 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"
    ],
    "TUR_medina_to_mecca_link": [
        "550 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 10 }",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_jerusalem_jaffa_railway_upgrade": [
        "552 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_anatolian_railway_loop": [
        "341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "347 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"
    ],
    "TUR_railway_telegraph_integration": [
        "add_tech_bonus = { name = industrial_bonus bonus = 0.50 uses = 1 category = industry }",
        "add_political_power = 50"
    ],
    "TUR_zonguldak_coal_basin_drives": [
        "341 = { add_resource = { type = steel amount = 12 } }",
        "add_political_power = 40"
    ],
    "TUR_ergani_copper_mines": [
        "354 = { add_resource = { type = steel amount = 8 } }",
        "add_political_power = 30"
    ],
    "TUR_tophane_ordnance_foundry": [
        "797 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_bakirkoy_textile_mills": [
        "797 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_zeytinburnu_munitions_complex": [
        "797 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_ankara_state_foundries": [
        "341 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_izmir_commercial_quays": [
        "339 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant_build = yes } }"
    ],
    "TUR_constantinople_electric_grid": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_amasya_metal_smelters": [
        "347 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_imperial_munitions_directorate": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 2 instant_build = yes } }",
        "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2500 producer = TUR }",
        "add_tech_bonus = { name = TUR_munitions bonus = 1.0 ahead_reduction = 1 category = weapons }",
        "army_experience = 20"
    ],
    "TUR_full_industrial_mobilization": [
        "add_war_support = 0.10",
        "346 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_anatolian_grain_reserves": [
        "343 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "344 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_stability = 0.08",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_willcocks_mesopotamia_irrigation": [
        "291 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_arab_unrest = -5 }"
    ],
    "TUR_cilicia_cotton_modernization": [
        "344 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_anti_locust_campaigns": [
        "country_event = { id = ww1_ottoman.18 }",
        "add_political_power = 40",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_state_silos_and_famine_relief": [
        "add_stability = 0.08",
        "add_political_power = 40",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_ziraat_bankasi_credit_expansion": [
        "add_political_power = 50",
        "346 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_mechanized_anatolian_farming": [
        "add_tech_bonus = { name = industrial_bonus bonus = 0.50 uses = 1 category = industry }",
        "add_stability = 0.05"
    ],
    "TUR_black_sea_timber_concessions": [
        "341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_political_power = 40"
    ],
    "TUR_agrarian_surplus_storage": [
        "add_stability = 0.08",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_breadbasket_of_the_empire": [
        "346 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_integrated_imperial_economy": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_anatolian_highway_system": [
        "346 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "347 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"
    ],
    "TUR_petroleum_concessions_mosul": [
        "country_event = { id = ww1_ottoman.25 }",
        "676 = { add_resource = { type = oil amount = 24 } }",
        "676 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "676 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = synthetic_refinery level = 1 instant_build = yes } }",
        "add_to_variable = { tur_foreign_influence = -15 }",
        "add_tech_bonus = { name = TUR_petroleum bonus = 1.0 ahead_reduction = 1 category = industry }"
    ],
    "TUR_sublime_porte_heavy_industry_board": [
        "341 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = industrial_bonus bonus = 0.50 uses = 1 category = industry }"
    ],
    "TUR_autarkic_imperial_foundation": [
        "add_stability = 0.08",
        "add_political_power = 50",
        "add_to_variable = { tur_foreign_influence = -15 }"
    ],
    "TUR_modern_ottoman_economic_miracle": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "341 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.10",
        "add_to_variable = { tur_public_debt = -20 }"
    ],

    # -------------------------------------------------------------------------
    # WING 3: ARMED FORCES, NAVY & AVIATION
    # -------------------------------------------------------------------------
    "TUR_reorganizing_the_imperial_army": [
        "army_experience = 30",
        "add_command_power = 25",
        "remove_ideas = TUR_army_modernization_struggle",
        "add_ideas = TUR_german_military_mission"
    ],
    "TUR_harbiye_academy_modernization": [
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }",
        "army_experience = 20"
    ],
    "TUR_purge_inefficient_cadres": [
        "army_experience = 25",
        "add_political_power = 50",
        "add_stability = -0.03"
    ],
    "TUR_standardize_mauser_rifles": [
        "341 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = infantry_weapons bonus = 0.50 uses = 1 category = infantry_weapons }"
    ],
    "TUR_krupp_quick_fire_artillery": [
        "346 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = artillery_bonus bonus = 0.50 uses = 1 category = artillery }"
    ],
    "TUR_anatolian_infantry_doctrine": [
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }",
        "army_experience = 25"
    ],
    "TUR_desert_camel_corps_regiments": [
        "add_manpower = 15000",
        "army_experience = 15"
    ],
    "TUR_caucasus_alpine_detachments": [
        "add_timed_idea = { idea = TUR_caucasus_alpine_preparations days = 720 }",
        "army_experience = 25",
        "add_command_power = 20"
    ],
    "TUR_machine_gun_companies": [
        "354 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = infantry_weapons bonus = 0.50 uses = 1 category = infantry_weapons }",
        "army_experience = 15"
    ],
    "TUR_field_medicine_red_crescent": [
        "add_timed_idea = { idea = TUR_red_crescent_logistics days = 720 }",
        "add_tech_bonus = { name = TUR_red_crescent bonus = 1.0 ahead_reduction = 1 category = support_tech }",
        "army_experience = 20"
    ],
    "TUR_gendarmerie_modernization_corps": [
        "add_stability = 0.08",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_heavy_siege_howitzers": [
        "346 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 150 producer = TUR }",
        "add_tech_bonus = { name = artillery_bonus bonus = 0.50 uses = 1 category = artillery }",
        "army_experience = 20"
    ],
    "TUR_comprehensive_conscription_law": [
        "add_manpower = 40000",
        "add_war_support = 0.08"
    ],
    "TUR_foreign_mission_choice": [
        "country_event = { id = ww1_ottoman.5 }",
        "army_experience = 20",
        "add_political_power = 40"
    ],
    "TUR_german_military_mission_sanders": [
        "country_event = { id = ww1_ottoman.5 }",
        "army_experience = 30",
        "add_opinion_modifier = { target = GER modifier = positive_50 }",
        "add_to_variable = { tur_foreign_influence = 5 }"
    ],
    "TUR_native_general_staff_kemal": [
        "if = { limit = { has_idea = TUR_german_military_mission } remove_ideas = TUR_german_military_mission }",
        "if = { limit = { has_idea = TUR_army_modernization_struggle } remove_ideas = TUR_army_modernization_struggle }",
        "add_ideas = TUR_kemalist_tactical_doctrine",
        "army_experience = 35",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_prusso_ottoman_doctrine": [
        "add_doctrine_cost_reduction = { name = TUR_prusso_doctrine cost_reduction = 0.5 category = land_doctrine }",
        "add_tech_bonus = { name = doctrine_bonus bonus = 1.0 ahead_reduction = 1 category = land_doctrine }",
        "army_experience = 35",
        "add_command_power = 25"
    ],
    "TUR_independent_tactical_flexibility": [
        "army_experience = 30",
        "add_command_power = 20"
    ],
    "TUR_krupp_heavy_ordnance_contracts": [
        "346 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = artillery_bonus bonus = 0.50 uses = 1 category = artillery }",
        "army_experience = 20"
    ],
    "TUR_anatolian_guerrilla_tradition": [
        "army_experience = 20",
        "add_war_support = 0.05",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_joint_staff_operational_drills": [
        "if = { limit = { has_idea = TUR_german_military_mission } remove_ideas = TUR_german_military_mission }",
        "if = { limit = { has_idea = TUR_kemalist_tactical_doctrine } remove_ideas = TUR_kemalist_tactical_doctrine }",
        "add_ideas = TUR_reformed_ottoman_corps",
        "army_experience = 30",
        "add_command_power = 25"
    ],
    "TUR_officer_corps_intellectual_vigor": [
        "army_experience = 25",
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }"
    ],
    "TUR_divisional_artillery_batteries": [
        "347 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "add_tech_bonus = { name = artillery_bonus bonus = 0.50 uses = 1 category = artillery }"
    ],
    "TUR_corps_level_reserves_doctrine": [
        "army_experience = 30",
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }"
    ],
    "TUR_rebuild_the_imperial_fleet": [
        "navy_experience = 30",
        "add_political_power = 50",
        "797 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant_build = yes } }"
    ],
    "TUR_the_dreadnought_contracts_uk": [
        "country_event = { id = ww1_ottoman.6 }",
        "navy_experience = 25",
        "add_opinion_modifier = { target = ENG modifier = positive_50 }"
    ],
    "TUR_golden_horn_shipyards_expansion": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 1 instant_build = yes } }"
    ],
    "TUR_public_donation_drive_sultan_osman": [
        "add_political_power = 60",
        "add_war_support = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 5 }"
    ],
    "TUR_torpedo_boat_flotillas": [
        "add_tech_bonus = { name = naval_bonus bonus = 0.50 uses = 1 category = naval_equipment }",
        "navy_experience = 20"
    ],
    "TUR_welcome_goeben_and_breslau": [
        "country_event = { id = ww1_ottoman.10 }",
        "add_timed_idea = { idea = TUR_yavuz_and_midilli_supremacy days = 720 }",
        "navy_experience = 30",
        "add_war_support = 0.10"
    ],
    "TUR_black_sea_submarine_patrols": [
        "add_tech_bonus = { name = naval_bonus bonus = 0.50 uses = 1 category = naval_equipment }",
        "navy_experience = 25"
    ],
    "TUR_coastal_minelayer_force": [
        "navy_experience = 20",
        "341 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }"
    ],
    "TUR_naval_gunnery_schools": [
        "navy_experience = 30",
        "add_command_power = 20"
    ],
    "TUR_cruiser_escort_squadrons": [
        "navy_experience = 25",
        "339 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant_build = yes } }"
    ],
    "TUR_sovereign_black_sea_fleet": [
        "add_war_support = 0.10",
        "navy_experience = 35",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_yesilkoy_aviation_school": [
        "341 = { add_building_construction = { type = air_base level = 2 instant_build = yes } }",
        "air_experience = 35",
        "add_tech_bonus = { name = air_bonus bonus = 0.50 uses = 1 category = air_equipment }"
    ],
    "TUR_strengthen_canakkale_batteries": [
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "remove_ideas = TUR_straits_fortress_cannons",
        "add_ideas = TUR_canakkale_impenetrable_bastion"
    ],
    "TUR_procure_bleriot_and_rumpler_monoplanes": [
        "air_experience = 25",
        "add_tech_bonus = { name = air_bonus bonus = 0.50 uses = 1 category = air_equipment }"
    ],
    "TUR_underwater_minefields_straits": [
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "add_war_support = 0.05"
    ],
    "TUR_aerial_reconnaissance_detachments": [
        "air_experience = 25",
        "add_command_power = 20"
    ],
    "TUR_searchlight_batteries_dardanelles": [
        "341 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_joint_command_supreme_staff": [
        "341 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "army_experience = 30",
        "navy_experience = 20",
        "add_command_power = 30"
    ],
    "TUR_modern_field_communications": [
        "add_tech_bonus = { name = electronics_bonus bonus = 0.50 uses = 1 category = electronics }",
        "army_experience = 20"
    ],
    "TUR_logistics_motor_truck_corps": [
        "341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "army_experience = 20"
    ],
    "TUR_imperial_arsenals_peak_output": [
        "554 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }",
        "army_experience = 25"
    ],
    "TUR_harbiye_tactical_doctrine_zenith": [
        "army_experience = 40",
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }"
    ],
    "TUR_invincible_mehmetcik_spirit": [
        "army_experience = 30",
        "add_war_support = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],

    # -------------------------------------------------------------------------
    # WING 4: DIPLOMACY & GREAT POWERS
    # -------------------------------------------------------------------------
    "TUR_sublime_porte_foreign_policy": [
        "add_political_power = 80",
        "add_to_variable = { tur_foreign_influence = 5 }"
    ],
    "TUR_western_thrace_border_vigilance": [
        "184 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }",
        "add_war_support = 0.05"
    ],
    "TUR_edirne_fortress_complex": [
        "184 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_bulgarian_friendship_treaty": [
        "add_opinion_modifier = { target = BUL modifier = positive_50 }",
        "add_stability = 0.05"
    ],
    "TUR_romanian_grain_accord": [
        "add_opinion_modifier = { target = ROM modifier = positive_50 }",
        "add_political_power = 40",
        "add_stability = 0.05"
    ],
    "TUR_reaffirm_libyan_sovereignty": [
        "add_war_support = 0.08",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_sanusi_brotherhood_pact": [
        "add_manpower = 20000",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_tripoli_coastal_fortifications": [
        "448 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_aegean_island_garrisons": [
        "339 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_german_rapprochement": [
        "add_opinion_modifier = { target = GER modifier = positive_75 }",
        "add_to_variable = { tur_foreign_influence = 10 }"
    ],
    "TUR_secret_alliance_august_1914": [
        "country_event = { id = ww1_ottoman.12 }",
        "add_political_power = 80",
        "add_opinion_modifier = { target = GER modifier = positive_75 }"
    ],
    "TUR_german_gold_loans": [
        "add_political_power = 100",
        "add_to_variable = { tur_public_debt = -10 }"
    ],
    "TUR_souchon_black_sea_raid": [
        "country_event = { id = ww1_ottoman.13 }",
        "add_war_support = 0.15"
    ],
    "TUR_join_central_powers_faction": [
        "add_to_faction = GER",
        "add_war_support = 0.10"
    ],
    "TUR_berlin_constantinople_axis": [
        "add_opinion_modifier = { target = GER modifier = positive_100 }",
        "add_political_power = 60"
    ],
    "TUR_austro_hungarian_danubian_link": [
        "add_opinion_modifier = { target = AUS modifier = positive_75 }",
        "add_stability = 0.05"
    ],
    "TUR_bulgarian_transit_corridor": [
        "add_opinion_modifier = { target = BUL modifier = positive_75 }",
        "add_political_power = 40"
    ],
    "TUR_central_powers_war_council": [
        "army_experience = 35",
        "add_command_power = 30"
    ],
    "TUR_shared_munitions_standardization": [
        "army_experience = 30",
        "add_tech_bonus = { name = infantry_weapons bonus = 0.50 uses = 1 category = infantry_weapons }"
    ],
    "TUR_strict_armed_neutrality": [
        "add_stability = 0.15",
        "add_political_power = 100",
        "add_to_variable = { tur_foreign_influence = -15 }"
    ],
    "TUR_close_straits_to_all_belligerents": [
        "country_event = { id = ww1_ottoman.11 }",
        "add_political_power = 50",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_demand_belligerent_transit_tolls": [
        "add_political_power = 75",
        "add_to_variable = { tur_public_debt = -5 }"
    ],
    "TUR_internal_development_focus": [
        "341 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.08"
    ],
    "TUR_profit_from_wartime_trade": [
        "add_political_power = 120",
        "add_to_variable = { tur_public_debt = -15 }"
    ],
    "TUR_swiss_of_the_orient_neutrality": [
        "add_stability = 0.20",
        "add_political_power = 100",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_diplomatic_mediation_summit": [
        "add_political_power = 150",
        "add_stability = 0.10"
    ],
    "TUR_neutral_soovereignty_guaranteed": [
        "add_stability = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_entente_diplomatic_demands": [
        "add_political_power = 50",
        "add_to_variable = { tur_foreign_influence = 5 }"
    ],
    "TUR_demand_dreadnought_deliveries": [
        "country_event = { id = ww1_ottoman.1 }",
        "add_war_support = 0.15",
        "add_political_power = 60"
    ],
    "TUR_territorial_integrity_guarantees": [
        "add_stability = 0.10",
        "add_political_power = 60"
    ],
    "TUR_anglo_ottoman_gulf_treaty": [
        "add_opinion_modifier = { target = ENG modifier = positive_75 }",
        "add_political_power = 50"
    ],
    "TUR_neutralize_russian_threat": [
        "add_opinion_modifier = { target = RUS modifier = positive_50 }",
        "add_stability = 0.05"
    ],
    "TUR_french_syrian_economic_pact": [
        "553 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_opinion_modifier = { target = FRA modifier = positive_50 }"
    ],
    "TUR_entente_cooperation_treaty": [
        "add_opinion_modifier = { target = ENG modifier = positive_75 }",
        "add_opinion_modifier = { target = FRA modifier = positive_75 }",
        "add_political_power = 75"
    ],
    "TUR_secured_ottoman_borders": [
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_the_sovereign_straits_regime": [
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_dardanelles_maritime_hegemony": [
        "navy_experience = 30",
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }"
    ],
    "TUR_levantine_coastal_security": [
        "553 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_sublime_porte_global_standing": [
        "add_stability = 0.15",
        "add_political_power = 100",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_destiny_of_the_near_east": [
        "add_stability = 0.15",
        "add_war_support = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_pax_osmanica_reasserted": [
        "add_stability = 0.20",
        "add_political_power = 150",
        "add_to_variable = { tur_imperial_cohesion = 25 }"
    ],

    # -------------------------------------------------------------------------
    # WING 5: WAR THEATERS & ENDGAME
    # -------------------------------------------------------------------------
    "TUR_the_war_for_imperial_survival": [
        "add_war_support = 0.15",
        "army_experience = 25",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_caucasus_logistics_preparation": [
        "354 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "army_experience = 20"
    ],
    "TUR_third_army_mountain_offensive": [
        "country_event = { id = ww1_ottoman.15 }",
        "army_experience = 30",
        "add_to_variable = { tur_imperial_cohesion = -5 }"
    ],
    "TUR_trabzon_supply_lifeline": [
        "341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_retake_kars_ardahan_batum": [
        "add_war_support = 0.15",
        "army_experience = 30",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_army_of_islam_caucasus": [
        "country_event = { id = ww1_ottoman.22 }",
        "add_manpower = 25000",
        "army_experience = 25",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_baku_petroleum_drive": [
        "add_war_support = 0.15",
        "add_political_power = 80",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_caspian_flotilla_organization": [
        "navy_experience = 20",
        "add_command_power = 20"
    ],
    "TUR_caucasian_tribal_auxiliaries": [
        "add_manpower = 20000",
        "army_experience = 15"
    ],
    "TUR_transcaucasian_security_sphere": [
        "add_stability = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_cevat_pasha_artillery_defence": [
        "country_event = { id = ww1_ottoman.16 }",
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "army_experience = 35"
    ],
    "TUR_chunuk_bair_counterattack": [
        "country_event = { id = ww1_ottoman.17 }",
        "army_experience = 40",
        "add_war_support = 0.15"
    ],
    "TUR_fifth_army_mobile_reserves": [
        "add_manpower = 20000",
        "army_experience = 25"
    ],
    "TUR_drive_invaders_into_the_sea": [
        "add_war_support = 0.15",
        "add_stability = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_anafartalar_heroism_legacy": [
        "add_war_support = 0.10",
        "army_experience = 30",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_fortress_canakkale_permanent": [
        "341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }",
        "add_stability = 0.10"
    ],
    "TUR_tigris_river_flotilla": [
        "navy_experience = 20",
        "army_experience = 15"
    ],
    "TUR_defense_of_kut_al_amara": [
        "country_event = { id = ww1_ottoman.17 }",
        "291 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "army_experience = 30"
    ],
    "TUR_encirclement_of_townshend_army": [
        "add_war_support = 0.15",
        "army_experience = 35",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_halil_kut_triumph": [
        "add_timed_idea = { idea = TUR_kut_al_amara_triumph days = 365 }",
        "add_stability = 0.10",
        "add_political_power = 75"
    ],
    "TUR_secure_basra_access": [
        "811 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "army_experience = 20"
    ],
    "TUR_shatt_al_arab_defensive_perimeter": [
        "811 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_cross_the_sinai_desert": [
        "army_experience = 25",
        "add_command_power = 25"
    ],
    "TUR_suez_canal_raids": [
        "add_war_support = 0.10",
        "army_experience = 30",
        "add_political_power = 50"
    ],
    "TUR_gaza_beersheba_defensive_line": [
        "country_event = { id = ww1_ottoman.21 }",
        "552 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "add_timed_idea = { idea = TUR_gaza_beersheba_defensive_wall days = 365 }"
    ],
    "TUR_defense_of_jerusalem": [
        "552 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "add_stability = 0.08"
    ],
    "TUR_damascus_bastion": [
        "554 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "army_experience = 20"
    ],
    "TUR_levantine_supply_depots": [
        "553 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_protect_hejaz_railway_garrisons": [
        "551 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
    "TUR_fakhri_pasha_medina_defense": [
        "country_event = { id = ww1_ottoman.20 }",
        "add_timed_idea = { idea = TUR_fakhri_pasha_desert_stand days = 365 }",
        "add_war_support = 0.10",
        "army_experience = 30"
    ],
    "TUR_crush_or_reconcile_sharifians": [
        "country_event = { id = ww1_ottoman.19 }",
        "add_political_power = 60",
        "add_to_variable = { tur_arab_unrest = -20 }"
    ],
    "TUR_holy_relics_safeguard": [
        "add_stability = 0.10",
        "add_political_power = 50",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_red_sea_desert_patrols": [
        "army_experience = 20",
        "add_command_power = 20"
    ],
    "TUR_war_bread_and_rationing": [
        "add_timed_idea = { idea = TUR_war_bread_and_rationing days = 365 }",
        "add_political_power = 40"
    ],
    "TUR_requisition_imperial_resources": [
        "add_war_support = 0.10",
        "add_political_power = 50"
    ],
    "TUR_teskilat_asymmetric_warfare": [
        "army_experience = 30",
        "add_command_power = 25"
    ],
    "TUR_counter_the_blockade": [
        "797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_total_war_labour_mobilization": [
        "add_war_support = 0.10",
        "346 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }"
    ],
    "TUR_emergency_war_levies": [
        "add_manpower = 50000",
        "add_stability = -0.05"
    ],
    "TUR_the_eastern_storm_survived": [
        "add_stability = 0.15",
        "add_war_support = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_brest_litovsk_claims": [
        "country_event = { id = ww1_ottoman.30 }",
        "add_political_power = 100",
        "add_war_support = 0.10",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_middle_eastern_hegemon": [
        "add_political_power = 120",
        "add_stability = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 20 }"
    ],
    "TUR_1918_total_victory_protocol": [
        "country_event = { id = ww1_ottoman.28 }",
        "add_stability = 0.20",
        "add_political_power = 150",
        "add_to_variable = { tur_imperial_cohesion = 30 }"
    ],
    "TUR_reborn_empire_destiny": [
        "country_event = { id = ww1_ottoman.28 }",
        "add_stability = 0.20",
        "add_war_support = 0.15",
        "add_to_variable = { tur_imperial_cohesion = 30 }"
    ],
    "TUR_republican_renaissance_destiny": [
        "add_stability = 0.15",
        "add_political_power = 120",
        "add_to_variable = { tur_imperial_cohesion = 25 }"
    ],
    "TUR_eternal_sublime_destiny": [
        "country_event = { id = ww1_ottoman.28 }",
        "add_stability = 0.25",
        "add_political_power = 200",
        "add_to_variable = { tur_imperial_cohesion = 35 }"
    ],

    # Additional foci to complete the 256 set
    "TUR_macedonian_and_thracian_veterans": [
        "army_experience = 30",
        "add_manpower = 20000"
    ],
    "TUR_constantinople_press_syndicate": [
        "add_political_power = 60",
        "add_stability = 0.05"
    ],
    "TUR_al_fatat_secret_dialogue": [
        "add_political_power = 50",
        "add_to_variable = { tur_arab_unrest = -15 }",
        "add_to_variable = { tur_imperial_cohesion = 10 }"
    ],
    "TUR_arab_notables_chamber": [
        "country_event = { id = ww1_ottoman.27 }",
        "add_stability = 0.10",
        "add_to_variable = { tur_arab_unrest = -20 }",
        "add_to_variable = { tur_imperial_cohesion = 15 }"
    ],
    "TUR_pontic_coal_shipping": [
        "341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_political_power = 40"
    ],
    "TUR_cilicia_irrigation_canals": [
        "344 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_aleppo_commercial_hub": [
        "554 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"
    ],
    "TUR_syrian_grain_storage": [
        "554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_izmir_naval_seaplane_base": [
        "air_experience = 20",
        "navy_experience = 20"
    ],
    "TUR_marmara_anti_submarine_nets": [
        "797 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
        "navy_experience = 15"
    ],
    "TUR_cavalry_reconnaissance_squadrons": [
        "army_experience = 20",
        "add_command_power = 20"
    ],
    "TUR_harbiye_cadet_battalions": [
        "army_experience = 25",
        "add_manpower = 15000"
    ],
    "TUR_rome_mediterranean_dialogue": [
        "add_opinion_modifier = { target = ITA modifier = positive_50 }",
        "add_political_power = 40"
    ],
    "TUR_paris_credit_negotiations": [
        "add_opinion_modifier = { target = FRA modifier = positive_50 }",
        "add_to_variable = { tur_public_debt = -10 }"
    ],
    "TUR_persian_border_security": [
        "354 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }",
        "add_stability = 0.05"
    ],
    "TUR_cyrenaica_desert_posts": [
        "448 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }",
        "army_experience = 15"
    ],
    "TUR_erzurum_fortress_line": [
        "354 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "army_experience = 20"
    ],
    "TUR_trench_warfare_drills_canakkale": [
        "army_experience = 30",
        "add_tech_bonus = { name = doctrine_bonus bonus = 0.50 uses = 1 category = land_doctrine }"
    ],
    "TUR_ctesiphon_defensive_stand": [
        "291 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }",
        "army_experience = 25"
    ],
    "TUR_hejaz_armored_train_patrols": [
        "551 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }",
        "add_to_variable = { tur_arab_unrest = -10 }"
    ],
}

def update_generator():
    gen_file = Path("scripts/generate_full_ottoman_tree.py")
    lines = gen_file.read_text(encoding="utf-8").splitlines()
    
    new_lines = []
    i = 0
    updated_count = 0
    
    while i < len(lines):
        line = lines[i]
        # Match add_f("FOCUS_ID", ...
        m = re.match(r'^(add_f\(\s*)"([^"]+)"(.*)$', line)
        if m:
            prefix, fid, rest = m.group(1), m.group(2), m.group(3)
            # Gather lines until closing parenthesis of add_f
            block_lines = [line]
            while i + 1 < len(lines) and not block_lines[-1].strip().endswith(")") and not (block_lines[-1].strip().endswith("),") or (")" in block_lines[-1] and "add_f" not in lines[i+1])):
                i += 1
                block_lines.append(lines[i])
            
            block_text = "\n".join(block_lines)
            
            if fid in REWARDS_MAP:
                new_rewards_list = REWARDS_MAP[fid]
                formatted_rewards = "rewards=[" + ", ".join([f'"{r}"' for r in new_rewards_list]) + "]"
                
                # Regex replace rewards=[...]
                if "rewards=" in block_text:
                    block_text = re.sub(r'rewards=\[[^\]]*\]', formatted_rewards, block_text)
                else:
                    if "filters=" in block_text:
                        block_text = re.sub(r'filters=', f'{formatted_rewards},\n      filters=', block_text)
                    else:
                        block_text = block_text[:-1] + f",\n      {formatted_rewards})"
                updated_count += 1
            
            new_lines.append(block_text)
        else:
            new_lines.append(line)
        i += 1
        
    gen_file.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"Updated {updated_count} focuses in {gen_file}")

if __name__ == "__main__":
    update_generator()
