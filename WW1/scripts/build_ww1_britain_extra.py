"""UK extra content: events, decisions and timed institutions that consume focus flags which nothing used before.

    python scripts/build_ww1_britain_extra.py

Writes (all idempotent, generated, never hand-edit):
  events/ww1_britain_extra_events.txt            namespace ww1_britain_x (10 dated events)
  common/decisions/ww1_britain_extra_decisions.txt   17 decisions, in the three existing UK categories
  common/ideas/ww1_britain_extra_ideas.txt       5 timed institutions
  localisation/{english,braz_por}/ww1_britain_extra_l_*.yml

Design rules (checked by tests/test_ww1_britain_extra.py):
  * every decision is unlocked by a flag that a focus sets (so the focus description's promise is now real);
  * no free units, equipment or unpaid manpower; every benefit has a visible cost;
  * all numbers are small; UK state variables (debt, labour, Irish/Ulster tension, dominion consent) are clamped weekly.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = "ww1_britain_x"
V = {"debt": "ww1_britain_debt_burden", "lab": "ww1_britain_labour_support", "irish": "ww1_britain_irish_tension",
     "ulster": "ww1_britain_ulster_tension", "dom": "ww1_britain_dominion_consent"}
BASE = "tag = ENG has_capitulated = no has_country_flag = ww1_britain_initialised"


def fx(tokens):
    out = []
    for tok in tokens.split():
        k, _, a = tok.partition(":")
        if k in V:
            out.append(f"add_to_variable = {{ {V[k]} = {a} }}")
        elif k == "pp":
            out.append(f"add_political_power = {a}")
        elif k == "stab":
            out.append(f"add_stability = {a}")
        elif k == "ws":
            out.append(f"add_war_support = {a}")
        elif k == "axp":
            out.append(f"army_experience = {a}")
        elif k == "nxp":
            out.append(f"navy_experience = {a}")
        elif k == "fxp":
            out.append(f"air_experience = {a}")
        elif k == "idea":
            name, _, days = a.partition(":")
            out.append(f"add_timed_idea = {{ idea = ENG_ww1_x_{name} days = {days} }}")
        else:
            raise KeyError(tok)
    return " ".join(out)


# ------------------------------------------------------------------ events
# key, trigger, mtth days, EN title, PT title, EN text, PT text, [(EN, PT, tokens, ai)]
EVENTS = [
 ("agadir", "date > 1911.6.20 date < 1912.1.1 has_war = no", 8,
  "The Panther at Agadir", "O Panther em Agadir",
  "A German gunboat drops anchor at Agadir and Paris asks what London intends to do. The Foreign Office wants a firm answer, the Radicals want none, and Lloyd George has a speech ready for the Mansion House.",
  "Uma canhoneira alemã lança âncora em Agadir e Paris pergunta o que Londres pretende fazer. O Foreign Office quer uma resposta firme, os radicais não querem nenhuma, e Lloyd George já tem um discurso pronto para a Mansion House.",
  [("Speak at the Mansion House", "Discursar na Mansion House", "ws:0.01 pp:-15 axp:2", 40),
   ("Back France quietly", "Apoiar a França em silêncio", "axp:3 pp:-20", 30),
   ("Counsel restraint", "Aconselhar moderação", "pp:15 stab:0.005", 30)]),
 ("naval_scare", "date > 1912.3.1 date < 1912.11.1 has_war = no", 10,
  "The Mediterranean Question", "A questão do Mediterrâneo",
  "The new German fleet law leaves the Admiralty with too few battleships for both the North Sea and Malta. Churchill wants the Mediterranean squadron home; the Foreign Office fears what Italy and Austria will conclude.",
  "A nova lei naval alemã deixa o Almirantado com poucos encouraçados para o Mar do Norte e para Malta ao mesmo tempo. Churchill quer a esquadra do Mediterrâneo em casa; o Foreign Office teme o que a Itália e a Áustria concluirão.",
  [("Concentrate the fleet in home waters", "Concentrar a frota em águas territoriais", "nxp:3 debt:1", 40),
   ("Keep a Mediterranean squadron", "Manter uma esquadra no Mediterrâneo", "nxp:2 pp:-20", 30),
   ("Rely on the French fleet", "Confiar na frota francesa", "pp:15 debt:-1", 30)]),
 ("suffragettes", "date > 1913.4.1 date < 1914.3.1 has_war = no", 12,
  "Votes for Women", "Voto para as mulheres",
  "Windows are broken in the West End and prisoners on hunger strike are released and arrested again. The Home Office has a law for it, the Speaker's Conference is a dream, and the public is tired of both sides.",
  "Vidraças são quebradas no West End e presas em greve de fome são soltas e presas de novo. O Home Office tem uma lei para isso, a Conferência do Presidente é um sonho, e o público está cansado dos dois lados.",
  [("Apply the Cat and Mouse Act", "Aplicar a lei do Gato e Rato", "stab:-0.01 pp:20 lab:-2", 30),
   ("Open talks on a limited franchise", "Abrir negociações sobre um sufrágio limitado", "lab:3 pp:-25", 40),
   ("Leave it to the courts", "Deixar com os tribunais", "stab:-0.005 pp:10", 30)]),
 ("curragh", "date > 1914.3.18 date < 1914.7.1 has_war = no check_variable = { ww1_britain_ulster_tension > 9 }", 3,
  "The Curragh Incident", "O incidente de Curragh",
  "Cavalry officers at the Curragh say they would rather resign than march against Ulster. The War Office hesitates, the Cabinet contradicts itself, and the Irish benches ask who governs the army.",
  "Oficiais de cavalaria em Curragh dizem preferir renunciar a marchar contra o Ulster. O Ministério da Guerra hesita, o Gabinete se contradiz e os bancos irlandeses perguntam quem governa o exército.",
  [("Reassure the officers", "Tranquilizar os oficiais", "irish:6 ulster:-4 axp:2", 35),
   ("Court-martial the ringleaders", "Submeter os cabeças a corte marcial", "irish:-3 ulster:6 stab:-0.01 pp:-20", 20),
   ("Let the Prime Minister take the War Office", "Deixar o Primeiro-Ministro assumir o Ministério da Guerra", "pp:-15 stab:0.005", 45)]),
 ("lusitania", "date > 1915.5.6 date < 1915.9.1 has_war = yes", 2,
  "The Lusitania", "O Lusitania",
  "A German submarine sinks the liner off the Old Head of Kinsale. More than a thousand are dead, among them Americans, and crowds smash German shop windows in Liverpool and London.",
  "Um submarino alemão afunda o transatlântico perto de Old Head of Kinsale. Mais de mil mortos, entre eles americanos, e multidões quebram vitrines alemãs em Liverpool e Londres.",
  [("Publish the casualty lists", "Publicar as listas de vítimas", "ws:0.02 pp:-20", 40),
   ("Send a measured note to Washington", "Enviar uma nota comedida a Washington", "pp:10 ws:0.005", 35),
   ("Reopen the convoy question", "Reabrir a questão dos comboios", "nxp:2 pp:-15", 25)]),
 ("passchendaele", "date > 1917.7.25 date < 1917.12.1 has_war = yes", 3,
  "Third Ypres", "A Terceira Batalha de Ypres",
  "The rains come early and the ridge is a swamp. Haig believes one more push breaks the German army; Lloyd George fears the casualty lists and the Italian front is calling for guns.",
  "As chuvas chegam cedo e a crista é um pântano. Haig acredita que mais um empurrão quebra o exército alemão; Lloyd George teme as listas de baixas e a frente italiana pede canhões.",
  [("Press the offensive", "Prosseguir com a ofensiva", "axp:6 ws:-0.02 lab:-2 debt:1", 40),
   ("Halt after the ridge", "Parar depois da crista", "pp:15 axp:2", 30),
   ("Send guns to Italy", "Enviar canhões à Itália", "axp:3 pp:-10 ws:-0.005", 30)]),
 ("cambrai", "date > 1917.11.15 date < 1918.3.1 has_war = yes", 3,
  "Cambrai", "Cambrai",
  "Hundreds of tanks roll over the Hindenburg Line without a preliminary bombardment, and for the first time the church bells ring in London. The German counter-attack ten days later takes most of it back.",
  "Centenas de tanques atravessam a Linha Hindenburg sem bombardeio preliminar e, pela primeira vez, os sinos de Londres repicam. O contra-ataque alemão dez dias depois retoma quase tudo.",
  [("Ring the bells and back the tanks", "Repicar os sinos e apoiar os tanques", "axp:4 ws:0.01 debt:1", 40),
   ("Study the lessons", "Estudar as lições", "axp:6 pp:-20", 35),
   ("Caution the press", "Moderar a imprensa", "pp:10", 25)]),
 ("influenza", "date > 1918.9.1 date < 1919.4.1", 15,
  "The Influenza", "A gripe",
  "The second wave of the influenza empties factories, schools and barracks. Doctors want the cinemas closed; the Local Government Board wants the trains kept running.",
  "A segunda onda da gripe esvazia fábricas, escolas e quartéis. Os médicos querem os cinemas fechados; o Conselho de Governo Local quer os trens funcionando.",
  [("Fund hospitals and inspectors", "Financiar hospitais e inspetores", "debt:1 stab:0.01 pp:-15", 45),
   ("Leave it to local boards", "Deixar com os conselhos locais", "pp:10 stab:-0.015 lab:-1", 30),
   ("Censor the figures", "Censurar os números", "stab:-0.02 ws:0.01", 25)]),
 ("amritsar", "date > 1919.4.10 date < 1919.10.1", 5,
  "Jallianwala Bagh", "Jallianwala Bagh",
  "General Dyer's troops have fired into an unarmed crowd in Amritsar. The Viceroy's telegrams are cautious, the Punjab is under martial law, and Montagu demands to know what was done in the Crown's name.",
  "As tropas do general Dyer dispararam contra uma multidão desarmada em Amritsar. Os telegramas do vice-rei são cautelosos, o Punjab está sob lei marcial e Montagu exige saber o que foi feito em nome da Coroa.",
  [("Appoint the Hunter Committee", "Nomear o Comitê Hunter", "pp:-20 dom:2 lab:1 stab:0.005", 40),
   ("Stand by General Dyer", "Apoiar o general Dyer", "pp:10 dom:-4 stab:-0.01", 15),
   ("Censure and retire him quietly", "Censurá-lo e aposentá-lo discretamente", "pp:-5 dom:1", 45)]),
 ("chanak", "date > 1922.9.10 date < 1923.1.1 has_war = no", 3,
  "The Chanak Crisis", "A crise de Chanak",
  "Kemal's army reaches the neutral zone at the Straits and a few British battalions stand between it and the sea. The Dominions are asked to send troops and Canada does not answer.",
  "O exército de Kemal chega à zona neutra dos Estreitos e poucos batalhões britânicos ficam entre ele e o mar. Os Domínios são convidados a enviar tropas e o Canadá não responde.",
  [("Stand firm at the Straits", "Manter-se firme nos Estreitos", "ws:0.01 pp:-25 dom:-5 nxp:2", 25),
   ("Negotiate at Mudanya", "Negociar em Mudanya", "pp:15 dom:2", 50),
   ("Appeal to the Dominions", "Apelar aos Domínios", "dom:-2 pp:-5", 25)]),
]

# ------------------------------------------------------------------ timed institutions
IDEAS = {  # key: (modifier text, EN name, PT name, EN desc, PT desc)
 "indian_corps": ("army_org_factor = .03 supply_consumption_factor = .02", "The Indian Corps", "O Corpo Indiano",
                  "Seasoned Indian regiments stiffen the line but cost shipping and supply.", "Regimentos indianos experientes reforçam a linha, mas consomem transporte e suprimentos."),
 "district_contracts": ("production_factory_efficiency_gain_factor = .05 consumer_goods_factor = .01", "District Contracts", "Contratos distritais",
                        "Contracts placed with the surveyed workshops of the Midlands and the Clyde speed up output at a cost to civilian goods.", "Contratos com as oficinas inspecionadas das Midlands e do Clyde aceleram a produção ao custo de bens civis."),
 "officer_courses": ("training_time_army_factor = -.05 experience_gain_army_factor = .03", "Officer Training Courses", "Cursos de formação de oficiais",
                     "Public schools and universities send a steady stream of trained subalterns.", "Escolas e universidades enviam um fluxo regular de subalternos treinados."),
 "city_credit_line": ("industrial_capacity_factory = .03 consumer_goods_factor = .01", "City Credit Line", "Linha de crédito da City",
                      "The City discounts industrial bills for a season; the debt remains.", "A City desconta títulos industriais por uma temporada; a dívida permanece."),
 "seaplane_patrols": ("naval_detection = .08 experience_gain_air_factor = .02", "Seaplane Patrol Rota", "Escala de patrulhas de hidroaviões",
                      "Seaplanes from Calshot, Felixstowe and Yarmouth watch the approaches.", "Hidroaviões de Calshot, Felixstowe e Yarmouth vigiam as aproximações."),
}

# ------------------------------------------------------------------ decisions
# key, category, visible flag, extra available, cost, days, factories, re-enable, when ('remove' | 'complete'), tokens, ai, EN, PT, EN desc, PT desc
S, E = "ENG_ww1_services_policy", "ENG_ww1_empire_policy"
DECISIONS = [
 ("call_indian_corps", S, "ENG_ww1_consulted_india", "has_war = yes NOT = { has_idea = ENG_ww1_x_indian_corps }", 35, 1, 0, 270, "complete", "idea:indian_corps:120 dom:-1 debt:1", 1,
  "Call the Indian Corps", "Convocar o Corpo Indiano",
  "The liaison with the Indian Army allows a call for its regiments. They stiffen the line for 120 days, but shipping and supply suffer and India's consent cools.",
  "A ligação com o Exército Indiano permite convocar seus regimentos. Eles reforçam a linha por 120 dias, mas transporte e suprimentos sofrem e o consentimento indiano esfria."),
 ("place_district_contracts", S, "ENG_ww1_district_surveys", "num_of_civilian_factories_available_for_projects > 0", 30, 60, 1, 240, "remove", "idea:district_contracts:180 debt:1", 1,
  "Place District Contracts", "Firmar contratos distritais",
  "Use the survey of the industrial districts to place orders. One civilian factory is tied up for 60 days; afterwards output improves for half a year and debt rises.",
  "Use o levantamento dos distritos industriais para firmar pedidos. Uma fábrica civil fica ocupada por 60 dias; depois a produção melhora por meio ano e a dívida aumenta."),
 ("rehearse_mobilisation", S, "ENG_ww1_mobilisation_tables", "has_war = no", 30, 45, 0, 300, "remove", "axp:3", 1,
  "Rehearse the Mobilisation Tables", "Ensaiar as tabelas de mobilização",
  "A paper rehearsal of trains, ports and depots for the Expeditionary Force. It teaches the Staff where the tables fail.",
  "Um ensaio em papel de trens, portos e depósitos da Força Expedicionária. Ensina ao Estado-Maior onde as tabelas falham."),
 ("summer_camp_season", S, "ENG_ww1_territorial_camps", "has_war = no", 25, 60, 0, 330, "remove", "axp:3 stab:0.005", 1,
  "Hold the Summer Camps", "Realizar os acampamentos de verão",
  "The Territorial battalions pitch their tents for a fortnight. Volunteers and employers grumble, but the regiments learn to march together.",
  "Os batalhões Territoriais armam suas tendas por quinze dias. Voluntários e patrões resmungam, mas os regimentos aprendem a marchar juntos."),
 ("officer_courses", S, "ENG_ww1_officer_training_corps", "num_of_civilian_factories_available_for_projects > 0 NOT = { has_idea = ENG_ww1_x_officer_courses }", 40, 60, 1, 365, "remove", "idea:officer_courses:240", 1,
  "Expand the Officer Training Courses", "Ampliar os cursos de formação de oficiais",
  "Fund extra courses at the public schools and universities. One civilian factory worth of labour is tied up for 60 days; trained subalterns follow for eight months.",
  "Financie cursos extras em escolas e universidades. Mão de obra equivalente a uma fábrica civil fica ocupada por 60 dias; subalternos treinados chegam por oito meses."),
 ("aerial_sorties", S, "ENG_ww1_aerial_reports", "has_war = yes", 25, 45, 0, 120, "remove", "axp:2 fxp:2", 1,
  "Fly Reconnaissance Sorties", "Realizar missões de reconhecimento aéreo",
  "Order systematic photographic sorties over the enemy lines. Staff and squadrons learn to read the pictures together.",
  "Ordene missões fotográficas sistemáticas sobre as linhas inimigas. Estado-Maior e esquadrilhas aprendem a interpretar as imagens juntos."),
 ("night_patrols", S, "ENG_ww1_night_flying", "has_war = yes", 30, 60, 0, 150, "remove", "fxp:3 stab:0.005", 1,
  "Fly Night Patrols", "Realizar patrulhas noturnas",
  "Pilots take off in the dark to meet the raiders over London. The city sleeps a little better.",
  "Pilotos decolam no escuro para encontrar os bombardeiros sobre Londres. A cidade dorme um pouco melhor."),
 ("shipping_audit", S, "ENG_ww1_merchant_register", "", 25, 45, 0, 200, "remove", "nxp:2 debt:-1", 1,
  "Audit the Merchant Register", "Auditar o registro mercante",
  "Lloyd's and the Board of Trade check which hulls can carry cargo, troops or hospitals. Idle tonnage is found and sold.",
  "Lloyd's e o Board of Trade verificam quais cascos podem levar carga, tropas ou hospitais. A tonelagem ociosa é encontrada e vendida."),
 ("seaplane_rota", S, "ENG_ww1_seaplane_stations", "has_war = yes NOT = { has_idea = ENG_ww1_x_seaplane_patrols }", 30, 60, 0, 200, "remove", "idea:seaplane_patrols:150 nxp:1", 1,
  "Set the Seaplane Patrol Rota", "Fixar a escala de patrulhas de hidroaviões",
  "Draw up a rota for the stations on the east coast. For five months the approaches are watched more closely.",
  "Monte uma escala para as estações da costa leste. Por cinco meses as aproximações são vigiadas de perto."),
 ("gas_drill", S, "ENG_ww1_gas_discipline", "has_war = yes", 30, 45, 0, 180, "remove", "axp:3 debt:1", 1,
  "Drill Gas Discipline", "Treinar disciplina contra gás",
  "Every battalion rotates through the gas chambers and respirator drill. It costs time and equipment but saves lives.",
  "Todo batalhão passa pelas câmaras de gás e pelo treino de máscaras. Custa tempo e equipamento, mas salva vidas."),
 ("cargo_priorities", E, "ENG_ww1_shipping_pool", "has_war = yes is_in_faction = yes", 40, 30, 0, 240, "remove", "debt:-2 nxp:1", 1,
  "Set the Allied Cargo Priorities", "Definir as prioridades de carga aliadas",
  "The allied council ranks troops, munitions, wheat and coal. Tonnage is shared and the Treasury pays fewer freight bills.",
  "O conselho aliado ordena tropas, munições, trigo e carvão. A tonelagem é compartilhada e o Tesouro paga menos fretes."),
 ("city_bills", E, "ENG_ww1_city_credit", "NOT = { has_idea = ENG_ww1_x_city_credit_line }", 25, 1, 0, 300, "complete", "idea:city_credit_line:150 debt:2", 0.3,
  "Discount Industrial Bills in the City", "Descontar títulos industriais na City",
  "The City of London discounts industrial bills for five months. Factories get working capital; the debt remains to be paid.",
  "A City de Londres desconta títulos industriais por cinco meses. As fábricas ganham capital de giro; a dívida continua por pagar."),
 ("reconstruction_commission", E, "ENG_ww1_peace_administration", "has_war = no num_of_civilian_factories_available_for_projects > 0", 35, 90, 1, 365, "remove", "lab:3 stab:0.01 debt:1", 1,
  "Appoint a Reconstruction Commission", "Nomear uma comissão de reconstrução",
  "A commission takes over housing, employment and demobilisation grievances. It ties up one civilian factory for 90 days and costs money.",
  "Uma comissão assume habitação, emprego e queixas da desmobilização. Ocupa uma fábrica civil por 90 dias e custa dinheiro."),
 ("service_the_debt", E, "ENG_ww1_debt_service_commission", "check_variable = { ww1_britain_debt_burden > 25 }", 50, 1, 0, 240, "complete", "debt:-3 lab:-1", 0.5,
  "Service the War Debt", "Pagar o serviço da dívida de guerra",
  "The commission redeems a tranche of the war debt out of revenue. Debt falls, but the fiscal squeeze is felt in wages.",
  "A comissão resgata uma parcela da dívida de guerra com a receita. A dívida cai, mas o aperto fiscal é sentido nos salários."),
 ("demob_schedule", E, "ENG_ww1_demobilisation_planned", "has_war = no", 30, 60, 0, 999, "remove", "lab:3 stab:0.01 debt:-1", 1,
  "Issue the Demobilisation Schedule", "Publicar o cronograma de desmobilização",
  "Men are released by age, trade and length of service. Workers return to factories in an orderly way instead of in a flood.",
  "Os homens são liberados por idade, ofício e tempo de serviço. Os trabalhadores voltam às fábricas de forma ordenada em vez de em enxurrada."),
 ("industrial_council", E, "ENG_ww1_industrial_conference", "has_war = no", 30, 60, 0, 300, "remove", "lab:3 stab:0.005", 1,
  "Convene the Industrial Council", "Convocar o Conselho Industrial",
  "Employers and union leaders meet under the Ministry of Labour. A season of talks lowers the temperature in the mills and the docks.",
  "Patrões e líderes sindicais se reúnem sob o Ministério do Trabalho. Uma temporada de conversas reduz a temperatura nas fábricas e nas docas."),
 ("imperial_defence_committee", E, "ENG_ww1_imperial_defence_review", "has_war = no", 30, 45, 0, 300, "remove", "dom:3 nxp:1", 1,
  "Meet the Imperial Defence Committee", "Reunir o Comitê de Defesa Imperial",
  "The Dominions' representatives sit with the Admiralty and the War Office to plan the next decade of imperial defence.",
  "Os representantes dos Domínios se sentam com o Almirantado e o Ministério da Guerra para planejar a próxima década de defesa imperial."),
]


def esc(s):
    return s.replace('"', "'")


def build_events():
    out = [f"add_namespace = {NS}", ""]
    for n, (key, trig, mtth, *_rest) in enumerate(EVENTS, 1):
        opts = _rest[4]
        eid = f"{NS}.{n}"
        out += ["country_event = {", f" id = {eid} title = {eid}.t desc = {eid}.d", f" picture = GFX_event_ww1_britain_x_{key}",
                " fire_only_once = yes", f" trigger = {{ {BASE} {trig} }}", f" mean_time_to_happen = {{ days = {mtth} }}"]
        for k, (_en, _pt, tokens, ai) in enumerate(opts):
            out += [" option = {", f"  name = {eid}.{'abc'[k]}", f"  ai_chance = {{ base = {ai} }}", "  " + fx(tokens), " }"]
        out.append("}")
    return "\n".join(out) + "\n"


def build_ideas():
    lines = ["ideas = {", " country = {"]
    for key, (mod, *_r) in IDEAS.items():
        lines.append(f"  ENG_ww1_x_{key} = {{ picture = ENG_ww1_x_{key} allowed = {{ original_tag = ENG }} removal_cost = -1 modifier = {{ {mod} }} }}")
    lines += [" }", "}"]
    return "\n".join(lines) + "\n"


def build_decisions():
    by = {S: [], E: []}
    for (key, cat, flag, avail, cost, days, fac, reen, when, tokens, ai, *_t) in DECISIONS:
        did = f"ENG_ww1_x_{key}"
        b = [f" {did} = {{", f"  icon = GFX_decision_ENG_ww1_x_{key}", f"  visible = {{ has_country_flag = {flag} }}",
             f"  available = {{ has_capitulated = no {avail} }}".replace("  ", " ", 0),
             f"  cost = {cost} days_re_enable = {reen}"]
        if reen >= 999:
            b[-1] = f"  cost = {cost}\n  fire_only_once = yes"
        if days > 1:
            b.append(f"  days_remove = {days}")
        if fac:
            b.append(f"  civilian_factory_use = {fac}")
        eff = fx(tokens)
        b.append(f"  {'complete_effect' if when == 'complete' else 'remove_effect'} = {{ {eff} }}")
        b.append(f"  ai_will_do = {{ base = {ai} }}")
        b.append(" }")
        by[cat].extend(b)
    return "\n".join(f"{c} = {{\n" + "\n".join(v) + "\n}" for c, v in by.items()) + "\n"


def loc_pairs():
    en, pt = {}, {}
    for n, (key, trig, mtth, t_en, t_pt, d_en, d_pt, opts) in enumerate(EVENTS, 1):
        eid = f"{NS}.{n}"
        en[eid + ".t"], pt[eid + ".t"] = t_en, t_pt
        en[eid + ".d"], pt[eid + ".d"] = d_en, d_pt
        for k, (o_en, o_pt, _tok, _ai) in enumerate(opts):
            en[f"{eid}.{'abc'[k]}"], pt[f"{eid}.{'abc'[k]}"] = o_en, o_pt
    for key, (_mod, n_en, n_pt, d_en, d_pt) in IDEAS.items():
        en[f"ENG_ww1_x_{key}"], pt[f"ENG_ww1_x_{key}"] = n_en, n_pt
        en[f"ENG_ww1_x_{key}_desc"], pt[f"ENG_ww1_x_{key}_desc"] = d_en, d_pt
    for (key, *_m, n_en, n_pt, d_en, d_pt) in DECISIONS:
        did = f"ENG_ww1_x_{key}"
        en[did], pt[did] = n_en, n_pt
        en[did + "_desc"], pt[did + "_desc"] = d_en, d_pt
    return en, pt


def write(rel, text, bom=False):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((b"\xef\xbb\xbf" if bom else b"") + text.replace("\r\n", "\n").encode("utf-8"))


def main():
    write("events/ww1_britain_extra_events.txt", build_events())
    write("common/ideas/ww1_britain_extra_ideas.txt", build_ideas())
    write("common/decisions/ww1_britain_extra_decisions.txt", build_decisions())
    en, pt = loc_pairs()
    for lang, d in (("english", en), ("braz_por", pt)):
        body = "\n".join(f' {k}:0 "{esc(v)}"' for k, v in d.items())
        write(f"localisation/{lang}/ww1_britain_extra_l_{lang}.yml", f"l_{lang}:\n{body}\n", bom=True)
    print({"events": len(EVENTS), "ideas": len(IDEAS), "decisions": len(DECISIONS), "loc_keys": len(en)})


if __name__ == "__main__":
    main()
