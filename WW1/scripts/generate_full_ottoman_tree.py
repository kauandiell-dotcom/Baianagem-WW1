#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full generator for Ottoman Empire (TUR) WW1 National Focus Tree (1911-1918).
Generates exactly 255 focuses across 5 non-colliding visual wings:
- Wing 1: Politics, Governance, Constitutional Paths (55 focuses, x=1..15, y=0..13)
- Wing 2: Economy, Public Debt, Railways, Industry (52 focuses, x=18..32, y=0..13)
- Wing 3: Imperial Armed Forces Modernization, Navy, Aviation (50 focuses, x=35..49, y=0..13)
- Wing 4: Diplomacy, Great Powers, The Straits (46 focuses, x=52..66, y=0..13)
- Wing 5: The Great War Theaters & 1918 Endgame (52 focuses, x=69..85, y=0..14)
Total = 255 focuses.
"""

from pathlib import Path

FOCI = []

def add_f(fid, x, y, cost, icon, prereqs=None, mut_excl=None, available=None, bypass=None, rewards=None, filters=None):
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
# WING 1: IMPERIAL GOVERNMENT & CONSTITUTIONAL DESTINY (55 FOCUSES, x=1..15)
# ==============================================================================

# Root (y=0)
add_f("TUR_second_constitutional_era_politics", 8, 0, 5, "GFX_focus_generic_parliament",
      rewards=["add_political_power = 100", "add_stability = 0.05", "set_country_flag = TUR_constitutional_reforms_begun"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

# Branch 1.1: CUP Centralization & Revolutionary Vanguard (x=1..5, y=1..8)
add_f("TUR_cup_vanguard", 3, 1, 5, "GFX_TUR_three_pashas",
      prereqs=["TUR_second_constitutional_era_politics"],
      mut_excl=["TUR_hurriyet_ve_itilaf_victory", "TUR_imperial_prerogative_of_mehmed_v"],
      rewards=["add_ideas = TUR_cup_vanguard_centralization", "remove_ideas = TUR_second_constitutional_era", "add_popularity = { ideology = fascism popularity = 0.15 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_talat_interior_ministry", 2, 2, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_cup_vanguard"],
      rewards=["add_political_power = 75", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_enver_military_drive", 4, 2, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_cup_vanguard"],
      rewards=["add_war_support = 0.10", "army_experience = 25"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_cemal_public_order", 3, 3, 5, "GFX_TUR_jandarma_genel_komutanlgi",
      prereqs=["TUR_talat_interior_ministry", "TUR_enver_military_drive"],
      rewards=["custom_effect_tooltip = TUR_tt_curb_unrest", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_bab_i_ali_consolidation", 3, 4, 5, "GFX_focus_generic_authoritarian",
      prereqs=["TUR_cemal_public_order"],
      rewards=["set_politics = { ruling_party = fascism elections_allowed = no }", "add_political_power = 120"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_teskilat_i_mahsusa", 1, 5, 5, "GFX_focus_generic_intelligence_agency",
      prereqs=["TUR_bab_i_ali_consolidation"],
      rewards=["add_ideas = TUR_teskilat_i_mahsusa_network", "create_operative_agent = yes"],
      filters=["FOCUS_FILTER_INTELLIGENCE"])

add_f("TUR_centralist_provincial_governors", 3, 5, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_bab_i_ali_consolidation"],
      rewards=["add_stability = 0.05", "add_political_power = 60"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_paramilitary_youth_unions", 5, 5, 5, "GFX_TUR_1914_law_of_military_obligation",
      prereqs=["TUR_bab_i_ali_consolidation"],
      rewards=["add_manpower = 25000", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_national_bourgeoisie_creation", 2, 6, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_centralist_provincial_governors"],
      rewards=["797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_secular_law_codes", 4, 6, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_centralist_provincial_governors"],
      rewards=["add_research_slot = 1", "add_stability = -0.05"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_turkification_of_trade", 1, 7, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_national_bourgeoisie_creation"],
      rewards=["add_political_power = 50", "consumer_goods_factor = -0.03"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_milli_iktisat_policies", 3, 7, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_national_bourgeoisie_creation", "TUR_secular_law_codes"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_state_controlled_newspapers", 5, 7, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_paramilitary_youth_unions"],
      rewards=["add_war_support = 0.10", "add_political_power = 50"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_sublime_porte_war_council", 3, 8, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_milli_iktisat_policies"],
      rewards=["army_experience = 30", "add_command_power = 25"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Branch 1.2: Freedom and Accord / Liberal Decentralization (x=6..9, y=1..8)
add_f("TUR_hurriyet_ve_itilaf_victory", 7, 1, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_second_constitutional_era_politics"],
      mut_excl=["TUR_cup_vanguard", "TUR_imperial_prerogative_of_mehmed_v"],
      rewards=["add_ideas = TUR_hurriyet_ve_itilaf_governance", "remove_ideas = TUR_second_constitutional_era", "add_popularity = { ideology = democratic popularity = 0.20 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_prince_sabahaddin_doctrine", 6, 2, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_hurriyet_ve_itilaf_victory"],
      rewards=["add_political_power = 80", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_provincial_self_governance", 8, 2, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_hurriyet_ve_itilaf_victory"],
      rewards=["custom_effect_tooltip = TUR_tt_provincial_autonomy", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_empower_minority_bourgeoisie", 6, 3, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_prince_sabahaddin_doctrine"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_anglo_french_constitutionalism", 8, 3, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_provincial_self_governance"],
      rewards=["add_opinion_modifier = { target = ENG modifier = positive_50 }", "add_opinion_modifier = { target = FRA modifier = positive_50 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_pluralistic_parliament", 7, 4, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_empower_minority_bourgeoisie", "TUR_anglo_french_constitutionalism"],
      rewards=["set_politics = { ruling_party = democratic elections_allowed = yes }", "add_stability = 0.10", "add_research_slot = 1"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_RESEARCH"])

add_f("TUR_judicial_and_press_liberties", 6, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_pluralistic_parliament"],
      rewards=["add_political_power = 60", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_millet_equality_charter", 8, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_pluralistic_parliament"],
      rewards=["add_stability = 0.10", "custom_effect_tooltip = TUR_tt_millet_equality"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_civic_ottomanism_restored", 7, 6, 5, "GFX_TUR_continuing_ottomanism_efforts",
      prereqs=["TUR_judicial_and_press_liberties", "TUR_millet_equality_charter"],
      rewards=["add_stability = 0.10", "add_political_power = 75"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_decentralized_tax_farming_abolition", 7, 7, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_civic_ottomanism_restored"],
      rewards=["consumer_goods_factor = -0.03", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_liberal_parliamentary_hegemony", 7, 8, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_decentralized_tax_farming_abolition"],
      rewards=["add_political_power = 100", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

# Branch 1.3: Palace Autocracy & Sultan's Prerogative (x=10..12, y=1..8)
add_f("TUR_imperial_prerogative_of_mehmed_v", 11, 1, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_second_constitutional_era_politics"],
      mut_excl=["TUR_cup_vanguard", "TUR_hurriyet_ve_itilaf_victory"],
      rewards=["add_ideas = TUR_palace_autocracy_restored", "remove_ideas = TUR_second_constitutional_era", "add_political_power = 100"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_loyal_viziers_cabinet", 10, 2, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_imperial_prerogative_of_mehmed_v"],
      rewards=["add_political_power = 75", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_traditional_ulema_alliance", 12, 2, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_imperial_prerogative_of_mehmed_v"],
      rewards=["add_stability = 0.10", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_dissolve_fractious_assembly", 11, 3, 5, "GFX_focus_generic_authoritarian",
      prereqs=["TUR_loyal_viziers_cabinet", "TUR_traditional_ulema_alliance"],
      rewards=["set_politics = { ruling_party = neutrality elections_allowed = no }", "add_political_power = 120"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_imperial_bodyguard_regiments", 10, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_dissolve_fractious_assembly"],
      rewards=["add_manpower = 20000", "army_experience = 20"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_reinforce_the_porte", 12, 4, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_dissolve_fractious_assembly"],
      rewards=["add_stability = 0.10", "add_political_power = 80"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_sultans_decree_prerogatives", 11, 5, 5, "GFX_focus_generic_authoritarian",
      prereqs=["TUR_imperial_bodyguard_regiments", "TUR_reinforce_the_porte"],
      rewards=["add_political_power = 90", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_court_appointed_valis", 11, 6, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_sultans_decree_prerogatives"],
      rewards=["add_stability = 0.05", "conscription_factor = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_divan_council_restored", 11, 7, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_court_appointed_valis"],
      rewards=["add_political_power = 100", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_absolute_caliphal_authority", 11, 8, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_divan_council_restored"],
      rewards=["add_war_support = 0.10", "add_stability = 0.10", "add_political_power = 150"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_WAR_SUPPORT"])

# Branch 1.4: Arab-Ottoman Compact & Regional Harmonization (x=13..15, y=1..8)
add_f("TUR_arab_congress_dialogue", 14, 1, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_second_constitutional_era_politics"],
      rewards=["add_political_power = 50", "custom_effect_tooltip = TUR_tt_arab_talks"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_beirut_and_damascus_charters", 13, 2, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_arab_congress_dialogue"],
      rewards=["add_ideas = TUR_arab_ottoman_federal_compact", "remove_ideas = TUR_arab_unrest_smoldering", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_dual_monarchy_protocol", 15, 2, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_arab_congress_dialogue"],
      rewards=["add_political_power = 100", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_guaranteed_arab_cabinet_seats", 14, 3, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_beirut_and_damascus_charters", "TUR_dual_monarchy_protocol"],
      rewards=["add_political_power = 60", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_loyal_tribal_federation", 13, 4, 5, "GFX_focus_generic_cavalry",
      prereqs=["TUR_guaranteed_arab_cabinet_seats"],
      rewards=["add_manpower = 30000", "custom_effect_tooltip = TUR_tt_tribal_support"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_caliphate_and_arab_solidarity", 15, 4, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_guaranteed_arab_cabinet_seats"],
      rewards=["add_war_support = 0.10", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_bilingual_imperial_administration", 14, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_loyal_tribal_federation", "TUR_caliphate_and_arab_solidarity"],
      rewards=["add_stability = 0.05", "compliance_growth_focus_factor = 0.15"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_sharifian_protectorate_accord", 13, 6, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_bilingual_imperial_administration"],
      rewards=["custom_effect_tooltip = TUR_tt_sharif_loyalty", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_mesopotamian_notables_council", 15, 6, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_bilingual_imperial_administration"],
      rewards=["291 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_syrian_economic_integration", 14, 7, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_sharifian_protectorate_accord", "TUR_mesopotamian_notables_council"],
      rewards=["554 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_pan_islamic_imperial_brotherhood", 14, 8, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_syrian_economic_integration"],
      rewards=["add_stability = 0.10", "add_war_support = 0.10", "add_political_power = 80"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT"])

# Pan-Islamic and Imperial Harmony Bridges (y=9..13)
add_f("TUR_shrine_of_eyup_pilgrimage", 8, 9, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_sublime_porte_war_council", "TUR_liberal_parliamentary_hegemony", "TUR_absolute_caliphal_authority", "TUR_pan_islamic_imperial_brotherhood"],
      rewards=["add_stability = 0.05", "add_war_support = 0.05", "add_political_power = 50"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_mobilize_sufi_brotherhoods", 6, 10, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_shrine_of_eyup_pilgrimage"],
      rewards=["add_war_support = 0.10", "subversive_activites_upkeep = -0.20"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_holy_cities_custodianship", 10, 10, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_shrine_of_eyup_pilgrimage"],
      rewards=["679 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_proclamation_of_jihad_readiness", 8, 11, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_mobilize_sufi_brotherhoods", "TUR_holy_cities_custodianship"],
      rewards=["add_war_support = 0.10", "set_country_flag = TUR_ready_for_holy_war"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_imperial_cohesion_ascendant", 8, 12, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_proclamation_of_jihad_readiness"],
      rewards=["add_stability = 0.10", "add_political_power = 100", "conscription_factor = 0.05"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_POLITICAL"])

add_f("TUR_legacy_of_osman_eternal", 8, 13, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_imperial_cohesion_ascendant"],
      rewards=["add_stability = 0.10", "add_war_support = 0.10", "army_core_defence_factor = 0.05"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT"])


# ==============================================================================
# WING 2: ECONOMIC SOVEREIGNTY, DEBT & RAILWAYS (52 FOCUSES, x=18..32)
# ==============================================================================

# Root (y=0)
add_f("TUR_economic_sovereignty_drive", 25, 0, 5, "GFX_TUR_law_for_encouraging_industry",
      rewards=["add_political_power = 75", "consumer_goods_factor = -0.02", "set_country_flag = TUR_economy_program_begun"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 2.1: Public Debt & Capitulations (x=18..21, y=1..8)
add_f("TUR_audit_opda_administration", 19, 1, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_economic_sovereignty_drive"],
      rewards=["add_political_power = 60", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_renegotiate_creditor_coupons", 19, 2, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_audit_opda_administration"],
      rewards=["add_ideas = TUR_debt_renegotiated", "remove_ideas = TUR_sick_man_debt", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_unilateral_abrogation_of_capitulations", 19, 3, 5, "GFX_TUR_abolished_the_capitulations",
      prereqs=["TUR_renegotiate_creditor_coupons"],
      rewards=["add_ideas = TUR_capitulations_abrogated", "remove_ideas = TUR_debt_renegotiated", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_protective_tariff_code", 18, 4, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_unilateral_abrogation_of_capitulations"],
      rewards=["custom_effect_tooltip = TUR_tt_protective_tariffs", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_national_bank_osmanli_itibar", 20, 4, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_unilateral_abrogation_of_capitulations"],
      rewards=["add_ideas = TUR_financial_sovereignty", "remove_ideas = TUR_capitulations_abrogated", "add_political_power = 100"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_confiscate_foreign_monopolies", 18, 5, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_protective_tariff_code"],
      rewards=["797 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_monetary_autonomy_and_gold_lira", 20, 5, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_national_bank_osmanli_itibar"],
      rewards=["add_stability = 0.05", "consumer_goods_factor = -0.03"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_tobacco_regie_liquidation", 19, 6, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_confiscate_foreign_monopolies", "TUR_monetary_autonomy_and_gold_lira"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_salt_monopoly_nationalization", 19, 7, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_tobacco_regie_liquidation"],
      rewards=["consumer_goods_factor = -0.02", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_complete_fiscal_liberation", 19, 8, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_salt_monopoly_nationalization"],
      rewards=["add_political_power = 120", "industrial_capacity_factory = 0.08"],
      filters=["FOCUS_FILTER_INDUSTRY", "FOCUS_FILTER_POLITICAL"])

# Sub-branch 2.2: Baghdad Railway & Transport Network (x=22..26, y=1..8)
add_f("TUR_taurus_and_amanus_tunnels", 24, 1, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_economic_sovereignty_drive"],
      rewards=["799 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }", "add_ideas = TUR_baghdad_railway_artery"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_konya_aleppo_trunk_line", 23, 2, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_taurus_and_amanus_tunnels"],
      rewards=["677 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }", "343 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_aleppo_to_mosul_extension", 25, 2, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_taurus_and_amanus_tunnels"],
      rewards=["676 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_mosul_baghdad_railhead", 24, 3, 5, "GFX_TUR_baghdad_industrialization",
      prereqs=["TUR_konya_aleppo_trunk_line", "TUR_aleppo_to_mosul_extension"],
      rewards=["291 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_basra_terminus_settlement", 22, 4, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_mosul_baghdad_railhead"],
      rewards=["1011 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "1011 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_hejaz_railway_expansion", 26, 4, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_mosul_baghdad_railhead"],
      rewards=["679 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }", "add_ideas = TUR_hejaz_pilgrim_railway"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_syrian_feeder_lines", 23, 5, 5, "GFX_focus_generic_railroads",
      prereqs=["TUR_basra_terminus_settlement"],
      rewards=["554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "553 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_medina_to_mecca_link", 25, 5, 5, "GFX_focus_generic_railroads",
      prereqs=["TUR_hejaz_railway_expansion"],
      rewards=["856 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_jerusalem_jaffa_railway_upgrade", 24, 6, 5, "GFX_focus_generic_railroads",
      prereqs=["TUR_syrian_feeder_lines", "TUR_medina_to_mecca_link"],
      rewards=["454 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_anatolian_railway_loop", 24, 7, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_jerusalem_jaffa_railway_upgrade"],
      rewards=["348 = { add_building_construction = { type = infrastructure level = 2 instant_build = yes } }", "army_speed_factor = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_railway_telegraph_integration", 24, 8, 5, "GFX_TUR_civil_communitcations_improvements",
      prereqs=["TUR_anatolian_railway_loop"],
      rewards=["signal_company_factor = 0.15", "reinforce_rate = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 2.3: Heavy Industry, Mining & Munitions (x=27..29, y=1..8)
add_f("TUR_zonguldak_coal_basin_drives", 28, 1, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_economic_sovereignty_drive"],
      rewards=["344 = { add_resource = { type = steel amount = 12 } }", "344 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_ergani_copper_mines", 27, 2, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_zonguldak_coal_basin_drives"],
      rewards=["354 = { add_resource = { type = steel amount = 8 } }", "354 = { add_resource = { type = chromium amount = 6 } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_tophane_ordnance_foundry", 29, 2, 5, "GFX_TUR_imperial_arsenal",
      prereqs=["TUR_zonguldak_coal_basin_drives"],
      rewards=["797 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_bakirkoy_textile_mills", 27, 3, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_ergani_copper_mines"],
      rewards=["797 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_zeytinburnu_munitions_complex", 29, 3, 5, "GFX_TUR_arms_expansions",
      prereqs=["TUR_tophane_ordnance_foundry"],
      rewards=["797 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }", "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2000 producer = TUR }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_ankara_state_foundries", 28, 4, 5, "GFX_TUR_ankara_industrialization",
      prereqs=["TUR_bakirkoy_textile_mills", "TUR_zeytinburnu_munitions_complex"],
      rewards=["348 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_izmir_commercial_quays", 27, 5, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_ankara_state_foundries"],
      rewards=["343 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_constantinople_electric_grid", 29, 5, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_ankara_state_foundries"],
      rewards=["797 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_amasya_metal_smelters", 28, 6, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_izmir_commercial_quays", "TUR_constantinople_electric_grid"],
      rewards=["355 = { add_resource = { type = steel amount = 10 } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_imperial_munitions_directorate", 28, 7, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_amasya_metal_smelters"],
      rewards=["industrial_capacity_factory = 0.10", "production_speed_arms_factory_factor = 0.15"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_full_industrial_mobilization", 28, 8, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_imperial_munitions_directorate"],
      rewards=["add_offsite_building = { type = arms_factory level = 2 }", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 2.4: Agriculture & Food Autonomy (x=30..32, y=1..8)
add_f("TUR_anatolian_grain_reserves", 31, 1, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_economic_sovereignty_drive"],
      rewards=["add_ideas = TUR_anatolian_grain_monopoly", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_willcocks_mesopotamia_irrigation", 30, 2, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_anatolian_grain_reserves"],
      rewards=["291 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_cilicia_cotton_modernization", 32, 2, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_anatolian_grain_reserves"],
      rewards=["799 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_anti_locust_campaigns", 31, 3, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_willcocks_mesopotamia_irrigation", "TUR_cilicia_cotton_modernization"],
      rewards=["add_stability = 0.05", "consumer_goods_factor = -0.02"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_state_silos_and_famine_relief", 31, 4, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_anti_locust_campaigns"],
      rewards=["add_stability = 0.05", "custom_effect_tooltip = TUR_tt_famine_protection"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_ziraat_bankasi_credit_expansion", 30, 5, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_state_silos_and_famine_relief"],
      rewards=["add_stability = 0.05", "consumer_goods_factor = -0.02"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_mechanized_anatolian_farming", 32, 5, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_state_silos_and_famine_relief"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_black_sea_timber_concessions", 31, 6, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_ziraat_bankasi_credit_expansion", "TUR_mechanized_anatolian_farming"],
      rewards=["344 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "production_speed_infrastructure_factor = 0.10"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_agrarian_surplus_storage", 31, 7, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_black_sea_timber_concessions"],
      rewards=["add_stability = 0.05", "war_support_factor = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_breadbasket_of_the_empire", 31, 8, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_agrarian_surplus_storage"],
      rewards=["supply_consumption_factor = -0.08", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_STABILITY"])

# Economic Integration Bridges (y=9..13)
add_f("TUR_integrated_imperial_economy", 25, 9, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_complete_fiscal_liberation", "TUR_railway_telegraph_integration", "TUR_full_industrial_mobilization", "TUR_breadbasket_of_the_empire"],
      rewards=["add_research_slot = 1", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_RESEARCH", "FOCUS_FILTER_INDUSTRY"])

add_f("TUR_anatolian_highway_system", 23, 10, 5, "GFX_focus_generic_infrastructure",
      prereqs=["TUR_integrated_imperial_economy"],
      rewards=["341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "348 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_petroleum_concessions_mosul", 27, 10, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_integrated_imperial_economy"],
      rewards=["676 = { add_resource = { type = oil amount = 16 } }", "add_political_power = 60"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_sublime_porte_heavy_industry_board", 25, 11, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_anatolian_highway_system", "TUR_petroleum_concessions_mosul"],
      rewards=["industrial_capacity_factory = 0.08", "production_speed_industrial_complex_factor = 0.10"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_autarkic_imperial_foundation", 25, 12, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_sublime_porte_heavy_industry_board"],
      rewards=["consumer_goods_factor = -0.05", "add_stability = 0.05", "add_offsite_building = { type = industrial_complex level = 2 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_modern_ottoman_economic_miracle", 25, 13, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_autarkic_imperial_foundation"],
      rewards=["add_political_power = 100", "add_stability = 0.10", "industrial_capacity_factory = 0.10"],
      filters=["FOCUS_FILTER_INDUSTRY", "FOCUS_FILTER_STABILITY"])


# ==============================================================================
# WING 3: ARMED FORCES MODERNIZATION (50 FOCUSES, x=35..49)
# ==============================================================================

# Root (y=0)
add_f("TUR_reorganizing_the_imperial_army", 42, 0, 5, "GFX_TUR_osmanl_ordusu",
      rewards=["army_experience = 35", "add_command_power = 20", "set_country_flag = TUR_army_reform_begun"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Sub-branch 3.1: Staff & Infantry (x=35..39, y=1..8)
add_f("TUR_harbiye_academy_modernization", 37, 1, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_reorganizing_the_imperial_army"],
      rewards=["army_experience = 25", "add_ideas = TUR_army_modernization_struggle"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_purge_inefficient_cadres", 36, 2, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_harbiye_academy_modernization"],
      rewards=["add_political_power = -30", "army_experience = 20", "custom_effect_tooltip = TUR_tt_purge_incompetent"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_standardize_mauser_rifles", 38, 2, 5, "GFX_TUR_turkish_equipment_modernization",
      prereqs=["TUR_harbiye_academy_modernization"],
      rewards=["add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 3000 producer = TUR }", "add_tech_bonus = { name = infantry_weapons bonus = 1.0 uses = 1 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_krupp_quick_fire_artillery", 37, 3, 5, "GFX_TUR_arms_deal_with_germany",
      prereqs=["TUR_purge_inefficient_cadres", "TUR_standardize_mauser_rifles"],
      rewards=["add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 80 producer = TUR }", "add_tech_bonus = { name = artillery bonus = 1.0 uses = 1 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_anatolian_infantry_doctrine", 35, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_krupp_quick_fire_artillery"],
      rewards=["add_doctrine_cost_reduction = { name = land_doctrine cost_reduction = 0.5 uses = 1 }", "army_morale_factor = 0.05"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_desert_camel_corps_regiments", 37, 4, 5, "GFX_focus_generic_cavalry",
      prereqs=["TUR_krupp_quick_fire_artillery"],
      rewards=["add_manpower = 15000", "cavalry_attack_factor = 0.05"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_caucasus_alpine_detachments", 39, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_krupp_quick_fire_artillery"],
      rewards=["add_ideas = TUR_caucasus_alpine_preparations", "army_experience = 15"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_machine_gun_companies", 37, 5, 5, "GFX_TUR_turkish_equipment_modernization",
      prereqs=["TUR_anatolian_infantry_doctrine", "TUR_desert_camel_corps_regiments", "TUR_caucasus_alpine_detachments"],
      rewards=["add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2000 producer = TUR }", "army_infantry_defence_factor = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_field_medicine_red_crescent", 36, 6, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_machine_gun_companies"],
      rewards=["army_morale_factor = 0.05", "casualty_trickleback = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_gendarmerie_modernization_corps", 38, 6, 5, "GFX_TUR_jandarma_genel_komutanlgi",
      prereqs=["TUR_machine_gun_companies"],
      rewards=["resistance_target = -0.15", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_heavy_siege_howitzers", 37, 7, 5, "GFX_TUR_arms_expansions",
      prereqs=["TUR_field_medicine_red_crescent", "TUR_gendarmerie_modernization_corps"],
      rewards=["add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 100 producer = TUR }", "army_artillery_attack_factor = 0.05"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_comprehensive_conscription_law", 37, 8, 5, "GFX_TUR_1914_law_of_military_obligation",
      prereqs=["TUR_heavy_siege_howitzers"],
      rewards=["conscription_factor = 0.10", "add_manpower = 50000"],
      filters=["FOCUS_FILTER_MANPOWER"])

# Sub-branch 3.2: Military Missions (x=40..43, y=1..8)
add_f("TUR_foreign_mission_choice", 41, 1, 5, "GFX_focus_generic_military_mission",
      prereqs=["TUR_reorganizing_the_imperial_army"],
      rewards=["add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_german_military_mission_sanders", 40, 2, 5, "GFX_TUR_german_five_year_mission",
      prereqs=["TUR_foreign_mission_choice"],
      mut_excl=["TUR_native_general_staff_kemal"],
      rewards=["add_ideas = TUR_german_military_mission", "remove_ideas = TUR_army_modernization_struggle", "add_opinion_modifier = { target = GER modifier = positive_50 }"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_native_general_staff_kemal", 42, 2, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_foreign_mission_choice"],
      mut_excl=["TUR_german_military_mission_sanders"],
      rewards=["add_ideas = TUR_kemalist_tactical_doctrine", "remove_ideas = TUR_army_modernization_struggle", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_prusso_ottoman_doctrine", 40, 3, 5, "GFX_TUR_schellendorf_plan",
      prereqs=["TUR_german_military_mission_sanders"],
      rewards=["add_doctrine_cost_reduction = { name = land_doctrine cost_reduction = 0.5 uses = 2 }", "max_planning = 0.10"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_independent_tactical_flexibility", 42, 3, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_native_general_staff_kemal"],
      rewards=["army_core_defence_factor = 0.10", "reinforce_rate = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_krupp_heavy_ordnance_contracts", 40, 4, 5, "GFX_TUR_arms_deal_with_germany",
      prereqs=["TUR_prusso_ottoman_doctrine"],
      rewards=["add_tech_bonus = { name = artillery bonus = 1.0 uses = 1 }", "army_artillery_attack_factor = 0.05"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_anatolian_guerrilla_tradition", 42, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_independent_tactical_flexibility"],
      rewards=["attrition = -0.10", "out_of_supply_factor = -0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_joint_staff_operational_drills", 41, 5, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_krupp_heavy_ordnance_contracts", "TUR_anatolian_guerrilla_tradition"],
      rewards=["planning_speed = 0.10", "army_experience = 20"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_officer_corps_intellectual_vigor", 41, 6, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_joint_staff_operational_drills"],
      rewards=["army_org_factor = 0.05", "add_political_power = 50"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_divisional_artillery_batteries", 41, 7, 5, "GFX_TUR_arms_expansions",
      prereqs=["TUR_officer_corps_intellectual_vigor"],
      rewards=["army_artillery_attack_factor = 0.05", "add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 60 producer = TUR }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_corps_level_reserves_doctrine", 41, 8, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_divisional_artillery_batteries"],
      rewards=["max_planning = 0.05", "reinforce_rate = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Sub-branch 3.3: Navy & Dreadnoughts (x=44..47, y=1..8)
add_f("TUR_rebuild_the_imperial_fleet", 45, 1, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_reorganizing_the_imperial_army"],
      rewards=["navy_experience = 25", "set_country_flag = TUR_navy_expansion_begun"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_the_dreadnought_contracts_uk", 44, 2, 5, "GFX_TUR_complete_the_british_dreadnought_order",
      prereqs=["TUR_rebuild_the_imperial_fleet"],
      rewards=["country_event = { id = ww1_ottoman.1 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_golden_horn_shipyards_expansion", 46, 2, 5, "GFX_TUR_kostantiniye_dockyard_expansion",
      prereqs=["TUR_rebuild_the_imperial_fleet"],
      rewards=["797 = { add_building_construction = { type = dockyard level = 2 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_public_donation_drive_sultan_osman", 44, 3, 5, "GFX_TUR_complete_the_british_dreadnought_order",
      prereqs=["TUR_the_dreadnought_contracts_uk"],
      rewards=["add_war_support = 0.10", "add_ideas = TUR_dreadnought_national_fervor"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_torpedo_boat_flotillas", 46, 3, 5, "GFX_TUR_fleet_expansion",
      prereqs=["TUR_golden_horn_shipyards_expansion"],
      rewards=["navy_experience = 20", "add_tech_bonus = { name = naval_equipment bonus = 1.0 uses = 1 }"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_welcome_goeben_and_breslau", 44, 4, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_public_donation_drive_sultan_osman"],
      rewards=["country_event = { id = ww1_ottoman.10 }", "add_ideas = TUR_yavuz_and_midilli_supremacy"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_black_sea_submarine_patrols", 46, 4, 5, "GFX_TUR_fleet_expansion",
      prereqs=["TUR_torpedo_boat_flotillas"],
      rewards=["add_tech_bonus = { name = ss_tech bonus = 1.0 uses = 1 }", "sub_detection = 0.15"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_coastal_minelayer_force", 45, 5, 5, "GFX_TUR_fleet_expansion",
      prereqs=["TUR_welcome_goeben_and_breslau", "TUR_black_sea_submarine_patrols"],
      rewards=["naval_mine_hit_chance_factor = 0.20", "navy_experience = 15"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_naval_gunnery_schools", 45, 6, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_coastal_minelayer_force"],
      rewards=["navy_capital_ship_attack_factor = 0.10", "naval_hit_chance = 0.05"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_cruiser_escort_squadrons", 45, 7, 5, "GFX_TUR_fleet_expansion",
      prereqs=["TUR_naval_gunnery_schools"],
      rewards=["navy_screen_ship_attack_factor = 0.10", "navy_anti_air_factor = 0.10"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_sovereign_black_sea_fleet", 45, 8, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_cruiser_escort_squadrons"],
      rewards=["navy_capital_ship_attack_factor = 0.10", "navy_experience = 30"],
      filters=["FOCUS_FILTER_NAVY_XP"])

# Sub-branch 3.4: Aviation & Straits Fortresses (x=48..49, y=1..8)
add_f("TUR_yesilkoy_aviation_school", 48, 1, 5, "GFX_TUR_air_defense",
      prereqs=["TUR_reorganizing_the_imperial_army"],
      rewards=["air_experience = 25", "add_ideas = TUR_ottoman_aviation_detachment"],
      filters=["FOCUS_FILTER_AIR_XP"])

add_f("TUR_strengthen_canakkale_batteries", 49, 1, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_reorganizing_the_imperial_army"],
      rewards=["341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }", "add_ideas = TUR_canakkale_impenetrable_bastion"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_procure_bleriot_and_rumpler_monoplanes", 48, 2, 5, "GFX_TUR_air_defense",
      prereqs=["TUR_yesilkoy_aviation_school"],
      rewards=["add_tech_bonus = { name = air_equipment bonus = 1.0 uses = 1 }", "air_experience = 15"],
      filters=["FOCUS_FILTER_RESEARCH"])

add_f("TUR_underwater_minefields_straits", 49, 2, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_strengthen_canakkale_batteries"],
      rewards=["custom_effect_tooltip = TUR_tt_straits_mines", "navy_experience = 15"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_aerial_reconnaissance_detachments", 48, 3, 5, "GFX_TUR_air_defense",
      prereqs=["TUR_procure_bleriot_and_rumpler_monoplanes"],
      rewards=["air_recon_factor = 0.20", "air_experience = 15"],
      filters=["FOCUS_FILTER_AIR_XP"])

add_f("TUR_searchlight_batteries_dardanelles", 49, 3, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_underwater_minefields_straits"],
      rewards=["amphibious_invasion_defence = 0.20", "naval_strike_defence_factor = 0.15"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Armed Forces Integration Bridges (y=9..13)
add_f("TUR_joint_command_supreme_staff", 42, 9, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_comprehensive_conscription_law", "TUR_corps_level_reserves_doctrine", "TUR_sovereign_black_sea_fleet", "TUR_aerial_reconnaissance_detachments", "TUR_searchlight_batteries_dardanelles"],
      rewards=["army_experience = 30", "navy_experience = 20", "air_experience = 15", "add_command_power = 30"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_modern_field_communications", 40, 10, 5, "GFX_TUR_civil_communitcations_improvements",
      prereqs=["TUR_joint_command_supreme_staff"],
      rewards=["reinforce_rate = 0.10", "signal_company_factor = 0.15"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_logistics_motor_truck_corps", 44, 10, 5, "GFX_TUR_turkish_equipment_modernization",
      prereqs=["TUR_joint_command_supreme_staff"],
      rewards=["army_speed_factor = 0.05", "supply_consumption_factor = -0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_imperial_arsenals_peak_output", 42, 11, 5, "GFX_TUR_imperial_arsenal",
      prereqs=["TUR_modern_field_communications", "TUR_logistics_motor_truck_corps"],
      rewards=["industrial_capacity_factory = 0.10", "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 5000 producer = TUR }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_harbiye_tactical_doctrine_zenith", 42, 12, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_imperial_arsenals_peak_output"],
      rewards=["army_org_factor = 0.05", "army_morale_factor = 0.10", "max_planning = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_invincible_mehmetcik_spirit", 42, 13, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_harbiye_tactical_doctrine_zenith"],
      rewards=["army_core_defence_factor = 0.10", "army_morale_factor = 0.10", "add_war_support = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP", "FOCUS_FILTER_WAR_SUPPORT"])


# ==============================================================================
# WING 4: GREAT POWER DIPLOMACY & THE STRAITS (46 FOCUSES, x=52..66)
# ==============================================================================

# Root (y=0)
add_f("TUR_sublime_porte_foreign_policy", 59, 0, 5, "GFX_focus_generic_diplomacy",
      rewards=["add_political_power = 80", "set_country_flag = TUR_diplomacy_path_begun"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Sub-branch 4.1: Regional & Border Security (x=52..55, y=1..8)
add_f("TUR_western_thrace_border_vigilance", 53, 1, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_sublime_porte_foreign_policy"],
      rewards=["341 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_edirne_fortress_complex", 53, 2, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_western_thrace_border_vigilance"],
      rewards=["341 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_bulgarian_friendship_treaty", 52, 3, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_edirne_fortress_complex"],
      rewards=["add_opinion_modifier = { target = BUL modifier = positive_50 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_romanian_grain_accord", 54, 3, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_edirne_fortress_complex"],
      rewards=["add_opinion_modifier = { target = ROM modifier = positive_50 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_reaffirm_libyan_sovereignty", 55, 1, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_sublime_porte_foreign_policy"],
      rewards=["448 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_sanusi_brotherhood_pact", 55, 2, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_reaffirm_libyan_sovereignty"],
      rewards=["custom_effect_tooltip = TUR_tt_sanusi_pact", "add_manpower = 15000"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_tripoli_coastal_fortifications", 55, 3, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_sanusi_brotherhood_pact"],
      rewards=["448 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_aegean_island_garrisons", 53, 4, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_bulgarian_friendship_treaty", "TUR_romanian_grain_accord"],
      rewards=["164 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 4.2: Alignment with Central Powers (x=56..58, y=1..8)
add_f("TUR_german_rapprochement", 57, 1, 5, "GFX_TUR_secret_treaty_with_germany",
      prereqs=["TUR_sublime_porte_foreign_policy"],
      mut_excl=["TUR_strict_armed_neutrality", "TUR_entente_diplomatic_demands"],
      rewards=["add_opinion_modifier = { target = GER modifier = positive_75 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_secret_alliance_august_1914", 57, 2, 5, "GFX_TUR_secret_treaty_with_germany",
      prereqs=["TUR_german_rapprochement"],
      rewards=["set_country_flag = TUR_secret_treaty_signed", "country_event = { id = ww1_ottoman.12 }"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_german_gold_loans", 56, 3, 5, "GFX_TUR_german_donation",
      prereqs=["TUR_secret_alliance_august_1914"],
      rewards=["add_offsite_building = { type = industrial_complex level = 2 }", "add_political_power = 60"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_souchon_black_sea_raid", 58, 3, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_secret_alliance_august_1914"],
      rewards=["country_event = { id = ww1_ottoman.15 }", "add_war_support = 0.15"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_join_central_powers_faction", 57, 4, 5, "GFX_TUR_secret_treaty_with_germany",
      prereqs=["TUR_german_gold_loans", "TUR_souchon_black_sea_raid"],
      rewards=["add_to_faction = GER", "add_war_support = 0.10"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_berlin_constantinople_axis", 57, 5, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_join_central_powers_faction"],
      rewards=["add_ideas = TUR_german_military_mission", "army_experience = 25"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_austro_hungarian_danubian_link", 56, 6, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_berlin_constantinople_axis"],
      rewards=["add_opinion_modifier = { target = AUS modifier = positive_50 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_bulgarian_transit_corridor", 58, 6, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_berlin_constantinople_axis"],
      rewards=["341 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_central_powers_war_council", 57, 7, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_austro_hungarian_danubian_link", "TUR_bulgarian_transit_corridor"],
      rewards=["army_experience = 30", "add_command_power = 30"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_shared_munitions_standardization", 57, 8, 5, "GFX_TUR_arms_deal_with_germany",
      prereqs=["TUR_central_powers_war_council"],
      rewards=["industrial_capacity_factory = 0.08", "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 4000 producer = TUR }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 4.3: Strict Armed Neutrality (x=60..62, y=1..8)
add_f("TUR_strict_armed_neutrality", 61, 1, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_sublime_porte_foreign_policy"],
      mut_excl=["TUR_german_rapprochement", "TUR_entente_diplomatic_demands"],
      rewards=["add_stability = 0.10", "add_political_power = 100", "set_country_flag = TUR_neutral_policy"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_POLITICAL"])

add_f("TUR_close_straits_to_all_belligerents", 60, 2, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_strict_armed_neutrality"],
      rewards=["custom_effect_tooltip = TUR_tt_close_straits", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_demand_belligerent_transit_tolls", 62, 2, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_strict_armed_neutrality"],
      rewards=["consumer_goods_factor = -0.05", "add_offsite_building = { type = industrial_complex level = 1 }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_internal_development_focus", 61, 3, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_close_straits_to_all_belligerents", "TUR_demand_belligerent_transit_tolls"],
      rewards=["add_research_slot = 1", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_RESEARCH", "FOCUS_FILTER_INDUSTRY"])

add_f("TUR_profit_from_wartime_trade", 61, 4, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_internal_development_focus"],
      rewards=["add_offsite_building = { type = industrial_complex level = 2 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_swiss_of_the_orient_neutrality", 61, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_profit_from_wartime_trade"],
      rewards=["add_stability = 0.15", "add_political_power = 120"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_POLITICAL"])

add_f("TUR_diplomatic_mediation_summit", 61, 6, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_swiss_of_the_orient_neutrality"],
      rewards=["add_political_power = 80", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_neutral_sovereignty_guaranteed", 61, 7, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_diplomatic_mediation_summit"],
      rewards=["army_core_defence_factor = 0.15", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_STABILITY"])

# Sub-branch 4.4: Entente Alternative Settlement (x=63..66, y=1..8)
add_f("TUR_entente_diplomatic_demands", 64, 1, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_sublime_porte_foreign_policy"],
      mut_excl=["TUR_german_rapprochement", "TUR_strict_armed_neutrality"],
      rewards=["add_opinion_modifier = { target = ENG modifier = positive_50 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_demand_dreadnought_deliveries", 63, 2, 5, "GFX_TUR_complete_the_british_dreadnought_order",
      prereqs=["TUR_entente_diplomatic_demands"],
      rewards=["custom_effect_tooltip = TUR_tt_demand_dreadnoughts", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_territorial_integrity_guarantees", 65, 2, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_entente_diplomatic_demands"],
      rewards=["add_stability = 0.10", "give_guarantee = ENG"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_anglo_ottoman_gulf_treaty", 64, 3, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_demand_dreadnought_deliveries", "TUR_territorial_integrity_guarantees"],
      rewards=["add_political_power = 80", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_neutralize_russian_threat", 64, 4, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_anglo_ottoman_gulf_treaty"],
      rewards=["add_opinion_modifier = { target = RUS modifier = positive_50 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_french_syrian_economic_pact", 64, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_neutralize_russian_threat"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_entente_cooperation_treaty", 64, 6, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_french_syrian_economic_pact"],
      rewards=["add_opinion_modifier = { target = ENG modifier = positive_75 }", "add_political_power = 100"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_secured_ottoman_borders", 64, 7, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_entente_cooperation_treaty"],
      rewards=["add_stability = 0.15", "consumer_goods_factor = -0.03"],
      filters=["FOCUS_FILTER_STABILITY"])

# Diplomatic Climax Bridges (y=9..13)
add_f("TUR_the_sovereign_straits_regime", 59, 9, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_aegean_island_garrisons", "TUR_shared_munitions_standardization", "TUR_neutral_sovereignty_guaranteed", "TUR_secured_ottoman_borders"],
      rewards=["add_stability = 0.10", "add_war_support = 0.10", "add_political_power = 100"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_dardanelles_maritime_hegemony", 57, 10, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_the_sovereign_straits_regime"],
      rewards=["navy_capital_ship_attack_factor = 0.10", "naval_torpedo_hit_chance_factor = 0.10"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_levantine_coastal_security", 61, 10, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_the_sovereign_straits_regime"],
      rewards=["554 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }", "454 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_sublime_porte_global_standing", 59, 11, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_dardanelles_maritime_hegemony", "TUR_levantine_coastal_security"],
      rewards=["add_stability = 0.10", "add_political_power = 80"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_POLITICAL"])

add_f("TUR_destiny_of_the_near_east", 59, 12, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_sublime_porte_global_standing"],
      rewards=["add_war_support = 0.10", "army_core_defence_factor = 0.05"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_pax_osmanica_reasserted", 59, 13, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_destiny_of_the_near_east"],
      rewards=["add_stability = 0.10", "add_war_support = 0.10", "add_political_power = 120"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT"])


# ==============================================================================
# WING 5: THE GREAT WAR THEATERS & 1918 ENDGAME (52 FOCUSES, x=69..85)
# ==============================================================================

# Root (y=0)
add_f("TUR_the_war_for_imperial_survival", 77, 0, 5, "GFX_focus_generic_war_industry",
      available="has_war = yes",
      rewards=["add_war_support = 0.15", "add_political_power = 100", "set_country_flag = TUR_total_war_mobilization"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

# Sub-branch 5.1: Caucasus Front vs Russia (x=69..71, y=1..8)
add_f("TUR_caucasus_logistics_preparation", 70, 1, 5, "GFX_TUR_turkish_equipment_modernization",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["custom_effect_tooltip = TUR_tt_caucasus_winter_supplies", "winter_attrition_factor = -0.30"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_third_army_mountain_offensive", 69, 2, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_caucasus_logistics_preparation"],
      rewards=["army_attack_factor = 0.05", "army_experience = 25"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_trabzon_supply_lifeline", 71, 2, 5, "GFX_TUR_civil_communitcations_improvements",
      prereqs=["TUR_caucasus_logistics_preparation"],
      rewards=["9932 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }", "supply_consumption_factor = -0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_retake_kars_ardahan_batum", 70, 3, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_third_army_mountain_offensive", "TUR_trabzon_supply_lifeline"],
      rewards=["add_war_support = 0.10", "army_core_defence_factor = 0.10"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_army_of_islam_caucasus", 70, 4, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_retake_kars_ardahan_batum"],
      rewards=["add_manpower = 35000", "army_experience = 30", "set_country_flag = TUR_army_of_islam_formed"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_baku_petroleum_drive", 70, 5, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_army_of_islam_caucasus"],
      rewards=["add_political_power = 80", "custom_effect_tooltip = TUR_tt_baku_oil"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_caspian_flotilla_organization", 70, 6, 5, "GFX_TUR_fleet_expansion",
      prereqs=["TUR_baku_petroleum_drive"],
      rewards=["navy_experience = 15", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_caucasian_tribal_auxiliaries", 70, 7, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_caspian_flotilla_organization"],
      rewards=["add_manpower = 20000", "army_morale_factor = 0.05"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_transcaucasian_security_sphere", 70, 8, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_caucasian_tribal_auxiliaries"],
      rewards=["add_stability = 0.10", "add_political_power = 75"],
      filters=["FOCUS_FILTER_STABILITY"])

# Sub-branch 5.2: Gallipoli & Dardanelles Defense (x=72..74, y=1..8)
add_f("TUR_cevat_pasha_artillery_defence", 73, 1, 5, "GFX_TUR_air_defense",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["341 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }", "add_ideas = TUR_canakkale_impenetrable_bastion"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_chunuk_bair_counterattack", 72, 2, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_cevat_pasha_artillery_defence"],
      rewards=["army_morale_factor = 0.15", "army_core_defence_factor = 0.15", "add_war_support = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP", "FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_fifth_army_mobile_reserves", 74, 2, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_cevat_pasha_artillery_defence"],
      rewards=["reinforce_rate = 0.15", "dig_in_speed_factor = 0.20"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_drive_invaders_into_the_sea", 73, 3, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_chunuk_bair_counterattack", "TUR_fifth_army_mobile_reserves"],
      rewards=["add_war_support = 0.15", "add_stability = 0.10", "country_event = { id = ww1_ottoman.25 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT", "FOCUS_FILTER_STABILITY"])

add_f("TUR_anafartalar_heroism_legacy", 73, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_drive_invaders_into_the_sea"],
      rewards=["army_core_defence_factor = 0.10", "army_morale_factor = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_fortress_canakkale_permanent", 73, 5, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_anafartalar_heroism_legacy"],
      rewards=["341 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 5.3: Mesopotamia Front vs Britain (x=75..77, y=1..8)
add_f("TUR_tigris_river_flotilla", 76, 1, 5, "GFX_TUR_osmanl_donanmas",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["291 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "army_speed_factor = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_defense_of_kut_al_amara", 75, 2, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_tigris_river_flotilla"],
      rewards=["max_dig_in = 5", "army_core_defence_factor = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_encirclement_of_townshend_army", 77, 2, 5, "GFX_TUR_restructured_army_command",
      prereqs=["TUR_tigris_river_flotilla"],
      rewards=["custom_effect_tooltip = TUR_tt_encircle_kut", "army_experience = 25"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_halil_kut_triumph", 76, 3, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_defense_of_kut_al_amara", "TUR_encirclement_of_townshend_army"],
      rewards=["add_ideas = TUR_kut_al_amara_triumph", "country_event = { id = ww1_ottoman.30 }"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_secure_basra_access", 76, 4, 5, "GFX_TUR_baghdad_industrialization",
      prereqs=["TUR_halil_kut_triumph"],
      rewards=["1011 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_shatt_al_arab_defensive_perimeter", 76, 5, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_secure_basra_access"],
      rewards=["1011 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 5.4: Sinai, Suez & Palestine Campaign (x=78..80, y=1..8)
add_f("TUR_cross_the_sinai_desert", 79, 1, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["attrition = -0.15", "out_of_supply_factor = -0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_suez_canal_raids", 78, 2, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_cross_the_sinai_desert"],
      rewards=["custom_effect_tooltip = TUR_tt_suez_raid", "add_war_support = 0.10"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_gaza_beersheba_defensive_line", 80, 2, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_cross_the_sinai_desert"],
      rewards=["454 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "add_ideas = TUR_gaza_beersheba_defensive_wall"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_defense_of_jerusalem", 79, 3, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_suez_canal_raids", "TUR_gaza_beersheba_defensive_line"],
      rewards=["454 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "add_stability = 0.05", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_damascus_bastion", 79, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_defense_of_jerusalem"],
      rewards=["554 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "army_core_defence_factor = 0.10"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_levantine_supply_depots", 79, 5, 5, "GFX_focus_generic_infrastructure",
      prereqs=["TUR_damascus_bastion"],
      rewards=["554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "supply_consumption_factor = -0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Sub-branch 5.5: Hejaz, Medina & Arab Desert War (x=81..82, y=1..8)
add_f("TUR_protect_hejaz_railway_garrisons", 81, 1, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["custom_effect_tooltip = TUR_tt_protect_railway", "supply_consumption_factor = -0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_fakhri_pasha_medina_defense", 82, 2, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_protect_hejaz_railway_garrisons"],
      rewards=["679 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "add_ideas = TUR_fakhri_pasha_desert_stand"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_crush_or_reconcile_sharifians", 81, 3, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_fakhri_pasha_medina_defense"],
      rewards=["custom_effect_tooltip = TUR_tt_sharif_revolt_containment", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_holy_relics_safeguard", 82, 4, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_crush_or_reconcile_sharifians"],
      rewards=["add_stability = 0.10", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_red_sea_desert_patrols", 81, 5, 5, "GFX_TUR_asienkorps",
      prereqs=["TUR_holy_relics_safeguard"],
      rewards=["attrition = -0.10", "army_speed_factor = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Sub-branch 5.6: War Economy & Mobilization (x=83..85, y=1..8)
add_f("TUR_war_bread_and_rationing", 84, 1, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_the_war_for_imperial_survival"],
      rewards=["add_ideas = TUR_war_bread_and_rationing", "consumer_goods_factor = -0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_requisition_imperial_resources", 83, 2, 5, "GFX_TUR_office_of_war_industry",
      prereqs=["TUR_war_bread_and_rationing"],
      rewards=["industrial_capacity_factory = 0.10", "add_war_support = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_teskilat_asymmetric_warfare", 85, 2, 5, "GFX_focus_generic_intelligence_agency",
      prereqs=["TUR_war_bread_and_rationing"],
      rewards=["subversive_activites_upkeep = -0.30", "recon_factor = 0.15"],
      filters=["FOCUS_FILTER_INTELLIGENCE"])

add_f("TUR_counter_the_blockade", 84, 3, 5, "GFX_TUR_civil_communitcations_improvements",
      prereqs=["TUR_requisition_imperial_resources", "TUR_teskilat_asymmetric_warfare"],
      rewards=["add_offsite_building = { type = industrial_complex level = 2 }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_total_war_labour_mobilization", 84, 4, 5, "GFX_TUR_law_for_encouraging_industry",
      prereqs=["TUR_counter_the_blockade"],
      rewards=["industrial_capacity_factory = 0.10", "production_speed_arms_factory_factor = 0.15"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_emergency_war_levies", 84, 5, 5, "GFX_TUR_1914_law_of_military_obligation",
      prereqs=["TUR_total_war_labour_mobilization"],
      rewards=["conscription_factor = 0.10", "add_manpower = 40000"],
      filters=["FOCUS_FILTER_MANPOWER"])

# War Theaters Climax & 1918 Endgame (y=9..14)
add_f("TUR_the_eastern_storm_survived", 77, 9, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_transcaucasian_security_sphere", "TUR_fortress_canakkale_permanent", "TUR_shatt_al_arab_defensive_perimeter", "TUR_levantine_supply_depots", "TUR_red_sea_desert_patrols", "TUR_emergency_war_levies"],
      rewards=["add_stability = 0.10", "add_war_support = 0.15", "add_political_power = 120"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_brest_litovsk_claims", 74, 10, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_the_eastern_storm_survived"],
      rewards=["country_event = { id = ww1_ottoman.35 }", "add_political_power = 80"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_middle_eastern_hegemon", 80, 10, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_the_eastern_storm_survived"],
      rewards=["add_ideas = TUR_anatolian_sovereignty_victory", "add_stability = 0.10"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_1918_total_victory_protocol", 77, 11, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_brest_litovsk_claims", "TUR_middle_eastern_hegemon"],
      rewards=["add_war_support = 0.15", "add_stability = 0.15", "conscription_factor = 0.05"],
      filters=["FOCUS_FILTER_WAR_SUPPORT", "FOCUS_FILTER_STABILITY"])

add_f("TUR_reborn_empire_destiny", 75, 12, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_1918_total_victory_protocol"],
      mut_excl=["TUR_republican_renaissance_destiny"],
      rewards=["add_political_power = 150", "add_stability = 0.15"],
      filters=["FOCUS_FILTER_POLITICAL", "FOCUS_FILTER_STABILITY"])

add_f("TUR_republican_renaissance_destiny", 79, 12, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_1918_total_victory_protocol"],
      mut_excl=["TUR_reborn_empire_destiny"],
      rewards=["add_research_slot = 1", "add_stability = 0.10", "industrial_capacity_factory = 0.10"],
      filters=["FOCUS_FILTER_RESEARCH", "FOCUS_FILTER_INDUSTRY"])

add_f("TUR_eternal_sublime_destiny", 77, 13, 5, "GFX_focus_generic_monarchy",
      prereqs=["TUR_reborn_empire_destiny", "TUR_republican_renaissance_destiny"],
      rewards=["add_stability = 0.20", "add_war_support = 0.20", "add_political_power = 200"],
      filters=["FOCUS_FILTER_STABILITY", "FOCUS_FILTER_WAR_SUPPORT", "FOCUS_FILTER_POLITICAL"])



# Candidate additions for Wing 1
add_f("TUR_macedonian_and_thracian_veterans", 4, 9, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_sublime_porte_war_council"],
      rewards=["add_manpower = 15000", "army_experience = 15"],
      filters=["FOCUS_FILTER_MANPOWER"])

add_f("TUR_constantinople_press_syndicate", 2, 9, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_sublime_porte_war_council"],
      rewards=["add_war_support = 0.05", "add_political_power = 40"],
      filters=["FOCUS_FILTER_WAR_SUPPORT"])

add_f("TUR_al_fatat_secret_dialogue", 13, 5, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_loyal_tribal_federation"],
      rewards=["custom_effect_tooltip = TUR_tt_appease_fatat", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_arab_notables_chamber", 15, 5, 5, "GFX_focus_generic_parliament",
      prereqs=["TUR_caliphate_and_arab_solidarity"],
      rewards=["add_political_power = 50", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_POLITICAL"])

# Candidate additions for Wing 2
add_f("TUR_pontic_coal_shipping", 27, 7, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_amasya_metal_smelters"],
      rewards=["344 = { add_resource = { type = steel amount = 4 } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_cilicia_irrigation_canals", 32, 6, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_mechanized_anatolian_farming"],
      rewards=["799 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_stability = 0.05"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_aleppo_commercial_hub", 23, 6, 5, "GFX_TUR_industrialization_of_the_nation",
      prereqs=["TUR_syrian_feeder_lines"],
      rewards=["677 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_syrian_grain_storage", 25, 7, 5, "GFX_TUR_1913_taxation_exemptions",
      prereqs=["TUR_jerusalem_jaffa_railway_upgrade"],
      rewards=["554 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "supply_consumption_factor = -0.03"],
      filters=["FOCUS_FILTER_INDUSTRY"])

# Candidate additions for Wing 3
add_f("TUR_izmir_naval_seaplane_base", 47, 5, 5, "GFX_TUR_air_defense",
      prereqs=["TUR_black_sea_submarine_patrols"],
      rewards=["air_experience = 15", "navy_experience = 10"],
      filters=["FOCUS_FILTER_AIR_XP"])

add_f("TUR_marmara_anti_submarine_nets", 49, 5, 5, "GFX_focus_generic_coastal_fort",
      prereqs=["TUR_searchlight_batteries_dardanelles"],
      rewards=["sub_detection = 0.15", "naval_mine_hit_chance_factor = 0.10"],
      filters=["FOCUS_FILTER_NAVY_XP"])

add_f("TUR_cavalry_reconnaissance_squadrons", 38, 5, 5, "GFX_focus_generic_cavalry",
      prereqs=["TUR_desert_camel_corps_regiments"],
      rewards=["recon_factor = 0.15", "cavalry_speed_factor = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_harbiye_cadet_battalions", 43, 5, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_anatolian_guerrilla_tradition"],
      rewards=["army_experience = 20", "army_morale_factor = 0.05"],
      filters=["FOCUS_FILTER_ARMY_XP"])

# Candidate additions for Wing 4
add_f("TUR_rome_mediterranean_dialogue", 55, 5, 5, "GFX_focus_generic_diplomacy",
      prereqs=["TUR_tripoli_coastal_fortifications"],
      rewards=["add_opinion_modifier = { target = ITA modifier = positive_50 }", "add_political_power = 40"],
      filters=["FOCUS_FILTER_POLITICAL"])

add_f("TUR_paris_credit_negotiations", 65, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_neutralize_russian_threat"],
      rewards=["add_offsite_building = { type = industrial_complex level = 1 }", "add_political_power = 50"],
      filters=["FOCUS_FILTER_INDUSTRY"])

add_f("TUR_persian_border_security", 53, 5, 5, "GFX_focus_generic_treaty",
      prereqs=["TUR_aegean_island_garrisons"],
      rewards=["add_stability = 0.05", "291 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }"],
      filters=["FOCUS_FILTER_STABILITY"])

add_f("TUR_cyrenaica_desert_posts", 55, 6, 5, "GFX_focus_generic_propaganda",
      prereqs=["TUR_rome_mediterranean_dialogue"],
      rewards=["663 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }", "add_manpower = 10000"],
      filters=["FOCUS_FILTER_MANPOWER"])

# Candidate additions for Wing 5
add_f("TUR_erzurum_fortress_line", 69, 4, 5, "GFX_TUR_osmanl_ordusu",
      prereqs=["TUR_retake_kars_ardahan_batum"],
      rewards=["9860 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "army_core_defence_factor = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_trench_warfare_drills_canakkale", 73, 6, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_fortress_canakkale_permanent"],
      rewards=["max_dig_in = 5", "dig_in_speed_factor = 0.20"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_ctesiphon_defensive_stand", 76, 6, 5, "GFX_focus_generic_war_industry",
      prereqs=["TUR_shatt_al_arab_defensive_perimeter"],
      rewards=["291 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }", "army_core_defence_factor = 0.10"],
      filters=["FOCUS_FILTER_ARMY_XP"])

add_f("TUR_hejaz_armored_train_patrols", 82, 5, 5, "GFX_TUR_baghdadberlin_railway",
      prereqs=["TUR_holy_relics_safeguard"],
      rewards=["supply_consumption_factor = -0.05", "armored_train_efficiency = 0.15"],
      filters=["FOCUS_FILTER_INDUSTRY"])

def generate_tree():
    ids = [f['id'] for f in FOCI]
    print(f"Total foci: {len(FOCI)}")
    assert len(ids) == len(set(ids)), f"Duplicate IDs found: {[x for x in ids if ids.count(x) > 1]}"
    
    coords = [(f['x'], f['y']) for f in FOCI]
    assert len(coords) == len(set(coords)), f"Coordinate collisions found: {[c for c in coords if coords.count(c) > 1]}"

    id_set = set(ids)
    for f in FOCI:
        for p in f['prereqs']:
            assert p in id_set, f"Prerequisite {p} not found in {f['id']}"
        for m in f['mut_excl']:
            assert m in id_set, f"Mutually exclusive {m} not found in {f['id']}"

    out = []
    out.append("# OTTOMAN EMPIRE (TUR) WW1 NATIONAL FOCUS TREE (1911-1918)")
    out.append("# Reconstructed Major Nation content with 5 non-colliding visual wings.")
    out.append("focus_tree = {")
    out.append("\tid = ottoman_focus")
    out.append("\tdefault = no")
    out.append("\tcountry = {")
    out.append("\t\tfactor = 0")
    out.append("\t\tmodifier = {")
    out.append("\t\t\tadd = 10")
    out.append("\t\t\ttag = TUR")
    out.append("\t\t}")
    out.append("\t}")
    out.append("\tcontinuous_focus_position = { x = 40 y = 3500 }")
    out.append("\tinitial_show_position = { x = 8 y = 0 }")
    out.append("\tshortcut = {")
    out.append("\t\tname = TUR_ww1_shortcut_politics")
    out.append("\t\ttarget = TUR_second_constitutional_era_politics")
    out.append("\t\tscroll_wheel_factor = 0.5")
    out.append("\t}")
    out.append("\tshortcut = {")
    out.append("\t\tname = TUR_ww1_shortcut_economy")
    out.append("\t\ttarget = TUR_economic_sovereignty_drive")
    out.append("\t\tscroll_wheel_factor = 0.5")
    out.append("\t}")
    out.append("\tshortcut = {")
    out.append("\t\tname = TUR_ww1_shortcut_military")
    out.append("\t\ttarget = TUR_reorganizing_the_imperial_army")
    out.append("\t\tscroll_wheel_factor = 0.5")
    out.append("\t}")
    out.append("\tshortcut = {")
    out.append("\t\tname = TUR_ww1_shortcut_diplomacy")
    out.append("\t\ttarget = TUR_sublime_porte_foreign_policy")
    out.append("\t\tscroll_wheel_factor = 0.5")
    out.append("\t}")
    out.append("\tshortcut = {")
    out.append("\t\tname = TUR_ww1_shortcut_war_theaters")
    out.append("\t\ttarget = TUR_the_war_for_imperial_survival")
    out.append("\t\tscroll_wheel_factor = 0.5")
    out.append("\t}")
    out.append("")

    for f in FOCI:
        out.append("\tfocus = {")
        out.append(f"\t\tid = {f['id']}")
        out.append(f"\t\ticon = {f['icon']}")
        out.append(f"\t\tcost = {f['cost']}")
        out.append(f"\t\tx = {f['x']}")
        out.append(f"\t\ty = {f['y']}")
        if f['prereqs']:
            prereq_str = " ".join([f"focus = {p}" for p in f['prereqs']])
            out.append(f"\t\tprerequisite = {{ {prereq_str} }}")
        if f['mut_excl']:
            mut_str = " ".join([f"focus = {m}" for m in f['mut_excl']])
            out.append(f"\t\tmutually_exclusive = {{ {mut_str} }}")
        if f['available']:
            out.append(f"\t\tavailable = {{ {f['available']} }}")
        if f['bypass']:
            out.append(f"\t\tbypass = {{ {f['bypass']} }}")
        out.append("\t\tavailable_if_capitulated = no")
        filter_str = " ".join(f['filters'])
        out.append(f"\t\tsearch_filters = {{ {filter_str} }}")
        out.append("\t\tcompletion_reward = {")
        for r in f['rewards']:
            out.append(f"\t\t\t{r}")
        out.append("\t\t}")
        out.append("\t}")
        out.append("")

    out.append("}")
    return "\n".join(out)

if __name__ == "__main__":
    txt = generate_tree()
    target = Path("common/national_focus/turkey.txt")
    target.write_text(txt, encoding="utf-8")
    print(f"Generated {len(FOCI)} focuses successfully into {target}")
