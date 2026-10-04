import re
import glob

with open('common/national_focus/soviet.txt', 'r', encoding='utf-8') as f:
    soviet_text = f.read()
    soviet_focuses = re.findall(r'icon\s*=\s*([^\s]+)', soviet_text)

print(f'Total icon references in soviet.txt: {len(soviet_focuses)}')

gfx_sprites = {}
for g in glob.glob('interface/*.gfx'):
    with open(g, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    matches = re.findall(r'SpriteType\s*=\s*\{\s*name\s*=\s*["\']([^"\']+)["\']\s*texturefile\s*=\s*["\']([^"\']+)["\']', text, re.IGNORECASE)
    for name, tex in matches:
        gfx_sprites[name] = tex

print(f'Total sprite definitions loaded: {len(gfx_sprites)}')

tex_to_icons = {}
not_found = []
for ic in soviet_focuses:
    tex = gfx_sprites.get(ic)
    if not tex:
        not_found.append(ic)
    else:
        tex_to_icons.setdefault(tex, []).append(ic)

print(f'Not found in local gfx: {len(not_found)}')
if not_found:
    print('Sample not found (first 10):', not_found[:10])

print(f'Distinct textures used: {len(tex_to_icons)}')
print('Duplicate textures:')
for tex, ics in sorted(tex_to_icons.items(), key=lambda x: -len(x[1])):
    if len(ics) > 1:
        print(f'{tex} ({len(ics)} times): {ics}')
