#!/usr/bin/env python3
"""
HOI4 Focus Tree Spatial & Structural Layout Validator
Audits coordinates, edge directions (dy >= 1), collision overlaps, mutual exclusivity symmetry, and DAG cycles.
"""

import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

def parse_focus_tree(file_path):
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        content = f.read()

    foci = {}
    focus_pattern = re.compile(r'\bfocus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}|.)*?\}[^{}]*)*)\}', re.DOTALL)
    
    # Simple line index tracker for line numbers
    lines = content.splitlines()

    for m in focus_pattern.finditer(content):
        block = m.group(1)
        
        # Line number
        line_num = content[:m.start()].count('\n') + 1

        # ID
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_m:
            continue
        fid = id_m.group(1)

        # X, Y
        x_m = re.search(r'\bx\s*=\s*(-?\d+)', block)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', block)
        x = int(x_m.group(1)) if x_m else None
        y = int(y_m.group(1)) if y_m else None

        # Prerequisites
        prereqs = []
        for p_match in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', block):
            inner = p_match.group(1)
            for p_id in re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', inner):
                prereqs.append(p_id)

        # Mutually exclusive
        mut_ex = []
        for m_match in re.finditer(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block):
            inner = m_match.group(1)
            for m_id in re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', inner):
                mut_ex.append(m_id)

        has_allow_branch = "allow_branch" in block

        foci[fid] = {
            "id": fid,
            "line": line_num,
            "x": x,
            "y": y,
            "prerequisites": prereqs,
            "mutually_exclusive": mut_ex,
            "has_allow_branch": has_allow_branch
        }

    return foci

def audit_tree(foci):
    errors = []
    warnings = []

    # 1. Coordinate Collisions
    coord_map = defaultdict(list)
    for fid, data in foci.items():
        if data["x"] is not None and data["y"] is not None:
            coord_map[(data["x"], data["y"])].append(fid)

    for (x, y), ids in coord_map.items():
        if len(ids) > 1:
            errors.append(f"COORDINATE COLLISION at (x={x}, y={y}): Foci {ids} share the exact same spot!")

    # 2. Prerequisites & Edge Directions
    for fid, data in foci.items():
        cx, cy = data["x"], data["y"]
        for p in data["prerequisites"]:
            if p not in foci:
                errors.append(f"MISSING PREREQUISITE: Focus '{fid}' (line {data['line']}) depends on non-existent '{p}'.")
                continue
            
            p_data = foci[p]
            px, py = p_data["x"], p_data["y"]
            if cy is not None and py is not None:
                dy = cy - py
                dx = abs(cx - px) if (cx is not None and px is not None) else 0

                if dy < 0:
                    errors.append(f"BACKWARD EDGE: Focus '{fid}' (y={cy}) is ABOVE parent '{p}' (y={py}). dy={dy} < 0! Engine arrow points backward.")
                elif dy == 0:
                    errors.append(f"SAME-ROW EDGE: Focus '{fid}' and parent '{p}' share row y={cy}. dy=0 renders a line through same-row focus boxes.")
                elif dy > 2:
                    warnings.append(f"LONG VERTICAL JUMP: Focus '{fid}' is dy={dy} rows below parent '{p}'. Consider intermediate node or tightening.")

                if dx > 4:
                    warnings.append(f"WIDE HORIZONTAL SPAN: Focus '{fid}' (x={cx}) is dx={dx} columns apart from parent '{p}' (x={px}).")

    # 3. Mutual Exclusivity Symmetry
    for fid, data in foci.items():
        for mex in data["mutually_exclusive"]:
            if mex not in foci:
                errors.append(f"MISSING MUTUALLY_EXCLUSIVE TARGET: Focus '{fid}' excludes non-existent '{mex}'.")
            else:
                other_mex = foci[mex]["mutually_exclusive"]
                if fid not in other_mex:
                    warnings.append(f"ASYMMETRIC EXCLUSIVITY: Focus '{fid}' excludes '{mex}', but '{mex}' does not list '{fid}' in mutually_exclusive.")

    # 4. Cycle Detection (Tarjan's DFS)
    visited = {}
    recursion_stack = {}

    def is_cyclic(u):
        visited[u] = True
        recursion_stack[u] = True
        for neighbor in foci[u]["prerequisites"]:
            if neighbor not in foci:
                continue
            if not visited.get(neighbor, False):
                if is_cyclic(neighbor):
                    return True
            elif recursion_stack.get(neighbor, False):
                return True
        recursion_stack[u] = False
        return False

    for node in foci:
        if not visited.get(node, False):
            if is_cyclic(node):
                errors.append(f"CYCLIC DEPENDENCY DETECTED: Focus graph contains a cycle involving '{node}'!")
                break

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description="HOI4 Focus Tree Validator")
    parser.add_argument("--tree", required=True, help="Path to focus tree file (.txt)")
    args = parser.parse_args()

    tree_path = Path(args.tree)
    if not tree_path.exists():
        print(f"Error: File '{tree_path}' does not exist.")
        sys.exit(1)

    print(f"Auditing focus tree: {tree_path}...")
    foci = parse_focus_tree(tree_path)
    print(f"Parsed {len(foci)} total focus definitions.")

    errors, warnings = audit_tree(foci)

    if warnings:
        print(f"\n--- WARNINGS ({len(warnings)}) ---")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print(f"\n--- ERRORS ({len(errors)}) ---")
        for e in errors:
            print(f"  [FAIL] {e}")
        print(f"\nAudit FAILED: {len(errors)} critical issues found.")
        sys.exit(1)
    else:
        print(f"\nAudit PASSED: 0 errors found across {len(foci)} foci.")
        sys.exit(0)

if __name__ == "__main__":
    main()
