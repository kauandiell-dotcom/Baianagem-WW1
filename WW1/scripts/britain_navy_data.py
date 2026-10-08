"""UK content, wing 4 (Navy and Aviation): rewards, descriptions, events, ideas, decisions.

Namespace ww1_britain_nav. Partner events (10-12) run in the partner's scope: ROOT = partner, FROM = ENG.
Rewards stay small and traded-off: no free ships, aircraft or equipment; research bonuses are one-use.
Already-finished focuses (admiralty survey, estimates, dreadnoughts, fleet maintenance, convoys, pilot
instruction, RAF) only had the stub reward; every one of the 40 is implemented here.
"""
from britain_politics_data import var, flag, idea, remove_idea, pp, stab, navy_xp

NS = "ww1_britain_nav"
CATEGORY = "ENG_ww1_services_policy"
CATEGORY_DEF = True
PEACE_CLEANUP = ["ENG_ww1_convoy_system"]


def ev(n, days=0):
    extra = f" days = {days}" if days else ""
    return f"country_event = {{ id = {NS}.{n}{extra} }}"


def to(tag, n):
    return f"if = {{ limit = {{ country_exists = {tag} }} {tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}"


def to_enemy(tag, n):
    return (f"if = {{ limit = {{ country_exists = {tag} has_war_with = {tag} }} "
            f"{tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}")


def to_ally(tag, n):
    return (f"if = {{ limit = {{ country_exists = {tag} is_in_faction_with = {tag} }} "
            f"{tag} = {{ country_event = {{ id = {NS}.{n} }} }} }}")


def air_xp(n):
    return f"air_experience = {n}"


def army_xp(n):
    return f"army_experience = {n}"


def tech(name, category, bonus=0.25):
    # One use, no free technology: a modest research-speed bonus on one category.
    return f"add_tech_bonus = {{ name = ENG_ww1_{name} bonus = {bonus} uses = 1 category = {category} }}"


def build(state, kind, slots=1):
    return (f"{state} = {{ add_extra_state_shared_building_slots = {slots} "
            f"add_building_construction = {{ type = {kind} level = 1 }} }}")


FOCI = {
# ------------------------------------------------------------------ naval (20)
"admiralty_fleet_survey": (
    ["remove_ideas = ENG_two_power_standard", pp(15), idea("admiralty_war_staff"), flag("fleet_survey")],
    "O Almirantado mede a prontidão da frota e cria o Estado-Maior de Guerra Naval em 1912. Ganha 15 de poder político e a instituição Estado-Maior Naval (+10% de ganho de XP naval).",
    "The Admiralty measures fleet readiness and establishes the Admiralty War Staff in 1912. Grants 15 political power and the Admiralty War Staff institution (+10% naval XP gain)."),
"the_naval_estimates": (
    [build(132, "dockyard"), var("debt_burden", 1), navy_xp(5), pp(10), flag("naval_estimates")],
    "O Almirantado amplia os estaleiros de Birkenhead e Cammell Laird para a corrida de couraçados. Enfileira 1 estaleiro no noroeste, ganha 5 de experiência naval e 10 de poder político; a dívida sobe 1.",
    "The Admiralty expands the Birkenhead and Cammell Laird yards for the battleship race. Queues 1 dockyard in the North-West, grants 5 naval experience and 10 political power; debt rises by 1."),
"dreadnought_construction_planning": (
    [build(133, "dockyard"), tech("dreadnought_construction_planning", "bb_tech"), var("debt_burden", 1), flag("super_dreadnoughts")],
    "A classe Queen Elizabeth adota canhões de 15 polegadas e óleo nos estaleiros do Clyde. Enfileira 1 estaleiro em Strathclyde e bônus de 25% em couraçados; dívida sobe 1.",
    "The Queen Elizabeth class adopts 15-inch guns and oil firing in the Clyde yards. Queues 1 dockyard in Strathclyde, grants a 25% battleship research bonus; debt rises by 1."),
"battlecruiser_squadron_planning": (
    [build(131, "dockyard"), tech("battlecruiser_squadron_planning", "bc_tech"), navy_xp(5), flag("battlecruiser_squadron")],
    "Beatty comanda uma esquadra rápida produzida nos estaleiros do Tyne. Enfileira 1 estaleiro no norte da Inglaterra, ganha 5 de experiência naval e bônus de 25% em cruzadores de batalha.",
    "Beatty commands a fast squadron built in the Tyne yards. Queues 1 dockyard in Northern England, grants 5 naval experience and a 25% battlecruiser research bonus."),
"destroyer_flotilla_planning": (
    [build(119, "dockyard"), tech("destroyer_flotilla_planning", "dd_tech"), navy_xp(5), flag("destroyer_flotillas")],
    "Harland & Wolff e estaleiros em Belfast recebem encomendas para contratorpedeiros. Enfileira 1 estaleiro na Irlanda do Norte, ganha 5 de experiência naval e bônus de 25% em contratorpedeiros.",
    "Harland & Wolff and yards in Belfast receive orders for destroyers. It queues 1 dockyard in Northern Ireland, grants 5 naval experience and a 25% research bonus on destroyers."),
"submarine_service_development": (
    [tech("submarine_service_development", "ss_tech"), navy_xp(5), pp(10), flag("submarine_service")],
    "Os submarinos classe E são pensados para a defesa costeira e a vigia da baía alemã. Ganha 5 de experiência naval, 10 de poder político e bônus de pesquisa de 25% em submarinos.",
    "The E-class submarines are meant for coastal defence and watching the German Bight. Grants 5 naval experience, 10 political power and a 25% research bonus on submarines."),
"naval_gunnery_calibration": (
    [tech("naval_gunnery_calibration", "naval_artillery"), navy_xp(10), flag("fire_control_tables")],
    "As mesas de controle de fogo de Dreyer e Pollen prometem disparos precisos a longa distância. Ganha 10 de experiência naval e bônus de pesquisa de 25% em artilharia naval.",
    "The fire-control tables of Dreyer and Pollen promise accurate long-range fire. Grants 10 naval experience and a 25% research bonus on naval artillery."),
"the_north_sea_watch": (
    [remove_idea("admiralty_war_staff"), idea("northern_patrol"), navy_xp(5), flag("north_sea_watch")],
    "Cruzadores e navios armados patrulham entre a Escócia e a Noruega. Substitui o estado-maior inicial pela instituição Patrulha do Norte (detecção naval +10%) e 5 de experiência naval.",
    "Cruisers and armed merchant vessels patrol between Scotland and Norway. Replaces initial staff with the Northern Patrol institution (naval detection +10%) and 5 naval experience."),
"grand_fleet_maintenance": (
    [remove_idea("northern_patrol"), idea("grand_fleet_anchorage"), "120 = { add_building_construction = { type = coastal_bunker level = 1 } }", "120 = { add_building_construction = { type = naval_base level = 1 province = 11064 } }", "121 = { add_building_construction = { type = naval_base level = 1 province = 6300 } }", var("debt_burden", 1), flag("scapa_flow")],
    "Scapa Flow e Rosyth ganham baterias costeiras e bases navais. Substitui patrulhas pela instituição Fundeadouros da Grande Frota (reparo naval +10%); dívida sobe 1.",
    "Scapa Flow and Rosyth receive coastal batteries and expanded naval bases. Replaces patrols with Grand Fleet Anchorages institution (naval repair +10%); debt rises by 1."),
"merchant_shipping_register": (
    [navy_xp(5), stab(0.02), pp(15), flag("merchant_register")],
    "O registro do Lloyd's lista navios mercantes que podem virar transportes e escoltas. Ganha 5 de experiência naval, 2% de estabilidade e 15 de poder político.",
    "The Lloyd's register lists merchant ships adaptable as transports and escorts. Grants 5 naval experience, 2% stability and 15 political power."),
"maritime_blockade_coordination": (
    [navy_xp(5), pp(10), flag("blockade"), to_enemy("GER", 10), to("USA", 11)],
    "O Bloqueio da Alemanha sufoca o comércio imperial alemão. Ganha 5 de experiência naval e 10 de poder político; a Alemanha sente a fome e os EUA debatem protestos.",
    "The blockade of Germany chokes German trade. Grants 5 naval experience and 10 political power; Germany feels hunger and the US considers protests."),
"hydrophone_trials": (
    [tech("hydrophone_trials", "asw_tech"), navy_xp(5), flag("hydrophones")],
    "A estação de Hawkcraig testa microfones submersos para detectar motores submarinos. Ganha 5 de experiência naval e bônus de pesquisa de 25% em guerra antissubmarina.",
    "The Hawkcraig station tests underwater microphones to detect submarine engines. Grants 5 naval experience and a 25% research bonus on anti-submarine warfare."),
"depth_charge_trials": (
    [tech("depth_charge_trials", "dd_tech"), navy_xp(5), flag("depth_charges")],
    "A carga de profundidade tipo D é lançada por contratorpedeiros sobre áreas de mergulho. Ganha 5 de experiência naval e bônus de pesquisa de 25% em contratorpedeiros.",
    "The Type D depth charge is dropped by destroyers over dive zones. Grants 5 naval experience and a 25% research bonus on destroyers."),
"convoy_system_organisation": (
    [ev(2)],
    "Em 1917 os submarinos afundam um navio em cada quatro que saem para o mar. Lloyd George pressiona o Almirantado, que resiste a formar comboios. Dispara o debate do comboio: a escolha muda a guerra no Atlântico.",
    "In 1917 submarines sink one in four ships that put to sea. Lloyd George presses the Admiralty, which resists forming convoys. It triggers the convoy debate: the choice changes the war in the Atlantic."),
"escort_refit_contracts": (
    [build(127, "dockyard"), tech("escort_refit_contracts", "dd_tech"), var("debt_burden", 1), navy_xp(5),
     "if = { limit = { has_idea = ENG_ww1_convoy_system } navy_experience = 5 }"],
    "Estaleiros em Devonport e Portsmouth convertem embarcações para escolta. Enfileira 1 estaleiro no sudeste, bônus de 25% em contratorpedeiros e dívida +1; ganha até 10 de experiência naval.",
    "Yards in Devonport and Portsmouth convert vessels for escort duty. Queues 1 dockyard in the South-East, a 25% destroyer bonus and debt rises by 1; grants up to 10 naval experience."),
"naval_signals_and_direction_finding": (
    [pp(15), tech("naval_signals_and_direction_finding", "decryption_tech"), flag("direction_finding")],
    "Estações de radiogoniometria triangulam sinais de submarinos alemães. Ganha 15 de poder político e bônus de pesquisa de 25% em decifração.",
    "Radio direction-finding stations triangulate German submarine signals. Grants 15 political power and a 25% research bonus on decryption."),
"mediterranean_convoy_liaison": (
    [navy_xp(10), pp(10), flag("med_liaison"), to_ally("JAP", 12), to_ally("ITA", 12), to_ally("FRA", 12), to_ally("GRE", 12)],
    "Marinhas aliadas compartilham a escolta no Mediterrâneo contra submarinos. Ganha 10 de experiência naval, 10 de poder político e propõe a cooperação aos aliados.",
    "Allied navies share escort duties in the Mediterranean against submarines. Grants 10 naval experience, 10 political power and proposes cooperation to allies."),
"the_postwar_fleet_review": (
    [remove_idea("grand_fleet_anchorage"), pp(20), navy_xp(5), flag("postwar_fleet_review")],
    "Com o armistício, o Almirantado faz a revista da frota, desmobilizando fundeadouros de guerra. Ganha 20 de poder político e 5 de experiência naval.",
    "With the armistice the Admiralty conducts the fleet review, standing down wartime anchorages. Grants 20 political power and 5 naval experience."),
"naval_budget_retrenchment": (
    [var("debt_burden", -3), pp(20), stab(0.02), flag("naval_retrenchment")],
    "O Tesouro corta o orçamento naval, aposenta couraçados velhos e cancela encomendas. A dívida cai 3; ganha 20 de poder político e 2% de estabilidade. Exclui as lições técnicas.",
    "The Treasury cuts the naval budget, retires old battleships and cancels orders. Debt falls by 3; it grants 20 political power and 2% stability. Excludes the technical lessons."),
"naval_technical_lessons": (
    [navy_xp(15), tech("naval_technical_lessons", "naval_equipment"), var("debt_burden", 1), flag("naval_lessons")],
    "O Almirantado estuda Jutland e a guerra submarina: munição com menos risco de explosão, blindagem de convés, controle de fogo. A dívida sobe 1; ganha 15 de experiência naval e bônus de pesquisa de 25% em equipamento naval (uso único). Exclui o corte orçamentário.",
    "The Admiralty studies Jutland and the submarine war: safer magazines, deck armour, fire control. Debt rises by 1; it grants 15 naval experience and a one-use 25% research bonus on naval equipment. Excludes the budget cuts."),
# ------------------------------------------------------------------ aviation (20)
"the_air_battalion_experiments": (
    [tech("the_air_battalion_experiments", "air_equipment"), air_xp(5), flag("air_battalion")],
    "O Batalhão Aéreo dos Engenheiros Reais testa dirigíveis e aeroplanos em Larkhill. Ganha 5 de experiência aérea e bônus de pesquisa de 25% em equipamento aéreo.",
    "The Air Battalion of the Royal Engineers tests airships and aeroplanes at Larkhill. Grants 5 air experience and a 25% research bonus on air equipment."),
"royal_flying_corps_organisation": (
    ["remove_ideas = ENG_two_power_standard", idea("royal_flying_corps"), air_xp(5), flag("royal_flying_corps")],
    "O Corpo Aéreo Real nasce em 1912 com a Escola Central de Voo em Upavon. Ganha a instituição Corpo Aéreo Real (+10% de ganho de XP aérea) e 5 de experiência aérea.",
    "The Royal Flying Corps is formed in 1912 with the Central Flying School at Upavon. Grants the Royal Flying Corps institution (+10% air XP gain) and 5 air experience."),
"military_pilot_instruction": (
    [tech("military_pilot_instruction", "air_doctrine", 0.25), air_xp(15), pp(10), flag("pilot_instruction")],
    "Pilotos aprendem navegação e tiro aéreo com manuais de instrução formais. Ganha 15 de experiência aérea, 10 de poder político e bônus de 25% em doutrina aérea.",
    "Pilots learn air navigation and gunnery through formal instruction manuals. Grants 15 air experience, 10 political power and a 25% air doctrine bonus."),
"aerial_reconnaissance_reports": (
    [tech("aerial_reconnaissance_reports", "recon_tech", 0.25), army_xp(5), air_xp(5), flag("aerial_reports")],
    "Relatórios de reconhecimento aéreo abastecem o planejamento do Estado-Maior. Ganha 5 de experiência de exército, 5 de experiência aérea e bônus de 25% em reconhecimento.",
    "Aerial reconnaissance reports inform General Staff operational planning. Grants 5 army experience, 5 air experience and a 25% reconnaissance bonus."),
"royal_naval_air_service_organisation": (
    [tech("royal_naval_air_service_organisation", "air_equipment", 0.25), navy_xp(5), air_xp(5), flag("rnas")],
    "O Serviço Aéreo Naval Real desenvolve hidroaviões e dirigíveis costeiros. Ganha 5 de experiência naval, 5 de experiência aérea e bônus de 25% em equipamentos aéreos.",
    "The Royal Naval Air Service develops seaplanes and coastal patrol airships. Grants 5 naval experience, 5 air experience and a 25% air equipment bonus."),
"wireless_and_aircraft_observation": (
    [tech("wireless_and_aircraft_observation", "electronics"), air_xp(5)],
    "Rádios de faísca transmitem dados de tiro de artilharia em tempo real. Ganha 5 de experiência aérea e bônus de pesquisa de 25% em eletrônica.",
    "Spark wireless transmitters relay artillery spotting data in real time. Grants 5 air experience and a 25% research bonus on electronics."),
"bristol_scout_trials": (
    [tech("bristol_scout_trials", "light_air"), air_xp(5), flag("bristol_scout")],
    "O Bristol Scout é a primeira aeronave britânica projetada para caçar no ar. Ganha 5 de experiência aérea e bônus de pesquisa de 25% em aviação leve.",
    "The Bristol Scout is the first British aircraft designed for aerial combat. Grants 5 air experience and a 25% research bonus on light aircraft."),
"naval_seaplane_stations": (
    ["125 = { add_building_construction = { type = naval_base level = 1 } }", navy_xp(5), air_xp(5), flag("seaplane_stations")],
    "Estações de hidroaviões em Calshot e Felixstowe vigiam o Mar do Norte. Adiciona 1 nível de base naval em East Anglia, ganha 5 de experiência naval e 5 aérea.",
    "Seaplane stations at Calshot and Felixstowe patrol the North Sea. Adds 1 naval base level in East Anglia, grants 5 naval experience and 5 air experience."),
"aircraft_production_contracts": (
    [tech("aircraft_production_contracts", "air_equipment"), var("debt_burden", 1), pp(10), air_xp(5)],
    "Contratos com Sopwith, Vickers e Bristol multiplicam a fabricação aeronáutica. Ganha 10 de poder político, 5 de experiência aérea e bônus de 25% em aviões; dívida sobe 1.",
    "Contracts with Sopwith, Vickers and Bristol multiply airframe output. Grants 10 political power, 5 air experience and a 25% aircraft bonus; debt rises by 1."),
"fighter_squadron_instruction": (
    [air_xp(15), tech("fighter_squadron_instruction", "light_fighter"), flag("fighter_instruction")],
    "Esquadrões de caça aprendem formações de voo e ataques em grupo coordenados. Ganha 15 de experiência aérea e bônus de pesquisa de 25% em caças leves.",
    "Fighter squadrons master tight flight formations and coordinated group attacks. Grants 15 air experience and a 25% research bonus on light fighters."),
"artillery_spotting_liaison": (
    [tech("artillery_spotting_liaison", "artillery", 0.25), army_xp(5), air_xp(5), flag("artillery_spotting")],
    "Observadores aéreos e baterias de artilharia sincronizam zonas de bombardeio. Ganha 5 de experiência de exército, 5 aérea e bônus de 25% em artilharia.",
    "Aerial observers and artillery batteries synchronise barrage sectors. Grants 5 army experience, 5 air experience and a 25% artillery bonus."),
"night_flying_experiments": (
    [tech("night_flying_experiments", "air_equipment", 0.25), air_xp(10), pp(10), flag("night_flying")],
    "Pilotos treinam voos noturnos e pousos com holofotes para combater Zeppelins. Ganha 10 de experiência aérea, 10 de poder político e bônus de 25% em equipamentos.",
    "Pilots train in night flying and flare landings to intercept Zeppelins. Grants 10 air experience, 10 political power and a 25% air equipment bonus."),
"bomber_range_experiments": (
    [tech("bomber_range_experiments", "tactical_bomber"), air_xp(5), flag("bomber_range")],
    "Voos de longo curso com tanques ampliados preparam bombardeios estratégicos. Ganha 5 de experiência aérea e bônus de pesquisa de 25% em bombardeiros táticos.",
    "Long-range flights with enlarged fuel tanks prepare strategic bombing missions. Grants 5 air experience and a 25% bonus on tactical bombers."),
"aircraft_engine_reliability": (
    [remove_idea("royal_flying_corps"), idea("engine_reliability"), var("debt_burden", 1), flag("engine_reliability")],
    "Motores Rolls-Royce Eagle e Le Rhône recebem peças padronizadas. Substitui o corpo inicial pela instituição Motores Confiáveis (acidentes aéreos -15%); dívida sobe 1.",
    "Rolls-Royce Eagle and Le Rhône engines receive standardised parts. Replaces early corps with Reliable Engines institution (air accidents -15%); debt rises by 1."),
"home_air_defence_coordination": (
    [remove_idea("engine_reliability"), remove_idea("royal_flying_corps"), idea("home_air_defence"), pp(10), flag("home_air_defence")],
    "Canhões AA, holofotes e patrulhas protegem Londres contra Zeppelins. Substitui melhorias de motores pela instituição Defesa Aérea Doméstica (estabilidade +1%) e 10 de poder político.",
    "AA guns, searchlights and patrols protect London against Zeppelins. Replaces engine improvements with the Home Air Defence institution (stability +1%) and 10 political power."),
"the_independent_air_service_debate": (
    [ev(6)],
    "Depois dos ataques dos Gotha a Londres, o general Smuts investiga a defesa aérea. A questão é se o Exército e a Marinha continuam com serviços aéreos separados ou se nasce uma força independente. Dispara o Relatório Smuts.",
    "After the Gotha raids on London, General Smuts investigates air defence. The question is whether the Army and the Navy keep separate air services or an independent force is born. It triggers the Smuts Report."),
"royal_air_force_unification": (
    ["remove_ideas = ENG_ww1_royal_flying_corps", remove_idea("home_air_defence"), remove_idea("engine_reliability"), idea("royal_air_force"), flag("raf_formed"),
     "if = { limit = { has_country_flag = ENG_ww1_air_independent } air_experience = 15 add_political_power = -10 }",
     "else = { air_experience = 5 add_political_power = 10 }"],
    "Em 1º de abril de 1918 nasce a Força Aérea Real, substituindo a defesa aérea provisória. Instituição Força Aérea Real (+15% de XP aérea, +5% de eficiência de missão).",
    "On 1 April 1918 the Royal Air Force is born, replacing provisional air defences. Royal Air Force institution (+15% air XP, +5% mission efficiency)."),
"postwar_aircraft_demobilisation": (
    [remove_idea("royal_air_force"), var("debt_burden", -2), pp(15), stab(0.01), flag("aircraft_demobilised")],
    "A Companhia de Alienação de Aeronaves vende excedentes, desmobilizando a força de guerra. A dívida cai 2; ganha 15 de poder político e 1% de estabilidade.",
    "The Aircraft Disposal Company sells surpluses, standing down wartime forces. Debt falls by 2; it grants 15 political power and 1% stability."),
"civil_aviation_research": (
    [tech("civil_aviation_research", "air_equipment"), stab(0.02), var("debt_burden", -1), flag("civil_aviation")],
    "O Comitê de Transporte Aéreo Civil estuda rotas aéreas imperiais. A dívida cai 1; ganha 2% de estabilidade e bônus de pesquisa de 25% em equipamento aéreo. Exclui a força militar permanente.",
    "The Civil Air Transport Committee studies imperial civil flight routes. Debt falls by 1; grants 2% stability and a 25% air equipment bonus. Excludes permanent military establishment."),
"a_sustainable_air_establishment": (
    [remove_idea("royal_air_force"), air_xp(15), pp(20), var("debt_burden", 1), flag("trenchard_memorandum")],
    "O memorando de Trenchard define uma RAF pequena, permanente e altamente qualificada. Remove instituições de guerra, ganha 15 de experiência aérea e 20 de poder político; dívida sobe 1. Exclui a pesquisa civil.",
    "Trenchard's memorandum establishes a small, permanent, highly trained RAF. Removes wartime institutions, grants 15 air experience and 20 political power; debt rises by 1. Excludes civil research."),
}

EXCLUSIVE = [("naval_budget_retrenchment", "naval_technical_lessons"),
             ("civil_aviation_research", "a_sustainable_air_establishment")]

# name -> (modifier, name_pt, name_en, desc_pt, desc_en, picture)
IDEAS = {
 "admiralty_war_staff": ("experience_gain_navy_factor = 0.1", "Estado-Maior Naval", "Admiralty War Staff",
   "Oficiais de estado-maior planejam a guerra no mar, e não só a próxima manobra.", "Staff officers plan the war at sea, not just the next manoeuvre.", ""),
 "northern_patrol": ("naval_detection = 0.1", "Patrulha do Norte", "Northern Patrol",
   "Cruzadores velhos e navios mercantes armados vigiam o acesso ao Atlântico.", "Old cruisers and armed merchant ships watch the gateway to the Atlantic.", ""),
 "grand_fleet_anchorage": ("repair_speed_factor = 0.1", "Fundeadouros da Grande Frota", "Grand Fleet Anchorages",
   "Scapa Flow e Rosyth dão abrigo, carvão e oficinas à Grande Frota.", "Scapa Flow and Rosyth give the Grand Fleet shelter, coal and workshops.", ""),
 "convoy_system": ("convoy_escort_efficiency = 0.15 industrial_capacity_dockyard = -0.05", "Sistema de Comboios", "Convoy System",
   "Navios mercantes viajam em grupo sob escolta. Escolta mais eficaz, mas os estaleiros gastam capacidade em escoltas.", "Merchant ships travel in groups under escort. Escorts are more effective, but the yards spend capacity on escort vessels.", ""),
 "royal_flying_corps": ("experience_gain_air_factor = 0.1", "Corpo Aéreo Real", "Royal Flying Corps",
   "Uma arma nova, de madeira e pano, que aprende a cada voo.", "A new arm of wood and fabric, learning on every flight.", ""),
 "engine_reliability": ("air_accidents_factor = -0.15", "Motores Confiáveis", "Reliable Engines",
   "Peças padronizadas e oficinas de campanha reduzem falhas de motor.", "Standard parts and field workshops reduce engine failures.", ""),
 "home_air_defence": ("air_defence_factor = 0.1 stability_factor = 0.01", "Defesa Aérea Doméstica", "Home Air Defence",
   "Guardas, holofotes e canhões protegem Londres. A população dorme um pouco mais tranquila.", "Guns, searchlights and watchers protect London. The public sleeps a little easier.", ""),
 "royal_air_force": ("experience_gain_air_factor = 0.15 air_mission_efficiency = 0.05", "Força Aérea Real", "Royal Air Force",
   "O primeiro serviço aéreo independente do mundo, com estado-maior, escolas e orçamento próprios.", "The first independent air service in the world, with its own staff, schools and budget.", ""),
}

# option = (name_pt, name_en, effects, ai). Partner events: trigger_full replaces the ENG default.
EVENTS = [
 dict(id=2, mode="trigger",
  t=("O debate do comboio", "The Convoy Debate"),
  d=("Em abril de 1917 os submarinos afundam quase um em cada quatro navios que deixam as ilhas. O Almirantado teme que comboios sejam alvos fáceis e lentos, mas Lloyd George já ameaça ir pessoalmente à sala de operações.",
     "In April 1917 submarines sink nearly one in four ships leaving the islands. The Admiralty fears convoys would be slow, easy targets, but Lloyd George already threatens to walk into the operations room himself."),
  options=[
   ("Adotar o sistema de comboios. (-10 de poder político; escolta +15%, capacidade de estaleiro -5%)", "Adopt the convoy system. (-10 political power; escort efficiency +15%, dockyard capacity -5%)",
    [pp(-10), idea("convoy_system"), flag("convoy_adopted")], 75),
   ("Manter as patrulhas. (+10 de poder político, experiência naval +2, dívida +2)", "Keep the patrols. (+10 political power, naval experience +2, debt +2)",
    [pp(10), navy_xp(2), var("debt_burden", 2), flag("convoy_rejected")], 25)]),
 dict(id=3, mode="mtth", days=20, once=True,
  trigger="date > 1916.5.29 date < 1917.1.1 has_war_with = GER",
  t=("A Batalha da Jutlândia", "The Battle of Jutland"),
  d=("A Grande Frota e a Frota de Alto-Mar se chocam ao largo da Dinamarca. Os britânicos perdem mais navios, mas a frota alemã volta ao porto e nunca mais busca a batalha decisiva. O comunicado do Almirantado soa como derrota.",
     "The Grand Fleet and the High Seas Fleet collide off Denmark. The British lose more ships, yet the German fleet returns to port and never again seeks a decisive battle. The Admiralty communique reads like a defeat."),
  options=[
   ("Publicar o relatório sóbrio de Jellicoe. (experiência naval +5, apoio à guerra -1%)", "Publish Jellicoe's sober report. (naval experience +5, war support -1%)",
    [navy_xp(5), "add_war_support = -0.01", flag("jutland_honest")], 50),
   ("Destacar a fuga alemã para o porto. (+15 de poder político, apoio à guerra +1%)", "Stress the German flight to port. (+15 political power, war support +1%)",
    [pp(15), "add_war_support = 0.01", flag("jutland_spin")], 50)]),
 dict(id=4, mode="mtth", days=30, once=True,
  trigger="date > 1915.1.18 date < 1916.9.1 has_war_with = GER",
  t=("Zeppelins sobre a Inglaterra", "Zeppelins over England"),
  d=("Dirigíveis alemães lançam bombas em Great Yarmouth e King's Lynn e depois em Londres. Há poucas mortes, mas o pânico é grande. Os jornais perguntam onde estão a Marinha e o Exército.",
     "German airships drop bombs on Great Yarmouth and King's Lynn and later on London. Few die, but panic is wide. The newspapers ask where the Navy and the Army are."),
  options=[
   ("Ordenar o apagão e confiar nos canhões. (apoio à guerra -1%, estabilidade -0,5%)", "Order the blackout and trust the guns. (war support -1%, stability -0.5%)",
    ["add_war_support = -0.01", stab(-0.005)], 50),
   ("Chamar esquadrões do continente para a defesa. (-10 de poder político, experiência aérea +2)", "Recall squadrons from the Continent for home defence. (-10 political power, air experience +2)",
    [pp(-10), air_xp(2), flag("home_squadrons")], 50)]),
 dict(id=5, mode="mtth", days=20, once=True,
  trigger="date > 1917.6.12 date < 1918.12.1 has_war_with = GER",
  t=("Os ataques dos Gotha", "The Gotha Raids"),
  d=("Bombardeiros Gotha atacam Londres em pleno dia, em junho de 1917, e matam mais de cem pessoas. A fúria pública é enorme e as fábricas pedem proteção. O gabinete exige respostas.",
     "Gotha bombers strike London in broad daylight in June 1917, killing over a hundred people. Public fury is immense and the factories ask for protection. The cabinet demands answers."),
  options=[
   ("Reorganizar a defesa de Londres. (-15 de poder político; o apoio à guerra cai só 0,5% se há defesa doméstica, senão 2%)", "Reorganise the defence of London. (-15 political power; war support falls only 0.5% with home air defence, otherwise 2%)",
    [pp(-15), "if = { limit = { has_country_flag = ENG_ww1_home_air_defence } add_war_support = -0.005 }",
     "else = { add_war_support = -0.02 }"], 60),
   ("Nomear o general Smuts para uma investigação. (-10 de poder político)", "Appoint General Smuts to investigate. (-10 political power)",
    [pp(-10), flag("smuts_commission")], 40)]),
 dict(id=6, mode="trigger",
  t=("O Relatório Smuts", "The Smuts Report"),
  d=("Smuts conclui que a guerra aérea será, no futuro, uma operação independente do mar e da terra. O Exército e a Marinha resistem a perder seus aviões, e o Conselho Aéreo precisa de uma decisão.",
     "Smuts concludes that air warfare will in future be an operation independent of sea and land. The Army and the Navy resist losing their aircraft, and the Air Council needs a decision."),
  options=[
   ("Criar um serviço aéreo independente. (-10 de poder político; apoio à guerra +1% se a comissão Smuts foi criada)", "Create an independent air service. (-10 political power; war support +1% if the Smuts commission was appointed)",
    [pp(-10), flag("air_independent"), "if = { limit = { has_country_flag = ENG_ww1_smuts_commission } add_war_support = 0.01 }"], 65),
   ("Manter o Corpo Aéreo e o Serviço Naval separados. (+10 de poder político)", "Keep the Flying Corps and the Naval Service separate. (+10 political power)",
    [pp(10), flag("air_separate")], 35)]),
 dict(id=10, mode="trigger", trigger_full="tag = GER has_war_with = ENG",
  t=("O bloqueio da fome", "The Hunger Blockade"),
  d=("A Marinha Real fecha o Mar do Norte e o Canal. Trigo, fertilizantes, salitre e borracha deixam de chegar. Nas cidades alemãs faltam pão e batatas, e as filas de comida crescem.",
     "The Royal Navy closes the North Sea and the Channel. Grain, fertiliser, saltpetre and rubber stop arriving. In German cities bread and potatoes run short and food queues grow."),
  options=[
   ("Racionar pão e batatas. (estabilidade -1%, apoio à guerra -1%)", "Ration bread and potatoes. (stability -1%, war support -1%)",
    [stab(-0.01), "add_war_support = -0.01"], 65),
   ("Culpar a pirataria britânica na imprensa neutra. (estabilidade -1,5%, apoio à guerra +1%)", "Blame British piracy in the neutral press. (stability -1.5%, war support +1%)",
    [stab(-0.015), "add_war_support = 0.01"], 35)]),
 dict(id=11, mode="trigger", trigger_full="tag = USA NOT = { OR = { has_war_with = GER is_in_faction_with = ENG } }",
  t=("As Ordens em Conselho", "The Orders in Council"),
  d=("Os britânicos revistam navios americanos em Kirkwall e apreendem cargas destinadas à Holanda e à Escandinávia. Os exportadores de algodão e cobre reclamam, mas os bancos de Nova York lucram com os pedidos aliados.",
     "The British search American ships at Kirkwall and seize cargoes bound for Holland and Scandinavia. Cotton and copper exporters complain, but New York banks profit from Allied orders."),
  options=[
   ("Protestar com firmeza em Londres. (+10 de poder político; estabilidade britânica -1%, dívida britânica +1)", "Protest firmly in London. (+10 political power; British stability -1%, British debt +1)",
    [pp(10), "FROM = { add_stability = -0.01 add_to_variable = { ww1_britain_debt_burden = 1 } }"], 40),
   ("Aceitar o bloqueio e manter o comércio. (estabilidade +1%)", "Accept the blockade and keep trading. (stability +1%)",
    [stab(0.01), "FROM = { set_country_flag = ENG_ww1_us_trade_accepted }"], 60)]),
 dict(id=12, mode="trigger", trigger_full="OR = { tag = JAP tag = ITA tag = FRA tag = GRE }",
  t=("Escoltas no Mediterrâneo", "Escorts in the Mediterranean"),
  d=("Londres propõe dividir a escolta dos comboios no Mediterrâneo: contratorpedeiros aliados cobrem Malta, Brindisi e Salonica, enquanto os britânicos cobrem o Egito. Os submarinos inimigos afundam navios todas as semanas.",
     "London proposes to share convoy escort in the Mediterranean: Allied destroyers cover Malta, Brindisi and Salonika while the British cover Egypt. Enemy submarines sink ships every week."),
  options=[
   ("Aceitar a cooperação. (experiência naval +2; a experiência naval britânica +2)", "Accept the cooperation. (naval experience +2; British naval experience +2)",
    [navy_xp(2), "FROM = { navy_experience = 2 }"], 70),
   ("Recusar. (sem efeitos)", "Decline. (no effects)", [], 30)]),
]

DECISIONS = [
 dict(id="ENG_ww1_tighten_the_blockade",
  lines=["  visible = { has_country_flag = ENG_ww1_blockade }",
         "  available = { has_war_with = GER has_capitulated = no country_exists = GER check_variable = { ww1_britain_blockade_level < 3 } }",
         "  cost = 25 days_re_enable = 240",
         "  complete_effect = {",
         "   add_to_variable = { ww1_britain_blockade_level = 1 }",
         "   add_to_variable = { ww1_britain_debt_burden = 1 }",
         "   navy_experience = 1",
         "   GER = { country_event = { id = ww1_britain_nav.10 } }",
         "  }",
         "  ai_will_do = { base = 1 }"],
  pt=("Apertar o bloqueio", "Gasta 25 de poder político. Em guerra contra a Alemanha, a Alemanha sente nova escassez (estabilidade e apoio à guerra caem), a dívida sobe 1 e ganha 1 de experiência naval. Pode ser usado três vezes, com intervalo de oito meses."),
  en=("Tighten the Blockade", "Spend 25 political power. At war with Germany, Germany suffers a new shortage (stability and war support fall), debt rises by 1 and it grants 1 naval experience. Can be used three times, eight months apart.")),
 dict(id="ENG_ww1_lend_escort_flotillas",
  lines=["  visible = { has_country_flag = ENG_ww1_med_liaison }",
         "  available = { has_war = yes has_capitulated = no }",
         "  cost = 20 days_re_enable = 300",
         "  complete_effect = {",
         "   every_other_country = { limit = { is_in_faction_with = ROOT } country_event = { id = ww1_britain_nav.12 } }",
         "  }",
         "  ai_will_do = { base = 1 }"],
  pt=("Partilhar flotilhas de escolta", "Gasta 20 de poder político. Em guerra, repete a proposta de escolta conjunta a cada aliado naval da facção, que decide se aceita. Exige a cooperação do Mediterrâneo."),
  en=("Share Escort Flotillas", "Spend 20 political power. At war, repeats the joint escort offer to each naval ally in the faction, who decides whether to accept. Requires the Mediterranean cooperation.")),
 dict(id="ENG_ww1_fund_home_air_defence",
  lines=["  visible = { has_country_flag = ENG_ww1_home_air_defence }",
         "  available = { has_war = yes has_capitulated = no }",
         "  cost = 30 days_re_enable = 365",
         "  complete_effect = { add_war_support = 0.01 add_to_variable = { ww1_britain_debt_burden = 1 } air_experience = 2 }",
         "  ai_will_do = { base = 1 }"],
  pt=("Financiar a defesa aérea doméstica", "Gasta 30 de poder político. Em guerra, apoio à guerra +1%, dívida +1 e 2 de experiência aérea. Disponível uma vez por ano, depois da coordenação da defesa aérea."),
  en=("Fund Home Air Defence", "Spend 30 political power. At war, war support +1%, debt +1 and 2 air experience. Available once a year after the home air defence coordination.")),
]

CATEGORY_LOC = ("Política das Forças Armadas", "Armed Services Policy",
                "Decisões ligadas à Marinha, à Força Aérea e ao Exército: bloqueio, escoltas, defesa aérea e estado-maior.",
                "Decisions tied to the Navy, the Air Force and the Army: blockade, escorts, air defence and staff work.")
