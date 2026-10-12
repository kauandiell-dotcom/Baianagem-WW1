"""Economy and Mezzogiorno (eco) Wing Data for Italy WW1 Tree.
Contains 35 focuses with historical depth, balance compliance, and bilingual loc.
Overhauled with real factories, dockyards, Carcano/artillery equipment stockpiles,
and progressive resolution of the Coal Famine and Southern Question debuffs.
"""

ECONOMY_FOCI = {
    "industrial_triangle": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_tech_bonus = { name = ITA_ww1_industry_prog_1 bonus = 0.25 uses = 1 category = industry } add_political_power = 25",
        "desc_en": "Consolidating the industrial core connecting Turin, Milan, and Genoa. Immediate effect: Constructs 1 civilian factory in Lombardy (Milan), grants 25% Industrial research bonus (1 use) and 25 Political Power.",
        "desc_pt": "Consolidação do núcleo fabril ligando Turim, Milão e Gênova. Efeito imediato: Constrói 1 fábrica civil na Lombardia (Milão), concede bônus de 25% em pesquisa Industrial (1 uso) e 25 de Poder Político."
    },
    "turin_motor_industry": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "158 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 2 instant_build = yes } } add_equipment_to_stockpile = { type = motorized_equipment_1 amount = 100 producer = ITA } add_tech_bonus = { name = ITA_ww1_motor_tech bonus = 0.25 uses = 1 category = motorized_equipment } add_political_power = 20",
        "desc_en": "Expanding FIAT, Lancia, and SCAT automotive engineering facilities in Piedmont. Immediate effect: Constructs 2 military factories in Piedmont (Turin), adds 100 trucks to stockpile, and grants 25% Motorized tech bonus.",
        "desc_pt": "Expansão das instalações automobilísticas da FIAT, Lancia e SCAT no Piemonte. Efeito imediato: Constrói 2 fábricas militares no Piemonte (Turim), adiciona 100 caminhões ao estoque e concede 25% de bônus em Motorizados."
    },
    "genoa_shipyards": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "158 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 2 instant_build = yes } } add_equipment_to_stockpile = { type = convoy_1 amount = 60 producer = ITA } navy_experience = 20",
        "desc_en": "Upgrading naval ways and marine engine workshops in the Gulf of Genoa. Immediate effect: Constructs 2 naval dockyards in Liguria (Genoa), adds 60 convoys to stockpile, and grants 20 Navy Experience.",
        "desc_pt": "Modernização de estaleiros navais e oficinas de motores marítimos no Golfo de Gênova. Efeito imediato: Constrói 2 estaleiros navais na Ligúria (Gênova), adiciona 60 comboios ao estoque e concede 20 de Experiência Naval."
    },
    "milan_banking": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "159 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_political_power = 50 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Banca Commerciale Italiana and Credito Italiano mobilize private capital for domestic manufacture. Immediate effect: Constructs 1 civilian factory in Lombardy, grants 50 Political Power and reduces Social Tension by 5.",
        "desc_pt": "A Banca Commerciale Italiana e o Credito Italiano mobilizam capital privado para a indústria nacional. Efeito imediato: Constrói 1 fábrica civil na Lombardia, concede 50 de Poder Político e reduz a Tensão Social em 5."
    },
    "hydroelectric_power": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_coal_iron_scarcity add_ideas = ITA_carbone_bianco_hydro 159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_tech_bonus = { name = ITA_ww1_hydro_tech bonus = 0.25 uses = 1 category = industry }",
        "desc_en": "Harnessing Alpine river torrents for white coal (carbone bianco) electricity generation. Immediate effect: Halves the coal famine debuff via Alpine White Coal national spirit, constructs 1 civilian factory and 1 infrastructure in Lombardy.",
        "desc_pt": "Aproveitamento dos cursos d'água alpinos para geração de eletricidade ('carvão branco'). Efeito imediato: Reduz pela metade a escassez de carvão com o espírito Carvão Branco dos Alpes, constrói 1 fábrica civil e 1 infraestrutura na Lombardia."
    },
    "mezzogiorno_programme": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_southern_question_gap add_ideas = ITA_mezzogiorno_development_stage 117 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -10 } add_political_power = 25",
        "desc_en": "Special state investments, tax reliefs, and rural roads across Southern Italy. Immediate effect: Mitigates the Southern Gap debuff, constructs 1 civilian factory and 1 infrastructure in Campania (Naples).",
        "desc_pt": "Investimentos estatais especiais, isenções fiscais e estradas rurais pelo Sul da Itália. Efeito imediato: Ameniza a disparidade do Sul com o espírito Desenvolvimento do Mezzogiorno, constrói 1 fábrica civil e 1 infraestrutura na Campânia (Nápoles)."
    },
    "tariff_protection": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } add_political_power = 30 add_to_variable = { ita_ww1_social_tension = 5 }",
        "desc_en": "Shielding northern metallurgy and heavy engineering behind protective customs duties. Immediate effect: Constructs 1 military factory in Piedmont, grants 30 Political Power and raises Social Tension by 5.",
        "desc_pt": "Proteção aduaneira para a metalurgia e a mecânica pesada do Norte. Efeito imediato: Constrói 1 fábrica militar no Piemonte, concede 30 de Poder Político e eleva a Tensão Social em 5."
    },
    "free_trade_opening": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "115 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_political_power = 30 add_to_variable = { ita_ww1_southern_gap = -5 }",
        "desc_en": "Lowering agricultural tariffs encourages southern citrus and olive exports. Immediate effect: Constructs 1 civilian factory in Sicily, grants 30 Political Power and narrows the Southern Gap by 5.",
        "desc_pt": "A redução das tarifas agrícolas estimula a exportação de cítricos e azeite do Mezzogiorno. Efeito imediato: Constrói 1 fábrica civil na Sicília, concede 30 de Poder Político e reduz a disparidade do Sul em 5."
    },
    "ilva_steel_consortium": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "162 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = arms_factory level = 1 instant_build = yes } } add_resource = { type = steel amount = 12 state = 162 } add_tech_bonus = { name = ITA_ww1_steel_tech bonus = 0.25 uses = 1 category = industry } add_political_power = 20",
        "desc_en": "State-backed consolidation of steel blast furnaces at Bagnoli, Piombino, and Portoferraio. Immediate effect: Constructs 1 civilian factory and 1 military factory in Tuscany, adds +12 Steel to state 162.",
        "desc_pt": "Consolidação dos altos-fornos siderúrgicos em Bagnoli, Piombino e Portoferraio com apoio estatal. Efeito imediato: Constrói 1 fábrica civil e 1 fábrica militar na Toscana, adiciona +12 de Aço ao estado 162."
    },
    "emigrant_remittances": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "118 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } country_event = { id = ww1_italy.69 days = 1 } add_to_variable = { ita_ww1_southern_gap = -5 } add_political_power = 30",
        "desc_en": "Harnessing millions of lire sent home by Italian emigrants across North and South America. Immediate effect: Constructs 1 civilian factory in Calabria, triggers Emigrant Remittances event and grants 30 Political Power.",
        "desc_pt": "Aproveitamento de milhões de liras enviadas por emigrantes das Américas para suas famílias. Efeito imediato: Constrói 1 fábrica civil na Calábria, dispara o evento de Remessas dos Emigrantes e concede 30 de Poder Político."
    },
    "apulian_aqueduct": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "157 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = infrastructure level = 2 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -15 } country_event = { id = ww1_italy.68 days = 1 }",
        "desc_en": "Constructing the monumental Acquedotto Pugliese to bring drinking water to parched Apulian plains. Immediate effect: Constructs 1 civilian factory and 2 Infrastructure in Apulia, dramatically narrowing the Southern Gap by 15.",
        "desc_pt": "Construção do monumental Acquedotto Pugliese trazendo água potável às planícies secas da Apúlia. Efeito imediato: Constrói 1 fábrica civil e 2 níveis de Infraestrutura na Apúlia, reduzindo amplamente a disparidade do Sul em 15."
    },
    "sicilian_sulphur": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "115 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_tech_bonus = { name = ITA_ww1_chem_tech bonus = 0.25 uses = 1 category = industry } add_political_power = 25",
        "desc_en": "Reorganizing the Sicilian sulphur syndicate to sustain chemical and gunpowder manufacture. Immediate effect: Constructs 1 civilian factory and 1 Infrastructure in Sicily, grants 25% Industrial research bonus.",
        "desc_pt": "Reorganização do consórcio de enxofre da Sicília para abastecer indústrias químicas e de pólvora. Efeito imediato: Constrói 1 fábrica civil e 1 nível de Infraestrutura na Sicília, concede 25% de bônus em Indústria."
    },
    "land_reclamation": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "160 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } 2 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -5 }",
        "desc_en": "Drainage and bonifica hydraulic schemes in the Pontine and Tuscan coastal marshes. Immediate effect: Constructs 1 civilian factory in Emilia-Romagna and 1 Infrastructure in Lazio (Rome).",
        "desc_pt": "Drenagem e obras hidráulicas de 'bonifica' nos pântanos costeiros do Lácio e da Toscana. Efeito imediato: Constrói 1 fábrica civil na Emilia-Romagna e 1 nível de Infraestrutura no Lácio (Roma)."
    },
    "merchant_marine_subsidies": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant_build = yes } } add_equipment_to_stockpile = { type = convoy_1 amount = 50 producer = ITA } navy_experience = 15 add_political_power = 20",
        "desc_en": "State postal and navigation subsidies modernize Italian oceanic steamship lines. Immediate effect: Constructs 1 dockyard in Liguria, adds 50 convoys to stockpile, and grants 15 Navy Experience.",
        "desc_pt": "Subsídios estatais de navegação modernizam as linhas a vapor da marinha mercante italiana. Efeito imediato: Constrói 1 estaleiro naval na Ligúria, adiciona 50 comboios ao estoque e concede 15 de Experiência Naval."
    },
    "libya_colonisation": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_libya_acquired",
        "ai": "factor = 10",
        "effect": "448 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } add_building_construction = { type = naval_base level = 1 instant_build = yes } } add_to_variable = { ita_ww1_irredentism = 5 } add_political_power = 20",
        "desc_en": "Directing agrarian emigration to Libyan coastal settlements on the Quarta Sponda. Immediate effect: Adds 1 Infrastructure and 1 Naval Base in Tripoli, raising Irredentism by 5.",
        "desc_pt": "Direcionamento da colonização agrária para as faixas litorâneas líbias da Quarta Margem. Efeito imediato: Constrói 1 nível de Infraestrutura e 1 Base Naval em Trípoli, elevando o Irredentismo em 5."
    },
    "industrial_mobilisation_committee": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 15",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } 159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } add_political_power = 30 country_event = { id = ww1_italy.70 days = 1 }",
        "desc_en": "General Dallolio creates regional committees to subordinate civilian factories to military production. Immediate effect: Constructs 2 military factories (Piedmont and Lombardy) and triggers Industrial Mobilisation event.",
        "desc_pt": "O General Dallolio cria comitês regionais subordinando fábricas civis às encomendas de guerra. Efeito imediato: Constrói 2 fábricas militares (Piemonte e Lombardia) e dispara o evento da Mobilização Industrial."
    },
    "munitions_undersecretariat": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 15",
        "effect": "159 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 2 instant_build = yes } } add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 2500 producer = ITA } add_tech_bonus = { name = ITA_ww1_munitions_tech bonus = 0.25 uses = 1 category = infantry_weapons } add_political_power = 25",
        "desc_en": "A dedicated government undersecretariat centralizes shell and rifle procurement. Immediate effect: Constructs 2 military factories in Lombardy, adds 2,500 Carcano Mod. 91 rifles to stockpile, and grants 25% Weapons tech bonus.",
        "desc_pt": "Subsecretaria governamental exclusiva centraliza o fornecimento de projéteis e fuzis. Efeito imediato: Constrói 2 fábricas militares na Lombardia, adiciona 2.500 fuzis Carcano Mod. 91 ao estoque e concede 25% de bônus em Armamentos."
    },
    "ansaldo_expansion": {
        "cost": 5,
        "available": "",
        "ai": "factor = 15",
        "effect": "158 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 2 instant_build = yes } } add_equipment_to_stockpile = { type = artillery_equipment_1 amount = 100 producer = ITA } add_tech_bonus = { name = ITA_ww1_artillery_prod bonus = 0.25 uses = 1 category = artillery }",
        "desc_en": "Massive vertical expansion of the Perrone brothers' steel, shipbuilding, and artillery conglomerate. Immediate effect: Constructs 2 military factories in Liguria, adds 100 artillery pieces to stockpile, and grants 25% Artillery tech bonus.",
        "desc_pt": "Expansão vertical massiva do conglomerado siderúrgico, naval e bélico dos irmãos Perrone. Efeito imediato: Constrói 2 fábricas militares na Ligúria, adiciona 100 canhões de artilharia ao estoque e concede 25% de bônus em Artilharia."
    },
    "aero_engine_contracts": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant_build = yes } } add_tech_bonus = { name = ITA_ww1_aero_engine bonus = 0.25 uses = 1 category = air_equipment } air_experience = 15",
        "desc_en": "State contracts with FIAT and Isotta Fraschini produce high-output aero-engines for military aviation. Immediate effect: Constructs 1 military factory in Piedmont, grants 25% Air research bonus and 15 Air Experience.",
        "desc_pt": "Contratos estatais com FIAT e Isotta Fraschini produzem motores aeronáuticos de alta potência. Efeito imediato: Constrói 1 fábrica militar no Piemonte, concede 25% de bônus de pesquisa Aérea e 15 de Experiência Aérea."
    },
    "war_loans": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "2 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 2 instant_build = yes } } add_political_power = 60 add_to_variable = { ita_ww1_social_tension = 5 }",
        "desc_en": "Flotation of consecutive national war loans mobilizes domestic savings and civic duty. Immediate effect: Constructs 2 civilian factories in Lazio (Rome) and grants 60 Political Power.",
        "desc_pt": "Lançamento sucessivo de empréstimos nacionais de guerra mobiliza a poupança popular. Efeito imediato: Constrói 2 fábricas civis no Lácio (Roma) e concede 60 de Poder Político."
    },
    "british_coal": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 15",
        "effect": "remove_ideas = ITA_coal_iron_scarcity remove_ideas = ITA_carbone_bianco_hydro add_ideas = ITA_energy_independence_spirit country_event = { id = ww1_italy.71 days = 1 } add_political_power = 25",
        "desc_en": "Securing priority colliers and credit lines from London to keep Italian blast furnaces burning. Immediate effect: Completely eliminates Coal Scarcity, establishes Energy Independence national spirit, and triggers British Coal protocol.",
        "desc_pt": "Garantia de navios carvoeiros e linhas de crédito de Londres para manter os altos-fornos acesos. Efeito imediato: Elimina completamente a escassez de carvão, ativa a Independência Energética e dispara o protocolo do Carvão Britânico."
    },
    "war_hydropower": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_coal_iron_scarcity remove_ideas = ITA_carbone_bianco_hydro add_ideas = ITA_energy_independence_spirit 159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_tech_bonus = { name = ITA_ww1_elec_tech bonus = 0.25 uses = 1 category = industry }",
        "desc_en": "Emergency electrification of Piedmontese and Lombard railway arteries replaces imported coal. Immediate effect: Completely eliminates Coal Scarcity, adds 1 civilian factory and 1 infrastructure in Lombardy.",
        "desc_pt": "Eletrificação emergencial de linhas ferroviárias piemontesas e lombardas substitui o carvão importado. Efeito imediato: Elimina completamente a escassez de carvão, constrói 1 fábrica civil e 1 infraestrutura na Lombardia."
    },
    "bread_rationing": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "add_ideas = ITA_ww1_peacetime_military_economy set_country_flag = ita_ww1_bread_rationing_decree add_to_variable = { ita_ww1_social_tension = 5 } add_political_power = 25",
        "desc_en": "Instituting grain and bread rationing cards to manage dwindling wheat stocks during the conflict. Immediate effect: Grants War Economy consumption efficiency spirit and 25 Political Power.",
        "desc_pt": "Instituição de cartões de racionamento de pão e cereais para gerir estoques escassos de trigo. Efeito imediato: Concede espírito de economia de guerra eficiente e 25 de Poder Político."
    },
    "price_controls": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "add_stability = 0.05 add_to_variable = { ita_ww1_social_tension = -5 } add_political_power = 30",
        "desc_en": "Fixing ceiling prices on essential foodstuffs to protect urban working families from gouging. Immediate effect: Grants +5% Stability, 30 Political Power and reduces Social Tension by 5.",
        "desc_pt": "Tabelamento de preços para gêneros de primeira necessidade protege famílias urbanas da carestia. Efeito imediato: Concede +5% de Estabilidade, 30 de Poder Político e reduz a Tensão Social em 5."
    },
    "grain_requisition": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "set_country_flag = ita_ww1_bread_rationing_decree add_war_support = 0.05 add_to_variable = { ita_ww1_social_tension = 5 } add_political_power = 25",
        "desc_en": "Mandatory agricultural quotas and state requisitions supply grain directly to front-line army depots. Immediate effect: Grants +5% War Support and 25 Political Power.",
        "desc_pt": "Cotas agrícolas obrigatórias e requisições estatais abastecem diretamente os depósitos do exército. Efeito imediato: Concede +5% de Apoio à Guerra e 25 de Poder Político."
    },
    "refugee_relief": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_caporetto_shock",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.73 days = 1 } add_stability = 0.05 add_political_power = 30",
        "desc_en": "Providing food, shelter, and medical care to over 400,000 citizens displaced by the Caporetto retreat. Immediate effect: Triggers Venetian Refugee Relief event, grants +5% Stability and 30 Political Power.",
        "desc_pt": "Alimentação, abrigo e assistência médica a mais de 400 mil cidadãos deslocados por Caporetto. Efeito imediato: Dispara o evento de Auxílio aos Refugiados, concede +5% de Estabilidade e 30 de Poder Político."
    },
    "inflation_management": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_political_power = 40 add_stability = 0.03 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Central bank currency stabilisation dampens run-away inflation following the end of hostilities. Immediate effect: Grants 40 Political Power, +3% Stability and reduces Social Tension by 5.",
        "desc_pt": "A estabilização monetária do banco central refreia a inflação desenfreada após o fim do conflito. Efeito imediato: Concede 40 de Poder Político, +3% de Estabilidade e diminui a Tensão Social em 5."
    },
    "war_profiteers_inquiry": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } country_event = { id = ww1_italy.74 days = 1 } add_political_power = 35",
        "desc_en": "Taxing windfall war profits (pescecani) recovers public revenue and soothes working-class fury. Immediate effect: Confiscated profits construct 1 civilian factory in Piedmont, grants 35 Political Power.",
        "desc_pt": "Tributação sobre lucros extraordinários de guerra recupera receitas e abranda a fúria popular. Efeito imediato: Os lucros confiscados constroem 1 fábrica civil no Piemonte, concedendo 35 de Poder Político."
    },
    "industrial_demobilisation": {
        "cost": 5,
        "available": "NOT = { has_war = yes }",
        "ai": "factor = 15",
        "effect": "158 = { remove_building = { type = arms_factory level = 1 } add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } 159 = { remove_building = { type = arms_factory level = 1 } add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_political_power = 35 add_to_variable = { ita_ww1_social_tension = 5 }",
        "desc_en": "Reconverting war factories to peacetime commercial manufacture triggers restructuring. Immediate effect: Converts 2 military factories into 2 civilian factories in Piedmont and Lombardy.",
        "desc_pt": "Reconversão de fábricas bélicas para bens civis desencadeia reestruturação industrial. Efeito imediato: Converte 2 fábricas militares em 2 fábricas civis no Piemonte e na Lombardia."
    },
    "veterans_land_settlement": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "117 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -10 } add_to_variable = { ita_ww1_social_tension = -5 } add_stability = 0.03",
        "desc_en": "Distributing reclaimed agricultural lands to demobilized peasant veterans in Apulia and Campania. Immediate effect: Constructs 1 civilian factory in Campania, grants +3% Stability and narrows Southern Gap by 10.",
        "desc_pt": "Distribuição de terras agricultáveis saneadas a veteranos camponeses na Apúlia e Campânia. Efeito imediato: Constrói 1 fábrica civil na Campânia, concede +3% de Estabilidade e reduz a disparidade do Sul em 10."
    },
    "public_works_programme": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "118 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } 115 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } 117 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_to_variable = { ita_ww1_social_tension = -10 }",
        "desc_en": "State-funded road construction, port repairs, and electrification absorb demobilized workers. Immediate effect: Constructs 1 civilian factory in Calabria, 1 civilian factory in Sicily, and 1 infrastructure in Campania.",
        "desc_pt": "Obras estatais em rodovias, portos e eletrificação absorvem trabalhadores desmobilizados. Efeito imediato: Constrói 1 fábrica civil na Calábria, 1 fábrica civil na Sicília e 1 infraestrutura na Campânia."
    },
    "discount_bank_crisis": {
        "cost": 5,
        "available": "date > 1921.1.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.76 days = 1 } add_political_power = -20",
        "desc_en": "The insolvency of the Banca Italiana di Sconto threatens the liquidity of Ansaldo and heavy industry. Immediate effect: Triggers the Discount Bank Crisis event and costs 20 Political Power.",
        "desc_pt": "A insolvência da Banca Italiana di Sconto ameaça a liquidez da Ansaldo e da indústria pesada. Efeito imediato: Dispara o evento da Crise do Banco de Desconto e custa 20 de Poder Político."
    },
    "bank_rescue_consortium": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_political_power = 50 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "A state-orchestrated consortium stabilizes the banking sector and protects industrial accounts. Immediate effect: Constructs 1 civilian factory in Lombardy, grants 50 Political Power and reduces Social Tension by 5.",
        "desc_pt": "Um consórcio orquestrado pelo Estado estabiliza o setor bancário e protege contas industriais. Efeito imediato: Constrói 1 fábrica civil na Lombardia, concede 50 de Poder Político e reduz a Tensão Social em 5."
    },
    "southern_development_charter": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_southern_question_gap remove_ideas = ITA_mezzogiorno_development_stage add_ideas = ITA_mezzogiorno_integrated add_to_variable = { ita_ww1_southern_gap = -25 } add_stability = 0.05",
        "desc_en": "A comprehensive legislative charter guarantees permanent credit and infrastructure development for the Mezzogiorno. Immediate effect: Completely solves the Southern Gap, replacing it with the Prosperous Mezzogiorno spirit (+5% Stability).",
        "desc_pt": "Carta legislativa abrangente garante crédito permanente e infraestrutura para o Mezzogiorno. Efeito imediato: Resolve definitivamente a disparidade do Sul com o espírito Mezzogiorno Integrado e Próspero (+5% de Estabilidade)."
    },
    "budget_balancing": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_political_power = 60 add_stability = 0.05 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "De Stefani's fiscal consolidation curbs public debt and restores investor confidence in the lira. Immediate effect: Grants 60 Political Power, +5% Stability and reduces Social Tension by 5.",
        "desc_pt": "A consolidação fiscal de De Stefani reduz o déficit público e restaura a confiança na lira. Efeito imediato: Concede 60 de Poder Político, +5% de Estabilidade e diminui a Tensão Social em 5."
    }
}
