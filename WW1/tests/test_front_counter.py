"""
Test Suite for Frontline Troop Counter (Front Strength Overlay)
Baianagem-WW1 Mod for Hearts of Iron IV 1.19.3
"""

import os
import unittest
import re

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class TestFrontlineTroopCounter(unittest.TestCase):

    def check_braces(self, filepath):
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Remove comments
        lines = [line.split("#")[0] for line in content.splitlines()]
        cleaned = "\n".join(lines)

        open_braces = cleaned.count("{")
        close_braces = cleaned.count("}")
        self.assertEqual(
            open_braces, close_braces,
            f"Unmatched braces in {filepath}: {open_braces} open vs {close_braces} close"
        )

    def test_syntax_and_braces(self):
        """Verify all new files have valid braces and no syntax errors."""
        target_files = [
            os.path.join(MOD_ROOT, "common", "decisions", "categories", "bww1_front_counter_decision_categories.txt"),
            os.path.join(MOD_ROOT, "common", "decisions", "bww1_front_counter_decisions.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_effects", "bww1_front_counter_effects.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_guis", "bww1_front_counter_scripted_gui.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_localisation", "bww1_front_counter_scripted_loc.txt"),
            os.path.join(MOD_ROOT, "common", "on_actions", "ww1_front_counter_on_actions.txt"),
            os.path.join(MOD_ROOT, "interface", "bww1_front_counter_mapicon.gui"),
        ]
        for tf in target_files:
            self.assertTrue(os.path.exists(tf), f"Missing file: {tf}")
            self.check_braces(tf)

    def test_bom_integrity(self):
        """Verify UTF-8 BOM presence on yaml and absence on txt/gui."""
        en_loc = os.path.join(MOD_ROOT, "localisation", "english", "bww1_front_counter_l_english.yml")
        pt_loc = os.path.join(MOD_ROOT, "localisation", "braz_por", "bww1_front_counter_l_braz_por.yml")

        with open(en_loc, "rb") as f:
            self.assertEqual(f.read(3), b"\xef\xbb\xbf", "English loc must have UTF-8 BOM")
        with open(pt_loc, "rb") as f:
            self.assertEqual(f.read(3), b"\xef\xbb\xbf", "Portuguese loc must have UTF-8 BOM")

        # txt and gui files must NOT have BOM
        non_bom_files = [
            os.path.join(MOD_ROOT, "common", "decisions", "categories", "bww1_front_counter_decision_categories.txt"),
            os.path.join(MOD_ROOT, "common", "decisions", "bww1_front_counter_decisions.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_effects", "bww1_front_counter_effects.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_guis", "bww1_front_counter_scripted_gui.txt"),
            os.path.join(MOD_ROOT, "common", "scripted_localisation", "bww1_front_counter_scripted_loc.txt"),
            os.path.join(MOD_ROOT, "common", "on_actions", "ww1_front_counter_on_actions.txt"),
            os.path.join(MOD_ROOT, "interface", "bww1_front_counter_mapicon.gui"),
        ]
        for nbf in non_bom_files:
            with open(nbf, "rb") as f:
                self.assertNotEqual(f.read(3), b"\xef\xbb\xbf", f"File must NOT have BOM: {nbf}")

    def test_gui_window_linkage(self):
        """Verify scripted_gui window_name matches containerWindowType name."""
        sgui_path = os.path.join(MOD_ROOT, "common", "scripted_guis", "bww1_front_counter_scripted_gui.txt")
        gui_path = os.path.join(MOD_ROOT, "interface", "bww1_front_counter_mapicon.gui")

        with open(sgui_path, "r", encoding="utf-8") as f:
            sgui_txt = f.read()
        with open(gui_path, "r", encoding="utf-8") as f:
            gui_txt = f.read()

        m = re.search(r'window_name\s*=\s*"([^"]+)"', sgui_txt)
        self.assertIsNotNone(m, "window_name not found in scripted_gui")
        window_name = m.group(1)

        self.assertIn(f'name = "{window_name}"', gui_txt, "window_name not found in interface gui")
        self.assertIn("context_type = state_mapicon", sgui_txt, "Must use state_mapicon")

    def test_transparency_for_micro_zoom(self):
        """Verify textboxes have alwaystransparent = yes so unit micro is never blocked."""
        gui_path = os.path.join(MOD_ROOT, "interface", "bww1_front_counter_mapicon.gui")
        with open(gui_path, "r", encoding="utf-8") as f:
            gui_txt = f.read()

        self.assertIn("alwaystransparent = yes", gui_txt, "Counter elements must be click-through transparent")

    def test_localization_keys(self):
        """Verify all loc keys are present in both English and Portuguese."""
        en_loc = os.path.join(MOD_ROOT, "localisation", "english", "bww1_front_counter_l_english.yml")
        pt_loc = os.path.join(MOD_ROOT, "localisation", "braz_por", "bww1_front_counter_l_braz_por.yml")

        required_keys = [
            "bww1_front_counter_category",
            "bww1_fc_enable_counter",
            "bww1_fc_disable_counter",
            "bww1_fc_refresh_counter",
            "bww1_fc_friendly_val",
            "bww1_fc_divider_val",
            "bww1_fc_enemy_val",
            "bww1_intel_high",
            "bww1_intel_medium",
            "bww1_intel_low",
        ]

        with open(en_loc, "r", encoding="utf-8-sig") as f:
            en_txt = f.read()
        with open(pt_loc, "r", encoding="utf-8-sig") as f:
            pt_txt = f.read()

        for k in required_keys:
            self.assertIn(k + ":", en_txt, f"Missing English loc key: {k}")
            self.assertIn(k + ":", pt_txt, f"Missing Portuguese loc key: {k}")

    def test_zero_gameplay_impact(self):
        """Verify decisions cost 0 PP and are restricted to humans only."""
        dec_path = os.path.join(MOD_ROOT, "common", "decisions", "bww1_front_counter_decisions.txt")
        with open(dec_path, "r", encoding="utf-8") as f:
            txt = f.read()

        self.assertIn("cost = 0", txt)
        self.assertIn("factor = 0", txt)
        self.assertIn("is_ai = no", txt)


if __name__ == "__main__":
    unittest.main()
