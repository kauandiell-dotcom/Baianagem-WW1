import os
import struct
import re
from PIL import Image

GFX_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\interface\ww1_germany_goals.gfx"
GOALS_DIR = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\gfx\interface\goals"
PLAN_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\PLANO_FOCUS_TREE_ALEMANHA_WW1.md"
REPORT_PATH = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\explorer_icons_gfx\icons_report.md"

def test_dds_binary_integrity():
    print("=== TEST 1: DDS Binary & Header Integrity ===")
    assert os.path.isdir(GOALS_DIR), f"Goals directory does not exist: {GOALS_DIR}"
    files = [f for f in os.listdir(GOALS_DIR) if f.endswith(".dds")]
    print(f"Found {len(files)} DDS files in {GOALS_DIR}")
    assert len(files) == 32, f"Expected exactly 32 DDS files, found {len(files)}"

    for f in sorted(files):
        path = os.path.join(GOALS_DIR, f)
        size = os.path.getsize(path)
        assert size > 0, f"File {f} is 0 bytes"
        
        with open(path, "rb") as fp:
            data = fp.read(128)
            assert len(data) >= 128, f"File {f} is too short to be a valid DDS ({len(data)} bytes)"
            magic = data[0:4]
            assert magic == b"DDS ", f"File {f} does not start with 'DDS ' magic: {magic}"
            
            header_size = struct.unpack("<I", data[4:8])[0]
            assert header_size == 124, f"File {f} has invalid DDS header size: {header_size} (expected 124)"
            
            flags = struct.unpack("<I", data[8:12])[0]
            height = struct.unpack("<I", data[12:16])[0]
            width = struct.unpack("<I", data[16:20])[0]
            
            # Check dimensions are typical icon dimensions (> 0, < 256)
            assert 16 <= width <= 256, f"File {f} width {width} out of expected icon range"
            assert 16 <= height <= 256, f"File {f} height {height} out of expected icon range"

        # Verify Pillow opens and decodes image
        with Image.open(path) as img:
            assert img.size == (width, height), f"Image dimension mismatch in {f}: {img.size} vs ({width}, {height})"
            # Check mode
            assert img.mode in ("RGBA", "RGB"), f"Unexpected mode {img.mode} for {f}"
            # Check non-blank content (bounding box or color variance)
            extrema = img.getextrema()
            # If all channels have min == max, the image is a solid flat block (potential dummy)
            is_flat = True
            for ch in extrema:
                if isinstance(ch, tuple) and ch[0] != ch[1]:
                    is_flat = False
                    break
            assert not is_flat, f"Suspicious: File {f} appears to be a completely flat/blank single-color image!"

        print(f"  [PASS] {f}: {width}x{height}, size={size} bytes, mode={img.mode}, not flat")
    print("Test 1 Passed: All 32 DDS files have valid binary DDS headers, non-zero size, valid dimensions, and genuine graphics data.\n")

def test_gfx_syntax_and_braces():
    print("=== TEST 2: GFX Syntax & Brace Balance ===")
    assert os.path.isfile(GFX_PATH), f"GFX file does not exist: {GFX_PATH}"
    
    with open(GFX_PATH, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        content = "".join(lines)
        
    open_count = content.count("{")
    close_count = content.count("}")
    print(f"Total lines: {len(lines)}")
    print(f"Opening braces: {open_count}, Closing braces: {close_count}")
    assert open_count == 257, f"Expected 257 open braces, got {open_count}"
    assert close_count == 257, f"Expected 257 close braces, got {close_count}"
    assert open_count == close_count, "Brace mismatch"

    # Nesting depth simulation
    depth = 0
    line_num = 0
    for line in lines:
        line_num += 1
        # strip comments
        code_part = line.split("#")[0]
        for ch in code_part:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                assert depth >= 0, f"Nesting error: closing brace without open at line {line_num}"
    assert depth == 0, f"Nesting error: ended with depth {depth} instead of 0"
    print("Nesting depth check passed: perfectly balanced throughout the file.")
    print("Test 2 Passed.\n")

def test_sprite_definitions():
    print("=== TEST 3: Sprite Definitions Completeness & Integrity ===")
    with open(GFX_PATH, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Find all spriteType blocks
    # A base sprite has: name = "...", texturefile = "..."
    # A shine sprite has: name = "..._shine", texturefile = "...", effectFile = "...", animation blocks
    
    # Parse blocks using regex or state machine
    sprite_names = re.findall(r'name\s*=\s*"([^"]+)"', content)
    print(f"Total sprite names found: {len(sprite_names)}")
    assert len(sprite_names) == 64, f"Expected 64 sprite names, got {len(sprite_names)}"
    
    base_names = [s for s in sprite_names if not s.endswith("_shine")]
    shine_names = [s for s in sprite_names if s.endswith("_shine")]
    
    assert len(base_names) == 32, f"Expected 32 base names, got {len(base_names)}"
    assert len(shine_names) == 32, f"Expected 32 shine names, got {len(shine_names)}"
    
    # Check 1:1 correspondence: every base sprite must have a corresponding shine sprite
    for b in base_names:
        expected_shine = f"{b}_shine"
        assert expected_shine in shine_names, f"Base sprite {b} is missing shine counterpart {expected_shine}"
        
    print("1:1 correspondence verified: exactly 32 base sprites and 32 corresponding _shine sprites.")

    # Check that each texturefile referenced in GFX exists in GOALS_DIR
    tex_refs = re.findall(r'texturefile\s*=\s*"([^"]+)"', content)
    print(f"Total texturefile references: {len(tex_refs)}")
    # Each base sprite has 1 texturefile, each shine has 1 texturefile (plus animationtexturefile).
    # Wait, does re.findall match animationtexturefile?
    # Note: re.findall(r'texturefile\s*=') might match 'animationtexturefile' if not preceded by word boundary!
    # Let's check with word boundary:
    strict_tex_refs = re.findall(r'\btexturefile\s*=\s*"([^"]+)"', content)
    print(f"Strict texturefile references (word boundary): {len(strict_tex_refs)}")
    assert len(strict_tex_refs) == 64, f"Expected 64 strict texturefile references, got {len(strict_tex_refs)}"
    
    for ref in strict_tex_refs:
        assert ref.startswith("gfx/interface/goals/"), f"Texturefile path {ref} does not use standard gfx/interface/goals/ prefix"
        filename = ref.replace("gfx/interface/goals/", "")
        local_path = os.path.join(GOALS_DIR, filename)
        assert os.path.isfile(local_path), f"Referenced file on disk missing: {local_path}"

    # Check shine overlays and effectFile
    effects = re.findall(r'\beffectFile\s*=\s*"([^"]+)"', content)
    assert len(effects) == 32, f"Expected 32 effectFile references, got {len(effects)}"
    for eff in effects:
        assert eff == "gfx/FX/buttonstate.lua", f"Unexpected effectFile: {eff}"
        
    anim_textures = re.findall(r'\banimationtexturefile\s*=\s*"([^"]+)"', content)
    # Each shine has 2 animation blocks, so 32 * 2 = 64 animationtexturefile references
    assert len(anim_textures) == 64, f"Expected 64 animationtexturefile references, got {len(anim_textures)}"
    for at in anim_textures:
        assert at == "gfx/interface/goals/shine_overlay.dds", f"Unexpected animationtexturefile: {at}"

    anim_masks = re.findall(r'\banimationmaskfile\s*=\s*"([^"]+)"', content)
    assert len(anim_masks) == 64, f"Expected 64 animationmaskfile references, got {len(anim_masks)}"

    print("Test 3 Passed: All 64 SpriteTypes are completely and properly defined with valid paths, lua shader, and shine animations.\n")

def test_plan_and_report_coverage():
    print("=== TEST 4: Coverage against PLAN and ICONS_REPORT ===")
    # Extract 32 focus IDs from PLAN_PATH
    with open(PLAN_PATH, "r", encoding="utf-8") as fp:
        plan_text = fp.read()
    
    # National focus IDs from the plan
    actual_focus_ids = [
        "GER_agadir_crisis_gambit",
        "GER_tirpitz_fourth_naval_bill",
        "GER_berlin_baghdad_railway",
        "GER_army_bill_1912",
        "GER_centenary_of_leipzig_1913",
        "GER_expand_heavy_howitzers",
        "GER_the_blank_cheque",
        "GER_execute_schlieffen_plan",
        "GER_smash_liege_forts",
        "GER_the_miracle_of_tannenberg",
        "GER_aufmarsch_ost_focus",
        "GER_haber_bosch_nitrogen_miracle",
        "GER_chemical_warfare_initiative",
        "GER_hindenburg_program",
        "GER_stosstruppen_tactics",
        "GER_silent_dictatorship_ohl",
        "GER_unrestricted_submarine_warfare",
        "GER_sealed_train_to_petrograd",
        "GER_treaty_of_brest_litovsk",
        "GER_the_kaiserschlacht_1918",
        "GER_bethmann_civilian_supremacy",
        "GER_prussian_franchise_reform",
        "GER_reichstag_peace_resolution",
        "GER_constitutional_monarchy_proclamation",
        "GER_found_vaterlandspartei",
        "GER_total_war_mobilization",
        "GER_annexation_of_belgium_and_briey",
        "GER_morphed_mitteleuropa_iron_rule",
        "GER_willy_nicky_telegrams_bjorko",
        "GER_hajj_wilhelm_pan_islamic_crusade",
        "GER_spartakusbund_proletarian_revolt",
        "GER_emergency_danubian_annexation",
    ]
    print(f"Checking {len(actual_focus_ids)} national focuses defined in plan...")
    for fid in actual_focus_ids:
        assert f"`{fid}`" in plan_text, f"Focus {fid} not found in PLAN_PATH!"

    # Read icons_report.md table
    with open(REPORT_PATH, "r", encoding="utf-8") as fp:
        report_text = fp.read()

    # Read GFX content to see sprites defined
    with open(GFX_PATH, "r", encoding="utf-8") as fp:
        gfx_text = fp.read()
        
    base_sprites = set(re.findall(r'name\s*=\s*"(GFX_[^"_]+(?:_[^"_]+)*)"', gfx_text))
    # Filter out _shine
    base_sprites = {s for s in base_sprites if not s.endswith("_shine")}
    print(f"Base sprites defined in GFX: {len(base_sprites)}")

    # Check mapping table in icons_report
    # Table format: | # | ID do Foco | Fase / Ramo | Sprite Principal | Target DDS ...
    table_rows = re.findall(r'\|\s*\d+\s*\|\s*`(GER_[a-z0-9_]+)`\s*\|\s*[^|]+\|\s*`([^`]+)`\s*\|\s*`([^`]+)`', report_text)
    print(f"Table rows parsed from icons_report: {len(table_rows)}")
    assert len(table_rows) == 32, f"Expected 32 table rows in icons_report, got {len(table_rows)}"

    for row in table_rows:
        fid, sprite, dds = row
        assert fid in actual_focus_ids, f"Focus {fid} in report table not found in master plan!"
        assert sprite in base_sprites, f"Sprite {sprite} mapped for {fid} not defined in ww1_germany_goals.gfx!"
        dds_disk = os.path.join(GOALS_DIR, dds)
        assert os.path.isfile(dds_disk), f"DDS file {dds} mapped for {fid} not on disk at {dds_disk}"

    print("Test 4 Passed: 100% coverage and alignment between master plan, explorer report, GFX definitions, and disk assets.\n")

def test_no_duplicate_sprites_in_mod():
    print("=== TEST 5: Duplicate Sprite Conflict Check ===")
    with open(GFX_PATH, "r", encoding="utf-8") as fp:
        our_sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', fp.read()))

    interface_dir = os.path.dirname(GFX_PATH)
    conflicts = []
    for root, dirs, files in os.walk(interface_dir):
        for f in files:
            if f.endswith(".gfx") and f != "ww1_germany_goals.gfx":
                gfx_path = os.path.join(root, f)
                try:
                    with open(gfx_path, "r", encoding="utf-8", errors="ignore") as fp:
                        other_sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', fp.read()))
                    overlap = our_sprites.intersection(other_sprites)
                    if overlap:
                        conflicts.append((f, overlap))
                except Exception as e:
                    pass

    if conflicts:
        print(f"Conflicts found: {conflicts}")
    else:
        print("PASS: Zero duplicate sprite conflicts across all mod interface GFX files.")
    assert len(conflicts) == 0, f"Sprite name conflicts found: {conflicts}"
    print("Test 5 Passed.\n")

def test_case_sensitivity():
    print("=== TEST 6: Exact Case-Sensitivity Check ===")
    with open(GFX_PATH, "r", encoding="utf-8") as fp:
        content = fp.read()
    strict_tex_refs = re.findall(r'\btexturefile\s*=\s*"([^"]+)"', content)
    disk_files = {f: f for f in os.listdir(GOALS_DIR)}
    
    mismatches = []
    for ref in strict_tex_refs:
        filename = os.path.basename(ref)
        if filename in disk_files:
            # On Windows, listdir returns actual filesystem casing
            actual_case = disk_files[filename]
            if filename != actual_case:
                mismatches.append((filename, actual_case))
        else:
            mismatches.append((filename, "MISSING"))
            
    if mismatches:
        print(f"Casing mismatches detected: {mismatches}")
    else:
        print("PASS: 100% exact character case match between GFX paths and disk filenames.")
    assert len(mismatches) == 0, f"Casing mismatches: {mismatches}"
    print("Test 6 Passed.\n")

if __name__ == "__main__":
    test_dds_binary_integrity()
    test_gfx_syntax_and_braces()
    test_sprite_definitions()
    test_plan_and_report_coverage()
    test_no_duplicate_sprites_in_mod()
    test_case_sensitivity()
    print("ALL 6 ADVERSARIAL TESTS PASSED!")
