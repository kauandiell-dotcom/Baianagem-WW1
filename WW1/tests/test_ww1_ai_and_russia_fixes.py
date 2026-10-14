"""Master QA Test Suite for AI Tactical Overhaul, Tag-Safe Russian Civil War, and Crisis Balance.

Validates:
1. Tactical defines (MIN_PLANNING_BONUS_TO_ATTACK, PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL, ORG_UNIT_WEAK, STRENGTH_UNIT_WEAK, CORPS_COMMANDER_DIVISIONS_CAP).
2. Bulgaria Alliance & War Entry (ww1_germany_events.33 war call on SER and ww1_bulgaria_ai_strategy.txt).
3. Tag-Safe Russian Civil War (zero start_civil_war commands, clean SOV/WHT tag references).
4. Russian Crisis Variable Reconciliation (zero SOV_unrest/SOV_hunger, migration to SOV_worker_unrest/SOV_urban_hunger).
5. Okhrana Crackdown Balance & Tooltips (custom_trigger_tooltip, non-instant days_remove >= 60).
"""

import os
import re
import unittest

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestAIAndRussiaFixes(unittest.TestCase):
    """QA test cases for WW1 AI tactical defines, Bulgarian war entry, and Russian rework fixes."""

    def test_ai_tactical_defines(self):
        """Verifies common/defines/ww1_ai_defines.lua configures tactical patience & corps limits."""
        defines_path = os.path.join(MOD_ROOT, "common", "defines", "ww1_ai_defines.lua")
        self.assertTrue(os.path.isfile(defines_path), f"Missing AI defines file: {defines_path}")

        with open(defines_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # MIN_PLANNING_BONUS_TO_ATTACK >= 0.65
        m_plan = re.search(r"\bMIN_PLANNING_BONUS_TO_ATTACK\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(m_plan, "MIN_PLANNING_BONUS_TO_ATTACK define not found in ww1_ai_defines.lua")
        self.assertGreaterEqual(
            float(m_plan.group(1)),
            0.65,
            f"MIN_PLANNING_BONUS_TO_ATTACK must be >= 0.65, found {m_plan.group(1)}"
        )

        # PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL >= 0.60
        m_cancel = re.search(r"\bPLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(m_cancel, "PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL define not found in ww1_ai_defines.lua")
        self.assertGreaterEqual(
            float(m_cancel.group(1)),
            0.60,
            f"PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL must be >= 0.60, found {m_cancel.group(1)}"
        )

        # ORG_UNIT_WEAK >= 0.40
        m_org = re.search(r"\bORG_UNIT_WEAK\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(m_org, "ORG_UNIT_WEAK define not found in ww1_ai_defines.lua")
        self.assertGreaterEqual(
            float(m_org.group(1)),
            0.40,
            f"ORG_UNIT_WEAK must be >= 0.40, found {m_org.group(1)}"
        )

        # STRENGTH_UNIT_WEAK >= 0.50
        m_str = re.search(r"\bSTRENGTH_UNIT_WEAK\s*=\s*([0-9.]+)", content)
        self.assertIsNotNone(m_str, "STRENGTH_UNIT_WEAK define not found in ww1_ai_defines.lua")
        self.assertGreaterEqual(
            float(m_str.group(1)),
            0.50,
            f"STRENGTH_UNIT_WEAK must be >= 0.50, found {m_str.group(1)}"
        )

        # CORPS_COMMANDER_DIVISIONS_CAP == 24
        m_cap = re.search(r"\bCORPS_COMMANDER_DIVISIONS_CAP\s*=\s*([0-9]+)", content)
        self.assertIsNotNone(m_cap, "CORPS_COMMANDER_DIVISIONS_CAP define not found in ww1_ai_defines.lua")
        self.assertEqual(
            int(m_cap.group(1)),
            24,
            f"CORPS_COMMANDER_DIVISIONS_CAP must equal 24, found {m_cap.group(1)}"
        )

    def test_bulgaria_alliance_and_war_call(self):
        """Verifies Bulgaria alliance event ww1_germany_events.33 calls war on SER and AI strategy exists."""
        events_path = os.path.join(MOD_ROOT, "events", "ww1_germany_events.txt")
        self.assertTrue(os.path.isfile(events_path), f"Missing {events_path}")
        with open(events_path, "r", encoding="utf-8", errors="replace") as f:
            events_text = f.read()

        # Find event ww1_germany_events.33
        evt_match = re.search(r"\bid\s*=\s*ww1_germany_events\.33\b", events_text)
        self.assertIsNotNone(evt_match, "ww1_germany_events.33 not found in ww1_germany_events.txt")

        start_idx = evt_match.start()
        # Find Option A
        opt_a_match = re.search(r"name\s*=\s*ww1_germany_events\.33\.a\b", events_text[start_idx:])
        self.assertIsNotNone(opt_a_match, "Option A not found in ww1_germany_events.33")
        opt_start = start_idx + opt_a_match.start()

        # Bounding Option A (before option B or closing brace)
        opt_b_match = re.search(r"name\s*=\s*ww1_germany_events\.33\.b\b", events_text[opt_start:])
        end_opt_a = opt_start + opt_b_match.start() if opt_b_match else opt_start + 1000
        opt_a_text = events_text[opt_start:end_opt_a]

        # Asserts declare_war_on or war call on SER in option A
        has_ser_war = (
            re.search(r"declare_war_on\s*=\s*\{\s*target\s*=\s*SER", opt_a_text) is not None or
            re.search(r"declare_war_on\s*=\s*SER", opt_a_text) is not None or
            re.search(r"add_to_war\s*=\s*\{\s*targeted_alliance\s*=\s*GER\s*enemy\s*=\s*SER", opt_a_text) is not None or
            re.search(r"SER\s*=\s*\{\s*ROOT\s*=\s*\{\s*declare_war_on", opt_a_text) is not None or
            re.search(r"(declare_war_on|add_to_war).*?SER", opt_a_text, re.DOTALL) is not None
        )
        self.assertTrue(
            has_ser_war,
            "ww1_germany_events.33 option A does not call Bulgaria to war / declare war against Serbia (SER)"
        )

        # Check common/ai_strategy/ww1_bulgaria_ai_strategy.txt
        strat_path = os.path.join(MOD_ROOT, "common", "ai_strategy", "ww1_bulgaria_ai_strategy.txt")
        self.assertTrue(os.path.isfile(strat_path), f"Missing Bulgaria AI strategy file: {strat_path}")
        with open(strat_path, "r", encoding="utf-8", errors="replace") as f:
            strat_text = f.read()

        # Asserts high weights for Germany alliance and Serbia war
        has_ger_strat = (
            re.search(r"(?:id|target)\s*=\s*GER\b.*?value\s*=\s*([0-9]+)", strat_text, re.DOTALL) is not None
        )
        self.assertTrue(has_ger_strat, "ww1_bulgaria_ai_strategy.txt does not configure strategy towards GER")

        has_ser_strat = (
            re.search(r"(?:id|target)\s*=\s*SER\b.*?value\s*=\s*([0-9]+)", strat_text, re.DOTALL) is not None
        )
        self.assertTrue(has_ser_strat, "ww1_bulgaria_ai_strategy.txt does not configure strategy towards SER")

    def test_tag_safe_russian_civil_war(self):
        """Verifies zero start_civil_war commands and asserts tag-safe SOV/WHT transition in ww1_russia.255 and 220."""
        events_path = os.path.join(MOD_ROOT, "events", "ww1_ger_rus_rework_events.txt")
        self.assertTrue(os.path.isfile(events_path), f"Missing {events_path}")
        with open(events_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Asserts zero occurrences of start_civil_war in the entire file!
        civil_war_matches = re.findall(r"\bstart_civil_war\b", content)
        self.assertEqual(
            len(civil_war_matches),
            0,
            f"Found {len(civil_war_matches)} occurrences of 'start_civil_war' in {events_path}. Tag-safe transition required!"
        )

        # Helper to extract event block
        def get_event_block(event_id: str) -> str:
            m = re.search(rf"(?m)^\t?id\s*=\s*{re.escape(event_id)}\b", content)
            if not m:
                m = re.search(rf"\bid\s*=\s*{re.escape(event_id)}\b", content)
            if not m:
                return ""
            start = m.start()
            next_m = re.search(r"(?m)^country_event\s*=", content[m.end():])
            end = m.end() + next_m.start() if next_m else len(content)
            return content[start:end]

        evt_255 = get_event_block("ww1_russia.255")
        self.assertTrue(len(evt_255) > 0, "Event ww1_russia.255 not found")
        self.assertIn("WHT", evt_255, "Event ww1_russia.255 does not reference tag WHT")
        self.assertIn("SOV", evt_255, "Event ww1_russia.255 does not reference tag SOV")

        evt_220 = get_event_block("ww1_russia.220")
        self.assertTrue(len(evt_220) > 0, "Event ww1_russia.220 not found")
        self.assertIn("WHT", evt_220, "Event ww1_russia.220 does not reference tag WHT")
        self.assertIn("SOV", evt_220, "Event ww1_russia.220 does not reference tag SOV")

        # Check Russian Civil War ignition event ww1_russia_civil_war.1
        cw_event_file = os.path.join(MOD_ROOT, "events", "ww1_russia_civil_war_events.txt")
        self.assertTrue(os.path.isfile(cw_event_file), f"Missing {cw_event_file}")
        with open(cw_event_file, "r", encoding="utf-8", errors="replace") as f:
            cw_text = f.read()

        self.assertIn("leave_faction = yes", cw_text, "SOV must leave the Entente on civil war eruption")
        self.assertIn("can_join_factions = no", cw_text, "Faction rule can_join_factions = no missing from civil war")
        self.assertIn("ww1_russia_civil_war.10", cw_text, "Red Victory scripted conclusion event missing")
        self.assertIn("ww1_russia_civil_war.20", cw_text, "White Victory scripted conclusion event missing")

        # Check AI isolation strategy exists
        strat_file = os.path.join(MOD_ROOT, "common", "ai_strategy", "ww1_russian_civil_war_ai_strategy.txt")
        self.assertTrue(os.path.isfile(strat_file), f"Missing {strat_file}")
        with open(strat_file, "r", encoding="utf-8", errors="replace") as f:
            strat_text = f.read()
        self.assertIn("join_faction", strat_text)
        self.assertIn("-5000", strat_text)

    def test_russian_crisis_variable_reconciliation(self):
        """Verifies zero legacy SOV_unrest/SOV_hunger and confirms SOV_worker_unrest/SOV_urban_hunger in decisions."""
        decisions_path = os.path.join(MOD_ROOT, "common", "decisions", "ww1_ger_rus_rework_decisions.txt")
        self.assertTrue(os.path.isfile(decisions_path), f"Missing {decisions_path}")
        with open(decisions_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Zero occurrences of legacy SOV_unrest and SOV_hunger as exact variable names
        unrest_matches = re.findall(r"\bSOV_unrest\b", content)
        hunger_matches = re.findall(r"\bSOV_hunger\b", content)

        self.assertEqual(
            len(unrest_matches),
            0,
            f"Found {len(unrest_matches)} legacy occurrences of 'SOV_unrest' in {decisions_path}. Must use 'SOV_worker_unrest'!"
        )
        self.assertEqual(
            len(hunger_matches),
            0,
            f"Found {len(hunger_matches)} legacy occurrences of 'SOV_hunger' in {decisions_path}. Must use 'SOV_urban_hunger'!"
        )

        # Must use SOV_worker_unrest and SOV_urban_hunger
        self.assertIn("SOV_worker_unrest", content, "Missing 'SOV_worker_unrest' in decisions")
        self.assertIn("SOV_urban_hunger", content, "Missing 'SOV_urban_hunger' in decisions")

    def test_okhrana_crackdown_balance_and_tooltips(self):
        """Verifies SOV_dec_crush_bolsheviks_okhrana has localized tooltips, non-instant duration, and tension/stability triggers."""
        decisions_path = os.path.join(MOD_ROOT, "common", "decisions", "ww1_ger_rus_rework_decisions.txt")
        self.assertTrue(os.path.isfile(decisions_path), f"Missing {decisions_path}")
        with open(decisions_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        m = re.search(r"\bSOV_dec_crush_bolsheviks_okhrana\s*=\s*\{", content)
        self.assertIsNotNone(m, "SOV_dec_crush_bolsheviks_okhrana decision not found in decisions file")

        # Extract decision block matching braces
        start = m.start()
        brace_pos = content.find("{", start)
        depth = 1
        cur = brace_pos + 1
        while cur < len(content) and depth > 0:
            if content[cur] == "{":
                depth += 1
            elif content[cur] == "}":
                depth -= 1
            cur += 1
        dec_block = content[start:cur]

        # Asserts custom_trigger_tooltip exists and references tension/stability
        self.assertIn("custom_trigger_tooltip", dec_block, "SOV_dec_crush_bolsheviks_okhrana must have a custom_trigger_tooltip")
        self.assertTrue(
            "tension" in dec_block.lower() or "SOV_revolutionary_tension" in dec_block,
            "SOV_dec_crush_bolsheviks_okhrana triggers must reference tension"
        )
        self.assertTrue(
            "stability" in dec_block.lower() or "has_stability" in dec_block,
            "SOV_dec_crush_bolsheviks_okhrana triggers must reference stability"
        )

        # Asserts days_remove >= 60 or multi-day mission rather than instant win
        m_days = re.search(r"\bdays_remove\s*=\s*([0-9]+)", dec_block)
        m_mission = re.search(r"\bdays_mission_timeout\s*=\s*([0-9]+)", dec_block)

        has_timed_duration = False
        if m_days and int(m_days.group(1)) >= 60:
            has_timed_duration = True
        elif m_mission and int(m_mission.group(1)) >= 60:
            has_timed_duration = True

        self.assertTrue(
            has_timed_duration,
            "SOV_dec_crush_bolsheviks_okhrana must have days_remove >= 60 (or multi-day mission >= 60) rather than instant resolution"
        )


if __name__ == "__main__":
    unittest.main()
