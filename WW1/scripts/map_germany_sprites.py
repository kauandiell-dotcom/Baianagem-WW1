import re

with open('scripts/all_normal_germany_sprites.txt', 'r', encoding='utf-8') as f:
    sprites = set(line.strip() for line in f if line.strip())

planned_focuses = [
    # Trunk
    'GER_kaiser_wilhelm_personal_rule',
    'GER_reichstag_1912_elections',
    'GER_centenary_of_leipzig_1913',
    'GER_reichstag_social_concessions',
    'GER_appease_the_junkers',
    'GER_prussian_franchise_debate',
    'GER_burgfrieden_declaration_1914',
    # Lane 1
    'GER_spartakusbund_proletarian_revolt',
    'GER_kiel_sailors_mutiny',
    'GER_berlin_january_mass_strikes',
    'GER_proclaim_freie_sozialistische_republik',
    'GER_soldiers_and_workers_councils',
    'GER_volksmarinedivision_guard',
    'GER_dissolve_the_junker_officer_caste',
    'GER_socialist_land_and_factory_collectivization',
    'GER_rote_ruhrarmee_formation',
    'GER_council_economic_planning',
    'GER_red_high_seas_fleet',
    'GER_alliance_with_soviet_russia',
    'GER_soviet_military_advisors',
    'GER_red_baltic_intervention',
    'GER_liberate_the_polish_proletariat',
    'GER_danubian_soviet_federation',
    'GER_liberate_the_balkans_workers',
    'GER_export_revolution_to_france',
    'GER_world_proletarian_revolution',
    # Lane 2
    'GER_prussian_franchise_reform',
    'GER_prince_max_von_baden_cabinet',
    'GER_proclaim_deutsche_republik',
    'GER_repeal_anti_socialist_heritage',
    'GER_antinationalist_civil_defense',
    'GER_stinnes_legien_social_compromise',
    'GER_rathenau_industrial_reorganization',
    'GER_weimar_national_assembly',
    'GER_zentrum_concordat_with_rome',
    'GER_post_war_welfare_and_reconstruction',
    'GER_federal_constitutional_balance',
    'GER_direct_negotiations_with_woodrow_wilson',
    'GER_alsace_lorraine_plebiscite',
    'GER_democratic_mitteleuropa_union',
    'GER_subjugate_luxembourg_customs',
    'GER_nordic_democratic_trade_compact',
    'GER_guarantee_independent_poland_buffer',
    'GER_baltic_democratic_confederation',
    'GER_pan_european_arbitration_league',
    # Lane 3
    'GER_silent_dictatorship_ohl',
    'GER_oust_bethmann_hollweg',
    'GER_hindenburg_program_mobilization',
    'GER_patriotic_auxiliary_service_law',
    'GER_krupp_ordnance_dictate',
    'GER_total_war_patriotism_kriegsanleihen',
    'GER_sturmtruppen_doctrine_offensive',
    'GER_subjugate_the_reichstag_politicians',
    'GER_unrestricted_submarine_mobilization',
    'GER_septemberprogramm_war_aims',
    'GER_annexation_of_belgium_and_briey',
    'GER_subjugate_romanian_ploesti_oil',
    'GER_brest_litovsk_carve_up',
    'GER_establish_generalgouvernement_warschau',
    'GER_finnish_intervention_von_der_goltz',
    'GER_carve_ukrainian_breadbasket',
    'GER_operation_faustschlag_crusade',
    'GER_subjugate_the_danubian_ally',
    'GER_hegemon_of_continental_europe',
    # Lane 4
    'GER_found_vaterlandspartei',
    'GER_kapp_and_tirpitz_rally',
    'GER_dissolve_the_reichstag',
    'GER_smash_general_strikes',
    'GER_militarize_the_entire_society',
    'GER_siegfrieden_manifesto',
    'GER_alldeutscher_verband_hegemony',
    'GER_autarkic_industrial_trusts',
    'GER_crush_marxism_and_defeatism',
    'GER_annex_the_flemish_coast',
    'GER_colonize_the_eastern_frontier_strip',
    'GER_baltic_crusade_landeswehr',
    'GER_crush_netherlands_neutrality',
    'GER_pan_german_settlement_east',
    'GER_subjugate_scandinavia',
    'GER_annex_french_iron_and_channel_ports',
    'GER_conquer_transcaucasia_oil',
    'GER_mittelafrika_total_empire',
    'GER_unconditional_victory_or_ruin',
]

print(f'Total planned focuses: {len(planned_focuses)}')

matches = {}
missing = []

for fid in planned_focuses:
    candidates = [
        f'GFX_focus_{fid}',
        f'GFX_{fid}',
        f'GFX_{fid.replace("GER_", "")}',
    ]
    found = None
    for c in candidates:
        if c in sprites:
            found = c
            break
    if found:
        matches[fid] = found
    else:
        missing.append(fid)

print(f'Direct matches found: {len(matches)}')
print(f'Missing direct matches: {len(missing)}')
if missing:
    print('Missing sample:', missing[:10])
