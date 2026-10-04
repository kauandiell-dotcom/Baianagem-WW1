import re

with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix GER_secret_ottoman_alliance_august_1914 icon to GFX_TUR_secret_treaty_with_germany
content = re.sub(
    r'(id\s*=\s*GER_secret_ottoman_alliance_august_1914\s*\n\s*)icon\s*=\s*GFX_focus_dreadnought_GER',
    r'\1icon = GFX_TUR_secret_treaty_with_germany',
    content
)

# 2. Fix GER_centenary_of_leipzig_1913 duplicate lines
old_leipzig = """		completion_reward = {
			add_stability = 0.05
			add_war_support = 0.05
			add_political_power = 60
			add_stability = 0.10
			add_war_support = 0.10
			add_political_power = 100
		}"""

new_leipzig = """		completion_reward = {
			add_stability = 0.10
			add_war_support = 0.10
			add_political_power = 100
			army_experience = 15
		}"""

content = content.replace(old_leipzig, new_leipzig)

# 3. Fix GER_kriegsbrot_and_flour_rationing duplicate lines
old_kriegsbrot = """		completion_reward = {
			add_stability = 0.05
			add_stability = 0.05
			add_political_power = 60
		}"""

new_kriegsbrot = """		completion_reward = {
			add_stability = 0.08
			add_political_power = 50
			# Food rationing softens blockade impact
			custom_effect_tooltip = GER_kriegsbrot_rationing_tt
			add_ideas = GER_wartime_rationing_spirit
		}"""

content = content.replace(old_kriegsbrot, new_kriegsbrot)

# 4. Enhance GER_establish_united_baltic_duchy
old_ubd = """	focus = {
		id = GER_establish_united_baltic_duchy
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 81
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 50
			add_stability = 0.05
		}
	}"""

new_ubd = """	focus = {
		id = GER_establish_united_baltic_duchy
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 81
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 75
			add_stability = 0.05
			custom_effect_tooltip = GER_establish_united_baltic_duchy_tt
			if = {
				limit = {
					owns_state = 189
				}
				189 = { add_extra_state_shared_building_slots = 2 }
				190 = { add_extra_state_shared_building_slots = 2 }
			}
			# Create or release client state
			if = {
				limit = { country_exists = UBD }
				GER = { puppet = UBD }
			}
			else = {
				if = {
					limit = { country_exists = LAT }
					GER = { puppet = LAT }
				}
				if = {
					limit = { country_exists = EST }
					GER = { puppet = EST }
				}
			}
		}
	}"""

content = content.replace(old_ubd, new_ubd)

# 5. Enhance GER_kingdom_of_lithuania_urach
old_lit = """	focus = {
		id = GER_kingdom_of_lithuania_urach
		icon = GFX_focus_ger_return_of_the_kaiser
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 83
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 40
			add_stability = 0.05
		}
	}"""

new_lit = """	focus = {
		id = GER_kingdom_of_lithuania_urach
		icon = GFX_focus_ger_return_of_the_kaiser
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 83
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 60
			add_stability = 0.05
			custom_effect_tooltip = GER_kingdom_of_lithuania_urach_tt
			if = {
				limit = { country_exists = LIT }
				GER = { puppet = LIT }
			}
			if = {
				limit = { owns_state = 188 }
				188 = {
					add_extra_state_shared_building_slots = 2
					add_building_construction = {
						type = arms_factory
						level = 1
						instant_build = yes
					}
				}
			}
		}
	}"""

content = content.replace(old_lit, new_lit)

# 6. Enhance GER_kingdom_of_finland_vassal
old_fin = """	focus = {
		id = GER_kingdom_of_finland_vassal
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 85
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 40
			add_stability = 0.05
		}
	}"""

new_fin = """	focus = {
		id = GER_kingdom_of_finland_vassal
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_treaty_of_brest_litovsk }
		cost = 5
		x = 85
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 60
			add_stability = 0.05
			custom_effect_tooltip = GER_kingdom_of_finland_vassal_tt
			if = {
				limit = { country_exists = FIN }
				GER = { puppet = FIN }
			}
			else = {
				GER = {
					add_opinion_modifier = {
						target = FIN
						modifier = ger_blank_cheque_op
					}
				}
			}
		}
	}"""

content = content.replace(old_fin, new_fin)

# 7. Enhance GER_colonize_the_eastern_frontier_strip
old_frontier = """	focus = {
		id = GER_colonize_the_eastern_frontier_strip
		icon = GFX_focus_GER_expand_the_reich
		prerequisite = { focus = GER_regency_kingdom_of_poland }
		cost = 7
		x = 87
		y = 12
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_stability = 0.05
			add_political_power = 50
		}
	}"""

new_frontier = """	focus = {
		id = GER_colonize_the_eastern_frontier_strip
		icon = GFX_focus_GER_expand_the_reich
		prerequisite = { focus = GER_regency_kingdom_of_poland }
		cost = 7
		x = 87
		y = 12
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 75
			67 = {
				add_extra_state_shared_building_slots = 3
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
		}
	}"""

content = content.replace(old_frontier, new_frontier)

# 8. Enhance GER_mittelafrika_colonial_vision
old_mittelafrika = """	focus = {
		id = GER_mittelafrika_colonial_vision
		icon = GFX_focus_GER_expand_the_reich
		prerequisite = { focus = GER_siegfrieden_manifesto }
		cost = 7
		x = 100
		y = 12
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 50
			add_war_support = 0.05
		}
	}"""

new_mittelafrika = """	focus = {
		id = GER_mittelafrika_colonial_vision
		icon = GFX_focus_GER_expand_the_reich
		prerequisite = { focus = GER_siegfrieden_manifesto }
		cost = 7
		x = 100
		y = 12
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 100
			add_war_support = 0.10
			custom_effect_tooltip = GER_mittelafrika_claims_tt
			add_state_claim = 272 # Belgian Congo
			add_state_claim = 183 # Central Africa
		}
	}"""

content = content.replace(old_mittelafrika, new_mittelafrika)

# 9. Enhance GER_max_von_oppenheim_memorandum
old_oppenheim = """	focus = {
		id = GER_max_von_oppenheim_memorandum
		icon = GFX_focus_GER_the_austrian_question
		prerequisite = { focus = GER_bjorko_treaty_reaffirmed }
		cost = 7
		x = 125
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 50
			add_war_support = 0.05
		}
	}"""

new_oppenheim = """	focus = {
		id = GER_max_von_oppenheim_memorandum
		icon = GFX_focus_GER_the_austrian_question
		prerequisite = { focus = GER_bjorko_treaty_reaffirmed }
		cost = 7
		x = 125
		y = 11
		ai_will_do = { factor = 90 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 80
			add_war_support = 0.10
			TUR = {
				add_war_support = 0.15
				add_equipment_to_stockpile = {
					type = infantry_equipment_1
					amount = 5000
				}
			}
			custom_effect_tooltip = GER_oppenheim_jihad_tt
		}
	}"""

content = content.replace(old_oppenheim, new_oppenheim)

# 10. Enhance GER_swiss_neutral_financial_corridor
old_swiss = """	focus = {
		id = GER_swiss_neutral_financial_corridor
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_rathenau_war_raw_materials_kra }
		cost = 7
		x = 35
		y = 8
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 50
			add_stability = 0.05
		}
	}"""

new_swiss = """	focus = {
		id = GER_swiss_neutral_financial_corridor
		icon = GFX_focus_GER_the_kaiser_reich
		prerequisite = { focus = GER_rathenau_war_raw_materials_kra }
		cost = 7
		x = 35
		y = 8
		ai_will_do = { factor = 85 }
		available_if_capitulated = yes

		completion_reward = {
			add_political_power = 80
			add_stability = 0.05
			50 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
			custom_effect_tooltip = GER_swiss_finance_corridor_tt
		}
	}"""

content = content.replace(old_swiss, new_swiss)

with open('common/national_focus/germany.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Germany focus tree with enriched content successfully.")
