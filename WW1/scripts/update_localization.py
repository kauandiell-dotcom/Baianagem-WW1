import os

# 1. Update English focus localization
with open('localisation/english/ww1_germany_focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    en_content = f.read()

en_additions = '''
 # 4 New Historical Kaiser Focuses & Mechanics
 GER_septemberprogramm_war_aims:0 "[Historical] Septemberprogramm War Aims"
 GER_septemberprogramm_war_aims_desc:0 "Drafted by Chancellor von Bethmann-Hollweg and the General Staff, the Septemberprogramm outlines Germany's grand strategic vision: securing Mitteleuropa through economic hegemony, territorial annexations in the East, and ending French and Belgian ability to menace the Fatherland."
 GER_total_war_patriotism_kriegsanleihen:0 "[Historical] Imperial War Loans (Kriegsanleihen)"
 GER_total_war_patriotism_kriegsanleihen_desc:0 "To finance the colossal expenditure of global industrial warfare, the Reichsbank launches nationwide Kriegsanleihen subscription campaigns. Millions of patriotic citizens invest their life savings directly into victory."
 GER_hohenzollern_imperial_hegemony:0 "[Historical] Hohenzollern Imperial Hegemony"
 GER_hohenzollern_imperial_hegemony_desc:0 "Consolidating absolute imperial authority, the Hohenzollern dynasty stands undefeated at the apex of European civilization. With military triumph guaranteed, the Kaiserreich establishes an enduring continental Pax Germanica."
 GER_secret_ottoman_alliance_august_1914:0 "[Historical] Secret Ottoman-German Alliance"
 GER_secret_ottoman_alliance_august_1914_desc:0 "On August 2, 1914, Ambassador Wangenheim and Grand Vizier Said Halim Pasha seal a secret military alliance in Constantinople. The Ottoman Empire pledges to stand firmly beside the Central Powers against Russia."
 ger_septemberprogramm_tt:0 "Formalizes Imperial war aims to establish political and economic hegemony across Central Europe."
 GER_kriegsanleihen_war_loans:0 "Kriegsanleihen War Bonds"
 GER_kriegsanleihen_war_loans_desc:0 "State war bonds subscribed by millions of patriotic German citizens fund ammunition, heavy artillery, and naval production."
 GER_volkskaiserreich_constitution:0 "Volkskaiserreich Constitution"
 GER_volkskaiserreich_constitution_desc:0 "Constitutional parliamentary reforms subordinate the military command to the elected Reichstag, uniting the social classes under a democratic constitutional monarchy."
 creeping_barrage_idea:0 "Creeping Barrage Tactics"
 creeping_barrage_idea_desc:0 "A carefully timed moving wall of artillery shells suppresses enemy defenders right ahead of advancing infantry assaults."
'''

en_content = en_content.replace('GER_execute_schlieffen_plan: "Execute the Schlieffen Plan"', 'GER_execute_schlieffen_plan: "[Historical] Execute the Schlieffen Plan"')
en_content = en_content.replace('GER_aufmarsch_ost_focus: "Aufmarsch II Ost"', 'GER_aufmarsch_ost_focus: "[Alternative] Aufmarsch II Ost (Eastern Focus)"')
en_content = en_content.replace('GER_silent_dictatorship_ohl: "Silent Military Dictatorship"', 'GER_silent_dictatorship_ohl: "[Historical] Silent Military Dictatorship (OHL)"')
en_content = en_content.replace('GER_bethmann_civilian_supremacy: "Civilian Parliamentary Supremacy"', 'GER_bethmann_civilian_supremacy: "[Alternative - Democratic] Civilian Parliamentary Supremacy"')
en_content = en_content.replace('GER_found_vaterlandspartei: "Found the Deutsche Vaterlandspartei"', 'GER_found_vaterlandspartei: "[Alternative - Nationalist] Found the Deutsche Vaterlandspartei"')
en_content = en_content.replace('GER_willy_nicky_telegrams_bjorko: "Willy-Nicky Telegrams: Björkö 2.0"', 'GER_willy_nicky_telegrams_bjorko: "[Alternative - Diplomacy] Willy-Nicky Telegrams: Björkö 2.0"')
en_content = en_content.replace('GER_spartakusbund_proletarian_revolt: "Spartakusbund Proletarian Revolt"', 'GER_spartakusbund_proletarian_revolt: "[Alternative - Socialist] Spartakusbund Proletarian Revolt"')

if 'GER_septemberprogramm_war_aims' not in en_content:
    en_content += en_additions

with open('localisation/english/ww1_germany_focus_l_english.yml', 'w', encoding='utf-8-sig') as f:
    f.write(en_content)

print('Updated English Focus Localisation.')

# 2. Update Portuguese focus localization
with open('localisation/braz_por/ww1_germany_focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    pt_content = f.read()

pt_additions = '''
 # 4 Novos Focos Históricos do Kaiser & Mecânicas
 GER_septemberprogramm_war_aims:0 "[Histórico] Metas de Guerra do Septemberprogramm"
 GER_septemberprogramm_war_aims_desc:0 "Elaborado pelo Chanceler von Bethmann-Hollweg e pelo Estado-Maior, o Septemberprogramm traça os objetivos supremos do Reich: estabelecer a hegemonia econômica na Mitteleuropa, anexações estratégicas no Leste e neutralizar a capacidade da França e da Bélgica de ameaçarem o solo germânico."
 GER_total_war_patriotism_kriegsanleihen:0 "[Histórico] Títulos de Guerra Imperiais (Kriegsanleihen)"
 GER_total_war_patriotism_kriegsanleihen_desc:0 "Para financiar os custos monumentais da guerra moderna, o Reichsbank lança campanhas públicas de emissão de títulos de guerra (Kriegsanleihen). Milhões de cidadãos investem suas poupanças para abastecer a máquina bélica do Reich."
 GER_hohenzollern_imperial_hegemony:0 "[Histórico] Hegemonia Imperial dos Hohenzollern"
 GER_hohenzollern_imperial_hegemony_desc:0 "Consolidando a autoridade suprema da coroa imperial, a dinastia Hohenzollern lidera o destino do continente. Sob a liderança do Kaiser e a bravura do exército, a Alemanha assegura uma duradoura Pax Germanica."
 GER_secret_ottoman_alliance_august_1914:0 "[Histórico] Aliança Secreta Germano-Otomana"
 GER_secret_ottoman_alliance_august_1914_desc:0 "Em 2 de agosto de 1914, o Embaixador Wangenheim e o Grão-Vizir Said Halim Paxá selam uma aliança militar secreta em Constantinopla. O Império Otomano assume o compromisso de combater ao lado das Potências Centrais contra a Rússia."
 ger_septemberprogramm_tt:0 "Formaliza as metas de guerra imperiais para assegurar a hegemonia política e econômica na Mitteleuropa."
 GER_kriegsanleihen_war_loans:0 "Títulos de Guerra Kriegsanleihen"
 GER_kriegsanleihen_war_loans_desc:0 "Títulos da dívida de guerra subscritos por milhões de cidadãos patriotas financiam a compra de munições, artilharia pesada e navios."
 GER_volkskaiserreich_constitution:0 "Constituição da Volkskaiserreich"
 GER_volkskaiserreich_constitution_desc:0 "As reformas parlamentares constitucionais subordinam o comando militar ao Reichstag eleito, unindo as classes sociais sob uma monarquia democrática moderna."
 creeping_barrage_idea:0 "Táticas de Barragem Rolante"
 creeping_barrage_idea_desc:0 "Uma cortina de projéteis de artilharia sincronizada avança à frente das vagas de infantaria, esmagando os ninhos de metralhadora inimigos."
'''

pt_content = pt_content.replace('GER_execute_schlieffen_plan: "Executar o Plano Schlieffen"', 'GER_execute_schlieffen_plan: "[Histórico] Executar o Plano Schlieffen"')
pt_content = pt_content.replace('GER_aufmarsch_ost_focus: "Aufmarsch II Ost (Ofensiva no Leste)"', 'GER_aufmarsch_ost_focus: "[Alternativo] Aufmarsch II Ost (Ofensiva no Leste)"')
pt_content = pt_content.replace('GER_silent_dictatorship_ohl: "A Ditadura Silenciosa da OHL"', 'GER_silent_dictatorship_ohl: "[Histórico] A Ditadura Silenciosa da OHL"')
pt_content = pt_content.replace('GER_bethmann_civilian_supremacy: "Supremacia Civil da Chancelaria"', 'GER_bethmann_civilian_supremacy: "[Alternativo - Democrático] Supremacia Civil da Chancelaria"')
pt_content = pt_content.replace('GER_found_vaterlandspartei: "Fundação do Partido da Pátria Alemã"', 'GER_found_vaterlandspartei: "[Alternativo - Nacionalista] Fundação do Partido da Pátria Alemã"')
pt_content = pt_content.replace('GER_willy_nicky_telegrams_bjorko: "Telegramas Willy-Nicky: Björkö 2.0"', 'GER_willy_nicky_telegrams_bjorko: "[Alternativo - Diplomacia] Telegramas Willy-Nicky: Björkö 2.0"')
pt_content = pt_content.replace('GER_spartakusbund_proletarian_revolt: "A Revolta Proletária Espartaquista"', 'GER_spartakusbund_proletarian_revolt: "[Alternativo - Socialista] A Revolta Proletária Espartaquista"')

if 'GER_septemberprogramm_war_aims' not in pt_content:
    pt_content += pt_additions

with open('localisation/braz_por/ww1_germany_focus_l_braz_por.yml', 'w', encoding='utf-8-sig') as f:
    f.write(pt_content)

print('Updated Portuguese Focus Localisation.')

# 3. Append missing mechanics & national modifiers to braz_por
with open('localisation/braz_por/ww1_mechanics_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    mech_pt = f.read()

pt_mechanics_additions = '''
 # =======================================================
 # ESPÍRITOS NACIONAIS & MODIFICADORES WW1
 # =======================================================
 ENG_two_power_standard:0 "Padrão Naval de Duas Potências"
 ENG_two_power_standard_desc:0 "O pilar da segurança britânica dita que a Marinha Real deve manter uma esquadra de batalha igual ou superior à soma das duas marinhas seguintes combinadas."
 ENG_city_of_london_credit:0 "Centro Financeiro da City de Londres"
 ENG_city_of_london_credit_desc:0 "Como câmara de compensação do comércio mundial e guardiã do Padrão-Ouro, a City de Londres oferece crédito internacional incomparável."
 ENG_professional_bef:0 "Força Expedicionária Britânica (BEF)"
 ENG_professional_bef_desc:0 "Pequeno em tamanho mas incomparável em precisão de tiro e disciplina, o exército voluntário profissional da Grã-Bretanha é capaz de rápida mobilização no continente."
 ENG_the_imperial_web:0 "A Teia Imperial"
 ENG_the_imperial_web_desc:0 "Cabos telegráficos globais, estações de carvão e rotas de navegação unem a Grã-Bretanha a Canadá, Austrália, Nova Zelândia, Índia e África do Sul."
 ENG_irish_home_rule_tension:0 "Crise da Home Rule Irlandesa"
 ENG_irish_home_rule_tension_desc:0 "Lutas parlamentares amargas sobre a autonomia da Irlanda ameaçam conflitos civis no Ulster e testam a estabilidade constitucional do império."

 FRA_wound_of_1870:0 "A Ferida Aberta de 1870"
 FRA_wound_of_1870_desc:0 "A perda da Alsácia-Lorena após a Guerra Franco-Prussiana permanece como um trauma aberto na sociedade francesa, alimentando o desejo inabalável de revanche nacional."
 FRA_elan_vital_doctrine:0 "Doutrina do Élan Vital"
 FRA_elan_vital_doctrine_desc:0 "A doutrina militar francesa deposita fé suprema na força moral e espiritual da ofensiva desenfreada — avançando com baionetas e coragem inabalável."
 FRA_canon_75mm_supremacy:0 "Supremacia do Canhão de 75mm"
 FRA_canon_75mm_supremacy_desc:0 "O revolucionário canhão de campanha francês de 75mm, disparando até 15 tiros rápidos de estilhaço por minuto, domina o campo de batalha moderno."
 FRA_demographic_stagnation:0 "Estagnação Demográfica"
 FRA_demographic_stagnation_desc:0 "Décadas de baixa natalidade deixam a França com menos recrutas do que a Alemanha, forçando a adoção da rigorosa Lei do Serviço Militar de Três Anos."
 FRA_third_republic_instability:0 "Faccionalismo da Terceira República"
 FRA_third_republic_instability_desc:0 "Coalizões instáveis, quedas frequentes de gabinete e atritos entre republicanos seculares e a elite militar tradicionalista dificultam a coerência estratégica."

 # UNIDADES ESPECIAIS & SUBUNIDADES WW1
 german_stosstruppen:0 "Stosstruppen"
 german_stosstruppen_desc:0 "Infantaria de assalto de elite treinada em táticas de infiltração, lança-chamas, granadas de mão e bypass de posições fortificadas."
 french_75mm_rapid_battery:0 "Bateria Rápida de 75mm"
 french_75mm_rapid_battery_desc:0 "Regimentos dedicados ao célebre Canon de 75 modelo 1897 lançando barragens devastadoras de estilhaços e alto-explosivos."
 russian_opolcheniye:0 "Milícia Opolcheniye"
 russian_opolcheniye_desc:0 "Batalhões de milícia imperial em massa, preenchendo as brechas das linhas com patriotas camponeses."
 kuk_gebirgsjaeger:0 "K.u.k. Gebirgsjäger"
 kuk_gebirgsjaeger_desc:0 "Infantaria de montanha de elite do Exército Austro-Húngaro, especializada no combate alpino nos picos tiroleses e Cárpatos."
 anzac_corps:0 "Corpo ANZAC"
 anzac_corps_desc:0 "Tropas voluntárias rústicas da Austrália e Nova Zelândia, célebres por sua tenacidade e bravura em Gallipoli e no front ocidental."
 italian_arditi:0 "Tropas de Choque Arditi"
 italian_arditi_desc:0 "Pelotões de choque armados com adagas e granadas escolhidos entre as unidades mais veteranas para tomar trincheiras inimigas."
 ottoman_ghazi_militia:0 "Irregulares Ghazi"
 ottoman_ghazi_militia_desc:0 "Beduínos e voluntários anatólios lutando com fervor religioso e domínio total de terrenos áridos."
 us_doughboys_division:0 "Doughboys Americanos"
 us_doughboys_division_desc:0 "Tropas expedicionárias americanas descansadas, bem nutridas e entusiastas, armadas com rifles Springfield e escopetas de trincheira."

 # HABILIDADES & IDEIAS TÁTICAS
 chemical_gas_disruption:0 "Ataque com Gás Químico"
 chemical_gas_disruption_desc:0 "Nuvens letais de cloro e gás mostarda sufocam as linhas inimigas, destruindo o moral e abrindo brechas para o assalto."
 landships_breakthrough_boost:0 "Barragem de Tanques Landships"
 landships_breakthrough_boost_desc:0 "Os primeiros tanques blindados esmagam o arame farpado e cruzam as trincheiras protegidos por fogo sincronizado."
 voie_sacree_resilience_idea:0 "Resiliência da Voie Sacrée"
 voie_sacree_resilience_idea_desc:0 "Um comboio contínuo de suprimentos motorizados 24 horas garante munição, comida e reforços para as defesas de Verdun."
 brusilov_offensive_shock_idea:0 "Choque de Infiltração Brusilov"
 brusilov_offensive_shock_idea_desc:0 "Preparação de artilharia rápida em linha ampla seguida de assaltos direcionados que quebram as linhas inimigas."
 skoda_siege_bombardment_idea:0 "Bombardeio Super-Pesado Skoda"
 skoda_siege_bombardment_idea_desc:0 "Morteiros pesados de 30.5 cm demolem fortificações de concreto e bunkers subterrâneos."
 arditi_infiltration_shock_idea:0 "Assalto de Adaga Arditi"
 arditi_infiltration_shock_idea_desc:0 "Incursões noturnas cirúrgicas com granadas que rompem o perímetro defensivo do inimigo."
 kemal_fanatic_defence_idea:0 "Linha Defensiva Fanática"
 kemal_fanatic_defence_idea_desc:0 "Tropas ordenadas não apenas a lutar, mas a morrer sustentando as posições altas da península."
 jihad_holy_call_idea:0 "Chamado à Guerra Santa"
 jihad_holy_call_idea_desc:0 "A proclamação do Califa convoca combatentes fiéis em todo o mundo islâmico para repelir as potências coloniais."
 trench_sweeper_shotgun_idea:0 "Escopetas Limpa-Trincheiras"
 trench_sweeper_shotgun_idea_desc:0 "Escopetas Winchester M1897 inflam estragos devastadores em combates a curta distância nos labirintos de trincheiras."
 german_infiltration_assault_idea:0 "Táticas de Infiltração Hutier"
 german_infiltration_assault_idea_desc:0 "Bombardeio furacão coordenado com tropas de assalto infiltrando as posições de comando e artilharia inimigas."
'''

if 'ENG_two_power_standard' not in mech_pt:
    mech_pt += pt_mechanics_additions

with open('localisation/braz_por/ww1_mechanics_l_braz_por.yml', 'w', encoding='utf-8-sig') as f:
    f.write(mech_pt)

print('Updated Portuguese Mechanics Localisation.')
