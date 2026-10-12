# scripts/build_eng_wings.py
import sys
sys.path.insert(0, '.')
from scripts.parsed_eng_focuses import ENG_FOCUSES

# Let's see the order of focuses in ENG_FOCUSES
for i, f in enumerate(ENG_FOCUSES):
    fid = f['id']
    x = f['x']
    y = f['y']
    print(f"{i+1:3d}: {fid:45s} | x={x:2d} | y={y:2d}")
