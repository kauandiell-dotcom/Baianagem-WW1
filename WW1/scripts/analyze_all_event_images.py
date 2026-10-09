import re
from pathlib import Path
from PIL import Image

sprites = {}
for gfx_file in Path('interface').glob('*.gfx'):
    txt = gfx_file.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', txt):
        sprites[m.group(1)] = (m.group(2).replace('\\', '/'), gfx_file)

events = []
for ev_file in Path('events').glob('*.txt'):
    txt = ev_file.read_text(encoding='utf-8', errors='ignore')
    # split by country_event or news_event
    tokens = re.split(r'\b(country_event|news_event)\s*=\s*\{', txt)
    for i in range(1, len(tokens), 2):
        ev_type = tokens[i]
        body = tokens[i+1]
        id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_\.]+)', body)
        pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_\.]+)', body)
        if id_m:
            ev_id = id_m.group(1)
            pic = pic_m.group(1) if pic_m else None
            events.append((ev_type, ev_id, pic, ev_file.name))

print(f"Total events found: {len(events)}")
country_evs = [e for e in events if e[0] == 'country_event']
news_evs = [e for e in events if e[0] == 'news_event']
print(f"Country events: {len(country_evs)}, News events: {len(news_evs)}")

# Map each unique texture file to whether it is used by country_event, news_event, or both
file_usage = {}
missing = []

for ev_type, ev_id, pic, fname in events:
    if not pic:
        continue
    if pic in sprites:
        tex_path, gfx_file = sprites[pic]
        p = Path(tex_path)
        if p.exists():
            file_usage.setdefault(p.resolve(), {'types': set(), 'events': [], 'path': p})['types'].add(ev_type)
            file_usage[p.resolve()]['events'].append((ev_type, ev_id, pic))
        else:
            missing.append((ev_type, ev_id, pic, tex_path, "FILE_NOT_FOUND"))
    else:
        # Check if it's vanilla or missing
        missing.append((ev_type, ev_id, pic, "", "SPRITE_NOT_FOUND"))

print(f"Total textures on disk in mod used by events: {len(file_usage)}")
print(f"Missing textures / sprites: {len(missing)}")

# Analyze dimensions
needs_country_resize = []
needs_news_resize = []
shared_conflicts = []
already_correct = []

for full_p, data in file_usage.items():
    p = data['path']
    types = data['types']
    try:
        im = Image.open(p)
        sz = im.size
    except Exception as e:
        print(f"Error opening {p}: {e}")
        continue
    
    if types == {'country_event'}:
        if sz == (210, 176):
            already_correct.append((p, sz, 'country'))
        else:
            needs_country_resize.append((p, sz, len(data['events'])))
    elif types == {'news_event'}:
        if sz == (397, 153):
            already_correct.append((p, sz, 'news'))
        else:
            needs_news_resize.append((p, sz, len(data['events'])))
    else:
        shared_conflicts.append((p, sz, data['events']))

print(f"\nAlready correct: {len(already_correct)}")
print(f"Country textures needing resize to (210, 176): {len(needs_country_resize)}")
for p, sz, c in needs_country_resize[:10]:
    print(f"  {p} ({sz}) -> used in {c} country events")

print(f"\nNews textures needing resize to (397, 153): {len(needs_news_resize)}")
for p, sz, c in needs_news_resize:
    print(f"  {p} ({sz}) -> used in {c} news events")

print(f"\nShared textures (used in both): {len(shared_conflicts)}")
for p, sz, evs in shared_conflicts:
    print(f"  {p} ({sz}) -> used in: {evs}")
