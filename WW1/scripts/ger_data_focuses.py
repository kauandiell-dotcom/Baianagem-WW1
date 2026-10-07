# -*- coding: utf-8 -*-
"""Focus definitions for Germany Politics & Society Wing (83 focuses)."""

FOCUSES = [
    {
        'id': 'GER_kaiser_wilhelm_personal_rule',
        'x': 10, 'y': 0, 'cost': 5,
        'prereqs': [],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_constitutional_monarchy_proclamation',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_political_power = 80
			add_stability = 0.05
			set_country_flag = GER_personal_rule_active
			add_ideas = GER_wilhelmine_personal_regime
			hidden_effect = {
				set_country_flag = GER_ww1_focus_tree_initialized
			}''',
    },
    {
        'id': 'GER_reichstag_1912_elections',
        'x': 10, 'y': 1, 'cost': 5,
        'prereqs': ['GER_kaiser_wilhelm_personal_rule'],
        'mut_ex': [],
        'icon': 'GFX_GER_Reichstag',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.201 }
			add_political_power = 60
			add_popularity = { ideology = democratic popularity = 0.05 }''',
    },
    {
        'id': 'GER_volkerschlacht_centenary_1913',
        'x': 10, 'y': 2, 'cost': 5,
        'prereqs': ['GER_reichstag_1912_elections'],
        'mut_ex': [],
        'icon': 'GFX_AUS_1913_acts_of_protection',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_war_support = 0.05
			add_stability = 0.05
			add_timed_idea = { idea = GER_volkerschlacht_spirit days = 360 }''',
    },
    {
        'id': 'GER_reichstag_social_concessions',
        'x': 8, 'y': 3, 'cost': 7,
        'prereqs': ['GER_volkerschlacht_centenary_1913'],
        'mut_ex': ['GER_appease_the_junkers'],
        'icon': 'GFX_focus_GER_workers_rights',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.05
			add_popularity = { ideology = democratic popularity = 0.08 }
			add_popularity = { ideology = communism popularity = 0.04 }
			swap_ideas = {
				remove_idea = GER_wilhelmine_personal_regime
				add_idea = GER_wilhelmine_reform_regime
			}''',
    },
    {
        'id': 'GER_appease_the_junkers',
        'x': 12, 'y': 3, 'cost': 7,
        'prereqs': ['GER_volkerschlacht_centenary_1913'],
        'mut_ex': ['GER_reichstag_social_concessions'],
        'icon': 'GFX_GER_Prussian_Zentrum',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_political_power = 100
			add_war_support = 0.05
			add_popularity = { ideology = neutrality popularity = 0.10 }
			set_country_flag = GER_junkers_appeased''',
    },
    {
        'id': 'GER_prussian_franchise_debate',
        'x': 10, 'y': 4, 'cost': 7,
        'prereqs': [['GER_reichstag_social_concessions', 'GER_appease_the_junkers']],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_strive_for_conservative_values',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.202 }
			add_political_power = 50''',
    },
    {
        'id': 'GER_burgfrieden_declaration_1914',
        'x': 10, 'y': 5, 'cost': 5,
        'prereqs': ['GER_prussian_franchise_debate'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_rally_the_nation',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_war_support = 0.10
			add_timed_idea = { idea = GER_burgfrieden_1914 days = 720 }
			set_country_flag = GER_burgfrieden_enacted''',
    },
    {
        'id': 'GER_spartakusbund_proletarian_revolt',
        'x': 2, 'y': 6, 'cost': 10,
        'prereqs': ['GER_burgfrieden_declaration_1914'],
        'mut_ex': ['GER_prussian_franchise_reform', 'GER_silent_dictatorship_ohl', 'GER_found_vaterlandspartei'],
        'icon': 'GFX_focus_GER_start_the_proletarian_revolution',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''country_event = { id = ww1_germany_events.210 }
			set_country_flag = GER_spartakus_revolution_unleashed
			add_popularity = { ideology = communism popularity = 0.20 }
			add_stability = -0.10''',
    },
    {
        'id': 'GER_kiel_sailors_revolt',
        'x': 0, 'y': 7, 'cost': 7,
        'prereqs': ['GER_spartakusbund_proletarian_revolt'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_navy',
        'filters': ['FOCUS_FILTER_MANPOWER', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''country_event = { id = ww1_germany_events.211 }
			add_war_support = 0.05
			navy_experience = 25
			random_owned_controlled_state = {
				limit = { state = 58 } # Schleswig-Holstein
				create_unit = {
					division = "name = \\"1. Rote Marine-Division\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
			}''',
    },
    {
        'id': 'GER_proclaim_freie_sozialistische_republik',
        'x': 2, 'y': 7, 'cost': 7,
        'prereqs': ['GER_spartakusbund_proletarian_revolt'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_proletarian_solidarity',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.212 }
			set_politics = {
				ruling_party = communism
				elections_allowed = no
			}
			add_popularity = { ideology = communism popularity = 0.30 }
			add_stability = 0.05''',
    },
    {
        'id': 'GER_berlin_january_mass_strikes',
        'x': 4, 'y': 7, 'cost': 7,
        'prereqs': ['GER_spartakusbund_proletarian_revolt'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_support_the_proletarian_uprising',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_political_power = 60
			add_popularity = { ideology = communism popularity = 0.10 }
			set_country_flag = GER_january_strikes_victorious''',
    },
    {
        'id': 'GER_soldiers_and_workers_councils',
        'x': 1, 'y': 8, 'cost': 7,
        'prereqs': ['GER_kiel_sailors_revolt', 'GER_proclaim_freie_sozialistische_republik'],
        'mut_ex': [],
        'icon': 'GFX_GER_SPD',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_ideas = GER_rate_republik
			add_political_power = 75
			set_country_flag = GER_council_power_consolidated''',
    },
    {
        'id': 'GER_volksmarinedivision_guard',
        'x': 3, 'y': 8, 'cost': 7,
        'prereqs': ['GER_proclaim_freie_sozialistische_republik', 'GER_berlin_january_mass_strikes'],
        'mut_ex': [],
        'icon': 'GFX_GER_Deutsche_Luftflotte',
        'filters': ['FOCUS_FILTER_MANPOWER', 'FOCUS_FILTER_ARMY_XP'],
        'reward': '''army_experience = 35
			64 = { # Brandenburg / Berlin
				create_unit = {
					division = "name = \\"Volksmarinedivision Berlin\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.4"
					owner = GER
				}
				create_unit = {
					division = "name = \\"Rote Garde Berlin\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
			}''',
    },
    {
        'id': 'GER_dissolve_the_junker_officer_caste',
        'x': 0, 'y': 9, 'cost': 7,
        'prereqs': ['GER_soldiers_and_workers_councils'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_root_out_imperialism',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_ideas = GER_red_commissars
			add_political_power = 50
			add_stability = -0.05
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_socialist_land_and_factory_collectivization',
        'x': 2, 'y': 9, 'cost': 7,
        'prereqs': ['GER_soldiers_and_workers_councils', 'GER_volksmarinedivision_guard'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_social_ownership',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''64 = { # Brandenburg
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 2
					instant_build = yes
				}
			}
			57 = { # Westfalen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 2
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_rote_ruhrarmee_formation',
        'x': 4, 'y': 9, 'cost': 7,
        'prereqs': ['GER_volksmarinedivision_guard'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ressurect_the_red_front_fighters_league',
        'filters': ['FOCUS_FILTER_MANPOWER', 'FOCUS_FILTER_ARMY_XP'],
        'reward': '''add_ideas = GER_ruhr_proletariat
			army_experience = 25
			57 = { # Westfalen
				create_unit = {
					division = "name = \\"1. Rote Ruhrarmee-Division\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
				create_unit = {
					division = "name = \\"2. Rote Ruhrarmee-Division\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
			}''',
    },
    {
        'id': 'GER_red_high_seas_fleet',
        'x': 0, 'y': 10, 'cost': 7,
        'prereqs': ['GER_dissolve_the_junker_officer_caste'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_rebuild_the_high_seas_fleet',
        'filters': ['FOCUS_FILTER_NAVY_XP'],
        'reward': '''navy_experience = 40
			add_doctrine_cost_reduction = {
				name = red_fleet_doctrine
				cost_reduction = 0.5
				uses = 2
				category = naval_doctrine
			}''',
    },
    {
        'id': 'GER_alliance_with_soviet_russia',
        'x': 1, 'y': 10, 'cost': 7,
        'prereqs': ['GER_dissolve_the_junker_officer_caste', 'GER_socialist_land_and_factory_collectivization'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_alliance_with_soviet_russia',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.213 }
			if = {
				limit = { country_exists = SOV }
				add_opinion_modifier = { target = SOV modifier = ger_sov_revolutionary_alliance }
				SOV = { add_opinion_modifier = { target = GER modifier = ger_sov_revolutionary_alliance } }
			}''',
    },
    {
        'id': 'GER_council_economic_planning',
        'x': 2, 'y': 10, 'cost': 7,
        'prereqs': ['GER_socialist_land_and_factory_collectivization'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_optimize_reich_labour_service',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_RESEARCH'],
        'reward': '''add_tech_bonus = {
				name = industrial_planning_bonus
				bonus = 1.0
				uses = 2
				category = industry
			}
			add_political_power = 60''',
    },
    {
        'id': 'GER_soviet_military_advisors',
        'x': 3, 'y': 10, 'cost': 7,
        'prereqs': ['GER_socialist_land_and_factory_collectivization', 'GER_rote_ruhrarmee_formation'],
        'mut_ex': [],
        'icon': 'GFX_AUS_1912_military_program',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_RESEARCH'],
        'reward': '''army_experience = 40
			add_doctrine_cost_reduction = {
				name = revolutionary_warfare_doctrine
				cost_reduction = 0.5
				uses = 2
				category = land_doctrine
			}''',
    },
    {
        'id': 'GER_red_baltic_intervention',
        'x': 0, 'y': 11, 'cost': 7,
        'prereqs': ['GER_red_high_seas_fleet', 'GER_alliance_with_soviet_russia'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_subduing_the_baltic_states',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_war_support = 0.05
			create_wargoal = {
				type = puppet_wargoal_focus
				target = LAT
			}
			create_wargoal = {
				type = puppet_wargoal_focus
				target = EST
			}
			create_wargoal = {
				type = puppet_wargoal_focus
				target = LIT
			}''',
    },
    {
        'id': 'GER_liberate_the_polish_proletariat',
        'x': 1, 'y': 11, 'cost': 7,
        'prereqs': ['GER_alliance_with_soviet_russia'],
        'mut_ex': [],
        'icon': 'GFX_focus_wake_up_poland',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''if = {
				limit = { country_exists = POL }
				create_wargoal = {
					type = puppet_wargoal_focus
					target = POL
				}
			}
			add_war_support = 0.05
			add_political_power = 60''',
    },
    {
        'id': 'GER_danubian_soviet_federation',
        'x': 2, 'y': 11, 'cost': 7,
        'prereqs': ['GER_alliance_with_soviet_russia', 'GER_council_economic_planning'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_emergency_danubian_annexation',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.214 }
			add_political_power = 75''',
    },
    {
        'id': 'GER_liberate_the_balkans_workers',
        'x': 3, 'y': 11, 'cost': 7,
        'prereqs': ['GER_soviet_military_advisors'],
        'mut_ex': [],
        'icon': 'GFX_focus_SOV_ww1_liberate_galician_ruthenians',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''create_wargoal = {
				type = puppet_wargoal_focus
				target = BUL
			}
			create_wargoal = {
				type = puppet_wargoal_focus
				target = ROM
			}
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_export_revolution_to_france',
        'x': 4, 'y': 11, 'cost': 7,
        'prereqs': ['GER_rote_ruhrarmee_formation', 'GER_soviet_military_advisors'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_war_with_france',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''if = {
				limit = { country_exists = FRA }
				create_wargoal = {
					type = puppet_wargoal_focus
					target = FRA
				}
			}
			add_war_support = 0.10
			army_experience = 30''',
    },
    {
        'id': 'GER_world_proletarian_revolution',
        'x': 2, 'y': 12, 'cost': 10,
        'prereqs': ['GER_liberate_the_polish_proletariat', 'GER_danubian_soviet_federation', 'GER_export_revolution_to_france'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_world_proletarian_revolution',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_ARMY_XP'],
        'reward': '''add_ideas = GER_world_revolution_vanguard
			add_war_support = 0.15
			army_experience = 50
			navy_experience = 50''',
    },
    {
        'id': 'GER_prussian_franchise_reform',
        'x': 7, 'y': 6, 'cost': 10,
        'prereqs': ['GER_burgfrieden_declaration_1914'],
        'mut_ex': ['GER_spartakusbund_proletarian_revolt', 'GER_silent_dictatorship_ohl', 'GER_found_vaterlandspartei'],
        'icon': 'GFX_focus_GER_prussian_franchise_reform',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.05
			add_popularity = { ideology = democratic popularity = 0.20 }
			add_political_power = 75
			set_country_flag = GER_three_class_franchise_abolished''',
    },
    {
        'id': 'GER_prince_max_von_baden_cabinet',
        'x': 6, 'y': 7, 'cost': 7,
        'prereqs': ['GER_prussian_franchise_reform'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_prince_max_von_baden_cabinet',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''add_political_power = 80
			add_popularity = { ideology = democratic popularity = 0.15 }
			set_country_flag = GER_prince_max_chancellor''',
    },
    {
        'id': 'GER_proclaim_deutsche_republik',
        'x': 8, 'y': 7, 'cost': 7,
        'prereqs': ['GER_prussian_franchise_reform'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_reestablish_free_elections',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''country_event = { id = ww1_germany_events.220 }
			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			add_popularity = { ideology = democratic popularity = 0.25 }
			add_stability = 0.10''',
    },
    {
        'id': 'GER_repeal_anti_socialist_heritage',
        'x': 5, 'y': 8, 'cost': 7,
        'prereqs': ['GER_prince_max_von_baden_cabinet'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_repeal_anti_socialist_heritage',
        'filters': ['FOCUS_FILTER_STABILITY', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_stability = 0.08
			add_political_power = 60
			add_popularity = { ideology = democratic popularity = 0.10 }''',
    },
    {
        'id': 'GER_antinationalist_civil_defense',
        'x': 7, 'y': 8, 'cost': 7,
        'prereqs': ['GER_prince_max_von_baden_cabinet', 'GER_proclaim_deutsche_republik'],
        'mut_ex': [],
        'icon': 'GFX_AUS_adriatic_coastal_defense',
        'filters': ['FOCUS_FILTER_MANPOWER', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.05
			army_experience = 20
			64 = { # Brandenburg
				create_unit = {
					division = "name = \\"1. Reichsbanner-Bataillon\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
				create_unit = {
					division = "name = \\"2. Reichsbanner-Bataillon\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.3"
					owner = GER
				}
			}''',
    },
    {
        'id': 'GER_stinnes_legien_social_compromise',
        'x': 9, 'y': 8, 'cost': 7,
        'prereqs': ['GER_proclaim_deutsche_republik'],
        'mut_ex': [],
        'icon': 'GFX_GER_Binnenwirtschaft',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.10
			57 = { # Westfalen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
			65 = { # Sachsen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_rathenau_industrial_reorganization',
        'x': 5, 'y': 9, 'cost': 7,
        'prereqs': ['GER_repeal_anti_socialist_heritage'],
        'mut_ex': [],
        'icon': 'GFX_GER_Rathenauplan',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_RESEARCH'],
        'reward': '''add_tech_bonus = {
				name = raw_materials_synthesis
				bonus = 1.0
				uses = 2
				category = synthetic_resources
			}
			64 = { # Brandenburg
				add_building_construction = {
					type = synthetic_refinery
					level = 1
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_weimar_national_assembly',
        'x': 7, 'y': 9, 'cost': 7,
        'prereqs': ['GER_antinationalist_civil_defense'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_reichstag',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_ideas = GER_weimar_democracy
			add_political_power = 100
			add_stability = 0.05''',
    },
    {
        'id': 'GER_zentrum_concordat_with_rome',
        'x': 9, 'y': 9, 'cost': 7,
        'prereqs': ['GER_stinnes_legien_social_compromise'],
        'mut_ex': [],
        'icon': 'GFX_GER_Zentrum',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.05
			add_political_power = 80
			add_popularity = { ideology = democratic popularity = 0.10 }''',
    },
    {
        'id': 'GER_post_war_welfare_and_reconstruction',
        'x': 6, 'y': 10, 'cost': 7,
        'prereqs': ['GER_rathenau_industrial_reorganization', 'GER_weimar_national_assembly'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_strengthen_the_welfare_state',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.08
			random_owned_controlled_state = {
				limit = { is_core_of = GER }
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_federal_constitutional_balance',
        'x': 8, 'y': 10, 'cost': 7,
        'prereqs': ['GER_weimar_national_assembly', 'GER_zentrum_concordat_with_rome'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_federal_constitutional_monarchy',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.07
			add_political_power = 80''',
    },
    {
        'id': 'GER_direct_negotiations_with_woodrow_wilson',
        'x': 7, 'y': 10, 'cost': 7,
        'prereqs': ['GER_weimar_national_assembly'],
        'mut_ex': [],
        'icon': 'GFX_GER_redirected_funding',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.221 }
			add_political_power = 60
			if = {
				limit = { country_exists = USA }
				add_opinion_modifier = { target = USA modifier = ger_wilson_14_points_cooperation }
				USA = { add_opinion_modifier = { target = GER modifier = ger_wilson_14_points_cooperation } }
			}''',
    },
    {
        'id': 'GER_alsace_lorraine_plebiscite',
        'x': 5, 'y': 11, 'cost': 7,
        'prereqs': ['GER_post_war_welfare_and_reconstruction', 'GER_direct_negotiations_with_woodrow_wilson'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_reintegrate_luxemburg_and_alsace_lorraine',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''country_event = { id = ww1_germany_events.222 }
			add_stability = 0.05
			add_political_power = 75''',
    },
    {
        'id': 'GER_democratic_mitteleuropa_union',
        'x': 6, 'y': 11, 'cost': 7,
        'prereqs': ['GER_direct_negotiations_with_woodrow_wilson'],
        'mut_ex': [],
        'icon': 'GFX_FRA_union_sacre',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_political_power = 90
			set_country_flag = GER_democratic_mitteleuropa_founded
			if = {
				limit = { country_exists = AUS }
				add_opinion_modifier = { target = AUS modifier = ger_mitteleuropa_customs_pact }
				AUS = { add_opinion_modifier = { target = GER modifier = ger_mitteleuropa_customs_pact } }
			}''',
    },
    {
        'id': 'GER_subjugate_luxembourg_customs',
        'x': 8, 'y': 11, 'cost': 7,
        'prereqs': ['GER_direct_negotiations_with_woodrow_wilson', 'GER_federal_constitutional_balance'],
        'mut_ex': [],
        'icon': 'GFX_GER_Deutsche_Luftstreitkrafte',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''if = {
				limit = { country_exists = LUX }
				LUX = {
					add_ideas = GER_zollverein_subordination
				}
				add_political_power = 50
			}
			5 = { # Luxembourg state
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_nordic_democratic_trade_compact',
        'x': 9, 'y': 11, 'cost': 7,
        'prereqs': ['GER_federal_constitutional_balance'],
        'mut_ex': [],
        'icon': 'GFX_focus_SOV_ww1_federal_democratic_republic',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''if = {
				limit = { country_exists = SWE }
				add_opinion_modifier = { target = SWE modifier = ger_nordic_trade_compact }
				SWE = { add_opinion_modifier = { target = GER modifier = ger_nordic_trade_compact } }
			}
			if = {
				limit = { country_exists = NOR }
				add_opinion_modifier = { target = NOR modifier = ger_nordic_trade_compact }
				NOR = { add_opinion_modifier = { target = GER modifier = ger_nordic_trade_compact } }
			}
			add_political_power = 60''',
    },
    {
        'id': 'GER_guarantee_independent_poland_buffer',
        'x': 6, 'y': 12, 'cost': 7,
        'prereqs': ['GER_democratic_mitteleuropa_union'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_reassert_eastern_claims',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''if = {
				limit = { country_exists = POL }
				give_guarantee = POL
				add_opinion_modifier = { target = POL modifier = ger_guarantee_independent_poland }
				POL = { add_opinion_modifier = { target = GER modifier = ger_guarantee_independent_poland } }
			}
			add_political_power = 75''',
    },
    {
        'id': 'GER_baltic_democratic_confederation',
        'x': 8, 'y': 12, 'cost': 7,
        'prereqs': ['GER_subjugate_luxembourg_customs', 'GER_nordic_democratic_trade_compact'],
        'mut_ex': [],
        'icon': 'GFX_SOV_baltic_fleet_priority',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''if = { limit = { country_exists = LIT } give_guarantee = LIT }
			if = { limit = { country_exists = LAT } give_guarantee = LAT }
			if = { limit = { country_exists = EST } give_guarantee = EST }
			add_political_power = 80''',
    },
    {
        'id': 'GER_pan_european_arbitration_league',
        'x': 7, 'y': 13, 'cost': 10,
        'prereqs': ['GER_guarantee_independent_poland_buffer', 'GER_baltic_democratic_confederation'],
        'mut_ex': [],
        'icon': 'GFX_GER_mllitary_leagues_demands',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_political_power = 150
			add_stability = 0.10
			every_other_country = {
				limit = { has_government = democratic }
				add_opinion_modifier = { target = GER modifier = ger_pan_european_league_admiration }
			}''',
    },
    {
        'id': 'GER_silent_dictatorship_ohl',
        'x': 12, 'y': 6, 'cost': 10,
        'prereqs': ['GER_burgfrieden_declaration_1914'],
        'mut_ex': ['GER_spartakusbund_proletarian_revolt', 'GER_prussian_franchise_reform', 'GER_found_vaterlandspartei'],
        'icon': 'GFX_focus_GER_silent_dictatorship_ohl',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''country_event = { id = ww1_germany_events.230 }
			add_ideas = GER_silent_dictatorship_ohl
			add_war_support = 0.10
			army_experience = 25
			set_country_flag = GER_third_ohl_established''',
    },
    {
        'id': 'GER_oust_bethmann_hollweg',
        'x': 10, 'y': 7, 'cost': 7,
        'prereqs': ['GER_silent_dictatorship_ohl'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_oust_bethmann_hollweg',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''add_political_power = 80
			add_popularity = { ideology = neutrality popularity = 0.15 }
			set_country_flag = GER_bethmann_ousted''',
    },
    {
        'id': 'GER_hindenburg_program_mobilization',
        'x': 12, 'y': 7, 'cost': 7,
        'prereqs': ['GER_silent_dictatorship_ohl'],
        'mut_ex': [],
        'icon': 'GFX_ENG_infrastructure_development_program',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_ideas = GER_hindenburg_program
			57 = { # Westfalen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 2
					instant_build = yes
				}
			}
			65 = { # Sachsen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 2
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_patriotic_auxiliary_service_law',
        'x': 14, 'y': 7, 'cost': 7,
        'prereqs': ['GER_silent_dictatorship_ohl'],
        'mut_ex': [],
        'icon': 'GFX_GER_Freiwilliger_Arbeitsdienst',
        'filters': ['FOCUS_FILTER_MANPOWER', 'FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_political_power = 50
			add_manpower = 50000
			add_stability = -0.05
			add_war_support = 0.05
			set_country_flag = GER_auxiliary_service_enacted''',
    },
    {
        'id': 'GER_krupp_ordnance_dictate',
        'x': 10, 'y': 8, 'cost': 7,
        'prereqs': ['GER_oust_bethmann_hollweg'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_krupp',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_RESEARCH'],
        'reward': '''army_experience = 35
			add_tech_bonus = {
				name = artillery_ordnance_bonus
				bonus = 1.0
				uses = 2
				category = artillery
			}''',
    },
    {
        'id': 'GER_total_war_patriotism_kriegsanleihen',
        'x': 12, 'y': 8, 'cost': 7,
        'prereqs': ['GER_hindenburg_program_mobilization'],
        'mut_ex': [],
        'icon': 'GFX_GER_Ufa_War_Propaganda',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_war_support = 0.10
			add_political_power = 100
			set_country_flag = GER_war_bonds_floated''',
    },
    {
        'id': 'GER_sturmtruppen_doctrine_offensive',
        'x': 14, 'y': 8, 'cost': 7,
        'prereqs': ['GER_patriotic_auxiliary_service_law'],
        'mut_ex': [],
        'icon': 'GFX_FRA_nivelle_offensive',
        'filters': ['FOCUS_FILTER_ARMY_XP'],
        'reward': '''army_experience = 45
			add_doctrine_cost_reduction = {
				name = sturmtruppen_tactics
				cost_reduction = 0.5
				uses = 2
				category = land_doctrine
			}
			64 = { # Brandenburg
				create_unit = {
					division = "name = \\"1. Sturmbataillon Rohr\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.6"
					owner = GER
				}
				create_unit = {
					division = "name = \\"2. Sturmbataillon Rohr\\" division_template = \\"Infanterie-Division\\" start_experience_factor = 0.6"
					owner = GER
				}
			}''',
    },
    {
        'id': 'GER_subjugate_the_reichstag_politicians',
        'x': 10, 'y': 9, 'cost': 7,
        'prereqs': ['GER_krupp_ordnance_dictate'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_total_control_over_domestic_affairs',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''add_political_power = 80
			add_stability = 0.05
			add_popularity = { ideology = neutrality popularity = 0.10 }''',
    },
    {
        'id': 'GER_septemberprogramm_war_aims',
        'x': 12, 'y': 9, 'cost': 7,
        'prereqs': ['GER_total_war_patriotism_kriegsanleihen'],
        'mut_ex': [],
        'icon': 'GFX_GER_Empower_the_Reichsbank',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_war_support = 0.10
			add_political_power = 75
			set_country_flag = GER_septemberprogramm_active''',
    },
    {
        'id': 'GER_unrestricted_submarine_mobilization',
        'x': 14, 'y': 9, 'cost': 7,
        'prereqs': ['GER_sturmtruppen_doctrine_offensive'],
        'mut_ex': [],
        'icon': 'GFX_ENG_mobilization_of_industry',
        'filters': ['FOCUS_FILTER_NAVY_XP'],
        'reward': '''country_event = { id = ww1_germany_events.231 }
			navy_experience = 40
			add_ideas = GER_unrestricted_submarine_warfare_spirit''',
    },
    {
        'id': 'GER_annexation_of_belgium_and_briey',
        'x': 10, 'y': 10, 'cost': 7,
        'prereqs': ['GER_subjugate_the_reichstag_politicians', 'GER_septemberprogramm_war_aims'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_annexation_of_belgium_and_briey',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_war_support = 0.05
			if = {
				limit = { country_exists = BEL }
				create_wargoal = {
					type = puppet_wargoal_focus
					target = BEL
				}
			}
			set_country_flag = GER_belgium_briey_annexation_claimed''',
    },
    {
        'id': 'GER_subjugate_romanian_ploesti_oil',
        'x': 12, 'y': 10, 'cost': 7,
        'prereqs': ['GER_septemberprogramm_war_aims'],
        'mut_ex': [],
        'icon': 'GFX_AUS_encourage_romanian_bureaucrats',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''if = {
				limit = { country_exists = ROM }
				create_wargoal = {
					type = puppet_wargoal_focus
					target = ROM
				}
			}
			add_war_support = 0.05
			add_political_power = 60''',
    },
    {
        'id': 'GER_brest_litovsk_carve_up',
        'x': 14, 'y': 10, 'cost': 7,
        'prereqs': ['GER_septemberprogramm_war_aims', 'GER_unrestricted_submarine_mobilization'],
        'mut_ex': [],
        'icon': 'GFX_GER_Helfferichplan',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.232 }
			add_political_power = 100
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_establish_generalgouvernement_warschau',
        'x': 10, 'y': 11, 'cost': 7,
        'prereqs': ['GER_annexation_of_belgium_and_briey'],
        'mut_ex': [],
        'icon': 'GFX_AUS_reestablish_croatian_constitution',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''add_political_power = 80
			set_country_flag = GER_generalgouvernement_warschau_proclaimed
			if = {
				limit = { country_exists = POL }
				puppet = POL
			}''',
    },
    {
        'id': 'GER_finnish_intervention_von_der_goltz',
        'x': 12, 'y': 11, 'cost': 7,
        'prereqs': ['GER_subjugate_romanian_ploesti_oil', 'GER_brest_litovsk_carve_up'],
        'mut_ex': [],
        'icon': 'GFX_GER_Winterhilfe',
        'filters': ['FOCUS_FILTER_ARMY_XP'],
        'reward': '''army_experience = 25
			if = {
				limit = { country_exists = FIN }
				add_opinion_modifier = { target = FIN modifier = ger_finnish_intervention_monarchy }
				FIN = {
					add_opinion_modifier = { target = GER modifier = ger_finnish_intervention_monarchy }
					set_politics = {
						ruling_party = neutrality
					}
				}
			}''',
    },
    {
        'id': 'GER_carve_ukrainian_breadbasket',
        'x': 14, 'y': 11, 'cost': 7,
        'prereqs': ['GER_brest_litovsk_carve_up'],
        'mut_ex': [],
        'icon': 'GFX_GER_a7v-86394.png',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''if = {
				limit = { country_exists = UKR }
				puppet = UKR
			}
			add_political_power = 75
			set_country_flag = GER_ukrainian_hetmanate_satellite''',
    },
    {
        'id': 'GER_operation_faustschlag_crusade',
        'x': 11, 'y': 12, 'cost': 7,
        'prereqs': ['GER_establish_generalgouvernement_warschau', 'GER_finnish_intervention_von_der_goltz'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_strike_eastward',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_timed_idea = { idea = GER_operation_faustschlag_timed days = 30 }
			army_experience = 40
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_subjugate_the_danubian_ally',
        'x': 13, 'y': 12, 'cost': 7,
        'prereqs': ['GER_finnish_intervention_von_der_goltz', 'GER_carve_ukrainian_breadbasket'],
        'mut_ex': [],
        'icon': 'GFX_focus_ARG_american_allyship',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''if = {
				limit = { country_exists = AUS }
				AUS = {
					add_ideas = GER_ohl_supreme_staff_coordination
				}
			}
			add_political_power = 80
			army_experience = 30''',
    },
    {
        'id': 'GER_hegemon_of_continental_europe',
        'x': 12, 'y': 13, 'cost': 10,
        'prereqs': ['GER_operation_faustschlag_crusade', 'GER_subjugate_the_danubian_ally'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_hohenzollern_imperial_hegemony',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_ideas = GER_continental_hegemony
			add_ideas = GER_morphed_mitteleuropa_iron_rule
			add_war_support = 0.15
			add_stability = 0.10
			add_political_power = 150''',
    },
    {
        'id': 'GER_found_vaterlandspartei',
        'x': 17, 'y': 6, 'cost': 10,
        'prereqs': ['GER_burgfrieden_declaration_1914'],
        'mut_ex': ['GER_spartakusbund_proletarian_revolt', 'GER_prussian_franchise_reform', 'GER_silent_dictatorship_ohl'],
        'icon': 'GFX_focus_GER_found_vaterlandspartei',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.240 }
			add_ideas = GER_vaterlandspartei_movement
			add_war_support = 0.10
			add_popularity = { ideology = fascism popularity = 0.20 }
			set_country_flag = GER_vaterlandspartei_founded''',
    },
    {
        'id': 'GER_kapp_and_tirpitz_rally',
        'x': 15, 'y': 7, 'cost': 7,
        'prereqs': ['GER_found_vaterlandspartei'],
        'mut_ex': [],
        'icon': 'GFX_GER_DVLP',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_POLITICAL'],
        'reward': '''add_war_support = 0.08
			add_political_power = 80
			navy_experience = 25''',
    },
    {
        'id': 'GER_militarize_the_entire_society',
        'x': 17, 'y': 7, 'cost': 7,
        'prereqs': ['GER_found_vaterlandspartei'],
        'mut_ex': [],
        'icon': 'GFX_GER_Expand_Kriegsschule',
        'filters': ['FOCUS_FILTER_MANPOWER'],
        'reward': '''add_manpower = 60000
			army_experience = 30
			set_country_flag = GER_society_militarized''',
    },
    {
        'id': 'GER_dissolve_the_reichstag',
        'x': 19, 'y': 7, 'cost': 7,
        'prereqs': ['GER_found_vaterlandspartei'],
        'mut_ex': [],
        'icon': 'GFX_GER_DkP',
        'filters': ['FOCUS_FILTER_POLITICAL'],
        'reward': '''country_event = { id = ww1_germany_events.241 }
			set_politics = {
				ruling_party = fascism
				elections_allowed = no
			}
			add_stability = -0.05
			add_popularity = { ideology = fascism popularity = 0.25 }''',
    },
    {
        'id': 'GER_smash_general_strikes',
        'x': 15, 'y': 8, 'cost': 7,
        'prereqs': ['GER_kapp_and_tirpitz_rally'],
        'mut_ex': [],
        'icon': 'GFX_SOV_main_directorate_of_the_general_staff',
        'filters': ['FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.10
			add_political_power = 60
			add_popularity = { ideology = communism popularity = -0.15 }''',
    },
    {
        'id': 'GER_alldeutscher_verband_hegemony',
        'x': 17, 'y': 8, 'cost': 7,
        'prereqs': ['GER_militarize_the_entire_society'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_monarchist_sentiment',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_political_power = 90
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_siegfrieden_manifesto',
        'x': 19, 'y': 8, 'cost': 7,
        'prereqs': ['GER_dissolve_the_reichstag'],
        'mut_ex': [],
        'icon': 'GFX_GER_adriatic_sea_reinforcement-45124.png',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''add_war_support = 0.15
			add_political_power = 75
			set_country_flag = GER_siegfrieden_declared''',
    },
    {
        'id': 'GER_autarkic_industrial_trusts',
        'x': 16, 'y': 9, 'cost': 7,
        'prereqs': ['GER_smash_general_strikes', 'GER_alldeutscher_verband_hegemony'],
        'mut_ex': [],
        'icon': 'GFX_GER_Thyssen_Pact',
        'filters': ['FOCUS_FILTER_INDUSTRY'],
        'reward': '''57 = { # Westfalen
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 2
					instant_build = yes
				}
			}
			64 = { # Brandenburg
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}''',
    },
    {
        'id': 'GER_crush_marxism_and_defeatism',
        'x': 18, 'y': 9, 'cost': 7,
        'prereqs': ['GER_alldeutscher_verband_hegemony', 'GER_siegfrieden_manifesto'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_totaler_krieg',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_STABILITY'],
        'reward': '''add_stability = 0.08
			add_war_support = 0.05
			add_popularity = { ideology = communism popularity = -0.10 }
			add_popularity = { ideology = democratic popularity = -0.10 }''',
    },
    {
        'id': 'GER_annex_the_flemish_coast',
        'x': 15, 'y': 10, 'cost': 7,
        'prereqs': ['GER_autarkic_industrial_trusts'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_the_austrian_question_annex',
        'filters': ['FOCUS_FILTER_NAVY_XP', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''navy_experience = 35
			add_war_support = 0.05
			set_country_flag = GER_flemish_coast_annexation_claimed''',
    },
    {
        'id': 'GER_colonize_the_eastern_frontier_strip',
        'x': 17, 'y': 10, 'cost': 7,
        'prereqs': ['GER_autarkic_industrial_trusts', 'GER_crush_marxism_and_defeatism'],
        'mut_ex': [],
        'icon': 'GFX_GER_asienkorps_units',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_MANPOWER'],
        'reward': '''add_political_power = 60
			add_stability = 0.05
			set_country_flag = GER_polnischer_grenzstreifen_colonized''',
    },
    {
        'id': 'GER_baltic_crusade_landeswehr',
        'x': 19, 'y': 10, 'cost': 7,
        'prereqs': ['GER_crush_marxism_and_defeatism'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_army_officer',
        'filters': ['FOCUS_FILTER_ARMY_XP', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''army_experience = 35
			add_war_support = 0.05
			create_wargoal = {
				type = puppet_wargoal_focus
				target = LAT
			}
			create_wargoal = {
				type = puppet_wargoal_focus
				target = EST
			}''',
    },
    {
        'id': 'GER_crush_netherlands_neutrality',
        'x': 15, 'y': 11, 'cost': 7,
        'prereqs': ['GER_annex_the_flemish_coast'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_west_wall',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''country_event = { id = ww1_germany_events.242 }
			if = {
				limit = { country_exists = HOL }
				create_wargoal = {
					type = puppet_wargoal_focus
					target = HOL
				}
			}
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_pan_german_settlement_east',
        'x': 17, 'y': 11, 'cost': 7,
        'prereqs': ['GER_colonize_the_eastern_frontier_strip'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_restore_the_brest_litovsk_borders',
        'filters': ['FOCUS_FILTER_MANPOWER'],
        'reward': '''add_manpower = 40000
			add_stability = 0.05
			add_political_power = 50''',
    },
    {
        'id': 'GER_subjugate_scandinavia',
        'x': 19, 'y': 11, 'cost': 7,
        'prereqs': ['GER_baltic_crusade_landeswehr'],
        'mut_ex': [],
        'icon': 'GFX_GER_asienkorps_units-86387.png',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_NAVY_XP'],
        'reward': '''create_wargoal = {
				type = puppet_wargoal_focus
				target = DEN
			}
			create_wargoal = {
				type = puppet_wargoal_focus
				target = NOR
			}
			navy_experience = 30
			add_war_support = 0.05''',
    },
    {
        'id': 'GER_annex_french_iron_and_channel_ports',
        'x': 16, 'y': 12, 'cost': 7,
        'prereqs': ['GER_crush_netherlands_neutrality', 'GER_pan_german_settlement_east'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_rhineland',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_INDUSTRY'],
        'reward': '''if = {
				limit = { country_exists = FRA }
				create_wargoal = {
					type = take_state_focus
					target = FRA
					generator = { 28 } # Alsace-Lorraine / Briey
				}
			}
			add_war_support = 0.08
			add_political_power = 75''',
    },
    {
        'id': 'GER_conquer_transcaucasia_oil',
        'x': 18, 'y': 12, 'cost': 7,
        'prereqs': ['GER_pan_german_settlement_east', 'GER_subjugate_scandinavia'],
        'mut_ex': [],
        'icon': 'GFX_GER_auftragstaktik',
        'filters': ['FOCUS_FILTER_INDUSTRY', 'FOCUS_FILTER_WAR_SUPPORT'],
        'reward': '''army_experience = 25
			add_war_support = 0.05
			set_country_flag = GER_caucasus_oil_conquest_active''',
    },
    {
        'id': 'GER_mittelafrika_total_empire',
        'x': 17, 'y': 13, 'cost': 7,
        'prereqs': ['GER_annex_french_iron_and_channel_ports', 'GER_conquer_transcaucasia_oil'],
        'mut_ex': [],
        'icon': 'GFX_AUS_address_empire_minorities',
        'filters': ['FOCUS_FILTER_POLITICAL', 'FOCUS_FILTER_INDUSTRY'],
        'reward': '''add_political_power = 100
			add_stability = 0.05
			set_country_flag = GER_mittelafrika_empire_declared''',
    },
    {
        'id': 'GER_unconditional_victory_or_ruin',
        'x': 17, 'y': 14, 'cost': 10,
        'prereqs': ['GER_mittelafrika_total_empire'],
        'mut_ex': [],
        'icon': 'GFX_focus_GER_ww1_unconditional_victory_or_ruin',
        'filters': ['FOCUS_FILTER_WAR_SUPPORT', 'FOCUS_FILTER_ARMY_XP'],
        'reward': '''add_ideas = GER_siegfrieden_triumph
			add_war_support = 0.20
			add_stability = 0.10
			army_experience = 50
			navy_experience = 50''',
    },
]
