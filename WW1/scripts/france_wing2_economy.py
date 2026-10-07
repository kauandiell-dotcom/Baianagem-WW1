# -*- coding: utf-8 -*-
"""France Wing 2: Économie, Belle Époque & Mobilisation Industrielle (35 focuses).
X range: 16 .. 28 | Y range: 0 .. 11
"""

WING2_FOCI = [
    # Y = 0
    {
        "id": "FRA_essor_de_la_belle_epoque",
        "x": 22, "y": 0, "cost": 10,
        "icon": "GFX_FRA_essor_de_la_belle_epoque",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 40
16 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Belle Époque Economic Prosperity",
        "title_pt": "Prosperidade Econômica da Belle Époque",
        "desc_en": "The Parisian stock exchange, flourishing trade, and rapid urban growth embody France's golden era of commercial wealth and cultural prestige.",
        "desc_pt": "A bolsa de valores de Paris, o comércio próspero e o rápido crescimento urbano simbolizam a era de ouro da riqueza comercial e do prestígio cultural da França."
    },

    # Y = 1
    {
        "id": "FRA_bassin_siderurgique_de_briey",
        "x": 19, "y": 1, "cost": 8,
        "icon": "GFX_FRA_bassin_siderurgique_de_briey",
        "prereq": ["FRA_essor_de_la_belle_epoque"], "mut": [],
        "reward": """28 = { add_resource = { type = steel amount = 16 } }
18 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Briey Iron Ore Basin",
        "title_pt": "Bacia de Minério de Ferro de Briey",
        "desc_en": "The minette iron deposits of Briey and Longwy supply 90% of French ore. Modern blast furnaces ensure our metallurgists produce world-class cast iron.",
        "desc_pt": "As jazidas de minério fosforoso de Briey e Longwy fornecem 90% do minério francês. Altos-fornos modernos garantem a produção de ferro fundido de padrão mundial."
    },
    {
        "id": "FRA_fonderies_de_lorraine",
        "x": 20, "y": 1, "cost": 8,
        "icon": "GFX_FRA_fonderies_de_lorraine",
        "prereq": ["FRA_essor_de_la_belle_epoque"], "mut": [],
        "reward": """18 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Lorraine Steel Foundries",
        "title_pt": "Fundições de Aço da Lorena",
        "desc_en": "Constructing state-of-the-art Thomas-Gilchrist converter towers turns phosphoric iron ore into high-tensile structural steel for railways and bridge spans.",
        "desc_pt": "A instalação de conversores Thomas-Gilchrist transforma minério fosforoso em aço estrutural de alta resistência para ferrovias e pontes."
    },
    {
        "id": "FRA_mines_de_charbon_du_nord",
        "x": 25, "y": 1, "cost": 8,
        "icon": "GFX_FRA_mines_de_charbon_du_nord",
        "prereq": ["FRA_essor_de_la_belle_epoque"], "mut": [],
        "reward": """29 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Coal Pits of Nord-Pas-de-Calais",
        "title_pt": "Minas de Carvão de Nord-Pas-de-Calais",
        "desc_en": "From Lens to Valenciennes, hundreds of thousands of miners extract anthracite to power France's locomotives, factories, and domestic hearths.",
        "desc_pt": "De Lens a Valenciennes, centenas de milhares de mineiros extraem antracito para alimentar as locomotivas, usinas e lareiras de toda a França."
    },

    # Y = 2
    {
        "id": "FRA_reseau_ferroviaire_du_nord_et_est",
        "x": 22, "y": 2, "cost": 8,
        "icon": "GFX_FRA_reseau_ferroviaire_du_nord_et_est",
        "prereq": ["FRA_bassin_siderurgique_de_briey", "FRA_mines_de_charbon_du_nord"], "mut": [],
        "reward": """build_railway = { path = { 11500 11437 3838 587 } }
16 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
18 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Nord & Est Railway Trunk Lines",
        "title_pt": "Troncos Ferroviários do Norte e Leste",
        "desc_en": "Upgrading the strategic double-track lines connecting Paris to Reims, Nancy, and Verdun ensures heavy freight and mobilization timetables run flawlessly.",
        "desc_pt": "A duplicação das linhas estratégicas conectando Paris a Reims, Nancy e Verdun assegura o tráfego pesado de cargas e os cronogramas de mobilização militar."
    },
    {
        "id": "FRA_modernisation_du_creusot",
        "x": 17, "y": 2, "cost": 8,
        "icon": "GFX_FRA_modernisation_du_creusot",
        "prereq": ["FRA_bassin_siderurgique_de_briey"], "mut": [],
        "reward": """27 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Le Creusot Heavy Foundry Expansion",
        "title_pt": "Expansão da Fundição Pesada de Le Creusot",
        "desc_en": "Installing massive 100-ton hydraulic steam hammers at Schneider et Cie enables casting mammoth gun barrels and thick armor plate for dreadnoughts.",
        "desc_pt": "A instalação de martelos a vapor hidráulicos de 100 toneladas na Schneider et Cie permite forjar canhões de grande calibre e couraças navais pesadas."
    },
    {
        "id": "FRA_bassin_textile_et_chimique_lille",
        "x": 27, "y": 2, "cost": 8,
        "icon": "GFX_FRA_bassin_textile_et_chimique_lille",
        "prereq": ["FRA_mines_de_charbon_du_nord"], "mut": [],
        "reward": """29 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Lille Textile & Chemical Basin",
        "title_pt": "Polo Têxtil e Químico de Lille",
        "desc_en": "Lille, Roubaix, and Tourcoing form the textile heart of France, spinning wool, linen, and uniforms for both export markets and military stockpiles.",
        "desc_pt": "Lille, Roubaix e Tourcoing formam o coração têxtil da França, tecendo lã, linho e uniformes tanto para os mercados de exportação quanto para o exército."
    },

    # Y = 3
    {
        "id": "FRA_etablissements_schneider_le_creusot",
        "x": 18, "y": 3, "cost": 8,
        "icon": "GFX_FRA_etablissements_schneider_le_creusot",
        "prereq": ["FRA_modernisation_du_creusot"], "mut": [],
        "reward": """add_tech_bonus = { name = art_tech bonus = 1.0 uses = 2 category = artillery }
27 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Schneider-Creusot Ordnance Works",
        "title_pt": "Oficinas de Artilharia Schneider-Creusot",
        "desc_en": "The Schneider family empire produces advanced rapid-fire howitzers, mountain guns, and fortress cupolas rivaling Krupp and Škoda in engineering excellence.",
        "desc_pt": "O império siderúrgico da família Schneider projeta obuses de tiro rápido, canhões de montanha e cúpulas blindadas que rivalizam com a Krupp e a Škoda."
    },
    {
        "id": "FRA_manufacture_d_armes_saint_etienne",
        "x": 22, "y": 3, "cost": 8,
        "icon": "GFX_FRA_manufacture_d_armes_saint_etienne",
        "prereq": ["FRA_reseau_ferroviaire_du_nord_et_est"], "mut": [],
        "reward": """33 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
add_tech_bonus = { name = inf_tech bonus = 1.0 uses = 1 category = infantry_weapons }""",
        "title_en": "Saint-Étienne National Arsenal (MAS)",
        "title_pt": "Arsenal Nacional de Saint-Étienne (MAS)",
        "desc_en": "Manufacture d'Armes de Saint-Étienne mass-produces the standard-issue Lebel M1886 and Berthier rifles, ensuring precision rifling and interchangeability.",
        "desc_pt": "A Manufacture d'Armes de Saint-Étienne produz em massa os fuzis Lebel M1886 e Berthier, garantindo canos raiados de precisão e padronização absoluta."
    },
    {
        "id": "FRA_ateliers_de_puteaux_et_tulle",
        "x": 26, "y": 3, "cost": 8,
        "icon": "GFX_FRA_ateliers_de_puteaux_et_tulle",
        "prereq": ["FRA_bassin_textile_et_chimique_lille"], "mut": [],
        "reward": """16 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
25 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Puteaux & Tulle Precision Arsenals",
        "title_pt": "Arsenais de Precisão de Puteaux e Tulle",
        "desc_en": "Atelier de Construction de Puteaux (APX) specializes in hydro-pneumatic recoil mechanisms for the 75mm gun, while Tulle manufactures machine gun components.",
        "desc_pt": "A oficina de Puteaux (APX) é especializada nos cilindros hidropneumáticos de recuo do canhão de 75mm, enquanto Tulle fabrica peças de metralhadoras."
    },

    # Y = 4
    {
        "id": "FRA_usines_automobiles_renault_panhard",
        "x": 20, "y": 4, "cost": 8,
        "icon": "GFX_FRA_usines_automobiles_renault_panhard",
        "prereq": ["FRA_etablissements_schneider_le_creusot", "FRA_manufacture_d_armes_saint_etienne"], "mut": [],
        "reward": """add_tech_bonus = { name = motorized_bonus bonus = 1.0 uses = 1 category = motorized_equipment }
16 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Renault, Panhard & Peugeot Motor Works",
        "title_pt": "Fábricas Automobilísticas Renault, Panhard e Peugeot",
        "desc_en": "France leads Europe in automobile production. Expanding the Boulogne-Billancourt lines of Louis Renault establishes mass assembly of lorries, ambulances, and taxis.",
        "desc_pt": "A França lidera a produção automobilística europeia. A expansão das fábricas de Louis Renault em Boulogne-Billancourt estabelece linhas de montagem de caminhões e ambulâncias."
    },
    {
        "id": "FRA_chimie_industrielle_saint_fons",
        "x": 24, "y": 4, "cost": 8,
        "icon": "GFX_FRA_chimie_industrielle_saint_fons",
        "prereq": ["FRA_manufacture_d_armes_saint_etienne", "FRA_ateliers_de_puteaux_et_tulle"], "mut": [],
        "reward": """20 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }
add_ideas = FRA_chemical_explosives_industry""",
        "title_en": "Saint-Fons Chemical & Explosives Hub",
        "title_pt": "Polo Químico e de Explosivos de Saint-Fons",
        "desc_en": "The chemical plants of Lyon and Saint-Fons synthesize nitric acid, Poudre B nitrocellulose, and melinite, securing independent production of high-explosive charges.",
        "desc_pt": "As usinas químicas de Lyon e Saint-Fons sintetizam ácido nítrico, pólvora B de nitrocelulose e melinite, assegurando produção autônoma de cargas explosivas."
    },

    # Y = 5
    {
        "id": "FRA_ports_charbonniers_rouen",
        "x": 16, "y": 5, "cost": 8,
        "icon": "GFX_FRA_ports_charbonniers_rouen",
        "prereq": ["FRA_perte_des_mines_du_nord_repli"], "mut": [],
        "reward": """15 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
add_ideas = FRA_rouen_coal_dispatch""",
        "title_en": "Rouen River Coal Transshipment Docks",
        "title_pt": "Diques de Carvão e Transbordo Fluvial de Rouen",
        "desc_en": "Deepening the Seine channel allows British colliers to steam directly into Rouen, offloading fuel onto river barges headed straight to Paris power stations.",
        "desc_pt": "A dragagem do Sena permite que cargueiros britânicos naveguem até Rouen, descarregando carvão em barcaças destinadas às usinas de energia de Paris."
    },
    {
        "id": "FRA_bassin_chimique_marseille",
        "x": 28, "y": 5, "cost": 8,
        "icon": "GFX_FRA_bassin_chimique_marseille",
        "prereq": ["FRA_importations_de_charbon_britannique"], "mut": [],
        "reward": """21 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Marseille Chemical & Oleochemical Plants",
        "title_pt": "Complexo Químico e Oleoquímico de Marselha",
        "desc_en": "Processing colonial peanut and palm oils into glycerin provides the key raw ingredient for nitroglycerin, smokeless cordite, and soap.",
        "desc_pt": "O processamento de óleos vegetais coloniais em glicerina fornece a matéria-prima essencial para nitroglicerina, cordite e sabão."
    },
    {
        "id": "FRA_crise_des_munitions_1914",
        "x": 22, "y": 5, "cost": 6,
        "icon": "GFX_FRA_crise_des_munitions_1914",
        "prereq": ["FRA_usines_automobiles_renault_panhard", "FRA_chimie_industrielle_saint_fons"], "mut": [],
        "reward": """add_ideas = FRA_shell_crisis_1914
custom_effect_tooltip = FRA_shell_crisis_tt""",
        "title_en": "The Great Shell Crisis of 1914",
        "title_pt": "A Crise das Munições de 1914",
        "desc_en": "The peacetime calculation of 13,000 shells a day collapses when battle consumes 50,000 daily. Empty depots threaten our artillery with starvation unless industry mobilizes.",
        "desc_pt": "O cálculo pré-guerra de 13.000 obuses por dia desmorona quando os canhões consomem 50.000 diariamente. Depósitos vazios ameaçam a artilharia com a paralisia total."
    },
    {
        "id": "FRA_perte_des_mines_du_nord_repli",
        "x": 18, "y": 5, "cost": 6,
        "icon": "GFX_FRA_perte_des_mines_du_nord_repli",
        "prereq": ["FRA_etablissements_schneider_le_creusot"], "mut": [],
        "reward": """27 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }
33 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Emergency Evacuation of Heavy Machinery",
        "title_pt": "Evacuação Emergencial de Maquinário Pesado",
        "desc_en": "With German armies invading the Briey basin and Nord departments, machine tools, blueprints, and skilled metalworkers are swiftly evacuated southward to the Loire and Massif Central.",
        "desc_pt": "Com a invasão alemã sobre a bacia de Briey e o departamento de Nord, tornos mecânicos, plantas e operários são evacuados para o Vale do Loire e Maciço Central."
    },
    {
        "id": "FRA_importations_de_charbon_britannique",
        "x": 26, "y": 5, "cost": 6,
        "icon": "GFX_FRA_importations_de_charbon_britannique",
        "prereq": ["FRA_ateliers_de_puteaux_et_tulle"], "mut": [],
        "reward": """add_ideas = FRA_british_coal_imports
14 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "British Coal Sea Convoys",
        "title_pt": "Comboios Marítimos de Carvão Britânico",
        "desc_en": "To replace lost northern coal pits, colliers ship millions of tonnes from Cardiff and Newcastle directly into Rouen, Brest, and Bordeaux under naval escort.",
        "desc_pt": "Para substituir o carvão das minas perdidas no norte, navios mercantes transportam milhões de toneladas de Cardiff e Newcastle diretamente para Rouen, Brest e Bordeaux."
    },

    # Y = 6
    {
        "id": "FRA_ministere_de_l_armement_albert_thomas",
        "x": 22, "y": 6, "cost": 8,
        "icon": "GFX_FRA_ministere_de_l_armement_albert_thomas",
        "prereq": ["FRA_crise_des_munitions_1914"], "mut": [],
        "reward": """swap_ideas = {
    remove_idea = FRA_shell_crisis_1914
    add_idea = FRA_albert_thomas_munitions_boom
}
add_political_power = 40""",
        "title_en": "Albert Thomas' Ministry of Armament",
        "title_pt": "Ministério do Armamento de Albert Thomas",
        "desc_en": "Socialist deputy Albert Thomas organizes national munitions committees, coordinates private industrialists, and standardizes contracts, raising shell output from 10,000 to 200,000 a day.",
        "desc_pt": "O deputado socialista Albert Thomas organiza comitês de produção, padroniza encomendas com industriais privados e eleva a fabricação de obuses de 10.000 para 200.000 diários."
    },

    # Y = 7
    {
        "id": "FRA_les_munitionnettes",
        "x": 19, "y": 7, "cost": 8,
        "icon": "GFX_FRA_les_munitionnettes",
        "prereq": ["FRA_ministere_de_l_armement_albert_thomas"], "mut": [],
        "reward": """add_ideas = FRA_munitionnettes_workforce
16 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
20 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Les Munitionnettes (Women in War Industry)",
        "title_pt": "Les Munitionnettes (Mulheres na Indústria Bélica)",
        "desc_en": "Hundreds of thousands of French women enter lathe workshops and powder mills, machining fuses, assembling artillery shells, and keeping the republic armed.",
        "desc_pt": "Centenas de milhares de mulheres francesas assumem tornos e fábricas de pólvora, usinando espoletas, montando projéteis e mantendo a república armada."
    },
    {
        "id": "FRA_affectes_speciaux_rappel_ouvriers",
        "x": 25, "y": 7, "cost": 8,
        "icon": "GFX_FRA_affectes_speciaux_rappel_ouvriers",
        "prereq": ["FRA_ministere_de_l_armement_albert_thomas"], "mut": [],
        "reward": """add_ideas = FRA_skilled_workforce_recall
add_manpower = -30000
27 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Recall of Skilled Mechanics from the Front",
        "title_pt": "Recolocação de Mecânicos e Operários do Front",
        "desc_en": "Recognizing that precision toolmakers are more valuable turning artillery shells than holding a trench line, half a million skilled soldiers are reassigned as 'affectés spéciaux'.",
        "desc_pt": "Reconhecendo que mestres-torneiros são mais valiosos usinando obuses do que na lama das trincheiras, meio milhão de soldados especializados retornam às fábricas."
    },

    # Y = 8
    {
        "id": "FRA_houille_blanche_des_alpes",
        "x": 17, "y": 8, "cost": 8,
        "icon": "GFX_FRA_houille_blanche_des_alpes",
        "prereq": ["FRA_les_munitionnettes"], "mut": [],
        "reward": """32 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }
735 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Alpine Hydroelectricity (Houille Blanche)",
        "title_pt": "Hidroeletricidade Alpina (Houille Blanche)",
        "desc_en": "Tapping glacial torrents in Grenoble and Savoy generates clean hydroelectric power for aluminum smelters, electrometallurgy, and synthetic calcium carbide.",
        "desc_pt": "O aproveitamento dos torrentes alpinos em Grenoble e Savoie gera energia hidrelétrica abundante para fundições de alumínio, eletrometalurgia e carboneto de cálcio."
    },
    {
        "id": "FRA_usines_de_poudre_saint_fons",
        "x": 23, "y": 8, "cost": 8,
        "icon": "GFX_FRA_usines_de_poudre_saint_fons",
        "prereq": ["FRA_ministere_de_l_armement_albert_thomas"], "mut": [],
        "reward": """20 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
33 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "National Explosives & Powder Mills",
        "title_pt": "Fábricas Nacionais de Pólvora e Explosivos",
        "desc_en": "Expanding the state powder monopolies at Bergerac, Ripault, and Saint-Médard ensures hundreds of tonnes of stable smokeless propellant are bottled daily.",
        "desc_pt": "A expansão das fábricas estatais de pólvora em Bergerac, Ripault e Saint-Médard assegura centenas de toneladas diárias de propelente sem fumaça para a artilharia."
    },
    {
        "id": "FRA_standardisation_des_calibres",
        "x": 27, "y": 8, "cost": 8,
        "icon": "GFX_FRA_standardisation_des_calibres",
        "prereq": ["FRA_affectes_speciaux_rappel_ouvriers"], "mut": [],
        "reward": """add_ideas = FRA_standardised_war_tooling
add_political_power = 30""",
        "title_en": "Standardisation of Ordnance Calibres",
        "title_pt": "Padronização dos Calibres de Guerra",
        "desc_en": "Retiring obsolete 19th-century fortress artillery calibres focuses manufacturing exclusively on 75mm field shells, 155mm howitzers, and 8mm rifle cartridges.",
        "desc_pt": "Aposentar canhões obsoletos do século XIX concentra o maquinário industrial exclusivamente no obus de 75mm, no morteiro de 155mm e na munição de fuzil 8mm."
    },

    # Y = 9
    {
        "id": "FRA_bons_de_la_defense_nationale",
        "x": 22, "y": 9, "cost": 8,
        "icon": "GFX_FRA_bons_de_la_defense_nationale",
        "prereq": ["FRA_houille_blanche_des_alpes", "FRA_usines_de_poudre_saint_fons"], "mut": [],
        "reward": """add_political_power = 60
add_stability = 0.04
add_ideas = FRA_defense_bonds_liquidity""",
        "title_en": "National Defense War Bonds",
        "title_pt": "Títulos da Defesa Nacional",
        "desc_en": "'Pour la France qui vient de loin, souscrivez!' Popular short-term bonds and patriotic posters mobilize household savings into billions of francs for victory.",
        "desc_pt": "'Pela França que vem de longe, subscrevam!' Cartazes patrióticos e títulos do tesouro mobilizam as economias populares em bilhões de francos para a vitória."
    },
    {
        "id": "FRA_or_des_francais_pour_la_patrie",
        "x": 18, "y": 9, "cost": 6,
        "icon": "GFX_FRA_or_des_francais_pour_la_patrie",
        "prereq": ["FRA_houille_blanche_des_alpes"], "mut": [],
        "reward": """add_political_power = 40
add_ideas = FRA_bank_of_france_gold_bullion""",
        "title_en": "Gold for the Fatherland Campaign",
        "title_pt": "O Ouro dos Franceses pela Pátria",
        "desc_en": "Citizens willingly exchange their gold Napoléon coins at bank counters for paper banknotes, stocking Banque de France vaults with immense reserves to back foreign loans.",
        "desc_pt": "Cidadãos trocam suas moedas de ouro de Napoleão por notas de banco nos caixas públicos, abastecendo os cofres do Banco da França para respaldar empréstimos no exterior."
    },
    {
        "id": "FRA_credits_financiers_anglo_americains",
        "x": 26, "y": 9, "cost": 8,
        "icon": "GFX_FRA_credits_financiers_anglo_americains",
        "prereq": ["FRA_standardisation_des_calibres"], "mut": [],
        "reward": """add_political_power = 50
16 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "Anglo-American Financial Credits",
        "title_pt": "Créditos Financeiros Anglo-Americanos",
        "desc_en": "Coordinating with the British Treasury and J.P. Morgan & Co. in New York secures vital foreign exchange to buy American copper, cotton, and grain without currency collapse.",
        "desc_pt": "A coordenação com o Tesouro britânico e o banco J.P. Morgan em Nova York assegura divisas vitais para importar cobre, algodão e trigo sem colapso cambial."
    },

    # Y = 10
    {
        "id": "FRA_rationnement_et_ravitaillement",
        "x": 20, "y": 10, "cost": 6,
        "icon": "GFX_FRA_rationnement_et_ravitaillement",
        "prereq": ["FRA_bons_de_la_defense_nationale"], "mut": [],
        "reward": """add_stability = 0.05
add_ideas = FRA_ww1_rationing""",
        "title_en": "Bread, Sugar & Coal Rationing",
        "title_pt": "Racionamento de Pão, Açúcar e Carvão",
        "desc_en": "Introducing ration cards and maximum prices prevents price-gouging, guarantees fair distribution among city workers, and ensures coal reaches frontline kitchens.",
        "desc_pt": "Cartões de racionamento e tabelamento de preços evitam a especulação, garantem distribuição justa nas cidades e mantêm o fornecimento de carvão aos fogões do exército."
    },
    {
        "id": "FRA_conversion_des_ateliers_civils",
        "x": 24, "y": 10, "cost": 8,
        "icon": "GFX_FRA_conversion_des_ateliers_civils",
        "prereq": ["FRA_bons_de_la_defense_nationale"], "mut": [],
        "reward": """24 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
30 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Civilian Workshop Conversion",
        "title_pt": "Conversão de Oficinas Civis",
        "desc_en": "Bicycle manufacturers assemble rifle bolts, clockmakers turn artillery timers, and perfume distilleries produce ether for smokeless powder.",
        "desc_pt": "Fábricas de bicicletas montam ferrolhos de fuzis, relojoeiros produzem espoletas de tempo e destilarias de perfume fabricam éter para pólvoras sem fumaça."
    },

    # Y = 11
    {
        "id": "FRA_puissance_industrielle_de_1918",
        "x": 22, "y": 11, "cost": 10,
        "icon": "GFX_FRA_puissance_industrielle_de_1918",
        "prereq": ["FRA_rationnement_et_ravitaillement", "FRA_conversion_des_ateliers_civils"], "mut": [],
        "reward": """add_ideas = FRA_supreme_industrial_mobilisation
add_political_power = 60
add_stability = 0.05
16 = { add_extra_state_shared_building_slots = 2 }""",
        "title_en": "Industrial Titan of 1918",
        "title_pt": "Titã Industrial de 1918",
        "desc_en": "By 1918, France has become the arsenal of the Entente, supplying not only her own armies but equipping American and allied divisions with artillery, aircraft, and tanks.",
        "desc_pt": "Em 1918, a França transformou-se no arsenal da Entente, abastecendo seus próprios exércitos e equipando as divisões americanas com artilharia, aviões e tanques."
    },
    {
        "id": "FRA_reconstitution_des_territoires_liberes",
        "x": 18, "y": 11, "cost": 8,
        "icon": "GFX_FRA_reconstitution_des_territoires_liberes",
        "prereq": ["FRA_or_des_francais_pour_la_patrie"], "mut": [],
        "reward": """18 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
29 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
add_political_power = 30""",
        "title_en": "Reconstruction of Liberated Basins",
        "title_pt": "Reconstrução das Regiões Libertadas",
        "desc_en": "Planning the clearing of minefields, restoration of flooded coal pits in Lens, and rebuilding destroyed canal locks prepares France for postwar renewal.",
        "desc_pt": "O planejamento para drenagem das minas inundadas de Lens, desminagem dos campos e reconstrução das eclusas prepara a França para o renascimento pós-guerra."
    },
    {
        "id": "FRA_credit_national_de_reconstruction",
        "x": 26, "y": 11, "cost": 8,
        "icon": "GFX_FRA_credit_national_de_reconstruction",
        "prereq": ["FRA_credits_financiers_anglo_americains"], "mut": [],
        "reward": """add_ideas = FRA_national_credit_solvency
add_political_power = 50""",
        "title_en": "National Reconstruction Credit Bank",
        "title_pt": "Banco do Crédito Nacional de Reconstrução",
        "desc_en": "Establishing a specialized public financial institution channels indemnities and state capital directly into rebuilding industrial factories and homes in the devastated north.",
        "desc_pt": "A criação de uma instituição pública especializada canaliza indenizações e capital estatal diretamente para reconstruir usinas e lares no norte devastado."
    },
    {
        "id": "FRA_modernisation_du_port_du_havre",
        "x": 16, "y": 4, "cost": 8,
        "icon": "GFX_FRA_modernisation_du_port_du_havre",
        "prereq": ["FRA_reseau_ferroviaire_du_nord_et_est"], "mut": [],
        "reward": """15 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Expansion of Le Havre & Rouen Docks",
        "title_pt": "Expansão dos Portos de Le Havre e Rouen",
        "desc_en": "Installing deep-water steam cranes and expanding rail connections on the Seine estuary allows unloading hundreds of thousands of tonnes of transatlantic freight weekly.",
        "desc_pt": "Guindastes a vapor e conexões ferroviárias diretas no estuário do Sena permitem desembarcar centenas de milhares de toneladas de suprimentos transatlânticos semanalmente."
    },
    {
        "id": "FRA_electrification_du_midi",
        "x": 28, "y": 4, "cost": 8,
        "icon": "GFX_FRA_electrification_du_midi",
        "prereq": ["FRA_reseau_ferroviaire_du_nord_et_est"], "mut": [],
        "reward": """21 = { add_extra_state_shared_building_slots = 1 }
22 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Electrification of Midi & Pyrenees Railways",
        "title_pt": "Eletrificação das Ferrovias do Midi e Pireneus",
        "desc_en": "Harnessing Pyrenean water turbines powers electric locomotives on the Midi network, saving precious coal and boosting transit between Toulouse and the coast.",
        "desc_pt": "Turbinas hídricas nos Pireneus alimentam locomotivas elétricas na malha do Midi, poupando carvão precioso e acelerando o transporte entre Toulouse e a costa."
    },
    {
        "id": "FRA_chantiers_navals_saint_nazaire",
        "x": 16, "y": 7, "cost": 8,
        "icon": "GFX_FRA_chantiers_navals_saint_nazaire",
        "prereq": ["FRA_modernisation_du_port_du_havre"], "mut": [],
        "reward": """30 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = dockyard level = 1 instant_build = yes } }""",
        "title_en": "Saint-Nazaire Chantiers de l'Atlantique",
        "title_pt": "Estaleiros do Atlântico em Saint-Nazaire",
        "desc_en": "The sprawling shipyards of Saint-Nazaire and Nantes construct large merchant hulls, troopships, and boiler machinery to defy German commerce raiders.",
        "desc_pt": "Os estaleiros de Saint-Nazaire e Nantes constroem cargueiros mercantes, transportes de tropas e turbinas para enfrentar a guerra submarina alemã."
    },
    {
        "id": "FRA_siderurgie_electrique_ugine",
        "x": 28, "y": 7, "cost": 8,
        "icon": "GFX_FRA_siderurgie_electrique_ugine",
        "prereq": ["FRA_electrification_du_midi"], "mut": [],
        "reward": """735 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }
add_tech_bonus = { name = industry_bonus bonus = 1.0 uses = 1 category = industry }""",
        "title_en": "Ugine Special Steels & Alloys",
        "title_pt": "Aços Especiais e Ligas de Ugine",
        "desc_en": "Paul Girod's electric arc furnaces produce high-grade chrome, nickel, and tungsten alloys essential for armor-piercing artillery projectiles and aircraft engines.",
        "desc_pt": "Fornos elétricos a arco de Paul Girod fundem ligas de cromo, níquel e tungstênio essenciais para obuses perfurantes e motores de aviação."
    }
]
