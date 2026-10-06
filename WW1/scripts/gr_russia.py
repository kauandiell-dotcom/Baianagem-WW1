"""Conteudo novo da Russia: motor de instabilidade, Revolucao automatica, guerra civil, fim do Imperio."""
from gr_lib import *

E = 'ww1_russia.'
UN, HU, LO, PR, DU, SE, RC = ('SOV_unrest', 'SOV_hunger', 'SOV_army_loyalty', 'SOV_tsar_prestige',
                              'SOV_duma_tension', 'SOV_separatism', 'SOV_repression_count')
pop = lambda ideo, v: 'add_popularity = { ideology = %s popularity = %s }' % (ideology_fix(ideo), v)


def ideology_fix(i):
    return i


def timed(idea_id, days):
    return 'add_timed_idea = { idea = %s days = %d }' % (idea_id, days)


# ============================================================ IDEIAS
MODS = {
    'SOV_hungry_cities_1': ('generic_agrarian_society', {'stability_factor': -0.04, 'consumer_goods_factor': 0.03},
                            'Hungry Cities', 'Cidades Famintas',
                            'Bread is scarce and dear in the industrial cities. Queues lengthen each week.',
                            'O pão é escasso e caro nas cidades industriais. As filas crescem a cada semana.'),
    'SOV_hungry_cities_2': ('generic_economic_crisis', {'stability_factor': -0.10, 'war_support_factor': -0.06, 'consumer_goods_factor': 0.06},
                            'Famine in the Cities', 'Fome nas Cidades',
                            'The capital and the industrial towns are starving. Every rumour of a bread shortage sends crowds into the streets.',
                            'A capital e as cidades industriais passam fome. Cada boato de falta de pão lança multidões nas ruas.'),
    'SOV_restless_workers_1': ('generic_democratic_opposition', {'political_power_gain': -0.10, 'industrial_capacity_factory': -0.04},
                               'Restless Workers', 'Operários Inquietos',
                               'Strikes and factory committees multiply. Production suffers from stoppages.',
                               'Greves e comitês de fábrica se multiplicam. A produção sofre com as paralisações.'),
    'SOV_restless_workers_2': ('generic_guerilla_warfare', {'stability_factor': -0.08, 'industrial_capacity_factory': -0.10, 'political_power_gain': -0.15},
                               'General Strike Fever', 'Febre de Greve Geral',
                               'Whole districts stop work at a word. The authorities no longer control the factory floor.',
                               'Bairros inteiros param de trabalhar a um sinal. As autoridades perderam o controle das fábricas.'),
    'SOV_wavering_army_1': ('generic_army_problems', {'army_morale_factor': -0.08, 'army_org_factor': -0.03},
                            'Wavering Army', 'Exército Vacilante',
                            'Desertion grows and the men grumble at officers and at the war itself.',
                            'As deserções crescem e os homens resmungam contra os oficiais e contra a própria guerra.'),
    'SOV_wavering_army_2': ('generic_disjointed_gov', {'army_morale_factor': -0.18, 'army_org_factor': -0.08, 'army_attack_factor': -0.05},
                            'Army on the Verge of Mutiny', 'Exército à Beira do Motim',
                            'Regiments refuse orders, elect committees and leave the trenches. The front is dissolving.',
                            'Regimentos recusam ordens, elegem comitês e abandonam as trincheiras. A frente se desfaz.'),
    'SOV_supreme_command_burden': ('generic_army_war_college', {'army_org_factor': -0.03, 'political_power_gain': -0.10, 'stability_factor': -0.03},
                                   'The Tsar at Mogilev', 'O Tsar em Mogilev',
                                   'The Tsar commands the army in person while the capital is left to the Empress and her favourite.',
                                   'O Tsar comanda o exército pessoalmente enquanto a capital fica nas mãos da Imperatriz e de seu favorito.'),
    'SOV_refugee_flood': ('generic_immigration', {'consumer_goods_factor': 0.04, 'stability_factor': -0.03, 'production_speed_buildings_factor': -0.05},
                          'Refugees on the Roads', 'Refugiados nas Estradas',
                          'Millions of refugees from Poland and Galicia strain the railways and the food supply of the interior.',
                          'Milhões de refugiados da Polônia e da Galícia sobrecarregam as ferrovias e o abastecimento do interior.'),
    'SOV_society_mobilised': ('generic_central_management', {'production_speed_buildings_factor': 0.05, 'industrial_capacity_factory': 0.03, 'stability_factor': 0.02},
                              'Society Mobilised', 'Sociedade Mobilizada',
                              'Zemstvos, town unions and industrialists organise supplies for the army alongside the state.',
                              'Zemstvos, uniões municipais e industriais organizam o abastecimento do exército ao lado do Estado.'),
    'SOV_lena_shadow': ('generic_exploit_mines', {'political_power_gain': -0.05, 'stability_factor': -0.02},
                        'Shadow of the Lena', 'A Sombra do Lena',
                        'The massacre in the goldfields has turned a generation of workers against the regime.',
                        'O massacre nos campos de ouro voltou uma geração de operários contra o regime.'),
    'SOV_separatist_fever': ('generic_local_self_management', {'stability_factor': -0.05, 'industrial_capacity_factory': -0.05, 'resistance_target': 0.05},
                             'Separatist Fever', 'Febre Separatista',
                             'Finns, Poles, Ukrainians, Balts and Caucasians look to independence as the centre weakens.',
                             'Finlandeses, poloneses, ucranianos, bálticos e caucasianos olham para a independência enquanto o centro se enfraquece.'),
    'SOV_civil_war_exhaustion': ('generic_monarchist_uprising', {'stability_factor': -0.05, 'industrial_capacity_factory': -0.10, 'consumer_goods_factor': 0.10, 'political_power_gain': -0.10},
                                 'Ravaged by Civil War', 'Devastada pela Guerra Civil',
                                 'Reds, Whites, Greens and foreign armies have wrecked railways, mines and harvests.',
                                 'Vermelhos, brancos, verdes e exércitos estrangeiros destruíram ferrovias, minas e colheitas.'),
    'SOV_nep_recovery': ('generic_economic_recovery', {'consumer_goods_factor': -0.05, 'stability_factor': 0.05, 'production_speed_buildings_factor': 0.10},
                         'New Economic Policy', 'Nova Política Econômica',
                         'Requisitions give way to a tax in kind and small private trade. The villages breathe again.',
                         'As requisições cedem lugar a um imposto em espécie e ao pequeno comércio privado. As aldeias respiram.'),
    'SOV_ussr_union': ('generic_flexible_foreign_policy', {'stability_factor': 0.05, 'political_power_gain': 0.10, 'resistance_target': -0.10},
                       'Union of Soviet Republics', 'União de Repúblicas Soviéticas',
                       'A federal treaty binds the Soviet republics into a single state.',
                       'Um tratado federal une as repúblicas soviéticas em um único Estado.'),
}
for k, (pic, m, en, pt, den, dpt) in MODS.items():
    idea(k, pic, m, en, pt, den, dpt)

# ============================================================ EVENTOS
NOT_ABD = 'NOT = { has_country_flag = SOV_tsar_abdicated }'

event(E + '200', 'sov_lena',
      ('Massacre at the Lena Goldfields', 'Massacre nas Minas de Ouro do Lena'),
      ('Troops have fired on striking miners in the Siberian goldfields of the Lena River. Hundreds lie dead or wounded, and the news is spreading through every factory town of the Empire.',
       'Tropas abriram fogo contra mineiros em greve nos campos de ouro do rio Lena, na Sibéria. Centenas estão mortos ou feridos, e a notícia corre por todas as cidades industriais do Império.'),
      [('The authorities acted within the law.', 'As autoridades agiram dentro da lei.',
        fx(V(UN, 9), V(PR, -3), 'add_political_power = 20', timed('SOV_lena_shadow', 540)), 60, None),
       ('Open a commission of inquiry.', 'Abrir uma comissão de inquérito.',
        fx(V(UN, 3), V(DU, -8), 'add_political_power = -25', 'add_stability = 0.01'), 40, None)])

event(E + '201', 'sov_putilov',
      ('The July Strikes', 'As Greves de Julho'),
      ('As French President Poincaré visits the capital, a wave of strikes grips the Putilov Works and the workers districts. Barricades go up in Petersburg while the Empire edges toward a European war.',
       'Enquanto o presidente francês Poincaré visita a capital, uma onda de greves toma a Fábrica Putilov e os bairros operários. Barricadas sobem em Petersburgo enquanto o Império se aproxima de uma guerra europeia.'),
      [('Break the strikes with police and Cossacks.', 'Quebrar as greves com a polícia e os cossacos.',
        fx(V(UN, -4), V(PR, -2), 'add_stability = -0.02'), 55, None),
       ('Wait for the war to unite the nation.', 'Esperar que a guerra una a nação.',
        fx(V(UN, 4), 'add_war_support = 0.02'), 45, None)])

event(E + '202', 'sov_supreme_command',
      ('The Tsar Takes Supreme Command', 'O Tsar Assume o Comando Supremo'),
      ('Against the advice of nearly all his ministers, Nicholas II dismisses Grand Duke Nicholas and takes personal command of the army at Mogilev, leaving the government of the capital to the Empress and Rasputin.',
       'Contra o conselho de quase todos os ministros, Nicolau II demite o Grão-Duque Nicolau e assume pessoalmente o comando do exército em Mogilev, deixando o governo da capital à Imperatriz e a Rasputin.'),
      [('The Tsar commands in person.', 'O Tsar comanda pessoalmente.',
        fx(V(PR, -8), V(LO, 4), 'add_ideas = SOV_supreme_command_burden'), 70, None),
       ('Persuade him to remain in the capital.', 'Persuadi-lo a permanecer na capital.',
        fx(V(DU, 5), V(LO, -3), 'add_political_power = -30', 'army_experience = 5'), 30, None)])

event(E + '203', 'sov_great_retreat',
      ('The Great Retreat', 'A Grande Retirada'),
      ('The Gorlice-Tarnów offensive has driven the army out of Galicia and Poland. Millions of refugees clog the roads east, and the shell shortage leaves the front without guns.',
       'A ofensiva de Gorlice-Tarnów expulsou o exército da Galícia e da Polônia. Milhões de refugiados entopem as estradas para o leste, e a falta de projéteis deixa a frente sem canhões.'),
      [('Scorched earth and mass evacuation.', 'Terra arrasada e evacuação em massa.',
        fx(V(HU, 8), V(UN, 6), 'army_experience = 10', timed('SOV_refugee_flood', 240)), 40, None),
       ('Hold the line at any cost.', 'Manter a linha a qualquer custo.',
        fx(V(LO, -6), 'army_experience = 15', timed('SOV_shell_shortage_crisis', 200)), 25, None),
       ('Call on society: Zemgor and the War Industries Committees.', 'Convocar a sociedade: Zemgor e os Comitês da Indústria de Guerra.',
        fx(V(DU, -10), 'add_political_power = -40', timed('SOV_society_mobilised', 300)), 35, None)])

event(E + '204', 'sov_duma_prorogued',
      ('The Duma Is Prorogued', 'A Duma É Suspensa'),
      ('The Progressive Bloc demands a government that enjoys public confidence. The Tsar answers by proroguing the Duma and sending the deputies home, closing the last legal outlet for criticism of the court.',
       'O Bloco Progressista exige um governo que goze da confiança pública. O Tsar responde suspendendo a Duma e mandando os deputados para casa, fechando a última saída legal para a crítica à corte.'),
      [('Prorogue the Duma.', 'Suspender a Duma.',
        fx(V(DU, 25), V(UN, 5), 'add_political_power = 25', 'add_stability = -0.02'), 55, None),
       ('Accept a Ministry of Public Confidence.', 'Aceitar um Ministério de Confiança Pública.',
        fx(V(DU, -15), V(PR, -5), 'add_stability = 0.03', 'add_political_power = -20'), 45, None)],
      trigger='has_war = yes')

event(E + '205', 'sov_rasputin_murder',
      ('The Murder of Rasputin', 'O Assassinato de Rasputin'),
      ('In the early hours, Prince Yusupov and Grand Duke Dmitri lure the starets to the Yusupov Palace. The favourite of the Empress is dead, but the court has lost its last hold on the Tsar and the nobility has shown it will act without him.',
       'De madrugada, o príncipe Yusupov e o Grão-Duque Dmitri atraem o starets ao Palácio Yusupov. O favorito da Imperatriz está morto, mas a corte perdeu seu último domínio sobre o Tsar e a nobreza mostrou que agirá sem ele.'),
      [('The court is finally rid of him.', 'A corte finalmente se livrou dele.',
        fx('set_country_flag = SOV_rasputin_dead', 'remove_ideas = SOV_rasputin_court_intrigues', V(PR, -6), V(DU, -10), 'add_stability = 0.02'), 60, None),
       ('Exile the conspirators to the front.', 'Exilar os conspiradores para a frente.',
        fx('set_country_flag = SOV_rasputin_dead', 'remove_ideas = SOV_rasputin_court_intrigues', V(PR, -3), V(UN, 3), V(LO, 2), 'add_political_power = 30'), 40, None)])

event(E + '206', 'sov_army_wavers',
      ('The Army Wavers', 'O Exército Vacila'),
      ('Reports from the front speak of desertion, fraternisation and soldiers who no longer salute their officers. The staff warns that the men are tired of a war they do not understand.',
       'Relatos da frente falam de deserção, confraternização e soldados que não saúdam mais os oficiais. O estado-maior alerta que os homens estão cansados de uma guerra que não compreendem.'),
      [('Shoot deserters and tighten discipline.', 'Fuzilar desertores e endurecer a disciplina.',
        fx(V(LO, 5), V(UN, 4), 'add_stability = -0.02', 'add_war_support = -0.01'), 40, None),
       ('Promise land after victory.', 'Prometer terra após a vitória.',
        fx(V(LO, 4), 'add_political_power = -20', 'add_war_support = 0.02'), 40, None),
       ('Rotate divisions to the rear for rest.', 'Revezar divisões para a retaguarda para descanso.',
        fx(V(LO, 7), 'add_political_power = -35', 'add_war_support = -0.02'), 20, None)])

event(E + '207', 'sov_stolypin_harvest',
      ('The Fruits of the Land Reform', 'Os Frutos da Reforma Agrária'),
      ('Years of land reform are bearing fruit: the Peasants Land Bank has settled a million households on consolidated farms and in Siberia. But the communal villages are bitter at the loss of the old ways.',
       'Anos de reforma agrária dão frutos: o Banco Camponês de Terras assentou um milhão de famílias em propriedades consolidadas e na Sibéria. Mas as aldeias comunais estão amargas com o fim dos velhos costumes.'),
      [('Press on with the reform.', 'Prosseguir com a reforma.',
        fx(V(HU, -4), V(UN, 3), 'add_stability = 0.01', 'add_political_power = 20'), 55, None),
       ('Slow the pace to calm the villages.', 'Reduzir o ritmo para acalmar as aldeias.',
        fx(V(UN, -3), V(HU, 2), 'add_political_power = -10'), 45, None)])

event(E + '208', 'sov_army_programme',
      ('The Great Military Programme', 'O Grande Programa Militar'),
      ('The War Ministry presents a vast expansion of the army and its artillery to be completed by 1917. The Finance Ministry warns that the budget cannot bear it.',
       'O Ministério da Guerra apresenta uma vasta expansão do exército e da artilharia a ser concluída até 1917. O Ministério das Finanças adverte que o orçamento não suporta.'),
      [('Approve the full programme.', 'Aprovar o programa completo.',
        fx('army_experience = 15', 'add_political_power = -25', 'add_stability = -0.01', 'add_war_support = 0.03'), 55, None),
       ('Approve a reduced programme.', 'Aprovar um programa reduzido.',
        fx('army_experience = 5', 'add_political_power = 15'), 45, None)])

event(E + '209', 'sov_bread_lines',
      ('Bread Lines in Petrograd', 'Filas de Pão em Petrogrado'),
      ('Snow and broken railways have cut grain deliveries to the capital. Women queue in the dark for bread while the price of flour doubles.',
       'A neve e as ferrovias quebradas cortaram as entregas de grãos à capital. Mulheres fazem fila no escuro por pão enquanto o preço da farinha dobra.'),
      [('Fix bread prices and ration flour.', 'Tabelar o preço do pão e racionar a farinha.',
        fx(V(HU, -8), V(UN, 2), 'add_political_power = -30', 'add_stability = -0.01'), 40, None),
       ('Send the police to disperse the queues.', 'Enviar a polícia para dispersar as filas.',
        fx(V(UN, 6), V(HU, 5), 'add_stability = -0.03'), 25, None),
       ('Ask the Zemstvos to organise relief.', 'Pedir aos Zemstvos que organizem socorro.',
        fx(V(HU, -5), V(DU, -5), 'add_political_power = -20'), 35, None)],
      immediate=fx(V(HU, 12), V(UN, 8)), trigger='has_war = yes')

# ---- a Revolucao
event(E + '210', 'sov_petrograd_uprising',
      ('The Petrograd Uprising', 'A Insurreição de Petrogrado'),
      ('Bread riots have turned into a general strike. Soldiers of the capital garrison have been ordered to fire on the crowds, and some regiments are refusing. The Tsar is at Mogilev, and Petrograd is slipping out of his hands.',
       'Os motins do pão viraram greve geral. Soldados da guarnição da capital receberam ordem de atirar nas multidões, e alguns regimentos se recusam. O Tsar está em Mogilev, e Petrogrado escapa de suas mãos.'),
      [('Let events run their course.', 'Deixar os acontecimentos seguirem seu curso.',
        fx(V(UN, 5), 'country_event = { id = ww1_russia.211 days = 3 }'), 55, None),
       ('Order the garrison to restore order.', 'Ordenar que a guarnição restabeleça a ordem.',
        fx(V(RC, 1), V(UN, -15), V(LO, -12), 'add_stability = -0.05', 'clr_country_flag = SOV_revolution_window_open',
           'set_country_flag = { flag = SOV_revolution_cooldown days = 60 }'), 45,
        'check_variable = { SOV_repression_count < 3 }')],
      immediate='set_country_flag = SOV_february_crisis_underway', trigger=NOT_ABD)
# fire_only_once impede repeticao da repressao; a janela reabre com um novo evento espelho:
event(E + '213', 'sov_april_theses',
      ('Lenin Returns to Petrograd', 'Lênin Retorna a Petrogrado'),
      ('Lenin has crossed Germany in a sealed train and arrives at the Finland Station. He denounces the war and the Provisional Government and demands all power to the Soviets.',
       'Lênin atravessou a Alemanha em um trem lacrado e chega à Estação da Finlândia. Denuncia a guerra e o Governo Provisório e exige todo o poder aos Sovietes.'),
      [('Dismiss him as a German agent.', 'Descartá-lo como agente alemão.',
        fx(V(UN, 3), pop('communism', 0.02), 'add_war_support = 0.02'), 40, None),
       ('Arrest the Bolshevik leaders.', 'Prender os líderes bolcheviques.',
        fx('add_political_power = -30', V(UN, 8), 'add_stability = -0.03', pop('communism', 0.01), 'set_country_flag = SOV_lenin_arrested'), 30, None),
       ('Offer the Soviet seats in the Cabinet.', 'Oferecer ao Soviete assentos no Gabinete.',
        fx(V(UN, -6), pop('democratic', 0.02), pop('communism', 0.03)), 30, None)],
      trigger='has_country_flag = SOV_provisional_gov_in_power')

event(E + '211', 'sov_abdication',
      ('The Tsar Abdicates', 'O Tsar Abdica'),
      ('Faced with mutiny in the capital and the advice of his generals, Nicholas II signs the instrument of abdication in a railway carriage at Pskov. Three centuries of Romanov rule are over; the Duma forms a Provisional Government alongside the Petrograd Soviet.',
       'Diante do motim na capital e do conselho de seus generais, Nicolau II assina a abdicação em um vagão de trem em Pskov. Três séculos de domínio Romanov terminam; a Duma forma um Governo Provisório ao lado do Soviete de Petrogrado.'),
      [('A Provisional Government takes over.', 'Um Governo Provisório assume.',
        fx('set_country_flag = SOV_tsar_abdicated', 'set_country_flag = SOV_provisional_gov_open', 'set_country_flag = SOV_provisional_gov_in_power',
           'clr_country_flag = SOV_revolution_window_open',
           'set_politics = { ruling_party = democratic elections_allowed = yes }',
           'remove_ideas = SOV_tsarist_autocracy', 'remove_ideas = SOV_supreme_command_burden', 'add_ideas = SOV_dual_power_dvoevlastie',
           pop('democratic', 0.15), pop('communism', 0.05), V(PR, -100), V(DU, -30), V(UN, -20), V(LO, -8),
           'country_event = { id = ww1_russia.212 days = 20 }',
           'if = { limit = { country_exists = GER } GER = { country_event = { id = ww1_germany_events.230 days = 2 } } }'), 90, None),
       ('The Tsar appeals to loyal troops.', 'O Tsar apela às tropas leais.',
        fx('set_country_flag = SOV_tsarist_path_open', 'set_country_flag = SOV_path_tsarist', 'clr_country_flag = SOV_revolution_window_open',
           V(LO, -5), V(UN, 10), 'add_stability = -0.05', 'add_ideas = SOV_divine_autocracy'), 10,
        'check_variable = { SOV_army_loyalty > 44 }')],
      trigger=NOT_ABD)

event(E + '212', 'sov_dual_power',
      ('Dual Power', 'Duplo Poder'),
      ('Two authorities now share the capital: the Provisional Government, which has the ministries, and the Petrograd Soviet, which has the soldiers. Order No. 1 has placed the garrison under elected committees.',
       'Duas autoridades dividem a capital: o Governo Provisório, que tem os ministérios, e o Soviete de Petrogrado, que tem os soldados. A Ordem n. 1 colocou a guarnição sob comitês eleitos.'),
      [('Rule through the Provisional Government.', 'Governar por meio do Governo Provisório.',
        fx(V(LO, -6), V(UN, -5), 'add_political_power = 30'), 60, None),
       ('Work with the Soviet executive.', 'Trabalhar com o executivo do Soviete.',
        fx(V(LO, 4), V(UN, -10), 'add_stability = -0.03', pop('communism', 0.04)), 40, None)])

event(E + '214', 'sov_july_days',
      ('The July Days', 'As Jornadas de Julho'),
      ('After the failed summer offensive, soldiers, sailors and workers march on the Tauride Palace demanding peace and bread. The government must decide how to answer.',
       'Após o fracasso da ofensiva de verão, soldados, marinheiros e operários marcham sobre o Palácio de Táurida exigindo paz e pão. O governo precisa decidir como responder.'),
      [('Crush the demonstrations.', 'Esmagar as manifestações.',
        fx(V(UN, -10), V(LO, -5), pop('communism', -0.02), 'add_stability = -0.02', 'set_country_flag = SOV_july_crushed'), 50, None),
       ('Promise reforms and talk.', 'Prometer reformas e dialogar.',
        fx(V(UN, -5), 'add_political_power = 25', pop('communism', 0.03)), 50, None)],
      trigger='has_country_flag = SOV_provisional_gov_in_power')

event(E + '215', 'sov_kornilov_crisis',
      ('The Kornilov Crisis', 'A Crise Kornilov'),
      ('General Kornilov, commander in chief, is marching troops toward Petrograd to restore order. The government calls on the capital workers and sailors to defend the revolution, arming the Bolsheviks in the process. It can no longer command the loyalty of either side.',
       'O general Kornilov, comandante em chefe, marcha com tropas para Petrogrado para restaurar a ordem. O governo convoca operários e marinheiros da capital para defender a revolução, armando os bolcheviques no processo. Já não comanda a lealdade de nenhum dos lados.'),
      [('Arrest Kornilov and arm the workers.', 'Prender Kornilov e armar os operários.',
        fx('set_country_flag = SOV_path_bolshevik', 'set_country_flag = SOV_bolshevik_path_open', V(LO, -8), V(UN, 10), pop('communism', 0.12),
           'country_event = { id = ww1_russia.216 days = 50 }'), 40, None),
       ('Join Kornilov against the Soviets.', 'Unir-se a Kornilov contra os Sovietes.',
        fx('set_country_flag = SOV_path_kornilov', 'set_country_flag = SOV_kornilov_path_open', pop('fascism', 0.10),
           'country_event = { id = ww1_russia.217 days = 10 }'), 25, None),
       ('Call a Constituent Assembly and hold the centre.', 'Convocar uma Assembleia Constituinte e manter o centro.',
        fx('set_country_flag = SOV_path_democratic', V(UN, 5), pop('democratic', 0.10),
           'country_event = { id = ww1_russia.218 days = 70 }'), 35, None)],
      trigger=fx('has_country_flag = SOV_provisional_gov_in_power',
                 'NOT = { has_country_flag = SOV_path_bolshevik }', 'NOT = { has_country_flag = SOV_path_kornilov }',
                 'NOT = { has_country_flag = SOV_path_democratic }'))

event(E + '216', 'sov_october',
      ('The October Revolution', 'A Revolução de Outubro'),
      ('On the night of 25 October, Red Guards and sailors seize the bridges, the telegraph and the Winter Palace. The Provisional Government is arrested, and the Second Congress of Soviets hands power to a Council of People Commissars under Lenin.',
       'Na noite de 25 de outubro, Guardas Vermelhos e marinheiros tomam as pontes, o telégrafo e o Palácio de Inverno. O Governo Provisório é preso, e o Segundo Congresso dos Sovietes entrega o poder a um Conselho de Comissários do Povo sob Lênin.'),
      [('All power to the Soviets!', 'Todo o poder aos Sovietes!',
        fx('set_politics = { ruling_party = communism elections_allowed = no }', 'remove_ideas = SOV_dual_power_dvoevlastie',
           'add_ideas = SOV_dictatorship_of_the_proletariat', 'set_country_flag = SOV_bolshevik_path_chosen', 'clr_country_flag = SOV_provisional_gov_in_power',
           pop('communism', 0.40), V(UN, -20), V(LO, -10), 'add_political_power = 100',
           'country_event = { id = ww1_russia.220 days = 45 }',
           'if = { limit = { country_exists = GER } GER = { country_event = { id = ww1_germany_events.231 days = 3 } } }'), 100, None)],
      trigger='has_country_flag = SOV_path_bolshevik')

event(E + '217', 'sov_kornilov_power',
      ('Kornilov Takes Petrograd', 'Kornilov Toma Petrogrado'),
      ('Kornilov Cossacks and shock battalions enter Petrograd. The Soviets are dissolved, the death penalty is restored at the front and the Provisional Government is swept aside by a military directory.',
       'Os cossacos de Kornilov e os batalhões de choque entram em Petrogrado. Os Sovietes são dissolvidos, a pena de morte volta à frente e o Governo Provisório é varrido por um diretório militar.'),
      [('A military dictatorship restores order.', 'Uma ditadura militar restabelece a ordem.',
        fx('set_politics = { ruling_party = fascism elections_allowed = no }', 'remove_ideas = SOV_dual_power_dvoevlastie',
           'add_ideas = SOV_salvation_directory_rule', 'set_country_flag = SOV_kornilov_path_chosen', 'clr_country_flag = SOV_provisional_gov_in_power',
           pop('fascism', 0.30), V(UN, -10), V(LO, 10), 'country_event = { id = ww1_russia.220 days = 30 }'), 100, None)],
      trigger='has_country_flag = SOV_path_kornilov')

event(E + '218', 'sov_assembly_election',
      ('Elections to the Constituent Assembly', 'Eleições para a Assembleia Constituinte'),
      ('Russia votes in the first free election in its history. The Socialist Revolutionaries win a plurality; the Bolsheviks hold the capital and the garrisons. The Assembly is to meet in Petrograd.',
       'A Rússia vota na primeira eleição livre de sua história. Os Socialistas Revolucionários obtêm a pluralidade; os bolcheviques dominam a capital e as guarnições. A Assembleia deve se reunir em Petrogrado.'),
      [('Convene the Assembly as planned.', 'Convocar a Assembleia como planejado.',
        fx(pop('democratic', 0.05), 'country_event = { id = ww1_russia.219 days = 45 }'), 60, None),
       ('Postpone it until the war is over.', 'Adiá-la até o fim da guerra.',
        fx(V(UN, 8), pop('communism', 0.06), 'set_country_flag = SOV_assembly_postponed', 'country_event = { id = ww1_russia.219 days = 45 }'), 40, None)],
      trigger='has_country_flag = SOV_path_democratic')

event(E + '219', 'sov_assembly_dispersal',
      ('The Constituent Assembly Meets', 'A Assembleia Constituinte se Reúne'),
      ('The Constituent Assembly meets in the Tauride Palace, guarded by armed sailors who are not its friends. Its fate depends on who commands the garrison.',
       'A Assembleia Constituinte se reúne no Palácio de Táurida, guardada por marinheiros armados que não são seus amigos. Seu destino depende de quem comanda a guarnição.'),
      [('The Assembly proclaims the Russian Republic.', 'A Assembleia proclama a República Russa.',
        fx('set_politics = { ruling_party = democratic elections_allowed = yes }', 'remove_ideas = SOV_dual_power_dvoevlastie',
           'add_ideas = SOV_russian_federal_republic', 'clr_country_flag = SOV_provisional_gov_in_power', pop('democratic', 0.20), 'add_stability = 0.05', V(UN, -8)), 100,
        'check_variable = { SOV_army_loyalty > 39 }\nNOT = { has_country_flag = SOV_assembly_postponed }'),
       ('The Red Guards disperse the Assembly.', 'A Guarda Vermelha dispersa a Assembleia.',
        fx('set_country_flag = SOV_path_bolshevik', 'country_event = { id = ww1_russia.216 days = 5 }'), 100,
        'OR = { check_variable = { SOV_army_loyalty < 40 } has_country_flag = SOV_assembly_postponed }')],
      trigger='has_country_flag = SOV_path_democratic')

event(E + '220', 'sov_civil_war',
      ('Reds and Whites', 'Vermelhos e Brancos'),
      ('Generals, Cossack atamans and Socialist Revolutionaries raise armies against the new order in the south, on the Volga and in Siberia. Russia is divided between Reds and Whites, and the Allies and the Central Powers watch for their chance.',
       'Generais, atamãs cossacos e Socialistas Revolucionários levantam exércitos contra a nova ordem no sul, no Volga e na Sibéria. A Rússia se divide entre vermelhos e brancos, e os Aliados e as Potências Centrais aguardam sua oportunidade.'),
      [('To arms!', 'Às armas!',
        fx('set_country_flag = SOV_civil_war_started', 'add_political_power = 50', V(UN, 10), 'add_ideas = SOV_civil_war_exhaustion',
           'if = { limit = { has_government = communism } start_civil_war = { ideology = neutrality size = 0.40 } }',
           'else_if = { limit = { has_government = fascism } start_civil_war = { ideology = communism size = 0.35 } }'), 100, None)],
      trigger='NOT = { has_country_flag = SOV_civil_war_started }')

event(E + '221', 'sov_czech_legion',
      ('The Czech Legion Revolts', 'A Legião Tcheca se Revolta'),
      ('Forty thousand Czechoslovak soldiers strung along the Trans-Siberian Railway refuse to disarm. In days they hold the line from the Volga to Vladivostok and the towns fall one after another.',
       'Quarenta mil soldados tchecoslovacos espalhados ao longo da Transiberiana recusam-se a desarmar. Em poucos dias controlam a linha do Volga a Vladivostok e as cidades caem uma após outra.'),
      [('Try to disarm the Legion by force.', 'Tentar desarmar a Legião pela força.',
        fx(V(UN, 5), 'army_experience = 10', 'add_stability = -0.03'), 50, None),
       ('Negotiate passage to Vladivostok.', 'Negociar a passagem para Vladivostok.',
        fx('add_political_power = -30', V(LO, 2), 'add_stability = 0.01'), 50, None)],
      trigger='has_country_flag = SOV_civil_war_started')

event(E + '222', 'sov_kolchak',
      ('Kolchak, Supreme Ruler', 'Kolchak, Governante Supremo'),
      ('Admiral Kolchak seizes power at Omsk and is proclaimed Supreme Ruler of Russia by the Whites. With Allied supplies behind him, his armies start westward over the Urals.',
       'O almirante Kolchak toma o poder em Omsk e é proclamado Governante Supremo da Rússia pelos brancos. Com suprimentos aliados às costas, seus exércitos avançam para o oeste pelos Urais.'),
      [('Send the best divisions east.', 'Enviar as melhores divisões para o leste.',
        fx('army_experience = 15', V(LO, 3), 'add_political_power = -50'), 60, None),
       ('Rely on partisans in the Siberian rear.', 'Confiar nos guerrilheiros na retaguarda siberiana.',
        fx(V(UN, 4), 'army_experience = 5', 'add_political_power = 20'), 40, None)],
      trigger='has_country_flag = SOV_civil_war_started')

event(E + '223', 'sov_wrangel',
      ('Wrangel in the Crimea', 'Wrangel na Crimeia'),
      ('Baron Wrangel reorganises the remnants of the White armies behind the Perekop isthmus and the Crimean fortifications. If the Reds can take the peninsula the civil war is won.',
       'O barão Wrangel reorganiza os restos dos exércitos brancos atrás do istmo de Perekop e das fortificações da Crimeia. Se os vermelhos tomarem a península, a guerra civil está ganha.'),
      [('Storm Perekop across the frozen Sivash.', 'Assaltar Perekop pelo Sivash congelado.',
        fx('army_experience = 20', V(LO, -3), 'add_stability = -0.02', 'set_country_flag = SOV_civil_war_won', 'remove_ideas = SOV_civil_war_exhaustion'), 60, None),
       ('Offer an amnesty to White officers.', 'Oferecer anistia aos oficiais brancos.',
        fx('add_political_power = -30', V(LO, 2), 'set_country_flag = SOV_civil_war_won', 'remove_ideas = SOV_civil_war_exhaustion'), 40, None)],
      trigger='has_country_flag = SOV_civil_war_started')

event(E + '224', 'sov_kronstadt',
      ('The Kronstadt Rebellion', 'A Rebelião de Kronstadt'),
      ('The sailors who were once the pride of the revolution raise the flag of revolt against the Bolsheviks: soviets without communists, free trade and an end to requisitions.',
       'Os marinheiros que já foram o orgulho da revolução levantam a bandeira da revolta contra os bolcheviques: sovietes sem comunistas, livre comércio e fim das requisições.'),
      [('Crush the rebels across the ice.', 'Esmagar os rebeldes pelo gelo.',
        fx(V(UN, -10), 'add_stability = -0.05', V(LO, 3)), 55, None),
       ('Open negotiations with the sailors.', 'Abrir negociações com os marinheiros.',
        fx(V(UN, 5), 'add_political_power = -40', 'add_stability = 0.01'), 45, None)],
      trigger=fx('has_government = communism', 'has_country_flag = SOV_civil_war_started'))

event(E + '225', 'sov_nep',
      ('The New Economic Policy', 'A Nova Política Econômica'),
      ('Lenin tells the Party Congress that the peasantry must be allowed to trade. Grain requisitions are replaced by a tax in kind and small enterprises may be privately run.',
       'Lênin diz ao Congresso do Partido que o campesinato deve poder comerciar. As requisições de grãos são substituídas por um imposto em espécie e pequenas empresas podem ser privadas.'),
      [('Adopt the New Economic Policy.', 'Adotar a Nova Política Econômica.',
        fx(V(HU, -15), V(UN, -10), 'add_ideas = SOV_nep_recovery', 'remove_ideas = SOV_civil_war_exhaustion', 'add_stability = 0.03'), 65, None),
       ('Keep War Communism a little longer.', 'Manter o Comunismo de Guerra por mais tempo.',
        fx(V(HU, 6), V(UN, 6), 'add_political_power = 40'), 35, None)],
      trigger=fx('has_government = communism', 'has_country_flag = SOV_civil_war_started'))

event(E + '226', 'sov_ussr',
      ('The Union Treaty', 'O Tratado da União'),
      ('Delegates of the Russian, Transcaucasian, Ukrainian and Belarusian Soviet republics sign a treaty of union. A single state with a single army, a single foreign policy and a single Party is born.',
       'Delegados das repúblicas soviéticas russa, transcaucasiana, ucraniana e bielorrussa assinam um tratado de união. Nasce um Estado único, com um só exército, uma só política externa e um só Partido.'),
      [('Sign the Treaty of Union.', 'Assinar o Tratado da União.',
        fx('add_ideas = SOV_ussr_union', 'add_stability = 0.05', 'add_political_power = 100', 'set_country_flag = SOV_ussr_formed'), 100, None)],
      trigger='has_government = communism')

event(E + '227', 'sov_tsar_family',
      ('The Fate of the Romanovs', 'O Destino dos Romanov'),
      ('The former Tsar and his family are held in the Ipatiev House in Yekaterinburg while White armies and the Czech Legion approach the town. The Ural Soviet asks what to do with its prisoners.',
       'O ex-Tsar e sua família estão presos na Casa Ipatiev, em Ecaterimburgo, enquanto exércitos brancos e a Legião Tcheca se aproximam da cidade. O Soviete dos Urais pergunta o que fazer com os prisioneiros.'),
      [('The Ural Soviet carries out the sentence.', 'O Soviete dos Urais executa a sentença.',
        fx(V(PR, -100), V(LO, 2), 'add_stability = -0.02', 'set_country_flag = SOV_romanovs_executed'), 55, None),
       ('Move them to Moscow for a public trial.', 'Transferi-los para Moscou para um julgamento público.',
        fx('add_political_power = -30', V(UN, 3), 'set_country_flag = SOV_romanovs_tried'), 45, None)],
      trigger=fx('has_country_flag = SOV_tsar_abdicated', 'has_government = communism'))

event(E + '228', 'sov_church_council',
      ('The All-Russian Church Council', 'O Concílio Panrusso da Igreja'),
      ('For the first time since Peter the Great the Orthodox Church meets in council and restores the Patriarchate. The question of its place in the new Russia hangs in the air.',
       'Pela primeira vez desde Pedro, o Grande, a Igreja Ortodoxa se reúne em concílio e restaura o Patriarcado. A questão de seu lugar na nova Rússia paira no ar.'),
      [('Support the Church as a pillar of order.', 'Apoiar a Igreja como pilar da ordem.',
        fx('add_stability = 0.02', V(UN, -3), 'add_political_power = -20'), 50, None),
       ('Separate Church and State.', 'Separar Igreja e Estado.',
        fx('add_political_power = 25', V(UN, 3), 'add_stability = -0.01'), 50, None)],
      trigger='has_country_flag = SOV_tsar_abdicated')

# ---- fim do Imperio: cada nacao
def breakup(eid, pic, tag, t, d, opts):
    event(E + eid, pic, t, d, opts,
          trigger='any_owned_state = { is_core_of = %s }' % tag)

refuse = lambda tag: fx(V(SE, 10), V(UN, 5), 'add_stability = -0.02')
breakup('230', 'sov_finland', 'FIN',
        ('Finland Demands Independence', 'A Finlândia Exige Independência'),
        ('With the Tsar gone, the Finnish Diet declares that the ties of union have fallen with the Grand Duke. Helsinki asks for recognition and the Finnish Red and White camps are already arming.',
         'Com o Tsar fora de cena, a Dieta finlandesa declara que os laços da união caíram com o Grão-Duque. Helsinque pede reconhecimento e os campos vermelho e branco finlandeses já se armam.'),
        [('Recognise Finnish independence.', 'Reconhecer a independência da Finlândia.', fx('release = FIN', V(SE, -10)), 35, None),
         ('Grant autonomy as a protectorate.', 'Conceder autonomia como protetorado.', fx('release_puppet = FIN', V(SE, -5)), 30, None),
         ('Refuse to discuss it.', 'Recusar discutir o assunto.', refuse('FIN'), 35, None)])
breakup('231', 'sov_ukraine', 'UKR',
        ('The Ukrainian Rada', 'A Rada Ucraniana'),
        ('The Central Rada in Kiev proclaims a Ukrainian People Republic. The grain of the south, the Donbas coal and a fifth of the empire population hang on the answer.',
         'A Rada Central em Kiev proclama uma República Popular Ucraniana. O trigo do sul, o carvão do Donbas e um quinto da população do império dependem da resposta.'),
        [('Recognise the Ukrainian Republic.', 'Reconhecer a República Ucraniana.', fx('release = UKR', V(SE, -10), V(HU, 8)), 35, None),
         ('Offer autonomy inside a federation.', 'Oferecer autonomia dentro de uma federação.', fx('release_puppet = UKR', V(SE, -5), V(HU, 4)), 25, None),
         ('Send troops to Kiev.', 'Enviar tropas a Kiev.', fx('army_experience = 10', V(SE, 8), V(LO, -4), V(UN, 4)), 40, None)])
breakup('232', 'sov_baltic', 'EST',
        ('The Baltic Lands', 'As Terras Bálticas'),
        ('German armies stand on the Dvina and the councils of Estonia, Latvia and Lithuania demand self-determination. Whatever Petrograd answers, Berlin will have its own plans for the Baltic.',
         'Exércitos alemães estão no Dvina e os conselhos da Estônia, Letônia e Lituânia exigem autodeterminação. Seja qual for a resposta de Petrogrado, Berlim terá seus próprios planos para o Báltico.'),
        [('Recognise the Baltic states.', 'Reconhecer os Estados bálticos.',
          fx('release = EST', 'release = LAT', 'release = LIT', V(SE, -10)), 35, None),
         ('Hold the Baltic provinces.', 'Manter as províncias bálticas.', refuse('EST'), 65, None)])
breakup('233', 'sov_caucasus', 'GEO',
        ('The Transcaucasian Federation', 'A Federação Transcaucasiana'),
        ('Georgians, Armenians and Azeris form a Transcaucasian commissariat and then a federation of their own, caught between Turkish armies and Russian retreat.',
         'Georgianos, armênios e azeris formam um comissariado transcaucasiano e depois uma federação própria, presos entre os exércitos turcos e a retirada russa.'),
        [('Recognise the Caucasian republics.', 'Reconhecer as repúblicas caucasianas.',
          fx('release = GEO', 'release = ARM', 'release = AZR', V(SE, -8)), 40, None),
         ('Keep the Caucasus by force.', 'Manter o Cáucaso pela força.', refuse('GEO'), 60, None)])
breakup('234', 'sov_poland', 'POL',
        ('Poland Rises Again', 'A Polônia Ressurge'),
        ('The Regency Council in Warsaw, the Allied declarations and the collapse of the partitioning empires leave no doubt: Poland will be a state again. The only question is its borders.',
         'O Conselho de Regência em Varsóvia, as declarações aliadas e o colapso dos impérios partilhadores não deixam dúvida: a Polônia será novamente um Estado. A única questão são suas fronteiras.'),
        [('Recognise the Polish state.', 'Reconhecer o Estado polonês.', fx('release = POL', V(SE, -8)), 50, None),
         ('Keep the Vistula provinces.', 'Manter as províncias do Vístula.', refuse('POL'), 50, None)])

# ============================================================ DECISOES
category('SOV_imperial_crisis', 'generic_crisis', 'original_tag = SOV',
         'original_tag = SOV\nhas_country_flag = SOV_rework_init',
         'Imperial Crisis Management', 'Gestão da Crise Imperial',
         'The Tsar and his ministers can still steer the Empire through its growing unrest. Every measure has its price.',
         'O Tsar e seus ministros ainda podem conduzir o Império em meio à agitação crescente. Cada medida tem seu preço.')
category('SOV_civil_war_front', 'generic_civil_support', 'original_tag = SOV',
         'original_tag = SOV\nhas_country_flag = SOV_civil_war_started\nNOT = { has_country_flag = SOV_civil_war_won }',
         'The Civil War Front', 'A Frente da Guerra Civil',
         'Reds and Whites fight for every railway junction and granary. Mobilisation and terror decide the war.',
         'Vermelhos e brancos lutam por cada entroncamento ferroviário e celeiro. Mobilização e terror decidem a guerra.')

C1, C2 = 'SOV_imperial_crisis', 'SOV_civil_war_front'
VIS = lambda extra='': 'original_tag = SOV\nhas_country_flag = SOV_rework_init' + ('\n' + extra if extra else '')
AI = lambda n, cond: 'modifier = { add = %d %s }' % (n, cond)
decision(C1, 'SOV_dec_convene_duma', 'generic_political_rally', 25, 150, NOT_ABD, VIS(NOT_ABD),
         fx(V(DU, -15), 'add_stability = 0.02', V(PR, -2)), AI(20, 'check_variable = { SOV_duma_tension > 60 }'),
         'Convene the Duma', 'Convocar a Duma',
         'Call the deputies back and listen to their grievances. Tension with the Duma falls.', 'Chamar os deputados de volta e ouvir suas queixas. A tensão com a Duma diminui.')
decision(C1, 'SOV_dec_prorogue_duma', 'generic_break_treaty', 20, 150, NOT_ABD, VIS(NOT_ABD),
         fx(V(DU, 15), 'add_political_power = 30', V(UN, 3)), AI(0, 'always = no'),
         'Prorogue the Duma', 'Suspender a Duma',
         'Send the deputies home. The court gains room to act, but the Duma remembers.', 'Mandar os deputados para casa. A corte ganha espaço para agir, mas a Duma se lembra.')
decision(C1, 'SOV_dec_fix_bread_prices', 'generic_fundraising', 30, 90, 'check_variable = { SOV_hunger > 20 }', VIS(),
         fx(V(HU, -10), 'add_stability = -0.01'), AI(30, 'check_variable = { SOV_hunger > 45 }'),
         'Fix Bread Prices', 'Tabelar o Preço do Pão',
         'Set maximum prices and ration flour in the big cities. The bakers grumble, but the queues shorten.', 'Fixar preços máximos e racionar a farinha nas grandes cidades. Os padeiros resmungam, mas as filas diminuem.')
decision(C1, 'SOV_dec_grain_requisition', 'generic_colonial_administration', 20, 90, 'has_war = yes', VIS('has_war = yes'),
         fx(V(HU, -7), V(UN, 5)), AI(15, 'check_variable = { SOV_hunger > 60 }'),
         'Requisition Grain', 'Requisitar Grãos',
         'Send purchasing agents and soldiers to the grain provinces. The cities eat, the villages seethe.', 'Enviar agentes e soldados às províncias de grãos. As cidades comem, as aldeias fervem.')
decision(C1, 'SOV_dec_visit_the_front', 'generic_army_support', 25, 120, fx('has_war = yes', NOT_ABD), VIS('has_war = yes'),
         fx(V(LO, 6), V(PR, 3)), AI(25, 'check_variable = { SOV_army_loyalty < 55 }'),
         'Visit the Front', 'Visitar a Frente',
         'The Tsar inspects the army and hands out medals. The men cheer, for now.', 'O Tsar inspeciona o exército e distribui medalhas. Os homens aplaudem, por enquanto.')
decision(C1, 'SOV_dec_okhrana_crackdown', 'generic_police_action', 40, 90, NOT_ABD, VIS(NOT_ABD),
         fx(V(UN, -10), 'add_stability = -0.03', V(PR, -2)), AI(20, 'check_variable = { SOV_unrest > 60 }'),
         'Okhrana Crackdown', 'Repressão da Okhrana',
         'Arrest agitators and close workers clubs. Calm returns, at a cost to the regime reputation.', 'Prender agitadores e fechar clubes operários. A calma retorna, à custa da reputação do regime.')
decision(C1, 'SOV_dec_conciliation_boards', 'generic_decision', 35, 120, 'check_variable = { SOV_unrest > 25 }', VIS(),
         fx(V(UN, -8), 'add_stability = 0.01'), AI(25, 'check_variable = { SOV_unrest > 45 }'),
         'Factory Conciliation Boards', 'Comissões de Conciliação nas Fábricas',
         'Let employers and elected workers sit together to settle disputes before they become strikes.', 'Fazer patrões e operários eleitos sentarem juntos para resolver disputas antes que virem greves.')
decision(C1, 'SOV_dec_field_courts', 'generic_disband_irregulars', 30, 90, fx('has_war = yes', NOT_ABD), VIS('has_war = yes'),
         fx(V(LO, 4), V(UN, 3)), AI(15, 'check_variable = { SOV_army_loyalty < 45 }'),
         'Field Courts-Martial', 'Cortes Marciais de Campanha',
         'Summary justice for deserters and agitators in uniform. Order is restored by fear.', 'Justiça sumária para desertores e agitadores fardados. A ordem é restaurada pelo medo.')
decision(C1, 'SOV_dec_patriotic_campaign', 'generic_brainwash', 20, 120, 'has_war = yes', VIS('has_war = yes'),
         fx('add_war_support = 0.03', V(UN, -3)), AI(20, 'has_war_support < 0.40'),
         'Patriotic Campaign', 'Campanha Patriótica',
         'Church bells, posters and war loans remind the people why they fight.', 'Sinos de igreja, cartazes e empréstimos de guerra lembram ao povo por que lutam.')
decision(C2, 'SOV_dec_mobilise_the_rear', 'generic_reorganize_irregulars', 30, 90, 'always = yes', VIS('has_country_flag = SOV_civil_war_started'),
         fx('army_experience = 10', V(UN, 4), V(HU, 4)), AI(25, 'always = yes'),
         'Mobilise the Rear', 'Mobilizar a Retaguarda',
         'Drafts, labour battalions and requisitions feed the fronts of the civil war.', 'Recrutamentos, batalhões de trabalho e requisições alimentam as frentes da guerra civil.')
decision(C2, 'SOV_dec_political_commissars', 'generic_intelligence_operation', 40, 120, 'has_government = communism', VIS('has_government = communism'),
         fx(V(LO, 8), 'add_stability = -0.01'), AI(25, 'check_variable = { SOV_army_loyalty < 55 }'),
         'Political Commissars', 'Comissários Políticos',
         'Attach a commissar to every former imperial officer to guarantee their loyalty.', 'Designar um comissário para cada ex-oficial imperial a fim de garantir sua lealdade.')
decision(C2, 'SOV_dec_amnesty_officers', 'generic_protection', 30, 150, 'always = yes', VIS('always = yes'),
         fx(V(LO, 5), V(UN, -4), 'add_political_power = -30'), AI(15, 'always = yes'),
         'Amnesty for Officers', 'Anistia aos Oficiais',
         'Pardon officers who switch sides. Experience is worth more than grudges.', 'Perdoar oficiais que mudem de lado. Experiência vale mais que rancores.')

loc('ww1_russia.20.c', 'Hold the centre: convene the Constituent Assembly.', 'Manter o centro: convocar a Assembleia Constituinte.')

# ============================================================ MOTOR (efeitos agendados)


def tier(var, hi, lo, idea_hi, idea_lo, invert=False):
    cmp = '<' if invert else '>'
    return f'''	if = {{
		limit = {{ check_variable = {{ {var} {cmp} {hi} }} }}
		if = {{ limit = {{ NOT = {{ has_idea = {idea_hi} }} }} remove_ideas = {idea_lo} add_ideas = {idea_hi} }}
	}}
	else_if = {{
		limit = {{ check_variable = {{ {var} {cmp} {lo} }} }}
		if = {{ limit = {{ NOT = {{ has_idea = {idea_lo} }} }} remove_ideas = {idea_hi} add_ideas = {idea_lo} }}
	}}
	else = {{ remove_ideas = {idea_lo} remove_ideas = {idea_hi} }}
'''


def sched(flag, cond, eid, extra=''):
    return f'''	if = {{
		limit = {{ NOT = {{ has_country_flag = {flag} }} {cond} }}
		set_country_flag = {flag}
		{extra}
		country_event = {{ id = ww1_russia.{eid} days = 2 }}
	}}
'''


TIERS = (tier('SOV_hunger', 65, 35, 'SOV_hungry_cities_2', 'SOV_hungry_cities_1')
         + tier('SOV_unrest', 70, 45, 'SOV_restless_workers_2', 'SOV_restless_workers_1')
         + tier('SOV_army_loyalty', 30, 50, 'SOV_wavering_army_2', 'SOV_wavering_army_1', invert=True))

NOT_ABD_B = 'NOT = { has_country_flag = SOV_tsar_abdicated }'
CAL = ''.join([
    sched('SOV_ev_lena', 'date > 1912.4.4', 200),
    sched('SOV_ev_army_programme', 'date > 1913.3.1', 208),
    sched('SOV_ev_stolypin_harvest', 'date > 1913.6.1', 207),
    sched('SOV_ev_putilov', 'date > 1914.7.8', 201),
    sched('SOV_ev_great_retreat', 'has_war = yes date > 1915.7.20', 203),
    sched('SOV_ev_supreme_command', 'has_war = yes date > 1915.9.5 ' + NOT_ABD_B, 202),
    sched('SOV_ev_duma', 'has_war = yes date > 1915.9.3', 204),
    sched('SOV_ev_bread_lines', 'has_war = yes date > 1916.11.20 ' + NOT_ABD_B, 209),
    sched('SOV_ev_army_wavers', 'has_war = yes check_variable = { SOV_army_loyalty < 48 }', 206),
    sched('SOV_ev_rasputin', 'has_war = yes date > 1916.12.17 NOT = { has_completed_focus = SOV_murder_of_rasputin }', 205),
    sched('SOV_ev_april', 'has_country_flag = SOV_provisional_gov_in_power date > 1917.4.3', 213),
    sched('SOV_ev_july', 'has_country_flag = SOV_provisional_gov_in_power date > 1917.7.3', 214),
    sched('SOV_ev_kornilov', 'has_country_flag = SOV_provisional_gov_in_power date > 1917.8.25 NOT = { has_completed_focus = SOV_the_kornilov_affair }', 215),
    sched('SOV_ev_church', 'has_country_flag = SOV_tsar_abdicated date > 1917.8.28', 228),
    sched('SOV_ev_finland', 'has_country_flag = SOV_tsar_abdicated date > 1917.11.15', 230),
    sched('SOV_ev_ukraine', 'has_country_flag = SOV_tsar_abdicated date > 1917.11.20', 231),
    sched('SOV_ev_baltic', 'has_country_flag = SOV_tsar_abdicated date > 1918.2.1', 232),
    sched('SOV_ev_caucasus', 'has_country_flag = SOV_tsar_abdicated date > 1918.4.1', 233),
    sched('SOV_ev_poland', 'has_country_flag = SOV_tsar_abdicated date > 1918.11.11', 234),
    sched('SOV_ev_czech', 'has_country_flag = SOV_civil_war_started date > 1918.5.14', 221),
    sched('SOV_ev_kolchak', 'has_country_flag = SOV_civil_war_started date > 1918.11.18', 222),
    sched('SOV_ev_romanovs', 'has_country_flag = SOV_tsar_abdicated has_government = communism date > 1918.7.10', 227),
    sched('SOV_ev_wrangel', 'has_country_flag = SOV_civil_war_started date > 1920.4.1', 223),
    sched('SOV_ev_kronstadt', 'has_country_flag = SOV_civil_war_started has_government = communism date > 1921.3.1', 224),
    sched('SOV_ev_nep', 'has_country_flag = SOV_civil_war_started has_government = communism date > 1921.3.16', 225),
    sched('SOV_ev_ussr', 'has_government = communism date > 1922.12.29', 226),
])

ENGINE = '''# Gerado por scripts/build_ger_rus_content.py - motor de instabilidade da Russia Imperial.
ww1_sov_rework_init = {
	set_country_flag = SOV_rework_init
	set_variable = { SOV_army_loyalty = 68 }
	set_variable = { SOV_hunger = 12 }
	set_variable = { SOV_unrest = 22 }
	set_variable = { SOV_tsar_prestige = 60 }
	set_variable = { SOV_duma_tension = 30 }
	set_variable = { SOV_separatism = 15 }
	set_variable = { SOV_repression_count = 0 }
}

ww1_sov_rework_weekly = {
	if = { limit = { NOT = { has_country_flag = SOV_rework_init } } ww1_sov_rework_init = yes }
	# ---------------- deriva semanal ----------------
	if = {
		limit = { has_war = yes any_enemy_country = { is_major = yes } }
		add_to_variable = { SOV_unrest = 0.22 }
		add_to_variable = { SOV_army_loyalty = -0.12 }
		add_to_variable = { SOV_hunger = 0.10 }
		add_to_variable = { SOV_tsar_prestige = -0.05 }
		if = { limit = { has_war_support < 0.40 } add_to_variable = { SOV_unrest = 0.15 } }
		if = { limit = { has_stability < 0.40 } add_to_variable = { SOV_unrest = 0.15 } }
		if = {
			limit = { check_variable = { ww1_infantry_equipment_ratio > 0.01 } check_variable = { ww1_infantry_equipment_ratio < 0.65 } }
			add_to_variable = { SOV_army_loyalty = -0.25 }
			add_to_variable = { SOV_unrest = 0.10 }
		}
		if = { limit = { surrender_progress > 0.15 } add_to_variable = { SOV_army_loyalty = -0.20 } }
	}
	else = {
		add_to_variable = { SOV_unrest = -0.15 }
		add_to_variable = { SOV_army_loyalty = 0.10 }
		add_to_variable = { SOV_hunger = -0.20 }
		add_to_variable = { SOV_tsar_prestige = 0.03 }
	}
	if = { limit = { check_variable = { SOV_duma_tension > 50 } } add_to_variable = { SOV_unrest = 0.05 } }
	if = { limit = { has_country_flag = SOV_tsar_abdicated has_country_flag = SOV_provisional_gov_in_power has_war = yes } add_to_variable = { SOV_separatism = 0.20 } }
	if = { limit = { has_country_flag = SOV_civil_war_started NOT = { has_country_flag = SOV_civil_war_won } } add_to_variable = { SOV_hunger = 0.15 } add_to_variable = { SOV_unrest = 0.08 } }
	clamp_variable = { var = SOV_unrest min = 0 max = 100 }
	clamp_variable = { var = SOV_army_loyalty min = 0 max = 100 }
	clamp_variable = { var = SOV_hunger min = 0 max = 100 }
	clamp_variable = { var = SOV_tsar_prestige min = 0 max = 100 }
	clamp_variable = { var = SOV_duma_tension min = 0 max = 100 }
	clamp_variable = { var = SOV_separatism min = 0 max = 100 }
	# ---------------- espiritos por nivel ----------------
''' + TIERS + '''	if = {
		limit = { check_variable = { SOV_separatism > 60 } }
		if = { limit = { NOT = { has_idea = SOV_separatist_fever } } add_ideas = SOV_separatist_fever }
	}
	else = { remove_ideas = SOV_separatist_fever }
	# ---------------- Janela da Revolucao de Fevereiro ----------------
	if = {
		limit = {
			NOT = { has_country_flag = SOV_tsar_abdicated }
			NOT = { has_country_flag = SOV_revolution_window_open }
			NOT = { has_country_flag = SOV_revolution_cooldown }
			NOT = { has_country_flag = SOV_path_tsarist }
			has_war = yes
			date > 1916.10.1
			OR = {
				check_variable = { SOV_unrest > 78 }
				AND = { check_variable = { SOV_hunger > 50 } check_variable = { SOV_army_loyalty < 42 } }
				AND = { date > 1917.2.15 check_variable = { SOV_unrest > 62 } }
				AND = { check_variable = { SOV_repression_count > 1 } check_variable = { SOV_unrest > 55 } }
			}
		}
		set_country_flag = SOV_revolution_window_open
		if = {
			limit = { check_variable = { SOV_repression_count > 0 } }
			country_event = { id = ww1_russia.211 days = 4 }
		}
		else = { country_event = { id = ww1_russia.210 days = 2 } }
	}
	# ---------------- Calendario historico ----------------
''' + CAL + '''}
'''
