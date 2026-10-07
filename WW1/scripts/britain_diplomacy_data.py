"""UK content, wing 3 (Diplomacy and Intelligence): rewards, descriptions, events, ideas, decisions.

Left untouched on purpose (already implemented through ww1_britain.5/.6/.7): continental_commitment,
armed_neutrality, reconsider_the_continental_policy (reward only; its icon is added in the art pass).
Partner events (dip.10-15) run in the partner's scope: ROOT = partner, FROM = ENG.
"""
from britain_politics_data import var, flag, idea, pp, stab, navy_xp

NS = "ww1_britain_dip"


def dip_ev(n):
    return f"country_event = {{ id = {NS}.{n} }}"


def to(tag, n):
    return f"if = {{ limit = {{ country_exists = {tag} }} {tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}"


def army_xp(n):
    return f"army_experience = {n}"


def tech(name, category, bonus=0.25):
    # One use, no free technology: a modest research-speed bonus on one category.
    return f"add_tech_bonus = {{ name = ENG_ww1_{name} bonus = {bonus} uses = 1 category = {category} }}"


FOCI = {
# ------------------------------------------------------------------ diplomatic (17 rewarded)
"edward_grey_and_the_entente": (
    [pp(15), flag("grey_entente")],
    "Sir Edward Grey conduz a política externa pela Entente Cordiale sem assinar uma aliança formal. Ganha 15 de poder político; os acordos com a França e a Rússia ficam sob a sua direção.",
    "Sir Edward Grey conducts foreign policy through the Entente Cordiale without signing a formal alliance. It grants 15 political power; the understandings with France and Russia stay under his direction."),
"the_french_naval_understanding": (
    [navy_xp(4), to("FRA", 14), flag("french_naval_understanding")],
    "Em 1912 a Marinha Real concentra-se no Mar do Norte e a francesa no Mediterrâneo. Ganha 4 de experiência naval e propõe o entendimento à França, que pode aceitar ou recusar.",
    "In 1912 the Royal Navy concentrates in the North Sea and the French fleet in the Mediterranean. It grants 4 naval experience and proposes the understanding to France, which may accept or decline."),
"french_staff_conversations": (
    [army_xp(5), flag("staff_conversations")],
    "Oficiais britânicos e franceses estudam, em sigilo, como um corpo expedicionário poderia chegar à França. Ganha 5 de experiência de exército; nenhum compromisso formal é assumido.",
    "British and French officers quietly study how an expeditionary force could reach France. It grants 5 army experience; no formal commitment is made."),
"belgian_treaty_obligations": (
    [pp(10), stab(0.01), flag("belgian_obligations"),
     "if = { limit = { country_exists = BEL has_country_flag = ENG_ww1_continental_commitment_selected } give_guarantee = BEL }"],
    "O Tratado de 1839 garante a neutralidade belga. Ganha 10 de poder político e 1% de estabilidade; se a política continental está ativa, a garantia à Bélgica é renovada.",
    "The 1839 Treaty guarantees Belgian neutrality. It grants 10 political power and 1% stability; if the continental policy is active, the guarantee to Belgium is renewed."),
"channel_expeditionary_coordination": (
    [army_xp(5), flag("channel_coordination")],
    "Portos, ferrovias e transportes são preparados para enviar a Força Expedicionária Britânica à França. Ganha 5 de experiência de exército.",
    "Ports, railways and transports are prepared to send the British Expeditionary Force to France. It grants 5 army experience."),
"russian_procurement_liaison": (
    ["if = { limit = { country_exists = RUS } RUS = { country_event = { id = ww1_britain_dip.13 } } }",
     "else_if = { limit = { country_exists = SOV } SOV = { country_event = { id = ww1_britain_dip.13 } } }",
     var("debt_burden", 1), flag("russian_liaison")],
    "Londres oferece crédito e armas à Rússia, que paga em grãos e matérias-primas. A dívida sobe 1; a Rússia decide se aceita.",
    "London offers credit and arms to Russia, which pays in grain and raw materials. Debt rises by 1; Russia decides whether to accept."),
"neutral_shipping_assurances": (
    [var("debt_burden", -1), pp(5), flag("neutral_shipping")],
    "A Declaração de Londres e garantias aos navios neutros reduzem atritos com os Estados Unidos e com países do Norte. A dívida cai 1 e ganha 5 de poder político.",
    "The Declaration of London and assurances to neutral ships reduce friction with the United States and the Northern countries. Debt falls by 1 and it grants 5 political power."),
"american_credit_negotiations": (
    [to("USA", 10), flag("credit_requested")],
    "Os bancos de Nova York financiam compras britânicas de munição e alimentos. Londres faz o pedido; os Estados Unidos decidem se concedem o crédito.",
    "New York banks finance British purchases of munitions and food. London makes the request; the United States decides whether to grant the credit."),
"italian_coalition_talks": (
    [to("ITA", 11), flag("italy_talks")],
    "Londres oferece à Itália Trentino, Trieste e a Dalmácia em troca de entrar na guerra. A Itália decide se ouve os termos; a resposta fica registrada.",
    "London offers Italy the Trentino, Trieste and Dalmatia in exchange for entering the war. Italy decides whether to hear the terms; the answer is recorded."),
"the_portuguese_connection": (
    [to("POR", 12), flag("portugal_talks")],
    "A aliança de 1373 é a mais antiga da Europa. Londres pede acesso a portos e colônias; Lisboa decide se renova as obrigações.",
    "The 1373 alliance is the oldest in Europe. London asks for access to ports and colonies; Lisbon decides whether to renew its obligations."),
"balkan_allied_coordination": (
    [to("SER", 15), to("GRE", 15), to("ROM", 15), flag("balkan_coordination")],
    "Sérvia, Grécia e Romênia recebem oferta de coordenação de suprimentos e de transporte. Cada um decide.",
    "Serbia, Greece and Romania receive an offer of coordinated supply and transport. Each decides."),
"coalition_shipping_priorities": (
    [var("debt_burden", -1), navy_xp(3), flag("shipping_pool")],
    "Um conselho aliado decide quais cargas têm prioridade: tropas, munição, trigo ou carvão. A dívida cai 1 e ganha 3 de experiência naval.",
    "An allied council decides which cargoes come first: troops, munitions, wheat or coal. Debt falls by 1 and it grants 3 naval experience."),
"the_supreme_war_council": (
    [dip_ev(2)],
    "Depois de Caporetto, aliados criam em Versalhes um Conselho Supremo de Guerra. A questão é se o comando passa a ser unificado.",
    "After Caporetto, the Allies create a Supreme War Council at Versailles. The question is whether command becomes unified."),
"armistice_consultations": (
    [dip_ev(3)],
    "Os aliados discutem as condições do armistício. Londres decide se defende termos moderados ou duros para os derrotados.",
    "The Allies discuss the terms of the armistice. London decides whether to press for moderate or hard terms on the defeated."),
"reconstruction_credit_negotiations": (
    ["if = { limit = { has_country_flag = ENG_ww1_american_credit } add_to_variable = { ww1_britain_debt_burden = -3 } }",
     "if = { limit = { NOT = { has_country_flag = ENG_ww1_american_credit } } add_to_variable = { ww1_britain_debt_burden = 2 } }",
     pp(10), flag("reconstruction_credit")],
    "Reestruturar a dívida de guerra depende de quem emprestou. Com crédito americano concedido, a dívida cai 3; sem ele, sobe 2. Ganha 10 de poder político.",
    "Restructuring the war debt depends on who lent. With American credit granted, debt falls by 3; without it, it rises by 2. It grants 10 political power."),
"the_naval_disarmament_conference": (
    [dip_ev(4)],
    "Washington, 1921: os Estados Unidos propõem limites à construção de couraçados. Londres decide se aceita a paridade naval.",
    "Washington, 1921: the United States proposes limits on battleship construction. London decides whether to accept naval parity."),
"a_european_security_settlement": (
    [pp(20), stab(0.01), flag("european_settlement")],
    "Locarno e a Liga das Nações buscam garantir a fronteira ocidental. Ganha 20 de poder político e 1% de estabilidade.",
    "Locarno and the League of Nations seek to guarantee the western frontier. It grants 20 political power and 1% stability."),
# ------------------------------------------------------------------ research (20)
"the_national_physical_laboratory": (
    [tech("the_national_physical_laboratory", "industry"), flag("npl")],
    "O laboratório de Teddington padroniza medidas, ligas e instrumentos. Um bônus de pesquisa de 25% (uso único) em tecnologia industrial.",
    "The Teddington laboratory standardises measures, alloys and instruments. A one-use research bonus of 25% on industrial technology."),
"university_military_contracts": (
    [pp(10), tech("university_military_contracts", "electronics")],
    "Cambridge, Manchester e Imperial College assinam contratos de pesquisa com o governo. Ganha 10 de poder político e bônus de pesquisa de 25% em eletrônica (uso único).",
    "Cambridge, Manchester and Imperial College sign research contracts with the government. It grants 10 political power and a one-use 25% research bonus on electronics."),
"ordnance_metallurgy_research": (
    [tech("ordnance_metallurgy_research", "artillery")],
    "Woolwich e as siderúrgicas estudam ligas para canos e projéteis. Bônus de pesquisa de 25% em artilharia (uso único).",
    "Woolwich and the steelworks study alloys for barrels and shells. A one-use 25% research bonus on artillery."),
"machine_tool_standards": (
    [tech("machine_tool_standards", "engineers_tech")],
    "Padrões de ferramentas e calibres permitem trocar peças entre fábricas. Bônus de pesquisa de 25% em engenharia (uso único).",
    "Tool and gauge standards let parts be swapped between factories. A one-use 25% research bonus on engineering."),
"railway_engineering_standards": (
    [tech("railway_engineering_standards", "logistics_tech"), "build_railway = { level = 2 start_state = 128 target_state = 132 build_only_on_allied = yes }"],
    "Bitolas, pontes e locomotivas seguem padrões comuns, duplicando o tronco ferroviário entre Birmingham e Manchester. Bônus de 25% em logística e ferrovia nível 2 construída.",
    "Gauges, bridges and locomotives follow common standards, expanding the railway trunk between Birmingham and Manchester. A 25% research bonus on logistics and level 2 railway built."),
"naval_architecture_research": (
    [tech("naval_architecture_research", "dd_tech")],
    "O tanque de provas de Haslar testa cascos e hélices. Bônus de pesquisa de 25% em contratorpedeiros (uso único).",
    "The Haslar test tank tests hulls and propellers. A one-use 25% research bonus on destroyers."),
"explosive_safety_research": (
    [stab(0.01), tech("explosive_safety_research", "infantry_weapons")],
    "Normas de armazenagem e fabricação diminuem explosões em fábricas de cordite. Estabilidade +1% e bônus de pesquisa de 25% em armas de infantaria (uso único).",
    "Storage and manufacturing rules reduce explosions in cordite factories. Stability +1% and a one-use 25% research bonus on infantry weapons."),
"field_wireless_research": (
    [tech("field_wireless_research", "signal_company_tech")],
    "Rádios portáteis e válvulas de campanha para o Corpo de Sinais. Bônus de pesquisa de 25% em sinais (uso único).",
    "Portable sets and field valves for the Signal Service. A one-use 25% research bonus on signals."),
"signals_intelligence_organisation": (
    [pp(10), flag("sigint_organisation")],
    "Admiralty e War Office reúnem interceptações de rádio e cabo em um só escritório. Ganha 10 de poder político e abre o escritório da Sala 40.",
    "The Admiralty and War Office pool wireless and cable intercepts in one office. It grants 10 political power and opens the Room 40 office."),
"the_room_forty_office": (
    [idea("room_forty"), flag("room_forty")],
    "A Sala 40 lê códigos navais alemães e, em 1917, o telegrama Zimmermann. Instituição Sala 40: velocidade de decifração +10%.",
    "Room 40 reads German naval codes and, in 1917, the Zimmermann telegram. Room 40 institution: decryption speed +10%."),
"aerial_photography_research": (
    [tech("aerial_photography_research", "recon_tech")],
    "Câmeras em aviões mapeiam trincheiras e baterias. Bônus de pesquisa de 25% em reconhecimento (uso único).",
    "Aircraft cameras map trenches and batteries. A one-use 25% research bonus on reconnaissance."),
"artillery_survey_mathematics": (
    [army_xp(5), flag("artillery_survey")],
    "Matemáticos e topógrafos calculam alcance, vento e desgaste de canos. Ganha 5 de experiência de exército.",
    "Mathematicians and surveyors calculate range, wind and barrel wear. It grants 5 army experience."),
"chemical_protection_research": (
    [tech("chemical_protection_research", "hospital_tech")],
    "Depois do primeiro gás, cientistas criam respiradores e tratamentos. Bônus de pesquisa de 25% em serviços médicos (uso único).",
    "After the first gas attack, scientists devise respirators and treatments. A one-use 25% research bonus on medical services."),
"the_landships_technical_committee": (
    [army_xp(5), var("debt_burden", 1), flag("landships_committee")],
    "O Comitê dos Navios Terrestres de 1915 financia os primeiros tanques. Ganha 5 de experiência de exército; a dívida sobe 1. Nenhum tanque é entregue por este foco.",
    "The Landships Committee of 1915 funds the first tanks. It grants 5 army experience; debt rises by 1. No tank is delivered by this focus."),
"aircraft_engine_research": (
    [tech("aircraft_engine_research", "air_equipment")],
    "Rolls-Royce e Royal Aircraft Factory testam motores mais confiáveis. Bônus de pesquisa de 25% em equipamento aéreo (uso único).",
    "Rolls-Royce and the Royal Aircraft Factory test more reliable engines. A one-use 25% research bonus on air equipment."),
"hydrophone_analysis_laboratory": (
    [tech("hydrophone_analysis_laboratory", "torpedo")],
    "O laboratório de Hawkcraig analisa ruídos de submarinos em hidrofones. Bônus de pesquisa de 25% em torpedos e armas submarinas (uso único).",
    "The Hawkcraig laboratory analyses submarine noises on hydrophones. A one-use 25% research bonus on torpedoes and underwater weapons."),
"production_quality_standards": (
    [stab(0.01), pp(10), flag("quality_standards")],
    "Padrões de qualidade reduzem refugo e acidentes nas fábricas de guerra. Ganha 10 de poder político e 1% de estabilidade.",
    "Quality standards reduce scrap and accidents in war factories. It grants 10 political power and 1% stability."),
"the_postwar_research_council": (
    [pp(15), var("debt_burden", 1), flag("research_council")],
    "O Conselho de Pesquisa Científica e Industrial sobrevive à desmobilização. Ganha 15 de poder político; a dívida sobe 1.",
    "The Department of Scientific and Industrial Research survives demobilisation. It grants 15 political power; debt rises by 1."),
"industrial_patent_exchanges": (
    [pp(10), var("debt_burden", -1), flag("patent_exchanges")],
    "Patentes alemãs confiscadas são licenciadas a empresas britânicas. Ganha 10 de poder político e a dívida cai 1.",
    "Confiscated German patents are licensed to British firms. It grants 10 political power and debt falls by 1."),
"technical_education_for_reconstruction": (
    [stab(0.01), pp(10), flag("technical_education")],
    "Escolas técnicas e noturnas qualificam operários para a paz. Ganha 10 de poder político e 1% de estabilidade.",
    "Technical and evening schools qualify workers for peacetime. It grants 10 political power and 1% stability."),
}

EXCLUSIVE = []

IDEAS = {
 "room_forty": ("decryption_factor = .1", "Sala 40", "Room 40",
   "Criptoanalistas do Almirantado leem os códigos navais alemães.", "Admiralty cryptanalysts read German naval codes.", ""),
}

# option = (name_pt, name_en, effects, ai). Partner events: trigger_full replaces the ENG default.
EVENTS = [
 dict(id=2, mode="trigger",
  t=("O Conselho Supremo de Guerra", "The Supreme War Council"),
  d=("Depois de Caporetto, britânicos, franceses e italianos criam um conselho em Versalhes. Os generais discutem se um comando aliado único é melhor que seis estados-maiores nacionais.",
     "After Caporetto, British, French and Italians create a council at Versailles. Generals debate whether one Allied command is better than six national staffs."),
  options=[
   ("Aceitar um comando aliado unificado. (-10 de poder político, apoio à guerra +2%)", "Accept a unified Allied command. (-10 political power, war support +2%)",
    ["add_political_power = -10", "add_war_support = 0.02", flag("unified_command")], 60),
   ("Manter o comando britânico independente. (+10 de poder político)", "Keep the British command independent. (+10 political power)",
    ["add_political_power = 10", flag("national_command")], 40)]),
 dict(id=3, mode="trigger",
  t=("As condições do armistício", "The Terms of the Armistice"),
  d=("Foch e os governos discutem o que exigir da Alemanha. Lloyd George teme um bloqueio prolongado e um colapso social; a opinião pública exige punição.",
     "Foch and the governments discuss what to demand of Germany. Lloyd George fears a prolonged blockade and social collapse; public opinion demands punishment."),
  options=[
   ("Defender termos moderados. (+10 de poder político, estabilidade +1%)", "Press for moderate terms. (+10 political power, stability +1%)",
    ["add_political_power = 10", "add_stability = 0.01", flag("moderate_armistice")], 50),
   ("Defender termos duros. (+15 de poder político, estabilidade -1%)", "Press for hard terms. (+15 political power, stability -1%)",
    ["add_political_power = 15", "add_stability = -0.01", flag("strict_armistice")], 50)]),
 dict(id=4, mode="trigger",
  t=("A Conferência Naval de Washington", "The Washington Naval Conference"),
  d=("Os Estados Unidos propõem uma proporção de 5:5:3 para os maiores couraçados. O Almirantado resiste, mas o Tesouro não consegue sustentar uma corrida naval.",
     "The United States proposes a 5:5:3 ratio for capital ships. The Admiralty resists, but the Treasury cannot sustain a naval race."),
  options=[
   ("Aceitar a paridade naval. (dívida -3, -10 de poder político)", "Accept naval parity. (debt -3, -10 political power)",
    [var("debt_burden", -3), "add_political_power = -10", flag("naval_parity")], 60),
   ("Recusar os limites. (dívida +2, +10 de poder político)", "Refuse the limits. (debt +2, +10 political power)",
    [var("debt_burden", 2), "add_political_power = 10", flag("naval_race")], 40)]),
 dict(id=10, mode="trigger", trigger_full="tag = USA",
  t=("Um pedido britânico de crédito", "A British Request for Credit"),
  d=("O embaixador britânico pede que os bancos americanos financiem compras de munição, trigo e algodão. Wall Street está disposta; o governo, dividido entre neutralidade e interesse comercial.",
     "The British ambassador asks American banks to finance purchases of munitions, wheat and cotton. Wall Street is willing; the government is split between neutrality and commercial interest."),
  options=[
   ("Conceder o crédito. (+20 de poder político; a dívida britânica cai 5)", "Grant the credit. (+20 political power; British debt falls by 5)",
    ["add_political_power = 20", "FROM = { add_to_variable = { ww1_britain_debt_burden = -5 } set_country_flag = ENG_ww1_american_credit }"], 65),
   ("Recusar. (a dívida britânica sobe 2, estabilidade britânica -1%)", "Decline. (British debt rises by 2, British stability -1%)",
    ["FROM = { add_to_variable = { ww1_britain_debt_burden = 2 } add_stability = -0.01 }"], 35)]),
 dict(id=11, mode="trigger", trigger_full="tag = ITA",
  t=("As ofertas de Londres", "London's Offer"),
  d=("Sonnino e Salandra recebem os termos de Londres: Trentino, Alto Ádige, Trieste, Ístria e parte da Dalmácia, em troca de entrar na guerra ao lado da Entente. Viena faz uma oferta rival, menor.",
     "Sonnino and Salandra receive London's terms: the Trentino, South Tyrol, Trieste, Istria and part of Dalmatia in exchange for joining the Entente. Vienna makes a rival, smaller offer."),
  options=[
   ("Ouvir os termos de Londres. (a Itália registra a proposta)", "Hear London's terms. (Italy records the proposal)",
    ["set_country_flag = ITA_ww1_london_terms_open", "FROM = { set_country_flag = ENG_ww1_italy_terms_open }"], 50),
   ("Manter a Tríplice Aliança por ora. (a Itália registra a recusa)", "Keep the Triple Alliance for now. (Italy records the refusal)",
    ["set_country_flag = ITA_ww1_london_terms_refused", "FROM = { set_country_flag = ENG_ww1_italy_terms_refused }"], 50)]),
 dict(id=12, mode="trigger", trigger_full="tag = POR",
  t=("A aliança mais antiga", "The Oldest Alliance"),
  d=("Londres invoca o Tratado de Windsor de 1386 e pede acesso aos portos e às colônias portuguesas. Lisboa teme a Alemanha nas colônias africanas e busca garantias de proteção.",
     "London invokes the Treaty of Windsor of 1386 and asks for access to Portuguese ports and colonies. Lisbon fears Germany in its African colonies and seeks guarantees of protection."),
  options=[
   ("Renovar as obrigações da aliança. (estabilidade +2%; a dívida britânica sobe 1)", "Renew the alliance obligations. (stability +2%; British debt rises by 1)",
    ["add_stability = 0.02", "FROM = { add_to_variable = { ww1_britain_debt_burden = 1 } set_country_flag = ENG_ww1_portugal_renewed }"], 60),
   ("Permanecer neutro. (sem efeitos)", "Remain neutral. (no effects)", ["set_country_flag = POR_ww1_declined_london"], 40)]),
 dict(id=13, mode="trigger", trigger_full="OR = { tag = RUS tag = SOV }",
  t=("Crédito britânico em munição", "British Munitions Credit"),
  d=("Londres oferece armas e crédito ao exército russo, que paga em trigo, linho e madeira. A entrega depende de portos no Báltico e no Ártico.",
     "London offers arms and credit to the Russian army, which pays in wheat, flax and timber. Delivery depends on ports on the Baltic and the Arctic."),
  options=[
   ("Aceitar o crédito. (+10 de poder político; a dívida britânica sobe 1)", "Accept the credit. (+10 political power; British debt rises by 1)",
    ["add_political_power = 10", "FROM = { add_to_variable = { ww1_britain_debt_burden = 1 } set_country_flag = ENG_ww1_russian_credit }"], 70),
   ("Recusar. (a Grã-Bretanha nota a recusa russa)", "Decline. (Britain notes Russian refusal)",
    ["FROM = { set_country_flag = ENG_ww1_russian_credit_refused }"], 30)]),
 dict(id=14, mode="trigger", trigger_full="tag = FRA",
  t=("O entendimento naval anglo-francês", "The Anglo-French Naval Understanding"),
  d=("Londres propõe que a Marinha Real proteja o Canal e o Mar do Norte, e a frota francesa o Mediterrâneo. Paris aceita, mas quer saber até onde vai o compromisso britânico.",
     "London proposes that the Royal Navy guard the Channel and the North Sea while the French fleet guards the Mediterranean. Paris agrees but wants to know how far the British commitment goes."),
  options=[
   ("Aceitar a divisão de áreas. (estabilidade +1%; experiência naval britânica +3)", "Accept the division of areas. (stability +1%; British naval experience +3)",
    ["add_stability = 0.01", "FROM = { navy_experience = 3 set_country_flag = ENG_ww1_french_naval_agreed }"], 70),
   ("Recusar o compromisso. (a Grã-Bretanha mantém patrulhas próprias)", "Decline the commitment. (Britain keeps independent patrols)",
    ["FROM = { set_country_flag = ENG_ww1_french_naval_refused }"], 30)]),
 dict(id=15, mode="trigger", trigger_full="OR = { tag = SER tag = GRE tag = ROM }",
  t=("Suprimentos para os Bálcãs", "Supplies for the Balkans"),
  d=("Londres oferece coordenar transporte e suprimentos aliados para o exército local, usando portos gregos e ferrovias romenas e sérvias.",
     "London offers to coordinate allied transport and supply for the local army through Greek ports and Romanian and Serbian railways."),
  options=[
   ("Aceitar a coordenação. (estabilidade +2%; a dívida britânica sobe 1)", "Accept the coordination. (stability +2%; British debt rises by 1)",
    ["add_stability = 0.02", "FROM = { add_to_variable = { ww1_britain_debt_burden = 1 } set_country_flag = ENG_ww1_balkan_coordination_agreed }"], 65),
   ("Recusar. (a Grã-Bretanha poupa suprimentos)", "Decline. (Britain spares supplies)",
    ["FROM = { set_country_flag = ENG_ww1_balkan_coordination_refused }"], 35)]),
]

DECISIONS = [
 dict(id="ENG_ww1_renew_american_credit",
  lines=["  visible = { has_country_flag = ENG_ww1_american_credit }",
         "  available = { has_war = yes has_capitulated = no country_exists = USA }",
         "  cost = 20 days_re_enable = 300",
         "  complete_effect = { USA = { country_event = { id = ww1_britain_dip.10 } } }",
         "  ai_will_do = { base = 1 modifier = { factor = 4 check_variable = { ww1_britain_debt_burden > 50 } } }"],
  pt=("Renovar o crédito americano", "Gasta 20 de poder político. Em guerra, repete o pedido de crédito aos Estados Unidos, que podem conceder ou recusar. Exige que o primeiro crédito tenha sido concedido."),
  en=("Renew the American Credit", "Spend 20 political power. At war, repeat the credit request to the United States, which may grant or decline. Requires the first credit to have been granted.")),
]
