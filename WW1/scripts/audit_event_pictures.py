import glob
import re
import os

# Collect all spriteTypes and their texturefile paths from interface/*.gfx
declared_sprites = {}
for fpath in glob.glob('interface/*.gfx'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    # match spriteType = { name = "..." texturefile = "..." }
    for m in re.finditer(r'spriteType\s*=\s*\{[^}]*name\s*=\s*"([^"]+)"[^}]*texturefile\s*=\s*"([^"]+)"', c):
        declared_sprites[m.group(1)] = m.group(2)

print(f"Total declared spriteTypes in interface/*.gfx: {len(declared_sprites)}")

# Check events/*.txt
missing_event_sprites = {}
missing_files = {}

for fpath in glob.glob('events/*.txt'):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    pics = re.findall(r'picture\s*=\s*([a-zA-Z0-9_]+)', c)
    for p in pics:
        if p not in declared_sprites:
            missing_event_sprites.setdefault(fname, set()).add(p)
        else:
            tex = declared_sprites[p]
            # normalize path
            tex_clean = tex.replace('\\', '/')
            if tex_clean.startswith('/'):
                tex_clean = tex_clean[1:]
            if not os.path.isfile(tex_clean):
                missing_files.setdefault(fname, set()).add((p, tex_clean))

print(f"\nMissing Sprite Declarations in interface/*.gfx:")
if not missing_event_sprites:
    print("  None! (0 missing)")
for fname, mis in missing_event_sprites.items():
    print(f"  {fname}: {len(mis)} missing: {mis}")

print(f"\nMissing Texture Files on Disk:")
if not missing_files:
    print("  None! (0 missing)")
for fname, mis in missing_files.items():
    print(f"  {fname}: {len(mis)} missing files:")
    for p, tex in mis:
        print(f"     {p} -> {tex}")
