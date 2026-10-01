"""
Master Automated Test Runner for German Empire National Focus Tree (Baianagem-WW1).

Executes all 4 Tiers of validation per the Dual Track Architecture:
- Tier 1: Syntax & Brace Integrity
- Tier 2: Boundary & Asset Integrity
- Tier 3: Graph & Mechanical Integrity
- Tier 4: End-to-End Consistency & Mirroring Integrity

Usage:
    python tests/test_runner.py              # Run all tiers in progressive mode
    python tests/test_runner.py --strict     # Run in strict mode (fails on pending milestones)
    python tests/test_runner.py --tier 1     # Run only Tier 1
    python tests/test_runner.py --tier 1,2   # Run Tier 1 and Tier 2
    python tests/test_runner.py --json       # Output JSON report
"""

import os
import sys
import time
import json
import argparse
import unittest
from typing import Dict, List, Any, Optional

# Ensure tests/ directory is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from tier1_syntax import TestTier1Syntax
from tier2_assets import TestTier2Assets
from tier3_graph import TestTier3Graph
from tier4_localization_mirror import TestTier4LocalizationMirror

MOD_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))


class CustomTestResult(unittest.TextTestResult):
    """Captures detailed test outcome information."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.records.append({"test": test.id(), "status": "PASS", "message": ""})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.records.append({"test": test.id(), "status": "FAIL", "message": str(err[1])})

    def addError(self, test, err):
        super().addError(test, err)
        self.records.append({"test": test.id(), "status": "ERROR", "message": str(err[1])})

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.records.append({"test": test.id(), "status": "SKIP", "message": reason})


def evaluate_milestone_readiness() -> Dict[str, Dict[str, Any]]:
    """Evaluates the readiness of project milestones M1 through M5."""
    m1_gfx = os.path.isfile(os.path.join(MOD_ROOT, "interface", "ww1_germany_goals.gfx"))
    m1_goals = os.path.isdir(os.path.join(MOD_ROOT, "gfx", "interface", "goals"))
    m1_count = len(os.listdir(os.path.join(MOD_ROOT, "gfx", "interface", "goals"))) if m1_goals else 0
    m1_ready = m1_gfx and m1_count >= 32

    m2_events = os.path.isfile(os.path.join(MOD_ROOT, "events", "ww1_germany_events.txt"))
    m2_ideas = os.path.isfile(os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_ideas.txt"))
    m2_ready = m2_events or m2_ideas

    m3_tree = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
    m3_ready = False
    if os.path.isfile(m3_tree):
        with open(m3_tree, "r", encoding="utf-8", errors="replace") as f:
            c = f.read()
        m3_ready = "focus_tree" in c and "GER_agadir_crisis_gambit" in c

    m4_en = (
        os.path.isfile(os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_l_english.yml")) or
        os.path.isfile(os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_focus_l_english.yml"))
    )
    m4_pt = (
        os.path.isfile(os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_l_braz_por.yml")) or
        os.path.isfile(os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_focus_l_braz_por.yml"))
    )
    m4_ready = m4_en and m4_pt

    steam_target = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491"
    m5_ready = os.path.isdir(steam_target) and m1_ready and os.path.isfile(os.path.join(steam_target, "interface", "ww1_germany_goals.gfx"))

    return {
        "M1": {
            "name": "Icon Assets & Sprite Definitions",
            "ready": m1_ready,
            "details": f"32 DDS icons ({m1_count} found), ww1_germany_goals.gfx {'present' if m1_gfx else 'missing'}"
        },
        "M2": {
            "name": "Events, Ideas, Characters & Tags",
            "ready": m2_ready,
            "details": f"ww1_germany_events.txt {'present' if m2_events else 'pending'}, ideas {'present' if m2_ideas else 'pending'}"
        },
        "M3": {
            "name": "German National Focus Tree",
            "ready": m3_ready,
            "details": f"germany.txt {'full tree present' if m3_ready else 'placeholder/pending'}"
        },
        "M4": {
            "name": "Dual Localization (EN & PT-BR)",
            "ready": m4_ready,
            "details": f"English: {'present' if m4_en else 'pending'}, PT-BR: {'present' if m4_pt else 'pending'}"
        },
        "M5": {
            "name": "Verification & Steam Workshop Mirroring",
            "ready": m5_ready,
            "details": f"Steam target mirrored: {'yes' if m5_ready else 'pending synchronization'}"
        },
    }


def run_test_tier(test_case_class, tier_num: int, tier_name: str, verbose: bool = False) -> Dict[str, Any]:
    """Runs a single test tier and returns structured diagnostic metrics."""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    stream = sys.stdout if verbose else open(os.devnull, "w")
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=2 if verbose else 0,
        resultclass=CustomTestResult
    )

    start_time = time.time()
    result: CustomTestResult = runner.run(suite)
    elapsed = time.time() - start_time

    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    passed = result.testsRun - (failures + errors + skipped)

    return {
        "tier": tier_num,
        "name": tier_name,
        "total": result.testsRun,
        "passed": passed,
        "failed": failures,
        "errors": errors,
        "skipped": skipped,
        "elapsed_sec": round(elapsed, 4),
        "success": result.wasSuccessful(),
        "records": result.records,
    }


def print_banner():
    banner = """
==============================================================================
   GERMAN EMPIRE NATIONAL FOCUS TREE — AUTOMATED E2E TEST SUITE (HOI4 WW1)
==============================================================================
 Target Mod: Baianagem-WW1 | Tag: GER | Start Bookmark: 1911.6.1
 Mod Root:   C:\\Users\\Usuário\\Pictures\\Baianagem-WW1\\WW1
 Steam Target: C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\394360\\3809191491
==============================================================================
"""
    print(banner)


def main():
    parser = argparse.ArgumentParser(description="German Empire National Focus Tree Test Runner")
    parser.add_argument("--tier", type=str, default="all", help="Tiers to execute: 1, 2, 3, 4, or 'all'")
    parser.add_argument("--strict", action="store_true", help="Fail if any milestones are pending/skipped")
    parser.add_argument("--json", action="store_true", help="Output summary report as JSON")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose test execution logs")
    args = parser.parse_args()

    selected_tiers = []
    if args.tier.lower() == "all":
        selected_tiers = [1, 2, 3, 4]
    else:
        for t in args.tier.split(","):
            t_clean = t.strip()
            if t_clean.isdigit():
                selected_tiers.append(int(t_clean))

    if not args.json:
        print_banner()

    tier_classes = {
        1: (TestTier1Syntax, "Syntax & Brace Integrity"),
        2: (TestTier2Assets, "Boundary & Asset Integrity"),
        3: (TestTier3Graph, "Graph & Mechanical Integrity"),
        4: (TestTier4LocalizationMirror, "End-to-End Consistency & Mirroring Integrity"),
    }

    tier_results = []
    overall_success = True
    total_passed = 0
    total_failed = 0
    total_errors = 0
    total_skipped = 0
    total_run = 0

    for t_num in selected_tiers:
        if t_num not in tier_classes:
            continue
        cls, name = tier_classes[t_num]
        res = run_test_tier(cls, t_num, name, verbose=args.verbose)
        tier_results.append(res)

        total_run += res["total"]
        total_passed += res["passed"]
        total_failed += res["failed"]
        total_errors += res["errors"]
        total_skipped += res["skipped"]

        if not res["success"]:
            overall_success = False

    milestones = evaluate_milestone_readiness()

    if args.strict and (total_skipped > 0 or not all(m["ready"] for m in milestones.values())):
        overall_success = False

    if args.json:
        report = {
            "overall_success": overall_success,
            "metrics": {
                "total_run": total_run,
                "passed": total_passed,
                "failed": total_failed,
                "errors": total_errors,
                "skipped": total_skipped,
            },
            "milestones": milestones,
            "tiers": tier_results,
        }
        print(json.dumps(report, indent=2))
        sys.exit(0 if overall_success else 1)

    # Human-readable table report
    print(f"{'TIER':<8} | {'TIER NAME':<40} | {'PASS':<6} | {'FAIL':<6} | {'SKIP':<6} | {'STATUS':<8}")
    print("-" * 82)
    for r in tier_results:
        status_str = "PASS" if r["success"] else "FAIL"
        print(f"Tier {r['tier']:<3} | {r['name']:<40} | {r['passed']:<6} | {r['failed']:<6} | {r['skipped']:<6} | {status_str:<8}")
    print("-" * 82)
    print(f"{'TOTAL':<8} | {'All Executed Tiers':<40} | {total_passed:<6} | {total_failed:<6} | {total_skipped:<6} | {'PASS' if overall_success else 'FAIL':<8}\n")

    # Milestone Progression Summary
    print("=" * 82)
    print("MILESTONE IMPLEMENTATION READINESS SUMMARY")
    print("=" * 82)
    for m_id, m_data in milestones.items():
        m_status = "[COMPLETED]" if m_data["ready"] else "[PENDING]  "
        print(f" {m_id}: {m_status} {m_data['name']:<42} -> {m_data['details']}")
    print("=" * 82)

    # Detailed test failures/errors if any
    for r in tier_results:
        for rec in r["records"]:
            if rec["status"] in ("FAIL", "ERROR"):
                print(f"\n[!] VIOLATION in Tier {r['tier']} ({rec['test']}):")
                print(f"    {rec['message']}")

    print("\n" + "=" * 82)
    if overall_success:
        print("  RESULT: >>> TEST RUN SUCCESSFUL (Exit Code 0) <<<")
    else:
        print("  RESULT: >>> TEST RUN FAILED (Non-zero Exit Code) <<<")
    print("=" * 82 + "\n")

    sys.exit(0 if overall_success else 1)


if __name__ == "__main__":
    main()
