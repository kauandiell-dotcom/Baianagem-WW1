from pathlib import Path
import re

ROOT = Path(".")

# 1. Investigate the 3 undefined German icons
print("=== 1. German Undefined Icons ===")
sprites = {}
for g in (ROOT / "interface").rglob("*.gfx"):
    with open(g, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for m in re.finditer(r'name\s*=\s*\"([^\"]+)\"\s+texturefile\s*=\s*\"([^\"]+)\"', content, re.IGNORECASE):
        sprites[m.group(1)] = m.group(2)

targets = ['GFX_GER_a7v-86394', 'GFX_GER_adriatic_sea_reinforcement-45124', 'GFX_GER_asienkorps_units-86387']
for t in targets:
    print(f"Target: {t} -> in sprites: {t in sprites}")
    base = t.replace('GFX_', '').split('-')[0]
    matches = [s for s in sprites if base.lower() in s.lower()]
    print(f"  Matches for {base}: {matches}")

# 2. Investigate duplicate event IDs in side_ww1_ger_rus_depth.txt
print("\n=== 2. Duplicate Event IDs ===")
events_dir = ROOT / "events"
events_map = {}
for p in events_dir.rglob("*.txt"):
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        for line_no, line in enumerate(f, 1):
            m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_\.\-]+)', line)
            if m:
                eid = m.group(1)
                events_map.setdefault(eid, []).append((p.name, line_no))

dupes = {k: v for k, v in events_map.items() if len(v) > 1}
print(f"Found {len(dupes)} duplicate event IDs.")
for eid, locs in sorted(dupes.items()):
    if "side_ww1_ger_rus" in eid or "ww1" in eid or "germany" in eid:
        print(f"  {eid}: {locs}")

# 3. Investigate localization coverage for recent content
print("\n=== 3. Localisation Coverage Analysis ===")
recent_files_en = [
    "ww1_germany_rework_l_english.yml",
    "ww1_france_rework_l_english.yml",
    "ww1_britain_rework_l_english.yml",
    "ww1_austria_hungary_l_english.yml",
    "ww1_italy_l_english.yml"
]

for rf in recent_files_en:
    p_en = ROOT / "localisation" / "english" / rf
    rf_pt = rf.replace("l_english.yml", "l_braz_por.yml")
    p_pt = ROOT / "localisation" / "braz_por" / rf_pt
    if not p_en.exists():
        print(f"MISSING EN FILE: {rf}")
        continue
    if not p_pt.exists():
        print(f"MISSING PT FILE: {rf_pt}")
        continue
    
    with open(p_en, "r", encoding="utf-8-sig") as f:
        en_keys = {m.group(1) for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE)}
    with open(p_pt, "r", encoding="utf-8-sig") as f:
        pt_keys = {m.group(1) for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE)}
    
    missing_in_pt = en_keys - pt_keys
    print(f"{rf}: {len(en_keys)} EN keys | {len(pt_keys)} PT keys | {len(missing_in_pt)} MISSING in PT")
    if missing_in_pt:
        for k in sorted(list(missing_in_pt))[:5]:
            print(f"   sample missing: {k}")

# 4. Search for raw code IDs appearing in strings
print("\n=== 4. Raw Code IDs in Localisation Strings ===")
raw_code_patterns = re.compile(r'\"([a-zA-Z0-9_]+\.(dds|txt|png)|ITA_ww1_\w+|GER_ww1_\w+|FRA_ww1_\w+|ENG_ww1_\w+|AUS_ww1_\w+)\"')
for path in (ROOT / "localisation").rglob("*.yml"):
    with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()
    matches = raw_code_patterns.findall(content)
    if matches:
        print(f"  {path.name}: {matches[:5]}")
