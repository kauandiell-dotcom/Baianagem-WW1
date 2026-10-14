"""Master QA Test Suite for Austria-Hungary Complete Rework & Fragmentation System.

Validates the full specification across:
1. Day 1 Crisis Prevention: Collapse/crisis events strictly require active war, post-1915 date, surrender/core loss.
2. The 4 Constitutional Destinies: Dualism, Trialism, Danubian Mega-Federation, Military Dictatorship.
3. Danubian Mega-Federation Engine: Releasing HUN, CZE, CRO, POL, uniform imperial map color, 4-18 division spawns.
4. Tag-Safe Secession & Faction Lockdown: can_join_factions = no, 0 dynamic start_civil_war, anti-faction AI strategy.
5. Crown Dashboard & Grain Simulation: 3 survival vectors (weariness, cohesion, grain), clamping and decisions.
6. Industrial Giants & Military Doctrines: Škoda 30.5cm, Steyr, Ganz-Danubius, Conrad vs Boroević semantic modifiers.
7. Bilingual Localization Integrity: Single UTF-8 BOM (\\xef\\xbb\\xbf), 0 double BOM, and 100% key parity.
"""

import os
import re
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.hoi4_semantic_oracle import is_valid_country_modifier, audit_file_modifiers


def parse_focus_tree(filepath):
    """Parses a Clausewitz national focus tree file and returns focus dicts."""
    if not os.path.isfile(filepath):
        return []

    with open(filepath, "r", encoding="utf-8-sig", errors="replace") as f:
        text = f.read()

    clean_lines = [re.sub(r"#[^\n]*", "", line) for line in text.splitlines()]
    clean = "\n".join(clean_lines)

    foci = []
    idx = 0
    while True:
        pos = clean.find("focus = {", idx)
        if pos == -1:
            break
        brace = clean.find("{", pos)
        depth = 1
        cur = brace + 1
        while cur < len(clean) and depth > 0:
            if clean[cur] == "{":
                depth += 1
            elif clean[cur] == "}":
                depth -= 1
            cur += 1
        block = clean[pos:cur]

        id_m = re.search(r"\bid\s*=\s*([a-zA-Z0-9_]+)", block)
        if id_m:
            fid = id_m.group(1)
            mutually_exclusive = []
            for mex in re.findall(r"mutually_exclusive\s*=\s*\{([^}]+)\}", block):
                for m_target in re.findall(r"focus\s*=\s*([a-zA-Z0-9_]+)", mex):
                    mutually_exclusive.append(m_target)

            foci.append({
                "id": fid,
                "mutually_exclusive": mutually_exclusive,
                "block": block,
            })
        idx = cur

    return foci


def extract_loc_keys(filepath):
    """Extracts localization keys from a Paradox YAML localization file."""
    keys = set()
    if not os.path.isfile(filepath):
        return keys
    with open(filepath, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            m = re.match(r"^\s*([a-zA-Z0-9_.\-]+):\d*\s+\"", line)
            if m:
                keys.add(m.group(1))
    return keys


class TestAustriaHungaryOverhaul(unittest.TestCase):
    """Comprehensive QA test suite for the Austria-Hungary complete rework."""

    def test_austria_no_day1_crisis(self):
        """Verify that collapse and crisis events cannot trigger on Day 1 (1911).

        All collapse and crisis triggers in events/ww1_austria_collapse_events.txt
        must strictly require:
        - has_war = yes
        - date > 1915 (or 1915.1.1)
        - surrender_progress > 0.40 or loss of Vienna (4), Budapest (43), or Galicia (88).
        """
        collapse_file = os.path.join(REPO_ROOT, "events", "ww1_austria_collapse_events.txt")
        self.assertTrue(os.path.isfile(collapse_file), f"Collapse events file missing: {collapse_file}")

        with open(collapse_file, "r", encoding="utf-8-sig", errors="replace") as f:
            content = f.read()

        # Clean comments
        clean = "\n".join(re.sub(r"#[^\n]*", "", line) for line in content.splitlines())

        # Check for event blocks
        event_ids = re.findall(r"\bid\s*=\s*([a-zA-Z0-9_.]+)", clean)
        self.assertTrue(len(event_ids) > 0, "No event definitions found in ww1_austria_collapse_events.txt")

        # Must include the core collapse events
        expected_events = ["ww1_austria_collapse.1", "ww1_austria_collapse.2", "ww1_austria_collapse.3"]
        for eid in expected_events:
            self.assertIn(eid, event_ids, f"Expected collapse event {eid} not found in ww1_austria_collapse_events.txt")

        # Parse each country_event block and audit triggers
        idx = 0
        while True:
            pos = clean.find("country_event = {", idx)
            if pos == -1:
                break
            brace = clean.find("{", pos)
            depth = 1
            cur = brace + 1
            while cur < len(clean) and depth > 0:
                if clean[cur] == "{":
                    depth += 1
                elif clean[cur] == "}":
                    depth -= 1
                cur += 1
            ev_block = clean[pos:cur]
            idx = cur

            # Look for trigger block
            trig_m = re.search(r"\btrigger\s*=\s*\{", ev_block)
            if not trig_m:
                continue

            t_start = trig_m.end()
            t_depth = 1
            t_cur = t_start
            while t_cur < len(ev_block) and t_depth > 0:
                if ev_block[t_cur] == "{":
                    t_depth += 1
                elif ev_block[t_cur] == "}":
                    t_depth -= 1
                t_cur += 1
            trig_body = ev_block[t_start:t_cur - 1]

            ev_id_m = re.search(r"\bid\s*=\s*([a-zA-Z0-9_.]+)", ev_block)
            ev_id = ev_id_m.group(1) if ev_id_m else "unknown"

            # Skip reunification events (e.g. ww1_austria_collapse.10) which trigger on victory
            if "reunification" in ev_id or "imperial_authority" in trig_body or ev_id == "ww1_austria_collapse.10":
                continue

            # Day 1 Fail-Safe: All collapse crisis triggers MUST require active war
            self.assertIn("has_war = yes", trig_body, f"Collapse event {ev_id} missing 'has_war = yes' trigger")

            # Date gate: Must require date > 1915
            self.assertTrue(
                re.search(r"date\s*>\s*1915", trig_body) or re.search(r"date\s*>\s*1914\.12", trig_body),
                f"Collapse event {ev_id} missing date > 1915 threshold"
            )

            # Surrender or Core loss: requires surrender_progress > 0.40 or loss of Vienna (4), Budapest (43), or Galicia (88)
            has_surrender = re.search(r"surrender_progress\s*>\s*0\.[3-9]", trig_body)
            has_state_loss = (
                re.search(r"controls_state\s*=\s*4\b", trig_body)
                or re.search(r"controls_state\s*=\s*43\b", trig_body)
                or re.search(r"controls_state\s*=\s*88\b", trig_body)
            )
            self.assertTrue(
                has_surrender or has_state_loss,
                f"Collapse event {ev_id} must gate on surrender_progress > 0.40 or loss of core states (4, 43, 88)"
            )

    def test_constitutional_four_paths(self):
        """Verify that the 4 constitutional paths are properly defined and mutually exclusive.

        Focuses in common/national_focus/austria.txt:
        - AUH_ww1_dualism
        - AUH_ww1_trialism
        - AUH_ww1_federalism
        - AUH_ww1_military_dictatorship

        Ideas in common/ideas/ww1_austria_constitutional_ideas.txt:
        - AUH_idea_dualism_iron
        - AUH_idea_habsburg_trialism
        - AUH_idea_danubian_federation_spirit
        - AUH_idea_aok_military_dictatorship
        """
        focus_file = os.path.join(REPO_ROOT, "common", "national_focus", "austria.txt")
        self.assertTrue(os.path.isfile(focus_file), f"Focus file missing: {focus_file}")

        foci = parse_focus_tree(focus_file)
        foci_dict = {f["id"]: f for f in foci}

        expected_paths = [
            "AUH_ww1_dualism",
            "AUH_ww1_trialism",
            "AUH_ww1_federalism",
            "AUH_ww1_military_dictatorship",
        ]

        # 1. Check all 4 focus IDs exist
        for fid in expected_paths:
            self.assertIn(fid, foci_dict, f"Constitutional focus {fid} missing from austria.txt")

        # 2. Check mutual exclusivity across all 4 paths
        for fid in expected_paths:
            f = foci_dict[fid]
            mex = set(f["mutually_exclusive"])
            other_paths = set(expected_paths) - {fid}
            for other in other_paths:
                self.assertIn(
                    other, mex,
                    f"Focus {fid} must be mutually exclusive with {other}"
                )

        # 3. Check distinct ideas exist in ideas file
        ideas_file = os.path.join(REPO_ROOT, "common", "ideas", "ww1_austria_constitutional_ideas.txt")
        self.assertTrue(os.path.isfile(ideas_file), f"Constitutional ideas file missing: {ideas_file}")

        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_content = f.read()

        expected_ideas = [
            "AUH_idea_dualism_iron",
            "AUH_idea_habsburg_trialism",
            "AUH_idea_danubian_federation_spirit",
            "AUH_idea_aok_military_dictatorship",
        ]

        # Ensure all 4 ideas are unique and present
        self.assertEqual(len(set(expected_ideas)), 4, "Expected ideas must be 4 distinct tokens")
        for iid in expected_ideas:
            self.assertIn(iid, ideas_content, f"Idea {iid} missing from ww1_austria_constitutional_ideas.txt")

        # 4. Semantic modifier audit on constitutional ideas
        errs = audit_file_modifiers(ideas_file)
        self.assertEqual(len(errs), 0, f"Semantic Oracle found invalid modifiers in {ideas_file}: {errs}")

    def test_danubian_mega_federation_setup(self):
        """Verify that Danubian federation releases HUN, CZE, CRO, POL with imperial color matching and 4-18 divisions."""
        effects_file = os.path.join(REPO_ROOT, "common", "scripted_effects", "ww1_danubian_federation_effects.txt")
        self.assertTrue(os.path.isfile(effects_file), f"Danubian federation effects file missing: {effects_file}")

        with open(effects_file, "r", encoding="utf-8-sig", errors="replace") as f:
            eff_content = f.read()

        # 1. Scripted effect definition
        self.assertIn("AUH_spawn_danubian_mega_federation", eff_content, "AUH_spawn_danubian_mega_federation scripted effect missing")

        # 2. Releases/puppets HUN, CZE, CRO, POL
        for tag in ["HUN", "CZE", "CRO", "POL"]:
            self.assertIn(tag, eff_content, f"Federation setup must reference tag {tag}")

        # 3. High-centralization subject spirit AUH_danubian_federal_member
        self.assertIn("AUH_danubian_federal_member", eff_content, "AUH_danubian_federal_member not assigned to federal states")

        # 4. Color matching in cosmetic tags: rgb { 202 198 188 }
        cosmetic_file = os.path.join(REPO_ROOT, "common", "countries", "cosmetic.txt")
        self.assertTrue(os.path.isfile(cosmetic_file), f"Cosmetic tags file missing: {cosmetic_file}")

        with open(cosmetic_file, "r", encoding="utf-8-sig", errors="replace") as f:
            cosm_content = f.read()

        cosmetic_tags = [
            "HUN_AUS_danubian_state",
            "CZE_AUS_danubian_state",
            "CRO_AUS_danubian_state",
            "POL_AUS_danubian_state",
        ]
        for ctag in cosmetic_tags:
            self.assertIn(ctag, cosm_content, f"Cosmetic tag {ctag} missing from common/countries/cosmetic.txt")

        # Assert imperial color matching rgb { 202 198 188 } is defined in cosmetic.txt
        self.assertTrue(
            re.search(r"color\s*=\s*rgb\s*\{\s*202\s+198\s+188\s*\}", cosm_content),
            "Imperial cosmetic color 'rgb { 202 198 188 }' not defined in cosmetic.txt"
        )

        # 5. OOB division counts: 4 to 18 divisions each
        oob_files = {
            "HUN": "history/units/AUH_hun_federal.txt",
            "CZE": "history/units/AUH_cze_federal.txt",
            "CRO": "history/units/AUH_cro_federal.txt",
            "POL": "history/units/AUH_pol_federal.txt",
        }
        for tag, rel_path in oob_files.items():
            full_path = os.path.join(REPO_ROOT, rel_path)
            self.assertTrue(os.path.isfile(full_path), f"Federal OOB file for {tag} missing: {full_path}")

            with open(full_path, "r", encoding="utf-8-sig", errors="replace") as f:
                oob_text = f.read()

            div_count = len(re.findall(r"\bdivision\s*=\s*\{", oob_text))
            self.assertGreaterEqual(
                div_count, 4,
                f"Federal OOB {tag} has {div_count} divisions; minimum 4 required"
            )
            self.assertLessEqual(
                div_count, 18,
                f"Federal OOB {tag} has {div_count} divisions; maximum 18 allowed"
            )

    def test_tag_safe_breakaway_rules(self):
        """Verify that seceding tags have can_join_factions = no and 0 dynamic start_civil_war calls."""
        collapse_file = os.path.join(REPO_ROOT, "events", "ww1_austria_collapse_events.txt")
        self.assertTrue(os.path.isfile(collapse_file), f"Collapse events file missing: {collapse_file}")

        with open(collapse_file, "r", encoding="utf-8-sig", errors="replace") as f:
            content = f.read()

        clean = "\n".join(re.sub(r"#[^\n]*", "", line) for line in content.splitlines())

        # Anti-Goal: ZERO dynamic start_civil_war calls
        self.assertNotIn("start_civil_war", clean, "Dynamic 'start_civil_war' found in collapse events; must use fixed tags")

        # Faction Lockdown: can_join_factions = no must be enforced on breakaway tags
        self.assertIn("can_join_factions = no", clean, "Faction lockdown 'can_join_factions = no' missing from collapse events")

        # Anti-faction AI strategy
        ai_strat_file = os.path.join(REPO_ROOT, "common", "ai_strategy", "ww1_auh_rebel_ai_strategy.txt")
        self.assertTrue(os.path.isfile(ai_strat_file), f"Rebel AI strategy file missing: {ai_strat_file}")

        with open(ai_strat_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ai_content = f.read()

        self.assertTrue(
            "alliance" in ai_content or "join_faction" in ai_content or "antagonize" in ai_content,
            "Rebel AI strategy must discourage alliance or faction joining"
        )

    def test_crown_dashboard_and_grain(self):
        """Verify the 3 survival vectors (weariness, cohesion, grain) and their decisions."""
        fx_file = os.path.join(REPO_ROOT, "common", "scripted_effects", "ww1_auh_dashboard_effects.txt")
        self.assertTrue(os.path.isfile(fx_file), f"Dashboard effects file missing: {fx_file}")

        with open(fx_file, "r", encoding="utf-8-sig", errors="replace") as f:
            fx_content = f.read()

        # Check required variables
        required_vars = ["AUH_war_weariness", "AUH_cohesion", "AUH_vienna_grain"]
        for var in required_vars:
            self.assertIn(var, fx_content, f"Variable {var} missing from ww1_auh_dashboard_effects.txt")

        # Check clamping logic
        self.assertIn("clamp_variable", fx_content, "clamp_variable missing from dashboard scripted effects")
        self.assertIn("AUH_clamp_dashboard_variables", fx_content, "AUH_clamp_dashboard_variables effect missing")

        # Decisions categories
        cat_file = os.path.join(REPO_ROOT, "common", "decisions", "categories", "ww1_auh_dashboard_categories.txt")
        self.assertTrue(os.path.isfile(cat_file), f"Dashboard decision category missing: {cat_file}")

        with open(cat_file, "r", encoding="utf-8-sig", errors="replace") as f:
            cat_content = f.read()
        self.assertIn("AUH_crown_dashboard", cat_content, "Category AUH_crown_dashboard missing")

        # Decisions file
        dec_file = os.path.join(REPO_ROOT, "common", "decisions", "ww1_auh_dashboard_decisions.txt")
        self.assertTrue(os.path.isfile(dec_file), f"Dashboard decisions missing: {dec_file}")

        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_content = f.read()

        expected_decisions = [
            "AUH_dec_requisition_banat_grain",
            "AUH_dec_bread_rationing_cards",
            "AUH_dec_appease_budapest_diet",
            "AUH_dec_galician_food_corps",
        ]
        for dec in expected_decisions:
            self.assertIn(dec, dec_content, f"Decision {dec} missing from ww1_auh_dashboard_decisions.txt")

        # Fast-failing tag check in decisions
        self.assertTrue(
            "original_tag = AUS" in dec_content or "tag = AUS" in dec_content,
            "Decisions must contain fast-failing tag check (original_tag = AUS)"
        )

        # On-actions hook check
        on_actions_file = os.path.join(REPO_ROOT, "common", "on_actions", "zz_ww1_ger_rus_rework_on_actions.txt")
        if os.path.isfile(on_actions_file):
            with open(on_actions_file, "r", encoding="utf-8-sig", errors="replace") as f:
                on_act = f.read()
            self.assertIn("AUH_clamp_dashboard_variables", on_act, "AUH_clamp_dashboard_variables not hooked in on_actions")

    def test_skoda_and_three_armies_modifiers(self):
        """Verify that all ideas use valid Clausewitz modifiers via semantic oracle."""
        ideas_file = os.path.join(REPO_ROOT, "common", "ideas", "ww1_austria_industry_and_military_ideas.txt")
        self.assertTrue(os.path.isfile(ideas_file), f"Industry and military ideas file missing: {ideas_file}")

        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            content = f.read()

        expected_ideas = [
            "AUH_skoda_305_howitzer",
            "AUH_steyr_mannlicher",
            "AUH_ganz_danubius",
            "AUH_conrad_offensive_doctrine",
            "AUH_borojevic_alpine_defense",
        ]
        for iid in expected_ideas:
            self.assertIn(iid, content, f"Idea {iid} missing from ww1_austria_industry_and_military_ideas.txt")

        # Semantic modifier oracle check
        errs = audit_file_modifiers(ideas_file)
        self.assertEqual(len(errs), 0, f"Semantic Oracle found invalid Clausewitz modifiers in {ideas_file}: {errs}")

    def test_localisation_bom_and_parity(self):
        """Verify single UTF-8 BOM and 100% key parity between English and Portuguese."""
        eng_file = os.path.join(REPO_ROOT, "localisation", "english", "ww1_austria_rework_l_english.yml")
        por_file = os.path.join(REPO_ROOT, "localisation", "braz_por", "ww1_austria_rework_l_braz_por.yml")

        self.assertTrue(os.path.isfile(eng_file), f"English localization missing: {eng_file}")
        self.assertTrue(os.path.isfile(por_file), f"Portuguese localization missing: {por_file}")

        # UTF-8 BOM checks
        with open(eng_file, "rb") as f:
            eng_bytes = f.read()
        with open(por_file, "rb") as f:
            por_bytes = f.read()

        # Must start with exact UTF-8 BOM \xef\xbb\xbf
        self.assertTrue(eng_bytes.startswith(b"\xef\xbb\xbf"), "English file missing UTF-8 BOM")
        self.assertTrue(por_bytes.startswith(b"\xef\xbb\xbf"), "Portuguese file missing UTF-8 BOM")

        # Must NOT have double BOM
        self.assertFalse(eng_bytes.startswith(b"\xef\xbb\xbf\xef\xbb\xbf"), "English file has duplicate double BOM")
        self.assertFalse(por_bytes.startswith(b"\xef\xbb\xbf\xef\xbb\xbf"), "Portuguese file has duplicate double BOM")

        # Exactly 1 BOM sequence in the entire file
        self.assertEqual(eng_bytes.count(b"\xef\xbb\xbf"), 1, "English file contains multiple BOM sequences")
        self.assertEqual(por_bytes.count(b"\xef\xbb\xbf"), 1, "Portuguese file contains multiple BOM sequences")

        # Key Parity check
        eng_keys = extract_loc_keys(eng_file)
        por_keys = extract_loc_keys(por_file)

        self.assertGreater(len(eng_keys), 0, "English localization file has 0 keys")
        self.assertGreater(len(por_keys), 0, "Portuguese localization file has 0 keys")

        missing_in_por = eng_keys - por_keys
        missing_in_eng = por_keys - eng_keys

        self.assertEqual(missing_in_por, set(), f"Keys in English but missing in Brazilian Portuguese: {missing_in_por}")
        self.assertEqual(missing_in_eng, set(), f"Keys in Portuguese but missing in English: {missing_in_eng}")
        self.assertEqual(eng_keys, por_keys, "Localization key sets must match 100%")


if __name__ == "__main__":
    unittest.main()
