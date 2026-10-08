"""UK content, wing 1 (Politics, Empire and Ireland): focus rewards + descriptions.

Each entry: focus id (without ENG_ww1_) -> (reward, desc_pt, desc_en).
Variables (all 0-100, clamped weekly in ww1_britain_weekly_administration):
  ww1_britain_debt_burden, ww1_britain_irish_tension, ww1_britain_labour_support,
  ww1_britain_ulster_tension (new), ww1_britain_dominion_consent (new).
Rewards stay small and traded-off: no free divisions or equipment, few permanent modifiers.
"""


def var(name, amount):
    return f"add_to_variable = {{ ww1_britain_{name} = {amount} }}"


def flag(name):
    return f"set_country_flag = ENG_ww1_{name}"


def ev(number, days=0):
    extra = f" days = {days}" if days else ""
    return f"country_event = {{ id = ww1_britain_pol.{number}{extra} }}"


def idea(name):
    return f"add_ideas = ENG_ww1_{name}"


def remove_idea(name):
    return f"remove_ideas = ENG_ww1_{name}"


def pp(n):
    return f"add_political_power = {n}"


def stab(x):
    return f"add_stability = {x}"


def navy_xp(n):
    return f"navy_experience = {n}"


def autonomy(tag, ratio):
    # Concession (positive) raises the dominion's freedom score; it costs extraction, buys consent.
    return (f"if = {{ limit = {{ country_exists = {tag} }} {tag} = {{ add_autonomy_ratio = "
            f"{{ value = {ratio} localization = ENG_ww1_autonomy_consultation }} }} }}")


FOCI = {
# ------------------------------------------------------------------ constitutional (20)
"parliament_act": (
    [pp(25), stab(0.01), var("irish_tension", -2), flag("parliament_act_passed")],
    "A Lei do Parlamento de 1911 tira dos Lordes o poder de barrar leis financeiras e limita o veto às demais leis a dois anos. Ganha 25 de poder político, 1% de estabilidade, a tensão irlandesa cai 2 pontos e o caminho da autonomia irlandesa se abre.",
    "The Parliament Act of 1911 strips the Lords of their power over money bills and limits their veto on other bills to a two-year delay. The cabinet gains 25 political power, 1% stability, Irish tension falls by 2 and the road to Irish self-government opens."),
"national_insurance": (
    ["remove_ideas = ENG_city_of_london_credit", idea("national_insurance"), var("labour_support", 5), var("debt_burden", 1)],
    "O Seguro Nacional de Lloyd George cobre saúde e desemprego de milhões de trabalhadores. Substitui o crédito da City pela instituição Seguro Nacional (estabilidade +2%, bens de consumo +1%), apoio trabalhista +5 e dívida +1.",
    "Lloyd George's National Insurance covers sickness and unemployment for millions of workers. Replaces City credit with the National Insurance institution (stability +2%, consumer goods +1%), labour support +5 and debt +1."),
"the_liberal_cabinet": (
    [pp(15), flag("liberal_government")],
    "O gabinete liberal de Asquith depende dos votos irlandeses e trabalhistas para governar. Ganha 15 de poder político; as próximas reformas dependem dessa maioria apertada.",
    "Asquith's Liberal cabinet governs on Irish and Labour votes. It gains 15 political power; the reforms that follow depend on that narrow majority."),
"the_lords_and_the_commons": (
    [pp(10), stab(0.01), flag("lords_curbed")],
    "Depois do orçamento de 1909 e das duas eleições de 1910, a convenção constitucional assenta: os Comuns mandam. Ganha 10 de poder político e 1% de estabilidade.",
    "After the 1909 budget and the two elections of 1910 the constitutional convention settles: the Commons rule. It grants 10 political power and 1% stability."),
"irish_parliamentary_support": (
    [pp(15), var("irish_tension", -5), flag("irish_party_support"), flag("home_rule_promised")],
    "O Partido Parlamentar Irlandês de Redmond sustenta a maioria liberal em troca de uma promessa: autonomia para a Irlanda. Ganha 15 de poder político e a tensão irlandesa cai 5, mas a promessa precisa ser cumprida no projeto de lei.",
    "Redmond's Irish Parliamentary Party props up the Liberal majority in exchange for a promise: self-government for Ireland. It grants 15 political power and Irish tension falls by 5, but the promise must be delivered in the Bill."),
"home_rule_bill": (
    [flag("home_rule_bill_introduced"), ev(1)],
    "Em abril de 1912 Asquith apresenta o Terceiro Projeto de Autonomia. Os Lordes só podem atrasá-lo por dois anos, mas os unionistas do Ulster ameaçam resistir pelas armas. A forma do projeto decide quanto problema virá depois.",
    "In April 1912 Asquith introduces the Third Home Rule Bill. The Lords can only delay it for two years, but the Ulster Unionists threaten armed resistance. How the Bill is framed decides how much trouble follows."),
"ulster_conference": (
    [ev(2)],
    "Com o Ulster armado e o exército incerto, o rei convoca líderes de todos os lados para uma conferência. O resultado define se o Ulster será excluído da autonomia.",
    "With Ulster armed and the army uncertain, the King calls leaders from every side to a conference. The outcome decides whether Ulster will be excluded from Home Rule."),
"electoral_registration": (
    [pp(10), var("labour_support", 2)],
    "A reforma do registro eleitoral acaba com o voto plural e simplifica a inscrição. Ganha 10 de poder político e apoio trabalhista +2.",
    "Electoral registration reform ends plural voting and simplifies enrolment. It grants 10 political power and labour support +2."),
"the_defence_of_the_realm": (
    [remove_idea("national_insurance"), idea("defence_of_the_realm"), flag("dora_enacted")],
    "A Lei de Defesa do Reino de agosto de 1914 dá poderes de emergência sobre imprensa e ofícios. Substitui o seguro social pela instituição Defesa do Reino (apoio à guerra +5%, estabilidade -2%, poder político -3%).",
    "The Defence of the Realm Act of August 1914 gives emergency powers over press and trades. Replaces social insurance with Defence of the Realm institution (war support +5%, stability -2%, political power -3%)."),
"wartime_parliamentary_scrutiny": (
    [remove_idea("national_insurance"), idea("cabinet_consultation"), stab(0.02), var("labour_support", 2)],
    "Mesmo em guerra, o Parlamento mantém o direito de interpelar ministros. Substitui o seguro pela instituição Consulta ao Gabinete (poder político -2,5%), estabilidade +2% e apoio trabalhista +2.",
    "Even at war Parliament keeps the right to question ministers. Replaces insurance with Cabinet Consultation institution (political power -2.5%), stability +2% and labour support +2."),
"the_coalition_cabinet": (
    [ev(3)],
    "A crise dos projéteis e a demissão de Fisher derrubam o gabinete liberal em maio de 1915. O governo precisa decidir se divide o poder com conservadores e trabalhistas.",
    "The shell crisis and Fisher's resignation bring down the Liberal cabinet in May 1915. The government must decide whether to share power with Conservatives and Labour."),
"the_military_service_act": (
    [flag("military_service_authorised"), "remove_ideas = ENG_professional_bef", var("labour_support", -6), var("irish_tension", 4)],
    "A Lei do Serviço Militar de janeiro de 1916 encerra o voluntariado em toda a Grã-Bretanha e remove a antiga força profissional estrita. Autoriza leis de recrutamento geral, com apoio trabalhista -6 e tensão irlandesa +4.",
    "The Military Service Act of January 1916 ends voluntary enlistment across Britain and retires the old professional service idea. Authorises conscription laws, labour support falls by 6 and Irish tension rises by 4."),
"reserved_civilian_occupations": (
    [remove_idea("defence_of_the_realm"), idea("reserved_occupations")],
    "Mineiros, operários de munição e ferroviários ficam fora do alistamento militar. Substitui restrições gerais pela instituição Ofícios Reservados (capacidade industrial +2%, recrutamento -0,15%).",
    "Miners, munition workers and railwaymen are exempted from military enlistment. Replaces general restrictions with Reserved Occupations institution (industrial capacity +2%, recruitment -0.15%)."),
"the_war_cabinet": (
    [ev(4)],
    "Em dezembro de 1916 a crise de liderança opõe Asquith a Lloyd George. O país escolhe entre um pequeno gabinete de guerra e a reorganização de comitês.",
    "In December 1916 a leadership crisis pits Asquith against Lloyd George. The country chooses between a small War Cabinet and a reorganisation of committees."),
"the_franchise_debate": (
    [pp(10), var("labour_support", 3), flag("franchise_debated")],
    "A Conferência do Presidente da Câmara reúne todos os partidos para discutir o voto. Ganha 10 de poder político e apoio trabalhista +3.",
    "The Speaker's Conference brings every party together to discuss the vote. It grants 10 political power and labour support +3."),
"representation_of_the_people": (
    [remove_idea("defence_of_the_realm"), remove_idea("reserved_occupations"), idea("enlarged_franchise"), var("labour_support", 8), flag("franchise_extended")],
    "A Lei da Representação do Povo de 1918 dá voto a todos os homens e mulheres acima de 30 anos. Substitui leis de emergência pela instituição Eleitorado Ampliado (estabilidade +2%, poder político -2%) e apoio trabalhista +8.",
    "The Representation of the People Act of 1918 enfranchises all men and women over 30. Replaces emergency laws with Enlarged Electorate institution (stability +2%, political power -2%) and labour support +8."),
"the_coalition_election": (
    [ev(5)],
    "A eleição de dezembro de 1918 põe à prova a coalizão de guerra: lançar o aval do governo aos candidatos ou disputar como partidos separados.",
    "The December 1918 election tests the wartime coalition: issue the government's coupon to its candidates or fight as separate parties."),
"liberal_reconstruction": (
    [remove_idea("defence_of_the_realm"), remove_idea("reserved_occupations"), pp(25), stab(0.03), var("debt_burden", 3), flag("liberal_reconstruction_programme")],
    "Habitação, saúde e educação: o programa de reconstrução de 1919 encerra restrições de guerra. Ganha 25 de poder político e 3% de estabilidade, mas a dívida sobe 3.",
    "Housing, health and education: the 1919 reconstruction programme retires wartime restrictions. Grants 25 political power and 3% stability, but debt rises by 3."),
"the_labour_alternative": (
    [remove_idea("defence_of_the_realm"), remove_idea("reserved_occupations"), idea("labour_compact"), var("labour_support", 10), stab(-0.02), pp(15), flag("labour_mandate")],
    "Sem maioria conservadora, o Partido Trabalhista assume como alternativa governamental. Substitui medidas de guerra pelo Pacto Trabalhista, apoio trabalhista +10, 15 de poder político e estabilidade -2%.",
    "Without a Conservative majority, Labour assumes office as an alternative government. Replaces war measures with the Labour Compact, labour support +10, 15 political power and stability -2%."),
"the_conservative_settlement": (
    [remove_idea("defence_of_the_realm"), remove_idea("reserved_occupations"), pp(25), stab(0.02), var("labour_support", -8), var("debt_burden", -4), flag("conservative_settlement")],
    "O fim da coalizão e a volta dos conservadores encerram restrições de guerra com disciplina fiscal. Ganha 25 de poder político e 2% de estabilidade; apoio trabalhista cai 8 e a dívida cai 4.",
    "The end of the coalition and the return of the Conservatives ends war restrictions with fiscal retrenchment. Grants 25 political power and 2% stability; labour support falls by 8 and debt falls by 4."),
# ------------------------------------------------------------------ imperial (20)
"the_imperial_conference": (
    [pp(10), var("dominion_consent", 8), flag("imperial_conference_held"), ev(6)],
    "A Conferência Imperial de 1911 reúne os primeiros-ministros dos domínios em Londres. Ganha 10 de poder político, consentimento dos domínios +8 e abre o debate sobre quem paga a defesa naval.",
    "The 1911 Imperial Conference brings the Dominion premiers to London. It grants 10 political power, dominion consent +8 and opens the debate over who pays for naval defence."),
"canadian_defence_consultation": (
    [var("dominion_consent", 3), autonomy("CAN", 0.02), flag("consulted_canada")],
    "Borden chega ao poder em 1911 contra o pagamento de couraçados para Londres. Consultar o Canadá rende consentimento +3 e dá um pouco mais de liberdade ao domínio.",
    "Borden takes office in 1911 against paying for battleships for London. Consulting Canada earns consent +3 and gives the Dominion a little more freedom."),
"australian_defence_consultation": (
    [var("dominion_consent", 3), autonomy("AST", 0.02), flag("consulted_australia")],
    "A Austrália já tem a sua própria esquadra. Consultá-la rende consentimento +3 e um pouco mais de liberdade ao domínio.",
    "Australia already has its own fleet. Consulting it earns consent +3 and gives the Dominion a little more freedom."),
"new_zealand_naval_consultation": (
    [var("dominion_consent", 3), autonomy("NZL", 0.02), flag("consulted_new_zealand")],
    "A Nova Zelândia pagou um couraçado para a Marinha Real em 1909. Consultá-la rende consentimento +3 e um pouco mais de liberdade.",
    "New Zealand paid for a battlecruiser for the Royal Navy in 1909. Consulting it earns consent +3 and a little more freedom."),
"south_african_cooperation": (
    [var("dominion_consent", 3), autonomy("SAF", 0.02), flag("consulted_south_africa")],
    "A União Sul-Africana reconcilia bôeres e britânicos, mas a lealdade é frágil. A cooperação rende consentimento +3 e um pouco mais de liberdade.",
    "The Union of South Africa reconciles Boer and Briton, but loyalty is fragile. Cooperation earns consent +3 and a little more freedom."),
"indian_army_liaison": (
    [var("dominion_consent", 2), flag("consulted_india")],
    "O Exército Indiano é a reserva imperial. A ligação com o Estado-Maior rende consentimento +2 e permite pedir tropas indianas depois.",
    "The Indian Army is the imperial reserve. Liaison with the General Staff earns consent +2 and allows a later call for Indian troops."),
"colonial_medical_services": (
    [stab(0.01), var("dominion_consent", 2)],
    "Médicos coloniais e hospitais de campanha compartilham experiência contra febres e feridas. Ganha 1% de estabilidade e consentimento +2.",
    "Colonial medical services share experience against fever and wounds. It grants 1% stability and consent +2."),
"dominion_procurement_offices": (
    ["remove_ideas = ENG_the_imperial_web", idea("dominion_procurement"), var("dominion_consent", 2)],
    "Escritórios de compras ligam Londres a matérias-primas ultramarinas. Substitui teia imperial por Compras nos Domínios (capacidade industrial +1,5%); consentimento +2.",
    "Procurement offices link London to overseas raw materials. Replaces imperial web with Dominion Procurement (industrial capacity +1.5%); consent +2."),
"the_mediterranean_stations": (
    [navy_xp(5), flag("mediterranean_stations")],
    "Malta, Gibraltar, Chipre e Suez sustentam a frota do Mediterrâneo. Ganha 5 de experiência naval.",
    "Malta, Gibraltar, Cyprus and Suez sustain the Mediterranean fleet. It grants 5 naval experience."),
"singapore_maritime_coordination": (
    [navy_xp(4), var("dominion_consent", 1)],
    "Singapura e Hong Kong coordenam a defesa marítima do Extremo Oriente com Austrália e Nova Zelândia. Ganha 4 de experiência naval e consentimento +1.",
    "Singapore and Hong Kong coordinate the maritime defence of the Far East with Australia and New Zealand. It grants 4 naval experience and consent +1."),
"imperial_troop_transport": (
    [remove_idea("dominion_procurement"), idea("imperial_sealift")],
    "Comboios de tropas trazem soldados dos domínios à Europa. Substitui escritórios de compras pelo Transporte Imperial (escolta de comboios +3%).",
    "Troop convoys bring Dominion soldiers to Europe. Replaces procurement offices with Imperial Sealift (convoy escort +3%)."),
"the_imperial_war_conference": (
    [var("dominion_consent", 6), flag("imperial_war_conference_held"), ev(8)],
    "Em 1917 Londres convoca os domínios para decidir a direção da guerra. Consentimento +6; o formato da participação é decidido em evento.",
    "In 1917 London summons the Dominions to decide the direction of the war. Consent +6; the format of their participation is decided in an event."),
"dominion_war_cabinet_delegates": (
    [pp(15), var("dominion_consent", 4), flag("dominion_delegates")],
    "Delegados dos domínios passam a sentar nas reuniões do gabinete imperial. Ganha 15 de poder político e consentimento +4.",
    "Dominion delegates now sit in the imperial cabinet meetings. It grants 15 political power and consent +4."),
"indian_constitutional_consultation": (
    [var("dominion_consent", 3), "if = { limit = { country_exists = RAJ } RAJ = { add_stability = 0.05 } }", flag("montagu_declaration")],
    "A Declaração Montagu de 1917 promete autogoverno responsável à Índia. Consentimento +3 e a Índia ganha 5% de estabilidade.",
    "The 1917 Montagu Declaration promises responsible government to India. Consent +3 and India gains 5% stability."),
"colonial_labour_contracts": (
    ["add_manpower = 12000", var("dominion_consent", -1)],
    "Trabalhadores da Índia, China e Caribe cavam trincheiras e descarregam navios. Ganha 12.000 de mão de obra, mas o consentimento cai 1 pela forma dos contratos.",
    "Workers from India, China and the Caribbean dig trenches and unload ships. It grants 12,000 manpower, but consent falls by 1 because of the contract terms."),
"a_commonwealth_consultation_charter": (
    ["remove_ideas = ENG_the_imperial_web", remove_idea("imperial_sealift"), remove_idea("dominion_procurement"), idea("commonwealth_consultation"), var("dominion_consent", 5), flag("commonwealth_charter")],
    "A Carta de Consulta transforma o império em uma comunidade de nações, encerrando restrições coloniais. Instituição Carta de Consulta (ganho de PP +3%); consentimento +5.",
    "The Consultation Charter turns empire into a commonwealth of nations, ending colonial restrictions. Consultation Charter institution (PP gain +3%); consent +5."),
"the_irish_settlement_conference": (
    [ev(9)],
    "A Convenção Irlandesa reúne nacionalistas, unionistas e o governo. O resultado define o rumo da Irlanda: autonomia, partilha ou repressão.",
    "The Irish Convention brings nationalists, unionists and the government together. The outcome sets Ireland's course: self-government, partition or repression."),
"dominion_status_for_ireland": (
    [ev(10)],
    "Depois da guerra de independência, o governo precisa escolher entre assinar o tratado do Estado Livre Irlandês ou seguir a repressão.",
    "After the war of independence the government must choose between signing the Irish Free State treaty or pursuing repression."),
"egyptian_political_negotiations": (
    [pp(15), "if = { limit = { country_exists = EGY } EGY = { add_stability = 0.03 } }", flag("egypt_negotiated")],
    "A revolução de 1919 e a Missão Milner forçam Londres a negociar com os nacionalistas egípcios. Ganha 15 de poder político e o Egito ganha 3% de estabilidade.",
    "The 1919 revolution and the Milner Mission force London to negotiate with Egyptian nationalists. It grants 15 political power and Egypt gains 3% stability."),
"imperial_defence_after_the_war": (
    [navy_xp(5), pp(15), var("dominion_consent", 3), flag("imperial_defence_review")],
    "O Comitê de Defesa Imperial revisa a estratégia depois da guerra, com Chanak e o Pacífico no horizonte. Ganha 5 de experiência naval, 15 de poder político e consentimento +3.",
    "The Committee of Imperial Defence reviews strategy after the war, with Chanak and the Pacific in view. It grants 5 naval experience, 15 political power and consent +3."),
}

# Extra mutual exclusions required by the new design (both directions are written).
EXCLUSIVE = [("the_labour_alternative", "the_conservative_settlement")]
