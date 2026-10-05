# Upgrade focus rewards in data_foci.py with concrete content, real factories, railways, units, and bilateral events

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from france_builder.data_foci import FRENCH_FOCI

REWARD_UPGRADES = {
    'FRA_preserver_la_republique': 'add_political_power = 120\nadd_stability = 0.05\nadd_ideas = FRA_republican_vigilance',
    'FRA_senat_et_chambre_des_deputes': 'add_political_power = 80\nadd_stability = 0.05\n16 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }',
    'FRA_laicite_republicaine': 'add_stability = 0.08\nadd_political_power = 60\nadd_research_slot = 1',
    'FRA_bassin_parisien_metallurgie': '16 = {\n\tadd_extra_state_shared_building_slots = 3\n\tadd_building_construction = { type = industrial_complex level = 2 instant_build = yes }\n}',
    'FRA_hauts_fourneaux_de_lorraine': '18 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = arms_factory level = 1 instant_build = yes }\n}\nadd_resource = { type = steel amount = 16 state = 18 }',
    'FRA_usines_du_nord_et_pas_de_calais': '29 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = industrial_complex level = 1 instant_build = yes }\n}\nadd_resource = { type = aluminium amount = 12 state = 29 }',
    'FRA_le_creusot_schneider': '20 = {\n\tadd_extra_state_shared_building_slots = 3\n\tadd_building_construction = { type = arms_factory level = 2 instant_build = yes }\n}\nadd_equipment_to_stockpile = { type = artillery_equipment_1 amount = 100 }',
    'FRA_manufacture_d_armes_saint_etienne': '24 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = arms_factory level = 2 instant_build = yes }\n}\nadd_equipment_to_stockpile = { type = infantry_equipment_1 amount = 5000 }',
    'FRA_industrie_automobile_renault_panhard': '16 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }\nadd_equipment_to_stockpile = { type = motorized_equipment_1 amount = 150 }\nadd_tech_bonus = { name = motorized_bonus bonus = 1.0 uses = 1 category = motorized_equipment }',
    'FRA_chimie_industrielle_du_rhone': '32 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }\nadd_tech_bonus = { name = synth_bonus bonus = 1.0 uses = 1 category = industry }',
    'FRA_etoile_ferroviaire_de_paris': '16 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 6547 } }\nadd_equipment_to_stockpile = { type = train_equipment_1 amount = 50 }',
    'FRA_chemins_de_fer_de_l_est': '18 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 648 } }\n20 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 6542 } }',
    'FRA_chemins_de_fer_du_nord': '29 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 929 } }',
    'FRA_wagons_de_mobilisation_rapide': 'add_equipment_to_stockpile = { type = train_equipment_1 amount = 100 }\narmy_speed_factor = 0.05\nsupply_consumption_factor = -0.05',
    'FRA_depots_reglements_du_genie': '18 = { add_building_construction = { type = supply_node level = 1 instant_build = yes province = 648 } }\nadd_equipment_to_stockpile = { type = support_equipment_1 amount = 500 }',
    'FRA_reconversion_industrielle_totale': '19 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = arms_factory level = 2 instant_build = yes }\n}\n32 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = arms_factory level = 2 instant_build = yes }\n}',
    'FRA_les_munitionnettes_ouvrieres': 'add_manpower = 50000\nindustrial_capacity_factory = 0.10\n16 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }',
    'FRA_importations_de_charbon_anglais': 'add_resource = { type = aluminium amount = 16 state = 15 }\nadd_equipment_to_stockpile = { type = convoy_1 amount = 50 }',
    'FRA_houille_blanche_des_alpes': '32 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = industrial_complex level = 1 instant_build = yes }\n}\nadd_resource = { type = aluminium amount = 14 state = 32 }',
    'FRA_usines_de_poudre_saint_fons': '32 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = arms_factory level = 1 instant_build = yes }\n}\nadd_equipment_to_stockpile = { type = support_equipment_1 amount = 1000 }',
    'FRA_mise_en_valeur_de_l_algerie': '460 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = industrial_complex level = 1 instant_build = yes }\n}\nadd_resource = { type = oil amount = 6 state = 460 }\nadd_resource = { type = steel amount = 10 state = 460 }',
    'FRA_protectorat_de_tunisie': '458 = {\n\tadd_extra_state_shared_building_slots = 2\n\tadd_building_construction = { type = industrial_complex level = 1 instant_build = yes }\n}\nadd_resource = { type = tungsten amount = 8 state = 458 }',
    'FRA_pacification_du_maroc_lyautey': 'promote_character = FRA_hubert_lyautey\nadd_ideas = FRA_lyautey_moroccan_order\n461 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }',
    'FRA_regiments_de_chasseurs_alpins': 'load_oob = "FRA_chasseurs_reinforcements"\nadd_equipment_to_stockpile = { type = infantry_equipment_1 amount = 3000 }\nadd_tech_bonus = { name = mountain_bonus bonus = 1.0 uses = 1 category = mountaineers }',
    'FRA_reseau_de_forts_sere_de_rivieres': '18 = { add_building_construction = { type = bunker level = 2 instant_build = yes province = 648 } }\n20 = { add_building_construction = { type = bunker level = 2 instant_build = yes province = 6542 } }',
    'FRA_canon_de_75mm_modele_1897': 'load_oob = "FRA_choc_75mm_reinforcements"\nadd_equipment_to_stockpile = { type = artillery_equipment_1 amount = 350 }\narmy_artillery_attack_factor = 0.10',
    'FRA_adopter_le_casque_adrian_m1915': 'add_ideas = FRA_horizon_blue_uniforms_idea\narmy_defence_factor = 0.05',
    'FRA_parc_d_artillerie_lourde_rimailho': 'add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 200 }\nadd_tech_bonus = { name = heavy_art_bonus bonus = 1.0 uses = 1 category = artillery }',
    'FRA_fusil_mitrailleur_chauchat': 'add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 4000 }\nadd_tech_bonus = { name = infantry_weapons_bonus bonus = 1.0 uses = 1 category = infantry_weapons }\narmy_infantry_attack_factor = 0.05',
    'FRA_chars_schneider_ca1_et_saint_chamond': 'add_equipment_to_stockpile = { type = medium_tank_chassis_1 amount = 60 }\nadd_tech_bonus = { name = armor_bonus bonus = 1.0 uses = 1 category = armor }',
    'FRA_char_leger_renault_ft': 'load_oob = "FRA_chars_ft_reinforcements"\nadd_equipment_to_stockpile = { type = light_tank_chassis_1 amount = 120 }\nadd_ideas = FRA_renault_ft_revolution',
    'FRA_emprunts_russes_chemin_de_fer': 'add_political_power = -30\nif = {\n\tlimit = { country_exists = SOV }\n\tSOV = { country_event = { id = ww1_france.201 days = 1 } }\n}',
    'FRA_pourparlers_d_etat_major_joffre_jilinsky': 'add_command_power = 25\nif = {\n\tlimit = { country_exists = SOV }\n\tSOV = { country_event = { id = ww1_france.204 days = 1 } }\n}',
    'FRA_accords_navals_franco_britanniques': 'add_political_power = 40\nif = {\n\tlimit = { country_exists = ENG }\n\tENG = { country_event = { id = ww1_france.210 days = 1 } }\n}',
    'FRA_plans_de_debarquement_du_bef': 'add_command_power = 25\nif = {\n\tlimit = { country_exists = ENG }\n\tENG = { country_event = { id = ww1_france.213 days = 1 } }\n}',
    'FRA_conseil_supreme_de_guerre_versailles': 'add_ideas = FRA_supreme_allied_command\nif = {\n\tlimit = { country_exists = ENG }\n\tENG = { country_event = { id = ww1_france.216 days = 1 } }\n}\nif = {\n\tlimit = { country_exists = USA }\n\tUSA = { country_event = { id = ww1_france.216 days = 1 } }\n}',
    'FRA_negocier_avec_l_italie_traite_de_londres': 'add_political_power = 50\nif = {\n\tlimit = { country_exists = ITA }\n\tITA = { country_event = { id = ww1_france.220 days = 1 } }\n}',
    'FRA_mission_militaire_en_roumanie_berthelot': 'add_political_power = 30\nif = {\n\tlimit = { country_exists = ROM }\n\tROM = { country_event = { id = ww1_france.232 days = 1 } }\n}',
    'FRA_soutien_inconditionnel_a_la_serbie': 'add_stability = 0.05\nif = {\n\tlimit = { country_exists = SER }\n\tSER = { country_event = { id = ww1_france.230 days = 1 } }\n}',
    'FRA_front_d_orient_a_salonique': 'add_manpower = 30000\nif = {\n\tlimit = { country_exists = GRE }\n\tGRE = { country_event = { id = ww1_france.234 days = 1 } }\n}',
    'FRA_offensive_du_vardar_franchet_d_esperey': 'promote_character = FRA_louis_franchet_d_esperey\nadd_command_power = 35\nif = {\n\tlimit = { country_exists = BUL }\n\tBUL = { country_event = { id = ww1_france.237 days = 1 } }\n}',
    'FRA_relations_financieres_avec_les_usa': 'add_political_power = 50\nif = {\n\tlimit = { country_exists = USA }\n\tUSA = { country_event = { id = ww1_france.250 days = 1 } }\n}',
    'FRA_instruction_militaire_des_doughboys': 'army_experience = 30\nif = {\n\tlimit = { country_exists = USA }\n\tUSA = { country_event = { id = ww1_france.253 days = 1 } }\n}',
    'FRA_voie_du_rapprochement_franco_allemand': 'set_country_flag = FRA_alt_diplomacy\nif = {\n\tlimit = { country_exists = GER }\n\tGER = { country_event = { id = ww1_france.260 days = 1 } }\n}',
    'FRA_condominium_d_alsace_lorraine': 'add_political_power = 60\nif = {\n\tlimit = { country_exists = GER }\n\tGER = { country_event = { id = ww1_france.265 days = 1 } }\n}',
    'FRA_pacte_de_non_agression_continental': 'add_stability = 0.15\nif = {\n\tlimit = { country_exists = GER }\n\tGER = { country_event = { id = ww1_france.268 days = 1 } }\n}',
    'FRA_le_bloc_latin_mediterraneen': 'create_faction = FRA_latin_entente\nif = {\n\tlimit = { country_exists = ITA }\n\tITA = { country_event = { id = ww1_france.270 days = 1 } }\n}\nif = {\n\tlimit = { country_exists = SPR }\n\tSPR = { country_event = { id = ww1_france.271 days = 1 } }\n}',
}

count = 0
for f in FRENCH_FOCI:
    fid = f['id']
    if fid in REWARD_UPGRADES:
        f['reward'] = REWARD_UPGRADES[fid]
        count += 1

print(f"Upgraded rewards for {count} focuses.")

# Write back data_foci.py
out_path = os.path.abspath('scripts/france_builder/data_foci.py')
with open(out_path, 'w', encoding='utf-8') as out:
    out.write("# Generated French Focus Tree Data (222 Foci)\n")
    out.write("FRENCH_FOCI = [\n")
    for f in FRENCH_FOCI:
        out.write(f"    {repr(f)},\n")
    out.write("]\n")

print(f"Successfully re-wrote {out_path} with {len(FRENCH_FOCI)} focuses.")
