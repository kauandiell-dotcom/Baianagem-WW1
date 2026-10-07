import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for gfile in [ROOT / 'interface' / 'ww1_germany_goals.gfx', ROOT / 'interface' / 'ww1_germany_focus_art.gfx', ROOT / 'interface' / 'ww1_ger_rus_rework_assets.gfx']:
    text = open(gfile, encoding='utf-8').read()
    names = set(re.findall(r'name\s*=\s*"([^"]+)"', text))
    normal = [n for n in names if not n.endswith('_shine')]
    kiel = [n for n in normal if any(k in n.lower() for k in ['kiel', 'marine', 'sailor', 'fleet', 'mutiny'])]
    if kiel:
        print(f"{gfile.name}: {kiel}")
