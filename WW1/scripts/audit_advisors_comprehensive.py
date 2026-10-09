from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# 1. Load sprite registry
sprites = {}
for p in (ROOT / "interface").glob("*.gfx"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', txt):
        sprites[m.group(1)] = (m.group(2).replace("\\", "/"), p.name)

# 2. Load localisation keys
loc_en = {}
loc_pt = {}
for p in (ROOT / "localisation").glob("**/*.yml"):
    raw = p.read_bytes()
    txt = raw.decode("utf-8-sig", errors="ignore")
    is_pt = "braz_por" in p.name.lower()
    for line in txt.splitlines():
        m = re.match(r'^\s*([^\s:#]+):(?:\d*)\s*"(.*)"\s*$', line)
        if m:
            k, val = m.group(1), m.group(2)
            if is_pt:
                loc_pt[k] = val
            else:
                loc_en[k] = val

print(f"Loaded {len(sprites)} sprites, {len(loc_en)} EN keys, {len(loc_pt)} PT keys.")

# 3. Parse all individual characters inside characters = { ... }
characters = []
for p in sorted((ROOT / "common/characters").glob("*.txt")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    tag = p.stem
    
    # Strip comments
    clean_txt = re.sub(r'#.*', '', txt)
    
    # Find characters = { ... }
    m = re.search(r'characters\s*=\s*\{([\s\S]*)\}', clean_txt)
    if not m:
        continue
    body = m.group(1)
    
    # Tokenize by depth to extract each character block
    # A character is defined as: <char_id> = { ... } at depth 1
    depth = 0
    token_start = None
    curr_char_id = None
    
    # Simple brace depth parser
    i = 0
    n = len(body)
    while i < n:
        c = body[i]
        if c == '{':
            if depth == 0:
                # Find the identifier preceding this {
                prefix = body[token_start:i].strip()
                # prefix should be something like "AUS_franz_conrad = "
                m_id = re.search(r'([a-zA-Z0-9_]+)\s*=$', prefix)
                curr_char_id = m_id.group(1) if m_id else "UNKNOWN"
                block_start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and curr_char_id:
                char_body = body[block_start:i+1]
                
                name_m = re.search(r'\bname\s*=\s*(?:\"([^\"]+)\"|([a-zA-Z0-9_\.]+))', char_body)
                name_val = name_m.group(1) or name_m.group(2) if name_m else None
                
                is_advisor = bool(re.search(r'\b(advisor|corps_commander|field_marshal|navy_leader)\s*=\s*\{', char_body))
                slots = re.findall(r'\bslot\s*=\s*([a-zA-Z0-9_]+)', char_body)
                smalls = re.findall(r'\bsmall\s*=\s*(?:\"([^\"]+)\"|([a-zA-Z0-9_]+))', char_body)
                small_list = [s[0] or s[1] for s in smalls]
                
                characters.append({
                    'tag': tag,
                    'id': curr_char_id,
                    'name': name_val,
                    'is_advisor': is_advisor or bool(slots),
                    'slots': slots,
                    'smalls': small_list,
                    'file': p.name
                })
                curr_char_id = None
                token_start = i + 1
        elif depth == 0 and not body[i].isspace() and token_start is None:
            token_start = i
        i += 1

print(f"Total individual characters parsed: {len(characters)}")

advisors = [c for c in characters if c['is_advisor'] or c['slots']]
print(f"Total advisors/commanders: {len(advisors)}")

missing_loc = []
missing_gfx = []

for c in advisors:
    tag = c['tag']
    cid = c['id']
    cname = c['name']
    
    # Check name loc
    name_key = cname if (cname and not ' ' in cname) else cid
    has_en = (name_key in loc_en) or (cname and ' ' in cname)
    has_pt = (name_key in loc_pt) or (cname and ' ' in cname)
    
    if not (has_en and has_pt):
        missing_loc.append((tag, cid, cname, has_en, has_pt, c['slots']))
        
    # Check GFX
    if not c['smalls']:
        missing_gfx.append((tag, cid, "NO_SMALL_PORTRAIT", ""))
    else:
        for s in c['smalls']:
            if s in sprites:
                tex_rel, gfx_file = sprites[s]
                tex_path = ROOT / tex_rel
                if not tex_path.exists():
                    missing_gfx.append((tag, cid, "FILE_NOT_FOUND", f"{s} -> {tex_rel}"))
            else:
                # Check if it exists as a loose file
                if not (ROOT / s).exists() and not (ROOT / f"gfx/interface/ideas/{s}.dds").exists():
                    missing_gfx.append((tag, cid, "SPRITE_NOT_FOUND", s))

print(f"\nAdvisors missing loc: {len(missing_loc)}")
for x in missing_loc[:25]:
    print(f"  [{x[0]}] {x[1]} (name={x[2]}): EN={x[3]}, PT={x[4]}, slots={x[5]}")

print(f"\nAdvisors missing GFX: {len(missing_gfx)}")
for x in missing_gfx[:25]:
    print(f"  [{x[0]}] {x[1]}: {x[2]} ({x[3]})")

with open("advisors_audit_results.txt", "w", encoding="utf-8") as f:
    f.write(f"=== ADVISORS MISSING LOC ({len(missing_loc)}) ===\n")
    for x in missing_loc:
        f.write(f"[{x[0]}] {x[1]} (name={x[2]}): EN={x[3]}, PT={x[4]}, slots={x[5]}\n")
    f.write(f"\n=== ADVISORS MISSING GFX ({len(missing_gfx)}) ===\n")
    for x in missing_gfx:
        f.write(f"[{x[0]}] {x[1]}: {x[2]} ({x[3]})\n")
