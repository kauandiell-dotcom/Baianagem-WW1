# Data for French Ideas & Spirits
# Evolutive national spirits avoiding stat inflation

FRENCH_IDEAS = {
    "FRA_three_year_conscription": {
        "name": "The Three-Year Service Law",
        "desc": "Passed in 1913 after fierce parliamentary debates, this law extends mandatory military service from two to three years, allowing France to maintain a peacetime standing army capable of confronting German numerical superiority.",
        "sprite": "GFX_idea_FRA_three_year_law_of_1913-69197",
        "file_icon": "idea_French_staff.png",
        "modifier": {
            "conscription_factor": 0.15,
            "training_time_army_factor": -0.10,
            "political_power_factor": -0.05,
        }
    },
    "FRA_force_noire_integration": {
        "name": "La Force Noire Integration",
        "desc": "Conceived by General Charles Mangin, the mobilization of African colonial regiments bridges the demographic deficit of the metropole, deploying courageous Tirailleurs to the frontlines.",
        "sprite": "GFX_idea_FRA_arme_coloniale-69211",
        "file_icon": "indochina_union.png",
        "modifier": {
            "conscription_factor": 0.08,
            "non_core_manpower": 0.05,
            "stability_factor": -0.03,
        }
    },
    "FRA_exhausted_classes_crisis": {
        "name": "Demographic Exhaustion of 1917",
        "desc": "Years of attritional warfare on the Western Front have bled France's youth dry. Calling up older classes and wounded veterans strains the very fabric of French society.",
        "sprite": "GFX_idea_FRA_idea_disunited_french_front",
        "file_icon": "FRA_idea_disunited_french_front.png",
        "modifier": {
            "conscription_factor": -0.10,
            "monthly_population": -0.15,
            "surrender_limit": -0.05,
        }
    },
    "FRA_technological_manpower_substitution": {
        "name": "Technological Manpower Substitution",
        "desc": "As advocated by General Pétain, machines and firepower must replace human flesh. Renault FT light tanks and massed artillery batteries preserve French soldiers' lives.",
        "sprite": "GFX_idea_FRA_renault",
        "file_icon": "FRA_renault.png",
        "modifier": {
            "army_artillery_attack_factor": 0.05,
            "industrial_capacity_factory": 0.05,
            "army_org_factor": 0.05,
        }
    },
    "FRA_union_sacree_spirit": {
        "name": "L'Union Sacrée",
        "desc": "In August 1914, all political parties, from socialists to monarchists, pledged unconditional unity to defend the motherland against the German invader.",
        "sprite": "GFX_idea_FRA_union_sacre-73662",
        "file_icon": "fra_coat_of_arms.png",
        "modifier": {
            "stability_factor": 0.10,
            "war_support_factor": 0.15,
            "political_power_factor": 0.10,
        }
    },
    "FRA_wearing_union_sacree": {
        "name": "Strain on the Sacred Union",
        "desc": "The endless slaughter at Verdun and the Somme has rekindled parliamentary friction, socialist pacifism, and trade union strike threats.",
        "sprite": "GFX_idea_FRA_french_advisors_bad",
        "file_icon": "french_advisors_bad.png",
        "modifier": {
            "war_support_factor": 0.05,
            "political_power_factor": -0.08,
            "stability_factor": -0.05,
        }
    },
    "FRA_clemenceau_iron_resolve": {
        "name": "Je Fais la Guerre",
        "desc": "Georges Clemenceau has assumed wartime leadership with ruthless determination. Defeatists, pacifists, and profiteers are silenced in the singular pursuit of total victory.",
        "sprite": "GFX_idea_FRA_Georges_Clemenceau",
        "file_icon": "idea_FRA_Georges_Clemenceau.png",
        "modifier": {
            "war_support_factor": 0.15,
            "weekly_stability": 0.001,
            "surrender_limit": -0.10,
            "drift_defence_factor": 0.25,
        }
    },
    "FRA_revanche_accomplished": {
        "name": "Revanche Accomplished",
        "desc": "The stain of 1870 is finally washed away. Alsace and Lorraine have returned to the bosom of the Republic, restoring French pride and continental pre-eminence.",
        "sprite": "GFX_idea_FRA_Soldier_Choking_Eagel",
        "file_icon": "FRA_Soldier_Choking_Eagel.png",
        "modifier": {
            "stability_factor": 0.15,
            "war_support_factor": 0.10,
            "political_power_gain": 0.25,
        }
    },
    "FRA_lessons_of_the_frontiers": {
        "name": "Lessons of the Frontiers",
        "desc": "The disastrous frontal assaults of August 1914 shattered the dogma of blind offensive spirit. The French Army has learned the bloody primacy of defensive firepower and entrenchment.",
        "sprite": "GFX_idea_FRA_they_shall_not_pass",
        "file_icon": "FRA_they_shall_not_pass.png",
        "modifier": {
            "army_defence_factor": 0.08,
            "max_entrenchment": 4,
            "army_morale_factor": -0.03,
        }
    },
    "FRA_firepower_doctrine": {
        "name": "Firepower Doctrine (L'Artillerie Conquiert)",
        "desc": "Artillery conquers, infantry occupies. Coordinated creeping barrages and massive heavy shell concentrations prepare every trench assault.",
        "sprite": "GFX_idea_FRA_manufacture_saint_etienne",
        "file_icon": "FRA_manufacture_saint_etienne.png",
        "modifier": {
            "army_artillery_attack_factor": 0.10,
            "max_entrenchment": 5,
            "army_infantry_defence_factor": 0.05,
        }
    },
    "FRA_petain_elastic_defense": {
        "name": "Pétain's Elastic Defense & Welfare",
        "desc": "General Philippe Pétain reorganized frontline depth, instituted decent food and leave rotations, and halted suicidal mass infantry charges, restoring faith among the poilus.",
        "sprite": "GFX_idea_FRA_philippe_petain",
        "file_icon": "FRA_philippe_petain.png",
        "modifier": {
            "army_defence_factor": 0.10,
            "army_org_factor": 0.08,
            "supply_consumption_factor": -0.10,
        }
    },
    "FRA_supreme_combined_arms": {
        "name": "Allied Supreme Command & Combined Arms",
        "desc": "Under Supreme Commander Ferdinand Foch, coordinated waves of Renault FT tanks, tactical aviation, and massed artillery sweep forward in decisive breakthrough operations.",
        "sprite": "GFX_idea_FRA_ferdinand_foch",
        "file_icon": "idea_FRA_ferdinand_foch.png",
        "modifier": {
            "breakthrough_factor": 0.12,
            "army_armor_attack_factor": 0.15,
            "planning_speed": 0.15,
        }
    },
    "FRA_poincare_national_firmness": {
        "name": "Poincaré's National Firmness",
        "desc": "Elected President of the Republic in 1913, Raymond Poincaré brings dignified firmness to the executive branch, revitalizing national alliances and military preparedness.",
        "sprite": "GFX_idea_FRA_raymond_poincare",
        "file_icon": "FRA_raymond_poincare.png",
        "modifier": {
            "political_power_factor": 0.10,
            "stability_factor": 0.05,
        }
    },
    "FRA_war_cabinet_discipline": {
        "name": "Wartime Cabinet Concentration",
        "desc": "Facing existential conflict, partisan squabbling in the Chamber of Deputies has been curtailed in favor of executive decrees and emergency committees.",
        "sprite": "GFX_idea_FRA_french_advisors",
        "file_icon": "french_advisors.png",
        "modifier": {
            "political_power_factor": 0.15,
            "war_support_factor": 0.05,
        }
    },
    "FRA_parliamentary_mutiny_turmoil": {
        "name": "Parliamentary Turmoil of 1917",
        "desc": "Following the collapse of the Nivelle Offensive, strikes in Paris and mutinies in the trenches threaten to topple the civilian government.",
        "sprite": "GFX_idea_FRA_idea_disunited_french_front",
        "file_icon": "FRA_idea_disunited_french_front.png",
        "modifier": {
            "stability_factor": -0.15,
            "political_power_factor": -0.20,
        }
    },
    "FRA_the_tiger_dictatorship": {
        "name": "Le Tigre War Ministry",
        "desc": "Clemenceau exercises supreme political willpower over the nation. Parliament is held in line and all industrial and civilian energy is subordinated to the war effort.",
        "sprite": "GFX_idea_FRA_Georges_Clemenceau",
        "file_icon": "idea_FRA_Georges_Clemenceau.png",
        "modifier": {
            "political_power_gain": 0.30,
            "stability_factor": 0.10,
            "drift_defence_factor": 0.30,
        }
    },
    "FRA_socialist_welfare_state": {
        "name": "The Social and Democratic Republic",
        "desc": "Guided by Jean Jaurès and the SFIO, France has enacted the 8-hour workday, progressive income taxation, and industrial arbitration, creating a model of social justice.",
        "sprite": "GFX_idea_FRA_jean_jaures",
        "file_icon": "idea_FRA_jean_jaures.png",
        "modifier": {
            "consumer_goods_factor": 0.02,
            "production_factory_max_efficiency_factor": 0.10,
            "stability_factor": 0.15,
            "conscription_factor": -0.05,
        }
    },
    "FRA_commune_revolutionary_ardor": {
        "name": "Revolutionary Ardor of the Commune",
        "desc": "The resurrected French Commune mobilizes workers' militias and revolutionary enthusiasm, willing to fight to the last brick in defense of proletarian liberty.",
        "sprite": "GFX_idea_FRA_marcel_cachin",
        "file_icon": "FRA_marcel_cachin.png",
        "modifier": {
            "conscription_factor": 0.20,
            "army_morale_factor": 0.15,
            "surrender_limit": -0.25,
            "stability_factor": -0.10,
        }
    },
    "FRA_presidential_executive_authority": {
        "name": "Strong Presidential Republic",
        "desc": "Under constitutional overhaul, the President exercises extensive executive powers free from parliamentary instability, steering national policy with decisive authority.",
        "sprite": "GFX_idea_FRA_alexandre_millerand",
        "file_icon": "idea_FRA_alexandre_millerand.png",
        "modifier": {
            "political_power_gain": 0.25,
            "stability_factor": 0.10,
            "justify_war_goal_time": -0.15,
        }
    },
    "FRA_royalist_catholic_order": {
        "name": "Traditional Monarchy & Catholic Order",
        "desc": "Action Française has restored the throne of Saint Louis. Corporation councils, traditional provincial liberties, and firm hierarchy replace parliamentary decadence.",
        "sprite": "GFX_idea_FRA_action_francaise",
        "file_icon": "FRA_action_francaise.png",
        "modifier": {
            "stability_factor": 0.15,
            "political_power_gain": 0.20,
            "conscription_factor": 0.05,
            "research_speed_factor": -0.03,
        }
    },
    "FRA_renault_ft_revolution": {
        "name": "Renault FT Armored Vanguard",
        "desc": "The revolutionary Renault FT light tank revolutionized armored doctrine worldwide. Massed production and mechanical reliability crush enemy trench cordons.",
        "sprite": "GFX_idea_FRA_renault",
        "file_icon": "FRA_renault.png",
        "modifier": {
            "production_speed_armor_factor": 0.15,
            "army_armor_speed_factor": 0.10,
            "army_armor_attack_factor": 0.10,
        }
    },
    "FRA_air_supremacy_spad": {
        "name": "Aéronautique Militaire Hegemony",
        "desc": "Equipped with SPAD XIII fighters and Breguet 14 bombers, French squadrons command the western skies, coordinating directly with ground artillery.",
        "sprite": "GFX_idea_FRA_auguste_edouard_hirschauer",
        "file_icon": "idea_FRA_auguste_edouard_hirschauer.png",
        "modifier": {
            "air_superiority_factor": 0.15,
            "air_agility_factor": 0.10,
            "air_cas_efficiency": 0.10,
        }
    },
    "FRA_mediterranean_dominance": {
        "name": "Marine Nationale Mediterranean Shield",
        "desc": "The French fleet securely seals the Mediterranean Sea, protecting North African transport routes and bottle-necking Austro-Hungarian and Ottoman naval sorties.",
        "sprite": "GFX_idea_FRA_Auguste_Boue_de_Lapeyrere",
        "file_icon": "idea_FRA_Auguste_Boue_de_Lapeyrere.png",
        "modifier": {
            "naval_coordination": 0.15,
            "navy_screen_attack_factor": 0.10,
            "navy_capital_ship_defence_factor": 0.08,
        }
    },
    "FRA_shell_crisis_1914": {
        "name": "The 1914 Munition Famine",
        "desc": "Peacetime stockpiles of 75mm artillery shells were exhausted within weeks. Heavy industry must urgently convert civilian workshops to shell production.",
        "sprite": "GFX_idea_FRA_manufacture_saint_etienne",
        "file_icon": "FRA_manufacture_saint_etienne.png",
        "modifier": {
            "army_artillery_attack_factor": -0.15,
            "army_infantry_attack_factor": -0.05,
        }
    },
    "FRA_albert_thomas_munitions_boom": {
        "name": "Munitions Ministry Expansion",
        "desc": "Under socialist organizer Albert Thomas, France produces over 200,000 artillery shells daily, supplying not only the French Army but allied forces as well.",
        "sprite": "GFX_idea_FRA_metallurgique_de_normandie",
        "file_icon": "FRA_metallurgique_de_normandie.png",
        "modifier": {
            "industrial_capacity_factory": 0.12,
            "production_speed_arms_factory_factor": 0.15,
        }
    },
    "FRA_la_voie_sacree_convoy": {
        "name": "La Voie Sacrée Logistical Artery",
        "desc": "A continuous convoy of thousands of trucks runs day and night along the road to Verdun, ensuring constant rotation of fresh divisions and endless ammunition.",
        "sprite": "GFX_idea_FRA_berliet",
        "file_icon": "FRA_berliet.png",
        "modifier": {
            "supply_consumption_factor": -0.20,
            "land_reinforce_rate": 0.25,
            "army_core_defence_factor": 0.10,
        }
    },
    "FRA_1914_fiscal_solvency": {
        "name": "1914 Income Tax Solvency",
        "desc": "Joseph Caillaux's progressive income tax reform enacted in July 1914 modernizes the French treasury, providing stable fiscal revenue to sustain prolonged mobilization.",
        "sprite": "GFX_idea_FRA_crdit_lyonnais-45149",
        "file_icon": "FRA_crdit_lyonnais-45149.png",
        "modifier": {
            "consumer_goods_factor": -0.03,
            "production_speed_industrial_complex_factor": 0.05,
            "political_power_gain": 0.15,
        }
    },
    "FRA_horizon_blue_uniforms_idea": {
        "name": "Bleu Horizon & Adrian Helmets",
        "desc": "Abandoning the fatal red trousers, French troops don camouflage Bleu Horizon coats and Louis Adrian's stamped steel helmets, drastically slashing shrapnel head trauma.",
        "sprite": "GFX_idea_FRA_horizon_blue_uniforms-69197",
        "file_icon": "FRA_horizon_blue_uniforms-69197.png",
        "modifier": {
            "army_defence_factor": 0.08,
            "casualty_trickleback": 0.05,
        }
    },
    "FRA_lyautey_moroccan_order": {
        "name": "Lyautey's Moroccan Pacification",
        "desc": "General Hubert Lyautey combines political tact with surgical military columns to pacify tribal unrest, creating a stable protectorate and recruiting loyal colonial battalions.",
        "sprite": "GFX_idea_FRA_hubert_lyautey",
        "file_icon": "idea_FRA_hubert_lyautey.png",
        "modifier": {
            "non_core_manpower": 0.04,
            "stability_factor": 0.05,
            "resistance_decay": 0.10,
        }
    },
    "FRA_supreme_allied_command": {
        "name": "Supreme Allied War Council",
        "desc": "Established at Versailles to synchronize British, French, Italian, and American strategy, preventing fragmented national efforts in the face of German unified offensives.",
        "sprite": "GFX_idea_FRA_supreme_allied_command-46517",
        "file_icon": "FRA_supreme_allied_command-46517.png",
        "modifier": {
            "planning_speed": 0.15,
            "max_planning": 0.10,
            "army_org_factor": 0.05,
        }
    },
    "FRA_they_shall_not_pass": {
        "name": "'Ils Ne Passeront Pas!'",
        "desc": "The sacred vow of the poilus at Verdun. No German division shall breach the ring of forts, no matter the sacrifice demanded.",
        "sprite": "GFX_idea_FRA_they_shall_not_pass",
        "file_icon": "FRA_they_shall_not_pass.png",
        "modifier": {
            "army_core_defence_factor": 0.15,
            "army_morale_factor": 0.10,
            "entrenchment_speed_factor": 0.20,
        }
    },
    "FRA_russian_steamroller_pledge": {
        "name": "Russian Steamroller M+15 Commitment",
        "desc": "Under the Joffre-Zhilinsky staff protocols, the Imperial Russian Army pledges an immediate general invasion of East Prussia by the 15th day of mobilization, forcing Germany to divide its forces.",
        "sprite": "GFX_idea_FRA_investment_in_russia-45149",
        "file_icon": "FRA_investment_in_russia-45149.png",
        "modifier": {
            "army_morale_factor": 0.08,
            "planning_speed": 0.10,
        }
    },
    "FRA_british_naval_entente": {
        "name": "Anglo-French Naval Partition",
        "desc": "The Royal Navy guards the North Sea and English Channel, allowing the Marine Nationale to secure absolute dominance across the Western Mediterranean and French African sea lanes.",
        "sprite": "GFX_idea_FRA_entente_cordiale-45115",
        "file_icon": "FRA_entente_cordiale-45115.png",
        "modifier": {
            "naval_coordination": 0.20,
            "convoy_escort_efficiency": 0.15,
        }
    },
    "FRA_us_financial_pipeline": {
        "name": "J.P. Morgan Credit Pipeline",
        "desc": "American investment banking houses open multi-billion dollar credit lines for French munitions purchases, raw materials, and agricultural food shipments.",
        "sprite": "GFX_idea_FRA_crdit_lyonnais-45149",
        "file_icon": "FRA_crdit_lyonnais-45149.png",
        "modifier": {
            "consumer_goods_factor": -0.04,
            "industrial_capacity_factory": 0.05,
        }
    },
    "FRA_republican_vigilance": {
        "name": "Republican Vigilance",
        "desc": "Defending secular civic institutions against anti-republican agitation and reactionary factions.",
        "sprite": "GFX_idea_FRA_parliamentary_mutiny_turmoil",
        "file_icon": "FRA_parliamentary_mutiny_turmoil.png",
        "modifier": {
            "stability_factor": 0.05,
            "political_power_gain": 0.10,
        }
    }
}
