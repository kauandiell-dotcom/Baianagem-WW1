# scripts/eng_data_politics.py
# British Empire WW1 - Politics & Imperial Governance (40 focuses)

POLITICS_DATA = {
    "ENG_ww1_parliament_act": {
        "pt_t": "A Lei do Parlamento de 1911",
        "en_t": "The Parliament Act of 1911",
        "pt_d": "A quebra definitiva do veto absoluto da Câmara dos Lordes consolida a primazia legislativa da Câmara dos Comuns, assegurando estabilidade institucional para aprovar os orçamentos do Estado.",
        "en_d": "The historic curtailment of the House of Lords' veto powers establishes the undisputed supremacy of the elected Commons, guaranteeing fiscal stability for essential state budgets.",
        "reward": """add_political_power = 75
add_stability = 0.05
set_country_flag = ENG_ww1_parliament_act_passed"""
    },
    "ENG_ww1_national_insurance": {
        "pt_t": "Seguro Nacional de Saúde e Desemprego",
        "en_t": "National Insurance Act",
        "pt_d": "A pioneira legislação de seguridade social de Lloyd George oferece auxílio-doença e proteção contra o desemprego para milhões de trabalhadores industriais britânicos.",
        "en_d": "Lloyd George's landmark social insurance reforms provide sickness benefits and unemployment protections to millions of British industrial workers, cementing working-class loyalty.",
        "reward": """add_stability = 0.05
add_political_power = 60"""
    },
    "ENG_ww1_the_liberal_cabinet": {
        "pt_t": "O Gabinete Liberal de H. H. Asquith",
        "en_t": "The Asquith Liberal Cabinet",
        "pt_d": "O Primeiro-Ministro Asquith conduz um governo de grandes talentos intelectuais, com Winston Churchill no Almirantado, Edward Grey no Foreign Office e Lloyd George no Tesouro.",
        "en_d": "Prime Minister Asquith directs a cabinet of formidable intellects, coordinating Winston Churchill at the Admiralty, Edward Grey in foreign policy, and Lloyd George at the Exchequer.",
        "reward": """add_political_power = 60
add_stability = 0.03
set_country_flag = ENG_ww1_liberal_government"""
    },
    "ENG_ww1_the_lords_and_the_commons": {
        "pt_t": "Equilíbrio entre Lordes e Comuns",
        "en_t": "The Lords and the Commons Balance",
        "pt_d": "A harmonização dos procedimentos parlamentares moderniza o rito legislativo em Westminster, permitindo tramitação veloz de leis vitais de arrecadação e defesa.",
        "en_d": "Streamlined legislative procedures at Westminster accelerate the passage of critical defense appropriations and imperial taxation bills.",
        "reward": """add_political_power = 50
add_stability = 0.03
set_country_flag = ENG_ww1_lords_curbed"""
    },
    "ENG_ww1_irish_parliamentary_support": {
        "pt_t": "A Aliança com o Partido Parlamentar Irlandês",
        "en_t": "Irish Parliamentary Accord",
        "pt_d": "O pacto de Asquith com John Redmond garante os votos nacionalistas irlandeses em Westminster em troca do compromisso solene de aprovar o Home Rule.",
        "en_d": "Asquith's legislative alliance with John Redmond's Irish Nationalist Party secures parliamentary majorities in return for the passage of Irish Home Rule.",
        "reward": """add_political_power = 60
add_stability = 0.04
set_country_flag = ENG_ww1_irish_party_support"""
    },
    "ENG_ww1_home_rule_bill": {
        "pt_t": "O Projeto de Autogoverno Irlandês (Home Rule)",
        "en_t": "Third Irish Home Rule Bill",
        "pt_d": "A introdução da lei concedendo parlamento próprio em Dublin reacende tensões inflamadas entre nacionalistas católicos e legalistas protestantes do Ulster.",
        "en_d": "The introduction of self-governance for Ireland triggers fervent celebrations across nationalist counties while provoking vehement resistance in Ulster.",
        "reward": """country_event = { id = ww1_britain_pol.1 }
add_political_power = 40
set_country_flag = ENG_ww1_home_rule_bill_introduced"""
    },
    "ENG_ww1_ulster_conference": {
        "pt_t": "A Conferência do Ulster & Pacto de Solemn League",
        "en_t": "The Ulster Crisis Conference",
        "pt_d": "Edward Carson mobiliza a Ulster Volunteer Force contra a submissão a Dublin. Westminster busca conciliação para evitar uma guerra civil nas ilhas britânicas.",
        "en_d": "Sir Edward Carson mobilizes the armed Ulster Volunteer Force, prompting urgent round-table consultations at Buckingham Palace to prevent fratricidal conflict.",
        "reward": """country_event = { id = ww1_britain_pol.2 }
add_political_power = 50"""
    },
    "ENG_ww1_electoral_registration": {
        "pt_t": "Reforma do Registro Eleitoral",
        "en_t": "Electoral Registration Act",
        "pt_d": "Modernização dos cadastros eleitorais urbanos e rurais, preparando as listas de votação e ampliando a transparência democrática.",
        "en_d": "Modernized voter rolls throughout the United Kingdom enhance civic participation and administrative responsiveness across regional constituencies.",
        "reward": """add_political_power = 50
add_stability = 0.03"""
    },
    "ENG_ww1_the_defence_of_the_realm": {
        "pt_t": "Lei de Defesa do Reino (DORA)",
        "en_t": "Defence of the Realm Act (DORA)",
        "pt_d": "Promulgada no início da guerra, a DORA concede ao Executivo amplos poderes para censurar correspondências de espionagem, controlar ferrovias e requisitar portos.",
        "en_d": "Passed upon the outbreak of war, DORA grants executive authority to censor sensitive dispatches, requisition civilian harbors, and take control of the rail network.",
        "reward": """swap_ideas = {
    remove_idea = ENG_irish_home_rule_tension
    add_idea = ENG_irish_home_rule_suspended
}
add_stability = 0.05
add_war_support = 0.05"""
    },
    "ENG_ww1_wartime_parliamentary_scrutiny": {
        "pt_t": "Supervisão Parlamentar de Guerra",
        "en_t": "Wartime Parliamentary Scrutiny",
        "pt_d": "Comissões multipartidárias fiscalizam gastos do Almirantado e do War Office, impedindo corrupção e desabastecimento nas frentes de batalha.",
        "en_d": "Cross-party select committees examine wartime expenditures, identifying logistical bottlenecks and holding military departments accountable.",
        "reward": """add_political_power = 75
add_stability = 0.04"""
    },
    "ENG_ww1_the_coalition_cabinet": {
        "pt_t": "O Gabinete de Coalizão de 1915",
        "en_t": "The 1915 Coalition Ministry",
        "pt_d": "A escassez crítica de obuses no front derruba o governo liberal puro. Asquith convoca conservadores e trabalhistas para formar uma frente nacional unida.",
        "en_d": "The catastrophic Shell Crisis forces the dissolution of the partisan Liberal cabinet, ushering in an all-party national coalition to mobilize the realm.",
        "reward": """country_event = { id = ww1_britain_pol.3 }
add_political_power = 80
add_stability = 0.05
set_country_flag = ENG_ww1_coalition_formed"""
    },
    "ENG_ww1_the_military_service_act": {
        "pt_t": "A Lei do Serviço Militar de 1916 (Conscrição)",
        "en_t": "Military Service Act 1916",
        "pt_d": "Diante das perdas avassaladoras nas trincheiras, a Grã-Bretanha abandona o voluntariado e introduz o recrutamento obrigatório para homens solteiros e casados.",
        "en_d": "Compelled by attrition on the Western Front, Parliament enacts universal conscription, guaranteeing an unbroken stream of divisions for Field Marshal Haig.",
        "reward": """add_manpower = 100000
add_war_support = 0.05
add_political_power = 40"""
    },
    "ENG_ww1_reserved_civilian_occupations": {
        "pt_t": "Ocupações Civis Reservadas",
        "en_t": "Reserved Civilian Occupations",
        "pt_d": "Mineiros de carvão, maquinistas de trem, metalúrgicos e operários de estaleiros são isentos da convocação para manter a máquina industrial britânica a todo vapor.",
        "en_d": "Miners, railway engineers, and shipyard caulkers are exempted from trench conscription, shielding vital war production from devastating labor shortages.",
        "reward": """128 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_stability = 0.03"""
    },
    "ENG_ww1_the_war_cabinet": {
        "pt_t": "O Gabinete de Guerra de Lloyd George",
        "en_t": "Lloyd George's Supreme War Cabinet",
        "pt_d": "David Lloyd George assume como Primeiro-Ministro com um conselho executivo de cinco líderes dedicados dia e noite à condução implacável da vitória militar.",
        "en_d": "David Lloyd George establishes a streamlined War Cabinet of five ministers, concentrating supreme decision-making authority to prosecute total war to victory.",
        "reward": """add_political_power = 100
add_war_support = 0.05
army_experience = 15
navy_experience = 15"""
    },
    "ENG_ww1_the_franchise_debate": {
        "pt_t": "O Debate da Extensão do Sufrágio",
        "en_t": "The Franchise Expansion Debate",
        "pt_d": "O sacrifício heróico dos soldados nas trincheiras e das mulheres nas fábricas de armas torna indefensável a exclusão de milhões da cidadania plena.",
        "en_d": "The heroism of millions in the trenches and the indispensability of female munition workers dismantle centuries of resistance to universal adult franchise.",
        "reward": """add_political_power = 60
add_stability = 0.04"""
    },
    "ENG_ww1_representation_of_the_people": {
        "pt_t": "Lei de Representação do Povo de 1918",
        "en_t": "Representation of the People Act 1918",
        "pt_d": "Todos os homens maiores de 21 anos e mulheres maiores de 30 recebem o voto, multiplicando o eleitorado britânico de 8 para mais de 21 milhões de pessoas.",
        "en_d": "Franchise is granted to all men over 21 and women over 30, expanding the electorate from 8 to 21 million citizens in a triumph of British democracy.",
        "reward": """swap_ideas = {
    remove_idea = ENG_irish_home_rule_suspended
    add_idea = ENG_irish_home_rule_compromise
}
add_stability = 0.08
add_political_power = 75"""
    },
    "ENG_ww1_the_coalition_election": {
        "pt_t": "A Eleição do Cupom de 1918",
        "en_t": "The Coupon Election of 1918",
        "pt_d": "Imediatamente após o Armistício, o governo de coalizão de Lloyd George obtém esmagadora vitória eleitoral com a promessa de reconstrução e justiça.",
        "en_d": "Following the Armistice, the coalition between Lloyd George and Conservative leaders wins an overwhelming parliamentary majority on a platform of renewal.",
        "reward": """add_political_power = 100
add_stability = 0.08
set_country_flag = ENG_ww1_coalition_victorious"""
    },
    "ENG_ww1_liberal_reconstruction": {
        "pt_t": "Programa de Reconstrução Social Liberal",
        "en_t": "Liberal Reconstruction Mandate",
        "pt_d": "Investimentos massivos em saúde comunitária, habitação pública e seguridade desfazem as cicatrizes da guerra nos bairros fabris.",
        "en_d": "Public housing initiatives, clinics, and expanded pensions heal domestic wounds, rewarding the sacrifices of the working classes.",
        "reward": """126 = {
    add_extra_state_shared_building_slots = 2
    add_building_construction = {
        type = industrial_complex
        level = 2
        instant_build = yes
    }
}
add_stability = 0.05"""
    },
    "ENG_ww1_the_labour_alternative": {
        "pt_t": "A Ascensão Trabalhista de Ramsay MacDonald",
        "en_t": "The Rise of the Labour Party",
        "pt_d": "O Partido Trabalhista se consolida como grande força de oposição, defendendo a Carta de Direitos dos Trabalhadores, controle estatal de serviços e diplomacia pacífica.",
        "en_d": "The Labour Party under Ramsay MacDonald rises as a premier parliamentary force, championing nationalization of utilities and collective security.",
        "reward": """add_political_power = 80
set_popularities = { democratic = 50 neutrality = 30 communism = 20 }"""
    },
    "ENG_ww1_the_conservative_settlement": {
        "pt_t": "A Ordem Conservadora de Bonar Law",
        "en_t": "The Conservative Settlement of Bonar Law",
        "pt_d": "Andrew Bonar Law e os conservadores assumem a liderança nacional, priorizando a disciplina fiscal, preferências comerciais imperiais e coesão da Coroa.",
        "en_d": "Andrew Bonar Law leads a Conservative ministry committed to balanced budgets, Imperial tariff preferences, and imperial solidarity.",
        "reward": """add_political_power = 100
add_stability = 0.06"""
    },
    "ENG_ww1_the_imperial_conference": {
        "pt_t": "A Conferência Imperial de 1911",
        "en_t": "The 1911 Imperial Conference",
        "pt_d": "Os Primeiros-Ministros do Canadá, Austrália, Nova Zelândia e África do Sul reúnem-se em Londres para coordenar planos de defesa marítima e telégrafo imperial.",
        "en_d": "Prime Ministers of the Dominions convene in London to coordinate imperial naval defenses, wireless networks, and shared strategic priorities.",
        "reward": """country_event = { id = ww1_britain_pol.6 }
add_political_power = 50
set_country_flag = ENG_ww1_imperial_conference_held"""
    },
    "ENG_ww1_canadian_defence_consultation": {
        "pt_t": "O Corpo Canadense e Sir Robert Borden",
        "en_t": "Canadian Corps Mobilization",
        "pt_d": "O Canadá mobiliza centenas de milhares de voluntários. O Corpo Canadense, comandado por Sir Arthur Currie, torna-se uma das forças de choque mais temidas da Europa.",
        "en_d": "Canada rallies hundreds of thousands of volunteers; under Sir Arthur Currie, the Canadian Corps emerges as the premier shock formation on the Western Front.",
        "reward": """add_tech_bonus = { name = canadian_doctrine bonus = 1.0 uses = 1 category = land_doctrine }
add_manpower = 75000
123 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }"""
    },
    "ENG_ww1_australian_defence_consultation": {
        "pt_t": "O Lendário Corpo Australiano (AIF)",
        "en_t": "Australian Imperial Force (AIF)",
        "pt_d": "Os bravos soldados do ANZAC e do general Sir John Monash cobrem-se de glória em Galípoli e na Frente Ocidental, liderando o avanço de armas combinadas em Hamel e Amiens.",
        "en_d": "Volunteers of the Australian Imperial Force, led by Sir John Monash, master combined-arms warfare at Hamel and spearhead the Hundred Days Offensive.",
        "reward": """add_tech_bonus = { name = anzac_infantry bonus = 1.0 uses = 1 category = infantry_weapons }
add_manpower = 60000
army_experience = 25"""
    },
    "ENG_ww1_new_zealand_naval_consultation": {
        "pt_t": "A Divisão Neozelandesa e o HMS New Zealand",
        "en_t": "New Zealand Naval and Expeditionary Force",
        "pt_d": "A Nova Zelândia financia o cruzador de batalha HMS New Zealand para a Grand Fleet e envia sua excelente divisão de infantaria veterana às frentes da Europa.",
        "en_d": "New Zealand gifts the battlecruiser HMS New Zealand to the Royal Navy and deploys exceptional infantry regiments to the Dardanelles and France.",
        "reward": """navy_experience = 20
add_manpower = 25000
add_political_power = 40"""
    },
    "ENG_ww1_south_african_cooperation": {
        "pt_t": "Cooperação Sul-Africana de Botha e Smuts",
        "en_t": "South African Defense under Botha & Smuts",
        "pt_d": "Os generais Louis Botha e Jan Smuts conquistam o Sudoeste Africano Alemão e enviam brigadas experientes para o Front Ocidental e a África Oriental.",
        "en_d": "Generals Louis Botha and Jan Smuts secure German South-West Africa and deploy crack brigades to Delville Wood and the East African theater.",
        "reward": """add_manpower = 35000
add_political_power = 50"""
    },
    "ENG_ww1_indian_army_liaison": {
        "pt_t": "Mobilização do Exército Indiano",
        "en_t": "Indian Army Global Mobilization",
        "pt_d": "Mais de 1,3 milhão de valorosos soldados indianos lutam na França, na Mesopotâmia, no Sinai e em Galípoli, sustentando o Império com heroísmo e disciplina.",
        "en_d": "Over 1.3 million Indian soldiers deploy across France, Mesopotamia, and Egypt, providing indispensable manpower and fighting valor to imperial fronts.",
        "reward": """add_manpower = 200000
126 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
add_war_support = 0.05"""
    },
    "ENG_ww1_colonial_medical_services": {
        "pt_t": "Serviços Médicos Imperiais e Hospitais de Campanha",
        "en_t": "Imperial Medical Services",
        "pt_d": "Ambulâncias motorizadas, hospitais de retaguarda e enfermarias coloniais reduzem drasticamente as mortes por febre e infecções nos fronts tropicais e europeus.",
        "en_d": "Expanded field dressing stations, motor ambulances, and convalescent depots preserve the lives of wounded soldiers across European and tropical theaters.",
        "reward": """add_tech_bonus = { name = field_medicine bonus = 1.0 uses = 1 category = hospital_tech }
add_stability = 0.04"""
    },
    "ENG_ww1_dominion_procurement_offices": {
        "pt_t": "Comissões de Compras dos Domínios",
        "en_t": "Dominion War Supply Integration",
        "pt_d": "Fábricas de munição canadenses, trigo australiano e lã neozelandesa são integrados em um circuito logístico soberano e contínuo para o esforço de guerra.",
        "en_d": "Canadian shell foundries, Australian durum wheat, and New Zealand wool are systematically funneled into the imperial logistical pipeline.",
        "reward": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 5000
    producer = ENG
}
add_political_power = 40"""
    },
    "ENG_ww1_the_mediterranean_stations": {
        "pt_t": "As Estações Navais de Gibraltar e Malta",
        "en_t": "Gibraltar and Malta Bastions",
        "pt_d": "Os baluartes estratégicos de Gibraltar e Malta protegem as rotas de passagem para o Canal de Suez e o comércio com a Índia e o Pacífico.",
        "en_d": "Fortified anchorages at Gibraltar and Malta safeguard the vital Mediterranean conduit linking Britain with Egypt, India, and the Far East.",
        "reward": """navy_experience = 25
118 = { add_building_construction = { type = coastal_bunker level = 2 instant_build = yes } }"""
    },
    "ENG_ww1_singapore_maritime_coordination": {
        "pt_t": "Coordenação Marítima de Singapura",
        "en_t": "Singapore Naval Coordination Hub",
        "pt_d": "O controle dos estreitos de Malaca e depósitos de carvão em Singapura garantem que cruzadores corsários inimigos não perturbem as rotas do Extremo Oriente.",
        "en_d": "Coaling stations and patrol flotillas based at Singapore secure the Malacca Strait, denying raiders access to Pacific imperial shipping.",
        "reward": """navy_experience = 15
336 = { add_building_construction = { type = dockyard level = 1 instant_build = yes } }"""
    },
    "ENG_ww1_imperial_troop_transport": {
        "pt_t": "Comboios Imperiais de Transporte de Tropas",
        "en_t": "Imperial Troop Convoy Escorts",
        "pt_d": "Transatlânticos oceânicos de passageiros como o Olympic e o Mauretania são convertidos em transportes rápidos blindados protegidos pela Marinha Real.",
        "en_d": "Luxury ocean liners, including the Olympic and Mauretania, are armed as high-speed troopships, ferrying hundreds of thousands safely across oceans.",
        "reward": """swap_ideas = {
    remove_idea = ENG_the_imperial_web
    add_idea = ENG_the_imperial_web_t2
}
add_equipment_to_stockpile = {
    type = convoy
    amount = 100
    producer = ENG
}
add_war_support = 0.05"""
    },
    "ENG_ww1_the_imperial_war_conference": {
        "pt_t": "A Conferência de Guerra Imperial de 1917",
        "en_t": "The Imperial War Conference of 1917",
        "pt_d": "Pela primeira vez na história, os chefes de governo dos Domínios deliberam de igual para igual sobre as decisões estratégicas do Império Britânico.",
        "en_d": "Dominion Prime Ministers join the Imperial War Cabinet, gaining a direct voice in the strategic direction of the war and postwar treaties.",
        "reward": """add_political_power = 100
add_war_support = 0.08
add_stability = 0.05"""
    },
    "ENG_ww1_dominion_war_cabinet_delegates": {
        "pt_t": "Delegados dos Domínios no Gabinete de Guerra",
        "en_t": "Dominion War Cabinet Delegates",
        "pt_d": "Sir Robert Borden e Jan Smuts assumem responsabilidades operacionais diretas no planejamento de frentes militares e diplomáticas.",
        "en_d": "Eminent Dominion statesmen direct high military councils, coordinating resources across five continents toward imperial victory.",
        "reward": """swap_ideas = {
    remove_idea = ENG_the_imperial_web_t2
    add_idea = ENG_the_imperial_web_t3
}
add_political_power = 75
add_stability = 0.05"""
    },
    "ENG_ww1_indian_constitutional_consultation": {
        "pt_t": "Declaração Montagu e Reformas na Índia",
        "en_t": "Montagu Declaration on India",
        "pt_d": "Em reconhecimento à lealdade e bravura incomparável dos soldados indianos, a Grã-Bretanha anuncia a meta de desenvolvimento gradual de autogoverno na Índia.",
        "en_d": "The historic Montagu Declaration pledges gradual development of self-governing institutions, honoring India's monumental contribution to the war effort.",
        "reward": """add_stability = 0.08
add_political_power = 60"""
    },
    "ENG_ww1_colonial_labour_contracts": {
        "pt_t": "Corpos Auxiliares de Trabalho do Império",
        "en_t": "Auxiliary Labor Corps",
        "pt_d": "Trabalhadores voluntários egípcios, chineses e sul-africanos descarregam navios nos portos franceses e pavimentam ferrovias vitais no front.",
        "en_d": "Hundreds of thousands of workers keep French ports and supply railheads operating around the clock, relieving combat troops for frontline service.",
        "reward": """production_speed_infrastructure_factor = 0.20
production_speed_rail_way_factor = 0.20"""
    },
    "ENG_ww1_a_commonwealth_consultation_charter": {
        "pt_t": "A Carta da Comunidade Britânica (Commonwealth)",
        "en_t": "Commonwealth Partnership Charter",
        "pt_d": "O Império evolui conscientemente para uma associação livre de nações soberanas unidas por valores compartilhados e lealdade à mesma Coroa.",
        "en_d": "The British Empire transforms into an egalitarian Commonwealth of free nations, bound by voluntary allegiance and constitutional liberty.",
        "reward": """add_stability = 0.10
add_political_power = 100"""
    },
    "ENG_ww1_the_irish_settlement_conference": {
        "pt_t": "A Conferência Constitucional Irlandesa",
        "en_t": "The Irish Constitutional Convention",
        "pt_d": "Negociações intensas buscam conciliar o nacionalismo irlandês e os protestantes do Ulster antes que a guerrilha consuma a ilha.",
        "en_d": "All-party deliberations seek a lasting constitutional compromise to avert civil war and reconcile Irish aspirations with imperial security.",
        "reward": """add_political_power = 60
add_stability = 0.05"""
    },
    "ENG_ww1_dominion_status_for_ireland": {
        "pt_t": "O Tratado Anglo-Irlandês & Status de Domínio",
        "en_t": "Anglo-Irish Treaty & Dominion Status",
        "pt_d": "A criação do Estado Livre Irlandês com status de Domínio paritário ao Canadá pacifica as relações históricas, mantendo bases navais vitais para a Royal Navy.",
        "en_d": "The establishment of the Irish Free State as a self-governing Dominion ends decades of bitter conflict while securing essential Treaty Ports for the Royal Navy.",
        "reward": """remove_ideas = ENG_irish_home_rule_tension
add_stability = 0.15
add_political_power = 75"""
    },
    "ENG_ww1_egyptian_political_negotiations": {
        "pt_t": "O Protetorado e Acordo do Egito",
        "en_t": "Egyptian Protectorate Treaty",
        "pt_d": "O Egito torna-se protetorado britânico formalizado, garantindo a proteção perpétua do Canal de Suez contra incursões otomanas e germânicas.",
        "en_d": "Formalization of the British Protectorate over Egypt guarantees the inviolability of the Suez Canal and stages the triumphant Levant campaigns.",
        "reward": """add_stability = 0.05
447 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }"""
    },
    "ENG_ww1_imperial_defence_after_the_war": {
        "pt_t": "Doutrina Pós-Guerra de Defesa Imperial",
        "en_t": "Postwar Imperial Defense Architecture",
        "pt_d": "A Royal Navy e os exércitos dos Domínios integram seus estados-maiores permanentes, assegurando que o Império Britânico permaneça inexpugnável em qualquer continente.",
        "en_d": "Integrated naval and air garrisons throughout the globe ensure that the British Empire emerges from the Great War as the preeminent global power.",
        "reward": """add_stability = 0.08
add_war_support = 0.05
add_political_power = 100"""
    }
}
