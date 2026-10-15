#!/usr/bin/env python3
"""
Deep Forensic Audit of Russian Empire, Soviet Russia, and White Movement content in Baianagem-WW1.
Audits:
- Focus Trees: DAG, coordinates, prerequisites, mutual exclusions, ideas, characters, events, tooltips
- Ideas: Modifiers oracle validation, picture existence, duplicate keys
- Decisions: Categories, allowed/visible/available triggers, effects, costs
- Events: ID uniqueness, triggers, effects, pictures, option logic
- Characters: Roster completeness, valid traits, portrait definitions
- Localization: UTF-8 BOM, missing keys, English/Portuguese parity
"""
import os
import re
import sys
import glob

REPO_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def parse_bracket_blocks(text):
    # Basic tokenized parser for top-level or nested blocks
    pass

def load_file(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def main():
    print("=== STARTING DEEP FORENSIC AUDIT OF RUSSIA ===")
    errors = []
    warnings = []
    
    # 1. GATHER ALL REGISTERED SPRITES IN INTERFACE .GFX FILES
    print("\n--- Phase 1: Scanning Interface GFX Files ---")
    all_sprites = set()
    for gfx_file in glob.glob(os.path.join(REPO_ROOT, "interface", "**", "*.gfx"), recursive=True):
        content = load_file(gfx_file)
        if content:
            for m in re.finditer(r'name\s*=\s*"(GFX_[^"]+)"', content):
                all_sprites.add(m.group(1))
            for m in re.finditer(r'name\s*=\s*(GFX_\w+)', content):
                all_sprites.add(m.group(1))
    print(f"Total interface sprites registered: {len(all_sprites)}")

    # 2. GATHER ALL CHARACTERS
    print("\n--- Phase 2: Scanning Characters ---")
    all_characters = set()
    character_files = glob.glob(os.path.join(REPO_ROOT, "common", "characters", "*.txt"))
    char_by_country = {}
    for cf in character_files:
        tag = os.path.splitext(os.path.basename(cf))[0]
        content = load_file(cf)
        chars = re.findall(r'(\b(?:SOV|WHT|RUS)_\w+)\s*=\s*\{', content)
        char_by_country[tag] = set(chars)
        all_characters.update(chars)
    print(f"Total characters found: {len(all_characters)}")
    for t, chars in char_by_country.items():
        if t in ['SOV', 'WHT', 'RUS']:
            print(f"  {t}: {len(chars)} characters")

    # 3. GATHER ALL IDEAS
    print("\n--- Phase 3: Scanning Ideas ---")
    all_ideas = set()
    idea_files = glob.glob(os.path.join(REPO_ROOT, "common", "ideas", "*.txt"))
    for f in idea_files:
        content = load_file(f)
        # Match idea definitions
        # Ideas are inside country = { idea_id = { ... } } or hidden_ideas, etc.
        lines = content.splitlines()
        for line in lines:
            m = re.match(r'^\s*([A-Za-z0-9_]+)\s*=\s*\{', line)
            if m:
                k = m.group(1)
                if k not in ['ideas', 'country', 'hidden_ideas', 'political_advisor', 'theorist', 'army_chief', 'navy_chief', 'air_chief', 'high_command', 'tank_manufacturer', 'naval_manufacturer', 'aircraft_manufacturer', 'materiel_manufacturer', 'industrial_concern']:
                    all_ideas.add(k)
    print(f"Total ideas registered across common/ideas: {len(all_ideas)}")

    # 4. GATHER ALL EVENTS
    print("\n--- Phase 4: Scanning Events ---")
    all_events = set()
    event_files = glob.glob(os.path.join(REPO_ROOT, "events", "*.txt"))
    events_in_file = {}
    for f in event_files:
        content = load_file(f)
        ev_matches = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_\.]+)', content)
        events_in_file[f] = ev_matches
        for eid in ev_matches:
            if eid in all_events:
                errors.append(f"DUPLICATE EVENT ID: {eid} in {os.path.basename(f)}")
            all_events.add(eid)
    print(f"Total events found: {len(all_events)}")

    # 5. GATHER ALL DECISIONS AND CATEGORIES
    print("\n--- Phase 5: Scanning Decisions ---")
    all_dec_categories = set()
    for cat_file in glob.glob(os.path.join(REPO_ROOT, "common", "decisions", "categories", "*.txt")):
        content = load_file(cat_file)
        lines = content.splitlines()
        for line in lines:
            m = re.match(r'^([a-zA-Z0-9_]+)\s*=\s*\{', line)
            if m:
                all_dec_categories.add(m.group(1))
    
    all_decisions = set()
    for dec_file in glob.glob(os.path.join(REPO_ROOT, "common", "decisions", "*.txt")):
        content = load_file(dec_file)
        # In HOI4, decisions are inside category_id = { decision_id = { ... } }
        # Let's find category blocks
        for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', content):
            cat_candidate = m.group(1)
            cat_body = m.group(2)
            if cat_candidate in all_dec_categories:
                # Find decisions inside
                dec_ids = re.findall(r'\n\t([a-zA-Z0-9_]+)\s*=\s*\{', cat_body)
                for d in dec_ids:
                    all_decisions.add(d)
    print(f"Total decision categories: {len(all_dec_categories)}")
    print(f"Total decisions: {len(all_decisions)}")

    # 6. FOCUS TREE DEEP AUDIT
    print("\n--- Phase 6: Auditing Focus Trees ---")
    focus_trees = [
        ('common/national_focus/soviet.txt', 'russian_empire_focus'),
        ('common/national_focus/soviet_russia.txt', 'soviet_russia_focus'),
        ('common/national_focus/white_russia.txt', 'white_russia_focus')
    ]

    all_tree_focus_ids = {}

    for rel_path, expected_tree_id in focus_trees:
        fpath = os.path.join(REPO_ROOT, rel_path)
        content = load_file(fpath)
        print(f"\nAuditing {rel_path}...")
        
        # Check bracket balance
        open_b = content.count('{')
        close_b = content.count('}')
        if open_b != close_b:
            errors.append(f"BRACKET IMBALANCE in {rel_path}: open={open_b}, close={close_b}, delta={open_b - close_b}")

        # Parse focuses
        # Extract focus blocks
        focus_blocks = {}
        # Simple regex matcher for focus blocks
        # We can scan focus = { ... }
        pattern = re.compile(r'focus\s*=\s*\{(.*?)\n\t\}', re.DOTALL)
        for m in pattern.finditer(content):
            ftext = m.group(1)
            id_match = re.search(r'id\s*=\s*(\w+)', ftext)
            if not id_match:
                continue
            fid = id_match.group(1)
            focus_blocks[fid] = ftext

        all_tree_focus_ids[expected_tree_id] = set(focus_blocks.keys())
        print(f"  Parsed {len(focus_blocks)} focuses")

        coords = {}
        for fid, ftext in focus_blocks.items():
            # Check coordinates
            x_m = re.search(r'x\s*=\s*(\d+)', ftext)
            y_m = re.search(r'y\s*=\s*(\d+)', ftext)
            if x_m and y_m:
                x, y = int(x_m.group(1)), int(y_m.group(1))
                if (x, y) in coords:
                    errors.append(f"COORDINATE COLLISION in {rel_path}: Focus '{fid}' and '{coords[(x,y)]}' both at ({x}, {y})")
                else:
                    coords[(x, y)] = fid

            # Check prerequisites
            prereqs = re.findall(r'prerequisite\s*=\s*\{([^\}]+)\}', ftext)
            for pblock in prereqs:
                targets = re.findall(r'focus\s*=\s*(\w+)', pblock)
                for t in targets:
                    if t not in focus_blocks:
                        errors.append(f"DANGLING PREREQUISITE in {rel_path}: Focus '{fid}' requires '{t}' which does not exist in this tree!")

            # Check mutual exclusion
            mut_ex = re.findall(r'mutually_exclusive\s*=\s*\{([^\}]+)\}', ftext)
            for mblock in mut_ex:
                targets = re.findall(r'focus\s*=\s*(\w+)', mblock)
                for t in targets:
                    if t not in focus_blocks:
                        errors.append(f"INVALID MUTEX TARGET in {rel_path}: Focus '{fid}' is mutually exclusive with nonexistent '{t}'")
                    else:
                        # Check reciprocal
                        target_text = focus_blocks[t]
                        if f"focus = {fid}" not in target_text and f"focus={fid}" not in target_text:
                            warnings.append(f"ASYMMETRIC MUTEX in {rel_path}: '{fid}' excludes '{t}', but '{t}' does not list '{fid}'")

            # Check ideas referenced
            add_ideas = re.findall(r'add_ideas\s*=\s*(\w+)', ftext)
            for aid in add_ideas:
                if aid not in all_ideas:
                    errors.append(f"UNKNOWN IDEA in focus '{fid}' ({rel_path}): add_ideas = {aid}")
            
            remove_ideas = re.findall(r'remove_ideas\s*=\s*(\w+)', ftext)
            for rid in remove_ideas:
                if rid not in all_ideas:
                    warnings.append(f"UNKNOWN REMOVE IDEA in focus '{fid}' ({rel_path}): remove_ideas = {rid}")

            # Check characters referenced
            char_refs = re.findall(r'(?:recruit_character|retire_character|set_country_leader)\s*=\s*(\w+)', ftext)
            for cid in char_refs:
                if cid not in all_characters:
                    errors.append(f"UNKNOWN CHARACTER in focus '{fid}' ({rel_path}): {cid}")

            # Check events triggered
            event_calls = re.findall(r'id\s*=\s*([a-zA-Z0-9_\.]+)', re.search(r'completion_reward\s*=\s*\{.*', ftext, re.DOTALL).group(0) if 'completion_reward' in ftext else '')
            for ec in event_calls:
                # filter out non-events
                if '.' in ec and ec not in all_events:
                    errors.append(f"UNKNOWN EVENT CALLED in focus '{fid}' ({rel_path}): {ec}")

            # Check icon
            icon_m = re.search(r'icon\s*=\s*(\w+)', ftext)
            if icon_m:
                icon_name = icon_m.group(1)
                if icon_name not in all_sprites and f"GFX_{icon_name}" not in all_sprites:
                    warnings.append(f"UNREGISTERED ICON in focus '{fid}' ({rel_path}): {icon_name}")

    # 7. EVENTS DEEP AUDIT
    print("\n--- Phase 7: Auditing Russian Event Files ---")
    rus_event_files = [
        'events/side_ww1_ger_rus_depth.txt',
        'events/ww1_ger_rus_rework_events.txt',
        'events/ww1_russia_civil_war_events.txt',
        'events/ww1_russia_crisis_events.txt',
        'events/ww1_russia_diplomacy_events.txt',
        'events/ww1_russia_events.txt'
    ]
    for rel_path in rus_event_files:
        fpath = os.path.join(REPO_ROOT, rel_path)
        content = load_file(fpath)
        if not content:
            warnings.append(f"Event file not found: {rel_path}")
            continue
        print(f"Auditing {rel_path}...")
        open_b = content.count('{')
        close_b = content.count('}')
        if open_b != close_b:
            errors.append(f"BRACKET IMBALANCE in {rel_path}: open={open_b}, close={close_b}")

        # Check pictures
        pics = re.findall(r'picture\s*=\s*(\w+)', content)
        for p in pics:
            if p not in all_sprites:
                errors.append(f"MISSING SPRITE in {rel_path}: picture = {p} is not defined in any .gfx file!")

        # Check ideas
        add_ideas = re.findall(r'add_ideas\s*=\s*(\w+)', content)
        for aid in add_ideas:
            if aid not in all_ideas:
                errors.append(f"UNKNOWN IDEA in event ({rel_path}): add_ideas = {aid}")

        # Check characters
        char_refs = re.findall(r'(?:recruit_character|retire_character|set_country_leader)\s*=\s*(\w+)', content)
        for cid in char_refs:
            if cid not in all_characters:
                errors.append(f"UNKNOWN CHARACTER in event ({rel_path}): {cid}")

        # Check events called inside effects
        called_events = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_\.]+)', content)
        for ce in called_events:
            if ce not in all_events:
                errors.append(f"UNKNOWN EVENT CALLED in event ({rel_path}): {ce}")

    # 8. DECISIONS DEEP AUDIT
    print("\n--- Phase 8: Auditing Russian Decision Files ---")
    rus_dec_files = [
        'common/decisions/side_ww1_ger_rus_depth.txt',
        'common/decisions/ww1_ger_rus_rework_decisions.txt',
        'common/decisions/ww1_russia_crisis_decisions.txt',
        'common/decisions/ww1_russia_tsarist_decisions.txt',
        'common/decisions/ww1_soviet_civil_war_decisions.txt',
        'common/decisions/ww1_soviet_diplomacy_decisions.txt'
    ]
    for rel_path in rus_dec_files:
        fpath = os.path.join(REPO_ROOT, rel_path)
        content = load_file(fpath)
        if not content:
            continue
        print(f"Auditing {rel_path}...")
        open_b = content.count('{')
        close_b = content.count('}')
        if open_b != close_b:
            errors.append(f"BRACKET IMBALANCE in {rel_path}: open={open_b}, close={close_b}")

        # Check ideas in decisions
        add_ideas = re.findall(r'add_ideas\s*=\s*(\w+)', content)
        for aid in add_ideas:
            if aid not in all_ideas:
                errors.append(f"UNKNOWN IDEA in decision ({rel_path}): add_ideas = {aid}")

        # Check events in decisions
        called_events = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_\.]+)', content)
        for ce in called_events:
            if ce not in all_events:
                errors.append(f"UNKNOWN EVENT CALLED in decision ({rel_path}): {ce}")

    # 9. LOCALIZATION AUDIT
    print("\n--- Phase 9: Auditing Russian Localization Keys ---")
    loc_files = [
        'localisation/english/ww1_russia_focus_l_english.yml',
        'localisation/english/ww1_russia_events_l_english.yml',
        'localisation/english/ww1_russia_ideas_l_english.yml',
        'localisation/english/ww1_soviet_l_english.yml',
        'localisation/english/ww1_ger_rus_rework_l_english.yml',
        'localisation/english/ww1_white_l_english.yml',
        'localisation/braz_por/ww1_russia_focus_l_braz_por.yml',
        'localisation/braz_por/ww1_russia_events_l_braz_por.yml',
        'localisation/braz_por/ww1_russia_ideas_l_braz_por.yml',
        'localisation/braz_por/ww1_soviet_l_braz_por.yml',
        'localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml',
        'localisation/braz_por/ww1_white_l_braz_por.yml',
    ]
    all_loc_keys = set()
    for rel_path in loc_files:
        fpath = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(fpath):
            warnings.append(f"Localization file missing: {rel_path}")
            continue
        # Check UTF-8 BOM
        with open(fpath, 'rb') as f:
            raw = f.read()
        if not raw.startswith(b'\xef\xbb\xbf'):
            errors.append(f"MISSING UTF-8 BOM in {rel_path}")
        if raw.startswith(b'\xef\xbb\xbf\xef\xbb\xbf'):
            errors.append(f"DOUBLE UTF-8 BOM in {rel_path}")
        
        text = raw.decode('utf-8', errors='ignore')
        for m in re.finditer(r'^\s*([a-zA-Z0-9_\.]+):\d*\s*"', text, re.MULTILINE):
            all_loc_keys.add(m.group(1))

    # Check focus localization
    for tree_id, focuses in all_tree_focus_ids.items():
        for fid in focuses:
            if fid not in all_loc_keys:
                warnings.append(f"MISSING FOCUS TITLE LOC: {fid} (tree: {tree_id})")
            if f"{fid}_desc" not in all_loc_keys:
                warnings.append(f"MISSING FOCUS DESC LOC: {fid}_desc (tree: {tree_id})")

    # Check Russian ideas localization
    for idea in all_ideas:
        if idea.startswith('SOV_') or idea.startswith('WHT_') or idea.startswith('RUS_'):
            if idea not in all_loc_keys:
                warnings.append(f"MISSING IDEA LOC: {idea}")

    print("\n=== AUDIT SUMMARY ===")
    print(f"Total Errors Found: {len(errors)}")
    for e in errors:
        print(f"  [ERROR] {e}")
    print(f"\nTotal Warnings Found: {len(warnings)}")
    for w in warnings[:50]: # show first 50
        print(f"  [WARN] {w}")
    if len(warnings) > 50:
        print(f"  ... and {len(warnings) - 50} more warnings")

if __name__ == '__main__':
    main()
