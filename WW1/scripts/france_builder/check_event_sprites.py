import os
import re

report_events = set()
for root, dirs, files in os.walk('interface'):
    for f in files:
        if f.endswith('.gfx'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as gf:
                content = gf.read()
                for m in re.finditer(r'name\s*=\s*"([^"]+)"', content):
                    sprite_name = m.group(1)
                    if 'event' in sprite_name.lower():
                        report_events.add(sprite_name)

print('Total event sprites found:', len(report_events))
with open('scripts/france_builder/event_sprites_list.txt', 'w', encoding='utf-8') as out:
    for s in sorted(report_events):
        out.write(s + '\n')
print('Wrote list to scripts/france_builder/event_sprites_list.txt')
