import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Read germany.txt outside wing 1
text = open(ROOT / 'common' / 'national_focus' / 'germany.txt', encoding='utf-8').read()
end_marker = '# WING 2: ECONOMY, LOGISTICS, RAW MATERIALS & FOOD'
pos = text.find(end_marker)
outside_icons = set(re.findall(r'icon\s*=\s*(\S+)', text[pos:]))

# All available normal sprites
all_sprites = set(open(ROOT / 'scripts' / 'all_normal_germany_sprites.txt', encoding='utf-8').read().splitlines())
available = sorted(all_sprites - outside_icons)

import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from ger_data_focuses import FOCUSES

used_in_wing1 = set()
new_assignments = {}

for f in FOCUSES:
    fid = f['id']
    curr_icon = f['icon']
    # If curr_icon is available and not yet used in wing 1, keep it!
    if curr_icon in available and curr_icon not in used_in_wing1:
        new_assignments[fid] = curr_icon
        used_in_wing1.add(curr_icon)
    else:
        # We need a new sprite from available
        new_assignments[fid] = None

# For those that need replacement, find the best thematic match from available
remaining_available = [s for s in available if s not in used_in_wing1]

keywords_map = {
    'volkerschlacht': ['völkerschlacht', 'leipzig', 'iron_cross', 'victory', 'monarch'],
    'sailors': ['sailor', 'marine', 'kiel', 'fleet', 'sea'],
    'spartakus': ['spartak', 'proletar', 'revolt', 'revolution', 'strike', 'red', 'marx'],
    'councils': ['spd', 'council', 'rate', 'social', 'workers'],
    'weimar': ['republic', 'reichstag', 'vote', 'reform', 'democracy', 'liberty'],
    'ohl': ['ohl', 'hindenburg', 'ludendorff', 'general', 'militar', 'army', 'ordnance'],
    'vaterland': ['vaterland', 'kapp', 'tirpitz', 'national', 'flag', 'siegfrieden'],
    'annex': ['annex', 'conquest', 'invade', 'strike', 'baltic', 'poland', 'belgium'],
}

for f in FOCUSES:
    fid = f['id']
    if new_assignments[fid] is None:
        # Search for a matching sprite in remaining_available
        # Try words in fid
        words = fid.lower().replace('ger_', '').split('_')
        best_candidate = None
        for cand in remaining_available:
            cand_l = cand.lower()
            if any(w in cand_l for w in words if len(w) > 3):
                best_candidate = cand
                break
        if not best_candidate:
            # Pick from remaining available that starts with GFX_focus_GER_ or GFX_GER_
            for cand in remaining_available:
                if cand.startswith('GFX_focus_GER_') or cand.startswith('GFX_GER_'):
                    best_candidate = cand
                    break
        if not best_candidate:
            best_candidate = remaining_available[0]

        new_assignments[fid] = best_candidate
        used_in_wing1.add(best_candidate)
        remaining_available.remove(best_candidate)

print(f"Total assigned focuses: {len(new_assignments)}")
print(f"Total unique icons assigned: {len(set(new_assignments.values()))}")
collision_with_outside = set(new_assignments.values()) & outside_icons
print(f"Collisions with outside wings: {len(collision_with_outside)}")

# Output the assignment dictionary code
with open(ROOT / 'scripts' / 'new_sprite_assignments.py', 'w', encoding='utf-8') as out:
    out.write("# -*- coding: utf-8 -*-\nNEW_SPRITES = {\n")
    for fid, sp in new_assignments.items():
        out.write(f"    '{fid}': '{sp}',\n")
    out.write("}\n")
print("Saved assignments to scripts/new_sprite_assignments.py")
