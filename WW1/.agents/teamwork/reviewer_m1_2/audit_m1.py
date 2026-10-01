import os
import re
import sys
from PIL import Image

PLAN_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\PLANO_FOCUS_TREE_ALEMANHA_WW1.md"
ICONS_REPORT_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\explorer_icons_gfx\icons_report.md"
GFX_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\interface\ww1_germany_goals.gfx"
GOALS_DIR = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\gfx\interface\goals"
MOD_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def run_audit():
    print("=" * 70)
    print("REVIEWER 2 INDEPENDENT ADVERSARIAL AUDIT - MILESTONE 1")
    print("=" * 70)
    
    findings = []
    
    # -------------------------------------------------------------
    # 1. Parse PLANO_FOCUS_TREE_ALEMANHA_WW1.md for Focus IDs
    # -------------------------------------------------------------
    print("\n[CHECK 1] Cross-referencing Focus IDs from Master Plan...")
    if not os.path.exists(PLAN_PATH):
        findings.append(("CRITICAL", f"Master plan missing: {PLAN_PATH}"))
        return findings

    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        plan_content = f.read()

    # Regex for focus IDs: bold or backtick `GER_...`
    raw_focus_ids = re.findall(r"`(GER_[a-zA-Z0-9_]+)`", plan_content)
    # Filter out modifiers, ideas, cosmetic tags
    excluded_ids = {
        "GER_grosser_generalstab",
        "GER_krupp_chemical_conglomerates",
        "GER_tirpitz_naval_ambition",
        "GER_encirclement_paranoia",
        "GER_burgfrieden_social_peace",
        "GER_turnip_winter_crisis",
        "GER_turnip_winter_crisis_1",
        "GER_turnip_winter_crisis_2",
        "GER_turnip_winter_crisis_3",
        "GER_hindenburg_program_victory",
        "GER_kaiserschlacht_idea",
        "GER_schlieffen_momentum",
        "GER_ober_ost",
        "GER_socialist",
    }
    
    plan_focuses = []
    for fid in raw_focus_ids:
        if fid not in excluded_ids and fid not in plan_focuses:
            plan_focuses.append(fid)

    print(f"-> Discovered {len(plan_focuses)} focus IDs in PLANO_FOCUS_TREE_ALEMANHA_WW1.md:")
    for idx, fid in enumerate(plan_focuses, 1):
        print(f"   {idx:02d}. {fid}")

    if len(plan_focuses) != 32:
        findings.append(("MAJOR", f"Expected 32 focus IDs in master plan, but extracted {len(plan_focuses)}."))

    # -------------------------------------------------------------
    # 2. Parse explorer icons_report.md for Focus -> Sprite mapping
    # -------------------------------------------------------------
    print("\n[CHECK 2] Parsing explorer mapping table from icons_report.md...")
    with open(ICONS_REPORT_PATH, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Extract table rows: | # | ID do Foco | Fase / Ramo | Sprite Principal | Target DDS ...
    table_matches = re.findall(r"\|\s*(\d+)\s*\|\s*`(GER_[a-zA-Z0-9_]+)`\s*\|\s*([^|]+)\|\s*`([^`]+)`\s*\|\s*`([^`]+)`", report_content)
    print(f"-> Extracted {len(table_matches)} mapped focuses from icons_report.md table.")
    
    mapping_dict = {}
    for num, fid, branch, sprite, dds in table_matches:
        mapping_dict[fid] = {
            "num": int(num),
            "branch": branch.strip(),
            "sprite": sprite.strip(),
            "dds": dds.strip()
        }

    # Verify all plan focuses exist in mapping
    missing_in_mapping = [f for f in plan_focuses if f not in mapping_dict]
    if missing_in_mapping:
        findings.append(("CRITICAL", f"Focuses in plan missing from icon mapping: {missing_in_mapping}"))
    else:
        print("-> All 32 plan focuses have explicit sprite and DDS mappings in icons_report.md.")

    # -------------------------------------------------------------
    # 3. Parse ww1_germany_goals.gfx for Sprites and Shine Definitions
    # -------------------------------------------------------------
    print("\n[CHECK 3] Validating ww1_germany_goals.gfx structure and syntax...")
    if not os.path.exists(GFX_PATH):
        findings.append(("CRITICAL", f"GFX file missing: {GFX_PATH}"))
        return findings

    with open(GFX_PATH, "r", encoding="utf-8") as f:
        gfx_content = f.read()

    # Brace counting & depth tracking
    open_braces = 0
    close_braces = 0
    brace_depth = 0
    depth_errors = 0
    line_num = 1
    for char in gfx_content:
        if char == "\n":
            line_num += 1
        elif char == "{":
            open_braces += 1
            brace_depth += 1
        elif char == "}":
            close_braces += 1
            brace_depth -= 1
            if brace_depth < 0:
                depth_errors += 1
                findings.append(("CRITICAL", f"Negative brace depth at line {line_num}!"))

    print(f"-> Opening braces: {open_braces}")
    print(f"-> Closing braces: {close_braces}")
    print(f"-> Final brace depth: {brace_depth}")
    
    if open_braces != close_braces:
        findings.append(("CRITICAL", f"Brace mismatch: {open_braces} open vs {close_braces} close!"))
    if brace_depth != 0:
        findings.append(("CRITICAL", f"Non-zero final brace depth: {brace_depth}!"))
    if open_braces != 257:
        findings.append(("MAJOR", f"Expected exactly 257 braces, found {open_braces}."))

    # Extract all SpriteType blocks
    # We parse blocks bounded by SpriteType = { ... }
    sprite_blocks = re.findall(r"SpriteType\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}", gfx_content)
    print(f"-> Total SpriteType blocks parsed: {len(sprite_blocks)}")
    if len(sprite_blocks) != 64:
        findings.append(("MAJOR", f"Expected 64 SpriteType blocks, found {len(sprite_blocks)}."))

    sprites_registered = {}
    for block in sprite_blocks:
        name_m = re.search(r'name\s*=\s*"([^"]+)"', block)
        tex_m = re.search(r'(?<!animation)texturefile\s*=\s*"([^"]+)"', block)
        if name_m:
            s_name = name_m.group(1)
            s_tex = tex_m.group(1) if tex_m else None
            sprites_registered[s_name] = {
                "texturefile": s_tex,
                "block": block
            }

    base_sprites = {k: v for k, v in sprites_registered.items() if not k.endswith("_shine")}
    shine_sprites = {k: v for k, v in sprites_registered.items() if k.endswith("_shine")}

    print(f"-> Base sprites: {len(base_sprites)}")
    print(f"-> Shine sprites: {len(shine_sprites)}")

    # Check that each mapping has its base sprite and shine sprite
    for fid, m in mapping_dict.items():
        req_sprite = m["sprite"]
        req_dds = m["dds"]
        
        # Check base sprite
        if req_sprite not in base_sprites:
            findings.append(("CRITICAL", f"Focus {fid} required sprite '{req_sprite}' NOT found in ww1_germany_goals.gfx!"))
        else:
            tex = base_sprites[req_sprite]["texturefile"]
            expected_tex = f"gfx/interface/goals/{req_dds}"
            if tex != expected_tex:
                findings.append(("MAJOR", f"Sprite '{req_sprite}' texturefile mismatch: got '{tex}', expected '{expected_tex}'!"))

        # Check shine sprite
        req_shine = f"{req_sprite}_shine"
        if req_shine not in shine_sprites:
            findings.append(("CRITICAL", f"Focus {fid} required shine sprite '{req_shine}' NOT found in ww1_germany_goals.gfx!"))
        else:
            s_data = shine_sprites[req_shine]
            tex = s_data["texturefile"]
            expected_tex = f"gfx/interface/goals/{req_dds}"
            if tex != expected_tex:
                findings.append(("MAJOR", f"Shine sprite '{req_shine}' texturefile mismatch: got '{tex}', expected '{expected_tex}'!"))
            
            # Validate HOI4 animation parameters in shine block
            block = s_data["block"]
            if 'effectFile = "gfx/FX/buttonstate.lua"' not in block:
                findings.append(("CRITICAL", f"Shine sprite '{req_shine}' missing effectFile 'gfx/FX/buttonstate.lua'!"))
            if 'legacy_lazy_load = no' not in block:
                findings.append(("MINOR", f"Shine sprite '{req_shine}' missing legacy_lazy_load = no."))
                
            # Count animations
            anim_blocks = re.findall(r"animation\s*=\s*\{([^}]+)\}", block)
            if len(anim_blocks) != 2:
                findings.append(("CRITICAL", f"Shine sprite '{req_shine}' expected 2 animation blocks, found {len(anim_blocks)}!"))
            else:
                # Validate animation 1 (-90.0)
                a1 = anim_blocks[0]
                if f'animationmaskfile = "{expected_tex}"' not in a1:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 1 maskfile invalid: expected '{expected_tex}'"))
                if 'animationtexturefile = "gfx/interface/goals/shine_overlay.dds"' not in a1:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 1 animationtexturefile invalid."))
                if 'animationrotation = -90.0' not in a1:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 1 rotation != -90.0"))
                if 'animationlooping = no' not in a1 or 'animationtype = "scrolling"' not in a1:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 1 parameters invalid."))

                # Validate animation 2 (90.0)
                a2 = anim_blocks[1]
                if f'animationmaskfile = "{expected_tex}"' not in a2:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 2 maskfile invalid: expected '{expected_tex}'"))
                if 'animationtexturefile = "gfx/interface/goals/shine_overlay.dds"' not in a2:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 2 animationtexturefile invalid."))
                if 'animationrotation = 90.0' not in a2:
                    findings.append(("MAJOR", f"Shine '{req_shine}' anim 2 rotation != 90.0"))

    # -------------------------------------------------------------
    # 4. Validate Texture Files on Disk
    # -------------------------------------------------------------
    print("\n[CHECK 4] Validating physical DDS texture files on disk...")
    if not os.path.exists(GOALS_DIR):
        findings.append(("CRITICAL", f"Goals directory does not exist: {GOALS_DIR}"))
        return findings

    disk_files = os.listdir(GOALS_DIR)
    print(f"-> Total files in {GOALS_DIR}: {len(disk_files)}")
    if len(disk_files) != 32:
        findings.append(("MAJOR", f"Expected 32 files in goals dir, found {len(disk_files)}."))

    disk_files_case_map = {f.lower(): f for f in disk_files}

    for fid, m in mapping_dict.items():
        req_dds = m["dds"]
        req_dds_lower = req_dds.lower()
        
        if req_dds_lower not in disk_files_case_map:
            findings.append(("CRITICAL", f"Required DDS file '{req_dds}' for {fid} NOT found on disk!"))
            continue
            
        actual_name = disk_files_case_map[req_dds_lower]
        if actual_name != req_dds:
            findings.append(("MAJOR", f"Case mismatch on disk for '{req_dds}': actual on disk is '{actual_name}'! (Breaks on Linux)"))
            
        full_path = os.path.join(GOALS_DIR, actual_name)
        size = os.path.getsize(full_path)
        if size == 0:
            findings.append(("CRITICAL", f"DDS file '{actual_name}' is 0 bytes (empty stub)!"))
            continue

        try:
            with Image.open(full_path) as im:
                w, h = im.size
                mode = im.mode
                fmt = im.format
                if fmt != "DDS":
                    findings.append(("CRITICAL", f"File '{actual_name}' format is '{fmt}', expected 'DDS'!"))
                if mode != "RGBA":
                    findings.append(("MAJOR", f"File '{actual_name}' mode is '{mode}', expected 'RGBA'!"))
                if w < 60 or w > 120 or h < 60 or h > 120:
                    findings.append(("MINOR", f"File '{actual_name}' has non-standard focus icon dimensions: {w}x{h}."))
        except Exception as e:
            findings.append(("CRITICAL", f"File '{actual_name}' corrupted or cannot be read by Pillow: {e}"))

    # Check for forward slash compliance in GFX paths
    for s_name, s_data in sprites_registered.items():
        tex = s_data["texturefile"]
        if tex and "\\" in tex:
            findings.append(("CRITICAL", f"Backslash detected in texturefile path for {s_name}: '{tex}'. HOI4 requires forward slashes."))

    # -------------------------------------------------------------
    # 5. Check Duplicate Definitions & Global Collisions
    # -------------------------------------------------------------
    print("\n[CHECK 5] Checking for duplicate definitions and collisions...")
    all_names = re.findall(r'name\s*=\s*"([^"]+)"', gfx_content)
    seen_names = set()
    dup_names = set()
    for n in all_names:
        if n in seen_names:
            dup_names.add(n)
        seen_names.add(n)
    if dup_names:
        findings.append(("CRITICAL", f"Duplicate sprite names detected in GFX: {dup_names}"))
    else:
        print("-> Zero duplicate sprite names in GFX.")

    # Cross-check other .gfx files in WW1/interface
    interface_dir = os.path.dirname(GFX_PATH)
    collisions = []
    for fname in os.listdir(interface_dir):
        if fname.endswith(".gfx") and fname != "ww1_germany_goals.gfx":
            fp = os.path.join(interface_dir, fname)
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()
                other_sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', c))
                overlap = set(sprites_registered.keys()).intersection(other_sprites)
                if overlap:
                    collisions.append((fname, overlap))
            except Exception as e:
                print(f"Error checking {fname}: {e}")

    if collisions:
        for fname, ov in collisions:
            findings.append(("MAJOR", f"Sprite name collision with existing file {fname}: {ov}"))
    else:
        print("-> Zero sprite name collisions with all existing mod .gfx files.")

    # Check BOM on GFX file
    with open(GFX_PATH, "rb") as f:
        first3 = f.read(3)
        if first3 == b"\xef\xbb\xbf":
            findings.append(("MINOR", "GFX file has UTF-8 BOM (UTF-8 without BOM is preferred for Clausewitz .gfx files)."))
        else:
            print("-> GFX file is clean UTF-8 without BOM (standard for Clausewitz).")


    # -------------------------------------------------------------
    # 6. Summary and Findings Reporting
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print("AUDIT SUMMARY & FINDINGS REPORT")
    print("=" * 70)
    print(f"Total findings: {len(findings)}")
    for sev, desc in findings:
        print(f"  [{sev}] {desc}")
        
    criticals = [f for f in findings if f[0] == "CRITICAL"]
    majors = [f for f in findings if f[0] == "MAJOR"]
    minors = [f for f in findings if f[0] == "MINOR"]
    
    print(f"\nBreakdown: {len(criticals)} Critical, {len(majors)} Major, {len(minors)} Minor")
    if len(criticals) == 0 and len(majors) == 0:
        print(">>> VERDICT: APPROVE <<<")
    else:
        print(">>> VERDICT: REQUEST_CHANGES <<<")
        
    return findings

if __name__ == "__main__":
    run_audit()
