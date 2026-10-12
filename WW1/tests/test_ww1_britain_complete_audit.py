"""
Master Automated Audit Suite for British Empire (ENG) in WW1.
Exercises the 4 core failure modes identified in Bruno's QA report:
1. Invalid Clausewitz modifier tokens producing empty 'grants ()'
2. Catastrophic national spirit stacking (>5 concurrent ideas)
3. Empty event options and meaningless events (Imperial Conference)
4. Missing shortcut keys and root focus localization with mandatory UTF-8 BOM
"""
import unittest
import os
import sys
import glob
import re

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if MOD_ROOT not in sys.path:
    sys.path.insert(0, MOD_ROOT)

from scripts.hoi4_semantic_oracle import audit_file_modifiers


class TestBritainCompleteAudit(unittest.TestCase):
    def test_zero_invalid_modifiers_in_uk_ideas(self):
        """Failure Mode 1: No ideas may contain invalid/hallucinated Clausewitz tokens."""
        idea_files = glob.glob(os.path.join(MOD_ROOT, "common", "ideas", "*britain*.txt"))
        all_errors = []
        for fpath in idea_files:
            rel = os.path.relpath(fpath, MOD_ROOT)
            errors = audit_file_modifiers(fpath)
            for line_no, token, ctx in errors:
                all_errors.append(f"{rel}:{line_no} [{ctx}]: Unknown modifier token '{token}'")

        self.assertEqual(
            len(all_errors), 0,
            f"Found {len(all_errors)} invalid modifier tokens in UK ideas:\n" + "\n".join(all_errors[:15])
        )

    def test_anti_stacking_limits(self):
        """Failure Mode 2: UK tree must NOT add 100+ separate unmanaged ideas. Max 5 persistent ideas."""
        uk_focus_file = os.path.join(MOD_ROOT, "common", "national_focus", "uk.txt")
        self.assertTrue(os.path.exists(uk_focus_file))

        with open(uk_focus_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        added_ideas = re.findall(r"add_ideas\s*=\s*([a-zA-Z0-9_]+)", content)
        # We allow swap_ideas, but raw unmanaged add_ideas across the 200 focuses must not exceed 5
        self.assertLessEqual(
            len(added_ideas), 5,
            f"Anti-Stacking Violation: UK focus tree calls add_ideas {len(added_ideas)} times! Max allowed is 5."
        )

    def test_decisions_have_no_invalid_modifiers_or_ghost_ideas(self):
        """Failure Mode 5: Decisions must not reference non-existent ideas or use invalid modifier tokens."""
        dec_files = glob.glob(os.path.join(MOD_ROOT, "common", "decisions", "*britain*.txt"))
        self.assertTrue(len(dec_files) > 0, "No UK decision files found!")

        # 1. Modifiers inside decisions must be valid
        all_mod_errors = []
        for df in dec_files:
            rel = os.path.relpath(df, MOD_ROOT)
            errors = audit_file_modifiers(df)
            for line_no, token, ctx in errors:
                all_mod_errors.append(f"{rel}:{line_no} [{ctx}]: Unknown modifier token '{token}'")

        self.assertEqual(len(all_mod_errors), 0, f"Found invalid modifiers in decisions:\n" + "\n".join(all_mod_errors[:10]))

        # 2. Check for references to ghost ideas
        ghost_ideas = [
            "ENG_ww1_x_indian_corps",
            "ENG_ww1_x_district_contracts",
            "ENG_ww1_x_seaplane_patrols",
            "ENG_ww1_x_city_credit_line",
            "ENG_ww1_x_officer_courses"
        ]
        ghost_errors = []
        for df in dec_files:
            rel = os.path.relpath(df, MOD_ROOT)
            with open(df, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for gid in ghost_ideas:
                if f"idea = {gid}" in content or f"has_idea = {gid}" in content:
                    ghost_errors.append(f"{rel}: References ghost idea '{gid}' that causes empty modifiers in game!")

        self.assertEqual(len(ghost_errors), 0, f"Found ghost ideas in decisions:\n" + "\n".join(ghost_errors))

    def test_events_have_tangible_effects_and_no_empty_options(self):
        """Failure Mode 3: No event option may be empty, and Imperial Conference must have tangible rewards."""
        event_files = glob.glob(os.path.join(MOD_ROOT, "events", "*britain*.txt"))
        empty_options = []

        def find_blocks(text, keyword):
            res = []
            idx = 0
            while True:
                pos = text.find(keyword, idx)
                if pos == -1:
                    break
                brace_pos = text.find("{", pos)
                if brace_pos == -1:
                    break
                depth = 1
                cur = brace_pos + 1
                while cur < len(text) and depth > 0:
                    if text[cur] == "{":
                        depth += 1
                    elif text[cur] == "}":
                        depth -= 1
                    cur += 1
                res.append(text[brace_pos + 1 : cur - 1])
                idx = cur
            return res

        for ef in event_files:
            rel = os.path.relpath(ef, MOD_ROOT)
            with open(ef, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            cevents = find_blocks(content, "country_event")
            for cev in cevents:
                m_id = re.search(r"id\s*=\s*([a-zA-Z0-9_\.]+)", cev)
                ev_id = m_id.group(1) if m_id else "unknown"
                options = find_blocks(cev, "option")
                for opt_idx, opt in enumerate(options, start=1):
                    lines = [
                        l.strip()
                        for l in opt.splitlines()
                        if l.strip()
                        and not l.strip().startswith("#")
                        and not l.strip().startswith("name")
                        and not l.strip().startswith("ai_chance")
                    ]
                    # Filter out purely internal flags/vars
                    body = " ".join(lines)
                    cleaned = re.sub(r"add_to_variable\s*=\s*\{[^}]*\}", "", body)
                    cleaned = re.sub(r"set_variable\s*=\s*\{[^}]*\}", "", cleaned)
                    cleaned = re.sub(r"set_country_flag\s*=\s*[a-zA-Z0-9_]+", "", cleaned)
                    cleaned = re.sub(r"clr_country_flag\s*=\s*[a-zA-Z0-9_]+", "", cleaned)
                    if not cleaned.strip():
                        empty_options.append(f"{rel}: event '{ev_id}' option #{opt_idx} has NO tangible gameplay effect!")

        self.assertEqual(
            len(empty_options), 0,
            f"Found {len(empty_options)} empty/meaningless event options:\n" + "\n".join(empty_options[:10])
        )

    def test_shortcuts_and_root_focus_localisation(self):
        """Failure Mode 4: Tree shortcuts and root focus must be localized in PT-BR and EN with UTF-8 BOM."""
        required_keys = [
            "ENG_ww1_shortcut_politics",
            "ENG_ww1_shortcut_economy",
            "ENG_ww1_shortcut_diplomacy",
            "ENG_ww1_shortcut_navy",
            "ENG_ww1_shortcut_army",
            "ENG_ww1_1911_1923"
        ]

        for lang, fname in [("English", "ww1_britain_l_english.yml"), ("Braz_Por", "ww1_britain_l_braz_por.yml")]:
            fpath = os.path.join(MOD_ROOT, "localisation", "english" if lang == "English" else "braz_por", fname)
            self.assertTrue(os.path.exists(fpath), f"File {fpath} must exist!")

            with open(fpath, "rb") as f:
                header = f.read(3)
            self.assertEqual(header, b"\xef\xbb\xbf", f"{fname} must start with UTF-8 BOM!")

            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            for key in required_keys:
                self.assertIn(key, content, f"Missing localization key '{key}' in {lang} ({fname})!")


if __name__ == "__main__":
    unittest.main()
