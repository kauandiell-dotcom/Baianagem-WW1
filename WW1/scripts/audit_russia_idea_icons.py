import os, re, glob

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

sprite_textures = {}
for gfx_file in glob.glob(os.path.join(repo, "interface", "*.gfx")):
    with open(gfx_file, "r", encoding="utf-8", errors="ignore") as f:
        txt = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    for m in re.finditer(r'name\s*=\s*["\']([^"\']+)["\'].*?texturefile\s*=\s*["\']([^"\']+)["\']', txt, re.DOTALL | re.IGNORECASE):
        sprite_textures[m.group(1)] = m.group(2)

print(f"Total sprites registered: {len(sprite_textures)}")

idea_files = [
    "ww1_russia_ideas.txt",
    "ww1_ger_rus_rework_ideas.txt",
    "side_ww1_ger_rus_depth.txt"
]

missing_sprites = []
missing_textures = []

for f in idea_files:
    p = os.path.join(repo, "common", "ideas", f)
    if not os.path.exists(p): continue
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
    txt = re.sub(r'#.*$', '', txt, flags=re.MULTILINE)
    
    # find picture = ...
    pics = re.findall(r'picture\s*=\s*([A-Za-z0-9_]+)', txt)
    for pic in set(pics):
        # In HOI4, picture = X can map to GFX_idea_X or X
        sprite_cand = f"GFX_idea_{pic}" if f"GFX_idea_{pic}" in sprite_textures else pic
        if sprite_cand not in sprite_textures:
            # Maybe the file exists directly in gfx/interface/ideas/
            direct_cand = os.path.join(repo, "gfx", "interface", "ideas", f"{pic}.dds")
            if not os.path.exists(direct_cand):
                missing_sprites.append((f, pic))
        else:
            tex = sprite_textures[sprite_cand]
            tex_clean = tex.replace("/", os.sep).replace("\\", os.sep)
            full_path = os.path.normpath(os.path.join(repo, tex_clean))
            if not os.path.exists(full_path):
                missing_textures.append((f, pic, tex))

if missing_sprites:
    print(f"Missing Idea Sprites ({len(missing_sprites)}):")
    for f, pic in sorted(missing_sprites):
        print(f"  [{f}] {pic}")
else:
    print("All Russian idea sprites: 100% REGISTERED!")

if missing_textures:
    print(f"Missing Idea Textures on disk ({len(missing_textures)}):")
    for f, pic, tex in sorted(missing_textures):
        print(f"  [{f}] {pic} -> {tex}")
else:
    print("All Russian idea textures: 100% EXIST ON DISK!")
