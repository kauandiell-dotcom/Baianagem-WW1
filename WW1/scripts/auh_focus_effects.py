"""Immediate, bounded rewards for the Austria-Hungary focuses that previously only set an unlock flag.

Every entry is a short token list expanded by `expand()` into native PDX effects plus a bilingual
sentence that is appended to the focus description. Rules kept on purpose:
  * no free divisions, equipment or manpower (test_no_free_unit_or_equipment_spawns);
  * small numbers, and a cost (political power, consent, confidence or war support) wherever the
    historical choice had a price;
  * permanent spirits only for institutions the focus actually creates;
  * physical construction (railways, factories, resources, building slots, forts) reflects
    genuine map development for the Austro-Hungarian crownlands and industrial basins.
"""

def _sign(n):
    return ("+" if float(n) >= 0 else "−") + (str(abs(float(n))).rstrip("0").rstrip("."))

def _pct(n):
    v = round(abs(float(n)) * 100, 2)
    s = (str(v).rstrip("0").rstrip(".")).replace(".", ",")
    return ("+" if float(n) >= 0 else "−") + s + "%", ("+" if float(n) >= 0 else "−") + s.replace(",", ".") + "%"

STATE_NAMES = {
    4: ("Baixa Áustria (Viena)", "Lower Austria (Vienna)"),
    9: ("Boêmia (Plzeň/Praga)", "Bohemia (Plzeň/Prague)"),
    39: ("Tirol Meridional", "South Tyrol"),
    43: ("Hungria Central (Budapeste)", "Central Hungary (Budapest)"),
    70: ("Eslováquia", "Slovakia"),
    73: ("Rutênia/Stanislau", "Ruthenia/Stanislau"),
    74: ("Silésia Austríaca", "Austrian Silesia"),
    75: ("Morávia", "Moravia"),
    80: ("Bucovina", "Bukovina"),
    82: ("Banato", "Banat"),
    84: ("Transilvânia", "Transylvania"),
    89: ("Galícia (Cracóvia/Przemyśl)", "Galicia (Kraków/Przemyśl)"),
    91: ("Galícia Oriental (Drohobych)", "East Galicia (Drohobych)"),
    103: ("Croácia", "Croatia"),
    104: ("Bósnia (Sarajevo)", "Bosnia (Sarajevo)"),
    152: ("Alta Áustria (Steyr)", "Upper Austria (Steyr)"),
    153: ("Tirol (Innsbruck)", "Tyrol (Innsbruck)"),
    154: ("Hungria Ocidental (Danúbio)", "Western Hungary (Danube)"),
    163: ("Dalmácia", "Dalmatia"),
    736: ("Litoral/Trieste", "Littoral/Trieste"),
    850: ("Trentino", "Trentino"),
}

RES_NAMES = {
    "steel": ("aço", "steel"),
    "oil": ("petróleo", "oil"),
    "aluminium": ("alumínio", "aluminium"),
    "tungsten": ("tungstênio", "tungsten"),
    "rubber": ("borracha", "rubber"),
    "chromium": ("cromo", "chromium"),
}

def _fx(kind, arg):
    """Return (effect, pt, en)."""
    if kind == "pp":
        return f"add_political_power = {arg}", f"{_sign(arg)} poder político", f"{_sign(arg)} political power"
    if kind == "stab":
        p, e = _pct(arg)
        return f"add_stability = {arg}", f"{p} estabilidade", f"{e} stability"
    if kind == "ws":
        p, e = _pct(arg)
        return f"add_war_support = {arg}", f"{p} apoio à guerra", f"{e} war support"
    if kind == "cons":
        return f"add_to_variable = {{ auh_ww1_consent = {arg} }}", f"{_sign(arg)} consentimento", f"{_sign(arg)} consent"
    if kind == "coh":
        return f"add_to_variable = {{ auh_ww1_cohesion = {arg} }}", f"{_sign(arg)} confiança provincial", f"{_sign(arg)} provincial confidence"
    if kind == "prov":
        return f"add_to_variable = {{ auh_ww1_provisions = {arg} }}", f"{_sign(arg)} reservas alimentares", f"{_sign(arg)} food reserves"
    if kind == "debt":
        return f"add_to_variable = {{ auh_ww1_debt = {arg} }}", f"{_sign(arg)} nível de dívida", f"{_sign(arg)} debt level"
    if kind == "axp":
        return f"army_experience = {arg}", f"{_sign(arg)} experiência terrestre", f"{_sign(arg)} army experience"
    if kind == "nxp":
        return f"navy_experience = {arg}", f"{_sign(arg)} experiência naval", f"{_sign(arg)} navy experience"
    if kind == "fxp":
        return f"air_experience = {arg}", f"{_sign(arg)} experiência aérea", f"{_sign(arg)} air experience"
    if kind == "cmd":
        return f"add_command_power = {arg}", f"{_sign(arg)} poder de comando", f"{_sign(arg)} command power"
    raise KeyError(kind)

# permanent institutions created by a focus: key -> (PT, EN)
SPIRITS = {
    "inst_staff_college": ("Escola de Estado-Maior", "Staff College"),
    "inst_sapper_school": ("Escola de sapadores", "Sapper School"),
    "inst_pilot_school": ("Escola de pilotos", "Pilot School"),
    "inst_investment_board": ("Junta de investimentos", "Investment Board"),
}

# focus key -> tokens
EFFECTS = {
 # --- constitution and crownlands
 "delegations": "cons:3 pp:20",
 "crownland_hearings": "coh:3 cons:-1",
 "budapest_compact": "stab:0.005 pp:20",
 "joint_budget": "cons:2 pp:-20",
 "honved_safeguards": "cons:3 coh:-1 axp:2",
 "quota_revision": "cons:3 pp:-25",
 "dual_war_cabinet": "ws:0.02 pp:15",
 "croatian_diet": "slot:103:1 coh:3 cons:-1",
 "bosnian_guarantees": "slot:104:1 coh:3 cons:-1",
 "common_customs": "stab:0.005 pp:20",
 "trialist_war_cabinet": "ws:0.02 pp:15",
 "constitutional_convention": "cons:3 coh:2 pp:-20",
 "language_rights": "stab:0.01",
 "council_of_peoples": "coh:3 pp:-15",
 "federal_common_army": "axp:4 coh:2",
 "federal_war_cabinet": "ws:0.02 pp:15",
 "bohemian_landtag": "slot:9:1 coh:2 cons:1 tech:industry:0.10",
 "moravian_compromise": "slot:75:1 coh:2 cons:1",
 "silesian_municipalities": "slot:74:1 coh:2 cons:1",
 "galician_autonomy": "slot:89:1 coh:2 prov:2",
 "ruthenian_schools": "slot:73:1 coh:3 cons:-1",
 "bukovina_compact": "slot:80:1 coh:2 cons:1",
 "slovak_petitions": "slot:70:1 coh:2 cons:-2",
 "transylvanian_guarantees": "slot:84:1 coh:2 cons:-1",
 "banat_council": "slot:82:1 coh:2 prov:2",
 "dalmatian_services": "slot:163:1 coh:2 cons:1",
 "trentino_council": "slot:850:1 coh:2 cons:1 pp:-10",
 "provincial_ombudsman": "coh:3 stab:0.01",
 # --- economy and infrastructure
 "economic_coordination": "cons:3 pp:25",
 "investment_board": "idea:inst_investment_board pp:-20",
 "pilsen_tooling": "arms:9:1 tech:artillery:0.10",
 "vitkovice_steel": "resource:75:steel:4 civ:75:1 coh:1 tech:industry:0.10",
 "steyr_small_arms": "arms:152:1 pp:-15",
 "weiss_csepel": "arms:43:1 cons:2 pp:15",
 "arsenal_standards": "cons:2 pp:-15",
 "hungarian_harvest": "prov:6 cons:-1",
 "granaries": "prov:6 pp:-20",
 "rural_exemptions": "prov:3 ws:-0.01",
 "fair_rationing": "prov:4 stab:0.005",
 "vienna_budapest_rail": "rail:4:43:2 cons:2 pp:-15",
 "prague_vienna_rail": "rail:9:4:2 coh:2",
 "galician_rail": "rail:43:89:2 coh:2",
 "bosnian_rail": "rail:43:104:2 coh:2",
 "adriatic_rail": "rail:4:736:2 coh:2",
 "railway_dispatch": "prov:2 pp:-15",
 "workers_housing": "infra:152:1 coh:3 pp:-15",
 "women_in_industry": "pp:15 coh:-1",
 "labour_arbitration": "coh:3 stab:0.01",
 "factory_canteens": "prov:4 coh:2",
 "strike_settlement": "coh:3 pp:-15",
 "common_bank": "pp:30",
 "price_inspection": "prov:3 cons:1",
 "fiscal_reserve": "debt:-1 pp:-20",
 "danube_services": "infra:154:1 prov:3 cons:1",
 "galician_oil": "resource:91:oil:4 infra:91:1 pp:15 coh:1",
 "civilian_conversion": "stab:0.005 pp:-15",
 # --- army and air service
 "staff_college": "idea:inst_staff_college",
 "sapper_school": "idea:inst_sapper_school",
 "mobilisation_tables": "axp:3 pp:-15",
 "regimental_languages": "axp:3",
 "landwehr_training": "axp:3 cons:1",
 "honved_training": "axp:3 cons:2",
 "junior_officers": "axp:3 coh:1",
 "trench_rotation": "coh:2 ws:0.01",
 "replacement_depots": "axp:2 coh:1",
 "artillery_reserves": "pp:-15 axp:2",
 "carpathian_survey": "axp:2",
 "alpine_routes": "infra:153:1 axp:2 pp:-10",
 "winter_equipment": "ws:0.01 axp:2",
 "defensive_manual": "axp:3",
 "przemysl_supply": "bunker:89:2 pp:-15 axp:2",
 "regional_defence": "coh:2 axp:2",
 "balkan_plan": "axp:2 cmd:10",
 "galician_plan": "axp:2 cmd:10",
 "isonzo_plan": "axp:2 cmd:10",
 "war_staff_review": "axp:3 pp:-20",
 "pilot_school": "idea:inst_pilot_school fxp:3",
 "airfield_services": "airbase:4:1 fxp:2 pp:-10",
 # --- diplomacy
 "consular_network": "pp:25 cons:1",
 "foreign_programme": "pp:20",
 "german_staff_exchange": "axp:3",
 "central_power_liaison": "cons:1 ws:0.01 axp:2",
 "sarajevo_services": "infra:104:1 coh:3 pp:-15",
 "balkan_restraint": "stab:0.005",
 "italian_minorities": "coh:2",
 "adriatic_consultation": "pp:15 coh:1",
 "tyrolean_services": "infra:39:1 coh:2 pp:-10",
 "italian_contingency": "axp:3 ws:0.01 coh:-1",
 "romanian_grain": "prov:4",
 "eastern_contingency": "axp:3 pp:-15",
 "eastern_refugees": "coh:3 prov:-2",
 "armistice_delegates": "pp:30 ws:-0.01",
 "conference_mandate": "pp:30",
 "peace_diplomacy": "stab:0.01 pp:25",
 # --- navy
 "naval_programme": "nxp:3 pp:-20",
 "fleet_gunnery": "nxp:3",
 "fleet_in_being": "coh:1 nxp:2",
 "trieste_yards": "dock:736:1 pp:-15 nxp:2",
 "naval_repair": "nxp:2",
 "naval_spares": "nxp:2 pp:-10",
 "dalmatian_ports": "navalbase:163:1 coh:2 nxp:2",
 "coastal_observation": "nxp:3",
 "merchant_training": "nxp:3 prov:1",
 "adriatic_supply": "prov:2 nxp:2",
 # --- postwar
 "veterans_registry": "coh:2 pp:-10",
 "reconstruction_board": "pp:40 cons:2",
 "veterans_pensions": "coh:3",
 "rehabilitation_centres": "coh:3 stab:0.005",
 "civilian_service": "stab:0.005",
 "regional_reconstruction": "coh:3 prov:3",
 "urban_reconstruction": "prov:3 cons:2",
 "peace_credit": "pp:20",
 "balanced_accounts": "debt:-1 pp:-20",
 "danubian_services": "cons:3 coh:3",
}

def expand(tokens):
    """Return (effect string, PT sentence, EN sentence)."""
    effects, pt, en = [], [], []
    for tok in tokens.split():
        parts = tok.split(":")
        tag = parts[0]
        if tag == "tech":
            cat, bonus = parts[1], parts[2]
            effects.append(f"add_tech_bonus = {{ name = AUH_ww1_research_program bonus = {bonus} uses = 1 category = {cat} }}")
            pct = int(round(float(bonus) * 100))
            pt.append(f"um auxílio único de {pct}% à pesquisa ({cat})")
            en.append(f"one {pct}% research bonus ({cat})")
        elif tag == "idea":
            name = parts[1]
            effects.append(f"add_ideas = AUH_ww1_{name}")
            pt.append(f"cria a instituição «{SPIRITS[name][0]}»")
            en.append(f"creates the “{SPIRITS[name][1]}” institution")
        elif tag == "rail":
            start, end, lvl = int(parts[1]), int(parts[2]), parts[3]
            s_pt, s_en = STATE_NAMES.get(start, (f"Estado {start}", f"State {start}"))
            e_pt, e_en = STATE_NAMES.get(end, (f"Estado {end}", f"State {end}"))
            effects.append(f"build_railway = {{ level = {lvl} start_state = {start} target_state = {end} build_only_on_allied = yes }}")
            pt.append(f"ferrovia nível {lvl} entre {s_pt} e {e_pt}")
            en.append(f"level {lvl} railway between {s_en} and {e_en}")
        elif tag == "infra":
            st, lvl = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_building_construction = {{ type = infrastructure level = {lvl} instant = yes }} }}")
            pt.append(f"+{lvl} infraestrutura em {s_pt}")
            en.append(f"+{lvl} infrastructure in {s_en}")
        elif tag == "arms":
            st, cnt = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_extra_state_shared_building_slots = {cnt} add_building_construction = {{ type = arms_factory level = {cnt} instant = yes }} }}")
            pt.append(f"+{cnt} fábrica militar e espaço para construção em {s_pt}")
            en.append(f"+{cnt} military factory and building slot in {s_en}")
        elif tag == "civ":
            st, cnt = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_extra_state_shared_building_slots = {cnt} add_building_construction = {{ type = industrial_complex level = {cnt} instant = yes }} }}")
            pt.append(f"+{cnt} fábrica civil e espaço para construção em {s_pt}")
            en.append(f"+{cnt} civilian factory and building slot in {s_en}")
        elif tag == "dock":
            st, cnt = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_extra_state_shared_building_slots = {cnt} add_building_construction = {{ type = dockyard level = {cnt} instant = yes }} }}")
            pt.append(f"+{cnt} estaleiro e espaço para construção em {s_pt}")
            en.append(f"+{cnt} dockyard and building slot in {s_en}")
        elif tag == "slot":
            st, cnt = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_extra_state_shared_building_slots = {cnt} }}")
            pt.append(f"+{cnt} espaço para construção em {s_pt}")
            en.append(f"+{cnt} building slot in {s_en}")
        elif tag == "resource":
            st, rtype, amt = int(parts[1]), parts[2], parts[3]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            r_pt, r_en = RES_NAMES.get(rtype, (rtype, rtype))
            effects.append(f"{st} = {{ add_resource = {{ type = {rtype} amount = {amt} }} }}")
            pt.append(f"+{amt} {r_pt} em {s_pt}")
            en.append(f"+{amt} {r_en} in {s_en}")
        elif tag == "bunker":
            st, lvl = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_building_construction = {{ type = bunker level = {lvl} instant = yes }} }}")
            pt.append(f"+{lvl} fortificações terrestres em {s_pt}")
            en.append(f"+{lvl} land forts in {s_en}")
        elif tag == "airbase":
            st, lvl = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_building_construction = {{ type = air_base level = {lvl} instant = yes }} }}")
            pt.append(f"+{lvl} base aérea em {s_pt}")
            en.append(f"+{lvl} air base in {s_en}")
        elif tag == "navalbase":
            st, lvl = int(parts[1]), parts[2]
            s_pt, s_en = STATE_NAMES.get(st, (f"Estado {st}", f"State {st}"))
            effects.append(f"{st} = {{ add_building_construction = {{ type = naval_base level = {lvl} instant = yes }} }}")
            pt.append(f"+{lvl} base naval em {s_pt}")
            en.append(f"+{lvl} naval base in {s_en}")
        else:
            e, p, n = _fx(parts[0], parts[1])
            effects.append(e); pt.append(p); en.append(n)
    return " ".join(effects), "Efeito imediato: " + ", ".join(pt) + ".", "Immediate effect: " + ", ".join(en) + "."

def apply(foci, loc, prefix="AUH_ww1_"):
    """Append the rewards to FOCI entries and their descriptions; returns the number of foci changed."""
    index = {a["id"]: a for a in foci}
    missing = [k for k in EFFECTS if prefix + k not in index]
    if missing:
        raise KeyError("unknown focus keys: " + ", ".join(missing))
    for key, tokens in EFFECTS.items():
        fid = prefix + key
        effect, pt, en = expand(tokens)
        index[fid]["effect"] = (index[fid]["effect"] + " " + effect).strip()
        dpt, den = loc[fid + "_desc"]
        loc[fid + "_desc"] = (dpt + " " + pt, den + " " + en)
    return len(EFFECTS)
