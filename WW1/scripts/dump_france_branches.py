with open('common/national_focus/france.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
idx = 0
foci = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[idx:])
    if not m: break
    start = idx + m.end()
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == '{': depth += 1
        elif text[i] == '}': depth -= 1
        i += 1
    foci.append(text[start:i-1])
    idx = i

parsed = []
for b in foci:
    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
    x = int(re.search(r'^\s*x\s*=\s*(-?\d+)', b, re.M).group(1))
    y = int(re.search(r'^\s*y\s*=\s*(-?\d+)', b, re.M).group(1))
    rel = re.search(r'^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)', b, re.M)
    rel_id = rel.group(1) if rel else None
    prereqs = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
    mut = re.findall(r'mutually_exclusive\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
    cost = float(re.search(r'\bcost\s*=\s*([0-9.]+)', b).group(1)) if re.search(r'\bcost\s*=\s*([0-9.]+)', b) else 10.0
    rew = re.search(r'completion_reward\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', b)
    rew_text = rew.group(1).strip() if rew else ''
    parsed.append({
        'id': fid, 'x': x, 'y': y, 'rel': rel_id, 'prereqs': prereqs,
        'mut': mut, 'cost': cost, 'reward': rew_text
    })

coord = {}
for p in parsed:
    if not p['rel']: coord[p['id']] = (p['x'], p['y'])
for _ in range(10):
    for p in parsed:
        if p['rel'] and p['rel'] in coord:
            coord[p['id']] = (coord[p['rel']][0] + p['x'], coord[p['rel']][1] + p['y'])

for p in parsed:
    p['abs_x'], p['abs_y'] = coord.get(p['id'], (p['x'], p['y']))

print(f'Total parsed: {len(parsed)}')
groups = [
    ('POL', 0, 25),
    ('ECO', 26, 36),
    ('COL', 37, 48),
    ('NAV', 49, 60),
    ('AIR', 61, 72),
    ('MIL', 73, 105),
    ('DIP', 106, 140)
]

for g, xmin, xmax in groups:
    f_in_g = [p for p in parsed if xmin <= p['abs_x'] <= xmax]
    print(f'=== {g} ({len(f_in_g)} focuses) ===')
    for p in sorted(f_in_g, key=lambda x: (x['abs_y'], x['abs_x'])):
        print(f"  {p['id']:<45} (abs_x={p['abs_x']:>3}, abs_y={p['abs_y']:>2}, cost={p['cost']})")
