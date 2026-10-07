# -*- coding: utf-8 -*-
"""France Wing 6: Diplomatie Global, Alianças da Entente & Relações Externas (35 focuses).
X range: 82 .. 98 | Y range: 0 .. 11
All references to Russia use the authentic WW1 tag 'RUS'!
Full reciprocal events for RUS, ENG, ITA, BEL, SER, ROM, GRE, USA.
"""

WING6_FOCI = [
    # Y = 0 (Diplomatic Roots)
    {
        "id": "FRA_question_du_maroc_1911",
        "x": 85, "y": 0, "cost": 10,
        "icon": "GFX_FRA_question_du_maroc_1911",
        "prereq": [], "mut": [],
        "reward": """country_event = { id = ww1_france.1 days = 1 }
add_political_power = 40""",
        "title_en": "The Moroccan Crisis (Agadir 1911)",
        "title_pt": "A Crise Marroquina (Agadir 1911)",
        "desc_en": "The arrival of the German gunboat SMS Panther at Agadir sparks a grave European standoff. France must defend her special rights in North Africa without precipitating general war.",
        "desc_pt": "A chegada da canhoneira alemã SMS Panther a Agadir deflagra grave crise europeia. A França deve defender seus direitos no Norte da África sem precipitar uma guerra prematura."
    },
    {
        "id": "FRA_l_alliance_franco_russe",
        "x": 91, "y": 0, "cost": 10,
        "icon": "GFX_FRA_l_alliance_franco_russe",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 50
add_ideas = FRA_franco_russian_sacred_alliance""",
        "title_en": "The Franco-Russian Sacred Alliance",
        "title_pt": "A Sagrada Aliança Franco-Russa",
        "desc_en": "Sealed in 1892 between the Republic and Tsar Alexander III, the Franco-Russian military convention guarantees mutual assistance in the event of German aggression, pinning Germany between two fronts.",
        "desc_pt": "Selada em 1892 entre a República e o Czar Alexandre III, a convenção militar franco-russa garante socorro mútuo contra agressão alemã, encurralando a Alemanha entre duas frentes."
    },
    {
        "id": "FRA_l_entente_cordiale",
        "x": 96, "y": 0, "cost": 10,
        "icon": "GFX_FRA_l_entente_cordiale",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 50
add_ideas = FRA_entente_cordiale_brotherhood""",
        "title_en": "The Anglo-French Entente Cordiale",
        "title_pt": "A Entente Cordiale Anglo-Francesa",
        "desc_en": "Forged in 1904 by Théophile Delcassé and King Edward VII, the Entente dissolves centuries of colonial rivalry, uniting the two great liberal democracies in diplomatic defense against German ambition.",
        "desc_pt": "Firmada em 1904 por Théophile Delcassé e Eduardo VII, a Entente dissolve séculos de rivalidade, unindo as duas democracias liberais na contenção das ambições germânicas."
    },

    # Y = 1
    {
        "id": "FRA_fermete_diplomatique_agadir",
        "x": 83, "y": 1, "cost": 6,
        "icon": "GFX_FRA_fermete_diplomatique_agadir",
        "prereq": ["FRA_question_du_maroc_1911"], "mut": ["FRA_compromis_colonial_allemand"],
        "reward": """add_war_support = 0.05
add_political_power = 30
if = {
    limit = { country_exists = GER }
    GER = { country_event = { id = ww1_france.3 days = 2 } }
}""",
        "title_en": "Firm Resolve Against German Gunboats",
        "title_pt": "Firmeza Diplomática em Agadir",
        "desc_en": "Backed by British Chancellor Lloyd George's Mansion House speech, Premier Joseph Caillaux rejects German intimidation, demonstrating Entente unity.",
        "desc_pt": "Apoiado pelo discurso britânico de Lloyd George na Mansion House, o primeiro-ministro Joseph Caillaux rejeita as exigências de Berlim, demonstrando a coesão da Entente."
    },
    {
        "id": "FRA_compromis_colonial_allemand",
        "x": 87, "y": 1, "cost": 6,
        "icon": "GFX_FRA_compromis_colonial_allemand",
        "prereq": ["FRA_question_du_maroc_1911"], "mut": ["FRA_fermete_diplomatique_agadir"],
        "reward": """add_stability = 0.05
add_political_power = 20
if = {
    limit = { country_exists = GER }
    GER = { country_event = { id = ww1_france.5 days = 2 } }
}""",
        "title_en": "Congo-Cameroon Colonial Compromise",
        "title_pt": "Compromisso Colonial do Congo-Camarões",
        "desc_en": "Ceding marshland territory in French Equatorial Congo to German Neukamerun in exchange for uncontested German recognition of France's Moroccan protectorate preserves European peace.",
        "desc_pt": "A cessão de territórios no Congo Francês para os Camarões Alemães em troca do reconhecimento formal do protetorado sobre o Marrocos preserva a paz temporária."
    },
    {
        "id": "FRA_emprunts_russes_chemin_de_fer",
        "x": 89, "y": 1, "cost": 8,
        "icon": "GFX_FRA_emprunts_russes_chemin_de_fer",
        "prereq": ["FRA_l_alliance_franco_russe"], "mut": [],
        "reward": """add_political_power = -30
if = {
    limit = { country_exists = RUS }
    RUS = { country_event = { id = ww1_france.201 days = 1 } }
}""",
        "title_en": "French Loans for Russian Strategic Rail",
        "title_pt": "Empréstimos Franceses para Ferrovias Russas",
        "desc_en": "French bondholders subscribe hundreds of millions of francs to fund double-track strategic railways across Poland and Western Russia, cutting Russian mobilization time in half.",
        "desc_pt": "Investidores franceses financiam centenas de milhões de francos em ferrovias de bitola dupla na Polônia e Rússia Ocidental, reduzindo o tempo de mobilização russa pela metade."
    },
    {
        "id": "FRA_pourparlers_d_etat_major_joffre_jilinsky",
        "x": 93, "y": 1, "cost": 8,
        "icon": "GFX_FRA_pourparlers_d_etat_major_joffre_jilinsky",
        "prereq": ["FRA_l_alliance_franco_russe"], "mut": [],
        "reward": """add_command_power = 25
if = {
    limit = { country_exists = RUS }
    RUS = { country_event = { id = ww1_france.204 days = 1 } }
}""",
        "title_en": "Joffre-Zhilinsky Staff Convention",
        "title_pt": "Convenção de Estados-Maiores Joffre-Jilinsky",
        "desc_en": "General Joffre and General Yakov Zhilinsky pledge that Russia will launch an immediate offensive into East Prussia by the 15th day of mobilization, compelling Germany to fight on two fronts.",
        "desc_pt": "O General Joffre e o General Yakov Zhilinsky acordam que a Rússia lançará ofensiva imediata na Prússia Oriental no 15º dia de mobilização, dividindo as forças alemãs."
    },
    {
        "id": "FRA_accords_navals_franco_britanniques",
        "x": 95, "y": 1, "cost": 8,
        "icon": "GFX_FRA_accords_navals_franco_britanniques",
        "prereq": ["FRA_l_entente_cordiale"], "mut": [],
        "reward": """add_navy_experience = 20
if = {
    limit = { country_exists = ENG }
    ENG = { country_event = { id = ww1_france.250 days = 1 } }
}""",
        "title_en": "1912 Anglo-French Naval Accords",
        "title_pt": "Acordos Navais Anglo-Franceses de 1912",
        "desc_en": "Winston Churchill and Boué de Lapeyrère agree to strategic maritime division: France concentrates her battle fleet in the Mediterranean, while Britain assumes defense of the Channel and Atlantic.",
        "desc_pt": "Winston Churchill e Boué de Lapeyrère acordam a divisão dos mares: a França concentra sua esquadra no Mediterrâneo, enquanto a Grã-Bretanha guarnece o Canal da Mancha e o Mar do Norte."
    },
    {
        "id": "FRA_plans_de_debarquement_du_bef",
        "x": 97, "y": 1, "cost": 8,
        "icon": "GFX_FRA_plans_de_debarquement_du_bef",
        "prereq": ["FRA_l_entente_cordiale"], "mut": [],
        "reward": """add_ideas = FRA_bef_channel_ports_coordination
if = {
    limit = { country_exists = ENG }
    ENG = { country_event = { id = ww1_france.253 days = 1 } }
}""",
        "title_en": "Secret BEF Landing & Deployment Plans",
        "title_pt": "Planos Secretos de Desembarque do BEF",
        "desc_en": "General Henry Wilson and French staff secretly map disembarkation timetables at Le Havre, Boulogne, and Rouen, aligning the British Expeditionary Force on the French left flank.",
        "desc_pt": "O General Henry Wilson e o estado-maior francês mapeiam os desembarques em Le Havre, Boulogne e Rouen, alinhando a Força Expedicionária Britânica no flanco esquerdo francês."
    },
    {
        "id": "FRA_garantie_de_la_neutralite_belge",
        "x": 96, "y": 1, "cost": 8,
        "icon": "GFX_FRA_garantie_de_la_neutralite_belge",
        "prereq": ["FRA_l_entente_cordiale"], "mut": [],
        "reward": """add_political_power = 40
add_ideas = FRA_treaty_of_london_1839_guarantor""",
        "title_en": "Guarantor of the 1839 Treaty of London",
        "title_pt": "Garantidor do Tratado de Londres de 1839",
        "desc_en": "Reaffirming France and Britain's solemn pledge to uphold Belgian perpetual neutrality protects the Low Countries against Prussian encroachment.",
        "desc_pt": "A reafirmação solene do compromisso franco-britânico de defender a neutralidade perpétua da Bélgica protege os Países Baixos contra a agressão prussiana."
    },

    # Y = 2
    {
        "id": "FRA_traite_de_fez_1912",
        "x": 85, "y": 2, "cost": 8,
        "icon": "GFX_FRA_traite_de_fez_1912",
        "prereq": ["FRA_fermete_diplomatique_agadir", "FRA_compromis_colonial_allemand"], "mut": [],
        "reward": """add_political_power = 40
add_ideas = FRA_morocco_treaty_of_fez""",
        "title_en": "Treaty of Fez (Moroccan Protectorate)",
        "title_pt": "Tratado de Fez (Protetorado Marroquino)",
        "desc_en": "Sultan Abdelhafid signs the Treaty of Fez, formally establishing the French Protectorate in Morocco under General Lyautey while recognizing Spanish interests in the north.",
        "desc_pt": "O Sultão Abdelhafid assina o Tratado de Fez, estabelecendo formalmente o Protetorado Francês no Marrocos sob Lyautey e reconhecendo a esfera espanhola no norte."
    },
    {
        "id": "FRA_visite_de_poincare_a_saint_petersbourg",
        "x": 91, "y": 2, "cost": 8,
        "icon": "GFX_FRA_visite_de_poincare_a_saint_petersbourg",
        "prereq": ["FRA_emprunts_russes_chemin_de_fer", "FRA_pourparlers_d_etat_major_joffre_jilinsky"], "mut": [],
        "reward": """add_political_power = 40
add_war_support = 0.08
add_stability = 0.04""",
        "title_en": "Poincaré's State Visit to St. Petersburg",
        "title_pt": "Visita de Estado de Poincaré a São Petersburgo",
        "desc_en": "In July 1914 aboard the battleship France, President Poincaré sails to Peterhof, reaffirming absolute, unshakeable French fidelity to Tsar Nicholas II as the July Crisis gathers storm.",
        "desc_pt": "Em julho de 1914, a bordo do couraçado France, Poincaré navega a São Petersburgo, reafirmando aliança inabalável com Nicolau II enquanto a Crise de Julho se avizinha."
    },
    {
        "id": "FRA_coordination_des_etats_majors_haig_joffre",
        "x": 98, "y": 2, "cost": 8,
        "icon": "GFX_FRA_coordination_des_etats_majors_haig_joffre",
        "prereq": ["FRA_plans_de_debarquement_du_bef"], "mut": [],
        "reward": """add_command_power = 20
add_ideas = FRA_joint_liaison_missions""",
        "title_en": "Haig-Joffre Staff Liaison Coordination",
        "title_pt": "Coordenação de Ligação Haig-Joffre",
        "desc_en": "Bilingual liaison officers stationed at British GHQ in Montreuil and French GQG in Chantilly coordinate boundary lines, artillery zones, and supply railheads.",
        "desc_pt": "Oficiais de ligação bilíngues em Montreuil e Chantilly coordenam linhas de limite de setor, zonas de artilharia e entroncamentos logísticos."
    },
    {
        "id": "FRA_solidarite_avec_la_belgique",
        "x": 96, "y": 2, "cost": 6,
        "icon": "GFX_FRA_solidarite_avec_la_belgique",
        "prereq": ["FRA_plans_de_debarquement_du_bef"], "mut": [],
        "reward": """add_political_power = 30
if = {
    limit = { country_exists = BEL }
    BEL = { country_event = { id = ww1_france.213 days = 1 } }
}""",
        "title_en": "Sacred Solidarity with Heroic Belgium",
        "title_pt": "Solidariedade com a Bélgica Heroica",
        "desc_en": "When German armies violate Belgian neutrality on 4 August 1914, France rushes division columns northwards to assist King Albert I's valiant defense of Liège and Namur.",
        "desc_pt": "Quando os exércitos alemães violam a neutralidade belga em 4 de agosto de 1914, a França envia divisões ao norte para apoiar a resistência do Rei Alberto I em Liège."
    },

    # Y = 3
    {
        "id": "FRA_loi_des_trois_ans_1913",
        "x": 85, "y": 3, "cost": 8,
        "icon": "GFX_FRA_loi_des_trois_ans_1913",
        "prereq": ["FRA_traite_de_fez_1912"], "mut": [],
        "reward": """add_ideas = FRA_three_year_conscription
add_manpower = 60000
add_war_support = 0.05""",
        "title_en": "The 1913 Three-Year Military Law",
        "title_pt": "A Lei Militar dos Três Anos de 1913",
        "desc_en": "Faced with Germany's rising peacetime army, Premier Louis Barthou passes the Three-Year Law, extending compulsory military service to keep 750,000 active troops under arms.",
        "desc_pt": "Diante da expansão do exército do Kaiser, o parlamento aprova a Lei dos Três Anos, estendendo o serviço militar obrigatório para manter 750.000 combatentes ativos sob as armas."
    },
    {
        "id": "FRA_coordination_sur_les_deux_fronts",
        "x": 91, "y": 3, "cost": 8,
        "icon": "GFX_FRA_coordination_sur_les_deux_fronts",
        "prereq": ["FRA_visite_de_poincare_a_saint_petersbourg"], "mut": [],
        "reward": """add_timed_idea = { idea = FRA_ww1_allied_staff days = 180 }
add_political_power = 30""",
        "title_en": "Two-Front Allied War Coordination",
        "title_pt": "Coordenação de Guerra em Duas Frentes",
        "desc_en": "General Janin in Petrograd and General Ignatiev in Paris synchronize operations, coordinating Grand Duke Nicholas' East Prussian drive to draw German corps away from Paris.",
        "desc_pt": "Generais de ligação em Paris e Petrogrado sincronizam os cronogramas operacionais, forçando o comando alemão a desviar corpos de exército do Marne para Tannenberg."
    },
    {
        "id": "FRA_conseil_supreme_de_guerre_versailles",
        "x": 96, "y": 3, "cost": 8,
        "icon": "GFX_FRA_conseil_supreme_de_guerre_versailles",
        "prereq": ["FRA_solidarite_avec_la_belgique"], "mut": [],
        "reward": """add_political_power = 40
add_command_power = 20
if = {
    limit = { country_exists = ENG }
    ENG = { country_event = { id = ww1_france.216 days = 1 } }
}""",
        "title_en": "Supreme War Council in Versailles",
        "title_pt": "Conselho Supremo de Guerra em Versalhes",
        "desc_en": "Established at Trianon Palace, the Supreme War Council coordinates allied strategic decisions, shipping, raw materials, and unified military reserves across the Entente.",
        "desc_pt": "Sediado no Palácio de Trianon, o Conselho Supremo de Guerra coordena estratégias militares, alocação de navios cargueiros e reservas aliadas unificadas."
    },

    # Y = 4
    {
        "id": "FRA_soutien_financier_au_tsar",
        "x": 91, "y": 4, "cost": 8,
        "icon": "GFX_FRA_soutien_financier_au_tsar",
        "prereq": ["FRA_coordination_sur_les_deux_fronts"], "mut": [],
        "reward": """add_political_power = -25
if = {
    limit = { country_exists = RUS }
    RUS = { country_event = { id = ww1_france.206 days = 1 } }
}""",
        "title_en": "Arms & Shell Shipments to Russia",
        "title_pt": "Envio de Armas e Projéteis à Rússia",
        "desc_en": "Despite our own shell famine, thousands of tons of heavy artillery, machine guns, and ammunition are shipped to the Russian army via Archangelsk and Vladivostok.",
        "desc_pt": "Apesar da escassez interna, comboios de armas pesadas, metralhadoras e munições são despachados para o exército do Czar através de Arkhangelsk e Vladivostok."
    },

    # Y = 5
    {
        "id": "FRA_gestion_du_collapsus_russe_1917",
        "x": 91, "y": 5, "cost": 8,
        "icon": "GFX_FRA_gestion_du_collapsus_russe_1917",
        "prereq": ["FRA_soutien_financier_au_tsar"], "mut": [],
        "reward": """add_war_support = 0.05
add_ideas = FRA_eastern_front_containment""",
        "title_en": "Handling the 1917 Russian Collapse",
        "title_pt": "Gerenciamento do Colapso Russo de 1917",
        "desc_en": "When revolution disintegrates the Russian front and the Bolsheviks sign the Brest-Litovsk peace, France stiffens her Western Front defenses against forty transferred German divisions.",
        "desc_pt": "Com a desintegração da frente russa pela revolução e o tratado de Brest-Litovsk, a França prepara suas defesas para conter quarenta divisões alemãs transferidas do leste."
    },

    # Y = 6 (Southern & Balkan Fronts)
    {
        "id": "FRA_negocier_avec_l_italie_traite_de_londres",
        "x": 84, "y": 6, "cost": 8,
        "icon": "GFX_FRA_negocier_avec_l_italie_traite_de_londres",
        "prereq": ["FRA_loi_des_trois_ans_1913"], "mut": [],
        "reward": """add_political_power = 50
if = {
    limit = { country_exists = ITA }
    ITA = { country_event = { id = ww1_france.220 days = 1 } }
}""",
        "title_en": "Secret Treaty of London with Italy (1915)",
        "title_pt": "Tratado Secreto de Londres com a Itália (1915)",
        "desc_en": "French and British diplomacy tempts Rome away from the Triple Alliance, promising Trentino, Trieste, Istria, and Dalmatian territories in exchange for attacking Austria-Hungary.",
        "desc_pt": "A diplomacia franco-britânica afasta Roma da Tríplice Aliança, garantindo o Trentino, Trieste e a Ístria em troca da declaração de guerra contra a Áustria-Hungria."
    },
    {
        "id": "FRA_soutien_inconditionnel_a_la_serbie",
        "x": 88, "y": 6, "cost": 8,
        "icon": "GFX_FRA_soutien_inconditionnel_a_la_serbie",
        "prereq": ["FRA_loi_des_trois_ans_1913"], "mut": [],
        "reward": """add_stability = 0.04
if = {
    limit = { country_exists = SER }
    SER = { country_event = { id = ww1_france.230 days = 1 } }
}""",
        "title_en": "Rescue & Evacuation of the Serbian Army",
        "title_pt": "Resgate e Reequipamento do Exército Sérvio",
        "desc_en": "Following the heroic winter retreat through the Albanian mountains, French naval vessels evacuate 140,000 Serbian troops to Corfu, rearming them with French rifles and 75mm guns.",
        "desc_pt": "Após a retirada pelos picos albaneses, navios franceses evacuam 140.000 soldados sérvios para Corfu, rearmando-os com fuzis e canhões franceses para retomar a luta."
    },

    # Y = 7
    {
        "id": "FRA_mission_militaire_en_roumanie_berthelot",
        "x": 84, "y": 7, "cost": 8,
        "icon": "GFX_FRA_mission_militaire_en_roumanie_berthelot",
        "prereq": ["FRA_negocier_avec_l_italie_traite_de_londres"], "mut": [],
        "reward": """add_political_power = 30
if = {
    limit = { country_exists = ROM }
    ROM = { country_event = { id = ww1_france.232 days = 1 } }
}""",
        "title_en": "General Berthelot's Romanian Mission",
        "title_pt": "Missão Militar Berthelot na Romênia",
        "desc_en": "General Henri Berthelot and hundreds of French staff officers reorganize the shattered Romanian army in Moldavia, teaching modern trench tactics that hold Mărășești.",
        "desc_pt": "O General Henri Berthelot e oficiais franceses reconstroem o exército romeno na Moldávia, introduzindo táticas modernas que garantem a vitória heróica em Mărășești."
    },
    {
        "id": "FRA_front_d_orient_a_salonique",
        "x": 88, "y": 7, "cost": 8,
        "icon": "GFX_FRA_front_d_orient_a_salonique",
        "prereq": ["FRA_soutien_inconditionnel_a_la_serbie"], "mut": [],
        "reward": """add_ideas = FRA_ww1_salonika_transport
if = {
    limit = { country_exists = GRE }
    GRE = { country_event = { id = ww1_france.234 days = 1 } }
}""",
        "title_en": "Allied Army of the Orient at Salonica",
        "title_pt": "Exército Aliado do Oriente em Salônica",
        "desc_en": "General Sarrail builds the fortified 'Birdcage' around Salonica, welcoming Serbian, British, Italian, and Greek divisions to tie down German and Bulgarian armies in the Balkans.",
        "desc_pt": "O General Sarrail constrói a linha fortificada de Salônica, reunindo divisões francesas, sérvias, britânicas e gregas para fixar os exércitos búlgaro e alemão nos Balcãs."
    },
    {
        "id": "FRA_exploiter_la_guerre_sous_marine_a_outrance",
        "x": 94, "y": 7, "cost": 8,
        "icon": "GFX_FRA_exploiter_la_guerre_sous_marine_a_outrance",
        "prereq": ["FRA_conseil_supreme_de_guerre_versailles"], "mut": [],
        "reward": """add_war_support = 0.05
add_political_power = 30""",
        "title_en": "Outrage Over Unrestricted Submarine Warfare",
        "title_pt": "Repúdio à Guerra Submarina Irrestrita",
        "desc_en": "German sinkings of neutral passenger liners like the Sussex and Lusitania are publicized worldwide, turning global and American sympathy decisively toward the Entente.",
        "desc_pt": "O torpedeamento alemão de navios mercantes neutros como o Sussex e Lusitania mobiliza a indignação mundial, voltando a simpatia americana para a Entente."
    },

    # Y = 8
    {
        "id": "FRA_offensive_du_vardar_franchet_d_esperey",
        "x": 86, "y": 8, "cost": 8,
        "icon": "GFX_FRA_offensive_du_vardar_franchet_d_esperey",
        "prereq": ["FRA_mission_militaire_en_roumanie_berthelot", "FRA_front_d_orient_a_salonique"], "mut": [],
        "reward": """add_war_support = 0.08
add_political_power = 50
if = {
    limit = { country_exists = BUL }
    BUL = { country_event = { id = ww1_france.236 days = 1 } }
}""",
        "title_en": "Franchet d'Espèrey's Vardar Breakthrough",
        "title_pt": "Ruptura de Franchet d'Espèrey no Vardar",
        "desc_en": "In September 1918, General Franchet d'Espèrey ('Desperate Frankie') smashes Bulgarian mountain positions at Dobro Pole, compelling Bulgaria to sign the first armistice of the war.",
        "desc_pt": "Em setembro de 1918, Franchet d'Espèrey rompe as defesas búlgaras em Dobro Pole, forçando a Bulgária a capitular e abrindo a rota de invasão da Áustria e Hungria."
    },
    {
        "id": "FRA_capitulation_de_la_bulgarie",
        "x": 86, "y": 9, "cost": 6,
        "icon": "GFX_FRA_capitulation_de_la_bulgarie",
        "prereq": ["FRA_offensive_du_vardar_franchet_d_esperey"], "mut": [],
        "reward": """add_stability = 0.05
add_war_support = 0.05
add_political_power = 40""",
        "title_en": "The Armistice of Salonica (Bulgarian Collapse)",
        "title_pt": "Armistício de Salônica (Capitulação Búlgara)",
        "desc_en": "Bulgaria signs the Armistice of Salonica on 29 September 1918, shattering the Central Powers' Balkan bridge to Istanbul and exposing Austria's southern frontier.",
        "desc_pt": "A Bulgária assina o Armistício de Salônica em 29 de setembro de 1918, rompendo a ligação das Potências Centrais com Istambul e expondo o flanco sul da Áustria."
    },
    {
        "id": "FRA_intervention_a_odessa_mer_noire",
        "x": 92, "y": 8, "cost": 6,
        "icon": "GFX_FRA_intervention_a_odessa_mer_noire",
        "prereq": ["FRA_gestion_du_collapsus_russe_1917"], "mut": [],
        "reward": """add_political_power = 25
add_navy_experience = 15""",
        "title_en": "Black Sea & Odessa Expedition",
        "title_pt": "Expedição Naval de Odessa e Mar Negro",
        "desc_en": "Following the collapse of Russian authority, French squadrons and colonial landing parties anchor in Odessa and Sevastopol to secure grain and protect southern allied interests.",
        "desc_pt": "Com a queda da autoridade imperial russa, esquadras francesas e tropas coloniais desembarcam em Odessa e Sebastopol para salvaguardar interesses aliados no Mar Negro."
    },

    # Y = 9 (American Intervention & Pre-Peace)
    {
        "id": "FRA_relations_financieres_avec_les_usa",
        "x": 94, "y": 8, "cost": 6,
        "icon": "GFX_FRA_relations_financieres_avec_les_usa",
        "prereq": ["FRA_conseil_supreme_de_guerre_versailles"], "mut": [],
        "reward": """add_political_power = 40
16 = { add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }""",
        "title_en": "American Commercial & Financial Ties",
        "title_pt": "Relações Comerciais e Financeiras com os EUA",
        "desc_en": "Massive French grain and copper purchases from the United States forge deep economic interdependency, laying the groundwork for Washington's eventual entry into the conflict.",
        "desc_pt": "Compras volumosas de cobre e grãos nos Estados Unidos forjam profunda interdependência econômica, pavimentando a entrada definitiva de Washington no conflito."
    },
    {
        "id": "FRA_mission_viviani_joffre_aux_usa",
        "x": 94, "y": 9, "cost": 6,
        "icon": "GFX_FRA_mission_viviani_joffre_aux_usa",
        "prereq": ["FRA_relations_financieres_avec_les_usa"], "mut": [],
        "reward": """add_war_support = 0.05
add_political_power = 40
if = {
    limit = { country_exists = USA }
    USA = { country_event = { id = ww1_france.260 days = 1 } }
}""",
        "title_en": "Joffre & Viviani Diplomatic Mission to Washington",
        "title_pt": "Missão Viviani-Joffre em Washington",
        "desc_en": "Marshal Joffre visits the White House in spring 1917 to thunderous American acclaim, urging President Woodrow Wilson to dispatch US divisions to France without delay.",
        "desc_pt": "O Marechal Joffre é ovacionado em Washington na primavera de 1917, convencendo Woodrow Wilson a acelerar o despacho de divisões americanas para a França."
    },
    {
        "id": "FRA_arrivee_du_corps_expeditionnaire_americain",
        "x": 94, "y": 10, "cost": 8,
        "icon": "GFX_FRA_arrivee_du_corps_expeditionnaire_americain",
        "prereq": ["FRA_mission_viviani_joffre_aux_usa"], "mut": [],
        "reward": """add_ideas = FRA_american_aef_arrival
add_war_support = 0.08
add_stability = 0.05""",
        "title_en": "'Lafayette, nous voilà!' (AEF Arrival)",
        "title_pt": "'Lafayette, nous voilà!' (Chegada da AEF)",
        "desc_en": "General John J. Pershing lands in France. At Picpus cemetery, Colonel Stanton declares: 'Lafayette, we are here!' Two million American Doughboys prepare to take their place on the line.",
        "desc_pt": "O General Pershing desembarca na França. No túmulo do Marquês de Lafayette, proclama-se a dívida de honra paga com a chegada de dois milhões de combatentes americanos."
    },
    {
        "id": "FRA_armer_l_armee_americaine",
        "x": 98, "y": 9, "cost": 8,
        "icon": "GFX_FRA_armer_l_armee_americaine",
        "prereq": ["FRA_relations_financieres_avec_les_usa"], "mut": [],
        "reward": """add_political_power = 60
if = {
    limit = { country_exists = USA }
    USA = { country_event = { id = ww1_france.265 days = 1 } }
}""",
        "title_en": "Equipping the Doughboys with French Arms",
        "title_pt": "Equipando os Americanos com Armas Francesas",
        "desc_en": "Because US industry is slow to retool, French arsenals supply American divisions with 3,000 75mm guns, 250 heavy howitzers, 40,000 Chauchat rifles, and 300 Renault FT tanks.",
        "desc_pt": "Como a indústria dos EUA demora a produzir armamento pesado, as usinas francesas fornecem 3.000 canhões de 75mm, fuzis Chauchat e tanques Renault FT para a AEF."
    },
    {
        "id": "FRA_instruction_militaire_des_doughboys",
        "x": 98, "y": 10, "cost": 8,
        "icon": "GFX_FRA_instruction_militaire_des_doughboys",
        "prereq": ["FRA_armer_l_armee_americaine"], "mut": [],
        "reward": """add_command_power = 30
add_ideas = FRA_joint_franco_american_staff""",
        "title_en": "French Officer Training for US Troops",
        "title_pt": "Instrução Francesa para as Divisões dos EUA",
        "desc_en": "French veteran officers and NCOs instruct newly arrived American divisions in gas warfare, hand grenade tactics, crawling under wire, and trench raid methods.",
        "desc_pt": "Veteranos e oficiais franceses treinam as tropas americanas em combate com máscaras de gás, lançamento de granadas de mão e ataques de trincheira na floresta de Argonne."
    },

    # Y = 11 (Armistice & Versailles)
    {
        "id": "FRA_le_wagon_de_rethondes_a_compiegne",
        "x": 90, "y": 11, "cost": 5,
        "icon": "GFX_FRA_le_wagon_de_rethondes_a_compiegne",
        "prereq": ["FRA_arrivee_du_corps_expeditionnaire_americain", "FRA_offensive_du_vardar_franchet_d_esperey"], "mut": [],
        "reward": """country_event = { id = ww1_france.270 days = 1 }
add_political_power = 100
add_war_support = 0.10""",
        "title_en": "The Armistice at Compiègne (Rethondes)",
        "title_pt": "O Armistício de Compiègne (Rethondes)",
        "desc_en": "On 11 November 1918 in Marshal Foch's railway coach in the forest of Compiègne, the German delegation signs the unconditional cessation of hostilities at the eleventh hour.",
        "desc_pt": "Em 11 de novembro de 1918, no vagão ferroviário de Foch na floresta de Compiègne, a delegação alemã assina o armistício na décima primeira hora, selando a vitória."
    },
    {
        "id": "FRA_retour_de_l_alsace_lorraine",
        "x": 94, "y": 11, "cost": 8,
        "icon": "GFX_FRA_retour_de_l_alsace_lorraine",
        "prereq": ["FRA_le_wagon_de_rethondes_a_compiegne"], "mut": [],
        "reward": """swap_ideas = {
    remove_idea = FRA_wound_of_1870
    add_idea = FRA_alsace_lorraine_reclaimed
}
add_stability = 0.10
add_political_power = 80""",
        "title_en": "Return of the Lost Daughters: Alsace-Lorraine",
        "title_pt": "O Retorno da Alsácia-Lorena",
        "desc_en": "After forty-seven years of sorrow, French troops march into Strasbourg and Metz amid tears of joy. The black veil is lifted from the statue of Strasbourg on Place de la Concorde.",
        "desc_pt": "Após 47 anos de luto, tropas francesas entram em Estrasburgo e Metz sob lágrimas de alegria. O véu negro é retirado da estátua de Estrasburgo na Place de la Concorde."
    },
    {
        "id": "FRA_la_paix_de_versailles_imposition",
        "x": 98, "y": 11, "cost": 10,
        "icon": "GFX_FRA_la_paix_de_versailles_imposition",
        "prereq": ["FRA_retour_de_l_alsace_lorraine"], "mut": [],
        "reward": """country_event = { id = ww1_france.271 days = 1 }
add_political_power = 100
add_stability = 0.10
add_ideas = FRA_versailles_supreme_guarantor""",
        "title_en": "The Treaty of Versailles in the Hall of Mirrors",
        "title_pt": "O Tratado de Versalhes na Galeria dos Espelhos",
        "desc_en": "On 28 June 1919 in the very hall where the German Empire was proclaimed in 1871, Georges Clemenceau presides over the signing of the Treaty of Versailles, securing French triumph.",
        "desc_pt": "Em 28 de junho de 1919, no mesmo salão onde o Império Alemão fora proclamado em 1871, Georges Clemenceau preside a assinatura da Paz de Versalhes, consagrando o triunfo da França."
    }
]
