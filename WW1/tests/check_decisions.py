import glob, re, os

print("=== CHECKING DECISIONS & MISSIONS ===")

with open('common/decisions/ww1_germany_decisions.txt', 'r', encoding='utf-8') as f:
    dec_text = f.read()

# Check braces
opens = dec_text.count('{')
closes = dec_text.count('}')
print(f"Brace check in ww1_germany_decisions.txt: Opens={opens}, Closes={closes}")
assert opens == closes, "Mismatched braces in ww1_germany_decisions.txt!"

# Find all decision category blocks
categories = re.findall(r'^([A-Za-z0-9_]+)\s*=\s*\{', dec_text, re.MULTILINE)
print(f"Categories in decisions file: {categories}")

# Check category definitions in common/decisions/categories/*.txt
defined_cats = set()
for f in glob.glob('common/decisions/categories/*.txt'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c_text = fp.read()
        cats = re.findall(r'^([A-Za-z0-9_]+)\s*=\s*\{', c_text, re.MULTILINE)
        for c in cats:
            defined_cats.add(c)

print(f"Categories defined in common/decisions/categories/: {len(defined_cats)}")
missing_cats = [c for c in categories if c not in defined_cats]
print(f"Missing decision categories: {missing_cats}")

# Check decision IDs
dec_ids = re.findall(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', dec_text, re.MULTILINE)
print(f"Total decisions & missions: {len(dec_ids)}")

# Check localization
with open('localisation/english/ww1_germany_focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    en_loc = f.read()

with open('localisation/braz_por/ww1_germany_focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    pt_loc = f.read()

missing_en = [d for d in dec_ids if f"{d}:" not in en_loc]
missing_pt = [d for d in dec_ids if f"{d}:" not in pt_loc]
print(f"Decisions missing EN loc: {len(missing_en)} {missing_en}")
print(f"Decisions missing PT loc: {len(missing_pt)} {missing_pt}")
