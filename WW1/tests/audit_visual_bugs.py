"""
Audit script for HoI4 German focus tree visual bugs:
- Backward edges (dy <= 0)
- Excessive vertical jumps (dy > 2)
- Cross-wing long horizontal lines (dx > 4)
- Missing spriteType definitions in interface/*.gfx
- Coordinate collisions
- Localization checks
"""
import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))
from tier3_graph import parse_focus_tree, MOD_ROOT

tree_path = os.path.join(MOD_ROOT, 'common', 'national_focus', 'germany.txt')
focuses = parse_focus_tree(tree_path)
print(f"=== FOCUS TREE AUDIT ===")
print(f"Total Focuses: {len(focuses)}")

# 1. Coordinate Collisions
coords = {}
collisions = []
for fid, f in focuses.items():
    pt = (f.x, f.y)
    if pt in coords:
        collisions.append((fid, coords[pt], pt))
    else:
        coords[pt] = fid

print(f"\n1. Coordinate Collisions: {len(collisions)}")
for c in collisions:
    print(f"   COLLISION: {c[0]} and {c[1]} at ({c[2][0]}, {c[2][1]})")

# 2. Prerequisite Edge Analysis
backward_edges = []
same_row_edges = []
excessive_vertical = []
cross_wing_edges = []

for fid, f in focuses.items():
    for or_group in f.prerequisites:
        for pid in or_group:
            if pid in focuses:
                p = focuses[pid]
                dy = f.y - p.y
                dx = abs(f.x - p.x)
                if dy < 0:
                    backward_edges.append((pid, fid, p.x, p.y, f.x, f.y, dy, dx))
                elif dy == 0:
                    same_row_edges.append((pid, fid, p.x, p.y, f.x, f.y, dy, dx))
                elif dy > 2:
                    excessive_vertical.append((pid, fid, p.x, p.y, f.x, f.y, dy, dx))
                
                if dx > 4:
                    cross_wing_edges.append((pid, fid, p.x, p.y, f.x, f.y, dy, dx))

print(f"\n2. Backward Edges (dy < 0) [CRITICAL VISUAL BUG: Arrow points UPWARDS]: {len(backward_edges)}")
for e in backward_edges:
    print(f"   BACKWARD: {e[0]} ({e[2]},{e[3]}) -> {e[1]} ({e[4]},{e[5]}) [dy={e[6]}, dx={e[7]}]")

print(f"\n3. Same-Row Edges (dy == 0) [CRITICAL VISUAL BUG: Horizontal line overlaps row]: {len(same_row_edges)}")
for e in same_row_edges:
    print(f"   SAME-ROW: {e[0]} ({e[2]},{e[3]}) -> {e[1]} ({e[4]},{e[5]}) [dy=0, dx={e[7]}]")

print(f"\n4. Long Vertical Jumps (dy > 2) [Clutters screen]: {len(excessive_vertical)}")
for e in excessive_vertical:
    print(f"   LONG VERTICAL: {e[0]} ({e[2]},{e[3]}) -> {e[1]} ({e[4]},{e[5]}) [dy={e[6]}, dx={e[7]}]")

print(f"\n5. Long Horizontal Jumps (dx > 4) [Spaghetti lines cutting across columns]: {len(cross_wing_edges)}")
for e in cross_wing_edges:
    print(f"   CROSS-WING: {e[0]} ({e[2]},{e[3]}) -> {e[1]} ({e[4]},{e[5]}) [dx={e[7]}, dy={e[6]}]")

# 6. Sprite / GFX Definition Audit
gfx_dir = os.path.join(MOD_ROOT, 'interface')
defined_sprites = set()
for fname in os.listdir(gfx_dir):
    if fname.endswith('.gfx'):
        fpath = os.path.join(gfx_dir, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as gf:
            content = gf.read()
            # find name = "..."
            for m in re.finditer(r'name\s*=\s*["\']([^"\']+)["\']', content):
                defined_sprites.add(m.group(1))

print(f"\n6. GFX Sprite Definitions found in interface/*.gfx: {len(defined_sprites)}")

missing_sprites = []
vanilla_fallbacks = [
    # Common vanilla sprites built into base game
    'GFX_goal_generic_scientific_exchange', 'GFX_goal_generic_production', 'GFX_goal_generic_intelligence_exchange',
    'GFX_goal_generic_propaganda', 'GFX_goal_generic_allies_build_infantry', 'GFX_goal_generic_army_motorized',
    'GFX_goal_generic_army_artillery', 'GFX_goal_generic_navy_cruiser', 'GFX_goal_generic_air_fighter',
    'GFX_goal_generic_air_bomber', 'GFX_goal_generic_radar', 'GFX_goal_generic_oil_refinery',
    'GFX_goal_generic_wolf_pack', 'GFX_goal_generic_trade', 'GFX_goal_generic_special_forces',
    'GFX_focus_generic_industry_1', 'GFX_focus_generic_industry_2', 'GFX_focus_generic_industry_3'
]

for fid, f in focuses.items():
    if f.icon and f.icon not in defined_sprites and f.icon not in vanilla_fallbacks:
        missing_sprites.append((fid, f.icon))

print(f"   Missing Custom Sprites: {len(missing_sprites)}")
for fid, icon in missing_sprites:
    print(f"     MISSING: {fid} -> {icon}")

# 7. Localization Audit
loc_dir = os.path.join(MOD_ROOT, 'localisation')
# check english and braz_por
for lang in ['english', 'braz_por']:
    loc_file = os.path.join(loc_dir, lang, f'ww1_germany_focus_l_{lang}.yml')
    if not os.path.exists(loc_file):
        print(f"\n7. Loc File MISSING: {loc_file}")
        continue
    with open(loc_file, 'r', encoding='utf-8', errors='ignore') as lf:
        loc_content = lf.read()
    
    missing_loc_names = []
    missing_loc_descs = []
    for fid in focuses:
        if f"{fid}:" not in loc_content:
            missing_loc_names.append(fid)
        if f"{fid}_desc:" not in loc_content:
            missing_loc_descs.append(fid)
    
    print(f"\n7. Localization [{lang}]: Missing Names: {len(missing_loc_names)}, Missing Descs: {len(missing_loc_descs)}")
    for m in missing_loc_names[:5]:
        print(f"   Missing name: {m}")
