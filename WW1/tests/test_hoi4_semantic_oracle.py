"""
Tests for the Clausewitz HOI4 Semantic Oracle.
Verifies that the oracle accurately detects invalid/hallucinated modifier tokens
and accepts valid HOI4 country modifiers.
"""
import unittest
import sys
import os

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if MOD_ROOT not in sys.path:
    sys.path.insert(0, MOD_ROOT)

from scripts.hoi4_semantic_oracle import (
    get_valid_modifiers,
    is_valid_country_modifier,
    audit_modifier_dict
)


class TestSemanticOracle(unittest.TestCase):
    def test_oracle_loads_modifiers(self):
        mods = get_valid_modifiers()
        self.assertGreater(len(mods), 400, "Oracle should contain at least 400 valid modifiers")
        # Check standard known modifiers
        self.assertIn("industrial_capacity_factory", mods)
        self.assertIn("army_org_factor", mods)
        self.assertIn("research_speed_factor", mods)
        self.assertIn("navy_submarine_attack_factor", mods)
        self.assertIn("consumer_goods_factor", mods)

    def test_oracle_rejects_hallucinated_tokens(self):
        hallucinated = [
            "carrier_traffic_factor",
            "production_cost_max_armor_factor",
            "electronics_tech_research_speed_factor",
            "industry_tech_research_speed_factor",
            "sub_attack",
            "sub_detection",
            "screen_defense_factor",
            "leader_cost_factor",
            "experience_gain_army_leader_factor",
            "cryptology_defense",
            "signal_company_initiative"
        ]
        for token in hallucinated:
            self.assertFalse(
                is_valid_country_modifier(token),
                f"Token '{token}' should be rejected as invalid/hallucinated!"
            )

    def test_audit_modifier_dict(self):
        bad_dict = {
            "sub_attack": 0.15,
            "army_org_factor": 0.05
        }
        invalid_keys = audit_modifier_dict(bad_dict)
        self.assertEqual(invalid_keys, ["sub_attack"])


if __name__ == "__main__":
    unittest.main()
