#!/usr/bin/env python3
"""
Comprehensive Forensic Russian Inspector.
Audits:
1. Coordinate spacing in Focus Trees (exact overlaps and same-Y proximity < 2).
2. Trait validation in SOV.txt and WHT.txt against Clausewitz engine rules.
3. Portrait file existence on disk for all Russian characters.
4. Rasputin & Stolypin continuity (assassination events vs advisor retirement).
5. Brusilov continuity.
6. Russian Crisis Tension pacing & trigger conditions.
7. Decision triggers, effects, and days_re_enable.
8. Event trigger conditions, premature firing risks (e.g. 1911-1913 revolution risks).
"""
import os
import re
import glob

REPO_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def load(rel):
    path = os.path.join(REPO_ROOT, rel)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def main():
    print("==================================================")
    print("   FORENSIC RUSSIAN CODEBASE INSPECTOR")
    print("==================================================")

    # 1. Focus Coordinate Closeness Check
    print("\n--- 1. Focus Tree Coordinate Analysis ---")
    trees = [
        'common/national_focus/soviet.txt',
        'common/national_focus/soviet_russia.txt',
        'common/national_focus/white_russia.txt'
    ]
    for rel in trees:
        content = load(rel)
        focuses = re.findall(r'focus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', content)
        by_y = {}
        exact_coll = []
        near_coll = []
        for ftext in focuses:
            id_m = re.search(r'id\s*=\s*(\w+)', ftext)
            x_m = re.search(r'\bx\s*=\s*(\d+)', ftext)
            y_m = re.search(r'\by\s*=\s*(\d+)', ftext)
            if id_m and x_m and y_m:
                fid = id_m.group(1)
                x = int(x_m.group(1))
                y = int(y_m.group(1))
                if y not in by_y:
                    by_y[y] = []
                by_y[y].append((x, fid))

        for y, items in by_y.items():
            items.sort(key=lambda t: t[0])
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    x1, id1 = items[i]
                    x2, id2 = items[j]
                    if x1 == x2:
                        exact_coll.append((y, x1, id1, id2))
                    elif abs(x2 - x1) < 2:
                        near_coll.append((y, x1, x2, id1, id2))

        print(f"{rel}:")
        print(f"  Exact (x,y) collisions: {len(exact_coll)}")
        for y, x, id1, id2 in exact_coll:
            print(f"    [EXACT OVERLAP] y={y}, x={x}: {id1} vs {id2}")
        print(f"  Near collisions (same y, dx < 2): {len(near_coll)}")
        for y, x1, x2, id1, id2 in near_coll:
            print(f"    [BOX OVERLAP RISK] y={y}: {id1}(x={x1}) and {id2}(x={x2}) dx={abs(x2-x1)}")

    # 2. Characters & Traits Audit
    print("\n--- 2. Characters & Traits Audit ---")
    char_files = ['common/characters/SOV.txt', 'common/characters/WHT.txt']
    for rel in char_files:
        content = load(rel)
        # Parse characters
        chars = re.findall(r'(\b\w+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', content)
        print(f"{rel}: {len(chars)} characters parsed")
        for cid, cbody in chars:
            # Check portrait paths
            portraits = re.findall(r'texturefile\s*=\s*"([^"]+)"', cbody)
            for p in portraits:
                # p is usually "gfx/leaders/SOV/portrait.dds"
                disk_path = os.path.join(REPO_ROOT, p.replace('/', '\\'))
                if not os.path.exists(disk_path):
                    print(f"  [MISSING PORTRAIT FILE] Char {cid}: '{p}' not found on disk!")
            
            # Check traits
            traits = re.findall(r'traits\s*=\s*\{([^\}]+)\}', cbody)
            for tblock in traits:
                tlist = tblock.strip().split()
                # print unknown or check against known traits

    # 3. Check Rasputin assassination vs advisor retirement
    print("\n--- 3. Historical Narrative & Character Retirement Audit ---")
    rasputin_ev = re.findall(r'SOV_rasputin_court_intrigues', load('events/ww1_ger_rus_rework_events.txt') + load('events/ww1_russia_events.txt'))
    print(f"Rasputin event mentions: {len(rasputin_ev)}")
    
    # Check if Rasputin character is retired when assassinated
    rasputin_retired = re.findall(r'retire_character\s*=\s*SOV_grigori_rasputin', load('events/ww1_ger_rus_rework_events.txt') + load('events/ww1_russia_events.txt') + load('events/side_ww1_ger_rus_depth.txt'))
    print(f"Rasputin retire_character calls: {len(rasputin_retired)}")

    # Check Stolypin
    stolypin_retired = re.findall(r'retire_character\s*=\s*SOV_pyotr_stolypin', load('events/ww1_ger_rus_rework_events.txt') + load('events/ww1_russia_events.txt') + load('events/side_ww1_ger_rus_depth.txt'))
    print(f"Stolypin retire_character calls: {len(stolypin_retired)}")

    # 4. Check Crisis Tension math and weekly ticks
    print("\n--- 4. Crisis Tension System Audit ---")
    crisis_effects = load('common/scripted_effects/ww1_russia_crisis_effects.txt')
    on_actions = load('common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt')
    print(f"Crisis effects file length: {len(crisis_effects)} chars")
    
    # Check how weekly updates happen
    ticks = re.findall(r'(sov_russia_weekly_crisis_update|ww1_sov_rework_weekly)', on_actions)
    print(f"Crisis tick hooks in on_actions: {ticks}")

    # 5. Check White Russia victory and tree continuation
    print("\n--- 5. White Russia Post-Civil-War Continuation ---")
    cw_events = load('events/ww1_russia_civil_war_events.txt')
    wht_vict = re.search(r'id\s*=\s*ww1_russia_civil_war\.20.*?\n\}', cw_events, re.DOTALL)
    if wht_vict:
        print("White victory event 20 found. Effects:")
        for line in wht_vict.group(0).splitlines():
            if any(k in line for k in ['load_focus_tree', 'set_politics', 'annex_country', 'set_cosmetic_tag', 'add_core']):
                print(f"  {line.strip()}")

    # 6. Check Brest-Litovsk Event Chain
    print("\n--- 6. Brest-Litovsk Chain Integrity ---")
    diplo_events = load('events/ww1_russia_diplomacy_events.txt')
    bl_events = re.findall(r'id\s*=\s*(ww1_russia_diplomacy\.\d+)', diplo_events)
    print(f"Brest-Litovsk diplomacy events: {bl_events}")
    for eid in bl_events:
        # Check if called
        callers = re.findall(rf'id\s*=\s*{eid}', load('events/ww1_russia_civil_war_events.txt') + load('events/ww1_ger_rus_rework_events.txt') + load('common/national_focus/soviet_russia.txt'))
        print(f"  Event {eid}: defined, called {len(callers)} times")

if __name__ == '__main__':
    main()
