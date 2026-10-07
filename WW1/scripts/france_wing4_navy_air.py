# -*- coding: utf-8 -*-
"""France Wing 4: Marine Nationale & Aéronautique Militaire (35 focuses).
X range: 46 .. 58 | Y range: 0 .. 11
"""

WING4_FOCI = [
    # Y = 0 (Navy & Air Roots)
    {
        "id": "FRA_ministere_de_la_marine",
        "x": 49, "y": 0, "cost": 10,
        "icon": "GFX_FRA_ministere_de_la_marine",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 40
add_navy_experience = 25
21 = { add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Ministry of the Navy Reorganisation",
        "title_pt": "Reorganização do Ministério da Marinha",
        "desc_en": "Admiral Auguste Boué de Lapeyrère sweeps away bureaucratic inertia on Rue Royale, establishing an aggressive battle fleet doctrine focused on battleships and Mediterranean command.",
        "desc_pt": "O Almirante Auguste Boué de Lapeyrère extingue a inércia burocrática na Rue Royale, estabelecendo uma doutrina agressiva de esquadra centrada em couraçados e no controle do Mediterrâneo."
    },
    {
        "id": "FRA_creer_l_aeronautique_militaire",
        "x": 55, "y": 0, "cost": 10,
        "icon": "GFX_FRA_creer_l_aeronautique_militaire",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 30
add_air_experience = 25
add_tech_bonus = { name = air_doctrine bonus = 1.0 uses = 1 category = air_doctrine }""",
        "title_en": "Founding of the Aéronautique Militaire",
        "title_pt": "Criação da Aéronautique Militaire",
        "desc_en": "By decree of March 1912, aviation is formally organized as an independent military service, pioneering organized military aviation with dedicated regiments, airfields, and depots.",
        "desc_pt": "Por decreto de março de 1912, a aviação é oficialmente organizada como arma militar autônoma, pioneira no mundo com regimentos, aeródromos e depósitos dedicados."
    },

    # Y = 1
    {
        "id": "FRA_statut_naval_de_1912",
        "x": 47, "y": 1, "cost": 8,
        "icon": "GFX_FRA_statut_naval_de_1912",
        "prereq": ["FRA_ministere_de_la_marine"], "mut": [],
        "reward": """add_tech_bonus = { name = bb_bonus bonus = 1.0 uses = 1 category = heavy_ship }
add_ideas = FRA_boue_de_lapeyrere_naval_law""",
        "title_en": "Naval Expansion Law of 1912",
        "title_pt": "Estatuto Naval de 1912",
        "desc_en": "Passing Boué de Lapeyrère's multi-year naval law funds construction of twenty-eight first-class dreadnought battleships to maintain naval superiority over Austro-Italian fleets.",
        "desc_pt": "A aprovação do estatuto naval plurianual de Boué de Lapeyrère financia a construção de vinte e oito couraçados de primeira linha para manter superioridade sobre frotas austro-italianas."
    },
    {
        "id": "FRA_arsenaux_de_toulon_et_brest",
        "x": 51, "y": 1, "cost": 8,
        "icon": "GFX_FRA_arsenaux_de_toulon_et_brest",
        "prereq": ["FRA_ministere_de_la_marine"], "mut": [],
        "reward": """21 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 1 instant_build = yes } }
14 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Great Arsenals of Toulon & Brest",
        "title_pt": "Grandes Arsenais de Toulon e Brest",
        "desc_en": "Modernising graving docks in Toulon (Bouches-du-Rhône) and Brest (Brittany) accommodates mammoth 25,000-tonne dreadnought hulls and continuous engine refits.",
        "desc_pt": "A modernização dos diques secos em Toulon e Brest permite acomodar cascos de couraçados de 25.000 toneladas e reformas contínuas de turbinas a vapor."
    },
    {
        "id": "FRA_ecoles_de_pilotage_pau_et_etampes",
        "x": 53, "y": 1, "cost": 8,
        "icon": "GFX_FRA_ecoles_de_pilotage_pau_et_etampes",
        "prereq": ["FRA_creer_l_aeronautique_militaire"], "mut": [],
        "reward": """add_air_experience = 20
add_ideas = FRA_pilot_training_corps""",
        "title_en": "Flight Schools of Pau & Étampes",
        "title_pt": "Escolas de Pilotagem de Pau e Étampes",
        "desc_en": "Civilian flying schools founded by Blériot and Farman are militarized to train hundreds of military aviators in aerobatics, navigation, and cross-country reconnaissance.",
        "desc_pt": "As escolas pioneiras fundadas por Blériot e Farman são militarizadas para treinar centenas de aviadores em acrobacias, navegação e reconhecimento de longa distância."
    },
    {
        "id": "FRA_dirigeables_et_ballons_d_observation",
        "x": 57, "y": 1, "cost": 8,
        "icon": "GFX_FRA_dirigeables_et_ballons_d_observation",
        "prereq": ["FRA_creer_l_aeronautique_militaire"], "mut": [],
        "reward": """add_tech_bonus = { name = air_support bonus = 1.0 uses = 1 category = air_doctrine }
add_ideas = FRA_caquot_observation_balloons""",
        "title_en": "Caquot Tethered Observation Balloons",
        "title_pt": "Balões Cativos de Observação Caquot",
        "desc_en": "Captain Albert Caquot designs aerodynamic kite-balloons ('saucisses') that remain rock-steady in high winds, providing artillery spotters telephone links to gun batteries.",
        "desc_pt": "O Capitão Albert Caquot projeta balões aerodinâmicos estáveis ('saucisses') que resistem a ventos fortes, ligando observadores de artilharia por telefone aos canhões de 75mm."
    },

    # Y = 2
    {
        "id": "FRA_dreadnoughts_classe_courbet",
        "x": 47, "y": 2, "cost": 8,
        "icon": "GFX_FRA_dreadnoughts_classe_courbet",
        "prereq": ["FRA_statut_naval_de_1912"], "mut": [],
        "reward": """add_tech_bonus = { name = heavy_ship_bonus bonus = 1.0 uses = 1 category = heavy_ship }
add_navy_experience = 20
21 = { add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Courbet-Class Dreadnoughts",
        "title_pt": "Couraçados da Classe Courbet",
        "desc_en": "Commissioning Jean Bart, Courbet, Paris, and France delivers twelve 305mm heavy guns in six turrets, giving the French battle line true dreadnought striking power.",
        "desc_pt": "O comissionamento do Jean Bart, Courbet, Paris e France entrega doze canhões pesados de 305mm em seis torres, garantindo poder de choque couraçado de primeira linha."
    },
    {
        "id": "FRA_flotte_de_haute_mer_mediterranee",
        "x": 51, "y": 2, "cost": 8,
        "icon": "GFX_FRA_flotte_de_haute_mer_mediterranee",
        "prereq": ["FRA_arsenaux_de_toulon_et_brest"], "mut": [],
        "reward": """add_ideas = FRA_mediterranean_battlefleet
add_navy_experience = 25""",
        "title_en": "1st High Seas Army in the Mediterranean",
        "title_pt": "1º Exército Naval de Alto-Mar no Mediterrâneo",
        "desc_en": "Stationing all modern battleships in Toulon and Mers-el-Kébir creates a formidable striking fist, ready to intercept the German battlecruiser Goeben or crush the Austrian fleet.",
        "desc_pt": "Concentrar todos os couraçados modernos em Toulon e Mers-el-Kébir forma uma formidável esquadra de ataque, pronta para interceptar o Goeben alemão ou aniquilar a frota austríaca."
    },
    {
        "id": "FRA_avions_de_reconnaissance_farman_voisin",
        "x": 55, "y": 2, "cost": 8,
        "icon": "GFX_FRA_avions_de_reconnaissance_farman_voisin",
        "prereq": ["FRA_ecoles_de_pilotage_pau_et_etampes"], "mut": [],
        "reward": """add_tech_bonus = { name = cas_bonus bonus = 1.0 uses = 1 category = air_equipment }
add_air_experience = 15""",
        "title_en": "Farman & Voisin Reconnaissance Biplanes",
        "title_pt": "Biplanos de Reconhecimento Farman e Voisin",
        "desc_en": "The pusher-propeller Maurice Farman MF.11 and Gabriel Voisin Type III biplanes spot Von Kluck's wheeling turn towards the Marne, proving that aviation alters strategy.",
        "desc_pt": "Os biplanos Maurice Farman e Voisin Type III avistam a manobra de Von Kluck em direção ao Marne, provando que a aviação altera radicalmente o destino da guerra terrestre."
    },

    # Y = 3
    {
        "id": "FRA_cuirasses_classe_bretagne",
        "x": 47, "y": 3, "cost": 8,
        "icon": "GFX_FRA_cuirasses_classe_bretagne",
        "prereq": ["FRA_dreadnoughts_classe_courbet"], "mut": [],
        "reward": """add_tech_bonus = { name = heavy_ship_bonus bonus = 1.0 uses = 1 category = heavy_ship }
add_navy_experience = 20""",
        "title_en": "Bretagne-Class Super-Dreadnoughts",
        "title_pt": "Super-Couraçados da Classe Bretagne",
        "desc_en": "Mounting ten 340mm guns along the centerline, Bretagne, Provence, and Lorraine elevate French firepower to counter any dreadnought built by Vienna or Berlin.",
        "desc_pt": "Armados com dez canhões pesados de 340mm na linha central, o Bretagne, Provence e Lorraine elevam o poder de fogo francês para rivalizar com qualquer navio de Berlim ou Viena."
    },
    {
        "id": "FRA_blocus_de_l_adriatique",
        "x": 51, "y": 3, "cost": 8,
        "icon": "GFX_FRA_blocus_de_l_adriatique",
        "prereq": ["FRA_flotte_de_haute_mer_mediterranee"], "mut": [],
        "reward": """add_ideas = FRA_adriatic_naval_blockade
add_political_power = 30""",
        "title_en": "Adriatic Blockade & Otranto Barrage",
        "title_pt": "Bloqueio do Adriático e Barragem de Otranto",
        "desc_en": "Bottling up the Austro-Hungarian fleet in Pola and Cattaro prevents enemy battleships from venturing into the Mediterranean or severing French troop convoys.",
        "desc_pt": "Confinar a esquadra austro-húngara em Pola e Cattaro impede os couraçados inimigos de navegarem pelo Mediterrâneo ou cortarem comboios coloniais franceses."
    },
    {
        "id": "FRA_croiseurs_cuirasses_classe_waldeck_rousseau",
        "x": 49, "y": 3, "cost": 8,
        "icon": "GFX_FRA_croiseurs_cuirasses_classe_waldeck_rousseau",
        "prereq": ["FRA_flotte_de_haute_mer_mediterranee"], "mut": [],
        "reward": """add_tech_bonus = { name = cr_bonus bonus = 1.0 uses = 1 category = cl_tech }
add_navy_experience = 15""",
        "title_en": "Armored Cruisers (Waldeck-Rousseau Class)",
        "title_pt": "Cruzadores Blindados da Classe Waldeck-Rousseau",
        "desc_en": "Fast armored cruisers armed with 194mm guns patrol open sea lanes, hunt enemy commerce raiders, and provide fleet reconnaissance.",
        "desc_pt": "Cruzadores blindados velozes com canhões de 194mm patrulham rotas oceânicas, caçam incursores corsários e realizam reconhecimento tático."
    },
    {
        "id": "FRA_synchronisation_de_mitrailleuse_garros",
        "x": 55, "y": 3, "cost": 6,
        "icon": "GFX_FRA_synchronisation_de_mitrailleuse_garros",
        "prereq": ["FRA_avions_de_reconnaissance_farman_voisin"], "mut": [],
        "reward": """add_tech_bonus = { name = fighter_bonus bonus = 1.0 uses = 1 category = light_fighter }
add_air_experience = 25""",
        "title_en": "Roland Garros' Gun Interrupter Deflector",
        "title_pt": "Defletores de Hélice de Roland Garros",
        "desc_en": "Roland Garros and Raymond Saulnier fit steel deflector wedges to propeller blades, allowing a forward-firing machine gun to aim through the propeller disc.",
        "desc_pt": "Roland Garros e Raymond Saulnier instalam cunhas defletoras de aço nas pás das hélices, permitindo que uma metralhadora frontal dispare através da rotação da hélice."
    },

    # Y = 4
    {
        "id": "FRA_base_navale_de_bizerte",
        "x": 49, "y": 4, "cost": 8,
        "icon": "GFX_FRA_base_navale_de_bizerte",
        "prereq": ["FRA_blocus_de_l_adriatique"], "mut": [],
        "reward": """458 = { add_building_construction = { type = naval_base level = 2 instant_build = yes } }
add_navy_experience = 15""",
        "title_en": "Fortified Naval Bastion of Bizerte",
        "title_pt": "Bastião Naval Fortificado de Bizerte",
        "desc_en": "Transforming the Tunisian saltwater lake into a protected submarine and torpedo boat harbor dominates the Sicilian Narrows and guards the western Mediterranean basin.",
        "desc_pt": "A transformação do lago de Bizerte em porto protegido de contratorpedeiros e submarinos domina o Estreito da Sicília e protege a bacia ocidental do Mediterrâneo."
    },
    {
        "id": "FRA_flottilles_de_sous_marins_narval",
        "x": 51, "y": 4, "cost": 8,
        "icon": "GFX_FRA_flottilles_de_sous_marins_narval",
        "prereq": ["FRA_blocus_de_l_adriatique"], "mut": [],
        "reward": """add_tech_bonus = { name = sub_tech bonus = 1.0 uses = 1 category = ss_tech }
add_navy_experience = 15""",
        "title_en": "Brumaire & Pluviôse Submarine Flotillas",
        "title_pt": "Flotilhas de Submarinos Brumaire e Pluviôse",
        "desc_en": "Deploying steam-and-diesel submarines into the Adriatic lays defensive minefields and harasses Austro-Hungarian battleships leaving naval anchorages.",
        "desc_pt": "O emprego de submarinos no Adriático estabelece campos minados defensivos e assedia os couraçados austro-húngaros na saída de seus ancoradouros."
    },
    {
        "id": "FRA_mitrailleuses_vickers_d_aviation",
        "x": 53, "y": 4, "cost": 8,
        "icon": "GFX_FRA_mitrailleuses_vickers_d_aviation",
        "prereq": ["FRA_synchronisation_de_mitrailleuse_garros"], "mut": [],
        "reward": """add_ideas = FRA_synchronized_vickers_guns
add_air_experience = 15""",
        "title_en": "Synchronized Vickers Machine Guns",
        "title_pt": "Metralhadoras Sincronizadas Vickers de Aviação",
        "desc_en": "Adopting the Alkan-Hamy mechanical synchronizer allows belt-fed Vickers machine guns to fire through the propeller arc without bullet deflectors.",
        "desc_pt": "A adoção do sincronizador mecânico Alkan-Hamy permite disparar metralhadoras Vickers alimentadas por fita através da hélice sem perda de cadência."
    },
    {
        "id": "FRA_avions_torpilleurs_marins",
        "x": 57, "y": 4, "cost": 8,
        "icon": "GFX_FRA_avions_torpilleurs_marins",
        "prereq": ["FRA_synchronisation_de_mitrailleuse_garros"], "mut": [],
        "reward": """add_tech_bonus = { name = nav_bomber bonus = 1.0 uses = 1 category = naval_bomber }
add_air_experience = 15""",
        "title_en": "Coastal Torpedo & Patrol Seaplanes",
        "title_pt": "Hidroaviões de Patrulha e Lançamento de Torpedos",
        "desc_en": "Twin-float seaplanes developed by Tellier and FBA patrol shipping lanes, detecting submerged U-boat silhouettes from the air and releasing depth charges.",
        "desc_pt": "Hidroaviões de flutuador duplo patrulham as rotas de navegação, avistando silhuetas submarinas do ar e lançando cargas de profundidade."
    },
    {
        "id": "FRA_moteurs_hispano_suiza_et_gnome",
        "x": 55, "y": 4, "cost": 8,
        "icon": "GFX_FRA_moteurs_hispano_suiza_et_gnome",
        "prereq": ["FRA_synchronisation_de_mitrailleuse_garros"], "mut": [],
        "reward": """add_ideas = FRA_hispano_suiza_aero_engines
16 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Hispano-Suiza & Gnome Aero Engines",
        "title_pt": "Motores Aeronáuticos Hispano-Suiza e Gnome",
        "desc_en": "Marc Birkigt's cast-aluminum V8 Hispano-Suiza engine and Gnome rotary engines deliver unprecedented power-to-weight ratios, propelling French aircraft to world supremacy.",
        "desc_pt": "O motor V8 de alumínio fundido Hispano-Suiza de Marc Birkigt e os motores rotativos Gnome entregam potência formidável, impulsionando os caças franceses ao topo mundial."
    },

    # Y = 5
    {
        "id": "FRA_reponse_a_la_menace_sous_marine",
        "x": 47, "y": 5, "cost": 8,
        "icon": "GFX_FRA_reponse_a_la_menace_sous_marine",
        "prereq": ["FRA_base_navale_de_bizerte"], "mut": [],
        "reward": """add_tech_bonus = { name = asw_tech bonus = 1.0 uses = 1 category = dd_tech }
add_navy_experience = 20""",
        "title_en": "Anti-Submarine Countermeasures",
        "title_pt": "Contramedidas Anti-Submarinas",
        "desc_en": "German U-boat raids in the Mediterranean sink merchantmen and troop transports. The navy rushes hydrophones, depth charge projectors, and coastal patrol flights into service.",
        "desc_pt": "Ataques de U-Boots no Mediterrâneo afundam cargueiros e transportes de tropas. A marinha instala hidrofones, calhas de cargas de profundidade e patrulhas aéreas litorâneas."
    },
    {
        "id": "FRA_chasseurs_nieuport_11_bebe",
        "x": 53, "y": 5, "cost": 8,
        "icon": "GFX_FRA_chasseurs_nieuport_11_bebe",
        "prereq": ["FRA_moteurs_hispano_suiza_et_gnome"], "mut": [],
        "reward": """add_tech_bonus = { name = light_fighter bonus = 1.0 uses = 1 category = light_fighter }
add_air_experience = 25""",
        "title_en": "Nieuport 11 'Bébé' Fighter Biplane",
        "title_pt": "O Caça Biplano Nieuport 11 'Bébé'",
        "desc_en": "Gustave Delage's lightweight sesquiplane out-turns and out-climbs the German Fokker Eindeckers, putting an end to the 'Fokker Scourge' over the Verdun front.",
        "desc_pt": "O leve biplano sesquiplano de Gustave Delage supera em agilidade e subida os Fokker Eindecker alemães, pondo fim ao 'Flagelo Fokker' sobre os céus de Verdun."
    },
    {
        "id": "FRA_bombardiers_breguet_14",
        "x": 57, "y": 5, "cost": 8,
        "icon": "GFX_FRA_bombardiers_breguet_14",
        "prereq": ["FRA_moteurs_hispano_suiza_et_gnome"], "mut": [],
        "reward": """add_tech_bonus = { name = tac_bonus bonus = 1.0 uses = 1 category = tactical_bomber }
add_air_experience = 20""",
        "title_en": "Breguet 14 All-Metal Bomber",
        "title_pt": "Bombardeiro e Reconhecimento Breguet 14",
        "desc_en": "Louis Breguet constructs the first mass-produced aircraft using duralumin metal framing. Sturdy and fast, the Breguet 14 bombs enemy railheads and tactical columns with impunity.",
        "desc_pt": "Louis Breguet constrói o primeiro avião produzido em massa com estrutura metálica de duralumínio. Robusto e veloz, bombardeia ferrovias e colunas táticas inimigas."
    },

    # Y = 6
    {
        "id": "FRA_torpilleurs_et_contre_torpilleurs",
        "x": 47, "y": 6, "cost": 8,
        "icon": "GFX_FRA_torpilleurs_et_contre_torpilleurs",
        "prereq": ["FRA_reponse_a_la_menace_sous_marine"], "mut": [],
        "reward": """add_tech_bonus = { name = dd_bonus bonus = 1.0 uses = 1 category = dd_tech }
14 = { add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Mass Torpedo-Boat Destroyer Production",
        "title_pt": "Produção em Massa de Contratorpedeiros",
        "desc_en": "Mass-producing the Bouclier and Bisson class destroyers provides swift, seaworthy escorts to hunt enemy submarines and shield battleship squadrons.",
        "desc_pt": "A produção em série dos contratorpedeiros das classes Bouclier e Bisson oferece escoltas velozes para caçar submarinos e proteger os esquadrões de couraçados."
    },
    {
        "id": "FRA_chasseurs_spad_vii_et_xiii",
        "x": 53, "y": 6, "cost": 8,
        "icon": "GFX_FRA_chasseurs_spad_vii_et_xiii",
        "prereq": ["FRA_chasseurs_nieuport_11_bebe"], "mut": [],
        "reward": """add_ideas = FRA_spad_fighter_supremacy
add_tech_bonus = { name = fighter_bonus bonus = 1.0 uses = 1 category = light_fighter }""",
        "title_en": "SPAD VII & XIII Heavy Pursuit Fighters",
        "title_pt": "Caças Pesados de Perseguição SPAD VII e XIII",
        "desc_en": "Built around the 220hp Hispano-Suiza engine, Louis Béchereau's SPAD XIII is a diving gun-platform capable of over 210 km/h, flown by all top Allied aces.",
        "desc_pt": "Projetado ao redor do motor Hispano-Suiza de 220 cv, o SPAD XIII de Louis Béchereau atinge mais de 210 km/h em mergulho, pilotado pelos maiores ases aliados."
    },
    {
        "id": "FRA_optiques_aeriennes_de_precision",
        "x": 57, "y": 6, "cost": 8,
        "icon": "GFX_FRA_optiques_aeriennes_de_precision",
        "prereq": ["FRA_bombardiers_breguet_14"], "mut": [],
        "reward": """add_ideas = FRA_aerial_photo_reconnaissance
add_air_experience = 15""",
        "title_en": "Aerial Photographic Mapping",
        "title_pt": "Fotografia Aérea e Mapeamento de Trincheiras",
        "desc_en": "Mounting precision focal lenses underneath aircraft fuselages maps enemy trench lines, pillboxes, and artillery positions with daily photographic accuracy.",
        "desc_pt": "Instalar câmeras de precisão nas fuselagens mapeia as linhas de trincheiras alemãs, casamatas e baterias de artilharia com atualização fotográfica diária."
    },

    # Y = 7
    {
        "id": "FRA_aviso_et_patrouilleurs_q_ships",
        "x": 47, "y": 7, "cost": 6,
        "icon": "GFX_FRA_aviso_et_patrouilleurs_q_ships",
        "prereq": ["FRA_torpilleurs_et_contre_torpilleurs"], "mut": [],
        "reward": """add_ideas = FRA_q_ships_and_coastal_avisos
add_navy_experience = 15""",
        "title_en": "Q-Ships & Armed Coastal Avisos",
        "title_pt": "Navios-Armadilha Q-Ships e Avisos Armados",
        "desc_en": "Disguised merchantmen concealing 75mm guns behind folding canvas screens lure surfaced U-boats into close-range gun duels, sinking unsuspecting raiders.",
        "desc_pt": "Navios mercantes camuflados ocultando canhões de 75mm atraem submarinos que emergem para o combate de superfície, afundando os incursores inimigos à queima-roupa."
    },
    {
        "id": "FRA_escadrille_des_cigognes_et_as_du_ciel",
        "x": 53, "y": 7, "cost": 8,
        "icon": "GFX_FRA_escadrille_des_cigognes_et_as_du_ciel",
        "prereq": ["FRA_chasseurs_spad_vii_et_xiii"], "mut": [],
        "reward": """add_ideas = FRA_legendary_flying_aces
add_war_support = 0.05
add_political_power = 30""",
        "title_en": "Escadrille des Cigognes (Flying Aces)",
        "title_pt": "Escadrille des Cigognes (Os Ases dos Céus)",
        "desc_en": "Pilots like Georges Guynemer, René Fonck, and Charles Nungesser of Groupe de Chasse 12 ('The Storks') become national legends, inspiring the whole nation with chivalric valor.",
        "desc_pt": "Aviadores como Georges Guynemer, René Fonck e Charles Nungesser tornam-se heróis nacionais, inspirando toda a nação com bravura lendária e combates aéreos."
    },
    {
        "id": "FRA_cooperation_air_artillerie_tsf",
        "x": 57, "y": 7, "cost": 8,
        "icon": "GFX_FRA_cooperation_air_artillerie_tsf",
        "prereq": ["FRA_optiques_aeriennes_de_precision"], "mut": [],
        "reward": """add_ideas = FRA_air_ground_tsf_radio_coordination
add_tech_bonus = { name = art_tech bonus = 1.0 uses = 1 category = artillery }""",
        "title_en": "Air-Ground Wireless Radio (TSF) Link",
        "title_pt": "Ligação Rádio TSF entre Aviação e Artilharia",
        "desc_en": "Equipping observation aircraft with wireless Morse transmitters directs artillery fire directly onto concealed German batteries within seconds of spotting.",
        "desc_pt": "Equipar aeronaves de observação com transmissores Morse de telegrafia sem fio orienta o tiro de artilharia sobre baterias alemãs camufladas em questão de segundos."
    },

    # Y = 8
    {
        "id": "FRA_tactique_des_convois_maritimes",
        "x": 47, "y": 8, "cost": 8,
        "icon": "GFX_FRA_tactique_des_convois_maritimes",
        "prereq": ["FRA_aviso_et_patrouilleurs_q_ships"], "mut": [],
        "reward": """add_ideas = FRA_escorted_maritime_convoys
add_stability = 0.04""",
        "title_en": "Mandatory Escorted Convoy System",
        "title_pt": "Sistema Obrigatório de Comboios Escoltados",
        "desc_en": "Grouping merchantmen into large convoys escorted by destroyers, armed trawlers, and flying boats reduces shipping losses by over eighty percent.",
        "desc_pt": "Reunir navios mercantes em comboios protegidos por contratorpedeiros, traineiras armadas e hidroaviões reduz as perdas navais em mais de oitenta por cento."
    },
    {
        "id": "FRA_division_aerienne_du_colonel_duval",
        "x": 55, "y": 8, "cost": 8,
        "icon": "GFX_FRA_division_aerienne_du_colonel_duval",
        "prereq": ["FRA_escadrille_des_cigognes_et_as_du_ciel", "FRA_cooperation_air_artillerie_tsf"], "mut": [],
        "reward": """add_ideas = FRA_colonel_duval_air_division
add_air_experience = 30""",
        "title_en": "Colonel Duval's Mass Air Division",
        "title_pt": "A Divisão Aérea do Coronel Duval",
        "desc_en": "Forming the world's first independent tactical air division—over 600 fighters and bombers massed under a single commander—delivers decisive aerial hammer blows wherever the enemy strikes.",
        "desc_pt": "Criar a primeira divisão aérea tática autônoma da história—mais de 600 caças e bombardeiros sob comando unificado—desfere golpes esmagadores onde quer que o inimigo ataque."
    },

    # Y = 9
    {
        "id": "FRA_controle_total_de_la_mediterranee",
        "x": 47, "y": 9, "cost": 10,
        "icon": "GFX_FRA_controle_total_de_la_mediterranee",
        "prereq": ["FRA_tactique_des_convois_maritimes"], "mut": [],
        "reward": """add_ideas = FRA_mediterranean_dominance
add_political_power = 50
add_war_support = 0.05""",
        "title_en": "Total Mediterranean Mastery",
        "title_pt": "Domínio Absoluto do Mediterrâneo",
        "desc_en": "With safe sea lanes, hundreds of thousands of African soldiers, grain shipments, and colonial supplies reach French ports uninterrupted throughout the conflict.",
        "desc_pt": "Com rotas marítimas invioláveis, centenas de milhares de combatentes africanos, trigo e suprimentos coloniais chegam aos portos da França sem qualquer interrupção."
    },
    {
        "id": "FRA_suprematie_aerienne_absolue",
        "x": 55, "y": 9, "cost": 10,
        "icon": "GFX_FRA_suprematie_aerienne_absolue",
        "prereq": ["FRA_division_aerienne_du_colonel_duval"], "mut": [],
        "reward": """add_ideas = FRA_air_supremacy_spad
add_political_power = 50
add_war_support = 0.05""",
        "title_en": "Absolute Air Supremacy Over the Front",
        "title_pt": "Supremacia Aérea Absoluta sobre o Front",
        "desc_en": "By late 1918, French squadrons dominate the skies over the Western Front, blinding German artillery while strafing retreating enemy columns across the Hindenburg Line.",
        "desc_pt": "Em 1918, as esquadrilhas francesas dominam completamente os céus do front ocidental, cegando a artilharia alemã e metralhando colunas em retirada na Linha Hindenburg."
    },

    # Side Branches for depth (Y=10..11)
    {
        "id": "FRA_chasseurs_de_nuit_et_projecteurs",
        "x": 57, "y": 10, "cost": 8,
        "icon": "GFX_FRA_chasseurs_de_nuit_et_projecteurs",
        "prereq": ["FRA_suprematie_aerienne_absolue"], "mut": [],
        "reward": """add_ideas = FRA_night_interception_patrols
add_stability = 0.03""",
        "title_en": "Night Air Interception & Searchlights",
        "title_pt": "Interceptação Noturna e Holofotes de Defesa",
        "desc_en": "Establishing rings of anti-aircraft searchlights and night-patrol fighters around Paris and Nancy shields civilian populations from German Gotha and Zeppelin bombers.",
        "desc_pt": "Anéis de holofotes antiaéreos e caças de patrulha noturna ao redor de Paris e Nancy blindam as populações civis contra bombardeiros Gotha e zepelins alemães."
    },
    {
        "id": "FRA_aviation_navale_et_porte_hydravions",
        "x": 49, "y": 10, "cost": 8,
        "icon": "GFX_FRA_aviation_navale_et_porte_hydravions",
        "prereq": ["FRA_controle_total_de_la_mediterranee"], "mut": [],
        "reward": """add_tech_bonus = { name = cv_bonus bonus = 1.0 uses = 1 category = cv_tech }
add_navy_experience = 20""",
        "title_en": "Naval Aviation & Seaplane Carriers",
        "title_pt": "Aviação Naval e Navios Porta-Hidroaviões",
        "desc_en": "Operating the seaplane carrier Foudre and coastal hydroplane stations pioneers maritime air spotting, mine detection, and torpedo air strikes.",
        "desc_pt": "Operar o navio porta-hidroaviões Foudre e estações de hidroplanos litorâneas pioneira o reconhecimento aéreo no mar, detecção de minas e ataques com torpedos."
    },
    {
        "id": "FRA_heritage_aeronautique_victorieux",
        "x": 55, "y": 11, "cost": 8,
        "icon": "GFX_FRA_heritage_aeronautique_victorieux",
        "prereq": ["FRA_suprematie_aerienne_absolue"], "mut": [],
        "reward": """add_ideas = FRA_victorious_aero_industry
add_political_power = 40""",
        "title_en": "Victorious French Aerospace Industry",
        "title_pt": "A Vitoriosa Indústria Aeroespacial Francesa",
        "desc_en": "Having produced over fifty thousand military aircraft during the war, French aerospace constructors lead the world into the era of commercial flight and national glory.",
        "desc_pt": "Tendo produzido mais de cinquenta mil aviões militares na guerra, os fabricantes aeroespaciais franceses lideram o mundo na era da aviação civil e glória nacional."
    },
    {
        "id": "FRA_flotte_de_la_victoire_1918",
        "x": 49, "y": 11, "cost": 8,
        "icon": "GFX_FRA_flotte_de_la_victoire_1918",
        "prereq": ["FRA_controle_total_de_la_mediterranee"], "mut": [],
        "reward": """add_political_power = 40
add_stability = 0.05
add_navy_experience = 25""",
        "title_en": "The Triumphant Marine Nationale",
        "title_pt": "A Triunfante Marine Nationale",
        "desc_en": "Entering the Dardanelles, Sevastopol, and Pola, the victorious French fleet stands as one of the world's foremost naval powers, decorated with steadfast naval honor.",
        "desc_pt": "Entrando nos Dardanelos, Sebastopol e Pola, a frota francesa vitoriosa consolida-se como uma das maiores potências navais do planeta, condecorada pela honra marítima."
    }
]
