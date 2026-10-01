import re
import os

with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# find each focus id and its icon
foci_icons = re.findall(r'id\s*=\s*(\w+).*?icon\s*=\s*(\w+)', text, re.DOTALL)
print(f"Total focus-icon pairs: {len(foci_icons)}")

gfx_path = 'interface/ww1_germany_goals.gfx'
sprite_map = {}
if os.path.exists(gfx_path):
    with open(gfx_path, 'r', encoding='utf-8', errors='ignore') as gf:
        gtext = gf.read()
        for m in re.finditer(r'name\s*=\s*["\']([^"\']+)["\'].*?texturefile\s*=\s*["\']([^"\']+)["\']', gtext, re.DOTALL):
            sprite_map[m.group(1)] = m.group(2)

print(f"Mapped {len(sprite_map)} sprites in ww1_germany_goals.gfx")

out_of_place = []
keywords = ['nazi', 'swastika', 'hitler', 'himmler', 'goring', 'ss_', 'fascist', 'prc', 'chi', 'soviet', 'jet', 'modern', 't_34', 'panther', 'tiger', 'generic_radar', 'generic_oil_refinery']

for fid, ic in foci_icons:
    tex = sprite_map.get(ic, 'BASE_GAME_OR_OTHER')
    combined = (fid + ' ' + ic + ' ' + tex).lower()
    if any(k in combined for k in keywords):
        out_of_place.append((fid, ic, tex))

print(f"\nOut of place icons ({len(out_of_place)}):")
for item in out_of_place:
    print(f"  Focus: {item[0]:45s} | Icon: {item[1]:40s} | Tex: {item[2]}")

print("\nAll unique icons used across tree:")
all_unique = sorted(list(set(ic for _, ic in foci_icons)))
for ic in all_unique:
    tex = sprite_map.get(ic, 'NOT_IN_CUSTOM_GFX')
    print(f"  {ic:45s} -> {tex}")
