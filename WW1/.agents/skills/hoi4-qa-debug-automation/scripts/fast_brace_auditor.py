#!/usr/bin/env python3
"""
HOI4 Fast Brace & Bracket Auditor
Audits curly brace balance ({}) across Paradox script files in milliseconds,
reporting exact line, column, and token context for any unclosed or extra braces.
"""

import sys
import time
import argparse
from pathlib import Path

def audit_file_braces(file_path):
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        content = f.read()

    lines = content.splitlines()
    stack = [] # (line_num, col_num, preview)
    in_string = False
    escape = False

    for line_idx, line in enumerate(lines, 1):
        col_idx = 0
        while col_idx < len(line):
            ch = line[col_idx]

            # Handle comments (outside strings)
            if not in_string and ch == "#":
                break # Comment extends to end of line

            # Handle strings
            if ch == '"' and not escape:
                in_string = not in_string
            elif ch == '\\' and in_string:
                escape = not escape
                col_idx += 1
                continue
            else:
                escape = False

            if not in_string:
                if ch == "{":
                    preview = line[:col_idx].strip()
                    stack.append((line_idx, col_idx + 1, preview))
                elif ch == "}":
                    if not stack:
                        return False, f"Unexpected closing brace '}}' at Line {line_idx}, Col {col_idx + 1} with no opening brace!"
                    stack.pop()

            col_idx += 1

    if stack:
        unclosed_line, unclosed_col, unclosed_preview = stack[-1]
        return False, f"Unclosed opening brace '{{' at Line {unclosed_line}, Col {unclosed_col} (near '{unclosed_preview}')! Total {len(stack)} unclosed braces at EOF."

    return True, "All braces perfectly balanced."

def main():
    parser = argparse.ArgumentParser(description="HOI4 Fast Brace Auditor")
    parser.add_argument("--path", required=True, help="File or directory to audit")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"Error: Path '{target}' does not exist.")
        sys.exit(1)

    files = [target] if target.is_file() else [f for f in target.rglob("*.txt") if "localisation" not in str(f)]
    
    start_time = time.time()
    errors = []

    print(f"Auditing brace syntax across {len(files)} files...")
    for f in files:
        ok, msg = audit_file_braces(f)
        if not ok:
            errors.append(f"{f}: {msg}")

    elapsed = (time.time() - start_time) * 1000.0

    if errors:
        print(f"\n--- FAILED ({len(errors)} errors found in {elapsed:.1f}ms) ---")
        for err in errors:
            print(f"  [FAIL] {err}")
        sys.exit(1)
    else:
        print(f"\n--- PASSED: All {len(files)} files audited with 100% balanced braces in {elapsed:.1f}ms ---")
        sys.exit(0)

if __name__ == "__main__":
    main()
