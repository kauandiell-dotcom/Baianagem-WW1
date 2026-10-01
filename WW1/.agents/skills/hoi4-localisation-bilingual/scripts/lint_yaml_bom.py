#!/usr/bin/env python3
"""
HOI4 Localisation & UTF-8 BOM Linter
Verifies UTF-8 BOM encoding, Paradox YAML syntax, absence of smart quotes/Lua comments,
and cross-language key parity between English and Brazilian Portuguese.
"""

import sys
import re
import argparse
from pathlib import Path

UTF8_BOM = b'\xef\xbb\xbf'
SMART_QUOTES = ["“", "”", "‘", "’"]

def check_file(file_path, auto_fix_bom=False):
    errors = []
    warnings = []

    # 1. Byte check for BOM
    with open(file_path, "rb") as f:
        header = f.read(3)
        if header != UTF8_BOM:
            if auto_fix_bom:
                with open(file_path, "rb") as f2:
                    rest = f2.read()
                with open(file_path, "wb") as f2:
                    f2.write(UTF8_BOM + rest)
                warnings.append("Missing UTF-8 BOM was automatically fixed.")
            else:
                errors.append("MISSING UTF-8 BOM: File does not start with '\\xef\\xbb\\xbf'. Clausewitz engine will corrupt accents.")

    # 2. Text checks
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        lines = f.readlines()

    keys = set()
    first_non_empty = None

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue

        if first_non_empty is None:
            first_non_empty = stripped
            if not (stripped.startswith("l_english:") or stripped.startswith("l_braz_por:") or stripped.startswith("l_")):
                errors.append(f"Line {idx}: First non-empty line must declare language (e.g., 'l_english:' or 'l_braz_por:'). Found: '{stripped}'")

        # Check for Lua comments
        if "--" in line and not stripped.startswith("#"):
            # Check if inside quotes or comment
            parts = line.split('"')
            if len(parts) % 2 == 1: # Outside quotes
                for i in range(0, len(parts), 2):
                    if "--" in parts[i]:
                        errors.append(f"Line {idx}: Lua comment syntax '--' detected! Only '#' is allowed in Clausewitz YAML.")
                        break

        # Check for smart quotes
        for sq in SMART_QUOTES:
            if sq in line:
                errors.append(f"Line {idx}: Smart/curly quote '{sq}' detected! Use standard ASCII '\"' (U+0022).")

        # Key parsing: KEY:0 "val"
        m = re.match(r'^\s*([a-zA-Z0-9_.]+):(?:\d+)?\s*"(.*)"\s*$', line)
        if m:
            keys.add(m.group(1))

    return keys, errors, warnings

def main():
    parser = argparse.ArgumentParser(description="HOI4 Localisation Linter")
    parser.add_argument("--loc", required=True, help="Path to localisation directory")
    parser.add_argument("--fix-bom", action="store_true", help="Automatically inject missing UTF-8 BOM")
    args = parser.parse_args()

    loc_dir = Path(args.loc)
    if not loc_dir.exists():
        print(f"Error: Path '{loc_dir}' does not exist.")
        sys.exit(1)

    yml_files = list(loc_dir.rglob("*.yml"))
    print(f"Auditing {len(yml_files)} localisation (.yml) files...")

    total_errors = 0
    total_warnings = 0
    lang_keys = {} # lang -> dict of file -> keys

    for f in yml_files:
        keys, errors, warnings = check_file(f, auto_fix_bom=args.fix_bom)
        rel_str = str(f.relative_to(loc_dir))
        lang = "braz_por" if "braz_por" in rel_str else ("english" if "english" in rel_str else "other")
        
        if lang not in lang_keys:
            lang_keys[lang] = {}
        lang_keys[lang][f.name] = keys

        if errors or warnings:
            print(f"\nFile: {f.name} ({rel_str})")
            for w in warnings:
                print(f"  [WARN] {w}")
                total_warnings += 1
            for e in errors:
                print(f"  [FAIL] {e}")
                total_errors += 1

    # Cross-language key parity check
    if "english" in lang_keys and "braz_por" in lang_keys:
        eng_total = set().union(*lang_keys["english"].values()) if lang_keys["english"] else set()
        por_total = set().union(*lang_keys["braz_por"].values()) if lang_keys["braz_por"] else set()

        missing_in_por = eng_total - por_total
        missing_in_eng = por_total - eng_total

        if missing_in_por:
            print(f"\n[KEY PARITY] {len(missing_in_por)} keys present in English but missing in Brazilian Portuguese:")
            for k in sorted(list(missing_in_por))[:10]:
                print(f"  - {k}")
            if len(missing_in_por) > 10:
                print(f"  ... and {len(missing_in_por) - 10} more.")

        if missing_in_eng:
            print(f"\n[KEY PARITY] {len(missing_in_eng)} keys present in Brazilian Portuguese but missing in English:")
            for k in sorted(list(missing_in_eng))[:10]:
                print(f"  - {k}")
            if len(missing_in_eng) > 10:
                print(f"  ... and {len(missing_in_eng) - 10} more.")

    print(f"\n--- AUDIT COMPLETE: {len(yml_files)} files checked, {total_errors} errors, {total_warnings} warnings ---")
    if total_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
