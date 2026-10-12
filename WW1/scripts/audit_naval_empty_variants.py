# scripts/audit_naval_empty_variants.py
import glob
import re

print("=== Countries with ww1_1911 variants without modules ===")
country_files = glob.glob('history/countries/*.txt')
for fpath in country_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    matches = re.findall(r'create_equipment_variant\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', text)
    no_mods = []
    for m in matches:
        if 'ww1_1911_' in m and 'modules' not in m:
            t = re.search(r'type\s*=\s*(\w+)', m)
            n = re.search(r'name\s*=\s*"([^"]+)"', m)
            if t and not t.group(1).endswith('_legacy'):
                no_mods.append((n.group(1) if n else '?', t.group(1)))
    if no_mods:
        print(f"{fpath}: {len(no_mods)} empty variants!")
        for name, htype in no_mods[:4]:
            print(f"   - {name} ({htype})")

print("\n=== Check OOB files for create_equipment_variant without modules ===")
oob_files = glob.glob('history/units/*.txt')
for fpath in oob_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    matches = re.findall(r'create_equipment_variant\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', text)
    no_mods = []
    for m in matches:
        if 'ww1_1911_' in m and 'modules' not in m:
            t = re.search(r'type\s*=\s*(\w+)', m)
            n = re.search(r'name\s*=\s*"([^"]+)"', m)
            if t and not t.group(1).endswith('_legacy'):
                no_mods.append((n.group(1) if n else '?', t.group(1)))
    if no_mods:
        print(f"{fpath}: {len(no_mods)} empty variants!")
