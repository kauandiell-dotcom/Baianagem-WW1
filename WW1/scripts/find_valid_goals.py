import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
text = open(ROOT / 'common' / 'national_focus' / 'germany.txt', encoding='utf-8').read()
used = set(re.findall(r'icon\s*=\s*(\S+)', text))

goals_gfx = open(ROOT / 'interface' / 'ww1_germany_goals.gfx', encoding='utf-8').read()
defined_goals = set(re.findall(r'name\s*=\s*"([^"]+)"', goals_gfx))
valid_normal_goals = {s for s in defined_goals if not s.endswith('_shine')}

available = sorted(valid_normal_goals - used)
print(f"Total available valid focus sprites in ww1_germany_goals.gfx: {len(available)}")

kiel_cands = [s for s in available if any(k in s.lower() for k in ['fleet', 'marine', 'sea', 'navy', 'water', 'ship'])]
baltic_cands = [s for s in available if any(k in s.lower() for k in ['baltic', 'crusade', 'landeswehr', 'east', 'army', 'officer', 'knight', 'prussia'])]

print("Kiel candidates:", kiel_cands[:8])
print("Baltic candidates:", baltic_cands[:8])
