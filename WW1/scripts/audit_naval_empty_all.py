import glob
import re

all_files = glob.glob('history/**/*.txt', recursive=True)
empty_count = 0
for f in all_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    # find create_equipment_variant
    blocks = re.findall(r'create_equipment_variant\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', content)
    empty_in_f = []
    for b in blocks:
        if 'ww1_1911_' in b or 'ww1_1917_' in b or 'ww1_1922_' in b:
            if 'modules' not in b:
                m_type = re.search(r'type\s*=\s*(\w+)', b)
                m_name = re.search(r'name\s*=\s*"([^"]+)"', b)
                t_str = m_type.group(1) if m_type else 'unknown'
                if not t_str.endswith('_legacy'):
                    empty_in_f.append((m_name.group(1) if m_name else '?', t_str))
    if empty_in_f:
        print(f"{f}: {len(empty_in_f)} empty variants")
        empty_count += len(empty_in_f)
print(f"Total empty variants across all files: {empty_count}")
