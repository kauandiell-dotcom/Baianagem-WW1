from pathlib import Path
import re

ROOT = Path(".")

print("=== DEEP LOCALISATION AUDIT ===")

loc_files = list(ROOT.glob("localisation/**/*.yml"))
raw_key_in_value = []
file_in_value = []
empty_values = []

for lf in loc_files:
    try:
        with open(lf, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {lf}: {e}")
        continue
    
    # check header
    if lines:
        header = lines[0].strip()
        expected = "l_english:" if "english" in str(lf) else "l_braz_por:"
        if not header.startswith(expected):
            print(f"HEADER MISMATCH in {lf.name}: line 1 is '{header}', expected '{expected}'")

    for idx, line in enumerate(lines, 1):
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        m = re.match(r'^\s*([\w\.\-]+):\d*\s*\"(.*)\"\s*$', line)
        if not m:
            continue
        k, v = m.group(1), m.group(2)
        
        # 1. value is literally the key name
        if k == v or v == f"{k}_desc":
            raw_key_in_value.append((lf.name, idx, k, v))
            
        # 2. value contains a file extension
        if re.search(r'\.(dds|png|tga|txt|yml|yaml|gui|gfx)\b', v, re.IGNORECASE):
            file_in_value.append((lf.name, idx, k, v))
            
        # 3. empty value
        if v == "":
            empty_values.append((lf.name, idx, k))

print(f"1. Keys whose value is identical to key name: {len(raw_key_in_value)}")
for fn, idx, k, v in raw_key_in_value[:20]:
    print(f"   [{fn}:{idx}] {k} -> \"{v}\"")

print(f"2. Values containing filenames (.dds, .txt, etc.): {len(file_in_value)}")
for fn, idx, k, v in file_in_value[:20]:
    print(f"   [{fn}:{idx}] {k} -> \"{v}\"")

print(f"3. Empty values: {len(empty_values)}")
for fn, idx, k in empty_values[:20]:
    print(f"   [{fn}:{idx}] {k}")
