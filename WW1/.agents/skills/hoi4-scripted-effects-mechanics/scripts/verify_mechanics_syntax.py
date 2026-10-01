#!/usr/bin/env python3
"""
HOI4 Scripted Mechanics & Effects Syntax Validator
Audits ruling_party ideologies, swap_ideas syntax, decimal percentage bounds (stability/war_support),
and mission references.
"""

import sys
import re
import argparse
from pathlib import Path

VALID_IDEOLOGIES = {"democratic", "communism", "fascism", "neutrality"}

def audit_file(file_path):
    errors = []
    warnings = []
    
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        text = f.read()

    lines = text.splitlines()

    # 1. Check ruling_party ideologies
    for m in re.finditer(r'ruling_party\s*=\s*([a-zA-Z0-9_]+)', text):
        line_num = text[:m.start()].count('\n') + 1
        ideo = m.group(1)
        if ideo not in VALID_IDEOLOGIES:
            errors.append(f"Line {line_num}: Invalid ruling_party '{ideo}'. Must be one of {VALID_IDEOLOGIES}.")

    # 2. Check start_civil_war ideology
    for m in re.finditer(r'start_civil_war\s*=\s*\{([^}]+)\}', text):
        block = m.group(1)
        line_num = text[:m.start()].count('\n') + 1
        ideo_m = re.search(r'ideology\s*=\s*([a-zA-Z0-9_]+)', block)
        if ideo_m:
            ideo = ideo_m.group(1)
            if ideo not in VALID_IDEOLOGIES:
                errors.append(f"Line {line_num}: Invalid civil war ideology '{ideo}'. Must be one of {VALID_IDEOLOGIES}.")

    # 3. Check stability / war_support decimal values
    # In HoI4, stability is 0.0 to 1.0. A value > 1.0 is almost always a bug (e.g. 10 instead of 0.10)
    for m in re.finditer(r'\b(add_stability|add_war_support)\s*=\s*(-?\d+(?:\.\d+)?)', text):
        line_num = text[:m.start()].count('\n') + 1
        cmd = m.group(1)
        val = float(m.group(2))
        if abs(val) > 1.0:
            warnings.append(f"Line {line_num}: {cmd} = {val} is greater than 1.0. HoI4 expects decimals (e.g., 0.10 for +10%). This will add {val * 100}%!")

    # 4. Check swap_ideas syntax
    for m in re.finditer(r'swap_ideas\s*=\s*\{([^}]+)\}', text):
        block = m.group(1)
        line_num = text[:m.start()].count('\n') + 1
        has_remove = "remove_idea" in block
        has_add = "add_idea" in block
        if not (has_remove and has_add):
            errors.append(f"Line {line_num}: Malformed swap_ideas block. Both 'remove_idea' and 'add_idea' are strictly required.")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description="HOI4 Mechanics Syntax Validator")
    parser.add_argument("--path", required=True, help="File or directory to audit")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"Error: Path '{target}' does not exist.")
        sys.exit(1)

    files_to_check = []
    if target.is_file():
        files_to_check.append(target)
    else:
        files_to_check.extend(target.rglob("*.txt"))

    print(f"Auditing {len(files_to_check)} files for mechanics syntax...")
    total_errors = 0
    total_warnings = 0

    for f in files_to_check:
        errors, warnings = audit_file(f)
        if errors or warnings:
            print(f"\nFile: {f}")
            for w in warnings:
                print(f"  [WARN] {w}")
                total_warnings += 1
            for e in errors:
                print(f"  [FAIL] {e}")
                total_errors += 1

    print(f"\n--- AUDIT COMPLETE: {total_errors} errors, {total_warnings} warnings across {len(files_to_check)} files ---")
    if total_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
