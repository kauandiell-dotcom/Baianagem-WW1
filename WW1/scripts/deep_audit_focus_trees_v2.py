import re, glob, os

def parse_blocks(content, keyword):
    blocks = []
    idx = 0
    pattern = re.compile(r'\b' + keyword + r'\s*=\s*\{')
    while True:
        m = pattern.search(content, idx)
        if not m:
            break
        open_brace = content.find('{', m.start())
        depth = 1
        cur = open_brace + 1
        while cur < len(content) and depth > 0:
            if content[cur] == '{':
                depth += 1
            elif content[cur] == '}':
                depth -= 1
            cur += 1
        blocks.append(content[open_brace+1:cur-1])
        idx = cur
    return blocks

base_dir = '.' if os.path.exists('common') else 'WW1'

focus_files = [
    os.path.join(base_dir, 'common/national_focus/soviet.txt'),
    os.path.join(base_dir, 'common/national_focus/soviet_russia.txt'),
    os.path.join(base_dir, 'common/national_focus/white_russia.txt')
]

for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    blocks = parse_blocks(content, 'focus')
    print(f"\n==========================================")
    print(f"PARSING {ff}: Found {len(blocks)} focus blocks")
    print(f"==========================================")
    
    focus_ids = {}
    coords = {}
    prereqs = {}
    mut_excl = {}
    roots = []
    bypasses = {}
    available = {}

    for b in blocks:
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b)
        if not id_m: continue
        fid = id_m.group(1)
        focus_ids[fid] = b

        x_m = re.search(r'\bx\s*=\s*(-?\d+)', b)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', b)
        if x_m and y_m:
            coords[fid] = (int(x_m.group(1)), int(y_m.group(1)))

        # find all prerequisite blocks inside this focus
        p_blocks = parse_blocks(b, 'prerequisite')
        p_list = []
        for pb in p_blocks:
            for p in re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', pb):
                p_list.append(p)
        if p_list:
            prereqs[fid] = p_list
        else:
            roots.append(fid)

        # find all mutually_exclusive blocks
        m_blocks = parse_blocks(b, 'mutually_exclusive')
        m_list = []
        for mb in m_blocks:
            for m in re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', mb):
                m_list.append(m)
        if m_list:
            mut_excl[fid] = m_list

        av_blocks = parse_blocks(b, 'available')
        if av_blocks:
            available[fid] = av_blocks[0]

        by_blocks = parse_blocks(b, 'bypass')
        if by_blocks:
            bypasses[fid] = by_blocks[0]

    # Report roots
    print(f"Total Roots (Entry points): {len(roots)}")
    for r in roots:
        coord = coords.get(r, (0, 0))
        print(f"   Root: {r} at {coord}")

    # Check DAG
    missing_p = {}
    for fid, plist in prereqs.items():
        for p in plist:
            if p not in focus_ids:
                missing_p.setdefault(fid, []).append(p)
    if missing_p:
        print(f"CRITICAL ERROR: Dangling prerequisites: {missing_p}")
    else:
        print("DAG Prerequisites: 100% valid (0 broken links)!")

    # Check Mutually Exclusive
    missing_m = {}
    for fid, mlist in mut_excl.items():
        for m in mlist:
            if m not in focus_ids:
                missing_m.setdefault(fid, []).append(m)
    if missing_m:
        print(f"CRITICAL ERROR: Broken mutually exclusive: {missing_m}")
    else:
        print("Mutually Exclusive: 100% valid!")

    # Check collisions
    coord_map = {}
    collisions = []
    for fid, c in coords.items():
        if c in coord_map:
            collisions.append((fid, coord_map[c], c))
        coord_map[c] = fid
    if collisions:
        print(f"CRITICAL ERROR: Exact coordinate collisions: {collisions}")
    else:
        print("Exact coordinate collisions: 0!")
