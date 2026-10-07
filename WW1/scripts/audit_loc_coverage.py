from pathlib import Path
import re

ROOT = Path(".")
print("=== COMPREHENSIVE LOCALISATION AUDIT ACROSS ALL ENTITIES ===")

# Load all loc keys
loc_keys_en = set()
loc_keys_pt = set()

for p in (ROOT / "localisation" / "english").rglob("*.yml"):
    with open(p, "r", encoding="utf-8-sig", errors="ignore") as f:
        for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE):
            loc_keys_en.add(m.group(1))

for p in (ROOT / "localisation" / "braz_por").rglob("*.yml"):
    with open(p, "r", encoding="utf-8-sig", errors="ignore") as f:
        for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE):
            loc_keys_pt.add(m.group(1))

for p in (ROOT / "localisation" / "replace").rglob("*.yml"):
    is_pt = "braz_por" in p.name
    with open(p, "r", encoding="utf-8-sig", errors="ignore") as f:
        for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"', f.read(), re.MULTILINE):
            if is_pt:
                loc_keys_pt.add(m.group(1))
            else:
                loc_keys_en.add(m.group(1))

print(f"Total English keys loaded: {len(loc_keys_en)}")
print(f"Total Portuguese keys loaded: {len(loc_keys_pt)}")

# 1. Check all ideas
ideas_dir = ROOT / "common" / "ideas"
all_ideas = []
for p in ideas_dir.rglob("*.txt"):
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    for lno, line in enumerate(lines, 1):
        m = re.match(r'^\s*([a-zA-Z0-9_\-]+)\s*=\s*\{', line)
        if m:
            token = m.group(1)
            if token not in ["country", "hidden_ideas", "political_advisor", "tank_manufacturer", "naval_manufacturer", "aircraft_manufacturer", "materiel_manufacturer", "industrial_concern", "theorist", "army_chief", "navy_chief", "air_chief", "high_command"]:
                all_ideas.append((p.name, lno, token))

missing_ideas_en = [i for i in all_ideas if i[2] not in loc_keys_en]
missing_ideas_pt = [i for i in all_ideas if i[2] not in loc_keys_pt]
print(f"\nIdeas defined in common/ideas: {len(all_ideas)}")
print(f"Ideas missing in EN: {len(missing_ideas_en)}")
print(f"Ideas missing in PT: {len(missing_ideas_pt)}")
if missing_ideas_pt:
    print("  Sample ideas missing in PT:")
    for fn, lno, tok in missing_ideas_pt[:20]:
        print(f"    [{fn}:{lno}] {tok} (in EN? {tok in loc_keys_en})")

# 2. Check all decisions and categories
decisions_dir = ROOT / "common" / "decisions"
all_decisions = []
all_categories = []
for p in decisions_dir.rglob("*.txt"):
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    in_cat = False
    for lno, line in enumerate(lines, 1):
        m_cat = re.match(r'^([a-zA-Z0-9_\-]+)\s*=\s*\{', line)
        if m_cat:
            all_categories.append((p.name, lno, m_cat.group(1)))
        m_dec = re.match(r'^\t([a-zA-Z0-9_\-]+)\s*=\s*\{', line)
        if m_dec:
            tok = m_dec.group(1)
            if tok not in ["allowed", "visible", "available", "cost", "days_remove", "fire_only_once", "ai_will_do", "complete_effect", "remove_effect"]:
                all_decisions.append((p.name, lno, tok))

missing_dec_pt = [d for d in all_decisions if d[2] not in loc_keys_pt]
missing_cat_pt = [c for c in all_categories if c[2] not in loc_keys_pt]
print(f"\nDecisions: {len(all_decisions)} | Missing in PT: {len(missing_dec_pt)}")
if missing_dec_pt:
    for fn, lno, tok in missing_dec_pt[:15]:
        print(f"  Missing dec PT: [{fn}:{lno}] {tok} (in EN? {tok in loc_keys_en})")
print(f"Categories: {len(all_categories)} | Missing in PT: {len(missing_cat_pt)}")
if missing_cat_pt:
    for fn, lno, tok in missing_cat_pt[:15]:
        print(f"  Missing cat PT: [{fn}:{lno}] {tok} (in EN? {tok in loc_keys_en})")

# 3. Check all focuses
focus_dir = ROOT / "common" / "national_focus"
all_focuses = []
for p in focus_dir.rglob("*.txt"):
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        for m in re.finditer(r'\bid\s*=\s*([a-zA-Z0-9_\-]+)', f.read()):
            all_focuses.append((p.name, m.group(1)))

missing_foc_pt = [f for f in all_focuses if f[1] not in loc_keys_pt]
print(f"\nFocuses across all trees: {len(all_focuses)} | Missing in PT: {len(missing_foc_pt)}")
if missing_foc_pt:
    for fn, tok in missing_foc_pt[:20]:
        print(f"  Missing focus PT: [{fn}] {tok}")
