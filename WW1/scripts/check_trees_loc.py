from pathlib import Path
import re

ROOT = Path(".")

# Load all loc keys from localisation/ (including replace/)
loc_keys_en = {}
loc_keys_pt = {}

for p in (ROOT / "localisation").rglob("*.yml"):
    is_pt = "braz_por" in p.name
    with open(p, "r", encoding="utf-8-sig", errors="ignore") as f:
        for m in re.finditer(r'^\s*([\w\.\-]+):\d*\s*\"([^\"]*)\"', f.read(), re.MULTILINE):
            k, v = m.group(1), m.group(2)
            if is_pt:
                loc_keys_pt[k] = (p.name, v)
            else:
                loc_keys_en[k] = (p.name, v)

print(f"Loaded {len(loc_keys_en)} EN keys and {len(loc_keys_pt)} PT keys.")

trees = ["germany.txt", "france.txt", "uk.txt", "austria.txt", "italy.txt"]
for tree in trees:
    p = ROOT / "common" / "national_focus" / tree
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # parse each focus
    focuses = re.findall(r'focus\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content)
    missing_en_title = []
    missing_en_desc = []
    missing_pt_title = []
    missing_pt_desc = []
    
    for fblock in focuses:
        m_id = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\-]+)', fblock)
        if not m_id:
            continue
        fid = m_id.group(1)
        if fid not in loc_keys_en:
            missing_en_title.append(fid)
        if f"{fid}_desc" not in loc_keys_en:
            missing_en_desc.append(fid)
        if fid not in loc_keys_pt:
            missing_pt_title.append(fid)
        if f"{fid}_desc" not in loc_keys_pt:
            missing_pt_desc.append(fid)

    print(f"\nTree {tree} ({len(focuses)} focuses):")
    print(f"  Missing EN Title: {len(missing_en_title)} | Missing EN Desc: {len(missing_en_desc)}")
    print(f"  Missing PT Title: {len(missing_pt_title)} | Missing PT Desc: {len(missing_pt_desc)}")
    if missing_en_title:
        print(f"    Sample missing EN Title: {missing_en_title[:5]}")
    if missing_en_desc:
        print(f"    Sample missing EN Desc: {missing_en_desc[:5]}")
    if missing_pt_title:
        print(f"    Sample missing PT Title: {missing_pt_title[:5]}")
    if missing_pt_desc:
        print(f"    Sample missing PT Desc: {missing_pt_desc[:5]}")
