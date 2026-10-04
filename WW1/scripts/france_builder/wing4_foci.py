# Wing 4: Armée de Terre, Artillery & Frontline Operations (52 foci)
# Coordinated geometry x: 75 to 105, strictly dy >= 1

def get_wing_4_foci():
    foci = []

    # 4.1 GQG & Initial Doctrine (1911-1914)
    foci.append({
        "id": "FRA_grand_quartier_general",
        "wing": 4, "x": 80, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_experience = 25\nadd_command_power = 30",
        "icon_query": ["gqg", "french_army", "general_staff", "focus_French_Air_Force"],
        "title": "Grand Quartier Général (GQG)",
        "desc": "The brain of the French Army, GQG brings together the brightest minds of the École Supérieure de Guerre, obsessively analyzing the coming confrontation with Germany."
    })
    foci.append({
        "id": "FRA_general_joffre_chef_d_etat_major",
        "wing": 4, "x": 77, "y": 1, "cost": 8,
        "prereq": ["FRA_grand_quartier_general"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_joseph_joffre\nadd_stability = 0.05",
        "icon_query": ["joffre", "joseph_joffre", "GFX_FRA_joseph_joffre"],
        "title": "General Joffre's Supreme Command",
        "desc": "Appointed Chief of the General Staff in 1911, the calm, unflappable engineering officer Joseph Joffre centralizes all military preparations with iron determination."
    })
    foci.append({
        "id": "FRA_culte_de_l_offensive_a_outrance",
        "wing": 4, "x": 83, "y": 1, "cost": 8,
        "prereq": ["FRA_grand_quartier_general"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_infantry_attack_factor = 0.08\narmy_morale_factor = 0.10",
        "icon_query": ["GFX_FRA_attaque__outrance-69190", "offensive_a_outrance", "bayonet_charge"],
        "title": "The Cult of 'L'Offensive à Outrance'",
        "desc": "Preached by Colonel de Grandmaison, the French military dogma dictates that victory belongs to whichever side attacks with supreme moral ferocity and the cold bayonet."
    })
    foci.append({
        "id": "FRA_uniformes_pantalon_rouge_tradition",
        "wing": 4, "x": 77, "y": 2, "cost": 8,
        "prereq": ["FRA_general_joffre_chef_d_etat_major"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.05\nadd_political_power = 40",
        "icon_query": ["pantalon_rouge", "french_uniform", "kepi"],
        "title": "Traditional Red Trousers ('Le Pantalon Rouge')",
        "desc": "Minister of War Eugène Étienne proclaimed: 'Abolish the red trousers? Never! The red trousers are France!' The brilliant garance trousers remain sacred tradition."
    })
    foci.append({
        "id": "FRA_adoption_du_plan_xvii",
        "wing": 4, "x": 83, "y": 2, "cost": 8,
        "prereq": ["FRA_culte_de_l_offensive_a_outrance"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "set_country_flag = FRA_plan_xvii_adopted\nadd_ideas = FRA_elan_vital_doctrine",
        "icon_query": ["plan_xvii", "GFX_FRA_plan_xvii-122742", "strategic_map_france"],
        "title": "Adoption of Plan XVII",
        "desc": "Replacing defensive doctrines, Joffre's Plan XVII focuses five French armies on an all-out offensive into the lost provinces of Alsace and Lorraine upon war's outbreak."
    })
    foci.append({
        "id": "FRA_concentration_des_cinq_armees",
        "wing": 4, "x": 80, "y": 3, "cost": 8,
        "prereq": ["FRA_uniformes_pantalon_rouge_tradition", "FRA_adoption_du_plan_xvii"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "planning_speed = 0.20\nmax_planning = 0.15",
        "icon_query": ["five_armies", "mobilization_deployment", "concentration_plan"],
        "title": "Concentration of the Five Armies",
        "desc": "Deploying the 1st Army (Dubail), 2nd Army (Castelnau), 3rd Army (Ruffey), 4th Army (de Langle de Cary), and 5th Army (Lanrezac) along the eastern frontier."
    })
    foci.append({
        "id": "FRA_regiments_de_chasseurs_alpins",
        "wing": 4, "x": 77, "y": 4, "cost": 8,
        "prereq": ["FRA_concentration_des_cinq_armees"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = mountain_bonus bonus = 1.0 uses = 1 category = mountaineers }\nadd_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2000 }",
        "icon_query": ["GFX_FRA_chasseurs_alpins-46859", "chasseurs_alpins", "blue_devils"],
        "title": "Chasseurs Alpins ('Les Diables Bleus')",
        "desc": "The elite mountain regiments wearing wide berets and dark blue tunics master the rocky heights of the Vosges and the Alpine passes with peerless grit."
    })
    foci.append({
        "id": "FRA_reseau_de_forts_sere_de_rivieres",
        "wing": 4, "x": 83, "y": 4, "cost": 8,
        "prereq": ["FRA_concentration_des_cinq_armees"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "18 = { add_building_construction = { type = bunker level = 2 instant_build = yes province = 6542 } }\n28 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = 9647 } }",
        "icon_query": ["sere_de_rivieres", "fortress", "verdun_fort", "fortification"],
        "title": "The Séré de Rivières Barrier Forts",
        "desc": "Concrete armored forts at Verdun, Toul, Épinal, and Belfort create an impregnable steel barrier along the Franco-German border, canalizing any enemy assault."
    })

    # 4.2 1914 Outbreak, Frontiers & Marne
    foci.append({
        "id": "FRA_bataille_des_frontieres",
        "wing": 4, "x": 80, "y": 5, "cost": 5,
        "prereq": ["FRA_regiments_de_chasseurs_alpins", "FRA_reseau_de_forts_sere_de_rivieres"], "mut_ex": [],
        "allow_branch": None,
        "available": "has_war = yes",
        "reward": "country_event = { id = ww1_france.50 days = 1 }",
        "icon_query": ["battle_frontiers", "clash_frontiers", "morhange"],
        "title": "Battle of the Frontiers (August 1914)",
        "desc": "The five French armies advance across the border into Morhange, Sarrebourg, and the Ardennes forest, colliding head-on with German fortified machine guns and heavy howitzers."
    })
    foci.append({
        "id": "FRA_echec_de_l_offensive_initiale",
        "wing": 4, "x": 80, "y": 6, "cost": 4,
        "prereq": ["FRA_bataille_des_frontieres"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_elan_vital_doctrine add_idea = FRA_lessons_of_the_frontiers }\nadd_stability = -0.05",
        "icon_query": ["retreat_frontiers", "soldier_dead", "tragic_lessons"],
        "title": "The Brutal Shock of Modern War",
        "desc": "Losing 27,000 dead on August 22 alone, the bloodiest day in French history exposes the catastrophe of charging concealed machine guns across open fields."
    })
    foci.append({
        "id": "FRA_grande_retraite_organisee",
        "wing": 4, "x": 77, "y": 7, "cost": 4,
        "prereq": ["FRA_echec_de_l_offensive_initiale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_speed_factor = 0.10\narmy_defence_factor = 0.05",
        "icon_query": ["great_retreat", "retraite", "marching_dust"],
        "title": "The Great Organized Retreat",
        "desc": "Under scorching August heat, Joffre maintains iron composure, executing a Fighting Retreat for 200 kilometers without allowing his armies to be encircled or crushed."
    })
    foci.append({
        "id": "FRA_gouvernement_militaire_de_paris_gallieni",
        "wing": 4, "x": 83, "y": 7, "cost": 5,
        "prereq": ["FRA_echec_de_l_offensive_initiale"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_joseph_gallieni\nadd_command_power = 25",
        "icon_query": ["gallieni", "joseph_gallieni", "GFX_FRA_joseph_gallieni"],
        "title": "General Gallieni Defends Paris",
        "desc": "'I have been given the mandate to defend Paris against the invader. This mandate I shall fulfill to the end.' Gallieni turns Paris into an active army bastion."
    })
    foci.append({
        "id": "FRA_operation_de_la_marne",
        "wing": 4, "x": 80, "y": 8, "cost": 5,
        "prereq": ["FRA_grande_retraite_organisee", "FRA_gouvernement_militaire_de_paris_gallieni"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.61 days = 1 }\nadd_war_support = 0.15",
        "icon_query": ["battle_of_the_marne", "miracle_of_the_marne", "taxi_marne"],
        "title": "The Miracle of the Marne",
        "desc": "Spotting von Kluck's exposed right flank, Joffre issues the order: 'A troop that can advance no further must die where it stands rather than yield ground.' The German advance is broken!"
    })
    foci.append({
        "id": "FRA_la_course_a_la_mer",
        "wing": 4, "x": 80, "y": 9, "cost": 5,
        "prereq": ["FRA_operation_de_la_marne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "max_entrenchment = 5\narmy_org_factor = 0.05",
        "icon_query": ["race_to_the_sea", "flanders_front", "ysir_inundation"],
        "title": "The Race to the Sea",
        "desc": "Both sides frantically attempt to outflank each other northward through Picardy and Artois, until the front freezes into continuous trenches from the Swiss border to the North Sea."
    })

    # 4.3 Trench Warfare & Firepower (1915-1916)
    foci.append({
        "id": "FRA_stabilisation_du_front_occidental",
        "wing": 4, "x": 95, "y": 10, "cost": 8,
        "prereq": ["FRA_la_course_a_la_mer"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "max_entrenchment = 5\nentrenchment_speed_factor = 0.20",
        "icon_query": ["trench_stabilization", "trench_line", "barbed_wire"],
        "title": "Western Front Trench Stalemate",
        "desc": "The war of movement has ended. In deep mud and chalk dugouts, two million French poilus dig in behind barbed wire, awaiting the artillery storms."
    })
    foci.append({
        "id": "FRA_canon_de_75mm_modele_1897",
        "wing": 4, "x": 91, "y": 11, "cost": 8,
        "prereq": ["FRA_stabilisation_du_front_occidental"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_artillery_attack_factor = 0.10\nadd_equipment_to_stockpile = { type = artillery_equipment_1 amount = 150 }",
        "icon_query": ["canon_75mm", "75mm_field_gun", "quick_firing_gun"],
        "title": "The Glorious Canon de 75mm Mle 1897",
        "desc": "The greatest rapid-fire field gun in history. Its hydro-pneumatic recoil allows firing 15 aimed shrapnel rounds per minute without releveling the trail."
    })
    foci.append({
        "id": "FRA_adopter_le_casque_adrian_m1915",
        "wing": 4, "x": 99, "y": 11, "cost": 8,
        "prereq": ["FRA_stabilisation_du_front_occidental"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_horizon_blue_uniforms_idea\narmy_defence_factor = 0.05",
        "icon_query": ["GFX_FRA_horizon_blue_uniforms-69197", "adrian_helmet", "casque_adrian"],
        "title": "The Adrian Helmet & Bleu Horizon",
        "desc": "Intendant-Général Louis Adrian designs the first mass-produced steel combat helmet, stamped with the republican flaming grenade, saving countless lives from shrapnel."
    })
    foci.append({
        "id": "FRA_parc_d_artillerie_lourde_rimailho",
        "wing": 4, "x": 91, "y": 12, "cost": 8,
        "prereq": ["FRA_canon_de_75mm_modele_1897"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = heavy_art_bonus bonus = 1.0 uses = 1 category = artillery }",
        "icon_query": ["heavy_howitzer", "schneider_155mm", "rimailho"],
        "title": "Heavy Howitzers: Schneider 155mm",
        "desc": "Realizing the 75mm cannot penetrate reinforced concrete bunkers, France orders hundreds of heavy 155mm C17S howitzers from Schneider to pulverize German pillboxes."
    })
    foci.append({
        "id": "FRA_mortiers_de_tranchee_crapouillots",
        "wing": 4, "x": 99, "y": 12, "cost": 8,
        "prereq": ["FRA_adopter_le_casque_adrian_m1915"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_infantry_attack_factor = 0.05\nmax_entrenchment = 3",
        "icon_query": ["crapouillots", "trench_mortar", "bomb_thrower"],
        "title": "Trench Mortars ('Les Crapouillots')",
        "desc": "Short-range curved-trajectory trench mortars lob heavy explosive canisters into enemy frontline parapets, clearing the opposing trench before infantry raids."
    })
    foci.append({
        "id": "FRA_fusil_mitrailleur_chauchat",
        "wing": 4, "x": 95, "y": 13, "cost": 8,
        "prereq": ["FRA_parc_d_artillerie_lourde_rimailho", "FRA_mortiers_de_tranchee_crapouillots"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = infantry_weapons_bonus bonus = 1.0 uses = 1 category = infantry_weapons }\nadd_equipment_to_stockpile = { type = infantry_equipment_1 amount = 3000 }",
        "icon_query": ["chauchat", "csr_chauchat", "automatic_rifle"],
        "title": "Chauchat CSRG Light Machine Gun",
        "desc": "The first mass-produced portable automatic squad weapon. Despite its open crescent magazine, it provides infantry platoons with organic mobile firepower on the assault."
    })
    foci.append({
        "id": "FRA_canons_sur_voie_ferree_alvf",
        "wing": 4, "x": 91, "y": 14, "cost": 8,
        "prereq": ["FRA_fusil_mitrailleur_chauchat"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_artillery_attack_factor = 0.08\nrailway_gun_bombardment_factor = 0.20",
        "icon_query": ["alvf", "railway_gun", "super_heavy_artillery"],
        "title": "Railway Super-Heavy Siege Artillery (ALVF)",
        "desc": "Mounting 320mm, 370mm, and 400mm naval and coastal barrels onto specialized rail bogies, Artillerie Lourde sur Voie Ferrée demolishes deep underground caverns."
    })
    foci.append({
        "id": "FRA_guerre_des_mines_vauquois",
        "wing": 4, "x": 99, "y": 14, "cost": 8,
        "prereq": ["FRA_fusil_mitrailleur_chauchat"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_breakthrough_factor = 0.05\nadd_manpower = 15000",
        "icon_query": ["mine_warfare", "vauquois", "tunneling_explosive"],
        "title": "Underground Mine Warfare at Vauquois",
        "desc": "Sappeur miners tunnel hundreds of meters beneath the chalk hills to detonate 60-ton ammonal charges under enemy strongpoints, ripping the terrain into lunar craters."
    })
    foci.append({
        "id": "FRA_offensives_de_champagne_et_artois",
        "wing": 4, "x": 95, "y": 15, "cost": 8,
        "prereq": ["FRA_canons_sur_voie_ferree_alvf", "FRA_guerre_des_mines_vauquois"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_experience = 30\nadd_ideas = FRA_firepower_doctrine",
        "icon_query": ["champagne_offensive", "artois_battle", "rolling_barrage"],
        "title": "The Attritional Bloodbaths of 1915",
        "desc": "Testing the creeping barrage doctrine in Champagne, Artois, and Neuve-Chapelle, the French Army proves that raw courage without heavy shell saturation achieves only martyrdom."
    })

    # 4.4 Verdun, Somme & Nivelle Crisis
    foci.append({
        "id": "FRA_la_fournaise_de_verdun",
        "wing": 4, "x": 95, "y": 16, "cost": 8,
        "prereq": ["FRA_offensives_de_champagne_et_artois"], "mut_ex": [],
        "allow_branch": None,
        "available": "date > 1916.1.1",
        "reward": "country_event = { id = ww1_france.71 days = 1 }",
        "icon_query": ["verdun_furnace", "douaumont", "battle_verdun"],
        "title": "The Furnace of Verdun (1916)",
        "desc": "On February 21, 1916, Erich von Falkenhayn unleashes 1,400 German guns onto the Meuse fortresses to bleed the French Army white. Verdun becomes the altar of France."
    })
    foci.append({
        "id": "FRA_organisation_de_la_voie_sacree",
        "wing": 4, "x": 91, "y": 17, "cost": 8,
        "prereq": ["FRA_la_fournaise_de_verdun"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_la_voie_sacree_convoy\nsupply_consumption_factor = -0.15",
        "icon_query": ["voie_sacree", "berliet_trucks", "convoy_verdun"],
        "title": "La Voie Sacrée Logistical Lifeline",
        "desc": "Connecting Bar-le-Duc to Verdun, Maurice Barrès dubbed it 'The Sacred Way'. One truck passed every 14 seconds day and night, transporting 50,000 tons of munitions weekly."
    })
    foci.append({
        "id": "FRA_rotation_de_la_noria_petain",
        "wing": 4, "x": 95, "y": 17, "cost": 8,
        "prereq": ["FRA_la_fournaise_de_verdun"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "land_reinforce_rate = 0.20\narmy_org_factor = 0.05",
        "icon_query": ["noria", "division_rotation", "petain_verdun"],
        "title": "Pétain's 'Noria' Division Rotation",
        "desc": "General Philippe Pétain rotates battered divisions out of the cauldron after ten days, ensuring that almost the entire French Army shares the glory and burden of Verdun."
    })
    foci.append({
        "id": "FRA_ils_ne_passeront_pas",
        "wing": 4, "x": 99, "y": 17, "cost": 8,
        "prereq": ["FRA_la_fournaise_de_verdun"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_they_shall_not_pass\nadd_war_support = 0.15",
        "icon_query": ["GFX_FRA_they_shall_not_pass", "ils_ne_passeront_pas", "vaux_fort"],
        "title": "'Ils Ne Passeront Pas!'",
        "desc": "Proclaimed by Nivelle and Pétain, the rallying cry echoes across Fort Vaux, Fleury, and Dead Man's Hill. France stood unbreakable; the German offensive was broken."
    })
    foci.append({
        "id": "FRA_la_bataille_de_la_somme_soutien",
        "wing": 4, "x": 95, "y": 18, "cost": 8,
        "prereq": ["FRA_organisation_de_la_voie_sacree", "FRA_rotation_de_la_noria_petain", "FRA_ils_ne_passeront_pas"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_artillery_attack_factor = 0.08\nadd_opinion_modifier = { target = ENG modifier = FRA_somme_allied_opinion }",
        "icon_query": ["battle_of_the_somme", "somme_artillery", "fayolle_offensive"],
        "title": "The Somme Joint Offensive",
        "desc": "General Fayolle's Sixth Army attacks south of the Somme River in July 1916, utilizing devastating heavy artillery barrages to relieve German pressure on Verdun."
    })
    foci.append({
        "id": "FRA_la_doctrine_nivelle_rupture",
        "wing": 4, "x": 91, "y": 19, "cost": 8,
        "prereq": ["FRA_la_bataille_de_la_somme_soutien"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_robert_nivelle\nbreakthrough_factor = 0.10",
        "icon_query": ["GFX_FRA_nivelle_offensive-91858", "nivelle", "robert_nivelle"],
        "title": "Nivelle's Grand Rupture Doctrine",
        "desc": "Flushed with success recapturing Fort Douaumont, General Robert Nivelle promises parliament to rupture the German front lines within 48 hours with a rolling barrage."
    })
    foci.append({
        "id": "FRA_catastrophe_du_chemin_des_dames",
        "wing": 4, "x": 95, "y": 20, "cost": 5,
        "prereq": ["FRA_la_doctrine_nivelle_rupture"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "country_event = { id = ww1_france.81 days = 1 }",
        "icon_query": ["chemin_des_dames", "craonne", "nivelle_disaster"],
        "title": "Catastrophe on the Chemin des Dames",
        "desc": "April 16, 1917: Assaulting the impregnable limestone ridge in sleet and freezing rain, 100,000 French soldiers fall in days against German machine-gun caverns."
    })
    foci.append({
        "id": "FRA_les_mutineries_des_poilus",
        "wing": 4, "x": 95, "y": 21, "cost": 5,
        "prereq": ["FRA_catastrophe_du_chemin_des_dames"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_trench_mutiny_crisis_3\nadd_stability = -0.15",
        "icon_query": ["poilus_mutiny", "chanson_de_craonne", "trench_rebellion"],
        "title": "The Poilus Mutinies of 1917",
        "desc": "Singing the Chanson de Craonne, sixty-eight divisions mutiny. The soldiers refuse to participate in suicidal butcheries, though promising to defend their trenches."
    })

    # 4.5 Pétain Reforms, Armor & Foch 1918
    foci.append({
        "id": "FRA_petain_commandant_en_chef",
        "wing": 4, "x": 95, "y": 22, "cost": 8,
        "prereq": ["FRA_les_mutineries_des_poilus"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_philippe_petain\nadd_command_power = 30",
        "icon_query": ["philippe_petain", "petain_commander", "GFX_FRA_philippe_petain"],
        "title": "Pétain Appointed Commander-in-Chief",
        "desc": "Replacing the discredited Nivelle, Pétain restores faith with common-sense realism: 'I am waiting for the tanks and the Americans.' Suicidal offensives cease."
    })
    foci.append({
        "id": "FRA_reforme_des_permissions_et_soupe",
        "wing": 4, "x": 91, "y": 23, "cost": 8,
        "prereq": ["FRA_petain_commandant_en_chef"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\narmy_org_factor = 0.05",
        "icon_query": ["permission", "leave_train", "pinard_wine", "poilu_meal"],
        "title": "Leave Rotations & The Poilu's Soup",
        "desc": "Pétain inspects hundreds of cantonments personally, ensuring fresh meat, hot soup, wine rations (le pinard), clean beds, and guaranteed home leaves for front soldiers."
    })
    foci.append({
        "id": "FRA_repression_mesuree_des_meneurs",
        "wing": 4, "x": 99, "y": 23, "cost": 8,
        "prereq": ["FRA_petain_commandant_en_chef"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "swap_ideas = { remove_idea = FRA_trench_mutiny_crisis_3 add_idea = FRA_petain_elastic_defense }\nadd_stability = 0.05",
        "icon_query": ["military_justice", "pardons", "measured_discipline"],
        "title": "Measured Discipline & Pardons",
        "desc": "Refusing mass executions, Pétain commutes hundreds of death sentences to hard labor, executing only 49 undeniable mutiny leaders while healing the army's spirit."
    })
    foci.append({
        "id": "FRA_developpement_des_chars_d_assaut",
        "wing": 4, "x": 95, "y": 24, "cost": 8,
        "prereq": ["FRA_reforme_des_permissions_et_soupe", "FRA_repression_mesuree_des_meneurs"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = armor_bonus bonus = 1.0 uses = 1 category = armor }",
        "icon_query": ["general_estienne", "tank_development", "artillerie_speciale"],
        "title": "General Estienne & L'Artillerie Spéciale",
        "desc": "General Jean-Baptiste Estienne envisioned armored caterpillar landships: 'Victory belongs to him who first mounts a 75mm cannon on a carriage able to cross trenches.'"
    })
    foci.append({
        "id": "FRA_chars_schneider_ca1_et_saint_chamond",
        "wing": 4, "x": 91, "y": 25, "cost": 8,
        "prereq": ["FRA_developpement_des_chars_d_assaut"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_equipment_to_stockpile = { type = medium_tank_chassis_1 amount = 40 }",
        "icon_query": ["schneider_ca1", "saint_chamond", "FRA_Saint_Chammond_Tank"],
        "title": "Schneider CA1 & Saint-Chamond Assault Tanks",
        "desc": "France's early medium tanks mounted with 75mm guns test combat armor at Berry-au-Bac in 1917, proving armor's ability to crush enemy machine-gun nests."
    })
    foci.append({
        "id": "FRA_char_leger_renault_ft",
        "wing": 4, "x": 95, "y": 25, "cost": 8,
        "prereq": ["FRA_developpement_des_chars_d_assaut"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_renault_ft_revolution\nadd_equipment_to_stockpile = { type = light_tank_chassis_1 amount = 80 }",
        "icon_query": ["GFX_FRA_renault_ft-45157", "renault_ft", "ft17_tank"],
        "title": "The Revolutionary Renault FT Light Tank",
        "desc": "Louis Renault created the ancestor of all modern tanks: a fully rotating 360° turret, engine in the rear, driver in front. Over 3,000 are produced to spearhead victory."
    })
    foci.append({
        "id": "FRA_doctrine_d_emploi_des_blindes_estienne",
        "wing": 4, "x": 99, "y": 25, "cost": 8,
        "prereq": ["FRA_developpement_des_chars_d_assaut"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_armor_attack_factor = 0.15\narmy_armor_defence_factor = 0.10",
        "icon_query": ["tank_doctrine", "swarm_tanks", "combined_arms"],
        "title": "Estienne's Swarm Armored Doctrine",
        "desc": "Rather than dispersed single infantry pillboxes, Renault FTs attack in mass swarms, coordinating with air cover and artillery to slice through deep defensive zones."
    })
    foci.append({
        "id": "FRA_ferdinand_foch_commandement_unique",
        "wing": 4, "x": 91, "y": 26, "cost": 8,
        "prereq": ["FRA_char_leger_renault_ft"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "promote_character = FRA_ferdinand_foch\nadd_command_power = 40",
        "icon_query": ["ferdinand_foch", "generalissimo", "foch_supreme_commander"],
        "title": "Ferdinand Foch Supreme Allied Commander",
        "desc": "At Doullens in March 1918, facing the great German offensive, Britain and France appoint Ferdinand Foch as Generalissimo of all allied forces in France."
    })
    foci.append({
        "id": "FRA_arret_des_offensives_ludendorff",
        "wing": 4, "x": 99, "y": 26, "cost": 8,
        "prereq": ["FRA_char_leger_renault_ft"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_defence_factor = 0.15\nadd_war_support = 0.10",
        "icon_query": ["halt_ludendorff", "second_marne", "kaiser_offensive_stopped"],
        "title": "Halt the 1918 Ludendorff Offensives",
        "desc": "Using Pétain's elastic defense at the Second Battle of the Marne, French divisions absorb the German stormtrooper spearheads in empty outpost zones and crush them."
    })
    foci.append({
        "id": "FRA_offensive_des_cent_jours",
        "wing": 4, "x": 95, "y": 27, "cost": 10,
        "prereq": ["FRA_ferdinand_foch_commandement_unique", "FRA_arret_des_offensives_ludendorff"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_supreme_combined_arms\nbreakthrough_factor = 0.15",
        "icon_query": ["hundred_days", "allied_counteroffensive", "villers_cotterets"],
        "title": "The Hundred Days Allied Counter-Offensive",
        "desc": "On July 18, 1918, Foch strikes back at Villers-Cotterêts with hundreds of Renault FT tanks without preliminary artillery warning, routing the German Seventh Army."
    })
    foci.append({
        "id": "FRA_rupture_de_la_ligne_hindenburg",
        "wing": 4, "x": 95, "y": 28, "cost": 10,
        "prereq": ["FRA_offensive_des_cent_jours"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_attack_factor = 0.15\nadd_stability = 0.15",
        "icon_query": ["break_german_lines", "hindenburg_line_broken", "triumph_poilus"],
        "title": "Break the Hindenburg Line",
        "desc": "Storming the deepest trench fortresses of the Siegfriedstellung, French, British, and American divisions smash through the German defenses, forcing Germany to capitulate."
    })

    return foci

if __name__ == "__main__":
    w4 = get_wing_4_foci()
    print("Wing 4 count:", len(w4))
