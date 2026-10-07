# -*- coding: utf-8 -*-
"""Idea and Decision definitions for Germany Politics & Society Wing."""

IDEAS_TXT = '''
		# =========================================================================
		# REWORKED POLITICS & EXPANSION IDEAS
		# =========================================================================

		GER_wilhelmine_personal_regime = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_wilhelm_ii
			modifier = {
				political_power_factor = 0.05
				stability_factor = -0.03
				consumer_goods_factor = 0.05
			}
		}

		GER_wilhelmine_reform_regime = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_wilhelm_ii
			modifier = {
				stability_factor = 0.05
				consumer_goods_factor = -0.02
				drift_defence_factor = 0.10
			}
		}

		GER_volkerschlacht_spirit = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_iron_cross
			modifier = {
				army_morale_factor = 0.05
				war_support_factor = 0.05
			}
		}

		GER_burgfrieden_1914 = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_burgfrieden
			modifier = {
				war_support_factor = 0.10
				political_power_cost = -0.15
			}
		}

		GER_rate_republik = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_council_republic
			modifier = {
				industrial_capacity_factory = 0.10
				war_support_factor = 0.15
				stability_factor = -0.05
			}
		}

		GER_red_commissars = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_red_guard
			modifier = {
				army_morale_factor = 0.05
				conscription_factor = 0.05
				army_org_factor = -0.05
			}
		}

		GER_ruhr_proletariat = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_ruhr_industry
			modifier = {
				mobilization_speed = 0.10
				reinforce_rate = 0.05
			}
		}

		GER_world_revolution_vanguard = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_world_revolution
			modifier = {
				war_support_factor = 0.15
				justify_war_goal_time = -0.30
				army_infantry_attack_factor = 0.08
			}
		}

		GER_weimar_democracy = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_weimar_eagle
			modifier = {
				stability_factor = 0.10
				political_power_factor = 0.15
				political_power_cost = -0.15
			}
		}

		GER_zollverein_subordination = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_customs_union
			modifier = {
				consumer_goods_factor = -0.03
				industrial_capacity_factory = 0.05
			}
		}

		GER_hindenburg_program = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_hindenburg_program
			modifier = {
				industrial_capacity_factory = 0.10
				consumer_goods_factor = 0.05
				production_factory_max_efficiency_factor = 0.10
			}
		}

		GER_operation_faustschlag_timed = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_faustschlag
			modifier = {
				breakthrough_factor = 0.20
				army_infantry_attack_factor = 0.15
				army_speed_factor = 0.10
			}
		}

		GER_continental_hegemony = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_continental_hegemony
			modifier = {
				war_support_factor = 0.15
				industrial_capacity_factory = 0.10
				stability_factor = 0.10
			}
		}

		GER_ohl_supreme_staff_coordination = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_staff_coordination
			modifier = {
				army_org_factor = 0.05
				max_dig_in = 5
			}
		}

		GER_vaterlandspartei_movement = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_vaterlandspartei
			modifier = {
				war_support_factor = 0.10
				mobilization_speed = 0.10
				stability_factor = -0.05
			}
		}

		GER_siegfrieden_triumph = {
			allowed = { always = no }
			removal_cost = -1
			picture = GFX_idea_GER_iron_cross
			modifier = {
				war_support_factor = 0.20
				army_infantry_attack_factor = 0.10
				industrial_capacity_factory = 0.15
				stability_factor = 0.10
			}
		}
'''

CATEGORIES_TXT = '''
GER_council_republic_revolution = {
	icon = generic_revolution
	allowed = {
		tag = GER
	}
	visible = {
		tag = GER
		has_government = communism
	}
	visible_when_empty = no
}

GER_weimar_democratic_diplomacy = {
	icon = generic_diplomacy
	allowed = {
		tag = GER
	}
	visible = {
		tag = GER
		has_government = democratic
	}
	visible_when_empty = no
}

GER_ohl_total_mobilization = {
	icon = military_operation
	allowed = {
		tag = GER
	}
	visible = {
		tag = GER
		has_country_flag = GER_third_ohl_established
	}
	visible_when_empty = no
}

GER_pan_german_annexations = {
	icon = generic_nationalism
	allowed = {
		tag = GER
	}
	visible = {
		tag = GER
		has_country_flag = GER_vaterlandspartei_founded
	}
	visible_when_empty = no
}
'''

DECISIONS_TXT = '''
# =========================================================================
# REWORKED GERMAN POLITICS & EXPANSION DECISIONS
# =========================================================================

# Council Republic Decisions
GER_council_republic_revolution = {
	ger_council_nationalize_heavy_syndicates = {
		icon = generic_industry
		cost = 50
		days_remove = 90
		available = {
			has_government = communism
		}
		visible = {
			has_government = communism
		}
		fire_only_once = yes
		complete_effect = {
			add_stability = -0.05
			57 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}
	}

	ger_council_red_guard_militia_call = {
		icon = generic_army
		cost = 40
		days_remove = 180
		available = {
			has_war = yes
			has_government = communism
		}
		visible = {
			has_government = communism
		}
		modifier = {
			mobilization_speed = 0.05
		}
		complete_effect = {
			add_manpower = 25000
		}
	}

	ger_council_propaganda_austria = {
		icon = generic_diplomacy
		cost = 35
		days_remove = 60
		available = {
			country_exists = AUS
			has_government = communism
		}
		visible = {
			has_government = communism
		}
		complete_effect = {
			AUS = {
				add_popularity = { ideology = communism popularity = 0.10 }
			}
		}
	}
}

# Weimar Democratic Decisions
GER_weimar_democratic_diplomacy = {
	ger_weimar_frankfurt_peace_congress = {
		icon = generic_diplomacy
		cost = 50
		days_remove = 120
		available = {
			has_government = democratic
		}
		visible = {
			has_government = democratic
		}
		fire_only_once = yes
		complete_effect = {
			add_stability = 0.08
			add_political_power = 60
		}
	}

	ger_weimar_expand_customs_treaty = {
		icon = generic_economy
		cost = 40
		days_remove = 360
		available = {
			has_government = democratic
		}
		visible = {
			has_government = democratic
		}
		modifier = {
			consumer_goods_factor = -0.02
		}
	}

	ger_weimar_rhineland_pacification = {
		icon = generic_industry
		cost = 30
		days_remove = 90
		available = {
			has_government = democratic
		}
		visible = {
			has_government = democratic
		}
		fire_only_once = yes
		complete_effect = {
			add_stability = 0.05
			42 = { # Rhineland
				add_extra_state_shared_building_slots = 1
				add_building_construction = {
					type = industrial_complex
					level = 1
					instant_build = yes
				}
			}
		}
	}
}

# OHL Total Mobilization Decisions
GER_ohl_total_mobilization = {
	ger_ohl_requisition_civilian_workshops = {
		icon = generic_industry
		cost = 50
		days_remove = 90
		available = {
			has_war = yes
			has_country_flag = GER_third_ohl_established
		}
		visible = {
			has_country_flag = GER_third_ohl_established
		}
		fire_only_once = yes
		complete_effect = {
			add_stability = -0.03
			57 = {
				add_building_construction = {
					type = arms_factory
					level = 1
					instant_build = yes
				}
			}
		}
	}

	ger_ohl_enforce_labor_quotas = {
		icon = generic_economy
		cost = 35
		days_remove = 180
		available = {
			has_war = yes
			has_country_flag = GER_third_ohl_established
		}
		visible = {
			has_country_flag = GER_third_ohl_established
		}
		modifier = {
			production_factory_efficiency_gain_factor = 0.10
		}
	}

	ger_ohl_deploy_sturmtruppen_spearhead = {
		icon = generic_army
		cost = 40
		days_remove = 60
		available = {
			has_war = yes
			has_country_flag = GER_third_ohl_established
		}
		visible = {
			has_country_flag = GER_third_ohl_established
		}
		modifier = {
			breakthrough_factor = 0.10
		}
	}
}

# Pan-German Annexation Decisions
GER_pan_german_annexations = {
	ger_pan_german_resettle_border_strip = {
		icon = generic_nationalism
		cost = 50
		days_remove = 120
		available = {
			has_country_flag = GER_vaterlandspartei_founded
		}
		visible = {
			has_country_flag = GER_vaterlandspartei_founded
		}
		fire_only_once = yes
		complete_effect = {
			add_manpower = 15000
			add_stability = 0.05
		}
	}

	ger_pan_german_annex_antwerp_harbor = {
		icon = generic_navy
		cost = 40
		days_remove = 90
		available = {
			has_country_flag = GER_vaterlandspartei_founded
		}
		visible = {
			has_country_flag = GER_vaterlandspartei_founded
		}
		fire_only_once = yes
		complete_effect = {
			navy_experience = 25
			add_war_support = 0.05
		}
	}

	ger_pan_german_caucasus_oil_concession = {
		icon = generic_industry
		cost = 60
		days_remove = 120
		available = {
			has_country_flag = GER_caucasus_oil_conquest_active
		}
		visible = {
			has_country_flag = GER_caucasus_oil_conquest_active
		}
		fire_only_once = yes
		complete_effect = {
			add_war_support = 0.05
			add_political_power = 60
		}
	}
}
'''
