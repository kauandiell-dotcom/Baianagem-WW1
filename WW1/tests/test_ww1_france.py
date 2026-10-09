"""Comprehensive unit test suite for the French Republic (Troisième République 1911-1918) rework.

Verifies:
- Focus tree topology, valid coordinates, zero collisions, strict downward dy >= 1 progression.
- Historical wartime and date gating on 1914-1918 focuses.
- Naval reinforcement OOBs and MtG/Legacy parity for Courbet and Bretagne classes.
- Absence of banned modifiers in French national ideas.
- Bilingual localization parity (English & Brazilian Portuguese) with UTF-8 BOM.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

BANNED_MODIFIERS = {
    'recovery_rate_factor', 'division_speed', 'production_speed_railway_factor',
    'entrenchment', 'artillery_attack_factor', 'attrition_for_enemy', 'escort_efficiency_factor'
}


class FranceContentReworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.focus_text = (ROOT / "common/national_focus/france.txt").read_text(encoding="utf-8")
        
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
                avail_m = re.search(r'available\s*=\s*\{([^}]+)\}', block)
                avail = avail_m.group(1).strip() if avail_m else None
                prereqs = [re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr)
                           for pr in re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', block)]
                cls.foci[fid] = {
                    "x": x, "y": y, "cost": cost, "available": avail,
                    "prereqs": prereqs, "block": block
                }
            idx = cur

    def test_focus_count_and_coordinate_collisions(self):
        """Verifies that all 200 French focuses are present with unique coordinates."""
        self.assertEqual(len(self.foci), 200, f"Expected exactly 200 French focuses, found {len(self.foci)}")
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
                    cy = data["y"]
                    self.assertGreater(cy, py, f"Focus {fid} (y={cy}) must be below parent {parent} (y={py})")

    def test_prewar_pacing_and_crisis_costs(self):
        """Verifies that 1911-1914 pre-war crisis focuses have agile costs (cost <= 5)."""
        agile_foci = [
            "FRA_question_du_maroc_1911", "FRA_fermete_diplomatique_agadir",
            "FRA_compromis_colonial_allemand", "FRA_traite_de_fez_1912",
            "FRA_loi_des_trois_ans_1913", "FRA_election_presidentielle_1913",
            "FRA_presidence_poincare", "FRA_presidence_pams",
            "FRA_le_scandale_calmette_caillaux", "FRA_assassinat_de_jean_jaures",
            "FRA_proclamer_union_sacree", "FRA_bataille_des_frontieres",
            "FRA_operation_de_la_marne"
        ]
        for fid in agile_foci:
            self.assertIn(fid, self.foci)
            self.assertLessEqual(self.foci[fid]["cost"], 5.0, f"Focus {fid} should have agile cost <= 5")

    def test_wartime_and_date_gating(self):
        """Verifies that key 1914-1918 wartime focuses cannot be taken during peacetime in 1911."""
        gated_foci = [
            "FRA_proclamer_union_sacree", "FRA_bataille_des_frontieres",
            "FRA_operation_de_la_marne", "FRA_la_fournaise_de_verdun",
            "FRA_la_bataille_de_la_somme_soutien", "FRA_offensive_nivelle_chemin_des_dames",
            "FRA_crise_des_mutineries_1917", "FRA_petain_commandant_en_chef",
            "FRA_arret_des_offensives_ludendorff", "FRA_ferdinand_foch_commandement_unique",
            "FRA_offensive_des_cent_jours", "FRA_le_wagon_de_rethondes_a_compiegne"
        ]
        for fid in gated_foci:
            self.assertIn(fid, self.foci)
            avail = self.foci[fid]["available"]
            self.assertIsNotNone(avail, f"Focus {fid} must have available gating!")
            has_war_or_date = ("has_war" in avail or "date >" in avail or "capitulated" in avail)
            self.assertTrue(has_war_or_date, f"Focus {fid} available must check has_war or date: {avail}")

    def test_political_cabinet_transitions(self):
        """Verifies that real set_politics effects are present in French leadership focuses."""
        poincare = self.foci["FRA_presidence_poincare"]["block"]
        self.assertIn("set_politics", poincare)
        self.assertIn("ruling_party = democratic", poincare)

        clemenceau = self.foci["FRA_je_fais_la_guerre"]["block"]
        self.assertIn("set_politics", clemenceau)
        self.assertIn("add_ideas = FRA_le_tigre_clemenceau", clemenceau)

    def test_naval_reinforcement_oob_parity(self):
        """Verifies that Courbet and Bretagne reinforcement OOBs exist and have identical MtG/Legacy rosters."""
        for class_name in ["ww1_fra_courbet_dreadnoughts", "ww1_fra_bretagne_super_dreadnoughts"]:
            mtg_path = ROOT / "history/units" / f"{class_name}.txt"
            legacy_path = ROOT / "history/units" / f"{class_name}_legacy.txt"
            self.assertTrue(mtg_path.exists(), f"Missing {mtg_path}")
            self.assertTrue(legacy_path.exists(), f"Missing {legacy_path}")

            mtg_ships = re.findall(r'name\s*=\s*"([^"]+)"', mtg_path.read_text(encoding="utf-8"))
            legacy_ships = re.findall(r'name\s*=\s*"([^"]+)"', legacy_path.read_text(encoding="utf-8"))
            self.assertGreater(len(mtg_ships), 0)
            self.assertEqual(mtg_ships, legacy_ships, f"Mismatched ship roster for {class_name}")

    def test_no_banned_modifiers_in_french_ideas(self):
        """Verifies that no banned engine modifiers are present in French idea files."""
        for path in [ROOT / "common/ideas/ww1_france_ideas.txt", ROOT / "common/ideas/zz_ww1_france_reforms.txt"]:
            clean = re.sub(r'#[^\n]*', '', path.read_text(encoding="utf-8"))
            for b in BANNED_MODIFIERS:
                self.assertIsNone(re.search(rf'\b{b}\s*=', clean), f"{path.name} contains banned modifier: {b}")

    def test_bilingual_localization_parity_and_bom(self):
        """Verifies that French localization files have UTF-8 BOM and mirror all new keys."""
        en_path = ROOT / "localisation/english/ww1_france_l_english.yml"
        pt_path = ROOT / "localisation/braz_por/ww1_france_l_braz_por.yml"

        self.assertTrue(en_path.read_bytes().startswith(b'\xef\xbb\xbf'), "English loc missing BOM")
        self.assertTrue(pt_path.read_bytes().startswith(b'\xef\xbb\xbf'), "Portuguese loc missing BOM")

        en_text = en_path.read_text(encoding="utf-8-sig")
        pt_text = pt_path.read_text(encoding="utf-8-sig")

        expected_keys = [
            "FRA_le_tigre_clemenceau", "FRA_ils_ne_passeront_pas",
            "FRA_poilus_reconcilies", "FRA_taxis_de_la_marne",
            "FRA_taxis_de_la_marne_active"
        ]
        for k in expected_keys:
            self.assertIn(f"{k}:", en_text, f"Missing {k} in English loc")
            self.assertIn(f"{k}_desc:", en_text, f"Missing {k}_desc in English loc")
            self.assertIn(f"{k}:", pt_text, f"Missing {k} in Portuguese loc")
            self.assertIn(f"{k}_desc:", pt_text, f"Missing {k}_desc in Portuguese loc")


if __name__ == "__main__":
    unittest.main()
