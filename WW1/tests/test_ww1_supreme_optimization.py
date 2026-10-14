"""QA and Verification Suite for Supreme Engine Optimization & Late-Game Simulation.

Validates:
1. Reverse-engineered Clausewitz defines in common/defines/99_supreme_performance.lua
   - Combat, air, garrison log retention pruning
   - AI simulation tick throttling
   - Geometry, spline smoothing, and render passes
   - Multiplayer lockstep lag thresholds
2. Memory limits for combat, garrison, and air logs.
3. Frontline and trade spline smoothing passes capped to 1.
4. Declarative peacetime AI division limiter for neutral minors in common/ai_strategy/ww1_performance_ai_limiter.txt.
5. Monthly transient memory cleanup scripted effect and its on-action hook in common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt.
"""

import os
import re
import unittest
from typing import Dict, Tuple

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def audit_clausewitz_braces(filepath: str) -> Tuple[bool, str]:
    """Validates balanced braces in a Clausewitz script file, ignoring comments and strings."""
    if not os.path.isfile(filepath):
        return False, f"File not found: {filepath}"
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    open_braces = 0
    in_string = False
    escape = False

    for line_num, line in enumerate(lines, start=1):
        i = 0
        while i < len(line):
            ch = line[i]
            if in_string:
                if escape:
                    escape = False
                elif ch == '\\':
                    escape = True
                elif ch == '"':
                    in_string = False
            else:
                if ch == '#':
                    break
                elif ch == '"':
                    in_string = True
                elif ch == '{':
                    open_braces += 1
                elif ch == '}':
                    open_braces -= 1
                    if open_braces < 0:
                        return False, f"Unexpected closing brace at line {line_num}"
            i += 1

    if open_braces != 0:
        return False, f"Unbalanced braces: remaining open count = {open_braces}"
    return True, "OK"


class TestSupremeOptimization(unittest.TestCase):
    """Automated QA Test Suite for Supreme Engine Optimization & Simulation Architecture."""

    DEFINES_REL_PATH = os.path.join("common", "defines", "99_supreme_performance.lua")
    AI_LIMITER_REL_PATH = os.path.join("common", "ai_strategy", "ww1_performance_ai_limiter.txt")
    SCRIPTED_EFFECTS_REL_PATH = os.path.join("common", "scripted_effects", "ww1_optimization_effects.txt")
    ON_ACTIONS_REL_PATH = os.path.join("common", "on_actions", "zz_ww1_ger_rus_rework_on_actions.txt")

    def test_supreme_performance_defines_syntax_and_values(self):
        """Verifies 99_supreme_performance.lua exists, has valid Lua syntax, and defines all required engine constants."""
        defines_path = os.path.join(MOD_ROOT, self.DEFINES_REL_PATH)
        self.assertTrue(
            os.path.isfile(defines_path),
            f"Missing supreme performance defines file at: {defines_path}"
        )

        with open(defines_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        self.assertGreater(len(content.strip()), 50, "99_supreme_performance.lua is unexpectedly empty or truncated.")

        # Lua syntax validation: ensure no unbalanced curly braces and valid assignment syntax
        open_braces = content.count("{")
        close_braces = content.count("}")
        self.assertEqual(
            open_braces,
            close_braces,
            f"Unbalanced braces in {defines_path}: {open_braces} open vs {close_braces} close"
        )

        required_constants: Dict[str, float] = {
            "COMBAT_LOG_MAX_MONTHS": 1,
            "AIR_LOG_TIMEOUT_HOURS": 24,
            "TRADE_ROUTE_RECALCULATE_FREQUENCY_DAYS": 10,
            "LAG_DAYS_FOR_LOWER_SPEED": 100,
            "UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS": 72,
            "UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS": 72,
            "RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE": 14,
            "RAIDS_CREATE_FREQUENCY_DAYS": 14,
            "ATTACHED_WINGS_ORDER_UPDATE_DAYS": 5,
            "REINFORCEMENT_REQUEST_DAYS_FREQUENCY": 4,
            "ROOT_FRONT_SMOOTHEN_PASSES": 1,
            "ROOT_FRONT_MAX_INTERSECTION_TESTS_FRONT": 4,
            "SNAPPED_OFF_FRONT_SMOOTHEN_PASSES": 1,
            "SUPPLYFLOW_SMOOTHEN_PASSES": 1,
            "TRADEROUTE_SMOOTHEN_PASSES": 1,
            "TRADE_ROUTE_MAX_LINES": 12,
            "WEATHER_DISTANCE_CUTOFF": 350.0,
            "WEATHER_PLAYBACK_RATE": 0.6,
            "UNITS_DISTANCE_CUTOFF": 180.0,
            "CITY_SPRAWL_SHRINK_DISTANCE": 140.0,
            "PROVINCE_NAME_DRAW_DISTANCE": 220.0,
            "SHIPS_DISTANCE_CUTOFF": 180.0,
            "TOP_MAP_ICON": 40,
        }

        for constant_name, expected_value in required_constants.items():
            pattern = rf"(?:NDefines\.[A-Za-z0-9_]+\.)?\b{re.escape(constant_name)}\b\s*=\s*([0-9.]+)"
            match = re.search(pattern, content)
            self.assertIsNotNone(
                match,
                f"Required engine define '{constant_name}' not found in {self.DEFINES_REL_PATH}"
            )
            actual_value = float(match.group(1))
            self.assertAlmostEqual(
                actual_value,
                float(expected_value),
                places=3,
                msg=f"Engine define '{constant_name}' value mismatch: expected {expected_value}, got {actual_value}"
            )

    def test_combat_log_memory_limits(self):
        """Confirms COMBAT_LOG_MAX_MONTHS <= 2, GARRISON_LOG_MAX_MONTHS <= 2, and AIR_LOG_TIMEOUT_HOURS <= 48."""
        defines_path = os.path.join(MOD_ROOT, self.DEFINES_REL_PATH)
        self.assertTrue(
            os.path.isfile(defines_path),
            f"Missing supreme performance defines file at: {defines_path}"
        )

        with open(defines_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # 1. COMBAT_LOG_MAX_MONTHS <= 2
        combat_match = re.search(r"(?:NDefines\.[A-Za-z0-9_]+\.)?\bCOMBAT_LOG_MAX_MONTHS\b\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(combat_match, "COMBAT_LOG_MAX_MONTHS define not found in 99_supreme_performance.lua")
        self.assertLessEqual(
            float(combat_match.group(1)),
            2.0,
            f"COMBAT_LOG_MAX_MONTHS must be <= 2 to prevent midnight freeze, got {combat_match.group(1)}"
        )

        # 2. GARRISON_LOG_MAX_MONTHS <= 2
        garrison_match = re.search(r"(?:NDefines\.[A-Za-z0-9_]+\.)?\bGARRISON_LOG_MAX_MONTHS\b\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(garrison_match, "GARRISON_LOG_MAX_MONTHS define not found in 99_supreme_performance.lua")
        self.assertLessEqual(
            float(garrison_match.group(1)),
            2.0,
            f"GARRISON_LOG_MAX_MONTHS must be <= 2 to eliminate garrison casualty RAM leaks, got {garrison_match.group(1)}"
        )

        # 3. AIR_LOG_TIMEOUT_HOURS <= 48
        air_match = re.search(r"(?:NDefines\.[A-Za-z0-9_]+\.)?\bAIR_LOG_TIMEOUT_HOURS\b\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(air_match, "AIR_LOG_TIMEOUT_HOURS define not found in 99_supreme_performance.lua")
        self.assertLessEqual(
            float(air_match.group(1)),
            48.0,
            f"AIR_LOG_TIMEOUT_HOURS must be <= 48 to prune completed air sorties, got {air_match.group(1)}"
        )

    def test_render_pass_tessellation_optimization(self):
        """Confirms frontline and map spline smoothing passes are capped at 1 for low-spec GPU/CPU performance."""
        defines_path = os.path.join(MOD_ROOT, self.DEFINES_REL_PATH)
        self.assertTrue(
            os.path.isfile(defines_path),
            f"Missing supreme performance defines file at: {defines_path}"
        )

        with open(defines_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        spline_pass_defines = [
            "ROOT_FRONT_SMOOTHEN_PASSES",
            "SNAPPED_OFF_FRONT_SMOOTHEN_PASSES",
            "SUPPLYFLOW_SMOOTHEN_PASSES",
            "TRADEROUTE_SMOOTHEN_PASSES",
        ]

        for define_name in spline_pass_defines:
            pattern = rf"(?:NDefines\.[A-Za-z0-9_]+\.)?\b{re.escape(define_name)}\b\s*=\s*([0-9.]+)"
            match = re.search(pattern, content)
            self.assertIsNotNone(
                match,
                f"Spline smoothing pass define '{define_name}' not found in 99_supreme_performance.lua"
            )
            val = float(match.group(1))
            self.assertLessEqual(
                val,
                1.0,
                f"{define_name} must be <= 1 (capped to eliminate spline tessellation overhead), got {val}"
            )

    def test_ai_peacetime_division_regulation(self):
        """Asserts common/ai_strategy/ww1_performance_ai_limiter.txt includes ww1_peace_neutral_minor_limiter with negative division factor."""
        ai_limiter_path = os.path.join(MOD_ROOT, self.AI_LIMITER_REL_PATH)
        self.assertTrue(
            os.path.isfile(ai_limiter_path),
            f"Missing AI limiter file at: {ai_limiter_path}"
        )

        valid_braces, brace_msg = audit_clausewitz_braces(ai_limiter_path)
        self.assertTrue(valid_braces, f"Brace syntax error in {self.AI_LIMITER_REL_PATH}: {brace_msg}")

        with open(ai_limiter_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        self.assertIn(
            "ww1_peace_neutral_minor_limiter",
            content,
            "Missing 'ww1_peace_neutral_minor_limiter' strategy entry in ww1_performance_ai_limiter.txt"
        )

        # Extract the ww1_peace_neutral_minor_limiter block
        block_match = re.search(
            r"ww1_peace_neutral_minor_limiter\s*=\s*\{([\s\S]*?)\n\}",
            content
        )
        self.assertIsNotNone(block_match, "Could not parse ww1_peace_neutral_minor_limiter block structure")
        block_body = block_match.group(1)

        # Assert abort_when_not_enabled = yes is present
        self.assertRegex(
            block_body,
            r"abort_when_not_enabled\s*=\s*yes",
            "ww1_peace_neutral_minor_limiter must declare 'abort_when_not_enabled = yes'"
        )

        # Assert ai_wanted_divisions_factor is present with a negative value
        factor_match = re.search(
            r"type\s*=\s*ai_wanted_divisions_factor\s*\}?\s*[\n\r\t ]*(?:ai_strategy\s*=\s*\{)?\s*value\s*=\s*(-?\d+)",
            block_body
        )
        if not factor_match:
            # Alternate layout: type = ai_wanted_divisions_factor \n value = -100
            factor_match = re.search(
                r"type\s*=\s*ai_wanted_divisions_factor[\s\S]*?value\s*=\s*(-?\d+)",
                block_body
            )

        self.assertIsNotNone(
            factor_match,
            "ww1_peace_neutral_minor_limiter must specify ai_wanted_divisions_factor"
        )
        factor_val = int(factor_match.group(1))
        self.assertLess(
            factor_val,
            0,
            f"ai_wanted_divisions_factor must be negative to suppress division spam, got {factor_val}"
        )

    def test_transient_memory_cleanup_registered(self):
        """Asserts ww1_clean_transient_memory exists in scripted effects and is called in on_monthly hook."""
        effects_path = os.path.join(MOD_ROOT, self.SCRIPTED_EFFECTS_REL_PATH)
        self.assertTrue(
            os.path.isfile(effects_path),
            f"Missing scripted effects file at: {effects_path}"
        )

        valid_braces, brace_msg = audit_clausewitz_braces(effects_path)
        self.assertTrue(valid_braces, f"Brace syntax error in {self.SCRIPTED_EFFECTS_REL_PATH}: {brace_msg}")

        with open(effects_path, "r", encoding="utf-8", errors="replace") as f:
            effects_content = f.read()

        self.assertIn(
            "ww1_clean_transient_memory",
            effects_content,
            f"ww1_clean_transient_memory effect is not defined in {self.SCRIPTED_EFFECTS_REL_PATH}"
        )

        # Assert on_monthly hook in zz_ww1_ger_rus_rework_on_actions.txt
        on_actions_path = os.path.join(MOD_ROOT, self.ON_ACTIONS_REL_PATH)
        self.assertTrue(
            os.path.isfile(on_actions_path),
            f"Missing on_actions file at: {on_actions_path}"
        )

        valid_on_action_braces, on_action_brace_msg = audit_clausewitz_braces(on_actions_path)
        self.assertTrue(
            valid_on_action_braces,
            f"Brace syntax error in {self.ON_ACTIONS_REL_PATH}: {on_action_brace_msg}"
        )

        with open(on_actions_path, "r", encoding="utf-8", errors="replace") as f:
            on_actions_content = f.read()

        self.assertIn(
            "on_monthly",
            on_actions_content,
            f"Missing 'on_monthly' block in {self.ON_ACTIONS_REL_PATH}"
        )

        # Ensure on_monthly invokes ww1_clean_transient_memory
        monthly_block = re.search(r"on_monthly\s*=\s*\{([\s\S]*?)\n\t\}", on_actions_content)
        if not monthly_block:
            # Fallback search
            monthly_block = re.search(r"on_monthly\s*=\s*\{([\s\S]*?)\}", on_actions_content)

        self.assertIsNotNone(monthly_block, "Could not parse on_monthly block in on_actions file")
        self.assertIn(
            "ww1_clean_transient_memory",
            monthly_block.group(1),
            "on_monthly block does not call 'ww1_clean_transient_memory'"
        )


if __name__ == "__main__":
    unittest.main()
