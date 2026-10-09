#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test suite for Kingdom of Serbia (SER) WW1 overhaul (1911-1918).
"""

import os
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class TestWW1Serbia(unittest.TestCase):

    def test_focus_count_and_coordinates(self):
        focus_file = ROOT / "common" / "national_focus" / "serbia.txt"
        self.assertTrue(focus_file.exists(), "serbia.txt must exist")
        txt = focus_file.read_text(encoding="utf-8")

        # Focus count
        foci = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)', txt)
        self.assertEqual(len(foci), 94, f"Expected exactly 94 focuses, found {len(foci)}")

        # Check coordinates and collisions
        coord_matches = re.findall(r'id\s*=\s*([a-zA-Z0-9_]+)[\s\S]*?x\s*=\s*(\d+)[\s\S]*?y\s*=\s*(\d+)', txt)
        coords = {}
        for fid, x_str, y_str in coord_matches:
            c = (int(x_str), int(y_str))
            self.assertNotIn(c, coords, f"Coordinate collision at {c} between {fid} and {coords.get(c)}")
            coords[c] = fid

        # Check dy >= 1 for prerequisites
        focus_blocks = re.split(r'\bfocus\s*=\s*\{', txt)[1:]
        foci_dict = {}
        for b in focus_blocks:
            fid_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
            x_m = re.search(r'x\s*=\s*(\d+)', b)
            y_m = re.search(r'y\s*=\s*(\d+)', b)
            if fid_m and x_m and y_m:
                fid = fid_m.group(1)
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', b)
                foci_dict[fid] = {
                    'x': int(x_m.group(1)),
                    'y': int(y_m.group(1)),
                    'prereqs': prereqs
                }

        for fid, data in foci_dict.items():
            for p in data['prereqs']:
                self.assertIn(p, foci_dict, f"Prerequisite {p} not found for {fid}")
                parent = foci_dict[p]
                self.assertGreater(data['y'], parent['y'],
                                   f"dy <= 0 violation: child {fid} (y={data['y']}) <= parent {p} (y={parent['y']})")

    def test_map_territorial_baseline_1911(self):
        """Audits state ownership to ensure 1911 map reality as established in the mod."""
        # Montenegro state 105: user explicitly instructed to keep owner = SER
        state_105 = (ROOT / "history" / "states" / "105-Montenegro.txt").read_text(encoding="utf-8")
        self.assertIn("owner = SER", state_105)

        # Core and regional states present under Serbian control in current mod map
        state_107 = (ROOT / "history" / "states" / "107-Kosavo.txt").read_text(encoding="utf-8")
        self.assertIn("owner = SER", state_107)
        state_108 = (ROOT / "history" / "states" / "108-Eastern Serbia.txt").read_text(encoding="utf-8")
        self.assertIn("owner = SER", state_108)
        state_802 = (ROOT / "history" / "states" / "802-Kosovo.txt").read_text(encoding="utf-8")
        self.assertIn("owner = SER", state_802)
        state_106 = (ROOT / "history" / "states" / "106-Macedonia.txt").read_text(encoding="utf-8")
        self.assertIn("owner = SER", state_106)

    def test_no_banned_modifiers_in_ideas(self):
        """Clausewitz engine prohibits certain modifiers in country ideas."""
        banned = [
            "recovery_rate_factor",
            "division_speed",
            "production_speed_railway_factor",
            "entrenchment",
            "artillery_attack_factor",
            "attrition_for_enemy",
            "escort_efficiency_factor"
        ]
        ideas_file = ROOT / "common" / "ideas" / "ww1_serbia_ideas.txt"
        self.assertTrue(ideas_file.exists())
        txt = ideas_file.read_text(encoding="utf-8")
        for b in banned:
            self.assertNotIn(b, txt, f"Banned modifier '{b}' detected in ww1_serbia_ideas.txt")

    def test_localization_integrity_and_bom(self):
        """Verifies UTF-8 BOM and key coverage in English and Portuguese."""
        loc_en_file = ROOT / "localisation" / "english" / "ww1_serbia_l_english.yml"
        loc_br_file = ROOT / "localisation" / "braz_por" / "ww1_serbia_l_braz_por.yml"

        self.assertTrue(loc_en_file.exists())
        self.assertTrue(loc_br_file.exists())

        # BOM check
        with open(loc_en_file, "rb") as f:
            self.assertEqual(f.read(3), b"\xef\xbb\xbf", "ww1_serbia_l_english.yml must have UTF-8 BOM")
        with open(loc_br_file, "rb") as f:
            self.assertEqual(f.read(3), b"\xef\xbb\xbf", "ww1_serbia_l_braz_por.yml must have UTF-8 BOM")

        # Key count check
        txt_en = loc_en_file.read_text(encoding="utf-8")
        txt_br = loc_br_file.read_text(encoding="utf-8")

        keys_en = set(re.findall(r'^\s*([a-zA-Z0-9_\.]+):', txt_en, re.MULTILINE))
        keys_br = set(re.findall(r'^\s*([a-zA-Z0-9_\.]+):', txt_br, re.MULTILINE))

        self.assertGreater(len(keys_en), 250, "Should have over 250 localized keys")
        self.assertEqual(keys_en, keys_br, "English and Portuguese keys must match 100%")

    def test_gfx_and_texture_assets(self):
        """Verifies that all 94 goal sprites and shines are defined and point to real textures."""
        gfx_file = ROOT / "interface" / "ww1_serbia_goals.gfx"
        self.assertTrue(gfx_file.exists())
        txt = gfx_file.read_text(encoding="utf-8")

        # 94 base sprites and 94 shine sprites = 188
        sprites = re.findall(r'name\s*=\s*"([^"]+)"', txt)
        base_sprites = [s for s in sprites if not s.endswith("_shine")]
        shine_sprites = [s for s in sprites if s.endswith("_shine")]

        self.assertEqual(len(base_sprites), 94, "Must have exactly 94 base goal sprites")
        self.assertEqual(len(shine_sprites), 94, "Must have exactly 94 shine goal sprites")

        # Verify all referenced textures exist on disk
        tex_files = re.findall(r'texturefile\s*=\s*"([^"]+)"', txt)
        for tf in tex_files:
            full_path = ROOT / tf
            self.assertTrue(full_path.exists(), f"Texture file {tf} referenced in GFX does not exist on disk!")

    def test_events_brace_integrity(self):
        """Verifies balanced braces and valid IDs in events/ww1_serbia_events.txt."""
        ev_file = ROOT / "events" / "ww1_serbia_events.txt"
        self.assertTrue(ev_file.exists())
        txt = ev_file.read_text(encoding="utf-8")

        open_b = txt.count("{")
        close_b = txt.count("}")
        self.assertEqual(open_b, close_b, f"Unbalanced braces in events: open={open_b}, close={close_b}")

        # Verify all 16 events exist
        for i in range(1, 17):
            ev_id = f"ww1_serbia.{i}"
            self.assertIn(ev_id, txt, f"Event {ev_id} missing in events file")

if __name__ == "__main__":
    unittest.main()
