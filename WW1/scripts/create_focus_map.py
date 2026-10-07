import re

# Load all verified normal sprites
with open('scripts/all_normal_germany_sprites.txt', 'r', encoding='utf-8') as f:
    sprites = set(line.strip() for line in f if line.strip())

# Define the exact mapping for each of the 83 focuses
focus_sprites = {
    # Trunk (7)
    'GER_kaiser_wilhelm_personal_rule': 'GFX_focus_GER_constitutional_monarchy_proclamation',
    'GER_reichstag_1912_elections': 'GFX_GER_Reichstag',
    'GER_centenary_of_leipzig_1913': 'GFX_focus_GER_centenary_of_leipzig_1913',
    'GER_reichstag_social_concessions': 'GFX_focus_GER_workers_rights',
    'GER_appease_the_junkers': 'GFX_GER_Prussian_Zentrum',
    'GER_prussian_franchise_debate': 'GFX_focus_GER_strive_for_conservative_values',
    'GER_burgfrieden_declaration_1914': 'GFX_focus_GER_rally_the_nation',

    # Lane 1: Spartakusbund & Workers' Councils (19)
    'GER_spartakusbund_proletarian_revolt': 'GFX_focus_GER_start_the_proletarian_revolution',
    'GER_kiel_sailors_mutiny': 'GFX_focus_GER_ww1_kiel_sailors_mutiny',
    'GER_berlin_january_mass_strikes': 'GFX_focus_GER_support_the_proletarian_uprising',
    'GER_proclaim_freie_sozialistische_republik': 'GFX_focus_GER_proletarian_solidarity',
    'GER_soldiers_and_workers_councils': 'GFX_GER_SPD',
    'GER_volksmarinedivision_guard': 'GFX_focus_GER_marinestosstrupp',
    'GER_dissolve_the_junker_officer_caste': 'GFX_focus_GER_root_out_imperialism',
    'GER_socialist_land_and_factory_collectivization': 'GFX_focus_GER_social_ownership',
    'GER_rote_ruhrarmee_formation': 'GFX_focus_GER_ressurect_the_red_front_fighters_league',
    'GER_council_economic_planning': 'GFX_focus_GER_optimize_reich_labour_service',
    'GER_red_high_seas_fleet': 'GFX_focus_GER_rebuild_the_high_seas_fleet',
    'GER_alliance_with_soviet_russia': 'GFX_focus_GER_ww1_alliance_with_soviet_russia',
    'GER_soviet_military_advisors': 'GFX_focus_GER_pool_technical_know_how',
    # Lane 1 Invasions & Conquistas Diplomaticas
    'GER_red_baltic_intervention': 'GFX_focus_GER_subduing_the_baltic_states',
    'GER_liberate_the_polish_proletariat': 'GFX_focus_wake_up_poland',
    'GER_danubian_soviet_federation': 'GFX_focus_GER_the_austrian_question',
    'GER_liberate_the_balkans_workers': 'GFX_focus_GER_sway_the_balkans',
    'GER_export_revolution_to_france': 'GFX_focus_GER_war_with_france',
    'GER_world_proletarian_revolution': 'GFX_focus_GER_ww1_world_proletarian_revolution',

    # Lane 2: Democratic Reform & Republic (19)
    'GER_prussian_franchise_reform': 'GFX_focus_GER_prussian_franchise_reform',
    'GER_prince_max_von_baden_cabinet': 'GFX_focus_GER_ww1_prince_max_von_baden_cabinet',
    'GER_proclaim_deutsche_republik': 'GFX_focus_GER_reestablish_free_elections',
    'GER_repeal_anti_socialist_heritage': 'GFX_focus_GER_ww1_repeal_anti_socialist_heritage',
    'GER_antinationalist_civil_defense': 'GFX_focus_GER_tend_to_the_future_of_germany',
    'GER_stinnes_legien_social_compromise': 'GFX_GER_Binnenwirtschaft',
    'GER_rathenau_industrial_reorganization': 'GFX_GER_Rathenauplan',
    'GER_weimar_national_assembly': 'GFX_focus_GER_reichstag',
    'GER_zentrum_concordat_with_rome': 'GFX_GER_Zentrum',
    'GER_post_war_welfare_and_reconstruction': 'GFX_focus_GER_strengthen_the_welfare_state',
    'GER_federal_constitutional_balance': 'GFX_focus_GER_ww1_federal_constitutional_monarchy',
    # Lane 2 Invasions & Conquistas Diplomaticas
    'GER_direct_negotiations_with_woodrow_wilson': 'GFX_focus_GER_ww1_ambassador_bernstorff_us_lobby',
    'GER_alsace_lorraine_plebiscite': 'GFX_focus_GER_reintegrate_luxemburg_and_alsace_lorraine',
    'GER_democratic_mitteleuropa_union': 'GFX_focus_GER_mitteleuropa_cooperation_sphere',
    'GER_subjugate_luxembourg_customs': 'GFX_focus_GER_low_countries_membership',
    'GER_nordic_democratic_trade_compact': 'GFX_focus_GER_swedish_trade_agreement',
    'GER_guarantee_independent_poland_buffer': 'GFX_focus_GER_reassert_eastern_claims',
    'GER_baltic_democratic_confederation': 'GFX_focus_GER_safeguard_the_baltic',
    'GER_pan_european_arbitration_league': 'GFX_focus_generic_world_peace',

    # Lane 3: OHL Military Dictatorship (19)
    'GER_silent_dictatorship_ohl': 'GFX_focus_GER_silent_dictatorship_ohl',
    'GER_oust_bethmann_hollweg': 'GFX_focus_GER_ww1_oust_bethmann_hollweg',
    'GER_hindenburg_program_mobilization': 'GFX_focus_GER_ww1_falkenhayn_dismissal_third_ohl',
    'GER_patriotic_auxiliary_service_law': 'GFX_GER_Freiwilliger_Arbeitsdienst',
    'GER_krupp_ordnance_dictate': 'GFX_focus_GER_ww1_krupp_heavy_ordnance_contracts',
    'GER_total_war_patriotism_kriegsanleihen': 'GFX_GER_Ufa_War_Propaganda',
    'GER_sturmtruppen_doctrine_offensive': 'GFX_GER_Sturmtruppen',
    'GER_subjugate_the_reichstag_politicians': 'GFX_focus_GER_total_control_over_domestic_affairs',
    'GER_unrestricted_submarine_mobilization': 'GFX_focus_GER_unrestricted_submarine_warfare',
    'GER_septemberprogramm_war_aims': 'GFX_focus_GER_spheres_of_influence',
    # Lane 3 Invasions & Conquistas Diplomaticas
    'GER_annexation_of_belgium_and_briey': 'GFX_focus_GER_annexation_of_belgium_and_briey',
    'GER_subjugate_romanian_ploesti_oil': 'GFX_focus_GER_subjugate_romanian_economy',
    'GER_brest_litovsk_carve_up': 'GFX_focus_GER_ww1_treaty_of_brest_litovsk',
    'GER_establish_generalgouvernement_warschau': 'GFX_focus_GER_see_to_the_eastern_front',
    'GER_finnish_intervention_von_der_goltz': 'GFX_focus_GER_support_finland',
    'GER_carve_ukrainian_breadbasket': 'GFX_focus_HUN_the_kingdom_of_ukraine',
    'GER_operation_faustschlag_crusade': 'GFX_focus_GER_strike_eastward',
    'GER_subjugate_the_danubian_ally': 'GFX_focus_GER_the_central_powers',
    'GER_hegemon_of_continental_europe': 'GFX_focus_GER_ww1_hohenzollern_imperial_hegemony',

    # Lane 4: Pan-German Radical Right / Vaterlandspartei (19)
    'GER_found_vaterlandspartei': 'GFX_focus_GER_found_vaterlandspartei',
    'GER_kapp_and_tirpitz_rally': 'GFX_GER_DVLP',
    'GER_dissolve_the_reichstag': 'GFX_GER_DkP',
    'GER_smash_general_strikes': 'GFX_focus_GER_rapid_army_expansion',
    'GER_militarize_the_entire_society': 'GFX_GER_Expand_Kriegsschule',
    'GER_siegfrieden_manifesto': 'GFX_focus_GER_ww1_siegfrieden_peace_with_france',
    'GER_alldeutscher_verband_hegemony': 'GFX_focus_GER_monarchist_sentiment',
    'GER_autarkic_industrial_trusts': 'GFX_GER_Thyssen_Pact',
    'GER_crush_marxism_and_defeatism': 'GFX_focus_GER_totaler_krieg',
    # Lane 4 Invasions & Conquistas Diplomaticas
    'GER_annex_the_flemish_coast': 'GFX_focus_GER_seeherrschaft',
    'GER_colonize_the_eastern_frontier_strip': 'GFX_focus_GER_ww1_baltic_german_colonization_order',
    'GER_baltic_crusade_landeswehr': 'GFX_focus_GER_subduing_the_baltic_states',
    'GER_crush_netherlands_neutrality': 'GFX_focus_GER_west_wall',
    'GER_pan_german_settlement_east': 'GFX_focus_GER_restore_the_brest_litovsk_borders',
    'GER_subjugate_scandinavia': 'GFX_focus_GER_the_northern_shield',
    'GER_annex_french_iron_and_channel_ports': 'GFX_focus_GER_rhineland',
    'GER_conquer_transcaucasia_oil': 'GFX_focus_GER_ww1_caucasus_baku_expedition',
    'GER_mittelafrika_total_empire': 'GFX_focus_GER_realize_mittelafrika',
    'GER_unconditional_victory_or_ruin': 'GFX_focus_GER_ww1_unconditional_victory_or_ruin',
}

print(f'Total mapped focuses: {len(focus_sprites)}')
unmatched = [fid for fid, s in focus_sprites.items() if s not in sprites]
print(f'Unmatched sprites: {len(unmatched)}')
if unmatched:
    for fid in unmatched:
        print(f'  {fid} -> {focus_sprites[fid]} NOT IN SPRITES')
else:
    print('ALL 83 FOCUSES HAVE 100% VALID, EXISTING SPRITES IN DATABASE!')
