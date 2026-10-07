import re, glob

all_sprites = set()
for path in ['interface/ww1_germany_goals.gfx', 'interface/ww1_germany_focus_art.gfx', 'interface/ww1_ger_rus_rework_assets.gfx']:
    try:
        content = open(path, encoding='utf-8', errors='ignore').read()
        sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', content))
        normal = [s for s in sprites if not s.endswith('_shine')]
        print(f'{path}: {len(normal)} normal sprites')
        all_sprites.update(normal)
    except Exception as e:
        print(f'Error reading {path}: {e}')

sorted_sprites = sorted(all_sprites)
print(f'Total unique normal sprites across German gfx files: {len(sorted_sprites)}')

with open('scripts/all_normal_germany_sprites.txt', 'w', encoding='utf-8') as f:
    for s in sorted_sprites:
        f.write(s + '\n')
print('Saved to scripts/all_normal_germany_sprites.txt')
