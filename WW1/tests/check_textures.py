import glob, re, os

# Collect all sprite definitions from all .gfx files
sprite_to_file = {}
for f in glob.glob('interface/*.gfx'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        matches = re.findall(r'name\s*=\s*"([^"]+)"[\s\S]*?texturefile\s*=\s*"([^"]+)"', content)
        for name, tex in matches:
            sprite_to_file[name] = tex

print(f'Total SpriteTypes indexed in interface/*.gfx: {len(sprite_to_file)}')

with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
    focus_text = f.read()

focus_icons = set(re.findall(r'icon\s*=\s*([A-Za-z0-9_]+)', focus_text))
print(f'Total unique icons in germany.txt: {len(focus_icons)}')

missing_sprites = [icon for icon in focus_icons if icon not in sprite_to_file]
print(f'Icons missing SpriteType definition: {len(missing_sprites)} {missing_sprites}')

# Check if texture files exist on disk
missing_texture_files = []
for icon in focus_icons:
    if icon in sprite_to_file:
        tex_path = sprite_to_file[icon].replace('/', os.sep).replace('\\\\', os.sep)
        # Texture path is relative to mod root
        if not os.path.exists(tex_path):
            missing_texture_files.append((icon, tex_path))

print(f'Icons with missing texture files on disk: {len(missing_texture_files)}')
if missing_texture_files:
    for m in missing_texture_files:
        print('  Missing:', m)
