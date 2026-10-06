"""Reviewed art choices for UK wings 1-2 (focus icons, event pictures, derived idea/decision icons).

Choices were made by looking at contact sheets from scripts/art_candidates.py, by subject, not by file name alone.
    python scripts/britain_art_picks.py SCRATCH_DIR   -> writes docs/britain_art_picks.json (self-contained)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# focus id -> (candidate set, subject key, index on the sheet)
FOCUS = {
 "the_coalition_election": ("focus", "the_coalition_election", 4),
 "dominion_procurement_offices": ("focus", "dominion_procurement_offices", 5),
 "the_mediterranean_stations": ("focus", "the_mediterranean_stations", 9),
 "imperial_troop_transport": ("focus", "imperial_troop_transport", 7),
 "the_imperial_war_conference": ("focus", "the_imperial_war_conference", 5),
 "dominion_war_cabinet_delegates": ("focus", "dominion_war_cabinet_delegates", 3),
 "indian_constitutional_consultation": ("focus", "indian_constitutional_consultation", 0),
 "colonial_labour_contracts": ("focus", "colonial_labour_contracts", 1),
 "a_commonwealth_consultation_charter": ("focus", "a_commonwealth_consultation_charter", 1),
 "the_irish_settlement_conference": ("focus", "the_irish_settlement_conference", 1),
 "dominion_status_for_ireland": ("focus", "dominion_status_for_ireland", 2),
 "egyptian_political_negotiations": ("focus", "egyptian_political_negotiations", 6),
 "imperial_defence_after_the_war": ("focus", "imperial_defence_after_the_war", 4),
 "industrial_district_surveys": ("focus", "industrial_district_surveys", 5),
 "midlands_machine_shops": ("focus", "midlands_machine_shops", 2),
 "clyde_shipyard_contracts": ("focus", "clyde_shipyard_contracts", 0),
 "lancashire_engineering": ("focus", "midlands_machine_shops", 4),
 "the_city_credit_market": ("focus", "the_city_credit_market", 3),
 "domestic_coal_allocation": ("focus", "domestic_coal_allocation", 3),
 "national_munitions_contracts": ("focus3", "national_munitions_contracts", 7),
 "shell_inspection_boards": ("focus", "shell_inspection_boards", 1),
 "wartime_labour_dilution": ("focus", "wartime_labour_dilution", 9),
 "the_ministry_of_food": ("focus", "the_ministry_of_food", 6),
 "austerity_and_public_credit": ("focus", "austerity_and_public_credit", 3),
 "convert_the_war_plants": ("focus", "convert_the_war_plants", 5),
 "the_peace_administration_office": ("focus", "the_peace_administration_office", 4),
 "military_demobilisation_planning": ("focus", "military_demobilisation_planning", 2),
 "shipping_repatriation_coordination": ("focus3", "shipping_repatriation_coordination", 4),
 "veterans_welfare_register": ("focus", "veterans_welfare_register", 9),
 "disability_pension_administration": ("focus", "disability_pension_administration", 4),
 "civilian_training_for_returning_soldiers": ("focus", "civilian_training_for_returning_soldiers", 2),
 "public_housing_contracts": ("focus", "public_housing_contracts", 4),
 "industrial_conversion_planning": ("focus", "industrial_conversion_planning", 8),
 "the_employment_exchanges": ("focus2", "the_employment_exchanges", 7),
 "restore_civilian_railway_traffic": ("focus", "restore_civilian_railway_traffic", 3),
 "public_debt_repayment": ("focus", "public_debt_repayment", 2),
 "treasury_expenditure_review": ("focus", "treasury_expenditure_review", 4),
 "merchant_marine_renewal": ("focus", "merchant_marine_renewal", 6),
 "the_public_health_settlement": ("focus", "the_public_health_settlement", 1),
 "the_education_reconstruction_programme": ("focus", "the_education_reconstruction_programme", 4),
 "local_government_finance": ("focus", "local_government_finance", 3),
 "the_industrial_relations_conference": ("focus", "the_industrial_relations_conference", 3),
 "the_postwar_parliamentary_mandate": ("focus", "the_postwar_parliamentary_mandate", 6),
 "the_nineteen_twenty_two_cabinet": ("focus", "the_nineteen_twenty_two_cabinet", 8),
 "the_nineteen_twenty_three_settlement": ("focus2", "the_nineteen_twenty_three_settlement", 10),
 "reconsider_the_continental_policy": ("w3", "reconsider_the_continental_policy", 9),
 "channel_expeditionary_coordination": ("w3", "channel_expeditionary_coordination", 1),
 "russian_procurement_liaison": ("w3", "russian_procurement_liaison", 2),
 "neutral_shipping_assurances": ("w3", "neutral_shipping_assurances", 0),
 "italian_coalition_talks": ("w3", "italian_coalition_talks", 8),
 "the_portuguese_connection": ("w3", "the_portuguese_connection", 3),
 "balkan_allied_coordination": ("w3", "balkan_allied_coordination", 5),
 "coalition_shipping_priorities": ("w3", "coalition_shipping_priorities", 7),
 "armistice_consultations": ("w3", "armistice_consultations", 9),
 "reconstruction_credit_negotiations": ("w3", "reconstruction_credit_negotiations", 9),
 "the_naval_disarmament_conference": ("w3", "the_naval_disarmament_conference", 2),
 "a_european_security_settlement": ("w3", "a_european_security_settlement", 0),
 "the_national_physical_laboratory": ("w3", "the_national_physical_laboratory", 4),
 "university_military_contracts": ("w3", "university_military_contracts", 8),
 "ordnance_metallurgy_research": ("w3", "ordnance_metallurgy_research", 5),
 "machine_tool_standards": ("w3", "machine_tool_standards", 2),
 "railway_engineering_standards": ("w3", "railway_engineering_standards", 0),
 "naval_architecture_research": ("w3", "naval_architecture_research", 8),
 "explosive_safety_research": ("w3", "explosive_safety_research", 8),
 "field_wireless_research": ("w3", "field_wireless_research", 4),
 "signals_intelligence_organisation": ("w3", "signals_intelligence_organisation", 4),
 "the_room_forty_office": ("w3", "the_room_forty_office", 3),
 "aerial_photography_research": ("w3", "aerial_photography_research", 6),
 "artillery_survey_mathematics": ("w3", "artillery_survey_mathematics", 7),
 "chemical_protection_research": ("w3", "chemical_protection_research", 3),
 "the_landships_technical_committee": ("w3", "the_landships_technical_committee", 5),
 "aircraft_engine_research": ("w3", "aircraft_engine_research", 7),
 "hydrophone_analysis_laboratory": ("w3", "hydrophone_analysis_laboratory", 7),
 "production_quality_standards": ("w3", "production_quality_standards", 6),
 "the_postwar_research_council": ("w3", "the_postwar_research_council", 3),
 "industrial_patent_exchanges": ("w3", "industrial_patent_exchanges", 4),
 "technical_education_for_reconstruction": ("w3", "technical_education_for_reconstruction", 6),
}

# art name -> (candidate subject key, index)
EVENT = {
 "home_rule_bill": ("pol1_home_rule", 1), "palace_conference": ("pol2_palace_conference", 3),
 "shell_crisis": ("pol3_coalition_shell_crisis", 3), "december_crisis": ("pol4_december_crisis", 6),
 "coupon_election": ("pol5_coupon_election", 2), "imperial_conference": ("pol6_imperial_conference", 7),
 "ulster_volunteers": ("pol7_ulster_volunteers", 2), "imperial_war_cabinet": ("pol8_imperial_war_cabinet", 6),
 "irish_convention": ("pol9_irish_convention", 4), "anglo_irish_treaty": ("pol10_anglo_irish_treaty", 5),
 "easter_rising": ("pol11_easter_rising", 4), "conscription_crisis": ("pol12_conscription_crisis", 6),
 "dominion_call": ("pol20_dominion_call", 1), "irish_unrest": ("brit3_irish_unrest", 3),
 "clydeside_strike": ("eco1_clydeside_strike", 1), "food_rationing": ("eco3_food_shortage", 7),
 "geddes_axe": ("eco5_treasury_cuts", 4), "miners_lockout": ("eco6_miners_strike", 6),
 "coal_for_allies": ("eco10_coal_allies", 7),
 "supreme_war_council": ("dip2_supreme_war_council", 6, "w3e"),
 "armistice_terms": ("dip3_armistice_terms", 0, "w3e"),
 "washington_conference": ("dip4_washington_conference", 3, "w3e"),
 "american_credit": ("dip10_american_credit", 3, "w3e"),
 "london_offer": ("dip11_london_offer", 5, "w3e"),
 "old_alliance": ("dip12_old_alliance", 4, "w3e"),
 "russian_credit": ("dip13_russian_credit", 7, "w3e"),
 "anglo_french_naval": ("dip14_anglo_french_naval", 1, "w3e"),
 "balkan_coordination": ("dip15_balkan_coordination", 1, "w3e"),
}

# event id -> art name (used by the builders)
EVENT_ART = {
 "ww1_britain_pol.1": "home_rule_bill", "ww1_britain_pol.2": "palace_conference", "ww1_britain_pol.3": "shell_crisis",
 "ww1_britain_pol.4": "december_crisis", "ww1_britain_pol.5": "coupon_election", "ww1_britain_pol.6": "imperial_conference",
 "ww1_britain_pol.7": "ulster_volunteers", "ww1_britain_pol.8": "imperial_war_cabinet", "ww1_britain_pol.9": "irish_convention",
 "ww1_britain_pol.10": "anglo_irish_treaty", "ww1_britain_pol.11": "easter_rising", "ww1_britain_pol.12": "conscription_crisis",
 "ww1_britain_pol.20": "dominion_call", "ww1_britain.3": "irish_unrest",
 "ww1_britain_eco.1": "clydeside_strike", "ww1_britain_eco.3": "food_rationing", "ww1_britain_eco.5": "geddes_axe",
 "ww1_britain_eco.6": "miners_lockout", "ww1_britain_eco.10": "coal_for_allies",
 "ww1_britain_dip.2": "supreme_war_council",
 "ww1_britain_dip.3": "armistice_terms",
 "ww1_britain_dip.4": "washington_conference",
 "ww1_britain_dip.10": "american_credit",
 "ww1_britain_dip.11": "london_offer",
 "ww1_britain_dip.12": "old_alliance",
 "ww1_britain_dip.13": "russian_credit",
 "ww1_britain_dip.14": "anglo_french_naval",
 "ww1_britain_dip.15": "balkan_coordination",
}

# wings 4 and 5 (navy/aviation, army/operations)
EVENT_ART.update({
 "ww1_britain_nav.2": "convoy_debate", "ww1_britain_nav.3": "jutland", "ww1_britain_nav.4": "zeppelins",
 "ww1_britain_nav.5": "gotha_raids", "ww1_britain_nav.6": "smuts_report", "ww1_britain_nav.10": "hunger_blockade",
 "ww1_britain_nav.11": "orders_in_council", "ww1_britain_nav.12": "med_escorts",
 "ww1_britain_mil.2": "dardanelles_decision", "ww1_britain_mil.3": "kut_siege", "ww1_britain_mil.4": "somme_first_day",
 "ww1_britain_mil.5": "demobilisation", "ww1_britain_mil.6": "spring_offensive", "ww1_britain_mil.7": "amiens_black_day",
 "ww1_britain_mil.8": "calais_mutinies", "ww1_britain_mil.10": "bef_arrives", "ww1_britain_mil.11": "straits_fleet",
 "ww1_britain_mil.12": "german_black_day", "ww1_britain_mil.13": "liaison_officers",
})


def event_sprite(event_id):
    return "GFX_event_ww1_britain_" + EVENT_ART[event_id]


# idea sprite name (picture) -> focus whose image it is made from
DERIVED_IDEAS = {
 "ENG_ww1_national_insurance": "national_insurance", "ENG_ww1_defence_of_the_realm": "the_defence_of_the_realm",
 "ENG_ww1_reserved_occupations": "reserved_civilian_occupations", "ENG_ww1_enlarged_franchise": "representation_of_the_people",
 "ENG_ww1_dominion_procurement": "dominion_procurement_offices", "ENG_ww1_imperial_sealift": "imperial_troop_transport",
 "ENG_ww1_commonwealth_consultation": "a_commonwealth_consultation_charter",
 "ENG_ww1_railway_executive": "railway_freight_coordination", "ENG_ww1_coal_allocation": "domestic_coal_allocation",
 "ENG_ww1_munitions_contracts": "national_munitions_contracts", "ENG_ww1_shell_inspection": "shell_inspection_boards",
 "ENG_ww1_labour_dilution": "wartime_labour_dilution", "ENG_ww1_food_control": "the_ministry_of_food",
 "ENG_ww1_industrial_conversion": "industrial_conversion_planning",
 "ENG_ww1_room_forty": "the_room_forty_office",
}
# decision id -> focus image
DERIVED_DECISIONS = {
 "ENG_ww1_empire_policy": "the_imperial_war_conference",
 "ENG_ww1_request_dominion_contingent_CAN": "canadian_defence_consultation",
 "ENG_ww1_request_dominion_contingent_AST": "australian_defence_consultation",
 "ENG_ww1_request_dominion_contingent_NZL": "new_zealand_naval_consultation",
 "ENG_ww1_request_dominion_contingent_SAF": "south_african_cooperation",
 "ENG_ww1_reconvene_imperial_conference": "the_imperial_conference",
 "ENG_ww1_release_irish_prisoners": "irish_parliamentary_support",
 "ENG_ww1_emergency_suppression": "the_military_service_act",
 "ENG_ww1_coal_to_allies": "domestic_coal_allocation",
 "ENG_ww1_war_savings_drive": "austerity_and_public_credit",
 "ENG_ww1_renew_american_credit": "american_credit_negotiations",
}


def main(scratch):
    scratch = Path(scratch)
    sets = {"focus": json.loads((scratch / "sheets_focus/candidates.json").read_text(encoding="utf-8")),
            "focus2": json.loads((scratch / "sheets_focus2/candidates.json").read_text(encoding="utf-8")),
            "focus3": json.loads((scratch / "sheets_focus3/candidates.json").read_text(encoding="utf-8")),
            "w3": json.loads((scratch / "sheets_w3/candidates.json").read_text(encoding="utf-8")),
            "w3e": json.loads((scratch / "sheets_w3e/candidates.json").read_text(encoding="utf-8")),
            "event": json.loads((scratch / "sheets_event/candidates.json").read_text(encoding="utf-8"))}
    out = {"focus": {}, "event": {}, "derived_ideas": DERIVED_IDEAS, "derived_decisions": DERIVED_DECISIONS}
    for fid, (s, subj, idx) in FOCUS.items():
        donor, rel = sets[s][subj][idx]
        out["focus"][fid] = {"donor": donor, "source_relative": rel, "subject": subj}
    for name, spec in EVENT.items():
        subj, idx = spec[0], spec[1]
        donor, rel = sets[spec[2] if len(spec) > 2 else "event"][subj][idx]
        out["event"][name] = {"donor": donor, "source_relative": rel, "subject": subj}
    (ROOT / "docs/britain_art_picks.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(out["focus"]), "focus icons,", len(out["event"]), "event pictures")


if __name__ == "__main__":
    main(sys.argv[1])
