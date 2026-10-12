# scripts/check_eng_gfx.py
import re
with open('interface/ww1_britain_goals.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

sprites = re.findall(r'name\s*=\s*"([^"]+)"', text)
print(f'Total sprites in ww1_britain_goals.gfx: {len(sprites)}')
normal = set(s for s in sprites if not s.endswith('_shine'))
shine = set(s for s in sprites if s.endswith('_shine'))
print(f'Normal sprites: {len(normal)}, Shine: {len(shine)}')

from scripts.parsed_eng_focuses import ENG_FOCUSES
missing_normal = []
missing_shine = []
for f in ENG_FOCUSES:
    fid = f['id']
    exp_norm = f"GFX_goal_ww1_{fid}"
    exp_shine = f"GFX_goal_ww1_{fid}_shine"
    if exp_norm not in normal:
        missing_normal.append(exp_norm)
    if exp_shine not in shine:
        missing_shine.append(exp_shine)

print(f'Missing normal sprites: {len(missing_normal)}')
print(f'Missing shine sprites: {len(missing_shine)}')
