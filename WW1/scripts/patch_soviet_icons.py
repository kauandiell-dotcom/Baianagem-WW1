import os

p = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\common\national_focus\soviet_russia.txt"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    'id = SOV_the_red_terror\n\t\ticon = GFX_focus_sov_great_purge': 'id = SOV_the_red_terror\n\t\ticon = GFX_SOV_red_terror',
    'id = SOV_nationalization_of_heavy_industry\n\t\ticon = GFX_goal_generic_soviet_construction': 'id = SOV_nationalization_of_heavy_industry\n\t\ticon = GFX_SOV_expand_industrialization',
    'id = SOV_worker_food_rationing_cards\n\t\ticon = GFX_goal_generic_production': 'id = SOV_worker_food_rationing_cards\n\t\ticon = GFX_SOV_grain_requisition_brigades',
    'id = SOV_eradicate_counter_revolutionary_cells\n\t\ticon = GFX_goal_generic_intelligence_exchange': 'id = SOV_eradicate_counter_revolutionary_cells\n\t\ticon = GFX_SOV_cheka_revolutionary_tribunal',
    'id = SOV_conscription_of_the_toilers\n\t\ticon = GFX_goal_generic_allies_build_infantry': 'id = SOV_conscription_of_the_toilers\n\t\ticon = GFX_SOV_workers_and_peasants_red_army',
    'id = SOV_arsenals_of_tula_and_izhevsk\n\t\ticon = GFX_goal_generic_construct_mil_factory': 'id = SOV_arsenals_of_tula_and_izhevsk\n\t\ticon = GFX_SOV_tula_arms_plant',
    'id = SOV_shaturskaya_power_station\n\t\ticon = GFX_goal_generic_construct_civ_factory': 'id = SOV_shaturskaya_power_station\n\t\ticon = GFX_SOV_goelro_plan',
    'id = SOV_reopen_the_donbass_coalfields\n\t\ticon = GFX_goal_generic_soviet_construction': 'id = SOV_reopen_the_donbass_coalfields\n\t\ticon = GFX_SOV_superindustrialization',
    'id = SOV_baku_oil_syndicate\n\t\ticon = GFX_goal_generic_oil_refinery': 'id = SOV_baku_oil_syndicate\n\t\ticon = GFX_focus_AUS_the_matzen_oil_fields',
    'id = SOV_stabilize_the_soviet_chervonets\n\t\ticon = GFX_goal_generic_trade': 'id = SOV_stabilize_the_soviet_chervonets\n\t\ticon = GFX_RUS_Strong_Currency',
    'id = SOV_state_industrial_monopolies\n\t\ticon = GFX_goal_generic_soviet_construction': 'id = SOV_state_industrial_monopolies\n\t\ticon = GFX_SOV_superindustrialization',
    'id = SOV_ural_kuznetsk_combine\n\t\ticon = GFX_goal_generic_construct_mil_factory': 'id = SOV_ural_kuznetsk_combine\n\t\ticon = GFX_SOV_izhevsk_machinebuilding_plant',
    'id = SOV_twenty_one_conditions\n\t\ticon = GFX_focus_sov_the_hands_do': 'id = SOV_twenty_one_conditions\n\t\ticon = GFX_SOV_third_international_comintern',
    'id = SOV_ignite_the_western_flame\n\t\ticon = GFX_goal_generic_propaganda': 'id = SOV_ignite_the_western_flame\n\t\ticon = GFX_goal_ww1_ITA_ww1_propaganda_service',
    'id = SOV_proclaim_the_curzon_line\n\t\ticon = GFX_goal_generic_military_sphere': 'id = SOV_proclaim_the_curzon_line\n\t\ticon = GFX_SOV_tukhachevsky_deep_battle',
    'id = SOV_aid_to_anatolian_nationalists\n\t\ticon = GFX_goal_generic_scientific_exchange': 'id = SOV_aid_to_anatolian_nationalists\n\t\ticon = GFX_RUS_Russo_German_Diplomacy',
    'id = SOV_the_genoa_conference_diplomacy\n\t\ticon = GFX_goal_generic_trade': 'id = SOV_the_genoa_conference_diplomacy\n\t\ticon = GFX_focus_generic_diplomatic_treaty',
    'id = SOV_tomka_chemical_weapons_testing\n\t\ticon = GFX_goal_generic_secret_weapon': 'id = SOV_tomka_chemical_weapons_testing\n\t\ticon = GFX_SOV_tsar_tank',
    'id = SOV_sovietization_of_belarus\n\t\ticon = GFX_focus_sov_the_hands_do': 'id = SOV_sovietization_of_belarus\n\t\ticon = GFX_SOV_autonomous_republics',
    'id = SOV_the_likbez_literacy_campaign\n\t\ticon = GFX_goal_generic_scientific_exchange': 'id = SOV_the_likbez_literacy_campaign\n\t\ticon = GFX_GER_research_funding',
    'id = SOV_the_1924_soviet_constitution\n\t\ticon = GFX_focus_sov_the_supreme_soviet': 'id = SOV_the_1924_soviet_constitution\n\t\ticon = GFX_SOV_treaty_of_the_creation_of_the_ussr',
    'id = SOV_emancipation_of_women_zhenotdel\n\t\ticon = GFX_goal_generic_national_unity': 'id = SOV_emancipation_of_women_zhenotdel\n\t\ticon = GFX_focus_RUS_womens_battalion'
}

count = 0
for k, v in replacements.items():
    if k in text:
        text = text.replace(k, v)
        count += 1
    else:
        print(f"FAILED TO MATCH: {k}")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Applied {count}/{len(replacements)} icon replacements to soviet_russia.txt successfully!")
