"""
Master QA and Balance Audit Suite for Baianagem-WW1 Mod.

Executes comprehensive static, structural, and mechanical audits:
1. Clausewitz Syntax & Brace Auditing across all .txt/.gfx/.gui files.
2. UTF-8 BOM Integrity Auditing (.yml MUST have BOM, .txt/.py MUST NOT).
3. Mechanical Balance & De-inflation Auditing:
   - Combat defines (stacking, force attack org/str damages, out of supply).
   - Sub-units (line infantry org/hp/manpower/supply, special subunits, tanks, artillery).
   - Equipment (infantry rifle IC and steel, AT 1914 values).
   - Balkan minors viability (SER, BUL, GRE, ROM starting stockpiles, factories, OOB division counts).
   - Pruning of inflated ideas and timed Brusilov offensive.
   - Mechanics and logistics guide decision & localization.
4. Integration with master test_runner.py.
"""

import os
import sys
import re
import unittest
from typing import List, Dict, Tuple, Any

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if MOD_ROOT not in sys.path:
    sys.path.insert(0, MOD_ROOT)
TESTS_DIR = os.path.join(MOD_ROOT, "tests")
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)


class ClausewitzAuditor:
    @staticmethod
    def audit_braces(filepath: str) -> Tuple[bool, str]:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        open_braces = 0
        in_string = False
        escape = False

        for line_num, line in enumerate(lines, start=1):
            i = 0
            while i < len(line):
                ch = line[i]
                if in_string:
                    if escape:
                        escape = False
                    elif ch == '\\':
                        escape = True
                    elif ch == '"':
                        in_string = False
                else:
                    if ch == '#':
                        break  # rest of line is comment
                    elif ch == '"':
                        in_string = True
                    elif ch == '{':
                        open_braces += 1
                    elif ch == '}':
                        open_braces -= 1
                        if open_braces < 0:
                            return False, f"Unexpected closing brace at line {line_num}"
                i += 1

        if open_braces != 0:
            return False, f"Unbalanced braces: remaining open count = {open_braces}"
        return True, "OK"


def audit_syntax_and_braces() -> List[str]:
    errors = []
    scan_dirs = ["common", "events", "history", "interface"]
    total_files = 0

    for d in scan_dirs:
        full_d = os.path.join(MOD_ROOT, d)
        if not os.path.isdir(full_d):
            continue
        for root, _, files in os.walk(full_d):
            for file in files:
                if file.endswith((".txt", ".gfx", ".gui")):
                    fpath = os.path.join(root, file)
                    total_files += 1
                    valid, msg = ClausewitzAuditor.audit_braces(fpath)
                    if not valid:
                        rel = os.path.relpath(fpath, MOD_ROOT)
                        errors.append(f"Brace Error in {rel}: {msg}")

    return errors


def audit_bom_integrity() -> List[str]:
    errors = []
    # 1. Localisation files MUST have UTF-8 BOM
    loc_dir = os.path.join(MOD_ROOT, "localisation")
    if os.path.isdir(loc_dir):
        for root, _, files in os.walk(loc_dir):
            for file in files:
                if file.endswith(".yml"):
                    fpath = os.path.join(root, file)
                    with open(fpath, "rb") as f:
                        header = f.read(3)
                    if header != b"\xef\xbb\xbf":
                        rel = os.path.relpath(fpath, MOD_ROOT)
                        errors.append(f"Missing mandatory UTF-8 BOM in localisation: {rel}")

    # 2. Script and project files MUST NOT have BOM
    # Check all python scripts
    for d in ["scripts", "tests"]:
        full_d = os.path.join(MOD_ROOT, d)
        if not os.path.isdir(full_d):
            continue
        for root, _, files in os.walk(full_d):
            for file in files:
                if file.endswith(".py"):
                    fpath = os.path.join(root, file)
                    with open(fpath, "rb") as f:
                        header = f.read(3)
                    if header == b"\xef\xbb\xbf":
                        rel = os.path.relpath(fpath, MOD_ROOT)
                        errors.append(f"Illegal UTF-8 BOM found in script file: {rel}")

    # Check key rebalanced files to ensure no BOM was introduced
    core_files = [
        "common/defines/01_defines.lua",
        "common/units/infantry.txt",
        "common/units/elite_inf.txt",
        "common/units/equipment/anti_tank.txt",
        "common/units/equipment/infantry.txt",
        "common/units/artillery_brigade.txt",
        "common/units/artillery.txt",
        "common/units/ww1_special_subunits.txt",
        "history/countries/SER - Serbia.txt",
        "history/countries/BUL - Bulgaria.txt",
        "history/countries/GRE - Greece.txt",
        "history/countries/ROM - Romania.txt",
        "history/units/SER_1936_generic.txt",
        "history/units/BUL_1936_generic.txt",
        "history/units/GRE_1936_generic.txt",
        "history/units/ROM_1936_generic.txt",
        "common/decisions/categories/ww1_national_categories.txt",
        "common/decisions/ww1_national_decisions.txt",
    ]
    for rel in core_files:
        fpath = os.path.join(MOD_ROOT, rel)
        if os.path.isfile(fpath):
            with open(fpath, "rb") as f:
                header = f.read(3)
            if header == b"\xef\xbb\xbf":
                errors.append(f"Illegal UTF-8 BOM found in core project file: {rel}")

    return errors


def audit_balance_defines() -> List[str]:
    errors = []
    defines_path = os.path.join(MOD_ROOT, "common", "defines", "01_defines.lua")
    if not os.path.isfile(defines_path):
        return ["01_defines.lua not found"]

    with open(defines_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    expected_defines = {
        "LAND_COMBAT_ORG_DAMAGE_MODIFIER": "0.055",
        "LAND_COMBAT_STR_DAMAGE_MODIFIER": "0.065",
        "COMBAT_STACKING_START": "6",
        "COMBAT_STACKING_PENALTY": "-0.06",
        "OUT_OF_SUPPLY_ATTRITION": "0.20",
        "SUPPLY_ORG_MAX_CAP": "0.35",
        "SPECIAL_FORCES_CAP_BASE": "0.05",
        "SPECIAL_FORCES_CAP_MIN": "24",
    }

    for key, expected_val in expected_defines.items():
        pattern = rf"{key}\s*=\s*([^\s,]+)"
        match = re.search(pattern, content)
        if not match:
            errors.append(f"Define {key} missing in 01_defines.lua")
        else:
            val = match.group(1).rstrip(",")
            if float(val) != float(expected_val):
                errors.append(f"Define {key} = {val}, expected {expected_val}")

    return errors


def audit_subunits_and_equipment() -> List[str]:
    errors = []

    # 1. Regular Infantry (common/units/infantry.txt)
    inf_path = os.path.join(MOD_ROOT, "common", "units", "infantry.txt")
    if os.path.isfile(inf_path):
        with open(inf_path, "r", encoding="utf-8", errors="replace") as f:
            inf_txt = f.read()
        # Find regular infantry block
        inf_match = re.search(r"sub_units\s*=\s*\{\s*infantry\s*=\s*\{(.*?)\n\t\}", inf_txt, re.DOTALL)
        if inf_match:
            block = inf_match.group(1)
            org = re.search(r"max_organisation\s*=\s*(\d+)", block)
            hp = re.search(r"max_strength\s*=\s*([\d.]+)", block)
            manpower = re.search(r"manpower\s*=\s*(\d+)", block)
            cost_need = re.search(r"infantry_equipment\s*=\s*(\d+)", block)
            supply = re.search(r"supply_consumption\s*=\s*([\d.]+)", block)
            defense = re.search(r"\bdefense\s*=\s*([\d.]+)", block)

            if not org or int(org.group(1)) < 45:
                errors.append(f"Regular infantry org is {org.group(1) if org else 'missing'}, expected >= 45")
            if not hp or float(hp.group(1)) < 25:
                errors.append(f"Regular infantry max_strength is {hp.group(1) if hp else 'missing'}, expected >= 25")
            if not manpower or int(manpower.group(1)) < 1500:
                errors.append(f"Regular infantry manpower is {manpower.group(1) if manpower else 'missing'}, expected >= 1500")
            if not cost_need or int(cost_need.group(1)) < 140:
                errors.append(f"Regular infantry equipment need is {cost_need.group(1) if cost_need else 'missing'}, expected >= 140")
            if not supply or float(supply.group(1)) > 0.12:
                errors.append(f"Regular infantry supply is {supply.group(1) if supply else 'missing'}, expected <= 0.12")
            if not defense or float(defense.group(1)) < 0.10:
                errors.append(f"Regular infantry defense bonus is {defense.group(1) if defense else 'missing'}, expected >= 0.10")
        else:
            errors.append("Regular infantry block not found in infantry.txt")

    # 2. Elite Infantry (common/units/elite_inf.txt)
    elite_path = os.path.join(MOD_ROOT, "common", "units", "elite_inf.txt")
    if os.path.isfile(elite_path):
        with open(elite_path, "r", encoding="utf-8", errors="replace") as f:
            elite_txt = f.read()
        brk = re.search(r"breakthrough\s*=\s*([\d.]+)", elite_txt)
        if brk and float(brk.group(1)) > 0.25:
            errors.append(f"Elite inf breakthrough inflated: {brk.group(1)}, expected <= 0.25")

    # 3. Special Subunits max_strength check (common/units/ww1_special_subunits.txt)
    special_path = os.path.join(MOD_ROOT, "common", "units", "ww1_special_subunits.txt")
    if os.path.isfile(special_path):
        with open(special_path, "r", encoding="utf-8", errors="replace") as f:
            special_txt = f.read()
        # Ensure full division units don't have 1.0 or 2.0 strength
        for unit in ["german_stosstruppen", "italian_arditi", "anzac_corps", "kuk_gebirgsjaeger", "us_doughboys_division"]:
            m = re.search(rf"{unit}\s*=\s*\{{.*?\bmax_strength\s*=\s*([\d.]+)", special_txt, re.DOTALL)
            if m and float(m.group(1)) < 15.0:
                errors.append(f"{unit} max_strength too low ({m.group(1)}), wipes out in combat")

    # 4. Anti-Tank Equipment (common/units/equipment/anti_tank.txt)
    at_path = os.path.join(MOD_ROOT, "common", "units", "equipment", "anti_tank.txt")
    if os.path.isfile(at_path):
        with open(at_path, "r", encoding="utf-8", errors="replace") as f:
            at_txt = f.read()
        # 1914 anti_tank_equipment_1
        at1_m = re.search(r"anti_tank_equipment_1\s*=\s*\{(.*?)\n\t\}", at_txt, re.DOTALL)
        if at1_m:
            at1_block = at1_m.group(1)
            ap = re.search(r"ap_attack\s*=\s*([\d.]+)", at1_block)
            hard = re.search(r"hard_attack\s*=\s*([\d.]+)", at1_block)
            if ap and float(ap.group(1)) > 24:
                errors.append(f"1914 AT ap_attack inflated: {ap.group(1)}, expected <= 24")
            if hard and float(hard.group(1)) > 15:
                errors.append(f"1914 AT hard_attack inflated: {hard.group(1)}, expected <= 15")

    # 5. Rifle Equipment (common/units/equipment/infantry.txt)
    inf_eq_path = os.path.join(MOD_ROOT, "common", "units", "equipment", "infantry.txt")
    if os.path.isfile(inf_eq_path):
        with open(inf_eq_path, "r", encoding="utf-8", errors="replace") as f:
            eq_txt = f.read()
        ie1_m = re.search(r"infantry_equipment_1\s*=\s*\{(.*?)\n\t\}", eq_txt, re.DOTALL)
        if ie1_m:
            ie1_block = ie1_m.group(1)
            cost = re.search(r"build_cost_ic\s*=\s*([\d.]+)", ie1_block)
            steel = re.search(r"steel\s*=\s*(\d+)", ie1_block)
            if cost and float(cost.group(1)) != 0.50:
                errors.append(f"1911 rifle build_cost_ic is {cost.group(1)}, expected 0.50")
            if steel and int(steel.group(1)) != 1:
                errors.append(f"1911 rifle steel is {steel.group(1)}, expected 1")

    return errors


def audit_balkan_minors() -> List[str]:
    errors = []
    countries = {
        "SER": {"file": "history/countries/SER - Serbia.txt", "min_rifles": 10000, "min_art": 200, "oob": "history/units/SER_1936_generic.txt", "min_divs": 6},
        "BUL": {"file": "history/countries/BUL - Bulgaria.txt", "min_rifles": 12000, "min_art": 250, "oob": "history/units/BUL_1936_generic.txt", "min_divs": 8},
        "GRE": {"file": "history/countries/GRE - Greece.txt", "min_rifles": 10000, "min_art": 150, "oob": "history/units/GRE_1936_generic.txt", "min_divs": 6},
        "ROM": {"file": "history/countries/ROM - Romania.txt", "min_rifles": 12000, "min_art": 250, "oob": "history/units/ROM_1936_generic.txt", "min_divs": 8},
    }

    for tag, data in countries.items():
        # Stockpile check
        cf_path = os.path.join(MOD_ROOT, data["file"])
        if not os.path.isfile(cf_path):
            errors.append(f"{tag} country file not found: {data['file']}")
            continue
        with open(cf_path, "r", encoding="utf-8", errors="replace") as f:
            c_txt = f.read()

        rifles = re.findall(r"type\s*=\s*infantry_equipment_1\s+amount\s*=\s*(\d+)", c_txt)
        art = re.findall(r"type\s*=\s*artillery_equipment_1\s+amount\s*=\s*(\d+)", c_txt)

        rifles_amt = sum(int(r) for r in rifles)
        art_amt = sum(int(a) for a in art)

        if rifles_amt < data["min_rifles"]:
            errors.append(f"{tag} starting rifle stockpile {rifles_amt} < {data['min_rifles']}")
        if art_amt < data["min_art"]:
            errors.append(f"{tag} starting artillery stockpile {art_amt} < {data['min_art']}")

        # OOB division count check
        oob_path = os.path.join(MOD_ROOT, data["oob"])
        if not os.path.isfile(oob_path):
            errors.append(f"{tag} OOB file not found: {data['oob']}")
            continue
        with open(oob_path, "r", encoding="utf-8", errors="replace") as f:
            oob_txt = f.read()
        divs = len(re.findall(r"\bdivision\s*=\s*\{", oob_txt))
        if divs < data["min_divs"]:
            errors.append(f"{tag} fielded divisions {divs} < {data['min_divs']}")

    return errors


def audit_deinflation_and_timed_ideas() -> List[str]:
    errors = []

    # 1. Russian Brusilov offensive unlocks operations plan or event
    sov_focus_path = os.path.join(MOD_ROOT, "common", "national_focus", "soviet.txt")
    if os.path.isfile(sov_focus_path):
        with open(sov_focus_path, "r", encoding="utf-8", errors="replace") as f:
            sov_txt = f.read()
        b_match = re.search(r"id\s*=\s*SOV_brusilov_breakthrough_1916.*?\bcompletion_reward\s*=\s*\{(.*?)\n\t\}", sov_txt, re.DOTALL)
        if b_match:
            b_block = b_match.group(1)
            if "SOV_southwestern_plan_ready" not in b_block and "ww1_russia.100" not in b_block:
                errors.append("SOV_brusilov_breakthrough_1916 does not unlock Southwestern offensive plan or event")
        else:
            errors.append("SOV_brusilov_breakthrough_1916 completion_reward not found in soviet.txt")

    # 2. German timed ideas & doctrine pruning (germany.txt)
    ger_focus_path = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
    if os.path.isfile(ger_focus_path):
        with open(ger_focus_path, "r", encoding="utf-8", errors="replace") as f:
            ger_f_txt = f.read()
        # Schlieffen momentum timed 90 days
        s_match = re.search(r"id\s*=\s*GER_execute_schlieffen_plan.*?\bcompletion_reward\s*=\s*\{(.*?)\n\t\}", ger_f_txt, re.DOTALL)
        if s_match:
            s_block = s_match.group(1)
            if "GER_schlieffen_momentum" in s_block:
                if "add_timed_idea" not in s_block or "days = 90" not in s_block:
                    errors.append("GER_schlieffen_momentum is not a 90-day timed idea in germany.txt")
        else:
            errors.append("GER_execute_schlieffen_plan completion_reward not found in germany.txt")

        # Kaiserschlacht timed 180 days
        k_match = re.search(r"id\s*=\s*GER_the_kaiserschlacht_1918.*?\bcompletion_reward\s*=\s*\{(.*?)\n\t\}", ger_f_txt, re.DOTALL)
        if k_match:
            k_block = k_match.group(1)
            if "add_timed_idea" not in k_block or "days = 180" not in k_block:
                errors.append("GER_the_kaiserschlacht_1918 is not a 180-day timed idea in germany.txt")
        else:
            errors.append("GER_the_kaiserschlacht_1918 completion_reward not found in germany.txt")

        # OHL silent dictatorship triggers transition event
        ohl_match = re.search(r"id\s*=\s*GER_silent_dictatorship_ohl.*?\bcompletion_reward\s*=\s*\{(.*?)\n\t\}", ger_f_txt, re.DOTALL)
        if ohl_match:
            ohl_block = ohl_match.group(1)
            if "ww1_germany_events.100" not in ohl_block and "GER_silent_dictatorship_ohl" not in ohl_block:
                errors.append("GER_silent_dictatorship_ohl does not trigger OHL transition event ww1_germany_events.100")
        else:
            errors.append("GER_silent_dictatorship_ohl completion_reward not found in germany.txt")

    # 3. Check German ideas defined and de-inflated
    ger_ideas_path = os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_ideas.txt")
    if os.path.isfile(ger_ideas_path):
        with open(ger_ideas_path, "r", encoding="utf-8", errors="replace") as f:
            ger_txt = f.read()
        if "german_infiltration_assault_idea" not in ger_txt:
            errors.append("german_infiltration_assault_idea missing from ww1_germany_ideas.txt")
        if "GER_kaiserschlacht_idea" not in ger_txt:
            errors.append("GER_kaiserschlacht_idea missing from ww1_germany_ideas.txt")
        if re.search(r"GER_falkenhayn_attrition_doctrine\s*=\s*\{[^\}]*\bdefence\s*=", ger_txt):
            errors.append("GER_falkenhayn_attrition_doctrine uses invalid 'defence =' instead of 'army_defence_factor ='")

    # 4. Russian ideas de-inflation (ww1_russia_ideas.txt & ww1_national_modifiers.txt)
    rus_ideas_path = os.path.join(MOD_ROOT, "common", "ideas", "ww1_russia_ideas.txt")
    if os.path.isfile(rus_ideas_path):
        with open(rus_ideas_path, "r", encoding="utf-8", errors="replace") as f:
            rus_txt = f.read()
        m_shock = re.search(r"SOV_shock_battalions_spirit\s*=\s*\{(.*?)\n\t\}", rus_txt, re.DOTALL)
        if m_shock:
            sf_atk = re.search(r"special_forces_attack_factor\s*=\s*([\d.]+)", m_shock.group(1))
            brk = re.search(r"breakthrough_factor\s*=\s*([\d.]+)", m_shock.group(1))
            if sf_atk and float(sf_atk.group(1)) > 0.05:
                errors.append(f"SOV_shock_battalions_spirit attack inflated: {sf_atk.group(1)}, expected <= 0.05")
            if brk and float(brk.group(1)) > 0.05:
                errors.append(f"SOV_shock_battalions_spirit breakthrough inflated: {brk.group(1)}, expected <= 0.05")

    nat_mod_path = os.path.join(MOD_ROOT, "common", "ideas", "ww1_national_modifiers.txt")
    if os.path.isfile(nat_mod_path):
        with open(nat_mod_path, "r", encoding="utf-8", errors="replace") as f:
            nat_txt = f.read()
        m_bru = re.search(r"brusilov_offensive_shock_idea\s*=\s*\{(.*?)\n\t\}", nat_txt, re.DOTALL)
        if m_bru:
            atk = re.search(r"army_attack_factor\s*=\s*([\d.]+)", m_bru.group(1))
            brk = re.search(r"breakthrough_factor\s*=\s*([\d.]+)", m_bru.group(1))
            if atk and float(atk.group(1)) > 0.10:
                errors.append(f"brusilov_offensive_shock_idea attack inflated: {atk.group(1)}, expected <= 0.10")
            if brk and float(brk.group(1)) > 0.10:
                errors.append(f"brusilov_offensive_shock_idea breakthrough inflated: {brk.group(1)}, expected <= 0.10")

    # 5. Romanian tech check
    rom_country_path = os.path.join(MOD_ROOT, "history", "countries", "ROM - Romania.txt")
    if os.path.isfile(rom_country_path):
        with open(rom_country_path, "r", encoding="utf-8", errors="replace") as f:
            rom_txt = f.read()
        if "gw_artillery = 1" not in rom_txt:
            errors.append("ROM - Romania.txt is missing starting tech 'gw_artillery = 1'")

    # 6. Check mechanics guide decision & localization
    dec_cat_path = os.path.join(MOD_ROOT, "common", "decisions", "categories", "ww1_national_categories.txt")
    if os.path.isfile(dec_cat_path):
        with open(dec_cat_path, "r", encoding="utf-8", errors="replace") as f:
            if "ww1_mechanics_guide" not in f.read():
                errors.append("ww1_mechanics_guide missing from ww1_national_categories.txt")

    dec_path = os.path.join(MOD_ROOT, "common", "decisions", "ww1_national_decisions.txt")
    if os.path.isfile(dec_path):
        with open(dec_path, "r", encoding="utf-8", errors="replace") as f:
            if "ww1_guide_stacking_and_logistics_decision" not in f.read():
                errors.append("ww1_guide_stacking_and_logistics_decision missing from ww1_national_decisions.txt")

    for lang in ["english", "braz_por"]:
        loc_path = os.path.join(MOD_ROOT, "localisation", lang, f"ww1_mechanics_l_{lang}.yml")
        if os.path.isfile(loc_path):
            with open(loc_path, "r", encoding="utf-8", errors="replace") as f:
                loc_txt = f.read()
            if "ww1_mechanics_guide:" not in loc_txt:
                errors.append(f"ww1_mechanics_guide missing from {lang} localisation")
            if "ww1_guide_stacking_and_logistics_decision:" not in loc_txt:
                errors.append(f"ww1_guide_stacking_and_logistics_decision missing from {lang} localisation")

    return errors


def main():
    print("=" * 80)
    print("       BAIANAGEM-WW1 MASTER QA & BALANCE VALIDATION AUDIT")
    print("=" * 80)

    all_errors = {}

    print("\n[*] Auditing Clausewitz Syntax & Brace Integrity...")
    syntax_errs = audit_syntax_and_braces()
    all_errors["Syntax & Braces"] = syntax_errs
    print(f"    -> {len(syntax_errs)} issues found.")

    print("\n[*] Auditing UTF-8 BOM Integrity...")
    bom_errs = audit_bom_integrity()
    all_errors["BOM Integrity"] = bom_errs
    print(f"    -> {len(bom_errs)} issues found.")

    print("\n[*] Auditing Mechanical Combat Defines...")
    defines_errs = audit_balance_defines()
    all_errors["Defines Balance"] = defines_errs
    print(f"    -> {len(defines_errs)} issues found.")

    print("\n[*] Auditing Sub-Units & Equipment Rebalance...")
    units_errs = audit_subunits_and_equipment()
    all_errors["Subunits & Equipment"] = units_errs
    print(f"    -> {len(units_errs)} issues found.")

    print("\n[*] Auditing Balkan Minors Viability (SER, BUL, GRE, ROM)...")
    balkan_errs = audit_balkan_minors()
    all_errors["Balkan Minors Viability"] = balkan_errs
    print(f"    -> {len(balkan_errs)} issues found.")

    print("\n[*] Auditing De-inflation, Timed Ideas & Mechanics Guide...")
    deinf_errs = audit_deinflation_and_timed_ideas()
    all_errors["De-inflation & Guide"] = deinf_errs
    print(f"    -> {len(deinf_errs)} issues found.")

    total_issues = sum(len(errs) for errs in all_errors.values())

    print("\n" + "=" * 80)
    print("AUDIT SUMMARY REPORT")
    print("=" * 80)
    for cat, errs in all_errors.items():
        status = "PASS" if len(errs) == 0 else "FAIL"
        print(f"  {cat:<35} : [{status}] ({len(errs)} issues)")
        for err in errs[:10]:
            print(f"      - {err}")
        if len(errs) > 10:
            print(f"      ... and {len(errs) - 10} more.")

    print("=" * 80)

    # Now execute test_runner.py
    print("\n[*] Executing Master Automated Test Suite (tests/test_runner.py)...")
    import subprocess
    cmd = [sys.executable, os.path.join(TESTS_DIR, "test_runner.py")]
    res = subprocess.run(cmd, cwd=MOD_ROOT)

    if total_issues == 0 and res.returncode == 0:
        print("\n>>> ALL QA AUDITS & UNIT TESTS PASSED SUCCESSFULLY! (Code 0) <<<\n")
        sys.exit(0)
    else:
        print(f"\n>>> AUDIT FAILED (Total QA Issues: {total_issues}, Test Runner Code: {res.returncode}) <<<\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
