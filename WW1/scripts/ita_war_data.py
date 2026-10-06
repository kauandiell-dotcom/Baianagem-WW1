"""Campaigns, Libyan Settlement, and Postwar (war) Wing Data for Italy WW1 Tree.
Contains 25 focuses with historical depth, balance compliance, and bilingual loc.
"""

WAR_FOCI = {
    "libyan_question": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_irredentism = 5 } add_political_power = 25",
        "desc_en": "Revisiting Italy's claims over Tripolitania and Cyrenaica under international agreements. Immediate effect: Raises Irredentism by 5 and grants 25 Political Power.",
        "desc_pt": "Exame das reivindicações italianas sobre a Tripolitânia e a Cirenaica sob acordos internacionais. Efeito imediato: Eleva o Irredentismo em 5 e concede 25 de Poder Político."
    },
    "ultimatum_to_the_porte": {
        "cost": 5,
        "available": "date > 1911.9.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.51 days = 1 } add_political_power = 30",
        "desc_en": "Delivering diplomatic terms to the Sublime Porte demanding the transfer of administrative control over Libya. Immediate effect: Triggers the Ottoman Diplomatic Offer event and grants 30 Political Power.",
        "desc_pt": "Entrega de termos diplomáticos à Sublime Porta exigindo a transferência do controle administrativo da Líbia. Efeito imediato: Dispara o evento de Termos Diplomáticos com os Otomanos e concede 30 de Poder Político."
    },
    "tripoli_landing": {
        "cost": 5,
        "available": "",
        "ai": "factor = 15",
        "effect": "navy_experience = 10 army_experience = 10",
        "desc_en": "Deploying naval detachments and marines to secure port facilities along the Libyan coastline. Immediate effect: Grants 10 Navy Experience and 10 Army Experience.",
        "desc_pt": "Desdobramento de destacamentos navais e fuzileiros para assegurar instalações portuárias líbias. Efeito imediato: Concede 10 de Experiência Naval e 10 de Experiência do Exército."
    },
    "first_aerial_bombing": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "air_experience = 15 add_tech_bonus = { name = ITA_ww1_early_air_recon bonus = 0.25 uses = 1 category = air_doctrine }",
        "desc_en": "Lieutenant Giulio Gavotti conducts the world's first aerial bombardment dropping Cipelli grenades near Ain Zara. Immediate effect: Grants 15 Air Experience and a 25% Air Doctrine research bonus (1 use).",
        "desc_pt": "O Tenente Giulio Gavotti realiza o primeiro bombardeio aéreo da história militar em Ain Zara. Efeito imediato: Concede 15 de Experiência Aérea e 25% de bônus em Doutrina Aérea (1 uso)."
    },
    "inland_oases_campaign": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "army_experience = 15 add_political_power = 20",
        "desc_en": "Securing key desert caravan junctions, fortified wells, and interior oases across Tripolitania. Immediate effect: Grants 15 Army Experience and 20 Political Power.",
        "desc_pt": "Ocupação de encruzilhadas de caravanas, poços fortificados e oásis do interior líbio. Efeito imediato: Concede 15 de Experiência do Exército e 20 de Poder Político."
    },
    "dodecanese_occupation": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "navy_experience = 15 add_to_variable = { ita_ww1_irredentism = 5 }",
        "desc_en": "Naval operations occupy Rhodes and the Aegean Dodecanese archipelago as a strategic pledge. Immediate effect: Grants 15 Navy Experience and raises Irredentism by 5.",
        "desc_pt": "Operações navais ocupam Rodes e as ilhas do Dodecaneso no Mar Egeu como penhor estratégico. Efeito imediato: Concede 15 de Experiência Naval e eleva o Irredentismo em 5."
    },
    "treaty_of_ouchy": {
        "cost": 5,
        "available": "date > 1912.10.1",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.52 days = 1 } add_political_power = 30",
        "desc_en": "Signing the Treaty of Ouchy (First Treaty of Lausanne) confirming Italian sovereignty over Libya. Immediate effect: Triggers the Treaty of Ouchy ratification event and grants 30 Political Power.",
        "desc_pt": "Assinatura do Tratado de Ouchy confirmando a soberania da Itália sobre a Líbia. Efeito imediato: Dispara o evento de Ratificação do Tratado de Ouchy e concede 30 de Poder Político."
    },
    "cyrenaica_pacification": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_libya_acquired",
        "ai": "factor = 10",
        "effect": "army_experience = 10 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Reaching administrative accords with local tribal sheikhs and Senussi leaders in Cyrenaica. Immediate effect: Grants 10 Army Experience and lowers Social Tension by 5.",
        "desc_pt": "Acordos administrativos com chefes tribais e líderes da ordem Senussi na Cirenaica. Efeito imediato: Concede 10 de Experiência do Exército e reduz a Tensão Social em 5."
    },
    "isonzo_offensives": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 20",
        "effect": "army_experience = 20 add_to_variable = { ita_ww1_army_morale = 5 }",
        "desc_en": "Launching successive massed assaults against Austro-Hungarian positions along the Isonzo river. Immediate effect: Grants 20 Army Experience and raises Army Morale by 5.",
        "desc_pt": "Lançamento de ofensivas em massa contra as posições austro-húngaras no rio Isonzo. Efeito imediato: Concede 20 de Experiência do Exército e eleva a Moral do Exército em 5."
    },
    "french_alpine_front": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 1",
        "effect": "army_experience = 20 add_to_variable = { ita_ww1_army_morale = 5 }",
        "desc_en": "Coordinating assault columns to pierce the French fortifications in the Maritime Alps. Immediate effect: Grants 20 Army Experience and raises Army Morale by 5.",
        "desc_pt": "Coordenação de colunas de ataque para romper as fortificações francesas nos Alpes Marítimos. Efeito imediato: Concede 20 de Experiência do Exército e eleva a Moral do Exército em 5."
    },
    "riviera_offensive": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "army_experience = 15 add_to_variable = { ita_ww1_irredentism = 10 }",
        "desc_en": "Pushing mechanized and cavalry spearheads along the Mediterranean coast toward Nice and Cannes. Immediate effect: Grants 15 Army Experience and raises Irredentism by 10.",
        "desc_pt": "Avanço de pontas de lança de cavalaria e infantaria pelo litoral mediterrâneo rumo a Nice. Efeito imediato: Concede 15 de Experiência do Exército e eleva o Irredentismo em 10."
    },
    "tunisian_landing": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "navy_experience = 15 army_experience = 15",
        "desc_en": "Executing amphibious landings along the Tunisian coast to liberate Italian settlers in Tunis. Immediate effect: Grants 15 Navy Experience and 15 Army Experience.",
        "desc_pt": "Operações anfíbias no litoral tunisiano em apoio à expressiva população italiana local. Efeito imediato: Concede 15 de Experiência Naval e 15 de Experiência do Exército."
    },
    "trentino_defence": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 15",
        "effect": "army_experience = 15 add_to_variable = { ita_ww1_army_morale = 5 }",
        "desc_en": "Halting the Austrian Strafexpedition in the high plateau of Asiago and Pasubio. Immediate effect: Grants 15 Army Experience and raises Army Morale by 5.",
        "desc_pt": "Contenção da Strafexpedition austríaca no planalto de Asiago e Pasubio. Efeito imediato: Concede 15 de Experiência do Exército e eleva a Moral do Exército em 5."
    },
    "gorizia": {
        "cost": 5,
        "available": "date > 1916.8.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.54 days = 1 } army_experience = 15",
        "desc_en": "Capturing the city of Gorizia and storming the fortified heights of Monte Sabotino and Podgora. Immediate effect: Triggers the Capture of Gorizia event and grants 15 Army Experience.",
        "desc_pt": "Tomada da cidade de Gorízia e assalto às alturas fortificadas de Monte Sabotino e Podgora. Efeito imediato: Dispara o evento da Conquista de Gorízia e concede 15 de Experiência do Exército."
    },
    "bainsizza": {
        "cost": 5,
        "available": "date > 1917.8.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.55 days = 1 } army_experience = 15",
        "desc_en": "The heroic crossing of the Isonzo and conquest of the vast Austrian plateau of Bainsizza. Immediate effect: Triggers the Bainsizza Plateau event and grants 15 Army Experience.",
        "desc_pt": "Travessia heroica do Isonzo e conquista do vasto planalto austríaco de Bainsizza. Efeito imediato: Dispara o evento do Planalto de Bainsizza e concede 15 de Experiência do Exército."
    },
    "caporetto": {
        "cost": 5,
        "available": "date > 1917.10.1",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.56 days = 1 } add_political_power = -20",
        "desc_en": "Weathering the catastrophic breakthrough of German infiltration divisions at Caporetto. Immediate effect: Triggers the Caporetto Crisis event and costs 20 Political Power.",
        "desc_pt": "Resistência ao rompimento catastrófico das divisões de assalto alemãs em Caporetto. Efeito imediato: Dispara o evento da Crise de Caporetto e custa 20 de Poder Político."
    },
    "piave_line": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_caporetto_shock",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.57 days = 1 } add_to_variable = { ita_ww1_army_morale = 15 }",
        "desc_en": "Rallying the shattered armies on the river Piave and Monte Grappa: 'Tutti eroi! O il Piave o tutti accoppati!'. Immediate effect: Triggers the Piave Line Stand event and raises Army Morale by 15.",
        "desc_pt": "Reagrupamento dos exércitos no rio Piave e no Monte Grappa com determinação inabalável. Efeito imediato: Dispara o evento da Linha do Piave e eleva a Moral do Exército em 15."
    },
    "solstice_battle": {
        "cost": 5,
        "available": "date > 1918.6.1",
        "ai": "factor = 20",
        "effect": "add_war_support = 0.03 country_event = { id = ww1_italy.59 days = 1 }",
        "desc_en": "Repulsing the final massive Austro-Hungarian offensive across Montello and the lower Piave. Immediate effect: Grants +3% War Support and triggers the Battle of the Solstice event.",
        "desc_pt": "Rechaço da última grande ofensiva austro-húngara no Montello e no baixo Piave. Efeito imediato: Concede +3% de Apoio à Guerra e dispara o evento da Batalha do Solstício."
    },
    "vittorio_veneto": {
        "cost": 5,
        "available": "date > 1918.10.1",
        "ai": "factor = 25",
        "effect": "add_war_support = 0.03 country_event = { id = ww1_italy.60 days = 1 }",
        "desc_en": "The decisive general offensive shattering the Austro-Hungarian lines and liberating Trento and Trieste. Immediate effect: Grants +3% War Support and triggers the Victory of Vittorio Veneto event.",
        "desc_pt": "A ofensiva geral decisiva que rompe as linhas austríacas e liberta Trento e Trieste. Efeito imediato: Concede +3% de Apoio à Guerra e dispara a vitória de Vittorio Veneto."
    },
    "villa_giusti_armistice": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_vittorio_veneto_won",
        "ai": "factor = 25",
        "effect": "add_stability = 0.03 country_event = { id = ww1_italy.61 days = 1 }",
        "desc_en": "Signing the armistice with defeated Austria-Hungary at Villa Giusti outside Padua on November 3, 1918. Immediate effect: Grants +3% Stability and triggers the Villa Giusti Armistice event.",
        "desc_pt": "Assinatura do armistício com a Áustria-Hungria derrotada na Villa Giusti em 3 de novembro de 1918. Efeito imediato: Concede +3% de Estabilidade e dispara o armistício de Villa Giusti."
    },
    "trento_trieste_integration": {
        "cost": 5,
        "available": "",
        "ai": "factor = 20",
        "effect": "add_stability = 0.03 add_to_variable = { ita_ww1_irredentism = -15 }",
        "desc_en": "Full administrative, judicial, and linguistic integration of the redeemed provinces into the Kingdom of Italy. Immediate effect: Grants +3% Stability and satisfies Irredentism by 15.",
        "desc_pt": "Integração administrativa, jurídica e linguística plena das províncias redimidas ao Reino da Itália. Efeito imediato: Concede +3% de Estabilidade e reduz a pressão do Irredentismo em 15."
    },
    "fiume_regency": {
        "cost": 5,
        "available": "date > 1919.9.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.62 days = 1 } add_political_power = 25",
        "desc_en": "Gabriele D'Annunzio leads mutinous legionaries into Fiume, defying the Allied supreme council. Immediate effect: Triggers the Fiume Occupation event and grants 25 Political Power.",
        "desc_pt": "Gabriele D'Annunzio lidera legionários amotinados para ocupar Fiume em desafio aos Aliados. Efeito imediato: Dispara o evento da Ocupação de Fiume e concede 25 de Poder Político."
    },
    "christmas_of_blood": {
        "cost": 5,
        "available": "date > 1920.12.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.64 days = 1 } add_political_power = 30",
        "desc_en": "The Italian navy bombards D'Annunzio's palace in Fiume, restoring legal compliance with the Treaty of Rapallo. Immediate effect: Triggers the Natale di Sangue event and grants 30 Political Power.",
        "desc_pt": "A marinha italiana bombardeia o palácio de D'Annunzio em Fiume, impondo o Tratado de Rapallo. Efeito imediato: Dispara o evento do Natal de Sangue e concede 30 de Poder Político."
    },
    "unknown_soldier": {
        "cost": 5,
        "available": "date > 1921.11.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.65 days = 1 } add_political_power = 35",
        "desc_en": "Solemn entombment of the Unknown Soldier at the Altare della Patria in Rome unites the nation in reverence. Immediate effect: Triggers the Unknown Soldier event and grants 35 Political Power.",
        "desc_pt": "Entombamento solene do Soldado Desconhecido no Altar da Pátria em Roma une a nação em reverência. Efeito imediato: Dispara o evento do Soldado Desconhecido e concede 35 de Poder Político."
    },
    "libyan_reconquest": {
        "cost": 5,
        "available": "date > 1922.1.1",
        "ai": "factor = 10",
        "effect": "army_experience = 15 add_to_variable = { ita_ww1_irredentism = 5 }",
        "desc_en": "Reasserting military dominance over interior desert tribes to consolidate the Fourth Shore. Immediate effect: Grants 15 Army Experience and raises Irredentism by 5.",
        "desc_pt": "Reafirmação do domínio militar sobre o interior desértico consolidando a Quarta Margem. Efeito imediato: Concede 15 de Experiência do Exército e eleva o Irredentismo em 5."
    }
}
