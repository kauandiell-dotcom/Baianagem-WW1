import glob
import re

for f in sorted(glob.glob('history/countries/*.txt')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    blocks = re.findall(r'create_equipment_variant\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', c)
    ww1 = [b for b in blocks if 'ww1_1911_' in b and 'modules' not in b]
    if ww1:
        print(f"=== {f} ({len(ww1)} empty variants) ===")
        by_type = {}
        for b in ww1:
            m_type = re.search(r'type\s*=\s*(\w+)', b)
            m_name = re.search(r'name\s*=\s*"([^"]+)"', b)
            if m_type and m_name:
                t = m_type.group(1)
                n = m_name.group(1)
                by_type.setdefault(t, []).append(n)
        for t, names in by_type.items():
            print(f"   {t} ({len(names)}): {names[:4]}")
