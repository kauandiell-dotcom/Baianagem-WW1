"""UK content, wing 1: events, decisions and institutions (data only).

Event ids are ww1_britain_pol.N. Picture is a shared placeholder until the art pass.
"""
from britain_politics_data import var, flag

PICTURE = "GFX_event_ww1_british_entry_debate"

TAGS = {"CAN": ("canada", "o Canadá", "Canada"), "AST": ("australia", "a Austrália", "Australia"),
        "NZL": ("new_zealand", "a Nova Zelândia", "New Zealand"), "SAF": ("south_africa", "a África do Sul", "South Africa")}

# ---------------------------------------------------------------- institutions (ideas)
# name -> (modifier text, name_pt, name_en, desc_pt, desc_en, picture)
IDEAS = {
 "national_insurance": ("stability_factor = .02 consumer_goods_factor = .01", "Seguro Nacional", "National Insurance",
   "Saúde e desemprego cobertos por contribuições de patrões, operários e Estado.", "Sickness and unemployment covered by employer, worker and state contributions.", "ENG_ww1_labour_compact"),
 "defence_of_the_realm": ("war_support_factor = .05 stability_factor = -.02 political_power_factor = -.03", "Defesa do Reino", "Defence of the Realm",
   "Poderes de emergência sobre imprensa, ofício e deslocamentos.", "Emergency powers over the press, trades and movement.", "ENG_ww1_emergency_controls"),
 "reserved_occupations": ("industrial_capacity_factory = .02 conscription = -.0015", "Ofícios reservados", "Reserved Occupations",
   "Mineiros, operários de munição e ferroviários ficam fora do alistamento.", "Miners, munition workers and railwaymen are kept out of enlistment.", "ENG_ww1_munitions_ministry"),
 "enlarged_franchise": ("stability_factor = .02 political_power_factor = -.02", "Eleitorado ampliado", "Enlarged Electorate",
   "Milhões de novos eleitores, homens e mulheres, exigem mais do Parlamento.", "Millions of new voters, men and women, demand more of Parliament.", "ENG_ww1_cabinet_consultation"),
 "dominion_procurement": ("industrial_capacity_factory = .015 consumer_goods_factor = .005", "Compras nos domínios", "Dominion Procurement",
   "Escritórios de compras ligam a indústria de Londres às matérias-primas dos domínios.", "Procurement offices link London's industry to the Dominions' raw materials.", "ENG_ww1_army_service_corps"),
 "imperial_sealift": ("convoy_escort_efficiency = .03 civilian_factory_use = 1", "Transporte imperial", "Imperial Sealift",
   "Navios mercantes e escoltas ligam a metrópole, os domínios e a Índia.", "Merchant ships and escorts link the metropole, the Dominions and India.", "ENG_ww1_convoy_service"),
 "commonwealth_consultation": ("political_power_factor = .03 consumer_goods_factor = .005", "Consulta imperial", "Commonwealth Consultation",
   "O império passa a ser uma comunidade de nações com voz própria.", "The empire becomes a community of nations with a voice of its own.", "ENG_ww1_war_cabinet"),
}

# ---------------------------------------------------------------- decisions
# Generated in the builder: contingent requests (4), reconvene conference, two Irish measures.

# ---------------------------------------------------------------- events
# option = (name_pt, name_en, effect, ai_base)
EVENTS = [
 dict(id=1, mode="trigger",
  t=("O Terceiro Projeto de Autonomia", "The Third Home Rule Bill"),
  d=("Em abril de 1912 Asquith apresenta o Projeto de Governo da Irlanda. O Partido Irlandês, de cujos votos depende a maioria liberal, exige o texto sem exclusões. Os unionistas do Ulster, liderados por Carson, prometem resistir, e os Lordes podem atrasá-lo por dois anos. A forma do projeto decide quanto problema virá depois.",
     "In April 1912 Asquith introduces the Government of Ireland Bill. The Irish Party, whose votes sustain the Liberal majority, demands it without exclusions. The Ulster Unionists under Carson promise resistance, and the Lords can delay it for two years. How the Bill is framed decides how much trouble follows."),
  options=[
   ("Apresentar o projeto sem exclusões. (tensão irlandesa -8, tensão no Ulster +15)", "Press the Bill without exclusions. (Irish tension -8, Ulster tension +15)",
    [var("irish_tension", -8), var("ulster_tension", 15), flag("home_rule_unamended"), "country_event = { id = ww1_britain_pol.7 days = 120 }"], 35),
   ("Apresentar com uma emenda que permite exclusão por condado. (tensão irlandesa +3, Ulster +4)", "Introduce it with an amendment allowing county opt-outs. (Irish tension +3, Ulster +4)",
    [var("irish_tension", 3), var("ulster_tension", 4), flag("home_rule_amended")], 40),
   ("Adiar o projeto até a questão dos Lordes esfriar. (tensão irlandesa +8, Ulster -5, +10 de poder político)", "Shelve the Bill until the Lords question cools. (Irish tension +8, Ulster -5, +10 political power)",
    [var("irish_tension", 8), var("ulster_tension", -5), "add_political_power = 10", flag("home_rule_deferred")], 25)]),
 dict(id=2, mode="trigger", trigger="has_country_flag = ENG_ww1_home_rule_bill_introduced",
  t=("A Conferência do Palácio de Buckingham", "The Buckingham Palace Conference"),
  d=("O rei convoca liberais, conservadores, nacionalistas e unionistas ao palácio para evitar a guerra civil. O ponto de atrito é geográfico: quais condados do Ulster ficam de fora da autonomia e por quanto tempo.",
     "The King summons Liberals, Conservatives, nationalists and unionists to the Palace to avert civil war. The sticking point is geographic: which Ulster counties stand outside Home Rule and for how long."),
  options=[
   ("Aceitar a exclusão temporária dos condados do Ulster. (tensão no Ulster -20, tensão irlandesa +10)", "Accept temporary exclusion of the Ulster counties. (Ulster tension -20, Irish tension +10)",
    [var("ulster_tension", -20), var("irish_tension", 10), flag("ulster_exclusion_accepted")], 55),
   ("Recusar qualquer exclusão. (tensão no Ulster +10, tensão irlandesa -5)", "Refuse any exclusion. (Ulster tension +10, Irish tension -5)",
    [var("ulster_tension", 10), var("irish_tension", -5), flag("home_rule_unamended")], 45)]),
 dict(id=3, mode="trigger",
  t=("A crise dos projéteis e a coalizão", "The Shell Crisis and the Coalition"),
  d=("A falta de projéteis na frente ocidental e a demissão do almirante Fisher deixam o gabinete liberal exposto. Os conservadores de Bonar Law pedem lugar no governo, e o líder trabalhista Henderson aceita entrar.",
     "The shell shortage on the Western Front and Admiral Fisher's resignation leave the Liberal cabinet exposed. Bonar Law's Conservatives ask for seats, and Labour's Henderson agrees to join."),
  options=[
   ("Formar um governo de coalizão. (+25 de poder político, estabilidade +2%, apoio trabalhista +3)", "Form a coalition government. (+25 political power, stability +2%, labour support +3)",
    ["add_political_power = 25", "add_stability = 0.02", var("labour_support", 3), flag("coalition_government")], 70),
   ("Continuar com um gabinete só liberal. (+10 de poder político, estabilidade -2%)", "Carry on with a Liberal-only cabinet. (+10 political power, stability -2%)",
    ["add_political_power = 10", "add_stability = -0.02", flag("liberal_only_government")], 30)]),
 dict(id=4, mode="trigger",
  t=("A crise de dezembro de 1916", "The December Crisis of 1916"),
  d=("Lloyd George exige um pequeno gabinete de guerra, sem Asquith na presidência dos trabalhos. A alternativa é reorganizar os comitês existentes, sem romper com o primeiro-ministro.",
     "Lloyd George demands a small War Cabinet without Asquith chairing its business. The alternative is reorganising existing committees without breaking with the prime minister."),
  options=[
   ("Criar o Gabinete de Guerra. (instituição Gabinete de Guerra, +20 de poder político, apoio trabalhista -2)", "Create the War Cabinet. (War Cabinet institution, +20 political power, labour support -2)",
    ["add_ideas = ENG_ww1_war_cabinet", "add_political_power = 20", var("labour_support", -2), flag("lloyd_george_premiership"), flag("liberal_split")], 75),
   ("Reorganizar os comitês existentes. (+10 de poder político, estabilidade +2%)", "Reorganise the existing committees. (+10 political power, stability +2%)",
    ["add_political_power = 10", "add_stability = 0.02", flag("asquith_retained")], 25)]),
 dict(id=5, mode="trigger",
  t=("A eleição do 'cupom'", "The Coupon Election"),
  d=("Com o armistício assinado, Lloyd George quer um mandato para a paz. O 'cupom' é uma carta de apoio do governo aos candidatos da coalizão; quem fica sem ele enfrenta o eleitorado sozinho.",
     "With the armistice signed, Lloyd George wants a mandate for the peace. The 'coupon' is a letter of support for coalition candidates; those without it face the electorate alone."),
  options=[
   ("Emitir o cupom aos candidatos da coalizão. (+25 de poder político, estabilidade +2%, apoio trabalhista -6)", "Issue the coupon to coalition candidates. (+25 political power, stability +2%, labour support -6)",
    ["add_political_power = 25", "add_stability = 0.02", var("labour_support", -6), flag("coupon_election")], 55),
   ("Disputar como partidos separados. (+5 de poder político, estabilidade -1%, apoio trabalhista +3)", "Fight as separate parties. (+5 political power, stability -1%, labour support +3)",
    ["add_political_power = 5", "add_stability = -0.01", var("labour_support", 3), flag("separate_parties_election")], 30),
   ("Adiar as eleições para um mandato de reconstrução. (-20 de poder político, estabilidade -3%)", "Delay the election for a reconstruction mandate. (-20 political power, stability -3%)",
    ["add_political_power = -20", "add_stability = -0.03", flag("election_delayed")], 15)]),
 dict(id=6, mode="trigger",
  t=("A Conferência Imperial de 1911", "The Imperial Conference of 1911"),
  d=("Os primeiros-ministros dos domínios discutem com Asquith e Grey a defesa comum. O Almirantado quer uma contribuição em dinheiro; os domínios preferem marinhas próprias, sob comando local em tempo de paz.",
     "The Dominion premiers discuss common defence with Asquith and Grey. The Admiralty wants a cash contribution; the Dominions prefer navies of their own under local control in peacetime."),
  options=[
   ("Insistir em uma contribuição comum para a Marinha Real. (consentimento -2, dívida -1)", "Press for a common contribution to the Royal Navy. (consent -2, debt -1)",
    [var("dominion_consent", -2), var("debt_burden", -1)], 30),
   ("Aceitar marinhas locais sob coordenação do Almirantado. (consentimento +4, dívida +1)", "Accept local navies coordinated by the Admiralty. (consent +4, debt +1)",
    [var("dominion_consent", 4), var("debt_burden", 1)], 70)]),
 dict(id=7, mode="trigger", trigger="has_country_flag = ENG_ww1_home_rule_unamended",
  t=("Os Voluntários do Ulster e o exército", "The Ulster Volunteers and the Army"),
  d=("Oficiais do exército em Curragh avisam que prefeririam ser demitidos a marchar contra o Ulster. Os Voluntários do Ulster já têm armas vindas da Alemanha. O governo precisa escolher entre disciplina e apaziguamento.",
     "Army officers at the Curragh warn that they would rather be dismissed than march against Ulster. The Ulster Volunteers already hold rifles landed from Germany. The government must choose between discipline and appeasement."),
  options=[
   ("Exigir disciplina do exército. (-25 de poder político, estabilidade -2%, tensão no Ulster -10)", "Demand army discipline. (-25 political power, stability -2%, Ulster tension -10)",
    ["add_political_power = -25", "add_stability = -0.02", var("ulster_tension", -10), var("irish_tension", -3)], 40),
   ("Aceitar as garantias dos oficiais e não coagir o Ulster. (tensão no Ulster -15, tensão irlandesa +10)", "Accept the officers' assurances and do not coerce Ulster. (Ulster tension -15, Irish tension +10)",
    [var("ulster_tension", -15), var("irish_tension", 10), "add_political_power = -5", flag("ulster_assured")], 60)]),
 dict(id=8, mode="trigger",
  t=("O Gabinete Imperial de Guerra", "The Imperial War Cabinet"),
  d=("Em 1917 os primeiros-ministros dos domínios chegam a Londres. Lloyd George precisa decidir se eles se sentam no gabinete como pares ou apenas são ouvidos.",
     "In 1917 the Dominion premiers arrive in London. Lloyd George must decide whether they sit in the cabinet as equals or are merely heard."),
  options=[
   ("Dar assento pleno aos primeiros-ministros. (consentimento +8, -10 de poder político)", "Give the premiers full seats. (consent +8, -10 political power)",
    [var("dominion_consent", 8), "add_political_power = -10", flag("imperial_war_cabinet_full")], 55),
   ("Consultá-los sem dar assento. (consentimento +2, +10 de poder político)", "Consult them without seats. (consent +2, +10 political power)",
    [var("dominion_consent", 2), "add_political_power = 10"], 45)]),
 dict(id=9, mode="trigger",
  t=("A Convenção Irlandesa", "The Irish Convention"),
  d=("Nacionalistas, unionistas do sul e o governo discutem um acordo para a ilha inteira. Carson exige a partilha; Redmond já não fala por todos os nacionalistas. Depois de 1916 e de 1918, o Sinn Féin pesa mais que o Partido Irlandês.",
     "Nationalists, southern unionists and the government seek a settlement for the whole island. Carson demands partition; Redmond no longer speaks for all nationalists. After 1916 and 1918 Sinn Féin outweighs the Irish Party."),
  options=[
   ("Negociar um acordo de autonomia para toda a ilha. (tensão irlandesa -15, tensão no Ulster +12)", "Negotiate self-government for the whole island. (Irish tension -15, Ulster tension +12)",
    [var("irish_tension", -15), var("ulster_tension", 12), flag("home_rule_devolved"), flag("irish_dominion_track")], 35),
   ("Partilhar: um parlamento no sul e outro no norte. (tensão irlandesa +5, Ulster -10)", "Partition: one parliament in the south and one in the north. (Irish tension +5, Ulster -10)",
    [var("irish_tension", 5), var("ulster_tension", -10), flag("irish_partition_act")], 45),
   ("Impor lei marcial. (tensão irlandesa +10, instituição Repressão Irlandesa)", "Impose martial law. (Irish tension +10, Irish Repression institution)",
    [var("irish_tension", 10), "add_ideas = ENG_ww1_irish_repression", flag("irish_coercion")], 20)]),
 dict(id=10, mode="trigger",
  t=("O Tratado Anglo-Irlandês", "The Anglo-Irish Treaty"),
  d=("Depois de dois anos de guerra, Lloyd George, Churchill e Collins negociam em Londres. A oferta é um Estado Livre da Irlanda com status de domínio; seis condados do nordeste permanecem no Reino Unido.",
     "After two years of fighting, Lloyd George, Churchill and Collins negotiate in London. The offer is an Irish Free State with Dominion status; six north-eastern counties remain in the United Kingdom."),
  options=[
   ("Assinar o Tratado: Estado Livre como domínio. (tensão irlandesa cai para 20, consentimento +5)", "Sign the Treaty: a Free State as a Dominion. (Irish tension falls to 20, consent +5)",
    ["if = { limit = { NOT = { country_exists = IRE } } release_autonomy = { target = IRE autonomy_state = autonomy_dominion freedom_level = 0.5 } }",
     "119 = { if = { limit = { is_owned_by = IRE } transfer_state_to = ENG } }",
     "set_variable = { ww1_britain_irish_tension = 20 }", var("dominion_consent", 5), flag("irish_free_state")], 65),
   ("Recusar e continuar a guerra. (tensão irlandesa +15, -20 de poder político)", "Refuse and continue the war. (Irish tension +15, -20 political power)",
    [var("irish_tension", 15), "add_political_power = -20", flag("irish_war_continues")], 35)]),
 dict(id=11, mode="mtth", days=15, once=True,
  trigger="has_war = yes date > 1916.4.23 date < 1916.8.1 113 = { is_owned_by = ENG }",
  t=("A Revolta da Páscoa", "The Easter Rising"),
  d=("Na segunda-feira de Páscoa, voluntários irlandeses e o Exército dos Cidadãos tomam pontos de Dublin e proclamam uma república. A revolta é esmagada em seis dias, mas a resposta do governo vai decidir o que a Irlanda lembra dela.",
     "On Easter Monday, Irish Volunteers and the Citizen Army seize points in Dublin and proclaim a republic. The revolt is crushed within a week, but the government's response will decide how Ireland remembers it."),
  options=[
   ("Lei marcial e conselhos de guerra. (tensão irlandesa +20, poder político +10)", "Martial law and courts-martial. (Irish tension +20, +10 political power)",
    [var("irish_tension", 20), "add_political_power = 10", flag("easter_rising_suppressed")], 60),
   ("Clemência e inquérito civil. (tensão irlandesa +8, -20 de poder político)", "Clemency and a civil inquiry. (Irish tension +8, -20 political power)",
    [var("irish_tension", 8), "add_political_power = -20", flag("easter_rising_inquiry")], 40)]),
 dict(id=12, mode="mtth", days=10, once=True,
  trigger="has_war = yes has_country_flag = ENG_ww1_military_service_authorised date > 1918.3.20 date < 1918.7.1",
  t=("A crise do recrutamento na Irlanda", "The Irish Conscription Crisis"),
  d=("A ofensiva alemã de março de 1918 esgota as reservas. O gabinete discute estender o serviço militar à Irlanda. Nacionalistas, a Igreja e os sindicatos prometem resistir, e a greve geral já está marcada.",
     "The German offensive of March 1918 drains the reserves. The cabinet debates extending conscription to Ireland. Nationalists, the Church and the unions promise resistance, and a general strike is already called."),
  options=[
   ("Estender a lei de serviço militar à Irlanda. (tensão irlandesa +25, fim da isenção irlandesa)", "Extend the Military Service Act to Ireland. (Irish tension +25, Irish exemption ends)",
    [var("irish_tension", 25), flag("irish_conscription_authorised")], 30),
   ("Aprovar o poder de aplicar a lei, sem usá-lo por ora. (tensão irlandesa +8, -10 de poder político)", "Pass the enabling power but hold it in reserve. (Irish tension +8, -10 political power)",
    [var("irish_tension", 8), "add_political_power = -10"], 40),
   ("Retirar a proposta. (tensão irlandesa -5, -15 de poder político)", "Withdraw the proposal. (Irish tension -5, -15 political power)",
    [var("irish_tension", -5), "add_political_power = -15"], 30)]),
]

# Dominion-side event (ROOT = dominion, FROM = ENG). Transfers manpower, creates none.
DOMINION_EVENT = dict(id=20,
  t=("Um pedido de Londres", "A Request from London"),
  d=("Londres pede voluntários para a frente europeia. O gabinete do domínio pesa a lealdade ao império contra as necessidades da lavoura, da fábrica e das famílias.",
     "London asks for volunteers for the European front. The Dominion cabinet weighs loyalty to the empire against the needs of farm, factory and family."),
  a=("Enviar voluntários. (15.000 de mão de obra passam ao Reino Unido; o consentimento britânico sobe +2)", "Send volunteers. (15,000 manpower pass to the United Kingdom; British consent rises +2)"),
  b=("Manter os homens em casa. (consentimento do Reino Unido -3, estabilidade +1%)", "Keep the men at home. (British consent -3, stability +1%)"))


# Weekly administration fires ww1_britain.3 when Irish tension passes 69. It lives in this
# file (not in ww1_britain_policy_events.txt) so another writer cannot drop it.
IRISH_CRISIS = dict(id="ww1_britain.3",
  t=("Agita??o na Irlanda", "Unrest in Ireland"),
  d=("Pris?es, boatos de recrutamento e a autonomia irlandesa parada levaram a tens?o al?m da administra??o comum. O Castelo de Dublin pergunta se o gabinete vai negociar, reprimir ou esperar. Conciliar custa capital pol?tico; reprimir derruba a tens?o por pouco tempo e deixa ressentimento duradouro; esperar mant?m o problema aberto.",
     "Arrests, conscription rumours and the stalled Home Rule settlement have pushed Irish tension past ordinary administration. Dublin Castle asks whether the cabinet will negotiate, suppress the agitation or wait. Conciliation costs political capital; repression lowers tension briefly and leaves lasting resentment; delay keeps the problem open."),
  options=[
   ("Abrir conversas com os representantes irlandeses. (-30 de poder pol?tico, tens?o cai para 45, institui??o de concilia??o)", "Open talks with the Irish representatives. (-30 political power, tension falls to 45, conciliation institution)",
    ["add_political_power = -30", "set_variable = { ww1_britain_irish_tension = 45 }", "remove_ideas = ENG_ww1_irish_repression",
     "if = { limit = { NOT = { has_idea = ENG_ww1_irish_conciliation } } add_ideas = ENG_ww1_irish_conciliation }"], 40),
   ("Usar os poderes de emerg?ncia. (tens?o 55, institui??o de repress?o, estabilidade -2%)", "Use the emergency powers. (tension 55, repression institution, stability -2%)",
    ["set_variable = { ww1_britain_irish_tension = 55 }", "remove_ideas = ENG_ww1_irish_conciliation",
     "if = { limit = { NOT = { has_idea = ENG_ww1_irish_repression } } add_ideas = ENG_ww1_irish_repression }", "add_stability = -0.02"], 30),
   ("Esperar por uma esta??o mais calma. (tens?o +4, +10 de poder pol?tico)", "Wait for a calmer season. (tension +4, +10 political power)",
    [var("irish_tension", 4), "add_political_power = 10"], 30)])

# Overrides for broken keys in the older policy localisation (space inside the variable name).
LOC_FIXES = {
  "ENG_ww1_cabinet_policy_desc": (
    "As dota??es de defesa reservam a administra??o civil e desviam a produ??o entre as armas. Carga da d?vida: [?ww1_britain_debt_burden|0]. Reverter uma pol?tica neutra exige novas consultas; os aliados podem recusar a admiss?o.",
    "Defence allocations reserve civilian administration and divert production between services. Debt burden: [?ww1_britain_debt_burden|0]. Reversing a neutral policy requires new consultations; allies may refuse admission."),
}
