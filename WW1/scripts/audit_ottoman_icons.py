# -*- coding: utf-8 -*-
from pathlib import Path
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]

# 1. Load existing goal sprites across all interface/*.gfx
goal_sprites = {}
for p in sorted((ROOT / "interface").glob("*.gfx")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"[^}]*?texturefile\s*=\s*"([^"]+)"', txt, re.DOTALL):
        name = m.group(1)
        tex = m.group(2)
        if "goal" in tex.lower() or "focus" in name.lower() or "goal" in name.lower():
            goal_sprites[name] = tex

print(f"Total registered goal sprites: {len(goal_sprites)}")

# 2. Parse Turkey focus tree
tur_txt = (ROOT / "common/national_focus/turkey.txt").read_text(encoding="utf-8")
focuses = []
for m in re.finditer(r'focus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)[\s\S]*?icon\s*=\s*([a-zA-Z0-9_]+)[\s\S]*?x\s*=\s*(\d+)[\s\S]*?y\s*=\s*(\d+)', tur_txt):
    fid = m.group(1)
    icon = m.group(2)
    x = int(m.group(3))
    y = int(m.group(4))
    focuses.append({'id': fid, 'icon': icon, 'x': x, 'y': y})

print(f"Parsed {len(focuses)} focuses in Turkey focus tree.")
icon_counts = Counter(f['icon'] for f in focuses)
print("Icons used more than 3 times:")
for ic, cnt in icon_counts.most_common():
    if cnt > 3:
        print(f"  {ic}: {cnt}")
