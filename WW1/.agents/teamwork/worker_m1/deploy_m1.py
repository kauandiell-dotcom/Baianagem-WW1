import os
import shutil
import sys
from PIL import Image

SOURCE_BASE = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3106240385\gfx\interface\goals"
TARGET_GOALS_DIR = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\gfx\interface\goals"
TARGET_GFX_FILE = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\interface\ww1_germany_goals.gfx"

# Exact 32 mapping entries
ASSET_CATALOG = [
    {
        "num": 1,
        "desc": "Agadir Crisis Gambit",
        "sprite": "GFX_focus_GER_agadir_crisis_gambit",
        "dds_out": "focus_GER_agadir_crisis_gambit.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_FRA_agadir_crisis-69194.dds"),
    },
    {
        "num": 2,
        "desc": "Tirpitz Fourth Naval Bill",
        "sprite": "GFX_focus_GER_navy",
        "dds_out": "focus_GER_navy.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_GER_navy.png"),
    },
    {
        "num": 3,
        "desc": "Berlin-Baghdad Railway",
        "sprite": "GFX_focus_GER_berlin_baghdad_railway",
        "dds_out": "focus_GER_berlin_baghdad_railway.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_TUR_baghdadberlin_railway-86221.dds"),
    },
    {
        "num": 4,
        "desc": "Army Bill 1912",
        "sprite": "GFX_focus_GER_army_bill_1912",
        "dds_out": "focus_GER_army_bill_1912.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_militarism-86387.dds"),
    },
    {
        "num": 5,
        "desc": "Centenary of Leipzig 1913",
        "sprite": "GFX_focus_GER_centenary_of_leipzig_1913",
        "dds_out": "focus_GER_centenary_of_leipzig_1913.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_germanempire.dds"),
    },
    {
        "num": 6,
        "desc": "Krupp Heavy Howitzers",
        "sprite": "GFX_focus_GER_krupp",
        "dds_out": "focus_GER_krupp.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_GER_krupp.png"),
    },
    {
        "num": 7,
        "desc": "Blank Cheque",
        "sprite": "GFX_focus_ger_support_austrian_claims",
        "dds_out": "focus_ger_support_austrian_claims.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_ger_support_austrian_claims.png"),
    },
    {
        "num": 8,
        "desc": "Schlieffen Plan",
        "sprite": "GFX_focus_ger_around_maginot",
        "dds_out": "focus_ger_around_maginot.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_ger_around_maginot.png"),
    },
    {
        "num": 9,
        "desc": "Smash Liege Forts",
        "sprite": "GFX_ww1_mex_upca_conquer",
        "dds_out": "ww1_mex_upca_conquer.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_mex_upca_conquer.dds"),
    },
    {
        "num": 10,
        "desc": "Tannenberg Triumph",
        "sprite": "GFX_focus_GER_the_miracle_of_tannenberg",
        "dds_out": "focus_GER_the_miracle_of_tannenberg.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_auftragstaktik-69190.dds"),
    },
    {
        "num": 11,
        "desc": "Aufmarsch Ost Focus",
        "sprite": "GFX_focus_GER_aufmarsch_ost_focus",
        "dds_out": "focus_GER_aufmarsch_ost_focus.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_russianempire.dds"),
    },
    {
        "num": 12,
        "desc": "Haber-Bosch Nitrogen Miracle",
        "sprite": "GFX_focus_GER_haber_bosch_nitrogen_miracle",
        "dds_out": "focus_GER_haber_bosch_nitrogen_miracle.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_chemical_industry_expansion-73665.dds"),
    },
    {
        "num": 13,
        "desc": "Chemical Warfare Initiative",
        "sprite": "GFX_ww1_nationalfocus_gasmask",
        "dds_out": "ww1_nationalfocus_gasmask.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_gasmask.dds"),
    },
    {
        "num": 14,
        "desc": "Hindenburg Program",
        "sprite": "GFX_focus_OHL",
        "dds_out": "focus_OHL.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_OHL.png"),
    },
    {
        "num": 15,
        "desc": "Stosstruppen Tactics",
        "sprite": "GFX_ww1_nationalfocus_ironcross",
        "dds_out": "ww1_nationalfocus_ironcross.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_ironcross.dds"),
    },
    {
        "num": 16,
        "desc": "OHL Silent Dictatorship",
        "sprite": "GFX_focus_GER_silent_dictatorship_ohl",
        "dds_out": "focus_GER_silent_dictatorship_ohl.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_military_dictatorship-86217.dds"),
    },
    {
        "num": 17,
        "desc": "Unrestricted Submarine Warfare",
        "sprite": "GFX_focus_GER_unrestricted_submarine_warfare",
        "dds_out": "focus_GER_unrestricted_submarine_warfare.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_kriegsmarine.png"),
    },
    {
        "num": 18,
        "desc": "Sealed Train to Petrograd",
        "sprite": "GFX_focus_GER_sealed_train_to_petrograd",
        "dds_out": "focus_GER_sealed_train_to_petrograd.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "focus_generic_train.png"),
    },
    {
        "num": 19,
        "desc": "Treaty of Brest-Litovsk",
        "sprite": "GFX_goal_deal_with_german_empire",
        "dds_out": "focus_deal_with_german_empire.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "focus_deal_with_german_empire.png"),
    },
    {
        "num": 20,
        "desc": "The 1918 Kaiserschlacht",
        "sprite": "GFX_focus_GER_the_kaiserschlacht_1918",
        "dds_out": "focus_GER_the_kaiserschlacht_1918.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_sturmtruppen-86215.dds"),
    },
    {
        "num": 21,
        "desc": "Civilian Supremacy (Bethmann)",
        "sprite": "GFX_focus_GER_bethmann_civilian_supremacy",
        "dds_out": "focus_GER_bethmann_civilian_supremacy.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "royal_prerogatives.png"),
    },
    {
        "num": 22,
        "desc": "Prussian Franchise Reform",
        "sprite": "GFX_focus_GER_prussian_franchise_reform",
        "dds_out": "focus_GER_prussian_franchise_reform.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "goal_generic_socdem.png"),
    },
    {
        "num": 23,
        "desc": "Reichstag Peace Resolution",
        "sprite": "GFX_focus_GER_reichstag_peace_resolution",
        "dds_out": "focus_GER_reichstag_peace_resolution.dds",
        "src": os.path.join(SOURCE_BASE, "GER", "expanded_duty.png"),
    },
    {
        "num": 24,
        "desc": "Constitutional Monarchy Proclamation",
        "sprite": "GFX_focus_GER_constitutional_monarchy_proclamation",
        "dds_out": "focus_GER_constitutional_monarchy_proclamation.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "goal_royal_edicts2.png"),
    },
    {
        "num": 25,
        "desc": "Found Vaterlandspartei",
        "sprite": "GFX_focus_GER_found_vaterlandspartei",
        "dds_out": "focus_GER_found_vaterlandspartei.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_mllitary_leagues_demands-86384.dds"),
    },
    {
        "num": 26,
        "desc": "Total War Mobilization",
        "sprite": "GFX_focus_GER_total_war_mobilization",
        "dds_out": "focus_GER_total_war_mobilization.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_auxiliary_service_law-87477.dds"),
    },
    {
        "num": 27,
        "desc": "Annexation of Belgium and Briey",
        "sprite": "GFX_focus_GER_annexation_of_belgium_and_briey",
        "dds_out": "focus_GER_annexation_of_belgium_and_briey.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "second_belgian_award.png"),
    },
    {
        "num": 28,
        "desc": "Mitteleuropa Iron Rule",
        "sprite": "GFX_focus_GER_morphed_mitteleuropa_iron_rule",
        "dds_out": "focus_GER_morphed_mitteleuropa_iron_rule.dds",
        "src": os.path.join(SOURCE_BASE, "GFX_GER_consolidate_central_powers-86219.dds"),
    },
    {
        "num": 29,
        "desc": "Willy-Nicky Telegrams (Bjorko 2.0)",
        "sprite": "GFX_focus_GER_willy_nicky_telegrams_bjorko",
        "dds_out": "focus_GER_willy_nicky_telegrams_bjorko.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "focus_deal_with_russia.png"),
    },
    {
        "num": 30,
        "desc": "Hajj Wilhelm Crusade",
        "sprite": "GFX_ww1_nationalfocus_islam",
        "dds_out": "ww1_nationalfocus_islam.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_islam.dds"),
    },
    {
        "num": 31,
        "desc": "Spartakusbund Revolt",
        "sprite": "GFX_goal_generic_workers",
        "dds_out": "focus_socialist_worker.dds",
        "src": os.path.join(SOURCE_BASE, "generic", "focus_socialist_worker.png"),
    },
    {
        "num": 32,
        "desc": "Emergency Danubian Annexation",
        "sprite": "GFX_focus_GER_emergency_danubian_annexation",
        "dds_out": "focus_GER_emergency_danubian_annexation.dds",
        "src": os.path.join(SOURCE_BASE, "hoi4tgw", "ww1_nationalfocus_austriahungary.dds"),
    },
]

def step1_deploy_dds():
    print("=== Step 1: Deploying DDS files ===")
    os.makedirs(TARGET_GOALS_DIR, exist_ok=True)
    deployed_files = []
    
    for item in ASSET_CATALOG:
        dds_out = item["dds_out"]
        src = item["src"]
        dest = os.path.join(TARGET_GOALS_DIR, dds_out)
        
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source file not found: {src}")
            
        if src.lower().endswith(".dds"):
            shutil.copyfile(src, dest)
            method = "COPIED_DDS"
        else:
            im = Image.open(src)
            if im.mode != "RGBA":
                im = im.convert("RGBA")
            im.save(dest, format="DDS")
            method = "CONVERTED_PNG_TO_DDS"
            
        file_size = os.path.getsize(dest)
        assert file_size > 0, f"File {dest} is 0 bytes!"
        deployed_files.append((dds_out, method, file_size))
        print(f"[{item['num']:02d}/32] {dds_out} ({method}, {file_size} bytes)")
        
    print(f"Successfully deployed all {len(deployed_files)} DDS files to {TARGET_GOALS_DIR}.\n")
    return deployed_files

def step2_generate_gfx():
    print("=== Step 2: Generating ww1_germany_goals.gfx ===")
    os.makedirs(os.path.dirname(TARGET_GFX_FILE), exist_ok=True)
    
    lines = []
    lines.append("spriteTypes = {")
    lines.append("")
    
    for item in ASSET_CATALOG:
        num = item["num"]
        desc = item["desc"]
        sprite = item["sprite"]
        dds = item["dds_out"]
        tex_path = f"gfx/interface/goals/{dds}"
        
        lines.append(f"\t### {num}. {desc}")
        # Base SpriteType
        lines.append("\tSpriteType = {")
        lines.append(f'\t\tname = "{sprite}"')
        lines.append(f'\t\ttexturefile = "{tex_path}"')
        lines.append("\t}")
        
        # Shine SpriteType
        lines.append("\tSpriteType = {")
        lines.append(f'\t\tname = "{sprite}_shine"')
        lines.append(f'\t\ttexturefile = "{tex_path}"')
        lines.append('\t\teffectFile = "gfx/FX/buttonstate.lua"')
        lines.append("\t\tanimation = {")
        lines.append(f'\t\t\tanimationmaskfile = "{tex_path}"')
        lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"')
        lines.append("\t\t\tanimationrotation = -90.0")
        lines.append("\t\t\tanimationlooping = no")
        lines.append("\t\t\tanimationtime = 0.75")
        lines.append("\t\t\tanimationdelay = 0")
        lines.append('\t\t\tanimationblendmode = "add"')
        lines.append('\t\t\tanimationtype = "scrolling"')
        lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
        lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }")
        lines.append("\t\t}")
        lines.append("\t\tanimation = {")
        lines.append(f'\t\t\tanimationmaskfile = "{tex_path}"')
        lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"')
        lines.append("\t\t\tanimationrotation = 90.0")
        lines.append("\t\t\tanimationlooping = no")
        lines.append("\t\t\tanimationtime = 0.75")
        lines.append("\t\t\tanimationdelay = 0")
        lines.append('\t\t\tanimationblendmode = "add"')
        lines.append('\t\t\tanimationtype = "scrolling"')
        lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
        lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }")
        lines.append("\t\t}")
        lines.append("\t\tlegacy_lazy_load = no")
        lines.append("\t}")
        lines.append("")
        
    lines.append("}")
    lines.append("")
    
    content = "\n".join(lines)
    with open(TARGET_GFX_FILE, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Generated {TARGET_GFX_FILE} with {len(lines)} lines.\n")

def step3_verify():
    print("=== Step 3: Verifying deployment and syntax ===")
    
    # Check all DDS files exist and are non-empty
    dds_files_found = 0
    for item in ASSET_CATALOG:
        dds_path = os.path.join(TARGET_GOALS_DIR, item["dds_out"])
        assert os.path.exists(dds_path), f"Missing DDS file: {dds_path}"
        sz = os.path.getsize(dds_path)
        assert sz > 0, f"DDS file is empty: {dds_path}"
        
        # Verify Pillow can open it
        with Image.open(dds_path) as img:
            assert img.size[0] > 0 and img.size[1] > 0, f"Invalid dimensions for {dds_path}"
            assert img.mode in ("RGBA", "RGB"), f"Unexpected mode {img.mode} for {dds_path}"
        dds_files_found += 1
        
    print(f"Verification 1: All {dds_files_found}/32 DDS files exist, non-empty, and valid images.")
    
    # Check braces balance in TARGET_GFX_FILE
    with open(TARGET_GFX_FILE, "r", encoding="utf-8") as f:
        gfx_text = f.read()
        
    open_braces = gfx_text.count("{")
    close_braces = gfx_text.count("}")
    
    print(f"Verification 2: Braces count in ww1_germany_goals.gfx:")
    print(f"  Opening braces '{{': {open_braces}")
    print(f"  Closing braces '}}': {close_braces}")
    assert open_braces == 257, f"Expected 257 opening braces, got {open_braces}"
    assert close_braces == 257, f"Expected 257 closing braces, got {close_braces}"
    assert open_braces == close_braces, "Brace mismatch!"
    
    # Count SpriteType entries
    import re
    sprite_types = re.findall(r"SpriteType\s*=", gfx_text, re.IGNORECASE)
    print(f"Verification 3: SpriteType count: {len(sprite_types)}")
    assert len(sprite_types) == 64, f"Expected 64 SpriteTypes, got {len(sprite_types)}"
    
    print("\nALL VERIFICATIONS PASSED 100%!")

if __name__ == "__main__":
    step1_deploy_dds()
    step2_generate_gfx()
    step3_verify()
