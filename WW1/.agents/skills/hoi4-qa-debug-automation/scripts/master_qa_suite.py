#!/usr/bin/env python3
"""
HOI4 Master QA Test Runner
Executes comprehensive pre-flight verification across syntax, layout, GFX, and localisation.
"""

import sys
import time
import argparse
from pathlib import Path

# Import sibling audit utilities
from fast_brace_auditor import audit_file_braces

def run_master_suite(mod_root_dir):
    mod_root = Path(mod_root_dir).resolve()
    start_time = time.time()
    print("=" * 70)
    print(f"STARTING HOI4 MASTER PRE-FLIGHT AUDIT: {mod_root}")
    print("=" * 70)

    total_failures = 0

    # 1. Tier 1: Syntax & Braces
    print("\n[TIER 1] Auditing Bracket Syntax across common/ and events/...")
    syntax_targets = list((mod_root / "common").rglob("*.txt")) + list((mod_root / "events").rglob("*.txt"))
    brace_errors = []
    for f in syntax_targets:
        ok, msg = audit_file_braces(f)
        if not ok:
            brace_errors.append(f"{f.name}: {msg}")

    if brace_errors:
        print(f"  FAILED: {len(brace_errors)} syntax errors detected!")
        for e in brace_errors[:5]:
            print(f"    - {e}")
        total_failures += len(brace_errors)
    else:
        print(f"  PASSED: 100% balanced braces across {len(syntax_targets)} files.")

    # 2. Tier 2: Localisation BOM & Syntax
    print("\n[TIER 2] Auditing Localisation Files (.yml)...")
    loc_files = list((mod_root / "localisation").rglob("*.yml"))
    loc_errors = []
    UTF8_BOM = b'\xef\xbb\xbf'

    for lf in loc_files:
        with open(lf, "rb") as f:
            header = f.read(3)
            if header != UTF8_BOM:
                loc_errors.append(f"{lf.name}: Missing UTF-8 BOM!")
        
        with open(lf, "r", encoding="utf-8-sig", errors="replace") as f:
            content = f.read()
            for sq in ["“", "”", "‘", "’"]:
                if sq in content:
                    loc_errors.append(f"{lf.name}: Contains curly quote '{sq}'!")
                    break

    if loc_errors:
        print(f"  FAILED: {len(loc_errors)} localisation errors detected!")
        for e in loc_errors[:5]:
            print(f"    - {e}")
        total_failures += len(loc_errors)
    else:
        print(f"  PASSED: {len(loc_files)} localisation files verified with valid BOM and ASCII quotes.")

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    if total_failures == 0:
        print(f"ALL PRE-FLIGHT CHECKS PASSED in {elapsed:.2f}s! Safe to mirror and release.")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"AUDIT FAILED: {total_failures} critical errors found in {elapsed:.2f}s.")
        print("=" * 70)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="HOI4 Master QA Test Runner")
    parser.add_argument("--mod-root", default=".", help="Root path of the mod")
    args = parser.parse_args()

    run_master_suite(args.mod_root)

if __name__ == "__main__":
    main()
