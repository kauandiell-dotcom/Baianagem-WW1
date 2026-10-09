#!/usr/bin/env python3
"""
Maps Serbian focuses to existing goal textures and generates interface/ww1_serbia_goals.gfx.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GOALS_DIR = ROOT / "gfx" / "interface" / "goals"
GFX_OUT = ROOT / "interface" / "ww1_serbia_goals.gfx"

# Verify existing DDS textures in goals
available_dds = {f.name: f"gfx/interface/goals/{f.name}" for f in GOALS_DIR.glob("*.dds")}
print(f"Total available DDS textures: {len(available_dds)}")

# Fallback texture if any specific one is not found
DEFAULT_TEX = "gfx/interface/goals/focus_BUL_prussia_of_the_balkans.dds"
if "focus_BUL_prussia_of_the_balkans.dds" not in available_dds:
    DEFAULT_TEX = next(iter(available_dds.values()))

# Thematic mapping for all 94 focuses
ICON_MAPPINGS = {
    # Sector 1: Economy & Kragujevac
    "SER_agrarian_kingdom_finances": "focus_generic_industry_1.dds",
    "SER_zadruga_cooperative_network": "focus_generic_agriculture.dds",
    "SER_expand_livestock_and_grain_trade": "GFX_focus_generic_trade.dds",
    "SER_belgrade_nis_rail_artery": "focus_generic_railroad.dds",
    "SER_morava_valley_logistics": "focus_generic_supply.dds",
    "SER_bor_copper_and_rudnik_mines": "focus_generic_steel.dds",
    "SER_modernize_trepca_prospects": "focus_generic_aluminum.dds",
    "SER_kragujevac_military_workshops": "focus_generic_arms_factory.dds",
    "SER_domestic_ammunition_lines": "GFX_ENG_mobilization_of_industry-46494.dds",
    "SER_creusot_schneider_contracts": "generic_artillery_antitank_antiair.dds",
    "SER_national_bank_monetary_stability": "GFX_focus_generic_treaty.dds",
    "SER_diversified_national_industry": "focus_generic_industry_2.dds",

    # Sector 2: Royal Army & General Staff
    "SER_radomir_putnik_doctrine": "focus_BUL_prussia_of_the_balkans.dds",
    "SER_three_ban_conscription_system": "focus_generic_military_academy.dds",
    "SER_mobilization_timetables": "focus_generic_planning_bonus.dds",
    "SER_peacetime_infantry_cadre": "focus_generic_infantry.dds",
    "SER_artillery_park_reorganization": "GER_prussian_artillery.dds",
    "SER_rapid_fire_field_guns": "GFX_AUS_mountain_artillery_guns-46859.dds",
    "SER_drina_defensive_survey": "focus_generic_defense.dds",
    "SER_danubian_flotilla_watch": "focus_generic_coastal_defense.dds",
    "SER_mountain_warfare_detachments": "GFX_AUS_imperialroyal_mountain_troops-46859.dds",
    "SER_entrenchment_and_counterstroke": "focus_generic_tactical_strike.dds",
    "SER_officer_corps_meritocracy": "focus_generic_army_reform.dds",
    "SER_military_telegraph_corps": "focus_generic_radio.dds",
    "SER_field_medical_directorate": "focus_generic_military_spending.dds",
    "SER_foreign_medical_missions": "focus_generic_human_resources.dds",
    "SER_veteran_serbian_soldier": "GFX_SOV_support_serbia-45156.dds",
    "SER_supreme_command_preparedness": "focus_generic_command.dds",

    # Sector 3: Internal Politics & Black Hand
    "SER_reign_of_peter_i": "focus_polish_crown_king.dds",
    "SER_radical_party_cabinet": "GFX_ENG_parliament_act_1911-46518.dds",
    "SER_independent_radicals_dialogue": "GFX_ENG_east_entente_diplomacy-45134.dds",
    "SER_strengthen_narodna_skupstina": "GFX_focus_generic_parliament.dds",
    "SER_constitutional_liberties_bill": "GFX_focus_generic_democracy.dds",
    "SER_crown_prince_regency_prep": "SOV_duma_and_crown.dds",
    "SER_investigate_officer_conspiracies": "GFX_focus_generic_police.dds",
    "SER_the_shadow_of_apis": "GFX_focus_generic_authoritarian.dds",
    "SER_narodna_odbrana_patronage": "GFX_focus_generic_propaganda.dds",
    "SER_military_intelligence_network": "focus_generic_intelligence_agency.dds",
    "SER_civilian_supremacy_charter": "focus_generic_constitutional_guarantees.dds",
    "SER_curb_secret_societies": "GFX_focus_generic_purge.dds",
    "SER_officer_corps_ascendancy": "focus_generic_junta.dds",
    "SER_clandestine_national_action": "GFX_focus_generic_shadow_government.dds",
    "SER_monarchic_arbiter": "focus_HUN_the_kingdom_of_ukraine.dds",
    "SER_patriotic_press_censorship": "GFX_focus_generic_censorship.dds",
    "SER_anticorruption_procurement": "focus_generic_anti_corruption.dds",
    "SER_professional_civil_service": "focus_generic_bureaucracy.dds",
    "SER_national_unity_covenant": "focus_generic_coalition.dds",
    "SER_regency_of_alexander": "focus_generic_monarchy.dds",

    # Sector 4: Balkan Diplomacy & South Slav Question
    "SER_balkan_diplomatic_initiatives": "GER_sway_the_balkans.dds",
    "SER_serbo_bulgarian_dialogue": "GFX_ENG_east_entente_diplomacy-45134.dds",
    "SER_macedonian_autonomy_proposal": "GFX_focus_generic_treaty.dds",
    "SER_bulgarian_non_aggression_pact": "GFX_focus_generic_pact.dds",
    "SER_montenegrin_dynastic_ties": "focus_generic_royal_wedding.dds",
    "SER_cetinje_military_convention": "focus_generic_alliance.dds",
    "SER_greek_commercial_transit": "GFX_focus_generic_trade.dds",
    "SER_romanian_danube_understanding": "focus_germany_romania_yugoslavia.dds",
    "SER_sublime_porte_normalization": "GFX_focus_generic_treaty.dds",
    "SER_balkan_equilibrium_accord": "focus_generic_diplomacy.dds",
    "SER_traditional_russian_patronage": "GFX_SOV_orthodox_brotherhood-45155.dds",
    "SER_saint_petersburg_arms_loans": "GFX_SOV_st_petersburg_industrial_project-45110.dds",
    "SER_banque_franco_serbe_credits": "GFX_focus_generic_loan.dds",
    "SER_entente_diplomatic_shield": "focus_generic_entente.dds",
    "SER_austrian_border_accommodation": "focus_ger_support_austrian_claims.dds",
    "SER_serbo_austrian_trade_treaty": "GFX_focus_generic_trade.dds",
    "SER_suppress_anti_habsburg_agitation": "focus_generic_crackdown.dds",
    "SER_south_slav_cultural_links": "focus_invite_yugoslavia.dds",
    "SER_greater_serbian_strategy": "focus_YUG_dissolve_serbia.dds",
    "SER_yugoslav_federal_ideal": "focus_generic_unification.dds",

    # Sector 5: 1914 Crisis, War, Exile, Liberation
    "SER_sarajevo_aftermath_crisis": "focus_generic_assassination.dds",
    "SER_internal_inquiry_on_conspirators": "focus_generic_investigation.dds",
    "SER_face_austrian_ultimatum": "focus_generic_ultimatum.dds",
    "SER_appeal_to_tsar_nicholas": "GFX_SOV_orthodox_brotherhood-45155.dds",
    "SER_general_mobilization_order": "focus_generic_mobilization.dds",
    "SER_defend_belgrade_perimeter": "focus_generic_fortifications.dds",
    "SER_drina_valley_ambush_lines": "focus_generic_mountain_defense.dds",
    "SER_total_defensive_war": "focus_generic_war_declaration.dds",
    "SER_battle_of_cer_heroism": "focus_generic_heroic_stand.dds",
    "SER_misic_kolubara_counteroffensive": "focus_generic_counter_offensive.dds",
    "SER_typhus_epidemic_containment": "focus_generic_pandemic_relief.dds",
    "SER_the_albanian_golgotha": "focus_generic_harsh_winter.dds",
    "SER_evacuation_of_military_cadres": "focus_generic_naval_convoy.dds",
    "SER_montenegrin_rearguard_stand": "GFX_AUS_imperialroyal_mountain_troops-46859.dds",
    "SER_government_in_exile_corfu": "focus_generic_government_in_exile.dds",
    "SER_rebuild_army_in_salonika": "focus_generic_rebuild_army.dds",
    "SER_french_chauchats_and_75mm": "GFX_FRA_char_de_rupture.dds",
    "SER_salonika_trial_of_apis": "focus_generic_military_tribunal.dds",
    "SER_corfu_declaration_accord": "focus_generic_charter.dds",
    "SER_allied_balkan_coordination": "focus_generic_allied_command.dds",
    "SER_breakthrough_at_dobro_pole": "focus_generic_stormtrooper_charge.dds",
    "SER_liberation_of_the_homeland": "focus_generic_liberation.dds",
    "SER_armistice_on_the_danube": "focus_generic_armistice.dds",
    "SER_podgorica_assembly_unification": "focus_generic_plebiscite.dds",
    "SER_proclamation_of_yugoslavia": "focus_generic_form_greater_nation.dds",
    "SER_restored_sovereign_serbia": "focus_generic_national_triumph.dds",
}

# Resolve each icon to an authentic DDS file that actually exists on disk!
resolved_map = {}
for fid, icon_file in ICON_MAPPINGS.items():
    if icon_file in available_dds:
        resolved_map[fid] = available_dds[icon_file]
    else:
        # Search for closest match or pick thematic fallback
        fallback = None
        for cand in available_dds:
            if any(term in cand.lower() for term in fid.lower().split("_")[1:3]):
                fallback = available_dds[cand]
                break
        resolved_map[fid] = fallback or DEFAULT_TEX

print(f"Mapped {len(resolved_map)} focuses to existing DDS files.")

# Generate interface/ww1_serbia_goals.gfx
lines = [
    "spriteTypes = {",
    "\t# ==============================================================================",
    "\t# KINGDOM OF SERBIA (SER) WW1 GOAL SPRITES & SHINE OVERLAYS (94 FOCUSES)",
    "\t# ==============================================================================",
    ""
]

for fid, texpath in resolved_map.items():
    sprite_name = f"GFX_{fid}"
    shine_name = f"GFX_{fid}_shine"
    lines.append(f"\t# Focus: {fid}")
    lines.append("\tSpriteType = {")
    lines.append(f'\t\tname = "{sprite_name}"')
    lines.append(f'\t\ttexturefile = "{texpath}"')
    lines.append("\t}")
    lines.append("\tSpriteType = {")
    lines.append(f'\t\tname = "{shine_name}"')
    lines.append(f'\t\ttexturefile = "{texpath}"')
    lines.append('\t\teffectFile = "gfx/FX/buttonstate.lua"')
    lines.append("\t\tanimation = {")
    lines.append(f'\t\t\tanimationmaskfile = "{texpath}"')
    lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"')
    lines.append("\t\t\tanimationrotation = -90.0")
    lines.append("\t\t\tanimationlooping = no")
    lines.append("\t\t\tanimationtime = 0.75")
    lines.append("\t\t\tanimationdelay = 0")
    lines.append('\t\t\tanimationblendmode = "add"')
    lines.append('\t\t\tanimationtype = "scrolling"')
    lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
    lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }")
    lines.append("\t\t}")
    lines.append("\t\tanimation = {")
    lines.append(f'\t\t\tanimationmaskfile = "{texpath}"')
    lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"')
    lines.append("\t\t\tanimationrotation = 90.0")
    lines.append("\t\t\tanimationlooping = no")
    lines.append("\t\t\tanimationtime = 0.75")
    lines.append("\t\t\tanimationdelay = 0")
    lines.append('\t\t\tanimationblendmode = "add"')
    lines.append('\t\t\tanimationtype = "scrolling"')
    lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
    lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }")
    lines.append("\t\t}")
    lines.append("\t\tlegacy_lazy_load = no")
    lines.append("\t}")
    lines.append("")

lines.append("}")
lines.append("")

GFX_OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated {GFX_OUT} successfully with {len(resolved_map)} goal sprites and shines!")
