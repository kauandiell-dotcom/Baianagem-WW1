# -*- coding: utf-8 -*-
"""Event definitions for Germany Politics & Society Wing (events 201-242)."""

EVENTS_TXT = '''
# =========================================================================
# REWORKED POLITICS & EXPANSION EVENTS (ww1_germany_events.201 - 242)
# =========================================================================

# 1912 Reichstag Elections
country_event = {
	id = ww1_germany_events.201
	title = ww1_germany_events.201.t
	desc = ww1_germany_events.201.d
	picture = GFX_event_WW1_ger_republic
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.201.a # Compromise with the SPD majority
		ai_chance = { factor = 50 }
		add_political_power = 40
		add_stability = 0.05
		add_popularity = { ideology = democratic popularity = 0.10 }
	}

	option = {
		name = ww1_germany_events.201.b # Form an imperial conservative-clerical bloc
		ai_chance = { factor = 50 }
		add_political_power = 75
		add_stability = -0.05
		add_popularity = { ideology = neutrality popularity = 0.10 }
	}
}

# Crisis of the Prussian Franchise
country_event = {
	id = ww1_germany_events.202
	title = ww1_germany_events.202.t
	desc = ww1_germany_events.202.d
	picture = GFX_event_WW1_ger_berlin_strike
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.202.a # Promise electoral reform after victory
		ai_chance = { factor = 70 }
		add_political_power = 50
		add_stability = 0.03
	}

	option = {
		name = ww1_germany_events.202.b # Reject reform: Prussian order must stand!
		ai_chance = { factor = 30 }
		add_political_power = 80
		add_stability = -0.05
		add_war_support = 0.05
	}
}

# The Spartakusbund Rises
country_event = {
	id = ww1_germany_events.210
	title = ww1_germany_events.210.t
	desc = ww1_germany_events.210.d
	picture = GFX_event_WW1_ger_january_strikes
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.210.a # All power to the workers' councils!
		ai_chance = { factor = 100 }
		add_political_power = 50
		add_war_support = 0.10
		add_stability = -0.05
	}
}

# Mutiny in the High Seas Fleet
country_event = {
	id = ww1_germany_events.211
	title = ww1_germany_events.211.t
	desc = ww1_germany_events.211.d
	picture = GFX_event_WW1_ger_berlin_strike
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.211.a # Hoist the red flag on every dreadnought!
		ai_chance = { factor = 100 }
		navy_experience = 25
		add_war_support = 0.05
	}
}

# Proclamation of the Free Socialist Republic
country_event = {
	id = ww1_germany_events.212
	title = ww1_germany_events.212.t
	desc = ww1_germany_events.212.d
	picture = GFX_event_WW1_ger_republic
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.212.a # Long live the socialist world revolution!
		ai_chance = { factor = 100 }
		add_political_power = 100
		add_stability = 0.10
	}
}

# The Treaty of Red Berlin
country_event = {
	id = ww1_germany_events.213
	title = ww1_germany_events.213.t
	desc = ww1_germany_events.213.d
	picture = GFX_event_WW1_sov_poland
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.213.a # Ratify the fraternal socialist alliance!
		ai_chance = { factor = 100 }
		add_political_power = 80
		if = {
			limit = { country_exists = SOV }
			create_faction = "Rote Internationale"
			add_to_faction = SOV
		}
	}
}

# The Danubian Socialist Federation
country_event = {
	id = ww1_germany_events.214
	title = ww1_germany_events.214.t
	desc = ww1_germany_events.214.d
	picture = GFX_event_WW1_sov_ukraine
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.214.a # Integrate our Danubian comrades!
		ai_chance = { factor = 100 }
		add_political_power = 75
		if = {
			limit = { country_exists = AUS }
			AUS = {
				set_politics = { ruling_party = communism }
			}
		}
		if = {
			limit = { country_exists = HUN }
			HUN = {
				set_politics = { ruling_party = communism }
			}
		}
	}
}

# Proclamation of the German Republic
country_event = {
	id = ww1_germany_events.220
	title = ww1_germany_events.220.t
	desc = ww1_germany_events.220.d
	picture = GFX_event_WW1_ger_republic
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.220.a # Long live the German Republic!
		ai_chance = { factor = 100 }
		add_political_power = 100
		add_stability = 0.10
	}
}

# Negotiations on Wilson's Fourteen Points
country_event = {
	id = ww1_germany_events.221
	title = ww1_germany_events.221.t
	desc = ww1_germany_events.221.d
	picture = GFX_event_WW1_ger_peace_resolution
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.221.a # Accept the 14 Points as basis for peace
		ai_chance = { factor = 80 }
		add_political_power = 75
		add_war_support = -0.05
		add_stability = 0.05
	}

	option = {
		name = ww1_germany_events.221.b # Demand colonial guarantees in return
		ai_chance = { factor = 20 }
		add_political_power = 50
		add_war_support = 0.05
	}
}

# The Plebiscite in Alsace-Lorraine
country_event = {
	id = ww1_germany_events.222
	title = ww1_germany_events.222.t
	desc = ww1_germany_events.222.d
	picture = GFX_event_WW1_ger_republic
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.222.a # Respect the popular mandate!
		ai_chance = { factor = 100 }
		add_political_power = 60
		add_stability = 0.05
	}
}

# The Silent Dictatorship Assumes Control
country_event = {
	id = ww1_germany_events.230
	title = ww1_germany_events.230.t
	desc = ww1_germany_events.230.d
	picture = GFX_event_WW1_ger_third_ohl
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.230.a # All authority to the Supreme War Command!
		ai_chance = { factor = 100 }
		add_war_support = 0.10
		add_political_power = 50
	}
}

# The Declaration of Unrestricted Submarine Warfare
country_event = {
	id = ww1_germany_events.231
	title = ww1_germany_events.231.t
	desc = ww1_germany_events.231.d
	picture = GFX_event_WW1_ger_third_ohl
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.231.a # Sink all shipping bound for Britain!
		ai_chance = { factor = 85 }
		navy_experience = 35
		add_war_support = 0.08
		if = {
			limit = { country_exists = USA }
			USA = { add_opinion_modifier = { target = GER modifier = ger_unrestricted_submarines_outrage } }
		}
	}

	option = {
		name = ww1_germany_events.231.b # Adhere strictly to cruiser prize rules
		ai_chance = { factor = 15 }
		add_political_power = 50
		add_war_support = -0.05
	}
}

# The Dismemberment of the Russian Empire
country_event = {
	id = ww1_germany_events.232
	title = ww1_germany_events.232.t
	desc = ww1_germany_events.232.d
	picture = GFX_event_WW1_sov_baltic
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.232.a # Enforce the German imperial sphere in the East!
		ai_chance = { factor = 100 }
		add_political_power = 120
		add_war_support = 0.10
	}
}

# Founding of the Deutsche Vaterlandspartei
country_event = {
	id = ww1_germany_events.240
	title = ww1_germany_events.240.t
	desc = ww1_germany_events.240.d
	picture = GFX_event_WW1_ger_third_ohl
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.240.a # For Kaiser, Volk and Total Victory!
		ai_chance = { factor = 100 }
		add_war_support = 0.15
		add_political_power = 80
	}
}

# The Dissolution of the Reichstag
country_event = {
	id = ww1_germany_events.241
	title = ww1_germany_events.241.t
	desc = ww1_germany_events.241.d
	picture = GFX_event_WW1_ger_berlin_strike
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.241.a # Parliament is dissolved. The nation is at war!
		ai_chance = { factor = 100 }
		add_political_power = 100
		add_stability = -0.05
		add_war_support = 0.10
	}
}

# The Ultimatum to the Low Countries
country_event = {
	id = ww1_germany_events.242
	title = ww1_germany_events.242.t
	desc = ww1_germany_events.242.d
	picture = GFX_event_WW1_ger_third_ohl
	is_triggered_only = yes

	option = {
		name = ww1_germany_events.242.a # Surrender your ports or face iron and fire!
		ai_chance = { factor = 100 }
		add_war_support = 0.08
		add_political_power = 50
	}
}
'''
