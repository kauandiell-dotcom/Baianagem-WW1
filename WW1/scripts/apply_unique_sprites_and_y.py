import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from ger_data_focuses import FOCUSES
from new_sprite_assignments import NEW_SPRITES

# Explicit override to ensure 100% GFX definitions exist
NEW_SPRITES['GER_kiel_sailors_revolt'] = 'GFX_focus_GER_navy'
NEW_SPRITES['GER_baltic_crusade_landeswehr'] = 'GFX_focus_GER_army_officer'

for f in FOCUSES:
    fid = f['id']
    f['icon'] = NEW_SPRITES[fid]
    if fid == 'GER_mittelafrika_total_empire':
        f['y'] = 13
    elif fid == 'GER_unconditional_victory_or_ruin':
        f['y'] = 14

# Rewrite ger_data_focuses.py with the updated data
with open(ROOT / 'scripts' / 'ger_data_focuses.py', 'w', encoding='utf-8') as out:
    out.write('# -*- coding: utf-8 -*-\n"""Focus definitions for Germany Politics & Society Wing (83 focuses)."""\n\nFOCUSES = [\n')
    for f in FOCUSES:
        out.write('    {\n')
        out.write(f"        'id': '{f['id']}',\n")
        out.write(f"        'x': {f['x']}, 'y': {f['y']}, 'cost': {f['cost']},\n")
        out.write(f"        'prereqs': {f['prereqs']},\n")
        out.write(f"        'mut_ex': {f['mut_ex']},\n")
        out.write(f"        'icon': '{f['icon']}',\n")
        out.write(f"        'filters': {f['filters']},\n")
        # Format reward
        reward_repr = f['reward'].strip().replace('\\', '\\\\')
        out.write(f"        'reward': '''{reward_repr}''',\n")
        out.write('    },\n')
    out.write(']\n')

print("Successfully updated scripts/ger_data_focuses.py with valid focus sprites and Y coordinates!")
