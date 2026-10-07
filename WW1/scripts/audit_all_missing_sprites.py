import re
from pathlib import Path

defined_sprites = set()
for p in Path('interface').glob('*.gfx'):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'name\s*=\s*"([^"]+)"', txt):
        defined_sprites.add(m.group(1))

# Collect all ideas in common/ideas/*.txt
all_ideas = {}
for p in Path('common/ideas').glob('*.txt'):
    itxt = p.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'(\b[a-zA-Z0-9_]+\b)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', itxt):
        iname, ibody = m.group(1), m.group(2)
        if iname in ('ideas', 'country', 'hidden_ideas'): continue
        if 'modifier' in ibody or 'allowed' in ibody or 'picture' in ibody:
            pic_m = re.search(r'\bpicture\s*=\s*([a-zA-Z0-9_]+)', ibody)
            pic = pic_m.group(1) if pic_m else iname
            all_ideas[iname] = (pic, p.name)

# Collect all added ideas across history and national focus
added_ideas = set()
for folder in ['history/countries', 'common/national_focus']:
    for p in Path(folder).glob('*.txt'):
        txt = p.read_text(encoding='utf-8', errors='ignore')
        for m in re.finditer(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', txt):
            added_ideas.add(m.group(1))

missing_by_file = {}
for iname in sorted(added_ideas):
    if iname in all_ideas:
        pic, source = all_ideas[iname]
        expected_sprite = pic if pic.startswith('GFX_') else f'GFX_idea_{pic}'
        if expected_sprite not in defined_sprites and pic not in defined_sprites:
            missing_by_file.setdefault(source, []).append((iname, pic, expected_sprite))

print(f'Total missing idea sprites across mod: {sum(len(v) for v in missing_by_file.values())}')
for source, items in missing_by_file.items():
    print(f'=== {source}: {len(items)} missing ===')
    for iname, pic, exp in items[:10]:
        print(f'   {iname} -> {exp}')
    if len(items) > 10:
        print(f'   ... and {len(items) - 10} more')
