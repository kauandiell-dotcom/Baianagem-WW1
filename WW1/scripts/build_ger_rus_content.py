"""Gera todo o conteudo novo da Alemanha e da Russia e aplica os remendos nas arvores de foco.

    python scripts/build_ger_rus_art.py            # 1) importa a arte dos eventos
    python scripts/relayout_wings.py germany       # 2) reorganiza as arvores (uma vez)
    python scripts/relayout_wings.py soviet
    python scripts/build_ger_rus_content.py        # 3) este script (idempotente)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent

import gr_lib as L
import gr_russia as R
import gr_germany as G
import gr_depth_loc  # noqa: F401  (registra os textos que faltavam)
import gr_patch as P

MARK = "# GR_PATCH_V1"


def w(rel, text, bom=False):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes((b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8"))


# ------------------------------------------------------------------ arquivos novos
def write_new_files():
    w("events/ww1_ger_rus_rework_events.txt",
      "# Gerado por scripts/build_ger_rus_content.py (nao editar a mao).\n\n" + "\n".join(L.EVENTS))
    w("common/ideas/ww1_ger_rus_rework_ideas.txt", L.render_ideas())
    w("common/decisions/categories/ww1_ger_rus_rework_categories.txt", "\n".join(L.CATEGORIES))
    w("common/decisions/ww1_ger_rus_rework_decisions.txt", L.render_decisions())
    w("common/scripted_effects/ww1_ger_rus_rework_effects.txt", R.ENGINE + "\n" + G.ENGINE)
    w("common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt", """on_actions = {
	on_weekly_SOV = {
		effect = {
			if = { limit = { original_tag = SOV } ww1_sov_rework_weekly = yes }
		}
	}
	on_weekly_GER = {
		effect = {
			if = { limit = { original_tag = GER } ww1_ger_rework_weekly = yes }
		}
	}
}
""")
    L.write_loc(ROOT)


# ------------------------------------------------------------------ remendos de arquivos existentes
def patch_russia_events():
    p = ROOT / "events/ww1_russia_events.txt"
    t = p.read_bytes().decode("utf-8-sig")
    if "SOV_path_democratic" in t:
        return
    # Caso Kornilov (evento 20): as escolhas passam a decidir o ramo
    nl = "\r\n" if "\r\n" in t else "\n"
    t = re.sub(r"(name = ww1_russia\.20\.a)\r?\n", lambda m: m.group(1) + nl + "\t\tset_country_flag = SOV_path_bolshevik" + nl, t, count=1)
    t = re.sub(r"(name = ww1_russia\.20\.b)\r?\n", lambda m: m.group(1) + nl + "\t\tset_country_flag = SOV_path_kornilov" + nl, t, count=1)
    i = t.find("name = ww1_russia.20.b")
    m = re.compile(r"\r?\n\t\}\r?\n").search(t, i)
    opt_c = ("\n\toption = {\n\t\tname = ww1_russia.20.c\n\t\tai_chance = { factor = 30 }\n"
             "\t\tset_country_flag = SOV_path_democratic\n\t\tadd_popularity = { ideology = democratic popularity = 0.10 }\n\t}\n").replace("\n", nl)
    t = t[:m.end()] + opt_c + t[m.end():]
    # eventos 101/102 estavam vazios
    t = re.sub(r"(name = ww1_russia\.101\.a)\s*\}", r"\1\n\t\tadd_war_support = 0.03\n\t\tarmy_experience = 10\n\t\tadd_to_variable = { SOV_army_loyalty = 3 }\n\t}", t, count=1)
    t = re.sub(r"(name = ww1_russia\.102\.a)\s*\}", r"\1\n\t\tadd_war_support = -0.03\n\t\tadd_stability = -0.02\n\t\tadd_to_variable = { SOV_army_loyalty = -3 }\n\t}", t, count=1)
    p.write_bytes(t.encode("utf-8"))


def patch_popularities():
    for fn, pops in (("GER - Germany.txt", (58, 20, 16, 6)), ("SOV - Soviet union.txt", (72, 12, 9, 7))):
        p = ROOT / "history/countries" / fn
        t = p.read_bytes().decode("utf-8-sig")
        new = "set_popularities = {\n\tneutrality = %d\n\tdemocratic = %d\n\tcommunism = %d\n\tfascism = %d\n}" % pops
        t2, n = re.subn(r"set_popularities\s*=\s*\{\s*neutrality\s*=\s*100\s*\}", new, t, count=1)
        if n:
            p.write_bytes(t2.encode("utf-8"))


RUS_DATES = {
    "SOV_kiev_opera_gala_1911": "1911.8.31", "SOV_the_fourth_state_duma_1912": "1912.10.15",
    "SOV_progressive_bloc_1915": "1915.8.1", "SOV_rodzianko_ultimatum": "1916.11.1",
    "SOV_murder_of_rasputin": "1916.12.1", "SOV_the_july_crisis_mobilization": "1914.7.20",
    "SOV_sarikamish_counter_encirclement": "1914.12.15", "SOV_storming_of_erzurum": "1916.1.20",
    "SOV_trabzon_amphibious_landing": "1916.4.1", "SOV_special_council_for_defense": "1915.8.1",
    "SOV_female_ammunition_workers": "1915.3.1", "SOV_end_the_shell_shortage": "1915.9.1",
    "SOV_the_shell_shortage_crisis": "1915.1.1", "SOV_the_great_retreat_to_the_dvina": "1915.7.1",
    "SOV_scovill_and_vickers_foreign_shells": "1915.6.1", "SOV_osowiec_and_novogeorgievsk_forts": "1915.7.1",
    "SOV_attack_of_the_dead_men_1915": "1915.8.6", "SOV_shock_battalions_of_death": "1917.5.1",
    "SOV_bochkareva_womens_battalion": "1917.5.1", "SOV_czech_legion_transsiberian_revolt": "1918.5.1",
    "SOV_tambov_peasant_rebellion": "1920.8.1", "SOV_armed_forces_of_south_russia": "1918.1.1",
    "SOV_omsk_siberian_government": "1918.11.1", "SOV_the_july_days_crisis": "1917.7.1",
    "SOV_moscow_state_conference": "1917.8.1", "SOV_murmansk_convoys_arrival": "1915.10.1",
    "SOV_motono_sazonov_treaty_1916": "1916.7.1", "SOV_expeditionary_corps_to_france": "1916.4.1",
    "SOV_bring_romania_into_the_war": "1916.8.1",
}
GER_DATES = {
    "GER_treaty_of_brest_litovsk": "1917.11.30", "GER_operation_michael_st_quentin": "1918.2.1",
    "GER_battle_of_verdun_attrition": "1916.1.1", "GER_kiel_sailors_mutiny": "1918.10.1",
    "GER_reichstag_peace_resolution": "1917.6.1", "GER_silent_dictatorship_ohl": "1916.8.1",
    "GER_the_great_retreat_of_1915": "1915.7.1", "GER_sealed_train_to_petrograd": "1917.3.1",
    "GER_treaty_of_bucharest_1918": "1918.3.1", "GER_battle_of_caporetto_breakthrough": "1917.9.1",
    "GER_invasion_of_romania_falkenhayn": "1916.7.1", "GER_gorlice_tarnow_breakthrough": "1915.4.1",
    "GER_battle_of_masurian_lakes": "1914.8.1", "GER_the_miracle_of_tannenberg": "1914.8.1",
    "GER_second_battle_of_ypres_gas": "1915.4.1", "GER_falkenhayn_dismissal_third_ohl": "1916.8.1",
    "GER_elastic_defense_in_depth": "1916.9.1", "GER_battle_of_cambrai_counterstroke": "1917.11.1",
    "GER_arras_and_vimy_ridge_stand": "1917.4.1", "GER_operation_georgette_flanders": "1918.4.1",
    "GER_operation_blucher_yorck": "1918.5.1", "GER_the_black_day_of_the_german_army": "1918.8.8",
    "GER_seek_armistice_fourteen_points": "1918.9.1", "GER_collapse_of_central_allies": "1918.9.15",
    "GER_fleet_sortie_order_mutiny": "1918.10.1", "GER_armistice_at_compiegne": "1918.11.1",
    "GER_the_stab_in_the_back_myth": "1918.11.1", "GER_spanish_flu_epidemic_crisis": "1918.6.1",
    "GER_skagerrak_battle_of_jutland_clash": "1916.5.1", "GER_operation_albion_baltic_islands": "1917.10.1",
    "GER_zimmermann_telegram_proposal": "1917.1.1", "GER_support_irish_easter_rising": "1916.4.1",
    "GER_gotha_raids_on_london": "1917.5.1", "GER_fokker_d_vii_air_supremacy": "1918.4.1",
    "GER_paris_gun_super_battery": "1918.3.1", "GER_first_german_tank_a7v": "1917.4.1",
    "GER_the_fokker_scourge_dominance": "1915.7.1",
}
GER_AI0 = [
    "GER_spartakusbund_proletarian_revolt", "GER_berlin_january_mass_strikes", "GER_soldiers_and_workers_councils",
    "GER_proclaim_freie_sozialistische_republik", "GER_consolidate_red_republic", "GER_world_proletarian_revolution",
    "GER_alliance_with_soviet_russia", "GER_dissolve_the_junker_officer_caste", "GER_socialist_land_and_factory_collectivization",
    "GER_entente_anti_bolshevik_intervention", "GER_kiel_sailors_mutiny", "GER_collapse_of_central_allies",
    "GER_fleet_sortie_order_mutiny", "GER_kaiser_abdication_amerongen", "GER_seek_armistice_fourteen_points",
    "GER_dissolve_the_reichstag", "GER_kapp_and_tirpitz_rally", "GER_the_black_day_of_the_german_army",
    "GER_armistice_at_compiegne",
]


def ai_text(flag=None):
    if flag:
        return "ai_will_do = { factor = 0 modifier = { add = 100 has_country_flag = %s } }" % flag
    return "ai_will_do = { factor = 0 }"


def patch_russia_tree():
    path = ROOT / "common/national_focus/soviet.txt"
    ids, nodes, text = P.all_ids(path)
    if MARK in text:
        print("soviet.txt ja remendado")
        return
    ops = {}
    def add(i, *o):
        ops.setdefault(i, []).extend(o)
    for i, d in RUS_DATES.items():
        add(i, ("available", "date > " + d))
    # nenhum foco da IA sem peso: padrao 10 para quem nao tem
    for i in ids:
        if i not in ("SOV_february_bread_riots_1917", "SOV_mutiny_of_petrograd_garrison", "SOV_abdication_at_pskov",
                     "SOV_murder_of_rasputin", "SOV_the_kornilov_affair", "SOV_provisional_government_formed",
                     "SOV_all_power_to_the_soviets", "SOV_kornilov_iron_dictatorship", "SOV_convene_constituent_assembly",
                     "SOV_the_tsar_refuses_abdication"):
            add(i, ("ai", "ai_will_do = { factor = 10 }"))
    # cadeia de fevereiro: so com a janela aberta (ou na data historica); a IA deixa aos eventos
    for i in ("SOV_february_bread_riots_1917", "SOV_mutiny_of_petrograd_garrison", "SOV_abdication_at_pskov"):
        add(i, ("available", "OR = { has_country_flag = SOV_revolution_window_open date > 1917.2.20 }"),
            ("bypass", "has_country_flag = SOV_tsar_abdicated"), ("ai", ai_text()))
    add("SOV_murder_of_rasputin", ("bypass", "has_country_flag = SOV_rasputin_dead"), ("ai", ai_text()))
    add("SOV_provisional_government_formed", ("bypass", "has_country_flag = SOV_provisional_gov_in_power"),
        ("reward", "set_country_flag = SOV_provisional_gov_in_power"), ("ai", ai_text("SOV_provisional_gov_open")))
    add("SOV_the_kornilov_affair", ("bypass", "OR = { has_country_flag = SOV_path_bolshevik has_country_flag = SOV_path_kornilov has_country_flag = SOV_path_democratic }"),
        ("available", "has_country_flag = SOV_provisional_gov_in_power"), ("ai", ai_text("SOV_provisional_gov_in_power")))
    # ramos excludentes decididos pelos eventos
    add("SOV_all_power_to_the_soviets", ("available", "has_country_flag = SOV_path_bolshevik"),
        ("mex", ["SOV_kornilov_iron_dictatorship", "SOV_convene_constituent_assembly"]), ("ai", ai_text("SOV_path_bolshevik")))
    add("SOV_kornilov_iron_dictatorship", ("available", "has_country_flag = SOV_path_kornilov"),
        ("mex", ["SOV_all_power_to_the_soviets", "SOV_convene_constituent_assembly"]), ("ai", ai_text("SOV_path_kornilov")))
    add("SOV_convene_constituent_assembly", ("available", "has_country_flag = SOV_path_democratic"),
        ("mex", ["SOV_all_power_to_the_soviets", "SOV_kornilov_iron_dictatorship"]), ("ai", ai_text("SOV_path_democratic")))
    add("SOV_the_tsar_refuses_abdication", ("available", "has_country_flag = SOV_path_tsarist"),
        ("mex", ["SOV_abdication_at_pskov", "SOV_provisional_government_formed"]), ("ai", ai_text("SOV_path_tsarist")))
    add("SOV_abdication_at_pskov", ("mex", ["SOV_the_tsar_refuses_abdication"]))
    add("SOV_provisional_government_formed", ("mex", ["SOV_the_tsar_refuses_abdication"]))
    n = P.patch_tree(path, ops)
    t = path.read_bytes().decode("utf-8-sig")
    path.write_bytes((MARK + "\n" + t).encode("utf-8"))
    print("soviet.txt: %d focos remendados" % n)


def patch_germany_tree():
    path = ROOT / "common/national_focus/germany.txt"
    ids, nodes, text = P.all_ids(path)
    if MARK in text:
        print("germany.txt ja remendado")
        return
    ops = {}
    def add(i, *o):
        ops.setdefault(i, []).extend(o)
    for i, d in GER_DATES.items():
        add(i, ("available", "date > " + d))
    for i in GER_AI0:
        add(i, ("ai", ai_text()))
    add("GER_constitutional_monarchy_proclamation", ("ai", ai_text("GER_october_reforms")))
    add("GER_kiel_sailors_mutiny", ("bypass", "has_country_flag = GER_kiel_mutiny_underway"))
    add("GER_kaiser_abdication_amerongen", ("available", "OR = { has_country_flag = GER_republic_proclaimed has_capitulated = yes }"),
        ("bypass", "has_country_flag = GER_kaiser_abdicated"))
    n = P.patch_tree(path, ops)
    t = path.read_bytes().decode("utf-8-sig")
    path.write_bytes((MARK + "\n" + t).encode("utf-8"))
    print("germany.txt: %d focos remendados" % n)


def main():
    write_new_files()
    patch_russia_events()
    patch_popularities()
    patch_russia_tree()
    patch_germany_tree()
    print("eventos:", len(L.EVENTS), "| ideias:", len(L.IDEAS), "| categorias:", len(L.CATEGORIES),
          "| decisoes:", sum(len(v) for v in L.DECISIONS.values()), "| chaves de texto EN/PT:",
          len(L.LOC["english"]), len(L.LOC["braz_por"]))


if __name__ == "__main__":
    main()
