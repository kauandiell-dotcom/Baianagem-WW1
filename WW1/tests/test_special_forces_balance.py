"""Special Forces Anti-Exploit, Division Hierarchy & Armor Rebalance QA Test Suite.

Asserts game rules and balances defined in the SDD specification:
- Global defines: SPECIAL_FORCES_CAP_BASE = 0.0, SPECIAL_FORCES_CAP_MIN = 48.
- Infantry Special Forces: org <= 38, breakthrough <= 0.05, hard_attack <= -0.20,
  plus polarized opposing terrain penalties.
- Historical subunits (K.u.k. Gebirgsjäger, ANZAC Corps) terrain penalties.
- Tech tree: improved_special_forces uses flat capacity (special_forces_min = 12)
  without percentage multipliers (special_forces_cap).
- Elite Infantry: preservation of shock role (breakthrough = 0.25, support & artillery eq).
- Armor / Tanks: low org (<= 15) to prevent tank-only divisions and fortress breaching buffs.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ww1_foundation import Node, parse, read


class TestSpecialForcesBalance(unittest.TestCase):
    def _get_subunits(self, relative_path: str) -> dict[str, Node]:
        nodes = parse(read(ROOT / relative_path))
        sub_units_node = next((n for n in nodes if n.key == "sub_units"), None)
        self.assertIsNotNone(sub_units_node, f"Missing 'sub_units' root in {relative_path}")
        return {n.key: n for n in sub_units_node.value if isinstance(n.value, list)}

    def _get_attr(self, node: Node, key: str) -> str | None:
        if not isinstance(node.value, list):
            return None
        for n in node.value:
            if n.key == key:
                return str(n.value)
        return None

    def _get_float_attr(self, node: Node, key: str) -> float | None:
        val = self._get_attr(node, key)
        if val is not None:
            try:
                return float(val)
            except ValueError:
                return None
        return None

    def _get_terrain_attack(self, node: Node, terrain: str) -> float | None:
        if not isinstance(node.value, list):
            return None
        terrain_node = next((n for n in node.value if n.key == terrain and isinstance(n.value, list)), None)
        if not terrain_node:
            return None
        for n in terrain_node.value:
            if n.key == "attack":
                try:
                    return float(n.value)
                except (ValueError, TypeError):
                    return None
        return None

    # 1. Global Defines in common/defines/01_defines.lua
    def test_special_forces_cap_defines(self):
        defines_text = read(ROOT / "common/defines/01_defines.lua")

        cap_base_match = re.search(r"NDefines\.NCountry\.SPECIAL_FORCES_CAP_BASE\s*=\s*([0-9.]+)", defines_text)
        self.assertIsNotNone(cap_base_match, "SPECIAL_FORCES_CAP_BASE define not found in 01_defines.lua")
        self.assertEqual(
            float(cap_base_match.group(1)),
            0.0,
            f"SPECIAL_FORCES_CAP_BASE should be 0.0 (anti-exploit base cap), found {cap_base_match.group(1)}",
        )

        cap_min_match = re.search(r"NDefines\.NCountry\.SPECIAL_FORCES_CAP_MIN\s*=\s*([0-9.]+)", defines_text)
        self.assertIsNotNone(cap_min_match, "SPECIAL_FORCES_CAP_MIN define not found in 01_defines.lua")
        self.assertEqual(
            int(float(cap_min_match.group(1))),
            48,
            f"SPECIAL_FORCES_CAP_MIN should be 48 (corps-level baseline), found {cap_min_match.group(1)}",
        )

    # 2. Marine Balance in common/units/infantry.txt
    def test_marine_balance(self):
        subunits = self._get_subunits("common/units/infantry.txt")
        self.assertIn("marine", subunits, "marine subunit definition missing in infantry.txt")
        marine = subunits["marine"]

        org = self._get_float_attr(marine, "max_organisation")
        self.assertIsNotNone(org, "marine max_organisation is missing")
        self.assertLessEqual(org, 38.0, f"marine max_organisation must be <= 38, found {org}")

        breakthrough = self._get_float_attr(marine, "breakthrough")
        self.assertIsNotNone(breakthrough, "marine breakthrough is missing")
        self.assertLessEqual(breakthrough, 0.05, f"marine breakthrough must be <= 0.05, found {breakthrough}")

        hard_attack = self._get_float_attr(marine, "hard_attack")
        self.assertIsNotNone(hard_attack, "marine hard_attack must be defined")
        self.assertLessEqual(hard_attack, -0.20, f"marine hard_attack must be <= -0.20, found {hard_attack}")

        mountain_atk = self._get_terrain_attack(marine, "mountain")
        self.assertIsNotNone(mountain_atk, "marine mountain terrain block with attack penalty is required")
        self.assertLessEqual(mountain_atk, -0.25, f"marine mountain attack must be <= -0.25, found {mountain_atk}")

        hills_atk = self._get_terrain_attack(marine, "hills")
        self.assertIsNotNone(hills_atk, "marine hills terrain block with attack penalty is required")
        self.assertLessEqual(hills_atk, -0.15, f"marine hills attack must be <= -0.15, found {hills_atk}")

    # 3. Mountaineers Balance in common/units/infantry.txt
    def test_mountaineers_balance(self):
        subunits = self._get_subunits("common/units/infantry.txt")
        self.assertIn("mountaineers", subunits, "mountaineers subunit definition missing in infantry.txt")
        mountaineers = subunits["mountaineers"]

        org = self._get_float_attr(mountaineers, "max_organisation")
        self.assertIsNotNone(org, "mountaineers max_organisation is missing")
        self.assertLessEqual(org, 38.0, f"mountaineers max_organisation must be <= 38, found {org}")

        breakthrough = self._get_float_attr(mountaineers, "breakthrough")
        self.assertIsNotNone(breakthrough, "mountaineers breakthrough is missing")
        self.assertLessEqual(breakthrough, 0.05, f"mountaineers breakthrough must be <= 0.05, found {breakthrough}")

        hard_attack = self._get_float_attr(mountaineers, "hard_attack")
        self.assertIsNotNone(hard_attack, "mountaineers hard_attack must be defined")
        self.assertLessEqual(hard_attack, -0.20, f"mountaineers hard_attack must be <= -0.20, found {hard_attack}")

        river_atk = self._get_terrain_attack(mountaineers, "river")
        self.assertIsNotNone(river_atk, "mountaineers river terrain block with attack penalty is required")
        self.assertLessEqual(river_atk, -0.25, f"mountaineers river attack must be <= -0.25, found {river_atk}")

        marsh_atk = self._get_terrain_attack(mountaineers, "marsh")
        self.assertIsNotNone(marsh_atk, "mountaineers marsh terrain block with attack penalty is required")
        self.assertLessEqual(marsh_atk, -0.25, f"mountaineers marsh attack must be <= -0.25, found {marsh_atk}")

        amphibious_atk = self._get_terrain_attack(mountaineers, "amphibious")
        self.assertIsNotNone(amphibious_atk, "mountaineers amphibious terrain block with attack penalty is required")
        self.assertLessEqual(
            amphibious_atk, -0.40, f"mountaineers amphibious attack must be <= -0.40, found {amphibious_atk}"
        )

    # 4. Ranger Battalion Balance in common/units/infantry.txt
    def test_ranger_battalion_balance(self):
        subunits = self._get_subunits("common/units/infantry.txt")
        self.assertIn("ranger_battalion", subunits, "ranger_battalion subunit definition missing in infantry.txt")
        ranger = subunits["ranger_battalion"]

        org = self._get_float_attr(ranger, "max_organisation")
        self.assertIsNotNone(org, "ranger_battalion max_organisation is missing")
        self.assertLessEqual(org, 38.0, f"ranger_battalion max_organisation must be <= 38, found {org}")

        breakthrough = self._get_float_attr(ranger, "breakthrough")
        self.assertIsNotNone(breakthrough, "ranger_battalion breakthrough is missing")
        self.assertLessEqual(breakthrough, 0.05, f"ranger_battalion breakthrough must be <= 0.05, found {breakthrough}")

        hard_attack = self._get_float_attr(ranger, "hard_attack")
        self.assertIsNotNone(hard_attack, "ranger_battalion hard_attack must be defined")
        self.assertLessEqual(hard_attack, -0.20, f"ranger_battalion hard_attack must be <= -0.20, found {hard_attack}")

        mountain_atk = self._get_terrain_attack(ranger, "mountain")
        self.assertIsNotNone(mountain_atk, "ranger_battalion mountain terrain block with attack penalty is required")
        self.assertLessEqual(mountain_atk, -0.15, f"ranger_battalion mountain attack must be <= -0.15, found {mountain_atk}")

        river_atk = self._get_terrain_attack(ranger, "river")
        self.assertIsNotNone(river_atk, "ranger_battalion river terrain block with attack penalty is required")
        self.assertLessEqual(river_atk, -0.15, f"ranger_battalion river attack must be <= -0.15, found {river_atk}")

    # 5. WW1 Special Subunits: K.u.k. Gebirgsjäger
    def test_ww1_special_subunits_kuk_gebirgsjaeger(self):
        subunits = self._get_subunits("common/units/ww1_special_subunits.txt")
        self.assertIn(
            "kuk_gebirgsjaeger", subunits, "kuk_gebirgsjaeger subunit missing in ww1_special_subunits.txt"
        )
        kuk = subunits["kuk_gebirgsjaeger"]

        river_atk = self._get_terrain_attack(kuk, "river")
        self.assertIsNotNone(river_atk, "kuk_gebirgsjaeger river terrain block with attack penalty is required")
        self.assertLessEqual(river_atk, -0.25, f"kuk_gebirgsjaeger river attack must be <= -0.25, found {river_atk}")

        amphibious_atk = self._get_terrain_attack(kuk, "amphibious")
        self.assertIsNotNone(amphibious_atk, "kuk_gebirgsjaeger amphibious terrain block with attack penalty is required")
        self.assertLessEqual(
            amphibious_atk, -0.40, f"kuk_gebirgsjaeger amphibious attack must be <= -0.40, found {amphibious_atk}"
        )

    # 6. WW1 Special Subunits: ANZAC Corps
    def test_ww1_special_subunits_anzac_corps(self):
        subunits = self._get_subunits("common/units/ww1_special_subunits.txt")
        self.assertIn("anzac_corps", subunits, "anzac_corps subunit missing in ww1_special_subunits.txt")
        anzac = subunits["anzac_corps"]

        mountain_atk = self._get_terrain_attack(anzac, "mountain")
        self.assertIsNotNone(mountain_atk, "anzac_corps mountain terrain block with attack penalty is required")
        self.assertLessEqual(mountain_atk, -0.15, f"anzac_corps mountain attack must be <= -0.15, found {mountain_atk}")

    # 7. Technology: improved_special_forces in common/technologies/infantry.txt
    def test_improved_special_forces_technology(self):
        nodes = parse(read(ROOT / "common/technologies/infantry.txt"))
        techs_node = next((n for n in nodes if n.key == "technologies"), None)
        self.assertIsNotNone(techs_node, "technologies block missing in infantry.txt")

        imp_tech = next((n for n in techs_node.value if n.key == "improved_special_forces"), None)
        self.assertIsNotNone(imp_tech, "improved_special_forces tech missing in infantry.txt")

        # Must have special_forces_min = 12
        min_cap = self._get_float_attr(imp_tech, "special_forces_min")
        self.assertIsNotNone(min_cap, "improved_special_forces must define special_forces_min")
        self.assertEqual(int(min_cap), 12, f"special_forces_min must be 12, found {min_cap}")

        # Must NOT have special_forces_cap
        pct_cap = self._get_attr(imp_tech, "special_forces_cap")
        self.assertIsNone(
            pct_cap, f"improved_special_forces must NOT define special_forces_cap multiplier, found {pct_cap}"
        )

    # 8. Elite Infantry Preservation in common/units/elite_inf.txt
    def test_elite_inf_breakthrough_and_equipment_preservation(self):
        subunits = self._get_subunits("common/units/elite_inf.txt")
        self.assertIn("elite_inf", subunits, "elite_inf subunit definition missing in elite_inf.txt")
        elite = subunits["elite_inf"]

        breakthrough = self._get_float_attr(elite, "breakthrough")
        self.assertIsNotNone(breakthrough, "elite_inf breakthrough missing")
        self.assertEqual(breakthrough, 0.25, f"elite_inf breakthrough must be 0.25, found {breakthrough}")

        need_node = next((n for n in elite.value if n.key == "need" and isinstance(n.value, list)), None)
        self.assertIsNotNone(need_node, "elite_inf need block missing")
        needs = {n.key: n.value for n in need_node.value}
        self.assertIn("support_equipment", needs, "elite_inf must require support_equipment")
        self.assertIn("artillery_equipment", needs, "elite_inf must require artillery_equipment")

    # 9. Tanks: heavy_armor
    def test_tank_heavy_armor(self):
        subunits = self._get_subunits("common/units/heavy_armor.txt")
        self.assertIn("heavy_armor", subunits, "heavy_armor subunit missing")
        tank = subunits["heavy_armor"]

        org = self._get_float_attr(tank, "max_organisation")
        self.assertIsNotNone(org, "heavy_armor max_organisation missing")
        self.assertLessEqual(org, 15.0, f"heavy_armor max_organisation must be <= 15, found {org}")

        fort_atk = self._get_terrain_attack(tank, "fort")
        self.assertIsNotNone(fort_atk, "heavy_armor fort attack modifier missing")
        self.assertGreaterEqual(fort_atk, 0.60, f"heavy_armor fort attack must be >= 0.60, found {fort_atk}")

    # 10. Tanks: medium_armor
    def test_tank_medium_armor(self):
        subunits = self._get_subunits("common/units/medium_armor.txt")
        self.assertIn("medium_armor", subunits, "medium_armor subunit missing")
        tank = subunits["medium_armor"]

        org = self._get_float_attr(tank, "max_organisation")
        self.assertIsNotNone(org, "medium_armor max_organisation missing")
        self.assertLessEqual(org, 15.0, f"medium_armor max_organisation must be <= 15, found {org}")

        fort_atk = self._get_terrain_attack(tank, "fort")
        self.assertIsNotNone(fort_atk, "medium_armor fort attack modifier missing")
        self.assertGreaterEqual(fort_atk, 0.45, f"medium_armor fort attack must be >= 0.45, found {fort_atk}")

    # 11. Tanks: light_armor
    def test_tank_light_armor(self):
        subunits = self._get_subunits("common/units/light_armor.txt")
        self.assertIn("light_armor", subunits, "light_armor subunit missing")
        tank = subunits["light_armor"]

        org = self._get_float_attr(tank, "max_organisation")
        self.assertIsNotNone(org, "light_armor max_organisation missing")
        self.assertLessEqual(org, 15.0, f"light_armor max_organisation must be <= 15, found {org}")

        fort_atk = self._get_terrain_attack(tank, "fort")
        self.assertIsNotNone(fort_atk, "light_armor fort attack modifier missing")
        self.assertGreaterEqual(fort_atk, 0.35, f"light_armor fort attack must be >= 0.35, found {fort_atk}")


if __name__ == "__main__":
    unittest.main()
