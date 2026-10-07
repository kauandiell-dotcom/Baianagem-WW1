import re
from pathlib import Path

gfx_path = Path("interface/ww1_france_ideas.gfx")
gfx_content = gfx_path.read_text(encoding="utf-8")
existing_sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', gfx_content))

# Collect ideas
ideas_txt = Path("common/ideas/ww1_france_ideas.txt").read_text(encoding="utf-8")
ideas_reforms = Path("common/ideas/zz_ww1_france_reforms.txt").read_text(encoding="utf-8")
all_ideas = set(re.findall(r'(\bFRA_[a-zA-Z0-9_]+\b)\s*=\s*\{', ideas_txt + "\n" + ideas_reforms))

missing = [i for i in sorted(all_ideas) if f"GFX_idea_{i}" not in existing_sprites]
print(f"Missing sprites to generate: {len(missing)}")

# Map of specific high-quality textures in gfx/interface/ideas/FRA
best_map = {
    "FRA_adrian_helmet_protection": "gfx/interface/ideas/FRA/FRA_horizon_blue_uniforms_idea.png",
    "FRA_adriatic_naval_blockade": "gfx/interface/ideas/FRA/FRA_mediterranean_dominance.dds",
    "FRA_aerial_photo_reconnaissance": "gfx/interface/ideas/FRA/FRA_breguet.png",
    "FRA_air_ground_tsf_radio_coordination": "gfx/interface/ideas/FRA/FRA_radiola.png",
    "FRA_algerian_spahis_cavalry": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_alsace_lorraine_reclaimed": "gfx/interface/ideas/FRA/FRA_revanche_accomplished.dds",
    "FRA_american_aef_arrival": "gfx/interface/ideas/FRA/FRA_us_financial_pipeline.png",
    "FRA_artillerie_speciale_cadres": "gfx/interface/ideas/FRA/FRA_renault_ft_revolution.png",
    "FRA_balanced_siege_and_field_artillery": "gfx/interface/ideas/FRA/FRA_famh.png",
    "FRA_bank_of_france_gold_bullion": "gfx/interface/ideas/FRA/FRA_1914_fiscal_solvency.png",
    "FRA_bef_channel_ports_coordination": "gfx/interface/ideas/FRA/FRA_british_naval_entente.png",
    "FRA_blaise_diagne_citizenship_reforms": "gfx/interface/ideas/FRA/idea_FRA_Amedee_Dunois.png",
    "FRA_boue_de_lapeyrere_naval_law": "gfx/interface/ideas/FRA/idea_FRA_Auguste_Boue_de_Lapeyrere.png",
    "FRA_british_coal_imports": "gfx/interface/ideas/FRA/FRA_british_naval_entente.png",
    "FRA_caquot_observation_balloons": "gfx/interface/ideas/FRA/FRA_caudron.png",
    "FRA_cent_jours_combined_arms": "gfx/interface/ideas/FRA/FRA_supreme_combined_arms.png",
    "FRA_chemical_explosives_industry": "gfx/interface/ideas/FRA/FRA_fcm.png",
    "FRA_colonel_duval_air_division": "gfx/interface/ideas/FRA/FRA_morane_saulnier.png",
    "FRA_colonial_logistics_labor": "gfx/interface/ideas/FRA/indochina_union.png",
    "FRA_colonial_order_aof": "gfx/interface/ideas/FRA/indochina_union2.png",
    "FRA_competent_civil_administration": "gfx/interface/ideas/FRA/idea_FRA_rene_viviani.png",
    "FRA_dakar_atlantic_hub": "gfx/interface/ideas/FRA/chantiers_de_penhoet.png",
    "FRA_dakar_niger_logistics": "gfx/interface/ideas/FRA/sncf.png",
    "FRA_defense_bonds_liquidity": "gfx/interface/ideas/FRA/FRA_1914_fiscal_solvency.png",
    "FRA_eastern_front_containment": "gfx/interface/ideas/FRA/FRA_russian_steamroller_pledge.png",
    "FRA_employer_union_compact": "gfx/interface/ideas/FRA/idea_FRA_leon_jouhaux.png",
    "FRA_entente_cordiale_brotherhood": "gfx/interface/ideas/FRA/FRA_british_naval_entente.png",
    "FRA_escorted_maritime_convoys": "gfx/interface/ideas/FRA/chantiers_de_penhoet.png",
    "FRA_foreign_legion_cadres": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_franco_russian_sacred_alliance": "gfx/interface/ideas/FRA/FRA_russian_steamroller_pledge.png",
    "FRA_fully_motorised_logistics": "gfx/interface/ideas/FRA/FRA_berliet.png",
    "FRA_hispano_suiza_aero_engines": "gfx/interface/ideas/FRA/FRA_breguet.png",
    "FRA_imperial_blood_solidarity": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_joffre_supreme_staff": "gfx/interface/ideas/FRA/idea_FRA_joseph_joffre.png",
    "FRA_joint_franco_american_staff": "gfx/interface/ideas/FRA/FRA_us_financial_pipeline.png",
    "FRA_joint_liaison_missions": "gfx/interface/ideas/FRA/FRA_supreme_allied_command.png",
    "FRA_kaiser_offensive_halted": "gfx/interface/ideas/FRA/FRA_Soldier_Choking_Eagel.png",
    "FRA_legendary_flying_aces": "gfx/interface/ideas/FRA/FRA_air_supremacy_spad.png",
    "FRA_light_machinegun_fireteams": "gfx/interface/ideas/FRA/FRA_manufacture_saint_etienne.png",
    "FRA_madagascar_strategic_minerals": "gfx/interface/ideas/FRA/FRA_metallurgique_de_normandie.png",
    "FRA_mass_swarm_tank_tactics": "gfx/interface/ideas/FRA/FRA_renault_ft_revolution.png",
    "FRA_mediterranean_battlefleet": "gfx/interface/ideas/FRA/FRA_mediterranean_dominance.dds",
    "FRA_miracle_of_the_marne": "gfx/interface/ideas/FRA/FRA_Soldier_Choking_Eagel.png",
    "FRA_morocco_treaty_of_fez": "gfx/interface/ideas/FRA/FRA_lyautey_moroccan_order.png",
    "FRA_munitionnettes_workforce": "gfx/interface/ideas/FRA/FRA_albert_thomas_munitions_boom.png",
    "FRA_national_credit_solvency": "gfx/interface/ideas/FRA/FRA_1914_fiscal_solvency.png",
    "FRA_night_interception_patrols": "gfx/interface/ideas/FRA/FRA_caudron.png",
    "FRA_nineteenth_corps_african_army": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_nivelle_offensive_surge": "gfx/interface/ideas/FRA/idea_FRA_robert_nivelle.png",
    "FRA_offensive_school": "gfx/interface/ideas/FRA/FRA_firepower_doctrine.dds",
    "FRA_pams_conciliatory_presidency": "gfx/interface/ideas/FRA/idea_FRA_jules_pams.png",
    "FRA_parliamentary_equilibrium": "gfx/interface/ideas/FRA/idea_FRA_rene_viviani.png",
    "FRA_pasteur_colonial_hygiene": "gfx/interface/ideas/FRA/scientists_exodus.png",
    "FRA_pilot_training_corps": "gfx/interface/ideas/FRA/FRA_potez.png",
    "FRA_plan_xvii_concentration": "gfx/interface/ideas/FRA/FRA_plan_xvii-122742.dds",
    "FRA_poincare_presidency": "gfx/interface/ideas/FRA/idea_FRA_raymond_poincare.png",
    "FRA_q_ships_and_coastal_avisos": "gfx/interface/ideas/FRA/FRA_ateliers_de_la_loire.png",
    "FRA_race_to_the_sea_entrenchment": "gfx/interface/ideas/FRA/FRA_la_voie_sacree_convoy.dds",
    "FRA_railway_super_heavy_artillery": "gfx/interface/ideas/FRA/FRA_atelier_de_puteaux.png",
    "FRA_rouen_coal_dispatch": "gfx/interface/ideas/FRA/FRA_metallurgique_de_normandie.png",
    "FRA_secular_civic_order": "gfx/interface/ideas/FRA/church_ideas.png",
    "FRA_skilled_workforce_recall": "gfx/interface/ideas/FRA/FRA_albert_thomas_munitions_boom.png",
    "FRA_socialist_labor_peace": "gfx/interface/ideas/FRA/idea_FRA_leon_jouhaux.png",
    "FRA_somme_artillery_coordination": "gfx/interface/ideas/FRA/FRA_firepower_doctrine.dds",
    "FRA_spad_fighter_supremacy": "gfx/interface/ideas/FRA/FRA_air_supremacy_spad.png",
    "FRA_standardised_war_tooling": "gfx/interface/ideas/FRA/peugeot.png",
    "FRA_supreme_industrial_mobilisation": "gfx/interface/ideas/FRA/FRA_albert_thomas_munitions_boom.png",
    "FRA_synchronized_vickers_guns": "gfx/interface/ideas/FRA/FRA_manufacture_saint_etienne.png",
    "FRA_tamatave_port_infrastructure": "gfx/interface/ideas/FRA/chantiers_de_penhoet.png",
    "FRA_three_year_law_and_colonial_ranks": "gfx/interface/ideas/FRA/FRA_three_year_conscription.dds",
    "FRA_tirailleurs_marocains_shock": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_tirailleurs_senegalais_valor": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_treaty_of_london_1839_guarantor": "gfx/interface/ideas/FRA/FRA_british_naval_entente.png",
    "FRA_trench_soup_and_wine_rations": "gfx/interface/ideas/FRA/ChampagneRiots.png",
    "FRA_verdun_resilience": "gfx/interface/ideas/FRA/FRA_they_shall_not_pass.png",
    "FRA_versailles_supreme_guarantor": "gfx/interface/ideas/FRA/idea_FRA_Georges_Clemenceau.png",
    "FRA_victorious_aero_industry": "gfx/interface/ideas/FRA/FRA_air_supremacy_spad.png",
    "FRA_wards_of_the_nation_care": "gfx/interface/ideas/FRA/idea_FRA_leon_jouhaux.png",
    "FRA_ww1_division_rotation": "gfx/interface/ideas/FRA/FRA_petain_elastic_defense.png",
    "FRA_ww1_field_fortification": "gfx/interface/ideas/FRA/FRA_la_voie_sacree_convoy.dds",
    "FRA_ww1_rationing": "gfx/interface/ideas/FRA/ChampagneRiots.png",
    "FRA_ww1_salonika_transport": "gfx/interface/ideas/FRA/FRA_ateliers_de_saint_nazaire.png",
    "FRA_ww1_eight_hour_day": "gfx/interface/ideas/FRA/idea_FRA_leon_jouhaux.png",
    "FRA_ww1_workers_councils": "gfx/interface/ideas/FRA/asset_jean_allemane.png",
    "FRA_ww1_employer_compact": "gfx/interface/ideas/FRA/idea_FRA_leon_jouhaux.png",
    "FRA_ww1_bank_credit": "gfx/interface/ideas/FRA/FRA_1914_fiscal_solvency.png",
    "FRA_ww1_industrial_mobilisation": "gfx/interface/ideas/FRA/FRA_albert_thomas_munitions_boom.png",
    "FRA_ww1_colonial_service": "gfx/interface/ideas/FRA/FRA_force_noire_integration.dds",
    "FRA_ww1_imperial_citizenship": "gfx/interface/ideas/FRA/idea_FRA_Amedee_Dunois.png",
    "FRA_ww1_naval_escorts": "gfx/interface/ideas/FRA/chantiers_de_penhoet.png",
    "FRA_ww1_observation_balloons": "gfx/interface/ideas/FRA/FRA_caudron.png",
    "FRA_ww1_offensive_school": "gfx/interface/ideas/FRA/FRA_firepower_doctrine.dds",
    "FRA_ww1_concentration": "gfx/interface/ideas/FRA/FRA_plan_xvii-122742.dds",
    "FRA_ww1_fighting_retreat": "gfx/interface/ideas/FRA/FRA_petain_elastic_defense.png",
    "FRA_ww1_allied_staff": "gfx/interface/ideas/FRA/FRA_supreme_allied_command.png",
    "FRA_ww1_infantry_training": "gfx/interface/ideas/FRA/FRA_horizon_blue_uniforms_idea.png",
}

new_entries = []
for iname in missing:
    tex = best_map.get(iname, "gfx/interface/ideas/FRA/FRA_union_sacree_spirit.png")
    new_entries.append(f"""\tspriteType = {{
\t\tname = "GFX_idea_{iname}"
\t\ttexturefile = "{tex}"
\t}}""")

insertion = "\n".join(new_entries)
# insert before the final closing brace
last_brace = gfx_content.rfind("}")
updated_gfx = gfx_content[:last_brace] + insertion + "\n}\n"
gfx_path.write_text(updated_gfx, encoding="utf-8")
print(f"Successfully appended {len(new_entries)} spriteType entries to ww1_france_ideas.gfx!")
