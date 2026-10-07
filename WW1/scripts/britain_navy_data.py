"""UK content, wing 4 (Navy and Aviation): rewards, descriptions, events, ideas, decisions.

Namespace ww1_britain_nav. Partner events (10-12) run in the partner's scope: ROOT = partner, FROM = ENG.
Rewards stay small and traded-off: no free ships, aircraft or equipment; research bonuses are one-use.
Already-finished focuses (admiralty survey, estimates, dreadnoughts, fleet maintenance, convoys, pilot
instruction, RAF) only had the stub reward; every one of the 40 is implemented here.
"""
from britain_politics_data import var, flag, idea, pp, stab, navy_xp

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
    [pp(10), idea("admiralty_war_staff"), flag("fleet_survey")],
    "O Almirantado mede a prontidão da frota e admite o que todos sabem: não existe um estado-maior naval de verdade. O Estado-Maior de Guerra Naval nasce em 1912. Ganha 10 de poder político e a instituição Estado-Maior Naval (+10% de experiência naval ganha).",
    "The Admiralty measures the readiness of the fleet and admits what everyone knows: there is no real naval staff. The Admiralty War Staff is born in 1912. It grants 10 political power and the Admiralty War Staff institution (+10% naval experience gain)."),
"the_naval_estimates": (
    [build(132, "dockyard"), var("debt_burden", 1), navy_xp(3), flag("naval_estimates")],
    "O Almirantado amplia os estaleiros de Birkenhead e Cammell Laird para a corrida de couraçados. Enfileira 1 estaleiro no noroeste; a dívida sobe 1 e ganha 3 de experiência naval.",
    "The Admiralty expands the Birkenhead and Cammell Laird yards for the battleship race. It queues 1 dockyard in the North-West; debt rises by 1 and grants 3 naval experience."),
"dreadnought_construction_planning": (
    [tech("dreadnought_construction_planning", "bb_tech"), var("debt_burden", 1), flag("super_dreadnoughts")],
    "A classe Queen Elizabeth troca os canhões de 13,5 por 15 polegadas e o carvão pelo óleo, uma aposta ousada. A dívida sobe 1 e ganha bônus de pesquisa de 25% em couraçados (uso único).",
    "The Queen Elizabeth class swaps 13.5-inch guns for 15-inch and coal for oil, a bold gamble. Debt rises by 1 and it grants a one-use 25% research bonus on battleships."),
"battlecruiser_squadron_planning": (
    [tech("battlecruiser_squadron_planning", "bc_tech"), navy_xp(2), flag("battlecruiser_squadron")],
    "Beatty comanda uma esquadra rápida, de canhões grandes e casco fino, feita para caçar cruzadores alemães. Ganha 2 de experiência naval e bônus de pesquisa de 25% em cruzadores de batalha (uso único).",
    "Beatty commands a fast squadron of big guns and thin hulls, built to hunt German cruisers. It grants 2 naval experience and a one-use 25% research bonus on battlecruisers."),
"destroyer_flotilla_planning": (
    [build(119, "dockyard"), tech("destroyer_flotilla_planning", "dd_tech"), navy_xp(2), flag("destroyer_flotillas")],
    "Harland & Wolff e estaleiros em Belfast recebem encomendas para contratorpedeiros. Enfileira 1 estaleiro na Irlanda do Norte, ganha 2 de experiência naval e bônus de pesquisa de 25% em contratorpedeiros (uso único).",
    "Harland & Wolff and yards in Belfast receive orders for destroyers. It queues 1 dockyard in Northern Ireland, grants 2 naval experience and a one-use 25% research bonus on destroyers."),
"submarine_service_development": (
    [tech("submarine_service_development", "ss_tech"), navy_xp(1), flag("submarine_service")],
    "Os submarinos classe E são pensados para a defesa costeira e a vigia da baía alemã, não para o comércio. Ganha 1 de experiência naval e bônus de pesquisa de 25% em submarinos (uso único).",
    "The E-class submarines are meant for coastal defence and watching the German Bight, not for commerce raiding. It grants 1 naval experience and a one-use 25% research bonus on submarines."),
"naval_gunnery_calibration": (
    [tech("naval_gunnery_calibration", "naval_artillery"), navy_xp(3), flag("fire_control_tables")],
    "As mesas de controle de fogo de Dreyer e Pollen prometem acertar a quase 15 quilômetros. Ganha 3 de experiência naval e bônus de pesquisa de 25% em artilharia naval (uso único).",
    "The fire-control tables of Dreyer and Pollen promise hits at nearly 15 kilometres. It grants 3 naval experience and a one-use 25% research bonus on naval artillery."),
"the_north_sea_watch": (
    [idea("northern_patrol"), navy_xp(2), flag("north_sea_watch")],
    "Cruzadores velhos e navios mercantes armados fecham o espaço entre a Escócia e a Noruega. Ganha a instituição Patrulha do Norte (detecção naval +10%) e 2 de experiência naval.",
    "Old cruisers and armed merchant ships close the gap between Scotland and Norway. It grants the Northern Patrol institution (naval detection +10%) and 2 naval experience."),
"grand_fleet_maintenance": (
    [idea("grand_fleet_anchorage"), "120 = { add_building_construction = { type = naval_base level = 1 province = 11064 } }", "121 = { add_building_construction = { type = naval_base level = 1 province = 6300 } }", var("debt_burden", 1), flag("scapa_flow")],
    "Scapa Flow e Rosyth ganham defesas costeiras e expansão de bases navais para abrigar a Grande Frota. Amplia as bases navais nas Terras Altas e Baixas da Escócia, instituição Fundeadouros da Grande Frota (reparo naval +10%); a dívida sobe 1.",
    "Scapa Flow and Rosyth gain coastal defences and naval base expansions to shelter the Grand Fleet. Expands naval bases in the Scottish Highlands and Lowlands, Grand Fleet Anchorages institution (naval repair +10%); debt rises by 1."),
"merchant_shipping_register": (
    [navy_xp(2), stab(0.01), flag("merchant_register")],
    "O registro do Lloyd's e do Board of Trade lista os navios mercantes que podem virar transporte, escolta ou navio-hospital. Ganha 2 de experiência naval e 1% de estabilidade.",
    "The Lloyd's and Board of Trade registers list the merchant ships that can become transports, escorts or hospital ships. It grants 2 naval experience and 1% stability."),
"maritime_blockade_coordination": (
    [navy_xp(3), flag("blockade"), to_enemy("GER", 10), to("USA", 11)],
    "O Bloqueio da Alemanha sufoca o comércio alemão e irrita os neutros. Ganha 3 de experiência naval; a Alemanha sente a fome, e os Estados Unidos decidem se protestam contra as Ordens em Conselho.",
    "The blockade of Germany chokes German trade and irritates the neutrals. It grants 3 naval experience; Germany feels the hunger, and the United States decides whether to protest the Orders in Council."),
"hydrophone_trials": (
    [tech("hydrophone_trials", "asw_tech"), navy_xp(1), flag("hydrophones")],
    "A estação de Hawkcraig testa microfones submersos para ouvir os motores dos submarinos. Ganha 1 de experiência naval e bônus de pesquisa de 25% em guerra antissubmarina (uso único).",
    "The Hawkcraig station tests underwater microphones to hear submarine engines. It grants 1 naval experience and a one-use 25% research bonus on anti-submarine warfare."),
"depth_charge_trials": (
    [tech("depth_charge_trials", "dd_tech"), navy_xp(2), flag("depth_charges")],
    "A carga de profundidade tipo D, de 1916, é lançada por contratorpedeiros sobre o ponto onde o submarino mergulhou. Ganha 2 de experiência naval e bônus de pesquisa de 25% em contratorpedeiros (uso único).",
    "The Type D depth charge of 1916 is dropped by destroyers on the spot where the submarine dived. It grants 2 naval experience and a one-use 25% research bonus on destroyers."),
"convoy_system_organisation": (
    [ev(2)],
    "Em 1917 os submarinos afundam um navio em cada quatro que saem para o mar. Lloyd George pressiona o Almirantado, que resiste a formar comboios. Dispara o debate do comboio: a escolha muda a guerra no Atlântico.",
    "In 1917 submarines sink one in four ships that put to sea. Lloyd George presses the Admiralty, which resists forming convoys. It triggers the convoy debate: the choice changes the war in the Atlantic."),
"escort_refit_contracts": (
    [tech("escort_refit_contracts", "dd_tech"), var("debt_burden", 1),
     "if = { limit = { has_idea = ENG_ww1_convoy_system } navy_experience = 4 }"],
    "Estaleiros convertem contratorpedeiros velhos, sloops e traineiras para escolta. A dívida sobe 1 e ganha bônus de pesquisa de 25% em contratorpedeiros (uso único); se o sistema de comboios já funciona, ganha mais 4 de experiência naval.",
    "Yards convert old destroyers, sloops and trawlers to escort duty. Debt rises by 1 and it grants a one-use 25% research bonus on destroyers; if the convoy system is already running, it also grants 4 naval experience."),
"naval_signals_and_direction_finding": (
    [pp(10), tech("naval_signals_and_direction_finding", "decryption_tech"), flag("direction_finding")],
    "Estações de rádio marcam a posição dos navios e submarinos alemães só pelo sinal que emitem. Ganha 10 de poder político e bônus de pesquisa de 25% em decifração (uso único).",
    "Radio stations fix the position of German ships and submarines from the signals they emit. It grants 10 political power and a one-use 25% research bonus on decryption."),
"mediterranean_convoy_liaison": (
    [navy_xp(2), flag("med_liaison"), to_ally("JAP", 12), to_ally("ITA", 12), to_ally("FRA", 12), to_ally("GRE", 12)],
    "Marinhas aliadas dividem a escolta no Mediterrâneo, onde os submarinos austríacos e alemães atacam. Ganha 2 de experiência naval e propõe a cooperação a cada aliado naval, que decide se aceita.",
    "Allied navies share escort duty in the Mediterranean, where Austrian and German submarines strike. It grants 2 naval experience and proposes cooperation to each naval ally, who decides whether to accept."),
"the_postwar_fleet_review": (
    [pp(15), navy_xp(2), flag("postwar_fleet_review")],
    "Com o armistício, o Almirantado faz a revista da frota: o que manter, o que vender e o que desarmar. Ganha 15 de poder político e 2 de experiência naval; o próximo passo é escolher entre economizar e aprender.",
    "With the armistice the Admiralty reviews the fleet: what to keep, what to sell and what to lay up. It grants 15 political power and 2 naval experience; the next step is a choice between saving and learning."),
"naval_budget_retrenchment": (
    [var("debt_burden", -3), pp(15), stab(0.01), flag("naval_retrenchment")],
    "O Tesouro corta o orçamento naval, aposenta couraçados velhos e cancela encomendas. A dívida cai 3; ganha 15 de poder político e 1% de estabilidade. Exclui as lições técnicas.",
    "The Treasury cuts the naval budget, retires old battleships and cancels orders. Debt falls by 3; it grants 15 political power and 1% stability. Excludes the technical lessons."),
"naval_technical_lessons": (
    [navy_xp(8), tech("naval_technical_lessons", "naval_equipment"), var("debt_burden", 1), flag("naval_lessons")],
    "O Almirantado estuda Jutland e a guerra submarina: munição com menos risco de explosão, blindagem de convés, controle de fogo. A dívida sobe 1; ganha 8 de experiência naval e bônus de pesquisa de 25% em equipamento naval (uso único). Exclui o corte orçamentário.",
    "The Admiralty studies Jutland and the submarine war: safer magazines, deck armour, fire control. Debt rises by 1; it grants 8 naval experience and a one-use 25% research bonus on naval equipment. Excludes the budget cuts."),
# ------------------------------------------------------------------ aviation (20)
"the_air_battalion_experiments": (
    [tech("the_air_battalion_experiments", "air_equipment"), air_xp(2), flag("air_battalion")],
    "O Batalhão Aéreo dos Engenheiros Reais testa balões, dirigíveis e aeroplanos em Larkhill. Ganha 2 de experiência aérea e bônus de pesquisa de 25% em equipamento aéreo (uso único).",
    "The Air Battalion of the Royal Engineers tests balloons, airships and aeroplanes at Larkhill. It grants 2 air experience and a one-use 25% research bonus on air equipment."),
"royal_flying_corps_organisation": (
    [idea("royal_flying_corps"), air_xp(2), flag("royal_flying_corps")],
    "O Corpo Aéreo Real nasce em 1912, com uma ala militar, uma ala naval e a Escola Central de Voo em Upavon. Ganha a instituição Corpo Aéreo Real (+10% de experiência aérea ganha) e 2 de experiência aérea.",
    "The Royal Flying Corps is born in 1912, with a military wing, a naval wing and the Central Flying School at Upavon. It grants the Royal Flying Corps institution (+10% air experience gain) and 2 air experience."),
"military_pilot_instruction": (
    [air_xp(5), pp(5), flag("pilot_instruction")],
    "Oficiais e sargentos aprendem a voar nas escolas de Upavon e Netheravon, com um diploma aeronáutico próprio. Ganha 5 de experiência aérea e 5 de poder político.",
    "Officers and sergeants learn to fly at Upavon and Netheravon, with their own aeronaut certificate. It grants 5 air experience and 5 political power."),
"aerial_reconnaissance_reports": (
    [army_xp(3), air_xp(2), flag("aerial_reports")],
    "Relatórios de observação aérea entram nos manuais do estado-maior do Exército. Ganha 3 de experiência de exército e 2 de experiência aérea.",
    "Aerial observation reports enter the army staff manuals. It grants 3 army experience and 2 air experience."),
"royal_naval_air_service_organisation": (
    [navy_xp(2), air_xp(3), flag("rnas")],
    "Em 1914 a ala naval se separa e vira o Serviço Aéreo Naval Real, com hidroaviões, dirigíveis e caças. Ganha 2 de experiência naval e 3 de experiência aérea.",
    "In 1914 the naval wing separates and becomes the Royal Naval Air Service, with seaplanes, airships and fighters. It grants 2 naval experience and 3 air experience."),
"wireless_and_aircraft_observation": (
    [tech("wireless_and_aircraft_observation", "electronics"), air_xp(2)],
    "Rádios de faísca, mesmo pesados, deixam o observador corrigir o tiro da artilharia pelo ar. Ganha 2 de experiência aérea e bônus de pesquisa de 25% em eletrônica (uso único).",
    "Spark wireless sets, though heavy, let the observer correct artillery fire from the air. It grants 2 air experience and a one-use 25% research bonus on electronics."),
"bristol_scout_trials": (
    [tech("bristol_scout_trials", "light_air"), air_xp(2), flag("bristol_scout")],
    "O Bristol Scout, pequeno e rápido, é a primeira aeronave britânica pensada para escoltar e caçar. Ganha 2 de experiência aérea e bônus de pesquisa de 25% em aviação leve (uso único).",
    "The Bristol Scout, small and fast, is the first British aircraft conceived to escort and hunt. It grants 2 air experience and a one-use 25% research bonus on light aircraft."),
"naval_seaplane_stations": (
    ["125 = { add_building_construction = { type = naval_base level = 1 } }", navy_xp(2), air_xp(2), flag("seaplane_stations")],
    "Estações de hidroaviões e ancoradouros em Calshot, Felixstowe e Great Yarmouth vigiam o Mar do Norte. Adiciona 1 nível de base naval em East Anglia, ganha 2 de experiência naval e 2 de experiência aérea.",
    "Seaplane stations and anchorages at Calshot, Felixstowe and Great Yarmouth watch the North Sea. Adds 1 naval base level in East Anglia, grants 2 naval experience and 2 air experience."),
"aircraft_production_contracts": (
    [tech("aircraft_production_contracts", "air_equipment"), var("debt_burden", 1), pp(5)],
    "A Fábrica Real de Aeronaves e empresas privadas como Sopwith, Vickers e Bristol disputam contratos. A dívida sobe 1; ganha 5 de poder político e bônus de pesquisa de 25% em equipamento aéreo (uso único).",
    "The Royal Aircraft Factory and private firms such as Sopwith, Vickers and Bristol compete for contracts. Debt rises by 1; it grants 5 political power and a one-use 25% research bonus on air equipment."),
"fighter_squadron_instruction": (
    [air_xp(4), tech("fighter_squadron_instruction", "light_fighter"), flag("fighter_instruction")],
    "Depois do Fokker, os esquadrões de caça aprendem a voar em formação e a atacar em grupo, e não mais sozinhos. Ganha 4 de experiência aérea e bônus de pesquisa de 25% em caças leves (uso único).",
    "After the Fokker, fighter squadrons learn to fly in formation and attack as a group, not alone. It grants 4 air experience and a one-use 25% research bonus on light fighters."),
"artillery_spotting_liaison": (
    [army_xp(3), air_xp(3), flag("artillery_spotting")],
    "Observadores aéreos e baterias passam a trabalhar juntos, com códigos de rádio e mapas comuns. Ganha 3 de experiência de exército e 3 de experiência aérea.",
    "Aerial observers and batteries begin to work together, with shared radio codes and maps. It grants 3 army experience and 3 air experience."),
"night_flying_experiments": (
    [air_xp(4), pp(5), flag("night_flying")],
    "Pilotos aprendem a decolar e pousar de noite, com lanternas e sinais, para interceptar os Zeppelins. Ganha 4 de experiência aérea e 5 de poder político.",
    "Pilots learn to take off and land at night, with flares and signals, to intercept the Zeppelins. It grants 4 air experience and 5 political power."),
"bomber_range_experiments": (
    [tech("bomber_range_experiments", "tactical_bomber"), air_xp(2), flag("bomber_range")],
    "Voos longos de teste, com tanques extras e miras novas, medem até onde um bombardeiro chega. Ganha 2 de experiência aérea e bônus de pesquisa de 25% em bombardeiros táticos (uso único).",
    "Long test flights, with extra tanks and new sights, measure how far a bomber can go. It grants 2 air experience and a one-use 25% research bonus on tactical bombers."),
"aircraft_engine_reliability": (
    [idea("engine_reliability"), var("debt_burden", 1), flag("engine_reliability")],
    "Os motores Rolls-Royce Eagle e os rotativos Le Rhône falham menos quando há peças padronizadas e oficinas de campanha. A dívida sobe 1; ganha a instituição Motores Confiáveis (acidentes aéreos -15%).",
    "Rolls-Royce Eagle engines and Le Rhône rotaries fail less when parts are standardised and field workshops exist. Debt rises by 1; it grants the Reliable Engines institution (air accidents -15%)."),
"home_air_defence_coordination": (
    [idea("home_air_defence"), pp(5), flag("home_air_defence")],
    "Canhões antiaéreos, holofotes e esquadrões de defesa doméstica protegem Londres e as cidades industriais. Ganha a instituição Defesa Aérea Doméstica (estabilidade +1%) e 5 de poder político; os ataques aéreos vão custar menos ao apoio à guerra.",
    "Anti-aircraft guns, searchlights and home defence squadrons protect London and the industrial cities. It grants the Home Air Defence institution (stability +1%) and 5 political power; air raids will cost less war support."),
"the_independent_air_service_debate": (
    [ev(6)],
    "Depois dos ataques dos Gotha a Londres, o general Smuts investiga a defesa aérea. A questão é se o Exército e a Marinha continuam com serviços aéreos separados ou se nasce uma força independente. Dispara o Relatório Smuts.",
    "After the Gotha raids on London, General Smuts investigates air defence. The question is whether the Army and the Navy keep separate air services or an independent force is born. It triggers the Smuts Report."),
"royal_air_force_unification": (
    ["remove_ideas = ENG_ww1_royal_flying_corps", idea("royal_air_force"), flag("raf_formed"),
     "if = { limit = { has_country_flag = ENG_ww1_air_independent } air_experience = 10 add_political_power = -10 }",
     "else = { air_experience = 4 add_political_power = 10 }"],
    "Em 1º de abril de 1918 nasce a Força Aérea Real, com o Corpo Aéreo e o Serviço Naval fundidos. Troca a instituição Corpo Aéreo Real por Força Aérea Real (+15% de experiência aérea ganha, +5% de eficiência de missão aérea). Se a força independente foi escolhida, ganha 10 de experiência aérea e perde 10 de poder político; senão, ganha 4 de experiência aérea e 10 de poder político.",
    "On 1 April 1918 the Royal Air Force is born, merging the Flying Corps and the Naval Service. It replaces the Royal Flying Corps institution with the Royal Air Force (+15% air experience gain, +5% air mission efficiency). If the independent force was chosen, it grants 10 air experience and costs 10 political power; otherwise it grants 4 air experience and 10 political power."),
"postwar_aircraft_demobilisation": (
    [var("debt_burden", -2), pp(10), stab(0.01), flag("aircraft_demobilised")],
    "Milhares de aviões sobram. A Companhia de Alienação de Aeronaves vende os excedentes e a RAF encolhe. A dívida cai 2; ganha 10 de poder político e 1% de estabilidade.",
    "Thousands of surplus aeroplanes remain. The Aircraft Disposal Company sells the surplus and the RAF shrinks. Debt falls by 2; it grants 10 political power and 1% stability."),
"civil_aviation_research": (
    [tech("civil_aviation_research", "air_equipment"), stab(0.01), var("debt_burden", -1), flag("civil_aviation")],
    "O Comitê de Transporte Aéreo Civil estuda rotas para o Império e para o Continente. A dívida cai 1; ganha 1% de estabilidade e bônus de pesquisa de 25% em equipamento aéreo (uso único). Exclui o plano de uma força aérea sustentável.",
    "The Civil Air Transport Committee studies routes to the Empire and the Continent. Debt falls by 1; it grants 1% stability and a one-use 25% research bonus on air equipment. Excludes the sustainable air force plan."),
"a_sustainable_air_establishment": (
    [air_xp(10), pp(15), var("debt_burden", 1), flag("trenchard_memorandum")],
    "O memorando de Trenchard defende uma RAF pequena, mas permanente, com escolas, esquadrões no Império e indústria própria. A dívida sobe 1; ganha 10 de experiência aérea e 15 de poder político. Exclui a pesquisa civil.",
    "Trenchard's memorandum defends a small but permanent RAF, with schools, squadrons in the Empire and its own industry. Debt rises by 1; it grants 10 air experience and 15 political power. Excludes civil aviation research."),
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
