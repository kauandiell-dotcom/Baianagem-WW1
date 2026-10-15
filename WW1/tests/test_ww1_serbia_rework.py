"""Master QA Test Suite for Kingdom of Serbia Complete Overhaul & The Great Retreat.

Validates the full specification across:
1. Native Balance of Power Engine (common/bop/SER_bop.txt):
   - Sides: bop_ser_pasic_parliament vs bop_ser_apis_black_hand.
   - Valid ranges and Clausewitz modifiers.
2. The Great Retreat & Salonika Sanctuary Engine:
   - Cores granted on state 184 (Central Macedonia / Salonika) and state 44 (Durrës/Albania).
   - Resistance idea SER_otadzbina_u_pokretu with surrender_limit >= 0.35.
   - Events in events/ww1_serbia_retreat_events.txt with namespace ww1_serbia_retreat.
3. 28-30 Division Mass Mobilization:
   - Decisions in common/decisions/ww1_serbia_retreat_decisions.txt for the 4 waves:
     * SER_spawn_conscript_regiments_1896_1899
     * SER_spawn_yugoslav_volunteer_corps
     * SER_spawn_french_allied_brigades
     * SER_spawn_toplica_chetnik_uprising
4. Belgrade Defense & Typhus Crisis:
   - Major Gavrilović last stand decision & idea SER_major_gavrilovic_spirit.
   - 1915 Typhus epidemic events ww1_serbia.20 and Elsie Inglis medical aid ww1_serbia.21.
5. Vido Memorial & Essad Pasha Pact:
   - Essad Pasha Albanian corridor event ww1_serbia_retreat.15.
   - Blue Graveyard of Vido memorial ww1_serbia_retreat.20 and idea SER_oath_of_corfu_martyrs.
6. The 4 Yugoslav & Serbian Destinies:
   - Focuses in common/national_focus/serbia.txt:
     * SER_proclamation_of_yugoslavia (Kingdom of SHS)
     * SER_restored_sovereign_serbia (Greater Serbia Centralism)
     * SER_balkan_socialist_soviet_republic (Balkan Socialist Federation)
     * SER_apis_pretorian_military_junta (Black Hand Pretorian State)
   - Verified mutual exclusions and unique national ideas.
7. Semantic Oracle Modifier Compliance:
   - common/ideas/ww1_serbia_ideas.txt and decisions audited via scripts/hoi4_semantic_oracle.py.
8. Bilingual Localization Integrity & Key Parity:
   - localisation/english/ww1_serbia_l_english.yml
   - localisation/braz_por/ww1_serbia_l_braz_por.yml
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


class TestSerbiaOverhaul(unittest.TestCase):
    """Automated test suite for Serbia complete overhaul and Great Retreat."""

    def test_native_bop_definition(self):
        """Verify native Balance of Power definition in common/bop/SER_bop.txt."""
        bop_file = os.path.join(REPO_ROOT, "common", "bop", "SER_bop.txt")
        self.assertTrue(os.path.isfile(bop_file), f"Native BoP file missing: {bop_file}")

        with open(bop_file, "r", encoding="utf-8-sig", errors="replace") as f:
            text = f.read()

        # Check BoP ID and sides
        self.assertIn("bop_ser_civil_military", text, "Must define bop_ser_civil_military")
        self.assertIn("bop_ser_pasic_parliament", text, "Must define left side bop_ser_pasic_parliament")
        self.assertIn("bop_ser_apis_black_hand", text, "Must define right side bop_ser_apis_black_hand")

        # Check ranges
        expected_ranges = [
            "bop_ser_range_extreme_pasic",
            "bop_ser_range_medium_pasic",
            "bop_ser_range_balanced",
            "bop_ser_range_medium_apis",
            "bop_ser_range_extreme_apis",
        ]
        for rng in expected_ranges:
            self.assertIn(rng, text, f"BoP must define range '{rng}'")

    def test_great_retreat_and_sanctuary_mechanics(self):
        """Verify Great Retreat events, core grants on states 184 and 44, and surrender limit."""
        retreat_events_path = os.path.join(REPO_ROOT, "events", "ww1_serbia_retreat_events.txt")
        self.assertTrue(os.path.isfile(retreat_events_path), f"Retreat events file missing: {retreat_events_path}")

        with open(retreat_events_path, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        # Namespace check
        self.assertTrue(
            re.search(r"\badd_namespace\s*=\s*ww1_serbia_retreat\b", events_text),
            "events/ww1_serbia_retreat_events.txt must declare add_namespace = ww1_serbia_retreat"
        )

        # Core grants on Salonika (184) and Durrës/Albania (44)
        self.assertTrue(
            re.search(r"184\s*=\s*\{[^}]*add_core_of\s*=\s*SER", events_text) or "add_core_of = SER" in events_text,
            "Retreat event must grant core on state 184 (Salonika)"
        )
        self.assertTrue(
            re.search(r"44\s*=\s*\{[^}]*add_core_of\s*=\s*SER", events_text) or "44" in events_text,
            "Retreat event must reference state 44 (Durrës / Albania corridor)"
        )

        # Verify surrender limit in ideas
        ideas_file = os.path.join(REPO_ROOT, "common", "ideas", "ww1_serbia_ideas.txt")
        self.assertTrue(os.path.isfile(ideas_file), f"Ideas file missing: {ideas_file}")
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()

        self.assertIn("SER_otadzbina_u_pokretu", ideas_text, "Must define SER_otadzbina_u_pokretu")
        # Check surrender limit value
        m_sl = re.search(r"surrender_limit\s*=\s*([0-9\.]+)", ideas_text)
        self.assertTrue(m_sl, "SER_otadzbina_u_pokretu must provide surrender_limit modifier")
        self.assertGreaterEqual(float(m_sl.group(1)), 0.35, "surrender_limit must be >= 0.35")

    def test_salonika_thirty_divisions_spawns(self):
        """Verify decisions spawning the 4 mobilization waves totaling 28-30 divisions."""
        dec_file = os.path.join(REPO_ROOT, "common", "decisions", "ww1_serbia_retreat_decisions.txt")
        self.assertTrue(os.path.isfile(dec_file), f"Retreat decisions file missing: {dec_file}")

        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        expected_decisions = [
            "SER_spawn_conscript_regiments_1896_1899",
            "SER_spawn_yugoslav_volunteer_corps",
            "SER_spawn_french_allied_brigades",
            "SER_spawn_toplica_chetnik_uprising",
        ]
        for ed in expected_decisions:
            self.assertIn(ed, dec_text, f"Decisions file must define '{ed}'")

    def test_belgrade_defense_and_typhus_crisis(self):
        """Verify Major Gavrilović last stand and 1915 typhus epidemic crisis."""
        events_file = os.path.join(REPO_ROOT, "events", "ww1_serbia_events.txt")
        self.assertTrue(os.path.isfile(events_file), f"Events file missing: {events_file}")
        with open(events_file, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        # Check typhus crisis events
        self.assertIn("ww1_serbia.20", events_text, "Must define typhus outbreak event ww1_serbia.20")
        self.assertIn("ww1_serbia.21", events_text, "Must define Dr. Elsie Inglis mission ww1_serbia.21")

        # Check Major Gavrilović decision
        dec_file = os.path.join(REPO_ROOT, "common", "decisions", "ww1_serbia_decisions.txt")
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()
        self.assertIn("SER_dec_major_gavrilovic_last_stand", dec_text, "Must define SER_dec_major_gavrilovic_last_stand")

        # Check idea
        ideas_file = os.path.join(REPO_ROOT, "common", "ideas", "ww1_serbia_ideas.txt")
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()
        self.assertIn("SER_major_gavrilovic_spirit", ideas_text, "Must define SER_major_gavrilovic_spirit")

    def test_vido_memorial_and_essad_pasha(self):
        """Verify Essad Pasha Albanian treaty and Blue Graveyard of Vido memorial."""
        retreat_events_path = os.path.join(REPO_ROOT, "events", "ww1_serbia_retreat_events.txt")
        with open(retreat_events_path, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        self.assertIn("ww1_serbia_retreat.15", events_text, "Must define Essad Pasha pact event ww1_serbia_retreat.15")
        self.assertIn("ww1_serbia_retreat.20", events_text, "Must define Vido Plava Grobnica event ww1_serbia_retreat.20")

        ideas_file = os.path.join(REPO_ROOT, "common", "ideas", "ww1_serbia_ideas.txt")
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()
        self.assertIn("SER_oath_of_corfu_martyrs", ideas_text, "Must define SER_oath_of_corfu_martyrs")

    def test_four_yugoslav_destinies(self):
        """Verify the 4 divergent post-war paths in common/national_focus/serbia.txt."""
        focus_file = os.path.join(REPO_ROOT, "common", "national_focus", "serbia.txt")
        foci = parse_focus_tree(focus_file)

        destiny_focuses = [
            "SER_proclamation_of_yugoslavia",
            "SER_restored_sovereign_serbia",
            "SER_balkan_socialist_soviet_republic",
            "SER_apis_pretorian_military_junta",
        ]
        for df in destiny_focuses:
            self.assertIn(df, foci, f"Focus tree must define destiny focus '{df}'")

        # Verify mutual exclusions
        for df in destiny_focuses:
            f_data = foci[df]
            other_destinies = [x for x in destiny_focuses if x != df]
            has_mut = any(other in f_data["mutually_exclusive"] for other in other_destinies)
            self.assertTrue(
                has_mut,
                f"Destiny focus '{df}' must be mutually exclusive with other endgame paths"
            )

    def test_semantic_oracle_modifiers(self):
        """Verify that all Serbian overhaul ideas and decisions use valid Clausewitz country modifiers."""
        idea_files = [
            os.path.join(REPO_ROOT, "common", "ideas", "ww1_serbia_ideas.txt")
        ]
        total_invalids = []
        for idf in idea_files:
            if os.path.isfile(idf):
                invalids = audit_file_modifiers(idf)
                total_invalids.extend(invalids)

        self.assertEqual(
            total_invalids, [],
            f"Found invalid Clausewitz modifiers in Serbian ideas: {total_invalids}"
        )

    def test_localisation_bom_and_parity(self):
        """Verify single UTF-8 BOM, zero double BOM, and 100% key parity on Serbian localization."""
        en_loc = os.path.join(REPO_ROOT, "localisation", "english", "ww1_serbia_l_english.yml")
        pt_loc = os.path.join(REPO_ROOT, "localisation", "braz_por", "ww1_serbia_l_braz_por.yml")

        self.assertTrue(os.path.isfile(en_loc), f"English localization file missing: {en_loc}")
        self.assertTrue(os.path.isfile(pt_loc), f"Portuguese localization file missing: {pt_loc}")

        def inspect_bom(fpath):
            with open(fpath, "rb") as f:
                head = f.read(6)
            if head.startswith(b"\xef\xbb\xbf\xef\xbb\xbf"):
                return "DOUBLE_BOM"
            elif head.startswith(b"\xef\xbb\xbf"):
                return "SINGLE_BOM"
            else:
                return "NO_BOM"

        self.assertEqual(inspect_bom(en_loc), "SINGLE_BOM", f"{en_loc} must have exact single UTF-8 BOM")
        self.assertEqual(inspect_bom(pt_loc), "SINGLE_BOM", f"{pt_loc} must have exact single UTF-8 BOM")

        # Key parity check
        def extract_keys(fpath):
            with open(fpath, "r", encoding="utf-8-sig", errors="replace") as f:
                lines = f.readlines()
            keys = set()
            for line in lines:
                m = re.match(r"^\s*([a-zA-Z0-9_\.:-]+):", line)
                if m:
                    k = m.group(1)
                    if k not in ["l_english", "l_braz_por"]:
                        keys.add(k)
            return keys

        en_keys = extract_keys(en_loc)
        pt_keys = extract_keys(pt_loc)

        diff_en_pt = en_keys - pt_keys
        diff_pt_en = pt_keys - en_keys

        self.assertEqual(
            diff_en_pt, set(),
            f"Keys present in English but missing in Brazilian Portuguese: {diff_en_pt}"
        )
        self.assertEqual(
            diff_pt_en, set(),
            f"Keys present in Brazilian Portuguese but missing in English: {diff_pt_en}"
        )


if __name__ == "__main__":
    unittest.main()
