import os, re, glob

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

sprite_textures = {}
for gfx_file in glob.glob(os.path.join(repo, "interface", "*.gfx")):
    with open(gfx_file, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    txt = re.sub(r'#.*$', '', txt, flags=re.MULTILINE)
    for m in re.finditer(r'name\s*=\s*["\']([^"\']+)["\'].*?texturefile\s*=\s*["\']([^"\']+)["\']', txt, re.DOTALL | re.IGNORECASE):
        sprite_textures[m.group(1)] = m.group(2)

print(f"Total sprites registered in .gfx: {len(sprite_textures)}")

trees = ["soviet.txt", "soviet_russia.txt", "white_russia.txt"]
missing_sprites = []
missing_textures = []

for t in trees:
    p = os.path.join(repo, "common", "national_focus", t)
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    icons = re.findall(r'icon\s*=\s*([A-Za-z0-9_]+)', txt)
    for ic in set(icons):
        if ic not in sprite_textures:
            missing_sprites.append((t, ic))
        else:
            tex = sprite_textures[ic]
            tex_clean = tex.replace("/", os.sep).replace("\\", os.sep)
            full_path = os.path.normpath(os.path.join(repo, tex_clean))
            if not os.path.exists(full_path):
                missing_textures.append((t, ic, tex))

if missing_sprites:
    print(f"[MISSING SPRITES IN .GFX] ({len(missing_sprites)}):")
    for t, ic in sorted(missing_sprites):
        print(f"  {t}: {ic}")
else:
    print("Sprites in .gfx: 100% COVERAGE")

if missing_textures:
    print(f"[MISSING TEXTURES ON DISK] ({len(missing_textures)}):")
    for t, ic, tex in sorted(missing_textures):
        print(f"  {t}: {ic} -> {tex}")
else:
    print("Textures on disk: 100% EXIST")
