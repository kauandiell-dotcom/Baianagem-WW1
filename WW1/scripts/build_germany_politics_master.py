#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Master builder and compiler for the German Politics & Society rework."""

import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from ger_data_focuses import FOCUSES
from ger_data_events import EVENTS_TXT
from ger_data_ideas_decisions import IDEAS_TXT, CATEGORIES_TXT, DECISIONS_TXT
from ger_data_loc import ENGLISH_LOC, BRAZ_POR_LOC

def format_focus(f):
    lines = []
    lines.append('\tfocus = {')
    lines.append(f"\t\tid = {f['id']}")
    lines.append(f"\t\ticon = {f['icon']}")
    lines.append(f"\t\tcost = {f['cost']}")
    lines.append(f"\t\tx = {f['x']}")
    lines.append(f"\t\ty = {f['y']}")

    # Prerequisites
    for p in f['prereqs']:
        if isinstance(p, list):
            p_str = ' '.join(f'focus = {item}' for item in p)
            lines.append(f'\t\tprerequisite = {{ {p_str} }}')
        else:
            lines.append(f'\t\tprerequisite = {{ focus = {p} }}')

    # Mutually exclusive
    if f['mut_ex']:
        m_str = ' '.join(f'focus = {item}' for item in f['mut_ex'])
        lines.append(f'\t\tmutually_exclusive = {{ {m_str} }}')

    lines.append('\t\tavailable_if_capitulated = no')

    # Search filters
    if f['filters']:
        filters_str = ' '.join(f['filters'])
        lines.append(f'\t\tsearch_filters = {{ {filters_str} }}')

    # Completion reward
    lines.append('\t\tcompletion_reward = {')
    for r_line in f['reward'].strip().splitlines():
        lines.append(f'\t\t\t{r_line.strip()}')
    lines.append('\t\t}')
    lines.append('\t}')
    return '\n'.join(lines)


def build_focuses_block():
    blocks = []
    blocks.append('\t# =========================================================================')
    blocks.append('\t# REWORKED WING 1: POLITICS, SOCIETY & EXPANSION (83 FOCUSES, 4 LANES)')
    blocks.append('\t# =========================================================================\n')
    for f in FOCUSES:
        blocks.append(format_focus(f))
        blocks.append('')
    return '\n'.join(blocks)


def update_germany_focus_file():
    path = ROOT / 'common' / 'national_focus' / 'germany.txt'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find start marker
    start_marker = '# WING 1: INTERNAL POLITICS, REICHSTAG & POLITICAL PATHS'
    if start_marker not in content:
        start_marker = '# REWORKED WING 1: POLITICS, SOCIETY & EXPANSION'
    start_pos = content.find(start_marker)

    # Find end marker (start of Wing 2)
    end_marker = '# WING 2: ECONOMY, LOGISTICS, RAW MATERIALS & FOOD'
    end_pos = content.find(end_marker)

    if start_pos == -1 or end_pos == -1:
        raise ValueError(f"Could not locate wing markers in germany.txt (start={start_pos}, end={end_pos})")

    new_block = build_focuses_block()
    # Format replacement
    new_content = content[:start_pos] + new_block + '\n\n\t' + content[end_pos:]

    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(new_content)

    print(f"Updated {path}: replaced old wing 1 with {len(FOCUSES)} new focuses.")


def update_germany_events():
    path = ROOT / 'events' / 'ww1_germany_events.txt'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    marker = "# REWORKED POLITICS & EXPANSION EVENTS (ww1_germany_events.201 - 242)"
    if marker in content:
        content = content[:content.find(marker)].rstrip()

    content = content.rstrip() + '\n\n' + EVENTS_TXT.strip() + '\n'

    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)

    print(f"Updated {path}: appended 16 new events.")


def update_germany_ideas():
    path = ROOT / 'common' / 'ideas' / 'ww1_germany_ideas.txt'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    marker = "# REWORKED POLITICS & EXPANSION IDEAS"
    if marker in content:
        content = content[:content.find(marker)].rstrip()
        # Ensure it has the closing braces
        if not content.endswith('}'):
            content += '\n\t}\n}\n'
        elif not content.endswith('}\n}'):
            content += '\n}\n'

    content = content.rstrip()
    if content.endswith('}\n\t}\n}'):
        content = content[:-4]
    elif content.endswith('\t}\n}'):
        content = content[:-4]
    elif content.endswith('}\n}'):
        content = content[:-3]
    elif content.endswith('}'):
        content = content[:-1]

    new_content = content + '\n' + IDEAS_TXT.rstrip() + '\n\t}\n}\n'

    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(new_content)

    print(f"Updated {path}: inserted 16 new national ideas.")


def update_germany_decision_categories():
    path = ROOT / 'common' / 'decisions' / 'categories' / 'ww1_germany_categories.txt'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    marker = "GER_council_republic_revolution"
    if marker in content:
        content = content[:content.find(marker)].rstrip()

    content = content.rstrip() + '\n\n' + CATEGORIES_TXT.strip() + '\n'
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)
    print(f"Updated {path}: appended 4 new decision categories.")


def update_germany_decisions():
    path = ROOT / 'common' / 'decisions' / 'ww1_germany_decisions.txt'
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    marker = "# REWORKED GERMAN POLITICS & EXPANSION DECISIONS"
    if marker in content:
        content = content[:content.find(marker)].rstrip()

    content = content.rstrip() + '\n\n' + DECISIONS_TXT.strip() + '\n'

    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)

    print(f"Updated {path}: appended 12 new decisions.")


def update_localizations():
    # English
    en_path = ROOT / 'localisation' / 'english' / 'ww1_germany_focus_l_english.yml'
    with open(en_path, 'r', encoding='utf-8-sig') as file:
        en_content = file.read()

    en_marker = " # REWORKED POLITICS & EXPANSION WING (ENGLISH)"
    if en_marker in en_content:
        en_content = en_content[:en_content.find(en_marker)].rstrip()

    en_lines = [en_content.rstrip(), '\n' + en_marker]
    for k, v in ENGLISH_LOC.items():
        v_clean = v.replace('"', '\\"')
        en_lines.append(f' {k}: "{v_clean}"')

    with open(en_path, 'w', encoding='utf-8-sig', newline='\n') as file:
        file.write('\n'.join(en_lines) + '\n')
    print(f"Updated {en_path}: added {len(ENGLISH_LOC)} English strings.")

    # Brazilian Portuguese
    pt_path = ROOT / 'localisation' / 'braz_por' / 'ww1_germany_focus_l_braz_por.yml'
    with open(pt_path, 'r', encoding='utf-8-sig') as file:
        pt_content = file.read()

    pt_marker = " # REWORKED POLITICS & EXPANSION WING (BRAZ_POR)"
    if pt_marker in pt_content:
        pt_content = pt_content[:pt_content.find(pt_marker)].rstrip()

    pt_lines = [pt_content.rstrip(), '\n' + pt_marker]
    for k, v in BRAZ_POR_LOC.items():
        v_clean = v.replace('"', '\\"')
        pt_lines.append(f' {k}: "{v_clean}"')

    with open(pt_path, 'w', encoding='utf-8-sig', newline='\n') as file:
        file.write('\n'.join(pt_lines) + '\n')
    print(f"Updated {pt_path}: added {len(BRAZ_POR_LOC)} Brazilian Portuguese strings.")


if __name__ == '__main__':
    print("=== STARTING GERMANY POLITICS MASTER BUILD ===")
    update_germany_focus_file()
    update_germany_events()
    update_germany_ideas()
    update_germany_decision_categories()
    update_germany_decisions()
    update_localizations()
    print("=== MASTER BUILD COMPLETED SUCCESSFULLY ===")
