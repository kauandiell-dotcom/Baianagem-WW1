import re, glob, os

base_dir = '.' if os.path.exists('common') else 'WW1'

focus_files = [
    os.path.join(base_dir, 'common/national_focus/soviet.txt'),
    os.path.join(base_dir, 'common/national_focus/soviet_russia.txt'),
    os.path.join(base_dir, 'common/national_focus/white_russia.txt')
]

# 1. Load all ideas defined in common/ideas/*.txt
defined_ideas = set()
for f in glob.glob(os.path.join(base_dir, 'common/ideas/*.txt')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    tokens = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{', txt)
    defined_ideas.update(tokens)

# 2. Load all characters defined in common/characters/*.txt
defined_chars = set()
for f in glob.glob(os.path.join(base_dir, 'common/characters/*.txt')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    chars = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{\s*name\s*=', txt)
    defined_chars.update(chars)

# 3. Load all sprite names in interface/*.gfx
defined_sprites = set()
for f in glob.glob(os.path.join(base_dir, 'interface/*.gfx')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    sprites = re.findall(r'name\s*=\s*"([^"]+)"', txt)
    defined_sprites.update(sprites)

print(f"Database loaded: {len(defined_ideas)} ideas, {len(defined_chars)} characters, {len(defined_sprites)} sprites.")

for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # parse focuses by regex
    focus_matches = re.finditer(r'\bfocus\s*=\s*\{', content)
    focus_starts = [m.start() for m in focus_matches]
    
    focus_ids = set()
    coords = {}
    prereqs = {}
    mut_excl = {}
    ideas_added = {}
    chars_recruited = {}
    leaders_set = {}
    icons = {}

    for i, start in enumerate(focus_starts):
        end = focus_starts[i+1] if i+1 < len(focus_starts) else len(content)
        chunk = content[start:end]

        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', chunk)
        if not id_m: continue
        fid = id_m.group(1)
        focus_ids.add(fid)

        x_m = re.search(r'\bx\s*=\s*(-?\d+)', chunk)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', chunk)
        if x_m and y_m:
            coords[fid] = (int(x_m.group(1)), int(y_m.group(1)))

        p_chunks = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', chunk)
        for pc in p_chunks:
            p_m = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pc)
            if p_m:
                prereqs.setdefault(fid, []).extend(p_m)

        m_chunks = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', chunk)
        for mc in m_chunks:
            m_m = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', mc)
            if m_m:
                mut_excl.setdefault(fid, []).extend(m_m)

        ia = re.findall(r'(?:add_ideas|add_timed_idea\s*=\s*\{\s*idea)\s*=\s*([a-zA-Z0-9_]+)', chunk)
        if ia:
            ideas_added[fid] = ia

        cr = re.findall(r'recruit_character\s*=\s*([a-zA-Z0-9_]+)', chunk)
        if cr:
            chars_recruited[fid] = cr
        ls = re.findall(r'set_country_leader\s*=\s*([a-zA-Z0-9_]+)', chunk)
        if ls:
            leaders_set[fid] = ls

        ic = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', chunk)
        if ic:
            icons[fid] = ic.group(1)

    print(f"\n==========================================")
    print(f"AUDITING {ff} ({len(focus_ids)} focuses)")
    print(f"==========================================")
    
    # 1. Check DAG
    missing_prereqs = {}
    for fid, plist in prereqs.items():
        for p in plist:
            if p not in focus_ids:
                missing_prereqs.setdefault(fid, []).append(p)
    if missing_prereqs:
        print(f"CRITICAL: Missing prerequisites: {missing_prereqs}")
    else:
        print("Prerequisites DAG: 100% valid!")

    # 2. Check Mutually Exclusive
    missing_mut = {}
    for fid, mlist in mut_excl.items():
        for m in mlist:
            if m not in focus_ids:
                missing_mut.setdefault(fid, []).append(m)
    if missing_mut:
        print(f"CRITICAL: Missing mutually exclusive: {missing_mut}")
    else:
        print("Mutually Exclusive: 100% valid!")

    # 3. Check Coordinate Collisions
    coord_map = {}
    collisions = []
    for fid, (x, y) in coords.items():
        if (x, y) in coord_map:
            collisions.append((fid, coord_map[(x, y)], (x, y)))
        coord_map[(x, y)] = fid
    if collisions:
        print(f"CRITICAL: Exact coordinate collisions: {collisions}")
    else:
        print("Exact coordinate collisions: 0!")

    # 4. Check Ideas
    missing_ideas = {}
    for fid, ilist in ideas_added.items():
        for i in ilist:
            if i not in defined_ideas:
                missing_ideas.setdefault(fid, []).append(i)
    if missing_ideas:
        print(f"Missing Ideas added: {missing_ideas}")
    else:
        print("Ideas added: 100% exist!")

    # 5. Check Characters
    missing_chars = {}
    for fid, clist in chars_recruited.items():
        for c in clist:
            if c not in defined_chars:
                missing_chars.setdefault(fid, []).append(c)
    for fid, llist in leaders_set.items():
        for l in llist:
            if l not in defined_chars:
                missing_chars.setdefault(fid, []).append(l)
    if missing_chars:
        print(f"Missing Characters referenced: {missing_chars}")
    else:
        print("Characters referenced: 100% exist!")

    # 6. Check Icons in GFX
    missing_icons = {}
    for fid, icon in icons.items():
        if icon not in defined_sprites:
            missing_icons[fid] = icon
    if missing_icons:
        print(f"Missing Sprite definitions in GFX: {len(missing_icons)} missing! Details:")
        for fid, ic in missing_icons.items():
            print(f"   {fid} -> {ic}")
    else:
        print("Icons: 100% registered in GFX!")
