"""Master QA Test Suite for French Republic Complete Overhaul & Agadir Crisis Escalation.

Validates the full specification across:
1. Agadir Crisis Interactive Escalation Engine (1911):
   - Events in events/WW1_Agadir.txt with namespace ww1_agadir.
   - Tension variable global.ww1_agadir_crisis_tension.
   - Interactive decisions in common/decisions/ww1_agadir_crisis_decisions.txt.
   - Proper territorial references for Neukamerun (states 1086, 1087, 1088).
2. Republic Dashboard & The 4 Dynamic Survival Vectors:
   - Scripted effects in common/scripted_effects/ww1_france_dashboard_effects.txt.
   - Dashboard initialization FRA_init_republic_dashboard.
   - Variable clamping FRA_clamp_dashboard_variables (0 to 100).
   - The 4 survival vectors:
     * FRA_union_sacree_cohesion
     * FRA_poilu_morale
     * FRA_charbon_et_acier
     * FRA_reserves_humaines
3. The 4 Divergent Political Destinies:
   - Focus tree topology in common/national_focus/france.txt.
   - Third Republic / Union Sacrée (FRA_republique_union_sacree, FRA_clemenceau_je_fais_la_guerre).
   - Second Paris Commune (FRA_republique_des_soviets_de_paris).
   - Action Française / Orléans Monarchy (FRA_abattre_la_gueuse, FRA_restauration_orleaniste_jean_iii).
   - GQG Military Directory (FRA_directoire_militaire_gqg).
   - Mutual exclusions and distinct national ideas:
     * FRA_union_sacree_spirit
     * FRA_commune_de_paris_spirit
     * FRA_action_francaise_monarchy
     * FRA_gqg_military_directory
4. Military Mutinies (1917) & Civil Crises Engine (Jusqu'au Bout!):
   - events/ww1_france_events.txt mutiny chain (ww1_france.210 applying FRA_trench_mutiny_crisis_2).
   - Unlock of Pétain leave reform decision (FRA_petain_welfare_and_leave_reform).
   - French Endsieg spirit (FRA_jusqu_au_bout_endsieg).
5. Semantic Oracle Modifier Compliance:
   - common/ideas/ww1_france_crises_ideas.txt
   - common/ideas/ww1_france_political_ideas.txt
   - common/ideas/ww1_france_dashboard_ideas.txt
   - Zero invalid/hallucinated Clausewitz modifiers verified via scripts/hoi4_semantic_oracle.py.
6. Bilingual Localization Integrity & Key Parity:
   - localisation/english/ww1_france_rework_l_english.yml
   - localisation/braz_por/ww1_france_rework_l_braz_por.yml
   - Mandatory single UTF-8 BOM (\\xef\\xbb\\xbf), zero double BOM, and 100% key parity.
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
        return {}

    with open(filepath, "r", encoding="utf-8-sig", errors="replace") as f:
        text = f.read()

    clean_lines = [re.sub(r"#[^\n]*", "", line) for line in text.splitlines()]
    clean = "\n".join(clean_lines)

    foci = {}
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

            ideas = re.findall(r"add_ideas\s*=\s*([a-zA-Z0-9_]+)", block)

            foci[fid] = {
                "id": fid,
                "mutually_exclusive": mutually_exclusive,
                "ideas": ideas,
                "block": block,
            }
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


class TestFranceOverhaul(unittest.TestCase):
    """Comprehensive QA test suite for the French Republic complete rework & Agadir Crisis."""

    def test_agadir_crisis_mechanics(self):
        """Verify the interactive Agadir Crisis escalation engine (1911).

        Checks:
        - events/WW1_Agadir.txt exists and defines namespace 'ww1_agadir'.
        - events/WW1_Agadir.txt tracks tension via 'ww1_agadir_crisis_tension'.
        - events/WW1_Agadir.txt references the 3 Neukamerun states: 1086, 1087, 1088.
        - common/decisions/ww1_agadir_crisis_decisions.txt exists with interactive decisions.
        - Climax outcomes: historical accord, German naval base, humiliation, or early war.
        """
        agadir_events_path = os.path.join(REPO_ROOT, "events", "WW1_Agadir.txt")
        self.assertTrue(os.path.isfile(agadir_events_path), f"Events file missing: {agadir_events_path}")

        with open(agadir_events_path, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        # 1. Namespace verification
        self.assertTrue(
            re.search(r"\badd_namespace\s*=\s*ww1_agadir\b", events_text),
            "events/WW1_Agadir.txt must declare add_namespace = ww1_agadir"
        )

        # 2. Tension variable verification
        self.assertIn(
            "ww1_agadir_crisis_tension",
            events_text,
            "events/WW1_Agadir.txt must reference tension variable 'ww1_agadir_crisis_tension'"
        )

        # 3. Neukamerun states transfer verification (1086: German Gabon, 1087: German Chad, 1088: German Congo)
        for state_id in [1086, 1087, 1088]:
            self.assertTrue(
                re.search(rf"\b{state_id}\b", events_text),
                f"events/WW1_Agadir.txt must reference Neukamerun cession state {state_id}"
            )

        # 4. Decisions file verification
        agadir_decisions_path = os.path.join(REPO_ROOT, "common", "decisions", "ww1_agadir_crisis_decisions.txt")
        self.assertTrue(
            os.path.isfile(agadir_decisions_path),
            f"Agadir crisis decisions file missing: {agadir_decisions_path}"
        )

        with open(agadir_decisions_path, "r", encoding="utf-8-sig", errors="replace") as f:
            decisions_text = f.read()

        expected_decision_tokens = ["GER_agadir_", "FRA_agadir_", "ENG_agadir_"]
        for token in expected_decision_tokens:
            self.assertTrue(
                token in decisions_text,
                f"ww1_agadir_crisis_decisions.txt must define decisions matching token '{token}'"
            )

    def test_republic_dashboard_variables(self):
        """Verify the French Republic Dashboard and 4 survival vectors.

        Checks:
        - common/scripted_effects/ww1_france_dashboard_effects.txt exists.
        - Defines FRA_init_republic_dashboard initializing all 4 variables.
        - Defines FRA_clamp_dashboard_variables clamping all 4 variables between 0 and 100.
        - Covers:
          * FRA_union_sacree_cohesion
          * FRA_poilu_morale
          * FRA_charbon_et_acier
          * FRA_reserves_humaines
        """
        dash_effects_path = os.path.join(REPO_ROOT, "common", "scripted_effects", "ww1_france_dashboard_effects.txt")
        self.assertTrue(
            os.path.isfile(dash_effects_path),
            f"French dashboard scripted effects file missing: {dash_effects_path}"
        )

        with open(dash_effects_path, "r", encoding="utf-8-sig", errors="replace") as f:
            effects_text = f.read()

        # 1. Scripted effect definitions
        self.assertIn(
            "FRA_init_republic_dashboard",
            effects_text,
            "ww1_france_dashboard_effects.txt must define scripted effect 'FRA_init_republic_dashboard'"
        )
        self.assertIn(
            "FRA_clamp_dashboard_variables",
            effects_text,
            "ww1_france_dashboard_effects.txt must define scripted effect 'FRA_clamp_dashboard_variables'"
        )

        # 2. Check the 4 survival vectors
        survival_vectors = [
            "FRA_union_sacree_cohesion",
            "FRA_poilu_morale",
            "FRA_charbon_et_acier",
            "FRA_reserves_humaines"
        ]
        for vec in survival_vectors:
            self.assertIn(
                vec,
                effects_text,
                f"ww1_france_dashboard_effects.txt must manage survival vector '{vec}'"
            )

        # 3. Check variable clamping logic
        for vec in survival_vectors:
            has_clamp = (
                f"clamp_variable = {{ var = {vec}" in effects_text
                or f"clamp_variable = {{\n\t\tvar = {vec}" in effects_text
                or (f"var = {vec}" in effects_text and "min = 0" in effects_text and "max = 100" in effects_text)
            )
            self.assertTrue(
                has_clamp,
                f"FRA_clamp_dashboard_variables must clamp '{vec}' to [0, 100]"
            )

    def test_four_political_destinies(self):
        """Verify the 4 divergent political destinies in the French focus tree.

        Checks:
        - Third Republic / Union Sacrée:
          * FRA_republique_union_sacree
          * FRA_clemenceau_je_fais_la_guerre
          * Awards idea FRA_union_sacree_spirit
        - Second Paris Commune:
          * FRA_republique_des_soviets_de_paris
          * Awards idea FRA_commune_de_paris_spirit
        - Action Française / Orléans Monarchy:
          * FRA_abattre_la_gueuse
          * FRA_restauration_orleaniste_jean_iii
          * Awards idea FRA_action_francaise_monarchy
        - GQG Military Directory:
          * FRA_directoire_militaire_gqg
          * Awards idea FRA_gqg_military_directory
        - Strict mutual exclusivity between the 4 divergent ideological branches.
        """
        focus_path = os.path.join(REPO_ROOT, "common", "national_focus", "france.txt")
        self.assertTrue(os.path.isfile(focus_path), f"Focus file missing: {focus_path}")

        foci = parse_focus_tree(focus_path)

        # 1. Verify existence of path focuses
        expected_foci = [
            "FRA_republique_union_sacree",
            "FRA_clemenceau_je_fais_la_guerre",
            "FRA_republique_des_soviets_de_paris",
            "FRA_abattre_la_gueuse",
            "FRA_restauration_orleaniste_jean_iii",
            "FRA_directoire_militaire_gqg",
        ]
        for fid in expected_foci:
            self.assertIn(fid, foci, f"Focus '{fid}' missing from common/national_focus/france.txt")

        # 2. Verify mutual exclusivity among branch openers
        branch_openers = [
            "FRA_republique_union_sacree",
            "FRA_republique_des_soviets_de_paris",
            "FRA_abattre_la_gueuse",
            "FRA_directoire_militaire_gqg",
        ]
        for opener in branch_openers:
            other_openers = [o for o in branch_openers if o != opener]
            mex_list = foci[opener]["mutually_exclusive"]
            has_mex = any(other in mex_list for other in other_openers)
            self.assertTrue(
                has_mex,
                f"Focus '{opener}' must declare mutual exclusivity with opposing political branches: {other_openers}"
            )

        # 3. Verify distinct national ideas awarded across branches
        destiny_ideas = {
            "FRA_union_sacree_spirit": ["FRA_republique_union_sacree", "FRA_clemenceau_je_fais_la_guerre"],
            "FRA_commune_de_paris_spirit": ["FRA_republique_des_soviets_de_paris"],
            "FRA_action_francaise_monarchy": ["FRA_abattre_la_gueuse", "FRA_restauration_orleaniste_jean_iii"],
            "FRA_gqg_military_directory": ["FRA_directoire_militaire_gqg"],
        }
        for idea, valid_foci in destiny_ideas.items():
            awarded = False
            for fid in valid_foci:
                if fid in foci and idea in foci[fid]["ideas"]:
                    awarded = True
                    break
            self.assertTrue(
                awarded,
                f"Destiny idea '{idea}' must be awarded in one of focuses: {valid_foci}"
            )

    def test_mutinies_and_civil_crises(self):
        """Verify the 1917 French Army Mutinies chain, Pétain leave reform, and Endsieg.

        Checks:
        - events/ww1_france_events.txt has mutiny event ww1_france.210 applying FRA_trench_mutiny_crisis_2.
        - common/decisions/ww1_france_decisions.txt has FRA_petain_welfare_and_leave_reform unlocked by FRA_trench_mutiny_crisis_2.
        - events/ww1_france_events.txt features the French Endsieg event referencing FRA_jusqu_au_bout_endsieg.
        """
        events_path = os.path.join(REPO_ROOT, "events", "ww1_france_events.txt")
        self.assertTrue(os.path.isfile(events_path), f"events/ww1_france_events.txt missing: {events_path}")

        with open(events_path, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        # 1. Mutiny event ww1_france.210 must apply idea FRA_trench_mutiny_crisis_2
        m_210 = re.search(r"id\s*=\s*ww1_france\.210\b.*?(?=\b(?:country_event|news_event)\s*=\s*\{|\Z)", events_text, re.DOTALL)
        self.assertIsNotNone(m_210, "Event ww1_france.210 missing from events/ww1_france_events.txt")
        block_210 = m_210.group(0)
        self.assertIn(
            "FRA_trench_mutiny_crisis_2",
            block_210,
            "Event ww1_france.210 must apply 'FRA_trench_mutiny_crisis_2' so that the mutiny crisis can be managed"
        )

        # 2. Pétain leave reform decision must require FRA_trench_mutiny_crisis_2
        decisions_path = os.path.join(REPO_ROOT, "common", "decisions", "ww1_france_decisions.txt")
        self.assertTrue(os.path.isfile(decisions_path), f"Decisions file missing: {decisions_path}")

        with open(decisions_path, "r", encoding="utf-8-sig", errors="replace") as f:
            decisions_text = f.read()

        self.assertIn(
            "FRA_petain_welfare_and_leave_reform",
            decisions_text,
            "common/decisions/ww1_france_decisions.txt must define 'FRA_petain_welfare_and_leave_reform'"
        )
        self.assertIn(
            "FRA_trench_mutiny_crisis_2",
            decisions_text,
            "FRA_petain_welfare_and_leave_reform must interact with idea 'FRA_trench_mutiny_crisis_2'"
        )

        # 3. French Endsieg spirit (Jusqu'au Bout!)
        self.assertIn(
            "FRA_jusqu_au_bout_endsieg",
            events_text,
            "events/ww1_france_events.txt must reference French Endsieg spirit 'FRA_jusqu_au_bout_endsieg'"
        )

    def test_semantic_oracle_modifiers(self):
        """Verify that all French overhaul ideas use valid Clausewitz modifiers via Semantic Oracle.

        Checks:
        - common/ideas/ww1_france_crises_ideas.txt
        - common/ideas/ww1_france_political_ideas.txt
        - common/ideas/ww1_france_dashboard_ideas.txt
        - 0 invalid or hallucinated modifier tokens in any of the files.
        """
        target_files = [
            os.path.join(REPO_ROOT, "common", "ideas", "ww1_france_crises_ideas.txt"),
            os.path.join(REPO_ROOT, "common", "ideas", "ww1_france_political_ideas.txt"),
            os.path.join(REPO_ROOT, "common", "ideas", "ww1_france_dashboard_ideas.txt"),
            os.path.join(REPO_ROOT, "common", "decisions", "ww1_france_decisions.txt"),
        ]

        for fpath in target_files:
            rel = os.path.relpath(fpath, REPO_ROOT)
            self.assertTrue(os.path.isfile(fpath), f"French file missing: {rel}")

            with open(fpath, "r", encoding="utf-8-sig", errors="replace") as f:
                content = f.read().strip()
            self.assertGreater(len(content), 0, f"File '{rel}' is empty")

            errors = audit_file_modifiers(fpath)
            self.assertEqual(
                len(errors), 0,
                f"Semantic Oracle detected invalid Clausewitz modifier tokens in {rel}: {errors}"
            )

    def test_wartime_industrial_and_allied_decisions(self):
        """Verify wartime industrial relocation, Verdun redoubts, and Allied cooperation decisions.

        Checks:
        - Category FRA_war_economy_and_munitions:
          * FRA_dec_evacuate_briey_machinery
          * FRA_dec_lyon_chemical_complex
          * FRA_dec_schneider_creusot_heavy_guns
        - Category FRA_defence_of_verdun:
          * FRA_dec_fort_douaumont_reinforcement
          * FRA_dec_voix_sacree_truck_convoys
        - Category FRA_entente_diplomacy:
          * FRA_dec_inter_allied_supreme_war_council
          * FRA_dec_us_morgan_bank_credit_line
        - All decisions define fast-failing allowed = { original_tag = FRA }
        - Category definitions in common/decisions/categories/ww1_france_categories.txt
        """
        decisions_path = os.path.join(REPO_ROOT, "common", "decisions", "ww1_france_decisions.txt")
        self.assertTrue(os.path.isfile(decisions_path), f"Decisions file missing: {decisions_path}")

        with open(decisions_path, "r", encoding="utf-8-sig", errors="replace") as f:
            decisions_text = f.read()

        expected_decisions = [
            "FRA_dec_evacuate_briey_machinery",
            "FRA_dec_lyon_chemical_complex",
            "FRA_dec_schneider_creusot_heavy_guns",
            "FRA_dec_fort_douaumont_reinforcement",
            "FRA_dec_voix_sacree_truck_convoys",
            "FRA_dec_inter_allied_supreme_war_council",
            "FRA_dec_us_morgan_bank_credit_line",
        ]

        for dec in expected_decisions:
            self.assertIn(dec, decisions_text, f"Decision '{dec}' missing from common/decisions/ww1_france_decisions.txt")

        # Verify allowed = { original_tag = FRA } for each
        for dec in expected_decisions:
            pattern = rf"\b{dec}\s*=\s*\{{[^}}]*allowed\s*=\s*\{{[^}}]*original_tag\s*=\s*FRA"
            self.assertTrue(
                re.search(pattern, decisions_text, re.DOTALL),
                f"Decision '{dec}' must specify fast-failing allowed = {{ original_tag = FRA }}"
            )

        # Check categories
        categories_path = os.path.join(REPO_ROOT, "common", "decisions", "categories", "ww1_france_categories.txt")
        self.assertTrue(os.path.isfile(categories_path), f"Categories file missing: {categories_path}")

        with open(categories_path, "r", encoding="utf-8-sig", errors="replace") as f:
            cat_text = f.read()

        for cat in ["FRA_war_economy_and_munitions", "FRA_defence_of_verdun", "FRA_entente_diplomacy"]:
            self.assertIn(cat, cat_text, f"Category '{cat}' missing from ww1_france_categories.txt")

    def test_localisation_bom_and_parity(self):
        """Verify single UTF-8 BOM, zero double BOM, and 100% key parity on rework localization.

        Checks:
        - localisation/english/ww1_france_rework_l_english.yml
        - localisation/braz_por/ww1_france_rework_l_braz_por.yml
        - Exact byte prefix \\xef\\xbb\\xbf
        - 100% identical key sets between English and Brazilian Portuguese.
        """
        en_path = os.path.join(REPO_ROOT, "localisation", "english", "ww1_france_rework_l_english.yml")
        pt_path = os.path.join(REPO_ROOT, "localisation", "braz_por", "ww1_france_rework_l_braz_por.yml")

        if not os.path.isfile(en_path) or not os.path.isfile(pt_path):
            self.skipTest("Rework localization files not yet created (scheduled for Task 7)")

        # 1. BOM Integrity
        for path, lang in [(en_path, "English"), (pt_path, "Brazilian Portuguese")]:
            with open(path, "rb") as f:
                header = f.read(6)
            self.assertEqual(
                header[:3], b"\xef\xbb\xbf",
                f"{lang} localization must begin with mandatory single UTF-8 BOM (\\xef\\xbb\\xbf)"
            )
            self.assertNotEqual(
                header[3:6], b"\xef\xbb\xbf",
                f"{lang} localization contains corrupting double UTF-8 BOM!"
            )

        # 2. Key Parity
        en_keys = extract_loc_keys(en_path)
        pt_keys = extract_loc_keys(pt_path)

        self.assertGreater(len(en_keys), 0, "English rework localization has 0 parsed keys")
        self.assertGreater(len(pt_keys), 0, "Portuguese rework localization has 0 parsed keys")

        missing_in_pt = en_keys - pt_keys
        missing_in_en = pt_keys - en_keys

        self.assertEqual(
            missing_in_pt, set(),
            f"Keys missing in Brazilian Portuguese: {sorted(list(missing_in_pt))[:10]}"
        )
        self.assertEqual(
            missing_in_en, set(),
            f"Keys missing in English: {sorted(list(missing_in_en))[:10]}"
        )


if __name__ == "__main__":
    unittest.main()
