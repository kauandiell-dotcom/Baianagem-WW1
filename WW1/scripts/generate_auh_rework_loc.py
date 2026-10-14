"""Generates bilingual localization files for Austria-Hungary rework with single UTF-8 BOM."""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOC_DATA = {
    # -------------------------------------------------------------
    # FOCUSES
    # -------------------------------------------------------------
    "AUH_ww1_constitutional_audit": (
        "[Historical] Constitutional Audit",
        "[Histórico] Auditoria Constitucional",
    ),
    "AUH_ww1_constitutional_audit_desc": (
        "The Compromise of 1867 is fraying at every seam. If the Habsburg Monarchy is to survive the storm engulfing Europe, the Crown must thoroughly audit the imperial constitution and chart a path between dualist inertia, federal reform, trialist autonomy, or martial rule.",
        "O Compromisso de 1867 está se desfazendo em todas as costuras. Se a Monarquia dos Habsburgo quiser sobreviver à tempestade que engole a Europa, a Coroa deve auditar minuciosamente a constituição imperial e traçar um caminho entre a inércia dualista, a reforma federal, a autonomia trialista ou a lei marcial.",
    ),
    "AUH_ww1_dualism": (
        "[Historical - Dualism] Dualism of Iron",
        "[Histórico - Dualismo] Dualismo de Ferro",
    ),
    "AUH_ww1_dualism_desc": (
        "Preserve the 1867 Compromise and double down on the alliance between the Austrian Germans and the Magyar aristocracy. Power shall remain shared strictly between Vienna and Budapest, uncompromising against minority agitations.",
        "Preservar o Compromisso de 1867 e reforçar a aliança entre os alemães austríacos e a aristocracia mágiar. O poder permanecerá dividido estritamente entre Viena e Budapeste, sem concessões a agitações de minorias.",
    ),
    "AUH_ww1_tisza_alliance": (
        "[Dualism] The Tisza Pact",
        "[Dualismo] O Pacto com Tisza",
    ),
    "AUH_ww1_tisza_alliance_desc": (
        "Prime Minister István Tisza commands the Hungarian Parliament with an iron grip. By securing his unconditional loyalty and guaranteeing Hungarian agrarian hegemony, the Crown ensures the grain fields of the Great Plain remain open to the imperial war effort.",
        "O Primeiro-Ministro István Tisza comanda o Parlamento húngaro com mão de ferro. Ao assegurar sua lealdade incondicional e garantir a hegemonia agrária húngara, a Coroa assegura que os campos de grãos da Grande Planície permaneçam abertos ao esforço de guerra imperial.",
    ),
    "AUH_ww1_magyar_cavalry_corps": (
        "[Dualism] Magyar Hussar Formations",
        "[Dualismo] Formações de Hussardos Mágiares",
    ),
    "AUH_ww1_magyar_cavalry_corps_desc": (
        "The Royal Hungarian Honvéd boasts storied equestrian traditions. By expanding the light cavalry regiments and mounting aggressive border reconnaissance patrols, we fortify the Carpathian gates against eastern threats.",
        "O Honvéd Real Húngaro ostenta gloriosas tradições equestres. Ao expandir os regimentos de cavalaria leve e montar patrulhas agressivas de reconhecimento de fronteira, fortificamos as passagens dos Cárpatos contra ameaças a leste.",
    ),
    "AUH_ww1_trialism": (
        "[Alternative - Trialism] Habsburg Trialism",
        "[Alternativo - Trialismo] Trialismo Habsburgo",
    ),
    "AUH_ww1_trialism_desc": (
        "End the dual monopoly of power by elevating the South Slav lands into a third equal kingdom within the Monarchy. Archduke Franz Ferdinand's favored vision establishes a unified Croato-Slav crown under Habsburg rule.",
        "Encerrar o monopólio dual de poder elevando as terras dos eslavos do sul a um terceiro reino igualitário dentro da Monarquia. A visão preferida do Arquiduque Franz Ferdinand estabelece uma coroa croata-eslava unificada sob o domínio dos Habsburgo.",
    ),
    "AUH_ww1_zagreb_coronation": (
        "[Trialism] The Zagreb Coronation",
        "[Trialismo] A Coroação de Zagreb",
    ),
    "AUH_ww1_zagreb_coronation_desc": (
        "Convene the Croatian Sabor in Zagreb and solemnize the union of Croatia, Slavonia, Dalmatia, and Bosnia-Herzegovina as the Kingdom of Illyria, binding South Slav loyalty eternally to the imperial throne.",
        "Convocar o Sabor Croata em Zagreb e solenizar a união da Croácia, Eslavônia, Dalmácia e Bósnia-Herzegovina como o Reino da Ilíria, vinculando a lealdade dos eslavos do sul eternamente ao trono imperial.",
    ),
    "AUH_ww1_pacify_south_slavs": (
        "[Trialism] Pacify the South Slavs",
        "[Trialismo] Pacificar os Eslavos do Sul",
    ),
    "AUH_ww1_pacify_south_slavs_desc": (
        "Neutralize Serbian irredentism and Narodna Odbrana agitators by granting complete administrative parity, native language rights, and regional self-government to our southern subjects.",
        "Neutralizar o irredentismo sérvio e os agitadores da Narodna Odbrana concedendo paridade administrativa completa, direitos linguísticos e autogoverno regional aos nossos súditos do sul.",
    ),
    "AUH_ww1_federalism": (
        "[Alternative - Federalism] Danubian Mega-Federation",
        "[Alternativo - Federalismo] Mega-Federação Danubiana",
    ),
    "AUH_ww1_federalism_desc": (
        "Dismantle the rigid Dualist compromise in favor of an enlightened federation of equal nationalities. Following Aurel Popovici's doctrine, every major ethnolinguistic group shall govern its homeland under a federal imperial mantle.",
        "Desmantelar o rígido compromisso dualista em favor de uma federação esclarecida de nacionalidades iguais. Seguindo a doutrina de Aurel Popovici, cada grande grupo etnolinguístico governará sua pátria sob um manto imperial federal.",
    ),
    "AUH_ww1_popovici_manifesto": (
        "[Federalism] The Popovici Manifesto",
        "[Federalismo] O Manifesto Popovici",
    ),
    "AUH_ww1_popovici_manifesto_desc": (
        "Promulgate the principles of the United States of Greater Austria. Drawing fifteen ethnic autonomous states with redrawn cantonal borders guarantees the civil rights and cultural preservation of Germans, Magyars, Czechs, Poles, Ruthenians, and Romanians alike.",
        "Promulgar os princípios dos Estados Unidos da Grande Áustria. O desenho de quinze estados autônomos com fronteiras cantonais redesenhadas garante os direitos civis e a preservação cultural de alemães, mágiares, tchecos, poloneses, rutenos e romenos.",
    ),
    "AUH_ww1_proclaim_danubian_federation": (
        "[Federalism] Proclaim the Danubian Mega-Federation",
        "[Federalismo] Proclamar a Mega-Federação Danubiana",
    ),
    "AUH_ww1_proclaim_danubian_federation_desc": (
        "Sign the historic imperial charter releasing Hungary, Bohemia, Croatia, and Galicia as autonomous constituent states under the House of Habsburg-Lorraine. Bound by common defense and single foreign representation, the Empire is reborn.",
        "Assinar a histórica carta imperial emancipando Hungria, Boêmia, Croácia e Galícia como estados constituintes autônomos sob a Casa de Habsburgo-Lorena. Unidos por uma defesa comum e representação externa única, o Império renasce.",
    ),
    "AUH_ww1_military_dictatorship": (
        "[Alternative - Junta] AOK Military Dictatorship",
        "[Alternativo - Junta] Ditadura Militar do AOK",
    ),
    "AUH_ww1_military_dictatorship_desc": (
        "Suspend constitutional niceties, dissolve obstinate parliamentary diets, and subordinate the civilian ministries directly to the Armeeoberkommando. In this supreme hour, iron martial discipline and the bayonet alone shall govern the realm.",
        "Suspender as formalidades constitucionais, dissolver dietas parlamentares obstinadas e subordinar os ministérios civis diretamente ao Armeeoberkommando. Nesta hora suprema, a disciplina militar de ferro e a baioneta governarão o reino.",
    ),
    "AUH_ww1_conrad_supreme_command": (
        "[Military Junta] Conrad's Supreme Command",
        "[Junta Militar] Comando Supremo de Conrad",
    ),
    "AUH_ww1_conrad_supreme_command_desc": (
        "Vest Field Marshal Count Franz Conrad von Hötzendorf with dictatorial wartime authority over all strategic assets, mobilization depots, and domestic communications. Offensive boldness shall override all timid civilian reservations.",
        "Investir o Marechal de Campo Conde Franz Conrad von Hötzendorf com autoridade ditatorial de tempo de guerra sobre todos os ativos estratégicos, depósitos de mobilização e comunicações civis. A audácia ofensiva se sobreporá a todas as tímidas reservas civis.",
    ),
    "AUH_ww1_war_surveillance_office": (
        "[Military Junta] The War Surveillance Office",
        "[Junta Militar] O Gabinete de Vigilância de Guerra",
    ),
    "AUH_ww1_war_surveillance_office_desc": (
        "Establish the Kriegsüberwachungsamt to supervise civilian industry, enforce strict press censorship, intercept seditious correspondence, and ruthlessly eliminate defeatism across all crown lands.",
        "Estabelecer o Kriegsüberwachungsamt para supervisionar a indústria civil, impor rígida censura à imprensa, interceptar correspondências sediciosas e eliminar impiedosamente o derrotismo em todas as terras da coroa.",
    ),
    "AUH_ww1_skoda_contracts": (
        "Expand Škoda Works Contracts",
        "Expandir Contratos da Škoda",
    ),
    "AUH_ww1_skoda_contracts_desc": (
        "Direct vast state subsidies to the Škoda armament foundries in Pilsen. Heavy metallurgy and specialized siege artillery development shall establish Austro-Hungarian gunsmiths as world leaders.",
        "Direcionar vastos subsídios estatais às fundições de armamento da Škoda em Pilsen. A metalurgia pesada e o desenvolvimento de artilharia de cerco especializada estabelecerão os armeiros austro-húngaros como líderes mundiais.",
    ),
    "AUH_ww1_steyr_small_arms": (
        "Steyr Arms Manufacturing",
        "Produção de Armas Steyr",
    ),
    "AUH_ww1_steyr_small_arms_desc": (
        "Contract the Österreichische Waffenfabriks-Gesellschaft in Steyr to ramp up mass fabrication of Mannlicher M.95 straight-pull rifles and Roth-Steyr service pistols for the imperial infantry.",
        "Contratar a Österreichische Waffenfabriks-Gesellschaft em Steyr para acelerar a fabricação em massa dos fuzis Mannlicher M.95 de ferrolho direto e pistolas Roth-Steyr para a infantaria imperial.",
    ),
    "AUH_ww1_trieste_yards": (
        "Trieste Naval Dockyards",
        "Estaleiros Navais de Trieste",
    ),
    "AUH_ww1_trieste_yards_desc": (
        "Enlarge the slipways and drydocks of the Stabilimento Tecnico Triestino and Monfalcone. The K.u.K. Kriegsmarine must construct dreadnoughts capable of contesting dominance over the Adriatic waters.",
        "Ampliar as rampas de lançamento e docas secas do Stabilimento Tecnico Triestino e de Monfalcone. A K.u.K. Kriegsmarine deve construir encouraçados modernos capazes de disputar o domínio sobre o Mar Adriático.",
    ),
    "AUH_ww1_isonzo_plan": (
        "The Isonzo Defensive Plan",
        "O Plano Defensivo do Isonzo",
    ),
    "AUH_ww1_isonzo_plan_desc": (
        "Survey the limestone cliffs, karst plateaus, and treacherous gorges of the Isonzo river valley. In-depth fortifications and alpine gun batteries will bar any invasion through the Gorizia gate.",
        "Mapear os penhascos calcários, planaltos cársticos e gargantas traiçoeiras do vale do rio Isonzo. Fortificações em profundidade e baterias de artilharia alpina bloquearão qualquer invasão pelos portões de Gorizia.",
    ),

    # -------------------------------------------------------------
    # IDEAS
    # -------------------------------------------------------------
    "AUH_idea_dualism_iron": (
        "Dualism of Iron",
        "Dualismo de Ferro",
    ),
    "AUH_idea_dualism_iron_desc": (
        "Austro-Hungarian dualism preserves the historic partnership of German and Hungarian ruling classes, commanding resolute obedience from imperial subjects at the cost of Slavic grievances.",
        "O dualismo austro-húngaro preserva a parceria histórica entre as classes dominantes alemã e húngara, exigindo obediência resoluta dos súditos imperiais ao custo do ressentimento eslavo.",
    ),
    "AUH_idea_habsburg_trialism": (
        "Habsburg Trialism",
        "Trialismo Habsburgo",
    ),
    "AUH_idea_habsburg_trialism_desc": (
        "By recognizing a South Slav crown alongside Austria and Hungary, the Monarchy secures the loyalty of its southern provinces and permanently shields its flanks from Balkan irredentism.",
        "Ao reconhecer uma coroa dos eslavos do sul ao lado da Áustria e da Hungria, a Monarquia garante a lealdade de suas províncias do sul e protege permanentemente seus flancos contra o irredentismo balcânico.",
    ),
    "AUH_idea_danubian_federation_spirit": (
        "Danubian Federal Spirit",
        "Espírito Federal Danubiano",
    ),
    "AUH_idea_danubian_federation_spirit_desc": (
        "A brotherhood of nationalities united under an enlightened Habsburg constitution. Broad regional autonomy fuels unprecedented civic cooperation, economic vigor, and social harmony.",
        "Uma irmandade de nacionalidades unidas sob uma esclarecida constituição dos Habsburgo. A ampla autonomia regional fomenta cooperação cívica sem precedentes, vigor econômico e harmonia social.",
    ),
    "AUH_idea_aok_military_dictatorship": (
        "AOK Military Dictatorship",
        "Ditadura Militar do AOK",
    ),
    "AUH_idea_aok_military_dictatorship_desc": (
        "The Armeeoberkommando holds absolute sway over state resources and citizen life. Every train, factory, and harvest is ruthlessly commandeered for the front, sparking civilian despair beneath a facade of relentless martial resolve.",
        "O Armeeoberkommando detém controle absoluto sobre os recursos estatais e a vida civil. Cada trem, fábrica e colheita é implacavelmente requisitado para a frente, provocando desespero civil sob a fachada de uma implacável determinação marcial.",
    ),
    "AUH_danubian_federal_member": (
        "Danubian Federal Member",
        "Membro Federal Danubiano",
    ),
    "AUH_danubian_federal_member_desc": (
        "As an autonomous constituent state of the Danubian Mega-Federation, this realm manages its internal cultural and judicial affairs while pooling military production, manpower levies, and fiscal revenue under the common imperial crown.",
        "Como estado constituinte autônomo da Mega-Federação Danubiana, este território gere seus assuntos culturais e jurídicos internos enquanto concentra a produção militar, alistamento e receitas fiscais sob a coroa imperial comum.",
    ),
    "AUH_skoda_305_howitzer": (
        "Škoda 30.5 cm Heavy Siege Howitzers",
        "Obuseiros Pesados de Cerco Škoda 30,5 cm",
    ),
    "AUH_skoda_305_howitzer_desc": (
        "The Škoda 30.5 cm M.11 Motormörser delivers catastrophic high-explosive ordnance against hardened enemy forts and entrenched frontlines, pulverizing all resistance.",
        "O Motormörser Škoda 30,5 cm M.11 dispara munições de alto impacto catastróficas contra fortes inimigos e linhas de frente entrincheiradas, pulverizando toda resistência.",
    ),
    "AUH_steyr_mannlicher": (
        "Steyr-Mannlicher Munitions Conglomerate",
        "Conglomerado de Armamentos Steyr-Mannlicher",
    ),
    "AUH_steyr_mannlicher_desc": (
        "Precision Austrian firearm manufacture equips the imperial rank and file with dependable straight-pull Mannlicher rifles and cutting-edge small arms technology.",
        "A manufatura de armas de precisão austríaca equipa a infantaria imperial com fuzis confiáveis Mannlicher de ferrolho direto e armas leves de ponta.",
    ),
    "AUH_ganz_danubius": (
        "Ganz-Danubius Shipbuilders",
        "Estaleiros Ganz-Danubius",
    ),
    "AUH_ganz_danubius_desc": (
        "Hungary's premier maritime and heavy engineering works constructs cruisers, destroyers, and submarines to protect Adriatic lifelines and project dual naval might.",
        "O principal complexo marítimo e de engenharia pesada da Hungria constrói cruzadores, contratorpedeiros e submarinos para proteger as linhas vitais do Adriático e projetar poder naval duplo.",
    ),
    "AUH_conrad_offensive_doctrine": (
        "Conrad's Cult of the Offensive",
        "O Culto à Ofensiva de Conrad",
    ),
    "AUH_conrad_offensive_doctrine_desc": (
        "Chief of the General Staff Franz Conrad von Hötzendorf prioritizes ceaseless offensive momentum and daring enveloping maneuvers, accepting severe tactical casualties in pursuit of grand strategic triumph.",
        "O Chefe do Estado-Maior Franz Conrad von Hötzendorf prioriza o ímpeto ofensivo incessante e ousadas manobras de cerco, aceitando pesadas baixas táticas na busca do triunfo estratégico definitivo.",
    ),
    "AUH_borojevic_alpine_defense": (
        "Boroević's Alpine Defense",
        "Defesa Alpina de Boroević",
    ),
    "AUH_borojevic_alpine_defense_desc": (
        "Field Marshal Svetozar Boroević von Bojna excels in unyielding static defense, utilizing rugged karst mountain terrain and stone parapets to turn hostile offensives into bloody catastrophes.",
        "O Marechal de Campo Svetozar Boroević von Bojna destaca-se pela defesa estática inabalável, utilizando o terreno montanhoso cárstico e parapeitos de pedra para transformar as ofensivas inimigas em catástrofes sangrentas.",
    ),

    # -------------------------------------------------------------
    # DECISIONS & CATEGORIES
    # -------------------------------------------------------------
    "AUH_crown_dashboard": (
        "The Imperial Crown Dashboard",
        "Painel da Coroa Imperial",
    ),
    "AUH_crown_dashboard_desc": (
        "Monitoring the three vital pillars of the Austro-Hungarian state during total war: War Weariness, Imperial Cohesion, and Vienna Grain Stockpiles. Balancing these competing vectors is essential to preventing famine riots and ethnic dissolution.",
        "Monitora os três pilares vitais do Estado austro-húngaro durante a guerra total: Cansaço de Guerra, Coesão Imperial e Estoques de Grãos de Viena. Equilibrar esses vetores é essencial para impedir revoltas de fome e a dissolução étnica.",
    ),
    "AUH_dec_requisition_banat_grain": (
        "Requisition Banat Grain Harvests",
        "Requisitar Colheitas de Grãos de Banat",
    ),
    "AUH_dec_requisition_banat_grain_desc": (
        "Despatch imperial requisition commissars into the fertile Banat and Vojvodina agricultural zones to feed the hungry workers and bread queues of Vienna, risking friction with local Magyar landowners.",
        "Despachar comissários imperiais de requisição para as férteis zonas agrícolas de Banat e Voivodina para alimentar os operários famintos e as filas de pão de Viena, arriscando atritos com proprietários de terras húngaros.",
    ),
    "AUH_dec_bread_rationing_cards": (
        "Institute Imperial Bread Rationing",
        "Instituir Racionamento Imperial de Pão",
    ),
    "AUH_dec_bread_rationing_cards_desc": (
        "Issue strict rationing coupons across Cisleithania to manage dwindling flour stockpiles. Bread consumption is curtailed, preserving strategic reserves at the price of popular discontent.",
        "Distribuir cupons de racionamento estritos por toda a Cisleitânia para gerenciar estoques de farinha em queda. O consumo de pão é controlado, preservando reservas estratégicas ao custo do descontentamento popular.",
    ),
    "AUH_dec_appease_budapest_diet": (
        "Appease the Budapest Diet",
        "Apaziguar a Dieta de Budapeste",
    ),
    "AUH_dec_appease_budapest_diet_desc": (
        "Offer fiscal concessions and reaffirm political guarantees to the Hungarian Parliament, soothing aristocratic outrage and preserving imperial cohesion between Vienna and Budapest.",
        "Oferecer concessões fiscais e reafirmar garantias políticas ao Parlamento húngaro, acalmando o clamor aristocrático e preservando a coesão imperial entre Viena e Budapeste.",
    ),
    "AUH_dec_galician_food_corps": (
        "Organize Galician Agricultural Corps",
        "Organizar Corpos Agrícolas Galicianos",
    ),
    "AUH_dec_galician_food_corps_desc": (
        "Mobilize civilian labor and auxiliary logistics brigades in Galicia to harvest and transport agricultural supplies back to the imperial capital.",
        "Mobilizar trabalhadores civis e brigadas logísticas auxiliares na Galícia para colher e transportar suprimentos agrícolas de volta à capital imperial.",
    ),
    "AUH_dec_skoda_siege_howitzers": (
        "Commission Škoda 30.5 cm Siege Howitzers",
        "Encomendar Obuseiros de Cerco Škoda 30,5 cm",
    ),
    "AUH_dec_skoda_siege_howitzers_desc": (
        "Authorize urgent priority production of Škoda's motor-drawn super-heavy siege howitzers, providing frontline divisions with devastating fortification-busting firepower.",
        "Autorizar produção prioritária urgente dos obuseiros superpesados motorizados de cerco da Škoda, fornecendo às divisões de frente um poder de fogo demolidor de fortificações.",
    ),
    "AUH_dec_galician_oil_extraction": (
        "Intensify Boryslav Oilfield Extraction",
        "Intensificar Extração de Petróleo de Boryslav",
    ),
    "AUH_dec_galician_oil_extraction_desc": (
        "Drill deeper wells and build modern refinery cracking plants in the Galician Boryslav basin, supplying vital petroleum products for the imperial military machine.",
        "Perfurar poços mais profundos e construir refinarias modernas na bacia galiciana de Boryslav, fornecendo derivados vitais de petróleo para a máquina militar imperial.",
    ),
    "AUH_dec_steep_alpine_redoubts": (
        "Construct Steep Alpine Fortified Redoubts",
        "Construir Redutos Fortificados nos Alpes",
    ),
    "AUH_dec_steep_alpine_redoubts_desc": (
        "Carve cavernous gun embrasures, barbed wire belts, and concrete pillboxes directly into the granite peaks of the Dolomites and the Isonzo river sector.",
        "Escavar canhoneiras cavernosas, cinturões de arame farpado e casamatas de concreto diretamente nos picos graníticos das Dolomitas e no setor do rio Isonzo.",
    ),
    "AUH_dec_prince_wied_albania": (
        "Support Prince Wilhelm of Wied in Albania",
        "Apoiar o Príncipe Guilherme de Wied na Albânia",
    ),
    "AUH_dec_prince_wied_albania_desc": (
        "Extend diplomatic and financial patronage to Prince Wilhelm of Wied's sovereignty over the newly established Principality of Albania, checking Italian and Serbian ambitions.",
        "Estender patrocínio diplomático e financeiro à soberania do Príncipe Guilherme de Wied sobre o recém-estabelecido Principado da Albânia, contendo as ambições italianas e sérvias.",
    ),
    "AUH_dec_danubian_customs_union": (
        "Propose the Danubian Customs Union",
        "Propor a União Aduaneira Danubiana",
    ),
    "AUH_dec_danubian_customs_union_desc": (
        "Establish a comprehensive Mitteleuropa customs union spanning the entire Danube basin, eliminating internal tariffs and cementing regional trade under Austrian auspices.",
        "Estabelecer uma união aduaneira abrangente para a Mitteleuropa em toda a bacia danubiana, eliminando tarifas internas e consolidando o comércio regional sob a liderança austríaca.",
    ),

    # -------------------------------------------------------------
    # EVENTS: SECESSION & REUNIFICATION
    # -------------------------------------------------------------
    "ww1_austria_collapse.1.t": (
        "The Bohemian Revolt: Czech Secession",
        "A Revolta Boêmia: Secessão Tcheca",
    ),
    "ww1_austria_collapse.1.d": (
        "Crushed beneath relentless military disaster, food shortages, and severe war weariness, the Czech National Committee in Prague has declared complete independence. Czech regiments have mutinied, raising the white-and-red banner over the Hradčany Castle and repudiating their allegiance to the Habsburg Crown.",
        "Esmagado pelo desastre militar implacável, escassez de alimentos e severo cansaço de guerra, o Comitê Nacional Tcheco em Praga declarou independência total. Regimentos tchecos se amotinaram, erguendo a bandeira alvirrubra sobre o Castelo de Hradčany e repudiando a lealdade à Coroa dos Habsburgo.",
    ),
    "ww1_austria_collapse.1.a": (
        "Traitors! Mobilize loyal garrisons to crush the rebellion!",
        "Traidores! Mobilizem guarnições leais para esmagar a rebelião!",
    ),
    "ww1_austria_collapse.2.t": (
        "The Hungarian Diet Dissolves the Union",
        "A Dieta Húngara Dissolve a União",
    ),
    "ww1_austria_collapse.2.d": (
        "Furious over wartime centralization, devastating casualties, and perceived imperial betrayal of the Compromise of 1867, the Hungarian Parliament in Budapest has proclaimed the dissolution of the Austro-Hungarian Union. Hungarian units are recalled from the frontlines to defend the fatherland.",
        "Furioso com a centralização de guerra, baixas devastadoras e a percebida traição imperial ao Compromisso de 1867, o Parlamento Húngaro em Budapeste proclamou a dissolução da União Austro-Húngara. Unidades húngaras são retiradas das frentes para defender a pátria.",
    ),
    "ww1_austria_collapse.2.a": (
        "The Crown of Saint Stephen cannot sever its sacred oath!",
        "A Coroa de Santo Estêvão não pode romper seu juramento sagrado!",
    ),
    "ww1_austria_collapse.3.t": (
        "The South Slav Rebellion in Zagreb",
        "A Rebelião dos Eslavos do Sul em Zagreb",
    ),
    "ww1_austria_collapse.3.d": (
        "The Croatian Sabor and representatives of the Slovenes, Croats, and Serbs in Zagreb have renounced all ties to the Dual Monarchy. Disillusioned soldiers returning from the front have established a National Council, demanding complete South Slav sovereignty.",
        "O Sabor Croata e representantes dos eslovenos, croatas e sérvios em Zagreb renunciaram a todos os laços com a Monarquia Dual. Soldados desiludidos que retornam do front estabeleceram um Conselho Nacional, exigindo soberania plena para os eslavos do sul.",
    ),
    "ww1_austria_collapse.3.a": (
        "The Empire will never relinquish the Adriatic coast!",
        "O Império jamais renunciará à costa do Adriático!",
    ),
    "ww1_austria_collapse.10.t": (
        "Imperial Authority Restored",
        "Autoridade Imperial Restaurada",
    ),
    "ww1_austria_collapse.10.d": (
        "Loyal imperial-royal forces have recaptured rebel provincial capitals, decisively breaking the back of the insurrection. Separatist ringleaders have been arrested or driven into exile, and the rebellious provinces are restored directly under the Habsburg crown.",
        "Forças imperiais e reais leais recapturaram as capitais provinciais rebeldes, quebrando de forma decisiva a espinha dorsal da insurreição. Os líderes separatistas foram presos ou exilados, e as províncias rebeldes retornam diretamente sob a coroa dos Habsburgo.",
    ),
    "ww1_austria_collapse.10.a": (
        "Gott erhalte Franz den Kaiser! The Monarchy endures!",
        "Gott erhalte Franz den Kaiser! A Monarquia resiste!",
    ),

    # -------------------------------------------------------------
    # EVENTS: DIPLOMACY & SCANDALS
    # -------------------------------------------------------------
    "ww1_austria_diplomacy.1.t": (
        "The Colonel Redl Espionage Affair",
        "O Caso de Espionagem do Coronel Redl",
    ),
    "ww1_austria_diplomacy.1.d": (
        "A catastrophic security breach has shaken the Evidenzbureau to its very foundations. Colonel Alfred Redl, former head of counter-intelligence and Chief of Staff of the VIII Corps in Prague, has been unmasked as a high-level Russian spy. Deep in debt and blackmailed over his private life, Redl has sold Austria's complete mobilization plans—Plan B for the Balkans and Plan R for Russia—directly to the Tsar's General Staff. Confronted in his Vienna hotel room, Redl took his own life with a service revolver left by investigators.",
        "Uma violação catastrófica de segurança abalou o Evidenzbureau em suas estruturas. O Coronel Alfred Redl, ex-chefe de contraespionagem e Chefe do Estado-Maior do VIII Corpo em Praga, foi desmascarado como espião russo de alto escalão. Afogado em dívidas e chantageado por sua vida privada, Redl vendeu os planos completos de mobilização austríacos — Plano B para os Bálcãs e Plano R para a Rússia — diretamente ao Estado-Maior do Tsar. Confrontado em seu quarto de hotel em Viena, Redl tirou a própria vida com um revólver deixado pelos investigadores.",
    ),
    "ww1_austria_diplomacy.1.a": (
        "Overhaul mobilization schedules and revise Plan B and R immediately!",
        "Reformular os calendários de mobilização e revisar os Planos B e R imediatamente!",
    ),
    "ww1_austria_diplomacy.1.b": (
        "Cover up the scandal to protect the honor of the officer corps.",
        "Encobrir o escândalo para proteger a honra do corpo de oficiais.",
    ),
    "ww1_austria_diplomacy.10.t": (
        "The Sixtus Affair: Secret Peace Feelers",
        "O Caso Sixtus: Negociações Secretas de Paz",
    ),
    "ww1_austria_diplomacy.10.d": (
        "Young Emperor Karl I, despairing over the horrific slaughter of World War I and the impending collapse of the Habsburg dynasty, has initiated clandestine diplomatic overtures toward the Entente. Utilizing his brother-in-law, Prince Sixte of Bourbon-Parma serving as an officer in the Belgian army, Karl has sent a secret handwritten letter to French President Poincaré, offering to support France's just claims to Alsace-Lorraine and restore Belgian sovereignty in exchange for an honorable separate peace.",
        "O jovem Imperador Karl I, desesperado com o massacre devastador da Primeira Guerra Mundial e o colapso iminente da dinastia dos Habsburgo, iniciou aberturas diplomáticas clandestinas com a Entente. Utilizando seu cunhado, o Príncipe Sixto de Bourbon-Parma servindo como oficial no exército belga, Karl enviou uma carta secreta ao presidente francês Poincaré, oferecendo apoiar as justas reivindicações francesas sobre a Alsácia-Lorena e restaurar a soberania belga em troca de uma paz separada honrosa.",
    ),
    "ww1_austria_diplomacy.10.a": (
        "Pursue the secret peace feelers through Prince Sixte.",
        "Prosseguir com as sondagens secretas de paz através do Príncipe Sixto.",
    ),
    "ww1_austria_diplomacy.10.b": (
        "Reaffirm steadfast fidelity to the German alliance.",
        "Reafirmar lealdade inabalável à aliança com a Alemanha.",
    ),
    "ww1_austria_diplomacy.11.t": (
        "Austrian Peace Overtures Received in Paris",
        "Sondagens Austríacas de Paz Recebidas em Paris",
    ),
    "ww1_austria_diplomacy.11.d": (
        "Prince Sixte of Bourbon-Parma has delivered a secret personal letter from Emperor Karl of Austria-Hungary to the Élysée Palace. Vienna hints at recognizing French sovereignty over Alsace-Lorraine and restoring Belgium if a separate peace can be concluded.",
        "O Príncipe Sixto de Bourbon-Parma entregou uma carta pessoal secreta do Imperador Karl da Áustria-Hungria no Palácio do Eliseu. Viena insinua reconhecer a soberania francesa sobre a Alsácia-Lorena e restaurar a Bélgica se uma paz separada puder ser acordada.",
    ),
    "ww1_austria_diplomacy.11.a": (
        "Study Vienna's terms with cautious interest.",
        "Analisar os termos de Viena com prudente interesse.",
    ),
    "ww1_austria_diplomacy.11.b": (
        "Reject separate talks without total Entente consensus.",
        "Rejeitar conversas separadas sem o consenso total da Entente.",
    ),
    "ww1_austria_diplomacy.12.t": (
        "Vienna Reaffirms the German Pact",
        "Viena Reafirma o Pacto com a Alemanha",
    ),
    "ww1_austria_diplomacy.12.d": (
        "Emperor Karl I has assured the German Supreme Command of Austria-Hungary's unwavering commitment to the Central Powers, renouncing all separate negotiations with Paris or London.",
        "O Imperador Karl I garantiu ao Comando Supremo Alemão o compromisso inabalável da Áustria-Hungria com as Potências Centrais, renunciando a quaisquer negociações separadas com Paris ou Londres.",
    ),
    "ww1_austria_diplomacy.12.a": (
        "Together until final victory!",
        "Juntos até a vitória final!",
    ),
    "ww1_austria_diplomacy.20.t": (
        "The Austro-Polish Solution",
        "A Solução Austro-Polonesa",
    ),
    "ww1_austria_diplomacy.20.d": (
        "Following the expulsion of Russian imperial forces from Congress Poland, the future political status of the Polish lands must be decided. Austrian diplomats advocate the Austro-Polish Solution: uniting Russian Poland with Austrian Galicia under a constitutional kingdom headed by Archduke Karl Stephan of Habsburg, binding a resurrected Poland permanently to Vienna.",
        "Após a expulsão das forças imperiais russas da Polônia do Congresso, o futuro status político das terras polonesas deve ser decidido. Diplomatas austríacos defendem a Solução Austro-Polonesa: unir a Polônia russa com a Galícia austríaca sob um reino constitucional chefiado pelo Arquiduque Karl Stephan de Habsburgo, vinculando uma Polônia ressuscitada permanentemente a Viena.",
    ),
    "ww1_austria_diplomacy.20.a": (
        "Crown Archduke Karl Stephan as King of Poland!",
        "Coroar o Arquiduque Karl Stephan como Rei da Polônia!",
    ),
    "ww1_austria_diplomacy.20.b": (
        "Cede governance to the German authorities in Warsaw.",
        "Ceder a administração às autoridades alemãs em Varsóvia.",
    ),
    "ww1_austria_diplomacy.30.t": (
        "The Brotfrieden: Bread Peace with Ukraine",
        "O Brotfrieden: A Paz do Pão com a Ucrânia",
    ),
    "ww1_austria_diplomacy.30.d": (
        "Famine conditions grip Vienna and Austrian industrial centers, with workers collapsing in bread lines and food riots erupting weekly. At Brest-Litovsk, Austro-Hungarian delegates have negotiated a separate peace treaty with the Ukrainian People's Republic. In exchange for diplomatic recognition and territorial assurances in the Kholm region, Ukraine agrees to deliver one million tons of grain, sugar, and livestock to relieve the starving Dual Monarchy.",
        "Condições de fome assolam Viena e os centros industriais austríacos, com operários desmaiando em filas de pão e revoltas explodindo a cada semana. Em Brest-Litovsk, delegados austro-húngaros negociaram um tratado de paz em separado com a República Popular da Ucrânia. Em troca de reconhecimento diplomático e garantias territoriais na região de Kholm, a Ucrânia concorda em entregar um milhão de toneladas de grãos, açúcar e gado para socorrer a combalida Monarquia Dual.",
    ),
    "ww1_austria_diplomacy.30.a": (
        "Ratify the treaty! Grain will save the Monarchy!",
        "Ratificar o tratado! O pão salvará a Monarquia!",
    ),
    "ww1_austria_diplomacy.30.b": (
        "Refuse concessions over the disputed Kholm territory.",
        "Recusar concessões sobre o território disputado de Kholm.",
    ),

    # -------------------------------------------------------------
    # COSMETIC TAGS
    # -------------------------------------------------------------
    "HUN_AUS_danubian_state": (
        "Kingdom of Hungary",
        "Reino da Hungria",
    ),
    "HUN_AUS_danubian_state_DEF": (
        "The Kingdom of Hungary",
        "O Reino da Hungria",
    ),
    "CZE_AUS_danubian_state": (
        "Kingdom of Bohemia",
        "Reino da Boêmia",
    ),
    "CZE_AUS_danubian_state_DEF": (
        "The Kingdom of Bohemia",
        "O Reino da Boêmia",
    ),
    "CRO_AUS_danubian_state": (
        "Kingdom of Croatia-Slavonia",
        "Reino da Croácia-Eslavônia",
    ),
    "CRO_AUS_danubian_state_DEF": (
        "The Kingdom of Croatia-Slavonia",
        "O Reino da Croácia-Eslavônia",
    ),
    "POL_AUS_danubian_state": (
        "Kingdom of Poland",
        "Reino da Polônia",
    ),
    "POL_AUS_danubian_state_DEF": (
        "The Kingdom of Poland",
        "O Reino da Polônia",
    ),

    # -------------------------------------------------------------
    # VARIABLES & CROWN DASHBOARD
    # -------------------------------------------------------------
    "AUH_war_weariness": (
        "Imperial War Weariness",
        "Cansaço de Guerra Imperial",
    ),
    "AUH_cohesion": (
        "Imperial Cohesion",
        "Coesão Imperial",
    ),
    "AUH_vienna_grain": (
        "Vienna Grain Stockpile",
        "Estoque de Grãos de Viena",
    ),

    # -------------------------------------------------------------
    # TOOLTIPS & OPINION MODIFIERS
    # -------------------------------------------------------------
    "ww1_austria_diplomacy.1.a_tt": (
        "Mobilization plans will be restructured, removing Russian advance intelligence advantages.",
        "Os planos de mobilização serão reformulados, eliminando a vantagem russa de inteligência prévia.",
    ),
    "ww1_austria_diplomacy.1.b_tt": (
        "Covering up Redl's espionage leaves Austrian deployment schedules compromised against Russia.",
        "Encobrir a espionagem de Redl deixa os planos de desdobramento austríacos comprometidos contra a Rússia.",
    ),
    "ww1_austria_diplomacy.10.a_tt": (
        "Secret envoys will approach Paris to explore conditions for a separate peace.",
        "Enviados secretos abordarão Paris para sondar condições para uma paz separada.",
    ),
    "ww1_austria_diplomacy.10.b_tt": (
        "Austria affirms iron loyalty to the Central Powers, reassuring Germany.",
        "A Áustria afirma lealdade de ferro às Potências Centrais, tranquilizando a Alemanha.",
    ),
    "ww1_austria_diplomacy.20.a_tt": (
        "Archduke Karl Stephan takes the Polish crown, establishing a loyal Habsburg client state.",
        "O Arquiduque Karl Stephan assume a coroa polonesa, estabelecendo um estado cliente leal aos Habsburgo.",
    ),
    "ww1_austria_diplomacy.20.b_tt": (
        "Germany will govern Warsaw, improving bilateral relations at the cost of Austrian influence.",
        "A Alemanha administrará Varsóvia, melhorando relações bilaterais às custas da influência austríaca.",
    ),
    "ww1_austria_diplomacy.30.a_tt": (
        "Agricultural shipments from Ukraine arrive in Vienna, filling grain reserves by §G+40§! and subduing war weariness.",
        "Carregamentos agrícolas da Ucrânia chegam a Viena, aumentando as reservas de grãos em §G+40§! e reduzindo o cansaço de guerra.",
    ),
    "ww1_austria_diplomacy.30.b_tt": (
        "Refusing the treaty deepens famine in Austrian cities, driving war weariness up by §R+15§!.",
        "Recusar o tratado aprofunda a fome nas cidades austríacas, aumentando o cansaço de guerra em §R+15§!.",
    ),
    "AUH_dec_prince_wied_albania_tt": (
        "Extends diplomatic backing to Albania, enhancing Habsburg prestige in the southern Balkans.",
        "Estende apoio diplomático à Albânia, aumentando o prestígio dos Habsburgo no sul dos Bálcãs.",
    ),
    "AUH_dec_danubian_customs_union_tt": (
        "Fosters trade across the Danube river basin, boosting grain reserves and cohesion.",
        "Estimula o comércio em toda a bacia do Danúbio, aumentando reservas de grãos e coesão.",
    ),
    "AUH_ww1_alliance_renewed": (
        "Alliance Reaffirmed",
        "Aliança Reafirmada",
    ),
}


def build_yaml(lang_tag: str, is_english: bool) -> bytes:
    lines = [f"{lang_tag}:"]
    idx = 0 if is_english else 1
    for key, vals in LOC_DATA.items():
        text = vals[idx].replace('"', '\\"')
        lines.append(f' {key}:0 "{text}"')
    content = "\n".join(lines) + "\n"
    # Single UTF-8 BOM
    return b"\xef\xbb\xbf" + content.encode("utf-8")


def main():
    eng_path = os.path.join(REPO_ROOT, "localisation", "english", "ww1_austria_rework_l_english.yml")
    por_path = os.path.join(REPO_ROOT, "localisation", "braz_por", "ww1_austria_rework_l_braz_por.yml")

    os.makedirs(os.path.dirname(eng_path), exist_ok=True)
    os.makedirs(os.path.dirname(por_path), exist_ok=True)

    eng_bytes = build_yaml("l_english", True)
    por_bytes = build_yaml("l_braz_por", False)

    with open(eng_path, "wb") as f:
        f.write(eng_bytes)
    with open(por_path, "wb") as f:
        f.write(por_bytes)

    print(f"Wrote {len(LOC_DATA)} keys to {eng_path} ({len(eng_bytes)} bytes)")
    print(f"Wrote {len(LOC_DATA)} keys to {por_path} ({len(por_bytes)} bytes)")


if __name__ == "__main__":
    main()
