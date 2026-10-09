"""UK content, wing 2 (Economy and Reconstruction): rewards, descriptions, events, ideas, decisions.

Same conventions as britain_politics_data.py. the_treasury_estimates is intentionally untouched
(it already drives the allocation debate through ww1_britain.1).
"""
from britain_politics_data import var, flag, ev, idea, remove_idea, pp, stab


def build(state, kind, slots=1):
    return (f"{state} = {{ add_extra_state_shared_building_slots = {slots} "
            f"add_building_construction = {{ type = {kind} level = 1 }} }}")


def eco_ev(n):
    return f"country_event = {{ id = ww1_britain_eco.{n} }}"


FOCI = {
# ------------------------------------------------------------------ industrial (19 + treasury estimates untouched)
"industrial_district_surveys": (
    [pp(15), var("debt_burden", -1), flag("district_surveys")],
    "Inspetores percorrem Midlands, Clyde, Tyne e Lancashire para listar oficinas, estaleiros e minas. Ganha 15 de poder político e reduz dívida em 1; as regiões industriais ficam prontas para contratos.",
    "Inspectors tour the Midlands, Clydeside, Tyneside and Lancashire to list workshops, yards and mines. It grants 15 political power and eases debt by 1; the industrial districts are ready for contracts."),
"midlands_machine_shops": (
    [build(128, "industrial_complex"), var("debt_burden", 1)],
    "As oficinas de máquinas-ferramenta de Birmingham e Coventry passam a trabalhar com contratos do Estado. Abre uma vaga de construção e enfileira um complexo industrial nas Midlands Ocidentais; a dívida sobe 1.",
    "The machine-tool shops of Birmingham and Coventry take on state contracts. It opens a construction slot and queues an industrial complex in the West Midlands; debt rises by 1."),
"clyde_shipyard_contracts": (
    [build(133, "dockyard"), var("debt_burden", 1)],
    "Os estaleiros do Clyde recebem encomendas de casco e máquinas. Abre uma vaga e enfileira um estaleiro em Strathclyde; a dívida sobe 1.",
    "The Clyde yards receive hull and engine orders. It opens a slot and queues a dockyard in Strathclyde; debt rises by 1."),
"tyne_steel_and_ordnance": (
    [build(131, "arms_factory"), var("debt_burden", 1)],
    "Armstrong e Vickers ampliam o aço e a artilharia no Tyne. Abre uma vaga e enfileira uma fábrica de armas no norte da Inglaterra; a dívida sobe 1.",
    "Armstrong and Vickers expand steel and ordnance on the Tyne. It opens a slot and queues an arms factory in Northern England; debt rises by 1."),
"lancashire_engineering": (
    [build(132, "industrial_complex"), var("labour_support", 1)],
    "As oficinas de locomotivas e teares de Lancashire convertem parte da capacidade para máquinas pesadas. Abre uma vaga e enfileira um complexo industrial no noroeste; apoio trabalhista +1.",
    "Lancashire's locomotive and loom works convert part of their capacity to heavy machinery. It opens a slot and queues an industrial complex in the North-West; labour support +1."),
"the_city_credit_market": (
    [var("debt_burden", -2), pp(15), flag("city_credit")],
    "A City de Londres financia o governo com títulos e aceita letras de câmbio de aliados. A dívida cai 2 e ganha 15 de poder político.",
    "The City of London finances the government through bonds and accepts bills from allies. Debt falls by 2 and it grants 15 political power."),
"railway_freight_coordination": (
    [idea("railway_executive"), "build_railway = { level = 2 start_state = 126 target_state = 127 build_only_on_allied = yes }", pp(10), flag("railway_executive")],
    "O Comitê Executivo das Ferrovias coordena cargas e duplica a linha Londres-Southampton. Institui o Executivo Ferroviário (consumo de suprimento -2%), ferrovia nível 2 e 10 de poder político.",
    "The Railway Executive Committee coordinates freight and expands London-Southampton link. Establishes Railway Executive (supply consumption -2%), level 2 railway and 10 political power."),
"domestic_coal_allocation": (
    [build(130, "industrial_complex"), idea("coal_allocation"), "122 = { add_building_construction = { type = infrastructure level = 1 } }", flag("coal_allocation_done")],
    "O carvão galês é a base da indústria, da frota e das exportações. Adiciona 1 nível de infraestrutura no País de Gales, complexo industrial em Yorkshire e instituição Alocação do Carvão.",
    "Welsh coal underpins industry, the fleet and exports. Adds 1 infrastructure level in Wales, industrial complex in Yorkshire and Coal Allocation institution."),
"national_munitions_contracts": (
    ["hidden_effect = { remove_ideas = ENG_ww1_coal_allocation }", build(126, "arms_factory"), build(128, "arms_factory"), idea("munitions_contracts"), var("debt_burden", 2)],
    "Contratos nacionais ampliam Woolwich e Birmingham com duas fábricas militares. Instituição Contratos de Munição (capacidade +1,5%); dívida sobe 2.",
    "National contracts expand Woolwich and Birmingham with two arms factories. Munitions Contracts institution (capacity +1.5%); debt rises by 2."),
"the_ministry_of_munitions": (
    ["hidden_effect = { remove_ideas = ENG_ww1_coal_allocation remove_ideas = ENG_ww1_munitions_contracts }", idea("munitions_ministry"), var("labour_support", -3), flag("ministry_of_munitions")],
    "Lloyd George assume a produção de guerra em maio de 1915. O Ministério estabelece o Ministério de Munições (capacidade industrial +4%, eficiência máxima +2,5%); apoio trabalhista -3.",
    "Lloyd George takes charge of war production in May 1915. Establishes Ministry of Munitions (industrial capacity +4%, maximum efficiency +2.5%); labour support -3."),
"shell_inspection_boards": (
    ["hidden_effect = { remove_ideas = ENG_ww1_munitions_contracts remove_ideas = ENG_ww1_coal_allocation }", build(130, "arms_factory"), idea("shell_inspection"), flag("shell_inspection")],
    "Inspetores reorganizam a produção de projéteis em Sheffield com fábrica militar em Yorkshire. Instituição Inspeção de Projéteis.",
    "Inspectors reorganise shell production in Sheffield with an arms factory in Yorkshire. Shell Inspection institution."),
"wartime_labour_dilution": (
    ["hidden_effect = { remove_ideas = ENG_ww1_shell_inspection remove_ideas = ENG_ww1_coal_allocation }", idea("labour_dilution"), var("labour_support", -4), flag("labour_dilution")],
    "O Acordo do Tesouro de 1915 permite mulheres e operários sem ofício em funções técnicas. Instituição Diluição da Mão de Obra; apoio trabalhista -4.",
    "The 1915 Treasury Agreement allows women and unskilled hands in technical posts. Labour Dilution institution; labour support -4."),
"the_shop_stewards_agreement": (
    ["hidden_effect = { remove_ideas = ENG_ww1_labour_dilution remove_ideas = ENG_ww1_shell_inspection }", idea("labour_compact"), var("labour_support", 6), flag("shop_stewards_agreement")],
    "Delegados de oficina ganham voz nas fábricas de guerra. Institui o Pacto Trabalhista e apoio trabalhista +6.",
    "Shop stewards gain a voice in war plants. Establishes Labour Compact and labour support +6."),
"emergency_factory_controls": (
    ["hidden_effect = { remove_ideas = ENG_ww1_labour_dilution remove_ideas = ENG_ww1_shell_inspection }", idea("emergency_controls"), var("labour_support", -6), flag("emergency_factory_controls")],
    "O Estado assume controle direto de contratações e salários fabris. Institui Controles Emergenciais; apoio trabalhista -6.",
    "The state takes direct control of hiring and plant wages. Establishes Emergency Controls; labour support -6."),
"the_ministry_of_food": (
    [var("debt_burden", 1), flag("ministry_of_food"), eco_ev(3)],
    "Em dezembro de 1916 nasce o Ministério da Alimentação. O governo precisa decidir entre racionamento obrigatório e apelo voluntário. A dívida sobe 1.",
    "The Ministry of Food is born in December 1916. The government must choose between compulsory rationing and a voluntary appeal. Debt rises by 1."),
"austerity_and_public_credit": (
    [var("debt_burden", -3), var("labour_support", -2), pp(10), flag("austerity_measures")],
    "Impostos de guerra e empréstimos forçados reduzem a pressão sobre o crédito público. A dívida cai 3, apoio trabalhista cai 2 e ganha 10 de poder político. Abre a decisão da campanha de poupança de guerra.",
    "War taxes and forced loans ease pressure on public credit. Debt falls by 3, labour support falls by 2 and it grants 10 political power. Unlocks the war savings campaign decision."),
"debt_service_commission": (
    [var("debt_burden", -4), stab(-0.01), flag("debt_service_commission")],
    "Uma comissão organiza o pagamento dos juros da dívida de guerra. A dívida cai 4, mas o corte de gastos custa 1% de estabilidade.",
    "A commission organises service of the war debt. Debt falls by 4, but the spending squeeze costs 1% stability."),
"convert_the_war_plants": (
    [pp(20), stab(0.02), var("labour_support", 3), flag("war_plants_converted")],
    "Depois do armistício, fábricas de munição voltam a produzir máquinas e locomotivas. Ganha 20 de poder político, 2% de estabilidade e apoio trabalhista +3.",
    "After the armistice, munition plants return to machines and locomotives. It grants 20 political power, 2% stability and labour support +3."),
"housing_and_civilian_employment": (
    ["hidden_effect = { remove_ideas = ENG_ww1_emergency_controls remove_ideas = ENG_ww1_labour_compact remove_ideas = ENG_ww1_labour_dilution }", build(129, "industrial_complex"), idea("housing_programme"), var("debt_burden", 3), var("labour_support", 4)],
    "A Lei Addison promove casas para veteranos com um complexo industrial nas Midlands. Institui o Programa de Habitação; dívida +3 e apoio trabalhista +4.",
    "The Addison Act builds homes for veterans with an industrial complex in the East Midlands. Establishes Housing Programme; debt rises by 3 and labour support +4."),
# ------------------------------------------------------------------ reconstruction (20)
"the_peace_administration_office": (
    [pp(15), flag("peace_administration")],
    "Um escritório civil assume a transição da guerra para a paz. Ganha 15 de poder político e abre as etapas da reconstrução.",
    "A civil office takes charge of the transition from war to peace. It grants 15 political power and opens the reconstruction steps."),
"military_demobilisation_planning": (
    [pp(10), stab(0.01), flag("demobilisation_planned")],
    "Listas por idade, ofício e tempo de serviço organizam a volta dos soldados. Ganha 10 de poder político e 1% de estabilidade.",
    "Lists by age, trade and length of service organise the soldiers' return. It grants 10 political power and 1% stability."),
"shipping_repatriation_coordination": (
    [var("debt_burden", 1), stab(0.01), flag("repatriation_shipping")],
    "Navios de transporte levam tropas de volta da França, do Oriente Médio e dos domínios. A dívida sobe 1 e a estabilidade sobe 1%.",
    "Transports carry troops home from France, the Middle East and the Dominions. Debt rises by 1 and stability rises by 1%."),
"veterans_welfare_register": (
    [pp(15), stab(0.01), idea("veterans_settlement"), var("debt_burden", 1)],
    "Um registro nacional liga cada veterano a pensão e emprego. Garante o Assentamento de Veteranos; estabilidade +1% e dívida +1.",
    "A national register links each veteran to pension and employment. Grants Veterans' Settlement; stability +1% and debt +1."),
"disability_pension_administration": (
    [var("debt_burden", 2), stab(0.02), var("labour_support", 4), pp(10)],
    "Centenas de milhares de mutilados e viúvas passam a receber pensão regular. Ganha 10 de poder político, estabilidade sobe 2% e apoio trabalhista +4; dívida sobe 2.",
    "Hundreds of thousands of disabled men and widows receive regular pensions. Grants 10 political power, stability rises by 2% and labour support +4; debt rises by 2."),
"civilian_training_for_returning_soldiers": (
    [pp(10), var("labour_support", 2), flag("soldier_retraining")],
    "Escolas técnicas e oficinas reciclam ex-soldados para empregos civis. Ganha 10 de poder político e apoio trabalhista +2.",
    "Technical schools and workshops retrain ex-soldiers for civilian jobs. It grants 10 political power and labour support +2."),
"public_housing_contracts": (
    [var("debt_burden", 2), var("labour_support", 3), stab(0.01), "128 = { add_building_construction = { type = infrastructure level = 1 } }"],
    "Prefeituras assinam contratos para construir moradias populares com subsídio do Estado, ampliando a infraestrutura das Midlands. A dívida sobe 2, apoio trabalhista +3 e 1% de estabilidade.",
    "Local authorities sign contracts to build council housing with state subsidies, expanding infrastructure in the Midlands. Debt rises by 2, labour support +3 and 1% stability."),
"industrial_conversion_planning": (
    ["hidden_effect = { remove_ideas = ENG_ww1_housing_programme remove_ideas = ENG_ww1_munitions_ministry remove_ideas = ENG_ww1_coal_allocation }", idea("industrial_conversion"), flag("industrial_conversion_planned")],
    "Planos de conversão de aço e químicos para uso civil coordenam as prioridades da paz. Instituição Conversão Industrial (bens de consumo -2%).",
    "Plans to convert steel and chemicals to civilian use organise peacetime priorities. Industrial Conversion institution (consumer goods -2%)."),
"the_employment_exchanges": (
    [var("labour_support", 3), stab(0.01), flag("employment_exchanges")],
    "Bolsas de emprego ligam desempregados e vagas em todo o país. Apoio trabalhista +3 e 1% de estabilidade.",
    "Labour exchanges match the unemployed with vacancies across the country. Labour support +3 and 1% stability."),
"restore_civilian_railway_traffic": (
    [stab(0.01), pp(15), var("debt_burden", 1), "hidden_effect = { remove_ideas = ENG_ww1_railway_executive }", flag("railways_restored")],
    "As companhias retomam o controle das linhas civis. Ganha 15 de poder político, estabilidade +1% e desmobiliza o controle estatal ferroviário; dívida +1.",
    "The companies regain control of civilian lines. Grants 15 political power, stability +1% and demobilises state railway control; debt +1."),
"public_debt_repayment": (
    [var("debt_burden", -5), var("labour_support", -2)],
    "O Tesouro usa receitas para resgatar títulos de guerra. A dívida cai 5 e apoio trabalhista cai 2 pelo custo fiscal.",
    "The Treasury uses revenue to redeem war bonds. Debt falls by 5 and labour support falls by 2 because of the fiscal squeeze."),
"treasury_expenditure_review": (
    [var("debt_burden", -3), pp(10), var("labour_support", -2)],
    "O Comitê de Economia revisa cada ministério. A dívida cai 3, ganha 10 de poder político e apoio trabalhista cai 2.",
    "The Economy Committee reviews every department. Debt falls by 3, it grants 10 political power and labour support falls by 2."),
"merchant_marine_renewal": (
    [build(133, "dockyard"), var("debt_burden", 2)],
    "A marinha mercante perdeu milhões de toneladas na guerra. Enfileira um estaleiro extra em Strathclyde (abrindo uma vaga); a dívida sobe 2.",
    "The merchant marine lost millions of tons in the war. It queues an extra dockyard in Strathclyde (opening a slot); debt rises by 2."),
"the_public_health_settlement": (
    [stab(0.02), var("debt_burden", 1), var("labour_support", 2)],
    "O Ministério da Saúde de 1919 reúne hospitais, seguros e saneamento. Estabilidade +2%, dívida +1 e apoio trabalhista +2.",
    "The 1919 Ministry of Health unites hospitals, insurance and sanitation. Stability +2%, debt +1 and labour support +2."),
"the_education_reconstruction_programme": (
    [stab(0.01), var("debt_burden", 1), flag("fisher_act")],
    "A Lei Fisher eleva a idade escolar e cria continuação educacional. Estabilidade +1% e dívida +1.",
    "The Fisher Act raises the school-leaving age and creates continuation schools. Stability +1% and debt +1."),
"local_government_finance": (
    [var("debt_burden", -1), pp(10), var("labour_support", -1)],
    "Municípios recebem uma nova fórmula de impostos locais e subsídios. A dívida cai 1, ganha 10 de poder político e apoio trabalhista cai 1.",
    "Local authorities receive a new formula of rates and grants. Debt falls by 1, it grants 10 political power and labour support falls by 1."),
"the_industrial_relations_conference": (
    [var("labour_support", 4), pp(10), flag("industrial_conference")],
    "A Conferência Industrial Nacional reúne patrões e sindicatos para evitar greves. Apoio trabalhista +4 e 10 de poder político.",
    "The National Industrial Conference brings employers and unions together to avoid strikes. Labour support +4 and 10 political power."),
"the_postwar_parliamentary_mandate": (
    [stab(0.02), pp(25), flag("postwar_mandate")],
    "Com os temas da paz resolvidos, o governo busca um mandato claro no Parlamento. Estabilidade +2% e 25 de poder político.",
    "With the questions of the peace settled, the government seeks a clear mandate in Parliament. Stability +2% and 25 political power."),
"the_nineteen_twenty_two_cabinet": (
    [flag("cabinet_1922"), eco_ev(5)],
    "A queda da coalizão em outubro de 1922 leva Bonar Law ao poder. O novo gabinete herda cortes e greves já marcados.",
    "The fall of the coalition in October 1922 brings Bonar Law to power. The new cabinet inherits cuts and strikes already in motion."),
"the_nineteen_twenty_three_settlement": (
    [pp(15), var("debt_burden", -2), flag("settlement_1923")],
    "Baldwin tenta estabilizar finanças e política com a dívida americana acertada. Ganha 15 de poder político e a dívida cai 2.",
    "Baldwin tries to stabilise finance and politics with the American debt settled. It grants 15 political power and debt falls by 2."),
}

EXCLUSIVE = []  # shop stewards vs emergency controls already exclusive in uk.txt

IDEAS = {
 "railway_executive": ("supply_consumption_factor = -.02 civilian_factory_use = 1", "Executivo ferroviário", "Railway Executive",
   "As companhias ferroviárias operam sob uma direção única.", "The railway companies run under one direction.", "ENG_ww1_railway_freight_coordination"),
 "coal_allocation": ("industrial_capacity_factory = .01 consumer_goods_factor = .005", "Alocação do carvão", "Coal Allocation",
   "A indústria tem preferência sobre o consumo doméstico.", "Industry has priority over household use.", "ENG_ww1_domestic_coal_allocation"),
 "munitions_contracts": ("industrial_capacity_factory = .015 production_factory_efficiency_gain_factor = -.05", "Contratos de munição", "Munitions Contracts",
   "Muitos fornecedores, qualidade desigual.", "Many suppliers, uneven quality.", "ENG_ww1_national_munitions_contracts"),
 "shell_inspection": ("production_factory_max_efficiency_factor = .02 industrial_capacity_factory = .01", "Inspeção de projéteis", "Shell Inspection",
   "Lotes defeituosos são rejeitados antes do embarque.", "Defective lots are rejected before shipment.", "ENG_ww1_shell_inspection_boards"),
 "labour_dilution": ("industrial_capacity_factory = .02 stability_weekly = -.0003", "Diluição da mão de obra", "Labour Dilution",
   "Mulheres e operários sem ofício ocupam postos qualificados.", "Women and unskilled hands fill skilled posts.", "ENG_ww1_wartime_labour_dilution"),
 "food_control": ("stability_factor = .02 consumer_goods_factor = .01", "Controle de alimentos", "Food Control",
   "Preços e racionamento sob o Ministério da Alimentação.", "Prices and rationing under the Ministry of Food.", "ENG_ww1_the_ministry_of_food"),
 "industrial_conversion": ("consumer_goods_factor = -.02 industrial_capacity_factory = -.015", "Conversão industrial", "Industrial Conversion",
   "A indústria de guerra volta ao uso civil.", "War industry returns to civilian use.", "ENG_ww1_industrial_conversion_planning"),
}

# option = (name_pt, name_en, effects, ai)
EVENTS = [
 dict(id=1, mode="mtth", days=20, once=True, trigger="has_war = yes date > 1915.10.1 date < 1916.3.1",
  t=("As greves de aluguel do Clyde", "The Clydeside Rent Strikes"),
  d=("Senhorios aumentam aluguéis perto das fábricas de guerra em Glasgow. Operárias e mulheres de soldados montam piquetes nas portas dos despejos, e os delegados de oficina ameaçam parar o Clyde.",
     "Landlords raise rents near the war factories of Glasgow. Working women and soldiers' wives picket evictions, and shop stewards threaten to stop the Clyde."),
  options=[
   ("Congelar os aluguéis por lei. (apoio trabalhista +5, dívida +1, estabilidade +1%)", "Freeze rents by law. (labour support +5, debt +1, stability +1%)",
    [var("labour_support", 5), var("debt_burden", 1), "add_stability = 0.01", flag("rent_restriction")], 60),
   ("Quebrar a greve e prender os líderes. (apoio trabalhista -6, estabilidade -2%, +10 de poder político)", "Break the strike and jail the leaders. (labour support -6, stability -2%, +10 political power)",
    [var("labour_support", -6), "add_stability = -0.02", "add_political_power = 10", flag("clyde_strike_broken")], 40)]),
 dict(id=3, mode="trigger", trigger="has_country_flag = ENG_ww1_ministry_of_food",
  t=("O racionamento de alimentos", "Food Rationing"),
  d=("Os submarinos cortam importações de trigo e açúcar, e as filas crescem. O Ministério da Alimentação pode impor racionamento obrigatório ou pedir contenção voluntária.",
     "U-boats cut wheat and sugar imports, and the queues grow. The Ministry of Food can impose compulsory rationing or ask for voluntary restraint."),
  options=[
   ("Impor racionamento obrigatório. (instituição Controle de Alimentos, estabilidade +1%)", "Impose compulsory rationing. (Food Control institution, stability +1%)",
    ["add_ideas = ENG_ww1_food_control", "add_stability = 0.01"], 60),
   ("Pedir contenção voluntária. (estabilidade -1%, +10 de poder político, instituição Controle de Alimentos)", "Appeal for voluntary restraint. (stability -1%, +10 political power, Food Control institution)",
    ["add_ideas = ENG_ww1_food_control", "add_stability = -0.01", "add_political_power = 10"], 40)]),
 dict(id=5, mode="trigger", trigger="has_country_flag = ENG_ww1_cabinet_1922",
  t=("O Machado de Geddes", "The Geddes Axe"),
  d=("O Comitê Geddes propõe cortes profundos em gastos militares, educação e habitação. Os economistas pedem equilíbrio; os sindicatos e os veteranos prometem resistir.",
     "The Geddes Committee proposes deep cuts in military, education and housing spending. Economists call for balance; unions and veterans promise resistance."),
  options=[
   ("Aceitar todos os cortes. (dívida -6, apoio trabalhista -5, +15 de poder político, estabilidade -1%)", "Accept every cut. (debt -6, labour support -5, +15 political power, stability -1%)",
    [var("debt_burden", -6), var("labour_support", -5), "add_political_power = 15", "add_stability = -0.01", flag("geddes_axe_full")], 40),
   ("Aceitar só metade. (dívida -3, apoio trabalhista -2)", "Accept half. (debt -3, labour support -2)",
    [var("debt_burden", -3), var("labour_support", -2), flag("geddes_axe_half")], 40),
   ("Recusar os cortes. (apoio trabalhista +3, -10 de poder político)", "Refuse the cuts. (labour support +3, -10 political power)",
    [var("labour_support", 3), "add_political_power = -10"], 20)]),
 dict(id=6, mode="mtth", days=15, once=True, trigger="has_war = no date > 1921.3.1 date < 1921.8.1",
  t=("A Sexta-feira Negra dos mineiros", "Black Friday for the Miners"),
  d=("Com o fim do controle estatal das minas, os donos cortam salários. A Aliança Tríplice de mineiros, ferroviários e transportadores ameaça greve geral, e os aliados do governo hesitam.",
     "With state control of the mines ended, owners cut wages. The Triple Alliance of miners, railwaymen and transport workers threatens a general strike, and the government's allies hesitate."),
  options=[
   ("Apoiar os donos das minas. (apoio trabalhista -8, estabilidade -2%, dívida -1)", "Back the mine owners. (labour support -8, stability -2%, debt -1)",
    [var("labour_support", -8), "add_stability = -0.02", var("debt_burden", -1), flag("miners_lockout")], 55),
   ("Subsidiar os salários por alguns meses. (dívida +4, apoio trabalhista +4)", "Subsidise wages for some months. (debt +4, labour support +4)",
    [var("debt_burden", 4), var("labour_support", 4), flag("miners_subsidy")], 45)]),
]

# Ally-side event: ROOT = ally in the British faction, FROM = ENG.
ALLY_EVENT = dict(id=10,
  t=("Carvão britânico para os aliados", "British Coal for the Allies"),
  d=("Londres oferece navios de carvão para manter fábricas, ferrovias e esquadras aliadas em funcionamento. O preço é crédito e tonelagem que a marinha mercante britânica também poderia usar.",
     "London offers shiploads of coal to keep allied factories, railways and fleets running. The price is credit and tonnage that the British merchant marine could also use."),
  a=("Aceitar o carvão. (estabilidade +2%; a dívida britânica sobe 1)", "Accept the coal. (stability +2%; British debt rises by 1)"),
  b=("Recusar a oferta.", "Decline the offer."))

DECISION_DEFS = {
 "ENG_ww1_coal_to_allies": dict(
   pt=("Enviar carvão aos aliados", "Gasta 15 de poder político. Em guerra, oferece carvão a cada aliado da facção britânica; quem aceita ganha 1 de estabilidade e a dívida britânica sobe 1 por aceite. Exige a alocação do carvão."),
   en=("Ship Coal to the Allies", "Spend 15 political power. At war, offer coal to each member of the British faction; each one that accepts gains 2% stability and British debt rises by 1 per acceptance. Requires the coal allocation.")),
 "ENG_ww1_war_savings_drive": dict(
   pt=("Campanha de poupança de guerra", "Gasta 20 de poder político. A dívida cai 2 e o apoio trabalhista cai 1 pelo sacrifício. Exige medidas de austeridade."),
   en=("War Savings Campaign", "Spend 20 political power. Debt falls by 2 and labour support falls by 1 from the sacrifice asked. Requires the austerity measures.")),
}

# Decision text fix: ally stability is +2% in the event.
DECISION_DEFS["ENG_ww1_coal_to_allies"]["pt"] = (DECISION_DEFS["ENG_ww1_coal_to_allies"]["pt"][0],
  "Gasta 15 de poder político. Em guerra, oferece carvão a cada aliado da facção britânica; quem aceita ganha 2% de estabilidade e a dívida britânica sobe 1 por aceite. Exige a alocação do carvão.")
