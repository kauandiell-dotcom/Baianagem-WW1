# scripts/check_naval_variants_detail.py
import glob
import re

all_c = glob.glob('history/countries/*.txt') + glob.glob('history/units/*.txt')
found = 0
for fpath in all_c:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    matches = re.findall(r'create_equipment_variant\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', text)
    for m in matches:
        if 'modules' in m and ('ship' in m or 'ww1_1911_' in m):
            t = re.search(r'type\s*=\s*(\w+)', m)
            n = re.search(r'name\s*=\s*"([^"]+)"', m)
            print(f"{fpath}: {n.group(1) if n else '?'} ({t.group(1) if t else '?'})")
            found += 1
            if found >= 10:
                break
    if found >= 10:
        break
