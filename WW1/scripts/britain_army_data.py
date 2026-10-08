"""UK content, wing 5 (Army and Operations): rewards, descriptions, events, ideas, decisions.

Namespace ww1_britain_mil. Partner events (10-13) run in the partner's scope: ROOT = partner, FROM = ENG.
Rewards stay small and traded-off: no free divisions or equipment; research bonuses are one-use;
manpower is only granted with a visible cost (debt, labour support, industry).
"""
from britain_politics_data import var, flag, idea, remove_idea, pp, stab, navy_xp

NS = "ww1_britain_mil"
CATEGORY = "ENG_ww1_services_policy"
PEACE_CLEANUP = ["ENG_ww1_kitchener_armies", "ENG_ww1_pals_battalions", "ENG_ww1_flanders_supply", "ENG_ww1_creeping_barrage"]


def ev(n, days=0):
    extra = f" days = {days}" if days else ""
    return f"country_event = {{ id = {NS}.{n}{extra} }}"


def to(tag, n):
    return f"if = {{ limit = {{ country_exists = {tag} }} {tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}"


def to_ally(tag, n):
    return (f"if = {{ limit = {{ country_exists = {tag} is_in_faction_with = {tag} }} "
            f"{tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}")


def to_outsider(tag, n):
    # the partner must exist and must not be in the British faction
    return (f"if = {{ limit = {{ country_exists = {tag} NOT = {{ is_in_faction_with = {tag} }} }} "
            f"{tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}")


def army_xp(n):
    return f"army_experience = {n}"


def manpower(n):
    return f"add_manpower = {n}"


def war_support(x):
    return f"add_war_support = {x}"


def tech(name, category, bonus=0.25):
    return f"add_tech_bonus = {{ name = ENG_ww1_{name} bonus = {bonus} uses = 1 category = {category} }}"


def build(state, kind, slots=1):
    return (f"{state} = {{ add_extra_state_shared_building_slots = {slots} "
            f"add_building_construction = {{ type = {kind} level = 1 }} }}")


FOCI = {
# ------------------------------------------------------------------ army (20)
"the_haldane_establishment": (
    ["remove_ideas = ENG_professional_bef", idea("haldane_reforms"), pp(15), army_xp(5), flag("haldane_reforms")],
    "As reformas de Haldane criam um Estado-Maior Geral, uma Força Expedicionária e uma Força Territorial, modernizando a força regular. Ganha 15 de poder político, 5 de experiência de exército e a instituição Reformas de Haldane (tempo de treinamento -10%).",
    "Haldane's reforms create a General Staff, an Expeditionary Force and a Territorial Force, modernising the regular army. It grants 15 political power, 5 army experience and the Haldane Reforms institution (training time -10%)."),
"territorial_force_camps": (
    [tech("territorial_force_camps", "land_doctrine", 0.25), army_xp(10), stab(0.01), flag("territorial_camps")],
    "Todo verão, voluntários da Força Territorial acampam por duas semanas, treinando manobras em campo. Ganha 10 de experiência de exército, 1% de estabilidade e bônus de 25% em doutrina terrestre.",
    "Every summer Territorial Force volunteers camp for two weeks, training field manoeuvres. It grants 10 army experience, 1% stability and a 25% land doctrine research bonus."),
"the_special_reserve": (
    [build(127, "arms_factory"), manpower(15000), var("debt_burden", 1), flag("special_reserve")],
    "A Reserva Especial treina ex-soldados e novos recrutas, mantendo depósitos de armas no sudeste. Enfileira 1 fábrica militar, ganha 15.000 de mão de obra; a dívida sobe 1.",
    "The Special Reserve trains former soldiers and new recruits, maintaining arms depots in the South-East. Queues 1 arms factory, grants 15,000 manpower; debt rises by 1."),
"officer_training_corps": (
    [tech("officer_training_corps", "land_doctrine", 0.25), army_xp(15), pp(15), flag("officer_training_corps")],
    "Escolas públicas e universidades formam jovens oficiais de estado-maior. Ganha 15 de experiência de exército, 15 de poder político e bônus de 25% em doutrina terrestre.",
    "Public schools and universities train young staff officers. It grants 15 army experience, 15 political power and a 25% land doctrine research bonus."),
"regular_army_mobilisation": (
    [build(130, "arms_factory"), pp(10), army_xp(5), flag("mobilisation_tables")],
    "Tabelas de mobilização organizam ferrovias e depósitos de armas em Yorkshire. Enfileira 1 fábrica militar, ganha 10 de poder político e 5 de experiência de exército.",
    "Mobilisation tables organise railways and ordnance depots in Yorkshire. Queues 1 arms factory, grants 10 political power and 5 army experience."),
"army_service_corps_offices": (
    [build(127, "arms_factory"), tech("army_service_corps_offices", "logistics_tech"), flag("army_service_corps")],
    "O Corpo de Serviço do Exército organiza oficinas de transporte e depósitos em Aldershot. Enfileira 1 fábrica militar e ganha bônus de 25% em logística.",
    "The Army Service Corps organises transport workshops and depots at Aldershot. Queues 1 arms factory and grants a 25% research bonus on logistics."),
"the_expeditionary_establishment": (
    [build(128, "arms_factory"), army_xp(10), pp(10), var("debt_burden", 1), flag("expeditionary_establishment")],
    "A Força Expedicionária recebe seis divisões e arsenais em Coventry. Enfileira 1 fábrica militar nas Midlands, ganha 10 de experiência de exército e 10 de poder político; dívida +1.",
    "The Expeditionary Force receives six divisions and ordnance works in Coventry. Queues 1 arms factory in the Midlands, grants 10 army experience and 10 political power; debt rises by 1."),
"kitchener_new_armies": (
    ["remove_ideas = ENG_professional_bef", remove_idea("haldane_reforms"), idea("kitchener_armies"), manpower(25000), var("labour_support", -2), flag("kitchener_armies")],
    "Kitchener pede um milhão de voluntários: a instituição Haldane cede lugar ao exército de massa. Remove reformas anteriores, ganha 25.000 de mão de obra e a instituição Novos Exércitos (moral +5%, capacidade industrial -3%); apoio trabalhista -2.",
    "Kitchener asks for a million volunteers: the Haldane institution gives way to a mass army. Removes previous reforms, grants 25,000 manpower and the New Armies institution (army morale +5%, industrial capacity -3%); labour support falls by 2."),
"the_pals_battalion_system": (
    [remove_idea("kitchener_armies"), idea("pals_battalions"), manpower(10000), flag("pals_battalions")],
    "Amigos e vizinhos se alistam juntos nos Batalhões de Camaradas. Substitui os Novos Exércitos pela instituição Batalhões de Amigos (organização +5%) e ganha 10.000 de mão de obra.",
    "Friends and neighbours enlist together in Pals Battalions. Replaces New Armies with the Pals Battalions institution (army organisation +5%) and grants 10,000 manpower."),
"the_rifle_training_depots": (
    [build(126, "arms_factory"), tech("the_rifle_training_depots", "infantry_weapons"), army_xp(5), flag("rifle_depots")],
    "A Fábrica Real de Enfield e a Escola de Hythe ampliam a produção e o treino de tiro rápido. Enfileira 1 fábrica militar em Londres, ganha 5 de experiência de exército e bônus de 25% em armas de infantaria.",
    "The Royal Small Arms Factory at Enfield and Hythe School expand rifle output and marksmanship. Queues 1 arms factory in London, grants 5 army experience and a 25% bonus on infantry weapons."),
"field_medical_organisation": (
    [tech("field_medical_organisation", "hospital_tech"), stab(0.01), flag("field_medical")],
    "Postos de socorro, hospitais de evacuação e trens-hospital salvam feridos que antes morreriam. Ganha 1% de estabilidade e bônus de pesquisa de 25% em hospitais de campanha (uso único).",
    "Aid posts, casualty clearing stations and ambulance trains save wounded men who would once have died. It grants 1% stability and a one-use 25% research bonus on field hospitals."),
"the_artillery_observation_school": (
    [tech("the_artillery_observation_school", "recon_tech"), army_xp(5), flag("artillery_school")],
    "A escola de Larkhill ensina a observar o alvo, medir o erro e corrigir o tiro de artilharia. Ganha 5 de experiência de exército e bônus de pesquisa de 25% em reconhecimento (uso único).",
    "The Larkhill school teaches how to observe the target, measure the error and correct artillery fire. It grants 5 army experience and a one-use 25% research bonus on reconnaissance."),
"machine_gun_corps_formation": (
    [build(132, "arms_factory"), army_xp(10), var("debt_burden", 1), flag("machine_gun_corps")],
    "O Corpo de Metralhadoras concentra armas em companhias próprias com produção reforçada em Lancashire. Enfileira 1 fábrica militar, ganha 10 de experiência de exército; a dívida sobe 1.",
    "The Machine Gun Corps gathers weapons into dedicated companies with expanded output in Lancashire. Queues 1 arms factory, grants 10 army experience; debt rises by 1."),
"trench_mortar_sections": (
    [build(128, "arms_factory"), tech("trench_mortar_sections", "artillery"), army_xp(5), flag("trench_mortars")],
    "Oficinas em Birmingham produzem morteiros Stokes para dar artilharia de trincheira à infantaria. Enfileira 1 fábrica militar nas Midlands, ganha 5 de experiência de exército e bônus de 25% em artilharia.",
    "Workshops in Birmingham produce Stokes mortars for trench artillery. Queues 1 arms factory in the Midlands, grants 5 army experience and a 25% bonus on artillery."),
"gas_protection_training": (
    [tech("gas_protection_training", "infantry_weapons", 0.25), army_xp(5), war_support(0.01), var("debt_burden", 1), flag("gas_discipline")],
    "Depois de Ypres, máscaras de flanela dão lugar ao respirador em caixa. Ganha 5 de experiência de exército, 1% de apoio à guerra, bônus de 25% em equipamentos e a dívida sobe 1.",
    "After Ypres, flannel masks give way to the box respirator. Grants 5 army experience, 1% war support, a 25% infantry weapons bonus and debt rises by 1."),
"the_infantry_training_directorate": (
    [remove_idea("pals_battalions"), idea("training_directorate"), pp(10), flag("training_directorate")],
    "A Diretoria de Treinamento padroniza o manual de combate, substituindo os batalhões de amigos. Instituição Diretoria de Treinamento (tempo de treinamento -10%, ganho de XP +5%) e 10 de poder político.",
    "The Training Directorate standardises combat manuals, replacing the pals battalions. Training Directorate institution (training time -10%, army XP gain +5%) and 10 political power."),
"combined_arms_staff_courses": (
    [remove_idea("training_directorate"), idea("combined_arms_staff"), army_xp(15), flag("combined_arms")],
    "Cursos de estado-maior unem infantaria, artilharia, engenharia e aviação, superando manuais básicos. Ganha 15 de experiência de exército e a instituição Armas Combinadas (velocidade de planejamento +10%).",
    "Staff courses integrate infantry, artillery, engineers and aviation, advancing beyond basic manuals. Grants 15 army experience and the Combined Arms institution (planning speed +10%)."),
"the_demobilisation_register": (
    [ev(5)],
    "Milhões de homens querem voltar para casa. O registro decide a ordem: tempo de serviço, emprego garantido ou unidades inteiras. Dispara o evento da desmobilização.",
    "Millions of men want to go home. The register decides the order: length of service, guaranteed job, or whole units. It triggers the demobilisation event."),
"a_smaller_professional_force": (
    [remove_idea("general_staff_lessons"), remove_idea("flanders_supply"), var("debt_burden", -3), pp(15), stab(0.01), flag("smaller_army")],
    "O Exército volta a ser pequeno e profissional, desmobilizando instituições de guerra. A dívida cai 3; ganha 15 de poder político e 1% de estabilidade. Exclui a renovação territorial.",
    "The Army returns to being small and professional, standing down wartime institutions. Debt falls by 3; it grants 15 political power and 1% stability. Excludes territorial renewal."),
"territorial_defence_renewal": (
    [tech("territorial_defence_renewal", "land_doctrine", 0.5), army_xp(15), stab(0.02), var("debt_burden", 1), pp(15), flag("territorial_army")],
    "O Exército Territorial renasce com veteranos e doutrina moderna. Ganha 15 de experiência de exército, 15 de poder político, 2% de estabilidade e bônus de 50% em doutrina terrestre. Exclui a força profissional menor.",
    "The Territorial Army is reborn with veterans and modern doctrine. Grants 15 army experience, 15 political power, 2% stability and a 50% land doctrine bonus. Excludes the smaller professional force."),
# ------------------------------------------------------------------ operations (20)
"the_channel_mobilisation_timetable": (
    [tech("the_channel_mobilisation_timetable", "land_doctrine", 0.25), pp(15), army_xp(5), flag("channel_timetable")],
    "Depois de Agadir, Wilson e o Estado-Maior fixam horários de trem e navios para o Canal. Ganha 15 de poder político, 5 de experiência de exército e bônus de 25% em doutrina terrestre.",
    "After Agadir, Wilson and the Staff fix train and ship timetables for the Channel. Grants 15 political power, 5 army experience and a 25% land doctrine bonus."),
"embarkation_depot_preparation": (
    ["127 = { add_building_construction = { type = naval_base level = 1 } }", tech("embarkation_depot_preparation", "train_tech"), flag("embarkation_depots")],
    "Southampton, Portsmouth e Folkestone recebem depósitos, cais e ampliação de base naval. Adiciona 1 nível de base naval no sudeste e bônus de pesquisa de 25% em transporte ferroviário.",
    "Southampton, Portsmouth and Folkestone receive depots, quays and naval base expansions. Adds 1 naval base level in the South-East and a 25% bonus on rail transport."),
"the_bef_deployment_plan": (
    [army_xp(10), flag("bef_deployed"), to_ally("FRA", 10)],
    "Em agosto de 1914, a Força Expedicionária Britânica cruza o Canal. A França recebe os ingleses com entusiasmo. Ganha 10 de experiência de exército; a França ganha apoio à guerra.",
    "In August 1914 the British Expeditionary Force crosses the Channel. France welcomes the British with enthusiasm. It grants 10 army experience; France gains war support."),
"the_flanders_supply_organisation": (
    [remove_idea("haldane_reforms"), idea("flanders_supply"), var("debt_burden", 1), flag("flanders_supply")],
    "Boulogne, Calais e Dunquerque viram portos de suprimento com ferrovias até a linha. A dívida sobe 1; ganha a instituição Suprimento de Flandres (consumo de suprimentos -5%).",
    "Boulogne, Calais and Dunkirk become supply ports, with railways to the front line. Debt rises by 1; it grants the Flanders Supply institution (supply consumption -5%)."),
"holding_the_continental_line": (
    ["126 = { add_building_construction = { type = bunker level = 1 } }", army_xp(15), war_support(0.01), flag("held_the_line")],
    "Mons, Le Cateau e Ypres custam quase todo o exército regular, mas a linha resiste e trincheiras são cavadas. Constrói 1 forte terrestre, ganha 15 de experiência de exército e 1% de apoio à guerra.",
    "Mons, Le Cateau and Ypres cost almost the entire regular army, but the line holds and defensive works are dug. Adds 1 bunker, grants 15 army experience and 1% war support."),
"artillery_ammunition_concentration": (
    [build(131, "arms_factory"), army_xp(10), var("debt_burden", 1), flag("ammo_concentration")],
    "Antes da ofensiva, canhões e caixas de munição são produzidos pelas fábricas do norte. Enfileira 1 fábrica militar em Sheffield/Elswick, ganha 10 de experiência de exército; a dívida sobe 1.",
    "Before the offensive, guns and shell crates are produced by northern ordnance works. Queues 1 arms factory in Sheffield/Elswick, grants 10 army experience; debt rises by 1."),
"a_limited_offensive_doctrine": (
    [tech("a_limited_offensive_doctrine", "land_doctrine", 0.5), army_xp(10), pp(10), flag("limited_offensive")],
    "Rawlinson defende a doutrina de morder e segurar com apoio de fogo cerrado. Ganha 10 de experiência de exército, 10 de poder político e bônus de 50% em doutrina terrestre.",
    "Rawlinson advocates the bite-and-hold doctrine with concentrated fire support. It grants 10 army experience, 10 political power and a 50% land doctrine bonus."),
"the_dardanelles_staff_study": (
    [ev(2)],
    "Churchill quer forçar os Dardanelos e abrir o caminho até Constantinopla. Fisher e Kitchener duvidam. Dispara o debate sobre o estreito: tentativa naval, desembarque conjunto ou arquivar o plano.",
    "Churchill wants to force the Dardanelles and open the road to Constantinople. Fisher and Kitchener doubt. It triggers the debate over the Straits: naval attempt, joint landing or shelving the plan."),
"mediterranean_landing_preparation": (
    [army_xp(10), navy_xp(5), flag("med_landing_prep")],
    "Lemnos e Mudros viram bases de desembarque com barcaças, cais e hospitais. Ganha 10 de experiência de exército e 5 de experiência naval.",
    "Lemnos and Mudros become landing bases with lighters, quays and hospitals. It grants 10 army experience and 5 naval experience."),
"mesopotamian_supply_review": (
    [tech("mesopotamian_supply_review", "maintenance_company_tech"), flag("mesopotamian_review")],
    "Um exército no Tigre precisa de rios, barcos, ferrovias e água potável que ninguém planejou. Ganha bônus de pesquisa de 25% em manutenção (uso único); o cerco de Kut será menos pesado.",
    "An army on the Tigris needs rivers, boats, railways and drinking water that no one planned. It grants a one-use 25% research bonus on maintenance; the siege of Kut will hurt less."),
"the_western_offensive_staff_study": (
    [tech("the_western_offensive_staff_study", "land_doctrine", 0.25), army_xp(10), pp(10), flag("loos_study")],
    "Loos e Festubert mostram as lições de reservas e artilharia. Ganha 10 de experiência de exército, 10 de poder político e bônus de 25% em doutrina terrestre.",
    "Loos and Festubert show lessons in reserves and artillery. It grants 10 army experience, 10 political power and a 25% land doctrine bonus."),
"the_creeping_barrage_school": (
    [remove_idea("combined_arms_staff"), idea("creeping_barrage"), tech("the_creeping_barrage_school", "artillery"), flag("creeping_barrage")],
    "A cortina de fogo cronometrada avança à frente dos soldados. Substitui o estado-maior de armas combinadas pela instituição Cortina de Fogo (ataque de artilharia +5%) e bônus de 25% em artilharia.",
    "The timed creeping barrage advances ahead of the soldiers. Replaces combined arms staff with the Creeping Barrage institution (artillery attack +5%) and a 25% artillery bonus."),
"tank_committee_experiments": (
    [build(129, "arms_factory"), tech("tank_committee_experiments", "armor"), var("debt_burden", 1), flag("tank_corps")],
    "O Comitê dos Navios Terrestres estabelece oficinas de montagem de tanques em Lincoln. Enfileira 1 fábrica militar, ganha bônus de pesquisa de 25% em blindados; a dívida sobe 1.",
    "The Landships Committee establishes tank assembly workshops in Lincoln. Queues 1 arms factory, grants a 25% research bonus on armour; debt rises by 1."),
"assault_coordination_exercises": (
    [tech("assault_coordination_exercises", "land_doctrine", 0.25), army_xp(10), "if = { limit = { has_country_flag = ENG_ww1_tank_corps } army_experience = 5 }", flag("assault_coordination")],
    "Infantaria, artilharia e tanques ensaiam o ataque coordenado em terreno demarcado. Ganha 10 de experiência de exército, bônus de 25% em doutrina terrestre e +5 XP com tanques.",
    "Infantry, artillery and tanks rehearse coordinated assault on marked ground. Grants 10 army experience, a 25% land doctrine bonus and +5 XP with tanks."),
"palestine_railway_liaison": (
    ["447 = { add_building_construction = { type = infrastructure level = 1 } }", tech("palestine_railway_liaison", "train_tech"), army_xp(5), pp(10)],
    "Allenby constrói ferrovia e canal de água potável no Sinai para alcançar Gaza. Adiciona 1 nível de infraestrutura no Sinai, ganha 5 de experiência de exército, 10 de poder político e bônus de pesquisa de 25% em ferrovias.",
    "Allenby builds a railway and pipeline across Sinai to reach Gaza. Adds 1 infrastructure level in Sinai, grants 5 army experience, 10 political power and a one-use 25% research bonus on rail transport."),
"the_spring_defence_plan": (
    [tech("the_spring_defence_plan", "land_doctrine", 0.5), pp(15), army_xp(10), flag("spring_defence_plan")],
    "O estado-maior prepara a defesa em profundidade para 1918 contra a investida alemã. Ganha 15 de poder político, 10 de experiência de exército e bônus de 50% em doutrina terrestre.",
    "The staff prepares defence in depth for 1918 against the German push. Grants 15 political power, 10 army experience and a 50% land doctrine bonus."),
"the_allied_counteroffensive_plan": (
    [ev(7)],
    "Foch coordena os exércitos aliados para uma ofensiva geral. Haig, Rawlinson e os canadenses planejam Amiens. Dispara o evento da ofensiva.",
    "Foch coordinates the Allied armies for a general offensive. Haig, Rawlinson and the Canadians plan Amiens. It triggers the offensive event."),
"operational_reserve_restoration": (
    [manpower(15000), var("labour_support", -2), army_xp(5)],
    "Lloyd George mobiliza divisões territoriais e recomposições para recompor as reservas. Ganha 15.000 de mão de obra e 5 de experiência de exército; o apoio trabalhista cai 2.",
    "Lloyd George mobilises territorial divisions and replenishments to rebuild the reserves. Grants 15,000 manpower and 5 army experience; labour support falls by 2."),
"the_armistice_stand_down_plan": (
    [pp(25), stab(0.02), army_xp(10), flag("armistice_stand_down")],
    "O armistício de 11 de novembro suspende operações e organiza a ocupação pacífica. Ganha 25 de poder político, 2% de estabilidade e 10 de experiência de exército.",
    "The armistice of 11 November suspends operations and organises peaceful occupation. Grants 25 political power, 2% stability and 10 army experience."),
"lessons_for_the_general_staff": (
    [remove_idea("creeping_barrage"), army_xp(15), pp(15), idea("general_staff_lessons"), flag("staff_lessons")],
    "O Estado-Maior Geral compila as doutrinas de quatro anos de combate nos novos manuais de 1919. Remove doutrinas provisórias, ganha 15 de experiência de exército, 15 de poder político e a instituição Lições da Guerra (ganho de XP +10%).",
    "The General Staff compiles four years of operational doctrine into new 1919 manuals. Removes interim doctrines, grants 15 army experience, 15 political power and the Lessons of the War institution (army XP gain +10%)."),
}

EXCLUSIVE = [("a_smaller_professional_force", "territorial_defence_renewal")]

IDEAS = {
 "haldane_reforms": ("training_time_factor = -0.1", "Reformas de Haldane", "Haldane Reforms",
   "Um exército pequeno, mas organizado, com reservas treinadas e um estado-maior.", "A small but organised army, with trained reserves and a general staff.", ""),
 "kitchener_armies": ("army_morale_factor = 0.05 industrial_capacity_factory = -0.03", "Novos Exércitos", "New Armies",
   "Milhares de voluntários entram no exército, e as fábricas sentem a falta deles.", "Thousands of volunteers join the army, and the factories feel their absence.", ""),
 "pals_battalions": ("army_org_factor = 0.05", "Batalhões de Amigos", "Pals Battalions",
   "Homens da mesma rua lutam juntos. A coesão é maior, mas uma batalha pode destruir uma cidade.", "Men of the same street fight together. Cohesion is higher, but one battle can wipe out a town.", ""),
 "flanders_supply": ("supply_consumption_factor = -0.05", "Suprimento de Flandres", "Flanders Supply",
   "Portos, canais e ferrovias levam suprimentos à frente com menos desperdício.", "Ports, canals and railways carry supplies forward with less waste.", ""),
 "training_directorate": ("training_time_factor = -0.1 experience_gain_army_factor = 0.05", "Diretoria de Treinamento", "Training Directorate",
   "Um só manual e uma só doutrina, da seção ao batalhão.", "One manual and one doctrine, from section to battalion.", ""),
 "combined_arms_staff": ("planning_speed = 0.1", "Armas Combinadas", "Combined Arms",
   "Estados-maiores aprendem a planejar infantaria, artilharia e aviação como um só sistema.", "Staffs learn to plan infantry, artillery and aviation as a single system.", ""),
 "creeping_barrage": ("army_artillery_attack_factor = 0.05", "Cortina de Fogo", "Creeping Barrage",
   "A artilharia avança à frente da infantria, segundo o relógio.", "Artillery advances ahead of the infantry, by the clock.", ""),
 "general_staff_lessons": ("experience_gain_army_factor = 0.1", "Lições da Guerra", "Lessons of the War",
   "O estado-maior transforma quatro anos de erros em manuais.", "The staff turns four years of mistakes into manuals.", ""),
}

EVENTS = [
 dict(id=2, mode="trigger",
  t=("A decisão dos Dardanelos", "The Dardanelles Decision"),
  d=("Churchill defende que a frota force o estreito e chegue a Constantinopla. Fisher e Kitchener duvidam da aventura, e o Conselho de Guerra precisa de uma decisão rápida, antes que a Turquia reforce as fortalezas.",
     "Churchill argues that the fleet should force the Straits and reach Constantinople. Fisher and Kitchener doubt the adventure, and the War Council needs a quick decision before Turkey reinforces the forts."),
  options=[
   ("Tentar só com a frota. (experiência naval +3, dívida +1)", "Try with the fleet alone. (naval experience +3, debt +1)",
    [navy_xp(3), var("debt_burden", 1), flag("dardanelles_naval"), to_outsider("TUR", 11)], 40),
   ("Fazer um desembarque conjunto. (experiência de exército +4, experiência naval +2, estabilidade -1%)", "Make a joint landing. (army experience +4, naval experience +2, stability -1%)",
    [army_xp(4), navy_xp(2), stab(-0.01), flag("dardanelles_landing"), to_outsider("TUR", 11)], 40),
   ("Arquivar o plano. (+10 de poder político)", "Shelve the plan. (+10 political power)",
    [pp(10), flag("dardanelles_shelved")], 20)]),
 dict(id=3, mode="mtth", days=10, once=True,
  trigger="date > 1916.4.1 date < 1917.1.1 has_war_with = TUR",
  t=("O cerco de Kut", "The Siege of Kut"),
  d=("A Sexta Divisão indiana, cercada em Kut-al-Amara pelos turcos, está sem comida. Os ataques de socorro falham na lama e nas inundações do Tigre. A rendição é questão de semanas.",
     "The Sixth Indian Division, surrounded at Kut-al-Amara by the Turks, is out of food. Relief attacks fail in the mud and the Tigris floods. Surrender is a matter of weeks."),
  options=[
   ("Tentar mais um ataque de socorro. (-10 de poder político, experiência de exército +4; apoio à guerra -1% com revisão de suprimento, senão -2%)", "Mount one more relief attempt. (-10 political power, army experience +4; war support -1% with the supply review, otherwise -2%)",
    [pp(-10), army_xp(4), "if = { limit = { has_country_flag = ENG_ww1_mesopotamian_review } add_war_support = -0.01 }",
     "else = { add_war_support = -0.02 }"], 55),
   ("Negociar a saída com os oficiais turcos. (dívida +1, apoio à guerra -1%)", "Negotiate terms with the Turkish officers. (debt +1, war support -1%)",
    [var("debt_burden", 1), war_support(-0.01), flag("kut_fallen")], 45)]),
 dict(id=4, mode="mtth", days=5, once=True,
  trigger="date > 1916.6.29 date < 1917.6.1 has_war_with = GER",
  t=("O primeiro dia do Somme", "The First Day of the Somme"),
  d=("Em 1º de julho de 1916 os batalhões de voluntários sobem das trincheiras em linha. Em poucas horas há quase sessenta mil baixas, e cidades inteiras perdem seus jovens. Haig exige continuar a batalha.",
     "On 1 July 1916 the volunteer battalions climb out of their trenches in line. Within hours there are nearly sixty thousand casualties, and whole towns lose their young men. Haig demands the battle go on."),
  options=[
   ("Aceitar as perdas e continuar a ofensiva. (experiência de exército +6, apoio à guerra -3%)", "Accept the losses and press the offensive. (army experience +6, war support -3%)",
    [army_xp(6), war_support(-0.03), flag("somme_pressed")], 60),
   ("Espalhar as perdas entre os regimentos. (estabilidade +1%, apoio à guerra -1%, experiência de exército +2)", "Spread the losses across the regiments. (stability +1%, war support -1%, army experience +2)",
    ["remove_ideas = ENG_ww1_pals_battalions", stab(0.01), war_support(-0.01), army_xp(2), flag("pals_disbanded")], 40)]),
 dict(id=5, mode="trigger",
  t=("A desmobilização", "Demobilisation"),
  d=("Milhões de homens esperam a volta para casa. O gabinete decide se vale o tempo de serviço, o emprego garantido ou a manutenção de unidades inteiras. Quem fica mais tempo na França pensa que é injusto.",
     "Millions of men await the trip home. The cabinet decides whether length of service, guaranteed jobs or the keeping of whole units counts. Those left longer in France think it unfair."),
  options=[
   ("Liberar por tempo de serviço e necessidade civil. (estabilidade +2%, dívida +1, apoio trabalhista +3)", "Release by length of service and civilian need. (stability +2%, debt +1, labour support +3)",
    [stab(0.02), var("debt_burden", 1), var("labour_support", 3), flag("fast_demobilisation")], 60),
   ("Manter as unidades juntas e liberar devagar. (estabilidade -1%, apoio trabalhista -3, dívida -1)", "Keep the units together and release slowly. (stability -1%, labour support -3, debt -1)",
    [stab(-0.01), var("labour_support", -3), var("debt_burden", -1), flag("slow_demobilisation")], 40)]),
 dict(id=6, mode="mtth", days=3, once=True,
  trigger="date > 1918.3.20 date < 1918.6.1 has_war_with = GER",
  t=("A ofensiva de primavera alemã", "The German Spring Offensive"),
  d=("Em 21 de março de 1918 os alemães atacam na Picardia com nevoeiro e bombardeio de gás. A Quinta Exército cede, e a linha aliada corre o risco de se partir entre britânicos e franceses.",
     "On 21 March 1918 the Germans strike in Picardy under fog and a gas bombardment. The Fifth Army gives way, and the Allied line risks splitting between British and French."),
  options=[
   ("Trocar terreno por tempo. (-10 de poder político, experiência de exército +6; apoio à guerra -0,5% com o plano de defesa, senão -2%)", "Trade ground for time. (-10 political power, army experience +6; war support -0.5% with the defence plan, otherwise -2%)",
    [pp(-10), army_xp(6), "if = { limit = { has_country_flag = ENG_ww1_spring_defence_plan } add_war_support = -0.005 }",
     "else = { add_war_support = -0.02 }"], 65),
   ("Manter a zona avançada a qualquer custo. (experiência de exército +3, apoio à guerra -3%, dívida +1)", "Hold the forward zone at any cost. (army experience +3, war support -3%, debt +1)",
    [army_xp(3), war_support(-0.03), var("debt_burden", 1)], 35)]),
 dict(id=7, mode="trigger",
  t=("Amiens, o dia negro", "Amiens, the Black Day"),
  d=("Em 8 de agosto de 1918 tanques, canadenses e australianos rompem a linha alemã sob a neblina. Ludendorff chama o dia de o dia negro do exército alemão. Haig e Foch precisam decidir se aprofundam o avanço.",
     "On 8 August 1918 tanks, Canadians and Australians break the German line under fog. Ludendorff calls it the black day of the German army. Haig and Foch must decide whether to deepen the advance."),
  options=[
   ("Pressionar em toda a frente. (experiência de exército +8, apoio à guerra +3%, dívida +1)", "Press along the whole front. (army experience +8, war support +3%, debt +1)",
    [army_xp(8), war_support(0.03), var("debt_burden", 1),
     "if = { limit = { country_exists = GER has_war_with = GER } GER = { country_event = { id = ww1_britain_mil.12 } } }"], 60),
   ("Parar para trazer as armas. (experiência de exército +4, +10 de poder político)", "Pause to bring up the guns. (army experience +4, +10 political power)",
    [army_xp(4), pp(10)], 40)]),
 dict(id=8, mode="mtth", days=20, once=True,
  trigger="date > 1919.1.1 date < 1919.6.1 has_country_flag = ENG_ww1_slow_demobilisation",
  t=("Os motins de Calais", "The Calais Mutinies"),
  d=("Soldados cansados de esperar em Folkestone e Calais se recusam a embarcar de volta à França e elegem comitês. Os generais temem uma revolução, e Churchill, no Ministério da Guerra, prepara uma resposta.",
     "Soldiers weary of waiting at Folkestone and Calais refuse to re-embark for France and elect committees. The generals fear a revolution, and Churchill, at the War Office, prepares a response."),
  options=[
   ("Acelerar as liberações imediatamente. (estabilidade +1%, dívida +1)", "Speed up the releases at once. (stability +1%, debt +1)",
    [stab(0.01), var("debt_burden", 1)], 65),
   ("Enviar unidades leais para restabelecer a ordem. (estabilidade -2%, +10 de poder político, apoio trabalhista -4)", "Send loyal units to restore order. (stability -2%, +10 political power, labour support -4)",
    [stab(-0.02), pp(10), var("labour_support", -4)], 35)]),
 dict(id=10, mode="trigger", trigger_full="tag = FRA",
  t=("Os ingleses chegam", "The British Arrive"),
  d=("Desembarcam em Boulogne e Le Havre os primeiros batalhões da Força Expedicionária Britânica. A multidão aplaude os soldados cáqui, e Paris recupera a esperança de que não estará só.",
     "The first battalions of the British Expeditionary Force land at Boulogne and Le Havre. The crowd cheers the khaki soldiers, and Paris recovers the hope that it will not stand alone."),
  options=[
   ("Receber a Força Expedicionária. (apoio à guerra +2%, estabilidade +1%)", "Welcome the Expeditionary Force. (war support +2%, stability +1%)",
    ["add_war_support = 0.02", stab(0.01)], 100)]),
 dict(id=11, mode="trigger", trigger_full="tag = TUR",
  t=("A frota aliada no estreito", "The Allied Fleet at the Straits"),
  d=("Navios aliados bombardeiam as fortalezas de Dardanelos. O governo em Constantinopla tem poucos canhões e pouca munição, mas o país se levanta: a ameaça contra a capital une até os adversários.",
     "Allied ships bombard the Dardanelles forts. The government in Constantinople has few guns and little ammunition, but the country rallies: the threat to the capital unites even its opponents."),
  options=[
   ("Defender os estreitos a qualquer custo. (apoio à guerra +3%, estabilidade +2%)", "Defend the Straits at any cost. (war support +3%, stability +2%)",
    ["add_war_support = 0.03", stab(0.02)], 100)]),
 dict(id=12, mode="trigger", trigger_full="tag = GER",
  t=("O dia negro do exército alemão", "The Black Day of the German Army"),
  d=("Divisões inteiras se rendem com poucos tiros. Ludendorff diz ao Kaiser que a guerra não pode mais ser ganha pela força. O estado-maior precisa decidir como falar disso ao país.",
     "Whole divisions surrender with few shots. Ludendorff tells the Kaiser that the war can no longer be won by force. The staff must decide how to tell the country."),
  options=[
   ("Ordenar que as tropas resistam. (apoio à guerra -2%, estabilidade -1%)", "Order the troops to hold on. (war support -2%, stability -1%)",
    ["add_war_support = -0.02", stab(-0.01)], 65),
   ("Procurar o chanceler para pedir o armistício. (apoio à guerra -3%, estabilidade -2%)", "Approach the Chancellor to seek an armistice. (war support -3%, stability -2%)",
    ["add_war_support = -0.03", stab(-0.02)], 35)]),
 dict(id=13, mode="trigger", trigger_full="NOT = { tag = ENG } is_in_faction_with = ENG",
  t=("Oficiais de ligação britânicos", "British Liaison Officers"),
  d=("Londres oferece enviar oficiais de estado-maior ao quartel-general aliado para coordenar planos, suprimentos e transporte. Os comandantes locais ficam divididos entre a utilidade e o orgulho.",
     "London offers to send staff officers to Allied headquarters to coordinate plans, supplies and transport. Local commanders are divided between usefulness and pride."),
  options=[
   ("Aceitar os oficiais. (experiência de exército +2; a experiência de exército britânica +2)", "Accept the officers. (army experience +2; British army experience +2)",
    [army_xp(2), "FROM = { army_experience = 2 }"], 70),
   ("Recusar. (sem efeitos)", "Decline. (no effects)", [], 30)]),
]

DECISIONS = [
 dict(id="ENG_ww1_staff_college_course",
  lines=["  visible = { has_country_flag = ENG_ww1_combined_arms }",
         "  available = { has_war = yes has_capitulated = no }",
         "  cost = 25 days_re_enable = 365",
         "  complete_effect = { army_experience = 5 add_to_variable = { ww1_britain_debt_burden = 1 } }",
         "  ai_will_do = { base = 1 }"],
  pt=("Curso do Colégio de Estado-Maior", "Gasta 25 de poder político. Em guerra, ganha 5 de experiência de exército e a dívida sobe 1. Disponível uma vez por ano, depois dos cursos de armas combinadas."),
  en=("Staff College Course", "Spend 25 political power. At war, it grants 5 army experience and debt rises by 1. Available once a year after the combined arms courses.")),
 dict(id="ENG_ww1_send_liaison_officers",
  lines=["  visible = { has_country_flag = ENG_ww1_bef_deployed }",
         "  available = { has_war = yes has_capitulated = no }",
         "  cost = 20 days_re_enable = 240",
         "  complete_effect = {",
         "   every_other_country = { limit = { is_in_faction_with = ROOT } country_event = { id = ww1_britain_mil.13 } }",
         "  }",
         "  ai_will_do = { base = 1 }"],
  pt=("Enviar oficiais de ligação", "Gasta 20 de poder político. Em guerra, oferece oficiais de estado-maior a cada aliado da facção, que decide se aceita. Quem aceita e o Reino Unido ganham 2 de experiência de exército. Exige o plano de implantação da Força Expedicionária."),
  en=("Send Liaison Officers", "Spend 20 political power. At war, offers staff officers to each ally in the faction, who decides whether to accept. Whoever accepts and Britain gain 2 army experience. Requires the BEF deployment plan.")),
]
