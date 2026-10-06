"""Country-owned AUH content compiler; no Steam, donor, git or shared-file writes.

Catalogue -> playable PDX files + EN/PT localisation. Run explicitly to rebuild.
Artwork bindings are maintained separately in docs/auh_visual_bindings.json.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
P = "AUH_ww1_"
FOCI, PROJECTS, LOC = [], {}, {}

def loc(key, pt, en):
    LOC[key] = (pt, en)

def variable(name, amount):
    return f"add_to_variable = {{ auh_ww1_{name} = {amount} }}"

def f(key, pt, en, parent, x, y, effect, why_pt, why_en, cost=5, available="", excludes=(), ai=1):
    fid = P + key
    FOCI.append(dict(id=fid, parent=parent, x=x, y=y, effect=effect, cost=cost,
                     available=available, excludes=list(excludes), ai=ai))
    loc(fid, pt, en)
    loc(fid+"_desc", why_pt, why_en)
    return key

def chain(rows, parent, x, y, common="", cost=5):
    for i, row in enumerate(rows):
        key, pt, en, effect, dpt, den = row
        parent = f(key, pt, en, parent, x, y+i*2, effect, dpt, den, cost, common)
    return parent

def xp(amount=5, folder="land"):
    return f"{'army' if folder=='land' else 'navy' if folder=='naval' else 'air'}_experience = {amount}"

def tech(category, amount=.25):
    # One use, no ahead-of-time reduction: no free technology or 1936 equipment.
    return f"add_tech_bonus = {{ name = AUH_ww1_research_program bonus = {amount} uses = 1 category = {category} }}"

def idea(name):
    return "auh_ww1_set_"+name+" = yes"

def ev(number):
    return f"country_event = {{ id = ww1_auh.{number} days = 1 }}"

def unlock(name):
    return f"set_country_flag = auh_ww1_{name}_unlocked"

def project(key, pt, en, effect, dpt, den, states=(), days=120, factories=2, pp=35,
            available="", one=True):
    PROJECTS[key] = dict(pt=pt, en=en, effect=effect, dpt=dpt, den=den,
                         states=list(states), days=days, factories=factories,
                         pp=pp, available=available, one=one)
    return unlock("project_"+key)

def infrastructure(key, state, pt, en):
    return project(key, pt, en,
        f"{state} = {{ add_building_construction = {{ type = infrastructure level = 1 instant = yes }} }}",
        "Dois estabelecimentos civis ficam ocupados por 120 dias. Conclui um nível de infraestrutura; o projeto é cancelado se perdermos a região.",
        "Two civilian factories are committed for 120 days. Completes one infrastructure level; losing the region cancels the project.",
        states=[state], available=f"{state} = {{ infrastructure < 5 }}")

def railway(key, start, end, pt, en, level=2):
    return project(key, pt, en,
        f"build_railway = {{ level = {level} start_state = {start} target_state = {end} build_only_on_allied = yes }}",
        "Dois estabelecimentos civis ficam ocupados por 180 dias. As duas regiões devem permanecer sob nosso controle. A ferrovia segue território aliado.",
        "Two civilian factories are committed for 180 days. Both regions must remain under our control. The railway follows allied territory.",
        states=[start,end], days=180)

def industry(key, state, pt, en, kind="industrial_complex"):
    return project(key,pt,en,
        f"{state} = {{ add_extra_state_shared_building_slots = 1 add_building_construction = {{ type = {kind} level = 1 instant = yes }} }}",
        "Quatro estabelecimentos civis ficam ocupados por um ano. Conclui uma fábrica, sem alterar o orçamento industrial inicial.",
        "Four civilian factories are committed for one year. Completes one factory without changing the opening industrial budget.",
        states=[state],days=365,factories=4,pp=60)

def region(key, state, pt, en, modifier="provincial_council"):
    return project(key,pt,en,
        f"{state} = {{ add_dynamic_modifier = {{ modifier = AUH_ww1_{modifier} scope = AUS }} }} "+variable("cohesion",3),
        "A administração regional recebe autonomia civil permanente: reduz a extração de recursos em troca de melhores serviços e apoio local. O benefício regional só vale para a Áustria-Hungria.",
        "The regional administration receives permanent civilian autonomy: resource extraction falls in return for better services and local support. The regional benefit applies only to Austria-Hungary.",
        states=[state],days=90,factories=1,pp=40)

PEACE = "has_war = no has_capitulated = no"
WAR = "has_war = yes has_capitulated = no"
KARL = "has_country_flag = auh_ww1_karl_accession"
POST = "has_war = no has_capitulated = no has_country_flag = auh_ww1_fought_war"

# 40 political focuses: three constitutions and a separate crownland programme.
chain([
 ("crown_council","Reunir o Conselho da Coroa","Convene the Crown Council",ev(1),"Viena e Budapeste precisam definir o que a monarquia comum pode realmente financiar.","Vienna and Budapest must decide what their common monarchy can actually finance."),
 ("delegations","As delegações de 1911","The Delegations of 1911",unlock("delegations"),"Negociações regulares com as duas delegações podem obter consentimento, mas consomem influência política.","Regular negotiations with both delegations can secure consent, but consume political influence."),
 ("constitutional_audit","Revisar o compromisso de 1867","Review the Compromise of 1867",ev(2),"Não basta anunciar uma reforma. Escolheremos quem cede poderes e quem assume seu custo.","An announcement is not a reform. We must decide who yields power and who pays for it."),
 ("crownland_hearings","Ouvir as terras da Coroa","Hear the Crownlands",unlock("hearings"),"Representantes provinciais ganham acesso a consultas, sem promessas de lealdade automática.","Provincial representatives gain access to consultations, without promises of automatic loyalty.")
],None,8,0)

f("dualism","Renovar o dualismo","Renew Dualism","constitutional_audit",2,8,ev(3),"Preservar os dois centros de poder exige um orçamento negociado e mantém privilégios contestados.","Preserving two centres of power requires a negotiated budget and retains contested privileges.",excludes=["trialism","federalism"],ai=8)
chain([
 ("budapest_compact","O acordo de Budapeste","The Budapest Compact",variable("consent",8)+" "+variable("cohesion",-2),"O apoio magiar vem acompanhado de concessões às elites húngaras; outras províncias percebem o preço.","Magyar support comes with concessions to Hungarian elites; other provinces notice the price."),
 ("joint_budget","Ratificar o orçamento comum","Ratify the Common Budget",idea("budget_negotiated"),"Uma repartição negociada reduz o bloqueio orçamentário, sem eliminar a administração duplicada.","An agreed contribution reduces budget obstruction without abolishing the duplicated administration."),
 ("honved_safeguards","As garantias do Honvéd","Honvéd Safeguards",unlock("honved_contract"),"O contingente húngaro será financiado por contratos de formação e equipamento, e não por soldados criados do nada.","The Hungarian contingent will be funded through training and equipment contracts, rather than appearing from nothing."),
 ("crown_arbitration","Arbitragem da Coroa","Crown Arbitration",ev(4),"Uma disputa entre as administrações oferece a escolha entre impor a decisão ou aceitar mediação.","A dispute between administrations offers a choice between imposing a decision and accepting mediation."),
 ("quota_revision","Revisão das quotas econômicas","Revise the Economic Quotas",idea("budget_settled"),"A estabilidade do orçamento custa uma parcela permanente de consumo civil.","A stable budget still costs a permanent share of civilian consumption."),
 ("provincial_petitions","Direito de petição provincial","Provincial Right of Petition",variable("cohesion",6)+" add_political_power = -40", "Reconhecer petições compensa parcialmente a exclusão das nacionalidades, ao custo de influência do governo.","Recognising petitions partly offsets the exclusion of nationalities at a cost to government influence."),
 ("dual_war_cabinet","Dois governos, um gabinete de guerra","Two Governments, One War Cabinet",unlock("civil_cabinet"),"A coordenação em guerra será temporária e só poderá ser ativada com as duas administrações de acordo.","Wartime coordination is temporary and can only be activated with both administrations in agreement.")
],"dualism",2,10)
f("trialism","Negociar uma terceira Coroa","Negotiate a Third Crown","constitutional_audit",8,8,ev(5),"Um reino sul-eslavo altera a relação com Budapeste e exige garantias para sérvios, croatas e bósnios.","A South Slav kingdom changes the relationship with Budapest and requires safeguards for Serbs, Croats and Bosnians.",excludes=["dualism","federalism"],ai=1)
chain([
 ("croatian_diet","Convocar o Sabor","Convene the Sabor",region("sabor",103,"Organizar o Sabor ampliado","Organise the Expanded Sabor"),"O parlamento croata recebe um projeto de autonomia civil; o exército comum continua sujeito a negociação.","The Croatian parliament receives a civilian autonomy project; the common army remains subject to negotiation."),
 ("bosnian_guarantees","Garantias para a Bósnia","Guarantees for Bosnia",region("bosnia",104,"Garantias civis na Bósnia","Civil Guarantees in Bosnia"),"A terceira Coroa não pode transformar a população bósnia numa simples extensão de Zagreb.","The third Crown cannot turn Bosnia's population into a mere extension of Zagreb."),
 ("trialist_compensation","Compensar a administração húngara","Compensate the Hungarian Administration",variable("consent",12)+" add_political_power = -60", "Recuperar apoio em Budapeste exige concessões reais antes de ratificar o novo pacto.","Recovering support in Budapest requires real concessions before ratifying the new compact."),
 ("third_crown_charter","A carta da terceira Coroa","Charter of the Third Crown",ev(6),"O acordo só será ratificado com consentimento suficiente; a recusa mantém a monarquia em negociação.","The agreement can only be ratified with sufficient consent; refusal leaves the monarchy negotiating."),
 ("common_customs","Uma alfândega, três Coroas","One Customs Area, Three Crowns",idea("budget_trialist"),"O mercado comum preserva as receitas, mas financiar três administrações não é gratuito.","A common market preserves revenue, but funding three administrations is not free."),
 ("slavic_officer_school","Formação de oficiais sul-eslavos","South Slav Officer Training",tech("infantry_tech")+" "+variable("cohesion",3),"Abrir o corpo de oficiais melhora o acesso à formação, sem atribuir superioridade de combate por nacionalidade.","Opening the officer corps improves access to training without granting combat superiority by nationality."),
 ("trialist_war_cabinet","O gabinete das três Coroas","The Three Crowns Cabinet",unlock("civil_cabinet"),"A nova Coroa participa da administração da guerra e do custo do recrutamento.","The new Crown participates in administering the war and bearing the cost of recruitment.")
],"trialism",8,10)
f("federalism","Preparar uma monarquia federal","Prepare a Federal Monarchy","constitutional_audit",14,8,ev(7),"Um pacto federal é uma alternativa plausível, mas enfrenta oposição aristocrática e magiar.","A federal compact is a plausible alternative, but faces aristocratic and Magyar opposition.",excludes=["dualism","trialism"],ai=1)
chain([
 ("constitutional_convention","A convenção constitucional","The Constitutional Convention",unlock("convention"),"Delegados terão de negociar a repartição de poderes antes da promulgação da constituição.","Delegates must negotiate the distribution of powers before promulgating the constitution."),
 ("language_rights","Direitos linguísticos civis","Civil Language Rights",variable("cohesion",8)+" "+variable("consent",-5),"Reconhecer idiomas provinciais reforça a confiança local, mas enfrenta quem teme perder influência.","Recognising provincial languages strengthens local confidence, but meets resistance from those fearing lost influence."),
 ("federal_tax_compact","O pacto fiscal federal","The Federal Tax Compact",ev(8),"A federação precisa decidir quanto cada província retém e quanto entrega aos serviços comuns.","The federation must decide how much each province retains and how much funds common services."),
 ("council_of_peoples","Um conselho dos povos","A Council of Peoples",idea("council"),"A representação provincial limita a liberdade do executivo e torna a negociação uma obrigação permanente.","Provincial representation limits executive freedom and makes negotiation a permanent obligation."),
 ("federal_constitution","Promulgar a constituição federal","Promulgate the Federal Constitution",ev(9),"A ratificação exige apoio das administrações e das províncias; o nome do Estado acompanha a mudança constitucional.","Ratification requires administrative and provincial support; the state's name reflects its constitutional change."),
 ("federal_common_army","Um exército federal comum","A Federal Common Army",unlock("federal_service"),"A constituição mantém a defesa comum, com formação financiada e recrutamento supervisionado.","The constitution retains common defence, with funded training and supervised recruitment."),
 ("federal_war_cabinet","Gabinete federal de emergência","Federal Emergency Cabinet",unlock("civil_cabinet"),"A emergência poderá coordenar a produção, mas não apaga os direitos das províncias.","An emergency may coordinate production, but does not erase provincial rights.")
],"federalism",14,10)
for x, rows in [(0,[
 ("bohemian_landtag","O Landtag da Boêmia","The Bohemian Landtag",region("bohemia",9,"Conselho provincial da Boêmia","Bohemian Provincial Council"),"Representação local deve chegar à administração e ao orçamento, além de uma declaração imperial.","Local representation must reach administration and budgets, beyond an imperial declaration."),
 ("moravian_compromise","Ampliar o compromisso morávio","Extend the Moravian Compromise",region("moravia",75,"Serviços bilíngues na Morávia","Bilingual Services in Moravia"),"O precedente morávio oferece um modelo limitado de acomodação linguística.","The Moravian precedent offers a limited model of linguistic accommodation."),
 ("silesian_municipalities","As municipalidades da Silésia","Silesian Municipalities",region("silesia",74,"Acordos municipais da Silésia","Silesian Municipal Agreements"),"Serviços municipais e receitas locais são negociados sem mudar fronteiras por decreto.","Municipal services and local revenue are negotiated without changing borders by decree.")]),(6,[
 ("galician_autonomy","Autonomia civil na Galícia","Civil Autonomy in Galicia",region("galicia",89,"Conselho civil da Galícia","Galician Civil Council"),"Poloneses e rutenos precisam de garantias que sobrevivam à mobilização.","Poles and Ruthenians need safeguards that survive mobilisation."),
 ("ruthenian_schools","Escolas rutenas","Ruthenian Schools",region("ruthenia",73,"Financiar escolas rutenas","Fund Ruthenian Schools"),"Financiar serviços em idioma local fortalece a confiança, com custos administrativos reais.","Funding services in the local language builds confidence at a real administrative cost."),
 ("bukovina_compact","O acordo da Bucovina","The Bukovina Compact",region("bukovina",80,"Conselho plural da Bucovina","Plural Council of Bukovina"),"Uma província diversa exige representação compartilhada, sem lealdade automática de qualquer grupo.","A diverse province requires shared representation, without automatic loyalty from any group.")]),(12,[
 ("slovak_petitions","As petições eslovacas","Slovak Petitions",region("slovakia",70,"Atender petições eslovacas","Address Slovak Petitions"),"A negociação provincial enfrenta a concentração de poder na administração húngara.","Provincial negotiation confronts concentrated power in the Hungarian administration."),
 ("transylvanian_guarantees","Garantias na Transilvânia","Transylvanian Guarantees",region("transylvania",84,"Garantias municipais transilvanas","Transylvanian Municipal Safeguards"),"Romênios, magiares e saxões disputam influência; o acordo não cria núcleos ou territórios adicionais.","Romanians, Magyars and Saxons contest influence; the agreement creates no additional cores or territory."),
 ("banat_council","Um conselho para o Banato","A Council for the Banat",region("banat",82,"Conselho municipal do Banato","Banat Municipal Council"),"Negociar serviços regionais reduz conflitos administrativos sem eliminar divergências nacionais.","Negotiating regional services reduces administrative conflict without eliminating national disagreements.")]),(18,[
 ("dalmatian_services","Serviços civis na Dalmácia","Civil Services in Dalmatia",region("dalmatia",163,"Administração provincial dálmata","Dalmatian Provincial Administration"),"A costa adriática também precisa de administração civil, além de bases navais.","The Adriatic coast also needs civilian administration, beyond naval bases."),
 ("trentino_council","O conselho do Trentino","The Trentino Council",region("trentino",850,"Garantias civis no Trentino","Civil Guarantees in Trentino"),"Direitos locais não resolvem o irredentismo, mas tornam a permanência na monarquia menos onerosa.","Local rights do not resolve irredentism, but make remaining in the monarchy less burdensome."),
 ("provincial_ombudsman","Uma ouvidoria das províncias","A Provincial Ombudsman",unlock("ombudsman"),"Um canal permanente de reclamações reduz a distância entre as administrações e os súditos.","A permanent complaints channel reduces the distance between administrations and their subjects.")])]:
 chain(rows,"crownland_hearings",x,26)

# 40 economic focuses: projects take civilian capacity and have territorial cancellation.
chain([
 ("economic_inventory","Inventário econômico da monarquia","Survey the Monarchy's Economy",ev(10),"A indústria boêmia e o campo húngaro são complementares, mas não obedecem à mesma administração.","Bohemian industry and Hungarian agriculture are complementary, but answer to different administrations."),
 ("economic_coordination","Coordenar as duas economias","Coordinate the Two Economies",unlock("economic_coordination"),"Um gabinete econômico permite coordenar prioridades sem criar fábricas instantâneas.","An economic office coordinates priorities without conjuring instant factories."),
 ("common_statistics","Estatísticas econômicas comuns","Common Economic Statistics",tech("industry",.15),"Dados comparáveis permitem estudar métodos de produção dentro dos limites da tecnologia disponível.","Comparable data supports production research within the limits of available technology."),
 ("investment_board","Uma junta de investimentos","An Investment Board",unlock("investments"),"A junta autoriza projetos limitados; o jogador deverá reservar capacidade civil para executá-los.","The board authorises limited projects; the player must commit civilian capacity to carry them out.")
],None,38,0)
chain([
 ("skoda_contracts","Contratos com a Škoda","Škoda Contracts",tech("artillery"),"A especialização industrial sustenta pesquisa em artilharia, sem aumentar todos os ataques do exército.","Industrial specialisation supports artillery research without raising every army attack statistic."),
 ("pilsen_tooling","Ferramentaria em Plzeň","Toolmaking in Plzeň",industry("pilsen",9,"Ampliar a ferramentaria de Plzeň","Expand Plzeň Toolmaking","arms_factory"),"A ampliação de uma fábrica exige investimento civil prolongado na Boêmia.","Expanding a factory requires sustained civilian investment in Bohemia."),
 ("vitkovice_steel","Aço de Vítkovice","Vítkovice Steel",project("vitkovice","Investir nas instalações de Vítkovice","Invest in Vítkovice Facilities","75 = { add_resource = { type = steel amount = 4 } }","Duas fábricas civis por 180 dias desenvolvem quatro unidades de aço na Morávia.","Two civilian factories for 180 days develop four steel units in Moravia.",states=[75],days=180),"Carvão, metalurgia e transporte determinam quanto aço pode chegar aos arsenais.","Coal, metallurgy and transport determine how much steel reaches the arsenals."),
 ("steyr_small_arms","Armas leves de Steyr","Steyr Small Arms",tech("infantry_weapons"),"A padronização de armamento melhora a pesquisa sem entregar milhares de rifles gratuitos.","Standardising weapons assists research without handing out thousands of free rifles."),
 ("weiss_csepel","As oficinas de Csepel","The Csepel Workshops",industry("csepel",43,"Ampliar as oficinas de Csepel","Expand the Csepel Workshops","arms_factory"),"A indústria húngara pode sustentar o esforço comum se receber tempo e capital.","Hungarian industry can sustain the common effort if given time and capital."),
 ("arsenal_standards","Normas comuns dos arsenais","Common Arsenal Standards",idea("arsenals_standardised"),"Inspeções substituem a vantagem inicial genérica da Škoda por uma melhora modesta de produção e retenção.","Inspections replace the initial generic Škoda advantage with a modest production and retention improvement.")
],"investment_board",26,8)
chain([
 ("hungarian_harvest","A colheita húngara","The Hungarian Harvest",unlock("grain_agreement"),"Reservas urbanas dependem de comprar e transportar cereal, não apenas de possuir terras agrícolas.","Urban reserves depend on purchasing and transporting grain, not merely owning farmland."),
 ("granaries","Armazéns de cereal","Grain Warehouses",project("granaries","Construir armazéns comuns","Build Common Warehouses",variable("provisions",12),"Dois estabelecimentos civis por 120 dias ampliam as reservas alimentares. O estoque máximo é 100.","Two civilian factories for 120 days expand food reserves. Stocks are capped at 100.",states=[43,154]),"Os armazéns dão margem para enfrentar interrupções, sem abastecimento infinito.","Warehouses provide a buffer against disruption, without infinite supplies."),
 ("agricultural_tools","Ferramentas para o campo","Tools for the Countryside",tech("industry",.15)+" "+variable("provisions",4),"Métodos agrícolas e equipamentos simples ajudam a conservar trabalhadores no campo.","Agricultural methods and simple equipment help retain workers in the countryside."),
 ("rural_exemptions","Dispensas agrícolas sazonais","Seasonal Agricultural Exemptions",unlock("harvest_leave"),"Liberar parte dos contingentes para a colheita tem um custo de mobilização temporário.","Releasing part of the contingent for harvest carries a temporary mobilisation cost."),
 ("common_food_board","Uma comissão comum de alimentos","A Common Food Commission",ev(11),"A comissão pode negociar compras ou requisitar estoques. Cada opção afeta consentimento e coesão.","The commission may negotiate purchases or requisition stocks. Each choice affects consent and cohesion."),
 ("fair_rationing","Rações com distribuição equitativa","Equitable Ration Distribution",idea("rationing")+" "+unlock("rationing"),"A distribuição mais regular protege a reserva, mas continua retirando recursos da economia de guerra.","More regular distribution protects reserves, but still diverts resources from the war economy.")
],"investment_board",30,8)
chain([
 ("vienna_budapest_rail","A ligação Viena–Budapeste","The Vienna–Budapest Connection",railway("vienna_budapest",4,43,"Duplicar a ligação Viena–Budapeste","Double the Vienna–Budapest Connection"),"O eixo ferroviário entre as capitais precisa de obras concluídas para transportar mais carga.","The railway axis between the capitals needs completed works to carry more freight."),
 ("prague_vienna_rail","A ferrovia Praga–Viena","The Prague–Vienna Railway",railway("prague_vienna",9,4,"Ampliar a ferrovia Praga–Viena","Expand the Prague–Vienna Railway"),"A indústria boêmia só abastece os exércitos se a carga alcançar os centros de distribuição.","Bohemian industry only supplies the armies if freight reaches distribution centres."),
 ("galician_rail","A ferrovia da Galícia","The Galician Railway",railway("galician_rail",43,89,"Ampliar o corredor da Galícia","Expand the Galician Corridor"),"Um corredor melhor permite deslocar reservas para o leste, sem aumentar velocidade de todas as divisões.","A better corridor moves reserves east without raising the speed of every division."),
 ("bosnian_rail","O acesso ferroviário à Bósnia","Rail Access to Bosnia",railway("bosnian_rail",43,104,"Ampliar o acesso à Bósnia","Expand Access to Bosnia"),"A logística balcânica exige corredores reais em território aliado.","Balkan logistics requires real corridors through allied territory."),
 ("adriatic_rail","O corredor para o Adriático","The Adriatic Corridor",railway("adriatic_rail",4,736,"Ampliar o corredor adriático","Expand the Adriatic Corridor"),"Ligar Viena ao litoral favorece o porto e a frente italiana, desde que a linha permaneça aberta.","Connecting Vienna to the coast supports the port and Italian front while the line remains open."),
 ("railway_dispatch","Despacho ferroviário unificado","Unified Railway Dispatch",idea("logistics_organised"),"Horários comuns substituem a improvisação; a redução de consumo de suprimentos permanece limitada.","Common timetables replace improvisation; supply consumption savings remain limited.")
],"investment_board",34,8)
chain([
 ("factory_inspection","Inspeção das condições nas fábricas","Inspect Factory Conditions",ev(12),"Jornadas maiores podem elevar a produção por algum tempo, mas cobram um preço dos trabalhadores.","Longer shifts may raise production temporarily, but take a toll on workers."),
 ("workers_housing","Moradia dos trabalhadores","Workers' Housing",infrastructure("workers_housing",152,"Obras de habitação industrial","Industrial Housing Works"),"Habitação e serviços em zonas industriais exigem capacidade civil em vez de bônus permanentes ilimitados.","Housing and services in industrial areas require civilian capacity rather than unlimited permanent bonuses."),
 ("women_in_industry","Mulheres na indústria de guerra","Women in War Industry",unlock("industrial_labour"),"A contratação precisa de treinamento e proteção laboral; a mão de obra não surge sem custo.","Hiring requires training and labour safeguards; labour does not appear without cost."),
 ("labour_arbitration","Arbitragem trabalhista","Labour Arbitration",idea("labour_compact"),"Negociar com trabalhadores reduz o risco administrativo, à custa de uma parcela da produção máxima.","Negotiating with workers reduces administrative risk at the cost of a share of maximum output."),
 ("factory_canteens","Refeitórios nas fábricas","Factory Canteens",project("canteens","Instalar refeitórios industriais","Install Industrial Canteens",variable("provisions",8)+" "+variable("cohesion",4),"Capacidade civil ocupada por 120 dias melhora a distribuição alimentar e a confiança dos trabalhadores.","Civilian capacity committed for 120 days improves food distribution and workers' confidence.",states=[9,43]),"Alimentar trabalhadores concorre com outras despesas, mas ajuda a sustentar um esforço prolongado.","Feeding workers competes with other spending, but helps sustain a prolonged effort."),
 ("strike_settlement","Acordos para evitar paralisações","Agreements to Avoid Stoppages",unlock("labour_mediation"),"A mediação oferecerá alívio econômico limitado e condicionado ao apoio das administrações.","Mediation offers limited economic relief conditional on administrative support.")
],"investment_board",38,8)
chain([
 ("common_bank","O banco austro-húngaro","The Austro-Hungarian Bank",unlock("bond_issue"),"Crédito de emergência pode financiar a guerra, com obrigações que persistem depois dela.","Emergency credit can finance the war, with obligations that persist afterwards."),
 ("public_accounts","Publicar as contas comuns","Publish the Common Accounts",variable("consent",4)+" add_political_power = -35", "Contas transparentes ajudam a negociar novas quotas e limitam a liberdade do executivo.","Transparent accounts help negotiate new contributions and limit executive freedom."),
 ("wartime_credit","Limites para o crédito de guerra","Limits on War Credit",ev(13),"Uma emissão de dívida exige escolher entre capacidade imediata e pressão fiscal futura.","A debt issue requires choosing between immediate capacity and future fiscal pressure."),
 ("price_inspection","Inspeção de preços","Price Inspection",unlock("price_inspection"),"Combater desvios de distribuição exige pessoal e influência; inspeções não criam cereal.","Combating distribution abuses requires personnel and influence; inspections do not create grain."),
 ("municipal_taxation","Acordos de tributação municipal","Municipal Tax Agreements",variable("consent",5)+" "+variable("cohesion",2)+" add_political_power = -50", "Uma tributação negociada aumenta a confiança no financiamento dos serviços comuns.","Negotiated taxation strengthens confidence in funding common services."),
 ("fiscal_reserve","Reservas para o pós-guerra","Reserves for the Postwar Years",unlock("debt_repayment"),"Preparar a amortização da dívida permite evitar que a paz apenas prolongue a emergência fiscal.","Preparing debt repayment keeps peace from merely prolonging the fiscal emergency.")
],"investment_board",42,8)
chain([
 ("polytechnic_network","A rede de escolas politécnicas","The Polytechnic Network",tech("industry",.20),"Institutos técnicos estudam produção e manutenção, sem acelerar toda a pesquisa indefinidamente.","Technical institutes study production and maintenance without accelerating all research indefinitely."),
 ("technical_apprentices","Aprendizes técnicos","Technical Apprentices",tech("maintenance_company_tech"),"A formação técnica melhora o estudo da manutenção de equipamento já disponível.","Technical training improves research into maintaining available equipment."),
 ("danube_services","Serviços comerciais no Danúbio","Commercial Services on the Danube",infrastructure("danube",154,"Melhorar os serviços do Danúbio","Improve Danube Services"),"A navegação fluvial precisa de instalações, acesso e investimento, em vez de comércio abstrato gratuito.","River navigation requires facilities, access and investment rather than free abstract trade."),
 ("galician_oil","O petróleo da Galícia","Galician Oil",project("galician_oil","Desenvolver os campos petrolíferos","Develop the Oil Fields","91 = { add_resource = { type = oil amount = 3 } }","Investimento de 180 dias acrescenta três unidades de petróleo na região; a perda da Galícia cancela as obras.","A 180-day investment adds three oil units in the region; losing Galicia cancels the works.",states=[91],days=180),"A produção local reduz uma vulnerabilidade limitada; não torna a monarquia autossuficiente.","Local production reduces a limited vulnerability; it does not make the monarchy self-sufficient."),
 ("electrical_workshops","Oficinas de eletricidade e comunicações","Electrical and Communications Workshops",tech("electronics",.20),"A pesquisa elétrica permanece vinculada às tecnologias de sua época.","Electrical research remains tied to the technologies of its period."),
 ("civilian_conversion","Reconversão industrial preparada","Prepare Industrial Reconversion",industry("civilian_conversion",152,"Ampliar a produção civil austríaca","Expand Austrian Civilian Production"),"Um projeto civil pode diversificar a indústria, mas ocupa capacidade durante um ano inteiro.","A civilian project can diversify industry, but occupies capacity for a full year.")
],"investment_board",46,8)

# 50 army/air focuses: training, templates, logistics and paid operational missions.
chain([
 ("common_army_review","Revisar o exército comum","Review the Common Army",ev(14),"A organização do exército depende de orçamento, comunicação e reservas, não de inferioridade étnica.","Army organisation depends on budgets, communication and reserves, not ethnic inferiority."),
 ("staff_college","O colégio de estado-maior","The Staff College",xp(8),"Formação de oficiais produz experiência utilizável na organização das forças.","Officer training provides experience usable in organising the forces."),
 ("regimental_languages","Instrutores nos idiomas regimentais","Instructors in Regimental Languages",idea("languages_trained"),"O treinamento linguístico reduz parte da penalidade inicial de comunicação, com custos institucionais.","Language training reduces part of the opening communication penalty, with institutional costs."),
 ("mobilisation_tables","Quadros de mobilização revisados","Revised Mobilisation Tables",unlock("reserve_training"),"Reservistas precisarão de rifles, oficiais e tempo; o plano não cria divisões gratuitas.","Reservists require rifles, officers and time; the plan does not create free divisions."),
 ("military_programme","Um programa militar sustentável","A Sustainable Military Programme",ev(15),"A monarquia precisa escolher a prioridade entre equipamento, reservas e coordenação.","The monarchy must choose its priority among equipment, reserves and coordination.")
],None,64,0)
chain([
 ("mannlicher_standards","Padronizar os Mannlicher","Standardise the Mannlicher Rifles",tech("infantry_weapons"),"A inspeção de rifles melhora a pesquisa e evita fornecer armamento sem produção.","Rifle inspection assists research and avoids supplying weapons without production."),
 ("landwehr_training","Treinamento da Landwehr","Landwehr Training",unlock("landwehr_training"),"Formar forças territoriais exige equipamento retirado dos estoques e capacidade civil.","Training territorial forces requires equipment drawn from stocks and civilian capacity."),
 ("honved_training","Treinamento do Honvéd","Honvéd Training",unlock("honved_training"),"O treinamento húngaro depende do consentimento da administração de Budapeste.","Hungarian training depends on the consent of the Budapest administration."),
 ("reserve_template","Organização da infantaria de reserva","Reserve Infantry Organisation","load_oob = ww1_auh_reserve_templates", "A nova organização oferece uma divisão de reserva menor, que o jogador ainda deve recrutar e equipar.","The new organisation offers a smaller reserve division which the player must still recruit and equip."),
 ("machine_gun_sections","Seções de metralhadoras","Machine Gun Sections",tech("infantry_tech",.20),"As metralhadoras serão estudadas como equipamento da infantaria, sem bônus geral de ataque.","Machine guns are researched as infantry equipment without a general attack bonus."),
 ("junior_officers","Oficiais subalternos de carreira","Career Junior Officers",idea("languages_staff"),"Um corpo profissional melhora a comunicação e substitui o estágio anterior da reforma.","A professional corps improves communication and replaces the previous reform stage."),
 ("trench_rotation","Rotação de unidades nas trincheiras","Trench Unit Rotation",unlock("rest_rotation"),"Retirar contingentes para descanso reduz a pressão interna, mas exige tempo e despesas.","Withdrawing contingents for rest reduces internal pressure, but requires time and expense."),
 ("infantry_field_manual","Um manual comum de infantaria","A Common Infantry Field Manual",xp(8),"Um manual compartilhado oferece experiência para reorganizar as unidades existentes.","A shared manual provides experience for reorganising existing units."),
 ("replacement_depots","Depósitos de substituição","Replacement Depots",idea("languages_reformed"),"A reforma final remove a penalidade inicial de comunicação sem transformar o exército em uma força excepcional.","The final reform removes the initial communication penalty without turning the army into an exceptional force.")
],"military_programme",54,10)
chain([
 ("siege_school","A escola de artilharia de cerco","The Siege Artillery School",tech("artillery"),"A competência dos arsenais sustenta pesquisa; a conquista de fortalezas ainda depende do combate.","Arsenal expertise supports research; capturing fortresses still depends on combat."),
 ("battery_survey","Levantamento das baterias","Survey the Batteries",xp(6),"Inventariar calibres oferece experiência para ajustar os modelos das divisões.","Surveying calibres provides experience for adjusting division designs."),
 ("ammunition_inspection","Inspeção de munições","Ammunition Inspection",tech("artillery",.20),"A qualidade da munição deve ser estudada e produzida, em vez de garantir vitórias pelo foco.","Ammunition quality must be researched and produced rather than guaranteeing victories through a focus."),
 ("pack_artillery","Artilharia transportável nos Alpes","Pack Artillery in the Alps",tech("mountaineers_tech"),"O transporte em montanha melhora a formação especializada sem equipar todo o exército com tropas de elite.","Mountain transport supports specialist training without turning the entire army into elite troops."),
 ("observation_sections","Seções de observação de tiro","Gunnery Observation Sections",tech("recon_tech"),"Observadores precisam de treinamento para integrar reconhecimento e fogo.","Observers require training to connect reconnaissance and fire."),
 ("counter_battery","Estudo de contrabateria","Counter-Battery Studies",xp(8),"A experiência de tiro poderá financiar adaptações da organização militar.","Gunnery experience can fund adaptations to military organisation."),
 ("artillery_reserves","Reservas de munição por frente","Ammunition Reserves by Front",unlock("artillery_supply"),"As reservas operacionais serão reunidas a partir do estoque real e utilizadas em uma preparação limitada.","Operational reserves are assembled from actual stocks and used for limited preparation."),
 ("fire_control","Procedimentos de controle de fogo","Fire-Control Procedures",tech("signal_company_tech"),"Comunicações melhores devem chegar ao campo pela pesquisa e pelo equipamento de apoio.","Better communications must reach the field through research and support equipment."),
 ("siege_logistics","Logística da artilharia pesada","Heavy Artillery Logistics",tech("logistics_tech"),"O ganho tecnológico reduz problemas de transporte sem conceder ataque pesado permanente.","Technological progress reduces transport problems without granting permanent heavy attack.")
],"military_programme",59,10)
chain([
 ("carpathian_survey","Levantamento dos Cárpatos","Survey the Carpathians",unlock("carpathian_defence"),"A defesa depende de regiões mantidas e de projetos concluídos antes da ofensiva inimiga.","Defence depends on retained regions and projects completed before the enemy offensive."),
 ("alpine_routes","Rotas de abastecimento alpinas","Alpine Supply Routes",infrastructure("alpine_routes",153,"Melhorar as rotas alpinas","Improve Alpine Routes"),"As obras alpinas beneficiam uma região concreta, sem proteção uniforme sobre toda a monarquia.","Alpine works benefit a concrete region without uniform protection across the monarchy."),
 ("winter_equipment","Equipamento para o inverno","Winter Equipment",unlock("winter_stores"),"A reserva de inverno exige equipamento de apoio e prepara operações durante um período limitado.","Winter reserves require support equipment and prepare operations for a limited period."),
 ("sapper_school","A escola de sapadores","The Sapper School",tech("engineers_tech"),"Sapadores precisam de pesquisa e equipamento para apoiar divisões reais.","Sappers require research and equipment to support real divisions."),
 ("medical_services","Serviços médicos de campanha","Field Medical Services",tech("hospital_tech"),"A medicina de campanha reduz vulnerabilidades por meio de companhias pesquisadas e equipadas.","Field medicine reduces vulnerabilities through researched and equipped companies."),
 ("transport_columns","Colunas de transporte","Transport Columns",tech("logistics_tech",.20),"Transportes de campanha precisam caber no orçamento de suprimentos.","Field transport must fit within the supply budget."),
 ("defensive_manual","O manual defensivo de Borojević","Borojević's Defensive Manual",idea("defensive_staff"),"Uma escola defensiva traz uma melhora modesta de preparação e limita a velocidade de planejamento ofensivo.","A defensive school brings modest preparation improvements and limits offensive planning speed."),
 ("przemysl_supply","Abastecer Przemyśl","Supply Przemyśl",railway("przemysl",89,91,"Reforçar a ligação para Przemyśl","Reinforce the Przemyśl Connection"),"A fortaleza depende de um corredor de abastecimento preservado; o foco não impede sua queda.","The fortress depends on a retained supply corridor; the focus does not prevent its fall."),
 ("regional_defence","Defesa por setores regionais","Defence by Regional Sectors",unlock("defensive_sectors"),"Setores terão preparação temporária e objetivos de controle territorial, com fracasso possível.","Sectors receive temporary preparation and territorial-control objectives, with failure possible.")
],"military_programme",64,10)
chain([
 ("balkan_plan","Reavaliar o plano balcânico","Reassess the Balkan Plan",unlock("serbia_operation"),"A operação exige guerra real contra a Sérvia, munição e conquista territorial para ser considerada um sucesso.","The operation requires a real war against Serbia, ammunition and territorial conquest to count as a success."),
 ("galician_plan","O plano de recuperação da Galícia","The Plan to Recover Galicia",unlock("galicia_operation"),"Recuperar território depende do mapa atual; não haverá vitória automática contra a Rússia.","Recovering territory depends on the current map; there will be no automatic victory over Russia."),
 ("isonzo_plan","Planejar a defesa do Isonzo","Plan the Defence of the Isonzo",unlock("isonzo_operation"),"O setor só recebe preparação se houver guerra com a Itália e se o litoral estiver sob nosso controle.","The sector receives preparation only during war with Italy and while the coast remains under our control."),
 ("offensive_audit","Auditar os planos de Conrad","Audit Conrad's Plans",ev(16),"O estado-maior pode priorizar ofensivas ou preservar reservas. A escolha substitui a instituição anterior.","The staff may prioritise offensives or preserve reserves. The choice replaces the previous institution."),
 ("combined_staff","Coordenação entre frentes","Coordination Between Fronts",xp(10),"A coordenação gera experiência para ajustes de doutrina e organização, sem estatísticas de combate empilhadas.","Coordination generates experience for doctrine and organisational changes without stacked combat statistics."),
 ("field_telephones","Telefones de campanha","Field Telephones",tech("signal_company_tech",.20),"A transmissão de ordens deve ser pesquisada e distribuída às tropas.","Order transmission must be researched and issued to the troops."),
 ("reconnaissance_cavalry","Cavalaria de reconhecimento","Reconnaissance Cavalry",tech("recon_tech",.20),"A cavalaria conserva uma função de reconhecimento, sem se tornar uma força de ruptura anacrônica.","Cavalry retains a reconnaissance role without becoming an anachronistic breakthrough force."),
 ("doctrine_lessons","Aprender com as operações","Learn from Operations",xp(12)+" add_mastery_bonus = { name = AUH_ww1_operational_lessons bonus = .10 days = 180 folder = land }", "Experiência e aprendizado temporário alimentam as doutrinas da versão 1.19; não substituem o combate.","Experience and temporary learning support the version 1.19 doctrine system; they do not replace combat."),
 ("war_staff_review","Revisão do estado-maior em guerra","Wartime Staff Review",unlock("staff_review"),"Revisões periódicas permitem mudar a prioridade institucional, pagando novamente pelo preparo.","Periodic reviews allow a change in institutional priorities, paying again for preparation.")
],"military_programme",69,10,common=WAR)
chain([
 ("luftfahrtruppen","Organizar as Luftfahrtruppen","Organise the Luftfahrtruppen",xp(5,"air"),"Uma aviação nascente precisa de formação, equipamento e missões adequadas ao período.","An emerging air service requires training, equipment and missions suited to its period."),
 ("pilot_school","A escola de pilotos","The Pilot School",unlock("pilot_training"),"Cursos de pilotagem consomem equipamento de apoio e capacidade civil.","Pilot courses consume support equipment and civilian capacity."),
 ("lohner_workshops","As oficinas Lohner","The Lohner Workshops",tech("air_equipment",.20),"A pesquisa aeronáutica recebe auxílio limitado; aeronaves modernas continuam sujeitas às datas tecnológicas.","Aeronautical research receives limited assistance; modern aircraft remain subject to technological dates."),
 ("aerial_observation","Observação aérea","Aerial Observation",tech("cat_scout_plane"),"O reconhecimento é uma missão própria da aviação inicial, sem supremacia aérea gratuita.","Reconnaissance is a role for early aviation without free air supremacy."),
 ("aviatik_contracts","Contratos com a Aviatik","Aviatik Contracts",tech("light_fighter",.20),"A contratação prepara a pesquisa de caças, sem adicionar aviões aos estoques.","Contracts prepare fighter research without adding aircraft to stocks."),
 ("airfield_services","Serviços de aeródromo","Airfield Services",project("airfield","Ampliar os aeródromos austríacos","Expand Austrian Airfields","4 = { add_building_construction = { type = air_base level = 1 instant = yes } }","Dois estabelecimentos civis por 120 dias ampliam em um nível a base aérea na Áustria.","Two civilian factories for 120 days expand the Austrian air base by one level.",states=[4],available="4 = { air_base < 10 }"),"A infraestrutura aérea precisa ser construída antes de apoiar forças maiores.","Air infrastructure must be built before supporting larger forces."),
 ("air_artillery_liaison","Ligação entre aviadores e baterias","Liaison Between Airmen and Batteries",xp(6,"air"),"O treinamento conjunto oferece experiência aérea para organizar a força existente.","Joint training provides air experience to organise the existing force."),
 ("aeronautical_testing","Ensaios aeronáuticos","Aeronautical Trials",tech("plane_modules_tech",.20),"Os ensaios melhoram a pesquisa de módulos disponíveis sem bônus de antecipação tecnológica.","Trials improve research into available modules without ahead-of-time bonuses."),
 ("air_service_manual","Manual do serviço aéreo","Air Service Manual",xp(8,"air")+" add_mastery_bonus = { name = AUH_ww1_air_training bonus = .10 days = 180 folder = air }", "O serviço aprende por tempo limitado dentro das doutrinas atuais, preservando a escala inicial da aviação.","The service learns for a limited time within current doctrines, preserving the scale of early aviation.")
],"military_programme",74,10)

# 35 diplomatic focuses. Proposals produce recipient decisions, including refusal.
chain([
 ("ballhausplatz","Revisar a política do Ballhausplatz","Review Ballhausplatz Policy",ev(17),"A monarquia precisa decidir entre acomodação regional e pressão diplomática, sem bônus genérico para justificar guerras.","The monarchy must choose between regional accommodation and diplomatic pressure, without a generic war-justification bonus."),
 ("consular_network","A rede consular","The Consular Network",unlock("consular_contacts"),"Contatos consulares abrem canais de proposta com resposta do outro país.","Consular contacts open proposal channels that require a response from the other country."),
 ("diplomatic_accounts","As obrigações internacionais","International Obligations",variable("consent",3)+" add_political_power = -30", "As duas administrações devem conhecer o custo dos compromissos externos.","Both administrations must know the cost of external commitments."),
 ("dynastic_protocol","Protocolo dinástico revisado","Revised Dynastic Protocol",ev(18),"A sucessão segue a situação da casa imperial. Reformas civis não garantem impedir o atentado de Sarajevo.","Succession follows the situation of the imperial house. Civil reforms do not guarantee preventing the Sarajevo assassination."),
 ("foreign_programme","Uma política externa com limites","A Foreign Policy with Limits",unlock("foreign_programme"),"Alianças e acordos serão propostas recíprocas, com condições de guerra e de soberania.","Alliances and agreements will be reciprocal proposals with war and sovereignty conditions.")
],None,94,0)
chain([
 ("berlin_mission","Uma missão em Berlim","A Mission to Berlin",ev(30),"A Alemanha poderá aceitar ou rejeitar uma comissão militar conjunta; Viena não decide por ela.","Germany may accept or reject a joint military commission; Vienna does not decide for it."),
 ("german_staff_exchange","Intercâmbio de estado-maior","Staff Exchange with Germany",unlock("german_staff_exchange"),"O intercâmbio só pode ocorrer se a Alemanha concordou e continuamos aliados ou em paz entre nós.","The exchange can occur only if Germany agreed and we remain allied or at peace with each other."),
 ("german_supply_protocol","Protocolo de abastecimento aliado","Allied Supply Protocol",tech("logistics_tech",.20),"A coordenação de abastecimento orienta pesquisa; não transfere equipamento alemão sem sua autorização.","Supply coordination supports research; it does not transfer German equipment without permission."),
 ("common_war_assessment","Avaliação conjunta da guerra","Joint Assessment of the War",xp(8),"O planejamento conjunto oferece experiência e continua subordinado às frentes reais.","Joint planning provides experience and remains subordinate to actual fronts."),
 ("alliance_independence","Preservar a autonomia na aliança","Preserve Autonomy Within the Alliance",ev(19),"A monarquia escolhe entre maior dependência política e uma coordenação de custos mais limitada.","The monarchy chooses between greater political dependence and more limited cost coordination."),
 ("central_power_liaison","Ligação permanente com os aliados","Permanent Allied Liaison",unlock("allied_liaison"),"A ligação militar financiará cursos temporários enquanto a relação diplomática permitir.","Military liaison funds temporary courses while diplomatic relations permit.")
],"foreign_programme",84,10)
chain([
 ("belgrade_channel","Abrir um canal com Belgrado","Open a Channel to Belgrade",ev(32),"Uma normalização comercial depende da aceitação sérvia e só vale em paz.","Trade normalisation depends on Serbian acceptance and applies only in peacetime."),
 ("bosnian_civil_security","Segurança civil na Bósnia","Civil Security in Bosnia",ev(20),"A segurança pode ser negociada ou imposta; a repressão amplia tensões internas e não impede eventos por decreto.","Security may be negotiated or imposed; repression increases internal tensions and does not prevent events by decree."),
 ("sarajevo_services","Serviços públicos em Sarajevo","Public Services in Sarajevo",infrastructure("sarajevo",104,"Melhorar os serviços de Sarajevo","Improve Sarajevo Services"),"Investimento civil torna a administração mais presente sem prometer eliminar o nacionalismo.","Civil investment strengthens administration without promising to eliminate nationalism."),
 ("albanian_contacts","Contatos na Albânia","Contacts in Albania",ev(34),"A ajuda civil será proposta ao governo albanês; nenhum protetorado será imposto gratuitamente.","Civil assistance is proposed to the Albanian government; no protectorate is imposed for free."),
 ("montenegrin_channel","Um canal com Montenegro","A Channel to Montenegro",ev(36),"Um pacto de não agressão só existe se os dois lados concordarem.","A non-aggression pact exists only if both sides agree."),
 ("balkan_restraint","Limitar compromissos nos Bálcãs","Limit Commitments in the Balkans",idea("diplomatic_restraint"),"A acomodação reduz a pressão política interna, mas torna novas justificações de guerra mais lentas.","Accommodation reduces internal political pressure, but makes new war justifications slower.")
],"foreign_programme",89,10,common=PEACE)
chain([
 ("rome_channel","Conversações com Roma","Talks with Rome",ev(38),"Roma poderá aceitar um pacto de consulta ou recusar. O pacto não garante neutralidade eterna.","Rome may accept a consultation pact or refuse. The pact does not guarantee permanent neutrality."),
 ("italian_minorities","Direitos das comunidades italianas","Rights of Italian Communities",region("litorale",736,"Garantias civis no Litoral","Civil Safeguards in the Littoral"),"Direitos civis limitados custam capacidade administrativa e não anulam as reivindicações italianas.","Limited civil rights cost administrative capacity and do not cancel Italian claims."),
 ("adriatic_consultation","Consultas sobre o Adriático","Adriatic Consultations",unlock("italian_consultation"),"O canal de consulta permite renovar confiança somente enquanto a relação não se tornou uma guerra.","The consultation channel renews confidence only while the relationship has not become a war."),
 ("tyrolean_services","Serviços para o Tirol","Services for Tyrol",infrastructure("south_tyrol",39,"Melhorar serviços no Tirol do Sul","Improve South Tyrol Services"),"A fronteira alpina precisa de administração e transporte, além de símbolos imperiais.","The Alpine frontier needs administration and transport as well as imperial symbols."),
 ("italian_contingency","Preparar uma ruptura com a Itália","Prepare for a Break with Italy",unlock("italian_contingency"),"A preparação só será ativada diante de guerra real, consumindo equipamento de apoio.","Preparation is activated only during an actual war, consuming support equipment."),
 ("adriatic_civil_compact","Um compromisso civil no Adriático","A Civil Compact on the Adriatic",variable("cohesion",5)+" add_political_power = -50", "A administração costeira precisa de garantias locais mesmo quando a diplomacia fracassa.","Coastal administration requires local safeguards even when diplomacy fails.")
],"foreign_programme",94,10)
chain([
 ("bucharest_channel","Uma missão em Bucareste","A Mission to Bucharest",ev(40),"A Romênia decide se aceita o pacto agrícola; o território transilvano não será entregue ou ampliado pelo foco.","Romania decides whether to accept the agricultural pact; Transylvanian territory is neither ceded nor expanded by the focus."),
 ("romanian_grain","Contratos de cereal romeno","Romanian Grain Contracts",unlock("romanian_grain"),"Compras exigem acordo vigente, paz e capacidade civil para transporte.","Purchases require an active agreement, peace and civilian transport capacity."),
 ("transylvanian_dialogue","Diálogo com as municipalidades","Dialogue with the Municipalities",variable("cohesion",4)+" add_political_power = -35", "O diálogo local reforça a administração sem declarar que uma população abandonou sua identidade.","Local dialogue strengthens administration without declaring that a population abandoned its identity."),
 ("russian_channel","Um canal diplomático russo","A Russian Diplomatic Channel",ev(42),"Um pacto de consulta oferece espaço de negociação pré-guerra, com possibilidade de recusa.","A consultation pact offers room for prewar negotiation, with refusal possible."),
 ("eastern_contingency","A contingência oriental","The Eastern Contingency",unlock("eastern_contingency"),"O planejamento defensivo permanece relevante se a Rússia rejeitar o entendimento.","Defensive planning remains relevant if Russia rejects an understanding."),
 ("eastern_refugees","Assistência a refugiados orientais","Assist Eastern Refugees",unlock("refugee_assistance"),"A assistência consome capacidade civil e ajuda a sustentar a confiança, sem bônus de recrutamento de refugiados.","Assistance consumes civilian capacity and helps sustain confidence, without refugee recruitment bonuses.")
],"foreign_programme",99,10)
chain([
 ("karl_foreign_review","Carlos revisa os objetivos da guerra","Karl Reviews the War Aims",ev(21),"O novo soberano pode limitar objetivos e abrir negociações, pagando um custo de prestígio político.","The new sovereign may limit aims and open negotiations at a political prestige cost."),
 ("sixtus_channel","Abrir o canal de Sixtus","Open the Sixtus Channel",ev(44),"A França pode aceitar ou rejeitar a mediação. Um canal aberto não é uma paz automática.","France may accept or reject mediation. An open channel is not automatic peace."),
 ("armistice_delegates","Delegados para um armistício","Armistice Delegates",unlock("armistice_proposal"),"Uma proposta precisa de consentimento de todos os países que ainda combatem a monarquia.","A proposal requires the consent of every country still fighting the monarchy."),
 ("renounce_annexations","Renunciar às anexações de guerra","Renounce Wartime Annexations",variable("cohesion",5)+" add_war_support = -.03", "A renúncia ajuda a legitimar a negociação interna, mas reduz o apoio à continuação da guerra.","Renunciation helps legitimise internal negotiation, but reduces support for continuing the war."),
 ("conference_mandate","Um mandato para a conferência","A Mandate for the Conference",unlock("conference"),"O governo poderá concluir a negociação apenas quando todos os inimigos deram seu consentimento.","The government may conclude negotiations only once all enemies have consented."),
 ("peace_diplomacy","Uma diplomacia para a paz","Diplomacy for Peace",unlock("postwar_diplomacy"),"A diplomacia civil continuará disponível após a guerra, sujeita à soberania dos demais países.","Civil diplomacy remains available after the war, subject to other countries' sovereignty.")
],"foreign_programme",104,10,common=KARL)

# 20 naval focuses: preserve opening ships, fund yards and train the fleet.
chain([
 ("admiralty_review","Revisar o Almirantado","Review the Admiralty",ev(22),"O Adriático estreito pede uma marinha compatível com os recursos e as bases existentes.","The narrow Adriatic calls for a navy compatible with existing resources and bases."),
 ("naval_programme","Um programa naval limitado","A Limited Naval Programme",unlock("naval_programme"),"A marinha competirá com o exército por verba, pesquisa e capacidade industrial.","The navy competes with the army for funding, research and industrial capacity.")
],None,118,0)
chain([
 ("pola_maintenance","Manutenção em Pola","Maintenance at Pola",tech("maintenance_company_tech",.15),"As oficinas estudam manutenção; os navios iniciais não serão substituídos por cascos modernos.","Workshops study maintenance; starting ships are not replaced by modern hulls."),
 ("naval_artillery","A artilharia naval Škoda","Škoda Naval Artillery",tech("naval_artillery"),"O contrato auxilia a pesquisa de artilharia naval sem entregar couraçados prontos.","The contract assists naval artillery research without delivering completed battleships."),
 ("fleet_gunnery","Exercícios de tiro da esquadra","Fleet Gunnery Exercises",unlock("fleet_training"),"Exercícios custam capacidade civil e equipamento de apoio; sua experiência poderá financiar doutrina.","Exercises cost civilian capacity and support equipment; their experience can fund doctrine."),
 ("fleet_signalling","Sinalização da esquadra","Fleet Signalling",xp(8,"naval"),"O treinamento de sinalização oferece experiência para organizar a frota.","Signalling training provides experience for organising the fleet."),
 ("fleet_in_being","Preservar a esquadra de batalha","Preserve the Battle Fleet",idea("fleet_cautious"),"Uma postura cautelosa favorece retirada e preservação, mas reduz a velocidade operacional.","A cautious posture favours withdrawal and preservation, but reduces operational speed."),
 ("naval_lessons","Lições de operações no Adriático","Lessons from Adriatic Operations",xp(10,"naval")+" add_mastery_bonus = { name = AUH_ww1_naval_training bonus = .10 days = 180 folder = naval }", "O aprendizado naval segue o sistema atual de doutrina e dura um período definido.","Naval learning follows the current doctrine system and lasts for a defined period.")
],"naval_programme",112,4)
chain([
 ("trieste_yards","Os estaleiros de Trieste","The Trieste Shipyards",industry("trieste_yards",736,"Investir nos estaleiros de Trieste","Invest in the Trieste Shipyards","dockyard"),"Um estaleiro adicional exige quatro fábricas civis durante um ano; nenhum navio é gratuito.","An additional dockyard requires four civilian factories for one year; no ship is free."),
 ("torpedo_workshop","Oficinas de torpedos","Torpedo Workshops",tech("torpedo"),"O torpedo será pesquisado, fabricado e usado pela frota existente.","Torpedoes are researched, manufactured and used by the existing fleet."),
 ("escort_design","Projetos de escolta","Escort Designs",tech("dd_tech"),"Projetos de navios leves competem com a pesquisa dos grandes cascos.","Light-ship designs compete with research into larger hulls."),
 ("submarine_school","A escola de submarinos","The Submarine School",tech("ss_tech"),"A formação submarina não cria embarcações ou alcance oceânico impossível.","Submarine training creates neither vessels nor impossible oceanic range."),
 ("naval_repair","Organizar as oficinas navais","Organise Naval Workshops",idea("naval_refit_priority"),"A reequipagem ganha uma melhora limitada, à custa de parte da capacidade de construção naval.","Refitting receives a limited improvement at the cost of part of shipbuilding capacity."),
 ("naval_spares","Reservas de peças navais","Naval Spare Parts",unlock("naval_spares"),"Cursos de manutenção dependem de material retirado dos estoques.","Maintenance courses depend on material drawn from stocks.")
],"naval_programme",118,4)
chain([
 ("dalmatian_ports","Instalações da costa dálmata","Dalmatian Coastal Facilities",infrastructure("dalmatian_ports",163,"Melhorar instalações na Dalmácia","Improve Facilities in Dalmatia"),"Instalações terrestres apoiam o litoral sem criar um império naval global.","Land facilities support the coast without creating a global naval empire."),
 ("naval_patrols","Treinar patrulhas costeiras","Train Coastal Patrols",xp(6,"naval"),"A experiência vem de exercícios de patrulha, sem revelação automática da frota inimiga.","Experience comes from patrol exercises without automatically revealing the enemy fleet."),
 ("coastal_observation","Postos de observação costeira","Coastal Observation Posts",unlock("coastal_observation"),"Preparar observação exige pessoal e apoio; não substitui missões reais de patrulha.","Preparing observation requires personnel and support; it does not replace actual patrol missions."),
 ("seaplane_trials","Ensaios com hidroaviões","Seaplane Trials",tech("naval_air",.20),"A aviação marítima recebe pesquisa adequada ao período, sem porta-aviões modernos.","Maritime aviation receives period-appropriate research without modern aircraft carriers."),
 ("merchant_training","Formação da marinha mercante","Merchant Marine Training",unlock("merchant_training"),"A formação gera experiência naval a um custo civil; os comboios continuam sendo construídos pelo jogador.","Training generates naval experience at a civilian cost; the player still builds convoys."),
 ("adriatic_supply","Sustentar as bases do Adriático","Sustain the Adriatic Bases",railway("adriatic_supply",736,163,"Melhorar a ligação entre as bases","Improve the Connection Between Bases"),"As bases precisam de ligações terrestres e de costa mantida sob controle.","Bases require land connections and a coast retained under control.")
],"naval_programme",124,4)

# 15 postwar focuses: no forced 1918 collapse; institutions depend on actual peace.
chain([
 ("postwar_inventory","O inventário após a guerra","The Postwar Inventory",ev(23),"A reconstrução começa com a paz efetiva e com o custo acumulado da campanha.","Reconstruction begins with actual peace and the accumulated cost of the campaign."),
 ("veterans_registry","Registro dos veteranos","Register the Veterans",unlock("veterans"),"A assistência aos veteranos terá gastos civis regulares, sem devolver todas as baixas ao recrutamento.","Veteran assistance requires regular civilian spending without returning all casualties to recruitment."),
 ("reconstruction_board","Uma junta de reconstrução","A Reconstruction Board",unlock("reconstruction"),"A junta libera projetos territoriais que podem recuperar serviços e ajustar o orçamento da paz.","The board unlocks territorial projects that can restore services and adapt the peacetime budget.")
],None,138,0,common=POST)
chain([
 ("demobilisation","Desmobilização negociada","Negotiated Demobilisation",ev(24),"A paz exige escolher o ritmo de retorno à vida civil e pagar o custo da reintegração.","Peace requires choosing the pace of return to civilian life and paying for reintegration."),
 ("veterans_pensions","Pensões dos veteranos","Veterans' Pensions",idea("veterans"),"As pensões sustentam a confiança, mas permanecem uma despesa do orçamento civil.","Pensions sustain confidence but remain a civilian budget expense."),
 ("rehabilitation_centres","Centros de reabilitação","Rehabilitation Centres",project("rehabilitation","Instalar centros de reabilitação","Establish Rehabilitation Centres",variable("cohesion",6),"Duas fábricas civis por 180 dias financiam a reintegração dos veteranos e melhoram a confiança.","Two civilian factories for 180 days fund veteran reintegration and improve confidence.",states=[4],days=180),"Reintegrar sobreviventes e feridos é uma obrigação civil, sem bônus militar permanente.","Reintegrating survivors and wounded veterans is a civilian obligation without permanent military bonuses."),
 ("civilian_service","Serviços civis de paz","Peacetime Civil Services",idea("peace_administration"),"A administração sai da emergência e mantém um orçamento limitado para serviços comuns.","Administration leaves the emergency and retains a limited budget for common services.")
],"reconstruction_board",132,6,common=POST)
chain([
 ("regional_reconstruction","Reconstrução regional","Regional Reconstruction",infrastructure("galician_reconstruction",91,"Reconstruir os serviços da Galícia","Rebuild Galician Services"),"A recuperação das regiões exige território mantido e obras civis concluídas.","Regional recovery requires retained territory and completed civilian works."),
 ("urban_reconstruction","Recuperação das cidades","Urban Recovery",infrastructure("budapest_reconstruction",43,"Recuperar os serviços de Budapeste","Restore Budapest Services"),"As cidades precisam de investimento depois da mobilização prolongada.","Cities require investment after prolonged mobilisation."),
 ("peace_credit","Crédito para a reconstrução","Credit for Reconstruction",unlock("peace_credit"),"O crédito poderá ser contratado ou recusado, com dívida real na administração do país.","Credit may be contracted or refused, with real debt in the country's administration."),
 ("balanced_accounts","Equilibrar as contas da paz","Balance the Peacetime Accounts",unlock("peace_accounts"),"Amortizar obrigações reduz a pressão fiscal; nenhum foco apaga dívida acumulada de forma automática.","Repaying obligations reduces fiscal pressure; no focus automatically erases accumulated debt.")
],"reconstruction_board",138,6,common=POST)
chain([
 ("postwar_constitution","Reexaminar o pacto constitucional","Revisit the Constitutional Compact",ev(25),"A experiência da guerra pode justificar manter a monarquia, ampliar a federação ou convocar uma assembleia republicana.","The war experience may justify retaining the monarchy, extending federation or convening a republican assembly."),
 ("peacetime_elections","Representação política na paz","Peacetime Political Representation",ev(26),"O governo deve decidir entre eleição vinculante e representação consultiva; a escolha muda o regime e suas regras.","The government must choose between binding elections and consultative representation; the choice changes the regime and its rules."),
 ("danubian_services","Reconciliação das administrações","Reconcile the Administrations",unlock("danubian_services"),"A reconciliação continua exigindo concessões, sem declarar resolvidos todos os conflitos nacionais.","Reconciliation continues to require concessions without declaring every national conflict solved."),
 ("monarchy_future","O futuro do Estado danubiano","The Future of the Danubian State",ev(27),"O resultado da campanha depende dos territórios, da constituição e da sustentação social preservados pelo jogador.","The campaign's outcome depends on the territory, constitution and social support preserved by the player.")
],"reconstruction_board",144,6,common=POST)

assert len(FOCI)==200, len(FOCI)

# Immediate, bounded rewards for the focuses that previously only set an unlock flag.
from auh_focus_effects import apply as apply_focus_effects
apply_focus_effects(FOCI, LOC, P)

def write(path, text, bom=False):
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text.rstrip()+"\n",encoding="utf-8-sig" if bom else "utf-8")

# Wing roots in left-to-right order -> (shortcut key, EN, PT, search filter)
WINGS=[("crown_council","Constitution and Crownlands","Constituição e terras da Coroa","FOCUS_FILTER_POLITICAL"),
       ("economic_inventory","Economy and Infrastructure","Economia e infraestrutura","FOCUS_FILTER_INDUSTRY"),
       ("common_army_review","Army and Air Service","Exército e serviço aéreo","FOCUS_FILTER_ARMY_XP"),
       ("ballhausplatz","Diplomacy and Alliances","Diplomacia e alianças","FOCUS_FILTER_POLITICAL"),
       ("admiralty_review","Navy","Marinha","FOCUS_FILTER_NAVY_XP"),
       ("postwar_inventory","Postwar Settlement","Pacificação do pós-guerra","FOCUS_FILTER_STABILITY")]

def apply_layout():
    """Reshape ladders into diamonds and compute positions (scripts/focus_layout.py)."""
    import focus_layout as fl
    def listify(p): return [] if not p else ([p] if isinstance(p,str) else list(p))
    nodes=[dict(id=a['id'],parents=[P+p for p in listify(a['parent'])],also=[],
                excl=[P+e for e in a['excludes']],x=a['x'],y=a['y']) for a in FOCI]
    fl.diamondize(nodes)
    pos=fl.layout(nodes)
    for a,n in zip(FOCI,nodes):
        a['parent']=[p[len(P):] for p in n['parents']] or None
        a['also']=[p[len(P):] for p in n['also']]
        a['x'],a['y']=pos[a['id']]
    return nodes,pos

def build_focuses():
    nodes,pos=apply_layout()
    by={a['id']:a for a in FOCI}
    wing_pos={w[0]:by[P+w[0]] for w in WINGS}
    root_wing={}
    for a in FOCI:  # wing of a focus = root reached through its first parent
        cur=a
        while cur['parent']:cur=by[P+cur['parent'][0]]
        root_wing[a['id']]=cur['id'][len(P):]
    first=wing_pos[WINGS[0][0]]
    parts=["# AUH-owned campaign, June 1911–1923. 200 focuses; constitutional routes are exclusive.",
           "# Layout generated by scripts/focus_layout.py: six wings, forks and merges, no straight ladders.",
           "focus_tree = {", " id = AUH_ww1_tree", " country = { factor = 0 modifier = { add = 100 tag = AUS } }", " default = no",
           f" initial_show_position = {{ x = {first['x']} y = {first['y']} }}",
           " continuous_focus_position = { x = 100 y = 1800 }"]
    for key,en,pt,_ in WINGS:
        loc(P+"shortcut_"+key,"Ir para: "+pt,"Go to: "+en)
        w=wing_pos[key]
        parts += [" shortcut = {", f"  name = {P}shortcut_{key}", f"  target = {w['id']}", "  scroll_wheel_factor = 0.5", " }"]
    filters={w[0]:w[3] for w in WINGS}
    for a in FOCI:
        fid=a['id']; text=[" focus = {",f"  id = {fid}",f"  icon = GFX_focus_{fid}",f"  x = {a['x']}",f"  y = {a['y']}",f"  cost = {a['cost']}",
                           "  search_filters = { "+filters.get(root_wing[fid],"FOCUS_FILTER_POLITICAL")+" }"]
        if a['parent']:
            parents=a['parent'] if isinstance(a['parent'],list) else [a['parent']]
            text.append("  prerequisite = { "+" ".join("focus = "+P+p for p in parents)+" }")
        for q in a.get('also',[]): text.append("  prerequisite = { focus = "+P+q+" }")
        if a['excludes']: text.append("  mutually_exclusive = { "+" ".join("focus = "+P+x for x in a['excludes'])+" }")
        reward=a['effect'].replace('name = AUH_ww1_research_program','name = '+fid)
        text += ["  available = { has_capitulated = no "+a['available']+" }",
                 "  cancel_if_invalid = yes", "  continue_if_invalid = no", "  available_if_capitulated = no",
                 f"  ai_will_do = {{ factor = {a['ai']} }}",
                 "  completion_reward = { "+reward+" auh_ww1_clamp_counters = yes }", " }"]
        parts.extend(text)
    parts.append("}")
    write("common/national_focus/austria.txt","\n".join(parts))

if __name__ == "__main__":
    # Remaining build functions are defined in the country support module.
    from auh_country_support import build_support
    build_support(ROOT,FOCI,PROJECTS,LOC)
    from auh_content_extra import build_extra
    extra=build_extra(ROOT,LOC)
    build_focuses()
    write("docs/auh_focus_catalogue.json",json.dumps(FOCI,ensure_ascii=False,indent=2))
    for lang,index in [("braz_por",0),("english",1)]:
        lines=["l_"+lang+":"]
        for key,values in sorted(LOC.items()):
            v=values[index].replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')
            lines.append(f' {key}:0 "{v}"')
        write(f"localisation/{lang}/ww1_austria_hungary_l_{lang}.yml","\n".join(lines),bom=True)
    print(f"Built {len(FOCI)} AUH focuses, {len(PROJECTS)} projects and {len(LOC)} bilingual keys; extra content: {extra}.")
