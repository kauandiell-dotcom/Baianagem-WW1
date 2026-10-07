from pathlib import Path
import re

ROOT = Path(".")

en_files = list((ROOT / "localisation" / "english").glob("*.yml"))
file_stats = []

for ef in en_files:
    with open(ef, "r", encoding="utf-8-sig", errors="ignore") as f:
        en_keys = {m.group(1) for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE)}
    
    pt_f = ROOT / "localisation" / "braz_por" / ef.name.replace("_l_english.yml", "_l_braz_por.yml")
    if pt_f.exists():
        with open(pt_f, "r", encoding="utf-8-sig", errors="ignore") as f:
            pt_keys = {m.group(1) for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE)}
    else:
        pt_keys = set()
    
    missing_count = len(en_keys - pt_keys)
    file_stats.append((ef.name, len(en_keys), len(pt_keys), missing_count))

file_stats.sort(key=lambda x: x[3], reverse=True)
print(f"{'FILE':<35} | {'EN KEYS':<8} | {'PT KEYS':<8} | {'MISSING PT':<10}")
print("-" * 70)
for fn, enk, ptk, mis in file_stats:
    if mis > 0:
        print(f"{fn:<35} | {enk:<8} | {ptk:<8} | {mis:<10}")
