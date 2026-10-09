# -*- coding: utf-8 -*-
from pathlib import Path
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

large = []
missing = []

for p in sorted((ROOT / "interface").glob("*.gfx")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    # match spriteType blocks with name = "GFX_idea_..."
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"[^}]*?texturefile\s*=\s*"([^"]+)"', txt, re.DOTALL):
        name = m.group(1)
        tex = m.group(2)
        if not name.startswith("GFX_idea_"):
            continue
        fp = ROOT / tex
        if not fp.exists():
            missing.append((p.name, name, tex))
            continue
        try:
            im = Image.open(fp)
            w, h = im.size
            if w > 82 or h > 90:
                large.append((p.name, name, tex, f"{w}x{h}"))
        except Exception as e:
            pass

print(f"Total GFX_idea with large dimensions across ALL interface/*.gfx: {len(large)}")
for item in large:
    print(f"[{item[0]}] {item[1]} -> {item[2]} ({item[3]})")

print(f"\nMissing files for GFX_idea: {len(missing)}")
for item in missing[:20]:
    print(f"[{item[0]}] {item[1]} -> {item[2]}")
