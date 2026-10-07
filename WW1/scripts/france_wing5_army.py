# -*- coding: utf-8 -*-
"""France Wing 5: Armée de Terre, GQG & Grandes Doutrinas (35 focuses).
X range: 62 .. 78 | Y range: 0 .. 12
Flattened from Y=28 to Y<=12 through 3 parallel operational tracks:
Track A: Doutrina & Comando (X: 62 .. 66)
Track B: Tecnologia, Trincheiras & Blindados (X: 68 .. 72)
Track C: Campanhas Operacionais & Missões (X: 74 .. 78)
"""

WING5_FOCI = [
    # --- TRACK A: DOUTRINA & COMANDO (X: 62..66) ---
    {
        "id": "FRA_grand_quartier_general",
        "x": 64, "y": 0, "cost": 10,
        "icon": "GFX_FRA_grand_quartier_general",
        "prereq": [], "mut": [],
        "reward": """add_political_power = 40
add_army_experience = 25
add_command_power = 25""",
        "title_en": "Grand Quartier Général (GQG)",
        "title_pt": "Grand Quartier Général (GQG)",
        "desc_en": "Establishing the supreme military headquarters in Chantilly unifies operational command, communications, intelligence, and logistical movement across all French field armies.",
        "desc_pt": "O estabelecimento do quartel-general supremo em Chantilly unifica o comando operacional, inteligência e comunicações de todas as armadas francesas de campanha."
    },
    {
        "id": "FRA_general_joffre_chef_d_etat_major",
        "x": 62, "y": 1, "cost": 8,
        "icon": "GFX_FRA_general_joffre_chef_d_etat_major",
        "prereq": ["FRA_grand_quartier_general"], "mut": [],
        "reward": """add_ideas = FRA_joffre_supreme_staff
add_command_power = 20""",
        "title_en": "General Joffre's Staff Centralisation",
        "title_pt": "Centralização do Estado-Maior de Joffre",
        "desc_en": "General Joseph Joffre imposes imperturbable calm, weeding out political favorites and appointing capable tacticians to lead army corps regardless of faction.",
        "desc_pt": "O General Joseph Joffre impõe calma inabalável, afastando oficiais incompetentes e promovendo comandantes capazes com rigor e disciplina profissional."
    },
    {
        "id": "FRA_culte_de_l_offensive_a_outrance",
        "x": 66, "y": 1, "cost": 8,
        "icon": "GFX_FRA_culte_de_l_offensive_a_outrance",
        "prereq": ["FRA_grand_quartier_general"], "mut": [],
        "reward": """add_ideas = FRA_offensive_school
add_army_experience = 15""",
        "title_en": "Doctrine of 'Offensive à Outrance'",
        "title_pt": "Doutrina da 'Offensive à Outrance'",
        "desc_en": "Influenced by Colonel de Grandmaison, the École de Guerre preaches that sheer morale, cold steel, and fierce bayonet charges will conquer all enemy fire.",
        "desc_pt": "Influenciada pelo Coronel de Grandmaison, a Escola de Guerra prega que a moral ofensiva, o aço frio e cargas de baioneta decididas superarão todo fogo inimigo."
    },
    {
        "id": "FRA_lecons_sanglantes_des_frontieres",
        "x": 64, "y": 2, "cost": 8,
        "icon": "GFX_FRA_lecons_sanglantes_des_frontieres",
        "prereq": ["FRA_general_joffre_chef_d_etat_major", "FRA_culte_de_l_offensive_a_outrance"], "mut": [],
        "reward": """add_ideas = FRA_lessons_of_the_frontiers
add_army_experience = 20""",
        "title_en": "Bloody Lessons of the Frontiers",
        "title_pt": "Lições Sangrentas das Fronteiras",
        "desc_en": "Suffering twenty-seven thousand casualties in a single day at Rossignol shatters obsolete dogma: machine guns and shrapnel kill blind heroism. Tactical reality must prevail.",
        "desc_pt": "A perda de vinte e sete mil soldados em um único dia em Rossignol destrói os dogmas obsoletos: metralhadoras e estilhaços massacram o heroísmo cego."
    },
    {
        "id": "FRA_uniformes_horizon_bleu",
        "x": 64, "y": 3, "cost": 6,
        "icon": "GFX_FRA_uniformes_horizon_bleu",
        "prereq": ["FRA_lecons_sanglantes_des_frontieres"], "mut": [],
        "reward": """add_ideas = FRA_horizon_blue_uniforms_idea
add_stability = 0.03""",
        "title_en": "Adoption of 'Bleu Horizon' Uniforms",
        "title_pt": "Adoção dos Uniformes 'Azul-Horizonte'",
        "desc_en": "Discarding the deadly crimson red trousers ('pantalons rouges') that made French infantry easy targets, troops receive drab blue-grey camouflage suited to mud and chalk.",
        "desc_pt": "Abandonar os calções vermelhos brilhantes que tornavam os soldados alvos fáceis e vestir o azul-horizonte confere camuflagem essencial nas trincheiras."
    },
    {
        "id": "FRA_doctrine_petain_feu_et_materiel",
        "x": 64, "y": 6, "cost": 8,
        "icon": "GFX_FRA_doctrine_petain_feu_et_materiel",
        "prereq": ["FRA_uniformes_horizon_bleu"], "mut": [],
        "reward": """swap_ideas = {
    remove_idea = FRA_elan_vital_doctrine
    add_idea = FRA_firepower_doctrine
}
add_army_experience = 25""",
        "title_en": "Pétain's Doctrine: 'Firepower Kills'",
        "title_pt": "Doutrina de Pétain: 'O Fogo Conquista'",
        "desc_en": "'Firepower kills!' General Pétain's revolutionary motto replaces wasteful infantry charges with devastating artillery barrages, deep trench belts, and elastic defense.",
        "desc_pt": "'O fogo mata!' A máxima revolucionária de Pétain substitui ataques suicidas por barragens concentradas de artilharia pesada e defesa elástica em profundidade."
    },
    {
        "id": "FRA_crise_des_mutineries_1917",
        "x": 62, "y": 7, "cost": 6,
        "icon": "GFX_FRA_crise_des_mutineries_1917",
        "prereq": ["FRA_doctrine_petain_feu_et_materiel"], "mut": [],
        "reward": """country_event = { id = ww1_france.210 days = 1 }
add_ideas = FRA_trench_mutiny_crisis_2""",
        "title_en": "The 1917 Poilu Mutinies Crisis",
        "title_pt": "A Crise dos Motins dos Poilus de 1917",
        "desc_en": "Disillusioned by futile slaughter on the Chemin des Dames, half of all French combat divisions refuse suicidal attacks, singing the 'Chanson de Craonne'.",
        "desc_pt": "Desiludidos com o massacre inútil no Chemin des Dames, regimentos inteiros recusam ordens de ataque suicida, entoando a 'Chanson de Craonne'."
    },
    {
        "id": "FRA_petain_commandant_en_chef",
        "x": 64, "y": 8, "cost": 8,
        "icon": "GFX_FRA_petain_commandant_en_chef",
        "prereq": ["FRA_crise_des_mutineries_1917"], "mut": [],
        "reward": """add_ideas = FRA_petain_elastic_defense
add_political_power = 40""",
        "title_en": "Pétain Appointed Commander-in-Chief",
        "title_pt": "Pétain Nomeado Comandante-em-Chefe",
        "desc_en": "Replacing the reckless Nivelle, Philippe Pétain restores faith in high command by personally visiting over ninety divisions, promising no more butchery.",
        "desc_pt": "Substituindo o imprudente Nivelle, Philippe Pétain visita pessoalmente dezenas de divisões, prometendo o fim dos massacres e restaurando a confiança dos soldados."
    },
    {
        "id": "FRA_reforme_des_permissions_et_soupe",
        "x": 62, "y": 9, "cost": 6,
        "icon": "GFX_FRA_reforme_des_permissions_et_soupe",
        "prereq": ["FRA_petain_commandant_en_chef"], "mut": [],
        "reward": """remove_ideas = FRA_trench_mutiny_crisis_2
add_stability = 0.08
add_war_support = 0.05""",
        "title_en": "Trench Rest, Rations & Regular Leave",
        "title_pt": "Reformas de Licenças, Sopas Quentes e Vinho",
        "desc_en": "Pétain guarantees regular seven-day furloughs to families, cleans frontline canteens, and ensures hot soup and fresh wine reach the forward dugouts daily.",
        "desc_pt": "Pétain garante licenças regulares de sete dias para rever as famílias, limpa os alojamentos e assegura sopa quente e rações de vinho nas trincheiras."
    },
    {
        "id": "FRA_justice_militaire_mesuree",
        "x": 66, "y": 9, "cost": 6,
        "icon": "GFX_FRA_justice_militaire_mesuree",
        "prereq": ["FRA_petain_commandant_en_chef"], "mut": [],
        "reward": """add_stability = 0.05
add_political_power = 25""",
        "title_en": "Measured Military Justice & Pardons",
        "title_pt": "Justiça Militar Medida e Indultos",
        "desc_en": "Refusing draconian decimation demanded by reactionaries, Pétain pardons hundreds of condemned soldiers, executing only fifty-five ringleaders and quelling rebellion.",
        "desc_pt": "Recusando fuzilamentos em massa, Pétain comuta centenas de sentenças de morte, executando apenas líderes comprovados e pacificando o exército com moderação."
    },
    {
        "id": "FRA_ferdinand_foch_commandement_unique",
        "x": 64, "y": 11, "cost": 10,
        "icon": "GFX_FRA_ferdinand_foch_commandement_unique",
        "prereq": ["FRA_reforme_des_permissions_et_soupe", "FRA_justice_militaire_mesuree"], "mut": [],
        "reward": """add_ideas = FRA_supreme_allied_command
add_command_power = 50
add_army_experience = 30
add_political_power = 75
add_stability = 0.05
add_war_support = 0.05""",
        "title_en": "Foch: Supreme Allied Commander & Marshal",
        "title_pt": "Foch: Comando Único Aliado e Bastão de Marechal",
        "desc_en": "At Doullens in March 1918, General Ferdinand Foch is elevated to supreme commander over all Allied forces on the Western Front, receiving the baton of Maréchal de France for guiding the nation to victory.",
        "desc_pt": "Na conferência de Doullens em março de 1918, o General Ferdinand Foch é nomeado Generalíssimo de todas as forças aliadas na frente ocidental, recebendo o bastão de Marechal da França."
    },

    # --- TRACK B: TECNOLOGIA, TRINCHEIRAS & BLINDADOS (X: 68..72) ---
    {
        "id": "FRA_stabilisation_du_front_de_tranchees",
        "x": 70, "y": 2, "cost": 8,
        "icon": "GFX_FRA_stabilisation_du_front_de_tranchees",
        "prereq": ["FRA_grand_quartier_general"], "mut": [],
        "reward": """add_ideas = FRA_ww1_field_fortification
add_tech_bonus = { name = eng_tech bonus = 1.0 uses = 1 category = support_tech }""",
        "title_en": "Trench System Engineering",
        "title_pt": "Engenharia de Sistemas de Trincheiras",
        "desc_en": "From the Swiss border to the North Sea, sappers excavate three parallel defense lines with traverses, deep dugouts, parapets, and dense barbed-wire aprons.",
        "desc_pt": "Da Suíça ao Mar do Norte, os sapadores escavam três linhas paralelas com abrigos profundos, parapeitos e densas redes de arame farpado."
    },
    {
        "id": "FRA_canon_de_75mm_modele_1897",
        "x": 68, "y": 3, "cost": 8,
        "icon": "GFX_FRA_canon_de_75mm_modele_1897",
        "prereq": ["FRA_stabilisation_du_front_de_tranchees"], "mut": [],
        "reward": """swap_ideas = {
    remove_idea = FRA_canon_75mm_supremacy
    add_idea = FRA_balanced_siege_and_field_artillery
}
add_tech_bonus = { name = art_tech bonus = 1.0 uses = 1 category = artillery }""",
        "title_en": "75mm Mle 1897 Rapid-Fire Supremacy",
        "title_pt": "Supremacia do Canhão de 75mm Mle 1897",
        "desc_en": "Capable of firing fifteen aimed shrapnel shells per minute without re-aiming, the French 75 remains the undisputed king of field artillery.",
        "desc_pt": "Capaz de disparar quinze obuses por minuto sem sair do ponto de mira graças ao freio hidropneumático, o canhão de 75mm reina supremo nos campos."
    },
    {
        "id": "FRA_adopter_le_casque_adrian_m1915",
        "x": 72, "y": 3, "cost": 6,
        "icon": "GFX_FRA_adopter_le_casque_adrian_m1915",
        "prereq": ["FRA_stabilisation_du_front_de_tranchees"], "mut": [],
        "reward": """add_ideas = FRA_adrian_helmet_protection
add_army_experience = 15""",
        "title_en": "Adoption of the Adrian M1915 Helmet",
        "title_pt": "Adoção do Capacete Adrian M1915",
        "desc_en": "Designed by Intendant Louis Adrian, the pressed-steel crested helmet cuts head wounds and shell-splinter casualties among frontline poilus by over two-thirds.",
        "desc_pt": "Projetado por Louis Adrian, o capacete de aço estampado com crista reduz as baixas por estilhaços na cabeça em mais de dois terços entre os poilus."
    },
    {
        "id": "FRA_mortiers_de_tranchee_crapouillots",
        "x": 68, "y": 4, "cost": 6,
        "icon": "GFX_FRA_mortiers_de_tranchee_crapouillots",
        "prereq": ["FRA_canon_de_75mm_modele_1897"], "mut": [],
        "reward": """add_tech_bonus = { name = support_art bonus = 1.0 uses = 1 category = artillery }
add_army_experience = 15""",
        "title_en": "'Crapouillot' Trench Mortars",
        "title_pt": "Morteiros de Trincheira 'Crapouillots'",
        "desc_en": "Improvised from old bronze fortress mortars, 'crapouillots' lob high-trajectory aerial torpedoes directly into enemy traverses, blowing apart barbed-wire entanglements.",
        "desc_pt": "Apelidados de 'crapouillots', esses morteiros de tiro curvo lançam torpedos aéreos dentro dos parapeitos inimigos, pulverizando ninhos de metralhadoras."
    },
    {
        "id": "FRA_parc_d_artillerie_lourde_rimailho",
        "x": 72, "y": 4, "cost": 8,
        "icon": "GFX_FRA_parc_d_artillerie_lourde_rimailho",
        "prereq": ["FRA_adopter_le_casque_adrian_m1915"], "mut": [],
        "reward": """add_tech_bonus = { name = heavy_art bonus = 1.0 uses = 2 category = artillery }
27 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "Heavy Artillery Expansion (Schneider 155mm)",
        "title_pt": "Expansão de Artilharia Pesada (Schneider 155mm)",
        "desc_en": "Rectifying prewar blindness, massive orders of 155mm Schneider short howitzers and 220mm siege mortars give the army crushing counter-battery punch.",
        "desc_pt": "Corrigindo as deficiências pré-guerra, encomendas maciças de obuses Schneider de 155mm e morteiros de 220mm conferem poder esmagador de contra-bateria."
    },
    {
        "id": "FRA_fusil_mitrailleur_chauchat",
        "x": 70, "y": 5, "cost": 6,
        "icon": "GFX_FRA_fusil_mitrailleur_chauchat",
        "prereq": ["FRA_mortiers_de_tranchee_crapouillots", "FRA_parc_d_artillerie_lourde_rimailho"], "mut": [],
        "reward": """add_tech_bonus = { name = infantry_weapons bonus = 1.0 uses = 1 category = infantry_weapons }
add_ideas = FRA_light_machinegun_fireteams""",
        "title_en": "Chauchat CSRG Light Automatic Rifle",
        "title_pt": "Fuzil-Metralhadora Leve Chauchat CSRG",
        "desc_en": "Mass-produced from stamped sheet metal, the Chauchat equips every infantry combat squad with marching fire capacity, supporting attacks with mobile automatic bursts.",
        "desc_pt": "Estampado em chapas de aço, o Chauchat equipa cada pelotão de infantaria com fogo automático móvel, apoiando assaltos a trincheiras."
    },
    {
        "id": "FRA_canons_sur_voie_ferree_alvf",
        "x": 68, "y": 6, "cost": 8,
        "icon": "GFX_FRA_canons_sur_voie_ferree_alvf",
        "prereq": ["FRA_fusil_mitrailleur_chauchat"], "mut": [],
        "reward": """add_tech_bonus = { name = railway_gun bonus = 1.0 uses = 1 category = artillery }
add_ideas = FRA_railway_super_heavy_artillery""",
        "title_en": "ALVF Railway Super-Heavy Siege Guns",
        "title_pt": "Artilharia Pesada sobre Trilhos (ALVF)",
        "desc_en": "Mounting 320mm and 400mm naval barrels onto specialized railroad carriages allows pulverizing deep reinforced concrete bunkers from twenty miles away.",
        "desc_pt": "Canhões de 320mm e 400mm instalados sobre vagões ferroviários especiais pulverizam casamatas de concreto armado e túneis inimigos a dezenas de quilômetros."
    },
    {
        "id": "FRA_developpement_des_chars_d_assaut",
        "x": 70, "y": 7, "cost": 8,
        "icon": "GFX_FRA_developpement_des_chars_d_assaut",
        "prereq": ["FRA_fusil_mitrailleur_chauchat"], "mut": [],
        "reward": """add_tech_bonus = { name = armor_bonus bonus = 1.0 uses = 1 category = armor }
add_ideas = FRA_artillerie_speciale_cadres""",
        "title_en": "Colonel Estienne & 'Artillerie Spéciale'",
        "title_pt": "Coronel Estienne e a 'Artillerie Spéciale'",
        "desc_en": "'Victory will belong to whoever puts a gun on a caterpillar track first,' writes Jean-Baptiste Estienne, founding the French armored combat branch.",
        "desc_pt": "'A vitória pertencerá àquele que primeiro colocar um canhão sobre esteiras', preconiza o Coronel Estienne, fundando os blindados franceses."
    },
    {
        "id": "FRA_chars_schneider_ca1_et_saint_chamond",
        "x": 68, "y": 8, "cost": 8,
        "icon": "GFX_FRA_chars_schneider_ca1_et_saint_chamond",
        "prereq": ["FRA_developpement_des_chars_d_assaut"], "mut": [],
        "reward": """add_tech_bonus = { name = heavy_armor bonus = 1.0 uses = 1 category = armor }
add_army_experience = 20""",
        "title_en": "Schneider CA1 & Saint-Chamond Assault Tanks",
        "title_pt": "Carros de Combate Schneider CA1 e Saint-Chamond",
        "desc_en": "The first French armored vehicles surmount trenches with forward trench-cutting bows and short 75mm guns, testing armored warfare at Berry-au-Bac.",
        "desc_pt": "Os primeiros tanques franceses transpõem trincheiras e cortam arames farpados com canhões de 75mm, estreados em combate em Berry-au-Bac."
    },
    {
        "id": "FRA_char_leger_renault_ft",
        "x": 70, "y": 9, "cost": 10,
        "icon": "GFX_FRA_char_leger_renault_ft",
        "prereq": ["FRA_developpement_des_chars_d_assaut"], "mut": [],
        "reward": """add_tech_bonus = { name = light_armor bonus = 1.0 uses = 2 category = armor }
add_ideas = FRA_renault_ft_revolution
16 = { add_building_construction = { type = arms_factory level = 1 instant_build = yes } }""",
        "title_en": "The Revolutionary Renault FT-17",
        "title_pt": "O Revolucionário Tanque Renault FT-17",
        "desc_en": "Engineered by Louis Renault and Estienne, the FT-17 invents modern tank layout: engine in back, driver in front, and a fully rotating 360-degree top turret.",
        "desc_pt": "Criado por Louis Renault e Estienne, o FT-17 define o layout clássico de todos os blindados do futuro: motor atrás, piloto à frente e torre giratória de 360 graus."
    },
    {
        "id": "FRA_doctrine_d_emploi_des_blindes_estienne",
        "x": 72, "y": 10, "cost": 8,
        "icon": "GFX_FRA_doctrine_d_emploi_des_blindes_estienne",
        "prereq": ["FRA_char_leger_renault_ft"], "mut": [],
        "reward": """add_ideas = FRA_mass_swarm_tank_tactics
add_army_experience = 25""",
        "title_en": "Estienne's Swarm Armor Doctrine",
        "title_pt": "Doutrina de Enxame de Blindados de Estienne",
        "desc_en": "Instead of lone leviathans, France deploys thousands of small, agile FT-17 tanks operating in tight swarms with infantry and artillery, overwhelming trench lines.",
        "desc_pt": "Em vez de monstros isolados, a França emprega milhares de tanques FT-17 ágeis avançando em enxames cerrados com a infantaria para quebrar as linhas alemãs."
    },
    {
        "id": "FRA_armee_moderne_motorisee",
        "x": 70, "y": 11, "cost": 8,
        "icon": "GFX_FRA_armee_moderne_motorisee",
        "prereq": ["FRA_doctrine_d_emploi_des_blindes_estienne"], "mut": [],
        "reward": """add_ideas = FRA_fully_motorised_logistics
add_army_experience = 20""",
        "title_en": "Fully Motorised Combined-Arms Army",
        "title_pt": "Exército Motorizado de Armas Combinadas",
        "desc_en": "With forty thousand Renault and Peugeot trucks hauling supplies, French mechanized logistical muscle outpaces rail reliance, sealing tactical breakthroughs.",
        "desc_pt": "Com mais de quarenta mil caminhões Renault e Peugeot transportando homens e munições, o exército francês atinge mobilidade incomparável na frente."
    },

    # --- TRACK C: CAMPANHAS OPERACIONAIS & MISSÕES (X: 74..78) ---
    {
        "id": "FRA_adoption_du_plan_xvii",
        "x": 76, "y": 1, "cost": 8,
        "icon": "GFX_FRA_adoption_du_plan_xvii",
        "prereq": ["FRA_grand_quartier_general"], "mut": [],
        "reward": """add_ideas = FRA_plan_xvii_concentration
add_command_power = 25""",
        "title_en": "Deployment of Plan XVII",
        "title_pt": "Desdobramento do Plano XVII",
        "desc_en": "Concentrating five field armies along the eastern frontier from Belfort to Mézières prepares a massive head-on drive into recovered Alsace and Lorraine.",
        "desc_pt": "A concentração de cinco exércitos na fronteira oriental de Belfort a Mézières prepara uma ofensiva direta para recuperar a Alsácia e a Lorena."
    },
    {
        "id": "FRA_reseau_de_forts_sere_de_rivieres",
        "x": 74, "y": 2, "cost": 8,
        "icon": "GFX_FRA_reseau_de_forts_sere_de_rivieres",
        "prereq": ["FRA_adoption_du_plan_xvii"], "mut": [],
        "reward": """18 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }
17 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }""",
        "title_en": "Séré de Rivières Fortress System",
        "title_pt": "Cadeia de Fortalezas Séré de Rivières",
        "desc_en": "The fortified barrier camps of Verdun, Toul, Épinal, and Belfort funnel any German invasion into prepared killing corridors along the Meuse and Moselle.",
        "desc_pt": "As fortalezas de Verdun, Toul, Épinal e Belfort canalizam as invasões alemãs para zonas de aniquilação preparadas ao longo do Mosa e Mosela."
    },
    {
        "id": "FRA_bataille_des_frontieres",
        "x": 76, "y": 3, "cost": 6,
        "icon": "GFX_FRA_bataille_des_frontieres",
        "prereq": ["FRA_adoption_du_plan_xvii"], "mut": [],
        "reward": """add_army_experience = 20
add_war_support = 0.05""",
        "title_en": "Battle of the Frontiers (August 1914)",
        "title_pt": "Batalha das Fronteiras (Agosto de 1914)",
        "desc_en": "Over two million men clash in the Ardennes, Charleroi, and Morhange in the largest opening clash in human history, meeting German flanking armies head-on.",
        "desc_pt": "Mais de dois milhões de homens colidem nas Ardenas, Charleroi e Morhange no maior choque militar de abertura da história contra os exércitos alemães."
    },
    {
        "id": "FRA_operation_de_la_marne",
        "x": 76, "y": 4, "cost": 8,
        "icon": "GFX_FRA_operation_de_la_marne",
        "prereq": ["FRA_bataille_des_frontieres"], "mut": [],
        "reward": """add_ideas = FRA_miracle_of_the_marne
add_stability = 0.08
add_war_support = 0.08""",
        "title_en": "Miracle of the Marne & Gallieni's Taxis",
        "title_pt": "O Milagre do Marne e os Táxis de Gallieni",
        "desc_en": "General Gallieni requisitions Parisian taxis to rush the 7th Division to the Ourcq. Joffre strikes Von Kluck's exposed flank, saving Paris and repelling the invader.",
        "desc_pt": "O General Gallieni requisita os táxis de Paris para lançar reservas sobre o Ourcq. Joffre golpeia o flanco exposto de Von Kluck, salvando Paris."
    },
    {
        "id": "FRA_la_course_a_la_mer",
        "x": 76, "y": 5, "cost": 6,
        "icon": "GFX_FRA_la_course_a_la_mer",
        "prereq": ["FRA_operation_de_la_marne"], "mut": [],
        "reward": """add_ideas = FRA_race_to_the_sea_entrenchment
29 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }""",
        "title_en": "The Race to the Sea (Flanders Front)",
        "title_pt": "A Corrida para o Mar (Frente de Flandres)",
        "desc_en": "Both armies race northwards in furious flanking attempts, ending when French marines, Belgians at the Yser, and the BEF seal the front at the English Channel.",
        "desc_pt": "Ambos os exércitos manobram para o norte tentando flanquear-se, até que fuzileiros franceses e belgas selam o front junto ao Canal da Mancha."
    },
    {
        "id": "FRA_la_fournaise_de_verdun",
        "x": 76, "y": 6, "cost": 8,
        "icon": "GFX_FRA_la_fournaise_de_verdun",
        "prereq": ["FRA_la_course_a_la_mer"], "mut": [],
        "reward": """activate_mission = FRA_verdun_resilience_mission
add_timed_idea = { idea = FRA_verdun_resilience days = 45 }
add_war_support = 0.08""",
        "title_en": "The Furnace of Verdun: 'Ils ne passeront pas!'",
        "title_pt": "A Fornalha de Verdun: 'Eles Não Passarão!'",
        "desc_en": "'They shall not pass!' Facing Falkenhayn's meatgrinder offensive, the French army stands firm on the hills of Douaumont and Vaux in a test of national will.",
        "desc_pt": "'Eles não passarão!' Enfrentando a ofensiva de atrito de Falkenhayn, o exército francês resiste inabalável nas colinas de Douaumont e Vaux."
    },
    {
        "id": "FRA_organisation_de_la_voie_sacree",
        "x": 74, "y": 7, "cost": 6,
        "icon": "GFX_FRA_organisation_de_la_voie_sacree",
        "prereq": ["FRA_la_fournaise_de_verdun"], "mut": [],
        "reward": """add_ideas = FRA_la_voie_sacree_convoy
18 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }""",
        "title_en": "La Voie Sacrée (The Sacred Road)",
        "title_pt": "La Voie Sacrée (A Via Sagrada)",
        "desc_en": "Three thousand trucks run bumper-to-bumper 24 hours a day along the Bar-le-Duc artery, carrying 50,000 tonnes of ammunition and 90,000 men weekly into Verdun.",
        "desc_pt": "Três mil caminhões operam dia e noite na artéria Bar-le-Duc-Verdun, transportando cinquenta mil toneladas de projéteis e noventa mil soldados semanalmente."
    },
    {
        "id": "FRA_rotation_de_la_noria_petain",
        "x": 78, "y": 7, "cost": 6,
        "icon": "GFX_FRA_rotation_de_la_noria_petain",
        "prereq": ["FRA_la_fournaise_de_verdun"], "mut": [],
        "reward": """add_ideas = FRA_ww1_division_rotation
add_stability = 0.04""",
        "title_en": "Pétain's 'Noria' Division Rotation",
        "title_pt": "O Sistema da 'Noria' de Pétain",
        "desc_en": "Instead of leaving units to be bled dry in the line, seventy out of ninety-five French divisions rotate through Verdun for brief, intense stints before relief.",
        "desc_pt": "Em vez de deixar divisões serem aniquiladas no front, setenta divisões francesas revezam-se em turnos de alta intensidade antes de serem poupadas."
    },
    {
        "id": "FRA_la_bataille_de_la_somme_soutien",
        "x": 76, "y": 8, "cost": 8,
        "icon": "GFX_FRA_la_bataille_de_la_somme_soutien",
        "prereq": ["FRA_organisation_de_la_voie_sacree", "FRA_rotation_de_la_noria_petain"], "mut": [],
        "reward": """add_ideas = FRA_somme_artillery_coordination
add_army_experience = 20""",
        "title_en": "Battle of the Somme (French 6th Army)",
        "title_pt": "Batalha do Somme (6º Exército Francês)",
        "desc_en": "South of the Somme river, General Fayolle's 6th Army achieves remarkable tactical gains with creeping artillery barrages, relieving intense pressure on Verdun.",
        "desc_pt": "Ao sul do Somme, o 6º Exército do General Fayolle avança com barragens de artilharia rolante, aliviando de forma decisiva a pressão sobre Verdun."
    },
    {
        "id": "FRA_offensive_nivelle_chemin_des_dames",
        "x": 76, "y": 9, "cost": 6,
        "icon": "GFX_FRA_offensive_nivelle_chemin_des_dames",
        "prereq": ["FRA_la_bataille_de_la_somme_soutien"], "mut": [],
        "reward": """activate_mission = FRA_nivelle_offensive_mission
add_timed_idea = { idea = FRA_nivelle_offensive_surge days = 30 }""",
        "title_en": "The Nivelle Offensive at Chemin des Dames",
        "title_pt": "A Ofensiva Nivelle no Chemin des Dames",
        "desc_en": "General Robert Nivelle promises rupture in forty-eight hours. The bloody assault against fortified ridges in April 1917 triggers a moral reckoning.",
        "desc_pt": "O General Robert Nivelle promete a ruptura em 48 horas. O sangrento assalto às cristas fortificadas em abril de 1917 precipita um choque moral profundo."
    },
    {
        "id": "FRA_arret_des_offensives_ludendorff",
        "x": 74, "y": 10, "cost": 8,
        "icon": "GFX_FRA_arret_des_offensives_ludendorff",
        "prereq": ["FRA_offensive_nivelle_chemin_des_dames"], "mut": [],
        "reward": """add_ideas = FRA_kaiser_offensive_halted
add_war_support = 0.08
add_stability = 0.05""",
        "title_en": "Halting Ludendorff's 1918 Spring Offensives",
        "title_pt": "Contenção das Ofensivas Ludendorff de 1918",
        "desc_en": "Absorbing the shock of German Sturmtruppen on the Matz and the Marne, French counter-attacks at Villers-Cotterêts in July 1918 turn the tide of the war forever.",
        "desc_pt": "Absorvendo o choque das tropas de assalto alemãs no Marne, o contra-ataque de Villers-Cotterêts em julho de 1918 vira definitivamente a maré da guerra."
    },
    {
        "id": "FRA_offensive_des_cent_jours",
        "x": 76, "y": 11, "cost": 10,
        "icon": "GFX_FRA_offensive_des_cent_jours",
        "prereq": ["FRA_arret_des_offensives_ludendorff", "FRA_char_leger_renault_ft"], "mut": [],
        "reward": """activate_mission = FRA_cent_jours_final_offensive
add_timed_idea = { idea = FRA_cent_jours_combined_arms days = 45 }
add_war_support = 0.10""",
        "title_en": "Foch's Grand Hundred Days Offensive",
        "title_pt": "A Grande Ofensiva dos Cem Dias de Foch",
        "desc_en": "'Everyone to battle!' Foch unleashes continuous, synchronized attacks along the entire Western Front with tanks, airplanes, and infantry, breaking the Hindenburg Line.",
        "desc_pt": "'Todos à batalha!' Foch desfere ataques sincronizados por toda a frente com tanques, aviões e artilharia pesada, despedaçando a Linha Hindenburg."
    }
]
