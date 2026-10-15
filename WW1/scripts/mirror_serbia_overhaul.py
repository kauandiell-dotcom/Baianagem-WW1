import os
import shutil

SRC_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"
DST_ROOT = r"E:\SteamLibrary\steamapps\workshop\content\394360\3809191491"

FILES = [
    r"common\bop\SER_bop.txt",
    r"common\characters\SER.txt",
    r"common\country_leader\ww1_serbia_traits.txt",
    r"common\decisions\categories\ww1_serbia_decision_categories.txt",
    r"common\decisions\ww1_serbia_decisions.txt",
    r"common\decisions\ww1_serbia_retreat_decisions.txt",
    r"common\ideas\ww1_serbia_ideas.txt",
    r"common\national_focus\serbia.txt",
    r"common\on_actions\zz_ww1_ger_rus_rework_on_actions.txt",
    r"common\scripted_effects\ww1_serbia_bop_effects.txt",
    r"events\ww1_serbia_events.txt",
    r"events\ww1_serbia_retreat_events.txt",
    r"history\countries\SER - Serbia.txt",
    r"localisation\english\ww1_serbia_l_english.yml",
    r"localisation\braz_por\ww1_serbia_l_braz_por.yml",
]

def mirror():
    print(f"Target mirror directory: {DST_ROOT}")
    if not os.path.exists(DST_ROOT):
        raise FileNotFoundError(f"Destination folder does not exist: {DST_ROOT}")
    
    success = 0
    for rel_path in FILES:
        src = os.path.join(SRC_ROOT, rel_path)
        dst = os.path.join(DST_ROOT, rel_path)
        
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source file missing: {src}")
            
        dst_dir = os.path.dirname(dst)
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copy2(src, dst)
        
        src_size = os.path.getsize(src)
        dst_size = os.path.getsize(dst)
        assert src_size == dst_size, f"Size mismatch for {rel_path}: {src_size} vs {dst_size}"
        print(f"[MIRRORED] {rel_path} ({src_size} bytes)")
        success += 1
        
    print(f"\nSuccessfully mirrored all {success}/{len(FILES)} files to Steam Workshop staging!")

if __name__ == "__main__":
    mirror()
