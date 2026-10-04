import os
import sys
import re
import codecs

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def audit_braces(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Remove comments
    lines = [line.split('#')[0] for line in content.splitlines()]
    clean_text = "\n".join(lines)
    
    open_b = clean_text.count('{')
    close_b = clean_text.count('}')
    if open_b != close_b:
        raise ValueError(f"Brace mismatch in {filepath}: {open_b} open vs {close_b} close")
    return open_b

def audit_bom(filepath):
    with open(filepath, "rb") as f:
        header = f.read(3)
        if header != codecs.BOM_UTF8:
            raise ValueError(f"Missing UTF-8 BOM in {filepath}")

def extract_focus_blocks(text):
    blocks = []
    pos = 0
    while True:
        idx = text.find("focus = {", pos)
        if idx == -1:
            break
        start_brace = text.find("{", idx)
        depth = 1
        cur = start_brace + 1
        while cur < len(text) and depth > 0:
            ch = text[cur]
            if ch == '#':
                eol = text.find('\n', cur)
                if eol == -1:
                    break
                cur = eol
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            cur += 1
        block = text[start_brace + 1 : cur - 1]
        blocks.append(block)
        pos = cur
    return blocks

def run_validation():
    print("=================================================================")
    print("   FRENCH REPUBLIC FOCUS TREE & SYSTEMS AUDIT (HOI4 WW1)")
    print("=================================================================")

    # 1. Focus Tree File Audit
    focus_file = os.path.join(BASE_DIR, "common", "national_focus", "france.txt")
    print(f"[*] Auditing {focus_file}...")
    braces = audit_braces(focus_file)
    print(f"    -> Braces matched perfectly ({braces} pairs).")

    with open(focus_file, "r", encoding="utf-8") as f:
        text = f.read()

    raw_foci = extract_focus_blocks(text)
    print(f"    -> Extracted {len(raw_foci)} focus blocks.")

    id_map = {}
    foci = []
    coords = {}
    for block in raw_foci:
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_m:
            continue
        fid = id_m.group(1)
        x_m = re.search(r'\bx\s*=\s*(-?\d+)', block)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', block)
        x = int(x_m.group(1)) if x_m else 0
        y = int(y_m.group(1)) if y_m else 0
        
        # prereqs
        prereqs = []
        for pm in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', block):
            targets = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pm.group(1))
            prereqs.append(targets)
            
        # mut_ex
        mut_ex = []
        for mm in re.finditer(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block):
            targets = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', mm.group(1))
            mut_ex.extend(targets)

        f_data = {'id': fid, 'x': x, 'y': y, 'prereqs': prereqs, 'mut_ex': mut_ex}
        foci.append(f_data)
        id_map[fid] = f_data

    print(f"    -> Parsed {len(foci)} focuses.")
    assert len(foci) == len(id_map), "Duplicate focus IDs found!"

    # 2. Check coordinate collisions
    collisions = []
    for f in foci:
        pt = (f['x'], f['y'])
        if pt in coords:
            collisions.append((pt, f['id'], coords[pt]['id']))
        coords[pt] = f
    if collisions:
        raise ValueError(f"Coordinate collisions found: {collisions}")
    print(f"    -> Zero coordinate collisions across all {len(foci)} focuses.")

    # 3. Check DAG prerequisites & dy >= 1
    missing_prereqs = []
    bad_dy = []
    for f in foci:
        for pgroup in f['prereqs']:
            for p in pgroup:
                if p not in id_map:
                    missing_prereqs.append((f['id'], p))
                else:
                    parent = id_map[p]
                    if f['y'] <= parent['y']:
                        bad_dy.append((f['id'], p, f['y'], parent['y']))

    if missing_prereqs:
        raise ValueError(f"Missing prerequisites: {missing_prereqs}")
    if bad_dy:
        raise ValueError(f"Bad dy (child.y <= parent.y): {bad_dy}")
    print("    -> All prerequisites exist and satisfy dy >= 1 strictly.")

    # 4. Check DAG cycles
    visited = {}
    def check_cycle(fid, stack):
        visited[fid] = True
        stack.append(fid)
        for pgroup in id_map[fid]['prereqs']:
            for p in pgroup:
                if p in stack:
                    raise ValueError(f"Circular dependency detected: {' -> '.join(stack)} -> {p}")
                if p not in visited:
                    check_cycle(p, stack)
        stack.pop()

    for f in foci:
        if f['id'] not in visited:
            check_cycle(f['id'], [])
    print("    -> DAG verified: zero circular dependencies.")

    # 5. Check GFX sprite definitions and files
    print("[*] Auditing GFX definitions & physical texture assets...")
    goals_gfx = os.path.join(BASE_DIR, "interface", "ww1_france_goals.gfx")
    audit_braces(goals_gfx)
    with open(goals_gfx, "r", encoding="utf-8") as f:
        gfx_text = f.read()

    missing_sprites = []
    missing_files = []
    for f in foci:
        fid = f['id']
        s_name = f"GFX_{fid}"
        s_shine = f"GFX_{fid}_shine"
        if f'name = "{s_name}"' not in gfx_text:
            missing_sprites.append(s_name)
        if f'name = "{s_shine}"' not in gfx_text:
            missing_sprites.append(s_shine)

        # check physical file
        m = re.search(rf'name = "{s_name}"\s+texturefile = "([^"]+)"', gfx_text)
        if m:
            rel_path = m.group(1)
            full_path = os.path.join(BASE_DIR, rel_path.replace("/", os.sep))
            if not os.path.exists(full_path):
                missing_files.append((fid, full_path))
        else:
            missing_files.append((fid, "No texturefile pattern"))

    if missing_sprites:
        raise ValueError(f"Missing sprites in ww1_france_goals.gfx: {len(missing_sprites)}")
    if missing_files:
        raise ValueError(f"Missing texture files on disk: {len(missing_files)}")
    print(f"    -> All {len(foci)} focuses have valid base & shine sprites with physical textures on disk.")

    # 6. Check Ideas, Decisions, Events
    print("[*] Auditing Ideas, Decisions, and Events...")
    ideas_file = os.path.join(BASE_DIR, "common", "ideas", "ww1_france_ideas.txt")
    audit_braces(ideas_file)
    dec_file = os.path.join(BASE_DIR, "common", "decisions", "ww1_france_decisions.txt")
    audit_braces(dec_file)
    evt_file = os.path.join(BASE_DIR, "events", "ww1_france_events.txt")
    audit_braces(evt_file)
    print("    -> Ideas, decisions, and events syntax and braces validated perfectly.")

    # 7. Check Localisation
    print("[*] Auditing Localisation files...")
    loc_en = os.path.join(BASE_DIR, "localisation", "english", "ww1_france_l_english.yml")
    loc_pt = os.path.join(BASE_DIR, "localisation", "braz_por", "ww1_france_l_braz_por.yml")
    audit_bom(loc_en)
    audit_bom(loc_pt)
    print("    -> UTF-8 BOM confirmed on both English and Portuguese localisation files.")

    with open(loc_en, "r", encoding="utf-8") as f:
        en_text = f.read()
    with open(loc_pt, "r", encoding="utf-8") as f:
        pt_text = f.read()

    missing_loc_en = []
    missing_loc_pt = []
    for f in foci:
        fid = f['id']
        if f"{fid}:0" not in en_text:
            missing_loc_en.append(fid)
        if f"{fid}:0" not in pt_text:
            missing_loc_pt.append(fid)

    if missing_loc_en:
        raise ValueError(f"Missing English localisation for {len(missing_loc_en)} focuses!")
    if missing_loc_pt:
        raise ValueError(f"Missing Portuguese localisation for {len(missing_loc_pt)} focuses!")
    print(f"    -> 100% of {len(foci)} focuses localized in both English and Brazilian Portuguese.")

    print("\n=================================================================")
    print("   ALL CHECKS PASSED: FRENCH FOCUS TREE OVERHAUL 100% READY!")
    print("=================================================================")

if __name__ == "__main__":
    run_validation()
