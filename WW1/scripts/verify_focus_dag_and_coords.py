# Full definition of focuses: (id, x, y, cost, prereqs, mut_ex, sprite)
focuses_def = [
    # Trunk (7)
    ('GER_kaiser_wilhelm_personal_rule', 10, 0, 5, [], [], 'GFX_focus_GER_constitutional_monarchy_proclamation'),
    ('GER_reichstag_1912_elections', 10, 1, 5, ['GER_kaiser_wilhelm_personal_rule'], [], 'GFX_GER_Reichstag'),
    ('GER_centenary_of_leipzig_1913', 10, 2, 5, ['GER_reichstag_1912_elections'], [], 'GFX_focus_GER_centenary_of_leipzig_1913'),
    ('GER_reichstag_social_concessions', 8, 3, 7, ['GER_centenary_of_leipzig_1913'], ['GER_appease_the_junkers'], 'GFX_focus_GER_workers_rights'),
    ('GER_appease_the_junkers', 12, 3, 7, ['GER_centenary_of_leipzig_1913'], ['GER_reichstag_social_concessions'], 'GFX_GER_Prussian_Zentrum'),
    ('GER_prussian_franchise_debate', 10, 4, 7, [['GER_reichstag_social_concessions', 'GER_appease_the_junkers']], [], 'GFX_focus_GER_strive_for_conservative_values'),
    ('GER_burgfrieden_declaration_1914', 10, 5, 5, ['GER_prussian_franchise_debate'], [], 'GFX_focus_GER_rally_the_nation'),

    # Lane 1: Spartakusbund & Workers' Councils (19)
    ('GER_spartakusbund_proletarian_revolt', 2, 6, 10, ['GER_burgfrieden_declaration_1914'], ['GER_prussian_franchise_reform', 'GER_silent_dictatorship_ohl', 'GER_found_vaterlandspartei'], 'GFX_focus_GER_start_the_proletarian_revolution'),
    ('GER_kiel_sailors_mutiny', 0, 7, 7, ['GER_spartakusbund_proletarian_revolt'], [], 'GFX_focus_GER_ww1_kiel_sailors_mutiny'),
    ('GER_proclaim_freie_sozialistische_republik', 2, 7, 7, ['GER_spartakusbund_proletarian_revolt'], [], 'GFX_focus_GER_proletarian_solidarity'),
    ('GER_berlin_january_mass_strikes', 4, 7, 7, ['GER_spartakusbund_proletarian_revolt'], [], 'GFX_focus_GER_support_the_proletarian_uprising'),
    ('GER_soldiers_and_workers_councils', 1, 8, 7, ['GER_kiel_sailors_mutiny', 'GER_proclaim_freie_sozialistische_republik'], [], 'GFX_GER_SPD'),
    ('GER_volksmarinedivision_guard', 3, 8, 7, ['GER_proclaim_freie_sozialistische_republik', 'GER_berlin_january_mass_strikes'], [], 'GFX_focus_GER_marinestosstrupp'),
    ('GER_dissolve_the_junker_officer_caste', 0, 9, 7, ['GER_soldiers_and_workers_councils'], [], 'GFX_focus_GER_root_out_imperialism'),
    ('GER_socialist_land_and_factory_collectivization', 2, 9, 7, ['GER_soldiers_and_workers_councils', 'GER_volksmarinedivision_guard'], [], 'GFX_focus_GER_social_ownership'),
    ('GER_rote_ruhrarmee_formation', 4, 9, 7, ['GER_volksmarinedivision_guard'], [], 'GFX_focus_GER_ressurect_the_red_front_fighters_league'),
    ('GER_red_high_seas_fleet', 0, 10, 7, ['GER_dissolve_the_junker_officer_caste'], [], 'GFX_focus_GER_rebuild_the_high_seas_fleet'),
    ('GER_alliance_with_soviet_russia', 1, 10, 7, ['GER_dissolve_the_junker_officer_caste', 'GER_socialist_land_and_factory_collectivization'], [], 'GFX_focus_GER_ww1_alliance_with_soviet_russia'),
    ('GER_council_economic_planning', 2, 10, 7, ['GER_socialist_land_and_factory_collectivization'], [], 'GFX_focus_GER_optimize_reich_labour_service'),
    ('GER_soviet_military_advisors', 3, 10, 7, ['GER_socialist_land_and_factory_collectivization', 'GER_rote_ruhrarmee_formation'], [], 'GFX_focus_GER_pool_technical_know_how'),
    ('GER_red_baltic_intervention', 0, 11, 7, ['GER_red_high_seas_fleet', 'GER_alliance_with_soviet_russia'], [], 'GFX_focus_GER_subduing_the_baltic_states'),
    ('GER_liberate_the_polish_proletariat', 1, 11, 7, ['GER_alliance_with_soviet_russia'], [], 'GFX_focus_wake_up_poland'),
    ('GER_danubian_soviet_federation', 2, 11, 7, ['GER_alliance_with_soviet_russia', 'GER_council_economic_planning'], [], 'GFX_focus_GER_the_austrian_question'),
    ('GER_liberate_the_balkans_workers', 3, 11, 7, ['GER_soviet_military_advisors'], [], 'GFX_focus_GER_sway_the_balkans'),
    ('GER_export_revolution_to_france', 4, 11, 7, ['GER_rote_ruhrarmee_formation', 'GER_soviet_military_advisors'], [], 'GFX_focus_GER_war_with_france'),
    ('GER_world_proletarian_revolution', 2, 12, 10, ['GER_liberate_the_polish_proletariat', 'GER_danubian_soviet_federation', 'GER_export_revolution_to_france'], [], 'GFX_focus_GER_ww1_world_proletarian_revolution'),

    # Lane 2: Democratic Reform & Republic (19)
    ('GER_prussian_franchise_reform', 7, 6, 10, ['GER_burgfrieden_declaration_1914'], ['GER_spartakusbund_proletarian_revolt', 'GER_silent_dictatorship_ohl', 'GER_found_vaterlandspartei'], 'GFX_focus_GER_prussian_franchise_reform'),
    ('GER_prince_max_von_baden_cabinet', 6, 7, 7, ['GER_prussian_franchise_reform'], [], 'GFX_focus_GER_ww1_prince_max_von_baden_cabinet'),
    ('GER_proclaim_deutsche_republik', 8, 7, 7, ['GER_prussian_franchise_reform'], [], 'GFX_focus_GER_reestablish_free_elections'),
    ('GER_repeal_anti_socialist_heritage', 5, 8, 7, ['GER_prince_max_von_baden_cabinet'], [], 'GFX_focus_GER_ww1_repeal_anti_socialist_heritage'),
    ('GER_antinationalist_civil_defense', 7, 8, 7, ['GER_prince_max_von_baden_cabinet', 'GER_proclaim_deutsche_republik'], [], 'GFX_focus_GER_tend_to_the_future_of_germany'),
    ('GER_stinnes_legien_social_compromise', 9, 8, 7, ['GER_proclaim_deutsche_republik'], [], 'GFX_GER_Binnenwirtschaft'),
    ('GER_rathenau_industrial_reorganization', 5, 9, 7, ['GER_repeal_anti_socialist_heritage'], [], 'GFX_GER_Rathenauplan'),
    ('GER_weimar_national_assembly', 7, 9, 7, ['GER_antinationalist_civil_defense'], [], 'GFX_focus_GER_reichstag'),
    ('GER_zentrum_concordat_with_rome', 9, 9, 7, ['GER_stinnes_legien_social_compromise'], [], 'GFX_GER_Zentrum'),
    ('GER_post_war_welfare_and_reconstruction', 6, 10, 7, ['GER_rathenau_industrial_reorganization', 'GER_weimar_national_assembly'], [], 'GFX_focus_GER_strengthen_the_welfare_state'),
    ('GER_federal_constitutional_balance', 8, 10, 7, ['GER_weimar_national_assembly', 'GER_zentrum_concordat_with_rome'], [], 'GFX_focus_GER_ww1_federal_constitutional_monarchy'),
    ('GER_direct_negotiations_with_woodrow_wilson', 7, 10, 7, ['GER_weimar_national_assembly'], [], 'GFX_focus_GER_ww1_ambassador_bernstorff_us_lobby'),
    ('GER_alsace_lorraine_plebiscite', 5, 11, 7, ['GER_post_war_welfare_and_reconstruction', 'GER_direct_negotiations_with_woodrow_wilson'], [], 'GFX_focus_GER_reintegrate_luxemburg_and_alsace_lorraine'),
    ('GER_democratic_mitteleuropa_union', 6, 11, 7, ['GER_direct_negotiations_with_woodrow_wilson'], [], 'GFX_focus_GER_mitteleuropa_cooperation_sphere'),
    ('GER_subjugate_luxembourg_customs', 8, 11, 7, ['GER_direct_negotiations_with_woodrow_wilson', 'GER_federal_constitutional_balance'], [], 'GFX_focus_GER_low_countries_membership'),
    ('GER_nordic_democratic_trade_compact', 9, 11, 7, ['GER_federal_constitutional_balance'], [], 'GFX_focus_GER_swedish_trade_agreement'),
    ('GER_guarantee_independent_poland_buffer', 6, 12, 7, ['GER_democratic_mitteleuropa_union'], [], 'GFX_focus_GER_reassert_eastern_claims'),
    ('GER_baltic_democratic_confederation', 8, 12, 7, ['GER_subjugate_luxembourg_customs', 'GER_nordic_democratic_trade_compact'], [], 'GFX_focus_GER_safeguard_the_baltic'),
    ('GER_pan_european_arbitration_league', 7, 13, 10, ['GER_guarantee_independent_poland_buffer', 'GER_baltic_democratic_confederation'], [], 'GFX_focus_generic_world_peace'),

    # Lane 3: OHL Military Dictatorship (19)
    ('GER_silent_dictatorship_ohl', 12, 6, 10, ['GER_burgfrieden_declaration_1914'], ['GER_spartakusbund_proletarian_revolt', 'GER_prussian_franchise_reform', 'GER_found_vaterlandspartei'], 'GFX_focus_GER_silent_dictatorship_ohl'),
    ('GER_oust_bethmann_hollweg', 10, 7, 7, ['GER_silent_dictatorship_ohl'], [], 'GFX_focus_GER_ww1_oust_bethmann_hollweg'),
    ('GER_hindenburg_program_mobilization', 12, 7, 7, ['GER_silent_dictatorship_ohl'], [], 'GFX_focus_GER_ww1_falkenhayn_dismissal_third_ohl'),
    ('GER_patriotic_auxiliary_service_law', 14, 7, 7, ['GER_silent_dictatorship_ohl'], [], 'GFX_GER_Freiwilliger_Arbeitsdienst'),
    ('GER_krupp_ordnance_dictate', 10, 8, 7, ['GER_oust_bethmann_hollweg'], [], 'GFX_focus_GER_ww1_krupp_heavy_ordnance_contracts'),
    ('GER_total_war_patriotism_kriegsanleihen', 12, 8, 7, ['GER_hindenburg_program_mobilization'], [], 'GFX_GER_Ufa_War_Propaganda'),
    ('GER_sturmtruppen_doctrine_offensive', 14, 8, 7, ['GER_patriotic_auxiliary_service_law'], [], 'GFX_GER_Sturmtruppen'),
    ('GER_subjugate_the_reichstag_politicians', 10, 9, 7, ['GER_krupp_ordnance_dictate'], [], 'GFX_focus_GER_total_control_over_domestic_affairs'),
    ('GER_septemberprogramm_war_aims', 12, 9, 7, ['GER_total_war_patriotism_kriegsanleihen'], [], 'GFX_focus_GER_spheres_of_influence'),
    ('GER_unrestricted_submarine_mobilization', 14, 9, 7, ['GER_sturmtruppen_doctrine_offensive'], [], 'GFX_focus_GER_unrestricted_submarine_warfare'),
    ('GER_annexation_of_belgium_and_briey', 10, 10, 7, ['GER_subjugate_the_reichstag_politicians', 'GER_septemberprogramm_war_aims'], [], 'GFX_focus_GER_annexation_of_belgium_and_briey'),
    ('GER_subjugate_romanian_ploesti_oil', 12, 10, 7, ['GER_septemberprogramm_war_aims'], [], 'GFX_focus_GER_subjugate_romanian_economy'),
    ('GER_brest_litovsk_carve_up', 14, 10, 7, ['GER_septemberprogramm_war_aims', 'GER_unrestricted_submarine_mobilization'], [], 'GFX_focus_GER_ww1_treaty_of_brest_litovsk'),
    ('GER_establish_generalgouvernement_warschau', 10, 11, 7, ['GER_annexation_of_belgium_and_briey'], [], 'GFX_focus_GER_see_to_the_eastern_front'),
    ('GER_finnish_intervention_von_der_goltz', 12, 11, 7, ['GER_subjugate_romanian_ploesti_oil', 'GER_brest_litovsk_carve_up'], [], 'GFX_focus_GER_support_finland'),
    ('GER_carve_ukrainian_breadbasket', 14, 11, 7, ['GER_brest_litovsk_carve_up'], [], 'GFX_focus_HUN_the_kingdom_of_ukraine'),
    ('GER_operation_faustschlag_crusade', 11, 12, 7, ['GER_establish_generalgouvernement_warschau', 'GER_finnish_intervention_von_der_goltz'], [], 'GFX_focus_GER_strike_eastward'),
    ('GER_subjugate_the_danubian_ally', 13, 12, 7, ['GER_finnish_intervention_von_der_goltz', 'GER_carve_ukrainian_breadbasket'], [], 'GFX_focus_GER_the_central_powers'),
    ('GER_hegemon_of_continental_europe', 12, 13, 10, ['GER_operation_faustschlag_crusade', 'GER_subjugate_the_danubian_ally'], [], 'GFX_focus_GER_ww1_hohenzollern_imperial_hegemony'),

    # Lane 4: Pan-German Radical Right / Vaterlandspartei (19)
    ('GER_found_vaterlandspartei', 17, 6, 10, ['GER_burgfrieden_declaration_1914'], ['GER_spartakusbund_proletarian_revolt', 'GER_prussian_franchise_reform', 'GER_silent_dictatorship_ohl'], 'GFX_focus_GER_found_vaterlandspartei'),
    ('GER_kapp_and_tirpitz_rally', 15, 7, 7, ['GER_found_vaterlandspartei'], [], 'GFX_GER_DVLP'),
    ('GER_militarize_the_entire_society', 17, 7, 7, ['GER_found_vaterlandspartei'], [], 'GFX_GER_Expand_Kriegsschule'),
    ('GER_dissolve_the_reichstag', 19, 7, 7, ['GER_found_vaterlandspartei'], [], 'GFX_GER_DkP'),
    ('GER_smash_general_strikes', 15, 8, 7, ['GER_kapp_and_tirpitz_rally'], [], 'GFX_focus_GER_rapid_army_expansion'),
    ('GER_alldeutscher_verband_hegemony', 17, 8, 7, ['GER_militarize_the_entire_society'], [], 'GFX_focus_GER_monarchist_sentiment'),
    ('GER_siegfrieden_manifesto', 19, 8, 7, ['GER_dissolve_the_reichstag'], [], 'GFX_focus_GER_ww1_siegfrieden_peace_with_france'),
    ('GER_autarkic_industrial_trusts', 16, 9, 7, ['GER_smash_general_strikes', 'GER_alldeutscher_verband_hegemony'], [], 'GFX_GER_Thyssen_Pact'),
    ('GER_crush_marxism_and_defeatism', 18, 9, 7, ['GER_alldeutscher_verband_hegemony', 'GER_siegfrieden_manifesto'], [], 'GFX_focus_GER_totaler_krieg'),
    ('GER_annex_the_flemish_coast', 15, 10, 7, ['GER_autarkic_industrial_trusts'], [], 'GFX_focus_GER_seeherrschaft'),
    ('GER_colonize_the_eastern_frontier_strip', 17, 10, 7, ['GER_autarkic_industrial_trusts', 'GER_crush_marxism_and_defeatism'], [], 'GFX_focus_GER_ww1_baltic_german_colonization_order'),
    ('GER_baltic_crusade_landeswehr', 19, 10, 7, ['GER_crush_marxism_and_defeatism'], [], 'GFX_focus_GER_subduing_the_baltic_states'),
    ('GER_crush_netherlands_neutrality', 15, 11, 7, ['GER_annex_the_flemish_coast'], [], 'GFX_focus_GER_west_wall'),
    ('GER_pan_german_settlement_east', 17, 11, 7, ['GER_colonize_the_eastern_frontier_strip'], [], 'GFX_focus_GER_restore_the_brest_litovsk_borders'),
    ('GER_subjugate_scandinavia', 19, 11, 7, ['GER_baltic_crusade_landeswehr'], [], 'GFX_focus_GER_the_northern_shield'),
    ('GER_annex_french_iron_and_channel_ports', 16, 12, 7, ['GER_crush_netherlands_neutrality', 'GER_pan_german_settlement_east'], [], 'GFX_focus_GER_rhineland'),
    ('GER_conquer_transcaucasia_oil', 18, 12, 7, ['GER_pan_german_settlement_east', 'GER_subjugate_scandinavia'], [], 'GFX_focus_GER_ww1_caucasus_baku_expedition'),
    ('GER_mittelafrika_total_empire', 17, 12, 7, ['GER_annex_french_iron_and_channel_ports', 'GER_conquer_transcaucasia_oil'], [], 'GFX_focus_GER_realize_mittelafrika'),
    ('GER_unconditional_victory_or_ruin', 17, 13, 10, ['GER_mittelafrika_total_empire'], [], 'GFX_focus_GER_ww1_unconditional_victory_or_ruin'),
]

# Validation
ids = set()
coords = {}
errors = []

for item in focuses_def:
    fid, x, y, cost, prereqs, mut, sprite = item
    if fid in ids:
        errors.append(f"Duplicate ID: {fid}")
    ids.add(fid)
    if (x, y) in coords:
        errors.append(f"Coordinate collision at ({x}, {y}): {fid} and {coords[(x, y)]}")
    coords[(x, y)] = fid

# Check prereqs
for item in focuses_def:
    fid, x, y, cost, prereqs, mut, sprite = item
    for p in prereqs:
        if isinstance(p, list):
            for sub_p in p:
                if sub_p not in ids:
                    errors.append(f"Missing prereq {sub_p} for {fid}")
        else:
            if p not in ids:
                errors.append(f"Missing prereq {p} for {fid}")

# Check mut_ex
for item in focuses_def:
    fid, x, y, cost, prereqs, mut, sprite = item
    for m in mut:
        if m not in ids:
            errors.append(f"Missing mut_ex {m} for {fid}")

print(f"Total focuses: {len(focuses_def)}")
print(f"Total coordinates: {len(coords)}")
if errors:
    print("ERRORS:")
    for e in errors:
        print("  ", e)
else:
    print("VALIDATION SUCCESS: 0 coordinate collisions, 0 missing prereqs, 0 missing mutual exclusions!")
