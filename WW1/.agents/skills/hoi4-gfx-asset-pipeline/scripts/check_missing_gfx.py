#!/usr/bin/env python3
"""
HOI4 Missing GFX & Texture Checker
Verifies that all focus icons in a focus tree have registered SpriteType entries,
valid physical texture files on disk, and proper _shine animation blocks.
"""

import sys
import re
import argparse
from pathlib import Path

def parse_tree_icons(tree_path):
    with open(tree_path, "r", encoding="utf-8-sig", errors="replace") as f:
        content = f.read()
    icons = set(re.findall(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', content))
    return icons

def parse_gfx_files(gfx_paths):
    sprites = {} # sprite_name -> texture_rel_path
    shines = set()

    sprite_pattern = re.compile(r'SpriteType\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}|.)*?\}[^{}]*)*)\}', re.DOTALL)

    for p in gfx_paths:
        with open(p, "r", encoding="utf-8-sig", errors="replace") as f:
            text = f.read()

        for m in sprite_pattern.finditer(text):
            block = m.group(1)
            name_m = re.search(r'\bname\s*=\s*"([^"]+)"', block)
            tex_m = re.search(r'\btexturefile\s*=\s*"([^"]+)"', block)
            if name_m:
                sname = name_m.group(1)
                if sname.endswith("_shine"):
                    shines.add(sname)
                elif tex_m:
                    sprites[sname] = tex_m.group(1)

    return sprites, shines

def main():
    parser = argparse.ArgumentParser(description="HOI4 GFX & Texture Auditor")
    parser.add_argument("--tree", required=True, help="Path to focus tree .txt")
    parser.add_argument("--gfx", required=True, nargs="+", help="Path to one or more .gfx files")
    parser.add_argument("--mod-root", required=True, help="Path to mod root directory (contains gfx/)")
    args = parser.parse_args()

    tree_path = Path(args.tree)
    gfx_paths = [Path(p) for p in args.gfx]
    mod_root = Path(args.mod_root)

    print(f"Auditing GFX for tree: {tree_path}...")
    icons = parse_tree_icons(tree_path)
    print(f"Found {len(icons)} unique focus icon references in tree.")

    sprites, shines = parse_gfx_files(gfx_paths)
    print(f"Loaded {len(sprites)} base sprites and {len(shines)} shine definitions from .gfx files.")

    errors = []
    warnings = []

    for icon in sorted(icons):
        if icon not in sprites:
            errors.append(f"UNREGISTERED SPRITE: Icon '{icon}' referenced in tree is NOT defined in any provided .gfx file!")
            continue

        tex_rel = sprites[icon]
        physical_path = mod_root / tex_rel
        if not physical_path.exists():
            errors.append(f"MISSING TEXTURE FILE: Sprite '{icon}' points to '{tex_rel}', but file does not exist on disk at '{physical_path}'!")

        shine_name = f"{icon}_shine"
        if shine_name not in shines:
            warnings.append(f"MISSING SHINE SPRITE: Base sprite '{icon}' exists, but '{shine_name}' is missing in .gfx. Engine error.log will trigger on mouseover.")

    if warnings:
        print(f"\n--- WARNINGS ({len(warnings)}) ---")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print(f"\n--- ERRORS ({len(errors)}) ---")
        for e in errors:
            print(f"  [FAIL] {e}")
        print(f"\nAudit FAILED: {len(errors)} critical texture errors found.")
        sys.exit(1)
    else:
        print(f"\nAudit PASSED: All {len(icons)} focus icons properly registered and verified on disk.")
        sys.exit(0)

if __name__ == "__main__":
    main()
