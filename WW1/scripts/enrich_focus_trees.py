import re

def enrich_trees():
    # =========================================================================
    # GERMANY
    # =========================================================================
    with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
        ger_text = f.read()

    ger_replacements = {
        'GER_prussian_franchise_debate': """		completion_reward = {
			add_stability = 0.05
			add_political_power = 75
			64 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_oust_bethmann_hollweg': """		completion_reward = {
			add_political_power = 80
			add_war_support = 0.08
			add_stability = -0.05
			army_experience = 25
		}""",
        'GER_chancellor_michaelis_puppet': """		completion_reward = {
			add_political_power = 80
			add_war_support = 0.05
			51 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_three_class_franchise_abolition_law': """		completion_reward = {
			add_stability = 0.10
			add_political_power = 75
			add_ideas = GER_democratic_franchise_reform
		}""",
        'GER_repeal_anti_socialist_heritage': """		completion_reward = {
			add_stability = 0.08
			add_political_power = 60
			65 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_hohenzollern_imperial_hegemony': """		completion_reward = {
			add_political_power = 150
			add_war_support = 0.15
			add_stability = 0.10
			add_ideas = GER_kaiserliche_weltmacht
		}""",
        'GER_siegfrieden_manifesto': """		completion_reward = {
			add_war_support = 0.15
			add_political_power = 75
			add_state_claim = 17 # Briey-Longwy
			59 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = dockyard
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_post_war_welfare_and_reconstruction': """		completion_reward = {
			add_stability = 0.12
			add_political_power = 75
			50 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
			52 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_federal_constitutional_monarchy': """		completion_reward = {
			add_stability = 0.15
			add_political_power = 120
			add_ideas = GER_democratic_legitimacy
		}""",
        'GER_unconditional_victory_or_ruin': """		completion_reward = {
			add_war_support = 0.25
			add_political_power = 100
			add_manpower = 50000
			51 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_imperial_war_credits_kriegsanleihen': """		completion_reward = {
			add_political_power = 120
			add_war_support = 0.10
			54 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
			67 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}""",
        'GER_seek_armistice_fourteen_points': """		completion_reward = {
			add_stability = 0.10
			add_political_power = 80
			set_global_flag = ger_armistice_fourteen_points_sought
		}""",
        'GER_partition_of_british_sphere_asia': """		completion_reward = {
			add_political_power = 100
			add_war_support = 0.10
			58 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = dockyard
					level = 1
					instant_build = yes
				}
			}
		}"""
    }

    def replace_focus_reward(text, fid, new_rew):
        idx = text.find(f'id = {fid}')
        if idx == -1:
            print(f'Warning: {fid} not found!')
            return text
        rew_idx = text.find('completion_reward = {', idx)
        # find matching brace for completion_reward
        start_brace = text.find('{', rew_idx)
        brace = 1
        end_brace = start_brace + 1
        while brace > 0 and end_brace < len(text):
            if text[end_brace] == '{': brace += 1
            elif text[end_brace] == '}': brace -= 1
            end_brace += 1
        
        old_block = text[rew_idx:end_brace]
        return text[:rew_idx] + new_rew + text[end_brace:]

    for fid, rew in ger_replacements.items():
        ger_text = replace_focus_reward(ger_text, fid, rew)

    with open('common/national_focus/germany.txt', 'w', encoding='utf-8') as f:
        f.write(ger_text)
    print('Updated Germany focus tree with enriched rewards!')

    # =========================================================================
    # RUSSIA
    # =========================================================================
    with open('common/national_focus/soviet.txt', 'r', encoding='utf-8') as f:
        sov_text = f.read()

    sov_replacements = {
        'SOV_the_empire_of_nicholas_ii': """		completion_reward = {
			add_political_power = 150
			add_stability = 0.05
			add_war_support = 0.05
			army_experience = 20
			navy_experience = 15
			195 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_goremykin_stagnation': """		completion_reward = {
			add_stability = -0.05
			add_political_power = -50
			add_ideas = SOV_goremykin_reactionary_cabinet
		}""",
        'SOV_ministry_of_national_confidence': """		completion_reward = {
			add_political_power = 100
			add_stability = 0.08
			add_war_support = 0.05
			remove_ideas = SOV_goremykin_reactionary_cabinet
			add_ideas = SOV_progressive_coalition_cabinet
			248 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_rodzianko_ultimatum': """		completion_reward = {
			add_stability = -0.05
			add_war_support = 0.05
			add_political_power = 60
			195 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_mutiny_of_petrograd_garrison': """		completion_reward = {
			add_stability = -0.20
			add_war_support = -0.15
			add_ideas = SOV_petrograd_soviet_order_no_1
			division_template = {
				name = "Petrogradsky Krasnogvardeysky Polk"
				regiments = {
					infantry = { x = 0 y = 0 }
					infantry = { x = 0 y = 1 }
					infantry = { x = 0 y = 2 }
					infantry = { x = 1 y = 0 }
					infantry = { x = 1 y = 1 }
				}
			}
			random_owned_controlled_state = {
				prioritize = { 195 }
				create_unit = {
					division = "name = \\"1-y Petrogradsky Krasnogvardeysky Polk\\" division_template = \\"Petrogradsky Krasnogvardeysky Polk\\" start_experience_factor = 0.5"
					owner = SOV
					count = 2
				}
			}
		}""",
        'SOV_decree_on_peace': """		completion_reward = {
			add_war_support = -0.25
			add_stability = 0.15
			add_manpower = 50000
		}""",
        'SOV_decree_on_land': """		completion_reward = {
			remove_ideas = SOV_backward_agrarian_system
			add_ideas = SOV_land_socialization_decree
			add_stability = 0.15
			add_political_power = 75
			add_manpower = 150000
		}""",
        'SOV_founding_of_the_cheka': """		completion_reward = {
			add_stability = 0.15
			add_political_power = 100
			add_ideas = SOV_all_russian_cheka
		}""",
        'SOV_autonomy_to_minority_nations': """		completion_reward = {
			add_stability = 0.12
			add_political_power = 80
			add_ideas = SOV_declaration_rights_peoples
		}""",
        'SOV_unleash_the_black_hundreds': """		completion_reward = {
			add_stability = 0.10
			add_political_power = 100
			add_ideas = SOV_black_hundreds_paramilitaries
			division_template = {
				name = "Chernosotenny Dobrovolchesky Batalon"
				regiments = {
					infantry = { x = 0 y = 0 }
					infantry = { x = 0 y = 1 }
					infantry = { x = 0 y = 2 }
				}
			}
			random_owned_controlled_state = {
				prioritize = { 195 219 }
				create_unit = {
					division = "name = \\"Petrogradskaya Chernaya Sotnya\\" division_template = \\"Chernosotenny Dobrovolchesky Batalon\\" start_experience_factor = 0.6"
					owner = SOV
					count = 2
				}
			}
		}""",
        'SOV_dissolve_the_rebellious_duma': """		completion_reward = {
			add_political_power = 150
			add_stability = 0.05
			add_war_support = 0.05
			add_ideas = SOV_undivided_autocratic_will
			219 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_absolutist_restoration': """		completion_reward = {
			add_political_power = 120
			add_war_support = 0.10
			add_stability = 0.10
			add_ideas = SOV_sacred_romanov_autocracy
			195 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_purification_of_the_empire': """		completion_reward = {
			add_stability = 0.15
			add_political_power = 100
			add_ideas = SOV_imperial_secret_police
		}""",
        'SOV_centralized_grain_procurement': """		completion_reward = {
			add_stability = 0.08
			add_political_power = 60
			add_war_support = 0.05
			add_ideas = SOV_grain_procurement_system
			221 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
			227 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_trabzon_amphibious_landing': """		completion_reward = {
			add_political_power = 75
			add_war_support = 0.10
			army_experience = 20
			navy_experience = 25
			add_tech_bonus = {
				name = tp_bonus
				bonus = 1.0
				uses = 1
				category = tp_tech
			}
			if = {
				limit = { owns_state = 231 }
				231 = {
					add_building_construction = {
						type = naval_base
						level = 2
						instant_build = yes
					}
					add_building_construction = {
						type = coastal_bunker
						level = 2
						instant_build = yes
					}
				}
			}
			division_template = {
				name = "Kavkazskaya Plastunskaya Brigada"
				regiments = {
					infantry = { x = 0 y = 0 }
					infantry = { x = 0 y = 1 }
					infantry = { x = 0 y = 2 }
					cavalry = { x = 1 y = 0 }
					cavalry = { x = 1 y = 1 }
				}
				support = {
					artillery = { x = 0 y = 0 }
				}
			}
			random_owned_controlled_state = {
				prioritize = { 231 }
				create_unit = {
					division = "name = \\"1-ya Kavkazskaya Plastunskaya Brigada\\" division_template = \\"Kavkazskaya Plastunskaya Brigada\\" start_experience_factor = 0.75"
					owner = SOV
				}
			}
		}""",
        'SOV_bochkareva_womens_battalion': """		completion_reward = {
			add_stability = 0.05
			add_war_support = 0.15
			army_experience = 20
			recruit_character = SOV_maria_bochkareva
			division_template = {
				name = "Zhenskiy Batalon Smerti"
				priority = 3
				is_locked = no
				regiments = {
					infantry = { x = 0 y = 0 }
					infantry = { x = 0 y = 1 }
					infantry = { x = 0 y = 2 }
					infantry = { x = 1 y = 0 }
					infantry = { x = 1 y = 1 }
					infantry = { x = 1 y = 2 }
				}
				support = {
					artillery = { x = 0 y = 0 }
				}
			}
			random_owned_controlled_state = {
				prioritize = { 195 }
				create_unit = {
					division = "name = \\"1st Russian Women's Battalion of Death\\" division_template = \\"Zhenskiy Batalon Smerti\\" start_experience_factor = 1.0"
					owner = SOV
				}
			}
		}""",
        'SOV_third_rome_foreign_policy': """		completion_reward = {
			add_war_support = 0.15
			add_political_power = 100
			add_ideas = SOV_defender_of_orthodox_christendom
			every_country = {
				limit = {
					OR = {
						tag = SER
						tag = GRE
						tag = BUL
						tag = ROM
						tag = MNT
					}
				}
				add_opinion_modifier = {
					target = SOV
					modifier = SOV_slavic_brother_opinion
				}
			}
		}""",
        'SOV_pan_slavic_protectorate': """		completion_reward = {
			add_political_power = 80
			add_war_support = 0.15
			give_guarantee = SER
			give_guarantee = MNT
			add_ideas = SOV_pan_slavic_patronage
		}""",
        'SOV_first_balkan_war_mediation': """		completion_reward = {
			add_political_power = 100
			add_stability = 0.08
			add_war_support = 0.05
			195 = {
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_liberate_south_slavs': """		completion_reward = {
			add_stability = 0.10
			add_war_support = 0.15
			add_political_power = 100
			add_ideas = SOV_shield_of_the_slavs
			SER = {
				add_state_claim = 104
				add_state_claim = 103
				add_state_claim = 108
			}
		}""",
        'SOV_claim_tsargrad_and_the_straits': """		completion_reward = {
			add_political_power = 100
			add_war_support = 0.15
			add_state_claim = 341
			add_state_claim = 340
			if = {
				limit = { is_in_faction_with = FRA }
				FRA = { country_event = { id = ww1_diplomacy.70 days = 1 } }
			}
			if = {
				limit = { is_in_faction_with = ENG }
				ENG = { country_event = { id = ww1_diplomacy.70 days = 1 } }
			}
		}""",
        'SOV_storm_the_bosphorus_and_dardanelles': """		completion_reward = {
			add_war_support = 0.20
			add_stability = 0.10
			add_political_power = 120
			navy_experience = 30
			army_experience = 20
			add_tech_bonus = {
				name = tp_bonus
				bonus = 1.0
				uses = 1
				category = tp_tech
			}
		}""",
        'SOV_continental_league_against_britain': """		completion_reward = {
			add_war_support = 0.15
			add_political_power = 120
			add_state_claim = 265
			if = {
				limit = {
					country_exists = GER
					NOT = { has_war_with = GER }
				}
				add_opinion_modifier = {
					target = GER
					modifier = SOV_bjorko_pact_opinion
				}
				GER = {
					add_opinion_modifier = {
						target = SOV
						modifier = SOV_bjorko_pact_opinion
					}
				}
			}
		}""",
        'SOV_siberian_fur_trade_treasury': """		completion_reward = {
			add_political_power = 100
			add_stability = 0.05
			569 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
			571 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
				add_building_construction = {
					type = infrastructure
					level = 1
					instant_build = yes
				}
			}
		}""",
        'SOV_expeditionary_corps_to_france': """		completion_reward = {
			add_opinion_modifier = {
				target = FRA
				modifier = SOV_russian_blood_on_the_marne
			}
			add_war_support = 0.10
			army_experience = 25
			add_tech_bonus = {
				name = art_bonus
				bonus = 1.0
				ahead_reduction = 1
				uses = 1
				category = artillery
			}
		}"""
    }

    for fid, rew in sov_replacements.items():
        sov_text = replace_focus_reward(sov_text, fid, rew)

    with open('common/national_focus/soviet.txt', 'w', encoding='utf-8') as f:
        f.write(sov_text)
    print('Updated Russia focus tree with enriched rewards!')

if __name__ == '__main__':
    enrich_trees()
