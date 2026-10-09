# -*- coding: utf-8 -*-
from pathlib import Path
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

# 1. Map all sprite names to their texture files across all .gfx files
sprite_to_tex = {}
for p in sorted((ROOT / "interface").glob("*.gfx")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"[^}]*?texturefile\s*=\s*"([^"]+)"', txt, re.DOTALL):
        name = m.group(1)
        tex = m.group(2)
        sprite_to_tex[name] = tex

print(f"Total sprites registered in interface/*.gfx: {len(sprite_to_tex)}")

# 2. Check all active (uncommented) characters' small portraits
bad_characters = []
total_active = 0
for p in sorted((ROOT / "common/characters").glob("*.txt")):
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    for line_idx, line in enumerate(lines, 1):
        clean = line.strip()
        if clean.startswith("#"):
            continue
        clean = re.sub(r'#.*', '', clean)
        m = re.search(r'small\s*=\s*(?:"([^"]+)"|([a-zA-Z0-9_./\\-]+))', clean)
        if not m:
            continue
        total_active += 1
        small_val = m.group(1) or m.group(2)
        
        # small_val can be a sprite name or a direct path
        tex_path = None
        if small_val in sprite_to_tex:
            tex_path = sprite_to_tex[small_val]
        elif (ROOT / small_val).exists():
            tex_path = small_val
        elif (ROOT / f"gfx/interface/ideas/{small_val}.dds").exists():
            tex_path = f"gfx/interface/ideas/{small_val}.dds"
        elif (ROOT / f"gfx/interface/ideas/{small_val}.png").exists():
            tex_path = f"gfx/interface/ideas/{small_val}.png"
            
        if not tex_path:
            bad_characters.append((p.name, line_idx, small_val, "MISSING_TEXTURE", "N/A"))
            continue
            
        fp = ROOT / tex_path
        if not fp.exists():
            bad_characters.append((p.name, line_idx, small_val, f"FILE_NOT_FOUND: {tex_path}", "N/A"))
            continue
            
        try:
            im = Image.open(fp)
            w, h = im.size
            if w > 82 or h > 90:
                bad_characters.append((p.name, line_idx, small_val, tex_path, f"{w}x{h}"))
        except Exception as e:
            bad_characters.append((p.name, line_idx, small_val, f"ERROR: {e}", "N/A"))

print(f"Total active small portrait entries scanned: {total_active}")
print(f"Active characters with BAD or LARGE small portraits: {len(bad_characters)}")
for item in bad_characters:
    print(f"[{item[0]}:{item[1]}] {item[2]} -> {item[3]} ({item[4]})")
