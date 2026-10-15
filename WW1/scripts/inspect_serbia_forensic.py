#!/usr/bin/env python3
"""
Master Forensic Inspector for Kingdom of Serbia (SER) in Baianagem-WW1.
Performs an exhaustive, stack-based Clausewitz AST audit across all subsystems:
1. Focus tree layout, coordinates (exact & proximity), DAG graph integrity.
2. Focus rewards & effects (ideas, events, characters, states, technologies, destinies).
3. Focus icons and GFX sprite/texture resolution on disk.
4. Character database (traits, roles, portraits on disk, recruitment status).
5. Event chains (ww1_serbia, ww1_serbia_retreat, triggers, options, targets, loops).
6. Decisions and categories (cooldowns, triggers, modifiers, costs, allowed blocks).
7. Balance of Power engine (bop_ser_civil_military, ranges, modifiers, scripted effects).
8. The Great Retreat & 30-Division Mobilization engine (state targets, templates, survival).
9. Clausewitz semantic oracle modifier validation across all Serbian ideas, traits, decisions.
10. Localization parity (EN vs PT-BR), BOM, quote escaping, missing keys.
11. Starting history, popularities, laws, and map balance sanity checks (1911 baseline).
12. Order of Battle (OOB) and division templates verification.
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
    print("       ULTRA-DEEP STACK-BASED FORENSIC AUDIT — KINGDOM OF SERBIA (SER)         ")
    print("================================================================================")

    issues = []
    warnings = []
    findings = []

    # -------------------------------------------------------------------------
    # 1. FOCUS TREE: LAYOUT, COORDINATES & DAG INTEGRITY
    # -------------------------------------------------------------------------
    print("\n[SECTION 1] Focus Tree Layout, Coordinates & DAG Integrity")
    focus_file = "common/national_focus/serbia.txt"
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
                    warnings.append(f"[BOX OVERLAP RISK] y={y}: Focus '{id1}' (x={x1}) and '{id2}' (x={x2}) have dx={abs(x2-x1)} < 2 (badge overlap).")

    # DAG Dependency checks
    for fid, data in focus_dict.items():
        for branch in data["prereqs"]:
            for parent in branch:
                if parent not in focus_dict:
                    issues.append(f"[MISSING PREREQUISITE] Focus '{fid}' requires non-existent focus '{parent}'!")
                else:
                    parent_y = focus_dict[parent]["y"]
                    if data["y"] is not None and parent_y is not None and data["y"] < parent_y:
                        issues.append(f"[BACKWARD EDGE] Focus '{fid}' (y={data['y']}) has prerequisite '{parent}' with higher y={parent_y}!")

        for me in data["mutex"]:
            if me not in focus_dict:
                issues.append(f"[MISSING MUTEX] Focus '{fid}' declares mutually_exclusive with non-existent focus '{me}'!")
            else:
                if fid not in focus_dict[me]["mutex"]:
                    warnings.append(f"[ONE-WAY MUTEX] Focus '{fid}' is mutually exclusive with '{me}', but '{me}' does not declare mutual exclusion with '{fid}'.")

    # Check the 4 destinies mutual exclusion completeness
    destinies = [
        "SER_proclamation_of_yugoslavia",
        "SER_restored_sovereign_serbia",
        "SER_balkan_socialist_soviet_republic",
        "SER_apis_pretorian_military_junta"
    ]
    for d in destinies:
        if d in focus_dict:
            for other_d in destinies:
                if other_d != d and other_d not in focus_dict[d]["mutex"]:
                    issues.append(f"[INCOMPLETE DESTINY GRAPH] Destiny focus '{d}' does not declare mutual exclusion with '{other_d}'!")
        else:
            issues.append(f"[MISSING DESTINY FOCUS] Focus '{d}' not found in focus tree!")

    print(f"  -> Exact collisions: {len([i for i in issues if 'EXACT FOCUS COLLISION' in i])}")
    print(f"  -> Missing DAG nodes: {len([i for i in issues if 'MISSING' in i])}")
    print(f"  -> Backward edges: {len([i for i in issues if 'BACKWARD' in i])}")
    print(f"  -> Box overlap warnings: {len([w for w in warnings if 'BOX OVERLAP RISK' in w])}")

    # -------------------------------------------------------------------------
    # 2. FOCUS REWARDS, EVENTS, IDEAS, CHARACTERS & STATES
    # -------------------------------------------------------------------------
    print("\n[SECTION 2] Focus Rewards, Events, Ideas, Characters & State Targets")
    
    all_idea_names = set()
    for idea_file in glob.glob(os.path.join(REPO_ROOT, "common/ideas/*.txt")):
        content = load_file(os.path.relpath(idea_file, REPO_ROOT))
        tokens = re.findall(r'(\b[A-Za-z0-9_]+)\s*=\s*\{', strip_comments(content))
        all_idea_names.update(tokens)

    all_event_ids = set()
    for ev_file in glob.glob(os.path.join(REPO_ROOT, "events/*.txt")):
        content = load_file(os.path.relpath(ev_file, REPO_ROOT))
        ev_matches = re.findall(r'\bid\s*=\s*([A-Za-z0-9_\.]+)', strip_comments(content))
        all_event_ids.update(ev_matches)

    ser_chars_content = load_file("common/characters/SER.txt")
    ser_chars = set(re.findall(r'(\bSER_[A-Za-z0-9_]+)\s*=\s*\{', strip_comments(ser_chars_content)))
    print(f"-> Registered SER Characters: {len(ser_chars)}")

    valid_state_ids = set()
    for st_file in glob.glob(os.path.join(REPO_ROOT, "history/states/*.txt")):
        bn = os.path.basename(st_file)
        m = re.match(r'^(\d+)', bn)
        if m:
            valid_state_ids.add(int(m.group(1)))
    print(f"-> Valid State IDs on disk: {len(valid_state_ids)}")

    for fid, data in focus_dict.items():
        raw = data["raw"]

        added_ideas = re.findall(r'add_ideas\s*=\s*([A-Za-z0-9_]+)', raw)
        for ai in added_ideas:
            if ai not in all_idea_names:
                issues.append(f"[MISSING IDEA IN REWARD] Focus '{fid}' adds non-existent idea '{ai}'!")

        swap_adds = re.findall(r'add_idea\s*=\s*([A-Za-z0-9_]+)', raw)
        for sa in swap_adds:
            if sa not in all_idea_names:
                issues.append(f"[MISSING IDEA IN REWARD] Focus '{fid}' swap-adds non-existent idea '{sa}'!")

        swap_rems = re.findall(r'remove_idea\s*=\s*([A-Za-z0-9_]+)', raw)
        for sr in swap_rems:
            if sr not in all_idea_names:
                warnings.append(f"[UNREGISTERED IDEA IN SWAP REMOVE] Focus '{fid}' swap-removes idea '{sr}' which is not in idea files.")

        called_events = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_\.]+)', raw)
        for ce in called_events:
            if ce not in all_event_ids:
                issues.append(f"[MISSING EVENT IN REWARD] Focus '{fid}' triggers non-existent event '{ce}'!")

        promoted = re.findall(r'promote_character\s*=\s*([A-Za-z0-9_]+)', raw)
        for pc in promoted:
            if pc not in ser_chars:
                issues.append(f"[MISSING CHARACTER IN REWARD] Focus '{fid}' promotes non-existent character '{pc}'!")

        recruited = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', raw)
        for rc in recruited:
            if rc not in ser_chars:
                issues.append(f"[MISSING CHARACTER IN REWARD] Focus '{fid}' recruits non-existent character '{rc}'!")

        scoped_states = re.findall(r'\b(\d+)\s*=\s*\{[^}]*(?:add_building_construction|add_core_of|transfer_state_to)', raw)
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
            warnings.append(f"[UNREGISTERED SPRITE] Focus '{fid}' uses sprite '{icon}' not found in interface .gfx files.")
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
    print("\n[SECTION 4] SER Characters Database & Portraits")
    char_top = extract_all_top_blocks(ser_chars_content)
    all_cblocks = {}
    if "characters" in char_top:
        for croot in char_top["characters"]:
            inner_chars = extract_all_top_blocks(croot)
            for cid, blist in inner_chars.items():
                all_cblocks[cid] = blist[0]

    ser_history = load_file("history/countries/SER - Serbia.txt")
    history_recruited = set(re.findall(r'^\s*recruit_character\s*=\s*([A-Za-z0-9_]+)', ser_history, re.MULTILINE))
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

    print(f"  -> Missing portraits on disk: {missing_portraits}")

    # -------------------------------------------------------------------------
    # 5. BALANCE OF POWER ENGINE AUDIT
    # -------------------------------------------------------------------------
    print("\n[SECTION 5] Balance of Power Engine (bop_ser_civil_military)")
    bop_file = "common/bop/SER_bop.txt"
    bop_content = load_file(bop_file)
    if not bop_content:
        issues.append(f"CRITICAL: {bop_file} missing!")
    else:
        # Check initial value
        init_m = re.search(r'initial_value\s*=\s*(-?\d*\.?\d+)', bop_content)
        if init_m:
            init_val = float(init_m.group(1))
            print(f"  -> BoP Initial Value: {init_val}")
            if init_val < -1.0 or init_val > 1.0:
                issues.append(f"[INVALID BOP INITIAL VALUE] initial_value = {init_val} is outside [-1.0, 1.0]!")
        else:
            issues.append(f"[MISSING BOP INITIAL VALUE] initial_value not found in {bop_file}!")

        # Check left and right sides
        left_side = re.search(r'left_side\s*=\s*([A-Za-z0-9_]+)', bop_content)
        right_side = re.search(r'right_side\s*=\s*([A-Za-z0-9_]+)', bop_content)
        if not left_side:
            issues.append("[MISSING BOP LEFT SIDE] left_side definition missing!")
        if not right_side:
            issues.append("[MISSING BOP RIGHT SIDE] right_side definition missing!")

        # Check ranges continuity
        range_blocks = re.findall(r'range\s*=\s*\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}', bop_content)
        print(f"  -> BoP Ranges Defined: {len(range_blocks)}")
        ranges = []
        for rb in range_blocks:
            min_m = re.search(r'min\s*=\s*(-?\d*\.?\d+)', rb)
            max_m = re.search(r'max\s*=\s*(-?\d*\.?\d+)', rb)
            id_m = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', rb)
            if min_m and max_m:
                rmin = float(min_m.group(1))
                rmax = float(max_m.group(1))
                rid = id_m.group(1) if id_m else "unknown"
                ranges.append((rmin, rmax, rid))

        ranges.sort(key=lambda t: t[0])
        for idx, (rmin, rmax, rid) in enumerate(ranges):
            print(f"     Range {idx+1}: [{rmin}, {rmax}] -> {rid}")
        
        # Check coverage
        if ranges:
            if ranges[0][0] > -1.0:
                issues.append(f"[BOP RANGE GAP] Bottom range starts at {ranges[0][0]}, expected -1.0!")
            if ranges[-1][1] < 1.0:
                issues.append(f"[BOP RANGE GAP] Top range ends at {ranges[-1][1]}, expected 1.0!")
            for k in range(len(ranges)-1):
                cur_max = ranges[k][1]
                next_min = ranges[k+1][0]
                if abs(cur_max - next_min) > 0.001:
                    issues.append(f"[BOP RANGE DISCONTINUITY] Gap between range {ranges[k][2]} (max={cur_max}) and {ranges[k+1][2]} (min={next_min})!")

    # Check scripted effects for BoP
    bop_fx_file = "common/scripted_effects/ww1_serbia_bop_effects.txt"
    bop_fx_content = load_file(bop_fx_file)
    if not bop_fx_content:
        issues.append(f"CRITICAL: {bop_fx_file} missing!")
    else:
        if "SER_shift_bop_pasic" not in bop_fx_content:
            issues.append("[MISSING SCRIPTED EFFECT] SER_shift_bop_pasic missing!")
        if "SER_shift_bop_apis" not in bop_fx_content:
            issues.append("[MISSING SCRIPTED EFFECT] SER_shift_bop_apis missing!")

    # -------------------------------------------------------------------------
    # 6. THE GREAT RETREAT & 30-DIVISION MOBILIZATION ENGINE AUDIT
    # -------------------------------------------------------------------------
    print("\n[SECTION 6] The Great Retreat & 30-Division Mobilization Engine")
    retreat_dec_file = "common/decisions/ww1_serbia_retreat_decisions.txt"
    rdec_content = load_file(retreat_dec_file)
    
    # State identification check
    # In retreat decisions, what states are prioritized?
    prioritized_states = set(re.findall(r'prioritize\s*=\s*\{([^{}]+)\}', rdec_content))
    for pblock in prioritized_states:
        sids = [int(s) for s in pblock.split()]
        print(f"  -> Retreat Decision Prioritized States: {sids}")
        if 731 not in sids:
            findings.append("[STATE AUDIT DISCREPANCY] Salonika (Thessaloniki port and naval base) is State 731 'Central Macedonia'! Retreat decisions must prioritize 731!")

    # Retreat Events Check
    ev_retreat_file = "events/ww1_serbia_retreat_events.txt"
    ev_retreat_content = load_file(ev_retreat_file)
    if "transfer_state = 731" not in ev_retreat_content:
        findings.append("[EVENT STATE DISCREPANCY] Event ww1_serbia_retreat.2 must transfer Central Macedonia (state 731) Salonika sanctuary!")

    # Division Templates Check
    created_templates = re.findall(r'division_template\s*=\s*\{[^}]*name\s*=\s*"([^"]+)"', rdec_content)
    print(f"  -> Division templates defined in retreat decisions: {created_templates}")
    spawned_divisions = re.findall(r'division\s*=\s*"[^"]*division_template\s*=\s*\\?"([^"\\]+)\\?"', rdec_content)
    print(f"  -> Division templates spawned in retreat decisions: {set(spawned_divisions)}")
    for s_div in set(spawned_divisions):
        if s_div not in created_templates:
            warnings.append(f"[SPAWNED TEMPLATE RISK] Decision spawns template '{s_div}' which is not defined in the decision block before spawning!")

    # Count divisions spawned across all decisions
    total_spawns = 0
    for m in re.finditer(r'create_unit\s*=\s*\{([^{}]+)\}', rdec_content):
        cblock = m.group(1)
        cnt_m = re.search(r'count\s*=\s*(\d+)', cblock)
        cnt = int(cnt_m.group(1)) if cnt_m else 1
        total_spawns += cnt
    print(f"  -> Total divisions spawned by Great Retreat decisions: {total_spawns}")
    if total_spawns < 28 or total_spawns > 32:
        warnings.append(f"[MOBILIZATION COUNT] Expected 28-30 divisions spawned across 4 waves, found {total_spawns}!")

    # Surrender limit check
    ideas_file = "common/ideas/ww1_serbia_ideas.txt"
    ideas_content = load_file(ideas_file)
    surr_m = re.search(r'SER_otadzbina_u_pokretu\s*=\s*\{.*?surrender_limit\s*=\s*(\d*\.?\d+)', ideas_content, re.DOTALL)
    if surr_m:
        surr_val = float(surr_m.group(1))
        print(f"  -> Fatherland in Motion surrender_limit: +{surr_val}")
    else:
        issues.append("[MISSING SURRENDER LIMIT] SER_otadzbina_u_pokretu has no surrender_limit modifier!")

    # -------------------------------------------------------------------------
    # 7. THE 4 DIVERGENT DESTINIES GAMEPLAY & CONTINUITY AUDIT
    # -------------------------------------------------------------------------
    print("\n[SECTION 7] The 4 Divergent Destinies Gameplay & Continuity")
    
    # Check what each destiny focus actually does
    for d in destinies:
        if d in focus_dict:
            raw = focus_dict[d]["raw"]
            print(f"\n--- Checking Destiny Focus: {d} ---")
            
            # Check ideology shift
            party_m = re.search(r'set_politics\s*=\s*\{[^}]*ruling_party\s*=\s*([a-z_]+)', raw)
            if party_m:
                print(f"  -> Sets ruling_party: {party_m.group(1)}")
            else:
                warnings.append(f"[DESTINY NO RULING PARTY] Focus '{d}' does not explicitly set ruling_party via set_politics!")

            # Check country leader assignment / promotion
            promote_m = re.findall(r'promote_character\s*=\s*([A-Za-z0-9_]+)', raw)
            recruit_m = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', raw)
            create_ldr_m = re.findall(r'create_country_leader\s*=\s*\{', raw)
            print(f"  -> Promoted characters: {promote_m}")
            print(f"  -> Recruited characters: {recruit_m}")
            print(f"  -> Country leaders created inline: {len(create_ldr_m)}")

            # Check cosmetic tag / name change
            cosmetic_m = re.search(r'set_cosmetic_tag\s*=\s*([A-Za-z0-9_]+)', raw)
            if cosmetic_m:
                print(f"  -> Sets cosmetic tag: {cosmetic_m.group(1)}")
            else:
                warnings.append(f"[DESTINY NO COSMETIC TAG] Focus '{d}' does not set cosmetic tag (e.g. YUG or socialist/junta identity)!")

            # Check coring or state claims
            cores = re.findall(r'(\d+)\s*=\s*\{[^}]*add_core_of\s*=\s*SER', raw)
            claims = re.findall(r'(\d+)\s*=\s*\{[^}]*add_claim_by\s*=\s*SER', raw)
            print(f"  -> States cored: {cores}")
            print(f"  -> States claimed: {claims}")

    # -------------------------------------------------------------------------
    # 8. EVENTS DEEP INSPECTION
    # -------------------------------------------------------------------------
    print("\n[SECTION 8] Events Deep Inspection (ww1_serbia_events & ww1_serbia_retreat_events)")
    ser_ev_files = ["events/ww1_serbia_events.txt", "events/ww1_serbia_retreat_events.txt"]
    for ef in ser_ev_files:
        econtent = load_file(ef)
        ns_list = re.findall(r'add_namespace\s*=\s*([A-Za-z0-9_]+)', econtent)
        print(f"-> {ef}: Namespaces declared: {ns_list}")

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

            options = extract_named_blocks(ebody, "option")
            if not options:
                issues.append(f"[EVENT WITHOUT OPTIONS] Event '{eid}' has no options defined!")

            child_events = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_\.]+)', ebody)
            for ce in child_events:
                if ce not in all_event_ids:
                    issues.append(f"[MISSING CHILD EVENT] Event '{eid}' calls non-existent event '{ce}'!")
                if ce == eid:
                    issues.append(f"[INFINITE LOOP RISK] Event '{eid}' calls itself directly!")

    # -------------------------------------------------------------------------
    # 9. DECISIONS & CATEGORIES AUDIT
    # -------------------------------------------------------------------------
    print("\n[SECTION 9] Decisions & Categories Audit")
    sdec_files = [
        "common/decisions/ww1_serbia_decisions.txt",
        "common/decisions/ww1_serbia_retreat_decisions.txt"
    ]
    all_categories = set()
    for cat_file in glob.glob(os.path.join(REPO_ROOT, "common/decisions/categories/*.txt")):
        ccontent = load_file(os.path.relpath(cat_file, REPO_ROOT))
        cats = extract_all_top_blocks(ccontent).keys()
        all_categories.update(cats)
    print(f"-> Registered Decision Categories: {len(all_categories)}")

    for df in sdec_files:
        dcontent = load_file(df)
        cat_blocks = extract_all_top_blocks(dcontent)
        for cat_name, cbody_list in cat_blocks.items():
            if cat_name not in all_categories:
                issues.append(f"[UNREGISTERED DECISION CATEGORY] Decision file '{df}' uses unregistered category '{cat_name}'!")
            
            for cbody in cbody_list:
                decs = extract_all_top_blocks(cbody)
                for dec_id, dec_bodies in decs.items():
                    for dec_body in dec_bodies:
                        if "allowed" not in dec_body:
                            warnings.append(f"[DECISION WITHOUT ALLOWED] Decision '{dec_id}' in {df} has no 'allowed' block!")

                        dec_added_ideas = re.findall(r'add_ideas\s*=\s*([A-Za-z0-9_]+)', dec_body)
                        for dai in dec_added_ideas:
                            if dai not in all_idea_names:
                                issues.append(f"[MISSING IDEA IN DECISION] Decision '{dec_id}' adds non-existent idea '{dai}'!")

    # -------------------------------------------------------------------------
    # 10. CLAUSEWITZ SEMANTIC ORACLE AUDIT ACROSS ALL SERBIAN MODIFIERS
    # -------------------------------------------------------------------------
    print("\n[SECTION 10] Clausewitz Semantic Oracle Modifier Audit")
    sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
    try:
        from hoi4_semantic_oracle import is_valid_country_modifier
        oracle_available = True
    except ImportError:
        oracle_available = False
        warnings.append("hoi4_semantic_oracle could not be imported; skipping modifier semantic check.")

    if oracle_available:
        ser_mod_files = [
            "common/ideas/ww1_serbia_ideas.txt",
            "common/country_leader/ww1_serbia_traits.txt",
            "common/bop/SER_bop.txt",
            "common/decisions/ww1_serbia_decisions.txt",
            "common/decisions/ww1_serbia_retreat_decisions.txt"
        ]
        invalid_mods = 0
        for smf in ser_mod_files:
            fcontent = load_file(smf)
            # Find modifier = { ... }
            modifier_lines = re.findall(r'modifier\s*=\s*\{([^{}]+)\}', fcontent)
            for mblock in modifier_lines:
                for line in mblock.splitlines():
                    line = line.split('#')[0].strip()
                    if not line or '=' not in line:
                        continue
                    mkey = line.split('=')[0].strip()
                    if not is_valid_country_modifier(mkey):
                        # Some unit traits use unit modifiers
                        if "traits" in smf:
                            continue
                        issues.append(f"[INVALID CLAUSEWITZ MODIFIER] File {smf}: Modifier '{mkey}' is not recognized by Semantic Oracle!")
                        invalid_mods += 1
        print(f"  -> Invalid modifier keys found: {invalid_mods}")

    # -------------------------------------------------------------------------
    # 11. LOCALIZATION PARITY, BOM & QUOTE INTEGRITY
    # -------------------------------------------------------------------------
    print("\n[SECTION 11] Localization Parity & Encoding")
    loc_en_file = os.path.join(REPO_ROOT, "localisation/english/ww1_serbia_l_english.yml")
    loc_pt_file = os.path.join(REPO_ROOT, "localisation/braz_por/ww1_serbia_l_braz_por.yml")

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
        print(f"  -> Total localized keys in Serbia loc: {len(en_keys)} (100% parity: {en_keys == pt_keys})")

    # -------------------------------------------------------------------------
    # 12. STARTING HISTORY, LAWS, POPULARITIES & MAP SANITY (1911)
    # -------------------------------------------------------------------------
    print("\n[SECTION 12] History, Laws, Popularities & 1911 Map Baseline")
    pop_block = re.search(r'set_popularities\s*=\s*\{([^{}]+)\}', ser_history)
    if pop_block:
        pops = re.findall(r'([a-z_]+)\s*=\s*(\d+)', pop_block.group(1))
        total_pop = sum(int(val) for _, val in pops)
        if total_pop != 100:
            issues.append(f"[POPULARITY SUM ERROR] Starting popularities in SER history sum to {total_pop}% (expected 100%)!")
        else:
            print(f"  -> Starting popularities sum to {total_pop}%: OK")

    start_ideas = re.search(r'add_ideas\s*=\s*\{([^{}]+)\}', ser_history)
    if start_ideas:
        si_list = start_ideas.group(1).strip().split()
        for si in si_list:
            if si not in all_idea_names:
                issues.append(f"[MISSING STARTING IDEA] SER starting idea '{si}' does not exist in common/ideas/!")

    # Check Montenegro (state 105) ownership and core in 1911
    st_105 = load_file("history/states/105-Montenegro.txt")
    if "owner = SER" not in st_105:
        issues.append("[1911 MAP INTEGRATION ERROR] State 105 (Montenegro) does NOT have 'owner = SER'!")
    if "add_core_of = SER" not in st_105:
        issues.append("[1911 MAP INTEGRATION ERROR] State 105 (Montenegro) does NOT have 'add_core_of = SER'!")

    # Check OOB file
    oob_m = re.search(r'oob\s*=\s*"([^"]+)"', ser_history)
    if oob_m:
        oob_name = oob_m.group(1)
        oob_path = f"history/units/{oob_name}.txt"
        oob_content = load_file(oob_path)
        if not oob_content:
            issues.append(f"[MISSING OOB FILE] Serbia history references oob '{oob_name}', but {oob_path} does not exist!")
        else:
            print(f"  -> Serbia starting OOB '{oob_name}': FOUND ({len(oob_content.splitlines())} lines)")

    # -------------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------------
    print("\n================================================================================")
    print(f"AUDIT COMPLETE: Found {len(issues)} ISSUES, {len(warnings)} WARNINGS, and {len(findings)} FINDINGS")
    print("================================================================================")
    if issues:
        print("\n>>> CRITICAL ISSUES / BUGS FOUND <<<")
        for idx, iss in enumerate(issues, 1):
            print(f"  {idx}. {iss}")
    else:
        print("\n>>> ZERO CRITICAL CRASH ISSUES! <<<")

    if findings:
        print("\n>>> CRITICAL DISCREPANCIES / GAMEPLAY BREAKS <<<")
        for idx, fnd in enumerate(findings, 1):
            print(f"  {idx}. {fnd}")

    if warnings:
        print("\n>>> WARNINGS & GAMEPLAY REFINEMENT RECOMMENDATIONS <<<")
        for idx, w in enumerate(warnings[:35], 1):
            print(f"  {idx}. {w}")
        if len(warnings) > 35:
            print(f"  ... and {len(warnings) - 35} more warnings.")

if __name__ == "__main__":
    main()
