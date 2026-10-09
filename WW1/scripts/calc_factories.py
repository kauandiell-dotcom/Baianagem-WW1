import glob, re, os

tags = ['GER', 'ENG', 'FRA', 'SOV', 'RUS', 'AUS', 'ITA', 'TUR', 'USA', 'JAP']

stats = {t: {'civ': 0, 'mil': 0, 'dock': 0, 'states': 0} for t in tags}

def parse_blocks(text):
    """Parse key = { ... } blocks handling arbitrary nesting depth."""
    tokens = []
    i = 0
    n = len(text)
    while i < n:
        # Match word = {
        m = re.search(r'([a-zA-Z0-9_\.]+)\s*=\s*\{', text[i:])
        if not m:
            break
        key = m.group(1)
        start_brace = i + m.end() - 1
        # Find matching closing brace
        depth = 1
        j = start_brace + 1
        while j < n and depth > 0:
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
            j += 1
        body = text[start_brace + 1 : j - 1]
        tokens.append((key, body))
        i = j
    return tokens

state_files = glob.glob('history/states/*.txt')

for sf in state_files:
    with open(sf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Strip comments
    content_clean = re.sub(r'#[^\n]*', '', content)
    
    # Find state block
    state_blocks = parse_blocks(content_clean)
    for skey, sbody in state_blocks:
        if skey == 'state':
            # Inside state block, find history block
            for hkey, hbody in parse_blocks(sbody):
                if hkey == 'history':
                    # Get owner before any 1939 overrides
                    # Remove date blocks like 1939.1.1 = { ... }
                    date_blocks = parse_blocks(hbody)
                    base_hbody = hbody
                    for dkey, dbody in date_blocks:
                        if re.match(r'\d+\.\d+\.\d+', dkey):
                            # Remove this block from base_hbody
                            pass
                    
                    owner_m = re.search(r'\bowner\s*=\s*(\w+)', hbody)
                    if not owner_m:
                        continue
                    owner = owner_m.group(1)
                    
                    if owner in stats:
                        stats[owner]['states'] += 1
                        # Find buildings block in history
                        for bkey, bbody in parse_blocks(hbody):
                            if bkey == 'buildings':
                                # Now count industrial_complex, arms_factory, dockyard in this buildings block
                                # Note: ignore nested date blocks if any
                                civ_m = re.search(r'\bindustrial_complex\s*=\s*(\d+)', bbody)
                                mil_m = re.search(r'\barms_factory\s*=\s*(\d+)', bbody)
                                dock_m = re.search(r'\bdockyard\s*=\s*(\d+)', bbody)
                                
                                if civ_m:
                                    stats[owner]['civ'] += int(civ_m.group(1))
                                if mil_m:
                                    stats[owner]['mil'] += int(mil_m.group(1))
                                if dock_m:
                                    stats[owner]['dock'] += int(dock_m.group(1))
                                break # only the first (1911) buildings block!

# Check offsite buildings in history/countries/
offsite = {t: {'civ': 0, 'mil': 0, 'dock': 0} for t in tags}
for t in tags:
    cfs = glob.glob(f'history/countries/{t}*.txt')
    if cfs:
        with open(cfs[0], 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        offsite[t]['civ'] = sum(int(x) for x in re.findall(r'type\s*=\s*industrial_complex\s+level\s*=\s*(\d+)', c))
        offsite[t]['mil'] = sum(int(x) for x in re.findall(r'type\s*=\s*arms_factory\s+level\s*=\s*(\d+)', c))
        offsite[t]['dock'] = sum(int(x) for x in re.findall(r'type\s*=\s*dockyard\s+level\s*=\s*(\d+)', c))

print("="*75)
print(f"{'País (TAG)':<25} | {'Civis':<7} | {'Militares':<9} | {'Estaleiros':<10} | {'Total':<6}")
print("="*75)

# If SOV has states but RUS doesn't, or vice-versa
if stats['SOV']['states'] > 0 and stats['RUS']['states'] == 0:
    stats['RUS'] = stats['SOV']
    offsite['RUS'] = offsite['SOV']
    del stats['SOV']
elif stats['SOV']['states'] == 0 and stats['RUS']['states'] > 0:
    if 'SOV' in stats: del stats['SOV']

country_names = {
    'USA': 'Estados Unidos (USA)',
    'GER': 'Alemanha (GER)',
    'ENG': 'Reino Unido (ENG)',
    'FRA': 'França (FRA)',
    'RUS': 'Rússia (RUS/SOV)',
    'AUS': 'Áustria-Hungria (AUS)',
    'ITA': 'Itália (ITA)',
    'JAP': 'Japão (JAP)',
    'TUR': 'Império Otomano (TUR)'
}

# Sort by total factories descending
results = []
for t, s in stats.items():
    if s['states'] == 0:
        continue
    c = s['civ'] + offsite.get(t, {}).get('civ', 0)
    m = s['mil'] + offsite.get(t, {}).get('mil', 0)
    d = s['dock'] + offsite.get(t, {}).get('dock', 0)
    total = c + m + d
    results.append((total, t, c, m, d, s['states']))

results.sort(key=lambda x: x[0], reverse=True)

for total, t, c, m, d, st in results:
    name = country_names.get(t, t)
    off_str = ""
    if offsite.get(t, {}).get('civ', 0) or offsite.get(t, {}).get('mil', 0):
        off_str = f" [offsite: +{offsite[t]['civ']} civ, +{offsite[t]['mil']} mil]"
    print(f"{name:<25} | {c:<7} | {m:<9} | {d:<10} | {total:<6}{off_str}")

print("="*75)
