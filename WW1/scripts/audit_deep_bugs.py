import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def audit_localisation_file_names():
    print("\n" + "="*70)
    print("1. LOCALISATION DEEP CHECK: FILENAMES / PATHS / PLACEHOLDERS IN STRINGS")
    print("="*70)
    loc_dir = ROOT / "localisation"
    file_extensions = re.compile(r'\b[\w\-\.\/\\\:]+\.(dds|png|tga|txt|yml|yaml|gui|gfx|shader|fxh)\b', re.IGNORECASE)
    path_pattern = re.compile(r'[a-zA-Z]:[\\/]|(?:gfx|common|events|history)[\\/]', re.IGNORECASE)
    issues = []

    for path in loc_dir.rglob("*.yml"):
        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                lines = f.readlines()
        except Exception as e:
            issues.append((path, 0, f"Encoding error reading file: {e}"))
            continue

        for i, line in enumerate(lines, 1):
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            m = re.match(r'^\s*([\w\.\-]+):\d*\s*\"(.*)\"\s*$', line)
            if not m:
                continue
            key, val = m.group(1), m.group(2)
            
            # Check if key itself looks like a filename
            if file_extensions.search(key):
                issues.append((path, i, f"KEY contains filename: {key}"))
                
            # Check if value literally contains a filename or file path
            found_ext = file_extensions.findall(val)
            if found_ext:
                # filter out benign words if any
                issues.append((path, i, f"STRING contains filename: key='{key}' -> \"{val}\""))
                
            if path_pattern.search(val):
                issues.append((path, i, f"STRING contains filesystem path: key='{key}' -> \"{val}\""))
                
            # Check for raw unlocalized placeholders like "Focus Name" or "TODO"
            if re.match(r'^(TODO|REPLACE_ME|Focus Name|MISSING)$', val, re.IGNORECASE):
                issues.append((path, i, f"STRING has placeholder text: key='{key}' -> \"{val}\""))

    print(f"Total filename/path/placeholder issues found in localisation: {len(issues)}")
    for p, line_no, desc in issues[:40]:
        print(f"  [{p.relative_to(ROOT)}:{line_no}] {desc}")
    if len(issues) > 40:
        print(f"  ... and {len(issues) - 40} more.")
    return issues


def audit_missing_loc_keys():
    print("\n" + "="*70)
    print("2. AUDIT MISSING LOCALISATION FOR RECENT TREES (GER, FRA, ENG, AUS, ITA)")
    print("="*70)
    # Collect all loc keys in english and braz_por
    loc_keys = {"english": set(), "braz_por": set()}
    for lang in ["english", "braz_por"]:
        lang_dir = ROOT / "localisation" / lang
        if not lang_dir.exists():
            continue
        for p in lang_dir.rglob("*.yml"):
            try:
                with open(p, "r", encoding="utf-8-sig") as f:
                    for line in f:
                        m = re.match(r'^\s*([\w\.\-]+):\d*\s*\"', line)
                        if m:
                            loc_keys[lang].add(m.group(1))
            except Exception:
                pass

    print(f"Loaded {len(loc_keys['english'])} English keys and {len(loc_keys['braz_por'])} Portuguese keys.")

    trees = ["germany.txt", "france.txt", "uk.txt", "austria.txt", "italy.txt"]
    missing_report = []

    for tree in trees:
        tree_file = ROOT / "common" / "national_focus" / tree
        if not tree_file.exists():
            continue
        with open(tree_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Find all focuses
        focus_blocks = re.findall(r'focus\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content)
        for block in focus_blocks:
            id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\-]+)', block)
            if not id_m:
                continue
            f_id = id_m.group(1)
            # check title and desc
            title_key = f_id
            desc_key = f"{f_id}_desc"
            for lang in ["english", "braz_por"]:
                if title_key not in loc_keys[lang]:
                    missing_report.append((tree, f_id, lang, "title", title_key))
                if desc_key not in loc_keys[lang]:
                    missing_report.append((tree, f_id, lang, "desc", desc_key))

    print(f"Total missing focus loc keys across 5 major trees: {len(missing_report)}")
    for t, fid, lang, kind, key in missing_report[:30]:
        print(f"  [{t}] {fid} missing {lang} {kind} (key: {key})")
    if len(missing_report) > 30:
        print(f"  ... and {len(missing_report) - 30} more.")
    return missing_report


def audit_gfx_and_sprites():
    print("\n" + "="*70)
    print("3. AUDIT GFX DEFINITIONS & SPRITES ON DISK")
    print("="*70)
    # Collect all spriteType definitions in interface/*.gfx
    gfx_sprites = {}
    interface_dir = ROOT / "interface"
    for p in interface_dir.rglob("*.gfx"):
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # find spriteType blocks
            matches = re.findall(r'SpriteType\s*=\s*\{[^}]*name\s*=\s*\"([^\"]+)\"[^}]*texturefile\s*=\s*\"([^\"]+)\"', content, re.IGNORECASE)
            for name, tex in matches:
                gfx_sprites[name] = tex.replace("\\", "/")
        except Exception:
            pass

    print(f"Loaded {len(gfx_sprites)} SpriteType definitions from interface/*.gfx.")

    # Check focus trees for icon validity
    trees = ["germany.txt", "france.txt", "uk.txt", "austria.txt", "italy.txt"]
    broken_icons = []
    missing_files = []

    for tree in trees:
        tree_file = ROOT / "common" / "national_focus" / tree
        if not tree_file.exists():
            continue
        with open(tree_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        focus_blocks = re.findall(r'focus\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content)
        for block in focus_blocks:
            id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\-]+)', block)
            f_id = id_m.group(1) if id_m else "unknown"
            icon_m = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_\-]+)', block)
            if not icon_m:
                broken_icons.append((tree, f_id, "NO_ICON_SPECIFIED"))
                continue
            icon = icon_m.group(1)
            if icon not in gfx_sprites:
                broken_icons.append((tree, f_id, icon))
            else:
                tex_path = ROOT / gfx_sprites[icon]
                if not tex_path.exists():
                    missing_files.append((tree, f_id, icon, gfx_sprites[icon]))

    print(f"Total undefined spriteType icons in focus trees: {len(broken_icons)}")
    for t, fid, icon in broken_icons[:20]:
        print(f"  [{t}] {fid} uses undefined icon: {icon}")
    print(f"Total defined sprites with missing files on disk: {len(missing_files)}")
    for t, fid, icon, path in missing_files[:20]:
        print(f"  [{t}] {fid} sprite {icon} points to missing disk file: {path}")

    return broken_icons, missing_files


def audit_focus_prerequisites_and_collisions():
    print("\n" + "="*70)
    print("4. AUDIT FOCUS TREE PREREQUISITES, DAG CYCLES & COORDINATE COLLISIONS")
    print("="*70)
    trees = ["germany.txt", "france.txt", "uk.txt", "austria.txt", "italy.txt"]
    issues = []

    for tree in trees:
        tree_file = ROOT / "common" / "national_focus" / tree
        if not tree_file.exists():
            continue
        with open(tree_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Parse focuses
        # Extract id, x, y, prerequisites
        focus_pattern = re.compile(r'focus\s*=\s*\{(.*?)\n\t\}', re.DOTALL)
        focus_dict = {}
        coords = {}

        # simpler extraction
        lines = content.splitlines()
        current_focus = None
        in_focus = 0
        current_data = {}

        for line in lines:
            if re.search(r'\bfocus\s*=\s*\{', line):
                in_focus += 1
                current_data = {"prereqs": [], "mutually_exclusive": [], "x": None, "y": None}
                continue
            if in_focus > 0:
                if "{" in line:
                    in_focus += line.count("{")
                if "}" in line:
                    in_focus -= line.count("}")
                    if in_focus == 0:
                        if "id" in current_data:
                            fid = current_data["id"]
                            focus_dict[fid] = current_data
                            if current_data["x"] is not None and current_data["y"] is not None:
                                pt = (current_data["x"], current_data["y"])
                                coords.setdefault(pt, []).append(fid)
                        current_data = {}
                        continue

                m_id = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\-]+)', line)
                if m_id and "id" not in current_data:
                    current_data["id"] = m_id.group(1)
                m_x = re.search(r'\bx\s*=\s*(\d+)', line)
                if m_x and current_data["x"] is None:
                    current_data["x"] = int(m_x.group(1))
                m_y = re.search(r'\by\s*=\s*(\d+)', line)
                if m_y and current_data["y"] is None:
                    current_data["y"] = int(m_y.group(1))
                m_pre = re.findall(r'focus\s*=\s*([a-zA-Z0-9_\-]+)', line)
                if m_pre:
                    current_data["prereqs"].extend(m_pre)

        # check coordinate collisions
        collisions = {pt: ids for pt, ids in coords.items() if len(ids) > 1}
        if collisions:
            for pt, ids in collisions.items():
                issues.append((tree, f"COORDINATE COLLISION at x={pt[0]}, y={pt[1]}: {ids}"))

        # check dangling prerequisites
        for fid, data in focus_dict.items():
            for p in data["prereqs"]:
                if p not in focus_dict:
                    issues.append((tree, f"DANGLING PREREQUISITE: {fid} requires non-existent focus '{p}'"))

    print(f"Total DAG & Coordinate issues found: {len(issues)}")
    for t, desc in issues:
        print(f"  [{t}] {desc}")
    return issues


def audit_starting_spirits_and_ideas():
    print("\n" + "="*70)
    print("5. AUDIT STARTING SPIRITS DEFINED IN HISTORY VS COMMON/IDEAS")
    print("="*70)
    # Collect all idea ids defined in common/ideas/*.txt
    all_ideas = set()
    ideas_dir = ROOT / "common" / "ideas"
    for p in ideas_dir.rglob("*.txt"):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # an idea is typically a block under country = { ... }
                m = re.match(r'^\s*([a-zA-Z0-9_\-]+)\s*=\s*\{', line)
                if m:
                    all_ideas.add(m.group(1))

    print(f"Found {len(all_ideas)} candidate idea IDs in common/ideas/*.txt.")

    # Check history files for GER, FRA, ENG, AUS, ITA, SOV, TUR
    history_files = [
        "GER - Germany.txt", "FRA - France.txt", "ENG - Britain.txt",
        "AUS - Austria.txt", "ITA - Italy.txt", "SOV - Soviet union.txt", "TUR - Turkey.txt"
    ]
    missing_spirits = []
    for hf in history_files:
        p = ROOT / "history" / "countries" / hf
        if not p.exists():
            continue
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        in_ideas = False
        for line in lines:
            if "ideas = {" in line:
                in_ideas = True
                continue
            if in_ideas:
                if "}" in line:
                    in_ideas = False
                    continue
                tokens = re.findall(r'[a-zA-Z0-9_\-]+', line)
                for t in tokens:
                    if t not in all_ideas:
                        missing_spirits.append((hf, t))

    print(f"Total undefined starting ideas in history: {len(missing_spirits)}")
    for hf, spirit in missing_spirits:
        print(f"  [{hf}] Idea '{spirit}' used in history is NOT defined in common/ideas!")
    return missing_spirits


def audit_events_and_decisions():
    print("\n" + "="*70)
    print("6. AUDIT EVENT IDS AND DECISIONS SYNTAX")
    print("="*70)
    events_dir = ROOT / "events"
    event_ids = set()
    duplicate_events = []
    
    for p in events_dir.rglob("*.txt"):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, 1):
                m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.\-]+)', line)
                if m and ("country_event" in line or "news_event" in line or line.strip().startswith("id =")):
                    eid = m.group(1)
                    if eid in event_ids:
                        duplicate_events.append((p.name, line_no, eid))
                    else:
                        event_ids.add(eid)

    print(f"Total duplicate event IDs found: {len(duplicate_events)}")
    for fn, lno, eid in duplicate_events[:20]:
        print(f"  [{fn}:{lno}] Duplicate event ID: {eid}")
    return duplicate_events


if __name__ == "__main__":
    audit_localisation_file_names()
    audit_missing_loc_keys()
    audit_gfx_and_sprites()
    audit_focus_prerequisites_and_collisions()
    audit_starting_spirits_and_ideas()
    audit_events_and_decisions()
