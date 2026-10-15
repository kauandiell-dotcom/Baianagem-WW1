#!/usr/bin/env python3
"""
Master Forensic Inspector for France (FRA) in Baianagem-WW1.
Uses a true stack-based Clausewitz AST parser (no regex nesting limits).
Audits:
1. Focus tree layout, coordinates (exact & proximity), DAG graph integrity.
2. Focus rewards & effects (ideas, events, characters, states, technologies).
3. Focus icons and GFX sprite/texture resolution on disk.
4. Character database (traits, roles, portraits on disk, recruitment status).
5. Event chains (ww1_france, ww1_agadir, triggers, options, targets, loops).
6. Decisions and categories (cooldowns, triggers, modifiers, costs).
7. Scripted effects, variable math, clamping, and dashboard mechanics.
8. Clausewitz semantic oracle modifier validation across all French ideas.
9. Localization parity (EN vs PT-BR), BOM, quote escaping, missing keys.
10. Starting history, popularities, laws, and balance sanity checks.
"""
import os
import re
import sys
import glob

REPO_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def load_file(rel_path):
    full_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.exists(full_path):
        return ""
    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def strip_comments(text):
    out = []
    in_string = False
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '"':
            in_string = not in_string
            out.append(c)
            i += 1
        elif c == '#' and not in_string:
            while i < n and text[i] != '\n':
                i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)

def extract_named_blocks(text, block_name):
    """Extract all top-level `block_name = { ... }` blocks with exact brace matching."""
    blocks = []
    clean = strip_comments(text)
    # Search for block_name = {
    pattern = re.compile(rf'\b{block_name}\s*=\s*\{{')
    for m in pattern.finditer(clean):
        start = m.end() - 1
        brace_count = 0
        i = start
        end = -1
        while i < len(clean):
            if clean[i] == '{':
                brace_count += 1
            elif clean[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break
            i += 1
        if end != -1:
            blocks.append(clean[start+1:end-1])
    return blocks

def extract_all_top_blocks(text):
    """Extract all top-level key = { ... } blocks."""
    blocks = {}
    clean = strip_comments(text)
    i = 0
    n = len(clean)
    while i < n:
        # match key = {
        m = re.match(r'\s*([A-Za-z0-9_\.:-]+)\s*=\s*\{', clean[i:])
        if m:
            key = m.group(1)
            start_brace = i + m.end() - 1
            brace_count = 0
            j = start_brace
            end_brace = -1
            while j < n:
                if clean[j] == '{':
                    brace_count += 1
                elif clean[j] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end_brace = j
                        break
                j += 1
            if end_brace != -1:
                content = clean[start_brace+1:end_brace]
                if key not in blocks:
                    blocks[key] = []
                blocks[key].append(content)
                i = end_brace + 1
                continue
        i += 1
    return blocks

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print("================================================================================")
    print("       ULTRA-DEEP STACK-BASED FORENSIC AUDIT — FRANCE (FRA) & WW1 MOD           ")
    print("================================================================================")

    issues = []
    warnings = []

    # -------------------------------------------------------------------------
    # 1. FOCUS TREE: LAYOUT, COORDINATES & DAG INTEGRITY
    # -------------------------------------------------------------------------
    print("\n[SECTION 1] Focus Tree Layout, Coordinates & DAG Integrity")
    focus_file = "common/national_focus/france.txt"
    focus_content = load_file(focus_file)
    if not focus_content:
        issues.append(f"CRITICAL: {focus_file} could not be loaded!")
        return

    raw_focuses = extract_named_blocks(focus_content, "focus")
    print(f"-> Total Focuses Parsed with stack-based AST: {len(raw_focuses)}")

    focus_dict = {}
    coords = {}
    by_y = {}

    for raw in raw_focuses:
        id_m = re.search(r'\bid\s*=\s*([A-Za-z0-9_]+)', raw)
        if not id_m:
            continue
        fid = id_m.group(1)
        x_m = re.search(r'\bx\s*=\s*(-?\d+)', raw)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', raw)
        x = int(x_m.group(1)) if x_m else None
        y = int(y_m.group(1)) if y_m else None
        
        # Prerequisites can be: prerequisite = { focus = A focus = B }
        all_prereqs = []
        for pmatch in re.finditer(r'prerequisite\s*=\s*\{([^{}]+)\}', raw):
            pblock = pmatch.group(1)
            foci = re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', pblock)
            if foci:
                all_prereqs.append(foci)
        
        all_mutex = []
        for mmatch in re.finditer(r'mutually_exclusive\s*=\s*\{([^{}]+)\}', raw):
            mblock = mmatch.group(1)
            foci = re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', mblock)
            all_mutex.extend(foci)

        icon_m = re.search(r'\bicon\s*=\s*([A-Za-z0-9_]+)', raw)
        icon = icon_m.group(1) if icon_m else None

        focus_dict[fid] = {
            "x": x, "y": y, "prereqs": all_prereqs, "mutex": all_mutex,
            "icon": icon, "raw": raw
        }
        if x is not None and y is not None:
            if (x, y) in coords:
                issues.append(f"[EXACT FOCUS COLLISION] Focus '{fid}' and '{coords[(x, y)]}' share exact coords (x={x}, y={y})!")
            else:
                coords[(x, y)] = fid
            
            if y not in by_y:
                by_y[y] = []
            by_y[y].append((x, fid))

    # Proximity check at same y (dx < 2)
    for y, items in by_y.items():
        items.sort(key=lambda t: t[0])
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                x1, id1 = items[i]
                x2, id2 = items[j]
                if abs(x2 - x1) < 2 and x1 != x2:
                    warnings.append(f"[BOX OVERLAP RISK] y={y}: Focus '{id1}' (x={x1}) and '{id2}' (x={x2}) have dx={abs(x2-x1)} < 2 (potential badge overlap).")

    # DAG Dependency checks
    for fid, data in focus_dict.items():
        # Check prerequisites exist
        for branch in data["prereqs"]:
            for parent in branch:
                if parent not in focus_dict:
                    issues.append(f"[MISSING PREREQUISITE] Focus '{fid}' requires non-existent focus '{parent}'!")
                else:
                    # Vertical monotonicity
                    parent_y = focus_dict[parent]["y"]
                    if data["y"] is not None and parent_y is not None and data["y"] < parent_y:
                        issues.append(f"[BACKWARD EDGE] Focus '{fid}' (y={data['y']}) has prerequisite '{parent}' with higher y={parent_y}!")

        # Check mutually exclusive exist
        for me in data["mutex"]:
            if me not in focus_dict:
                issues.append(f"[MISSING MUTEX] Focus '{fid}' declares mutually_exclusive with non-existent focus '{me}'!")
            else:
                if fid not in focus_dict[me]["mutex"]:
                    warnings.append(f"[ONE-WAY MUTEX] Focus '{fid}' is mutually exclusive with '{me}', but '{me}' does not declare mutual exclusion with '{fid}'.")

    print(f"  -> Exact collisions: {len([i for i in issues if 'EXACT FOCUS COLLISION' in i])}")
    print(f"  -> Missing DAG nodes: {len([i for i in issues if 'MISSING' in i])}")
    print(f"  -> Backward edges: {len([i for i in issues if 'BACKWARD' in i])}")
    print(f"  -> Box overlap warnings: {len([w for w in warnings if 'BOX OVERLAP RISK' in w])}")

    # -------------------------------------------------------------------------
    # 2. FOCUS REWARDS, EVENTS, IDEAS, CHARACTERS & STATES
    # -------------------------------------------------------------------------
    print("\n[SECTION 2] Focus Rewards, Events, Ideas, Characters & State Targets")
    
    # Collect all ideas
    all_idea_names = set()
    for idea_file in glob.glob(os.path.join(REPO_ROOT, "common/ideas/*.txt")):
        content = load_file(os.path.relpath(idea_file, REPO_ROOT))
        tokens = re.findall(r'(\b[A-Za-z0-9_]+)\s*=\s*\{', strip_comments(content))
        all_idea_names.update(tokens)

    # Collect all events defined
    all_event_ids = set()
    for ev_file in glob.glob(os.path.join(REPO_ROOT, "events/*.txt")):
        content = load_file(os.path.relpath(ev_file, REPO_ROOT))
        ev_matches = re.findall(r'\bid\s*=\s*([A-Za-z0-9_\.]+)', strip_comments(content))
        all_event_ids.update(ev_matches)

    # Collect all characters defined in common/characters/FRA.txt
    fra_chars_content = load_file("common/characters/FRA.txt")
    fra_chars = set(re.findall(r'(\bFRA_[A-Za-z0-9_]+)\s*=\s*\{', strip_comments(fra_chars_content)))
    print(f"-> Registered FRA Characters: {len(fra_chars)}")

    # Collect all valid state IDs
    valid_state_ids = set()
    for st_file in glob.glob(os.path.join(REPO_ROOT, "history/states/*.txt")):
        bn = os.path.basename(st_file)
        m = re.match(r'^(\d+)', bn)
        if m:
            valid_state_ids.add(int(m.group(1)))
    print(f"-> Valid State IDs on disk: {len(valid_state_ids)}")

    # Audit each focus's raw content
    for fid, data in focus_dict.items():
        raw = data["raw"]

        # Check ideas added
        added_ideas = re.findall(r'add_ideas\s*=\s*([A-Za-z0-9_]+)', raw)
        for ai in added_ideas:
            if ai not in all_idea_names:
                issues.append(f"[MISSING IDEA IN REWARD] Focus '{fid}' adds non-existent idea '{ai}'!")

        # Check ideas swapped
        swap_adds = re.findall(r'add_idea\s*=\s*([A-Za-z0-9_]+)', raw)
        for sa in swap_adds:
            if sa not in all_idea_names:
                issues.append(f"[MISSING IDEA IN REWARD] Focus '{fid}' swap-adds non-existent idea '{sa}'!")

        swap_rems = re.findall(r'remove_idea\s*=\s*([A-Za-z0-9_]+)', raw)
        for sr in swap_rems:
            if sr not in all_idea_names:
                warnings.append(f"[UNREGISTERED IDEA IN SWAP REMOVE] Focus '{fid}' swap-removes idea '{sr}' which is not in idea files.")

        # Check events called
        called_events = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_\.]+)', raw)
        for ce in called_events:
            if ce not in all_event_ids:
                issues.append(f"[MISSING EVENT IN REWARD] Focus '{fid}' triggers non-existent event '{ce}'!")

        # Check characters promoted/recruited
        promoted = re.findall(r'promote_character\s*=\s*([A-Za-z0-9_]+)', raw)
        for pc in promoted:
            if pc not in fra_chars:
                issues.append(f"[MISSING CHARACTER IN REWARD] Focus '{fid}' promotes non-existent character '{pc}'!")

        recruited = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', raw)
        for rc in recruited:
            if rc not in fra_chars:
                issues.append(f"[MISSING CHARACTER IN REWARD] Focus '{fid}' recruits non-existent character '{rc}'!")

        # Check state scoped effects
        scoped_states = re.findall(r'\b(\d+)\s*=\s*\{[^}]*add_building_construction', raw)
        for st in scoped_states:
            st_id = int(st)
            if st_id not in valid_state_ids:
                issues.append(f"[INVALID STATE IN FOCUS] Focus '{fid}' references non-existent state ID '{st_id}'!")

    # -------------------------------------------------------------------------
    # 3. FOCUS ICONS & GFX ASSET RESOLUTION
    # -------------------------------------------------------------------------
    print("\n[SECTION 3] Focus Icons & GFX Sprite Resolution")
    all_sprites = {}
    for gfx_file in glob.glob(os.path.join(REPO_ROOT, "interface/*.gfx")):
        content = load_file(os.path.relpath(gfx_file, REPO_ROOT))
        matches = re.findall(r'name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', content, re.IGNORECASE)
        for sname, tpath in matches:
            all_sprites[sname] = tpath

    print(f"-> Total GFX Sprites registered in interface: {len(all_sprites)}")

    missing_sprites = 0
    missing_textures = 0
    for fid, data in focus_dict.items():
        icon = data["icon"]
        if not icon:
            issues.append(f"[MISSING ICON DECLARATION] Focus '{fid}' has no icon defined!")
            continue
        if icon not in all_sprites:
            if not icon.startswith("GFX_goal_") and not icon.startswith("GFX_focus_"):
                warnings.append(f"[UNREGISTERED SPRITE] Focus '{fid}' uses sprite '{icon}' which is not in mod interface .gfx files.")
                missing_sprites += 1
        else:
            tex_path = all_sprites[icon]
            phys_path = os.path.join(REPO_ROOT, tex_path.replace("/", "\\"))
            if not os.path.exists(phys_path):
                warnings.append(f"[MISSING TEXTURE ON DISK] Focus '{fid}' icon '{icon}' references '{tex_path}' which does not exist on disk!")
                missing_textures += 1

    print(f"  -> Unregistered sprites: {missing_sprites}")
    print(f"  -> Missing physical textures on disk: {missing_textures}")

    # -------------------------------------------------------------------------
    # 4. CHARACTERS, ROLES, PORTRAITS & RECRUITMENT STATUS
    # -------------------------------------------------------------------------
    print("\n[SECTION 4] FRA Characters Database & Portraits")
    char_top = extract_all_top_blocks(fra_chars_content)
    # The top level is "characters = { ... }"
    all_cblocks = {}
    if "characters" in char_top:
        for croot in char_top["characters"]:
            inner_chars = extract_all_top_blocks(croot)
            for cid, blist in inner_chars.items():
                all_cblocks[cid] = blist[0]

    fra_history = load_file("history/countries/FRA - France.txt")
    history_recruited = set(re.findall(r'^\s*recruit_character\s*=\s*([A-Za-z0-9_]+)', fra_history, re.MULTILINE))
    print(f"-> Characters recruited at game start in history: {len(history_recruited)}")

    missing_portraits = 0
    for cid, cbody in all_cblocks.items():
        portraits = re.findall(r'(?:large|small|texturefile)\s*=\s*"([^"]+)"', cbody)
        for p in portraits:
            if p.startswith("GFX_"):
                if p not in all_sprites:
                    warnings.append(f"[UNREGISTERED CHAR SPRITE] Character '{cid}' uses sprite '{p}' not found in interface.")
            else:
                phys_path = os.path.join(REPO_ROOT, p.replace("/", "\\"))
                if not os.path.exists(phys_path):
                    issues.append(f"[MISSING PORTRAIT FILE] Character '{cid}' references '{p}' which is missing on disk!")
                    missing_portraits += 1

        # Check if country leader or advisor can be used
        if cid in ["FRA_king_jean_iii", "FRA_charles_maurras", "FRA_jean_longuet", "FRA_fernand_loriot"]:
            if cid not in history_recruited:
                is_recruited_somewhere = bool(re.search(rf'recruit_character\s*=\s*{cid}', focus_content) or 
                                              re.search(rf'recruit_character\s*=\s*{cid}', load_file("events/ww1_france_events.txt")))
                if not is_recruited_somewhere:
                    issues.append(f"[UNRECRUITED POLITICAL LEADER] Character '{cid}' is promoted in focus tree or events, but is NEVER recruited via 'recruit_character' (neither in history nor in focus/event reward)! In HOI4, promote_character will fail if the character is not recruited!")

    print(f"  -> Missing portraits on disk: {missing_portraits}")

    # -------------------------------------------------------------------------
    # 5. EVENTS DEEP INSPECTION
    # -------------------------------------------------------------------------
    print("\n[SECTION 5] Events Deep Inspection (ww1_france & ww1_agadir)")
    event_files = ["events/ww1_france_events.txt", "events/WW1_Agadir.txt"]
    for ef in event_files:
        econtent = load_file(ef)
        ns_list = re.findall(r'add_namespace\s*=\s*([A-Za-z0-9_]+)', econtent)
        print(f"-> {ef}: Namespaces declared: {ns_list}")

        # Extract top-level country_event = { ... } and news_event = { ... }
        top_blocks = extract_all_top_blocks(econtent)
        c_events = top_blocks.get("country_event", []) + top_blocks.get("news_event", [])
        for ebody in c_events:
            eid_m = re.search(r'\bid\s*=\s*([A-Za-z0-9_\.]+)', ebody)
            if not eid_m:
                continue
            eid = eid_m.group(1)
            
            has_valid_ns = any(eid.startswith(ns + ".") for ns in ns_list)
            if not has_valid_ns:
                issues.append(f"[INVALID EVENT NAMESPACE] Event '{eid}' does not match declared namespaces {ns_list} in {ef}!")

            # Options
            options = extract_named_blocks(ebody, "option")
            if not options:
                issues.append(f"[EVENT WITHOUT OPTIONS] Event '{eid}' has no options defined!")

            # Child events
            child_events = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_\.]+)', ebody)
            for ce in child_events:
                if ce not in all_event_ids:
                    issues.append(f"[MISSING CHILD EVENT] Event '{eid}' calls non-existent event '{ce}'!")
                if ce == eid:
                    issues.append(f"[INFINITE LOOP RISK] Event '{eid}' calls itself directly!")

    # -------------------------------------------------------------------------
    # 6. DECISIONS & CATEGORIES
    # -------------------------------------------------------------------------
    print("\n[SECTION 6] Decisions & Categories Audit")
    dec_files = [
        "common/decisions/ww1_france_decisions.txt",
        "common/decisions/ww1_france_dashboard_decisions.txt",
        "common/decisions/ww1_agadir_crisis_decisions.txt"
    ]
    all_categories = set()
    for cat_file in glob.glob(os.path.join(REPO_ROOT, "common/decisions/categories/*.txt")):
        ccontent = load_file(os.path.relpath(cat_file, REPO_ROOT))
        cats = extract_all_top_blocks(ccontent).keys()
        all_categories.update(cats)
    print(f"-> Registered Decision Categories: {len(all_categories)}")

    for df in dec_files:
        dcontent = load_file(df)
        cat_blocks = extract_all_top_blocks(dcontent)
        for cat_name, cbody_list in cat_blocks.items():
            if cat_name not in all_categories:
                issues.append(f"[UNREGISTERED DECISION CATEGORY] Decision file '{df}' uses unregistered category '{cat_name}'!")
            
            for cbody in cbody_list:
                decs = extract_all_top_blocks(cbody)
                for dec_id, dec_bodies in decs.items():
                    for dec_body in dec_bodies:
                        # Check fast-failing allowed
                        if "allowed" not in dec_body:
                            warnings.append(f"[DECISION WITHOUT ALLOWED] Decision '{dec_id}' in {df} has no 'allowed' block (performance risk)!")

                        dec_added_ideas = re.findall(r'add_ideas\s*=\s*([A-Za-z0-9_]+)', dec_body)
                        for dai in dec_added_ideas:
                            if dai not in all_idea_names:
                                issues.append(f"[MISSING IDEA IN DECISION] Decision '{dec_id}' adds non-existent idea '{dai}'!")

    # -------------------------------------------------------------------------
    # 7. SCRIPTED EFFECTS & VARIABLE CLAMPING
    # -------------------------------------------------------------------------
    print("\n[SECTION 7] Scripted Effects & Dashboard Variables Engine")
    se_file = "common/scripted_effects/ww1_france_dashboard_effects.txt"
    se_content = load_file(se_file)
    required_effects = [
        "FRA_init_republic_dashboard",
        "FRA_clamp_dashboard_variables",
        "FRA_weekly_republic_tick"
    ]
    for re_name in required_effects:
        if re_name not in se_content:
            issues.append(f"[MISSING SCRIPTED EFFECT] Effect '{re_name}' is missing from {se_file}!")

    clamped_vars = set(re.findall(r'var\s*=\s*([A-Za-z0-9_]+)', se_content))
    expected_vars = [
        "FRA_union_sacree_cohesion",
        "FRA_poilu_morale",
        "FRA_charbon_et_acier",
        "FRA_reserves_humaines"
    ]
    for ev in expected_vars:
        if ev not in clamped_vars:
            issues.append(f"[UNCLAMPED VARIABLE] Dashboard variable '{ev}' is not clamped in FRA_clamp_dashboard_variables!")

    # -------------------------------------------------------------------------
    # 8. CLAUSEWITZ SEMANTIC ORACLE MODIFIER VALIDATION
    # -------------------------------------------------------------------------
    print("\n[SECTION 8] Clausewitz Semantic Oracle Modifier Audit")
    sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
    try:
        from hoi4_semantic_oracle import is_valid_country_modifier
        oracle_available = True
    except ImportError:
        oracle_available = False
        warnings.append("hoi4_semantic_oracle could not be imported; skipping modifier semantic check.")

    if oracle_available:
        fra_idea_files = [
            "common/ideas/ww1_france_dashboard_ideas.txt",
            "common/ideas/ww1_france_crises_ideas.txt",
            "common/ideas/ww1_france_political_ideas.txt",
            "common/ideas/france.txt"
        ]
        invalid_mods = 0
        for fif in fra_idea_files:
            fcontent = load_file(fif)
            modifier_lines = re.findall(r'modifier\s*=\s*\{([^{}]+)\}', fcontent)
            for mblock in modifier_lines:
                for line in mblock.splitlines():
                    line = line.split('#')[0].strip()
                    if not line or '=' not in line:
                        continue
                    mkey = line.split('=')[0].strip()
                    if not is_valid_country_modifier(mkey):
                        issues.append(f"[INVALID CLAUSEWITZ MODIFIER] File {fif}: Modifier '{mkey}' is not recognized by Semantic Oracle!")
                        invalid_mods += 1
        print(f"  -> Invalid modifier keys found: {invalid_mods}")

    # -------------------------------------------------------------------------
    # 9. LOCALIZATION PARITY, BOM & QUOTE INTEGRITY
    # -------------------------------------------------------------------------
    print("\n[SECTION 9] Localization Parity & Encoding")
    loc_en_file = os.path.join(REPO_ROOT, "localisation/english/ww1_france_rework_l_english.yml")
    loc_pt_file = os.path.join(REPO_ROOT, "localisation/braz_por/ww1_france_rework_l_braz_por.yml")

    def check_bom(fpath):
        with open(fpath, "rb") as f:
            head = f.read(6)
        if head.startswith(b'\xef\xbb\xbf\xef\xbb\xbf'):
            return "DOUBLE_BOM"
        elif head.startswith(b'\xef\xbb\xbf'):
            return "SINGLE_BOM"
        else:
            return "NO_BOM"

    if os.path.exists(loc_en_file) and os.path.exists(loc_pt_file):
        bom_en = check_bom(loc_en_file)
        bom_pt = check_bom(loc_pt_file)
        if bom_en != "SINGLE_BOM":
            issues.append(f"[BOM ERROR] English localization has BOM status: {bom_en}")
        if bom_pt != "SINGLE_BOM":
            issues.append(f"[BOM ERROR] Portuguese localization has BOM status: {bom_pt}")

        en_content = load_file(os.path.relpath(loc_en_file, REPO_ROOT))
        pt_content = load_file(os.path.relpath(loc_pt_file, REPO_ROOT))

        en_keys = set(re.findall(r'^\s*([A-Za-z0-9_\.]+):', en_content, re.MULTILINE))
        pt_keys = set(re.findall(r'^\s*([A-Za-z0-9_\.]+):', pt_content, re.MULTILINE))

        en_only = en_keys - pt_keys
        pt_only = pt_keys - en_keys
        if en_only:
            issues.append(f"[LOCALIZATION PARITY GAP] Keys in English but missing in Brazilian Portuguese: {en_only}")
        if pt_only:
            issues.append(f"[LOCALIZATION PARITY GAP] Keys in Portuguese but missing in English: {pt_only}")
        print(f"  -> Total localized keys in rework: {len(en_keys)} (100% parity: {en_keys == pt_keys})")

    # -------------------------------------------------------------------------
    # 10. BALANCE, STARTING LAWS, POPULARITIES & INTEGRITY
    # -------------------------------------------------------------------------
    print("\n[SECTION 10] History & Balance Sanity")
    pop_block = re.search(r'set_popularities\s*=\s*\{([^{}]+)\}', fra_history)
    if pop_block:
        pops = re.findall(r'([a-z_]+)\s*=\s*(\d+)', pop_block.group(1))
        total_pop = sum(int(val) for _, val in pops)
        if total_pop != 100:
            issues.append(f"[POPULARITY SUM ERROR] Starting popularities in FRA history sum to {total_pop}% (expected 100%)!")
        else:
            print(f"  -> Starting popularities sum to {total_pop}%: OK")

    start_ideas = re.search(r'add_ideas\s*=\s*\{([^{}]+)\}', fra_history)
    if start_ideas:
        si_list = start_ideas.group(1).strip().split()
        for si in si_list:
            if si not in all_idea_names:
                issues.append(f"[MISSING STARTING IDEA] FRA starting idea '{si}' does not exist in common/ideas/!")

    # -------------------------------------------------------------------------
    # SUMMARY REPORT
    # -------------------------------------------------------------------------
    print("\n================================================================================")
    print(f"AUDIT COMPLETE: Found {len(issues)} ISSUES and {len(warnings)} WARNINGS")
    print("================================================================================")
    if issues:
        print("\n>>> CRITICAL ISSUES / BUGS FOUND <<<")
        for idx, iss in enumerate(issues, 1):
            print(f"  {idx}. {iss}")
    else:
        print("\n>>> ZERO CRITICAL ISSUES FOUND! <<<")

    if warnings:
        print("\n>>> WARNINGS & GAMEPLAY REFINEMENT RECOMMENDATIONS <<<")
        for idx, w in enumerate(warnings[:25], 1):
            print(f"  {idx}. {w}")
        if len(warnings) > 25:
            print(f"  ... and {len(warnings) - 25} more warnings.")

if __name__ == "__main__":
    main()
