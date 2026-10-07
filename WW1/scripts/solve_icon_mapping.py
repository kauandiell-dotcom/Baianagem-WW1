import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from france_wing1_politics import WING1_FOCI
from france_wing2_economy import WING2_FOCI
from france_wing3_colonial import WING3_FOCI
from france_wing4_navy_air import WING4_FOCI
from france_wing5_army import WING5_FOCI
from france_wing6_diplomacy import WING6_FOCI

all_foci = WING1_FOCI + WING2_FOCI + WING3_FOCI + WING4_FOCI + WING5_FOCI + WING6_FOCI

with open(ROOT / 'scripts' / 'all_normal_france_sprites.txt', 'r', encoding='utf-8') as f:
    available_sprites = [line.strip() for line in f if line.strip()]

avail_set = set(available_sprites)
print(f'Total available real sprites: {len(available_sprites)}')

# Exact matches first
focus_to_sprite = {}
used_sprites = set()

for f in all_foci:
    fid = f['id']
    target = f['icon']
    if target in avail_set and target not in used_sprites:
        focus_to_sprite[fid] = target
        used_sprites.add(target)

print(f'Exact matches assigned: {len(focus_to_sprite)}')

# Explicit high-quality thematic mapping from available_sprites
# strictly ensuring each chosen sprite is in avail_set and not in used_sprites
priority_mapping = {
    # Politics
    'FRA_pacifisme_de_jean_jaures': 'GFX_FRA_protection_de_jean_jaures',
    'FRA_loi_des_retraites_ouvrieres': 'GFX_FRA_journee_de_huit_heures',
    'FRA_suffrage_et_citoyennete': 'GFX_FRA_citoyennete_francaise_elargie',
    'FRA_assassinat_de_jean_jaures': 'GFX_FRA_le_scandale_calmette_caillaux',
    'FRA_repressions_du_defaitisme': 'GFX_FRA_censure_et_bourrage_de_crane',
    'FRA_comite_des_forges_coordination': 'GFX_FRA_transition_vers_l_economie_de_guerre',
    'FRA_maintien_du_parlementarisme_guerre': 'GFX_FRA_stabilite_ministerielle_garantie',
    'FRA_reconciliation_avec_les_catholiques': 'GFX_FRA_ordre_moral_et_republicain',
    'FRA_presse_populaire_et_illustres': 'GFX_FRA_mobilisation_des_esprits',
    'FRA_statut_des_fonctionnaires': 'GFX_FRA_la_republique_autoritaire',
    'FRA_justice_militaire_mesuree': 'GFX_FRA_repression_mesuree_des_meneurs',
    'FRA_reorganisation_post_guerre': 'GFX_FRA_la_paix_de_versailles_imposition',
    'FRA_solidarite_nationale_veufs_orphelins': 'GFX_FRA_le_pain_et_la_paix_juste',
    'FRA_ecole_normale_et_instituteurs': 'GFX_FRA_republique_sociale_et_democratique',

    # Economy
    'FRA_bassin_siderurgique_de_briey': 'GFX_FRA_bassin_parisien_metallurgie',
    'FRA_fonderies_de_lorraine': 'GFX_FRA_hauts_fourneaux_de_lorraine',
    'FRA_mines_de_charbon_du_nord': 'GFX_FRA_usines_du_nord_et_pas_de_calais',
    'FRA_etablissements_schneider_le_creusot': 'GFX_FRA_le_creusot_schneider',
    'FRA_modernisation_du_creusot': 'GFX_FRA_manufacture_d_armes_saint_etienne',
    'FRA_usines_automobiles_renault_panhard': 'GFX_FRA_industrie_automobile_renault_panhard',
    'FRA_ateliers_de_puteaux_et_tulle': 'GFX_FRA_depots_reglements_du_genie',
    'FRA_bassin_textile_et_chimique_lille': 'GFX_FRA_nationalisation_des_mines_et_chemins_de_fer',
    'FRA_chimie_industrielle_saint_fons': 'GFX_FRA_usines_de_poudre_saint_fons',
    'FRA_bassin_chimique_marseille': 'GFX_FRA_chimie_industrielle_du_rhone',
    'FRA_siderurgie_electrique_ugine': 'GFX_FRA_autogestion_des_usines',
    'FRA_electrification_du_midi': 'GFX_FRA_houille_blanche_des_alpes',
    'FRA_chemins_de_fer_nord_africains': 'GFX_FRA_chemins_de_fer_sahariens',
    'FRA_reseau_ferroviaire_du_nord_et_est': 'GFX_FRA_chemins_de_fer_du_nord',
    'FRA_ports_charbonniers_rouen': 'GFX_FRA_importations_de_charbon_anglais',
    'FRA_modernisation_du_port_du_havre': 'GFX_FRA_escorteurs_rapides_classe_ailette',
    'FRA_chantiers_navals_saint_nazaire': 'GFX_FRA_projet_cuirasses_classe_lyon',
    'FRA_perte_des_mines_du_nord_repli': 'GFX_FRA_repli_du_gouvernement_a_bordeaux',
    'FRA_crise_des_munitions_1914': 'GFX_FRA_la_crise_des_munitions_1914',
    'FRA_les_munitionnettes': 'GFX_FRA_les_munitionnettes_ouvrieres',
    'FRA_affectes_speciaux_rappel_ouvriers': 'GFX_FRA_discipline_sociale_et_patronat',
    'FRA_conversion_des_ateliers_civils': 'GFX_FRA_reconversion_industrielle_totale',
    'FRA_bons_de_la_defense_nationale': 'GFX_FRA_emprunts_nationaux_de_la_defense',
    'FRA_or_des_francais_pour_la_patrie': 'GFX_FRA_reforme_fiscale_impot_revenu',
    'FRA_rationnement_et_ravitaillement': 'GFX_FRA_rationnement_du_pain_et_charbon',
    'FRA_credits_financiers_anglo_americains': 'GFX_FRA_credit_lyonnais_et_haute_banque',
    'FRA_standardisation_des_calibres': 'GFX_FRA_puissance_industrielle_de_1918',
    'FRA_importations_de_charbon_britannique': 'GFX_FRA_accord_sur_le_minerai_et_le_charbon',
    'FRA_credit_national_de_reconstruction': 'GFX_FRA_la_demande_d_armistice_allemande',
    'FRA_reconstitution_des_territoires_liberes': 'GFX_FRA_le_wagon_de_rethondes_a_compiegne',

    # Colonial
    'FRA_protectorat_marocain_lyautey': 'GFX_FRA_pacification_du_maroc_lyautey',
    'FRA_afrique_occidentale_francaise_aof': 'GFX_FRA_ressources_de_l_aof_dakar',
    'FRA_l_indochine_francaise': 'GFX_FRA_chemin_de_fer_yunnan_vietnam',
    'FRA_port_strategique_de_dakar': 'GFX_FRA_surveillance_du_detroit_de_gibraltar',
    'FRA_chemin_de_fer_dakar_niger': 'GFX_FRA_etoile_ferroviaire_de_paris',
    'FRA_mines_de_fer_de_l_ouenza': 'GFX_FRA_protectorat_de_tunisie',
    'FRA_phosphates_de_tunisie': 'GFX_FRA_communaute_imperiale_unie',
    'FRA_caoutchouc_et_riz_d_indochine': 'GFX_FRA_riz_et_mines_d_indochine',
    'FRA_ressources_de_madagascar': 'GFX_FRA_ressources_de_l_aef_brazzaville',
    'FRA_ports_de_madagascar': 'GFX_FRA_ports_de_saigon_et_haiphong',
    'FRA_missions_medicales_coloniales_calmette': 'GFX_FRA_reforme_des_statuts_indigenes',
    'FRA_la_force_noire_de_mangin': 'GFX_FRA_la_force_noire_du_general_mangin',
    'FRA_zouaves_et_spahis_d_afrique': 'GFX_FRA_tirailleurs_algeriens_et_goumiers',
    'FRA_regiments_de_tirailleurs_marocains': 'GFX_FRA_tirailleurs_senegalais',
    'FRA_recrutement_des_spahis_algeriens': 'GFX_FRA_regiments_de_chasseurs_alpins',
    'FRA_bataillons_indochinois_et_malgaches': 'GFX_FRA_bataillons_coloniaux_au_front',
    'FRA_recrutement_des_legions_etrangeres': 'GFX_FRA_federation_coloniale_associee',
    'FRA_le_sang_de_l_empire': 'GFX_FRA_travailleurs_coloniaux_de_marseille',
    'FRA_citoyennete_et_recompenses_coloniales': 'GFX_FRA_compromis_des_deux_ans_et_demi',

    # Navy & Air
    'FRA_statut_naval_de_1912': 'GFX_FRA_statut_naval_boue_de_lapeyrere',
    'FRA_cuirasses_classe_bretagne': 'GFX_FRA_superdreadnoughts_classe_bretagne',
    'FRA_croiseurs_cuirasses_classe_waldeck_rousseau': 'GFX_FRA_dreadnoughts_classe_courbet',
    'FRA_torpilleurs_et_contre_torpilleurs': 'GFX_FRA_torpilleurs_de_haute_mer_arabe',
    'FRA_flottilles_de_sous_marins_narval': 'GFX_FRA_sous_marins_classe_pluviose',
    'FRA_flotte_de_haute_mer_mediterranee': 'GFX_FRA_flotte_de_la_mediterranee_toulon',
    'FRA_base_navale_de_bizerte': 'GFX_FRA_le_bloc_latin_mediterraneen',
    'FRA_arsenaux_de_toulon_et_brest': 'GFX_FRA_escadre_de_l_atlantique_brest',
    'FRA_base_navale_de_saigon': 'GFX_FRA_ravitaillement_naval_du_front_salonique',
    'FRA_blocus_de_l_adriatique': 'GFX_FRA_blocus_du_canal_d_otrante',
    'FRA_reponse_a_la_menace_sous_marine': 'GFX_FRA_patrouilles_anti_sous_marines',
    'FRA_aviso_et_patrouilleurs_q_ships': 'GFX_FRA_croiseurs_auxiliaires_et_q_ships',
    'FRA_tactique_des_convois_maritimes': 'GFX_FRA_grenades_anti_sous_marines_guiraud',
    'FRA_controle_total_de_la_mediterranee': 'GFX_FRA_maitrise_definitive_de_la_mediterranee',
    'FRA_aviation_navale_et_porte_hydravions': 'GFX_FRA_porte_hydravions_foudre',
    'FRA_flotte_de_la_victoire_1918': 'GFX_FRA_fusiliers_marins_amiral_ronarch',
    'FRA_ecoles_de_pilotage_pau_et_etampes': 'GFX_FRA_ecoles_d_aviation_pau_avord',
    'FRA_avions_de_reconnaissance_farman_voisin': 'GFX_FRA_biplans_farman_reconnaissance',
    'FRA_synchronisation_de_mitrailleuse_garros': 'GFX_FRA_tir_a_travers_l_helice_garros',
    'FRA_chasseurs_spad_vii_et_xiii': 'GFX_FRA_chasseurs_spad_vii_hispano',
    'FRA_escadrille_des_cigognes_et_as_du_ciel': 'GFX_FRA_escadrille_la_fayette',
    'FRA_cooperation_air_artillerie_tsf': 'GFX_FRA_reglage_d_artillerie_par_tsh',
    'FRA_moteurs_hispano_suiza_et_gnome': 'GFX_FRA_chasseurs_spad_xiii_suprematie',
    'FRA_dirigeables_et_ballons_d_observation': 'GFX_FRA_ballons_captifs_saucisses',
    'FRA_chasseurs_de_nuit_et_projecteurs': 'GFX_FRA_avions_de_chasse_de_nuit',
    'FRA_heritage_aeronautique_victorieux': 'GFX_FRA_suprematie_aerienne_absolue',

    # Army
    'FRA_loi_des_trois_ans_1913': 'GFX_FRA_la_loi_des_trois_ans_1913',
    'FRA_lecons_sanglantes_des_frontieres': 'GFX_FRA_echec_de_l_offensive_initiale',
    'FRA_stabilisation_du_front_de_tranchees': 'GFX_FRA_stabilisation_du_front_occidental',
    'FRA_uniformes_horizon_bleu': 'GFX_FRA_uniformes_pantalon_rouge_tradition',
    'FRA_doctrine_petain_feu_et_materiel': 'GFX_FRA_petain_commandant_en_chef',
    'FRA_offensive_nivelle_chemin_des_dames': 'GFX_FRA_catastrophe_du_chemin_des_dames',
    'FRA_crise_des_mutineries_1917': 'GFX_FRA_les_mutineries_des_poilus',
    'FRA_armee_moderne_motorisee': 'GFX_FRA_chars_schneider_ca1_et_saint_chamond',

    # Diplomacy
    'FRA_fermete_diplomatique_agadir': 'GFX_FRA_reponse_au_coup_d_agadir',
    'FRA_compromis_colonial_allemand': 'GFX_FRA_accord_colonial_franco_allemand',
    'FRA_soutien_financier_au_tsar': 'GFX_FRA_emprunts_russes_chemin_de_fer',
    'FRA_intervention_a_odessa_mer_noire': 'GFX_FRA_intervention_a_odessa_mar_noir',
    'FRA_solidarite_avec_la_belgique': 'GFX_FRA_defense_de_dixmude_1914',
    'FRA_mission_viviani_joffre_aux_usa': 'GFX_FRA_relations_financieres_avec_les_usa',
    'FRA_armer_l_armee_americaine': 'GFX_FRA_arrivee_du_corps_expeditionnaire_americain',
}

for fid, spr in priority_mapping.items():
    assert spr in avail_set, f'Sprite {spr} not in available_sprites'
    if spr in used_sprites:
        # If already used by another focus, find who used it
        conflict = [k for k, v in focus_to_sprite.items() if v == spr]
        print(f'Warning: {spr} was used by {conflict}, reassigning to {fid}')
        for c in conflict:
            del focus_to_sprite[c]
    focus_to_sprite[fid] = spr
    used_sprites.add(spr)

print(f'Total mapped after priority: {len(focus_to_sprite)}')

# Check any remaining unmapped focuses
unmapped = [f['id'] for f in all_foci if f['id'] not in focus_to_sprite]
print(f'Unmapped count: {len(unmapped)}')

unused_pool = [s for s in available_sprites if s not in focus_to_sprite.values()]
print(f'Unused sprites in pool: {len(unused_pool)}')

for fid in unmapped:
    spr = unused_pool.pop(0)
    focus_to_sprite[fid] = spr
    print(f'Assigned from pool: {fid} -> {spr}')

print(f'Final mapped count: {len(focus_to_sprite)}')
assert len(focus_to_sprite) == 200, f'Expected 200 mapped focuses, got {len(focus_to_sprite)}'
used_final = list(focus_to_sprite.values())
dup_final = [s for s in set(used_final) if used_final.count(s) > 1]
assert not dup_final, f'Duplicate sprites: {dup_final}'
for spr in used_final:
    assert spr in avail_set, f'Sprite {spr} not in avail_set'

print('SUCCESS: All 200 focuses mapped to 100% UNIQUE REAL sprites!')

# Save dictionary to map_france_icons.py
with open(ROOT / 'scripts' / 'map_france_icons.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('final_icon_map = {\n')
    for fid in sorted(focus_to_sprite.keys()):
        f.write(f'    "{fid}": "{focus_to_sprite[fid]}",\n')
    f.write('}\n')
print('Wrote clean final_icon_map to scripts/map_france_icons.py')
