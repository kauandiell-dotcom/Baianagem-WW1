import glob
import re
import os

# Collect all spriteTypes in interface/*.gfx
declared_sprites = set()
for fpath in glob.glob('interface/*.gfx'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    for m in re.finditer(r'name\s*=\s*"([^"]+)"', c):
        declared_sprites.add(m.group(1))

print(f"Total declared sprites in mod interface: {len(declared_sprites)}")

def parse_ideas_file(fpath):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Find ideas = { country = { ... } }
    # Let's count brace depth
    ideas = []
    i = 0
    depth = 0
    curr_id = None
    curr_pic = None
    stack = []
    
    # Simple tokenizer
    tokens = re.findall(r'([a-zA-Z0-9_\.]+|[{}])', content)
    idx = 0
    while idx < len(tokens):
        tok = tokens[idx]
        if tok == '{':
            depth += 1
            idx += 1
        elif tok == '}':
            depth -= 1
            idx += 1
        elif depth == 2: # inside country = { HERE }
            idea_name = tok
            if idx + 1 < len(tokens) and tokens[idx+1] == '=' and idx + 2 < len(tokens) and tokens[idx+2] == '{':
                # Parse idea body
                # find closing brace for this idea (when depth drops back to 2)
                sub_idx = idx + 3
                sub_depth = 3
                pic = None
                while sub_idx < len(tokens) and sub_depth > 2:
                    if tokens[sub_idx] == '{':
                        sub_depth += 1
                    elif tokens[sub_idx] == '}':
                        sub_depth -= 1
                    elif tokens[sub_idx] == 'picture' and sub_idx + 2 < len(tokens) and tokens[sub_idx+1] == '=':
                        pic = tokens[sub_idx+2]
                    sub_idx += 1
                ideas.append((idea_name, pic))
                idx = sub_idx
            else:
                idx += 1
        else:
            idx += 1
    return ideas

missing_by_file = {}
for fpath in glob.glob('common/ideas/*.txt'):
    fname = os.path.basename(fpath)
    ideas = parse_ideas_file(fpath)
    for iname, pic in ideas:
        has_sprite = False
        if pic:
            if pic in declared_sprites or ('GFX_idea_' + pic) in declared_sprites or ('GFX_' + pic) in declared_sprites:
                has_sprite = True
        else:
            if ('GFX_idea_' + iname) in declared_sprites or ('GFX_' + iname) in declared_sprites:
                has_sprite = True
        
        if not has_sprite:
            exp = 'GFX_idea_' + (pic if pic else iname)
            missing_by_file.setdefault(fname, []).append((iname, pic, exp))

for fname, mis in missing_by_file.items():
    print(f"\n{fname}: {len(mis)} ideas missing sprites:")
    for m in mis[:10]:
        print(f"   idea: {m[0]} | picture: {m[1]} -> expected: {m[2]}")
