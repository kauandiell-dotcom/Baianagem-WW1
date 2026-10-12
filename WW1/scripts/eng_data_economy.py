# scripts/eng_data_economy.py
# British Empire WW1 - Economy, Munitions & Postwar Reconstruction (40 focuses)

ECONOMY_DATA = {
    "ENG_ww1_the_treasury_estimates": {
        "pt_t": "Estimativas Orçamentárias do Tesouro",
        "en_t": "The Treasury Estimates",
        "pt_d": "O Chanceler do Tesouro revisa as dotações fiscais e aloca fundos de emergência para modernização industrial e preparo das defesas nacionais do Reino Unido.",
        "en_d": "The Chancellor of the Exchequer reviews fiscal appropriations and allocates emergency funds for industrial modernization and imperial defense readiness.",
        "reward": """add_political_power = 60
126 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
128 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_industrial_district_surveys": {
        "pt_t": "Levantamento dos Distritos Industriais",
        "en_t": "Industrial District Surveys",
        "pt_d": "Uma rigorosa inspeção técnica nas bacias manufatureiras britânicas mapeia a capacidade produtiva de forjas, tornos mecânicos e oficinas para conversão militar.",
        "en_d": "A thorough survey of British manufacturing heartlands maps machine-tool capacity, forging facilities, and workshop availability for defense contracts.",
        "reward": """add_tech_bonus = {
    name = industry_survey_bonus
    bonus = 1.0
    uses = 1
    category = industry
}
add_political_power = 40"""
    },
    "ENG_ww1_midlands_machine_shops": {
        "pt_t": "Oficinas Mecânicas de Midlands",
        "en_t": "Midlands Machine Shops",
        "pt_d": "As indústrias metalúrgicas de Birmingham e Coventry são equipadas com ferramentas de alta precisão para a usinagem de cartuchos, fuzis e peças de artilharia.",
        "en_d": "The metalworking plants of Birmingham and Coventry are retooled with precision machinery to mass-produce rifle receivers, cartridges, and artillery components.",
        "reward": """128 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_clyde_shipyard_contracts": {
        "pt_t": "Contratos dos Estaleiros do Rio Clyde",
        "en_t": "Clyde Shipyard Contracts",
        "pt_d": "As margens do Clyde, na Escócia, recebem volumosos pedidos de construção naval para contratorpedeiros, cruzadores e navios de escolta da Royal Navy.",
        "en_d": "The shipyards along Scotland's River Clyde receive heavy naval orders for destroyers, escort craft, and capital ships to sustain British sea supremacy.",
        "reward": """133 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = dockyard
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_tyne_steel_and_ordnance": {
        "pt_t": "Aço e Armamento do Rio Tyne",
        "en_t": "Tyne Steel and Ordnance",
        "pt_d": "Os complexos industriais de Newcastle e do Rio Tyne concentram sua enorme capacidade siderúrgica na fundição de canhões navais e blindagens de alta resistência.",
        "en_d": "Heavy steelworks and armaments foundries on the River Tyne and Newcastle ramp up the production of heavy naval ordnance and specialized armor plating.",
        "reward": """131 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_lancashire_engineering": {
        "pt_t": "Engenharia Têxtil e Pesada de Lancashire",
        "en_t": "Lancashire Engineering",
        "pt_d": "A tradicional base manufatureira de Manchester e Lancashire expande a produção de tecidos para uniformes, motores pesados e peças de reposição mecânica.",
        "en_d": "Lancashire's vast engineering workshops and textile mills mobilize to manufacture heavy engines, uniforms, canvas, and replacement parts for the imperial services.",
        "reward": """132 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_the_city_credit_market": {
        "pt_t": "O Mercado de Crédito da City de Londres",
        "en_t": "The City of London Credit Market",
        "pt_d": "O centro financeiro mundial na City mobiliza linhas globais de crédito comercial e títulos de guerra para financiar suprimentos vitais para a Entente.",
        "en_d": "The global financial hub in the City of London unlocks credit syndicates and issues war loan bonds to finance vital material acquisitions for the Entente.",
        "reward": """add_political_power = 75
add_stability = 0.05"""
    },
    "ENG_ww1_railway_freight_coordination": {
        "pt_t": "Coordenação Ferroviária de Carga",
        "en_t": "Railway Freight Coordination",
        "pt_d": "O Comitê Executivo Ferroviário assume o controle operacional unificado das linhas férreas britânicas, priorizando o fluxo ininterrupto de carvão e munições para os portos.",
        "en_d": "The Railway Executive Committee assumes centralized traffic control across British lines, guaranteeing expedited coal and ammunition movements to deepwater ports.",
        "reward": """128 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}
129 = {
    add_building_construction = {
        type = infrastructure
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_domestic_coal_allocation": {
        "pt_t": "Alocação Doméstica de Carvão",
        "en_t": "Domestic Coal Allocation",
        "pt_d": "O carvão de alta qualidade do País de Gales e de Yorkshire é reservado estrategicamente para abastecer as caldeiras da Grand Fleet e as fundições de aço bélico.",
        "en_d": "High-calorific Welsh and Yorkshire steam coal is strategically rationed to feed Grand Fleet boilers, munitions furnaces, and export commitments.",
        "reward": """131 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_political_power = 40"""
    },
    "ENG_ww1_national_munitions_contracts": {
        "pt_t": "Contratos das Fábricas Nacionais de Munição",
        "en_t": "National Munitions Contracts",
        "pt_d": "A criação das National Shell Factories e da monumental usina química de Gretna impulsiona a produção estatal de projéteis de artilharia e explosivos cordite.",
        "en_d": "The founding of National Shell Factories and massive propellant works at Gretna scales state-owned production of artillery shells and cordite.",
        "reward": """130 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 250
    producer = ENG
}"""
    },
    "ENG_ww1_the_ministry_of_munitions": {
        "pt_t": "O Ministério das Munições de David Lloyd George",
        "en_t": "The Ministry of Munitions",
        "pt_d": "Criado para superar a dramática Crise dos Projéteis de 1915, o ministério revoluciona a produção bélica, integrando ciência, indústria pesada e trabalho em escala total.",
        "en_d": "Established to overcome the catastrophic 1915 Shell Crisis, the Ministry under David Lloyd George organizes industry, labor, and state resources for total war.",
        "reward": """swap_ideas = {
    remove_idea = ENG_city_of_london_credit
    add_idea = ENG_city_of_london_credit_t2
}
128 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = arms_factory
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_shell_inspection_boards": {
        "pt_t": "Conselhos de Inspeção de Projéteis",
        "en_t": "Shell Inspection Boards",
        "pt_d": "Normas rigorosas de controle químico e metalúrgico eliminam falhas de detonação em projéteis de alto explosivo e espoletas temporizadas britânicas.",
        "en_d": "Rigorous metallurgical and chemical inspection regimes eliminate defective duds among British high-explosive shells and timed artillery fuses.",
        "reward": """130 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}
add_equipment_to_stockpile = {
    type = artillery_equipment_1
    amount = 120
    producer = ENG
}"""
    },
    "ENG_ww1_wartime_labour_dilution": {
        "pt_t": "Diluição do Trabalho e as 'Munitionettes'",
        "en_t": "Wartime Labour Dilution",
        "pt_d": "Quase um milhão de mulheres entram nas fábricas de projéteis e componentes aeronáuticos, garantindo produção recorde enquanto os homens marcham para o front.",
        "en_d": "Hundreds of thousands of female workers ('munitionettes') enter arms factories and engineering plants, sustaining record industrial output while soldiers enlist.",
        "reward": """add_manpower = 60000
add_war_support = 0.05"""
    },
    "ENG_ww1_the_shop_stewards_agreement": {
        "pt_t": "Acordo com os Delegados Sindicais (Shop Stewards)",
        "en_t": "The Shop Stewards Agreement",
        "pt_d": "Negociações salariais transparentes e garantias de direitos pós-guerra desarmam greves operárias no Clyde e asseguram paz nas linhas de montagem bélica.",
        "en_d": "Constructive industrial arbitration and post-war restoration guarantees avert destabilizing strikes on the Clyde and secure uninterrupted factory shifts.",
        "reward": """add_political_power = 50
add_stability = 0.05
set_country_flag = ENG_ww1_labour_peace_secured"""
    },
    "ENG_ww1_emergency_factory_controls": {
        "pt_t": "Controles de Emergência sobre Fábricas Controladas",
        "en_t": "Emergency Factory Controls",
        "pt_d": "Mais de cinco mil estabelecimentos industriais são designados 'Estabelecimentos Controlados', dedicados integralmente à vitória militar sob a égide da DORA.",
        "en_d": "Over five thousand manufacturing plants are gazetted as 'Controlled Establishments', operating under direct government scheduling to maximize war output.",
        "reward": """swap_ideas = {
    remove_idea = ENG_city_of_london_credit_t2
    add_idea = ENG_city_of_london_credit_t3
}
129 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = arms_factory
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_the_ministry_of_food": {
        "pt_t": "O Ministério da Alimentação e Racionamento",
        "en_t": "The Ministry of Food",
        "pt_d": "O controle científico de estoques de trigo, açúcar e carne, somado ao racionamento equitativo, derrota as tentativas alemãs de estrangular o sustento britânico.",
        "en_d": "Centralized food purchasing, scientific calorie management, and fair rationing successfully defeat the German attempt to starve the British Isles.",
        "reward": """add_stability = 0.05
add_political_power = 50"""
    },
    "ENG_ww1_austerity_and_public_credit": {
        "pt_t": "Austeridade e Crédito Público",
        "en_t": "Austerity and Public Credit",
        "pt_d": "Campanhas patrióticas de empréstimos de guerra engajam cidadãos de todas as classes, canalizando a poupança nacional para as despesas soberanas de defesa.",
        "en_d": "Mass-market National War Bonds mobilize domestic savings across all social strata, underpinning sovereign wartime credit with patriotic discipline.",
        "reward": """add_political_power = 60
add_stability = 0.04
add_war_support = 0.03"""
    },
    "ENG_ww1_debt_service_commission": {
        "pt_t": "Comissão de Serviço da Dívida Externa",
        "en_t": "Debt Service Commission",
        "pt_d": "Especialistas do Tesouro e banqueiros de Londres organizam o cronograma de liquidação de compromissos cambiais contraídos nos Estados Unidos.",
        "en_d": "Treasury and Bank of England specialists structure long-term debt repayment frameworks to safeguard the value of the Pound Sterling globally.",
        "reward": """add_political_power = 50
add_stability = 0.03
set_country_flag = ENG_ww1_debt_service_active"""
    },
    "ENG_ww1_convert_the_war_plants": {
        "pt_t": "Conversão das Fábricas Bélicas",
        "en_t": "Convert the War Plants",
        "pt_d": "Fábricas de artilharia e cartuchos são convertidas rapidamente para a produção de tratores, locomotivas civis, automóveis e bens de consumo popular.",
        "en_d": "Explosive and shell plants transition to civilian production of locomotives, commercial motorcars, and consumer goods to kickstart the postwar economy.",
        "reward": """128 = {
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
130 = {
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.05"""
    },
    "ENG_ww1_housing_and_civilian_employment": {
        "pt_t": "Habitação e Emprego: 'Lares Dignos de Heróis'",
        "en_t": "Housing and Civilian Employment",
        "pt_d": "O programa habitacional de Addison ('Homes Fit for Heroes') ergue conjuntos residenciais modernos com saneamento, gerando centenas de milhares de empregos.",
        "en_d": "The Addison Housing Act finances high-standard council housing with sanitation for demobilized veterans, generating widespread civilian employment.",
        "reward": """126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.05"""
    },
    "ENG_ww1_the_peace_administration_office": {
        "pt_t": "Gabinete de Administração da Paz",
        "en_t": "The Peace Administration Office",
        "pt_d": "Uma secretaria ministerial especial assume a gestão integrada da transição de emergência bélica para as garantias institucionais do tempo de paz.",
        "en_d": "A dedicated ministerial office coordinates the complex transition from total war mobilisation to peacetime civil administration.",
        "reward": """add_political_power = 75
add_stability = 0.05
set_country_flag = ENG_ww1_peace_office_founded"""
    },
    "ENG_ww1_military_demobilisation_planning": {
        "pt_t": "Planejamento da Desmobilização Militar",
        "en_t": "Military Demobilisation Planning",
        "pt_d": "Critérios escalonados por ocupação e tempo de serviço garantem o retorno ordeiro de milhões de soldados às suas cidades sem gerar colapso econômico.",
        "en_d": "A methodical points system prioritized by civilian profession and service duration facilitates the orderly repatriation of millions of frontline soldiers.",
        "reward": """add_manpower = 50000
add_stability = 0.05"""
    },
    "ENG_ww1_shipping_repatriation_coordination": {
        "pt_t": "Coordenação da Frota de Repatriação",
        "en_t": "Shipping Repatriation Coordination",
        "pt_d": "Navios mercantes e transatlânticos da Grã-Bretanha transportam divisões imperiais de volta ao Canadá, Austrália, Nova Zelândia e Índia com celeridade.",
        "en_d": "Liners and merchantmen under the Ministry of Shipping swiftly transport imperial contingents back to Canada, Australia, New Zealand, and India.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy_1
    amount = 150
    producer = ENG
}
add_political_power = 40"""
    },
    "ENG_ww1_veterans_welfare_register": {
        "pt_t": "Registro de Bem-Estar dos Veteranos",
        "en_t": "Veterans Welfare Register",
        "pt_d": "Criação de um cadastro nacional unificado para apoiar ex-combatentes com recolocação profissional, assistência psicológica e amparo familiar.",
        "en_d": "Establishment of a national register guaranteeing veteran rehabilitation, job placement, and family support networks across Britain.",
        "reward": """add_stability = 0.05
add_war_support = 0.05
add_political_power = 40"""
    },
    "ENG_ww1_disability_pension_administration": {
        "pt_t": "Administração de Pensões de Invalidez de Guerra",
        "en_t": "Disability Pension Administration",
        "pt_d": "O Ministério das Pensões garante auxílio financeiro vitalício e cuidados hospitalares para centenas de milhares de soldados amputados e gaseados.",
        "en_d": "The Ministry of Pensions secures lifelong financial sustenance and specialized clinical treatment for disabled veterans and war widows.",
        "reward": """add_stability = 0.08
add_political_power = 50"""
    },
    "ENG_ww1_civilian_training_for_returning_soldiers": {
        "pt_t": "Capacitação Civil para Veteranos",
        "en_t": "Civilian Training for Returning Soldiers",
        "pt_d": "Escolas técnicas e centros de aprendizagem industrial capacitam ex-soldados nas novas tecnologias mecânicas, elétricas e de engenharia automotiva.",
        "en_d": "Government training colleges qualify returning servicemen in modern mechanical engineering, electrical installations, and industrial trades.",
        "reward": """add_tech_bonus = {
    name = postwar_industry_bonus
    bonus = 1.0
    uses = 1
    category = industry
}
add_political_power = 40"""
    },
    "ENG_ww1_public_housing_contracts": {
        "pt_t": "Contratos de Habitação Pública Popular",
        "en_t": "Public Housing Contracts",
        "pt_d": "Recursos públicos são repassados aos conselhos municipais para erradicar favelas urbanas e construir moradias arejadas e dignas para as famílias operárias.",
        "en_d": "Municipal subsidies eradicate urban tenements, constructing high-standard suburban homes with electric lighting and green parklands.",
        "reward": """126 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.05"""
    },
    "ENG_ww1_industrial_conversion_planning": {
        "pt_t": "Planejamento de Reconversão Industrial",
        "en_t": "Industrial Conversion Planning",
        "pt_d": "Engenheiros civis e líderes fabris estabelecem diretrizes para rápida reconversão de plantas de explosivos em indústrias químicas de fertilizantes e plásticos.",
        "en_d": "Civilian planners and business federations facilitate the conversion of propellant plants into chemical fertilizer and synthetic dye manufacturers.",
        "reward": """130 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 2
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_the_employment_exchanges": {
        "pt_t": "Bolsas Nacionais de Emprego",
        "en_t": "The Employment Exchanges",
        "pt_d": "A rede pública de agências de trabalho cruza ofertas industriais e agrícolas com a mão de obra disponível, reduzindo drasticamente o desemprego pós-guerra.",
        "en_d": "The expanded network of state labour exchanges connects demobilized workers with industrial vacancies, stabilizing the post-war labor market.",
        "reward": """add_stability = 0.05
add_political_power = 50
set_country_flag = ENG_ww1_labour_exchanges_upgraded"""
    },
    "ENG_ww1_restore_civilian_railway_traffic": {
        "pt_t": "Restauração do Tráfego Ferroviário Civil",
        "en_t": "Restore Civilian Railway Traffic",
        "pt_d": "As locomotivas e vagões requisitados na guerra são revisados e devolvidos ao tráfego comercial, restaurando o transporte eficiente de bens de consumo.",
        "en_d": "Requisitioned rolling stock is fully refurbished and returned to commercial lines, restoring reliable domestic freight and commuter traffic.",
        "reward": """126 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
128 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
add_political_power = 40"""
    },
    "ENG_ww1_public_debt_repayment": {
        "pt_t": "Amortização Responsável da Dívida Pública",
        "en_t": "Public Debt Repayment",
        "pt_d": "Uma gestão orçamentária rigorosa e a amortização contínua de títulos nos mercados internacionais restauram a solidez inabalável da Libra Esterlina.",
        "en_d": "Disciplined fiscal management and orderly bond amortizations on international markets reaffirm the global primacy of the Pound Sterling.",
        "reward": """add_political_power = 75
add_stability = 0.05"""
    },
    "ENG_ww1_treasury_expenditure_review": {
        "pt_t": "Revisão de Despesas do Tesouro (Geddes Axe)",
        "en_t": "Treasury Expenditure Review",
        "pt_d": "O comitê liderado por Sir Eric Geddes elimina redundâncias administrativas e gastos militares supérfluos, equilibrando o orçamento nacional.",
        "en_d": "The committee chaired by Sir Eric Geddes cuts wartime bureaucratic overhead and redundant defense expenditures to balance the state budget.",
        "reward": """add_political_power = 75
add_stability = 0.04
set_country_flag = ENG_ww1_geddes_axe_passed"""
    },
    "ENG_ww1_merchant_marine_renewal": {
        "pt_t": "Renovação da Marinha Mercante",
        "en_t": "Merchant Marine Renewal",
        "pt_d": "Estaleiros do Tyne e do Clyde entregam modernos navios de carga movidos a óleo combustível, recompondo e ampliando a frota mercante imperial.",
        "en_d": "British shipyards build modern oil-fired freighters to replace wartime shipping losses, reasserting British mastery of global maritime commerce.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy_1
    amount = 200
    producer = ENG
}
133 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = dockyard
        level = 1
        instant_build = yes
    }
}"""
    },
    "ENG_ww1_the_public_health_settlement": {
        "pt_t": "Acordo Nacional de Saúde Pública",
        "en_t": "The Public Health Settlement",
        "pt_d": "A fundação do Ministério da Saúde unifica o combate a epidemias, saneamento urbano, assistência materno-infantil e vigilância sanitária nacional.",
        "en_d": "The creation of the Ministry of Health consolidates epidemic control, urban sanitation, and maternity welfare into a unified national system.",
        "reward": """add_stability = 0.08
add_manpower = 40000"""
    },
    "ENG_ww1_the_education_reconstruction_programme": {
        "pt_t": "Programa de Reconstrução da Educação (Fisher Act)",
        "en_t": "The Education Reconstruction Programme",
        "pt_d": "A Lei Fisher de 1918 eleva a idade escolar obrigatória para 14 anos e amplia colégios técnicos, forjando uma geração de trabalhadores altamente qualificados.",
        "en_d": "The Fisher Education Act raises the compulsory school age to 14 and expands continuation colleges, cultivating a highly literate technical generation.",
        "reward": """add_tech_bonus = {
    name = education_science_bonus
    bonus = 1.0
    uses = 2
    category = electronics
}
add_political_power = 50"""
    },
    "ENG_ww1_local_government_finance": {
        "pt_t": "Financiamento do Governo Local",
        "en_t": "Local Government Finance",
        "pt_d": "Repasses fiscais para os governos de condados e cidades financiam estradas pavimentadas, iluminação pública elétrica e serviços de água potável.",
        "en_d": "Fiscal block grants to county councils and municipal corporations finance paved highways, public electrical grids, and urban water works.",
        "reward": """126 = { add_extra_state_shared_building_slots = 1 }
128 = { add_extra_state_shared_building_slots = 1 }
130 = { add_extra_state_shared_building_slots = 1 }
132 = { add_extra_state_shared_building_slots = 1 }
add_political_power = 40"""
    },
    "ENG_ww1_the_industrial_relations_conference": {
        "pt_t": "Conferência Nacional de Relações Industriais",
        "en_t": "The Industrial Relations Conference",
        "pt_d": "Os Conselhos Whitley estabelecem fóruns permanentes de negociação paritária entre industriais e sindicatos, garantindo estabilidade produtiva duradoura.",
        "en_d": "Whitley Councils institutionalize joint industrial bargaining councils between trade unions and employers, preventing class conflict.",
        "reward": """add_stability = 0.08
add_political_power = 50"""
    },
    "ENG_ww1_the_postwar_parliamentary_mandate": {
        "pt_t": "O Mandato Parlamentar do Pós-Guerra",
        "en_t": "The Postwar Parliamentary Mandate",
        "pt_d": "A ratificação soberana de leis fundamentais pelos Comuns restabelece as liberdades civis plenas e a supremacia do direito parlamentar britânico.",
        "en_d": "The full restoration of civilian constitutional supremacy by Parliament dissolves wartime executive decrees and re-establishes British liberties.",
        "reward": """add_political_power = 100
add_stability = 0.05
set_country_flag = ENG_ww1_postwar_mandate_secured"""
    },
    "ENG_ww1_the_nineteen_twenty_two_cabinet": {
        "pt_t": "O Gabinete Conservador de 1922",
        "en_t": "The 1922 Conservative Cabinet",
        "pt_d": "A reunião histórica do Carlton Club dissolve a coalizão de Lloyd George; Bonar Law e Stanley Baldwin assumem o governo com foco na estabilidade e tranquilidade.",
        "en_d": "The Carlton Club meeting brings an end to the Lloyd George coalition, ushering in Bonar Law and Stanley Baldwin on a platform of tranquility and stability.",
        "reward": """add_political_power = 75
add_stability = 0.06
set_country_flag = ENG_ww1_conservative_rule_1922"""
    },
    "ENG_ww1_the_nineteen_twenty_three_settlement": {
        "pt_t": "A Consolidação Imperial de 1923",
        "en_t": "The 1923 Imperial Settlement",
        "pt_d": "O Reino Unido consolida sua recuperação interna e o alinhamento com a Comunidade de Nações, assegurando uma era de estabilidade democrática e prosperidade.",
        "en_d": "Britain cements its domestic recovery and economic equilibrium with the Commonwealth, inaugurating a decade of democratic resilience and peace.",
        "reward": """add_stability = 0.10
add_political_power = 100"""
    }
}
