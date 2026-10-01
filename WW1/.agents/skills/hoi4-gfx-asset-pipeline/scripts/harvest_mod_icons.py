#!/usr/bin/env python3
"""
HOI4 Mod Icon Harvester & GFX Generator
Searches donor mod folders (Europe In Flames, TGWR), copies matching texture files,
and appends base + shine SpriteType blocks into a target .gfx file.
"""

import sys
import shutil
import argparse
from pathlib import Path

SHINE_TEMPLATE = """
    SpriteType = {{
        name = "{sprite_name}"
        texturefile = "{rel_path}"
    }}
    SpriteType = {{
        name = "{sprite_name}_shine"
        texturefile = "{rel_path}"
        effectFile = "gfx/FX/buttonstate.lua"
        animation = {{
            animationmaskfile = "{rel_path}"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = -90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }}
        }}
        legacy_lazy_load = no
    }}
"""

def harvest_icons(donor_dir, dest_dir, query, tag_prefix, gfx_file):
    donor_path = Path(donor_dir)
    dest_path = Path(dest_dir)
    dest_path.mkdir(parents=True, exist_ok=True)
    gfx_path = Path(gfx_file)

    matches = []
    query_lower = query.lower()
    for f in donor_path.rglob("*"):
        if f.is_file() and f.suffix.lower() in [".dds", ".png", ".tga"]:
            if query_lower in f.stem.lower():
                matches.append(f)

    print(f"Found {len(matches)} files matching query '{query}' in {donor_path}.")
    if not matches:
        return

    gfx_entries = []
    for src in matches[:20]: # Limit batch to 20 to avoid flooding
        clean_stem = src.stem.replace(" ", "_")
        target_name = f"{tag_prefix}_{clean_stem}{src.suffix.lower()}"
        target_file = dest_path / target_name
        
        # Copy file if not exists
        if not target_file.exists():
            shutil.copy2(src, target_file)
            print(f"  [COPIED] {src.name} -> {target_file.name}")
        else:
            print(f"  [EXISTS] {target_file.name}")

        sprite_name = f"GFX_{tag_prefix}_{clean_stem}"
        rel_path = f"gfx/interface/goals/{target_name}"
        gfx_entries.append(SHINE_TEMPLATE.format(sprite_name=sprite_name, rel_path=rel_path))

    # Append to .gfx file
    if gfx_path.exists():
        with open(gfx_path, "r", encoding="utf-8-sig", errors="replace") as f:
            existing_gfx = f.read()

        # Insert before closing brace if present
        if existing_gfx.strip().endswith("}"):
            idx = existing_gfx.rfind("}")
            updated_gfx = existing_gfx[:idx] + "\n".join(gfx_entries) + "\n}\n"
        else:
            updated_gfx = existing_gfx + "\n".join(gfx_entries)
    else:
        gfx_path.parent.mkdir(parents=True, exist_ok=True)
        updated_gfx = "spriteTypes = {\n" + "\n".join(gfx_entries) + "\n}\n"

    with open(gfx_path, "w", encoding="utf-8") as f:
        f.write(updated_gfx)
    print(f"\nSuccessfully registered {len(gfx_entries)} sprites in {gfx_path}.")

def main():
    parser = argparse.ArgumentParser(description="HOI4 Icon Harvester")
    parser.add_argument("--donor", required=True, help="Donor mod directory to search")
    parser.add_argument("--dest", required=True, help="Destination directory (e.g. WW1/gfx/interface/goals/)")
    parser.add_argument("--query", required=True, help="Keyword query (e.g. artillery, dreadnought, trench)")
    parser.add_argument("--tag", default="WW1", help="Prefix tag for sprite and filename")
    parser.add_argument("--gfx", required=True, help="Target .gfx file to update")
    args = parser.parse_args()

    harvest_icons(args.donor, args.dest, args.query, args.tag, args.gfx)

if __name__ == "__main__":
    main()
