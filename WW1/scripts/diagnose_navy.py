# scripts/diagnose_navy.py
import glob
import re

print("=== 1. Country Naval OOBs and Variants ===")
for tag in ['ENG', 'GER', 'FRA', 'RUS', 'USA', 'ITA', 'TUR', 'AUH', 'JAP']:
    cfiles = glob.glob(f'history/countries/{tag}*.txt')
    if not cfiles:
        continue
    with open(cfiles[0], 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    oobs = re.findall(r'set_naval_oob\s*=\s*"([^"]+)"', c)
    variants = re.findall(r'create_equipment_variant\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', c)
    print(f"\n{tag} (file: {cfiles[0]}):")
    print(f"  OOBs: {oobs}")
    print(f"  Variants in country file: {len(variants)}")
    if variants:
        for v in variants[:3]:
            name = re.search(r'name\s*=\s*"([^"]+)"', v)
            hull = re.search(r'type\s*=\s*(\w+)', v)
            print(f"    variant: name={name.group(1) if name else '?'} type={hull.group(1) if hull else '?'}")

print("\n=== 2. Check OOB files for ships ===")
sample_oobs = glob.glob('history/units/*naval*.txt')[:15]
for oob in sample_oobs:
    with open(oob, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    variants = re.findall(r'create_equipment_variant\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', text)
    ships = re.findall(r'ship\s*=\s*\{([^}]+)\}', text)
    if '1911' in oob or 'ENG' in oob or 'GER' in oob:
        print(f"OOB {oob}: {len(ships)} ships, {len(variants)} variants")

print("\n=== 3. Check ww1_1911_naval_hulls.txt vs MTG hulls ===")
with open('common/units/equipment/ww1_1911_naval_hulls.txt', 'r', encoding='utf-8', errors='ignore') as f:
    hulls_txt = f.read()

hulls = re.findall(r'(\bww1_1911_\w+)\s*=\s*\{', hulls_txt)
print(f"Hulls in ww1_1911_naval_hulls.txt ({len(hulls)}):")
print(hulls)

print("\n=== 4. Check modules in ww1_1911_naval_modules.txt ===")
with open('common/units/equipment/modules/ww1_1911_naval_modules.txt', 'r', encoding='utf-8', errors='ignore') as f:
    mods_txt = f.read()

modules = re.findall(r'(\bww1_1911_\w+)\s*=\s*\{', mods_txt)
print(f"Modules in ww1_1911_naval_modules.txt ({len(modules)}):")
print(modules)
