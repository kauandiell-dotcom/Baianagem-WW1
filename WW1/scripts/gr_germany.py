"""Conteudo novo da Alemanha: frente interna, calendario historico, Revolucao de Novembro e Weimar."""
from gr_lib import *
from gr_russia import pop, timed, tier, sched

G = 'ww1_germany_events.'
SP, HU, DI, KP, RC = ('GER_social_peace', 'GER_hunger', 'GER_discontent', 'GER_kaiser_prestige', 'GER_revolution_count')
NOT_REP = 'NOT = { has_country_flag = GER_republic_proclaimed }'

# ============================================================ IDEIAS
for k, (pic, m, en, pt, den, dpt) in {
    'GER_social_peace_frayed': ('generic_king_handled', {'stability_factor': -0.05, 'war_support_factor': -0.04},
                                'Burgfrieden Frayed', 'Burgfrieden Esgarçado',
                                'The truce between government, parties and unions no longer holds. The Reichstag quarrels again.',
                                'A trégua entre governo, partidos e sindicatos já não se sustenta. O Reichstag volta a brigar.'),
    'GER_revolutionary_mood': ('generic_communism_banned', {'stability_factor': -0.10, 'army_morale_factor': -0.08, 'political_power_gain': -0.10},
                               'Revolutionary Mood', 'Clima Revolucionário',
                               'Workers councils, mutinous sailors and hungry crowds have brought revolution to the edge of the Reich.',
                               'Conselhos operários, marinheiros amotinados e multidões famintas levaram a revolução à beira do Reich.'),
    'GER_zabern_distrust': ('generic_commission', {'political_power_gain': -0.05, 'stability_factor': -0.02},
                            'Zabern Distrust', 'Desconfiança de Zabern',
                            'The army has been shown to stand above the law, and the civilian parties will not forget it.',
                            'Ficou claro que o exército está acima da lei, e os partidos civis não vão esquecer.'),
    'GER_weimar_fragile': ('generic_conference', {'stability_factor': -0.05, 'political_power_gain': -0.05},
                           'Fragile Republic', 'República Frágil',
                           'The Republic was born in defeat and has enemies on the Left and on the Right.',
                           'A República nasceu na derrota e tem inimigos à esquerda e à direita.'),
    'GER_hyperinflation': ('generic_devalue_currency', {'consumer_goods_factor': 0.15, 'stability_factor': -0.10, 'industrial_capacity_factory': -0.10},
                           'Hyperinflation', 'Hiperinflação',
                           'Prices double by the day and wages are paid twice daily. The savings of the middle class are gone.',
                           'Os preços dobram por dia e os salários são pagos duas vezes ao dia. As economias da classe média evaporaram.'),
    'GER_ruhr_passive_resistance': ('generic_energy_concern', {'industrial_capacity_factory': -0.08, 'consumer_goods_factor': 0.05, 'war_support_factor': 0.05},
                                    'Passive Resistance in the Ruhr', 'Resistência Passiva no Ruhr',
                                    'Miners, railwaymen and officials refuse to work for the occupiers. The state pays them to sit at home.',
                                    'Mineiros, ferroviários e funcionários se recusam a trabalhar para os ocupantes. O Estado paga para que fiquem em casa.'),
    'GER_freikorps_menace': ('generic_fascist_workers', {'stability_factor': -0.03, 'political_power_gain': 0.05},
                             'Freikorps Menace', 'Ameaça dos Freikorps',
                             'Armed veterans stand ready to defend the Republic or to overthrow it, depending on who pays.',
                             'Veteranos armados estão prontos para defender a República ou derrubá-la, conforme quem pague.'),
}.items():
    idea(k, pic, m, en, pt, den, dpt)

# ============================================================ EVENTOS
event(G + '200', 'ger_elections_1912',
      ('The Reichstag Election of 1912', 'A Eleição do Reichstag de 1912'),
      ('The Social Democrats win more votes than any other party and become the largest group in the Reichstag. The Emperor and the Junkers see red; the Centre and the Progressives see a majority for reform.',
       'Os social-democratas obtêm mais votos que qualquer outro partido e se tornam o maior grupo do Reichstag. O Imperador e os junkers veem vermelho; o Centro e os Progressistas veem uma maioria para reformas.'),
      [('Accept the result and court the Centre and the Progressives.', 'Aceitar o resultado e cortejar o Centro e os Progressistas.',
        fx(pop('democratic', 0.06), pop('communism', 0.04), V(SP, 3), 'add_political_power = -20'), 40, None),
       ('Lean on the Bundesrat and the Emperor.', 'Apoiar-se no Bundesrat e no Imperador.',
        fx(V(DI, 5), V(KP, -2), 'add_political_power = 30'), 60, None)])

event(G + '201', 'ger_zabern',
      ('The Zabern Affair', 'O Caso Zabern'),
      ('A young lieutenant in Alsace insults the locals, and the garrison answers protests with arrests. The Reichstag votes to censure the Chancellor, but the Emperor sides with the army.',
       'Um jovem tenente na Alsácia insulta os moradores, e a guarnição responde aos protestos com prisões. O Reichstag vota pela censura ao Chanceler, mas o Imperador fica ao lado do exército.'),
      [('Back the army.', 'Apoiar o exército.',
        fx('army_experience = 10', V(DI, 6), V(KP, -3), timed('GER_zabern_distrust', 540)), 65, None),
       ('Censure the officers.', 'Censurar os oficiais.',
        fx('add_political_power = -30', V(DI, -3), V(SP, 3)), 35, None)])

event(G + '202', 'ger_burgfrieden',
      ('No Parties, Only Germans', 'Sem Partidos, Só Alemães'),
      ('In the Reichstag, the Social Democrats vote the war credits. The Emperor declares that he no longer knows parties, only Germans. The Burgfrieden is proclaimed and the nation goes to war in a wave of enthusiasm.',
       'No Reichstag, os social-democratas votam os créditos de guerra. O Imperador declara que não conhece mais partidos, apenas alemães. O Burgfrieden é proclamado e a nação vai à guerra em uma onda de entusiasmo.'),
      [('No parties, only Germans!', 'Sem partidos, só alemães!',
        fx(V(SP, 20), 'add_war_support = 0.08'), 70, None),
       ('Keep the Social Democrats at arm length.', 'Manter os social-democratas à distância.',
        fx(V(SP, 5), 'add_political_power = 25', V(DI, 3)), 30, None)],
      trigger='has_war = yes')

event(G + '203', 'ger_moltke',
      ('Moltke Is Dismissed', 'Moltke É Demitido'),
      ('After the Marne, the Chief of the General Staff is a broken man. The Emperor must choose who will direct the war in the west.',
       'Depois do Marne, o Chefe do Estado-Maior é um homem alquebrado. O Imperador precisa escolher quem conduzirá a guerra no oeste.'),
      [('Falkenhayn takes over the General Staff.', 'Falkenhayn assume o Estado-Maior.',
        fx('army_experience = 10', V(KP, -2)), 70, None),
       ('Keep Moltke in command.', 'Manter Moltke no comando.',
        fx('army_experience = 5', 'add_war_support = -0.01'), 30, None)],
      trigger='has_war_with = FRA')

event(G + '204', 'ger_lusitania',
      ('The Lusitania', 'O Lusitania'),
      ('A German submarine has sunk the liner Lusitania with over a hundred Americans aboard. Washington protests in the strongest terms and the Navy Office asks that the campaign continue.',
       'Um submarino alemão afundou o transatlântico Lusitania com mais de cem americanos a bordo. Washington protesta nos termos mais duros e o Almirantado pede que a campanha continue.'),
      [('Defend the submarine campaign.', 'Defender a campanha submarina.',
        fx('add_war_support = 0.02', V(KP, -2), 'set_country_flag = ger_lusitania_defended'), 40, None),
       ('Restrict the U-boats to cruiser rules.', 'Restringir os U-boote às regras de cruzador.',
        fx('set_country_flag = ger_respected_sussex_pledge', 'add_stability = 0.01', 'add_political_power = -20'), 60, None)],
      trigger='has_war_with = ENG')

event(G + '205', 'ger_third_ohl',
      ('The Third Supreme Command', 'A Terceira Comissão Suprema'),
      ('With Verdun bled white and Romania entering the war, Falkenhayn falls. Hindenburg and Ludendorff take over the Supreme Army Command and begin to run the economy, the press and the Chancellor.',
       'Com Verdun sangrada e a Romênia entrando na guerra, Falkenhayn cai. Hindenburg e Ludendorff assumem o Comando Supremo do Exército e começam a dirigir a economia, a imprensa e o Chanceler.'),
      [('Hindenburg and Ludendorff take over.', 'Hindenburg e Ludendorff assumem.',
        fx(timed('GER_defense_in_depth_doctrine', 720), V(KP, -4), V(SP, -4), 'add_war_support = 0.03'), 65, None),
       ('Keep civilian control of the war.', 'Manter o controle civil da guerra.',
        fx('add_stability = 0.02', V(SP, 4), 'add_political_power = -25'), 35, None)],
      trigger='has_war = yes')

event(G + '206', 'ger_berlin_strike',
      ('The May Day Strike of 1916', 'A Greve de Primeiro de Maio de 1916'),
      ('Karl Liebknecht is arrested at a May Day demonstration in Potsdamer Platz, and tens of thousands of Berlin workers down tools in protest. The Social Democratic party itself begins to split.',
       'Karl Liebknecht é preso em uma manifestação de Primeiro de Maio na Potsdamer Platz, e dezenas de milhares de operários berlinenses cruzam os braços em protesto. O próprio Partido Social-Democrata começa a se dividir.'),
      [('Arrest the leaders and prosecute them.', 'Prender os líderes e processá-los.',
        fx(V(DI, 8), V(SP, -3), 'add_stability = -0.02', pop('communism', 0.03)), 55, None),
       ('Let the protest pass and talk to the unions.', 'Deixar o protesto passar e conversar com os sindicatos.',
        fx(V(DI, -2), V(SP, 3), 'add_political_power = -20'), 45, None)],
      trigger='has_war = yes')

event(G + '207', 'ger_hunger',
      ('The Turnip Winter', 'O Inverno dos Nabos'),
      ('The potato harvest has failed and the British blockade has stopped imports. The cities eat turnips, the black market thrives and the people blame the government for every empty plate.',
       'A colheita de batatas fracassou e o bloqueio britânico interrompeu as importações. As cidades comem nabos, o mercado negro prospera e o povo culpa o governo por cada prato vazio.'),
      [('Expand the War Food Office controls.', 'Ampliar os controles do Escritório de Alimentação de Guerra.',
        fx(V(HU, -6), 'add_political_power = -30'), 40, None),
       ('Serve the army first.', 'Servir primeiro o exército.',
        fx(V(HU, 4), V(DI, 4), 'add_war_support = 0.02'), 25, None),
       ('Price controls and public soup kitchens.', 'Controle de preços e cozinhas populares.',
        fx(V(HU, -4), V(DI, -2), 'add_political_power = -20'), 35, None)],
      immediate=fx(V(HU, 14), timed('GER_naval_blockade_strain', 400)), trigger='has_war = yes')

event(G + '208', 'ger_zimmermann',
      ('The Zimmermann Telegram', 'O Telegrama Zimmermann'),
      ('The Foreign Office proposes to Mexico an alliance against the United States, should Washington enter the war. The cable travels over a route the British read.',
       'O Ministério das Relações Exteriores propõe ao México uma aliança contra os Estados Unidos, caso Washington entre na guerra. O telegrama trafega por uma rota que os britânicos leem.'),
      [('Send the telegram.', 'Enviar o telegrama.',
        fx('set_country_flag = GER_zimmermann_sent', 'add_political_power = 25'), 50, None),
       ('Shelve the plan.', 'Arquivar o plano.',
        fx(V(KP, 1), 'add_stability = 0.01'), 50, None)],
      trigger='has_war_with = ENG')

event(G + '209', 'ger_peace_resolution',
      ('The Peace Resolution', 'A Resolução de Paz'),
      ('The Reichstag majority of Social Democrats, Centre and Progressives calls for a peace without annexations. The Supreme Command answers by forcing out the Chancellor.',
       'A maioria do Reichstag, de social-democratas, Centro e Progressistas, pede uma paz sem anexações. O Comando Supremo responde forçando a saída do Chanceler.'),
      [('The Reichstag declares for peace without annexations.', 'O Reichstag se declara por uma paz sem anexações.',
        fx('set_country_flag = GER_reichstag_peace_resolution_passed', V(SP, 8), 'add_war_support = -0.03', pop('democratic', 0.04)), 40, None),
       ('The Supreme Command ignores the resolution.', 'O Comando Supremo ignora a resolução.',
        fx('set_country_flag = GER_reichstag_peace_resolution_rejected', V(DI, 6), timed('GER_vaterlandspartei_iron_fist', 540)), 60, None)],
      trigger='has_war = yes')

event(G + '210', 'ger_hertling',
      ('A New Chancellor', 'Um Novo Chanceler'),
      ('Michaelis has lasted a hundred days. The Centre proposes the aged Bavarian Count Hertling, while the Reichstag parties ask for a say in the choice.',
       'Michaelis durou cem dias. O Centro propõe o idoso conde bávaro Hertling, enquanto os partidos do Reichstag pedem voz na escolha.'),
      [('Appoint Count Hertling.', 'Nomear o conde Hertling.',
        fx(V(KP, 2), 'add_political_power = -20'), 60, None),
       ('Appoint parliamentary ministers.', 'Nomear ministros parlamentares.',
        fx(V(SP, 6), pop('democratic', 0.04)), 40, None)],
      trigger='has_war = yes')

event(G + '211', 'ger_spring_offensive',
      ('Operation Michael', 'Operação Michael'),
      ('With the East closed, the divisions of the Ostheer move west. Ludendorff plans to break the Allies before the Americans arrive in strength.',
       'Com o Leste fechado, as divisões do Ostheer se deslocam para o oeste. Ludendorff planeja quebrar os Aliados antes que os americanos cheguem em força.'),
      [('Stake everything on one great blow.', 'Apostar tudo em um grande golpe.',
        fx('army_experience = 20', timed('GER_bruchmueller_artillery', 120), V(DI, 6)), 60, None),
       ('Limited offensives on a narrower front.', 'Ofensivas limitadas em uma frente mais estreita.',
        fx('army_experience = 8', V(DI, 2)), 40, None)],
      trigger='has_war = yes')

event(G + '212', 'ger_january_strikes',
      ('The January Strikes', 'As Greves de Janeiro'),
      ('Half a million workers down tools in Berlin, Hamburg and Kiel, demanding peace without annexations, food and the vote. Workers councils elect delegates in the factories.',
       'Meio milhão de operários cruza os braços em Berlim, Hamburgo e Kiel, exigindo paz sem anexações, comida e o voto. Conselhos operários elegem delegados nas fábricas.'),
      [('Crush the strikes.', 'Esmagar as greves.',
        fx(V(DI, -6), 'add_stability = -0.03', pop('communism', 0.03)), 55, None),
       ('Negotiate with the Social Democratic leaders.', 'Negociar com os líderes social-democratas.',
        fx(V(SP, 6), V(DI, -4), 'add_war_support = -0.02'), 45, None)],
      trigger='has_war = yes')

event(G + '213', 'ger_max_von_baden',
      ('The October Reforms', 'As Reformas de Outubro'),
      ('With the front breaking, Ludendorff demands an armistice and advises parliamentary government. Prince Max of Baden becomes Chancellor with Social Democrats in the Cabinet, and the Emperor remains in name.',
       'Com a frente ruindo, Ludendorff exige um armistício e aconselha o governo parlamentar. O príncipe Max de Baden se torna Chanceler com social-democratas no Gabinete, e o Imperador permanece no cargo apenas de nome.'),
      [('Parliamentary government under Prince Max.', 'Governo parlamentar sob o príncipe Max.',
        fx('set_country_flag = GER_october_reforms', V(SP, 10), pop('democratic', 0.10), 'add_stability = 0.03'), 65, None),
       ('Refuse reform and fight to the end.', 'Recusar a reforma e lutar até o fim.',
        fx('set_country_flag = GER_october_refused', V(DI, 10), 'add_war_support = 0.03'), 35, None)],
      trigger='has_war = yes')

event(G + '214', 'ger_kiel',
      ('Mutiny at Kiel', 'Motim em Kiel'),
      ('The High Seas Fleet is ordered to sea for a last battle. The stokers draw their fires, the crews refuse orders and red flags rise on the battleships. By morning Kiel is in the hands of sailors and workers councils.',
       'A Frota de Alto-Mar recebe ordem de sair para uma última batalha. Os foguistas apagam as caldeiras, as tripulações recusam ordens e bandeiras vermelhas sobem nos couraçados. Ao amanhecer, Kiel está nas mãos de marinheiros e conselhos operários.'),
      [('Negotiate with the sailors councils.', 'Negociar com os conselhos de marinheiros.',
        fx(V(DI, -5), 'add_stability = -0.05', 'set_country_flag = GER_kiel_negotiated', 'country_event = { id = ww1_germany_events.215 days = 8 }'), 50, None),
       ('Crush the mutiny by force.', 'Esmagar o motim pela força.',
        fx(V(RC, 1), V(DI, 10), 'add_stability = -0.08', 'clr_country_flag = GER_kiel_window_open',
           'set_country_flag = { flag = GER_kiel_cooldown days = 25 }'), 50,
        'check_variable = { GER_revolution_count < 1 }')],
      immediate='set_country_flag = GER_kiel_mutiny_underway', trigger=NOT_REP, once=False)

event(G + '215', 'ger_republic',
      ('The November Revolution', 'A Revolução de Novembro'),
      ('On 9 November Prince Max hands the chancellorship to Friedrich Ebert. From a Reichstag window Scheidemann proclaims the German Republic; across town Liebknecht proclaims a Socialist Republic from the balcony of the Palace.',
       'Em 9 de novembro o príncipe Max entrega a chancelaria a Friedrich Ebert. De uma janela do Reichstag, Scheidemann proclama a República Alemã; do outro lado da cidade, Liebknecht proclama uma República Socialista da sacada do Palácio.'),
      [('Ebert and the Social Democrats take charge.', 'Ebert e os social-democratas assumem.',
        fx('set_country_flag = GER_republic_proclaimed', 'set_politics = { ruling_party = democratic elections_allowed = yes }',
           'remove_ideas = GER_burgfrieden_social_peace', pop('democratic', 0.25), V(KP, -100), 'country_event = { id = ww1_germany_events.216 days = 2 }'), 85, None),
       ('The Spartacists and the Independents seize the streets.', 'Os espartaquistas e os independentes tomam as ruas.',
        fx('set_country_flag = GER_republic_proclaimed', 'set_country_flag = GER_red_revolution', pop('communism', 0.20),
           'country_event = { id = ww1_germany_events.51 days = 2 }'), 15, 'check_variable = { GER_discontent > 70 }')],
      trigger=NOT_REP)

event(G + '216', 'ger_abdication',
      ('The Kaiser Goes', 'O Kaiser Parte'),
      ('Wilhelm II, who had hoped to lead his army home, is told by Hindenburg that the troops are no longer behind him. He crosses the Dutch border and the Hohenzollern monarchy ends.',
       'Guilherme II, que esperava conduzir seu exército de volta para casa, ouve de Hindenburg que as tropas não estão mais com ele. Cruza a fronteira holandesa e a monarquia Hohenzollern chega ao fim.'),
      [('The Emperor goes into exile in the Netherlands.', 'O Imperador parte para o exílio nos Países Baixos.',
        fx('set_country_flag = GER_kaiser_abdicated', 'add_ideas = GER_stab_in_the_back_myth', 'add_war_support = -0.10',
           'country_event = { id = ww1_germany_events.217 days = 2 }'), 100, None)])

event(G + '217', 'ger_ebert_groener',
      ('The Ebert-Groener Pact', 'O Pacto Ebert-Groener'),
      ('General Groener telephones Ebert on the secret line: the army will serve the new government if it keeps order against the councils. Ebert accepts.',
       'O general Groener telefona a Ebert pela linha secreta: o exército servirá ao novo governo se ele mantiver a ordem contra os conselhos. Ebert aceita.'),
      [('Ally with the army against the councils.', 'Aliar-se ao exército contra os conselhos.',
        fx(V(DI, -10), 'add_stability = 0.03', 'army_experience = 10', pop('communism', -0.03), 'set_country_flag = GER_ebert_groener'), 70, None),
       ('Trust the workers and soldiers councils.', 'Confiar nos conselhos de operários e soldados.',
        fx(pop('communism', 0.08), V(DI, 4), 'add_political_power = -20', 'set_country_flag = GER_councils_trusted'), 30, None)])

event(G + '218', 'ger_spartacists',
      ('The Spartacist Uprising', 'A Insurreição Espartaquista'),
      ('Berlin workers occupy the newspaper district and raise barricades. Liebknecht and Luxemburg call for a second revolution against Ebert.',
       'Operários berlinenses ocupam o bairro dos jornais e erguem barricadas. Liebknecht e Luxemburgo convocam uma segunda revolução contra Ebert.'),
      [('Let the Freikorps crush the uprising.', 'Deixar que os Freikorps esmaguem a insurreição.',
        fx(V(DI, -15), 'add_stability = -0.03', pop('communism', -0.05), timed('GER_freikorps_menace', 720)), 70, None),
       ('Negotiate with the insurgents.', 'Negociar com os insurgentes.',
        fx(V(DI, 5), pop('communism', 0.05), 'add_political_power = -30'), 30, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '219', 'ger_weimar',
      ('The Weimar National Assembly', 'A Assembleia Nacional de Weimar'),
      ('Away from Berlin\'s barricades the National Assembly meets in Goethe\'s town and drafts a democratic constitution with a strong President and universal suffrage for men and women.',
       'Longe das barricadas de Berlim, a Assembleia Nacional se reúne na cidade de Goethe e redige uma constituição democrática com um Presidente forte e sufrágio universal para homens e mulheres.'),
      [('Adopt the Weimar Constitution.', 'Adotar a Constituição de Weimar.',
        fx('set_politics = { ruling_party = democratic elections_allowed = yes }', 'add_ideas = GER_weimar_fragile', 'add_stability = 0.05', V(SP, 15)), 100, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '220', 'ger_kapp',
      ('The Kapp Putsch', 'O Putsch de Kapp'),
      ('Freikorps brigades march into Berlin and install Wolfgang Kapp as Chancellor. The government flees, and the trade unions call a general strike.',
       'Brigadas Freikorps marcham sobre Berlim e instalam Wolfgang Kapp como Chanceler. O governo foge, e os sindicatos convocam uma greve geral.'),
      [('The general strike defeats the putsch.', 'A greve geral derrota o putsch.',
        fx(V(DI, -5), pop('democratic', 0.03), 'add_political_power = 25'), 60, None),
       ('Compromise with the putschists.', 'Transigir com os golpistas.',
        fx(pop('fascism', 0.04), V(DI, 5), 'add_stability = -0.03'), 40, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '221', 'ger_rathenau',
      ('The Murder of Rathenau', 'O Assassinato de Rathenau'),
      ('Foreign Minister Walther Rathenau, who negotiated Rapallo, is shot by nationalist extremists. Hundreds of thousands march in defence of the Republic.',
       'O ministro das Relações Exteriores Walther Rathenau, que negociou Rapallo, é morto a tiros por extremistas nacionalistas. Centenas de milhares marcham em defesa da República.'),
      [('Pass the Law for the Protection of the Republic.', 'Aprovar a Lei de Proteção da República.',
        fx('add_stability = 0.02', V(DI, -5), pop('fascism', -0.03)), 100, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '222', 'ger_ruhr',
      ('The Occupation of the Ruhr', 'A Ocupação do Ruhr'),
      ('French and Belgian troops occupy the Ruhr for unpaid reparations. Berlin must choose between surrender and a costly strike of the whole region.',
       'Tropas francesas e belgas ocupam o Ruhr por reparações não pagas. Berlim precisa escolher entre a rendição e uma greve custosa de toda a região.'),
      [('Passive resistance.', 'Resistência passiva.',
        fx(timed('GER_ruhr_passive_resistance', 240), V(HU, 8), V(DI, 3)), 60, None),
       ('Resume reparations payments.', 'Retomar o pagamento das reparações.',
        fx('add_political_power = -50', V(DI, 8), 'add_stability = -0.02'), 40, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '223', 'ger_inflation',
      ('The Mark Collapses', 'O Marco Desaba'),
      ('A loaf of bread costs millions, wages are paid twice a day and savings are wiped out. The Republic can print no more money than it already has.',
       'Um pão custa milhões, os salários são pagos duas vezes ao dia e as economias são aniquiladas. A República não pode imprimir mais dinheiro do que já imprimiu.'),
      [('A new currency must be found.', 'É preciso encontrar uma nova moeda.',
        fx('add_ideas = GER_hyperinflation', V(DI, 6), 'set_country_flag = GER_hyperinflation_active'), 100, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '224', 'ger_volksmarine',
      ('The Christmas Crisis', 'A Crise de Natal'),
      ('The People Naval Division occupies the Chancellery and holds a government hostage over unpaid wages. Ebert calls in regular troops, and the Independents leave the government.',
       'A Divisão Naval do Povo ocupa a Chancelaria e mantém um governo refém por salários atrasados. Ebert chama tropas regulares, e os Independentes deixam o governo.'),
      [('Use regular troops.', 'Usar tropas regulares.',
        fx(V(DI, -5), 'army_experience = 5', pop('communism', 0.04)), 60, None),
       ('Pay the sailors and settle.', 'Pagar os marinheiros e fechar acordo.',
        fx('add_political_power = -40', V(DI, 3)), 40, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '225', 'ger_scuttling',
      ('Scapa Flow', 'Scapa Flow'),
      ('Interned at Scapa Flow and told the armistice will be extended, Admiral von Reuter orders his ships scuttled rather than let them be divided among the Allies.',
       'Internado em Scapa Flow e informado de que o armistício será prorrogado, o almirante von Reuter ordena que seus navios sejam afundados em vez de divididos entre os Aliados.'),
      [('The fleet is scuttled.', 'A frota é afundada.',
        fx('navy_experience = 10', 'add_war_support = 0.02', 'add_political_power = -15'), 100, None)],
      trigger='has_country_flag = GER_republic_proclaimed')

event(G + '230', 'ger_russian_opportunity',
      ('Revolution in Russia', 'Revolução na Rússia'),
      ('The Tsar is gone and Russia is in turmoil. The General Staff sees a chance to knock the Eastern enemy out of the war, and the Foreign Office has contacts among the exiled revolutionaries.',
       'O Tsar partiu e a Rússia está em convulsão. O Estado-Maior vê uma chance de tirar o inimigo oriental da guerra, e o Ministério das Relações Exteriores tem contatos entre os revolucionários exilados.'),
      [('Facilitate Lenin\'s return by sealed train.', 'Facilitar o retorno de Lênin em trem lacrado.',
        fx('set_country_flag = GER_sealed_train_supported', 'add_war_support = 0.02', 'add_political_power = -20'), 60, None),
       ('Stay out of Russian politics and strengthen the front.', 'Ficar fora da política russa e reforçar a frente.',
        fx('army_experience = 8', 'add_political_power = 20'), 40, None)])

event(G + '231', 'sov_sovnarkom',
      ('The Soviet Offer of Armistice', 'A Oferta Soviética de Armistício'),
      ('The new Bolshevik government proposes an immediate armistice on all fronts. Hoffmann and Kuhlmann are to receive the Russian delegation at Brest-Litovsk.',
       'O novo governo bolchevique propõe um armistício imediato em todas as frentes. Hoffmann e Kuhlmann receberão a delegação russa em Brest-Litovsk.'),
      [('Open armistice talks.', 'Abrir conversações de armistício.',
        fx('add_political_power = -10', 'if = { limit = { has_war_with = SOV } SOV = { country_event = { id = ww1_diplomacy.31 days = 2 } } }'), 65, None),
       ('Press the advance in the Ukraine and the Baltic.', 'Pressionar o avanço na Ucrânia e no Báltico.',
        fx('army_experience = 10', V(DI, 3)), 35, None)])

# ============================================================ DECISOES
category('GER_home_front', 'generic_crisis', 'original_tag = GER',
         'original_tag = GER\nhas_country_flag = GER_rework_init',
         'The Home Front', 'A Frente Interna',
         'The Reich war effort depends on the mood of the cities, the loyalty of the Social Democrats and the bread ration.',
         'O esforço de guerra do Reich depende do humor das cidades, da lealdade dos social-democratas e da ração de pão.')
H = 'GER_home_front'
GV = 'original_tag = GER\nhas_country_flag = GER_rework_init'
decision(H, 'GER_dec_war_loans', 'generic_electricity', 25, 120, 'has_war = yes', GV + '\nhas_war = yes',
         fx('add_war_support = 0.03', V(SP, -1)), 'modifier = { add = 20 has_war_support < 0.45 }',
         'War Loans Campaign', 'Campanha de Empréstimos de Guerra',
         'Posters and bank rallies ask every citizen to lend the Reich their savings.', 'Cartazes e comícios de bancos pedem a cada cidadão que empreste suas economias ao Reich.')
decision(H, 'GER_dec_turnip_relief', 'generic_forestry', 35, 90, 'check_variable = { GER_hunger > 20 }', GV,
         fx(V(HU, -9), 'add_stability = -0.01'), 'modifier = { add = 30 check_variable = { GER_hunger > 45 } }',
         'War Food Office Measures', 'Medidas do Escritório de Alimentação',
         'Ration cards, communal kitchens and price ceilings. Nobody is satisfied but fewer go hungry.', 'Cartões de racionamento, cozinhas comunitárias e tetos de preços. Ninguém fica satisfeito, mas menos gente passa fome.')
decision(H, 'GER_dec_censor_press', 'generic_wreckers', 25, 90, 'has_war = yes', GV + '\nhas_war = yes',
         fx(V(DI, -8), V(SP, -3)), 'modifier = { add = 20 check_variable = { GER_discontent > 60 } }',
         'Tighten the Censorship', 'Endurecer a Censura',
         'Confiscate newspapers and ban strike meetings. Discontent cools, trust in the government does not.', 'Confiscar jornais e proibir reuniões de greve. O descontentamento esfria, a confiança no governo não.')
decision(H, 'GER_dec_court_the_spd', 'generic_monarchy', 30, 120, 'always = yes', GV,
         fx(V(SP, 8), V(DI, -4), 'add_war_support = -0.01'), 'modifier = { add = 25 check_variable = { GER_social_peace < 45 } }',
         'Court the Social Democrats', 'Cortejar os Social-Democratas',
         'Invite Ebert and Scheidemann to the Chancellery and promise reform after the war.', 'Convidar Ebert e Scheidemann à Chancelaria e prometer reformas após a guerra.')
decision(H, 'GER_dec_kaiser_visits_front', 'generic_pickelhaube', 25, 120, fx('has_war = yes', NOT_REP), GV + '\nhas_war = yes\n' + NOT_REP,
         fx('add_war_support = 0.02', V(KP, 4)), 'modifier = { add = 15 check_variable = { GER_kaiser_prestige < 50 } }',
         'The Emperor Visits the Front', 'O Imperador Visita a Frente',
         'Wilhelm appears in a field-grey uniform among his soldiers. Morale rises for a while.', 'Guilherme aparece de uniforme cinza entre seus soldados. O moral sobe por um tempo.')
decision(H, 'GER_dec_eastern_requisition', 'generic_scorched_earth', 30, 120, 'has_country_flag = brest_litovsk_concluded', GV + '\nhas_country_flag = brest_litovsk_concluded',
         fx(V(HU, -6), 'add_stability = -0.01'), 'modifier = { add = 25 check_variable = { GER_hunger > 40 } }',
         'Requisition from the East', 'Requisição no Leste',
         'Grain trains from Ober Ost and the Ukraine feed the home front, at the price of local resentment.', 'Trens de grãos do Ober Ost e da Ucrânia alimentam a frente interna, ao preço do ressentimento local.')
decision(H, 'GER_dec_support_republic', 'generic_planted_spear', 40, 120, 'has_country_flag = GER_republic_proclaimed', GV + '\nhas_country_flag = GER_republic_proclaimed',
         fx('add_stability = 0.03', V(DI, -6)), 'modifier = { add = 30 always = yes }',
         'Rally to the Republic', 'Mobilizar pela República',
         'Mass meetings and the black-red-gold flag. The Republic needs defenders among the people.', 'Comícios de massa e a bandeira preto-vermelho-dourada. A República precisa de defensores entre o povo.')
decision(H, 'GER_dec_curb_freikorps', 'generic_fortification', 35, 150, 'has_country_flag = GER_republic_proclaimed', GV + '\nhas_country_flag = GER_republic_proclaimed',
         fx('remove_ideas = GER_freikorps_menace', 'add_stability = 0.01', 'army_experience = -5'), 'modifier = { add = 20 has_idea = GER_freikorps_menace }',
         'Disband the Freikorps', 'Dissolver os Freikorps',
         'Fold the volunteer corps into the small regular army allowed by the peace terms.', 'Incorporar os corpos de voluntários ao pequeno exército regular permitido pelos termos de paz.')
decision(H, 'GER_dec_stabilise_mark', 'generic_independence', 60, 90, 'has_idea = GER_hyperinflation', GV + '\nhas_idea = GER_hyperinflation',
         fx('remove_ideas = GER_hyperinflation', 'add_stability = 0.04', V(DI, -6)), 'modifier = { add = 50 always = yes }',
         'Introduce the Rentenmark', 'Introduzir o Rentenmark',
         'A new currency backed by land and industry stops the fall. Sacrifices will be hard.', 'Uma nova moeda lastreada em terra e indústria detém a queda. Os sacrifícios serão duros.')

# ============================================================ MOTOR
TIERS = (tier('GER_hunger', 65, 35, 'GER_turnip_winter_crisis', 'GER_kriegsbrot_rationing')
         + tier('GER_discontent', 80, 60, 'GER_revolutionary_mood', 'GER_reichstag_strike_unrest'))

CAL = ''.join([
    sched('GER_ev_1912', 'date > 1912.1.14', 200),
    sched('GER_ev_zabern', 'date > 1913.11.25', 201),
    sched('GER_ev_burgfrieden', 'has_war = yes date > 1914.8.3', 202),
    sched('GER_ev_moltke', 'has_war_with = FRA date > 1914.9.14', 203),
    sched('GER_ev_lusitania', 'has_war_with = ENG date > 1915.5.8', 204),
    sched('GER_ev_third_ohl', 'has_war = yes date > 1916.8.29', 205),
    sched('GER_ev_berlin_strike', 'has_war = yes date > 1916.5.1', 206),
    sched('GER_ev_turnip', 'has_war = yes date > 1916.11.1', 207),
    sched('GER_ev_zimmermann', 'has_war_with = ENG date > 1917.1.17', 208),
    sched('GER_ev_peace_resolution', 'has_war = yes date > 1917.7.10', 209),
    sched('GER_ev_hertling', 'has_war = yes date > 1917.10.31', 210),
    sched('GER_ev_jan_strikes', 'has_war = yes date > 1918.1.28', 212),
    sched('GER_ev_michael', 'has_war = yes date > 1918.3.21', 211),
    sched('GER_ev_october', 'has_war = yes date > 1918.9.30 ' + NOT_REP + ' OR = { surrender_progress > 0.15 check_variable = { GER_discontent > 60 } has_war_support < 0.30 }', 213),
    sched('GER_ev_christmas', 'has_country_flag = GER_republic_proclaimed date > 1918.12.23', 224),
    sched('GER_ev_spartacists', 'has_country_flag = GER_republic_proclaimed date > 1919.1.5', 218),
    sched('GER_ev_weimar', 'has_country_flag = GER_republic_proclaimed date > 1919.2.6', 219),
    sched('GER_ev_scapa', 'has_country_flag = GER_republic_proclaimed has_war = no date > 1919.6.21', 225),
    sched('GER_ev_kapp', 'has_country_flag = GER_republic_proclaimed date > 1920.3.12', 220),
    sched('GER_ev_rathenau', 'has_country_flag = GER_republic_proclaimed date > 1922.6.24', 221),
    sched('GER_ev_ruhr', 'has_country_flag = GER_republic_proclaimed date > 1923.1.11', 222),
    sched('GER_ev_inflation', 'has_country_flag = GER_republic_proclaimed date > 1923.7.1', 223),
]).replace('ww1_russia.', 'ww1_germany_events.')

ENGINE = '''# Gerado por scripts/build_ger_rus_content.py - frente interna do Imperio Alemao.
ww1_ger_rework_init = {
	set_country_flag = GER_rework_init
	set_variable = { GER_social_peace = 74 }
	set_variable = { GER_hunger = 6 }
	set_variable = { GER_discontent = 12 }
	set_variable = { GER_kaiser_prestige = 68 }
	set_variable = { GER_revolution_count = 0 }
}

ww1_ger_rework_weekly = {
	if = { limit = { NOT = { has_country_flag = GER_rework_init } } ww1_ger_rework_init = yes }
	if = {
		limit = { has_war = yes any_enemy_country = { is_major = yes } }
		add_to_variable = { GER_social_peace = -0.09 }
		add_to_variable = { GER_discontent = 0.14 }
		add_to_variable = { GER_hunger = 0.06 }
		add_to_variable = { GER_kaiser_prestige = -0.03 }
		if = { limit = { has_war_with = ENG date > 1915.3.1 } add_to_variable = { GER_hunger = 0.09 } }
		if = { limit = { has_war_support < 0.40 } add_to_variable = { GER_discontent = 0.12 } }
		if = { limit = { has_stability < 0.40 } add_to_variable = { GER_discontent = 0.12 } }
		if = { limit = { surrender_progress > 0.10 } add_to_variable = { GER_discontent = 0.15 } add_to_variable = { GER_kaiser_prestige = -0.10 } }
	}
	else = {
		add_to_variable = { GER_social_peace = 0.15 }
		add_to_variable = { GER_discontent = -0.15 }
		add_to_variable = { GER_hunger = -0.20 }
		add_to_variable = { GER_kaiser_prestige = 0.03 }
	}
	if = { limit = { has_country_flag = GER_revolutionary_unrest } add_to_variable = { GER_discontent = 0.08 } }
	if = { limit = { has_country_flag = GER_reichstag_peace_resolution_rejected } add_to_variable = { GER_discontent = 0.03 } }
	if = { limit = { has_country_flag = GER_reichstag_peace_resolution_passed } add_to_variable = { GER_social_peace = 0.03 } }
	if = { limit = { has_idea = GER_ukraine_grain_relief } add_to_variable = { GER_hunger = -0.10 } }
	if = { limit = { has_country_flag = brest_litovsk_concluded NOT = { has_country_flag = GER_ev_ukraine_relief } }
		set_country_flag = GER_ev_ukraine_relief
		add_timed_idea = { idea = GER_ukraine_grain_relief days = 365 } }
	if = { limit = { has_country_flag = ger_schlieffen_failed NOT = { has_country_flag = GER_ev_schlieffen_failed } }
		set_country_flag = GER_ev_schlieffen_failed
		add_timed_idea = { idea = GER_schlieffen_plan_failed days = 180 } }
	clamp_variable = { var = GER_social_peace min = 0 max = 100 }
	clamp_variable = { var = GER_discontent min = 0 max = 100 }
	clamp_variable = { var = GER_hunger min = 0 max = 100 }
	clamp_variable = { var = GER_kaiser_prestige min = 0 max = 100 }
	if = {
		limit = { check_variable = { GER_social_peace < 45 } }
		if = { limit = { NOT = { has_idea = GER_social_peace_frayed } } add_ideas = GER_social_peace_frayed }
	}
	else = { remove_ideas = GER_social_peace_frayed }
''' + TIERS + '''	# ---------------- Motim de Kiel / Revolucao de Novembro ----------------
	if = {
		limit = {
			NOT = { has_country_flag = GER_republic_proclaimed }
			NOT = { has_country_flag = GER_kiel_mutiny_underway }
			NOT = { has_country_flag = GER_kiel_cooldown }
			has_war = yes
			date > 1918.10.25
			OR = {
				surrender_progress > 0.20
				has_war_support < 0.30
				check_variable = { GER_discontent > 70 }
			}
		}
		set_country_flag = GER_kiel_window_open
		if = {
			limit = { check_variable = { GER_revolution_count > 0 } }
			country_event = { id = ww1_germany_events.215 days = 4 }
		}
		else = { country_event = { id = ww1_germany_events.214 days = 2 } }
	}
	if = {
		limit = { has_country_flag = GER_kiel_mutiny_underway NOT = { has_country_flag = GER_republic_proclaimed } NOT = { has_country_flag = GER_kiel_window_open } }
		clr_country_flag = GER_kiel_mutiny_underway
	}
	# ---------------- Calendario historico ----------------
''' + CAL + '''}
'''
