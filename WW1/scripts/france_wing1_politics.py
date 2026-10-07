# -*- coding: utf-8 -*-
"""France Wing 1: Politique, République & Union Sacrée (35 focuses).
X range: 0 .. 12 | Y range: 0 .. 11
"""

WING1_FOCI = [
    # Y = 0
    {
        "id": "FRA_preserver_la_republique",
        "x": 6, "y": 0, "cost": 10,
        "icon": "GFX_FRA_preserver_la_republique",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 60
add_stability = 0.04
add_ideas = FRA_republican_vigilance""",
        "title_en": "Preserve the Third Republic",
        "title_pt": "Preservar a Terceira República",
        "desc_en": "Born from the ashes of Sedan in 1870, the Third Republic stands as the beacon of liberty, secular democracy, and citizen equality. Despite parliamentary turbulence, the republican regime remains our sacred sanctuary.",
        "desc_pt": "Nascida das cinzas de Sedan em 1870, a Terceira República ergue-se como o baluarte da liberdade, da democracia secular e da igualdade cívica. Apesar das turbulências parlamentares, o regime republicano permanece nosso santuário sagrado."
    },

    # Y = 1
    {
        "id": "FRA_senat_et_chambre_des_deputes",
        "x": 4, "y": 1, "cost": 8,
        "icon": "GFX_FRA_senat_et_chambre_des_deputes",
        "prereq": ["FRA_preserver_la_republique"], "mut": [],
        "reward": """add_political_power = 40
add_ideas = FRA_parliamentary_equilibrium""",
        "title_en": "Senate & Chamber of Deputies",
        "title_pt": "Senado e Câmara dos Deputados",
        "desc_en": "Balancing the conservative wisdom of the Senate with the lively democratic passions of the Palais Bourbon ensures legislative equilibrium and protects the Republic against any autocrat or military adventurer.",
        "desc_pt": "Equilibrar a sabedoria conservadora do Senado com as vívidas paixões democráticas do Palais Bourbon assegura o equilíbrio legislativo e protege a República contra autocratas ou aventureiros militares."
    },
    {
        "id": "FRA_laicite_republicaine",
        "x": 8, "y": 1, "cost": 8,
        "icon": "GFX_FRA_laicite_republicaine",
        "prereq": ["FRA_preserver_la_republique"], "mut": [],
        "reward": """add_stability = 0.03
add_political_power = 30
swap_ideas = {
    remove_idea = FRA_third_republic_instability
    add_idea = FRA_secular_civic_order
}""",
        "title_en": "Republican Secularism (Laïcité)",
        "title_pt": "Secularismo Republicano (Laicidade)",
        "desc_en": "The 1905 law separating Church and State consolidated the secular school system. The children of France are educated as free citizens of the Republic, immune to clerical reaction.",
        "desc_pt": "A lei de 1905 que separa Igreja e Estado consolidou a escola pública laica. Os filhos da França são educados como cidadãos livres da República, imunes à reação clerical."
    },

    # Y = 2
    {
        "id": "FRA_le_parti_radical",
        "x": 2, "y": 2, "cost": 8,
        "icon": "GFX_FRA_le_parti_radical",
        "prereq": ["FRA_senat_et_chambre_des_deputes"], "mut": [],
        "reward": """add_political_power = 50
add_popularity = { ideology = democratic popularity = 0.10 }""",
        "title_en": "The Radical-Socialist Party",
        "title_pt": "O Partido Radical-Socialista",
        "desc_en": "Neither reactionary nor collectivist, the Radical Party of Joseph Caillaux defends small property owners, secular schooling, and civic freedom as the true center of gravity of French politics.",
        "desc_pt": "Nem reacionário nem coletivista, o Partido Radical de Joseph Caillaux defende os pequenos proprietários, a escola laica e as liberdades cívicas como o verdadeiro centro de gravidade da política francesa."
    },
    {
        "id": "FRA_alliance_democratique",
        "x": 6, "y": 2, "cost": 8,
        "icon": "GFX_FRA_alliance_democratique",
        "prereq": ["FRA_senat_et_chambre_des_deputes", "FRA_laicite_republicaine"], "mut": [],
        "reward": """add_political_power = 50
add_ideas = FRA_poincare_national_firmness""",
        "title_en": "Democratic Alliance Center-Right",
        "title_pt": "Aliança Democrática de Centro-Direita",
        "desc_en": "Raymond Poincaré and the moderates provide financial orthodoxy, national patriotism, and administrative competence, counterbalancing socialist radicalism with bourgeois respectability.",
        "desc_pt": "Raymond Poincaré e os moderados oferecem ortodoxia financeira, patriotismo resoluto e competência administrativa, contrabalançando o radicalismo socialista com a respeitabilidade burguesa."
    },
    {
        "id": "FRA_essor_de_la_sfio",
        "x": 10, "y": 2, "cost": 8,
        "icon": "GFX_FRA_essor_de_la_sfio",
        "prereq": ["FRA_laicite_republicaine"], "mut": [],
        "reward": """add_political_power = 40
add_stability = 0.03
add_ideas = FRA_socialist_labor_peace""",
        "title_en": "Rise of the SFIO Socialists",
        "title_pt": "Ascensão da SFIO Socialista",
        "desc_en": "Led by the eloquent Jean Jaurès, the Section Française de l'Internationale Ouvrière champions working-class rights, universal pensions, and international peace, rallying workers to constitutional socialism.",
        "desc_pt": "Liderada pelo eloquente Jean Jaurès, a Seção Francesa da Internacional Operária luta pelos direitos dos trabalhadores, previdência e paz internacional, atraindo os operários para o socialismo constitucional."
    },

    # Y = 3
    {
        "id": "FRA_pacifisme_de_jean_jaures",
        "x": 10, "y": 3, "cost": 6,
        "icon": "GFX_FRA_pacifisme_de_jean_jaures",
        "prereq": ["FRA_essor_de_la_sfio"], "mut": [],
        "reward": """add_political_power = 30
add_stability = 0.04
add_war_support = -0.05
country_event = { id = ww1_france.40 days = 2 }""",
        "title_en": "Jean Jaurès' Crusade for Peace",
        "title_pt": "A Cruzada de Paz de Jean Jaurès",
        "desc_en": "Through impassioned oratory and the pages of L'Humanité, Jaurès warns of the impending slaughter of European youth, urging solidarity among French and German workers to avert the catastrophe.",
        "desc_pt": "Com oratória apaixonada e através das páginas do L'Humanité, Jaurès alerta para o massacre iminente da juventude europeia, conclamando a solidariedade entre operários franceses e alemães para evitar a catástrofe."
    },
    {
        "id": "FRA_election_presidentielle_1913",
        "x": 6, "y": 3, "cost": 8,
        "icon": "GFX_FRA_election_presidentielle_1913",
        "prereq": ["FRA_alliance_democratique"], "mut": [],
        "reward": """country_event = { id = ww1_france.20 days = 1 }""",
        "title_en": "Presidential Election of 1913",
        "title_pt": "Eleição Presidencial de 1913",
        "desc_en": "Meeting at the Palace of Versailles, the National Assembly must choose the successor to President Armand Fallières. The contest between Raymond Poincaré and Jules Pams will define French foreign resolve.",
        "desc_pt": "Reunida no Palácio de Versalhes, a Assembleia Nacional deve eleger o sucessor do presidente Armand Fallières. A disputa entre Raymond Poincaré e Jules Pams definirá a firmeza externa da França."
    },
    {
        "id": "FRA_loi_des_retraites_ouvrieres",
        "x": 2, "y": 3, "cost": 8,
        "icon": "GFX_FRA_loi_des_retraites_ouvrieres",
        "prereq": ["FRA_le_parti_radical"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = -25
16 = { add_extra_state_shared_building_slots = 1 }""",
        "title_en": "Workers' Pensions Law",
        "title_pt": "Lei de Previdência Operária",
        "desc_en": "Implementing modest state retirement pensions for industrial and agricultural workers pacifies labor unrest and deepens peasant loyalty to the republic.",
        "desc_pt": "A implementação de aposentadorias públicas para trabalhadores industriais e rurais pacifica as agitações sindicais e consolida a lealdade dos camponeses à república."
    },

    # Y = 4
    {
        "id": "FRA_suffrage_et_citoyennete",
        "x": 2, "y": 4, "cost": 8,
        "icon": "GFX_FRA_suffrage_et_citoyennete",
        "prereq": ["FRA_loi_des_retraites_ouvrieres"], "mut": [],
        "reward": """add_political_power = 40
add_stability = 0.04""",
        "title_en": "Universal Suffrage & Civic Equality",
        "title_pt": "Sufrágio Universal e Cidadania Cívica",
        "desc_en": "Consolidating direct universal male suffrage and defending local municipal councils deepens grassroots loyalty to the Third Republic across rural communes.",
        "desc_pt": "A consolidação do sufrágio universal masculino direto e a valorização das prefeituras fortalecem a lealdade republicana nas comunas rurais."
    },
    {
        "id": "FRA_presidence_poincare",
        "x": 4, "y": 4, "cost": 8,
        "icon": "GFX_FRA_presidence_poincare",
        "prereq": ["FRA_election_presidentielle_1913"], "mut": ["FRA_presidence_pams"],
        "reward": """add_political_power = 60
add_war_support = 0.08
add_ideas = FRA_poincare_presidency""",
        "title_en": "Poincaré's Patriotic Presidency",
        "title_pt": "Presidência Patriótica de Poincaré",
        "desc_en": "A son of Lorraine who witnessed German victory in 1870, Raymond Poincaré brings dignified firmness to the Élysée, determined that France shall never bow to foreign ultimatums.",
        "desc_pt": "Filho da Lorena que testemunhou a vitória alemã em 1870, Raymond Poincaré traz digna firmeza ao Palácio do Eliseu, determinado a não permitir que a França se curve a ultimatos externos."
    },
    {
        "id": "FRA_presidence_pams",
        "x": 8, "y": 4, "cost": 8,
        "icon": "GFX_FRA_presidence_pams",
        "prereq": ["FRA_election_presidentielle_1913"], "mut": ["FRA_presidence_poincare"],
        "reward": """add_political_power = 40
add_stability = 0.08
add_ideas = FRA_pams_conciliatory_presidency""",
        "title_en": "Jules Pams Conciliatory Presidency",
        "title_pt": "Presidência Conciliadora de Jules Pams",
        "desc_en": "Supported by Clemenceau and the left radicals, Jules Pams emphasizes domestic welfare reforms, reduction of diplomatic friction, and constitutional harmony over revanchist militarism.",
        "desc_pt": "Apoiado por Clemenceau e pelos radicais de esquerda, Jules Pams prioriza reformas sociais internas, redução de tensões diplomáticas e harmonia constitucional contra o militarismo revanchista."
    },

    # Y = 5
    {
        "id": "FRA_le_scandale_calmette_caillaux",
        "x": 4, "y": 5, "cost": 6,
        "icon": "GFX_FRA_le_scandale_calmette_caillaux",
        "prereq": ["FRA_presidence_poincare"], "mut": [],
        "reward": """add_political_power = -20
add_stability = -0.02
country_event = { id = ww1_france.30 days = 1 }""",
        "title_en": "The Calmette-Caillaux Affair",
        "title_pt": "O Caso Calmette-Caillaux",
        "desc_en": "In March 1914, Henriette Caillaux shot Gaston Calmette, editor of Le Figaro, after he threatened to publish private letters. The sensational trial transfixes the nation on the eve of the European crisis.",
        "desc_pt": "Em março de 1914, Henriette Caillaux atirou em Gaston Calmette, editor do Le Figaro, após ameaças de publicação de cartas íntimas. O sensacional julgamento paralisa a nação às vésperas da crise europeia."
    },
    {
        "id": "FRA_apaiser_les_tensions_sociales",
        "x": 8, "y": 5, "cost": 6,
        "icon": "GFX_FRA_apaiser_les_tensions_sociales",
        "prereq": ["FRA_presidence_pams"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = 25""",
        "title_en": "Appease Social Unrest",
        "title_pt": "Apaziguar Tensões Sociais",
        "desc_en": "By opening channels with trade unions and moderating labor policing, the government prevents general strikes and maintains social calm across industrial basins.",
        "desc_pt": "Ao abrir canais de diálogo com os sindicatos e moderar a repressão policial, o governo evita greves gerais e garante estabilidade social nas bacias operárias."
    },
    {
        "id": "FRA_reforme_fiscale_impot_revenu",
        "x": 6, "y": 5, "cost": 8,
        "icon": "GFX_FRA_reforme_fiscale_impot_revenu",
        "prereq": ["FRA_presidence_poincare", "FRA_presidence_pams"], "mut": [],
        "reward": """add_political_power = 30
add_ideas = FRA_1914_fiscal_solvency
16 = { add_extra_state_shared_building_slots = 1 }
20 = { add_extra_state_shared_building_slots = 1 }""",
        "title_en": "The 1914 Income Tax Reform",
        "title_pt": "Reforma do Imposto de Renda de 1914",
        "desc_en": "After bitter parliamentary battles, Joseph Caillaux's progressive income tax bill passes into law, granting the Republic a modern tax base to finance impending state obligations.",
        "desc_pt": "Após árduas batalhas parlamentares, a lei de imposto de renda progressivo de Joseph Caillaux é aprovada, conferindo à República uma base tributária moderna para financiar os gastos de Estado."
    },

    # Y = 6
    {
        "id": "FRA_assassinat_de_jean_jaures",
        "x": 10, "y": 6, "cost": 5,
        "icon": "GFX_FRA_assassinat_de_jean_jaures",
        "prereq": ["FRA_pacifisme_de_jean_jaures"], "mut": [],
        "reward": """add_stability = -0.05
add_war_support = 0.05
country_event = { id = ww1_france.50 days = 1 }""",
        "title_en": "Assassination of Jean Jaurès",
        "title_pt": "Assassinato de Jean Jaurès",
        "desc_en": "On 31 July 1914 at Café du Croissant in Paris, fanatic nationalist Raoul Villain murders Jean Jaurès. The death of the great pacifist removes the final obstacle to total national cohesion.",
        "desc_pt": "Em 31 de julho de 1914, no Café du Croissant em Paris, o fanático nacionalista Raoul Villain assassina Jean Jaurès. A morte do grande tribuno remove o último obstáculo à coesão patriótica."
    },
    {
        "id": "FRA_proclamer_union_sacree",
        "x": 6, "y": 6, "cost": 10,
        "icon": "GFX_FRA_proclamer_union_sacree",
        "prereq": ["FRA_reforme_fiscale_impot_revenu"], "mut": [],
        "reward": """add_war_support = 0.12
add_stability = 0.08
swap_ideas = {
    remove_idea = FRA_third_republic_instability
    add_idea = FRA_union_sacree_spirit
}
country_event = { id = ww1_france.51 days = 2 }""",
        "title_en": "Proclaim the Sacred Union",
        "title_pt": "Proclamar a União Sagrada",
        "desc_en": "'Nothing will break the Sacred Union of all Frenchmen in the face of the enemy,' proclaims President Poincaré. Catholics, socialists, radicals, and royalists stand shoulder-to-shoulder in the trenches.",
        "desc_pt": "'Nada quebrará a União Sagrada de todos os franceses diante do inimigo', proclama o Presidente Poincaré. Católicos, socialistas, radicais e monarquistas cerram fileiras lado a lado nas trincheiras."
    },

    # Y = 7
    {
        "id": "FRA_gouvernement_de_defense_nationale",
        "x": 4, "y": 7, "cost": 8,
        "icon": "GFX_FRA_gouvernement_de_defense_nationale",
        "prereq": ["FRA_proclamer_union_sacree"], "mut": [],
        "reward": """add_political_power = 60
add_ideas = FRA_war_cabinet_discipline""",
        "title_en": "National Defense Government",
        "title_pt": "Governo de Defesa Nacional",
        "desc_en": "Premier René Viviani reorganizes the cabinet to include socialist leaders Jules Guesde and Marcel Sembat alongside Alexandre Millerand, cementing national unity across the political spectrum.",
        "desc_pt": "O primeiro-ministro René Viviani reorganiza o ministério para incluir os líderes socialistas Jules Guesde e Marcel Sembat ao lado de Alexandre Millerand, consolidando a frente política republicana."
    },
    {
        "id": "FRA_repli_du_gouvernement_a_bordeaux",
        "x": 8, "y": 7, "cost": 6,
        "icon": "GFX_FRA_repli_du_gouvernement_a_bordeaux",
        "prereq": ["FRA_proclamer_union_sacree"], "mut": [],
        "reward": """add_stability = 0.03
19 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Government Relocation to Bordeaux",
        "title_pt": "Retirada do Governo para Bordeaux",
        "desc_en": "With German cavalry scouts nearing Paris in September 1914, the government and the Banque de France temporarily relocate to Bordeaux, ensuring state continuity while Gallieni defends the capital.",
        "desc_pt": "Com a cavalaria alemã aproximando-se de Paris em setembro de 1914, o governo e o Banco da França transferem-se temporariamente para Bordeaux, assegurando a continuidade do Estado enquanto Gallieni defende a capital."
    },

    # Y = 8
    {
        "id": "FRA_censure_et_bourrage_de_crane",
        "x": 2, "y": 8, "cost": 8,
        "icon": "GFX_FRA_censure_et_bourrage_de_crane",
        "prereq": ["FRA_gouvernement_de_defense_nationale"], "mut": [],
        "reward": """add_war_support = 0.05
add_stability = 0.03
add_political_power = -20""",
        "title_en": "Press Censorship & War Morale",
        "title_pt": "Censura à Imprensa e Moral de Guerra",
        "desc_en": "The military press bureau ('Anastasie') excises military leaks, defeats, and defeatist defeatism from newspapers, preserving home-front calm despite grim trench reality.",
        "desc_pt": "O bureau de imprensa militar ('Anastasie') elimina vazamentos sobre recuos e boatos derrotistas dos jornais, preservando a firmeza civil na retaguarda perante as realidades das trincheiras."
    },
    {
        "id": "FRA_comite_de_guerre_secret",
        "x": 6, "y": 8, "cost": 8,
        "icon": "GFX_FRA_comite_de_guerre_secret",
        "prereq": ["FRA_gouvernement_de_defense_nationale"], "mut": [],
        "reward": """add_command_power = 20
add_political_power = 40""",
        "title_en": "Secret War Committee",
        "title_pt": "Comitê Secreto de Guerra",
        "desc_en": "Meeting behind closed doors, key parliamentary leaders examine logistics, shell shortages, and general staff decisions without alerting enemy espionage.",
        "desc_pt": "Reunindo-se a portas fechadas, lideranças parlamentares chave avaliam a logística, a produção de munições e as operações do estado-maior sem expor segredos à espionagem inimiga."
    },
    {
        "id": "FRA_mobilisation_des_esprits",
        "x": 10, "y": 8, "cost": 8,
        "icon": "GFX_FRA_mobilisation_des_esprits",
        "prereq": ["FRA_repli_du_gouvernement_a_bordeaux"], "mut": [],
        "reward": """add_war_support = 0.06
add_political_power = 30""",
        "title_en": "Mobilisation of the Minds",
        "title_pt": "Mobilização das Consciências",
        "desc_en": "Intellectuals, teachers, scientists, and the Académie Française rally in cultural defense of civilization against Germanic militarism, instilling enduring resolve across all schools.",
        "desc_pt": "Intelectuais, professores, cientistas e a Academia Francesa mobilizam-se na defesa cultural da civilização contra o militarismo germânico, incutindo determinação cívica em todas as escolas."
    },

    # Y = 9
    {
        "id": "FRA_la_crise_politique_de_1917",
        "x": 6, "y": 9, "cost": 8,
        "icon": "GFX_FRA_la_crise_politique_de_1917",
        "prereq": ["FRA_comite_de_guerre_secret"], "mut": [],
        "reward": """add_stability = -0.06
add_political_power = -30
country_event = { id = ww1_france.52 days = 1 }""",
        "title_en": "The Political Crisis of 1917",
        "title_pt": "A Crise Política de 1917",
        "desc_en": "After three years of trench bloodbaths, strikes erupt in munitions factories, the Russian ally collapses, and political infighting brings down cabinets in rapid succession.",
        "desc_pt": "Após três anos de hecatombe nas trincheiras, eclodem greves nas fábricas de armas, a Rússia aliada entra em colapso e disputas políticas derrubam gabinetes em rápida sucessão."
    },
    {
        "id": "FRA_repressions_du_defaitisme",
        "x": 2, "y": 9, "cost": 6,
        "icon": "GFX_FRA_repressions_du_defaitisme",
        "prereq": ["FRA_censure_et_bourrage_de_crane"], "mut": [],
        "reward": """add_stability = 0.04
add_political_power = 30""",
        "title_en": "Prosecution of Defeatism",
        "title_pt": "Repressão ao Derrotismo",
        "desc_en": "Subversive pacifist networks, German-funded publications like Le Bonnet Rouge, and corrupt officials are unmasked and prosecuted to maintain civilian courage.",
        "desc_pt": "Redes pacifistas clandestinas, publicações financiadas pela Alemanha como o Le Bonnet Rouge e agentes corruptos são desmascarados e julgados para manter a coragem da retaguarda."
    },
    {
        "id": "FRA_comite_des_forges_coordination",
        "x": 10, "y": 9, "cost": 8,
        "icon": "GFX_FRA_comite_des_forges_coordination",
        "prereq": ["FRA_mobilisation_des_esprits"], "mut": [],
        "reward": """add_ideas = FRA_employer_union_compact
27 = { add_extra_state_shared_building_slots = 1 }""",
        "title_en": "Heavy Industry Coordination Compact",
        "title_pt": "Pacto de Coordenação da Indústria Pesada",
        "desc_en": "The Comité des Forges negotiates price ceilings and guaranteed steel allocations with ministry officials, keeping blast furnaces operating day and night.",
        "desc_pt": "O Comité des Forges estabelece tetos de preço e cotas de aço garantidas com os ministérios, mantendo os altos-fornos em operação dia e noite."
    },

    # Y = 10
    {
        "id": "FRA_appel_au_tigre",
        "x": 4, "y": 10, "cost": 6,
        "icon": "GFX_FRA_appel_au_tigre",
        "prereq": ["FRA_la_crise_politique_de_1917"], "mut": [],
        "reward": """country_event = { id = ww1_france.61 days = 1 }
add_political_power = 75
add_war_support = 0.08""",
        "title_en": "Call to The Tiger (Clemenceau)",
        "title_pt": "O Chamado ao Tigre (Clemenceau)",
        "desc_en": "Swallowing personal antipathy, President Poincaré summons 76-year-old Georges Clemenceau, 'The Tiger', to form a government of unbending iron will.",
        "desc_pt": "Engolindo antipatias pessoais, o Presidente Poincaré convoca Georges Clemenceau, o 'Tigre' de 76 anos, para assumir a chefia do governo com determinação de aço."
    },
    {
        "id": "FRA_maintien_du_parlementarisme_guerre",
        "x": 8, "y": 10, "cost": 8,
        "icon": "GFX_FRA_maintien_du_parlementarisme_guerre",
        "prereq": ["FRA_la_crise_politique_de_1917"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = 40""",
        "title_en": "Parliamentary Oversight in War",
        "title_pt": "Supervisão Parlamentar na Guerra",
        "desc_en": "Unlike Germany's military dictatorship under Ludendorff, France preserves legislative supremacy. Civilian parliamentarians regularly inspect frontline hospital trains and trenches.",
        "desc_pt": "Diferente da ditadura militar de Ludendorff na Alemanha, a França preserva a supremacia republicana legislativa. Deputados inspecionam hospitais de campanha e trincheiras regularmente."
    },

    # Y = 11
    {
        "id": "FRA_je_fais_la_guerre",
        "x": 4, "y": 11, "cost": 10,
        "icon": "GFX_FRA_je_fais_la_guerre",
        "prereq": ["FRA_appel_au_tigre"], "mut": [],
        "reward": """add_ideas = FRA_clemenceau_iron_resolve
add_war_support = 0.10
add_stability = 0.05""",
        "title_en": "'Je fais la guerre' (I Wage War)",
        "title_pt": "'Je fais la guerre' (Eu Faço a Guerra)",
        "desc_en": "'Home policy? I wage war. Foreign policy? I wage war. Russia deserts us? I wage war. Until the final quarter of an hour!' Clemenceau galvanizes the French soul to victory.",
        "desc_pt": "'Política interna? Eu faço a guerra. Política externa? Eu faço a guerra. A Rússia nos trai? Eu faço a guerra. Até o último quarto de hora!' Clemenceau galvaniza o espírito francês para a vitória."
    },
    {
        "id": "FRA_la_victoire_de_la_republique",
        "x": 8, "y": 11, "cost": 10,
        "icon": "GFX_FRA_la_victoire_de_la_republique",
        "prereq": ["FRA_maintien_du_parlementarisme_guerre", "FRA_je_fais_la_guerre"], "mut": [],
        "reward": """add_political_power = 100
add_stability = 0.10
add_war_support = 0.10
swap_ideas = {
    remove_idea = FRA_union_sacree_spirit
    add_idea = FRA_union_sacree_victory
}""",
        "title_en": "Victory of the Republic",
        "title_pt": "A Vitória da República",
        "desc_en": "The democratic republic has endured the greatest storm in human history without collapsing into tyranny, proving to the world that free citizens can defeat autocracy.",
        "desc_pt": "A república democrática resistiu à maior tempestade da história humana sem sucumbir à tirania, provando ao mundo que cidadãos livres podem triunfar sobre a autocracia."
    },
    {
        "id": "FRA_reconciliation_avec_les_catholiques",
        "x": 0, "y": 4, "cost": 8,
        "icon": "GFX_FRA_reconciliation_avec_les_catholiques",
        "prereq": ["FRA_senat_et_chambre_des_deputes"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = 25""",
        "title_en": "Reconciliation with Catholics",
        "title_pt": "Reconciliação com os Católicos",
        "desc_en": "Clergy serving as stretcher-bearers and officers in the trenches dissolve anticlerical resentment, uniting believers and freethinkers under the tricolor.",
        "desc_pt": "Padres e seminaristas atuando como maqueiros e oficiais nas trincheiras dissolvem velhos ressentimentos anticlericais, unindo fiéis e laicos sob o tricolor."
    },
    {
        "id": "FRA_presse_populaire_et_illustres",
        "x": 12, "y": 4, "cost": 8,
        "icon": "GFX_FRA_presse_populaire_et_illustres",
        "prereq": ["FRA_laicite_republicaine"], "mut": [],
        "reward": """add_political_power = 30
add_stability = 0.03""",
        "title_en": "Mass Press & Popular Broadsheets",
        "title_pt": "Imprensa Popular e Ilustrados",
        "desc_en": "Le Petit Journal, Le Matin, and L'Écho de Paris foster a shared civic culture, linking Parisian debate with provincial villages through affordable print.",
        "desc_pt": "O Le Petit Journal, Le Matin e L'Écho de Paris consolidam uma cultura cívica compartilhada, conectando os debates de Paris às vilas provincianas por centavos."
    },
    {
        "id": "FRA_statut_des_fonctionnaires",
        "x": 0, "y": 7, "cost": 8,
        "icon": "GFX_FRA_statut_des_fonctionnaires",
        "prereq": ["FRA_reconciliation_avec_les_catholiques"], "mut": [],
        "reward": """add_political_power = 40
add_ideas = FRA_competent_civil_administration""",
        "title_en": "Civil Service Merit Code",
        "title_pt": "Estatuto do Funcionalismo Público",
        "desc_en": "Professionalising the prefects and ministry bureaucracy ensures transparent administration, fiscal integrity, and swift mobilization.",
        "desc_pt": "A profissionalização dos prefeitos e da burocracia ministerial garante uma administração transparente, rigor fiscal e rápida capacidade de mobilização."
    },
    {
        "id": "FRA_ecole_normale_et_instituteurs",
        "x": 12, "y": 7, "cost": 8,
        "icon": "GFX_FRA_ecole_normale_et_instituteurs",
        "prereq": ["FRA_presse_populaire_et_illustres"], "mut": [],
        "reward": """add_research_slot = 1
add_political_power = 25""",
        "title_en": "Republic's Black Hussars (Teachers)",
        "title_pt": "Os Hussardos Negros da República",
        "desc_en": "The secular schoolmasters ('Hussards noirs') form the moral backbone of every commune, teaching scientific method, French history, and unyielding civic duty.",
        "desc_pt": "Os professores públicos laicos ('Hussards noirs') formam a espinha dorsal moral de cada comuna, ensinando o método científico, a história da França e o dever cívico."
    },
    {
        "id": "FRA_solidarite_nationale_veufs_orphelins",
        "x": 0, "y": 10, "cost": 8,
        "icon": "GFX_FRA_solidarite_nationale_veufs_orphelins",
        "prereq": ["FRA_statut_des_fonctionnaires"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = -20
add_ideas = FRA_wards_of_the_nation_care""",
        "title_en": "Pupils of the Nation (War Widows & Orphans)",
        "title_pt": "Pupilos da Nação (Viúvas e Órfãos)",
        "desc_en": "The Republic adopts war orphans as 'Pupilles de la Nation', guaranteeing state funding for their education, healthcare, and livelihood.",
        "desc_pt": "A República adota os órfãos de guerra como 'Pupilles de la Nation', garantindo financiamento público integral para sua educação, saúde e subsistência."
    },
    {
        "id": "FRA_reorganisation_post_guerre",
        "x": 12, "y": 10, "cost": 8,
        "icon": "GFX_FRA_reorganisation_post_guerre",
        "prereq": ["FRA_ecole_normale_et_instituteurs"], "mut": [],
        "reward": """add_political_power = 50
16 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "Post-War Institutional Renewal",
        "title_pt": "Renovação Institucional do Pós-Guerra",
        "desc_en": "Streamlining parliamentary commissions and updating prefectural powers prepares the state to manage reconstruction and demobilization.",
        "desc_pt": "A modernização das comissões parlamentares e dos poderes das prefeituras prepara o Estado para liderar a reconstrução e a desmobilização."
    }
]
