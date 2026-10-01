import os
import re
from PIL import Image

TARGET_GOALS_DIR = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\gfx\interface\goals"
TARGET_GFX_FILE = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\interface\ww1_germany_goals.gfx"

EXPECTED_DDS = [
    "focus_GER_agadir_crisis_gambit.dds",
    "focus_GER_navy.dds",
    "focus_GER_berlin_baghdad_railway.dds",
    "focus_GER_army_bill_1912.dds",
    "focus_GER_centenary_of_leipzig_1913.dds",
    "focus_GER_krupp.dds",
    "focus_ger_support_austrian_claims.dds",
    "focus_ger_around_maginot.dds",
    "ww1_mex_upca_conquer.dds",
    "focus_GER_the_miracle_of_tannenberg.dds",
    "focus_GER_aufmarsch_ost_focus.dds",
    "focus_GER_haber_bosch_nitrogen_miracle.dds",
    "ww1_nationalfocus_gasmask.dds",
    "focus_OHL.dds",
    "ww1_nationalfocus_ironcross.dds",
    "focus_GER_silent_dictatorship_ohl.dds",
    "focus_GER_unrestricted_submarine_warfare.dds",
    "focus_GER_sealed_train_to_petrograd.dds",
    "focus_deal_with_german_empire.dds",
    "focus_GER_the_kaiserschlacht_1918.dds",
    "focus_GER_bethmann_civilian_supremacy.dds",
    "focus_GER_prussian_franchise_reform.dds",
    "focus_GER_reichstag_peace_resolution.dds",
    "focus_GER_constitutional_monarchy_proclamation.dds",
    "focus_GER_found_vaterlandspartei.dds",
    "focus_GER_total_war_mobilization.dds",
    "focus_GER_annexation_of_belgium_and_briey.dds",
    "focus_GER_morphed_mitteleuropa_iron_rule.dds",
    "focus_GER_willy_nicky_telegrams_bjorko.dds",
    "ww1_nationalfocus_islam.dds",
    "focus_socialist_worker.dds",
    "focus_GER_emergency_danubian_annexation.dds",
]

def verify_all():
    print("=" * 60)
    print("INDEPENDENT VERIFICATION AUDIT - MILESTONE 1")
    print("=" * 60)
    
    # Check DDS files
    print("\n--- 1. Checking 32 DDS Focus Icons ---")
    assert os.path.exists(TARGET_GOALS_DIR), f"Directory {TARGET_GOALS_DIR} does not exist!"
    
    actual_files = os.listdir(TARGET_GOALS_DIR)
    print(f"Total files in {TARGET_GOALS_DIR}: {len(actual_files)}")
    assert len(actual_files) == 32, f"Expected 32 files, found {len(actual_files)}"
    
    for idx, dds in enumerate(EXPECTED_DDS, 1):
        full_path = os.path.join(TARGET_GOALS_DIR, dds)
        assert os.path.exists(full_path), f"File {dds} is missing!"
        size = os.path.getsize(full_path)
        assert size > 0, f"File {dds} has 0 bytes!"
        with Image.open(full_path) as im:
            width, height = im.size
            mode = im.mode
            fmt = im.format
        print(f"[{idx:02d}/32] OK: {dds:<50} ({size:>5} bytes, {width}x{height}, mode={mode}, format={fmt})")
        
    print("\n--- 2. Checking ww1_germany_goals.gfx ---")
    assert os.path.exists(TARGET_GFX_FILE), f"File {TARGET_GFX_FILE} does not exist!"
    with open(TARGET_GFX_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    open_braces = content.count("{")
    close_braces = content.count("}")
    print(f"Opening braces: {open_braces}")
    print(f"Closing braces: {close_braces}")
    assert open_braces == 257, f"Expected 257 opening braces, found {open_braces}"
    assert close_braces == 257, f"Expected 257 closing braces, found {close_braces}"
    assert open_braces == close_braces, "Brace imbalance detected!"
    
    # Check SpriteTypes
    all_sprites = re.findall(r'name\s*=\s*"([^"]+)"', content)
    base_sprites = [s for s in all_sprites if not s.endswith("_shine")]
    shine_sprites = [s for s in all_sprites if s.endswith("_shine")]
    
    print(f"Total Sprite names found: {len(all_sprites)} ({len(base_sprites)} base, {len(shine_sprites)} shine)")
    assert len(all_sprites) == 64, f"Expected 64 sprite definitions, found {len(all_sprites)}"
    assert len(base_sprites) == 32, f"Expected 32 base sprites, found {len(base_sprites)}"
    assert len(shine_sprites) == 32, f"Expected 32 shine sprites, found {len(shine_sprites)}"
    
    # Verify every texturefile exists in the directory
    texture_paths = re.findall(r'(?<!animation)texturefile\s*=\s*"([^"]+)"', content)
    print(f"Total direct texturefile references: {len(texture_paths)}")
    assert len(texture_paths) == 64, f"Expected 64 direct texture references, found {len(texture_paths)}"
    
    unique_textures = set(texture_paths)
    print(f"Unique direct textures referenced: {len(unique_textures)}")
    assert len(unique_textures) == 32, f"Expected 32 unique texture references, found {len(unique_textures)}"
    
    for tp in unique_textures:
        filename = os.path.basename(tp)
        local_path = os.path.join(TARGET_GOALS_DIR, filename)
        assert os.path.exists(local_path), f"Referenced texture does not exist: {local_path}"
        
    print("\n" + "=" * 60)
    print("ALL AUDIT CRITERIA PASSED: 32/32 DDS VALID, 64 SPRITES VALID, 257/257 BRACES BALANCED")
    print("=" * 60)

if __name__ == "__main__":
    verify_all()
