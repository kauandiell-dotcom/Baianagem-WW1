# Generates data_foci.py with all 245 French focuses across 5 wings
import os, sys

def get_wing_3_foci():
    foci = []
    # 3.1 Marine Nationale
    foci.append({
        "id": "FRA_ministere_de_la_marine",
        "wing": 3, "x": 54, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_political_power = 60\nadd_doctrine_cost_factor = { category = naval_doctrine cost_factor = -0.10 }",
        "icon_query": ["marine_nationale", "anchor", "navy", "admiral"],
        "title": "Ministère de la Marine",
        "desc": "Operating from the Rue Royale in Paris, the Ministry of the Navy oversees our battlefleets in the Atlantic and Mediterranean, balancing colonial defense with European sea control."
    })
    foci.append({
        "id": "FRA_statut_naval_boue_de_lapeyrere",
        "wing": 3, "x": 54, "y": 1, "cost": 8,
        "prereq": ["FRA_ministere_de_la_marine"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = capital_ships_bonus bonus = 1.0 uses = 2 category = naval_equipment }",
        "icon_query": ["boue_de_lapeyrere", "naval_reform", "admiralty"],
        "title": "Lapeyrère's Naval Organic Statute",
        "desc": "Admiral Boué de Lapeyrère's ambitious 1912 program ended the confusion of the Jeune École, committing France to a modern battle fleet of 28 modern dreadnoughts."
    })
    foci.append({
        "id": "FRA_dreadnoughts_classe_courbet",
        "wing": 3, "x": 51, "y": 2, "cost": 8,
        "prereq": ["FRA_statut_naval_boue_de_lapeyrere"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_experience = 25\nadd_building_construction = { type = dockyard level = 1 instant_build = yes province = 9811 }",
        "icon_query": ["dreadnought", "courbet", "battleship", "focus_dreadnought_FRA"],
        "title": "Courbet-Class Dreadnoughts",
        "desc": "France's first true dreadnoughts—Courbet, Jean Bart, Paris, and France—mount twelve 305mm guns, giving our line of battle decisive striking power."
    })
    foci.append({
        "id": "FRA_flotte_de_la_mediterranee_toulon",
        "wing": 3, "x": 57, "y": 2, "cost": 8,
        "prereq": ["FRA_statut_naval_boue_de_lapeyrere"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "21 = { add_building_construction = { type = naval_base level = 2 instant_build = yes province = 9811 } }",
        "icon_query": ["toulon", "mediterranean_fleet", "naval_base"],
        "title": "Toulon Mediterranean Battle Fleet",
        "desc": "The Arsenal of Toulon concentrates our premier naval power, safeguarding the sea lanes between Marseille and Algiers against Austrian and Ottoman ambitions."
    })
    foci.append({
        "id": "FRA_superdreadnoughts_classe_bretagne",
        "wing": 3, "x": 51, "y": 3, "cost": 8,
        "prereq": ["FRA_dreadnoughts_classe_courbet"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_experience = 20\nadd_tech_bonus = { name = heavy_armor_naval bonus = 1.0 uses = 1 category = naval_equipment }",
        "icon_query": ["superdreadnought", "bretagne", "big_guns_battleship"],
        "title": "Bretagne-Class Super-Dreadnoughts",
        "desc": "Upgrading to ten 340mm guns mounted along the centerline, the Bretagne, Provence, and Lorraine represent the pinnacle of French wartime naval architecture."
    })
    foci.append({
        "id": "FRA_escadre_de_l_atlantique_brest",
        "wing": 3, "x": 57, "y": 3, "cost": 8,
        "prereq": ["FRA_flotte_de_la_mediterranee_toulon"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "19 = { add_building_construction = { type = dockyard level = 1 instant_build = yes province = 11467 } }",
        "icon_query": ["brest", "atlantic_fleet", "dockyard_brest"],
        "title": "Brest Atlantic Squadron",
        "desc": "Guarding the approaches to the English Channel and the Bay of Biscay, the squadron at Brest patrols transatlantic commerce and escorts incoming troop transports."
    })
    foci.append({
        "id": "FRA_projet_cuirasses_classe_lyon",
        "wing": 3, "x": 51, "y": 4, "cost": 8,
        "prereq": ["FRA_superdreadnoughts_classe_bretagne"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = advanced_heavy_hull bonus = 1.5 uses = 1 category = naval_equipment }",
        "icon_query": ["lyon_class", "quadruple_turret", "future_battleship"],
        "title": "Lyon-Class Quadruple Turret Project",
        "desc": "Conceived with sixteen 340mm guns in four revolutionary quadruple turrets, the Lyon project points the way toward future naval mastery."
    })
    foci.append({
        "id": "FRA_patrouilles_anti_sous_marines",
        "wing": 3, "x": 57, "y": 4, "cost": 8,
        "prereq": ["FRA_escadre_de_l_atlantique_brest"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_screen_defence_factor = 0.10\nsub_detection = 0.15",
        "icon_query": ["asw_patrol", "submarine_hunter", "depth_charges"],
        "title": "Anti-Submarine Patrols & Escorts",
        "desc": "Arming trawlers, torpedo boats, and fast yachts with depth charges and searchlights counters the growing menace of unrestricted German submarine warfare."
    })
    foci.append({
        "id": "FRA_sous_marins_classe_pluviose",
        "wing": 3, "x": 51, "y": 5, "cost": 8,
        "prereq": ["FRA_projet_cuirasses_classe_lyon"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = submarine_bonus bonus = 1.0 uses = 2 category = ss_tech }",
        "icon_query": ["pluviose", "submarine", "french_sub"],
        "title": "Pluviôse & Brumaire Submarines",
        "desc": "French steam and diesel submersibles prove their endurance in the Adriatic and Aegean Seas, penetrating defended enemy anchorages."
    })
    foci.append({
        "id": "FRA_grenades_anti_sous_marines_guiraud",
        "wing": 3, "x": 57, "y": 5, "cost": 8,
        "prereq": ["FRA_patrouilles_anti_sous_marines"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_anti_sub_factor = 0.20\nadd_equipment_to_stockpile = { type = support_equipment_1 amount = 50 }",
        "icon_query": ["guiraud", "hydrophone", "depth_charge_thrower"],
        "title": "Guiraud Depth Charges & Hydrophones",
        "desc": "Invented by French naval engineers, hydrostatic depth charges and underwater listening hydrophones allow surface escorts to strike submerged U-boats."
    })
    foci.append({
        "id": "FRA_blocus_du_canal_d_otrante",
        "wing": 3, "x": 54, "y": 6, "cost": 8,
        "prereq": ["FRA_sous_marins_classe_pluviose", "FRA_grenades_anti_sous_marines_guiraud"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_morale_factor = 0.10\nadd_opinion_modifier = { target = ITA modifier = FRA_naval_cooperation_opinion }",
        "icon_query": ["otranto_barrage", "strait_blockade", "adriatic_naval"],
        "title": "The Otranto Barrage Blockade",
        "desc": "Joining British and Italian flotillas across the Strait of Otranto, French destroyers and drifters bottle up the Austro-Hungarian fleet in Pola."
    })
    foci.append({
        "id": "FRA_croiseurs_auxiliaires_et_q_ships",
        "wing": 3, "x": 51, "y": 7, "cost": 8,
        "prereq": ["FRA_blocus_du_canal_d_otrante"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "convoy_escort_efficiency = 0.15\nadd_political_power = 40",
        "icon_query": ["q_ship", "auxiliary_cruiser", "decoy_ship"],
        "title": "Auxiliary Cruisers & Decoy Ships",
        "desc": "Concealing heavy 138mm naval guns behind dummy cargo crates, French Q-ships lure surfaced U-boats into close-range ambushes."
    })
    foci.append({
        "id": "FRA_porte_hydravions_foudre",
        "wing": 3, "x": 57, "y": 7, "cost": 8,
        "prereq": ["FRA_blocus_du_canal_d_otrante"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = carrier_bonus bonus = 1.0 uses = 1 category = cv_tech }",
        "icon_query": ["seaplane_carrier", "la_foudre", "naval_aviation"],
        "title": "Seaplane Tender 'La Foudre'",
        "desc": "The world's first operational seaplane carrier, La Foudre launches Farman and Caudron floatplanes to scout enemy coastlines and spot naval gunfire."
    })
    foci.append({
        "id": "FRA_torpilleurs_de_haute_mer_arabe",
        "wing": 3, "x": 51, "y": 8, "cost": 8,
        "prereq": ["FRA_croiseurs_auxiliaires_et_q_ships"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_screen_attack_factor = 0.10\nnavy_screen_defence_factor = 0.10",
        "icon_query": ["torpedo_boat", "destroyer_arabe", "fast_screener"],
        "title": "Arabe-Class Fleet Torpedo Destroyers",
        "desc": "Built in Japanese and French shipyards, these fast destroyers provide agile screening and torpedo salvos for French heavy divisions."
    })
    foci.append({
        "id": "FRA_surveillance_du_detroit_de_gibraltar",
        "wing": 3, "x": 57, "y": 8, "cost": 8,
        "prereq": ["FRA_porte_hydravions_foudre"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "naval_coordination = 0.10\nadd_political_power = 40",
        "icon_query": ["gibraltar_patrol", "strait_surveillance", "naval_mines"],
        "title": "Gibraltar Strait Surveillance",
        "desc": "Coordinating with the British garrison at the Rock, French maritime patrol aircraft and patrol craft seal the western entrance to the Mediterranean."
    })
    foci.append({
        "id": "FRA_escorteurs_rapides_classe_ailette",
        "wing": 3, "x": 51, "y": 9, "cost": 8,
        "prereq": ["FRA_torpilleurs_de_haute_mer_arabe"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_dockyard_output_factor = 0.10",
        "icon_query": ["escort_ship", "corvette", "sub_hunter_boat"],
        "title": "Ailette Fast Convoy Escorts",
        "desc": "Purpose-built shallow-draft escort sloops protect merchant shipping convoys from Saint-Nazaire and Bordeaux against coastal mining and U-boat raids."
    })
    foci.append({
        "id": "FRA_dragage_des_mines_de_mer",
        "wing": 3, "x": 57, "y": 9, "cost": 8,
        "prereq": ["FRA_surveillance_du_detroit_de_gibraltar"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "mine_clearing_efficiency = 0.25",
        "icon_query": ["minesweeper", "sea_mines", "sweeper_flotilla"],
        "title": "Minesweeping Flotillas",
        "desc": "Clearing the deadly minefields sown across the English Channel and the Gulf of Lion ensures allied troopships sail with minimal losses."
    })
    foci.append({
        "id": "FRA_fusiliers_marins_amiral_ronarch",
        "wing": 3, "x": 54, "y": 10, "cost": 8,
        "prereq": ["FRA_escorteurs_rapides_classe_ailette", "FRA_dragage_des_mines_de_mer"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_manpower = 25000\narmy_core_defence_factor = 0.08",
        "icon_query": ["fusiliers_marins", "ronarch", "breton_sailors"],
        "title": "Admiral Ronarc'h's Fusiliers Marins",
        "desc": "When the front cracked in 1914, Admiral Pierre-Alexis Ronarc'h organized 6,000 Breton sailors into the Brigade des Fusiliers Marins to fight as infantry."
    })
    foci.append({
        "id": "FRA_defense_de_dixmude_1914",
        "wing": 3, "x": 54, "y": 11, "cost": 8,
        "prereq": ["FRA_fusiliers_marins_amiral_ronarch"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_stability = 0.08\nadd_war_support = 0.08",
        "icon_query": ["dixmude", "battle_dixmude", "ysir_river"],
        "title": "The Immortal Stand at Dixmude",
        "desc": "Holding Dixmude on the Yser against three German army corps for three desperate weeks, the Fusiliers Marins saved the allied flank and anchored the race to the sea."
    })
    foci.append({
        "id": "FRA_ravitaillement_naval_du_front_salonique",
        "wing": 3, "x": 51, "y": 12, "cost": 8,
        "prereq": ["FRA_defense_de_dixmude_1914"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "naval_attrition = -0.15\nadd_political_power = 40",
        "icon_query": ["salonika_convoy", "orient_fleet", "supply_ships"],
        "title": "Naval Lifeline to Salonika",
        "desc": "Maintaining uninterrupted transport and hospital ship runs across the Aegean keeps General Sarrail's multinational Army of the Orient supplied."
    })
    foci.append({
        "id": "FRA_chasseurs_de_sous_marins_sub_chaser",
        "wing": 3, "x": 57, "y": 12, "cost": 8,
        "prereq": ["FRA_defense_de_dixmude_1914"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "navy_screen_attack_factor = 0.10\nnavy_submarine_attack_factor = 0.15",
        "icon_query": ["sub_chaser", "motor_launch", "patrol_boat"],
        "title": "American Wooden Sub-Chaser Contracts",
        "desc": "Purchasing 110-foot wooden sub-chasers from US shipyards supplements French escorts with agile, mass-produced anti-submarine screening craft."
    })
    foci.append({
        "id": "FRA_maitrise_definitive_de_la_mediterranee",
        "wing": 3, "x": 54, "y": 13, "cost": 10,
        "prereq": ["FRA_ravitaillement_naval_du_front_salonique", "FRA_chasseurs_de_sous_marins_sub_chaser"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_mediterranean_dominance\nadd_stability = 0.10",
        "icon_query": ["mediterranean_mastery", "fleet_triumph", "marine_victory"],
        "title": "Mastery of the Mediterranean",
        "desc": "From Gibraltar to Port Said, the tricolor rules the waves. The central powers remain blockaded, while French colonial lines flow without hindrance."
    })

    # 3.2 Aéronautique Militaire
    foci.append({
        "id": "FRA_creer_l_aeronautique_militaire",
        "wing": 3, "x": 66, "y": 0, "cost": 10,
        "prereq": [], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_experience = 25\nadd_tech_bonus = { name = air_bonus bonus = 1.0 uses = 1 category = air_equipment }",
        "icon_query": ["GFX_FRA_aronautique_militaire-69196", "french_air_force", "early_plane", "focus_French_Air_Force"],
        "title": "L'Aéronautique Militaire",
        "desc": "Created as an official arm of the French Army in March 1912, military aviation takes flight. Pioneers like Clément Ader and Louis Blériot established French pre-eminence."
    })
    foci.append({
        "id": "FRA_monoplans_morane_saulnier",
        "wing": 3, "x": 63, "y": 1, "cost": 8,
        "prereq": ["FRA_creer_l_aeronautique_militaire"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = fighter_bonus bonus = 1.0 uses = 1 category = light_fighter }",
        "icon_query": ["morane_saulnier", "monoplane", "scout_plane"],
        "title": "Morane-Saulnier Monoplanes",
        "desc": "The parasol-wing monoplanes of Morane-Saulnier offer superb downward visibility and speed, serving as our primary scout and observation machines."
    })
    foci.append({
        "id": "FRA_biplans_farman_reconnaissance",
        "wing": 3, "x": 69, "y": 1, "cost": 8,
        "prereq": ["FRA_creer_l_aeronautique_militaire"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "recon_factor = 0.15\nadd_equipment_to_stockpile = { type = scout_plane_equipment_1 amount = 50 }",
        "icon_query": ["farman", "biplane", "reconnaissance_aircraft"],
        "title": "Farman HF.20 Reconnaissance",
        "desc": "The stable pusher-biplanes of the Farman brothers map enemy trench layouts and troop movements, providing headquarters with daily aerial photography."
    })
    foci.append({
        "id": "FRA_reglage_d_artillerie_par_tsh",
        "wing": 3, "x": 66, "y": 2, "cost": 8,
        "prereq": ["FRA_monoplans_morane_saulnier", "FRA_biplans_farman_reconnaissance"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "army_artillery_attack_factor = 0.08\nair_cas_efficiency = 0.10",
        "icon_query": ["artillery_spotting", "tsh_radio", "aerial_observation"],
        "title": "Wireless Artillery Spotting (TSH)",
        "desc": "Equipping observation aircraft with Télégraphie Sans Fil (TSH) allows airborne observers to correct artillery fire in real time onto hidden German batteries."
    })
    foci.append({
        "id": "FRA_chasseurs_nieuport_11_bebe",
        "wing": 3, "x": 63, "y": 3, "cost": 8,
        "prereq": ["FRA_reglage_d_artillerie_par_tsh"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = nieuport_bonus bonus = 1.0 uses = 1 category = light_fighter }",
        "icon_query": ["nieuport_11", "nieuport_bebe", "fighter_plane"],
        "title": "Nieuport 11 'Bébé' Fighters",
        "desc": "Designed by Gustave Delage, the nimble Nieuport 11 sesquiplane ended the 'Fokker Scourge' in 1916, dominating the sky over Verdun."
    })
    foci.append({
        "id": "FRA_tir_a_travers_l_helice_garros",
        "wing": 3, "x": 69, "y": 3, "cost": 8,
        "prereq": ["FRA_reglage_d_artillerie_par_tsh"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_attack_factor = 0.15\nair_experience = 20",
        "icon_query": ["roland_garros", "synchronization_gear", "gun_propeller"],
        "title": "Roland Garros Armored Deflector Blades",
        "desc": "Aviator Roland Garros fitted armored steel wedges to his propeller blades, enabling his Hotchkiss machine gun to fire directly through the propeller arc."
    })
    foci.append({
        "id": "FRA_les_as_de_la_chasse_guynemer",
        "wing": 3, "x": 66, "y": 4, "cost": 8,
        "prereq": ["FRA_chasseurs_nieuport_11_bebe", "FRA_tir_a_travers_l_helice_garros"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_war_support = 0.10\nair_ace_generation_chance_factor = 0.50",
        "icon_query": ["guynemer", "fonck", "cigognes", "air_ace"],
        "title": "Les As: Guynemer & Les Cigognes",
        "desc": "Georges Guynemer and the legendary 'Escadrille des Cigognes' become immortal national symbols. Their duels in the clouds inspire a war-weary population."
    })
    foci.append({
        "id": "FRA_escadrille_la_fayette",
        "wing": 3, "x": 63, "y": 5, "cost": 8,
        "prereq": ["FRA_les_as_de_la_chasse_guynemer"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_opinion_modifier = { target = USA modifier = FRA_lafayette_escadrille_opinion }\nadd_war_support = 0.05",
        "icon_query": ["escadrille_lafayette", "american_volunteers", "sioux_indian_head"],
        "title": "L'Escadrille La Fayette",
        "desc": "American volunteer pilots flock to France under the emblem of a Sioux warrior head, flying hazardous combat missions long before US official entry."
    })
    foci.append({
        "id": "FRA_chasseurs_spad_vii_hispano",
        "wing": 3, "x": 69, "y": 5, "cost": 8,
        "prereq": ["FRA_les_as_de_la_chasse_guynemer"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = spad_bonus bonus = 1.0 uses = 1 category = light_fighter }",
        "icon_query": ["spad_vii", "hispano_suiza", "sturdy_fighter"],
        "title": "SPAD VII & Hispano-Suiza V8",
        "desc": "Powered by Marc Birkigt's cast-aluminum water-cooled V8 engine, the SPAD VII is rugged, heavy, and capable of devastating high-speed diving attacks."
    })
    foci.append({
        "id": "FRA_chasseurs_spad_xiii_suprematie",
        "wing": 3, "x": 66, "y": 6, "cost": 8,
        "prereq": ["FRA_escadrille_la_fayette", "FRA_chasseurs_spad_vii_hispano"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_superiority_factor = 0.15\nair_agility_factor = 0.10",
        "icon_query": ["spad_xiii", "french_fighter", "twin_vickers"],
        "title": "SPAD XIII Aerial Supremacy",
        "desc": "Carrying twin synchronized Vickers guns and a 220 hp engine, the SPAD XIII outclimbs and outdives every German opponent across the 1918 battlefields."
    })
    foci.append({
        "id": "FRA_bombardiers_breguet_14",
        "wing": 3, "x": 63, "y": 7, "cost": 8,
        "prereq": ["FRA_chasseurs_spad_xiii_suprematie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_tech_bonus = { name = breguet_bonus bonus = 1.0 uses = 1 category = tactical_bomber }",
        "icon_query": ["breguet_14", "day_bomber", "duralumin_aircraft"],
        "title": "Breguet 14 Duralumin Bombers",
        "desc": "Louis Breguet's masterpiece utilizes welded duralumin structural frames, creating a rugged day bomber and reconnaissance plane capable of carrying 300 kg of bombs."
    })
    foci.append({
        "id": "FRA_avions_d_attaque_au_sol_salmson",
        "wing": 3, "x": 69, "y": 7, "cost": 8,
        "prereq": ["FRA_chasseurs_spad_xiii_suprematie"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_cas_efficiency = 0.15\narmy_artillery_attack_factor = 0.05",
        "icon_query": ["salmson_2", "ground_support", "radial_engine"],
        "title": "Salmson 2A2 Ground Assault",
        "desc": "Water-cooled radial engines and self-sealing fuel tanks allow Salmson biplanes to strafe retreating German columns from tree-top height."
    })
    foci.append({
        "id": "FRA_optiques_aeriennes_de_precision",
        "wing": 3, "x": 63, "y": 8, "cost": 8,
        "prereq": ["FRA_bombardiers_breguet_14"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "recon_factor = 0.20",
        "icon_query": ["aerial_camera", "telephoto_lens", "precision_recon"],
        "title": "Aerial Telephoto Precision Optics",
        "desc": "Giant 50cm focal length cameras mounted through aircraft fuselages photograph entire enemy defensive systems, revealing hidden battery positions."
    })
    foci.append({
        "id": "FRA_avions_torpilleurs_marins",
        "wing": 3, "x": 69, "y": 8, "cost": 8,
        "prereq": ["FRA_avions_d_attaque_au_sol_salmson"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "naval_strike = 0.15",
        "icon_query": ["torpedo_bomber", "aerial_torpedo", "coastal_patrol"],
        "title": "Aerial Torpedo Launchers",
        "desc": "Adapting naval torpedoes for aerial release from coastal floatplanes establishes the doctrine of anti-shipping airborne strikes."
    })
    foci.append({
        "id": "FRA_ecoles_d_aviation_pau_avord",
        "wing": 3, "x": 66, "y": 9, "cost": 8,
        "prereq": ["FRA_optiques_aeriennes_de_precision", "FRA_avions_torpilleurs_marins"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_training_factor = -0.20\nair_ace_generation_chance_factor = 0.25",
        "icon_query": ["flight_school", "pilot_training", "pau_aviation"],
        "title": "Aviation Academies: Pau & Avord",
        "desc": "Thousands of cadet pilots are trained through rigorous aerobatic regimens, stunt maneuvers, and aerial gunnery on the sunny plains of southwestern France."
    })
    foci.append({
        "id": "FRA_mitrailleuses_vickers_d_aviation",
        "wing": 3, "x": 63, "y": 10, "cost": 8,
        "prereq": ["FRA_ecoles_d_aviation_pau_avord"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_attack_factor = 0.10",
        "icon_query": ["vickers_air", "twin_guns", "ammunition_drum"],
        "title": "Twin Vickers Heavy Armament",
        "desc": "Standardizing twin air-cooled Vickers guns with incendiary and armor-piercing ammunition allows French scouts to shred fabric biplanes in seconds."
    })
    foci.append({
        "id": "FRA_avions_de_chasse_de_nuit",
        "wing": 3, "x": 69, "y": 10, "cost": 8,
        "prereq": ["FRA_ecoles_d_aviation_pau_avord"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_night_penalty = -0.25",
        "icon_query": ["night_fighter", "searchlight_interception", "gotha_defense"],
        "title": "Night Fighter Defense of Paris",
        "desc": "Special night-fighting squadrons guided by ground searchlight rings intercept German Gotha and Giant bombers raiding Paris in the dark."
    })
    foci.append({
        "id": "FRA_ballons_captifs_saucisses",
        "wing": 3, "x": 66, "y": 11, "cost": 8,
        "prereq": ["FRA_mitrailleuses_vickers_d_aviation", "FRA_avions_de_chasse_de_nuit"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "max_entrenchment = 3\nrecon_factor = 0.10",
        "icon_query": ["caquot_balloon", "captive_balloon", "saucisse"],
        "title": "Caquot Observation Balloons ('Les Saucisses')",
        "desc": "Albert Caquot's teardrop-shaped kite balloons remain stable in 90 km/h winds, providing observers with telephone links to artillery commanders."
    })
    foci.append({
        "id": "FRA_bombardement_strategique_usines_rhenanes",
        "wing": 3, "x": 63, "y": 12, "cost": 8,
        "prereq": ["FRA_ballons_captifs_saucisses"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_bombing_factor = 0.15",
        "icon_query": ["strategic_bombing", "rhine_bombing", "krupp_raids"],
        "title": "Strategic Raids on the Rhineland",
        "desc": "French heavy bombers fly deep into Germany to strike the blast furnaces of Völklingen and the chemical works of Ludwigshafen, disrupting enemy production."
    })
    foci.append({
        "id": "FRA_escadrilles_de_protection_du_gqg",
        "wing": 3, "x": 69, "y": 12, "cost": 8,
        "prereq": ["FRA_ballons_captifs_saucisses"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_superiority_factor = 0.10\nadd_political_power = 40",
        "icon_query": ["gqg_escort", "patrol_skies", "fighter_escort"],
        "title": "High Command Air Escort Groups",
        "desc": "Elite fighter flights circle overhead allied railway hubs and army command headquarters, shooting down German reconnaissance scouts."
    })
    foci.append({
        "id": "FRA_division_aerienne_du_colonel_duval",
        "wing": 3, "x": 66, "y": 13, "cost": 10,
        "prereq": ["FRA_bombardement_strategique_usines_rhenanes", "FRA_escadrilles_de_protection_du_gqg"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "add_ideas = FRA_air_supremacy_spad\nair_experience = 50",
        "icon_query": ["division_aerienne", "duval", "mass_aviation"],
        "title": "Colonel Duval's 1st Air Division",
        "desc": "Formed in May 1918, the Division Aérienne masses over 600 fighters and day bombers into a single operational air corps, acting as a tactical sledgehammer."
    })
    foci.append({
        "id": "FRA_suprematie_aerienne_absolue",
        "wing": 3, "x": 66, "y": 14, "cost": 10,
        "prereq": ["FRA_division_aerienne_du_colonel_duval"], "mut_ex": [],
        "allow_branch": None, "available": None,
        "reward": "air_superiority_factor = 0.20\nadd_war_support = 0.10",
        "icon_query": ["sky_supremacy", "wings_victory", "tricolor_wings"],
        "title": "Uncontested Mastery of the Air",
        "desc": "French roundels fly supreme over every square mile of the Western Front. No German division can march by daylight without being strafed from above."
    })

    return foci

if __name__ == "__main__":
    w3 = get_wing_3_foci()
    print("Wing 3 count:", len(w3))
