import os, re, glob
repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

# Parse all spriteType definitions in interface/*.gfx
sprites = {}
for gf in glob.glob(os.path.join(repo, "interface", "*.gfx")):
    with open(gf, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    txt = re.sub(r'#.*$', '', txt, flags=re.MULTILINE)
    for m in re.finditer(r'name\s*=\s*["\']([^"\']+)["\'].*?texturefile\s*=\s*["\']([^"\']+)["\']', txt, re.DOTALL | re.IGNORECASE):
        sprites[m.group(1)] = m.group(2)

print(f"Total sprites registered: {len(sprites)}")

chars_files = ["SOV.txt", "WHT.txt"]
missing_sprites = []
missing_files = []

for cf in chars_files:
    p = os.path.join(repo, "common", "characters", cf)
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    txt = re.sub(r'#.*$', '', txt, flags=re.MULTILINE)
    portraits = re.findall(r'(?:large|small)\s*=\s*"([^"]+)"', txt)
    for port in set(portraits):
        if port.startswith("GFX_"):
            if port not in sprites:
                missing_sprites.append((cf, port))
            else:
                tex = sprites[port]
                full = os.path.normpath(os.path.join(repo, tex.replace("/", os.sep).replace("\\", os.sep)))
                if not os.path.exists(full):
                    missing_files.append((cf, port, tex))
        else:
            full = os.path.normpath(os.path.join(repo, port.replace("/", os.sep).replace("\\", os.sep)))
            if not os.path.exists(full):
                missing_files.append((cf, port, port))

if missing_sprites:
    print(f"Missing Sprites in .gfx ({len(missing_sprites)}):")
    for cf, port in missing_sprites:
        print(f"  [{cf}] {port}")
else:
    print("All character GFX_ sprites are registered in .gfx!")

if missing_files:
    print(f"Missing Textures on disk ({len(missing_files)}):")
    for cf, port, tex in missing_files:
        print(f"  [{cf}] {port} -> {tex}")
else:
    print("All character textures exist 100% on disk!")
