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

from scripts.hoi4_semantic_oracle import audit_file_modifiers

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
        """Verifies that all 256 Ottoman focuses are present with unique coordinates and dx >= 2 on every row."""
        self.assertEqual(len(self.foci), 256, f"Expected exactly 256 Ottoman focuses, found {len(self.foci)}")
        coords = {}
        rows = {}
        for fid, data in self.foci.items():
            coord = (data["x"], data["y"])
            self.assertNotIn(coord, coords, f"Collision at {coord}: {fid} vs {coords.get(coord)}")
            coords[coord] = fid
            rows.setdefault(data["y"], []).append({"id": fid, "x": data["x"], "y": data["y"]})

        horizontal_collisions = []
        for y, row in sorted(rows.items()):
            row_sorted = sorted(row, key=lambda f: f["x"])
            for i in range(len(row_sorted) - 1):
                f1, f2 = row_sorted[i], row_sorted[i + 1]
                if abs(f2["x"] - f1["x"]) < 2:
                    horizontal_collisions.append((y, f1["id"], f1["x"], f2["id"], f2["x"]))

        self.assertEqual(
            horizontal_collisions,
            [],
            f"Expected 0 horizontal banner collisions (dx >= 2), found {len(horizontal_collisions)}: {horizontal_collisions[:10]}"
        )

    def test_prerequisite_integrity_and_downward_progression(self):
        """Verifies that all prerequisites exist and children satisfy 1 <= dy <= 3."""
        long_vertical_arrows = []
        for fid, data in self.foci.items():
            for pr_group in data["prereqs"]:
                for parent in pr_group:
                    self.assertIn(parent, self.foci, f"Focus {fid} has non-existent parent {parent}")
                    py = self.foci[parent]["y"]
                    dy = data["y"] - py
                    if not (1 <= dy <= 3):
                        long_vertical_arrows.append((parent, py, fid, data["y"], dy))

        self.assertEqual(
            long_vertical_arrows,
            [],
            f"Expected all prerequisite links to satisfy 1 <= dy <= 3, found {len(long_vertical_arrows)} violations: {long_vertical_arrows}"
        )

    def test_zero_hollow_focuses(self):
        """Verifies every focus grants tangible rewards beyond flat PP/stability/war support/variables/flags."""
        hollow_focuses = []
        for fid, data in self.foci.items():
            block = data["block"]
            reward_pos = block.find("completion_reward")
            self.assertNotEqual(reward_pos, -1, f"Focus {fid} missing completion_reward")
            start_brace = block.find("{", reward_pos)
            depth = 1
            cur = start_brace + 1
            while cur < len(block) and depth > 0:
                if block[cur] == "{":
                    depth += 1
                elif block[cur] == "}":
                    depth -= 1
                cur += 1
            reward_body = block[start_brace + 1 : cur - 1]
            cleaned = re.sub(r"#[^\n]*", "", reward_body)
            cleaned = re.sub(r"\badd_political_power\s*=\s*[-0-9.]+", "", cleaned)
            cleaned = re.sub(r"\badd_stability\s*=\s*[-0-9.]+", "", cleaned)
            cleaned = re.sub(r"\badd_war_support\s*=\s*[-0-9.]+", "", cleaned)
            cleaned = re.sub(r"\badd_to_variable\s*=\s*\{[^}]*\}", "", cleaned)
            cleaned = re.sub(r"\bset_country_flag\s*=\s*[a-zA-Z0-9_]+", "", cleaned)
            if not cleaned.strip():
                hollow_focuses.append(fid)

        self.assertEqual(
            hollow_focuses,
            [],
            f"Expected 0 hollow focuses, found {len(hollow_focuses)}: {hollow_focuses[:15]}"
        )

    def test_all_referenced_ideas_exist_and_oracle_clean(self):
        """Verifies all required Ottoman ideas exist and Semantic Oracle reports 0 errors on ideas and decisions."""
        ideas_path = ROOT / "common/ideas/ww1_ottoman_ideas.txt"
        decisions_path = ROOT / "common/decisions/ww1_ottoman_decisions.txt"
        ideas_text = ideas_path.read_text(encoding="utf-8")

        required_ideas = [
            "TUR_sick_man_debt",
            "TUR_mehmetcik_tenacity",
            "TUR_straits_fortress_cannons",
            "TUR_caliphate_global_banner",
            "TUR_arab_revolt_insurgency",
            "TUR_imperial_vilayets_pacified",
            "TUR_senussi_desert_brotherhood",
        ]
        missing_ideas = [
            idea for idea in required_ideas
            if not re.search(rf"\b{idea}\s*=\s*\{{", ideas_text)
        ]
        self.assertEqual(missing_ideas, [], f"Missing required Ottoman ideas: {missing_ideas}")

        idea_oracle_errors = audit_file_modifiers(str(ideas_path))
        self.assertEqual(
            idea_oracle_errors,
            [],
            f"Semantic Oracle errors in ww1_ottoman_ideas.txt: {idea_oracle_errors}"
        )

        decision_oracle_errors = audit_file_modifiers(str(decisions_path))
        self.assertEqual(
            decision_oracle_errors,
            [],
            f"Semantic Oracle errors in ww1_ottoman_decisions.txt: {decision_oracle_errors}"
        )

    def test_arab_vilayet_state_securing_and_opda_decisions(self):
        """Verifies Arab vilayet security decisions, OPDA debt decisions, events 31-32, 0 orphan events, and commanders."""
        decisions_text = (ROOT / "common/decisions/ww1_ottoman_decisions.txt").read_text(encoding="utf-8")
        required_decisions = [
            "TUR_deploy_hejaz_armored_garrison",
            "TUR_teskilat_counter_insurgency_sweep",
            "TUR_subsidize_bedouin_sheikhs",
            "TUR_pacify_arab_insurgency_campaign",
            "TUR_liquidate_opda_debt_tranche",
            "TUR_curb_foreign_consular_courts",
            "TUR_dispatch_officers_to_tripolitania",
        ]
        missing_decisions = [
            dec for dec in required_decisions
            if not re.search(rf"\b{dec}\s*=\s*\{{", decisions_text)
        ]
        self.assertEqual(missing_decisions, [], f"Missing required Ottoman decisions: {missing_decisions}")

        events_text = (ROOT / "events/ww1_ottoman_events.txt").read_text(encoding="utf-8")
        for ev_id in ("ww1_ottoman.31", "ww1_ottoman.32"):
            self.assertIsNotNone(
                re.search(rf"\bid\s*=\s*{re.escape(ev_id)}\b(?!\.)", events_text),
                f"Missing event definition {ev_id} in events/ww1_ottoman_events.txt"
            )

        orphan_events = []
        for i in range(1, 33):
            ev_id = f"ww1_ottoman.{i}"
            # Check if event is defined and triggered
            in_focus = bool(re.search(rf"\b{re.escape(ev_id)}\b(?!\.)", self.focus_text))
            in_decisions = bool(re.search(rf"\b{re.escape(ev_id)}\b(?!\.)", decisions_text))
            event_id_matches = re.findall(rf"\bid\s*=\s*{re.escape(ev_id)}\b(?!\.)", events_text)
            in_events_followup = len(event_id_matches) > 1
            if not (in_focus or in_decisions or in_events_followup):
                orphan_events.append(ev_id)

        self.assertEqual(orphan_events, [], f"Found orphan events never triggered: {orphan_events}")

        tur_history = (ROOT / "history/countries/TUR - Turkey.txt").read_text(encoding="utf-8")
        for char_id in ("TUR_ismail_enver_pasha", "TUR_fakhri_pasha", "TUR_halil_kut"):
            self.assertIn(
                f"recruit_character = {char_id}",
                tur_history,
                f"Missing recruit_character = {char_id} in history/countries/TUR - Turkey.txt"
            )

        tur_chars = (ROOT / "common/characters/TUR.txt").read_text(encoding="utf-8")
        self.assertNotIn("ideology=nazism", tur_chars, "common/characters/TUR.txt must not contain anachronistic ideology=nazism")

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
        """Verifies 100% localization parity, strictly single UTF-8 BOM, and zero generic/untranslated strings."""
        en_path = ROOT / "localisation/english/ww1_ottoman_l_english.yml"
        pt_path = ROOT / "localisation/braz_por/ww1_ottoman_l_braz_por.yml"

        self.assertTrue(en_path.exists(), "English localization file missing")
        self.assertTrue(pt_path.exists(), "Portuguese localization file missing")

        en_bytes = en_path.read_bytes()
        pt_bytes = pt_path.read_bytes()

        self.assertEqual(en_bytes[:3], b"\xef\xbb\xbf", "English localization must start with UTF-8 BOM")
        self.assertNotEqual(en_bytes[3:6], b"\xef\xbb\xbf", "English localization must not have a double UTF-8 BOM")
        self.assertEqual(pt_bytes[:3], b"\xef\xbb\xbf", "Portuguese localization must start with UTF-8 BOM")
        self.assertNotEqual(pt_bytes[3:6], b"\xef\xbb\xbf", "Portuguese localization must not have a double UTF-8 BOM")

        en_text = en_bytes.decode("utf-8")
        pt_text = pt_bytes.decode("utf-8")

        for fid in self.foci:
            self.assertIn(f"{fid}:0", en_text, f"Missing English title for {fid}")
            self.assertIn(f"{fid}_desc:0", en_text, f"Missing English description for {fid}")
            self.assertIn(f"{fid}:0", pt_text, f"Missing Portuguese title for {fid}")
            self.assertIn(f"{fid}_desc:0", pt_text, f"Missing Portuguese description for {fid}")

        banned_placeholders = [
            "Reflete as realidades estruturais e esforços administrativos do Estado Otomano.",
            "Aplica medidas operacionais especializadas para a defesa e prosperidade do império.",
            "Iniciativa estratégica entra em vigor nos territórios imperiais pertinentes.",
        ]
        for placeholder in banned_placeholders:
            self.assertNotIn(placeholder, pt_text, f"Generic copy-paste placeholder found in PT-BR localization: {placeholder}")

        untranslated_titles = [
            "Subsidize Anatolian Grain",
            "Second Constitutional Era",
        ]
        for title in untranslated_titles:
            self.assertNotIn(title, pt_text, f"Untranslated English title found in PT-BR localization: {title}")

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
