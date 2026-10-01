import glob, os, re

print("=== CHECKING ALL YAML LOCALIZATION FILES ===")

yaml_files = glob.glob('localisation/**/*.yml', recursive=True)
print(f"Total YAML files found: {len(yaml_files)}")

errors = []
for f in yaml_files:
    # Check BOM
    with open(f, 'rb') as fp:
        raw = fp.read()
        if not raw.startswith(b'\xef\xbb\xbf'):
            errors.append(f"{f}: Missing UTF-8 BOM!")
    
    # Check text lines
    with open(f, 'r', encoding='utf-8-sig', errors='replace') as fp:
        lines = fp.readlines()
        if not lines:
            errors.append(f"{f}: Empty file!")
            continue
        first_line = lines[0].strip()
        if not (first_line.startswith('l_english:') or first_line.startswith('l_braz_por:')):
            errors.append(f"{f}: Invalid first line: {first_line}")
        
        for idx, line in enumerate(lines[1:], 2):
            s = line.strip()
            if not s or s.startswith('#'):
                continue
            # Each entry should be: key: "value" or key:0 "value"
            # Check quotes balance
            q_count = s.count('"')
            if q_count < 2:
                errors.append(f"{f}:{idx}: Missing closing quote in line: {s[:50]}")
            elif q_count % 2 != 0:
                errors.append(f"{f}:{idx}: Unbalanced quotes in line: {s[:50]}")

print(f"YAML validation errors: {len(errors)}")
if errors:
    for e in errors:
        print(" ", e)
else:
    print("All YAML files are 100% valid with UTF-8 BOM and correct quote balancing!")
assert len(errors) == 0, "YAML validation failed!"
