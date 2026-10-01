import os
import sys
import struct
import hashlib
import json
from PIL import Image
import numpy as np

SOURCE_BASE = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3106240385\gfx\interface\goals"
TARGET_GOALS_DIR = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\gfx\interface\goals"
TARGET_GFX_FILE = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\interface\ww1_germany_goals.gfx"
DEPLOY_SCRIPT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\worker_m1\deploy_m1.py"

ASSET_CATALOG = [
    {"num": 1, "sprite": "GFX_focus_GER_agadir_crisis_gambit", "dds_out": "focus_GER_agadir_crisis_gambit.dds", "src": os.path.join(SOURCE_BASE, "GFX_FRA_agadir_crisis-69194.dds")},
    {"num": 2, "sprite": "GFX_focus_GER_navy", "dds_out": "focus_GER_navy.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_GER_navy.png")},
    {"num": 3, "sprite": "GFX_focus_GER_berlin_baghdad_railway", "dds_out": "focus_GER_berlin_baghdad_railway.dds", "src": os.path.join(SOURCE_BASE, "GFX_TUR_baghdadberlin_railway-86221.dds")},
    {"num": 4, "sprite": "GFX_focus_GER_army_bill_1912", "dds_out": "focus_GER_army_bill_1912.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_militarism-86387.dds")},
    {"num": 5, "sprite": "GFX_focus_GER_centenary_of_leipzig_1913", "dds_out": "focus_GER_centenary_of_leipzig_1913.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_germanempire.dds")},
    {"num": 6, "sprite": "GFX_focus_GER_krupp", "dds_out": "focus_GER_krupp.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_GER_krupp.png")},
    {"num": 7, "sprite": "GFX_focus_ger_support_austrian_claims", "dds_out": "focus_ger_support_austrian_claims.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_ger_support_austrian_claims.png")},
    {"num": 8, "sprite": "GFX_focus_ger_around_maginot", "dds_out": "focus_ger_around_maginot.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_ger_around_maginot.png")},
    {"num": 9, "sprite": "GFX_ww1_mex_upca_conquer", "dds_out": "ww1_mex_upca_conquer.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_mex_upca_conquer.dds")},
    {"num": 10, "sprite": "GFX_focus_GER_the_miracle_of_tannenberg", "dds_out": "focus_GER_the_miracle_of_tannenberg.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_auftragstaktik-69190.dds")},
    {"num": 11, "sprite": "GFX_focus_GER_aufmarsch_ost_focus", "dds_out": "focus_GER_aufmarsch_ost_focus.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_russianempire.dds")},
    {"num": 12, "sprite": "GFX_focus_GER_haber_bosch_nitrogen_miracle", "dds_out": "focus_GER_haber_bosch_nitrogen_miracle.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_chemical_industry_expansion-73665.dds")},
    {"num": 13, "sprite": "GFX_ww1_nationalfocus_gasmask", "dds_out": "ww1_nationalfocus_gasmask.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_gasmask.dds")},
    {"num": 14, "sprite": "GFX_focus_OHL", "dds_out": "focus_OHL.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_OHL.png")},
    {"num": 15, "sprite": "GFX_ww1_nationalfocus_ironcross", "dds_out": "ww1_nationalfocus_ironcross.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_ironcross.dds")},
    {"num": 16, "sprite": "GFX_focus_GER_silent_dictatorship_ohl", "dds_out": "focus_GER_silent_dictatorship_ohl.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_military_dictatorship-86217.dds")},
    {"num": 17, "sprite": "GFX_focus_GER_unrestricted_submarine_warfare", "dds_out": "focus_GER_unrestricted_submarine_warfare.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_kriegsmarine.png")},
    {"num": 18, "sprite": "GFX_focus_GER_sealed_train_to_petrograd", "dds_out": "focus_GER_sealed_train_to_petrograd.dds", "src": os.path.join(SOURCE_BASE, "generic", "focus_generic_train.png")},
    {"num": 19, "sprite": "GFX_goal_deal_with_german_empire", "dds_out": "focus_deal_with_german_empire.dds", "src": os.path.join(SOURCE_BASE, "GER", "focus_deal_with_german_empire.png")},
    {"num": 20, "sprite": "GFX_focus_GER_the_kaiserschlacht_1918", "dds_out": "focus_GER_the_kaiserschlacht_1918.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_sturmtruppen-86215.dds")},
    {"num": 21, "sprite": "GFX_focus_GER_bethmann_civilian_supremacy", "dds_out": "focus_GER_bethmann_civilian_supremacy.dds", "src": os.path.join(SOURCE_BASE, "generic", "royal_prerogatives.png")},
    {"num": 22, "sprite": "GFX_focus_GER_prussian_franchise_reform", "dds_out": "focus_GER_prussian_franchise_reform.dds", "src": os.path.join(SOURCE_BASE, "generic", "goal_generic_socdem.png")},
    {"num": 23, "sprite": "GFX_focus_GER_reichstag_peace_resolution", "dds_out": "focus_GER_reichstag_peace_resolution.dds", "src": os.path.join(SOURCE_BASE, "GER", "expanded_duty.png")},
    {"num": 24, "sprite": "GFX_focus_GER_constitutional_monarchy_proclamation", "dds_out": "focus_GER_constitutional_monarchy_proclamation.dds", "src": os.path.join(SOURCE_BASE, "generic", "goal_royal_edicts2.png")},
    {"num": 25, "sprite": "GFX_focus_GER_found_vaterlandspartei", "dds_out": "focus_GER_found_vaterlandspartei.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_mllitary_leagues_demands-86384.dds")},
    {"num": 26, "sprite": "GFX_focus_GER_total_war_mobilization", "dds_out": "focus_GER_total_war_mobilization.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_auxiliary_service_law-87477.dds")},
    {"num": 27, "sprite": "GFX_focus_GER_annexation_of_belgium_and_briey", "dds_out": "focus_GER_annexation_of_belgium_and_briey.dds", "src": os.path.join(SOURCE_BASE, "generic", "second_belgian_award.png")},
    {"num": 28, "sprite": "GFX_focus_GER_morphed_mitteleuropa_iron_rule", "dds_out": "focus_GER_morphed_mitteleuropa_iron_rule.dds", "src": os.path.join(SOURCE_BASE, "GFX_GER_consolidate_central_powers-86219.dds")},
    {"num": 29, "sprite": "GFX_focus_GER_willy_nicky_telegrams_bjorko", "dds_out": "focus_GER_willy_nicky_telegrams_bjorko.dds", "src": os.path.join(SOURCE_BASE, "generic", "focus_deal_with_russia.png")},
    {"num": 30, "sprite": "GFX_ww1_nationalfocus_islam", "dds_out": "ww1_nationalfocus_islam.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_islam.dds")},
    {"num": 31, "sprite": "GFX_goal_generic_workers", "dds_out": "focus_socialist_worker.dds", "src": os.path.join(SOURCE_BASE, "generic", "focus_socialist_worker.png")},
    {"num": 32, "sprite": "GFX_focus_GER_emergency_danubian_annexation", "dds_out": "focus_GER_emergency_danubian_annexation.dds", "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_austriahungary.dds")},
]

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def parse_dds_header(filepath):
    with open(filepath, "rb") as f:
        magic = f.read(4)
        if magic != b"DDS ":
            return {"valid": False, "error": f"Invalid magic bytes: {magic}"}
        
        header_bytes = f.read(124)
        if len(header_bytes) < 124:
            return {"valid": False, "error": "Header too short (< 124 bytes)"}
        
        dwSize, dwFlags, dwHeight, dwWidth, dwPitchOrLinearSize, dwDepth, dwMipMapCount = struct.unpack("<7I", header_bytes[0:28])
        
        # Pixel format is at offset 72 (relative to header start, or 76 from file start)
        pf_bytes = header_bytes[72:104]
        pf_dwSize, pf_dwFlags, pf_dwFourCC, pf_dwRGBBitCount, pf_dwRBitMask, pf_dwGBitMask, pf_dwBBitMask, pf_dwABitMask = struct.unpack("<8I", pf_bytes)
        
        fourcc_str = "".join([chr((pf_dwFourCC >> (8 * i)) & 0xFF) for i in range(4)]) if pf_dwFlags & 0x4 else "UNCOMPRESSED"
        
        return {
            "valid": True,
            "dwSize": dwSize,
            "dwFlags": hex(dwFlags),
            "dwHeight": dwHeight,
            "dwWidth": dwWidth,
            "dwPitch": dwPitchOrLinearSize,
            "dwMipMapCount": dwMipMapCount,
            "pf_dwSize": pf_dwSize,
            "pf_dwFlags": hex(pf_dwFlags),
            "fourcc": fourcc_str,
            "rgb_bits": pf_dwRGBBitCount,
            "bitmasks": (hex(pf_dwRBitMask), hex(pf_dwGBitMask), hex(pf_dwBBitMask), hex(pf_dwABitMask))
        }

def parse_clausewitz_blocks(text):
    """
    Proper recursive / stack-based block extractor for Clausewitz syntax.
    Returns a list of top-level blocks inside the root scope.
    """
    # Strip comments
    lines = []
    for line in text.splitlines():
        if "#" in line:
            line = line.split("#")[0]
        lines.append(line)
    clean_text = "\n".join(lines)

    # Tokenize by { and } while tracking positions
    tokens = []
    idx = 0
    while idx < len(clean_text):
        ch = clean_text[idx]
        if ch in ("{", "}"):
            tokens.append((ch, idx))
            idx += 1
        elif ch == '"':
            # Skip string literal
            end_quote = clean_text.find('"', idx + 1)
            if end_quote == -1:
                idx += 1
            else:
                idx = end_quote + 1
        else:
            idx += 1

    # Now find SpriteType blocks
    import re
    # We find all occurrences of SpriteType = { and match their matching closing brace
    sprite_blocks = []
    pattern = re.compile(r'SpriteType\s*=\s*\{', re.IGNORECASE)
    for match in pattern.finditer(clean_text):
        start_brace_pos = match.end() - 1
        # find matching closing brace
        depth = 0
        end_brace_pos = None
        for ch, pos in tokens:
            if pos < start_brace_pos:
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end_brace_pos = pos
                    break
        if end_brace_pos is not None:
            block_content = clean_text[start_brace_pos + 1 : end_brace_pos]
            sprite_blocks.append(block_content)
        else:
            raise ValueError(f"Unclosed SpriteType block starting at position {match.start()}")

    return sprite_blocks

def run_audit():
    results = {
        "dds_checks": [],
        "gfx_checks": {},
        "prohibited_patterns": [],
        "overall_status": "CLEAN"
    }

    print("=== FORENSIC CHECK 1: DIRECTORY & FILE ENUMERATION ===")
    if not os.path.exists(TARGET_GOALS_DIR):
        print(f"FAIL: {TARGET_GOALS_DIR} does not exist!")
        results["overall_status"] = "INTEGRITY VIOLATION"
        return results

    files_in_goals = os.listdir(TARGET_GOALS_DIR)
    print(f"Total files in goals directory: {len(files_in_goals)}")
    if len(files_in_goals) != 32:
        print(f"FAIL: Expected 32 files, found {len(files_in_goals)}")
        results["overall_status"] = "INTEGRITY VIOLATION"

    print("\n=== FORENSIC CHECK 2: DDS BINARY HEADER & PAYLOAD VALIDATION ===")
    for item in ASSET_CATALOG:
        dds_name = item["dds_out"]
        dds_path = os.path.join(TARGET_GOALS_DIR, dds_name)
        src_path = item["src"]
        is_source_dds = src_path.lower().endswith(".dds")
        
        entry = {
            "num": item["num"],
            "file": dds_name,
            "source": src_path,
            "source_type": "DDS" if is_source_dds else "PNG",
            "errors": []
        }
        
        if not os.path.exists(dds_path):
            entry["errors"].append("File missing on disk")
            results["dds_checks"].append(entry)
            results["overall_status"] = "INTEGRITY VIOLATION"
            continue
            
        file_size = os.path.getsize(dds_path)
        entry["file_size"] = file_size
        if file_size < 128:
            entry["errors"].append(f"File size {file_size} is less than DDS header (128 bytes)")
            
        hdr = parse_dds_header(dds_path)
        entry["header"] = hdr
        if not hdr.get("valid"):
            entry["errors"].append(f"DDS header invalid: {hdr.get('error')}")
        else:
            if hdr["dwSize"] != 124:
                entry["errors"].append(f"dwSize != 124 ({hdr['dwSize']})")
            if hdr["dwHeight"] <= 0 or hdr["dwWidth"] <= 0:
                entry["errors"].append(f"Invalid dimensions: {hdr['dwWidth']}x{hdr['dwHeight']}")
            if hdr["pf_dwSize"] != 32:
                entry["errors"].append(f"PixelFormat dwSize != 32 ({hdr['pf_dwSize']})")

        # Check visual content and entropy
        try:
            with Image.open(dds_path) as im:
                im_rgba = im.convert("RGBA")
                arr = np.array(im_rgba)
                entry["dimensions"] = f"{im.size[0]}x{im.size[1]}"
                entry["mode"] = im.mode
                
                # Check for blank / dummy image (all zeros or constant value)
                std_dev = np.std(arr)
                entry["std_dev"] = float(std_dev)
                if std_dev < 1.0:
                    entry["errors"].append(f"Image appears to be dummy/solid stub (std_dev = {std_dev:.2f})")
                
                # If source was DDS, verify identical copy
                if is_source_dds:
                    target_hash = sha256_file(dds_path)
                    src_hash = sha256_file(src_path)
                    entry["target_sha256"] = target_hash
                    entry["src_sha256"] = src_hash
                    if target_hash != src_hash:
                        entry["errors"].append(f"Hash mismatch with workshop source: {target_hash} vs {src_hash}")
                    else:
                        entry["provenance"] = "VERIFIED_IDENTICAL_TO_WORKSHOP_DDS"
                else:
                    # If source was PNG, compare dimensions and pixel correlation
                    with Image.open(src_path) as src_im:
                        src_rgba = src_im.convert("RGBA")
                        src_arr = np.array(src_rgba)
                        if src_im.size != im.size:
                            entry["errors"].append(f"Dimension mismatch: source {src_im.size} vs target {im.size}")
                        else:
                            # Mean squared error
                            mse = np.mean((arr.astype("float") - src_arr.astype("float")) ** 2)
                            entry["mse_vs_source_png"] = float(mse)
                            if mse > 50.0:
                                entry["errors"].append(f"Significant difference from source PNG (MSE = {mse:.2f})")
                            else:
                                entry["provenance"] = f"VERIFIED_GENUINE_CONVERSION_FROM_WORKSHOP_PNG (MSE={mse:.2f})"
        except Exception as e:
            entry["errors"].append(f"Pillow failed to open DDS: {str(e)}")

        status_str = "PASS" if not entry["errors"] else f"FAIL ({len(entry['errors'])} errors: {', '.join(entry['errors'])})"
        print(f"[{item['num']:02d}/32] {dds_name:<48} | Size: {file_size:>5} B | Format: {hdr.get('fourcc', 'N/A'):<12} | Dim: {entry.get('dimensions', 'N/A'):<8} | Prov: {entry.get('provenance', 'N/A')[:35]} | {status_str}")
        
        if entry["errors"]:
            results["overall_status"] = "INTEGRITY VIOLATION"
        results["dds_checks"].append(entry)

    print("\n=== FORENSIC CHECK 3: CLAUSEWITZ GFX SCRIPT PARSING & VALIDATION ===")
    if not os.path.exists(TARGET_GFX_FILE):
        print(f"FAIL: {TARGET_GFX_FILE} does not exist!")
        results["overall_status"] = "INTEGRITY VIOLATION"
        return results

    with open(TARGET_GFX_FILE, "r", encoding="utf-8") as f:
        gfx_text = f.read()

    # Stack-based brace validator
    brace_stack = []
    lines = gfx_text.splitlines()
    syntax_errors = []
    for line_idx, line in enumerate(lines, 1):
        clean_line = line.split("#")[0] # remove comments
        for char_idx, ch in enumerate(clean_line, 1):
            if ch == "{":
                brace_stack.append((line_idx, char_idx))
            elif ch == "}":
                if not brace_stack:
                    syntax_errors.append(f"Unmatched closing brace at line {line_idx}, col {char_idx}")
                else:
                    brace_stack.pop()

    if brace_stack:
        for unclosed in brace_stack:
            syntax_errors.append(f"Unclosed opening brace from line {unclosed[0]}, col {unclosed[1]}")

    results["gfx_checks"]["brace_balance_errors"] = syntax_errors
    results["gfx_checks"]["total_open_braces"] = gfx_text.count("{")
    results["gfx_checks"]["total_close_braces"] = gfx_text.count("}")

    print(f"Braces: {results['gfx_checks']['total_open_braces']} open, {results['gfx_checks']['total_close_braces']} close. Syntax errors: {len(syntax_errors)}")
    if syntax_errors:
        results["overall_status"] = "INTEGRITY VIOLATION"

    # Block parser for SpriteTypes using AST stack
    sprite_blocks = parse_clausewitz_blocks(gfx_text)
    print(f"Total SpriteType blocks parsed: {len(sprite_blocks)}")
    results["gfx_checks"]["sprite_blocks_count"] = len(sprite_blocks)

    if len(sprite_blocks) != 64:
        print(f"FAIL: Expected 64 SpriteType blocks, found {len(sprite_blocks)}")
        results["overall_status"] = "INTEGRITY VIOLATION"

    import re
    base_sprites_found = {}
    shine_sprites_found = {}
    for block in sprite_blocks:
        name_match = re.search(r'name\s*=\s*"([^"]+)"', block)
        tex_match = re.search(r'(?<!animation)texturefile\s*=\s*"([^"]+)"', block)
        
        if not name_match:
            syntax_errors.append("SpriteType block missing name definition")
            continue
        if not tex_match:
            syntax_errors.append(f"SpriteType {name_match.group(1)} missing texturefile")
            continue
            
        sname = name_match.group(1)
        stex = tex_match.group(1)
        
        # Check referenced file exists
        full_tex_path = os.path.join(r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1", stex.replace("/", os.sep))
        tex_exists = os.path.exists(full_tex_path)
        
        if not tex_exists:
            syntax_errors.append(f"Referenced texture does not exist: {full_tex_path}")
            
        if sname.endswith("_shine"):
            # Validate shine block structure
            has_anim1 = "animationrotation = -90.0" in block
            has_anim2 = "animationrotation = 90.0" in block
            has_effect = 'effectFile = "gfx/FX/buttonstate.lua"' in block
            has_lazy = "legacy_lazy_load = no" in block
            shine_sprites_found[sname] = {
                "texture": stex,
                "tex_exists": tex_exists,
                "has_dual_anim": (has_anim1 and has_anim2),
                "has_effect": has_effect,
                "has_lazy": has_lazy
            }
        else:
            base_sprites_found[sname] = {
                "texture": stex,
                "tex_exists": tex_exists
            }

    print(f"Base sprites parsed: {len(base_sprites_found)}/32")
    print(f"Shine sprites parsed: {len(shine_sprites_found)}/32")
    results["gfx_checks"]["base_sprites_count"] = len(base_sprites_found)
    results["gfx_checks"]["shine_sprites_count"] = len(shine_sprites_found)

    # Check 1:1 correspondence
    for item in ASSET_CATALOG:
        expected_base = item["sprite"]
        expected_shine = f"{expected_base}_shine"
        
        if expected_base not in base_sprites_found:
            print(f"FAIL: Missing base sprite: {expected_base}")
            results["overall_status"] = "INTEGRITY VIOLATION"
        if expected_shine not in shine_sprites_found:
            print(f"FAIL: Missing shine sprite: {expected_shine}")
            results["overall_status"] = "INTEGRITY VIOLATION"
        else:
            shine_info = shine_sprites_found[expected_shine]
            if not shine_info["has_dual_anim"] or not shine_info["has_effect"] or not shine_info["has_lazy"]:
                print(f"FAIL: Shine sprite {expected_shine} has incomplete animation definitions: {shine_info}")
                results["overall_status"] = "INTEGRITY VIOLATION"

    print("\n=== FORENSIC CHECK 4: PROHIBITED PATTERNS SCAN ===")
    with open(DEPLOY_SCRIPT, "r", encoding="utf-8") as f:
        deploy_content = f.read()

    prohibited = []
    if "return True" in deploy_content and "def step" in deploy_content:
        prohibited.append("Mocked step function returning constant True")
    
    for fname in os.listdir(TARGET_GOALS_DIR):
        fpath = os.path.join(TARGET_GOALS_DIR, fname)
        if os.path.getsize(fpath) == 0:
            prohibited.append(f"0-byte file: {fname}")

    results["prohibited_patterns"] = prohibited
    print(f"Prohibited patterns found: {len(prohibited)}")
    if prohibited:
        results["overall_status"] = "INTEGRITY VIOLATION"

    print("\n" + "=" * 60)
    print(f"FINAL FORENSIC VERDICT: {results['overall_status']}")
    print("=" * 60)
    
    report_json_path = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\auditor_m1_1\forensic_results.json"
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Detailed forensic results written to {report_json_path}")
    return results

if __name__ == "__main__":
    run_audit()
