import glob, re, os

for f in sorted(glob.glob('common/units/*.txt')):
    if '@' in f: 
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # parse each sub_unit block
    # find blocks inside sub_units = { ... }
    m_subunits = re.search(r'sub_units\s*=\s*\{([\s\S]+)\}', c)
    if not m_subunits:
        continue
    
    text = m_subunits.group(1)
    # find unit names: name = { ... }
    unit_matches = re.finditer(r'^\s*([a-zA-Z0-9_]+)\s*=\s*\{', text, re.MULTILINE)
    unit_starts = [(m.group(1), m.start()) for m in unit_matches]
    
    for i, (name, start) in enumerate(unit_starts):
        end = unit_starts[i+1][1] if i + 1 < len(unit_starts) else len(text)
        block = text[start:end]
        
        mp = re.search(r'manpower\s*=\s*(\d+)', block)
        org = re.search(r'max_organisation\s*=\s*(\d+)', block)
        hp = re.search(r'max_strength\s*=\s*([0-9.]+)', block)
        cw = re.search(r'combat_width\s*=\s*(\d+)', block)
        eq = re.search(r'need\s*=\s*\{([^}]+)\}', block)
        act = re.search(r'active\s*=\s*(\w+)', block)
        
        mp_val = mp.group(1) if mp else "N/A"
        org_val = org.group(1) if org else "N/A"
        hp_val = hp.group(1) if hp else "N/A"
        cw_val = cw.group(1) if cw else "N/A"
        eq_val = eq.group(1).strip().replace('\n', ' ') if eq else "N/A"
        act_val = act.group(1) if act else "yes"
        
        print(f"{os.path.basename(f):25} | {name:25} | MP: {mp_val:5} | Org: {org_val:3} | HP: {hp_val:4} | CW: {cw_val:2} | Act: {act_val:3} | Eq: {eq_val}")
