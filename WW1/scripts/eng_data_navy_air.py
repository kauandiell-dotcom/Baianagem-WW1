# scripts/eng_data_navy_air.py
# British Empire WW1 - Royal Navy, ASW, RFC & Royal Air Force (40 focuses)

NAVY_AIR_DATA = {
    "ENG_ww1_admiralty_fleet_survey": {
        "pt_t": "Inspeção da Frota do Almirantado",
        "en_t": "Admiralty Fleet Survey",
        "pt_d": "O Primeiro Lorde do Almirantado e o Primeiro Lorde do Mar Jackie Fisher avaliam a prontidão global da esquadra, reafirmando o 'Two-Power Standard'.",
        "en_d": "First Lord of the Admiralty and First Sea Lord Jackie Fisher survey the global fleet, reasserting the Two-Power Standard to ensure unmatched naval dominance.",
        "reward": """navy_experience = 30
add_political_power = 60"""
    },
    "ENG_ww1_the_naval_estimates": {
        "pt_t": "O Orçamento Naval de Winston Churchill",
        "en_t": "Churchill's Naval Estimates",
        "pt_d": "O orçamento naval de 1912 financia a rápida conversão das caldeiras da marinha para óleo combustível e a encomenda de novas divisões de encouraçados.",
        "en_d": "The ambitious 1912 naval appropriations finance the decisive transition to fuel oil propulsion and order cutting-edge dreadnought squadrons.",
        "reward": """133 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = dockyard
        level = 2
        instant_build = yes
    }
}
add_navy_experience = 15"""
    },
    "ENG_ww1_dreadnought_construction_planning": {
        "pt_t": "Super-Dreadnoughts da Classe Queen Elizabeth",
        "en_t": "Queen Elizabeth Class Super-Dreadnoughts",
        "pt_d": "Encouraçados velozes equipados com devastadores canhões de 15 polegadas e blindagem espessa asseguram supremacia de fogo absoluto em duelos de linha.",
        "en_d": "Fast dreadnoughts armed with formidable 15-inch guns and thick armor plating guarantee overwhelming firepower in any North Sea battle-line duel.",
        "reward": """add_tech_bonus = {
    name = bb_bonus
    bonus = 1.0
    uses = 2
    category = bb_tech
}
add_navy_experience = 20"""
    },
    "ENG_ww1_battlecruiser_squadron_planning": {
        "pt_t": "Esquadrões de Cruzadores de Batalha de Beatty",
        "en_t": "Beatty's Battlecruiser Squadrons",
        "pt_d": "Navios velozes da classe Lion e Tiger sob o Almirante David Beatty garantem o reconhecimento armado e caça aos cruzadores alemães em alta velocidade.",
        "en_d": "Swift capital ships of the Lion and Tiger classes under Admiral David Beatty provide aggressive reconnaissance and hunt down enemy raiders at 28 knots.",
        "reward": """add_tech_bonus = {
    name = bc_bonus
    bonus = 1.0
    uses = 1
    category = bc_tech
}
add_navy_experience = 15"""
    },
    "ENG_ww1_destroyer_flotilla_planning": {
        "pt_t": "Flotilhas de Contratorpedeiros de Alto-Mar",
        "en_t": "Fleet Destroyer Flotillas",
        "pt_d": "Construção maciça de contratorpedeiros das classes V e W, equipados com tubos de torpedos triplos e canhões rápidos para escolta da Grand Fleet.",
        "en_d": "Mass construction of V and W class fleet destroyers armed with high-velocity 4-inch guns and torpedo tubes to screen capital ship battle lines.",
        "reward": """add_tech_bonus = {
    name = dd_bonus
    bonus = 1.0
    uses = 2
    category = dd_tech
}
131 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_submarine_service_development": {
        "pt_t": "Desenvolvimento da Força de Submarinos da Marinha Real",
        "en_t": "Royal Navy Submarine Service",
        "pt_d": "Submarinos oceânicos das classes E e J patrulham as costas alemãs e o Mar Báltico, torpedeando navios de guerra e comboios de minério de ferro inimigos.",
        "en_d": "Ocean-going E-class submarines penetrate the Heligoland Bight and the Baltic Sea, sinking enemy cruisers and disrupting iron ore convoys.",
        "reward": """add_tech_bonus = {
    name = sub_bonus
    bonus = 1.0
    uses = 2
    category = ss_tech
}
navy_experience = 25
126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_naval_gunnery_calibration": {
        "pt_t": "Sistemas de Direção de Tiro e Calibração Balística",
        "en_t": "Director Firing and Gunnery Calibration",
        "pt_d": "A introdução das torres de controle de tiro de Sir Percy Scott e mesas mecânicas Dreyer confere precisão cirúrgica aos disparos em longa distância.",
        "en_d": "Adoption of Sir Percy Scott's director firing towers and Dreyer mechanical fire-control tables endows British salvos with devastating long-range accuracy.",
        "reward": """add_tech_bonus = {
    name = naval_gunnery_bonus
    bonus = 1.0
    uses = 1
    category = naval_equipment
}
navy_experience = 20"""
    },
    "ENG_ww1_the_north_sea_watch": {
        "pt_t": "A Patrulha do Norte no Mar do Marte",
        "en_t": "The Northern Patrol",
        "pt_d": "O 10º Esquadrão de Cruzadores vigia as passagens entre a Escócia, Ilhas Faroé e Noruega em mares bravios, interceptando qualquer carga destinada à Alemanha.",
        "en_d": "The 10th Cruiser Squadron patrols the Arctic passages between Scotland and Iceland through stormy seas, turning away all merchantmen bearing enemy cargo.",
        "reward": """navy_experience = 25
add_war_support = 0.05"""
    },
    "ENG_ww1_grand_fleet_maintenance": {
        "pt_t": "A Grand Fleet em Scapa Flow",
        "en_t": "The Grand Fleet at Scapa Flow",
        "pt_d": "Sob o comando do Almirante Sir John Jellicoe, a maior concentração de couraçados da história aguarda em prontidão permanente nas ilhas Órcades.",
        "en_d": "Under Admiral Sir John Jellicoe, the greatest concentration of dreadnoughts in world history remains permanently fueled and manned at Scapa Flow.",
        "reward": """swap_ideas = {
    remove_idea = ENG_two_power_standard
    add_idea = ENG_two_power_standard_t2
}
125 = {
    add_building_construction = {
        type = naval_base
        level = 1
        instant_build = yes
    }
}
navy_experience = 25"""
    },
    "ENG_ww1_merchant_shipping_register": {
        "pt_t": "Registro Geral da Marinha Mercante",
        "en_t": "Merchant Shipping Register",
        "pt_d": "Milhares de vapores comerciais britânicos são catalogados e colocados sob a autoridade do Almirantado para assegurar as linhas de vida imperiais.",
        "en_d": "Thousands of British merchantmen are inventoried and placed under Admiralty scheduling to guarantee food and raw material imports across the globe.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy_1
    amount = 175
    producer = ENG
}
add_political_power = 40"""
    },
    "ENG_ww1_maritime_blockade_coordination": {
        "pt_t": "O Bloqueio Distante da Alemanha",
        "en_t": "The Distant Maritime Blockade",
        "pt_d": "O bloqueio naval britânico sufoca as importações de salitre, borracha e cereais das Potências Centrais, desgastando sua capacidade econômica de sustentar a guerra.",
        "en_d": "The stranglehold of the Royal Navy blockade cuts off vital German imports of nitrates, rubber, and food, grinding down the Central Powers' home front.",
        "reward": """navy_experience = 30
add_equipment_to_stockpile = {
    type = convoy
    amount = 80
    producer = ENG
}"""
    },
    "ENG_ww1_hydrophone_trials": {
        "pt_t": "Ensaios com Hidrofones e Escuta Submarina",
        "en_t": "Hydrophone Detection Trials",
        "pt_d": "Cientistas da Marinha desenvolvem hidrofones subaquáticos direcionais capazes de escutar os motores e hélices dos U-boats alemães em imersão.",
        "en_d": "Admiralty researchers pioneer directional underwater hydrophones, enabling patrol craft to track submerged U-boat propeller vibrations.",
        "reward": """add_tech_bonus = {
    name = asw_sonar_bonus
    bonus = 1.0
    uses = 1
    category = asw_tech
}
add_navy_experience = 15"""
    },
    "ENG_ww1_depth_charge_trials": {
        "pt_t": "Cargas de Profundidade Tipo D e Lançadores",
        "en_t": "Type D Depth Charge Trials",
        "pt_d": "A arma definitiva anti-submarina: cilindros de alto explosivo acionados por pressão hidrostática que esmagam o casco de submarinos alemães submersos.",
        "en_d": "The definitive anti-submarine weapon: hydrostatic pressure-detonated canisters that shatter submerged U-boat pressure hulls with catastrophic force.",
        "reward": """add_tech_bonus = {
    name = asw_bonus
    bonus = 1.0
    uses = 1
    category = dd_tech
}
navy_experience = 20"""
    },
    "ENG_ww1_convoy_system_organisation": {
        "pt_t": "Implementação do Sistema Obrigatório de Comboios",
        "en_t": "The Convoy System Organisation",
        "pt_d": "A decisão histórica de Lloyd George em 1917 de navegar mercantes em grupos protegidos por destróieres e aeronaves reduz as perdas de navios a quase zero.",
        "en_d": "Lloyd George's historic 1917 mandate grouping merchant ships under naval destroyer escort dramatically breaks the unrestricted submarine campaign.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy
    amount = 100
    producer = ENG
}
navy_experience = 25"""
    },
    "ENG_ww1_escort_refit_contracts": {
        "pt_t": "Contratos de Conversão de Escoltas e Caça-Submarinos",
        "en_t": "Escort Refit Contracts",
        "pt_d": "Traineiras de pesca, iates e navios de passageiros são convertidos com canhões de 12 libras e cargas de profundidade para a patrulha das águas metropolitanas.",
        "en_d": "Civilian trawlers, coastal craft, and yachts are armed with 12-pounder guns and depth charge racks to saturate coastal approaches against raiders.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy_1
    amount = 120
    producer = ENG
}
125 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_naval_signals_and_direction_finding": {
        "pt_t": "Estações de Radiogoniometria (HF/DF Naval)",
        "en_t": "Naval Direction Finding Stations",
        "pt_d": "Uma cadeia de antenas goniométricas na costa britânica triangula transmissões de rádio alemãs instantaneamente, alertando patrulhas para emboscadas.",
        "en_d": "A coastal chain of wireless direction-finding stations instantly triangulates enemy radio transmissions, guiding patrol groups directly to U-boats.",
        "reward": """add_tech_bonus = {
    name = signals_bonus
    bonus = 1.0
    uses = 1
    category = electronics
}
navy_experience = 20"""
    },
    "ENG_ww1_mediterranean_convoy_liaison": {
        "pt_t": "Rede de Comboios do Mediterrâneo",
        "en_t": "Mediterranean Convoy Liaison",
        "pt_d": "Bases estratégicas em Gibraltar, Malta e Alexandria organizam a proteção contínua de cargueiros de trigo da Austrália e do Canal de Suez.",
        "en_d": "Naval coordination across Gibraltar, Malta, and Alexandria shields vital trade arteries transporting Indian and Australian troops through Suez.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy
    amount = 60
    producer = ENG
}
navy_experience = 15"""
    },
    "ENG_ww1_the_postwar_fleet_review": {
        "pt_t": "A Revista da Frota em Spithead",
        "en_t": "The Postwar Spithead Fleet Review",
        "pt_d": "O Rei George V passa em revista a frota triunfante em Spithead. Dezenas de milhas de navios de aço celebram a soberania britânica dos sete mares.",
        "en_d": "King George V reviews the victorious Royal Navy at Spithead. Miles of steel warships celebrate unshakeable British mastery of the oceans.",
        "reward": """add_political_power = 75
add_stability = 0.06
set_country_flag = ENG_ww1_spithead_review_held"""
    },
    "ENG_ww1_naval_budget_retrenchment": {
        "pt_t": "Ajuste Orçamentário da Marinha (Tratado de Washington)",
        "en_t": "Naval Budget Retrenchment",
        "pt_d": "O desarmamento naval negociado evita uma corrida armamentista ruinosa contra os Estados Unidos, mantendo a paridade e economizando milhões de libras.",
        "en_d": "Negotiated capital ship limits prevent a ruinous naval arms race while retaining qualitative British superiority and curbing public expenditure.",
        "reward": """123 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}
add_political_power = 60"""
    },
    "ENG_ww1_naval_technical_lessons": {
        "pt_t": "Lições Técnicas da Guerra no Mar (Jutlândia)",
        "en_t": "Technical Lessons of Naval Warfare",
        "pt_d": "A análise das perdas de cruzadores de batalha na Batalha da Jutlândia conduz à reformulação do manuseio de cordite, blindagem horizontal e controle de danos.",
        "en_d": "Exhaustive tactical reviews of Jutland reform magazine flash-protection doors, deck armor thickness, and damage control procedures for future capital ships.",
        "reward": """add_tech_bonus = {
    name = naval_doctrine_bonus
    bonus = 1.0
    uses = 2
    category = naval_doctrine
}
add_navy_experience = 30"""
    },
    "ENG_ww1_the_air_battalion_experiments": {
        "pt_t": "Experimentos do Batalhão Aéreo dos Engenheiros Reais",
        "en_t": "Air Battalion Royal Engineers Experiments",
        "pt_d": "Balões de observação amarrados e monoplanos primitivos na planície de Salisbury testam a aplicação militar da aviação para o exército.",
        "en_d": "Pioneering tethered balloons and fragile monoplanes on Salisbury Plain test military applications of aerial reconnaissance for the Army.",
        "reward": """add_air_experience = 15
add_tech_bonus = {
    name = early_fighter_bonus
    bonus = 1.0
    uses = 1
    category = light_fighter
}"""
    },
    "ENG_ww1_royal_flying_corps_organisation": {
        "pt_t": "Criação do Royal Flying Corps (RFC)",
        "en_t": "Royal Flying Corps Organisation",
        "pt_d": "Fundado em 1912 pelo Rei George V com o lema 'Per Ardua ad Astra', o RFC prepara esquadrilhas de observadores para operar junto com a BEF na França.",
        "en_d": "Founded in 1912 under the motto 'Per Ardua ad Astra', the RFC trains disciplined flying squadrons to provide tactical eyes for British field armies.",
        "reward": """air_experience = 25
add_tech_bonus = {
    name = rfc_bonus
    bonus = 1.0
    uses = 2
    category = air_equipment
}"""
    },
    "ENG_ww1_military_pilot_instruction": {
        "pt_t": "A Escola Central de Voo em Upavon",
        "en_t": "Central Flying School Pilot Instruction",
        "pt_d": "Instrutores veteranos padronizam o treinamento acrobático, recuperação de estol e navegação aérea em Upavon, formando aviadores de elite.",
        "en_d": "Veteran instructors at Upavon institutionalize rigorous stall recovery, formation flying, and aerial navigation to produce top-tier combat pilots.",
        "reward": """air_experience = 20
add_command_power = 20"""
    },
    "ENG_ww1_aerial_reconnaissance_reports": {
        "pt_t": "Reconhecimento Aéreo e Mapeamento de Trincheiras",
        "en_t": "Aerial Reconnaissance and Trench Mapping",
        "pt_d": "Câmeras aéreas acopladas à fuselagem fotografam as posições inimigas diariamente, fornecendo ao Estado-Maior mapas detalhados das defesas alemãs.",
        "en_d": "Fuselage-mounted cameras photograph enemy sectors daily, supplying the General Staff with up-to-the-minute trench maps of the Western Front.",
        "reward": """add_tech_bonus = {
    name = air_recon_bonus
    bonus = 1.0
    uses = 1
    category = air_doctrine
}
add_air_experience = 15"""
    },
    "ENG_ww1_royal_naval_air_service_organisation": {
        "pt_t": "Criação do Royal Naval Air Service (RNAS)",
        "en_t": "Royal Naval Air Service Organisation",
        "pt_d": "Sob o estímulo direto de Winston Churchill, a aviação naval ganha autonomia para caçar submarinos, defender bases e operar bombardeiros pesados.",
        "en_d": "Championed by Winston Churchill, the RNAS develops specialized naval aircraft to patrol coastlines, hunt U-boats, and attack Zeppelin sheds.",
        "reward": """navy_experience = 20
air_experience = 20
add_tech_bonus = {
    name = rnas_bonus
    bonus = 1.0
    uses = 2
    category = air_equipment
}"""
    },
    "ENG_ww1_wireless_and_aircraft_observation": {
        "pt_t": "Transmissão Sem Fio para Calibração de Artilharia",
        "en_t": "Wireless Artillery Observation",
        "pt_d": "Aparelhos de rádio transmissores a bordo dos aviões corrigem os disparos das baterias britânicas em tempo real, devastando alvos ocultos.",
        "en_d": "Compact aircraft wireless transmitters send real-time Morse corrections directly to heavy battery gunners, obliterating hidden enemy redoubts.",
        "reward": """add_tech_bonus = {
    name = air_doc_bonus
    bonus = 1.0
    uses = 1
    category = air_doctrine
}
add_air_experience = 15"""
    },
    "ENG_ww1_bristol_scout_trials": {
        "pt_t": "Ensaios com o Caça Bristol Scout",
        "en_t": "Bristol Scout Speed Trials",
        "pt_d": "O ágil biplano Bristol Scout abre caminho para aeronaves monoposto de alta velocidade dedicadas à superioridade aérea e interceptação.",
        "en_d": "The agile Bristol Scout establishes high-speed single-seat biplanes as the premier instrument for aggressive air combat and reconnaissance escort.",
        "reward": """add_tech_bonus = {
    name = fighter_tech_bonus
    bonus = 1.0
    uses = 2
    category = light_fighter
}
add_air_experience = 15"""
    },
    "ENG_ww1_naval_seaplane_stations": {
        "pt_t": "Estações de Hidroaviões e Navios-Aeródromo Pioneiros",
        "en_t": "Naval Seaplane Stations and Aircraft Carriers",
        "pt_d": "A Marinha Real pioneira converte o HMS Argus e o HMS Furious em navios com conveses corridos de voo, inventando o porta-aviões moderno.",
        "en_d": "The Royal Navy converts HMS Argus and HMS Furious with continuous flight decks, pioneering the modern aircraft carrier and shipboard launch tactics.",
        "reward": """add_tech_bonus = {
    name = carrier_bonus
    bonus = 1.0
    uses = 1
    category = cv_tech
}
add_equipment_to_stockpile = {
    type = nav_bomber_equipment_1
    amount = 50
    producer = ENG
}"""
    },
    "ENG_ww1_aircraft_production_contracts": {
        "pt_t": "Contratos Nacionais de Produção Aeronáutica",
        "en_t": "National Aircraft Production Contracts",
        "pt_d": "Fábricas da Sopwith, De Havilland, Vickers e Handley Page recebem vultosos contratos estatais, tornando a indústria britânica a mais produtiva do mundo.",
        "en_d": "Sopwith, De Havilland, Vickers, and Handley Page receive sweeping government orders, propelling British aircraft production to world-leading scale.",
        "reward": """126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}
add_air_experience = 15"""
    },
    "ENG_ww1_fighter_squadron_instruction": {
        "pt_t": "Doutrina de Caça dos Ases do RFC (Sopwith Camel)",
        "en_t": "RFC Fighter Squadron Instruction",
        "pt_d": "Ases como Mick Mannock e Billy Bishop, voando nos lendários Sopwith Camel e SE5a, dominam o espaço aéreo sobre os campos da França.",
        "en_d": "Combat doctrines developed by aces like Mick Mannock flying agile Sopwith Camels and SE5as secure hard-fought air supremacy over the Western Front.",
        "reward": """air_experience = 25
add_tech_bonus = {
    name = fighter_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}"""
    },
    "ENG_ww1_artillery_spotting_liaison": {
        "pt_t": "Oficiais de Ligação Aérea com a Artilharia",
        "en_t": "Artillery Spotting Liaison",
        "pt_d": "Protocolos estreitos de ligação entre observadores aéreos do RE8 e comandos de corpos de artilharia garantem barragens devastadoras.",
        "en_d": "Close-knit communication codes between RE8 spotters and corps artillery headquarters maximize counter-battery lethality.",
        "reward": """air_experience = 15
army_experience = 15"""
    },
    "ENG_ww1_night_flying_experiments": {
        "pt_t": "Táticas de Voo Noturno e Holofotes",
        "en_t": "Night Flying Experiments",
        "pt_d": "Iluminação de pistas e instrumentos fosforescentes no painel permitem interceptações aéreas na escuridão contra invasores alemães.",
        "en_d": "Runway flare paths and luminescent dashboard dials enable skilled night-fighter pilots to intercept nocturnal enemy intruders in total darkness.",
        "reward": """add_tech_bonus = {
    name = night_fighting_bonus
    bonus = 1.0
    uses = 1
    category = air_doctrine
}
add_air_experience = 15"""
    },
    "ENG_ww1_bomber_range_experiments": {
        "pt_t": "Bombardeiros Pesados Handley Page O/400",
        "en_t": "Handley Page Heavy Bomber Development",
        "pt_d": "O colossal bimotor Handley Page O/400 é capaz de carregar quase uma tonelada de bombas, permitindo ataques estratégicos profundos na Renânia.",
        "en_d": "The massive twin-engine Handley Page O/400 carries heavy bomb loads, enabling the independent bombing of industrial targets along the Rhine.",
        "reward": """add_tech_bonus = {
    name = strat_bomber_bonus
    bonus = 1.0
    uses = 2
    category = strat_bomber
}
add_equipment_to_stockpile = {
    type = strat_bomber_equipment_1
    amount = 30
    producer = ENG
}"""
    },
    "ENG_ww1_aircraft_engine_reliability": {
        "pt_t": "Motores Aeronáuticos Rolls-Royce Eagle e Falcon",
        "en_t": "Rolls-Royce Aero Engine Reliability",
        "pt_d": "Os motores V12 Rolls-Royce Eagle estabelecem um padrão incomparável de potência, resistência mecânica e altitude de operação.",
        "en_d": "Rolls-Royce Eagle and Falcon V12 liquid-cooled engines establish world-beating standards of horsepower, mechanical endurance, and high-altitude speed.",
        "reward": """add_tech_bonus = {
    name = engine_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}
air_experience = 15"""
    },
    "ENG_ww1_home_air_defence_coordination": {
        "pt_t": "Comando de Defesa Antiaérea de Londres (LADA)",
        "en_t": "London Air Defence Coordination",
        "pt_d": "A integração de baterias antiaéreas, holofotes potentes e caças noturnos derrota as incursões de zepelins e bombardeiros Gotha contra Londres.",
        "en_d": "Integration of anti-aircraft gun rings, searchlight batteries, and night fighters under General Ashmore neutralizes German Gotha raids on London.",
        "reward": """air_experience = 20
add_stability = 0.05"""
    },
    "ENG_ww1_the_independent_air_service_debate": {
        "pt_t": "O Relatório Smuts e a Força Aérea Independente",
        "en_t": "The Smuts Report on Independent Air Power",
        "pt_d": "O General Jan Smuts apresenta seu memorando histórico recomendando a fusão do RFC e do RNAS em um ministério do ar autônomo com doutrina própria.",
        "en_d": "General Jan Smuts presents his visionary report recommending the complete amalgamation of army and naval aviation into an autonomous air ministry.",
        "reward": """air_experience = 25
add_political_power = 40"""
    },
    "ENG_ww1_royal_air_force_unification": {
        "pt_t": "A Criação da Royal Air Force (RAF)",
        "en_t": "The Royal Air Force Unification",
        "pt_d": "Em 1 de abril de 1918, nasce a primeira força aérea independente do planeta sob Sir Hugh Trenchard, consolidando o poder aéreo como arma decisiva.",
        "en_d": "On 1 April 1918, the world's first independent air service is born under Sir Hugh Trenchard, cementing air power as an equal and decisive military arm.",
        "reward": """air_experience = 35
add_tech_bonus = {
    name = raf_bonus
    bonus = 1.0
    uses = 2
    category = air_doctrine
}"""
    },
    "ENG_ww1_postwar_aircraft_demobilisation": {
        "pt_t": "Desmobilização Aérea do Pós-Guerra",
        "en_t": "Postwar Aircraft Demobilisation",
        "pt_d": "Venda ordeira de excedentes de biplanos e transição de milhares de mecânicos e aviadores para as empresas aeronáuticas civis nascentes.",
        "en_d": "Orderly liquidation of wartime surplus biplanes and transition of skilled aviators and mechanics into the commercial aircraft manufacturing sector.",
        "reward": """add_political_power = 50
add_stability = 0.04"""
    },
    "ENG_ww1_civil_aviation_research": {
        "pt_t": "Pesquisa de Aviação Comercial e Imperial Airways",
        "en_t": "Civil Aviation and Imperial Airways",
        "pt_d": "Adaptação de bombardeiros pesados para voos de passageiros e mala postal, conectando Londres ao Cairo, Bagdá, Nova Délhi e Sydney.",
        "en_d": "Conversion of multi-engine bombers for long-range mail and passenger service, establishing pioneering air routes connecting London across the Empire.",
        "reward": """add_tech_bonus = {
    name = aviation_bonus
    bonus = 1.0
    uses = 1
    category = air_equipment
}
add_political_power = 40"""
    },
    "ENG_ww1_a_sustainable_air_establishment": {
        "pt_t": "A Fundação da Força Aérea Permanente de Trenchard",
        "en_t": "Trenchard's Permanent RAF Establishment",
        "pt_d": "A criação do RAF College em Cranwell e a doutrina de controle aéreo imperial garantem a sobrevivência e primazia da RAF no tempo de paz.",
        "en_d": "Founding RAF College Cranwell and developing imperial air-control doctrine ensures the permanent survival and prestige of the Royal Air Force.",
        "reward": """air_experience = 25
add_stability = 0.05"""
    }
}
