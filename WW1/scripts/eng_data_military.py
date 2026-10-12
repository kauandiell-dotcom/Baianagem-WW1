# scripts/eng_data_military.py
# British Empire WW1 - Army, Expeditions, Tactics & Tank Warfare (40 focuses)

MILITARY_DATA = {
    "ENG_ww1_the_haldane_establishment": {
        "pt_t": "As Reformas do Exército de Lord Haldane",
        "en_t": "The Haldane Army Establishment",
        "pt_d": "A reorganização estrutural conduzida pelo Secretário de Guerra Richard Haldane cria o Estado-Maior Imperial, a Força Territorial e a moderna Força Expedicionária.",
        "en_d": "Secretary of State for War Richard Haldane reorganizes the British military, creating the Imperial General Staff, the Territorial Force, and an elite Expeditionary Force.",
        "reward": """army_experience = 25
add_political_power = 60"""
    },
    "ENG_ww1_territorial_force_camps": {
        "pt_t": "Acampamentos de Instrução da Força Territorial",
        "en_t": "Territorial Force Training Camps",
        "pt_d": "Os batalhões de reservistas voluntários da Força Territorial realizam manobras anuais de verão, treinando tiro de fuzil e marcha sob disciplina militar estrita.",
        "en_d": "Part-time volunteers of the Territorial Force undergo rigorous annual field maneuvers, rifle marksmanship courses, and brigade-level staff exercises.",
        "reward": """add_manpower = 50000
add_army_experience = 10
add_equipment_to_stockpile = {
    type = infantry_equipment_0
    amount = 5000
    producer = ENG
}"""
    },
    "ENG_ww1_the_special_reserve": {
        "pt_t": "A Reserva Especial de Substituição",
        "en_t": "The Special Reserve Depots",
        "pt_d": "Batalhões de Reserva Especial são organizados em cada regimento britânico para receber e treinar recrutas, garantindo fluxo ininterrupto de reposições para o front.",
        "en_d": "Special Reserve battalions established at regimental depots maintain rapid mobilization structures to draft and train immediate reinforcements for regular units.",
        "reward": """add_manpower = 35000
add_army_experience = 10"""
    },
    "ENG_ww1_officer_training_corps": {
        "pt_t": "Corpo de Treinamento de Oficiais Universitários (OTC)",
        "en_t": "Officer Training Corps",
        "pt_d": "Unidades de cadetes em Oxford, Cambridge e escolas públicas britânicas formam milhares de subalternos cultos e decididos, prontos para comandar pelotões de infantaria.",
        "en_d": "Officer Training Corps contingents at British universities and public schools generate a disciplined reserve of junior officers ready for immediate commissioning.",
        "reward": """army_experience = 20
add_command_power = 30
add_manpower = 25000"""
    },
    "ENG_ww1_regular_army_mobilisation": {
        "pt_t": "Mobilização das Divisões Regulares",
        "en_t": "Regular Army Mobilisation",
        "pt_d": "Planos ferroviários detalhados concentram as seis divisões regulares da Grã-Bretanha e a Divisão de Cavalaria nos portos de embarque de Southampton e Dover.",
        "en_d": "Meticulous mobilization timetables concentrate Britain's six regular infantry divisions and Cavalry Division at southern ports within days of the war proclamation.",
        "reward": """add_war_support = 0.05
add_army_experience = 15
add_political_power = 40"""
    },
    "ENG_ww1_army_service_corps_offices": {
        "pt_t": "Diretoria de Intendência do Army Service Corps",
        "en_t": "Army Service Corps Logistics",
        "pt_d": "A introdução de caminhões motorizados e depósitos avançados de munição pelo Army Service Corps assegura que as tropas nunca fiquem sem rações e cartuchos.",
        "en_d": "The rapid expansion of mechanical motor transport and forward railhead depots under the Army Service Corps guarantees uninterrupted battlefield supply lines.",
        "reward": """add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 150
    producer = ENG
}
add_tech_bonus = {
    name = motorized_bonus
    bonus = 1.0
    uses = 1
    category = motorized_equipment
}"""
    },
    "ENG_ww1_the_expeditionary_establishment": {
        "pt_t": "A Força Expedicionária Britânica (BEF)",
        "en_t": "The British Expeditionary Force Establishment",
        "pt_d": "Os 'Old Contemptibles' cruzam o Canal da Mancha. Considerado o exército profissional mais bem treinado do planeta, cada soldado é capaz de disparar 15 tiros precisos por minuto.",
        "en_d": "The 'Old Contemptibles' cross into France. Recognized as the finest marksmanship force in the world, each regular soldier delivers 15 aimed rounds a minute.",
        "reward": """army_experience = 25
add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 4000
    producer = ENG
}"""
    },
    "ENG_ww1_kitchener_new_armies": {
        "pt_t": "O Apelo de Kitchener: 'Your Country Needs You'",
        "en_t": "Kitchener's New Armies",
        "pt_d": "O Secretário de Guerra Lord Kitchener prevê uma luta de longos anos e convoca a juventude imperial. Milhões de voluntários acorrem aos postos de recrutamento.",
        "en_d": "Foreseeing a protracted war of attrition, Lord Kitchener issues his iconic national summons, rallying millions of enthusiastic volunteers into the 'New Armies'.",
        "reward": """swap_ideas = {
    remove_idea = ENG_professional_bef
    add_idea = ENG_professional_bef_t2
}
add_manpower = 150000
add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 10000
    producer = ENG
}"""
    },
    "ENG_ww1_the_pals_battalion_system": {
        "pt_t": "Batalhões de Camaradas (Pals Battalions)",
        "en_t": "The Pals Battalion System",
        "pt_d": "Homens de uma mesma cidade, clube de futebol, ferrovia ou universidade se alistam juntos, forjando uma coesão fraterna lendária nos campos de batalha da França.",
        "en_d": "Men from identical towns, factory workshops, sports clubs, and universities enlist side-by-side, forging unparalleled unit cohesion and esprit de corps.",
        "reward": """add_manpower = 80000
add_war_support = 0.05"""
    },
    "ENG_ww1_the_rifle_training_depots": {
        "pt_t": "Depósitos de Instrução de Tiro com Lee-Enfield",
        "en_t": "Lee-Enfield Rifle Training Depots",
        "pt_d": "Instrução intensiva de tiro rápido com o lendário fuzil Short Magazine Lee-Enfield (SMLE Mk III) confere às tropas britânicas uma potência de fogo fulminante.",
        "en_d": "Intensive rapid-fire training with the iconic Short Magazine Lee-Enfield (SMLE Mk III) turns civilian recruits into lethal marksmen capable of the legendary 'mad minute'.",
        "reward": """127 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 10000
    producer = ENG
}
add_army_experience = 10"""
    },
    "ENG_ww1_field_medical_organisation": {
        "pt_t": "Organização Médica e Hospitalar do RAMC",
        "en_t": "Royal Army Medical Corps Organisation",
        "pt_d": "Ambulâncias motorizadas, hospitais de campanha de evacuação rápida e antissépticos modernos salvam as vidas de centenas de milhares de feridos em combate.",
        "en_d": "Motor ambulance convoys, forward casualty clearing stations, and blood transfusion protocols established by the RAMC dramatically reduce frontline mortality.",
        "reward": """add_tech_bonus = {
    name = medical_bonus
    bonus = 1.0
    uses = 2
    category = support_tech
}
add_manpower = 20000"""
    },
    "ENG_ww1_the_artillery_observation_school": {
        "pt_t": "Escola de Observação e Balística de Artilharia",
        "en_t": "The Artillery Observation School",
        "pt_d": "Cursos avançados em Larkhill desenvolvem técnicas de tiro indireto, calibração meteorológica e cooperação entre balões de observação e canhões QF de 18 libras.",
        "en_d": "Advanced gunnery courses at Larkhill pioneer indirect predicted fire, meteorological correction data, and close cooperation between spotters and 18-pounder batteries.",
        "reward": """128 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}
add_tech_bonus = {
    name = artillery_research_bonus
    bonus = 1.0
    uses = 2
    category = artillery
}
add_army_experience = 15"""
    },
    "ENG_ww1_machine_gun_corps_formation": {
        "pt_t": "Criação do Machine Gun Corps (MGC)",
        "en_t": "Machine Gun Corps Formation",
        "pt_d": "Reunindo metralhadoras Vickers .303 resfriadas a água sob um corpo especializado em Belton Park, a infantaria britânica adquire uma cortina defensiva intransponível.",
        "en_d": "Concentrating water-cooled Vickers .303 machine guns into a specialized branch at Belton Park endows British sectors with overwhelming sustained firepower.",
        "reward": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 5000
    producer = ENG
}
army_experience = 25"""
    },
    "ENG_ww1_trench_mortar_sections": {
        "pt_t": "Seções de Morteiros de Trincheira Stokes",
        "en_t": "Stokes Trench Mortar Sections",
        "pt_d": "A invenção do morteiro portátil Stokes de 3 polegadas por Sir Wilfred Stokes fornece apoio de fogo de curto alcance devastador diretamente nas trincheiras inimigas.",
        "en_d": "The adoption of Sir Wilfred Stokes' 3-inch trench mortar equips frontline infantry battalions with instant, high-angle bombardment to demolish enemy redoubts.",
        "reward": """add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 100
    producer = ENG
}
add_tech_bonus = {
    name = mortar_bonus
    bonus = 1.0
    uses = 1
    category = artillery
}"""
    },
    "ENG_ww1_gas_protection_training": {
        "pt_t": "Instrução Antigás e Máscaras Box Respirator",
        "en_t": "Gas Protection and Box Respirator Training",
        "pt_d": "A distribuição em larga escala da máscara Small Box Respirator e treinamentos em câmaras de gás neutralizam o terror das armas químicas nas trincheiras.",
        "en_d": "Universal issuance of the Small Box Respirator and realistic gas-chamber drills inoculate British soldiers against the lethal menace of chemical warfare.",
        "reward": """add_tech_bonus = {
    name = support_bonus
    bonus = 1.0
    uses = 1
    category = support_tech
}
army_experience = 15"""
    },
    "ENG_ww1_the_infantry_training_directorate": {
        "pt_t": "Diretoria de Treinamento Tático de Infantaria",
        "en_t": "The Infantry Training Directorate",
        "pt_d": "A reorganização da seção de infantaria em equipes combinadas de fuzileiros, granadeiros, atiradores Lewis e morteiros revoluciona o combate de assalto.",
        "en_d": "Reorganizing the platoon into mutually supporting specialists—riflemen, bombers, Lewis gunners, and rifle grenadiers—transforms British assault tactics.",
        "reward": """add_tech_bonus = {
    name = land_doc_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}
add_army_experience = 20"""
    },
    "ENG_ww1_combined_arms_staff_courses": {
        "pt_t": "Cursos de Armas Combinadas do Estado-Maior",
        "en_t": "Combined Arms Staff Courses",
        "pt_d": "Oficiais do Estado-Maior são instruídos a integrar tanques, aviação tática de ataque ao solo, artilharia rastejante e infantaria em ofensivas sincronizadas.",
        "en_d": "Staff colleges train commanders to orchestrate tanks, low-flying air support, creeping barrages, and infantry assaults into a seamless, synchronized hammer blow.",
        "reward": """army_experience = 30
add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}"""
    },
    "ENG_ww1_the_demobilisation_register": {
        "pt_t": "Cadastro de Desmobilização Militar",
        "en_t": "The Demobilisation Register",
        "pt_d": "Classificação metódica dos combatentes por tempo de serviço e prioridade econômica para assegurar a desmobilização ordenada sem convulsão social.",
        "en_d": "Methodical indexing of servicemen by civilian industrial necessity guarantees fair, riot-free demobilisation once arms are laid down.",
        "reward": """add_political_power = 50
add_stability = 0.04"""
    },
    "ENG_ww1_a_smaller_professional_force": {
        "pt_t": "Reestruturação do Exército Profissional Pós-Guerra",
        "en_t": "A Smaller Professional Postwar Force",
        "pt_d": "Retorno ao modelo de forças expedicionárias profissionais altamente treinadas e mecanizadas, adequadas à doutrina de contenção imperial global.",
        "en_d": "Return to an all-volunteer, highly motorized cadre army optimized for rapid imperial policing, garrisons, and expeditionary interventions.",
        "reward": """army_experience = 25
add_stability = 0.05"""
    },
    "ENG_ww1_territorial_defence_renewal": {
        "pt_t": "Renovação da Defesa Territorial Metropolitana",
        "en_t": "Territorial Defence Renewal",
        "pt_d": "A Força Territorial é revigorada com equipamento moderno excedente de guerra, servindo como esteio inquebrantável da defesa das Ilhas Britânicas.",
        "en_d": "The Territorial Army is reconstituted with surplus war materiel, forming an inexpensive yet formidable backbone for home island defense.",
        "reward": """add_manpower = 40000
army_experience = 15"""
    },
    "ENG_ww1_the_channel_mobilisation_timetable": {
        "pt_t": "Cronograma de Mobilização do Canal da Mancha",
        "en_t": "The Channel Mobilisation Timetable",
        "pt_d": "Embarcações requisitadas e comboios de tropas sob escolta naval realizam a travessia diária do Canal sem a perda de um único soldado britânico por ação inimiga.",
        "en_d": "Requisitioned cross-channel steamers and escorted transports execute clockwork sailings, moving men, horses, and guns to France with zero casualties.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy
    amount = 50
    producer = ENG
}
navy_experience = 15"""
    },
    "ENG_ww1_embarkation_depot_preparation": {
        "pt_t": "Preparação dos Portos de Embarque",
        "en_t": "Embarkation Depot Preparation",
        "pt_d": "Grandes depósitos de suprimentos, carvoeiros e instalações de guindastes pesados em Southampton e Portsmouth garantem carregamento dia e noite.",
        "en_d": "Vast staging depots, heavy crane networks, and supply camps at Southampton and Portsmouth ensure 24-hour round-the-clock embarkation cycles.",
        "reward": """127 = {
    add_building_construction = {
        type = naval_base
        level = 1
        instant_build = yes
    }
}
add_army_experience = 10"""
    },
    "ENG_ww1_the_bef_deployment_plan": {
        "pt_t": "Desdobramento da BEF em Flandres",
        "en_t": "The BEF Deployment Plan",
        "pt_d": "Sob o comando de Sir John French, o corpo expedicionário toma posições no flanco esquerdo francês em Mons, bloqueando o avanço do Plano Schlieffen alemão.",
        "en_d": "Under Field Marshal Sir John French, the British divisions deploy on the Allied left at Mons, standing as an immovable barrier against the Schlieffen advance.",
        "reward": """army_experience = 25
add_war_support = 0.05"""
    },
    "ENG_ww1_the_flanders_supply_organisation": {
        "pt_t": "Organização Logística de Flandres",
        "en_t": "The Flanders Supply Organisation",
        "pt_d": "Ferrovias de bitola estreita e depósitos subterrâneos garantem que o Exército Britânico nas trincheiras de Ypres e do Somme receba munições sem cessar.",
        "en_d": "Decauville narrow-gauge rail systems and subterranean ammunition depots guarantee unceasing logistical deliveries through the mud of Flanders.",
        "reward": """123 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 100
    producer = ENG
}"""
    },
    "ENG_ww1_holding_the_continental_line": {
        "pt_t": "Sustentando a Linha Continental de Trincheiras",
        "en_t": "Holding the Continental Line",
        "pt_d": "Em Ypres, Festubert e Givenchy, as tropas britânicas resistem a ataques furiosos de artilharia pesada inimiga com heroísmo inabalável.",
        "en_d": "At Ypres and Festubert, British battalions dig into the frozen mud, withstanding massive bombardments and preserving the Channel ports at all costs.",
        "reward": """army_experience = 20
add_manpower = 50000"""
    },
    "ENG_ww1_artillery_ammunition_concentration": {
        "pt_t": "Concentração Maciça de Munição de Artilharia",
        "en_t": "Artillery Ammunition Concentration",
        "pt_d": "Milhões de granadas de 18 libras e obuses pesados de 6 e 8 polegadas são acumulados para pulverizar as redes de arame farpado e casamatas inimigas.",
        "en_d": "Vast ammunition parks accumulate millions of high-explosive and shrapnel shells, feeding unprecedented artillery concentrations before major assaults.",
        "reward": """add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 350
    producer = ENG
}
add_army_experience = 15"""
    },
    "ENG_ww1_a_limited_offensive_doctrine": {
        "pt_t": "Doutrina de Ofensivas Limitadas (Bite and Hold)",
        "en_t": "A Limited Offensive Doctrine",
        "pt_d": "Táticas de 'morder e segurar': atacar objetivos estritamente dentro do alcance da artilharia e aniquilar contra-ataques inimigos com fogo defensivo mortal.",
        "en_d": "'Bite and hold' tactics: capturing limited objectives under overwhelming artillery protection, then demolishing enemy counterattacks with pre-sighted fire.",
        "reward": """add_tech_bonus = {
    name = land_doc_bonus
    bonus = 1.0
    uses = 1
    category = land_doctrine
}
add_army_experience = 15"""
    },
    "ENG_ww1_the_dardanelles_staff_study": {
        "pt_t": "Estudo Estratégico dos Dardanelos e Galípoli",
        "en_t": "The Dardanelles Staff Study",
        "pt_d": "O Almirantado e o Gabinete analisam o plano audacioso de forçar os estreitos turcos para reabrir as rotas navais com a Rússia e nocautear o Império Otomano.",
        "en_d": "Churchill and the War Council study amphibious plans to force the Dardanelles Straits, open communications with Russia, and knock the Ottomans out of the war.",
        "reward": """add_tech_bonus = {
    name = naval_invasion_bonus
    bonus = 1.0
    uses = 1
    category = marine_tech
}
add_political_power = 40"""
    },
    "ENG_ww1_mediterranean_landing_preparation": {
        "pt_t": "Preparação para Desembarque Anfíbio no Mediterrâneo",
        "en_t": "Mediterranean Landing Preparation",
        "pt_d": "Barges de desembarque 'Beetles' blindadas e batalhões de fuzileiros navais da Royal Naval Division preparam assaltos de praia pioneiros.",
        "en_d": "Armoured 'Beetle' landing craft and Royal Naval Division marines train for pioneering amphibious beachhead landings in the Aegean.",
        "reward": """add_tech_bonus = {
    name = marine_bonus
    bonus = 1.0
    uses = 1
    category = marine_tech
}
navy_experience = 20"""
    },
    "ENG_ww1_mesopotamian_supply_review": {
        "pt_t": "Revisão Logística da Mesopotâmia e Queda de Bagdá",
        "en_t": "Mesopotamian Supply Review and Capture of Baghdad",
        "pt_d": "Após a tragédia de Kut, o General Stanley Maude reorganiza ferrovias, vapores no Rio Tigre e hospitais, liderando a ofensiva triunfal que liberta Bagdá em 1917.",
        "en_d": "Following Kut, General Stanley Maude systematically upgrades Tigris paddle-steamers, rail links, and field medicine, conquering Baghdad in March 1917.",
        "reward": """add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 120
    producer = ENG
}
army_experience = 15"""
    },
    "ENG_ww1_the_western_offensive_staff_study": {
        "pt_t": "Estudo das Grandes Ofensivas da Frente Ocidental",
        "en_t": "The Western Offensive Staff Study",
        "pt_d": "Análise exaustiva das batalhas do Somme e Passchendaele, identificando a necessidade crucial de barragens móveis e infiltração profunda.",
        "en_d": "Thorough operational analysis of the Somme and Third Ypres, identifying the essential role of creeping barrages, counter-battery sound ranging, and smoke screens.",
        "reward": """add_tech_bonus = {
    name = land_doc_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}
add_army_experience = 25"""
    },
    "ENG_ww1_the_creeping_barrage_school": {
        "pt_t": "A Escola da Barragem Rastejante de Artilharia",
        "en_t": "The Creeping Barrage School",
        "pt_d": "Uma muralha viva de fogo de artilharia avança a exatos 50 metros à frente da infantaria com precisão cronometrada, mantendo os defensores inimigos enterrados em seus abrigos.",
        "en_d": "A curtain of exploding shells advances 50 yards ahead of the assaulting infantry like clockwork, keeping enemy machine gunners pinned in their deep dugouts.",
        "reward": """add_tech_bonus = {
    name = artillery_doctrine
    bonus = 1.0
    uses = 1
    category = artillery
}
army_experience = 25"""
    },
    "ENG_ww1_tank_committee_experiments": {
        "pt_t": "Experimentos do Comitê de Landships e os Blindados",
        "en_t": "Tank Committee Experiments",
        "pt_d": "Sob a liderança visionária de Winston Churchill e engenheiros britânicos, nasce o tanque de guerra: o 'Little Willie' e o couraçado de esteiras Mark I.",
        "en_d": "Sponsored by Winston Churchill's Landships Committee, British engineers construct the world's first combat tanks—'Little Willie' and the rhomboid Mark I.",
        "reward": """swap_ideas = {
    remove_idea = ENG_professional_bef_t2
    add_idea = ENG_professional_bef_t3
}
add_tech_bonus = {
    name = armor_bonus
    bonus = 1.0
    uses = 2
    category = armor
}
army_experience = 30"""
    },
    "ENG_ww1_assault_coordination_exercises": {
        "pt_t": "Exercícios de Assalto Combinado com Tanques (Cambrai)",
        "en_t": "Tank Assault Coordination Exercises",
        "pt_d": "Em Cambrai e Amiens, centenas de blindados esmagam o arame farpado e cruzam as trincheiras sem bombardeio prévio, conquistando ruptura tática histórica.",
        "en_d": "At Cambrai, hundreds of tanks breach the formidable Hindenburg wire without preliminary bombardment, demonstrating modern armored breakthrough.",
        "reward": """add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 1
    category = land_doctrine
}
army_experience = 20"""
    },
    "ENG_ww1_palestine_railway_liaison": {
        "pt_t": "Ferrovia Militar da Palestina e a Tomada de Jerusalém",
        "en_t": "Palestine Railway and the Capture of Jerusalem",
        "pt_d": "O General Edmund Allenby constrói uma ferrovia e adutora de água através do deserto do Sinai, rompendo a linha de Gaza-Beersheba e entrando vitorioso em Jerusalém a pé.",
        "en_d": "General Edmund Allenby lays railway lines and water pipelines across Sinai, smashing the Ottoman line at Beersheba and humbly entering Jerusalem on foot.",
        "reward": """130 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
army_experience = 15"""
    },
    "ENG_ww1_the_spring_defence_plan": {
        "pt_t": "O Plano Defensivo da Primavera: 'De Costas para a Parede'",
        "en_t": "The Spring Defence Plan",
        "pt_d": "A ordem histórica do Marechal Haig ('Backs to the Wall') conclama cada soldado a resistir até a morte contra a Kaiserschlacht alemã de 1918.",
        "en_d": "Field Marshal Haig's historic 'Backs to the Wall' order rallies every British and Dominion soldier to hold ground at all costs, breaking Ludendorff's final offensive.",
        "reward": """add_manpower = 75000
add_war_support = 0.08
army_experience = 20"""
    },
    "ENG_ww1_the_allied_counteroffensive_plan": {
        "pt_t": "A Ofensiva dos Cem Dias (Amiens até a Vitória)",
        "en_t": "The Hundred Days Allied Counteroffensive",
        "pt_d": "Em 8 de agosto de 1918, o 'dia negro do exército alemão', corpos britânicos, canadenses e australianos desferem o golpe definitivo que destrói a Linha Hindenburg.",
        "en_d": "On 8 August 1918—the 'black day of the German Army'—British, Canadian, and Australian shock corps launch the unyielding offensive that shatters the Hindenburg Line.",
        "reward": """army_experience = 35
add_war_support = 0.10"""
    },
    "ENG_ww1_operational_reserve_restoration": {
        "pt_t": "Restauração das Reservas Operacionais",
        "en_t": "Operational Reserve Restoration",
        "pt_d": "Reagrupamento rápido de divisões veteranas e fluxo ininterrupto de reposições garantem que o Exército Britânico mantenha pressão ofensiva constante.",
        "en_d": "Swift rotation of rested shock divisions and immediate equipment replenishment ensure relentless offensive momentum until the final victory.",
        "reward": """add_manpower = 50000
army_experience = 15"""
    },
    "ENG_ww1_the_armistice_stand_down_plan": {
        "pt_t": "O Plano de Cessar-Fogo do Armistício",
        "en_t": "The Armistice Stand Down Plan",
        "pt_d": "Às 11 horas do dia 11 de novembro de 1918, as armas silenciam na Frente Ocidental. As tropas britânicas avançam para vigiar a Renânia em perfeita ordem.",
        "en_d": "At the eleventh hour of the eleventh day of the eleventh month, the guns fall silent. British troops march forward to occupy the bridgeheads of the Rhine.",
        "reward": """add_political_power = 75
add_stability = 0.08
set_country_flag = ENG_ww1_armistice_order_completed"""
    },
    "ENG_ww1_lessons_for_the_general_staff": {
        "pt_t": "Lições Doutrinárias para o Estado-Maior Imperial",
        "en_t": "Lessons for the Imperial General Staff",
        "pt_d": "A síntese da guerra mecânica, cooperação aero-terrestre e artilharia científica transforma a doutrina britânica na mais avançada do mundo moderno.",
        "en_d": "The synthesis of armored warfare, creeping barrages, and air-ground coordination codifies British doctrine as the most sophisticated in the modern world.",
        "reward": """army_experience = 40
add_tech_bonus = {
    name = doctrine_bonus
    bonus = 1.0
    uses = 2
    category = land_doctrine
}"""
    }
}
