"""Comprehensive unit test suite for the Ottoman Empire (Devlet-i Aliyye-i Osmaniyye 1911-1918) rework.

Verifies:
- Focus tree topology, valid coordinates, zero collisions, strict downward dy >= 1 progression.
- Exact focus count (256 focuses across 5 non-colliding visual wings).
- Kuwait transfer to Great Britain (owner = ENG, controller = ENG) and British garrison in province 8085.
- Authentic 1911 starting political and military setup (Second Constitutional Era, no Three Pashas dictatorship).
- Ottoman North Africa garrisons in Tripoli and Benghazi.
- Absence of banned modifiers in Ottoman national ideas.
- Bilingual localization parity (English & Brazilian Portuguese) with UTF-8 BOM.
- 100% GFX goal sprite and shine completeness.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

BANNED_MODIFIERS = {
    'recovery_rate_factor', 'division_speed', 'production_speed_railway_factor',
    'entrenchment', 'artillery_attack_factor', 'attrition_for_enemy', 'escort_efficiency_factor'
}


class OttomanContentReworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.focus_text = (ROOT / "common/national_focus/turkey.txt").read_text(encoding="utf-8")
        
        # Parse focus blocks
        cls.foci = {}
        idx = 0
        while True:
            pos = cls.focus_text.find("focus = {", idx)
            if pos == -1:
                break
            start_brace = cls.focus_text.find("{", pos)
            depth = 1
            cur = start_brace + 1
            while cur < len(cls.focus_text) and depth > 0:
                if cls.focus_text[cur] == '{':
                    depth += 1
                elif cls.focus_text[cur] == '}':
                    depth -= 1
                cur += 1
            block = cls.focus_text[pos:cur]
            id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
            if id_m:
                fid = id_m.group(1)
                x = int(re.search(r'\bx\s*=\s*([0-9]+)', block).group(1))
                y = int(re.search(r'\by\s*=\s*([0-9]+)', block).group(1))
                cost = float(re.search(r'\bcost\s*=\s*([0-9.]+)', block).group(1))
                icon = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', block).group(1)
                avail_m = re.search(r'available\s*=\s*\{([^}]+)\}', block)
                avail = avail_m.group(1).strip() if avail_m else None
                prereqs = [re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr)
                           for pr in re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', block)]
                cls.foci[fid] = {
                    "x": x, "y": y, "cost": cost, "icon": icon, "available": avail,
                    "prereqs": prereqs, "block": block
                }
            idx = cur

    def test_focus_count_and_coordinate_collisions(self):
        """Verifies that all 256 Ottoman focuses are present with unique coordinates."""
        self.assertEqual(len(self.foci), 256, f"Expected exactly 256 Ottoman focuses, found {len(self.foci)}")
        coords = {}
        for fid, data in self.foci.items():
            coord = (data["x"], data["y"])
            self.assertNotIn(coord, coords, f"Collision at {coord}: {fid} vs {coords.get(coord)}")
            coords[coord] = fid

    def test_prerequisite_integrity_and_downward_progression(self):
        """Verifies that all prerequisites exist and children are strictly below parents (dy >= 1)."""
        for fid, data in self.foci.items():
            for pr_group in data["prereqs"]:
                for parent in pr_group:
                    self.assertIn(parent, self.foci, f"Focus {fid} has non-existent parent {parent}")
                    py = self.foci[parent]["y"]
                    self.assertGreaterEqual(
                        data["y"], py + 1,
                        f"Focus {fid} (y={data['y']}) is not below parent {parent} (y={py})"
                    )

    def test_kuwait_ownership_and_british_garrison(self):
        """Verifies Kuwait sovereignty is transferred to Great Britain with a British garrison."""
        kuwait_file = (ROOT / "history/states/656-Kuwait.txt").read_text(encoding="utf-8")
        self.assertIn("owner = ENG", kuwait_file, "Kuwait owner must be ENG")
        self.assertIn("controller = ENG", kuwait_file, "Kuwait controller must be ENG")

        eng_oob = (ROOT / "history/units/ENG_1936_generic.txt").read_text(encoding="utf-8")
        self.assertIn("location = 8085", eng_oob, "Kuwait City (prov 8085) must have a British garrison")

    def test_ottoman_starting_political_reality_1911(self):
        """Verifies 1911 starting ideas reflect the Second Constitutional Era rather than Three Pashas dictatorship."""
        tur_history = (ROOT / "history/countries/TUR - Turkey.txt").read_text(encoding="utf-8")
        self.assertIn("TUR_second_constitutional_era", tur_history)
        self.assertNotIn("TUR_three_pashas_dictatorship", tur_history)
        self.assertIn("TUR_straits_fortress_cannons", tur_history)
        self.assertIn("TUR_sick_man_debt", tur_history)
        self.assertIn("TUR_mehmetcik_tenacity", tur_history)

    def test_tripoli_and_benghazi_garrisons(self):
        """Verifies Ottoman North Africa starts with defensive garrisons in Tripoli and Benghazi."""
        tur_oob = (ROOT / "history/units/TUR_1936_generic.txt").read_text(encoding="utf-8")
        self.assertIn("location = 1149", tur_oob, "Tripoli (prov 1149) must have an Ottoman garrison")
        self.assertIn("location = 11954", tur_oob, "Benghazi (prov 11954) must have an Ottoman garrison")

    def test_no_banned_modifiers_in_ideas(self):
        """Verifies that ww1_ottoman_ideas.txt does not contain banned Clausewitz modifiers."""
        raw_text = (ROOT / "common/ideas/ww1_ottoman_ideas.txt").read_text(encoding="utf-8")
        clean = re.sub(r'#[^\n]*', '', raw_text)
        for modifier in BANNED_MODIFIERS:
            self.assertIsNone(
                re.search(rf'\b{modifier}\s*=', clean),
                f"Banned modifier '{modifier}' found in ww1_ottoman_ideas.txt"
            )

    def test_bilingual_localization_parity_and_utf8_bom(self):
        """Verifies 100% localization parity and UTF-8 BOM encoding for both English and PT-BR."""
        en_path = ROOT / "localisation/english/ww1_ottoman_l_english.yml"
        pt_path = ROOT / "localisation/braz_por/ww1_ottoman_l_braz_por.yml"

        self.assertTrue(en_path.exists(), "English localization file missing")
        self.assertTrue(pt_path.exists(), "Portuguese localization file missing")

        en_bytes = en_path.read_bytes()
        pt_bytes = pt_path.read_bytes()

        self.assertTrue(en_bytes.startswith(b"\xef\xbb\xbf"), "English localization must start with UTF-8 BOM")
        self.assertTrue(pt_bytes.startswith(b"\xef\xbb\xbf"), "Portuguese localization must start with UTF-8 BOM")

        en_text = en_bytes.decode("utf-8")
        pt_text = pt_bytes.decode("utf-8")

        for fid in self.foci:
            self.assertIn(f"{fid}:0", en_text, f"Missing English title for {fid}")
            self.assertIn(f"{fid}_desc:0", en_text, f"Missing English description for {fid}")
            self.assertIn(f"{fid}:0", pt_text, f"Missing Portuguese title for {fid}")
            self.assertIn(f"{fid}_desc:0", pt_text, f"Missing Portuguese description for {fid}")

    def test_gfx_sprites_and_shines_completeness(self):
        """Verifies that all focus icons used in turkey.txt have corresponding base and shine sprite definitions."""
        gfx_texts = []
        for gfx_file in (ROOT / "interface").glob("*.gfx"):
            gfx_texts.append(gfx_file.read_text(encoding="utf-8", errors="ignore"))
        combined_gfx = "\n".join(gfx_texts)

        for fid, data in self.foci.items():
            icon = data["icon"]
            self.assertIn(f'name = "{icon}"', combined_gfx, f"Missing sprite definition for {icon} (focus {fid})")
            self.assertIn(f'name = "{icon}_shine"', combined_gfx, f"Missing shine sprite for {icon} (focus {fid})")


if __name__ == "__main__":
    unittest.main()
