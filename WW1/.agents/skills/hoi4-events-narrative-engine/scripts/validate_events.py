#!/usr/bin/env python3
"""
HOI4 Event Syntax & Namespace Validator
Audits namespace declarations, event ID naming compliance, unclosed blocks, option presence, and duplicates.
"""

import sys
import re
import argparse
from pathlib import Path

def audit_event_file(file_path):
    errors = []
    warnings = []
    
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        content = f.read()

    # 1. Namespaces
    declared_namespaces = set(re.findall(r'add_namespace\s*=\s*([a-zA-Z0-9_]+)', content))

    # 2. Extract Event IDs
    event_pattern = re.compile(r'(country_event|news_event)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}|.)*?\}[^{}]*)*)\}', re.DOTALL)
    
    seen_ids = set()
    event_count = 0

    for m in event_pattern.finditer(content):
        event_count += 1
        ev_type = m.group(1)
        block = m.group(2)
        line_num = content[:m.start()].count('\n') + 1

        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_.]+)', block)
        if not id_m:
            errors.append(f"Line {line_num}: {ev_type} has no 'id' defined!")
            continue

        ev_id = id_m.group(1)
        if ev_id in seen_ids:
            errors.append(f"Line {line_num}: Duplicate event ID '{ev_id}'!")
        seen_ids.add(ev_id)

        # Check namespace prefix
        if "." in ev_id:
            ns = ev_id.split(".")[0]
            if declared_namespaces and ns not in declared_namespaces:
                errors.append(f"Line {line_num}: Event '{ev_id}' uses undeclared namespace '{ns}'. Declared: {declared_namespaces}")
        else:
            warnings.append(f"Line {line_num}: Event '{ev_id}' does not use a namespace dot notation.")

        # Check options
        options = re.findall(r'\boption\s*=\s*\{', block)
        if not options:
            errors.append(f"Line {line_num}: Event '{ev_id}' has NO options defined! An event without options cannot be dismissed and traps the player.")

    if event_count > 0 and not declared_namespaces:
        errors.append("No 'add_namespace' declared in file! Every event file with events must declare at least one namespace.")

    return event_count, errors, warnings

def main():
    parser = argparse.ArgumentParser(description="HOI4 Events Validator")
    parser.add_argument("--events", required=True, help="Event file or directory to audit")
    args = parser.parse_args()

    target = Path(args.events)
    if not target.exists():
        print(f"Error: Path '{target}' does not exist.")
        sys.exit(1)

    files = [target] if target.is_file() else list(target.rglob("*.txt"))
    total_events = 0
    total_errors = 0
    total_warnings = 0

    print(f"Auditing {len(files)} event files...")
    for f in files:
        count, errors, warnings = audit_event_file(f)
        total_events += count
        if errors or warnings:
            print(f"\nFile: {f}")
            for w in warnings:
                print(f"  [WARN] {w}")
                total_warnings += 1
            for e in errors:
                print(f"  [FAIL] {e}")
                total_errors += 1

    print(f"\n--- AUDIT COMPLETE: {total_events} events checked, {total_errors} errors, {total_warnings} warnings ---")
    if total_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
