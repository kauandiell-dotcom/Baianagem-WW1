# -*- coding: utf-8 -*-
"""France Wing 3: Império Colonial & La Force Noire (25 focuses).
X range: 32 .. 42 | Y range: 0 .. 10
"""

WING3_FOCI = [
    # Y = 0
    {
        "id": "FRA_l_empire_colonial_francais",
        "x": 37, "y": 0, "cost": 10,
        "icon": "GFX_FRA_l_empire_colonial_francais",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 50
459 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
671 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "The French Colonial Empire",
        "title_pt": "O Império Colonial Francês",
        "desc_en": "Covering over ten million square kilometres across Africa and Asia, the overseas empire provides strategic depth, vital raw materials, and millions of devoted subjects to the tricolor.",
        "desc_pt": "Cobrindo mais de dez milhões de quilômetros quadrados na África e Ásia, o império ultramarino oferece profundidade estratégica, matérias-primas e milhões de súditos leais ao tricolor."
    },

    # Y = 1
    {
        "id": "FRA_mise_en_valeur_de_l_algerie",
        "x": 34, "y": 1, "cost": 8,
        "icon": "GFX_FRA_mise_en_valeur_de_l_algerie",
        "prereq": ["FRA_l_empire_colonial_francais"], "mut": [],
        "reward": """459 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Development of French Algeria",
        "title_pt": "Desenvolvimento da Argélia Francesa",
        "desc_en": "Treated as integral departments of France, Algiers and Oran receive modern agricultural equipment, vineyards, and expanded ports to supply the mainland with grain, wine, and livestock.",
        "desc_pt": "Considerados departamentos integrantes da França, Argel e Oran recebem maquinário agrícola, vinhedos e portos ampliados para abastecer a metrópole com trigo, vinho e rebanhos."
    },
    {
        "id": "FRA_protectorat_marocain_lyautey",
        "x": 40, "y": 1, "cost": 8,
        "icon": "GFX_FRA_protectorat_marocain_lyautey",
        "prereq": ["FRA_l_empire_colonial_francais"], "mut": [],
        "reward": """add_ideas = FRA_lyautey_moroccan_order
461 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Lyautey's Moroccan Protectorate",
        "title_pt": "O Protetorado Marroquino de Lyautey",
        "desc_en": "General Hubert Lyautey administers Morocco with profound respect for indigenous institutions, pacifying tribal dissidence through economic building, roads, and medical dispensaries.",
        "desc_pt": "O General Hubert Lyautey governa o Marrocos com respeito às instituições locais, pacificando tribos dissidentes por meio de estradas, hospitais e desenvolvimento comercial."
    },

    # Y = 2
    {
        "id": "FRA_mines_de_fer_de_l_ouenza",
        "x": 34, "y": 2, "cost": 8,
        "icon": "GFX_FRA_mines_de_fer_de_l_ouenza",
        "prereq": ["FRA_mise_en_valeur_de_l_algerie"], "mut": [],
        "reward": """460 = { add_resource = { type = steel amount = 14 } }
460 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Ouenza Iron Ore Deposits",
        "title_pt": "Minas de Ferro de Ouenza",
        "desc_en": "Opening the mammoth open-cast iron deposits of Ouenza in eastern Algeria sends high-grade hematite ore via rail to Bône port, directly feeding metropolitan blast furnaces.",
        "desc_pt": "A exploração a céu aberto das gigantescas jazidas de hematita de Ouenza no leste da Argélia envia minério de alta pureza por ferrovia ao porto de Bône para a metrópole."
    },
    {
        "id": "FRA_phosphates_de_tunisie",
        "x": 40, "y": 2, "cost": 8,
        "icon": "GFX_FRA_phosphates_de_tunisie",
        "prereq": ["FRA_protectorat_marocain_lyautey"], "mut": [],
        "reward": """458 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Tunisian Phosphate Mines of Gafsa",
        "title_pt": "Minas de Fosfato de Gafsa na Tunísia",
        "desc_en": "The phosphate deposits of Gafsa provide essential raw material for chemical fertilizers, nitric acid synthesis, and munitions manufacturing across metropolitan plants.",
        "desc_pt": "As jazidas de fosfato de Gafsa fornecem matéria-prima indispensável para fertilizantes agrícolas, síntese de ácido nítrico e manufatura de munições na França."
    },

    # Y = 3
    {
        "id": "FRA_chemins_de_fer_nord_africains",
        "x": 37, "y": 3, "cost": 8,
        "icon": "GFX_FRA_chemins_de_fer_nord_africains",
        "prereq": ["FRA_mines_de_fer_de_l_ouenza", "FRA_phosphates_de_tunisie"], "mut": [],
        "reward": """459 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
460 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
458 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Trans-Maghreb Railway Interconnection",
        "title_pt": "Interconexão Ferroviária do Norte da África",
        "desc_en": "Standardising track gauge and completing the trunk lines linking Casablanca, Fez, Algiers, and Tunis enables rapid east-west troop movements across French North Africa.",
        "desc_pt": "A unificação da bitola e conclusão das linhas ligando Casablanca, Fez, Argel e Túnis permite a rápida redistribuição militar e de cargas por todo o Magrebe francês."
    },

    # Y = 4
    {
        "id": "FRA_l_indochine_francaise",
        "x": 34, "y": 4, "cost": 8,
        "icon": "GFX_FRA_l_indochine_francaise",
        "prereq": ["FRA_l_empire_colonial_francais"], "mut": [],
        "reward": """671 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "French Indochina & The Red River",
        "title_pt": "A Indochina Francesa e o Rio Vermelho",
        "desc_en": "Governor-General Albert Sarraut modernizes colonial governance across Tonkin, Annam, and Cochin-China, building schools, medical stations, and dikes in the rice deltas.",
        "desc_pt": "O Governador-Geral Albert Sarraut moderniza a administração em Tonkin, Annam e Cochinchina, construindo escolas, postos médicos e diques nos deltas arrozeiros."
    },
    {
        "id": "FRA_afrique_occidentale_francaise_aof",
        "x": 40, "y": 4, "cost": 8,
        "icon": "GFX_FRA_afrique_occidentale_francaise_aof",
        "prereq": ["FRA_l_empire_colonial_francais"], "mut": [],
        "reward": """add_political_power = 30
add_ideas = FRA_colonial_order_aof""",
        "title_en": "French West Africa Federation (AOF)",
        "title_pt": "Federação da África Ocidental Francesa (AOF)",
        "desc_en": "Coordinating administrative policy from Saint-Louis and Dakar guarantees peaceful governance across Senegal, French Guinea, Ivory Coast, and Dahomey.",
        "desc_pt": "A coordenação a partir de Saint-Louis e Dakar garante estabilidade administrativa e governança pacífica no Senegal, Guiné Francesa, Costa do Marfim e Daomé."
    },

    # Y = 5
    {
        "id": "FRA_caoutchouc_et_riz_d_indochine",
        "x": 34, "y": 5, "cost": 8,
        "icon": "GFX_FRA_caoutchouc_et_riz_d_indochine",
        "prereq": ["FRA_l_indochine_francaise"], "mut": [],
        "reward": """671 = { add_resource = { type = rubber amount = 16 } }""",
        "title_en": "Indochinese Rubber & Rice Harvests",
        "title_pt": "Látex e Colheitas de Arroz da Indochina",
        "desc_en": "Expanding Hevea rubber plantations in the red earth regions of Cambodia and Cochinchina feeds Michelin's pneumatic tyre mills, insulating France from rubber shortages.",
        "desc_pt": "As plantações de seringueiras nas terras vermelhas do Camboja e Cochinchina abastecem as fábricas de pneus da Michelin, blindando a França contra a escassez de borracha."
    },
    {
        "id": "FRA_port_strategique_de_dakar",
        "x": 40, "y": 5, "cost": 8,
        "icon": "GFX_FRA_port_strategique_de_dakar",
        "prereq": ["FRA_afrique_occidentale_francaise_aof"], "mut": [],
        "reward": """add_ideas = FRA_dakar_atlantic_hub
add_political_power = 25""",
        "title_en": "Strategic Deep-Water Port of Dakar",
        "title_pt": "Porto Estratégico de Águas Profundas de Dakar",
        "desc_en": "Deepening harbor basins, installing coal bunkering facilities, and fortifying Cap-Vert makes Dakar the premier naval pivot for French transatlantic and South Atlantic shipping.",
        "desc_pt": "A dragagem dos canais, depósitos de carvão e fortificação do Cabo Verde tornam Dakar a principal base naval francesa para as rotas do Atlântico Sul."
    },
    {
        "id": "FRA_chemin_de_fer_dakar_niger",
        "x": 42, "y": 5, "cost": 8,
        "icon": "GFX_FRA_chemin_de_fer_dakar_niger",
        "prereq": ["FRA_afrique_occidentale_francaise_aof"], "mut": [],
        "reward": """add_ideas = FRA_dakar_niger_logistics
add_political_power = 20""",
        "title_en": "Dakar-Niger Railway Construction",
        "title_pt": "Ferrovia Dakar-Níger",
        "desc_en": "Extending railway lines through French Sudan to Bamako unlocks peanut exports and accelerates colonial troop transport from the interior to coastal ports.",
        "desc_pt": "A extensão da linha férrea através do Sudão Francês até Bamako escoa safras e acelera o transporte de recrutas coloniais do interior para o litoral."
    },

    # Y = 6
    {
        "id": "FRA_base_navale_de_saigon",
        "x": 34, "y": 6, "cost": 8,
        "icon": "GFX_FRA_base_navale_de_saigon",
        "prereq": ["FRA_caoutchouc_et_riz_d_indochine"], "mut": [],
        "reward": """671 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }
add_political_power = 25""",
        "title_en": "Saïgon River Arsenal & Dry Dock",
        "title_pt": "Arsenal Fluvial e Dique Seco de Saïgon",
        "desc_en": "Maintaining gunboats, colonial sloops, and repair basins in Saïgon secures French maritime presence in the South China Sea and safeguards trade routes.",
        "desc_pt": "A manutenção de canhoneiras, avisos coloniais e bacias de reparo em Saïgon consolida a presença marítima francesa no Mar do Sul da China e protege o tráfego comercial."
    },
    {
        "id": "FRA_ressources_de_madagascar",
        "x": 40, "y": 6, "cost": 8,
        "icon": "GFX_FRA_ressources_de_madagascar",
        "prereq": ["FRA_port_strategique_de_dakar"], "mut": [],
        "reward": """add_ideas = FRA_madagascar_strategic_minerals""",
        "title_en": "Madagascar Graphite & Strategic Minerals",
        "title_pt": "Grafite e Minerais Estratégicos de Madagascar",
        "desc_en": "Madagascar supplies crucial flake graphite for metallurgy crucibles, mica for electrical insulation, and beef shipments for frontline poilu rations.",
        "desc_pt": "Madagascar fornece grafite cristalino para cadinhos metalúrgicos, mica para isolamento elétrico e carne em conserva para a alimentação dos soldados no front."
    },
    {
        "id": "FRA_ports_de_madagascar",
        "x": 42, "y": 6, "cost": 8,
        "icon": "GFX_FRA_ports_de_madagascar",
        "prereq": ["FRA_port_strategique_de_dakar"], "mut": [],
        "reward": """add_political_power = 25
add_ideas = FRA_tamatave_port_infrastructure""",
        "title_en": "Deep-Water Port of Tamatave",
        "title_pt": "Porto de Águas Profundas de Tamatave",
        "desc_en": "Developing quays and breakwaters at Tamatave and Diego Suarez establishes secure Indian Ocean coaling stations for colonial cruising squadrons.",
        "desc_pt": "A ampliação dos cais e quebra-mares em Tamatave e Diego Suarez garante bases de abastecimento de carvão no Oceano Índico para cruzadores coloniais."
    },

    # Y = 7
    {
        "id": "FRA_la_force_noire_de_mangin",
        "x": 37, "y": 7, "cost": 8,
        "icon": "GFX_FRA_la_force_noire_de_mangin",
        "prereq": ["FRA_chemins_de_fer_nord_africains", "FRA_port_strategique_de_dakar"], "mut": [],
        "reward": """swap_ideas = {
    remove_idea = FRA_demographic_stagnation
    add_idea = FRA_three_year_law_and_colonial_ranks
}
add_ideas = FRA_force_noire_integration
add_political_power = 40""",
        "title_en": "General Mangin's 'La Force Noire'",
        "title_pt": "A 'Force Noire' do General Mangin",
        "desc_en": "Lieutenant-Colonel Charles Mangin's prophetic treatise urges tapping the vast manpower of French West Africa to offset Germany's massive demographic advantage in Europe.",
        "desc_pt": "A tese profética do Coronel Charles Mangin defende o recrutamento do vasto contingente da África Ocidental para compensar a superioridade demográfica alemã na Europa."
    },

    # Y = 8
    {
        "id": "FRA_recrutement_des_spahis_algeriens",
        "x": 36, "y": 8, "cost": 8,
        "icon": "GFX_FRA_recrutement_des_spahis_algeriens",
        "prereq": ["FRA_la_force_noire_de_mangin"], "mut": [],
        "reward": """add_ideas = FRA_algerian_spahis_cavalry
add_manpower = 20000""",
        "title_en": "Algerian Spahis Cavalry Regiments",
        "title_pt": "Regimentos de Cavalaria dos Spahis Argelinos",
        "desc_en": "Dashing horsemen mounted on hardy North African barbs provide mobile reconnaissance, outpost screening, and pursuit cavalry on the Aisne and Champagne plains.",
        "desc_pt": "Montados em velozes cavalos berberes, os ginetes dos spahis argelinos realizam missões de reconhecimento móvel e perseguição nas planícies de Champagne."
    },

    # Y = 8
    {
        "id": "FRA_tirailleurs_senegalais",
        "x": 34, "y": 8, "cost": 8,
        "icon": "GFX_FRA_tirailleurs_senegalais",
        "prereq": ["FRA_la_force_noire_de_mangin"], "mut": [],
        "reward": """add_ideas = FRA_tirailleurs_senegalais_valor
add_manpower = 45000""",
        "title_en": "Tirailleurs Sénégalais Shock Battalions",
        "title_pt": "Batalhões de Assalto dos Tirailleurs Sénégalais",
        "desc_en": "Equipped with Lebel rifles and distinctive red chechias, the disciplined Senegalese tirailleurs serve with legendary courage at Ypres, the Somme, and Chemin des Dames.",
        "desc_pt": "Armados com fuzis Lebel e distintas quépis vermelhas, os disciplinados tirailleurs senegaleses combatem com lendária bravura em Ypres, no Somme e no Chemin des Dames."
    },
    {
        "id": "FRA_zouaves_et_spahis_d_afrique",
        "x": 40, "y": 8, "cost": 8,
        "icon": "GFX_FRA_zouaves_et_spahis_d_afrique",
        "prereq": ["FRA_la_force_noire_de_mangin"], "mut": [],
        "reward": """add_ideas = FRA_nineteenth_corps_african_army
add_manpower = 40000""",
        "title_en": "19th Army Corps (Zouaves, Spahis & Chasseurs)",
        "title_pt": "19º Corpo de Exército (Zouaves, Spahis e Chasseurs)",
        "desc_en": "The storied 19th Army Corps from Algeria and Morocco deploys elite colonial divisions to France, spearheaded by fierce Berber horsemen and veteran settler infantry.",
        "desc_pt": "O lendário 19º Corpo de Exército da Argélia e Marrocos envia divisões coloniais de elite à França, encabeçadas por ginetes berberes e infantes veteranos."
    },

    # Y = 9
    {
        "id": "FRA_bataillons_indochinois_et_malgaches",
        "x": 34, "y": 9, "cost": 6,
        "icon": "GFX_FRA_bataillons_indochinois_et_malgaches",
        "prereq": ["FRA_tirailleurs_senegalais"], "mut": [],
        "reward": """add_ideas = FRA_colonial_logistics_labor
add_manpower = 25000""",
        "title_en": "Indochinese & Malagasy Pioneer Battalions",
        "title_pt": "Batalhões de Pioneiros Indochineses e Malgaxes",
        "desc_en": "Over one hundred thousand Vietnamese and Malagasy recruits serve in ammunition factories, motor transport columns, hospital units, and trench excavation details.",
        "desc_pt": "Mais de cem mil recrutas vietnamitas e malgaxes operam fábricas de pólvora, colunas de transporte motorizado, hospitais de campanha e trabalhos de escavação."
    },
    {
        "id": "FRA_citoyennete_et_recompenses_coloniales",
        "x": 40, "y": 9, "cost": 8,
        "icon": "GFX_FRA_citoyennete_et_recompenses_coloniales",
        "prereq": ["FRA_zouaves_et_spahis_d_afrique"], "mut": [],
        "reward": """add_political_power = 60
add_stability = 0.05
add_ideas = FRA_blaise_diagne_citizenship_reforms""",
        "title_en": "Blaise Diagne's Citizenship Reforms",
        "title_pt": "Reformas de Cidadania de Blaise Diagne",
        "desc_en": "Senegalese deputy Blaise Diagne secures full French citizenship for residents of the Four Communes of Senegal in exchange for enthusiastic military enlistment.",
        "desc_pt": "O deputado senegalês Blaise Diagne assegura plena cidadania francesa aos habitantes das Quatro Comunas do Senegal em contrapartida ao engajamento patriótico militar."
    },

    # Y = 10
    {
        "id": "FRA_le_sang_de_l_empire",
        "x": 37, "y": 10, "cost": 10,
        "icon": "GFX_FRA_le_sang_de_l_empire",
        "prereq": ["FRA_bataillons_indochinois_et_malgaches", "FRA_citoyennete_et_recompenses_coloniales"], "mut": [],
        "reward": """add_ideas = FRA_imperial_blood_solidarity
add_war_support = 0.08
add_stability = 0.05
add_political_power = 50""",
        "title_en": "Blood of the Empire (Brotherhood of Arms)",
        "title_pt": "O Sangue do Império (Fraternidade de Armas)",
        "desc_en": "Over six hundred thousand colonial troops have fought across European battlefields. Their sacrifices irrevocably forge an enduring bond of mutual respect within the republic.",
        "desc_pt": "Mais de seiscentos mil soldados coloniais combateram nos campos da Europa. Seus sacrifícios forjam um laço inquebrantável de respeito mútuo dentro da república."
    },
    {
        "id": "FRA_chemins_de_fer_sahariens",
        "x": 32, "y": 3, "cost": 8,
        "icon": "GFX_FRA_chemins_de_fer_sahariens",
        "prereq": ["FRA_mise_en_valeur_de_l_algerie"], "mut": [],
        "reward": """459 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
460 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Saharan Outpost Supply Lines",
        "title_pt": "Linhas de Suprimento dos Fortes Saarianos",
        "desc_en": "Expanding caravan trails and light desert railway tracks from Biskra to Touggourt secures waterholes, camel corps outposts, and southern borders.",
        "desc_pt": "A expansão das trilhas e linhas férreas ligeiras de Biskra a Touggourt garante poços de água, fortes de meharistas e as fronteiras sul da Argélia."
    },
    {
        "id": "FRA_recrutement_des_legions_etrangeres",
        "x": 42, "y": 3, "cost": 8,
        "icon": "GFX_FRA_recrutement_des_legions_etrangeres",
        "prereq": ["FRA_protectorat_marocain_lyautey"], "mut": [],
        "reward": """add_ideas = FRA_foreign_legion_cadres
add_manpower = 15000""",
        "title_en": "French Foreign Legion (Sidi Bel Abbès)",
        "title_pt": "Legião Estrangeira Francesa (Sidi Bel Abbès)",
        "desc_en": "From their cradle at Sidi Bel Abbès, the battle-hardened regiments of the Foreign Legion welcome thousands of foreign volunteers rushing to defend Paris.",
        "desc_pt": "De seu berço em Sidi Bel Abbès, os regimentos calejados da Legião Estrangeira acolhem milhares de voluntários estrangeiros que acorrem para defender Paris."
    },
    {
        "id": "FRA_missions_medicales_coloniales_calmette",
        "x": 32, "y": 7, "cost": 8,
        "icon": "GFX_FRA_missions_medicales_coloniales_calmette",
        "prereq": ["FRA_chemins_de_fer_sahariens"], "mut": [],
        "reward": """add_ideas = FRA_pasteur_colonial_hygiene
add_stability = 0.04""",
        "title_en": "Pasteur Institutes & Tropical Hygiene",
        "title_pt": "Institutos Pasteur e Medicina Tropical",
        "desc_en": "Pasteur institutes in Saigon, Tunis, and Dakar eradicate malaria, sleeping sickness, and dysentery, safeguarding both native populations and troops.",
        "desc_pt": "Os institutos Pasteur em Saïgon, Túnis e Dakar combatem a malária, a doença do sono e a desinteria, protegendo populações nativas e soldados."
    },
    {
        "id": "FRA_regiments_de_tirailleurs_marocains",
        "x": 42, "y": 7, "cost": 8,
        "icon": "GFX_FRA_regiments_de_tirailleurs_marocains",
        "prereq": ["FRA_recrutement_des_legions_etrangeres"], "mut": [],
        "reward": """add_ideas = FRA_tirailleurs_marocains_shock
add_manpower = 25000""",
        "title_en": "Moroccan Goumiers & Tirailleurs",
        "title_pt": "Tirailleurs e Goumiers Marroquinos",
        "desc_en": "Organized into swift shock battalions, Moroccan tirailleurs demonstrate unmatched ferocity and mountain navigation in the Argonne and Vosges.",
        "desc_pt": "Organizados em batalhões de choque velozes, os tirailleurs marroquinos demonstram ferocidade e perícia tática na Argonne e nos Vosgos."
    }
]
