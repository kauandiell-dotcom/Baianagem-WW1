import re

content = open('interface/ww1_france_goals.gfx', encoding='utf-8', errors='ignore').read()
sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', content))
normal = sorted([s for s in sprites if not s.endswith('_shine')])
print(f'Total normal sprites: {len(normal)}')

with open('scripts/all_normal_france_sprites.txt', 'w', encoding='utf-8') as f:
    for s in normal:
        f.write(s + '\n')
print('Wrote all sprites to scripts/all_normal_france_sprites.txt')
