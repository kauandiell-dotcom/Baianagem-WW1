import os
import re

local_dir = r'gfx/interface/goals'
ref_dir = r'E:/SteamLibrary/steamapps/workshop/content/394360/3106240385/gfx/interface/goals'

local_files = os.listdir(local_dir) if os.path.exists(local_dir) else []
ref_files = os.listdir(ref_dir) if os.path.exists(ref_dir) else []

with open('interface/ww1_russia_goals.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

army_sprites = re.findall(r'name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"gfx/interface/goals/focus_RUS_army\.png"', text)
unique_army = [s for s in army_sprites if not s.endswith('_shine')]
print(f'Total non-shine sprites pointing to focus_RUS_army.png: {len(unique_army)}')

all_available = {}
for f in local_files:
    all_available[f.lower()] = ('local', f)
for f in ref_files:
    if f.lower() not in all_available:
        all_available[f.lower()] = ('ref', f)

print(f'Total available files across local and ref: {len(all_available)}')

for s in unique_army:
    core_name = s.replace('GFX_focus_', '').replace('GFX_', '')
    tokens = core_name.lower().split('_')
    # search candidates
    candidates = []
    for fn_lower, (src, orig) in all_available.items():
        score = sum(1 for t in tokens if t in fn_lower)
        if score > 0:
            candidates.append((score, src, orig))
    candidates.sort(key=lambda x: -x[0])
    top_cands = [f"{c[2]} ({c[1]})" for c in candidates[:3]]
    print(f"{s} (tokens: {tokens}): {top_cands}")
