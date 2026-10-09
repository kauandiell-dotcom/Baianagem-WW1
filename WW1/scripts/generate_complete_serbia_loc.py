#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates complete bilingual localization (English & Brazilian Portuguese)
for Kingdom of Serbia (SER) WW1 overhaul:
- 94 Focuses (names + descriptions)
- 16 Events (titles + descriptions + choices)
- 3 Decision Categories (names + descriptions)
- 11 Decisions (names + descriptions + tooltips)
- 16 National Ideas (names + descriptions)
- Characters & Leaders

Enforces mandatory UTF-8 BOM (\xef\xbb\xbf) on both output files.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOC_EN = ROOT / "localisation" / "english" / "ww1_serbia_l_english.yml"
LOC_BR = ROOT / "localisation" / "braz_por" / "ww1_serbia_l_braz_por.yml"

ENTRIES = {}

def add_loc(key, en_text, pt_text):
    ENTRIES[key] = (en_text, pt_text)

# ==============================================================================
# 1. CHARACTERS
# ==============================================================================
add_loc("SER_nikola_pasic", "Nikola Pašić", "Nikola Pašić")
add_loc("SER_alexander_i", "Crown Prince Alexander", "Príncipe Regente Alexandre")

# ==============================================================================
# 2. NATIONAL IDEAS
# ==============================================================================
add_loc("SER_civil_military_rivalry", "Civil-Military Rivalry", "Rivalidade Civil-Militar")
add_loc("SER_civil_military_rivalry_desc",
        "Bitter friction between Nikola Pašić's civilian cabinet and the clandestine military conspirators of the Black Hand hampers government cohesion and inflates political instability.",
        "A amarga fricção entre o gabinete civil de Nikola Pašić e os oficiais conspiratórios da Mão Negra atrapalha a coesão governamental e gera constante atrito político.")

add_loc("SER_civilian_supremacy_established", "Civilian Supremacy Established", "Supremacia Civil Estabelecida")
add_loc("SER_civilian_supremacy_established_desc",
        "Constitutional democracy reigns supreme in Belgrade. The parliament exercises undisputed authority over military expenditures and national policy, solidifying democratic stability.",
        "A democracia constitucional reina soberana em Belgrado. O Parlamento exerce autoridade incontestada sobre despesas militares e o rumo do Estado, garantindo estabilidade e legalidade.")

add_loc("SER_military_officer_ascendancy", "Military Officer Ascendancy", "Ascendência da Oficialidade Militar")
add_loc("SER_military_officer_ascendancy_desc",
        "The patriotic officer corps exercises paramount influence over national policy, prioritizing uncompromising military readiness and national expansion above all else.",
        "O corpo de oficiais patriotas detém influência primordial sobre as decisões do Estado, priorizando prontidão militar máxima e determinação férrea na defesa dos interesses nacionais.")

add_loc("SER_montenegrin_dynastic_union", "Montenegrin Dynastic Union", "União Dinástica de Montenegro")
add_loc("SER_montenegrin_dynastic_union_desc",
        "Bound by shared blood, mountain resilience, and centuries of defiance against Ottoman and Habsburg hegemony, Montenegro stands united with Serbia under the royal union.",
        "Unidos por laços de sangue, resiliência serrana e séculos de combate comum contra impérios invasores, Montenegro e Sérvia compartilham o mesmo destino e fraternidade.")

add_loc("SER_underdeveloped_agrarian_economy", "Underdeveloped Agrarian Economy", "Economia Agrária Subdesenvolvida")
add_loc("SER_underdeveloped_agrarian_economy_desc",
        "Dependent on smallholder peasant agriculture and lacking heavy metallurgical industry, Serbia struggles to finance modernization following years of economic isolation.",
        "Dependente da agricultura camponesa de subsistência e carente de metalurgia pesada, a Sérvia luta para financiar reformas fabris após anos de isolamento econômico.")

add_loc("SER_kragujevac_arsenal_expansion", "Kragujevac Arsenal Expansion", "Expansão do Arsenal de Kragujevac")
add_loc("SER_kragujevac_arsenal_expansion_desc",
        "New smelting workshops, cartridge tooling machinery, and modernized foundry halls at Kragujevac elevate domestic arms and ammunition manufacturing capacity.",
        "Novas fundições, prensas de cartuchos e linhas mecanizadas em Kragujevac ampliam a capacidade nacional de produzir armas e munições em larga escala.")

add_loc("SER_diversified_national_industry", "Diversified National Industry", "Indústria Nacional Diversificada")
add_loc("SER_diversified_national_industry_desc",
        "Through coordinated infrastructure investments and expanding domestic processing, Serbia has laid the groundwork for an autonomous, modern manufacturing economy.",
        "Com investimentos coordenados em transporte e manufatura, a Sérvia estabeleceu a base para uma economia produtiva autônoma, moderna e diversificada.")

add_loc("SER_french_serbian_trade_accord", "Franco-Serbian Trade Accord", "Acordo Comercial Franco-Sérvio")
add_loc("SER_french_serbian_trade_accord_desc",
        "Benefiting from French financial backing and privileged commercial links, Serbia secures modern arms, machinery, and investments on highly favorable terms.",
        "Respaldada por créditos e tratados comerciais com a França, a Sérvia obtém armamentos modernos e investimentos fundamentais para seu desenvolvimento.")

add_loc("SER_serbo_austrian_economic_pact", "Serbo-Austrian Economic Pact", "Pacto Econômico Sérvio-Austríaco")
add_loc("SER_serbo_austrian_economic_pact_desc",
        "A peaceful commercial settlement with the Dual Monarchy provides guaranteed export quotas for Serbian livestock and grain across central European railways.",
        "Um acordo comercial equilibrado com Viena assegura cotas de exportação garantidas para o gado e cereais sérvios pelas ferrovias da Europa Central.")

add_loc("SER_cer_counterstroke_glory", "Glory of the Cer Counter-Attack", "Glória do Contra-Ataque de Cer")
add_loc("SER_cer_counterstroke_glory_desc",
        "The electric spirit of the victory at Mount Cer courses through every Serbian battalion, inspiring heroic courage, disciplined entrenchment, and fierce defensive defiance.",
        "O espírito vitorioso do triunfo no Monte Cer inflama cada batalhão sérvio, inspirando bravura estoica, disciplina defensiva e repulsa a qualquer avanço inimigo.")

add_loc("SER_kolubara_maneuver_mastery", "Kolubara Maneuver Mastery", "Maestria de Manobra de Kolubara")
add_loc("SER_kolubara_maneuver_mastery_desc",
        "Channeling General Mišić's brilliant tactical timing, Serbian divisions strike with ferocious suddenness against overextended enemy salients, rolling back hostile armies.",
        "Inspirados no golpe magistral do General Mišić, as divisões sérvias desfecham ataques fulminantes contra flancos desguarnecidos, escorraçando os invasores.")

add_loc("SER_dobro_pole_breakthrough", "Dobro Pole Breakthrough Charge", "Carga da Ruptura de Dobro Pole")
add_loc("SER_dobro_pole_breakthrough_desc",
        "Driven by years of yearning for their occupied homes, Serbian storm columns advance with unmatched speed and fury, shattering all fortified mountain positions in their path.",
        "Movidos pela ânsia sagrada de libertar seus lares ocupados, as colunas sérvias atacam com velocidade e fúria indomáveis, rompendo qualquer barreira fortificada.")

add_loc("SER_typhus_epidemic_crisis", "Typhus Epidemic Crisis", "Crise Epidêmica de Tifo")
add_loc("SER_typhus_epidemic_crisis_desc",
        "Louse-borne typhus is ravaging frontline trenches, crowded hospital wards, and refugee villages, draining national manpower and demoralizing army formations.",
        "O tifo epidêmico assola as trincheiras e cidades, sobrecarregando hospitais improvisados e ceifando a juventude combatente da nação.")

add_loc("SER_rebuilt_salonika_corps", "Rebuilt Army of the Orient Corps", "Corpos Reconstituídos de Salônica")
add_loc("SER_rebuilt_salonika_corps_desc",
        "Equipped with modern Allied ordnance, disciplined by grueling trials, and unified under tested veteran generals, the resurrected Serbian army is ready for the liberation of the fatherland.",
        "Equipado com artilharia moderna aliada e forjado pelo sofrimento do exílio, o reconstruído exército sérvio ergue-se com moral renovada para a libertação da pátria.")

add_loc("SER_greater_serbia_ideal", "Greater Serbian Strategy", "Ideal da Grande Sérvia")
add_loc("SER_greater_serbia_ideal_desc",
        "Prioritizing the direct unification and liberation of all lands inhabited by ethnic Serbs strengthens national martial zeal, channeling all resources toward sovereign territorial expansion.",
        "Priorizar a união e libertação das terras etnicamente sérvias inflama a combatividade e concentra todas as energias do reino na defesa de sua gente.")

add_loc("SER_yugoslav_brotherhood_charter", "Yugoslav Brotherhood Charter", "Carta da Fraternidade Iugoslava")
add_loc("SER_yugoslav_brotherhood_charter_desc",
        "Pledging equal constitutional rights, regional autonomy, and cultural brotherhood to Croats, Slovenes, and Serbs forges enduring multi-ethnic solidarity across the South Slavic lands.",
        "Garantir direitos constitucionais iguais, respeito às liberdades regionais e fraternidade a croatas, eslovenos e sérvios alicerça a união duradoura da família sul-eslava.")

# ==============================================================================
# 3. DECISION CATEGORIES & DECISIONS
# ==============================================================================
add_loc("SER_black_hand_and_national_defense", "The Black Hand & National Defense", "A Mão Negra e a Defesa Nacional")
add_loc("SER_black_hand_and_national_defense_desc",
        "Internal politics in Belgrade are haunted by the shadow of the conspiratorial officer corps. Managing secret societies, gathering cross-border intelligence, and securing frontiers are essential for state stability.",
        "A política interna em Belgrado é assombrada pela sombra de conspiradores fardados. Monitorar sociedades secretas, colher inteligência além-fronteira e vigiar as passagens fluviais é vital para a estabilidade do Estado.")

add_loc("SER_wartime_emergency_measures", "Wartime Emergency Measures", "Medidas de Emergência de Guerra")
add_loc("SER_wartime_emergency_measures_desc",
        "During total war, the state must take drastic measures to ensure frontlines remain supplied, grain reaches starving cities, and deadly epidemics are halted in their tracks.",
        "Em tempos de guerra total, o Estado precisa tomar medidas drásticas para abastecer as frentes de combate, garantir o pão aos centros urbanos e conter surtos epidêmicos letais.")

add_loc("SER_salonika_and_corfu_exile", "Salonika & Corfu Exile Governance", "Governança no Exílio em Salônica e Corfu")
add_loc("SER_salonika_and_corfu_exile_desc",
        "Operating as a government-in-exile, Serbia coordinates with Allied forces, recruits South Slav volunteers, and manages diplomacy from afar until the sacred soil of the homeland can be liberated.",
        "Operando como governo no exílio, a Sérvia coordena esforços com frotas aliadas, arregimenta voluntários sul-eslavos e gere a diplomacia internacional até a libertação final do solo pátrio.")

add_loc("SER_monitor_ultranationalist_cells", "Monitor Ultranationalist Cells", "Monitorar Células Ultranacionalistas")
add_loc("SER_monitor_ultranationalist_cells_desc",
        "Deploy gendarmerie agents to watch radical national clubs in Belgrade, reducing internal volatility.",
        "Desdobrar agentes da polícia para monitorar círculos radicais em Belgrado, contendo a volatilidade política interna.")

add_loc("SER_infiltrate_bosnian_intelligence_network", "Infiltrate Intelligence Across the Drina", "Infiltrar Redes de Inteligência no Drina")
add_loc("SER_infiltrate_bosnian_intelligence_network_desc",
        "Expand secret observation posts and informants across the border to detect imperial military movements early.",
        "Expandir postos secretos de observação além-fronteira para detectar precocemente movimentações de tropas imperiais.")
add_loc("decision_cost_command_power_15", "Costs 15 Command Power", "Custa 15 de Poder de Comando")

add_loc("SER_purge_army_clandestine_officers", "Purge Clandestine Military Officers", "Expurgar Oficiais Clandestinos do Exército")
add_loc("SER_purge_army_clandestine_officers_desc",
        "Remove conspiratorial Black Hand loyalists from key brigade commands, cementing civilian supremacy.",
        "Afastar conspiradores da Mão Negra de postos de comando de brigada, assegurando a supremacia civil.")
add_loc("SER_purge_army_clandestine_officers_tt",
        "Civilian control over the armed forces is permanently secured.",
        "O controle civil irrestrito sobre as Forças Armadas é definitivamente assegurado.")

add_loc("SER_strengthen_border_watch", "Strengthen Sava and Drina Border Watch", "Reforçar a Vigília de Fronteira no Sava e Drina")
add_loc("SER_strengthen_border_watch_desc",
        "Station vigilant territorial watch detachments at river fords and mountain passes.",
        "Posicionar destacamentos territoriais vigilantes em vaus fluviais e desfiladeiros de montanha.")

add_loc("SER_typhus_quarantine_and_triage", "Typhus Quarantine and Medical Triage", "Quarentena e Triagem Médica contra o Tifo")
add_loc("SER_typhus_quarantine_and_triage_desc",
        "Implement strict disinfection procedures, delousing stations, and field hospital triage to halt the epidemic.",
        "Implantar desinfecção rigorosa, postos sanitários de campanha e triagem médica para exterminar o surto de tifo.")

add_loc("SER_drina_railway_ammunition_priority", "Railway Ammunition Priority for the Front", "Prioridade Ferroviária de Munição para a Frente")
add_loc("SER_drina_railway_ammunition_priority_desc",
        "Requisition all civilian rolling stock to rush artillery shells directly to threatened frontline batteries.",
        "Requisitar composições ferroviárias civis para despachar munição de artilharia urgente às baterias da frente.")

add_loc("SER_requisition_emergency_grain", "Requisition Emergency Grain Reserves", "Requisição Emergencial de Grãos")
add_loc("SER_requisition_emergency_grain_desc",
        "Collect grain reserves from rural cooperatives to feed bread rations to besieged urban centers.",
        "Arrecadar reservas de grãos das cooperativas rurais para abastecer as rações de pão nos centros urbanos.")

add_loc("SER_montenegrin_mountain_levies", "Call Montenegrin Mountain Volunteers", "Convocação dos Voluntários Montenegrinos de Lovćen")
add_loc("SER_montenegrin_mountain_levies_desc",
        "Rally the fierce mountain warriors of Lovćen and Durmitor to reinforce the Serbian army in battle.",
        "Convocar os bravos guerreiros de montanha de Lovćen e Durmitor para engrossar as fileiras sérvias no combate.")
add_loc("SER_montenegrin_mountain_levies_tt",
        "Thousands of hardened mountain fighters take up their rifles in defense of the realm.",
        "Milhares de valorosos combatentes das serras empunham seus fuzis na defesa do reino.")

add_loc("SER_recruit_south_slav_pow_volunteers", "Recruit South Slav POW Volunteers", "Recrutar Voluntários Sul-Eslavos Prisioneiros")
add_loc("SER_recruit_south_slav_pow_volunteers_desc",
        "Enlist thousands of Czech, Croat, and Slovene prisoners of war willing to fight for South Slav liberation.",
        "Alistar prisioneiros de guerra croatas, eslovenos e tchecos dispostos a lutar pela libertação dos povos eslavos.")

add_loc("SER_french_logistical_coordination", "French Intendance Coordination", "Coordenação com a Intendência Francesa")
add_loc("SER_french_logistical_coordination_desc",
        "Coordinate supply manifests directly with the French Armée d'Orient to receive rifles, uniforms, and shoes.",
        "Alinhar manifestos de carga com o exército francês do Oriente para receber fuzis, uniformes e calçados novos.")

add_loc("SER_diplomatic_appeal_corfu", "Diplomatic Appeal of Corfu", "Apelo Diplomático e Financeiro de Corfu")
add_loc("SER_diplomatic_appeal_corfu_desc",
        "Launch an international press and diplomatic campaign in Paris and London on behalf of occupied Serbia.",
        "Lançar uma campanha de imprensa e diplomacia em Paris e Londres em defesa da Sérvia ocupada.")

# ==============================================================================
# 4. EVENTS (16 EVENTS)
# ==============================================================================
add_loc("ww1_serbia.1.t", "The Pašić Ministry and Constitutional Stability", "O Gabinete Pašić e a Estabilidade Constitucional")
add_loc("ww1_serbia.1.d", "King Peter I Karađorđević rules through parliamentary democracy. Nikola Pašić's Radical Party holds the reins of governance, yet tensions between civilian ministries and national defense remain a delicate balancing act.", "O venerando Rei Pedro I Karađorđević governa estritamente sob as regras da democracia parlamentar. O Partido Radical de Nikola Pašić conduz o Estado com prudência, mas as relações entre os ministros civis e o exército exigem vigilância constante.")
add_loc("ww1_serbia.1.a", "Long live the constitutional monarchy of King Peter!", "Vida longa à monarquia constitucional de Pedro I!")
add_loc("ww1_serbia.1.b", "Ensure the National Assembly maintains fiscal control.", "Assegurar que a Assembleia Nacional controle as contas públicas.")

add_loc("ww1_serbia.2.t", "The Shadow of Apis: The Secret Society Unification or Death", "A Sombra de Apis: A Sociedade Secreta Unificação ou Morte")
add_loc("ww1_serbia.2.d", "Founded by nationalist military officers under Colonel Dragutin Dimitrijević 'Apis', the clandestine organization 'Unification or Death' (known popularly as the Black Hand) wields immense underground power across the army and press.", "Fundada por oficiais nacionalistas chefiados pelo Coronel Dragutin Dimitrijević 'Apis', a organização clandestina 'Unificação ou Morte' (a Mão Negra) estende seus tentáculos subterrâneos por guarnições e círculos patrióticos.")
add_loc("ww1_serbia.2.a", "We must keep close watch over these fiery officers.", "Devemos vigiar de perto estes oficiais impetuosos.")
add_loc("ww1_serbia.2.b", "Their patriotic devotion will shield the fatherland.", "Sua devoção patriótica protegerá o solo da pátria.")

add_loc("ww1_serbia.3.t", "The Banque Franco-Serbe Credits", "Os Empréstimos da Banque Franco-Serbe")
add_loc("ww1_serbia.3.d", "French financiers and diplomats have finalized generous credit agreements with the government in Belgrade, providing capital for railways, debt refinancing, and artillery orders from Creusot.", "Financistas e diplomatas franceses concluíram acordos de crédito com Belgrado, garantindo fundos para ferrovias, refinanciamento da dívida e compras de artilharia pesada da Creusot.")
add_loc("ww1_serbia.3.a", "A splendid financial foundation for national defense.", "Uma base financeira sólida para a defesa nacional.")

add_loc("ww1_serbia.4.t", "Bilateral Talks with Sofia", "Conversações Bilaterais com Sófia")
add_loc("ww1_serbia.4.d", "Envoys from Belgrade and Sofia have initiated high-level consultations to address frontier security and prevent fratricidal Slavic conflict in Ottoman border provinces.", "Emissários de Belgrado e Sófia iniciaram conversas diplomáticas para garantir a segurança das fronteiras e prevenir atritos fratricidas entre irmãos eslavos.")
add_loc("ww1_serbia.4.a", "Slavic brotherhood must triumph over imperial intrigue.", "A fraternidade eslava deve triunfar sobre intrigas imperiais.")
add_loc("ww1_serbia.4.b", "Proceed cautiously and protect Serbian interests.", "Avançar com cautela e resguardar os interesses sérvios.")

add_loc("ww1_serbia.5.t", "The Dynastic Accord with King Nikola of Montenegro", "O Acordo Dinástico com o Rei Nikola de Montenegro")
add_loc("ww1_serbia.5.d", "King Nikola I of Montenegro and King Peter I reaffirm their historic dynastic and fraternal solidarity. The two Serb realms pledge eternal mutual defense.", "O Rei Nikola I de Montenegro e o Rei Pedro I reafirmam a solidariedade dinástica e fraternal de seus povos. Os dois reinos irmãos juram auxílio militar perpétuo.")
add_loc("ww1_serbia.5.a", "Two crowns, one heroic soul! Živela Srbija i Crna Gora!", "Duas coroas, uma só alma heroica! Živela Srbija i Crna Gora!")

add_loc("ww1_serbia.6.t", "The Regency of Crown Prince Alexander", "A Regência do Príncipe Herdeiro Alexandre")
add_loc("ww1_serbia.6.d", "On June 24, 1914, King Peter I Karađorđević transfers full royal executive prerogatives to his energetic son, Crown Prince Alexander, due to declining physical health.", "Em 24 de junho de 1914, o idoso Rei Pedro I transfere oficialmente o exercício das prerrogativas régias a seu filho, o Príncipe Herdeiro Alexandre, devido à sua saúde fragilizada.")
add_loc("ww1_serbia.6.a", "Long live Prince Regent Alexander!", "Vida longa ao Príncipe Regente Alexandre!")

add_loc("ww1_serbia.7.t", "The Sarajevo Outrage: Storm Clouds Gather", "O Atentado de Sarajevo: Nuvens Negras no Horizonte")
add_loc("ww1_serbia.7.d", "Archduke Franz Ferdinand and Sophie Duchess of Hohenberg have been assassinated in Sarajevo by Gavrilo Princip. Vienna places full blame upon Belgrade.", "O Arquiduque Francisco Fernando e sua esposa foram assassinados em Sarajevo por Gavrilo Princip. Viena lança a culpa inteira sobre Belgrado e clama por vingança.")
add_loc("ww1_serbia.7.a", "A terrible tragedy. We must prepare for imperial rage.", "Uma terrível tragédia. Devemos nos preparar para a fúria imperial.")

add_loc("ww1_serbia.8.t", "The Austro-Hungarian Ultimatum", "O Ultimato Austro-Húngaro")
add_loc("ww1_serbia.8.d", "On July 23, Baron Giesl delivers Vienna's ten-point ultimatum, demanding an answer within 48 hours. Several demands infringe upon Serbia's national judicial sovereignty.", "Em 23 de julho, o Barão Giesl entrega o ultimato de dez pontos de Viena, exigindo resposta em 48 horas. Várias cláusulas ferem a soberania judicial do reino sérvio.")
add_loc("ww1_serbia.8.a", "Accept all reasonable points, but defend our sovereign courts!", "Aceitar todos os pontos razoáveis, mas defender nossa soberania!")
add_loc("ww1_serbia.8.b", "Total defiance! We shall never bow to imperial arrogance!", "Desafio total! Jamais nos curvaremos à arrogância de Viena!")

add_loc("ww1_serbia.9.t", "Putnik Proclaims General Mobilization", "Putnik Proclama a Mobilização Geral")
add_loc("ww1_serbia.9.d", "With diplomacy broken, Vojvoda Radomir Putnik orders all three Pozivs to take their stations. Over 400,000 Serbian soldiers take up arms for their homes.", "Com a ruptura diplomática consumada, o Vojvoda Putnik ordena a mobilização de todos os três Pozivs. Mais de 400.000 homens tomam seus postos na defesa da pátria.")
add_loc("ww1_serbia.9.a", "For King, Fatherland, and Liberty!", "Pelo Rei, pela Pátria e pela Liberdade!")

add_loc("ww1_serbia.10.t", "The Miracle of Kolubara", "O Triunfo de Kolubara")
add_loc("ww1_serbia.10.d", "After weeks of grueling retreat in freezing mud, General Živojin Mišić unleashed a thunderous counter-attack along the Kolubara River, shattering the Austrian Fifth and Sixth Armies and driving them from Serbian soil.", "Após semanas de penoso recuo na lama gelada, o General Živojin Mišić desfechou um colossal contra-ataque no Rio Kolubara, destroçando os exércitos austríacos e expulsando-os do solo sagrado sérvio.")
add_loc("ww1_serbia.10.a", "A legendary triumph! Belgrade is free!", "Um triunfo lendário! Belgrado está livre!!")

add_loc("ww1_serbia.11.t", "The Albanian Golgotha: The Great Retreat", "O Gólgota Albanês: A Grande Retirada")
add_loc("ww1_serbia.11.d", "Faced with overwhelming simultaneous offensives from Germany, Austria-Hungary, and Bulgaria, the Serbian army refuses surrender. The King and army undertake the grueling winter march across the mountains of Albania.", "Cercado por três exércitos imperiais, o exército sérvio recusa a rendição. O idoso monarca e suas divisões iniciam a heroica e trágica travessia invernal pelas cordilheiras albanesas.")
add_loc("ww1_serbia.11.a", "We retreat today so that Serbia may rise tomorrow!", "Recuamos hoje para que a Sérvia renasça amanhã!")

add_loc("ww1_serbia.12.t", "The Resurrected Kingdom: Exile in Corfu", "O Reino Ressuscitado: O Exílio em Corfu")
add_loc("ww1_serbia.12.d", "Rescued by Allied fleets, the Serbian government, parliament, and soldiers have reassembled on the Greek island of Corfu. Though displaced from our homeland, our state sovereignty endures unbroken.", "Resgatados pela frota aliada, o governo, os parlamentares e as tropas sérvias reagrupam-se na ilha grega de Corfu. Embora sem terra natal, a soberania sérvia permanece inquebrantável.")
add_loc("ww1_serbia.12.a", "Serbia lives on! We shall return in triumph!", "A Sérvia vive! Retornaremos triunfantes!")

add_loc("ww1_serbia.13.t", "The Salonika Trial: The Fall of the Black Hand", "O Julgamento de Salônica e o Fim da Mão Negra")
add_loc("ww1_serbia.13.d", "In 1917, the royal government uncovers a purported plot against Prince Alexander. Colonel Apis and the leadership of the Black Hand are tried and executed, ending military conspiracy once and for all.", "Em 1917, o governo militar julga o Coronel Apis e os cabeças da Mão Negra por conspiração. Com a execução dos líderes, o golpismo militar é extinto definitivamente.")
add_loc("ww1_serbia.13.a", "Constitutional authority is permanently restored.", "A autoridade constitucional civil é definitivamente restaurada.")

add_loc("ww1_serbia.14.t", "The Corfu Declaration: Pact of South Slav Unity", "A Declaração de Corfu e a Unidade Sul-Eslava")
add_loc("ww1_serbia.14.d", "Prime Minister Nikola Pašić and Ante Trumbić of the Yugoslav Committee sign the historic Corfu Declaration, pledging that Serbs, Croats, and Slovenes shall unite in a constitutional monarchy under the Karađorđević dynasty.", "O Primeiro-Ministro Nikola Pašić e Ante Trumbić firmam a Declaração de Corfu, selando que sérvios, croatas e eslovenos se fundirão em um único reino sob a coroa Karađorđević.")
add_loc("ww1_serbia.14.a", "A glorious dawn for the South Slavic nation!", "Um alvorecer glorioso para todos os povos sul-eslavos!")

add_loc("ww1_serbia.15.t", "The Breakthrough at Dobro Pole", "A Ruptura de Dobro Pole")
add_loc("ww1_serbia.15.d", "Serbian divisions charge up the sheer cliffs of Dobro Pole, breaking through enemy lines and precipitating the total collapse of the Central Powers in the Balkans.", "As divisões sérvias escalam os penhascos de Dobro Pole sob tempestade de aço, rompem as defesas búlgaras e causam o colapso irreversível dos Impérios Centrais nos Bálcãs.")
add_loc("ww1_serbia.15.a", "Forward to victory! The homeland awaits!", "Avançar até a vitória! A pátria nos espera!")

add_loc("ww1_serbia.16.t", "Proclamation of the Kingdom of Serbs, Croats, and Slovenes", "Proclamação do Reino dos Sérvios, Croatas e Eslovenos")
add_loc("ww1_serbia.16.d", "On December 1, 1918, Prince Regent Alexander formally proclaims the unified Kingdom of Serbs, Croats, and Slovenes in Belgrade. A new era begins for the South Slavic peoples.", "Em 1 de dezembro de 1918, o Príncipe Regente Alexandre proclama solenemente a unificação do Reino dos Sérvios, Croatas e Eslovenos em Belgrado. Inicia-se uma nova era.")
add_loc("ww1_serbia.16.a", "Živeo Kralj! Long live united Yugoslavia!", "Živeo Kralj! Viva a Iugoslávia unida e livre!")

# ==============================================================================
# 5. FOCUSES (94 FOCUSES)
# ==============================================================================
# Import dictionary from previous section
from serbia_focus_loc_data import FOCUS_LOC

for fid, (en_name, en_desc, pt_name, pt_desc) in FOCUS_LOC.items():
    add_loc(fid, en_name, pt_name)
    add_loc(f"{fid}_desc", en_desc, pt_desc)

def compile_loc():
    print(f"Total localized entries: {len(ENTRIES)}")
    
    en_lines = ["l_english:"]
    pt_lines = ["l_braz_por:"]
    
    for k, (en_val, pt_val) in sorted(ENTRIES.items()):
        # Escape quotes if any
        clean_en = en_val.replace('"', '\\"')
        clean_pt = pt_val.replace('"', '\\"')
        en_lines.append(f' {k}:0 "{clean_en}"')
        pt_lines.append(f' {k}:0 "{clean_pt}"')
        
    en_content = "\n".join(en_lines) + "\n"
    pt_content = "\n".join(pt_lines) + "\n"
    
    # Write with UTF-8 BOM (\xef\xbb\xbf)
    LOC_EN.write_bytes(b"\xef\xbb\xbf" + en_content.encode("utf-8"))
    LOC_BR.write_bytes(b"\xef\xbb\xbf" + pt_content.encode("utf-8"))
    print(f"Wrote {LOC_EN} ({len(en_lines)} lines) with UTF-8 BOM")
    print(f"Wrote {LOC_BR} ({len(pt_lines)} lines) with UTF-8 BOM")

if __name__ == "__main__":
    compile_loc()
