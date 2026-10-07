import re
import sys
from pathlib import Path

def analyze_focus_file(path_str):
    path = Path(path_str)
    txt = path.read_text(encoding='utf-8')
    
    # Simple parser to extract each focus block
    focuses = []
    # Find positions of focus = {
    matches = list(re.finditer(r'\bfocus\s*=\s*\{', txt))
    for i, m in enumerate(matches):
        start = m.end()
        # Find matching closing brace
        depth = 1
        idx = start
        while depth > 0 and idx < len(txt):
            ch = txt[idx]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            idx += 1
        block = txt[start:idx-1]
        focuses.append(block)

    print(f"\n==========================================")
    print(f"=== {path.name} (Total Foci: {len(focuses)}) ===")
    print(f"==========================================")
    
    no_reward = []
    only_shallow = []
    
    substantive_keywords = [
        'add_ideas', 'swap_ideas', 'remove_ideas', 'country_event', 'news_event',
        'add_building_construction', 'add_extra_state_shared_building_slots',
        'add_research_slot', 'add_tech_bonus',
        'declare_war_on', 'create_faction', 'add_to_faction', 'create_wargoal',
        'army_experience', 'air_experience', 'navy_experience', 'command_power',
        'add_stability', 'add_war_support', 'add_manpower', 'add_offsite_building',
        'start_civil_war', 'set_politics', 'annex_country', 'transfer_state',
        'add_equipment_to_stockpile', 'activate_targeted_decision', 'enable_decision'
    ]
    
    for f in focuses:
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', f)
        if not id_m:
            continue
        fid = id_m.group(1)
        
        rew_m = re.search(r'completion_reward\s*=\s*\{', f)
        if not rew_m:
            no_reward.append(fid)
            continue
        
        # Extract completion_reward block
        start = rew_m.end()
        depth = 1
        idx = start
        while depth > 0 and idx < len(f):
            ch = f[idx]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            idx += 1
        reward_block = f[start:idx-1].strip()
        
        # Clean comments
        reward_clean = re.sub(r'#.*', '', reward_block).strip()
        if not reward_clean:
            no_reward.append(fid)
            continue
            
        has_substantive = False
        for kw in substantive_keywords:
            if kw in reward_clean:
                has_substantive = True
                break
                
        if not has_substantive:
            only_shallow.append((fid, reward_clean))

    print(f"No completion_reward: {len(no_reward)}")
    for fid in no_reward:
        print(f"  [NO_REWARD] {fid}")
        
    print(f"Shallow (only flags/variables/raw PP): {len(only_shallow)}")
    for fid, content in only_shallow:
        one_line = ' '.join(content.split())
        print(f"  [SHALLOW] {fid} -> {one_line[:110]}")

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        analyze_focus_file(arg)
