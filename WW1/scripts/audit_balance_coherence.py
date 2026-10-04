import os, re, glob

def parse_brackets(text):
    tokens = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '#':
            while i < n and text[i] != '\n':
                i += 1
            continue
        if text[i] in '{}=':
            tokens.append(text[i])
            i += 1
        elif text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 1
            tokens.append(text[i:j+1])
            i = j + 1
        elif not text[i].isspace():
            j = i
            while j < n and not text[j].isspace() and text[j] not in '{}=':
                j += 1
            tokens.append(text[i:j])
            i = j
        else:
            i += 1
    return tokens

# Let's inspect each major and minor country's OOB
majors = ['GER', 'SOV', 'FRA', 'ENG', 'AUS', 'ITA', 'USA', 'TUR', 'SER', 'BUL', 'BEL', 'ROM']

print("=== CHECKING DIVISION TEMPLATES AND COMPOSITION ===")
for tag in majors:
    path = f'history/units/{tag}_1936_generic.txt'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find division templates
    lines = content.splitlines()
    curr_template = None
    templates = {}
    in_regiments = False
    in_support = False
    
    for line in lines:
        line = line.split('#')[0].strip()
        m_tmpl = re.match(r'division_template\s*=\s*\{', line)
        if m_tmpl:
            curr_template = {}
            continue
        if curr_template is not None:
            m_name = re.search(r'name\s*=\s*"([^"]+)"', line)
            if m_name:
                curr_template['name'] = m_name.group(1)
                curr_template['regiments'] = []
                curr_template['support'] = []
            if 'regiments = {' in line:
                in_regiments = True
                continue
            if 'support = {' in line:
                in_support = True
                continue
            if in_regiments and '}' in line:
                in_regiments = False
            if in_support and '}' in line:
                in_support = False
            
            if in_regiments:
                sub = re.match(r'(\w+)\s*=\s*\{', line)
                if sub:
                    curr_template['regiments'].append(sub.group(1))
            if in_support:
                sub = re.match(r'(\w+)\s*=\s*\{', line)
                if sub:
                    curr_template['support'].append(sub.group(1))
            if line == '}' and not in_regiments and not in_support:
                if 'name' in curr_template:
                    templates[curr_template['name']] = curr_template
                curr_template = None

    div_count = len(re.findall(r'\bdivision\s*=', content))
    print(f"\n[{tag}] Total Divisions: {div_count}")
    for t_name, t_data in templates.items():
        regs = t_data['regiments']
        supp = t_data['support']
        # count occurrences
        from collections import Counter
        reg_counts = dict(Counter(regs))
        supp_counts = dict(Counter(supp))
        print(f"  * Template '{t_name}': {len(regs)} battalions {reg_counts} | support: {supp_counts}")
