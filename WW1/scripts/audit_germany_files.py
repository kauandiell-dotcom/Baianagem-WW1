import os, re

files = [
    'common/national_focus/germany.txt',
    'events/ww1_germany_events.txt',
    'common/decisions/ww1_germany_decisions.txt',
    'common/ideas/ww1_germany_ideas.txt',
    'interface/ww1_germany_goals.gfx',
    'localisation/english/ww1_germany_l_english.yml',
    'localisation/braz_por/ww1_germany_l_braz_por.yml'
]

print('=== GERMAN MOD FILES AUDIT ===')
for f in files:
    if os.path.exists(f):
        size = os.path.getsize(f)
        raw = open(f, 'rb').read()
        has_bom = raw.startswith(b'\xef\xbb\xbf')
        lines = len(raw.decode('utf-8', errors='ignore').splitlines())
        print(f'{f}: {size} bytes, {lines} lines, BOM={has_bom}')
    else:
        print(f'{f}: NOT FOUND')
