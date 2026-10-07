import os, re

states_dir = 'history/states'
ger_states = []

for f in sorted(os.listdir(states_dir)):
    if f.endswith('.txt'):
        path = os.path.join(states_dir, f)
        txt = open(path, 'r', encoding='utf-8', errors='ignore').read()
        if 'owner = GER' in txt:
            civ = sum(int(x) for x in re.findall(r'industrial_complex\s*=\s*(\d+)', txt))
            mil = sum(int(x) for x in re.findall(r'arms_factory\s*=\s*(\d+)', txt))
            dock = sum(int(x) for x in re.findall(r'dockyard\s*=\s*(\d+)', txt))
            name_m = re.search(r'name\s*=\s*"([^"]+)"', txt)
            sname = name_m.group(1) if name_m else f
            state_id = re.search(r'id\s*=\s*(\d+)', txt).group(1)
            ger_states.append({
                'file': f,
                'id': state_id,
                'name': sname,
                'civ': civ,
                'mil': mil,
                'dock': dock,
                'total': civ + mil + dock
            })

print(f'Total GER states: {len(ger_states)}')
total_civ = sum(s['civ'] for s in ger_states)
total_mil = sum(s['mil'] for s in ger_states)
total_dock = sum(s['dock'] for s in ger_states)
print(f'Current GER totals: Civ={total_civ}, Mil={total_mil}, Dock={total_dock} => Total={total_civ + total_mil + total_dock}')

print('\nTop industrial states for Germany:')
for s in sorted(ger_states, key=lambda x: x['total'], reverse=True)[:15]:
    print(f'  State {s["id"]} ({s["name"]} - {s["file"]}): Civ={s["civ"]}, Mil={s["mil"]}, Dock={s["dock"]} -> {s["total"]}')
