import os
import sys
import re
import glob

REPO_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def check_brackets(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # remove comments
    lines = []
    for line in content.splitlines():
        line = re.sub(r'#.*$', '', line)
        lines.append(line)
    clean = "\n".join(lines)
    open_b = clean.count("{")
    close_b = clean.count("}")
    return open_b, close_b, open_b - close_b

def audit_characters():
    print("=== AUDITING CHARACTERS ===")
    sov_chars_file = os.path.join(REPO_ROOT, "common", "characters", "SOV.txt")
    wht_chars_file = os.path.join(REPO_ROOT, "common", "characters", "WHT.txt")
    
    def parse_chars(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
        chars = {}
        # Simple regex for top-level characters inside characters = { ... }
        for m in re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', text, re.MULTILINE):
            char_id = m.group(1)
            # Find closing bracket or next char
            chars[char_id] = text[m.start():m.start() + 1500]
        return chars

    sov_chars = parse_chars(sov_chars_file)
    wht_chars = parse_chars(wht_chars_file)
    print(f"Found {len(sov_chars)} characters in SOV.txt")
    print(f"Found {len(wht_chars)} characters in WHT.txt")

    # Check portraits on disk
    for cid, block in {**sov_chars, **wht_chars}.items():
        portraits = re.findall(r'(?:large|small)\s*=\s*"([^"]+)"', block)
        for p in portraits:
            norm_p = os.path.normpath(os.path.join(REPO_ROOT, p.replace("/", os.sep)))
            if not os.path.exists(norm_p):
                print(f"  [MISSING PORTRAIT] Character {cid} references non-existent texture: {p}")

    # Check history recruitment
    sov_hist = os.path.join(REPO_ROOT, "history", "countries", "SOV - Soviet union.txt")
    with open(sov_hist, "r", encoding="utf-8", errors="ignore") as f:
        hist_text = f.read()

    recruited_sov = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', hist_text)
    print(f"Recruited in SOV history: {len(recruited_sov)} characters")
    for r in recruited_sov:
        if r not in sov_chars:
            print(f"  [UNDEFINED RECRUIT] {r} recruited in SOV history but NOT in SOV.txt!")

    # Check for legacy country leaders
    legacy_leaders = re.findall(r'create_country_leader\s*=\s*\{[^}]*name\s*=\s*"([^"]+)"', hist_text)
    if legacy_leaders:
        print(f"  [LEGACY LEADER OVERLAP] Found legacy create_country_leader in SOV history: {legacy_leaders}")

    return sov_chars, wht_chars

def audit_focus_trees():
    print("\n=== AUDITING FOCUS TREES ===")
    trees = [
        os.path.join(REPO_ROOT, "common", "national_focus", "soviet.txt"),
        os.path.join(REPO_ROOT, "common", "national_focus", "soviet_russia.txt"),
        os.path.join(REPO_ROOT, "common", "national_focus", "white_russia.txt")
    ]
    for tree_path in trees:
        fname = os.path.basename(tree_path)
        op, cl, delta = check_brackets(tree_path)
        print(f"\nTree: {fname} (Brackets: open={op}, close={cl}, delta={delta})")
        if delta != 0:
            print(f"  [BRACKET ERROR] {fname} has unbalanced brackets! Delta = {delta}")

        with open(tree_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Extract focus blocks
        focus_blocks = {}
        # Pattern matching focus = { id = ... }
        matches = list(re.finditer(r'focus\s*=\s*\{', content))
        for i, m in enumerate(matches):
            start = m.start()
            end = matches[i+1].start() if i+1 < len(matches) else len(content)
            chunk = content[start:end]
            id_match = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', chunk)
            if id_match:
                fid = id_match.group(1)
                focus_blocks[fid] = chunk

        print(f"  Found {len(focus_blocks)} focuses in {fname}")

        # Check coordinates & collisions
        coords = {}
        for fid, block in focus_blocks.items():
            x_m = re.search(r'x\s*=\s*(-?\d+)', block)
            y_m = re.search(r'y\s*=\s*(-?\d+)', block)
            if x_m and y_m:
                x, y = int(x_m.group(1)), int(y_m.group(1))
                coords[fid] = (x, y)
            else:
                print(f"  [MISSING COORDS] Focus {fid} missing x/y coordinates!")

        # Check collisions (same x and y, and not mutually exclusive)
        coord_map = {}
        for fid, (x, y) in coords.items():
            key = (x, y)
            if key in coord_map:
                coord_map[key].append(fid)
            else:
                coord_map[key] = [fid]
        
        for (x, y), fids in coord_map.items():
            if len(fids) > 1:
                print(f"  [COORDINATE COLLISION] Focuses {fids} collide at ({x}, {y})!")

        # Check prerequisites
        for fid, block in focus_blocks.items():
            prereqs = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([A-Za-z0-9_]+)', block)
            for p in prereqs:
                if p not in focus_blocks:
                    print(f"  [DEAD PREREQUISITE] Focus {fid} requires non-existent focus: {p}")

        # Check mutual exclusivity reciprocity
        for fid, block in focus_blocks.items():
            mutexes = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block)
            for mutex_chunk in mutexes:
                targets = re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', mutex_chunk)
                for t in targets:
                    if t not in focus_blocks:
                        print(f"  [DEAD MUTEX] Focus {fid} mutually exclusive with non-existent focus: {t}")
                    else:
                        t_block = focus_blocks[t]
                        if fid not in t_block:
                            print(f"  [ASYMMETRIC MUTEX] Focus {fid} lists {t} as mutex, but {t} does not list {fid}!")

def audit_events():
    print("\n=== AUDITING EVENTS ===")
    event_files = [
        os.path.join(REPO_ROOT, "events", "ww1_ger_rus_rework_events.txt"),
        os.path.join(REPO_ROOT, "events", "ww1_russia_civil_war_events.txt"),
        os.path.join(REPO_ROOT, "events", "ww1_russia_crisis_events.txt"),
        os.path.join(REPO_ROOT, "events", "ww1_russia_diplomacy_events.txt"),
        os.path.join(REPO_ROOT, "events", "ww1_russia_events.txt")
    ]
    all_defined_events = set()
    event_contents = {}

    for ef in event_files:
        fname = os.path.basename(ef)
        op, cl, delta = check_brackets(ef)
        print(f"Event file: {fname} (Brackets: open={op}, close={cl}, delta={delta})")
        if delta != 0:
            print(f"  [BRACKET ERROR] {fname} has unbalanced brackets! Delta = {delta}")
        with open(ef, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        event_contents[fname] = c
        # Find defined event IDs
        ev_ids = re.findall(r'(?:country_event|news_event)\s*=\s*\{[^}]*?id\s*=\s*([A-Za-z0-9_.]+)', c, re.DOTALL)
        for eid in ev_ids:
            all_defined_events.add(eid)
        print(f"  Found {len(ev_ids)} events in {fname}")

    print(f"Total defined Russian events: {len(all_defined_events)}")

    # Check event dispatches
    for fname, c in event_contents.items():
        dispatches = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_.]+)', c)
        for disp in dispatches:
            if disp.startswith("ww1_russia") or disp.startswith("ww1_sov") or disp.startswith("ww1_wht"):
                if disp not in all_defined_events:
                    print(f"  [DEAD EVENT DISPATCH] In {fname}: calls non-existent event {disp}!")

def audit_decisions():
    print("\n=== AUDITING DECISIONS ===")
    dec_files = [
        os.path.join(REPO_ROOT, "common", "decisions", "ww1_ger_rus_rework_decisions.txt"),
        os.path.join(REPO_ROOT, "common", "decisions", "ww1_russia_crisis_decisions.txt"),
        os.path.join(REPO_ROOT, "common", "decisions", "ww1_russia_tsarist_decisions.txt"),
        os.path.join(REPO_ROOT, "common", "decisions", "ww1_soviet_civil_war_decisions.txt"),
        os.path.join(REPO_ROOT, "common", "decisions", "ww1_soviet_diplomacy_decisions.txt"),
        os.path.join(REPO_ROOT, "common", "decisions", "zz_ww1_sov_operations.txt")
    ]
    for df in dec_files:
        if not os.path.exists(df):
            continue
        fname = os.path.basename(df)
        op, cl, delta = check_brackets(df)
        print(f"Decision file: {fname} (Brackets: delta={delta})")
        if delta != 0:
            print(f"  [BRACKET ERROR] {fname} has unbalanced brackets! Delta = {delta}")

def audit_localization():
    print("\n=== AUDITING LOCALIZATION ===")
    loc_files = [
        ("localisation/english/ww1_ger_rus_rework_l_english.yml", "localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml"),
        ("localisation/english/ww1_russia_events_l_english.yml", "localisation/braz_por/ww1_russia_events_l_braz_por.yml"),
        ("localisation/english/ww1_russia_focus_l_english.yml", "localisation/braz_por/ww1_russia_focus_l_braz_por.yml"),
        ("localisation/english/ww1_russia_ideas_l_english.yml", "localisation/braz_por/ww1_russia_ideas_l_braz_por.yml"),
        ("localisation/english/ww1_soviet_l_english.yml", "localisation/braz_por/ww1_soviet_l_braz_por.yml"),
        ("localisation/english/ww1_sov_wings_l_english.yml", "localisation/braz_por/ww1_sov_wings_l_braz_por.yml"),
        ("localisation/english/ww1_white_l_english.yml", "localisation/braz_por/ww1_white_l_braz_por.yml")
    ]
    for en_rel, pt_rel in loc_files:
        en_p = os.path.join(REPO_ROOT, en_rel)
        pt_p = os.path.join(REPO_ROOT, pt_rel)
        if not os.path.exists(en_p):
            print(f"  [MISSING FILE] {en_rel}")
            continue
        if not os.path.exists(pt_p):
            print(f"  [MISSING FILE] {pt_rel}")
            continue

        with open(en_p, "rb") as f:
            en_bytes = f.read()
        with open(pt_p, "rb") as f:
            pt_bytes = f.read()

        en_bom = en_bytes.startswith(b"\xef\xbb\xbf")
        pt_bom = pt_bytes.startswith(b"\xef\xbb\xbf")
        en_double = en_bytes.startswith(b"\xef\xbb\xbf\xef\xbb\xbf")
        pt_double = pt_bytes.startswith(b"\xef\xbb\xbf\xef\xbb\xbf")

        print(f"Loc pair: {os.path.basename(en_p)} / {os.path.basename(pt_p)}")
        if not en_bom or en_double:
            print(f"  [BOM ERROR] {en_rel}: BOM={en_bom}, Double={en_double}")
        if not pt_bom or pt_double:
            print(f"  [BOM ERROR] {pt_rel}: BOM={pt_bom}, Double={pt_double}")

        # Parse keys
        en_text = en_bytes.decode("utf-8", errors="ignore")
        pt_text = pt_bytes.decode("utf-8", errors="ignore")

        en_keys = set(re.findall(r'^\s*([A-Za-z0-9_.]+):', en_text, re.MULTILINE))
        pt_keys = set(re.findall(r'^\s*([A-Za-z0-9_.]+):', pt_text, re.MULTILINE))

        # Filter out language headers
        en_keys.discard("l_english")
        pt_keys.discard("l_braz_por")

        missing_in_pt = en_keys - pt_keys
        missing_in_en = pt_keys - en_keys
        if missing_in_pt:
            print(f"  [KEY PARITY] {len(missing_in_pt)} keys in English but missing in Brazilian Portuguese: {list(missing_in_pt)[:10]}")
        if missing_in_en:
            print(f"  [KEY PARITY] {len(missing_in_en)} keys in Brazilian Portuguese but missing in English: {list(missing_in_en)[:10]}")
        if not missing_in_pt and not missing_in_en:
            print(f"  -> Perfect parity! {len(en_keys)} keys matched 100%.")

if __name__ == "__main__":
    audit_characters()
    audit_focus_trees()
    audit_events()
    audit_decisions()
    audit_localization()
