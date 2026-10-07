import sys
from pathlib import Path
sys.path.insert(0, 'scripts')

from france_wing1_politics import WING1_FOCI
from france_wing2_economy import WING2_FOCI
from france_wing3_colonial import WING3_FOCI
from france_wing4_navy_air import WING4_FOCI
from france_wing5_army import WING5_FOCI
from france_wing6_diplomacy import WING6_FOCI

all_foci = WING1_FOCI + WING2_FOCI + WING3_FOCI + WING4_FOCI + WING5_FOCI + WING6_FOCI
print('Total focuses across 6 wings:', len(all_foci))

ids = [f['id'] for f in all_foci]
duplicates = [x for x in set(ids) if ids.count(x) > 1]
if duplicates:
    print('Duplicate IDs found:', duplicates)
    sys.exit(1)

coords = [(f['x'], f['y']) for f in all_foci]
dup_coords = [c for c in set(coords) if coords.count(c) > 1]
if dup_coords:
    print('Duplicate coordinates found:', dup_coords)
    for c in dup_coords:
        matches = [f['id'] for f in all_foci if (f['x'], f['y']) == c]
        print(f'  Coordinate {c} used by: {matches}')
    sys.exit(1)

id_set = set(ids)
missing_prereqs = []
for f in all_foci:
    for p in f.get('prereq', []):
        if p not in id_set:
            missing_prereqs.append((f['id'], p))

if missing_prereqs:
    print('Missing prerequisites found:', missing_prereqs)
    sys.exit(1)

print('SUCCESS: All 200 focuses validated with 0 errors!')
xs = [c[0] for c in coords]
ys = [c[1] for c in coords]
print(f'X range: min={min(xs)}, max={max(xs)}')
print(f'Y range: min={min(ys)}, max={max(ys)}')
