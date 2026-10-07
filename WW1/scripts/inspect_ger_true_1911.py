import os, re

states_dir = 'history/states'
ger_states = []

for f in sorted(os.listdir(states_dir)):
    if f.endswith('.txt'):
        path = os.path.join(states_dir, f)
        txt = open(path, 'r', encoding='utf-8', errors='ignore').read()
        # Find base owner (before any 193x date)
        base_history = txt.split('193')[0] # cut before 1936/1938/1939
        m_owner = re.search(r'\bowner\s*=\s*([A-Z]{3})\b', base_history)
        if m_owner and m_owner.group(1) == 'GER':
            # find buildings in base history
            buildings_block = ''
            if 'buildings = {' in base_history:
                start = base_history.find('buildings = {')
                depth = 1
                i = start + len('buildings = {')
                while i < len(base_history) and depth > 0:
                    if base_history[i] == '{': depth += 1
                    elif base_history[i] == '}': depth -= 1
                    i += 1
                buildings_block = base_history[start:i]
            
            civ = sum(int(x) for x in re.findall(r'industrial_complex\s*=\s*(\d+)', buildings_block))
            mil = sum(int(x) for x in re.findall(r'arms_factory\s*=\s*(\d+)', buildings_block))
            dock = sum(int(x) for x in re.findall(r'dockyard\s*=\s*(\d+)', buildings_block))
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

print(f'Total GER 1911 base states: {len(ger_states)}')
total_civ = sum(s['civ'] for s in ger_states)
total_mil = sum(s['mil'] for s in ger_states)
total_dock = sum(s['dock'] for s in ger_states)
print(f'True 1911 GER totals: Civ={total_civ}, Mil={total_mil}, Dock={total_dock} => Total={total_civ + total_mil + total_dock}')
