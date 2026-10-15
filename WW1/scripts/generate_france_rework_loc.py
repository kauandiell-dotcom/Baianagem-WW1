"""
Generate bilingual localization files for French Republic Overhaul and Agadir Crisis.
Ensures single UTF-8 BOM (0xef, 0xbb, 0xbf), zero double BOM, and 100% key parity.
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MOD_ROOT = os.path.dirname(SCRIPT_DIR)

EN_PATH = os.path.join(MOD_ROOT, "localisation", "english", "ww1_france_rework_l_english.yml")
PT_PATH = os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_france_rework_l_braz_por.yml")

# Data dictionary: key -> (english_text, portuguese_text)
LOC_ENTRIES = {
    # =========================================================================
    # AGADIR CRISIS (1911) ESCALATION ENGINE
    # =========================================================================
    "ww1_agadir_crisis": (
        "Agadir Crisis of 1911",
        "Crise de Agadir de 1911"
    ),
    "ww1_agadir_crisis_desc": (
        "The arrival of the gunboat SMS Panther in the Moroccan port of Agadir has triggered an acute international confrontation. The European powers must navigate ultimata, naval mobilizations, and colonial compensations to prevent early world war.",
        "A chegada da canhoneira SMS Panther ao porto marroquino de Agadir desencadeou uma grave confrontação internacional. As potências europeias devem navegar por ultimatos, mobilizações navais e compensações coloniais para impedir uma guerra mundial prematura."
    ),
    "ww1_agadir_crisis_tension": (
        "Agadir Crisis Tension",
        "Tensão da Crise de Agadir"
    ),
    "ww1_agadir_tension_increase_tt": (
        "§RIncreases Agadir Crisis Tension§!",
        "§RAumenta a Tensão da Crise de Agadir§!"
    ),
    "ww1_agadir_tension_decrease_tt": (
        "§GDecreases Agadir Crisis Tension§!",
        "§GReduz a Tensão da Crise de Agadir§!"
    ),
    "FRA_morocco_treaty_of_fez": (
        "Treaty of Fez & Moroccan Protectorate",
        "Tratado de Fez e Protetorado Marroquino"
    ),
    "FRA_morocco_treaty_of_fez_desc": (
        "The peaceful resolution of the Agadir Crisis confirms our sovereign protectorate over Morocco, securing French dominance across Northwest Africa.",
        "A resolução pacífica da Crise de Agadir confirma nosso protetorado soberano sobre o Marrocos, assegurando o domínio francês no noroeste da África."
    ),
    "FRA_poincare_national_firmness": (
        "Poincaré's Policy of Firmness",
        "Política de Firmeza de Poincaré"
    ),
    "FRA_poincare_national_firmness_desc": (
        "Raymond Poincaré brings uncompromising resolve to French diplomacy, consolidating the Entente Cordiale and deterring German aggression.",
        "Raymond Poincaré imprime determinação intransigente à diplomacia francesa, consolidando a Entente Cordiale e dissuadindo a agressão alemã."
    ),

    # German Decisions
    "GER_agadir_demand_naval_base": (
        "Demand Atlantic Naval Station at Agadir",
        "Exigir Base Naval no Atlântico em Agadir"
    ),
    "GER_agadir_demand_naval_base_desc": (
        "Assert the Kaiserliche Marine's right to establish a fortified coaling base on the Atlantic coast of Morocco, securing a permanent German strategic foothold.",
        "Afirmar o direito da Kaiserliche Marine de estabelecer uma base carvoeira fortificada na costa atlântica do Marrocos, assegurando um ponto de apoio estratégico permanente para a Alemanha."
    ),
    "GER_agadir_demand_congo_compensation": (
        "Demand Neukamerun Colonial Compensation",
        "Exigir Compensação Territorial de Neukamerun"
    ),
    "GER_agadir_demand_congo_compensation_desc": (
        "If France claims Morocco as an exclusive sphere of influence, Germany must receive substantial territorial cessions in French Equatorial Africa to enlarge Kamerun.",
        "Se a França reivindica o Marrocos como esfera exclusiva de influência, a Alemanha deve receber cessões territoriais substanciais na África Equatorial Francesa para expandir Camarões."
    ),
    "GER_agadir_send_sms_berlin": (
        "Dispatch SMS Berlin as Reinforcement",
        "Enviar SMS Berlin como Reforço"
    ),
    "GER_agadir_send_sms_berlin_desc": (
        "Reinforce SMS Panther with the light cruiser SMS Berlin, demonstrating Imperial Germany's unwavering resolve to back its diplomatic demands with naval steel.",
        "Reforçar o SMS Panther com o cruzador ligeiro SMS Berlin, demonstrando a determinação inabalável do Império Alemão em respaldar suas exigências diplomáticas com o poder naval."
    ),
    "GER_agadir_back_down_gracefully": (
        "Withdraw the Panther and De-escalate",
        "Retirar o Panther e Desescalar a Crise"
    ),
    "GER_agadir_back_down_gracefully_desc": (
        "With financial panic on the Berlin Börse and the Royal Navy mobilizing, prudent withdrawal avoids an untimely world war before our High Seas Fleet is completed.",
        "Diante do pânico financeiro na Bolsa de Berlim e da mobilização da Marinha Real, um recuo prudente evita uma guerra mundial precipitada antes da conclusão da nossa Frota de Alto-Mar."
    ),

    # French Decisions
    "FRA_agadir_caillaux_secret_channel": (
        "Caillaux's Secret Diplomatic Channel",
        "Canal Diplomático Secreto de Caillaux"
    ),
    "FRA_agadir_caillaux_secret_channel_desc": (
        "Premier Joseph Caillaux opens confidential back-channel communications with Berlin to negotiate a pragmatic territorial settlement away from hawkish interference.",
        "O Primeiro-Ministro Joseph Caillaux abre negociações confidenciais diretas com Berlim para alcançar um acordo territorial pragmático, contornando a ingerência dos setores belicistas."
    ),
    "FRA_agadir_delcasse_firm_resolve": (
        "Delcassé's Policy of Resolute Defiance",
        "Política de Firmeza Inabalável de Delcassé"
    ),
    "FRA_agadir_delcasse_firm_resolve_desc": (
        "The Minister of the Navy Théophile Delcassé urges unwavering resistance against German blackmail, rallying public opinion and coordinating closely with London.",
        "O Ministro da Marinha Théophile Delcassé defende resistência intransigente contra a chantagem alemã, mobilizando a opinião pública e coordenando ações de defesa com Londres."
    ),
    "FRA_agadir_financial_sanctions": (
        "Withdraw French Capital from Berlin",
        "Retirar Capital Francês de Berlim"
    ),
    "FRA_agadir_financial_sanctions_desc": (
        "Order French financial houses to liquidate short-term loans and pull credit from German markets, inducing an immediate liquidity squeeze on the Berlin stock exchange.",
        "Instruir as instituições financeiras francesas a liquidar empréstimos de curto prazo e resgatar créditos do mercado alemão, provocando uma crise imediata de liquidez na bolsa de valores de Berlim."
    ),
    "FRA_agadir_concede_congo_accord": (
        "Ratify the Morocco-Congo Exchange Accord",
        "Ratificar o Acordo de Troca Marrocos-Congo"
    ),
    "FRA_agadir_concede_congo_accord_desc": (
        "Conclude the bilateral agreement ceding sections of French Equatorial Africa to German Kamerun in exchange for Berlin's formal recognition of our Moroccan protectorate.",
        "Celebrar o acordo bilateral que cede partes da África Equatorial Francesa ao Camarões alemão em troca do reconhecimento formal de Berlim ao nosso protetorado no Marrocos."
    ),
    "FRA_agadir_concede_naval_station": (
        "Concede Naval Coaling Base to Germany",
        "Conceder Estação Naval Carvoeira à Alemanha"
    ),
    "FRA_agadir_concede_naval_station_desc": (
        "Capitulate to the Kaiser's demands and grant Germany sovereign coaling rights in Agadir, preserving fragile European peace at the heavy cost of national prestige.",
        "Capitular perante as exigências do Kaiser e conceder à Alemanha direitos soberanos de abastecimento naval em Agadir, preservando a frágil paz europeia ao alto custo do prestígio nacional."
    ),

    # British Decisions
    "ENG_agadir_mansion_house_speech": (
        "Lloyd George's Mansion House Speech",
        "Discurso de Mansion House de Lloyd George"
    ),
    "ENG_agadir_mansion_house_speech_desc": (
        "Chancellor David Lloyd George delivers a stern address warning Berlin that Britain will not permit its vital global interests to be sidelined by unilateral German threats.",
        "O Chanceler David Lloyd George pronuncia um discurso enérgico alertando Berlim de que a Grã-Bretanha não permitirá que seus interesses globais vitais sejam desconsiderados por ameaças unilaterais alemãs."
    ),
    "ENG_agadir_home_fleet_alert": (
        "Place the Home Fleet on War Footing",
        "Colocar a Home Fleet em Prontidão de Guerra"
    ),
    "ENG_agadir_home_fleet_alert_desc": (
        "Concentrate British battle squadrons at Portland and Scapa Flow, making it unmistakable that the Royal Navy stands shoulder-to-shoulder with France in the Channel.",
        "Concentrar os esquadrões de batalha britânicos em Portland e Scapa Flow, deixando evidente que a Marinha Real defenderá as costas francesas e o Canal contra qualquer incursão alemã."
    ),
    "ENG_agadir_urge_moderation": (
        "Urge Entente Moderation and Compromise",
        "Recomendar Moderação e Acordo na Entente"
    ),
    "ENG_agadir_urge_moderation_desc": (
        "Counsel Paris to seek an equitable colonial accommodation, avoiding an unprovoked conflagration over secondary West African river valleys.",
        "Aconselhar Paris a buscar uma solução colonial equilibrada, evitando uma conflagração desnecessária por bacias fluviais secundárias na África Ocidental."
    ),

    # Agadir Events
    "ww1_agadir.1.t": (
        "The Panthersprung: SMS Panther at Agadir",
        "O Panthersprung: SMS Panther em Agadir"
    ),
    "ww1_agadir.1.d": (
        "On July 1, 1911, the German gunboat SMS Panther dropped anchor in the closed Moroccan port of Agadir under the pretext of shielding German merchants. In truth, Berlin seeks to fracture the Anglo-French Entente and demand substantial colonial spoils in Africa. The capitals of Europe are gripped by tension.",
        "Em 1º de julho de 1911, a canhoneira alemã SMS Panther lançou âncora no porto marroquino de Agadir sob a justificativa de proteger comerciantes germânicos. Na verdade, Berlim procura fraturar a Entente Anglo-Francesa e exigir ganhos coloniais substanciais na África. A apreensão toma conta das capitais europeias."
    ),
    "ww1_agadir.1.a": (
        "Germany demands its place in the sun!",
        "A Alemanha exige o seu lugar ao sol!"
    ),
    "ww1_agadir.1.b": (
        "Disavow the deployment and preserve peace",
        "Desautorizar a expedição e preservar a paz"
    ),

    "ww1_agadir.2.t": (
        "French Outrage over the Agadir Intrusion",
        "Indignação Francesa com a Incursão em Agadir"
    ),
    "ww1_agadir.2.d": (
        "News of the Panther's arrival in Moroccan waters has provoked intense patriotic fury in Paris. The press and parliament denounce this naked act of gunboat diplomacy as a flagrant violation of the Act of Algeciras.",
        "A notícia da chegada do Panther em águas marroquinas provocou intensa comoção patriótica em Paris. A imprensa e a Câmara denunciam esse ato descarado de diplomacia de canhoneira como uma violação frontal da Ata de Algeciras."
    ),
    "ww1_agadir.2.a": (
        "The Republic will never yield to blackmail!",
        "A República jamais se curvará a chantagens!"
    ),

    "ww1_agadir.3.t": (
        "British Alarm over German Naval Ambitions",
        "Alarme Britânico com as Ambições Navais Alemãs"
    ),
    "ww1_agadir.3.d": (
        "The British Cabinet regards the presence of a German warship on Morocco's Atlantic coast as a direct peril to the vital sea lanes flanking Gibraltar. Whitehall firmly affirms its diplomatic solidarity with France.",
        "O Gabinete britânico enxerga a presença de um vaso de guerra alemão no litoral atlântico do Marrocos como uma ameaça palpável às rotas vitais do Estreito de Gibraltar. Whitehall manifesta sólida comunhão diplomática com a França."
    ),
    "ww1_agadir.3.a": (
        "Britain stands beside France.",
        "A Grã-Bretanha permanece ao lado da França."
    ),

    "ww1_agadir.4.t": (
        "German Demand: Atlantic Naval Base",
        "Exigência Alemã: Base Naval no Atlântico"
    ),
    "ww1_agadir.4.d": (
        "The German government submits an ambitious memorandum insisting upon sovereign coaling facilities in Agadir, asserting that Germany requires a permanent base to protect its Atlantic commercial navigation.",
        "O governo alemão apresenta um memorando exigindo a concessão soberana do porto de Agadir para instalar uma estação carvoeira, sob o pretexto de proteger a navegação comercial alemã no Atlântico."
    ),
    "ww1_agadir.4.a": (
        "Categorically reject! Not an inch of territory!",
        "Rejeitar taxativamente! Nem um centímetro de solo!"
    ),
    "ww1_agadir.4.b": (
        "Accede to avoid an immediate war",
        "Ceder para evitar uma guerra imediata"
    ),

    "ww1_agadir.5.t": (
        "Berlin Proposes Neukamerun Border Compensation",
        "Berlim Propõe Compensação Territorial em Neukamerun"
    ),
    "ww1_agadir.5.d": (
        "Berlin indicates that German objections to France's Moroccan protectorate can be resolved if Paris transfers expansive riverine territories in the French Congo to enlarge German Kamerun.",
        "Berlim faz saber que as objeções alemãs ao protetorado francês no Marrocos serão retiradas se Paris transferir territórios fluviais expressivos no Congo Francês para expandir o Camarões alemão."
    ),
    "ww1_agadir.5.a": (
        "Open diplomatic negotiations on colonial frontiers",
        "Abrir negociações diplomáticas sobre as fronteiras coloniais"
    ),
    "ww1_agadir.5.b": (
        "Refuse to entertain German extortion!",
        "Recusar peremptoriamente a extorsão alemã!"
    ),

    "ww1_agadir.10.t": (
        "The Morocco-Congo Accord & Treaty of Fez",
        "O Acordo Marrocos-Congo e o Tratado de Fez"
    ),
    "ww1_agadir.10.d": (
        "Diplomacy and compromise have triumphed over conflict. France and Germany have concluded the Franco-German Accord and Treaty of Fez. Germany acknowledges France's protectorate over Morocco, while France transfers 275,000 square kilometers of equatorial territory to German Kamerun (Neukamerun). The crisis is laid to rest.",
        "A diplomacia e o equilíbrio prevaleceram sobre as armas. A França e a Alemanha firmaram o Acordo Franco-Alemão e o Tratado de Fez. A Alemanha reconhece o protetorado francês sobre o Marrocos, enquanto a França transfere 275.000 quilômetros quadrados na África Equatorial ao Camarões alemão (Neukamerun). A crise é superada."
    ),
    "ww1_agadir.10.a": (
        "Peace is secured through diplomatic compromise.",
        "A paz foi salvaguardada por meio do compromisso diplomático."
    ),

    "ww1_agadir.11.t": (
        "Morocco Accord Ratified",
        "Acordo do Marrocos Ratificado"
    ),
    "ww1_agadir.11.d": (
        "The diplomatic agreement settling Moroccan status and Congolese border adjustments has been officially ratified by the signatory powers.",
        "O tratado diplomático sobre a situação marroquina e a retificação de fronteiras no Congo foi formalmente ratificado pelas nações signatárias."
    ),
    "ww1_agadir.11.a": (
        "A peaceful settlement.",
        "Uma resolução pacífica e ordenada."
    ),

    "ww1_agadir.20.t": (
        "Pan-German Triumph: Naval Station at Agadir",
        "Triunfo Pangermânico: Estação Naval em Agadir"
    ),
    "ww1_agadir.20.d": (
        "In an astonishing diplomatic capitulation, the French government has ceded naval port privileges in Agadir to the German Empire. The Kaiserliche Marine gains a heavily fortified Atlantic station flanking British trade corridors. Nationalist circles in Berlin celebrate a historic coup, while Paris reels in bitter humiliation.",
        "Numa rendição diplomática surpreendente, o governo francês cedeu direitos navais soberanos no porto de Agadir ao Império Alemão. A Kaiserliche Marine estabelece uma base fortificada no Atlântico que flanqueia as rotas mercantes britânicas. Setores nacionalistas em Berlim celebram, enquanto Paris afunda em consternação."
    ),
    "ww1_agadir.20.a": (
        "A monumental shift in the balance of naval power.",
        "Uma reviravolta sem precedentes no equilíbrio do poder naval."
    ),

    "ww1_agadir.30.t": (
        "The German Retreat: Panther Recalled",
        "O Recuo Alemão: Panther Despachado de Volta"
    ),
    "ww1_agadir.30.d": (
        "Staring down British naval mobilization and an accelerating financial crisis on the Berlin stock market, the Imperial German government has ordered the Panther to weigh anchor and depart Agadir without obtaining any colonial concessions. France celebrates an unmitigated triumph of deterrence.",
        "Diante da firme mobilização da frota britânica e de uma grave turbulência nos mercados de capitais em Berlim, o governo alemão determinou a partida do Panther de Agadir sem conquistar nenhuma compensação colonial. A França celebra uma vitória expressiva de dissuasão."
    ),
    "ww1_agadir.30.a": (
        "A humiliating diplomatic defeat for Berlin.",
        "Uma derrota diplomática desmoralizante para Berlim."
    ),

    "ww1_agadir.40.t": (
        "The Premature Conflagration: World War in 1911",
        "A Conflagração Prematura: Guerra Mundial em 1911"
    ),
    "ww1_agadir.40.d": (
        "Unrelenting escalation, aggressive naval posturing, and uncompromising ultimata have shattered European diplomacy. What began as a colonial dispute in Morocco has ignited a catastrophic clash between the Entente and the Central Powers. The Great War has erupted three years early!",
        "A escalada bélica descontrolada, demonstrações de força no mar e ultimatos inflexíveis destruíram a via diplomática europeia. O que começou como uma contenda colonial no Marrocos detonou um confronto colossal entre a Entente e as Potências Centrais. A Grande Guerra irrompeu três anos antes do previsto!"
    ),
    "ww1_agadir.40.a": (
        "Aux armes, citoyens!",
        "Aux armes, citoyens!"
    ),

    # =========================================================================
    # REPUBLIC DASHBOARD & SURVIVAL VECTORS
    # =========================================================================
    "FRA_union_sacree_cohesion": (
        "Union Sacrée Cohesion",
        "Coesão da União Sagrada"
    ),
    "FRA_poilu_morale": (
        "Poilu Morale",
        "Moral dos Poilus"
    ),
    "FRA_charbon_et_acier": (
        "Charbon et Acier (Coal & Steel)",
        "Carvão e Aço (Combustível e Metalurgia)"
    ),
    "FRA_reserves_humaines": (
        "Réserves Humaines (Manpower Pool)",
        "Reservas Humanas (Mão de Obra Militar)"
    ),

    "FRA_union_sacree_strong": (
        "Resilient Union Sacrée",
        "União Sagrada Inabalável"
    ),
    "FRA_union_sacree_strong_desc": (
        "From socialist syndicalists to royalist conservatives, the entire French political spectrum observes a sacred domestic truce in steadfast defense of the Fatherland.",
        "Dos operários socialistas aos nobres monarquistas, todo o espectro político francês adere à trégua sagrada na defesa patriótica irrestrita da República."
    ),
    "FRA_union_sacree_fractured": (
        "Fractured Union Sacrée",
        "União Sagrada Fraturada"
    ),
    "FRA_union_sacree_fractured_desc": (
        "Partisan recriminations, ideological clashes, and war weariness have severely undermined political consensus, threatening parliamentary paralysis.",
        "Atritos partidários, dissidências ideológicas e o cansaço da guerra corroeram o consenso político na Câmara, arriscando paralisar a administração."
    ),
    "FRA_poilu_morale_high": (
        "High Poilu Morale",
        "Moral Elevado dos Poilus"
    ),
    "FRA_poilu_morale_high_desc": (
        "The French soldier stands resolute in the muddy trenches, buoyed by profound patriotic devotion and unshakable faith in ultimate victory.",
        "O combatente francês nas trincheiras enlameadas persevera com bravura indomável, impulsionado por devoção patriótica e certeza na vitória."
    ),
    "FRA_poilu_morale_demoralized": (
        "Demoralized Poilus",
        "Poilus Desmoralizados"
    ),
    "FRA_poilu_morale_demoralized_desc": (
        "Repeated meatgrinder offensives and miserable frontline conditions have eroded the fighting will of the infantry, breeding widespread despair and insubordination.",
        "Ofensivas frontais frustradas e as condições desumanas das trincheiras quebraram a disposição de luta da tropa, gerando insubordinação e revolta."
    ),
    "FRA_charbon_et_acier_surplus": (
        "Abundant Coal & Steel",
        "Superávit de Carvão e Aço"
    ),
    "FRA_charbon_et_acier_surplus_desc": (
        "Sustained domestic extraction and allied maritime supply lines keep French foundries, blast furnaces, and shell-machining shops operating at peak efficiency.",
        "A extração interna eficiente e as rotas marítimas aliadas abastecem as siderúrgicas e fábricas de projéteis com ritmo de produção implacável."
    ),
    "FRA_charbon_et_acier_famine": (
        "Critical Coal & Steel Deficit",
        "Déficit Crítico de Carvão e Aço"
    ),
    "FRA_charbon_et_acier_famine_desc": (
        "With the northern metallurgical basin in German hands and merchant shipping squeezed, acute shortages of coking coal cripple national weapons manufacture.",
        "Com as jazidas carboníferas do norte sob controle inimigo e os transportes marítimos estrangulados, a carência de combustível asfixia as oficinas bélicas."
    ),

    "FRA_dec_british_channel_coal": (
        "British Channel Coal Convoys",
        "Comboios de Carvão Britânico pelo Canal"
    ),
    "FRA_dec_british_channel_coal_desc": (
        "Organize dedicated coal convoys escorted across the English Channel to supply Welsh steam coal directly to French coastal munitions plants and foundries.",
        "Organizar comboios de mercantes escoltados através do Canal da Mancha para fornecer carvão galês de primeira linha diretamente às usinas siderúrgicas francesas."
    ),
    "FRA_dec_call_up_class_1917": (
        "Call Up the Class of 1917 (Les Bleuets)",
        "Convocar a Classe de 1917 (Les Bleuets)"
    ),
    "FRA_dec_call_up_class_1917_desc": (
        "Mobilize the youthful conscript contingent ahead of statutory age to reconstitute shattered frontline divisions, notwithstanding the tragic human cost.",
        "Antecipar a incorporação da classe de jovens conscritos de dezoito anos para reconstituir as divisões desgastadas no fronte, assumindo o doloroso custo humano."
    ),
    "FRA_dec_colonial_recruitment_tirailleurs": (
        "Colonial Conscription: Tirailleurs Sénégalais",
        "Recrutamento Colonial: Tirailleurs Senegaleses"
    ),
    "FRA_dec_colonial_recruitment_tirailleurs_desc": (
        "Intensify troop levies across French West Africa, the Maghreb, and Indochina to furnish courageous colonial formations for frontline duty in Europe.",
        "Intensificar a conscrição e o alistamento voluntário na África Ocidental Francesa, no Magrebe e na Indochina para incorporar valorosas divisões coloniais no fronte europeu."
    ),
    "FRA_dec_union_sacree_cross_party_pact": (
        "Union Sacrée Cross-Party Concordat",
        "Pacto Interpartidário da União Sagrada"
    ),
    "FRA_dec_union_sacree_cross_party_pact_desc": (
        "Gather leaders of all parliamentary groups in the Palais Bourbon to renew mutual pledges of national unity and suspend partisan discord until victory is achieved.",
        "Reunir as lideranças de todas as bancadas no Palais Bourbon para renovar os votos de concórdia nacional e banir as intrigas partidárias até o triunfo final."
    ),

    # =========================================================================
    # 1917 CRISES, MUTINIES & ENDSIEG
    # =========================================================================
    "FRA_trench_mutiny_crisis_2": (
        "1917 French Army Mutinies",
        "Motins do Exército Francês de 1917"
    ),
    "FRA_trench_mutiny_crisis_2_desc": (
        "In the catastrophic wake of the Nivelle Offensive along the Chemin des Dames, widespread mutinies have erupted. Troops refuse suicidal frontal assaults while pledging to defend their own trenches.",
        "Após a carnificina inglória no Chemin des Dames, ondas de motins explodiram em regimentos inteiros. As tropas rejeitam investidas suicidas, embora permaneçam decididas a defender as linhas francesas."
    ),
    "FRA_poilus_reconcilies": (
        "Reconciled Poilus (Pétain's Reforms)",
        "Poilus Reconciliados (Reformas de Pétain)"
    ),
    "FRA_poilus_reconcilies_desc": (
        "General Philippe Pétain has rebuilt frontline confidence through compassionate leadership: regular leave, nutritious food, decent rest camps, and an end to futile human-wave attacks.",
        "O General Philippe Pétain recuperou a lealdade das tropas através de medidas atenciosas: concessão de licenças, alimentação quente, repouso adequado e suspensão de ataques frontais temerários."
    ),
    "FRA_munitionnettes_strike": (
        "Munitionnettes Strike Waves",
        "Greve das Munitionnettes"
    ),
    "FRA_munitionnettes_strike_desc": (
        "Female arms factory workers across Paris have walked off the assembly lines, striking against intolerable inflation, starvation wages, and grueling fourteen-hour shifts.",
        "As operárias da indústria de armamentos de Paris cruzaram os braços em protesto contra a inflação desmedida, remunerações aviltantes e jornadas estafantes de catorze horas."
    ),
    "FRA_jusqu_au_bout_endsieg": (
        "Jusqu'au Bout! (Total War to the End)",
        "Jusqu'au Bout! (Guerra Total até o Fim)"
    ),
    "FRA_jusqu_au_bout_endsieg_desc": (
        "\"Home policy? I wage war. Foreign policy? I wage war. All the time, I wage war!\" Premier Georges Clemenceau directs the total physical and moral willpower of France toward final victory.",
        "\"Política interna? Eu faço a guerra. Política externa? Eu faço a guerra. O tempo todo, eu faço a guerra!\" O Primeiro-Ministro Georges Clemenceau canaliza a energia de toda a França na direção da vitória absoluta."
    ),

    "ww1_france.210.t": (
        "The 1917 French Army Mutinies",
        "Os Motins do Exército Francês de 1917"
    ),
    "ww1_france.210.d": (
        "The horrific bloodshed of General Nivelle's promised breakthrough at the Chemin des Dames has exhausted the endurance of the French infantry. Mutinous demonstrations have spread across dozens of frontline divisions. Weary poilus refuse orders to launch senseless frontal assaults against unsuppressed German machine gun redoubts.",
        "O sacrifício brutal exigido na ofensiva do General Nivelle ao longo do Chemin des Dames esgotou as forças da infantaria. Motins eclodiram em dezenas de divisões. Cansados da mortandade fútil, os poilus negam-se a marchar contra posições guarnecidas por metralhadoras inimigas intactas."
    ),
    "ww1_france.210.a": (
        "General Nivelle must be relieved of command immediately!",
        "O General Nivelle deve ser exonerado incontinenti!"
    ),

    "ww1_france.211.t": (
        "General Pétain Appointed Commander-in-Chief",
        "General Pétain Nomeado Comandante-em-Chefe"
    ),
    "ww1_france.211.d": (
        "Philippe Pétain, the architect of defense at Verdun, has been elevated to Commander-in-Chief of the French armies. He promises an end to reckless bloodbaths, pledging to await tanks and American divisions while fundamentally reforming troop welfare, rest cycles, and home leave.",
        "Philippe Pétain, o defensor de Verdun, assume o comando supremo dos exércitos franceses. Ele estanca as ofensivas sanguinárias, assegurando aos soldados que esperará a chegada de blindados e contingentes americanos enquanto aperfeiçoa as condições de vida, descanso e licenças da tropa."
    ),
    "ww1_france.211.a": (
        "Implement Pétain's humanitarian and welfare reforms",
        "Executar as reformas humanitárias e de licenças de Pétain"
    ),
    "ww1_france.211.b": (
        "Impose strict disciplinary tribunals and firing squads",
        "Recorrer a tribunais militares sumários e pelotões de fuzilamento"
    ),

    "ww1_france.215.t": (
        "Munitionnettes Strike in the Capital",
        "Greve das Munitionnettes na Capital"
    ),
    "ww1_france.215.d": (
        "Inflation and crushing war burdens have pushed the female workforce in Parisian armaments factories to the breaking point. Thousands of women have downed tools to demand cost-of-living bonuses, shorter work hours, and immediate peace.",
        "A escalada dos preços e o rigor da jornada fabril levaram a mão de obra feminina dos arsenais de Paris ao esgotamento. Milhares de mulheres paralisaram a produção bélica exigindo reajustes de subsistência, jornadas humanas e o encerramento do conflito."
    ),
    "ww1_france.215.a": (
        "Grant wage increases and maternal work reforms",
        "Conceder reajustes salariais e benefícios de amparo às operárias"
    ),
    "ww1_france.215.b": (
        "Suppress the strikes through police force",
        "Reprimir as manifestações com contingentes policiais"
    ),

    "ww1_france.220.t": (
        "Clemenceau's Declaration: \"Je Fais la Guerre!\"",
        "Discurso de Clemenceau: \"Je Fais la Guerre!\""
    ),
    "ww1_france.220.d": (
        "Taking the reins of government at age 76, Georges Clemenceau electrifies the Chamber of Deputies with uncompromising oratorical fury: \"No more pacifist illusions! No more defeatist propaganda! Neither treason nor semi-treason: war! Nothing but war!\" The entire nation rallies with fierce resolve.",
        "Tomando a liderança do governo aos 76 anos de idade, Georges Clemenceau eletriza a Câmara dos Deputados com fervor patriótico inabalável: \"Basta de ilusões pacifistas! Nada de propaganda derrotista! Nem traição nem meia traição: guerra! Nada senão a guerra!\" O país cerra fileiras com ânimo renovado."
    ),
    "ww1_france.220.a": (
        "Jusqu'au bout! Victory or death!",
        "Jusqu'au bout! Vitória ou ruína!"
    ),

    "FRA_petain_welfare_reforms_unlocked_tt": (
        "§GUnlocks Pétain's Welfare & Leave Reform decision to resolve the mutiny crisis.§!",
        "§GDesbloqueia a decisão de Reformas Assistenciais e de Licenças de Pétain para encerrar a crise dos motins.§!"
    ),
    "FRA_petain_welfare_and_leave_reform": (
        "Pétain's Welfare & Leave Reforms",
        "Reformas Assistenciais e de Licenças de Pétain"
    ),
    "FRA_petain_welfare_and_leave_reform_desc": (
        "Enact General Pétain's vital welfare program: guaranteed seven-day furloughs, hygienic rest cantonments, warm rations, and strict limits on tactical offensive operations until allied material superiority is ensured.",
        "Cumprir as medidas assistenciais prometidas por Pétain: concessão obrigatória de folgas periódicas, cantonamentos higienizados, comida quente e a suspensão de investidas prematuras até dispor de franca supremacia material."
    ),

    # =========================================================================
    # THE 4 DIVERGENT POLITICAL DESTINIES & CHARACTERS
    # =========================================================================
    "FRA_republique_union_sacree": (
        "[Historical] The Union Sacrée Republic",
        "[Histórico] A República da União Sagrada"
    ),
    "FRA_republique_union_sacree_desc": (
        "Reaffirm the sacred truce of the Third Republic, uniting all French citizens regardless of political allegiance or religious creed in common defense of the motherland.",
        "Reafirmar a trégua sagrada da Terceira República, congregando todos os franceses sem distinção partidária ou religiosa na salvaguarda da terra natal."
    ),
    "FRA_clemenceau_je_fais_la_guerre": (
        "[Historical] Je Fais la Guerre",
        "[Histórico] Je Fais la Guerre"
    ),
    "FRA_clemenceau_je_fais_la_guerre_desc": (
        "Install Georges Clemenceau as Premier with sweeping war powers to purge defeatism, invigorate the high command, and relentlessly pursue complete victory.",
        "Empossar Georges Clemenceau na chefia do governo com poderes extraordinários para extirpar o derrotismo, revigorar a oficialidade e buscar incansavelmente a vitória cabal."
    ),
    "FRA_republique_des_soviets_de_paris": (
        "[Alternative - Socialist] The Paris Soviet Republic",
        "[Alternativo - Socialista] A República Soviética de Paris"
    ),
    "FRA_republique_des_soviets_de_paris_desc": (
        "Proclaim the Second Paris Commune! Dissolve the bourgeois parliament and transfer executive power to revolutionary worker councils and soldier soviets.",
        "Proclamar a Segunda Comuna de Paris! Dissolver o parlamento burguês e transferir as prerrogativas executivas aos conselhos de operários e sovietes de soldados."
    ),
    "FRA_comite_de_salut_public_1917": (
        "[Alternative - Socialist] Revolutionary Committee of Public Safety",
        "[Alternativo - Socialista] Comitê Revolucionário de Salvação Pública"
    ),
    "FRA_comite_de_salut_public_1917_desc": (
        "Revive the jacobin legacy of 1793. Empower an emergency Committee of Public Safety to requisition private wealth, purge reactionary officers, and arm the proletariat for revolutionary defense.",
        "Retomar as tradições jacobinas de 1793. Investir um Comitê de Salvação Pública para requisitar bens particulares, afastar oficiais reacionários e armar os trabalhadores na defesa da revolução."
    ),
    "FRA_abattre_la_gueuse": (
        "[Alternative - Monarchist] Abattre la Gueuse",
        "[Alternativo - Monarquista] Abattre la Gueuse"
    ),
    "FRA_abattre_la_gueuse_desc": (
        "\"Down with the Whore!\" Action Française leagues and Camelots du Roi mobilize in the streets to sweep away the corrupt parliamentary republic and prepare the royalist restoration.",
        "\"Abaixo a rameira!\" A Action Française e os Camelots du Roi organizam comícios multitudinários para sepultar a república corrupta e pavimentar o retorno da dinastia legítima."
    ),
    "FRA_restauration_orleaniste_jean_iii": (
        "[Alternative - Monarchist] Orléanist Restoration: King Jean III",
        "[Alternativo - Monarquista] Restauração Orleanista: Rei Jean III"
    ),
    "FRA_restauration_orleaniste_jean_iii_desc": (
        "Crowning the Duke of Guise as King Jean III of France, restoring the historic House of Orléans to establish an integral nationalist and constitutional monarchy.",
        "Entronizar o Duque de Guise como Rei Jean III da França, resgatando a linhagem histórica dos Orléans para erguer uma monarquia de nacionalismo integral e raízes católicas."
    ),
    "FRA_directoire_militaire_gqg": (
        "[Alternative - Military Junta] GQG Military Directory",
        "[Alternativo - Junta Militar] Diretório Militar do GQG"
    ),
    "FRA_directoire_militaire_gqg_desc": (
        "Tired of civilian incompetence and political interference, the Grand Quartier Général suspends parliamentary oversight and assumes absolute military executive control.",
        "Insatisfeito com as hesitações civis e os entraves da bancada política, o Grand Quartier Général suspende os ritos constitucionais e institui um diretório militar supremo."
    ),
    "FRA_etat_de_siege_permanent": (
        "[Alternative - Military Junta] Permanent State of Siege",
        "[Alternativo - Junta Militar] Estado de Sítio Permanente"
    ),
    "FRA_etat_de_siege_permanent_desc": (
        "Extend the state of siege indefinitely across all departments, placing transport, war industry, the press, and civil governance under regional military tribunals.",
        "Estender o estado de sítio por tempo indefinido a todos os departamentos, transferindo portos, malhas ferroviárias, censura e administração a oficiais generais."
    ),

    "FRA_union_sacree_spirit": (
        "Spirit of the Union Sacrée",
        "Espírito da União Sagrada"
    ),
    "FRA_union_sacree_spirit_desc": (
        "The indomitable political truce that knits together French society against foreign aggression, overcoming historical sectarian divisions.",
        "A firmeza da união patriótica que ampara o povo francês contra o invasor, sobrepondo o dever nacional a velhas divisões sectárias."
    ),
    "FRA_commune_de_paris_spirit": (
        "Spirit of the Paris Commune",
        "Espírito da Comuna de Paris"
    ),
    "FRA_commune_de_paris_spirit_desc": (
        "Revolutionary proletarian fervor transforms the imperialist conflagration into an emancipatory struggle for workers' liberation.",
        "O fervor revolucionário proletário converte o choque entre impérios numa cruzada emancipatória de libertação das classes trabalhadoras."
    ),
    "FRA_action_francaise_monarchy": (
        "Integral Nationalist Monarchy",
        "Monarquia Nacionalista Integral"
    ),
    "FRA_action_francaise_monarchy_desc": (
        "Charles Maurras's integral nationalism blends traditional royal authority, Catholic heritage, and martial discipline into an authoritarian state.",
        "O ideário de Charles Maurras funde autoridade dinástica, tradição católica e retidão castrense na construção de um regime imune à fraqueza parlamentar."
    ),
    "FRA_gqg_military_directory": (
        "GQG Supreme Directory",
        "Diretório Supremo do GQG"
    ),
    "FRA_gqg_military_directory_desc": (
        "A stern military junta under the general staff subordinates the entire civil economy to the uncompromising imperatives of operational warfare.",
        "Uma junta austera sob a égide do estado-maior condiciona a máquina produtiva e a vida civil aos imperativos irrenunciáveis das operações de campanha."
    ),

    # Characters
    "FRA_charles_maurras": (
        "Charles Maurras",
        "Charles Maurras"
    ),
    "FRA_king_jean_iii": (
        "Jean III",
        "Jean III"
    ),
    "FRA_jean_longuet": (
        "Jean Longuet",
        "Jean Longuet"
    ),
    "FRA_fernand_loriot": (
        "Fernand Loriot",
        "Fernand Loriot"
    ),
    "FRA_georges_clemenceau": (
        "Georges Clemenceau",
        "Georges Clemenceau"
    ),

    # =========================================================================
    # WARTIME INDUSTRIAL & ALLIED DECISIONS
    # =========================================================================
    "FRA_dec_evacuate_briey_machinery": (
        "Evacuate Briey & Longwy Industrial Machinery",
        "Evacuar Maquinário Industrial de Briey e Longwy"
    ),
    "FRA_dec_evacuate_briey_machinery_desc": (
        "Dismantle heavy machine tooling, steam presses, and metallurgical equipment from the vulnerable northeastern frontier and relocate them securely southward to Lyon.",
        "Remover tornos pesados, forjas mecânicas e trens de laminação da conflagrada bacia mineral do nordeste, transportando-os com rapidez para Lyon."
    ),
    "FRA_dec_lyon_chemical_complex": (
        "Expand Lyon Gunpowder & Chemical Complex",
        "Expandir Complexo Químico e de Pólvoras de Lyon"
    ),
    "FRA_dec_lyon_chemical_complex_desc": (
        "Channel substantial capital into the chemical manufacturing facilities of the Rhône valley to massively expand output of high explosives, nitrocellulose, and artillery shells.",
        "Aportar recursos nas instalações fabris de síntese do vale do Ródano para ampliar expressivamente a fabricação de altos explosivos, nitrocelulose e propelentes."
    ),
    "FRA_dec_schneider_creusot_heavy_guns": (
        "Mobilize Schneider-Creusot Heavy Artillery Works",
        "Mobilizar Usinas de Artilharia da Schneider-Creusot"
    ),
    "FRA_dec_schneider_creusot_heavy_guns_desc": (
        "Commission the heavy industrial foundries of Le Creusot to prioritize production of heavy siege howitzers and railway guns to overpower German fortification lines.",
        "Determinar que as fundições industriais de Le Creusot concentrem os fornos na manufatura de obuseiros pesados e peças sobre trilhos para sobrepujar as fortificações alemãs."
    ),
    "FRA_dec_fort_douaumont_reinforcement": (
        "Reinforce Fort Douaumont & Meuse Redoubts",
        "Reforçar o Forte Douaumont e Redutos do Mosa"
    ),
    "FRA_dec_fort_douaumont_reinforcement_desc": (
        "Reinstall armored turrets, casemate guns, and reinforced concrete underground bunkers at Fort Douaumont to establish an unbreachable bastion guarding Verdun.",
        "Remontar cúpulas de aço temperado, peças de casamata e galerias de concreto subterrâneas em Douaumont, consolidando um bastião inexpugnável diante de Verdun."
    ),
    "FRA_dec_voix_sacree_truck_convoys": (
        "La Voie Sacrée Emergency Truck Convoys",
        "Comboios de Caminhões de Emergência da Voie Sacrée"
    ),
    "FRA_dec_voix_sacree_truck_convoys_desc": (
        "Organize a relentless stream of Berliet motor trucks along the Bar-le-Duc artery, transporting reinforcements and artillery ammunition day and night to hold Verdun.",
        "Operar um fluxo rodoviário contínuo de milhares de caminhões Berliet pela rota de Bar-le-Duc, conduzindo reposições e projéteis dia e noite para sustentar Verdun."
    ),
    "FRA_dec_inter_allied_supreme_war_council": (
        "Establish Inter-Allied Supreme War Council",
        "Instituir Conselho Supremo de Guerra Interaliado"
    ),
    "FRA_dec_inter_allied_supreme_war_council_desc": (
        "Form an overarching strategic council of Entente political and military leaders at Versailles to coordinate grand offensives across the Western and Italian fronts.",
        "Constituir em Versalhes um colegiado permanente com líderes da Entente para alinhar planos de campanha e concertar grandes ofensivas no fronte europeu."
    ),
    "FRA_dec_us_morgan_bank_credit_line": (
        "Secure J.P. Morgan & Co. New York Credit Line",
        "Negociar Linha de Crédito com J.P. Morgan & Co."
    ),
    "FRA_dec_us_morgan_bank_credit_line_desc": (
        "Contract crucial loan agreements with the House of Morgan in New York to finance emergency purchases of American steel, nitrates, copper, and foodstuffs.",
        "Contratar expressivos empréstimos junto à casa bancária Morgan em Nova York para cobrir fornecimentos cruciais de aço, cobre, nitratos e alimentos norte-americanos."
    ),

    # Decision Categories
    "FRA_war_economy_and_munitions": (
        "War Economy & Munitions Production",
        "Economia de Guerra e Produção de Munições"
    ),
    "FRA_war_economy_and_munitions_desc": (
        "Strategic management of industrial relocations, arms manufactories, synthetic chemistry works, and coal distribution for total warfare.",
        "Coordenação da transferência de parques fabris, fabricação bélica, indústria química e fornecimento de carvão para a condução da guerra total."
    ),
    "FRA_defence_of_verdun": (
        "Defence of Verdun & Fortress Line",
        "Defesa de Verdun e Linha de Fortalezas"
    ),
    "FRA_defence_of_verdun_desc": (
        "Tactical redeployments, artillery concentrations, and supply lifelines safeguarding the Meuse defensive bastions.",
        "Articulação de reforços táticos, saturação de artilharia e corredores logísticos que sustentam os fortes do Mosa."
    ),
    "FRA_entente_diplomacy": (
        "Entente Diplomacy & Coalition Warfare",
        "Diplomacia da Entente e Esforço de Guerra Aliado"
    ),
    "FRA_entente_diplomacy_desc": (
        "Bilateral treaties, allied strategic synchronization, and overseas war financing to sustain coalition solidarity.",
        "Convênios estratégicos, alinhamento de estado-maior e financiamento externo voltados à coesão da coalizão."
    ),
    "FRA_mutinies_crisis_management": (
        "1917 Mutinies Crisis Management",
        "Gestão da Crise dos Motins de 1917"
    ),
    "FRA_mutinies_crisis_management_desc": (
        "Emergency civil and military initiatives to calm industrial unrest, suppress sedition, and rebuild infantry fighting spirit.",
        "Resoluções imediatas de cunho civil e castrense para suplantar o descontentamento fabril, coibir revoltas e resgatar a moral militar."
    ),
    "FRA_third_republic_politics": (
        "Third Republic Politics",
        "Política da Terceira República"
    ),
    "FRA_third_republic_politics_desc": (
        "Managing cross-party alliances, cabinet stability, civil-military relations, and the political cohesion of the Republic.",
        "Administração de acordos multipartidários, estabilidade de gabinete e articulação entre poder civil e comando militar."
    ),
    "FRA_western_front_operations": (
        "Western Front Operational Missions",
        "Missões Operacionais da Frente Ocidental"
    ),
    "FRA_western_front_operations_desc": (
        "Major tactical initiatives, offensive breakthroughs, and emergency defensive stands along the trench lines.",
        "Comandos táticos decisivos, planos de ruptura e posturas defensivas ao longo das trincheiras do fronte ocidental."
    ),

    # Tooltips & Bonuses
    "FRA_schneider_creusot_artillery_bonus": (
        "Schneider-Creusot Artillery Modernization",
        "Modernização da Artilharia Schneider-Creusot"
    ),
    "FRA_verdun_mission_timeout_tt": (
        "§YThe Meuse fortress line holds! Verdun stands victorious! \"Ils ne passeront pas!\"§!",
        "§YA linha fortificada do Mosa resistiu! Verdun permanece inexpugnável! \"Ils ne passeront pas!\"§!"
    ),
}


def write_loc_file(filepath: str, header: str, lang_dict: dict):
    """Writes a Paradox YAML localization file with mandatory single UTF-8 BOM."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Convert to lines
    lines = [f"{header}:"]
    for key in sorted(lang_dict.keys()):
        val = lang_dict[key]
        # Normalize and escape all internal double quotes as \"
        escaped_val = val.replace('\\"', '"').replace('"', r'\"')
        lines.append(f' {key}:0 "{escaped_val}"')

    content = "\n".join(lines) + "\n"

    # Write as bytes with exact UTF-8 BOM (\xef\xbb\xbf)
    with open(filepath, "wb") as f:
        f.write(b"\xef\xbb\xbf")
        f.write(content.encode("utf-8"))

    print(f"Wrote {len(lang_dict)} keys to {filepath}")


def main():
    en_dict = {k: v[0] for k, v in LOC_ENTRIES.items()}
    pt_dict = {k: v[1] for k, v in LOC_ENTRIES.items()}

    # Parity check
    assert set(en_dict.keys()) == set(pt_dict.keys()), "Parity mismatch!"

    write_loc_file(EN_PATH, "l_english", en_dict)
    write_loc_file(PT_PATH, "l_braz_por", pt_dict)


if __name__ == "__main__":
    main()
