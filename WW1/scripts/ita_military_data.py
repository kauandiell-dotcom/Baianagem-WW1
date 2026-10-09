"""Armed Forces data module for Italy (ITA) WW1 (Wing 4: mil, 55 focuses).

Covers:
- Army branch: General Staff reorganization, Cadorna, Alpini, mountain artillery,
  offensive doctrine vs war of position, Arditi assault troops, Diaz command,
  elastic defence vs offensive pressure, demobilization, postwar reform.
- Naval branch: Cavour and Andrea Doria battleships, Taranto & Brindisi bases,
  Otranto Barrage, Fleet in Being vs Flotilla warfare, MAS torpedo boats,
  Luigi Rizzo's raids (Premuda), human torpedoes (Mignatta), postwar review.
- Aviation branch: Battaglione Aviatori, flight schools, Caproni strategic bombers,
  Ansaldo SVA, fighter aces (Baracca's Black Horse), Douhet's strategic air theory,
  D'Annunzio's flight over Vienna, independent Regia Aeronautica foundations.
"""

WING = "mil"
WING_NAME = ("Armed Forces", "Forças Armadas")
SHORTCUT = ("ITA_ww1_shortcut_military", "Go to: Regio Esercito & Marina", "Ir para: Regio Esercito e Marinha")

# 55 Focuses of Wing mil
FOCI = {
    # Army Branch (25 focuses)
    "army_staff_reorganisation": {
        "cost": 5, "year": 1911, "available": "date > 1911.1.1",
        "effect": "remove_ideas = ITA_alpini_tradition add_ideas = ITA_ww1_general_staff_corps army_experience = 15 add_political_power = 20",
        "en_title": "Reorganise the General Staff",
        "pt_title": "Reorganizar o Estado-Maior",
        "en_desc": "Immediate effect: Reorganises staff sections under General Pollio; grants +10 army XP and General Staff idea.\n\nRestructuring operational planning, staff officer assignments, and railway mobilization schedules to modernize the Regio Esercito.",
        "pt_desc": "Efeito imediato: Reorganiza o Estado-Maior sob o General Pollio; concede +10 de XP militar e espírito Estado-Maior Geral.\n\nModerniza as seções operacionais, o corpo de oficiais e o planejamento de transporte ferroviário militar.",
        "ai": "base = 100"
    },
    "libya_lessons": {
        "cost": 5, "year": 1912, "available": "date > 1912.1.1",
        "effect": "army_experience = 10 add_tech_bonus = { name = ITA_ww1_colonial_infantry_tactics bonus = 0.25 uses = 1 category = infantry_weapons }",
        "en_title": "Lessons of the Libyan War",
        "pt_title": "Lições da Guerra da Líbia",
        "en_desc": "Immediate effect: Incorporates North African tactical lessons; grants +10 army XP and infantry weapons tech bonus (25%).\n\nAnalysing logistics, desert march discipline, and field wireless telegraphy gathered during colonial operations in Tripoli and Cyrenaica.",
        "pt_desc": "Efeito imediato: Incorpora as lições táticas da África do Norte; concede +10 de XP e bônus de pesquisa de infantaria (25%).\n\nAnalisa a logística, a marcha no deserto e o uso pioneiro de telegrafia sem fio e aviação nas operações líbias.",
        "ai": "base = 80"
    },
    "cadorna_chief_of_staff": {
        "cost": 5, "year": 1914, "available": "date > 1914.7.1",
        "effect": "remove_ideas = ITA_ww1_general_staff_corps add_ideas = ITA_ww1_cadorna_discipline army_experience = 15 add_to_variable = { ita_ww1_army_morale = -5 } ita_ww1_clamp_counters = yes",
        "en_title": "Cadorna Takes the Staff",
        "pt_title": "Cadorna Assume o Estado-Maior",
        "en_desc": "Immediate effect: General Luigi Cadorna becomes Chief of Staff; imposes rigid offensive discipline (+15 army XP).\n\nLuigi Cadorna imposes unbending central control over division commanders, preparing strict offensive plans aimed directly toward Ljubljana and Vienna.",
        "pt_desc": "Efeito imediato: O General Luigi Cadorna assume o comando; impõe férrea disciplina ofensiva (+15 de XP militar).\n\nLuigi Cadorna centraliza as operações militares e estrutura planos de ataque frontais voltados à conquista de Liubliana e Viena.",
        "ai": "base = 90"
    },
    "alpini_expansion": {
        "cost": 5, "year": 1911, "available": "date > 1911.3.1",
        "effect": "army_experience = 10 add_tech_bonus = { name = ITA_ww1_alpini_mountaineers bonus = 0.25 uses = 1 category = special_forces }",
        "en_title": "Expand the Alpini",
        "pt_title": "Expandir os Alpini",
        "en_desc": "Immediate effect: Expands the legendary Alpini mountain regiments; +10 army XP and special forces tech bonus (25%).\n\nRecruiting sturdy mountaineers from the Alpine valleys into autonomous ski battalions trained to fight amidst snow, ice, and dolomite crags.",
        "pt_desc": "Efeito imediato: Expande os históricos regimentos de Alpini; +10 de XP e bônus de forças especiais (25%).\n\nRecrutamento de camponeses dos vales alpinos em batalhões de esquiadores treinados para o combate nas geleiras e rochas.",
        "ai": "base = 85"
    },
    "artillery_modernisation": {
        "cost": 5, "year": 1912, "available": "date > 1912.1.1",
        "effect": "162 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 10 add_tech_bonus = { name = ITA_ww1_field_artillery_program bonus = 0.25 uses = 1 category = artillery }",
        "en_title": "Artillery Modernisation",
        "pt_title": "Modernização da Artilharia",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Terni (Tuscany), grants +10 army XP and 25% artillery tech bonus.\n\nReplacing obsolete bronze cannons with quick-firing 75/27 Modello 1906 field guns equipped with modern recoil cylinders.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar em Terni (Toscana), concede +10 de XP e bônus de artilharia (25%).\n\nSubstitui peças obsoletas por modernos canhões de campanha com freio de recuo hidráulico para apoiar a infantaria.",
        "ai": "base = 80"
    },
    "mountain_artillery": {
        "cost": 5, "year": 1913, "available": "date > 1913.1.1",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 15 add_tech_bonus = { name = ITA_ww1_mountain_artillery bonus = 0.25 uses = 1 category = artillery } add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 60 producer = ITA }",
        "en_title": "Mountain Artillery",
        "pt_title": "Artilharia de Montanha",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Piedmont (Turin), adds Mountain Howitzers idea and +10 army XP.\n\nMule-carried 65/17 mountain guns can be dismantled into pack loads and carried up sheer dolomite precipices to support Alpini assaults.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar no Piemonte (Turim), concede o espírito Obuseiros de Montanha e +10 de XP.\n\nCanhões desmontáveis conduzidos por muares sobem desfiladeiros íngremes para prestar apoio de fogo imediato aos Alpini.",
        "ai": "base = 75"
    },
    "heavy_guns": {
        "cost": 5, "year": 1914, "available": "date > 1914.1.1",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 10 add_tech_bonus = { name = ITA_ww1_siege_howitzers bonus = 0.25 uses = 1 category = artillery }",
        "en_title": "Heavy Guns",
        "pt_title": "Canhões Pesados",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Genoa (Ansaldo), grants +10 army XP and 25% artillery bonus.\n\nRealising that mountain forts and concrete caves require heavy ordnance to crack, the artillery directorate orders heavy siege batteries.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar em Gênova (Ansaldo), concede +10 de XP e bônus de artilharia (25%).\n\nReconhecendo que fortalezas de montanha e casamatas exigem calibres pesados, o exército encomenda baterias pesadas de cerco.",
        "ai": "base = 75"
    },
    "machine_guns": {
        "cost": 5, "year": 1914, "available": "date > 1914.6.1",
        "effect": "159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 10 add_tech_bonus = { name = ITA_ww1_fiat_revelli_gun bonus = 0.25 uses = 1 category = infantry_weapons }",
        "en_title": "Machine-Gun Companies",
        "pt_title": "Companhias de Metralhadoras",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Lombardy (Brescia), grants +10 army XP and 25% infantry weapons tech bonus.\n\nEquipping every infantry regiment with dedicated automatic fire sections to lay defensive swathes across barbed-wire perimeters.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar na Lombardia (Brescia), concede +10 de XP e bônus de armas de infantaria (25%).\n\nCria companhias autônomas de metralhadoras em cada regimento de infantaria para cobrir arames farpados com fogo contínuo.",
        "ai": "base = 80"
    },
    "north_east_mobilisation": {
        "cost": 5, "year": 1914, "available": "date > 1914.8.1",
        "effect": "160 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } } 736 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } } army_experience = 20 add_political_power = 30 add_command_power = 25",
        "en_title": "The North-East Mobilisation Plan",
        "pt_title": "O Plano de Mobilização do Nordeste",
        "en_desc": "Immediate effect: Completes railway timetables concentrating the Regio Esercito on the Venetian plain (+15 army XP).\n\nOrganising seventy-two trains per day across the Po Valley to marshal four field armies on the Austrian border in under twenty days.",
        "pt_desc": "Efeito imediato: Conclui a malha ferroviária de mobilização para concentrar os exércitos na planície vêneta (+15 de XP).\n\nCoordena dezenas de composições diárias pelo vale do Pó para concentrar quatro exércitos de campanha na fronteira em vinte dias.",
        "ai": "base = 85"
    },
    "frontier_fortifications": {
        "cost": 5, "year": 1914, "available": "date > 1914.9.1",
        "effect": "160 = { add_building_construction = { type = bunker level = 2 instant_build = yes } } 158 = { add_building_construction = { type = bunker level = 2 instant_build = yes } } army_experience = 15 add_tech_bonus = { name = ITA_ww1_alpine_fortifications bonus = 0.25 uses = 1 category = engineering }",
        "en_title": "Frontier Fortifications",
        "pt_title": "Fortificações Fronteiriças",
        "en_desc": "Immediate effect: Builds 2 land forts in Veneto (Asiago) and 1 in Piedmont, adds Alpine Fortresses idea and +10 army XP.\n\nArming armored fortress complexes (Forte Verena, Forte Campomolon) with rotating steel cupolas to dominate alpine valleys.",
        "pt_desc": "Efeito imediato: Constrói 2 fortes terrestres no Vêneto (Asiago) e 1 no Piemonte, concede Fortalezas Blindadas Alpinas e +10 de XP.\n\nEquipa fortalezas blindadas (Forte Verena e Campomolon) com cúpulas giratórias de aço para fechar os desfiladeiros alpinos.",
        "ai": "base = 70"
    },
    "offensive_doctrine": {
        "cost": 5, "year": 1915, "available": "date > 1915.1.1",
        "effect": "remove_ideas = ITA_ww1_cadorna_discipline army_experience = 15 add_ideas = ITA_ww1_cadornian_offensive_cult add_to_variable = { ita_ww1_army_morale = 5 }",
        "en_title": "The Offensive Doctrine",
        "pt_title": "A Doutrina Ofensiva",
        "en_desc": "Immediate effect: Replaces Cadornian Discipline with Cult of the Offensive (+15 army XP, +5 morale).\n\nThe General Staff's official tactical doctrine insists that sheer moral willpower and infantry bayonets will overcome enemy machine guns.",
        "pt_desc": "Efeito imediato: Substitui a Disciplina de Cadorna pelo Culto da Ofensiva (+15 de XP, +5 moral).\n\nA doutrina oficial sustenta que a força moral e a baioneta do infante prevalecerão sobre as metralhadoras inimigas.",
        "ai": "base = 70"
    },
    "war_of_position": {
        "cost": 5, "year": 1915, "available": "date > 1915.1.1",
        "effect": "remove_ideas = ITA_ww1_cadorna_discipline army_experience = 15 add_ideas = ITA_ww1_methodical_firepower_doctrine add_to_variable = { ita_ww1_army_morale = 5 }",
        "en_title": "The War of Position",
        "pt_title": "A Guerra de Posição",
        "en_desc": "Immediate effect: Replaces Cadornian Discipline with Methodical Firepower Doctrine (+15 army XP, +5 morale).\n\nRejecting reckless bayonet charges, this doctrine mandates methodical artillery destruction before committing infantry to the assault.",
        "pt_desc": "Efeito imediato: Substitui a Disciplina de Cadorna pela Doutrina Metódica de Fogo (+15 de XP, +5 moral).\n\nRejeitando cargas frontais desprotegidas, prioriza a destruição metódica dos obstáculos por artilharia pesada antes do avanço.",
        "ai": "base = 30"
    },
    "trench_mortars": {
        "cost": 5, "year": 1915, "available": "date > 1915.6.1",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 10 add_tech_bonus = { name = ITA_ww1_bombarda_trench_mortar bonus = 0.25 uses = 1 category = artillery }",
        "en_title": "Trench Mortars",
        "pt_title": "Morteiros de Trincheira",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Piedmont, grants +10 army XP and 25% artillery tech bonus.\n\nShort-range mortars lobbing heavy charges of high explosive lobbed directly into enemy trenches clear barbed-wire mazes on the Carso.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar no Piemonte, concede +10 de XP e bônus de artilharia (25%).\n\nMorteiros de tiro curvo lançam cargas pesadas de alto explosivo diretamente sobre as linhas inimigas nas rochas do Carso.",
        "ai": "base = 80"
    },
    "gas_defence": {
        "cost": 5, "year": 1916, "available": "date > 1916.1.1",
        "effect": "army_experience = 15 add_tech_bonus = { name = ITA_ww1_chemical_defence bonus = 0.25 uses = 1 category = support_tech } add_equipment_to_stockpile = { type = support_equipment_1 amount = 100 producer = ITA } add_to_variable = { ita_ww1_army_morale = 5 } ita_ww1_clamp_counters = yes",
        "en_title": "Gas Defence",
        "pt_title": "Defesa contra Gases",
        "en_desc": "Immediate effect: Issues British-designed box respirators and Polyvalent masks to frontline divisions (+10 army XP).\n\nFollowing deadly Austrian chemical gas attacks on Mount San Michele, the army distributes effective respirators and decontamination gear.",
        "pt_desc": "Efeito imediato: Distribui máscaras de caixa e respiradores polivalentes a todas as divisões do front (+10 de XP militar).\n\nApós o mortal ataque de gás austríaco no Monte San Michele, o exército equipa a infantaria com máscaras protetoras eficazes.",
        "ai": "base = 80"
    },
    "reserve_officer_schools": {
        "cost": 5, "year": 1916, "available": "date > 1916.6.1",
        "effect": "161 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 25 add_command_power = 30 add_political_power = 30",
        "en_title": "Reserve Officer Schools",
        "pt_title": "Escolas de Oficiais da Reserva",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Emilia-Romagna (Modena), grants +15 army XP, +20 PP and Reserve Sublieutenants idea.\n\nRapid training schools at Modena and Parma supply tens of thousands of enthusiastic junior officers to lead frontline platoons.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar na Emília-Romanha (Módena), concede +15 de XP, +20 PP e o espírito Oficiais de Complemento.\n\nCursos rápidos em Módena e Parma preparam oficiais subalternos para liderar pelotões na linha de frente.",
        "ai": "base = 75"
    },
    "dismounted_cavalry": {
        "cost": 5, "year": 1916, "available": "date > 1916.3.1",
        "effect": "army_experience = 20 add_equipment_to_stockpile = { type = infantry_equipment_0 amount = 1500 producer = ITA } add_tech_bonus = { name = ITA_ww1_cavalry_recon bonus = 0.25 uses = 1 category = recon_tech }",
        "en_title": "Dismounted Cavalry",
        "pt_title": "Cavalaria Desmontada",
        "en_desc": "Immediate effect: Dismounts elite cavalry regiments to serve as heavy trench assault infantry (+10 army XP).\n\nPrestigious regiments like Genova Cavalleria and Lancieri di Novara fight dismounted on the Carso with carbines and bayonets.",
        "pt_desc": "Efeito imediato: Desmonta regimentos clássicos de cavalaria para reforçar a infantaria de trincheira (+10 de XP militar).\n\nRegimentos de tradição como Genova Cavalleria lutam a pé no Carso com carabinas e baionetas como infantaria pesada.",
        "ai": "base = 65"
    },
    "assault_units": {
        "cost": 5, "year": 1917, "available": "date > 1917.7.1",
        "effect": "159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 25 add_tech_bonus = { name = ITA_ww1_arditi_assault_tactics bonus = 0.25 uses = 1 category = special_forces } add_equipment_to_stockpile = { type = support_equipment_1 amount = 50 producer = ITA }",
        "en_title": "Assault Units",
        "pt_title": "Unidades de Assalto (Arditi)",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Lombardy, grants Arditi Stormtrooper idea, +20 army XP and special forces tech bonus (25%).\n\nArmed with daggers, Thevenot hand grenades, and Villar Perosa submachine guns, black-flamed Arditi stormtroops spearhead trench assaults.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar na Lombardia, concede o espírito Arditi, +20 de XP e bônus de forças especiais (25%).\n\nArmados com punhais, granadas Thevenot e pistolas-metralhadoras Villar Perosa, os Arditi rompem as defesas inimigas com audácia.",
        "ai": "base = 95"
    },
    "diaz_takes_command": {
        "cost": 5, "year": 1917, "available": "date > 1917.11.9",
        "effect": "remove_ideas = ITA_ww1_cadornian_offensive_cult remove_ideas = ITA_ww1_methodical_firepower_doctrine army_experience = 15 add_ideas = ITA_ww1_diaz_humane_leadership add_to_variable = { ita_ww1_army_morale = 15 }",
        "en_title": "Diaz Takes Command",
        "pt_title": "Diaz Assume o Comando",
        "en_desc": "Immediate effect: General Armando Diaz replaces Cadorna; removes offensive cult, boosts army morale by +15 and grants Humane Leadership idea.\n\nArmando Diaz abolishes summary decimation executions, improves soldier rations, grants regular home leave, and prioritises defensive preservation of lives.",
        "pt_desc": "Efeito imediato: Armando Diaz substitui Cadorna; remove o culto ofensivo, eleva o moral em +15 e concede o espírito Liderança Humanitária.\n\nArmando Diaz abole execuções sumárias, melhora a alimentação dos soldados, institui licenças regulares e prioriza poupar vidas.",
        "ai": "base = 98"
    },
    "elastic_defence": {
        "cost": 5, "year": 1917, "available": "has_completed_focus = ITA_ww1_diaz_takes_command",
        "effect": "remove_ideas = ITA_ww1_diaz_humane_leadership army_experience = 15 add_ideas = ITA_ww1_defence_in_depth_piave add_to_variable = { ita_ww1_army_morale = 5 }",
        "en_title": "Elastic Defence",
        "pt_title": "Defesa Elástica",
        "en_desc": "Immediate effect: Evolves command doctrine into Defense in Depth on the Piave (+15 army XP, +5 morale).\n\nReplacing rigid trench lines with layered outpost zones, machine-gun nests, and pre-sighted artillery killing zones on the Montello.",
        "pt_desc": "Efeito imediato: Evolui a liderança para a Defesa em Profundidade no Piave (+15 de XP, +5 moral).\n\nSubstitui linhas rígidas por zonas de postos avançados e bolsas de fogo de artilharia pré-reguladas nas encostas do Montello.",
        "ai": "base = 80"
    },
    "offensive_pressure": {
        "cost": 5, "year": 1918, "available": "has_completed_focus = ITA_ww1_diaz_takes_command",
        "effect": "remove_ideas = ITA_ww1_diaz_humane_leadership army_experience = 15 add_ideas = ITA_ww1_continuous_offensive_pressure add_to_variable = { ita_ww1_army_morale = 5 }",
        "en_title": "Sustained Offensive Pressure",
        "pt_title": "Pressão Ofensiva Sustentada",
        "en_desc": "Immediate effect: Replaces defensive posture with Aggressive River Probing (+15 army XP, +5 morale).\n\nMaintaining constant raids across river sandbars to keep the Austro-Hungarian command under perpetual tension and force early deployment of reserves.",
        "pt_desc": "Efeito imediato: Substitui a postura defensiva pela Pressão Contínua nas Margens (+15 de XP, +5 moral).\n\nAtaques localizados nos bancos de areia do rio mantêm o comando imperial sob tensão constante, forçando o esgotamento precoce de reservas.",
        "ai": "base = 20"
    },
    "motor_transport": {
        "cost": 5, "year": 1917, "available": "date > 1917.1.1",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } army_experience = 10 add_tech_bonus = { name = ITA_ww1_fiat_lorry_transport bonus = 0.25 uses = 1 category = motorized_equipment }",
        "en_title": "Motor Transport Corps",
        "pt_title": "Corpo de Transporte Motorizado",
        "en_desc": "Immediate effect: Constructs 1 arms factory in Piedmont (FIAT lorries), grants +10 army XP and 25% motorized tech bonus.\n\nAutomotive convoys supply mountain armies with munitions, moving entire divisions between Trentino and Piave within forty-eight hours.",
        "pt_desc": "Efeito imediato: Constrói 1 fábrica militar no Piemonte (caminhões FIAT), concede +10 de XP e bônus de motorizados (25%).\n\nColunas automobilísticas abastecem os exércitos alpinos e deslocam divisões inteiras entre o Trentino e o Piave em dois dias.",
        "ai": "base = 75"
    },
    "army_demobilisation": {
        "cost": 5, "year": 1919, "available": "has_war = no date > 1919.1.1",
        "effect": "remove_ideas = ITA_ww1_defence_in_depth_piave remove_ideas = ITA_ww1_continuous_offensive_pressure add_political_power = 40 add_to_variable = { ita_ww1_social_tension = -10 }",
        "en_title": "Army Demobilisation",
        "pt_title": "Desmobilização do Exército",
        "en_desc": "Immediate effect: Removes wartime frontline combat doctrines, returns soldiers to civilian life (+40 PP, -10 social tension).\n\nReturning soldiers to farming and industrial workshops while avoiding runaway postwar unemployment through phased release schedules.",
        "pt_desc": "Efeito imediato: Remove as doutrinas de combate de trincheira da guerra, devolve soldados à vida civil (+40 PP, -10 tensão social).\n\nReintegra os soldados às lavouras e oficinas fabris de forma escalonada para evitar o desemprego em massa.",
        "ai": "base = 80"
    },
    "carabinieri_reinforcement": {
        "cost": 5, "year": 1919, "available": "date > 1919.6.1",
        "effect": "add_to_variable = { ita_ww1_social_tension = -10 } add_political_power = 40 add_stability = 0.02 ita_ww1_clamp_counters = yes",
        "en_title": "Reinforce the Carabinieri",
        "pt_title": "Reforçar os Carabinieri",
        "en_desc": "Immediate effect: Expands the Arma dei Carabinieri to police rural and urban unrest (+3% stability).\n\nStrengthening mobile legions of the royal gendarmerie to maintain public order amid postwar strike waves and ideological clashes.",
        "pt_desc": "Efeito imediato: Expande a Arma dei Carabinieri para policiar a ordem pública (+3% de estabilidade).\n\nFortalece as legiões móveis da gendarmaria real para resguardar a ordem pública durante as greves e confrontos políticos do pós-guerra.",
        "ai": "base = 75"
    },
    "postwar_army_reform": {
        "cost": 5, "year": 1920, "available": "date > 1920.1.1",
        "effect": "remove_ideas = ITA_alpini_tradition add_ideas = ITA_ww1_badoglio_standing_army army_experience = 20 add_political_power = 30",
        "en_title": "Postwar Army Reform",
        "pt_title": "Reforma do Exército no Pós-Guerra",
        "en_desc": "Immediate effect: General Badoglio reorganises the peacetime standing army into thirty modern divisions (+15 army XP).\n\nModernising artillery arsenals, retaining assault unit doctrines, and creating unified corps commands across the northern frontiers.",
        "pt_desc": "Efeito imediato: O General Badoglio reorganiza o exército permanente de paz em trinta divisões modernas (+15 de XP militar).\n\nModerniza o parque de artilharia, absorve a experiência tática dos Arditi e unifica os comandos de corpo de exército na fronteira.",
        "ai": "base = 70"
    },
    "army_budget_cuts": {
        "cost": 5, "year": 1922, "available": "date > 1922.1.1",
        "effect": "remove_ideas = ITA_ww1_badoglio_standing_army add_political_power = 50 add_ideas = ITA_ww1_peacetime_military_economy",
        "en_title": "Army Budget Cuts",
        "pt_title": "Cortes no Orçamento Militar",
        "en_desc": "Immediate effect: Replaces standing army expansion with Peacetime Fiscal Realism (+50 political power).\n\nRestricting annual conscription terms and mothballing heavy ordnance to rescue the national budget from catastrophic debt burdens.",
        "pt_desc": "Efeito imediato: Substitui a manutenção do exército pelo Realismo Fiscal em Tempo de Paz (+50 poder político).\n\nDiminui o tempo de serviço militar obrigatório e preserva material em depósito para sanear o orçamento nacional.",
        "ai": "base = 60"
    },

    # Naval Branch (18 focuses)
    "naval_estimates": {
        "cost": 5, "year": 1911, "available": "date > 1911.1.1",
        "effect": "remove_ideas = ITA_terre_irredente_dream add_ideas = ITA_ww1_regia_marina_cadres navy_experience = 15 add_political_power = 20",
        "en_title": "The Naval Estimates",
        "pt_title": "As Previsões Navais",
        "en_desc": "Immediate effect: Approves the 1911 naval estimates; grants +10 navy XP and Regia Marina Cadres idea.\n\nAdmiral Bettolo and the naval ministry secure parliament's blessing for long-term construction programmes to match Austro-Hungarian naval expansion.",
        "pt_desc": "Efeito imediato: Aprova o orçamento naval de 1911; concede +10 de XP naval e espírito Quadros da Regia Marina.\n\nO Almirante Bettolo e o ministério da marinha obtêm dotações plurianuais para competir com o rearmamento naval austríaco.",
        "ai": "base = 90"
    },
    "cavour_class": {
        "cost": 5, "year": 1911, "available": "date > 1911.6.1",
        "effect": "navy_experience = 15 add_tech_bonus = { name = ITA_ww1_dreadnought_armour bonus = 0.25 uses = 1 category = heavy_armor }",
        "en_title": "The Cavour-Class Battleships",
        "pt_title": "Os Encouraçados Classe Cavour",
        "en_desc": "Immediate effect: Lays down dreadnoughts Conte di Cavour, Giulio Cesare, and Leonardo da Vinci (+15 navy XP).\n\nArmed with thirteen 305mm guns arranged in innovative triple and twin center-line turrets, these dreadnoughts form the pride of the battle fleet.",
        "pt_desc": "Efeito imediato: Inicia a construção dos encouraçados Conte di Cavour, Giulio Cesare e Leonardo da Vinci (+15 de XP naval).\n\nArmados com treze canhões de 305mm em torres duplas e triplas centrais, formam a espinha dorsal da frota de batalha.",
        "ai": "base = 85"
    },
    "andrea_doria_class": {
        "cost": 5, "year": 1912, "available": "date > 1912.1.1",
        "effect": "navy_experience = 15 add_tech_bonus = { name = ITA_ww1_doria_battleship_design bonus = 0.25 uses = 1 category = naval_equipment }",
        "en_title": "The Andrea Doria Class",
        "pt_title": "A Classe Andrea Doria",
        "en_desc": "Immediate effect: Constructs super-dreadnoughts Andrea Doria and Caio Duilio (+15 navy XP).\n\nRefining armor layout, deck protection, and secondary battery barbettes to withstand heavy Austro-Hungarian naval shells.",
        "pt_desc": "Efeito imediato: Constrói os superencouraçados Andrea Doria e Caio Duilio (+15 de XP naval).\n\nAprimora a blindagem de convés e as baterias secundárias contra os projéteis pesados da marinha austro-húngara.",
        "ai": "base = 80"
    },
    "fast_cruisers": {
        "cost": 5, "year": 1912, "available": "date > 1912.4.1",
        "effect": "navy_experience = 10 add_tech_bonus = { name = ITA_ww1_scout_cruisers bonus = 0.25 uses = 1 category = cl_tech }",
        "en_title": "Fast Scout Cruisers",
        "pt_title": "Cruzadores Ligeiros de Reconhecimento",
        "en_desc": "Immediate effect: Builds fast light cruisers Nino Bixio and Marsala; light cruiser tech bonus (25%).\n\nHigh-speed scouts capable of 27 knots to locate enemy sorties in the narrow waters of the Adriatic Sea.",
        "pt_desc": "Efeito imediato: Constrói cruzadores ligeiros velozes Nino Bixio e Marsala; bônus de cruzadores (25%).\n\nNavios rápidos capazes de atingir 27 nós para localizar esquadras inimigas nas águas estreitas do Adriático.",
        "ai": "base = 75"
    },
    "taranto_base": {
        "cost": 5, "year": 1913, "available": "date > 1913.1.1",
        "effect": "157 = { add_building_construction = { type = naval_base level = 2 instant_build = yes } add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } } navy_experience = 20 add_political_power = 30 add_tech_bonus = { name = ITA_ww1_naval_repair bonus = 0.25 uses = 1 category = naval_equipment }",
        "en_title": "The Taranto Base",
        "pt_title": "A Base de Taranto",
        "en_desc": "Immediate effect: Expands Taranto naval base (+2 naval base, +1 coastal fort in Apulia), adds Taranto Arsenal idea and +10 navy XP.\n\nDredging navigation channels, building dry docks, and erecting coastal battery fortifications to shelter the primary battle fleet.",
        "pt_desc": "Efeito imediato: Expande a base naval de Taranto (+2 base naval, +1 forte costeiro na Apúlia), concede Arsenal de Taranto e +10 de XP.\n\nDragagem de canais, construção de docas secas e baterias costeiras fortificadas no Mar Piccolo e Mar Grande.",
        "ai": "base = 80"
    },
    "brindisi_venice_bases": {
        "cost": 5, "year": 1913, "available": "date > 1913.6.1",
        "effect": "160 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant_build = yes } } 157 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } } navy_experience = 20 add_tech_bonus = { name = ITA_ww1_submarine_detection bonus = 0.25 uses = 1 category = dd_tech }",
        "en_title": "Brindisi and Venice",
        "pt_title": "Brindisi e Veneza",
        "en_desc": "Immediate effect: Constructs 1 dockyard in Veneto (Venetian Arsenal), adds Adriatic Naval Stations idea and +10 navy XP.\n\nPositioning fast flotillas and submarine pens at Brindisi to interdict the Otranto straits and at Venice to guard the northern lagoons.",
        "pt_desc": "Efeito imediato: Constrói 1 estaleiro no Vêneto (Arsenal de Veneza), concede Estações Navais do Adriático e +10 de XP naval.\n\nPosiciona flotilhas velozes e bases de submarinos em Brindisi para vigiar o estreito de Otranto e em Veneza para cobrir as lagoas.",
        "ai": "base = 75"
    },
    "submarine_programme": {
        "cost": 5, "year": 1913, "available": "date > 1913.3.1",
        "effect": "navy_experience = 10 add_tech_bonus = { name = ITA_ww1_laurenti_submarines bonus = 0.25 uses = 1 category = ss_tech }",
        "en_title": "The Submarine Programme",
        "pt_title": "O Programa de Submarinos",
        "en_desc": "Immediate effect: Adopts engineer Cesare Laurenti's double-hull submarine designs; submarine tech bonus (25%).\n\nBuilding coastal submarines (Medusa and Nautilus classes) possessing superior submerged stability and reserve buoyancy for Mediterranean operations.",
        "pt_desc": "Efeito imediato: Adota os submarinos de duplo casco do engenheiro Cesare Laurenti; bônus de submarinos (25%).\n\nConstrução de submarinos costeiros com elevada estabilidade submersa para patrulhar as rotas mediterrâneas.",
        "ai": "base = 80"
    },
    "torpedo_boats": {
        "cost": 5, "year": 1913, "available": "date > 1913.8.1",
        "effect": "navy_experience = 10 add_tech_bonus = { name = ITA_ww1_torpedo_destroyers bonus = 0.25 uses = 1 category = dd_tech }",
        "en_title": "Torpedo Boat Flotillas",
        "pt_title": "Flotilhas de Torpedeiros",
        "en_desc": "Immediate effect: Builds 3PN and Indomito-class high-speed torpedo destroyers; destroyer tech bonus (25%).\n\nFast, heavily armed flotilla craft capable of laying minefields and launching night torpedo attacks against Austrian capital ships.",
        "pt_desc": "Efeito imediato: Constrói contratorpedeiros torpedeiros velozes das classes 3PN e Indomito; bônus de contratorpedeiros (25%).\n\nEmbarcações velozes aptas a semear campos de minas e desferir ataques noturnos de torpedos contra navios austríacos.",
        "ai": "base = 75"
    },
    "adriatic_watch": {
        "cost": 5, "year": 1914, "available": "date > 1914.8.1",
        "effect": "navy_experience = 25 add_to_variable = { ita_ww1_irredentism = 5 } add_tech_bonus = { name = ITA_ww1_patrol_doctrine bonus = 0.25 uses = 1 category = naval_doctrine } ita_ww1_clamp_counters = yes",
        "en_title": "The Adriatic Watch",
        "pt_title": "A Vigilância do Adriático",
        "en_desc": "Immediate effect: Deploys permanent surface patrols and sea mine barriers along the Italian east coast (+15 navy XP).\n\nGuarding the exposed Italian coastline against Austro-Hungarian shore bombardments from Pola and Cattaro.",
        "pt_desc": "Efeito imediato: Estabelece patrulhas permanentes e barreiras de minas ao longo do litoral oriental (+15 de XP naval).\n\nProtege as cidades costeiras indefesas contra bombardeios navais austro-húngaros lançados a partir de Pola e Cattaro.",
        "ai": "base = 80"
    },
    "otranto_barrage": {
        "cost": 5, "year": 1915, "available": "date > 1915.6.1",
        "effect": "navy_experience = 25 add_tech_bonus = { name = ITA_ww1_asw_barrage bonus = 0.25 uses = 1 category = naval_doctrine } add_political_power = 25",
        "en_title": "The Otranto Barrage",
        "pt_title": "A Barragem de Otranto",
        "en_desc": "Immediate effect: Installs submarine net barriers, hydrophones, and armed drifters across the Strait of Otranto.\n\nCooperating with British drifter trawlers, the barrage bottles up German and Austrian U-boats inside the Adriatic, preventing free egress into the Mediterranean.",
        "pt_desc": "Efeito imediato: Instala redes antissubmarino, hidrofones e traineiras armadas no Estreito de Otranto.\n\nBloqueia a saída de submarinos alemães e austríacos para o Mediterrâneo central, protegendo os comboios aliados.",
        "ai": "base = 85"
    },
    "battleship_fleet_in_being": {
        "cost": 5, "year": 1915, "available": "has_war = yes",
        "effect": "remove_ideas = ITA_ww1_regia_marina_cadres add_ideas = ITA_ww1_dreadnought_fleet_in_being navy_experience = 20 add_political_power = 25",
        "en_title": "Fleet in Being",
        "pt_title": "Esquadra em Potência",
        "en_desc": "Immediate effect: Preserves the primary dreadnought squadrons intact at Taranto (+15 navy XP, +25 PP).\n\nAdmiral Thaon di Revel's doctrine avoids risking irreplaceable battleships against mines and submarines, pinning down the enemy through menacing potential power.",
        "pt_desc": "Efeito imediato: Preserva a frota principal de encouraçados intacta em Taranto (+15 de XP naval, +25 de PP).\n\nO Almirante Thaon di Revel evita expor os encouraçados a minas e submarinos, imobilizando o inimigo pela ameaça latente de poder de fogo.",
        "ai": "base = 70"
    },
    "flotilla_warfare": {
        "cost": 5, "year": 1915, "available": "has_war = yes",
        "effect": "remove_ideas = ITA_ww1_regia_marina_cadres add_ideas = ITA_ww1_insidious_flotilla_doctrine navy_experience = 20 add_tech_bonus = { name = ITA_ww1_light_forces bonus = 0.25 uses = 1 category = naval_doctrine }",
        "en_title": "Flotilla Warfare",
        "pt_title": "Guerra de Flotilhas",
        "en_desc": "Immediate effect: Focuses resources on light craft, submarines, and stealth torpedo boats (+15 navy XP).\n\nRejecting conventional line-of-battle clashes, Italy wages an insidious, aggressive war of ambushes in Dalmatian island channels.",
        "pt_desc": "Efeito imediato: Concentra recursos em flotilhas ligeiras, submarinos e ataques furtivos de torpedos (+15 de XP naval).\n\nSubstitui grandes batalhas navais por uma guerra agressiva de emboscadas nos canais e arquipélagos dálmatas.",
        "ai": "base = 30"
    },
    "mas_boats": {
        "cost": 5, "year": 1915, "available": "date > 1915.9.1",
        "effect": "navy_experience = 25 add_tech_bonus = { name = ITA_ww1_mas_boat_doctrine bonus = 0.25 uses = 1 category = naval_doctrine } add_political_power = 25",
        "en_title": "The MAS Boats",
        "pt_title": "As Lanchas MAS",
        "en_desc": "Immediate effect: Builds Motobarca Armata SVAN (MAS) motor torpedo boats; naval doctrine bonus (25%).\n\nHigh-speed wooden motorboats armed with two torpedoes slip silently past harbor boom defenses, immortalized by D'Annunzio's motto 'Memento Audere Semper'.",
        "pt_desc": "Efeito imediato: Constrói as lanchas torpedeiras a motor MAS; bônus de doutrina naval (25%).\n\nEmbarcações velozes de madeira armadas com torpedos penetram furtivamente nas bases austríacas, imortalizadas pelo lema 'Memento Audere Semper'.",
        "ai": "base = 90"
    },
    "adriatic_convoys": {
        "cost": 5, "year": 1916, "available": "date > 1916.1.1",
        "effect": "navy_experience = 20 add_equipment_to_stockpile = { type = convoy_1 amount = 30 producer = ITA } add_political_power = 25",
        "en_title": "Adriatic Convoys",
        "pt_title": "Comboios do Adriático",
        "en_desc": "Immediate effect: Safeguards transport convoys sustaining Italian garrisons in Albania and the Aegean (+10 navy XP).\n\nMoving over two hundred thousand Italian and Serbian soldiers across the Adriatic without losing a single major troopship.",
        "pt_desc": "Efeito imediato: Protege comboios de transporte para as guarnições na Albânia e no Mar Egeu (+10 de XP naval).\n\nTransporta mais de duzentos mil soldados italianos e sérvios pelo mar sem a perda de um único navio de transporte de tropas.",
        "ai": "base = 75"
    },
    "anti_submarine_patrols": {
        "cost": 5, "year": 1917, "available": "date > 1917.1.1",
        "effect": "navy_experience = 15 add_tech_bonus = { name = ITA_ww1_depth_charges bonus = 0.25 uses = 1 category = naval_equipment }",
        "en_title": "Anti-Submarine Patrols",
        "pt_title": "Patrulhas Antissubmarino",
        "en_desc": "Immediate effect: Deploys depth charges, flying boats, and towed hydrophones (+15 navy XP).\n\nOrganizing integrated hunter-killer groups combining naval aircraft and fast sub-chasers to hunt Habsburg submarines.",
        "pt_desc": "Efeito imediato: Emprega cargas de profundidade, hidroaviões e hidrofones de reboque (+15 de XP naval).\n\nCombina patrulha aérea marítima e caça-submarinos velozes para neutralizar os submarinos inimigos no Adriático.",
        "ai": "base = 80"
    },
    "human_torpedoes": {
        "cost": 5, "year": 1918, "available": "date > 1918.6.1",
        "effect": "navy_experience = 30 add_tech_bonus = { name = ITA_ww1_mignatta_special_ops bonus = 0.25 uses = 1 category = naval_doctrine } add_political_power = 30",
        "en_title": "The Human Torpedoes",
        "pt_title": "Os Torpedos Humanos (Mignatta)",
        "en_desc": "Immediate effect: Special operations assault swimmers Paolucci and Rossetti sink the Austrian flagship Viribus Unitis at Pola (+20 navy XP).\n\nInventing the Mignatta steerable torpedo, daring naval divers infiltrate heavily mined enemy anchorages to attach limpet mines to enemy hulls.",
        "pt_desc": "Efeito imediato: Os mergulhadores Paolucci e Rossetti afundam o navio-almirante austríaco Viribus Unitis em Pola (+20 de XP naval).\n\nCom o torpedo tripulado Mignatta, mergulhadores de combate penetram na base de Pola e afundam o grande encouraçado inimigo.",
        "ai": "base = 85"
    },
    "postwar_fleet_review": {
        "cost": 5, "year": 1919, "available": "has_war = no date > 1919.1.1",
        "effect": "navy_experience = 15 add_political_power = 40",
        "en_title": "The Postwar Fleet Review",
        "pt_title": "A Revista da Esquadra no Pós-Guerra",
        "en_desc": "Immediate effect: Victorious fleet review off Venice celebrated by the King (+40 PP, +3% stability).\n\nThe dreadnoughts, scout cruisers, and decorated MAS flotillas assemble in the Venetian lagoon to celebrate total mastery of the Adriatic.",
        "pt_desc": "Efeito imediato: Revista naval vitoriosa em Veneza celebrada com o Rei (+40 de PP, +3% de estabilidade).\n\nEncouraçados, cruzadores e as célebres flotilhas MAS desfilam na lagoa de Veneza celebrando o domínio inconteste do Adriático.",
        "ai": "base = 75"
    },
    "capital_ship_modernisation": {
        "cost": 5, "year": 1922, "available": "date > 1922.1.1",
        "effect": "remove_ideas = ITA_ww1_dreadnought_fleet_in_being remove_ideas = ITA_ww1_insidious_flotilla_doctrine navy_experience = 20 add_ideas = ITA_ww1_capital_fleet_modernisation",
        "en_title": "Capital Ship Modernisation",
        "pt_title": "Modernização dos Navios Capitais",
        "en_desc": "Immediate effect: Modernises capital fleet for peacetime, replacing wartime doctrines (+20 navy XP).\n\nModernising Conte di Cavour and Andrea Doria classes to maintain operational readiness within Washington treaty limits.",
        "pt_desc": "Efeito imediato: Moderniza a esquadra de batalha para o pós-guerra, substituindo doutrinas de conflito (+20 de XP naval).\n\nModerniza os navios das classes Cavour e Doria para manter capacidade de combate no padrão das potências do pós-guerra.",
        "ai": "base = 65"
    },

    # Aviation Branch (12 focuses)
    "aviators_battalion": {
        "cost": 5, "year": 1911, "available": "date > 1911.1.1",
        "effect": "air_experience = 25 add_tech_bonus = { name = ITA_ww1_early_aviation bonus = 0.25 uses = 1 category = air_equipment } add_political_power = 25",
        "en_title": "The Aviators' Battalion",
        "pt_title": "O Batalhão de Aviadores",
        "en_desc": "Immediate effect: Founds the Battaglione Aviatori under the Army Engineers; grants +15 air XP.\n\nFormed at the Centocelle aerodrome near Rome, Italy's first military aviation unit trains pilots and tests early monoplanes.",
        "pt_desc": "Efeito imediato: Cria o Battaglione Aviatori junto à Engenharia Militar; concede +15 de XP aérea.\n\nInstalado no campo de Centocelle em Roma, o primeiro núcleo de aviação militar treina pilotos e avalia monoplanos de observação.",
        "ai": "base = 90"
    },
    "pilot_schools": {
        "cost": 5, "year": 1912, "available": "date > 1912.1.1",
        "effect": "air_experience = 25 add_tech_bonus = { name = ITA_ww1_flight_training bonus = 0.25 uses = 1 category = air_doctrine } add_political_power = 20",
        "en_title": "Pilot Schools",
        "pt_title": "Escolas de Pilotagem",
        "en_desc": "Immediate effect: Replaces experimental aviation battalion with formal flight academies (+15 air XP).\n\nStandardising pilot training curricula, navigation, and aerobatics to graduate hundreds of qualified military fliers.",
        "pt_desc": "Efeito imediato: Substitui o batalhão experimental por academias formais de voo (+15 de XP aérea).\n\nPadroniza o treinamento de navegação e manobras para formar centenas de pilotos aviadores militares.",
        "ai": "base = 80"
    },
    "caproni_bombers": {
        "cost": 5, "year": 1914, "available": "date > 1914.1.1",
        "effect": "air_experience = 20 add_tech_bonus = { name = ITA_ww1_caproni_heavy_bombers bonus = 0.25 uses = 1 category = heavy_air }",
        "en_title": "The Caproni Bombers",
        "pt_title": "Os Bombardeiros Caproni",
        "en_desc": "Immediate effect: Adopts Giovanni Caproni's massive three-engine heavy bombers (Ca.1 and Ca.3); bomber tech bonus (25%).\n\nPioneering heavy multi-engine strategic aviation, capable of carrying half a ton of bombs deep into Austrian rear areas.",
        "pt_desc": "Efeito imediato: Adota os bombardeiros pesados trimotores de Giovanni Caproni (Ca.1 e Ca.3); bônus de bombardeiros (25%).\n\nPioneirismo na aviação estratégica multimotor, capaz de lançar meia tonelada de bombas nas bases de retaguarda austríacas.",
        "ai": "base = 85"
    },
    "aeronautical_corps": {
        "cost": 5, "year": 1915, "available": "date > 1915.1.7",
        "effect": "air_experience = 25 add_tech_bonus = { name = ITA_ww1_air_recon bonus = 0.25 uses = 1 category = scout_plane } add_political_power = 25",
        "en_title": "The Military Aeronautical Corps",
        "pt_title": "O Corpo Aeronáutico Militar",
        "en_desc": "Immediate effect: Founds the autonomous wartime air corps, replacing training schools (+15 air XP, +25 PP).\n\nForming independent observation, fighter, and heavy bombardment squadrons directly responsive to General Headquarters.",
        "pt_desc": "Efeito imediato: Funda o corpo aeronáutico de guerra autônomo em substituição às escolas (+15 de XP aérea, +25 de PP).\n\nEstrutura esquadrilhas autônomas de caça, observação de artilharia e bombardeio pesado respondendo ao Alto Comando.",
        "ai": "base = 80"
    },
    "isotta_engines": {
        "cost": 5, "year": 1915, "available": "date > 1915.6.1",
        "effect": "air_experience = 10 add_tech_bonus = { name = ITA_ww1_aero_engines bonus = 0.25 uses = 1 category = air_equipment }",
        "en_title": "Isotta Fraschini Engines",
        "pt_title": "Motores Isotta Fraschini",
        "en_desc": "Immediate effect: Mass-produces reliable 250hp Isotta Fraschini and FIAT A.12 in-line aircraft engines (25% air tech bonus).\n\nSupplying domestic aircraft manufacturers with high-altitude, liquid-cooled engines renowned for their endurance and power.",
        "pt_desc": "Efeito imediato: Produz em larga escala motores de aviação Isotta Fraschini e FIAT A.12 de 250 hp; bônus de aviação (25%).\n\nFornece às fábricas nacionais propulsores refrigerados a água confiáveis e de grande rendimento em altitude.",
        "ai": "base = 75"
    },
    "flying_boats": {
        "cost": 5, "year": 1915, "available": "date > 1915.8.1",
        "effect": "air_experience = 15 add_tech_bonus = { name = ITA_ww1_macchi_flying_boats bonus = 0.25 uses = 1 category = naval_air }",
        "en_title": "Flying Boats",
        "pt_title": "Hidroaviões da Marinha",
        "en_desc": "Immediate effect: Builds agile Macchi M.5 and M.7 fighter flying boats for Adriatic coastal defense (+15 air XP).\n\nSingle-seat flying boats based in Venice and Brindisi combat Austrian seaplanes and escort anti-submarine drifters.",
        "pt_desc": "Efeito imediato: Constrói os hidroaviões de caça Macchi M.5 e M.7 para defender o Adriático (+15 de XP aérea).\n\nHidroaviões manobráveis operando de lagoas costeiras combatem aeronaves austríacas e vigiam o tráfego naval.",
        "ai": "base = 75"
    },
    "sva_reconnaissance": {
        "cost": 5, "year": 1916, "available": "date > 1916.6.1",
        "effect": "air_experience = 15 add_tech_bonus = { name = ITA_ww1_ansaldo_sva_aircraft bonus = 0.25 uses = 1 category = air_equipment }",
        "en_title": "SVA Reconnaissance Aircraft",
        "pt_title": "Aeronaves de Reconhecimento SVA",
        "en_desc": "Immediate effect: Introduces the fast Ansaldo SVA.5 long-range reconnaissance biplane (25% air tech bonus).\n\nCapable of flying 140 mph with an unprecedented six-hour endurance, the SVA maps Austrian rail networks across the Alps.",
        "pt_desc": "Efeito imediato: Adota o biplano veloz Ansaldo SVA.5 de longo alcance; bônus de equipamento aéreo (25%).\n\nCom velocidade superior a 220 km/h e seis horas de autonomia, fotografa as ferrovias austríacas nos Alpes.",
        "ai": "base = 80"
    },
    "fighter_squadrons": {
        "cost": 5, "year": 1916, "available": "date > 1916.1.1",
        "effect": "air_experience = 15 add_tech_bonus = { name = ITA_ww1_fighter_interception bonus = 0.25 uses = 1 category = light_fighter }",
        "en_title": "Fighter Squadrons",
        "pt_title": "Esquadrões de Caça",
        "en_desc": "Immediate effect: Organises dedicated fighter squadrons (Squadriglie da Caccia) armed with synchronized machine guns.\n\nPupils trained in air deflection shooting fly French Nieuport and SPAD scouts to sweep Austrian reconnaissance craft from the skies.",
        "pt_desc": "Efeito imediato: Cria esquadrões de caça dedicados equipados com metralhadoras sincronizadas (+15 de XP aérea).\n\nPilotos treinados no combate aéreo voam caças Nieuport e SPAD para limpar os céus da frente das aeronaves austríacas.",
        "ai": "base = 80"
    },
    "ace_squadrons": {
        "cost": 5, "year": 1917, "available": "date > 1917.1.1",
        "effect": "air_experience = 30 add_tech_bonus = { name = ITA_ww1_baracca_fighter_tactics bonus = 0.25 uses = 1 category = light_fighter } country_event = { id = ww1_italy.62 days = 1 }",
        "en_title": "The Elite Squadrons",
        "pt_title": "Os Esquadrões de Elite",
        "en_desc": "Immediate effect: Major Francesco Baracca's 91st Squadron (Squadriglia degli Assi) achieves legendary renown (+20 air XP).\n\nDecorated with the Prancing Horse emblem (Cavallino Rampante), Baracca, Ruffo di Calabria, and Piccio down dozens of enemy aircraft.",
        "pt_desc": "Efeito imediato: A 91ª Esquadrilha de Ases de Francesco Baracca alcança renome lendário (+20 de XP aérea, +3% apoio de guerra).\n\nExibindo o Cavalo Rampante na fuselagem, Baracca e os principais ases italianos dominam as batalhas aéreas nos Alpes.",
        "ai": "base = 85"
    },
    "strategic_bombing": {
        "cost": 5, "year": 1917, "available": "date > 1917.6.1",
        "effect": "air_experience = 25 add_tech_bonus = { name = ITA_ww1_douhet_strategic_theory bonus = 0.25 uses = 1 category = air_doctrine } add_political_power = 25",
        "en_title": "Strategic Bombing",
        "pt_title": "Bombardeio Estratégico",
        "en_desc": "Immediate effect: Implements Colonel Giulio Douhet's theories of independent strategic air power (+20 air XP).\n\nConcentrated Caproni bomber wings strike Austrian rail junctions, naval arsenals at Pola, and ammunition dumps in deep rear areas.",
        "pt_desc": "Efeito imediato: Implementa as teorias do Coronel Giulio Douhet de bombardeio estratégico independente (+20 de XP aérea).\n\nGrandes esquadras de Caproni atacam as ferrovias de abastecimento e o arsenal de Pola nas profundezas da retaguarda inimiga.",
        "ai": "base = 85"
    },
    "vienna_flight": {
        "cost": 5, "year": 1918, "available": "date > 1918.8.9",
        "effect": "air_experience = 25 add_political_power = 40 country_event = { id = ww1_italy.60 days = 1 }",
        "en_title": "The Flight over Vienna",
        "pt_title": "O Voo sobre Viena",
        "en_desc": "Immediate effect: D'Annunzio's 87th Serenissima Squadron drops 400,000 tricolor leaflets over the Austrian capital (+40 PP).\n\nCovering seven hundred miles across high mountains without bombs, Italian fliers prove they can strike Vienna at will while showering citizens with peace manifestos.",
        "pt_desc": "Efeito imediato: A 87ª Esquadrilha de D'Annunzio lança 400 mil panfletos tricolores sobre a capital austríaca (+40 de PP).\n\nPercorrendo mais de mil quilômetros sobre os Alpes, aviadores italianos demonstram a vulnerabilidade de Viena e desferem golpe psicológico.",
        "ai": "base = 85"
    },
    "air_autonomy_debate": {
        "cost": 5, "year": 1919, "available": "date > 1919.1.1",
        "effect": "159 = { add_building_construction = { type = air_base level = 2 instant_build = yes } } air_experience = 30 add_political_power = 40",
        "en_title": "The Air Autonomy Debate",
        "pt_title": "O Debate da Autonomia da Aviação",
        "en_desc": "Immediate effect: Establishes foundations for an independent Air Ministry, transitioning from wartime air corps (+15 air XP, +25 PP).\n\nEstablishing independent air budget lines, specialized test centers at Guidonia, and professional aeronautical officer careers.",
        "pt_desc": "Efeito imediato: Estabelece as bases do Ministério da Aeronáutica, em transição do corpo aéreo de guerra (+15 de XP aérea, +25 de PP).\n\nCria dotações orçamentárias próprias, centros de teste aeronáutico e uma carreira militar independente para a aviação.",
        "ai": "base = 75"
    },
}

# Military events (16 events, all with >= 2 options)
EVENTS = [
    {
        "id": 60, "picture": "GFX_event_ww1_italy_60", "is_triggered": True,
        "t": ("The Flight over Vienna", "O Voo sobre Viena"),
        "d": ("On 9 August 1918, eleven Ansaldo SVA aircraft led by poet Gabriele D'Annunzio appear in the clear morning skies above Vienna, dropping thousands of tricolor leaflets urging the Austrian public to surrender.",
              "Em 9 de agosto de 1918, onze aviões Ansaldo SVA comandados por Gabriele D'Annunzio surgem nos céus de Viena, lançando milhares de panfletos tricolores convidando a população à paz."),
        "options": [
            ("A breathtaking triumph of Italian aviation spirit!", "Um triunfo deslumbrante do gênio da aviação italiana!",
             "air_experience = 25 add_political_power = 40", 90),
            ("Conserve precious aircraft for frontline reconnaissance", "Poupar os aviões para o reconhecimento no Piave",
             "air_experience = 15 add_political_power = 20", 10)
        ]
    },
    {
        "id": 61, "picture": "GFX_event_ww1_italy_61", "is_triggered": True,
        "t": ("Premuda: Rizzo Sinks the Szent István", "Premuda: Rizzo Afunda o Szent István"),
        "d": ("Commander Luigi Rizzo in tiny MAS 15 intercepts the Austrian dreadnought division off Premuda Island, firing two torpedoes that capsize and sink the massive battleship SMS Szent István.",
              "O comandante Luigi Rizzo a bordo da lancha MAS 15 intercepta a divisão naval austríaca na ilha de Premuda, afundando com dois torpedos o grande encouraçado SMS Szent István."),
        "options": [
            ("Hail the heroism of the light flotillas!", "Celebrar a audácia heroica das flotilhas ligeiras!",
             "navy_experience = 20 add_war_support = 0.03 add_political_power = 30", 95),
            ("Award Gold Medals of Military Valour to Rizzo's crew", "Conceder a Medalha de Ouro ao valor militar à tripulação",
             "navy_experience = 15 add_war_support = 0.03 add_stability = 0.02", 5)
        ]
    },
    {
        "id": 62, "picture": "GFX_event_ww1_italy_62", "is_triggered": True,
        "t": ("The Passing of Francesco Baracca", "A Queda do Ás Francesco Baracca"),
        "d": ("Major Francesco Baracca, Italy's ace of aces with 34 aerial victories, is shot down over the Montello during a low-level strafing run against Austrian infantry.",
              "O Major Francesco Baracca, maior ás da aviação italiana com 34 vitórias aéreas, é abatido no Montello durante um ataque a baixa altitude contra trincheiras inimigas."),
        "options": [
            ("His Prancing Horse emblem shall inspire future generations", "Seu Cavalo Rampante inspirará gerações de guerreiros",
             "add_war_support = 0.02 add_stability = 0.02 add_political_power = 25", 85),
            ("Dedicate permanent pilot scholarships in his honor", "Criar bolsas de estudo permanentes de pilotagem em sua memória",
             "air_experience = 15 add_stability = 0.02", 15)
        ]
    },
    {
        "id": 63, "picture": "GFX_event_ww1_italy_63", "is_triggered": True,
        "t": ("The Founding of the Arditi", "A Fundação dos Arditi"),
        "d": ("Captain Giuseppe Bassi forms the first Department of Assault (Reparto d'Assalto) at Sdricca di Manzano, training aggressive volunteers in dagger combat, grenade throwing, and flamethrowers.",
              "O capitão Giuseppe Bassi organiza o primeiro Reparto d'Assalto em Sdricca di Manzano, treinando voluntários selecionados no combate com punhais, granadas e lança-chamas."),
        "options": [
            ("Approve the creation of Arditi battalions across all armies", "Aprovar a criação de batalhões de Arditi em todos os corpos",
             "army_experience = 15 add_ideas = ITA_ww1_arditi_shock_troops", 90),
            ("Retain assault cadres as divisional specialist platoons", "Manter as tropas de choque como pelotões especializados divisionais",
             "army_experience = 20 add_political_power = 15", 10)
        ]
    },
    {
        "id": 64, "picture": "GFX_event_ww1_italy_64", "is_triggered": True,
        "t": ("Cadorna's Frontline Inspections", "As Inspeções de Cadorna no Front"),
        "d": ("Chief of Staff Cadorna inspects the rocky Carso front, demanding aggressive discipline and relieving generals who fail to attain offensive objectives.",
              "O General Cadorna inspeciona a frente rochosa do Carso, exigindo disciplina rígida e destituindo generais que vacilem diante dos objetivos de ataque."),
        "options": [
            ("Support the high command's firm authority", "Apoiar a autoridade inflexível do Alto Comando",
             "army_experience = 10 add_political_power = 20", 70),
            ("Urge greater tactical flexibility on the ground", "Recomendar maior flexibilidade tática aos comandos locais",
             "add_to_variable = { ita_ww1_army_morale = 5 } add_political_power = -10 ita_ww1_clamp_counters = yes", 30)
        ]
    },
    {
        "id": 65, "picture": "GFX_event_ww1_italy_65", "is_triggered": True,
        "t": ("The Caproni Bomber Factory Surge", "A Expansão dos Bombardeiros Caproni"),
        "d": ("Giovanni Caproni opens new manufacturing hangars in Taliedo near Milan, delivering hundreds of heavy Ca.3 and Ca.4 biplanes to the Italian and Allied armies.",
              "Giovanni Caproni inaugura novas oficinas em Taliedo perto de Milão, entregando centenas de bombardeiros Ca.3 aos exércitos italiano e aliados."),
        "options": [
            ("Standardize Caproni production for strategic operations", "Padronizar os aviões Caproni para bombardeio estratégico",
             "air_experience = 15 add_ideas = ITA_ww1_douhet_air_doctrine", 80),
            ("Allocate engine output to twin-engine reconnaissance", "Direcionar motores para aeronaves de reconhecimento tático",
             "air_experience = 20 add_political_power = 15", 20)
        ]
    },
    {
        "id": 66, "picture": "GFX_event_ww1_italy_66", "is_triggered": True,
        "t": ("The Otranto Night Battle", "A Batalha Noturna de Otranto"),
        "d": ("Austrian light cruisers under Captain Miklós Horthy raid the Otranto barrage net lines at night, sinking several allied drifter trawlers before Italian cruisers engage.",
              "Cruzadores ligeiros austríacos comandados por Miklós Horthy atacam a barragem de Otranto à noite, afundando traineiras antes da chegada de reforços italianos."),
        "options": [
            ("Strengthen destroyer screens and aerial reconnaissance", "Reforçar as escoltas de contratorpedeiros e patrulhas aéreas",
             "navy_experience = 15 add_stability = 0.01", 85),
            ("Deploy heavier scout cruisers on permanent patrol", "Manter cruzadores de batalha em patrulha constante",
             "navy_experience = 10 add_political_power = -15", 15)
        ]
    },
    {
        "id": 67, "picture": "GFX_event_ww1_italy_67", "is_triggered": True,
        "t": ("Armored Cars at the Front", "Automóveis Blindados no Front"),
        "d": ("Ansaldo-Lancia 1Z armored cars equipped with twin machine-gun turrets prove their worth during breakthrough operations across the plains of Friuli.",
              "Automóveis blindados Ansaldo-Lancia 1Z armados com torres duplas de metralhadora destacam-se nas perseguições pelo vale do Friuli."),
        "options": [
            ("Expand motorized cavalry squadrons", "Expandir os esquadrões de cavalaria motorizada blindada",
             "army_experience = 10 add_ideas = ITA_ww1_motorized_shock_cadres", 75),
            ("Conserve chassis for artillery transport tractors", "Reservar chassis para tratores de transporte de artilharia",
             "army_experience = 15 add_political_power = 15", 25)
        ]
    },
    {
        "id": 68, "picture": "GFX_event_ww1_italy_68", "is_triggered": True,
        "t": ("The Mountain Teleferica Network", "A Rede de Teleféricos de Montanha"),
        "d": ("Army engineers construct thousands of miles of aerial cableways (teleferiche) stretching up sheer cliffs, hoisting artillery shells, food, and wounded men safely across ravines.",
              "A Engenharia Militar constrói milhares de quilômetros de teleféricos aéreos suspensos nas montanhas, transportando munições e feridos sobre os abismos."),
        "options": [
            ("Expand mountain logistics networks to every crest", "Expandir os teleféricos para todas as cristas alpinas",
             "army_experience = 10 add_to_variable = { ita_ww1_army_morale = 5 } ita_ww1_clamp_counters = yes", 85),
            ("Rely on mule trains for secondary ridges", "Empregar muares para os cumes secundários",
             "add_political_power = 20", 15)
        ]
    },
    {
        "id": 69, "picture": "GFX_event_ww1_italy_69", "is_triggered": True,
        "t": ("The Raid on Buccari (La Beffa di Buccari)", "A Troça de Buccari (La Beffa di Buccari)"),
        "d": ("Three Italian MAS boats under Costanzo Ciano and Gabriele D'Annunzio infiltrate fifty miles deep into Austrian territorial waters, launching torpedoes into Buccari harbor.",
              "Três lanchas MAS sob Costanzo Ciano e Gabriele D'Annunzio penetram 80 quilômetros na baía fortificada de Buccari, disparando torpedos contra ancoradouros austríacos."),
        "options": [
            ("Celebrate the audaça of the naval assault!", "Celebrar a audácia lendária dos marinheiros italianos!",
             "navy_experience = 15 add_war_support = 0.02 add_political_power = 25", 90),
            ("Focus on practical anti-submarine escort duties", "Priorizar a escolta pragmática de comboios mercantes",
             "navy_experience = 15 add_stability = 0.01", 10)
        ]
    },
    {
        "id": 70, "picture": "GFX_event_ww1_italy_70", "is_triggered": True,
        "t": ("The Sinking of the SMS Wien", "O Afundamento do SMS Wien"),
        "d": ("Lieutenant Luigi Rizzo slips MAS 9 into the heavily guarded harbor of Trieste, cutting steel harbor booms and sinking the Austrian coastal battleship SMS Wien.",
              "O Tenente Luigi Rizzo penetra no porto vigiado de Trieste com a lancha MAS 9, cortando as redes de aço e torpedeando o encouraçado costeiro SMS Wien."),
        "options": [
            ("Rizzo has struck a glorious blow in the lion's den!", "Rizzo desfere um golpe glorioso no covil do inimigo!",
             "navy_experience = 20 add_war_support = 0.03 add_political_power = 30", 95),
            ("Reward the torpedo flotilla with decorated standards", "Condecorar o estandarte da flotilha de torpedeiros",
             "navy_experience = 15 add_stability = 0.02", 5)
        ]
    },
    {
        "id": 71, "picture": "GFX_event_ww1_italy_71", "is_triggered": True,
        "t": ("High-Altitude Alpine Warfare", "A Guerra nas Geleiras Alpinas"),
        "d": ("On the Ortles and Adamello glaciers, Alpini and Austrian Kaiserjäger fight in blizzards at twelve thousand feet, carving barracks into glacial ice.",
              "Nas geleiras do Ortles e Adamello, os Alpini e os Kaiserjäger combatem a quase quatro mil metros de altitude, escavando túneis no gelo perpétuo."),
        "options": [
            ("Support the glacier garrisons with extreme mountain kits", "Abastecer as guarnições com equipamento de gelo extremo",
             "army_experience = 15 add_to_variable = { ita_ww1_army_morale = 5 } ita_ww1_clamp_counters = yes", 80),
            ("Consolidate positions in the lower mountain passes", "Manter as defesas concentradas nos desfiladeiros inferiores",
             "add_political_power = 20", 20)
        ]
    },
    {
        "id": 72, "picture": "GFX_event_ww1_italy_72", "is_triggered": True,
        "t": ("The Villar Perosa Submachine Gun", "A Submetralhadora Villar Perosa"),
        "d": ("Designed by Bethel Revelli, the twin-barrel Villar Perosa fires nine-millimeter pistol rounds at blistering speed, offering devastating close-quarters firepower for Arditi assaults.",
              "Projetada por Bethel Revelli, a arma bitubo Villar Perosa dispara projéteis de 9mm a cadência espantosa, fornecendo poder de fogo decisivo nos assaltos."),
        "options": [
            ("Issue Villar Perosa weapons to all frontline stormtroops", "Distribuir as Villar Perosa a todas as tropas de assalto",
             "army_experience = 15 add_tech_bonus = { name = ITA_ww1_submachine_gun_bonus bonus = 0.25 uses = 1 category = infantry_weapons }", 85),
            ("Mount them primarily on aircraft and sidecar motorcycles", "Montá-las preferencialmente em aeronaves e motocicletas",
             "air_experience = 10 army_experience = 10", 15)
        ]
    },
    {
        "id": 73, "picture": "GFX_event_ww1_italy_73", "is_triggered": True,
        "t": ("The Sinking of the Leonardo da Vinci", "O Naufrágio do Leonardo da Vinci"),
        "d": ("In August 1916, the dreadnought Leonardo da Vinci suffers a catastrophic internal magazine explosion in Taranto harbor, capsizing with heavy loss of life under suspicion of Austrian sabotage.",
              "Em agosto de 1916, o encouraçado Leonardo da Vinci sofre explosão interna no porto de Taranto, emborcando sob fortes suspeitas de sabotagem austríaca."),
        "options": [
            ("Tighten naval counter-intelligence and port security", "Reforçar a contrainteligência naval e a segurança portuária",
             "navy_experience = 10 add_stability = -0.02 add_political_power = 25", 80),
            ("Initiate immediate salvage and refloating operations", "Iniciar operações imediatas de salvamento e reflutuação",
             "navy_experience = 15 add_political_power = -20", 20)
        ]
    },
    {
        "id": 74, "picture": "GFX_event_ww1_italy_74", "is_triggered": True,
        "t": ("Postwar Aviation Standardization", "Padronização Aeronáutica no Pós-Guerra"),
        "d": ("Following the armistice, military planners evaluate aircraft production. Should Italy prioritize civilian postal routes or maintain military prototyping?",
              "Com o fim das hostilidades, a diretoria aeronáutica debate a transição entre rotas postais civis e a pesquisa militar contínua."),
        "options": [
            ("Preserve high-speed military prototyping and racing teams", "Preservar equipes de protótipos militares e velocidade",
             "air_experience = 20 add_ideas = ITA_ww1_independent_air_force_charter", 75),
            ("Divert aeronautical workshops to civil air transport", "Converter oficinas aeronáuticas para o transporte civil",
             "add_political_power = 30 add_stability = 0.02", 25)
        ]
    },
    {
        "id": 75, "picture": "GFX_event_ww1_italy_75", "is_triggered": True,
        "t": ("The Veterans of the Arditi (Associazione Arditi)", "A Associação dos Veteranos Arditi"),
        "d": ("Demobilised Arditi assault troopers form national brotherhoods across Milan and Rome. Proud of their black shirts and daggers, they refuse to return quietly to civilian obscurity.",
              "Veteranos dos Arditi fundam associações patrióticas em Milão e Roma. Orgulhosos de seus uniformes negros, recusam-se a retornar ao anonimato civil."),
        "options": [
            ("Incorporate Arditi cadres into police and frontier guards", "Incorporar os quadros de Arditi na polícia e guardas de fronteira",
             "army_experience = 10 add_political_power = 25 add_war_support = 0.02", 70),
            ("Order orderly disbandment and veteran pensions", "Decretar desmobilização ordeira e pensões de combatente",
             "add_stability = 0.03 add_to_variable = { ita_ww1_social_tension = -5 } ita_ww1_clamp_counters = yes", 30)
        ]
    }
]

# Decisions for Military category
DECISIONS = [
    {
        "id": "ita_ww1_alpini_winter_manoeuvres",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_18",
        "cost": 30, "days": 120,
        "effect": "army_experience = 15 add_to_variable = { ita_ww1_army_morale = 5 } ita_ww1_clamp_counters = yes",
        "en_title": "Alpine Winter Field Exercises",
        "pt_title": "Manobras de Inverno nos Alpes",
        "en_desc": "Conduct rigorous cold-weather combat drills and ski maneuvers on the high mountain passes.",
        "pt_desc": "Realizar exercícios de combate no gelo e manobras com esquis nos passos alpinos elevados."
    },
    {
        "id": "ita_ww1_torpedo_flotilla_night_sortie",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_19",
        "cost": 25, "days": 90,
        "effect": "navy_experience = 15 add_war_support = 0.02",
        "en_title": "Nocturnal Torpedo Sweep in the Channels",
        "pt_title": "Incursão Noturna de Torpedeiros nos Canais",
        "en_desc": "Deploy MAS flotillas on high-speed night sweeps among Dalmatian island anchorages.",
        "pt_desc": "Enviar flotilhas de lanchas MAS em incursões noturnas de emboscada nos canais dálmatas."
    },
    {
        "id": "ita_ww1_caproni_night_bombing_raid",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_20",
        "cost": 35, "days": 90,
        "effect": "air_experience = 20 add_war_support = 0.02",
        "en_title": "Night Strategic Bombing Raid",
        "pt_title": "Raid Noturno de Bombardeio Estratégico",
        "en_desc": "Dispatch Caproni heavy bomber wings to strike enemy railway yards under the cover of darkness.",
        "pt_desc": "Despachar esquadras de bombardeiros Caproni para atingir entroncamentos ferroviários sob a escuridão."
    },
    {
        "id": "ita_ww1_arditi_trench_raid",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_21",
        "cost": 30, "days": 60,
        "effect": "army_experience = 15 add_to_variable = { ita_ww1_army_morale = 10 } ita_ww1_clamp_counters = yes",
        "en_title": "Arditi Trench Surprise Raid",
        "pt_title": "Incursão de Surpresa dos Arditi",
        "en_desc": "Launch dagger-and-grenade nighttime raids to seize enemy outposts and capture staff intelligence.",
        "pt_desc": "Lançar incursões noturnas com punhais e granadas para capturar postos avançados e mapas inimigos."
    },
    {
        "id": "ita_ww1_naval_minefield_laying",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_22",
        "cost": 35, "days": 150,
        "effect": "navy_experience = 10 add_stability = 0.02",
        "en_title": "Deep Adriatic Minefields",
        "pt_title": "Campos de Minas no Alto Adriático",
        "en_desc": "Lay thousands of contact mines off Venice and Ancona to prevent enemy surface raids.",
        "pt_desc": "Lançar barreiras de minas ao largo de Veneza e Ancona para bloquear incursões navais inimigas."
    },
    {
        "id": "ita_ww1_fighter_interception_sweep",
        "category": "ITA_ww1_category_military",
        "icon": "GFX_decision_ITA_ww1_decision_23",
        "cost": 25, "days": 90,
        "effect": "air_experience = 15 add_war_support = 0.02",
        "en_title": "Fighter Sweep over the Montello",
        "pt_title": "Varredura de Caça sobre o Montello",
        "en_desc": "Scramble the 91st Squadriglia to clear airspace and protect artillery spotter planes.",
        "pt_desc": "Decolar a 91ª Esquadrilha para limpar o espaço aéreo e proteger os biplanos de regulação de tiro."
    }
]

# Ideas for Military Wing
IDEAS = {
    "ITA_ww1_general_staff_corps": {
        "pic": "ITA_ww1_idea_25",
        "modifier": "planning_speed = 0.05 max_planning = 0.05",
        "en_name": "General Staff Planning", "pt_name": "Planejamento do Estado-Maior",
        "en_desc": "Structured operational planning sections coordinating army mobilization and supplies.",
        "pt_desc": "Seções de planejamento operacional estruturadas coordenando mobilização e logística."
    },
    "ITA_ww1_cadorna_discipline": {
        "pic": "ITA_ww1_idea_26",
        "modifier": "army_attack_factor = 0.05 land_reinforce_rate = -0.003",
        "en_name": "Cadornian Iron Discipline", "pt_name": "Disciplina Férrea de Cadorna",
        "en_desc": "Unyielding offensive demands and draconian military discipline across all ranks.",
        "pt_desc": "Exigências ofensivas inflexíveis e rigor penal draconiano em todos os escalões."
    },
    "ITA_ww1_mountain_howitzers": {
        "pic": "ITA_ww1_idea_27",
        "modifier": "army_artillery_attack_factor = 0.05 army_morale_factor = 0.03",
        "en_name": "Alpine Mountain Howitzers", "pt_name": "Obuseiros de Montanha Alpinos",
        "en_desc": "Mule-transportable artillery pieces providing direct fire support on rocky precipices.",
        "pt_desc": "Canhões desmontáveis transportados por mulas fornecendo apoio direto nas escarpas rochosas."
    },
    "ITA_ww1_railway_mobilisation_plan": {
        "pic": "ITA_ww1_idea_28",
        "modifier": "army_speed_factor = 0.05 land_reinforce_rate = 0.05",
        "en_name": "Railway Mobilization Grids", "pt_name": "Malha Ferroviária de Mobilização",
        "en_desc": "Efficient railway timetables concentrating armies smoothly along the frontier.",
        "pt_desc": "Escalas ferroviárias eficientes concentrando as divisões na fronteira com agilidade."
    },
    "ITA_ww1_frontier_fortress_belt": {
        "pic": "ITA_ww1_idea_29",
        "modifier": "army_core_defence_factor = 0.08 max_dig_in = 2",
        "en_name": "Alpine Armoured Fortresses", "pt_name": "Fortalezas Blindadas Alpinas",
        "en_desc": "Steel cupolas and concrete fortresses sealing alpine passes against enemy advances.",
        "pt_desc": "Cúpulas de aço e casamatas de concreto fechando os passos alpinos contra invasores."
    },
    "ITA_ww1_cadornian_offensive_cult": {
        "pic": "ITA_ww1_idea_30",
        "modifier": "army_attack_factor = 0.08 army_speed_factor = 0.03",
        "en_name": "The Cult of the Offensive", "pt_name": "O Culto da Ofensiva",
        "en_desc": "Faith in continuous frontal infantry assault to break through enemy defensive lines.",
        "pt_desc": "Crença no assalto frontal obstinado da infantaria para romper as posições inimigas."
    },
    "ITA_ww1_methodical_firepower_doctrine": {
        "pic": "ITA_ww1_idea_31",
        "modifier": "army_artillery_attack_factor = 0.08 army_core_defence_factor = 0.05",
        "en_name": "Methodical Firepower Doctrine", "pt_name": "Doutrina Metódica de Fogo",
        "en_desc": "Systematic artillery bombardment and deliberate infantry advances conserving lives.",
        "pt_desc": "Bombardeio metódico de artilharia e avanço calculado de infantaria poupando baixas."
    },
    "ITA_ww1_gas_respirators": {
        "pic": "ITA_ww1_idea_32",
        "modifier": "attrition = -0.05 army_core_defence_factor = 0.03",
        "en_name": "Trench Gas Protection", "pt_name": "Proteção contra Gases de Trincheira",
        "en_desc": "Effective respirators and chemical decontamination units protecting frontline troops.",
        "pt_desc": "Máscaras eficientes e equipes de descontaminação resguardando as divisões do front."
    },
    "ITA_ww1_complimentary_officer_academies": {
        "pic": "ITA_ww1_idea_1",
        "modifier": "planning_speed = 0.05 experience_loss_factor = -0.05",
        "en_name": "Reserve Sublieutenants Corps", "pt_name": "Corpo de Oficiais de Complemento",
        "en_desc": "Educated university youth stepping forward to command infantry platoons under fire.",
        "pt_desc": "Jovens universitários patriotas assumindo o comando de pelotões de infantaria sob fogo."
    },
    "ITA_ww1_dismounted_cavalry_regiments": {
        "pic": "ITA_ww1_idea_2",
        "modifier": "cavalry_attack_factor = 0.05 cavalry_defence_factor = 0.05",
        "en_name": "Dismounted Cavalry Regiments", "pt_name": "Regimentos de Cavalaria Desmontada",
        "en_desc": "Elite cavalrymen reinforcing trench lines with disciplined carbine marksmanship.",
        "pt_desc": "Cavalarianos de elite reforçando as trincheiras com pontaria precisa de carabina."
    },
    "ITA_ww1_arditi_shock_troops": {
        "pic": "ITA_ww1_idea_3",
        "modifier": "special_forces_attack_factor = 0.15 breakthrough_factor = 0.10",
        "en_name": "Arditi Stormtrooper Units", "pt_name": "Unidades de Choque dos Arditi",
        "en_desc": "Daring assault specialists trained in hand-to-hand combat, flamethrowers, and wire-cutting.",
        "pt_desc": "Combatentes destemidos treinados no combate corpo a corpo, lança-chamas e assalto rápido."
    },
    "ITA_ww1_diaz_humane_leadership": {
        "pic": "ITA_ww1_idea_4",
        "modifier": "army_org_factor = 0.08 army_morale_factor = 0.08",
        "en_name": "Diaz Humane Leadership", "pt_name": "Liderança Humanitária de Diaz",
        "en_desc": "Compassionate commander prioritizing soldier welfare, decent rations, and defensive preservation.",
        "pt_desc": "Comandante atencioso priorizando o bem-estar da tropa, boa alimentação e economia de vidas."
    },
    "ITA_ww1_defence_in_depth_piave": {
        "pic": "ITA_ww1_idea_5",
        "modifier": "max_dig_in_factor = 0.10 army_core_defence_factor = 0.10",
        "en_name": "Piave Defense in Depth", "pt_name": "Defesa em Profundidade no Piave",
        "en_desc": "Layered defensive redoubts and pre-ranged artillery curtains shattering enemy bridgeheads.",
        "pt_desc": "Redutos defensivos em camadas e cortinas de artilharia afogando as ofensivas inimigas."
    },
    "ITA_ww1_continuous_offensive_pressure": {
        "pic": "ITA_ww1_idea_6",
        "modifier": "army_attack_factor = 0.06 army_speed_factor = 0.05",
        "en_name": "Aggressive River Probing", "pt_name": "Pressão Contínua nas Margens",
        "en_desc": "Constant raiding across river shallows wearing down Austro-Hungarian defensive reserves.",
        "pt_desc": "Incursões constantes através do rio desgastando as reservas austro-húngaras."
    },
    "ITA_ww1_strengthened_carabinieri": {
        "pic": "ITA_ww1_idea_7",
        "modifier": "stability_factor = 0.05 foreign_subversive_activites = -0.15",
        "en_name": "Strengthened Carabinieri Corps", "pt_name": "Arma dei Carabinieri Reforçada",
        "en_desc": "Prestigious royal gendarmerie enforcing civil order and constitutional legality.",
        "pt_desc": "Gendarmaria real de prestígio garantindo a paz interna e a legalidade constitucional."
    },
    "ITA_ww1_badoglio_standing_army": {
        "pic": "ITA_ww1_idea_8",
        "modifier": "army_org_factor = 0.05 army_core_defence_factor = 0.05",
        "en_name": "Postwar Professional Army", "pt_name": "Exército Profissional do Pós-Guerra",
        "en_desc": "A streamlined standing army preserving the hard-won operational doctrine of the Great War.",
        "pt_desc": "Um exército permanente enxuto preservando a rica doutrina tática da Grande Guerra."
    },
    "ITA_ww1_peacetime_military_economy": {
        "pic": "ITA_ww1_idea_9",
        "modifier": "consumer_goods_factor = -0.02 political_power_factor = 0.05",
        "en_name": "Peacetime Fiscal Realism", "pt_name": "Realismo Fiscal em Tempo de Paz",
        "en_desc": "Prudent reductions in military budgets to facilitate national economic recovery.",
        "pt_desc": "Redução prudente das dotações militares facilitando a recuperação econômica do país."
    },
    "ITA_ww1_regia_marina_cadres": {
        "pic": "ITA_ww1_idea_10",
        "modifier": "navy_max_range_factor = 0.05 naval_hit_chance = 0.03",
        "en_name": "Regia Marina Officer Cadres", "pt_name": "Quadros de Oficiais da Regia Marina",
        "en_desc": "Professional naval academy graduates at Livorno mastering modern naval artillery.",
        "pt_desc": "Oficiais graduados pela Academia Naval de Livorno dominando a artilharia moderna."
    },
    "ITA_ww1_taranto_naval_arsenal": {
        "pic": "ITA_ww1_idea_11",
        "modifier": "refit_speed = 0.10 industrial_capacity_dockyard = 0.05",
        "en_name": "Taranto Naval Arsenal", "pt_name": "Arsenal Naval de Taranto",
        "en_desc": "First-class dry docks and repair installations maintaining the battle fleet at high readiness.",
        "pt_desc": "Grandes docas secas e instalações de reparo mantendo a esquadra de batalha em prontidão."
    },
    "ITA_ww1_adriatic_naval_stations": {
        "pic": "ITA_ww1_idea_12",
        "modifier": "naval_coordination = 0.08 navy_submarine_detection_factor = 0.05",
        "en_name": "Adriatic Naval Stations", "pt_name": "Estuturas Navais do Adriático",
        "en_desc": "Dispersed destroyer and torpedo pens at Venice and Brindisi dominating coastal waters.",
        "pt_desc": "Bases avançadas de contratorpedeiros em Veneza e Brindisi dominando a costa oriental."
    },
    "ITA_ww1_adriatic_patrol_network": {
        "pic": "ITA_ww1_idea_13",
        "modifier": "naval_detection = 0.05 screening_efficiency = 0.05",
        "en_name": "Adriatic Patrol Network", "pt_name": "Rede de Patrulha do Adriático",
        "en_desc": "Continuous coastal scouting preventing surprise hostile bombardments from Pola.",
        "pt_desc": "Vigilância costeira contínua prevenindo bombardeios surpresa das esquadras de Pola."
    },
    "ITA_ww1_otranto_barrage_net": {
        "pic": "ITA_ww1_idea_14",
        "modifier": "navy_submarine_detection_factor = 0.10 sub_retreat_speed = -0.10",
        "en_name": "The Otranto Submarine Net", "pt_name": "A Rede de Bloqueio de Otranto",
        "en_desc": "Deep netting and hydrophone barriers trapping enemy U-boats within the Adriatic.",
        "pt_desc": "Redes profundas com hidrofones prendendo os submarinos inimigos no mar Adriático."
    },
    "ITA_ww1_dreadnought_fleet_in_being": {
        "pic": "ITA_ww1_idea_15",
        "modifier": "navy_capital_ship_defence_factor = 0.08 naval_enemy_fleet_size_ratio_penalty_factor = -0.10",
        "en_name": "Battle Fleet in Being", "pt_name": "Frota de Batalha em Potência",
        "en_desc": "Intact dreadnought squadrons at Taranto dictating naval caution to all Mediterranean powers.",
        "pt_desc": "Os encouraçados intactos em Taranto impondo cautela a todas as frotas do Mediterrâneo."
    },
    "ITA_ww1_insidious_flotilla_doctrine": {
        "pic": "ITA_ww1_idea_16",
        "modifier": "navy_screen_attack_factor = 0.08 naval_torpedo_hit_chance_factor = 0.05",
        "en_name": "Insidious Flotilla Warfare", "pt_name": "Guerra Insidiosa de Flotilhas",
        "en_desc": "Aggressive nighttime raids and concealed torpedo boat strikes in narrow island straits.",
        "pt_desc": "Ataques noturnos agressivos e emboscadas de torpedeiros nos canais das ilhas."
    },
    "ITA_ww1_mas_motor_torpedo_boats": {
        "pic": "ITA_ww1_idea_17",
        "modifier": "naval_torpedo_hit_chance_factor = 0.08 convoy_raiding_efficiency_factor = 0.10",
        "en_name": "MAS Motor Torpedo Flotillas", "pt_name": "Flotilhas de Lanchas Rápidas MAS",
        "en_desc": "Daring high-speed wooden torpedo boats piercing enemy harbors and sinking capital ships.",
        "pt_desc": "Lanchas torpedeiras velozes de madeira penetrando portos e afundando encouraçados."
    },
    "ITA_ww1_albanian_convoy_routes": {
        "pic": "ITA_ww1_idea_18",
        "modifier": "convoy_escort_efficiency = 0.10 navy_submarine_detection_factor = 0.05",
        "en_name": "Albanian Sea Lifelines", "pt_name": "Linhas de Comboio da Albânia",
        "en_desc": "Flawless transport coordination sustaining Italian overseas armies across the straits.",
        "pt_desc": "Coordenação impecável de comboios garantindo suprimentos às forças de além-mar."
    },
    "ITA_ww1_mignatta_special_raiders": {
        "pic": "ITA_ww1_idea_19",
        "modifier": "naval_critical_score_chance_factor = 0.10 navy_intel_to_others = -0.05",
        "en_name": "Mignatta Special Naval Raiders", "pt_name": "Incursores Navais Especiais Mignatta",
        "en_desc": "Stealth assault swimmers penetrating enemy harbor booms to attach explosive limpet mines.",
        "pt_desc": "Mergulhadores de assalto penetrando redes portuárias para fixar minas magnéticas."
    },
    "ITA_ww1_capital_fleet_modernisation": {
        "pic": "ITA_ww1_idea_20",
        "modifier": "navy_capital_ship_attack_factor = 0.05 refit_speed = 0.08",
        "en_name": "Capital Ship Modernisation", "pt_name": "Modernização dos Navios Capitais",
        "en_desc": "Continuous upgrades in armor, anti-aircraft guns, and propulsion preserving fleet power.",
        "pt_desc": "Atualizações contínuas de blindagem, canhões antiaéreos e propulsão na esquadra."
    },
    "ITA_ww1_battaglione_aviatori": {
        "pic": "ITA_ww1_idea_21",
        "modifier": "air_ace_generation_chance_factor = 0.10 air_mission_efficiency = 0.05",
        "en_name": "Battaglione Aviatori", "pt_name": "Battaglione Aviatori",
        "en_desc": "Pioneering aviation military battalion testing early combat aircraft at Centocelle.",
        "pt_desc": "Batalhão pioneiro de aviação testando os primeiros aparelhos de combate em Centocelle."
    },
    "ITA_ww1_military_flight_schools": {
        "pic": "ITA_ww1_idea_22",
        "modifier": "air_accidents_factor = -0.10 air_training_xp_gain_factor = 0.05",
        "en_name": "Military Aviation Academies", "pt_name": "Academias de Aviação Militar",
        "en_desc": "Rigorous pilot training producing thousands of skilled combat fliers for the front.",
        "pt_desc": "Treinamento rigoroso formando milhares de pilotos de combate qualificados para o front."
    },
    "ITA_ww1_corpo_aeronautico_militare": {
        "pic": "ITA_ww1_idea_23",
        "modifier": "air_superiority_detect_factor = 0.05 air_superiority_efficiency = 0.05",
        "en_name": "Corpo Aeronautico Militare", "pt_name": "Corpo Aeronautico Militare",
        "en_desc": "Autonomous air corps coordinating observation, fighter combat, and heavy bombardment.",
        "pt_desc": "Corpo aéreo autônomo coordenando caças, reconhecimento e bombardeio de saturação."
    },
    "ITA_ww1_baracca_ace_tradition": {
        "pic": "ITA_ww1_idea_24",
        "modifier": "air_ace_generation_chance_factor = 0.20 air_attack_factor = 0.05",
        "en_name": "The Prancing Horse Tradition", "pt_name": "A Tradição do Cavalo Rampante",
        "en_desc": "Heroic fighter pilot spirit forged by Francesco Baracca and the Squadriglia degli Assi.",
        "pt_desc": "Espírito heroico dos pilotos de caça forjado por Francesco Baracca na Esquadrilha de Ases."
    },
    "ITA_ww1_douhet_air_doctrine": {
        "pic": "ITA_ww1_idea_25",
        "modifier": "air_strategic_bomber_bombing_factor = 0.10 air_bombing_targetting = 0.05",
        "en_name": "Douhet Strategic Air Doctrine", "pt_name": "Doutrina Aérea Estratégica de Douhet",
        "en_desc": "Independent strategic bombers destroying enemy industrial centers and communications.",
        "pt_desc": "Bombardeiros estratégicos independentes atingindo os centros industriais do adversário."
    },
    "ITA_ww1_independent_air_force_charter": {
        "pic": "ITA_ww1_idea_26",
        "modifier": "production_speed_buildings_factor = 0.05 air_doctrine_cost_factor = -0.10",
        "en_name": "Regia Aeronautica Foundations", "pt_name": "Bases da Regia Aeronautica",
        "en_desc": "Legislative charter creating an independent third armed service for the skies.",
        "pt_desc": "Estatuto legal criando a terceira força armada independente para o domínio dos céus."
    },
    "ITA_ww1_motorized_shock_cadres": {
        "pic": "ITA_ww1_idea_27",
        "modifier": "motorized_attack_factor = 0.05 army_speed_factor = 0.03",
        "en_name": "Motorized Armoured Squadrons", "pt_name": "Esquadrões Blindados Motorizados",
        "en_desc": "Fast armoured cars breaking through enemy lines and pursuing retreating columns.",
        "pt_desc": "Automóveis blindados velozes rompendo linhas inimigas e perseguindo colunas em retirada."
    }
}
