import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

text = open(ROOT / 'common' / 'national_focus' / 'germany.txt', encoding='utf-8').read()
used = set(re.findall(r'icon\s*=\s*(\S+)', text))

goals_gfx = open(ROOT / 'interface' / 'ww1_germany_goals.gfx', encoding='utf-8').read()
defined_goals = set(re.findall(r'name\s*=\s*"([^"]+)"', goals_gfx))
valid_normal_goals = {s for s in defined_goals if not s.endswith('_shine')}

unused = sorted(valid_normal_goals - used)
print('Total unused in goals.gfx:', len(unused))

for u in unused:
    if any(k in u.lower() for k in ['navy', 'sea', 'fleet', 'sail', 'marine', 'ship', 'dread', 'torp', 'baltic', 'officer', 'landeswehr', 'east', 'pruss', 'war', 'army']):
        print(' ', u)
