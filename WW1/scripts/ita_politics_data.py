"""Politics and Society (pol) Wing Data for Italy WW1 Tree.
Contains 45 focuses with historical depth, balance compliance, and bilingual loc.
"""

# Dict mapping focus_id (without prefix) -> {
#   "effect": str,
#   "desc_en": str,
#   "desc_pt": str,
#   "cost": int,
#   "available": str,
#   "ai": str
# }

POLITICS_FOCI = {
    "giolitti_ministry": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_sacro_egoismo_policy add_ideas = ITA_ww1_trasformismo_politics add_political_power = 50 add_to_variable = { ita_ww1_interventionism = -5 }",
        "desc_en": "Giovanni Giolitti's parliamentary mastery governs through shifting coalitions and pragmatic reform. Immediate effect: Grants 50 Political Power, establishes the Trasformismo political idea, and cools interventionist fervor by 5.",
        "desc_pt": "O domínio parlamentar de Giovanni Giolitti governa por coalizões fluidas e reformas pragmáticas. Efeito imediato: Concede 50 de Poder Político, estabelece a ideia Trasformismo e reduz a agitação intervencionista em 5."
    },
    "suffrage_law": {
        "cost": 5,
        "available": "date > 1911.6.1",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_ww1_trasformismo_politics add_ideas = ITA_ww1_universal_suffrage add_stability = 0.02 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Expanding the franchise to all literate males aged 21 and all males aged 30 transforms Italian democracy. Immediate effect: Grants +2% Stability, introduces Universal Male Suffrage, and lowers Social Tension by 5.",
        "desc_pt": "A ampliação do voto a todos os homens alfabetizados maiores de 21 anos e a todos os homens de 30 anos transforma a democracia italiana. Efeito imediato: Concede +2% de Estabilidade, introduz o Sufrágio Universal Masculino e reduz a Tensão Social em 5."
    },
    "southern_inquiry": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_political_power = 30 add_to_variable = { ita_ww1_southern_gap = -5 }",
        "desc_en": "A formal parliamentary inquiry into agrarian backwardness and emigration across the Mezzogiorno. Immediate effect: Grants 30 Political Power and narrows the Southern Gap by 5.",
        "desc_pt": "Um inquérito parlamentar formal sobre o atraso agrário e a emigração no Mezzogiorno. Efeito imediato: Concede 30 de Poder Político e reduz a disparidade do Sul em 5."
    },
    "insurance_institute": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_political_power = 25 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Establishing the Istituto Nazionale delle Assicurazioni to create a state life insurance monopoly and fund welfare. Immediate effect: Grants 25 Political Power and reduces Social Tension by 5.",
        "desc_pt": "Criação do Istituto Nazionale delle Assicurazioni para instituir o monopólio estatal e financiar a previdência. Efeito imediato: Concede 25 de Poder Político e reduz a Tensão Social em 5."
    },
    "nationalist_association": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_to_variable = { ita_ww1_irredentism = 10 } add_political_power = 25",
        "desc_en": "Corradini and Federzoni organise the Associazione Nazionalista Italiana, preaching imperial expansion and irredentism. Immediate effect: Increases Irredentism by 10 and grants 25 Political Power.",
        "desc_pt": "Corradini e Federzoni organizam a Associação Nacionalista Italiana, pregando expansão imperial e irredentismo. Efeito imediato: Aumenta o Irredentismo em 10 e concede 25 de Poder Político."
    },
    "socialist_congress": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_to_variable = { ita_ww1_social_tension = 10 } add_political_power = -15 country_event = { id = ww1_italy.4 days = 1 }",
        "desc_en": "The Reggio Emilia Congress sees the maximalist wing expel reformists and elevate young Benito Mussolini to editor of Avanti!. Immediate effect: Increases Social Tension by 10, costs 15 Political Power, and triggers the Socialist Congress event.",
        "desc_pt": "O Congresso de Reggio Emilia assiste à vitória dos maximalistas, que expulsam reformistas e entregam o Avanti! a Benito Mussolini. Efeito imediato: Aumenta a Tensão Social em 10, custa 15 de Poder Político e dispara o evento do Congresso Socialista."
    },
    "trade_union_recognition": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_to_variable = { ita_ww1_social_tension = -5 } add_political_power = 20",
        "desc_en": "Pragmatic arbitration recognises the Confederazione Generale del Lavoro as a legitimate bargaining partner. Immediate effect: Decreases Social Tension by 5 and grants 20 Political Power.",
        "desc_pt": "A arbitragem pragmática reconhece a Confederazione Generale del Lavoro como interlocutora legítima. Efeito imediato: Reduz a Tensão Social em 5 e concede 20 de Poder Político."
    },
    "gentiloni_pact": {
        "cost": 5,
        "available": "date > 1913.1.1",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_ww1_universal_suffrage add_ideas = ITA_ww1_gentiloni_compact add_stability = 0.02 add_political_power = 25",
        "desc_en": "An agreement between the Catholic Electoral Union and liberal candidates secures religious votes against the socialists. Immediate effect: Grants +2% Stability, 30 Political Power, and the Gentiloni Compact national idea.",
        "desc_pt": "O acordo entre a União Eleitoral Católica e candidatos liberais assegura votos religiosos contra o avanço socialista. Efeito imediato: Concede +2% de Estabilidade, 30 de Poder Político e a ideia Pacto Gentiloni."
    },
    "catholic_social_action": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "country_event = { id = ww1_italy.6 days = 1 } add_to_variable = { ita_ww1_southern_gap = -5 }",
        "desc_en": "Catholic agrarian cooperatives and rural savings banks support smallholders in the countryside. Immediate effect: Triggers the Catholic Social Action event and reduces the Southern Gap by 5.",
        "desc_pt": "Cooperativas agrárias católicas e caixas rurais apoiam pequenos proprietários no campo. Efeito imediato: Dispara o evento de Ação Social Católica e reduz a disparidade do Sul em 5."
    },
    "red_week": {
        "cost": 5,
        "available": "date > 1914.5.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.7 days = 1 } add_to_variable = { ita_ww1_social_tension = 15 }",
        "desc_en": "Violent riots and general strikes paralyze Romagna and the Marches following police shootings in Ancona. Immediate effect: Triggers the Red Week event and increases Social Tension by 15.",
        "desc_pt": "Protestos violentos e greves gerais paralisam a Romagna e as Marcas após repressão policial em Ancona. Efeito imediato: Dispara o evento da Semana Vermelha e aumenta a Tensão Social em 15."
    },
    "public_order_measures": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_political_power = 30 add_to_variable = { ita_ww1_social_tension = -10 } country_event = { id = ww1_italy.8 days = 1 }",
        "desc_en": "Deployment of military garrisons and Carabinieri patrols restores civil order without provoking widespread insurrection. Immediate effect: Grants 30 Political Power and triggers the Public Order Restoration event.",
        "desc_pt": "O desdobramento de guarnições militares e patrulhas dos Carabineiros restaura a ordem civil. Efeito imediato: Concede 30 de Poder Político e dispara o evento de Restauração da Ordem."
    },
    "salandra_cabinet": {
        "cost": 5,
        "available": "date > 1914.3.1",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_ww1_gentiloni_compact add_ideas = ITA_ww1_salandra_emergency_cabinet add_political_power = 25 add_to_variable = { ita_ww1_interventionism = 10 } country_event = { id = ww1_italy.9 days = 1 }",
        "desc_en": "Antonio Salandra assumes leadership of a conservative cabinet, bringing an end to Giolittian trasformismo. Immediate effect: Replaces Trasformismo politics, grants 35 Political Power and triggers the Salandra Cabinet event.",
        "desc_pt": "Antonio Salandra assume a liderança de um gabinete conservador, encerrando o trasformismo giolittiano. Efeito imediato: Substitui a política do Trasformismo, concede 35 de Poder Político e dispara o evento do Gabinete Salandra."
    },
    "interventionist_press": {
        "cost": 5,
        "available": "",
        "ai": "factor = 15",
        "effect": "add_to_variable = { ita_ww1_interventionism = 10 } add_political_power = 20",
        "desc_en": "Major dailies such as Corriere della Sera rally bourgeois and intellectual circles behind the interventionist crusade. Immediate effect: Increases Interventionism by 10 and grants 20 Political Power.",
        "desc_pt": "Grandes jornais como o Corriere della Sera mobilizam círculos burgueses e intelectuais pela intervenção. Efeito imediato: Aumenta o Intervencionismo em 10 e concede 20 de Poder Político."
    },
    "neutralist_coalition": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "add_to_variable = { ita_ww1_interventionism = -15 } add_political_power = 40",
        "desc_en": "A parliamentary majority composed of Giolittian liberals, socialists, and Catholics organizes to preserve peace. Immediate effect: Reduces Interventionism by 15 and grants 40 Political Power.",
        "desc_pt": "Uma maioria parlamentar composta por liberais giolittianos, socialistas e católicos organiza-se pela paz. Efeito imediato: Reduz o Intervencionismo em 15 e concede 40 de Poder Político."
    },
    "popolo_ditalia": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.10 days = 1 } add_to_variable = { ita_ww1_interventionism = 5 }",
        "desc_en": "Benito Mussolini launches Il Popolo d'Italia with French and industrial subsidies, calling for revolutionary war. Immediate effect: Triggers the Popolo d'Italia event and raises Interventionism by 5.",
        "desc_pt": "Benito Mussolini lança Il Popolo d'Italia com subsídios industriais e franceses, convocando à guerra revolucionária. Efeito imediato: Dispara o evento de Il Popolo d'Italia e eleva o Intervencionismo em 5."
    },
    "quarto_rally": {
        "cost": 5,
        "available": "date > 1915.4.1",
        "ai": "factor = 15",
        "effect": "add_war_support = 0.02 add_to_variable = { ita_ww1_interventionism = 15 } country_event = { id = ww1_italy.11 days = 1 }",
        "desc_en": "Gabriele D'Annunzio delivers an ecstatic patriotic address at Quarto, unleashing nationalist crowds onto the streets. Immediate effect: Grants +2% War Support, raises Interventionism by 15, and triggers the Quarto Rally event.",
        "desc_pt": "Gabriele D'Annunzio profere inflamado discurso patriótico em Quarto, desencadeando multidões nacionalistas nas ruas. Efeito imediato: Concede +2% de Apoio à Guerra, eleva o Intervencionismo em 15 e dispara o evento do Discurso de Quarto."
    },
    "giolitti_parecchio": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "country_event = { id = ww1_italy.12 days = 1 } add_political_power = 30 add_to_variable = { ita_ww1_interventionism = -10 }",
        "desc_en": "Giolitti insists Italy can obtain parecchio (a great deal) through patient negotiation with Austria without bloodshed. Immediate effect: Triggers the Parecchio event and grants 30 Political Power.",
        "desc_pt": "Giolitti insiste que a Itália pode obter 'parecchio' (muita coisa) negociando com a Áustria sem derramamento de sangue. Efeito imediato: Dispara o evento do Parecchio e concede 30 de Poder Político."
    },
    "parliament_against_street": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_political_power = 35 add_to_variable = { ita_ww1_social_tension = 10 }",
        "desc_en": "The neutralist parliamentary majority stands firm against patriotic street intimidation in Rome and Milan. Immediate effect: Grants 35 Political Power and increases Social Tension by 10.",
        "desc_pt": "A maioria parlamentar neutralista resiste à intimidação das ruas nacionalistas em Roma e Milão. Efeito imediato: Concede 35 de Poder Político e aumenta a Tensão Social em 10."
    },
    "radiant_may": {
        "cost": 5,
        "available": "date > 1915.5.1",
        "ai": "factor = 20",
        "effect": "remove_ideas = ITA_ww1_salandra_emergency_cabinet add_ideas = ITA_ww1_radiant_may_fervor add_war_support = 0.04 add_to_variable = { ita_ww1_interventionism = 25 } country_event = { id = ww1_italy.13 days = 1 }",
        "desc_en": "The intense days of Maggio Radioso force the King and Parliament to reject neutralism and embrace war. Immediate effect: Grants +2% War Support, activates the Radiant May Fervor idea, and triggers the Radiant May event.",
        "desc_pt": "Os dias febris do Maggio Radioso forçam o Rei e o Parlamento a repudiar a neutralidade e abraçar o conflito. Efeito imediato: Concede +2% de Apoio à Guerra, ativa o fervor do Maio Radiante e dispara o evento do Maio Radiante."
    },
    "war_censorship": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "add_political_power = 25 add_to_variable = { ita_ww1_social_tension = -5 } country_event = { id = ww1_italy.14 days = 1 }",
        "desc_en": "Emergency wartime censorship suppresses defeatist propaganda and controls front-line reporting. Immediate effect: Grants 25 Political Power and triggers the War Censorship event.",
        "desc_pt": "Censura emergencial de tempos de guerra reprime propaganda derrotista e controla despachos do fronte. Efeito imediato: Concede 25 de Poder Político e dispara o evento da Censura de Guerra."
    },
    "boselli_national_unity": {
        "cost": 5,
        "available": "date > 1916.1.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 35 add_to_variable = { ita_ww1_social_tension = -5 } country_event = { id = ww1_italy.15 days = 1 }",
        "desc_en": "Paolo Boselli forms a broad coalition cabinet of national unity encompassing interventionists of all colors. Immediate effect: Grants 35 Political Power and triggers the Boselli Cabinet event.",
        "desc_pt": "Paolo Boselli forma um ministério amplo de união nacional abrangendo intervencionistas de todos os matizes. Efeito imediato: Concede 35 de Poder Político e dispara o evento do Gabinete Boselli."
    },
    "women_war_economy": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "158 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } } country_event = { id = ww1_italy.16 days = 1 } add_political_power = 25",
        "desc_en": "Hundreds of thousands of women enter munitions plants, textile mills, and agricultural cooperatives. Immediate effect: Triggers the Female Labour Mobilisation event and grants 20 Political Power.",
        "desc_pt": "Centenas de milhares de mulheres assumem postos em fábricas de munição, tecelagens e lavouras. Efeito imediato: Dispara o evento do Trabalho Feminino e concede 20 de Poder Político."
    },
    "propaganda_service": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "add_political_power = 30 add_to_variable = { ita_ww1_army_morale = 10 } country_event = { id = ww1_italy.17 days = 1 } ita_ww1_clamp_counters = yes",
        "desc_en": "Servizio P deploys trench illustrators, writers, and lecturers to sustain morale in the Alpine trenches. Immediate effect: Activates the Servizio P Propaganda idea and triggers the Propaganda Service event.",
        "desc_pt": "O Servizio P envia ilustradores, escritores e oradores para sustentar o ânimo nas trincheiras alpinas. Efeito imediato: Ativa a ideia Servizio P e dispara o evento do Serviço de Propaganda."
    },
    "land_for_soldiers": {
        "cost": 5,
        "available": "has_war = yes",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_army_morale = 5 } country_event = { id = ww1_italy.18 days = 1 }",
        "desc_en": "Public promises of post-war agrarian reform and land redistribution reassure the conscript infantry. Immediate effect: Increases Army Morale by 5 and triggers the Land for Soldiers event.",
        "desc_pt": "Promessas públicas de reforma agrária e redistribuição de terras tranquilizam a infantaria camponesa. Efeito imediato: Eleva a Moral do Exército em 5 e dispara o evento Terra aos Soldados."
    },
    "caporetto_inquiry": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_caporetto_shock",
        "ai": "factor = 20",
        "effect": "add_to_variable = { ita_ww1_army_morale = 5 } add_political_power = 20 country_event = { id = ww1_italy.19 days = 1 }",
        "desc_en": "A solemn parliamentary inquest investigates the command failures and logistical breakdown of the 12th Battle of the Isonzo. Immediate effect: Triggers the Caporetto Commission event and grants 20 Political Power.",
        "desc_pt": "Um inquérito parlamentar investiga as falhas de comando e o colapso logístico na 12ª Batalha do Isonzo. Efeito imediato: Dispara o evento da Comissão de Caporetto e concede 20 de Poder Político."
    },
    "orlando_government": {
        "cost": 5,
        "available": "date > 1917.10.1",
        "ai": "factor = 20",
        "effect": "add_to_variable = { ita_ww1_army_morale = 10 } add_political_power = 40 country_event = { id = ww1_italy.20 days = 1 }",
        "desc_en": "Vittorio Emanuele Orlando takes the helm with a single mandate: resistance on the Piave and total national mobilization. Immediate effect: Grants 40 Political Power and triggers the Orlando Government event.",
        "desc_pt": "Vittorio Emanuele Orlando assume a chefia do governo com mandato de ferro: resistência no Piave e vitória total. Efeito imediato: Concede 40 de Poder Político e dispara o evento do Governo Orlando."
    },
    "combatants_opera": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_political_power = 30 add_stability = 0.02 add_to_variable = { ita_ww1_social_tension = -5 } country_event = { id = ww1_italy.18 days = 1 } ita_ww1_clamp_counters = yes",
        "desc_en": "The Opera Nazionale Combattenti assists returning veterans with vocational training, credit, and settlement land. Immediate effect: Activates the Opera Nazionale Combattenti idea and grants 25 Political Power.",
        "desc_pt": "A Opera Nazionale Combattenti apoia os veteranos com reintegração profissional, crédito e lotes rurais. Efeito imediato: Ativa a ideia Opera Nazionale Combattenti e concede 25 de Poder Político."
    },
    "mutilated_victory": {
        "cost": 5,
        "available": "date > 1919.1.1",
        "ai": "factor = 15",
        "effect": "remove_ideas = ITA_ww1_radiant_may_fervor country_event = { id = ww1_italy.21 days = 1 } add_to_variable = { ita_ww1_irredentism = 10 }",
        "desc_en": "Disappointment over Dalmatia and Fiume at Versailles replaces wartime enthusiasm with the bitter Vittoria Mutilata myth. Immediate effect: Removes Radiant May Fervor, triggers Mutilated Victory event and raises Irredentism by 10.",
        "desc_pt": "O desapontamento em Versalhes substitui o entusiasmo bélico pelo mito amargo da Vittoria Mutilata. Efeito imediato: Remove o fervor do Maio Radiante, dispara a Vitória Mutilada e eleva o Irredentismo em 10."
    },
    "nitti_cabinet": {
        "cost": 5,
        "available": "date > 1919.6.1",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_social_tension = -5 } add_political_power = 30 country_event = { id = ww1_italy.22 days = 1 }",
        "desc_en": "Francesco Saverio Nitti takes power seeking fiscal retrenchment, demobilization, and social reconciliation. Immediate effect: Grants 30 Political Power and triggers the Nitti Cabinet event.",
        "desc_pt": "Francesco Saverio Nitti assume o governo buscando austeridade fiscal, desmobilização e reconciliação social. Efeito imediato: Concede 30 de Poder Político e dispara o evento do Gabinete Nitti."
    },
    "proportional_representation": {
        "cost": 5,
        "available": "date > 1919.8.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 25 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Electoral reform introduces proportional representation, shattering old liberal patron-client networks. Immediate effect: Grants 25 Political Power and lowers Social Tension by 5.",
        "desc_pt": "A reforma eleitoral introduz a representação proporcional, dissolvendo velhas redes liberais de clientelismo. Efeito imediato: Concede 25 de Poder Político e reduz a Tensão Social em 5."
    },
    "popular_party": {
        "cost": 5,
        "available": "date > 1919.1.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.23 days = 1 } add_political_power = 25",
        "desc_en": "Don Luigi Sturzo founds the Partito Popolare Italiano, organizing Christian democracy into an independent force. Immediate effect: Triggers the Foundation of PPI event and grants 25 Political Power.",
        "desc_pt": "Don Luigi Sturzo funda o Partito Popolare Italiano, organizando a democracia cristã como força independente. Efeito imediato: Dispara o evento de Fundação do PPI e concede 25 de Poder Político."
    },
    "fasci_di_combattimento": {
        "cost": 5,
        "available": "date > 1919.3.1",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_social_tension = 5 } add_political_power = 20",
        "desc_en": "Mussolini gathers war veterans, syndicalists, and Arditi in Milan's Piazza San Sepolcro to launch the Fasci. Immediate effect: Raises Social Tension by 5 and grants 20 Political Power.",
        "desc_pt": "Mussolini reúne veteranos, sindicalistas e Arditi na Piazza San Sepolcro em Milão para fundar os Fasci. Efeito imediato: Eleva a Tensão Social em 5 e concede 20 de Poder Político."
    },
    "biennio_rosso": {
        "cost": 5,
        "available": "date > 1919.9.1",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_social_tension = 15 } add_political_power = -20",
        "desc_en": "Two turbulent years of mass strikes, peasant land occupations, and bread price riots sweep Italy. Immediate effect: Increases Social Tension by 15 and costs 20 Political Power.",
        "desc_pt": "Dois anos turbulentos de greves de massas, ocupações camponesas de terras e protestos pelo pão varrem a Itália. Efeito imediato: Aumenta a Tensão Social em 15 e custa 20 de Poder Político."
    },
    "factory_occupations": {
        "cost": 5,
        "available": "date > 1920.8.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.24 days = 1 } add_to_variable = { ita_ww1_social_tension = 10 }",
        "desc_en": "Over 400,000 metalworkers hoist red and black flags over northern industrial plants, establishing workers' councils. Immediate effect: Triggers the Factory Occupations event and raises Social Tension by 10.",
        "desc_pt": "Mais de 400 mil metalúrgicos ocupam fábricas no Norte com bandeiras vermelhas e conselhos operários. Efeito imediato: Dispara o evento da Ocupação das Fábricas e eleva a Tensão Social em 10."
    },
    "third_giolitti": {
        "cost": 5,
        "available": "date > 1920.6.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 35 add_to_variable = { ita_ww1_social_tension = -10 }",
        "desc_en": "The elderly statesman returns to the premiership, choosing neutrality and negotiation over military confrontation. Immediate effect: Grants 35 Political Power and reduces Social Tension by 10.",
        "desc_pt": "O experiente estadista retorna à presidência do conselho, preferindo conciliação e mediação ao uso da força. Efeito imediato: Concede 35 de Poder Político e reduz a Tensão Social em 10."
    },
    "liberal_restoration": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "remove_ideas = ITA_ww1_squadrist_violence remove_ideas = ITA_ww1_pci_workers_councils add_political_power = 40 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "A concerted effort by constitutional liberals to preserve parliamentary democracy and suppress extremist paramilitary violence. Immediate effect: Removes squadrist and workers council spirits, grants 40 PP.",
        "desc_pt": "Esforço concentrado dos liberais constitucionais para preservar a ordem e reprimir a violência extremista. Efeito imediato: Remove a violência dos esquadrões e os conselhos de fábrica, concede 40 de PP.",
        "ai": "factor = 70"
    },
    "nationalist_order": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_political_power = 30 add_to_variable = { ita_ww1_irredentism = 10 }",
        "desc_en": "Landowners, industrialists, and middle classes embrace nationalist discipline to restore authority. Immediate effect: Grants 30 Political Power and increases Irredentism by 10.",
        "desc_pt": "Proprietários de terra, industriais e classes médias abraçam a disciplina nacionalista para restaurar a autoridade. Efeito imediato: Concede 30 de Poder Político e aumenta o Irredentismo em 10."
    },
    "socialist_turn": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "add_political_power = -25 add_to_variable = { ita_ww1_social_tension = 15 }",
        "desc_en": "The Italian labor movement takes an uncompromising revolutionary stance, rejecting bourgeois coalition governance. Immediate effect: Costs 25 Political Power and increases Social Tension by 15.",
        "desc_pt": "O movimento operário italiano adota postura revolucionária intransigente, rompendo com acordos burgueses. Efeito imediato: Custa 25 de Poder Político e eleva a Tensão Social em 15."
    },
    "facta_coalition": {
        "cost": 5,
        "available": "date > 1922.2.1",
        "ai": "factor = 5",
        "effect": "add_political_power = 35 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Luigi Facta presides over an indecisive liberal coalition struggling to curb escalating squadrist violence. Immediate effect: Grants 35 Political Power and lowers Social Tension by 5.",
        "desc_pt": "Luigi Facta preside uma coalizão liberal vacilante que luta para conter a violência dos esquadrões. Efeito imediato: Concede 35 de Poder Político e reduz a Tensão Social em 5."
    },
    "constitutional_reform": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_stability = 0.02 add_political_power = 35",
        "desc_en": "Strengthening parliamentary prerogatives and modernizing administrative structures under the Statuto Albertino. Immediate effect: Grants +2% Stability and 35 Political Power.",
        "desc_pt": "Reforço das prerrogativas parlamentares e modernização administrativa sob o Estatuto Albertino. Efeito imediato: Concede +2% de Estabilidade e 35 de Poder Político."
    },
    "squadrist_mobilisation": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "remove_ideas = ITA_ww1_mutilated_victory_syndrome add_ideas = ITA_ww1_squadrist_violence add_political_power = 20 add_to_variable = { ita_ww1_social_tension = 10 }",
        "desc_en": "Blackshirt action squads systematically attack socialist printing presses, peasant leagues, and labor halls. Immediate effect: Activates the Squadrist Violence idea and grants 20 Political Power.",
        "desc_pt": "Esquadrões de camisas-negras atacam sistematicamente gráficas socialistas, ligas camponesas e sedes sindicais. Efeito imediato: Ativa a ideia Violência Esquadrista e concede 20 de Poder Político."
    },
    "national_party": {
        "cost": 5,
        "available": "date > 1921.11.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 30 add_to_variable = { ita_ww1_irredentism = 5 }",
        "desc_en": "Transforming the dispersed combat leagues into the disciplined Partito Nazionale Fascista under Mussolini's central command. Immediate effect: Grants 30 Political Power and raises Irredentism by 5.",
        "desc_pt": "Transformação dos bandos dispersos no disciplinado Partido Nacional Fascista sob o comando central de Mussolini. Efeito imediato: Concede 30 de Poder Político e eleva o Irredentismo em 5."
    },
    "march_on_rome": {
        "cost": 5,
        "available": "date > 1922.10.1",
        "ai": "factor = 15",
        "effect": "remove_ideas = ITA_ww1_squadrist_violence country_event = { id = ww1_italy.25 days = 1 } add_political_power = 30",
        "desc_en": "Four fascist quadrumvirs orchestrate armed columns marching on the capital, forcing the crown to concede power. Immediate effect: Squads become the state, removing street squadrist violence idea, triggers March on Rome event and grants 30 PP.",
        "desc_pt": "Quatro quadrunviros coordenam colunas armadas sobre a capital, assumindo o poder. Efeito imediato: Os esquadrões assumem o controle do Estado, encerra a violência esquadrista de rua e concede 30 de PP.",
        "ai": "factor = 80"
    },
    "workers_councils": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "remove_ideas = ITA_ww1_squadrist_violence add_ideas = ITA_ww1_pci_workers_councils add_political_power = 20",
        "desc_en": "Gramsci and the Ordine Nuovo group organize elected factory councils to direct industrial production, breaking fascist squad control. Immediate effect: Replaces squadrist violence with Workers' Councils idea and grants 20 PP.",
        "desc_pt": "Gramsci e L'Ordine Nuovo organizam conselhos de fábrica que quebram o cerco esquadrista. Efeito imediato: Substitui a violência dos esquadrões pelos Conselhos Operários e concede 20 de PP.",
        "ai": "factor = 20"
    },
    "legalitarian_strike": {
        "cost": 5,
        "available": "date > 1922.7.1",
        "ai": "factor = 1",
        "effect": "add_to_variable = { ita_ww1_social_tension = -10 } add_political_power = -20",
        "desc_en": "The anti-fascist Alleanza del Lavoro calls a nationwide general strike in defense of constitutional liberties. Immediate effect: Reduces Social Tension by 10 and costs 20 Political Power.",
        "desc_pt": "A Aliança do Trabalho antifascista convoca greve geral nacional em defesa das liberdades constitucionais. Efeito imediato: Reduz a Tensão Social em 10 e custa 20 de Poder Político."
    }
}
