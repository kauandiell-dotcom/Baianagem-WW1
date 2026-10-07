import os, re

# 1. GFX sprites
content = open('interface/ww1_germany_goals.gfx', encoding='utf-8', errors='ignore').read()
sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', content))
normal = sorted([s for s in sprites if not s.endswith('_shine')])
print(f'Total sprites in ww1_germany_goals.gfx: {len(sprites)}')
print(f'Normal sprites in ww1_germany_goals.gfx: {len(normal)}')

# Filter sprites that match left-wing/socialist/SPD/republic/councils/general strikes
left_sprites = [s for s in normal if any(k in s.lower() for k in [
    'spart', 'sozial', 'rot', 'red', 'streik', 'strike', 'rat', 'counc', 'arbeit',
    'volk', 'prolet', 'ebert', 'liebknecht', 'luxemburg', 'scheidemann', 'kpd',
    'uspd', 'spd', 'republ', 'demokrat', 'reichstag', 'frieden', 'peace'
])]
print(f'Left-wing / Republican themed sprites available in GFX: {len(left_sprites)}')
for s in left_sprites[:30]:
    print('  ', s)

# 2. Check existing events in events/ww1_germany_events.txt
events_content = open('events/ww1_germany_events.txt', encoding='utf-8', errors='ignore').read()
events = re.findall(r'id\s*=\s*([a-zA-Z0-9_\.]+)', events_content)
print(f'\nTotal events in ww1_germany_events.txt: {len(events)}')
left_events = [e for e in events if any(k in e for k in ['spart', 'strike', 'republic', 'soviet', 'social', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])]
print('Sample event IDs related to left path:', left_events[:20])
