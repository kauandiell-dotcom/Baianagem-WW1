import re
from pathlib import Path

# collect all sprite names in interface/*.gfx
sprites = set()
for p in Path('interface').glob('*.gfx'):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'name\s*=\s*"([^"]+)"', txt):
        sprites.add(m.group(1))

files = ['common/ideas/ww1_france_ideas.txt', 'common/ideas/zz_ww1_france_reforms.txt']
for fname in files:
    txt = Path(fname).read_text(encoding='utf-8')
    ideas = re.findall(r'(\bFRA_[a-zA-Z0-9_]+\b)\s*=\s*\{', txt)
    missing = [i for i in ideas if f'GFX_idea_{i}' not in sprites]
    print(f'{fname}: {len(ideas)} ideas, {len(missing)} missing sprites:')
    for m in missing:
        print(f'   {m}')
