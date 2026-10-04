# Wing 5: Foreign Policy, Alliances, Crises & Endgames (48 foci)
# Coordinated geometry x: 106 to 135, strictly dy >= 1

def get_wing_5_foci():
    foci = []

    # 5.1 Moroccan Question & Agadir 1911
    foci.append({
        "id": "FRA_question_du_maroc_1911",
        "wing": 5, "x": 111, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_stability = 0.05",
        "icon_query": ["maroc", "morocco", "sultan_maroc", "fez"],
        "title": "The Moroccan Question",
        "desc": "The Sherifian Empire has fallen into tribal revolt and fiscal bankruptcy. To protect French citizens in Fez and consolidate North Africa, France must assert imperial paramountcy."
    })
    foci.append({
        "id": "FRA_reponse_au_coup_d_agadir",
        "wing": 5, "x": 111, "y": 1, "cost": 5,
        "prereq": ["FRA_question_du_maroc_1911"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.1 days = 1 }",
        "icon_query": ["GFX_FRA_agadir_crisis-69194", "agadir", "panther_gunboat"],
        "title": "Response to the Agadir Crisis",
        "desc": "July 1911: The German gunboat SMS Panther anchors at the Atlantic port of Agadir to challenge French hegemony. Paris refuses to be intimidated by gunboat diplomacy."
    })
    foci.append({
        "id": "FRA_soutien_du_cabinet_britannique",
        "wing": 5, "x": 108, "y": 2, "cost": 5,
        "prereq": ["FRA_reponse_au_coup_d_agadir"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = ENG modifier = FRA_entente_support_opinion }\nadd_war_support = 0.05",
        "icon_query": ["mansion_house", "lloyd_george", "british_alliance"],
        "title": "British Mansion House Solidarity",
        "desc": "David Lloyd George declares that Britain will not allow peace to be bought at the price of humiliation, standing shoulder-to-shoulder with France against German sabre-rattling."
    })
    foci.append({
        "id": "FRA_accord_colonial_franco_allemand",
        "wing": 5, "x": 114, "y": 2, "cost": 5,
        "prereq": ["FRA_reponse_au_coup_d_agadir"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_country_flag = FRA_congo_ceded_for_morocco\nadd_political_power = 50",
        "icon_query": ["colonial_accord", "congo_treaty", "treaty_negotiation"],
        "title": "Franco-German Colonial Settlement",
        "desc": "Premier Joseph Caillaux concludes a pragmatic bilateral exchange: France cedes part of the French Congo (Neukamerun) in exchange for Germany's recognition of France in Morocco."
    })
    foci.append({
        "id": "FRA_traite_de_fez_1912",
        "wing": 5, "x": 111, "y": 3, "cost": 8,
        "prereq": ["FRA_soutien_du_cabinet_britannique", "FRA_accord_colonial_franco_allemand"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.10 days = 1 }",
        "icon_query": ["GFX_FRA_protectorat_franais_au_maroc-73665", "traite_de_fez", "protectorat_maroc"],
        "title": "The Treaty of Fez (March 1912)",
        "desc": "Sultan Abd al-Hafid signs the formal treaty establishing the French Protectorate in Morocco, securing our western Mediterranean flank from Tangier to the Atlas."
    })
    foci.append({
        "id": "FRA_pacification_du_maroc_lyautey",
        "wing": 5, "x": 111, "y": 4, "cost": 8,
        "prereq": ["FRA_traite_de_fez_1912"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_hubert_lyautey\nadd_ideas = FRA_lyautey_moroccan_order",
        "icon_query": ["lyautey", "hubert_lyautey", "GFX_FRA_hubert_lyautey"],
        "title": "Resident-General Hubert Lyautey",
        "desc": "General Lyautey pacifies rebellious tribes with diplomacy, schools, and roads rather than brutal destruction: 'Show strength so as not to have to use it.'"
    })

    # 5.2 Three-Year Law of 1913
    foci.append({
        "id": "FRA_la_loi_des_trois_ans_1913",
        "wing": 5, "x": 111, "y": 5, "cost": 8,
        "prereq": ["FRA_pacification_du_maroc_lyautey"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.20 days = 1 }",
        "icon_query": ["GFX_FRA_threeyear_law-69197", "three_year_law", "loi_de_trois_ans"],
        "title": "The Three-Year Law Debate (1913)",
        "desc": "Facing the German Army Law of 1912, France must act. With only 39 million citizens against 65 million Germans, extending conscription to 3 years is a life-or-death decision."
    })
    foci.append({
        "id": "FRA_adopter_fermement_trois_ans",
        "wing": 5, "x": 108, "y": 6, "cost": 8,
        "prereq": ["FRA_la_loi_des_trois_ans_1913"], "mut_ex": ["FRA_compromis_des_deux_ans_et_demi"],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_demographic_stagnation add_idea = FRA_three_year_conscription }\nadd_manpower = 120000",
        "icon_query": ["conscription_three_years", "barracks_conscription", "active_service"],
        "title": "Adopt the Full Three-Year Service",
        "desc": "Despite socialist strikes and protests led by Jaurès, the law passes in August 1913, increasing the French standing peacetime army to 820,000 men on the eve of war."
    })
    foci.append({
        "id": "FRA_compromis_des_deux_ans_et_demi",
        "wing": 5, "x": 114, "y": 6, "cost": 8,
        "prereq": ["FRA_la_loi_des_trois_ans_1913"], "mut_ex": ["FRA_adopter_fermement_trois_ans"],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 60000\nadd_stability = 0.08",
        "icon_query": ["compromise_law", "social_peace", "conscription_compromise"],
        "title": "Two-and-a-Half Year Compromise",
        "desc": "A middle path between the army high command and socialist opposition: service is modestly extended, avoiding widespread domestic strikes while moderately boosting reserves."
    })
    foci.append({
        "id": "FRA_integration_des_conscrits_de_1913",
        "wing": 5, "x": 111, "y": 7, "cost": 8,
        "prereq": [["FRA_adopter_fermement_trois_ans", "FRA_compromis_des_deux_ans_et_demi"]], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "training_time_army_factor = -0.15\narmy_experience = 20",
        "icon_query": ["conscripts_training", "class_1913", "drills"],
        "title": "Incorporate the Class of 1913",
        "desc": "Barracks across France absorb the new recruits, subjecting them to intense bayonet drills, forced marches, and field maneuvers before August 1914."
    })

    # 5.3 Franco-Russian Alliance
    foci.append({
        "id": "FRA_l_alliance_franco_russe",
        "wing": 5, "x": 121, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = SOV modifier = FRA_sacred_alliance_opinion }\nadd_political_power = 60",
        "icon_query": ["franco_russian_alliance", "czar_nicholas", "RUS_franco_russian_treaty"],
        "title": "The Franco-Russian Alliance",
        "desc": "Concluded in 1892, the Dual Alliance guarantees that an attack on either France or Russia triggers an immediate war in two fronts against the German Empire."
    })
    foci.append({
        "id": "FRA_emprunts_russes_chemin_de_fer",
        "wing": 5, "x": 118, "y": 1, "cost": 8,
        "prereq": ["FRA_l_alliance_franco_russe"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = -30\nSOV = { add_building_construction = { type = railway level = 2 instant_build = yes province = 9345 } }",
        "icon_query": ["GFX_FRA_investment_in_russia-45149", "russian_loans", "emprunts_russes"],
        "title": "French Loans for Russian Strategic Rails",
        "desc": "French bondholders pour billions of francs into the Tsarist railway network, ensuring Russian mobilization can strike East Prussia by the 15th day of war."
    })
    foci.append({
        "id": "FRA_pourparlers_d_etat_major_joffre_jilinsky",
        "wing": 5, "x": 124, "y": 1, "cost": 8,
        "prereq": ["FRA_l_alliance_franco_russe"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "planning_speed = 0.15\nadd_command_power = 25",
        "icon_query": ["staff_talks", "joffre_zhilinsky", "joint_staff"],
        "title": "Annual Staff Protocols: Joffre & Zhilinsky",
        "desc": "Joint staff conferences define the timetable of war: Russia pledges 800,000 men to invade Germany instantly, preventing Germany from crushing France alone."
    })
    foci.append({
        "id": "FRA_visite_de_poincare_a_saint_petersbourg",
        "wing": 5, "x": 121, "y": 2, "cost": 8,
        "prereq": ["FRA_emprunts_russes_chemin_de_fer", "FRA_pourparlers_d_etat_major_joffre_jilinsky"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.10\nadd_stability = 0.05",
        "icon_query": ["poincare_stpetersburg", "czar_banquet", "krasnoye_selo"],
        "title": "Poincaré's State Visit to St. Petersburg (1914)",
        "desc": "July 1914: Sailing aboard the battleship France, Poincaré and Viviani toast Czar Nicholas II at Peterhof, reaffirming absolute solidarity during the Sarajevo crisis."
    })
    foci.append({
        "id": "FRA_coordination_sur_les_deux_fronts",
        "wing": 5, "x": 121, "y": 3, "cost": 8,
        "prereq": ["FRA_visite_de_poincare_a_saint_petersbourg"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_morale_factor = 0.08\nadd_political_power = 50",
        "icon_query": ["two_front_war", "two_fronts", "russian_steamroller"],
        "title": "Simultaneous Two-Front Strategy",
        "desc": "When the storm broke, Grand Duke Nicholas launched the Russian invasion of East Prussia, forcing Moltke to divert two German army corps from the Marne."
    })
    foci.append({
        "id": "FRA_gestion_du_collapsus_russe_1917",
        "wing": 5, "x": 118, "y": 4, "cost": 8,
        "prereq": ["FRA_coordination_sur_les_deux_fronts"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.05\nadd_political_power = 60",
        "icon_query": ["russian_collapse", "petrograd_soviet", "albert_thomas_russia"],
        "title": "Weathering the Russian Revolution",
        "desc": "As the Tsarist regime fell in 1917, Minister Albert Thomas traveled to Petrograd to encourage Kerensky's Provisional Government to stay in the fight."
    })
    foci.append({
        "id": "FRA_intervention_a_odessa_mar_noir",
        "wing": 5, "x": 124, "y": 4, "cost": 8,
        "prereq": ["FRA_coordination_sur_les_deux_fronts"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2000 }\nadd_political_power = 40",
        "icon_query": ["odessa_expedition", "black_sea_fleet", "intervention_russia"],
        "title": "Black Sea Naval Expedition to Odessa",
        "desc": "French naval divisions sail to Odessa and Sevastopol to safeguard allied armaments and assist anti-Bolshevik White Russian forces."
    })

    # 5.4 Entente Cordiale with Britain
    foci.append({
        "id": "FRA_l_entente_cordiale",
        "wing": 5, "x": 131, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = ENG modifier = FRA_entente_cordiale_opinion }\nadd_political_power = 60",
        "icon_query": ["GFX_FRA_entente_cordiale-45115", "entente_cordiale", "anglo_french"],
        "title": "L'Entente Cordiale",
        "desc": "Signed in 1904, the Entente Cordiale resolved colonial rivalries in Egypt and Morocco, laying the foundations for joint defense against the German Empire."
    })
    foci.append({
        "id": "FRA_accords_navals_franco_britanniques",
        "wing": 5, "x": 128, "y": 1, "cost": 8,
        "prereq": ["FRA_l_entente_cordiale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "naval_coordination = 0.15\nadd_political_power = 50",
        "icon_query": ["naval_division_channel", "royal_navy_entente", "two_fleets"],
        "title": "Anglo-French Naval Distribution of 1912",
        "desc": "France concentrates her battle fleet in the Mediterranean, while the Royal Navy takes responsibility for the English Channel and the North Sea."
    })
    foci.append({
        "id": "FRA_plans_de_debarquement_du_bef",
        "wing": 5, "x": 134, "y": 1, "cost": 8,
        "prereq": ["FRA_l_entente_cordiale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "planning_speed = 0.20\nadd_command_power = 25",
        "icon_query": ["bef_landing", "british_expeditionary_force", "wilson_hughes"],
        "title": "General Wilson & BEF Disembarkation Plans",
        "desc": "General Henry Wilson secretly liaises with the French General Staff, drawing up exact train and port timetables for the British Expeditionary Force to land at Le Havre."
    })
    foci.append({
        "id": "FRA_garantie_de_la_neutralite_belge",
        "wing": 5, "x": 131, "y": 2, "cost": 8,
        "prereq": ["FRA_accords_navals_franco_britanniques", "FRA_plans_de_debarquement_du_bef"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "give_guarantee = BEL\nadd_war_support = 0.10",
        "icon_query": ["belgian_neutrality", "scrap_of_paper", "1839_treaty"],
        "title": "Guarantee Belgian Neutrality",
        "desc": "The 1839 Treaty of London guarantees Belgian neutrality. Any German violation is the absolute casus belli ensuring Britain enters the war alongside France."
    })
    foci.append({
        "id": "FRA_coordination_des_etats_majors_haig_joffre",
        "wing": 5, "x": 131, "y": 3, "cost": 8,
        "prereq": ["FRA_garantie_de_la_neutralite_belge"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_org_factor = 0.08\nadd_opinion_modifier = { target = ENG modifier = FRA_joint_offensive_opinion }",
        "icon_query": ["haig_joffre", "chantilly_conference", "joint_command"],
        "title": "Chantilly Allied Staff Conferences",
        "desc": "Meeting at General Joffre's headquarters in Chantilly, allied commanders synchronize simultaneous grand offensives across France, Italy, and Russia."
    })
    foci.append({
        "id": "FRA_conseil_supreme_de_guerre_versailles",
        "wing": 5, "x": 131, "y": 4, "cost": 8,
        "prereq": ["FRA_coordination_des_etats_majors_haig_joffre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_supreme_allied_command\nadd_political_power = 60",
        "icon_query": ["GFX_FRA_supreme_allied_command-46517", "supreme_war_council", "versailles_council"],
        "title": "Supreme War Council at Versailles",
        "desc": "Created in late 1917, the Supreme War Council coordinates political and strategic leadership between Britain, France, Italy, and the United States."
    })

    # 5.5 Mediterranean, Balkans & Italy
    foci.append({
        "id": "FRA_negocier_avec_l_italie_traite_de_londres",
        "wing": 5, "x": 121, "y": 8, "cost": 8,
        "prereq": ["FRA_coordination_sur_les_deux_fronts"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = ITA modifier = FRA_treaty_of_londres_opinion }\nadd_political_power = 50",
        "icon_query": ["treaty_of_london", "italy_alliance", "barracca"],
        "title": "The Secret Treaty of London (1915)",
        "desc": "Promising Trentino, South Tyrol, Trieste, and Istria from the Habsburg Empire, the Entente convinces Italy to break with the Triple Alliance and join our side."
    })
    foci.append({
        "id": "FRA_mission_militaire_en_roumanie_berthelot",
        "wing": 5, "x": 118, "y": 9, "cost": 8,
        "prereq": ["FRA_negocier_avec_l_italie_traite_de_londres"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "ROM = { add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 3000 } }\nadd_opinion_modifier = { target = ROM modifier = FRA_berthelot_mission_opinion }",
        "icon_query": ["berthelot", "henri_berthelot", "romania_mission"],
        "title": "General Berthelot's Romanian Mission",
        "desc": "General Henri Berthelot takes command of the French military mission to Romania, training, reorganizing, and rearming the Romanian Army for the struggle in Moldavia."
    })
    foci.append({
        "id": "FRA_front_d_orient_a_salonique",
        "wing": 5, "x": 124, "y": 9, "cost": 8,
        "prereq": ["FRA_negocier_avec_l_italie_traite_de_londres"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 30000\nadd_political_power = 40",
        "icon_query": ["salonika", "sarrail", "armee_d_orient"],
        "title": "The Salonika Front & Armée d'Orient",
        "desc": "Disembarking in Greece, General Maurice Sarrail establishes the fortified camp of Salonika ('The Birdcage'), pinning down Bulgarian and German armies in the Balkans."
    })
    foci.append({
        "id": "FRA_soutien_inconditionnel_a_la_serbie",
        "wing": 5, "x": 121, "y": 10, "cost": 8,
        "prereq": ["FRA_mission_militaire_en_roumanie_berthelot", "FRA_front_d_orient_a_salonique"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "SER = { add_manpower = 25000 }\nadd_stability = 0.05",
        "icon_query": ["serbia_rescue", "corfu_evacuation", "serbian_brotherhood"],
        "title": "Evacuation of the Serbian Army to Corfu",
        "desc": "After their heroic retreat through the Albanian mountains, French ships rescue 140,000 Serbian soldiers to Corfu, nursing them back to health and re-equipping them."
    })
    foci.append({
        "id": "FRA_offensive_du_vardar_franchet_d_esperey",
        "wing": 5, "x": 121, "y": 11, "cost": 8,
        "prereq": ["FRA_soutien_inconditionnel_a_la_serbie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_louis_franchet_d_esperey\nadd_command_power = 35",
        "icon_query": ["franchet_d_esperey", "vardar_offensive", "balkan_breakthrough"],
        "title": "Franchet d'Espèrey's Vardar Breakthrough",
        "desc": "September 1918: General Louis Franchet d'Espèrey launches a daring assault through the steep Dobro Pole mountains, breaking the Bulgarian line in days."
    })
    foci.append({
        "id": "FRA_capitulation_de_la_bulgarie",
        "wing": 5, "x": 121, "y": 12, "cost": 8,
        "prereq": ["FRA_offensive_du_vardar_franchet_d_esperey"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.15\nadd_stability = 0.10",
        "icon_query": ["bulgaria_capitulates", "armistice_salonika", "balkan_victory"],
        "title": "The Armistice of Salonika",
        "desc": "On September 29, 1918, Bulgaria signs the first armistice of the war, exposing Austria-Hungary's southern frontier and cracking the Central Powers alliance."
    })

    # 5.6 American Intervention & Victory Endgame
    foci.append({
        "id": "FRA_relations_financieres_avec_les_usa",
        "wing": 5, "x": 131, "y": 8, "cost": 8,
        "prereq": ["FRA_conseil_supreme_de_guerre_versailles"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_extra_state_shared_building_slots = 2",
        "icon_query": ["jp_morgan", "wall_street_loans", "dollar_credit"],
        "title": "Wall Street Loans & J.P. Morgan Credits",
        "desc": "Through the banking house of J.P. Morgan & Co., France secures over three billion dollars in commercial credits, purchasing American grain, steel, and cotton."
    })
    foci.append({
        "id": "FRA_exploiter_la_guerre_sous_marine_a_outrance",
        "wing": 5, "x": 128, "y": 9, "cost": 8,
        "prereq": ["FRA_relations_financieres_avec_les_usa"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "USA = { add_war_support = 0.15 }\nadd_political_power = 40",
        "icon_query": ["unrestricted_submarines", "lusitania", "wilson_neutrality"],
        "title": "Denounce Unrestricted Submarine Warfare",
        "desc": "Germany's fatal decision in February 1917 to sink all neutral shipping gives French diplomats the ultimate argument to persuade President Woodrow Wilson to declare war."
    })
    foci.append({
        "id": "FRA_arrivee_du_corps_expeditionnaire_americain",
        "wing": 5, "x": 134, "y": 9, "cost": 8,
        "prereq": ["FRA_relations_financieres_avec_les_usa"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.111 days = 1 }",
        "icon_query": ["pershing_arrives", "doughboys", "lafayette_nous_voila"],
        "title": "'La Fayette, Nous Voilà!'",
        "desc": "Standing at the tomb of the Marquis de Lafayette in Picpus Cemetery, Colonel Charles Stanton announces to the world: 'Lafayette, we are here!' The doughboys land in Saint-Nazaire."
    })
    foci.append({
        "id": "FRA_instruction_militaire_des_doughboys",
        "wing": 5, "x": 131, "y": 10, "cost": 8,
        "prereq": ["FRA_exploiter_la_guerre_sous_marine_a_outrance", "FRA_arrivee_du_corps_expeditionnaire_americain"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_experience = 30\nadd_opinion_modifier = { target = USA modifier = FRA_military_training_opinion }",
        "icon_query": ["doughboy_training", "american_camp", "french_instructors"],
        "title": "Train & Equip the American Doughboys",
        "desc": "French officers instruct American divisions in modern trench defense, providing them with 75mm cannons, Chauchat machine guns, and Renault FT tanks."
    })
    foci.append({
        "id": "FRA_la_demande_d_armistice_allemande",
        "wing": 5, "x": 131, "y": 11, "cost": 5,
        "prereq": ["FRA_instruction_militaire_des_doughboys"], "mut_ex": [],
        "allow_branch": None,
        "available": "GER = { surrender_progress > 0.40 }",
        "reward": "add_war_support = 0.15\nadd_stability = 0.10",
        "icon_query": ["german_white_flag", "armistice_request", "peace_envoy"],
        "title": "The German Armistice Request",
        "desc": "With their armies in full retreat, their allies crumbling, and the fleet mutinying at Kiel, the German High Command sends Matthias Erzberger to sue for peace."
    })
    foci.append({
        "id": "FRA_le_wagon_de_rethondes_a_compiegne",
        "wing": 5, "x": 131, "y": 12, "cost": 5,
        "prereq": ["FRA_la_demande_d_armistice_allemande"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.131 days = 1 }",
        "icon_query": ["wagon_rethondes", "compiegne", "foch_car"],
        "title": "The Railway Carriage at Compiègne",
        "desc": "In a dining carriage parked in the Forest of Compiègne, Marshal Foch reads out the unbending terms of surrender. On the eleventh hour of the eleventh day, the guns fall silent."
    })
    foci.append({
        "id": "FRA_retour_de_l_alsace_lorraine",
        "wing": 5, "x": 128, "y": 13, "cost": 8,
        "prereq": ["FRA_le_wagon_de_rethondes_a_compiegne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.132 days = 1 }",
        "icon_query": ["alsace_lorraine_returns", "strasbourg_liberated", "tricolor_strasbourg"],
        "title": "The Sacred Return of Alsace-Lorraine",
        "desc": "Forty-eight years of waiting are over! French soldiers enter Strasbourg, Metz, and Colmar amidst cheering crowds. 'The child is returned to the mother!'"
    })
    foci.append({
        "id": "FRA_la_paix_de_versailles_imposition",
        "wing": 5, "x": 134, "y": 13, "cost": 10,
        "prereq": ["FRA_le_wagon_de_rethondes_a_compiegne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 200\nadd_stability = 0.20",
        "icon_query": ["versailles_treaty", "hall_of_mirrors", "clemenceau_versailles"],
        "title": "The Treaty of Versailles (1919)",
        "desc": "In the Hall of Mirrors where the German Empire was proclaimed in 1871, Clemenceau presides over the signing of the peace, securing reparations and the demilitarization of the Rhineland."
    })

    # 5.7 Alt-Diplomacy (Rapprochement, Latin Bloc, Colonial Federation)
    foci.append({
        "id": "FRA_voie_du_rapprochement_franco_allemand",
        "wing": 5, "x": 111, "y": 9, "cost": 10,
        "prereq": ["FRA_integration_des_conscrits_de_1913"], "mut_ex": [],
        "allow_branch": "NOT = { has_country_flag = FRA_historical_diplomacy }",
        "available": "NOT = { has_war = yes }",
        "reward": "add_opinion_modifier = { target = GER modifier = FRA_rapprochement_talks_opinion }\nset_country_flag = FRA_alt_diplomacy",
        "icon_query": ["franco_german_rapprochement", "caillaux_talks", "european_peace"],
        "title": "Franco-German Rapprochement (Caillaux Vision)",
        "desc": "Advocated by Joseph Caillaux, this vision seeks to overcome the blood-feud of 1870 through economic partnership between French capital and German industrial dynamism."
    })
    foci.append({
        "id": "FRA_accord_sur_le_minerai_et_le_charbon",
        "wing": 5, "x": 108, "y": 10, "cost": 8,
        "prereq": ["FRA_voie_du_rapprochement_franco_allemand"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = GER modifier = FRA_coal_steel_pact_opinion }\nindustrial_capacity_factory = 0.08",
        "icon_query": ["coal_steel_pact", "briey_ruhr_accord", "industrial_pact"],
        "title": "Briey-Ruhr Coal & Iron Compact",
        "desc": "Forging an industrial syndicate linking the minette iron mines of Briey with the coking coal of the Ruhr, creating mutual economic interdependence."
    })
    foci.append({
        "id": "FRA_condominium_d_alsace_lorraine",
        "wing": 5, "x": 114, "y": 10, "cost": 8,
        "prereq": ["FRA_voie_du_rapprochement_franco_allemand"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.10\nadd_political_power = 60",
        "icon_query": ["condominium_alsace", "neutral_alsace", "strasbourg_bridge"],
        "title": "Condominium of Alsace-Lorraine",
        "desc": "Proposing that Alsace-Lorraine become a neutral autonomous federal territory with dual Franco-German cultural rights and free trade, eliminating the spark of war."
    })
    foci.append({
        "id": "FRA_pacte_de_non_agression_continental",
        "wing": 5, "x": 111, "y": 11, "cost": 10,
        "prereq": ["FRA_accord_sur_le_minerai_et_le_charbon", "FRA_condominium_d_alsace_lorraine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "give_guarantee = GER\nadd_stability = 0.15",
        "icon_query": ["continental_peace", "european_handshake", "non_aggression"],
        "title": "Continental Non-Aggression Pact",
        "desc": "France and Germany sign a mutual pledge of non-aggression, dismantling the explosive alliance tripwires that threatened to drag Europe into self-destruction."
    })
    foci.append({
        "id": "FRA_le_bloc_latin_mediterraneen",
        "wing": 5, "x": 108, "y": 12, "cost": 10,
        "prereq": ["FRA_pacte_de_non_agression_continental"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "create_faction = FRA_latin_entente\nadd_political_power = 80",
        "icon_query": ["FRA_latin_union", "latin_bloc", "mediterranean_alliance"],
        "title": "The Latin Mediterranean Entente",
        "desc": "Turning away from eastern entanglements, France unites the Romanic world—France, Italy, Spain, and Portugal—into a powerful Mediterranean customs and defense union."
    })
    foci.append({
        "id": "FRA_alliance_avec_l_italie_et_l_espagne",
        "wing": 5, "x": 108, "y": 13, "cost": 8,
        "prereq": ["FRA_le_bloc_latin_mediterraneen"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_to_faction = ITA\nadd_to_faction = SPR",
        "icon_query": ["latin_union_treaty", "rome_madrid_paris", "trio_latin"],
        "title": "Treaty of the Latin Sisters",
        "desc": "Formalizing military and naval conventions across the Western Mediterranean, securing our southern flank and coordinating North African development."
    })
    foci.append({
        "id": "FRA_federation_coloniale_associee",
        "wing": 5, "x": 114, "y": 12, "cost": 10,
        "prereq": ["FRA_pacte_de_non_agression_continental"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.15\nconsumer_goods_factor = -0.02",
        "icon_query": ["colonial_federation", "federal_empire", "reformed_colonies"],
        "title": "Associated Colonial Federation",
        "desc": "Replacing colonial subjugation with an autonomous federal commonwealth, granting representation and internal home-rule to Indochina, Madagascar, and Africa."
    })
    foci.append({
        "id": "FRA_citoyennete_francaise_elargie",
        "wing": 5, "x": 114, "y": 13, "cost": 8,
        "prereq": ["FRA_federation_coloniale_associee"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "conscription_factor = 0.10\nadd_stability = 0.05",
        "icon_query": ["universal_citizenship", "equality_empire", "liberte_egalite_fraternite"],
        "title": "Universal Imperial Citizenship",
        "desc": "Extending full civic equality to all subjects of the overseas departments, cementing loyalty to the tricolor through liberty, equality, and fraternity."
    })

    return foci

if __name__ == "__main__":
    w5 = get_wing_5_foci()
    print("Wing 5 count:", len(w5))
