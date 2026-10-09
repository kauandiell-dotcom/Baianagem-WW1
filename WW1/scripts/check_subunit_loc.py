from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# Load all loc keys
en_keys = {}
pt_keys = {}

for p in (ROOT / "localisation").glob("**/*.yml"):
    raw = p.read_bytes()
    txt = raw.decode("utf-8-sig", errors="ignore")
    is_pt = "braz_por" in p.name.lower()
    for line in txt.splitlines():
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d*)\s*"(.*)"\s*$', line)
        if m:
            k, val = m.group(1), m.group(2)
            if is_pt:
                pt_keys[k] = val
            else:
                en_keys[k] = val

print(f"Loaded {len(en_keys)} EN keys and {len(pt_keys)} PT keys.")

# Parse subunits
subunits = {}
for p in (ROOT / "common/units").glob("*.txt"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'sub_units\s*=\s*\{([\s\S]*)\}', txt)
    if m:
        content = m.group(1)
        for unit_match in re.finditer(r'(?m)^[\t ]{1,2}([a-zA-Z0-9_]+)\s*=\s*\{', content):
            u_name = unit_match.group(1)
            if u_name not in ['type', 'categories', 'need', 'essential']:
                subunits[u_name] = p.name

missing_en = []
missing_pt = []

# Exclude terrain and noise parsed by script
noise = {'snow', 'plains', 'hills', 'mountain', 'desert', 'forest', 'jungle', 'marsh', 'urban', 'river', 'fort', 'amphibious', 'need_equipment', 'need_equipment_modules', 'critical_parts', 'battalion_mult', 'allowed_battalion_groups'}

real_subunits = {k: v for k, v in subunits.items() if k not in noise}

for u, src in sorted(real_subunits.items()):
    if u not in en_keys:
        missing_en.append((u, src))
    if u not in pt_keys:
        missing_pt.append((u, src))

print(f"\nTotal real sub-units: {len(real_subunits)}")
print(f"Sub-units missing in English: {len(missing_en)}")
for u, src in missing_en:
    print(f"  MISSING EN: {u} (from {src})")

print(f"\nSub-units missing in Portuguese: {len(missing_pt)}")
for u, src in missing_pt:
    print(f"  MISSING PT: {u} (from {src})")
