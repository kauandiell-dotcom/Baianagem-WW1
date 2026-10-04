import os
import sys
import shutil
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from france_builder.data_foci import FRENCH_FOCI
from france_builder.data_ideas import FRENCH_IDEAS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DONOR_GOALS = [
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3106240385\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3365515312\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2716194283\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2076426030\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3797323750\gfx\interface\goals',
    os.path.join(BASE_DIR, 'gfx', 'interface', 'goals'),
]

DONOR_IDEAS = [
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3106240385\gfx\interface\ideas',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3365515312\gfx\interface\ideas',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2716194283\gfx\interface\ideas',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2076426030\gfx\interface\ideas',
    os.path.join(BASE_DIR, 'gfx', 'interface', 'ideas'),
]

def tokenize(s):
    return set(re.findall(r'[a-zA-Z]{3,}', s.lower()))

STOPWORDS = {'the', 'and', 'for', 'with', 'from', 'our', 'les', 'des', 'une', 'qui', 'par', 'sur', 'dans', 'pour', 'plus', 'tous'}

def build_catalog(dirs):
    cat = []
    for d in dirs:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower().endswith(('.dds', '.png')):
                    base = os.path.splitext(f)[0].lower()
                    cat.append((base, os.path.join(root, f)))
    return cat

def harvest_goals():
    print("Building Goal Catalog...")
    catalog = build_catalog(DONOR_GOALS)
    print(f"Goal Catalog contains {len(catalog)} icons.")

    dest_dir = os.path.join(BASE_DIR, "gfx", "interface", "goals")
    os.makedirs(dest_dir, exist_ok=True)

    used_paths = set()
    focus_icon_files = {}

    for f in FRENCH_FOCI:
        fid = f['id']
        queries = [q.lower().replace('gfx_', '') for q in f.get('icon_query', [])]
        f_tokens = (tokenize(fid) | tokenize(f.get('title', ''))) - STOPWORDS
        
        best_cand = None
        best_score = -1
        
        # 1. Direct query match
        for q in queries:
            for base, full in catalog:
                if full in used_paths:
                    continue
                if base == q or base == 'gfx_' + q:
                    score = 1000
                    if score > best_score:
                        best_score = score
                        best_cand = full
                        break
            if best_score >= 1000:
                break
                
        # 2. Substring query match
        if best_score < 1000:
            for q in queries:
                q_clean = q.replace('gfx_', '')
                for base, full in catalog:
                    if full in used_paths:
                        continue
                    if q_clean in base:
                        score = 500 + len(q_clean)
                        if score > best_score:
                            best_score = score
                            best_cand = full
                            
        # 3. Token overlap match
        if best_score < 500:
            for base, full in catalog:
                if full in used_paths:
                    continue
                b_tokens = tokenize(base) - STOPWORDS
                overlap = len(f_tokens & b_tokens)
                if overlap > 0:
                    score = overlap * 50
                    if 'fra' in base or 'french' in base:
                        score += 40
                    if score > best_score:
                        best_score = score
                        best_cand = full

        # 4. Fallback: first unused candidate
        if not best_cand:
            for base, full in catalog:
                if full not in used_paths:
                    best_cand = full
                    break

        used_paths.add(best_cand)
        ext = os.path.splitext(best_cand)[1].lower()
        dest_filename = f"GFX_{fid}{ext}"
        dest_path = os.path.join(dest_dir, dest_filename)
        shutil.copy2(best_cand, dest_path)
        focus_icon_files[fid] = (dest_filename, ext)

    print(f"Copied {len(focus_icon_files)} goal textures to {dest_dir}.")

    # Write interface/ww1_france_goals.gfx
    gfx_out = os.path.join(BASE_DIR, "interface", "ww1_france_goals.gfx")
    with open(gfx_out, "w", encoding="utf-8") as out:
        out.write('spriteTypes = {\n\n')
        for fid in sorted(focus_icon_files.keys()):
            fname, ext = focus_icon_files[fid]
            rel_path = f"gfx/interface/goals/{fname}"
            
            # Base sprite
            out.write(f'\tspriteType = {{\n')
            out.write(f'\t\tname = "GFX_{fid}"\n')
            out.write(f'\t\ttexturefile = "{rel_path}"\n')
            out.write(f'\t}}\n')

            # Shine sprite
            out.write(f'\tspriteType = {{\n')
            out.write(f'\t\tname = "GFX_{fid}_shine"\n')
            out.write(f'\t\ttexturefile = "{rel_path}"\n')
            out.write(f'\t\teffectFile = "gfx/FX/buttonstate.lua"\n')
            out.write(f'\t\tanimation = {{\n')
            out.write(f'\t\t\tanimationmaskfile = "{rel_path}"\n')
            out.write(f'\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
            out.write(f'\t\t\tanimationrotation = -90.0\n')
            out.write(f'\t\t\tanimationlooping = no\n')
            out.write(f'\t\t\tanimationtime = 0.75\n')
            out.write(f'\t\t\tanimationdelay = 0\n')
            out.write(f'\t\t\tanimationblendmode = "add"\n')
            out.write(f'\t\t\tanimationtype = "scrolling"\n')
            out.write(f'\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}\n')
            out.write(f'\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}\n')
            out.write(f'\t\t}}\n')
            out.write(f'\t\tanimation = {{\n')
            out.write(f'\t\t\tanimationmaskfile = "{rel_path}"\n')
            out.write(f'\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
            out.write(f'\t\t\tanimationrotation = 90.0\n')
            out.write(f'\t\t\tanimationlooping = no\n')
            out.write(f'\t\t\tanimationtime = 0.75\n')
            out.write(f'\t\t\tanimationdelay = 0\n')
            out.write(f'\t\t\tanimationblendmode = "add"\n')
            out.write(f'\t\t\tanimationtype = "scrolling"\n')
            out.write(f'\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}\n')
            out.write(f'\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}\n')
            out.write(f'\t\t}}\n')
            out.write(f'\t\tlegacy_lazy_load = no\n')
            out.write(f'\t}}\n\n')

        out.write('}\n')

    print(f"Generated {gfx_out} with {len(focus_icon_files)} base and shine definitions.")

def harvest_ideas():
    print("Building Idea Catalog...")
    catalog = build_catalog(DONOR_IDEAS)
    print(f"Idea Catalog contains {len(catalog)} icons.")

    dest_dir = os.path.join(BASE_DIR, "gfx", "interface", "ideas", "FRA")
    os.makedirs(dest_dir, exist_ok=True)

    used_paths = set()
    idea_icon_files = {}

    for iid, idef in FRENCH_IDEAS.items():
        tokens = tokenize(iid) - STOPWORDS
        best_cand = None
        best_score = -1

        for base, full in catalog:
            if full in used_paths:
                continue
            b_tokens = tokenize(base) - STOPWORDS
            overlap = len(tokens & b_tokens)
            score = overlap * 50
            if 'fra' in base or 'french' in base:
                score += 30
            if score > best_score:
                best_score = score
                best_cand = full

        if not best_cand or best_score == 0:
            for base, full in catalog:
                if full not in used_paths:
                    best_cand = full
                    break

        used_paths.add(best_cand)
        ext = os.path.splitext(best_cand)[1].lower()
        dest_filename = f"{iid}{ext}"
        dest_path = os.path.join(dest_dir, dest_filename)
        shutil.copy2(best_cand, dest_path)
        idea_icon_files[iid] = (dest_filename, ext)

    print(f"Copied {len(idea_icon_files)} idea textures to {dest_dir}.")

    # Write interface/ww1_france_ideas.gfx
    gfx_out = os.path.join(BASE_DIR, "interface", "ww1_france_ideas.gfx")
    with open(gfx_out, "w", encoding="utf-8") as out:
        out.write('spriteTypes = {\n\n')
        for iid in sorted(idea_icon_files.keys()):
            fname, ext = idea_icon_files[iid]
            rel_path = f"gfx/interface/ideas/FRA/{fname}"
            out.write(f'\tspriteType = {{\n')
            out.write(f'\t\tname = "GFX_idea_{iid}"\n')
            out.write(f'\t\ttexturefile = "{rel_path}"\n')
            out.write(f'\t}}\n')
        out.write('}\n')

    print(f"Generated {gfx_out} with {len(idea_icon_files)} idea sprite definitions.")

if __name__ == "__main__":
    harvest_goals()
    harvest_ideas()
