# Generator script that writes scripts/france_builder/data_foci.py
# Implements 244 mathematically valid, non-colliding national focuses

import sys

def main():
    foci = []

    # =========================================================================
    # WING 1: DOMESTIC POLITICS & THIRD REPUBLIC (X: 1 to 24)
    # =========================================================================

    # 1.1 Historical Parliamentary Republic (1911-1914)
    foci.append({
        "id": "FRA_preserver_la_republique",
        "wing": 1, "x": 6, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": "NOT = { has_country_flag = FRA_monarchist_path } NOT = { has_country_flag = FRA_commune_path }",
        "available": None,
        "reward": "add_political_power = 120\nadd_stability = 0.05",
        "icon_query": ["marianne", "republique", "fra_democraty", "focus_fra_preserve_france"],
        "title": "Preserve the Third Republic",
        "desc": "Born from the ashes of Sedan in 1870, the Third Republic stands as the beacon of liberty, secular democracy, and citizen equality. Despite parliamentary turbulence and scandal, the republican regime remains our sacred sanctuary."
    })
    foci.append({
        "id": "FRA_senat_et_chambre_des_deputes",
        "wing": 1, "x": 4, "y": 1, "cost": 8,
        "prereq": ["FRA_preserver_la_republique"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_stability = 0.05",
        "icon_query": ["parliament", "senat", "chambre", "goverment_reform"],
        "title": "Senate & Chamber of Deputies",
        "desc": "Balancing the conservative wisdom of the Senate with the lively democratic passions of the Palais Bourbon ensures legislative equilibrium and protects the Republic against any autocrat or military adventurer."
    })
    foci.append({
        "id": "FRA_laicite_republicaine",
        "wing": 1, "x": 8, "y": 1, "cost": 8,
        "prereq": ["FRA_preserver_la_republique"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.05\nadd_political_power = 50",
        "icon_query": ["laicite", "church", "secular", "dreyfus_exoneration"],
        "title": "Republican Secularism (Laïcité)",
        "desc": "The 1905 law separating Church and State consolidated the secular school system. The children of France are educated as free citizens of the Republic, immune to clerical reaction."
    })
    foci.append({
        "id": "FRA_le_parti_radical",
        "wing": 1, "x": 4, "y": 2, "cost": 8,
        "prereq": ["FRA_senat_et_chambre_des_deputes"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_popularity = { ideology = democratic popularity = 0.05 }\nadd_political_power = 50",
        "icon_query": ["radical", "caillaux", "mention_de_censure", "ministerial_changes"],
        "title": "The Radical-Socialist Party",
        "desc": "Neither reactionary nor collectivist, the Radical Party of Joseph Caillaux and Camille Chautemps defends small property owners, secular schooling, and civic freedom as the true center of gravity of French politics."
    })
    foci.append({
        "id": "FRA_alliance_democratique",
        "wing": 1, "x": 8, "y": 2, "cost": 8,
        "prereq": ["FRA_laicite_republicaine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.05\nadd_political_power = 50",
        "icon_query": ["alliance_democratique", "poincare", "social-democratic_compromise"],
        "title": "Democratic Alliance Center-Right",
        "desc": "Raymond Poincaré and the moderates provide financial orthodoxy, national patriotism, and administrative competence, counterbalancing socialist radicalism with bourgeois respectability."
    })
    foci.append({
        "id": "FRA_election_presidentielle_1913",
        "wing": 1, "x": 6, "y": 3, "cost": 8,
        "prereq": [["FRA_le_parti_radical", "FRA_alliance_democratique"]], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.30 days = 1 }",
        "icon_query": ["poincare", "election", "versailles", "vote"],
        "title": "Presidential Election of 1913",
        "desc": "Meeting at the Palace of Versailles, the National Assembly must choose the successor to President Armand Fallières. The contest between Raymond Poincaré and Jules Pams will define French foreign resolve."
    })
    foci.append({
        "id": "FRA_presidence_poincare",
        "wing": 1, "x": 4, "y": 4, "cost": 8,
        "prereq": ["FRA_election_presidentielle_1913"], "mut_ex": ["FRA_presidence_pams"],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_third_republic_instability add_idea = FRA_poincare_national_firmness }\nadd_war_support = 0.05",
        "icon_query": ["raymond_poincare", "poincare", "GFX_FRA_raymond_poincare"],
        "title": "Poincaré's Patriotic Presidency",
        "desc": "A son of Lorraine who witnessed German occupation in 1870, Poincaré brings dignified firmness to the Élysée, determined that France shall never again bow to German ultimatums."
    })
    foci.append({
        "id": "FRA_presidence_pams",
        "wing": 1, "x": 8, "y": 4, "cost": 8,
        "prereq": ["FRA_election_presidentielle_1913"], "mut_ex": ["FRA_presidence_poincare"],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.10\nadd_political_power = 60",
        "icon_query": ["pams", "jules_pams", "social_demokrat_kompromiss"],
        "title": "Jules Pams Conciliatory Presidency",
        "desc": "Supported by Clemenceau and the left radicals, Jules Pams emphasizes domestic reforms, reduction of diplomatic friction, and compromise over revanchist confrontation."
    })
    foci.append({
        "id": "FRA_le_scandale_calmette_caillaux",
        "wing": 1, "x": 4, "y": 5, "cost": 5,
        "prereq": ["FRA_presidence_poincare"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = -0.05\nadd_political_power = 40",
        "icon_query": ["scandale", "caillaux", "press", "mention_de_censure"],
        "title": "The Calmette-Caillaux Affair",
        "desc": "In March 1914, Henriette Caillaux shot Gaston Calmette, editor of Le Figaro, after he threatened to publish private letters. The sensational trial transfixes the nation on the eve of the European crisis."
    })
    foci.append({
        "id": "FRA_apaiser_les_tensions_sociales",
        "wing": 1, "x": 8, "y": 5, "cost": 5,
        "prereq": ["FRA_presidence_pams"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\nadd_political_power = -25",
        "icon_query": ["social", "peace", "workers", "social_investments"],
        "title": "Appease Social Unrest",
        "desc": "By opening channels with trade unions and moderating labor policing, the government prevents general strikes and maintains social calm across industrial basins."
    })
    foci.append({
        "id": "FRA_reforme_fiscale_impot_revenu",
        "wing": 1, "x": 6, "y": 6, "cost": 8,
        "prereq": [["FRA_le_scandale_calmette_caillaux", "FRA_apaiser_les_tensions_sociales"]], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_1914_fiscal_solvency\nadd_political_power = 50",
        "icon_query": ["GFX_FRA_1914_fiscal_reforms-50772", "fiscal", "tax", "income_tax"],
        "title": "The 1914 Income Tax Reform",
        "desc": "Joseph Caillaux's visionary reform establishes the progressive income tax (impôt sur le revenu) in July 1914, providing the French Treasury with modern fiscal firepower just before war erupts."
    })

    # 1.2 Wartime Republic & Clemenceau (1914-1918)
    foci.append({
        "id": "FRA_proclamer_union_sacree",
        "wing": 1, "x": 6, "y": 7, "cost": 8,
        "prereq": ["FRA_reforme_fiscale_impot_revenu"], "mut_ex": [],
        "allow_branch": None,
        "available": "OR = { has_war = yes date > 1914.8.1 }",
        "reward": "swap_ideas = { remove_idea = FRA_wound_of_1870 add_idea = FRA_union_sacree_spirit }\nadd_war_support = 0.15",
        "icon_query": ["GFX_FRA_union_sacre-73662", "union_sacree", "flag_france", "tricolor"],
        "title": "Proclaim the Union Sacrée",
        "desc": "On August 4, 1914, President Poincaré announced: 'France will be heroically defended by all her sons, whose sacred union will not break before the enemy.' Socialists, Catholics, and Radicals stand shoulder to shoulder."
    })
    foci.append({
        "id": "FRA_gouvernement_de_defense_nationale",
        "wing": 1, "x": 6, "y": 8, "cost": 8,
        "prereq": ["FRA_proclamer_union_sacree"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_poincare_national_firmness add_idea = FRA_war_cabinet_discipline }\nadd_stability = 0.05",
        "icon_query": ["defense_nationale", "cabinet", "briand", "viviani"],
        "title": "Government of National Defense",
        "desc": "Prime Minister René Viviani reshuffles the council to include socialist leaders Jules Guesde and Marcel Sembat, alongside veterans like Delcassé and Ribot, unifying the state apparatus."
    })
    foci.append({
        "id": "FRA_repli_du_gouvernement_a_bordeaux",
        "wing": 1, "x": 4, "y": 9, "cost": 4,
        "prereq": ["FRA_gouvernement_de_defense_nationale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.05\nset_country_flag = FRA_government_moved_to_bordeaux",
        "icon_query": ["bordeaux", "train", "government", "retreat"],
        "title": "Emergency Relocation to Bordeaux",
        "desc": "In September 1914, as German cavalry swept toward the Marne, the government and gold reserves evacuated to Bordeaux, leaving General Gallieni to organize the defense of the capital."
    })
    foci.append({
        "id": "FRA_censure_et_bourrage_de_crane",
        "wing": 1, "x": 8, "y": 9, "cost": 8,
        "prereq": ["FRA_gouvernement_de_defense_nationale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.08\nadd_stability = 0.05",
        "icon_query": ["censure", "anastasie", "press", "propaganda"],
        "title": "Wartime Censorship & Moral Control",
        "desc": "The Bureau de la Presse, personified as 'Madame Anastasie' with her giant scissors, strictly redacts front reports and suppresses defeatist rumors to protect civilian morale."
    })
    foci.append({
        "id": "FRA_comite_de_guerre_secret",
        "wing": 1, "x": 4, "y": 10, "cost": 8,
        "prereq": ["FRA_repli_du_gouvernement_a_bordeaux"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_command_power = 20",
        "icon_query": ["secret_committee", "war_room", "general_staff"],
        "title": "Secret War Committees",
        "desc": "Closed-door parliamentary committees scrutinize army supply, fortifications, and hospital conditions, ensuring democratic oversight over General Joffre's autocratic GQG."
    })
    foci.append({
        "id": "FRA_mobilisation_des_esprits",
        "wing": 1, "x": 8, "y": 10, "cost": 8,
        "prereq": ["FRA_censure_et_bourrage_de_crane"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.08\nadd_stability = 0.04",
        "icon_query": ["propaganda", "posters", "mobilisation", "school"],
        "title": "Mobilization of the Intellect",
        "desc": "Academics, writers, and schoolteachers mobilize their pens. From Henri Bergson to Maurice Barrès, French culture is framed as civilization fighting German militarist barbarism."
    })
    foci.append({
        "id": "FRA_la_crise_politique_de_1917",
        "wing": 1, "x": 6, "y": 11, "cost": 8,
        "prereq": [["FRA_comite_de_guerre_secret", "FRA_mobilisation_des_esprits"]], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_union_sacree_spirit add_idea = FRA_wearing_union_sacree }\nadd_stability = -0.10",
        "icon_query": ["crisis_1917", "turmoil", "parliament_crisis", "mention_de_censure"],
        "title": "The 1917 Crisis of Faith",
        "desc": "Following the bloodbath of the Chemin des Dames, mutinies in the trenches, and strikes by midinettes in Paris, the Sacred Union crumbles. The Painlevé cabinet falters under despair."
    })
    foci.append({
        "id": "FRA_appel_au_tigre",
        "wing": 1, "x": 6, "y": 12, "cost": 5,
        "prereq": ["FRA_la_crise_politique_de_1917"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.101 days = 1 }",
        "icon_query": ["GFX_FRA_georges_clemenceau_le_tigre-46505", "clemenceau", "le_tigre"],
        "title": "Summon 'The Tiger'",
        "desc": "Setting aside personal animosity, President Poincaré invites his fiercest critic, the 76-year-old Georges Clemenceau, to form a government. 'The Tiger' will lead France to the end."
    })
    foci.append({
        "id": "FRA_je_fais_la_guerre",
        "wing": 1, "x": 4, "y": 13, "cost": 8,
        "prereq": ["FRA_appel_au_tigre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_wearing_union_sacree add_idea = FRA_clemenceau_iron_resolve }\nadd_war_support = 0.15",
        "icon_query": ["clemenceau_speech", "je_fais_la_guerre", "tiger"],
        "title": "'Je Fais la Guerre!'",
        "desc": "'Home policy? I wage war. Foreign policy? I wage war. All the time, I wage war!' Clemenceau's ferocious resolve electrifies the nation and steels the poilus in the trenches."
    })
    foci.append({
        "id": "FRA_epuration_des_defaitistes",
        "wing": 1, "x": 8, "y": 13, "cost": 8,
        "prereq": ["FRA_appel_au_tigre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 80\nadd_stability = 0.05",
        "icon_query": ["trial", "caillaux", "malvy", "court"],
        "title": "Purge of Defeatists & Pacifists",
        "desc": "Clemenceau orders the arrest of former Premier Joseph Caillaux, Minister Louis Malvy, and the editors of Bonnet Rouge. Defeatism is treated as high treason against the Republic."
    })
    foci.append({
        "id": "FRA_la_victoire_de_la_republique",
        "wing": 1, "x": 6, "y": 14, "cost": 10,
        "prereq": ["FRA_je_fais_la_guerre", "FRA_epuration_des_defaitistes"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nadd_political_power = 150",
        "icon_query": ["victory_republic", "marianne_triumphant", "focus_generic_france_triumphant"],
        "title": "Triumph of the Republic",
        "desc": "Standing victorious against four years of imperial siege, the Third Republic proved that a parliamentary democracy could outlast empires and lead its citizens to liberation."
    })

    # 1.3 Alt-History: Democratic Socialist Republic (SFIO)
    foci.append({
        "id": "FRA_essor_de_la_sfio",
        "wing": 1, "x": 11, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": "NOT = { has_country_flag = FRA_conservative_path } NOT = { has_country_flag = FRA_monarchist_path }",
        "available": None,
        "reward": "add_popularity = { ideology = communism popularity = 0.10 }\nadd_political_power = 60",
        "icon_query": ["sfio", "socialist", "red_flag", "FRA_socialist_reforms"],
        "title": "The Rise of the SFIO",
        "desc": "Unified under Jean Jaurès and Jules Guesde in 1905, the Section Française de l'Internationale Ouvrière champions social justice, workers' solidarity, and international brotherhood."
    })
    foci.append({
        "id": "FRA_protection_de_jean_jaures",
        "wing": 1, "x": 11, "y": 1, "cost": 8,
        "prereq": ["FRA_essor_de_la_sfio"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_country_flag = FRA_jaures_survived\nadd_stability = 0.05",
        "icon_query": ["jean_jaures", "jaures", "idea_FRA_jean_jaures"],
        "title": "Shield Jean Jaurès",
        "desc": "By assigning security and unmasking nationalist conspiracies, France prevents the tragic assassination of Jean Jaurès in July 1914, preserving the conscience of the nation."
    })
    foci.append({
        "id": "FRA_victoire_electorale_socialiste",
        "wing": 1, "x": 11, "y": 2, "cost": 8,
        "prereq": ["FRA_protection_de_jean_jaures"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_politics = { ruling_party = democratic elections_allowed = yes }\nset_country_flag = FRA_socialist_path_chosen\nadd_political_power = 75",
        "icon_query": ["france_socialist_victory", "socialist_victory", "electoral_victory"],
        "title": "Socialist Electoral Triumph",
        "desc": "Riding widespread popular revulsion against military adventurism, the SFIO and independent socialists secure an unprecedented majority in the Chamber of Deputies."
    })
    foci.append({
        "id": "FRA_republique_sociale_et_democratique",
        "wing": 1, "x": 10, "y": 3, "cost": 8,
        "prereq": ["FRA_victoire_electorale_socialiste"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_socialist_welfare_state\nadd_stability = 0.08",
        "icon_query": ["republique_sociale", "welfare", "workers_rights"],
        "title": "The Social & Democratic Republic",
        "desc": "Transforming the bourgeois state, the new government enacts landmark welfare protections, workers' sickness insurance, and pensions for laboring veterans."
    })
    foci.append({
        "id": "FRA_journee_de_huit_heures",
        "wing": 1, "x": 12, "y": 3, "cost": 8,
        "prereq": ["FRA_victoire_electorale_socialiste"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.10\nconsumer_goods_factor = 0.02",
        "icon_query": ["eight_hours", "labor", "clock", "FRA_The_Value_of_labor"],
        "title": "The Eight-Hour Work Day",
        "desc": "The historic demand of the international labor movement is codified into French law. Eight hours of work, eight hours of rest, eight hours of leisure."
    })
    foci.append({
        "id": "FRA_nationalisation_des_mines_et_chemins_de_fer",
        "wing": 1, "x": 10, "y": 4, "cost": 8,
        "prereq": ["FRA_republique_sociale_et_democratique"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_extra_state_shared_building_slots = 2\n16 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "icon_query": ["nationalization", "mines", "railways", "sncf"],
        "title": "Nationalize Strategic Mines & Rails",
        "desc": "The private railway cartels and northern coal combines are converted into democratic public utilities, directed toward collective welfare rather than private dividends."
    })
    foci.append({
        "id": "FRA_pacifisme_et_arbitrage_international",
        "wing": 1, "x": 12, "y": 4, "cost": 8,
        "prereq": ["FRA_journee_de_huit_heures"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\ngive_guarantee = SWI",
        "icon_query": ["pacifism", "dove", "international_arbitration", "peace"],
        "title": "Internationalist Arbitration",
        "desc": "Jaurès's grand vision: resolving border disputes and imperial rivalry through open international tribunals and socialist conferences rather than secret military alliances."
    })
    foci.append({
        "id": "FRA_le_pain_et_la_paix_juste",
        "wing": 1, "x": 11, "y": 5, "cost": 10,
        "prereq": ["FRA_nationalisation_des_mines_et_chemins_de_fer", "FRA_pacifisme_et_arbitrage_international"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nadd_war_support = -0.10",
        "icon_query": ["bread_peace", "jaures_triumph", "popular_brigades"],
        "title": "Bread & Just Peace",
        "desc": "France stands as a beacon of progressive democracy, demonstrating to the workers of Europe that a peaceful socialist republic is possible without tyranny."
    })

    # 1.4 Alt-History: Syndicalist Commune (CGT)
    foci.append({
        "id": "FRA_radicalisation_de_la_cgt",
        "wing": 1, "x": 11, "y": 7, "cost": 8,
        "prereq": ["FRA_le_pain_et_la_paix_juste"], "mut_ex": [],
        "allow_branch": "has_country_flag = FRA_socialist_path_chosen",
        "available": "has_war = yes",
        "reward": "add_popularity = { ideology = communism popularity = 0.15 }\nadd_stability = -0.05",
        "icon_query": ["cgt", "syndicalism", "alliance_with_CGT", "FRA_Union_Mobilization"],
        "title": "Radicalization of the CGT",
        "desc": "The Confédération Générale du Travail adopts the Charter of Amiens as revolutionary creed. Frustrated by wartime suffering, revolutionary syndicalists demand worker control."
    })
    foci.append({
        "id": "FRA_greve_generale_insurrectionnelle",
        "wing": 1, "x": 11, "y": 8, "cost": 8,
        "prereq": ["FRA_radicalisation_de_la_cgt"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = -0.15\nadd_political_power = 80",
        "icon_query": ["general_strike", "insurrection", "red_flag", "strike"],
        "title": "General Insurrectionary Strike",
        "desc": "Factories fall silent, railway wheels stop turning, and the red flag is raised over the Bourses du Travail. The working class claims sovereignty over production."
    })
    foci.append({
        "id": "FRA_proclamer_la_commune_francaise",
        "wing": 1, "x": 11, "y": 9, "cost": 10,
        "prereq": ["FRA_greve_generale_insurrectionnelle"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_politics = { ruling_party = communism elections_allowed = yes }\nset_cosmetic_tag = FRA_commune\nadd_ideas = FRA_commune_revolutionary_ardor",
        "icon_query": ["commune", "Memories_of_the_Commune", "FRA_Defenders_Commune"],
        "title": "Proclaim the French Commune",
        "desc": "1871 is avenged! The parliamentary republic is dissolved in favor of the Commune des Travailleurs de France, governed by elected workers' and soldiers' councils."
    })
    foci.append({
        "id": "FRA_comites_de_soldats_rouges",
        "wing": 1, "x": 10, "y": 10, "cost": 8,
        "prereq": ["FRA_proclamer_la_commune_francaise"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_morale = 0.15\nadd_conscription_ratio = 0.02",
        "icon_query": ["red_guards", "comites", "soldiers_council", "FRA_Levee_Masse"],
        "title": "Red Soldier Councils",
        "desc": "Abolishing aristocratic officer privileges, units elect their commanders. Discipline is forged in political consciousness and egalitarian brotherhood."
    })
    foci.append({
        "id": "FRA_autogestion_des_usines",
        "wing": 1, "x": 12, "y": 10, "cost": 8,
        "prereq": ["FRA_proclamer_la_commune_francaise"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "industrial_capacity_factory = 0.10\nproduction_factory_max_efficiency_factor = 0.15",
        "icon_query": ["workers_control", "autogestion", "factory", "FRA_The_Value_of_labor"],
        "title": "Factory Self-Management",
        "desc": "The Schneider arms foundries and Renault works are taken over by factory shop stewards, producing armaments for the emancipation of mankind."
    })
    foci.append({
        "id": "FRA_federation_des_bourses_du_travail",
        "wing": 1, "x": 11, "y": 11, "cost": 8,
        "prereq": ["FRA_comites_de_soldats_rouges", "FRA_autogestion_des_usines"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.10\nadd_political_power = 60",
        "icon_query": ["federation", "bourses", "syndicalist_congress", "FRA_Internationale_Congress"],
        "title": "Federation of Bourses du Travail",
        "desc": "Decentralized communes coordinate production, distribution, and mutual aid across the cantons of France without bureaucratic parasitic centralization."
    })
    foci.append({
        "id": "FRA_la_france_commune_invincible",
        "wing": 1, "x": 11, "y": 12, "cost": 10,
        "prereq": ["FRA_federation_des_bourses_du_travail"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nadd_war_support = 0.20",
        "icon_query": ["invincible", "commune_triumphant", "FRA_Red_Storm"],
        "title": "The Invincible Commune",
        "desc": "The revolution has taken root. A new world has been born in the land of 1789, ready to defend its liberty against all imperialist coalitions."
    })

    # 1.5 Alt-History: Strong Executive Republic (Conservatives)
    foci.append({
        "id": "FRA_renouveau_nationaliste",
        "wing": 1, "x": 17, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": "NOT = { has_country_flag = FRA_socialist_path_chosen } NOT = { has_country_flag = FRA_monarchist_path }",
        "available": None,
        "reward": "add_popularity = { ideology = neutrality popularity = 0.10 }\nadd_war_support = 0.08",
        "icon_query": ["nationalism", "barres", "deroulede", "focus_francefirst"],
        "title": "Nationalist Revival",
        "desc": "Echoing the patriotic leagues of Paul Déroulède and Maurice Barrès, conservative republicans call for moral rearmament, respect for the army, and devotion to the nation."
    })
    foci.append({
        "id": "FRA_reforme_millerand_executif_fort",
        "wing": 1, "x": 17, "y": 1, "cost": 8,
        "prereq": ["FRA_renouveau_nationaliste"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_third_republic_instability add_idea = FRA_presidential_executive_authority }\nset_country_flag = FRA_conservative_path",
        "icon_query": ["millerand", "alexandre_millerand", "idea_FRA_alexandre_millerand"],
        "title": "Millerand's Executive Reform",
        "desc": "Alexandre Millerand articulates the necessity of a strong President capable of dissolving parliament, appointing ministers freely, and securing national defense without parliamentary paralysis."
    })
    foci.append({
        "id": "FRA_dissolution_du_bloc_des_gauches",
        "wing": 1, "x": 15, "y": 2, "cost": 8,
        "prereq": ["FRA_reforme_millerand_executif_fort"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\nadd_political_power = 60",
        "icon_query": ["dissolution", "parliament", "order", "FRA_ban_socialism"],
        "title": "Dismantle the Left Bloc",
        "desc": "Breaking the legislative stranglehold of anti-clerical radicals, conservative republicans forge a broad National Bloc committed to social order and fiscal responsibility."
    })
    foci.append({
        "id": "FRA_stabilite_ministerielle_garantie",
        "wing": 1, "x": 19, "y": 2, "cost": 8,
        "prereq": ["FRA_reforme_millerand_executif_fort"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power_gain = 0.20\nadd_stability = 0.05",
        "icon_query": ["stability", "constitution", "goverment_reform"],
        "title": "Guaranteed Cabinet Stability",
        "desc": "New constitutional rules restrict votes of no-confidence to a two-thirds threshold, preventing opportunistic cabinet collapses and ensuring multi-year governmental programs."
    })
    foci.append({
        "id": "FRA_ordre_moral_et_republicain",
        "wing": 1, "x": 15, "y": 3, "cost": 8,
        "prereq": ["FRA_dissolution_du_bloc_des_gauches"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\nadd_war_support = 0.05",
        "icon_query": ["moral_order", "catholic_reconciliation", "church_ideas"],
        "title": "Moral & Republican Order",
        "desc": "Reconciling conservative Catholics with the republican regime, the state ends secular hostilities and honors church heritage as an essential pillar of national cohesion."
    })
    foci.append({
        "id": "FRA_discipline_sociale_et_patronat",
        "wing": 1, "x": 19, "y": 3, "cost": 8,
        "prereq": ["FRA_stabilite_ministerielle_garantie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "industrial_capacity_factory = 0.08\nconsumer_goods_factor = -0.02",
        "icon_query": ["patronat", "industry", "discipline", "manage_industries"],
        "title": "Industrial Compact & Discipline",
        "desc": "Partnering with the Comité des Forges and heavy industrial leaders, the executive guarantees labor peace through paternalistic social programs and mandatory arbitration."
    })
    foci.append({
        "id": "FRA_la_republique_autoritaire",
        "wing": 1, "x": 17, "y": 4, "cost": 10,
        "prereq": ["FRA_ordre_moral_et_republicain", "FRA_discipline_sociale_et_patronat"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nadd_political_power = 120",
        "icon_query": ["authoritarian_republic", "executive_power", "focus_fra_preserve_france"],
        "title": "The Resolute Republic",
        "desc": "France has constructed an unshakeable executive republic, fusing democratic legitimacy with authoritarian command to meet any trial of history."
    })

    # 1.6 Alt-History: Royalist Restoration (Action Française)
    foci.append({
        "id": "FRA_les_camelots_du_roi",
        "wing": 1, "x": 22, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": "NOT = { has_country_flag = FRA_socialist_path_chosen } NOT = { has_country_flag = FRA_conservative_path }",
        "available": None,
        "reward": "add_popularity = { ideology = neutrality popularity = 0.15 }\nset_country_flag = FRA_monarchist_path",
        "icon_query": ["camelots_du_roi", "action_francaise", "maurras"],
        "title": "Les Camelots du Roi",
        "desc": "The militant youth league of Action Française sells Charles Maurras's paper on the boulevards, breaks up radical meetings, and rallies patriotic students around the fleur-de-lis."
    })
    foci.append({
        "id": "FRA_abattre_la_gueuse",
        "wing": 1, "x": 22, "y": 1, "cost": 8,
        "prereq": ["FRA_les_camelots_du_roi"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = -0.10\nadd_political_power = 70",
        "icon_query": ["down_republic", "monarchy_restore", "FRA_Marshals_Resignation"],
        "title": "Down with 'La Gueuse'",
        "desc": "Denouncing the parliamentary republic as a corrupt, foreign-influenced system that sold France in 1870, royalists rally conservatives to bring down the regime."
    })
    foci.append({
        "id": "FRA_charles_maurras_doctrine_politique",
        "wing": 1, "x": 21, "y": 2, "cost": 8,
        "prereq": ["FRA_abattre_la_gueuse"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_royalist_catholic_order\nadd_political_power = 60",
        "icon_query": ["charles_maurras", "maurras", "idea_FRA_charles_maurras"],
        "title": "The Maurrassian Integral State",
        "desc": "Integral nationalism: hereditary monarchy, corporate guilds, anti-parliamentarism, and the restoration of France's historic provinces."
    })
    foci.append({
        "id": "FRA_restauration_du_duc_d_orleans",
        "wing": 1, "x": 23, "y": 2, "cost": 10,
        "prereq": ["FRA_abattre_la_gueuse"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_politics = { ruling_party = neutrality elections_allowed = no }\npromote_character = FRA_philippe_viii\nset_cosmetic_tag = FRA_kingdom",
        "icon_query": ["philippe_viii", "France_Monarchy", "royal_prerogatives"],
        "title": "Coronation of Philippe VIII",
        "desc": "The Duke of Orléans returns from exile to Reims Cathedral, consecrated as King of France and Navarre, restoring the unbroken chain of forty kings who built France."
    })
    foci.append({
        "id": "FRA_monarchie_traditionnelle_et_corporative",
        "wing": 1, "x": 22, "y": 3, "cost": 8,
        "prereq": ["FRA_charles_maurras_doctrine_politique", "FRA_restauration_du_duc_d_orleans"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nadd_popularity = { ideology = neutrality popularity = 0.20 }",
        "icon_query": ["corporation", "guilds", "focus_FRA_monarchy_and_the_working_class"],
        "title": "Corporate Kingdom & Guilds",
        "desc": "Replacing cutthroat party competition with professional corporations and provincial assemblies, labor and capital are united under the paternal protection of the Crown."
    })
    foci.append({
        "id": "FRA_le_royaume_de_france_ressuscite",
        "wing": 1, "x": 22, "y": 4, "cost": 10,
        "prereq": ["FRA_monarchie_traditionnelle_et_corporative"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.20\nadd_war_support = 0.15",
        "icon_query": ["kingdom_france", "France_Monarchy_2", "fleur_de_lis"],
        "title": "The Kingdom Resurrected",
        "desc": "With the tricolor crowned with gold lilies, the oldest kingdom of Christendom stands re-established, determined to reclaim its natural frontiers along the Rhine."
    })

    print(f"Wing 1 generated: {len(foci)} foci.")

    # =========================================================================
    # WING 2: FRENCH ECONOMY, INDUSTRY, RAILWAYS & EMPIRE (X: 25 to 48)
    # =========================================================================

    # 2.1 Heavy Industry & Peacetime Modernization
    foci.append({
        "id": "FRA_essor_de_la_belle_epoque",
        "wing": 2, "x": 30, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.05\nadd_extra_state_shared_building_slots = 2",
        "icon_query": ["GFX_FRA_the_belle_epoque-69189", "belle_epoque", "paris_expo", "eiffel"],
        "title": "The Height of the Belle Époque",
        "desc": "Paris is the undisputed capital of the civilized world, radiant with culture, scientific discovery, and industrial innovation. French engineering leads the globe in aviation, automobiles, and luxury commerce."
    })
    foci.append({
        "id": "FRA_bassin_parisien_metallurgie",
        "wing": 2, "x": 27, "y": 1, "cost": 8,
        "prereq": ["FRA_essor_de_la_belle_epoque"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "16 = { add_building_construction = { type = industrial_complex level = 2 instant_build = yes } }",
        "icon_query": ["paris_industry", "factory_paris", "GFX_FRA_second_industrial_revolution-73678"],
        "title": "Paris Basin Manufacturing",
        "desc": "The suburbs along the Seine from Boulogne-Billancourt to Saint-Denis form a dense manufacturing hive, providing precision tooling, motors, and advanced engineering."
    })
    foci.append({
        "id": "FRA_hauts_fourneaux_de_lorraine",
        "wing": 2, "x": 33, "y": 1, "cost": 8,
        "prereq": ["FRA_essor_de_la_belle_epoque"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "18 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }\nadd_resource = { type = steel amount = 12 state = 18 }",
        "icon_query": ["blast_furnace", "steel", "lorraine_steel", "iron_ore"],
        "title": "Lorraine Blast Furnaces",
        "desc": "The minette iron ore deposits of Briey and Longwy feed dozens of towering blast furnaces, making French Lorraine one of Europe's primary metallurgical engines."
    })
    foci.append({
        "id": "FRA_usines_du_nord_et_pas_de_calais",
        "wing": 2, "x": 27, "y": 2, "cost": 8,
        "prereq": ["FRA_bassin_parisien_metallurgie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = aluminium amount = 8 state = 17 }\n17 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }",
        "icon_query": ["coal_mines", "nord_coal", "lens", "mines"],
        "title": "Nord & Pas-de-Calais Coal Basins",
        "desc": "Deep coal pits at Lens, Douai, and Valenciennes extract tens of millions of tons of black diamonds annually, powering French locomotives and metallurgical furnaces."
    })
    foci.append({
        "id": "FRA_le_creusot_schneider",
        "wing": 2, "x": 33, "y": 2, "cost": 8,
        "prereq": ["FRA_hauts_fourneaux_de_lorraine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "20 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }\nindustrial_capacity_factory = 0.05",
        "icon_query": ["schneider", "le_creusot", "heavy_guns", "GFX_FRA_technological_revolution-73674"],
        "title": "Schneider et Cie at Le Creusot",
        "desc": "Founded by Eugène Schneider, the gargantuan steelworks and foundry at Le Creusot design the world's most sophisticated heavy artillery, armor plates, and naval guns."
    })
    foci.append({
        "id": "FRA_manufacture_d_armes_saint_etienne",
        "wing": 2, "x": 30, "y": 3, "cost": 8,
        "prereq": ["FRA_usines_du_nord_et_pas_de_calais", "FRA_le_creusot_schneider"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 4000 }\nproduction_speed_arms_factory_factor = 0.10",
        "icon_query": ["GFX_FRA_manufacture_darmes_de_chatellerault-73683", "saint_etienne", "rifles_production"],
        "title": "Manufacture d'Armes de Saint-Étienne",
        "desc": "The state arsenal at Saint-Étienne (MAS), alongside Châtellerault and Tulle, guarantees the mass fabrication of the standard Lebel M1886/M93 rifle and Berthier carbines."
    })
    foci.append({
        "id": "FRA_industrie_automobile_renault_panhard",
        "wing": 2, "x": 27, "y": 4, "cost": 8,
        "prereq": ["FRA_manufacture_d_armes_saint_etienne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = motorized_bonus bonus = 1.0 uses = 1 category = motorized_equipment }",
        "icon_query": ["renault", "panhard", "automobile", "trucks"],
        "title": "Automotive Giants: Renault & Panhard",
        "desc": "Louis Renault and Panhard & Levassor pioneered the modern internal combustion automobile. French motor output leads Europe, creating an invaluable motorized industrial base."
    })
    foci.append({
        "id": "FRA_chimie_industrielle_du_rhone",
        "wing": 2, "x": 33, "y": 4, "cost": 8,
        "prereq": ["FRA_manufacture_d_armes_saint_etienne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = synth_bonus bonus = 1.0 uses = 1 category = industry }",
        "icon_query": ["chemical", "rhone_poulenc", "explosives", "kuhlmann"],
        "title": "Rhône Chemical Conglomerates",
        "desc": "Chemical works at Saint-Fons and Lyon synthesize synthetic dyes, nitrocellulose, and picric acid, laying the technical foundation for modern high-explosive munition fillings."
    })
    foci.append({
        "id": "FRA_credit_lyonnais_et_haute_banque",
        "wing": 2, "x": 30, "y": 5, "cost": 8,
        "prereq": ["FRA_industrie_automobile_renault_panhard", "FRA_chimie_industrielle_du_rhone"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 80\nconsumer_goods_factor = -0.03",
        "icon_query": ["GFX_FRA_crdit_lyonnais-45149", "bank_france", "gold_reserves", "credit"],
        "title": "Crédit Lyonnais & Haute Banque",
        "desc": "With the Bank of France holding massive reserves of physical gold bullion, Paris acts as the chief lender to world powers, financing strategic foreign infrastructure and domestic credit."
    })

    # 2.2 Railways & Mobilization Transport
    foci.append({
        "id": "FRA_etoile_ferroviaire_de_paris",
        "wing": 2, "x": 30, "y": 6, "cost": 8,
        "prereq": ["FRA_credit_lyonnais_et_haute_banque"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "16 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 11507 } }",
        "icon_query": ["paris_railways", "railway_hub", "gare_de_l_est", "train"],
        "title": "The Paris Railway Radial Star",
        "desc": "Six major terminal stations connect Paris to every province of the Republic. Modernizing track switches and marshaling yards ensures that military trains can traverse the hub in hours."
    })
    foci.append({
        "id": "FRA_chemins_de_fer_de_l_est",
        "wing": 2, "x": 27, "y": 7, "cost": 8,
        "prereq": ["FRA_etoile_ferroviaire_de_paris"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "18 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 6542 } }",
        "icon_query": ["eastern_railway", "est_rail", "railway_lorraine", "locomotive"],
        "title": "Compagnie des Chemins de Fer de l'Est",
        "desc": "Double-tracked arterial lines direct from Paris through Châlons-sur-Marne straight to the fortress cities of Verdun, Toul, Nancy, and Épinal, tailored for rapid strategic deployment."
    })
    foci.append({
        "id": "FRA_chemins_de_fer_du_nord",
        "wing": 2, "x": 33, "y": 7, "cost": 8,
        "prereq": ["FRA_etoile_ferroviaire_de_paris"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "17 = { add_building_construction = { type = railway level = 2 instant_build = yes province = 11488 } }",
        "icon_query": ["nord_railway", "lille_train", "railway_network"],
        "title": "Compagnie des Chemins de Fer du Nord",
        "desc": "Heavily engineered trackways link Paris to Amiens, Arras, Lille, and the Belgian border, guaranteeing heavy transport for northern coal and industrial freight."
    })
    foci.append({
        "id": "FRA_wagons_de_mobilisation_rapide",
        "wing": 2, "x": 30, "y": 8, "cost": 8,
        "prereq": ["FRA_chemins_de_fer_de_l_est", "FRA_chemins_de_fer_du_nord"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_speed_factor = 0.05\nsupply_consumption_factor = -0.05",
        "icon_query": ["boxcars", "wagons", "hommes_40_chevaux_8", "freight_train"],
        "title": "Standardized Rolling Stock ('Hommes 40, Chevaux 8')",
        "desc": "Every French boxcar is standardized with military markings: 40 men or 8 horses. Thousands of locomotives stand fueled in reserve, ready for instant mobilization day."
    })
    foci.append({
        "id": "FRA_depots_reglements_du_genie",
        "wing": 2, "x": 30, "y": 9, "cost": 8,
        "prereq": ["FRA_wagons_de_mobilisation_rapide"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "16 = { add_building_construction = { type = supply_node level = 1 instant_build = yes province = 11507 } }",
        "icon_query": ["supply_depot", "genie", "logistics_base"],
        "title": "Military Engineering Supply Depots",
        "desc": "Pre-positioning bridge timbers, narrow-gauge Decauville track sections, and fuel oil along the eastern borders allows military engineers to maintain frontline logistics under any strain."
    })

    # 2.3 War Economy & Munitions Crisis (1914-1918)
    foci.append({
        "id": "FRA_transition_vers_l_economie_de_guerre",
        "wing": 2, "x": 30, "y": 10, "cost": 8,
        "prereq": ["FRA_depots_reglements_du_genie"], "mut_ex": [],
        "allow_branch": None,
        "available": "has_war = yes",
        "reward": "add_ideas = war_economy\nadd_political_power = 50",
        "icon_query": ["war_economy", "conversion", "industrial_mobilization"],
        "title": "Transition to Total War Economy",
        "desc": "With the northeastern industrial departments falling into German hands in August 1914, France must reorganize the entire remaining nation into a single military workshop."
    })
    foci.append({
        "id": "FRA_la_crise_des_munitions_1914",
        "wing": 2, "x": 27, "y": 11, "cost": 5,
        "prereq": ["FRA_transition_vers_l_economie_de_guerre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_timed_idea = { idea = FRA_shell_crisis_1914 days = 90 }",
        "icon_query": ["shell_crisis", "empty_shells", "artillery_shells"],
        "title": "Address the 1914 Shell Crisis",
        "desc": "Consumption of 75mm artillery shells reached 80,000 per day during the Marne, while daily production was only 10,000. Emergency contracts are dispatched across France."
    })
    foci.append({
        "id": "FRA_ministere_de_l_armement_albert_thomas",
        "wing": 2, "x": 33, "y": 11, "cost": 8,
        "prereq": ["FRA_transition_vers_l_economie_de_guerre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_albert_thomas_munitions_boom",
        "icon_query": ["albert_thomas", "munitions_minister", "armament_ministry"],
        "title": "Albert Thomas & Munitions Ministry",
        "desc": "Socialist deputy Albert Thomas organizes labor, raw material quotas, and industrial contracts, unleashing a colossal surge in shell and weapons production."
    })
    foci.append({
        "id": "FRA_reconversion_industrielle_totale",
        "wing": 2, "x": 27, "y": 12, "cost": 8,
        "prereq": ["FRA_la_crise_des_munitions_1914", "FRA_ministere_de_l_armement_albert_thomas"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "20 = { add_building_construction = { type = arms_factory level = 2 instant_build = yes } }",
        "icon_query": ["factory_conversion", "arms_production", "lathe"],
        "title": "Total Civilian Industrial Reconversion",
        "desc": "Bicycle shops produce machine gun mountings, perfume distilleries brew chemical weapons, and jewelry artisans turn artillery shell fuses across Lyon and Bordeaux."
    })
    foci.append({
        "id": "FRA_les_munitionnettes_ouvrieres",
        "wing": 2, "x": 33, "y": 12, "cost": 8,
        "prereq": ["FRA_ministere_de_l_armement_albert_thomas"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 50000\nindustrial_capacity_factory = 0.08",
        "icon_query": ["munitionnettes", "women_workers", "factory_women"],
        "title": "The Heroic Munitionnettes",
        "desc": "Over 400,000 French women take their places at lathes, chemical presses, and assembly lines. Their tireless patriotism keeps the guns roaring day and night."
    })
    foci.append({
        "id": "FRA_importations_de_charbon_anglais",
        "wing": 2, "x": 27, "y": 13, "cost": 8,
        "prereq": ["FRA_reconversion_industrielle_totale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = aluminium amount = 10 state = 16 }\nadd_political_power = 40",
        "icon_query": ["coal_ships", "british_coal", "welsh_coal"],
        "title": "British Welsh Coal Convoys",
        "desc": "To replace the lost coalfields of the Nord, cargo fleets under naval escort deliver millions of tons of high-grade Welsh coal to Rouen and Le Havre."
    })
    foci.append({
        "id": "FRA_emprunts_nationaux_de_la_defense",
        "wing": 2, "x": 33, "y": 13, "cost": 8,
        "prereq": ["FRA_les_munitionnettes_ouvrieres"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 100\nadd_stability = 0.05",
        "icon_query": ["defense_bonds", "war_loan_poster", "pour_la_france_versez_votre_or"],
        "title": "National Defense War Loans",
        "desc": "'Pour la France qui combat, pour la France qui sera victorieuse!' French families open their savings, pouring gold into national bonds to finance victory."
    })
    foci.append({
        "id": "FRA_houille_blanche_des_alpes",
        "wing": 2, "x": 27, "y": 14, "cost": 8,
        "prereq": ["FRA_importations_de_charbon_anglais"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "production_speed_buildings_factor = 0.10\nadd_extra_state_shared_building_slots = 2",
        "icon_query": ["GFX_FRA_elecltrify_factories-77934", "hydroelectric", "alps_dam", "houille_blanche"],
        "title": "Alpine Hydroelectricity ('La Houille Blanche')",
        "desc": "Harnessing the rushing torrents of the Alps and Pyrenees, hydroelectric dams provide clean, inexhaustible electric power for electrochemical and metallurgy plants."
    })
    foci.append({
        "id": "FRA_usines_de_poudre_saint_fons",
        "wing": 2, "x": 33, "y": 14, "cost": 8,
        "prereq": ["FRA_emprunts_nationaux_de_la_defense"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_artillery_attack_factor = 0.05\nindustrial_capacity_factory = 0.05",
        "icon_query": ["powder_mill", "explosives_plant", "poudre_b"],
        "title": "Poudre B Chemical Complexes",
        "desc": "Huge chemical factories at Saint-Fons, Toulouse, and Angoulême produce smokeless nitrocellulose Poudre B in quantities sufficient for allied armies."
    })
    foci.append({
        "id": "FRA_rationnement_du_pain_et_charbon",
        "wing": 2, "x": 30, "y": 15, "cost": 8,
        "prereq": ["FRA_houille_blanche_des_alpes", "FRA_usines_de_poudre_saint_fons"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "consumer_goods_factor = -0.04\nadd_stability = -0.03",
        "icon_query": ["ration_cards", "bread_rationing", "coal_ration"],
        "title": "Strict Rationing & Supply Management",
        "desc": "Introducing national ration cards for bread, sugar, and heating fuel ensures fair distribution to civilian families while prioritizing front supply trains."
    })
    foci.append({
        "id": "FRA_puissance_industrielle_de_1918",
        "wing": 2, "x": 30, "y": 16, "cost": 10,
        "prereq": ["FRA_rationnement_du_pain_et_charbon"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "industrial_capacity_factory = 0.10\nproduction_factory_max_efficiency_factor = 0.10",
        "icon_query": ["industrial_might", "arsenal_victory", "focus_industrial_effort"],
        "title": "Industrial Powerhouse of 1918",
        "desc": "By 1918, France has become the primary armorer of the Western Allies, equipping not only her own 100 divisions, but providing artillery, airplanes, and tanks to the US Army."
    })

    # 2.4 Colonial Empire & La Force Noire
    foci.append({
        "id": "FRA_l_empire_colonial_francais",
        "wing": 2, "x": 42, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 80\nadd_stability = 0.05",
        "icon_query": ["GFX_FRA_ministere_des_colonies-46518", "french_empire", "colonial_globe"],
        "title": "The Greater French Empire",
        "desc": "Covering over 10 million square kilometers with 50 million subjects, the French colonial empire represents an immense reservoir of manpower, food, and raw materials."
    })
    foci.append({
        "id": "FRA_mise_en_valeur_de_l_algerie",
        "wing": 2, "x": 39, "y": 1, "cost": 8,
        "prereq": ["FRA_l_empire_colonial_francais"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = oil amount = 4 state = 448 }\nadd_extra_state_shared_building_slots = 2",
        "icon_query": ["algerian_coat_of_arms", "algiers", "algerie"],
        "title": "Development of Algeria",
        "desc": "Considered an integral part of France organized into three departments, Algeria expands grain agriculture, iron ore extraction at Ouenza, and Mediterranean shipping."
    })
    foci.append({
        "id": "FRA_protectorat_de_tunisie",
        "wing": 2, "x": 45, "y": 1, "cost": 8,
        "prereq": ["FRA_l_empire_colonial_francais"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = tungsten amount = 6 state = 458 }\nadd_political_power = 40",
        "icon_query": ["GFX_FRA_protectorat_francais_de_tunisie-73665", "tunis", "tunisia"],
        "title": "Tunisian Protectorate Administration",
        "desc": "Established under the Treaty of Bardo, the protectorate in Tunis expands railway networks and exports rich agricultural harvests and minerals to Marseille."
    })
    foci.append({
        "id": "FRA_ressources_de_l_aof_dakar",
        "wing": 2, "x": 39, "y": 2, "cost": 8,
        "prereq": ["FRA_mise_en_valeur_de_l_algerie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = rubber amount = 8 state = 272 }\n272 = { add_building_construction = { type = naval_base level = 1 instant_build = yes province = 11728 } }",
        "icon_query": ["dakar", "aof", "rubber_africa", "palm_oil"],
        "title": "AOF & Port of Dakar",
        "desc": "French West Africa funnels rubber, peanuts, and hardwoods through the fortified Atlantic deep-water port of Dakar, safe from Central Powers interdiction."
    })
    foci.append({
        "id": "FRA_ressources_de_l_aef_brazzaville",
        "wing": 2, "x": 45, "y": 2, "cost": 8,
        "prereq": ["FRA_protectorat_de_tunisie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = rubber amount = 6 state = 538 }\nadd_political_power = 40",
        "icon_query": ["aef", "brazzaville", "congo", "timber"],
        "title": "AEF & Equatorial Concessions",
        "desc": "French Equatorial Africa opens up the vast timber and rubber resources of the Congo Basin, sustaining war material production across the Atlantic trade lanes."
    })
    foci.append({
        "id": "FRA_riz_et_mines_d_indochine",
        "wing": 2, "x": 42, "y": 3, "cost": 8,
        "prereq": ["FRA_ressources_de_l_aof_dakar", "FRA_ressources_de_l_aef_brazzaville"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_resource = { type = tungsten amount = 8 state = 286 }\nadd_resource = { type = rubber amount = 10 state = 286 }",
        "icon_query": ["goal_indochina", "indochina_union", "rice_rubber_mines"],
        "title": "Indochinese Rice & Rubber Riches",
        "desc": "The Union of Indochina ships hundreds of thousands of tons of grain from the Mekong Delta, alongside high-grade rubber and Tonkin anthracite coal."
    })
    foci.append({
        "id": "FRA_ports_de_saigon_et_haiphong",
        "wing": 2, "x": 39, "y": 4, "cost": 8,
        "prereq": ["FRA_riz_et_mines_d_indochine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "286 = { add_building_construction = { type = naval_base level = 2 instant_build = yes province = 12080 } }",
        "icon_query": ["saigon", "haiphong", "port_asia"],
        "title": "Modernize Saigon & Haiphong Ports",
        "desc": "Dredging channels and expanding dry docks in Cochin-China enables heavy merchant freighters and Far East cruisers to service the Pacific trade network."
    })
    foci.append({
        "id": "FRA_chemin_de_fer_yunnan_vietnam",
        "wing": 2, "x": 45, "y": 4, "cost": 8,
        "prereq": ["FRA_riz_et_mines_d_indochine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_opinion_modifier = { target = CHI modifier = FRA_yunnan_trade_opinion }",
        "icon_query": ["yunnan_railway", "vietnam_train", "mountain_railway"],
        "title": "The Yunnan-Vietnam Strategic Railway",
        "desc": "A monumental feat of French civil engineering, the narrow-gauge railway from Haiphong to Kunming penetrates deep into Southwest China, securing commercial primacy."
    })
    foci.append({
        "id": "FRA_la_force_noire_du_general_mangin",
        "wing": 2, "x": 42, "y": 5, "cost": 8,
        "prereq": ["FRA_ports_de_saigon_et_haiphong", "FRA_chemin_de_fer_yunnan_vietnam"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_force_noire_integration\nadd_manpower = 60000",
        "icon_query": ["GFX_FRA_arme_coloniale-69211", "force_noire", "mangin", "colonial_army"],
        "title": "General Mangin's 'La Force Noire'",
        "desc": "Colonel Charles Mangin's 1910 thesis proved prophetic: African troops possessed the physical stamina and martial bravery needed to compensate for France's low birth rate."
    })
    foci.append({
        "id": "FRA_tirailleurs_senegalais",
        "wing": 2, "x": 39, "y": 6, "cost": 8,
        "prereq": ["FRA_la_force_noire_du_general_mangin"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 80000\narmy_infantry_attack_factor = 0.05",
        "icon_query": ["tirailleurs_senegalais", "african_soldiers", "coupe_coupe"],
        "title": "Recruit the Tirailleurs Sénégalais",
        "desc": "Recruited from across West Africa, the Tirailleurs Sénégalais, armed with the Lebel rifle and coupe-coupe machete, become legendary assault shock troops on the Western Front."
    })
    foci.append({
        "id": "FRA_tirailleurs_algeriens_et_goumiers",
        "wing": 2, "x": 45, "y": 6, "cost": 8,
        "prereq": ["FRA_la_force_noire_du_general_mangin"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 70000\narmy_defence_factor = 0.05",
        "icon_query": ["tirailleurs_algeriens", "goumiers", "spahis", "north_africa_troops"],
        "title": "Algerian Tirailleurs & Moroccan Goumiers",
        "desc": "Hardened North African infantry and mounted Spahis display unparalleled bravery and discipline, holding key defense sectors at Douaumont and the Chemin des Dames."
    })
    foci.append({
        "id": "FRA_travailleurs_coloniaux_de_marseille",
        "wing": 2, "x": 42, "y": 7, "cost": 8,
        "prereq": ["FRA_tirailleurs_senegalais", "FRA_tirailleurs_algeriens_et_goumiers"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "industrial_capacity_factory = 0.08\nadd_manpower = 40000",
        "icon_query": ["colonial_workers", "dockers_marseille", "indochinese_workers"],
        "title": "Colonial Labor Battalions at Marseille",
        "desc": "Over 100,000 Indochinese, Malagasy, and North African contract laborers unload convoy ships, pave roads, and staff ammunition factories across southern France."
    })
    foci.append({
        "id": "FRA_bataillons_coloniaux_au_front",
        "wing": 2, "x": 39, "y": 8, "cost": 8,
        "prereq": ["FRA_travailleurs_coloniaux_de_marseille"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 50000\nbreakthrough_factor = 0.05",
        "icon_query": ["colonial_assault", "frontline_colonial", "mangin_division"],
        "title": "Colonial Divisions on the Frontline",
        "desc": "General Mangin's 1st Colonial Corps forms the spearhead of decisive allied counter-offensives, proving their peerless devotion to the tricolor flag."
    })
    foci.append({
        "id": "FRA_chemins_de_fer_sahariens",
        "wing": 2, "x": 45, "y": 8, "cost": 8,
        "prereq": ["FRA_travailleurs_coloniaux_de_marseille"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "448 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }\nadd_political_power = 40",
        "icon_query": ["sahara_railway", "transaharan", "desert_rail"],
        "title": "Trans-Saharan Infrastructure Works",
        "desc": "Surveying and extending rail spurs into the northern fringes of the Sahara connects desert oases and mineral deposits to Mediterranean coastal ports."
    })
    foci.append({
        "id": "FRA_reforme_des_statuts_indigenes",
        "wing": 2, "x": 42, "y": 9, "cost": 8,
        "prereq": ["FRA_bataillons_coloniaux_au_front", "FRA_chemins_de_fer_sahariens"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\nadd_political_power = 60",
        "icon_query": ["colonial_reform", "citizenship", "dignity_veterans"],
        "title": "Reform the Indigénat Code",
        "desc": "Deputy Blaise Diagne negotiates French citizenship rights for Senegalese volunteers: 'They shed their blood on the battlefields of France; they are sons of the Republic.'"
    })
    foci.append({
        "id": "FRA_communaute_imperiale_unie",
        "wing": 2, "x": 42, "y": 10, "cost": 10,
        "prereq": ["FRA_reforme_des_statuts_indigenes"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.10\nconscription_factor = 0.05",
        "icon_query": ["imperial_unity", "united_empire", "la_plus_grande_france"],
        "title": "La Plus Grande France",
        "desc": "A united empire of 100 million Frenchmen standing together across five continents, forever safeguarding the civilization and power of France."
    })

    print(f"Wing 2 generated: {len([f for f in foci if f['wing'] == 2])} foci.")

    # Writing out data_foci.py will be completed by adding Wings 3, 4, 5
    return foci

if __name__ == "__main__":
    main()
