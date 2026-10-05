import os
import sys
import shutil
import hashlib
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from france_builder.data_foci import FRENCH_FOCI

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DONOR_GOALS = [
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3106240385\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3365515312\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2716194283\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2076426030\gfx\interface\goals',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3797323750\gfx\interface\goals',
    os.path.join(BASE_DIR, 'gfx', 'interface', 'goals'),
]

STOPWORDS = {'the', 'and', 'for', 'with', 'from', 'our', 'les', 'des', 'une', 'qui', 'par', 'sur', 'dans', 'pour', 'plus', 'tous'}

def tokenize(s):
    return set(re.findall(r'[a-zA-Z]{3,}', s.lower()))

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def harvest_unique_icons():
    print("=" * 60)
    print("HARVESTING 100% UNIQUE TEXTURES FOR ALL 222 FRENCH FOCUSES")
    print("=" * 60)

    # 1. Build catalog of unique textures
    print("[*] Scanning donor directories...")
    catalog = [] # list of (basename, full_path, md5_hash)
    hash_to_path = {}
    
    for d in DONOR_GOALS:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower().endswith(('.dds', '.png')):
                    full = os.path.join(root, f)
                    try:
                        h = get_file_hash(full)
                        if h not in hash_to_path:
                            hash_to_path[h] = full
                            base = os.path.splitext(f)[0].lower()
                            catalog.append((base, full, h))
                    except Exception:
                        pass

    print(f"[*] Catalog indexed: {len(catalog)} uniquely distinct textures.")

    used_hashes = set()
    focus_matches = {}

    dest_dir = os.path.join(BASE_DIR, "gfx", "interface", "goals")
    os.makedirs(dest_dir, exist_ok=True)

    # Domain specific keywords for enhanced scoring
    wing_keywords = {
        1: {'republic', 'marianne', 'parliament', 'election', 'democracy', 'socialist', 'monarchy', 'royal', 'crown', 'commune', 'flag', 'liberty', 'france', 'law', 'constitution'},
        2: {'industry', 'factory', 'coal', 'steel', 'railway', 'train', 'mining', 'chemical', 'workers', 'money', 'gold', 'bank', 'colony', 'africa', 'senegal', 'indochina', 'algeria', 'morocco', 'tunisia', 'rubber', 'cotton'},
        3: {'navy', 'naval', 'ship', 'dreadnought', 'battleship', 'cruiser', 'submarine', 'torpedo', 'port', 'dockyard', 'admiral', 'air', 'plane', 'aircraft', 'biplane', 'aviation', 'fighter', 'bomber', 'ace', 'pilot', 'reconnaissance', 'guynemer', 'spad', 'nieuport'},
        4: {'army', 'infantry', 'soldier', 'trench', 'artillery', 'cannon', 'gun', 'howitzer', 'mortar', 'helmet', 'adrian', 'gas', 'tank', 'armor', 'renault', 'verdun', 'somme', 'marne', 'petain', 'joffre', 'foch', 'gallieni', 'charge', 'offensive', 'defense', 'fortress'},
        5: {'diplomacy', 'treaty', 'alliance', 'pact', 'handshake', 'britain', 'russia', 'italy', 'serbia', 'romania', 'greece', 'america', 'usa', 'belgium', 'germany', 'peace', 'armistice', 'rhine', 'alsace', 'lorraine', 'ambassador', 'conference'}
    }

    for f in FRENCH_FOCI:
        fid = f['id']
        wing = f['wing']
        queries = [q.lower().replace('gfx_', '') for q in f.get('icon_query', [])]
        f_tokens = (tokenize(fid) | tokenize(f.get('title', ''))) - STOPWORDS
        domain_tokens = wing_keywords.get(wing, set())

        best_cand = None
        best_score = -1

        for base, full, h in catalog:
            if h in used_hashes:
                continue

            score = 0
            # 1. Exact query match
            for q in queries:
                if base == q or base == 'gfx_' + q:
                    score = max(score, 1000)
                elif q in base:
                    score = max(score, 500 + len(q))

            # 2. Token overlap
            b_tokens = tokenize(base) - STOPWORDS
            overlap = len(f_tokens & b_tokens)
            if overlap > 0:
                score += overlap * 40

            # 3. Domain alignment bonus
            domain_overlap = len(domain_tokens & b_tokens)
            if domain_overlap > 0:
                score += domain_overlap * 20

            # 4. French specificity bonus
            if 'fra' in base or 'french' in base or 'france' in base:
                score += 30

            # 5. Penalize cross-domain absurdities (e.g. airplane icon for tank focus, or ship icon for infantry)
            if wing == 3 and not (b_tokens & {'air', 'plane', 'ship', 'navy', 'flight', 'torpedo', 'sea', 'pilot', 'spad', 'nieuport', 'dreadnought', 'boat'}):
                score -= 50
            if wing == 4 and (b_tokens & {'ship', 'submarine', 'dreadnought'}):
                score -= 100
            if wing != 3 and (b_tokens & {'plane', 'aircraft', 'biplane', 'spad'}):
                score -= 80

            if score > best_score:
                best_score = score
                best_cand = (base, full, h)

        # Fallback if no positive score found
        if not best_cand:
            for base, full, h in catalog:
                if h not in used_hashes:
                    best_cand = (base, full, h)
                    break

        used_hashes.add(best_cand[2])
        focus_matches[fid] = best_cand

    # Copy files and ensure unique names
    copied_files = {}
    for fid, (base, full, h) in focus_matches.items():
        ext = os.path.splitext(full)[1].lower()
        dest_filename = f"GFX_{fid}{ext}"
        dest_path = os.path.join(dest_dir, dest_filename)
        if os.path.abspath(full) != os.path.abspath(dest_path):
            shutil.copy2(full, dest_path)
        copied_files[fid] = dest_filename

    print(f"[*] Successfully copied {len(copied_files)} textures.")
    print(f"[*] Total unique MD5 hashes used: {len(used_hashes)} / {len(FRENCH_FOCI)}")
    assert len(used_hashes) == len(FRENCH_FOCI), "ERROR: Duplicate hashes detected!"

    # Generate interface/ww1_france_goals.gfx
    gfx_out = os.path.join(BASE_DIR, "interface", "ww1_france_goals.gfx")
    with open(gfx_out, "w", encoding="utf-8") as out:
        out.write('spriteTypes = {\n\n')
        for fid in sorted(copied_files.keys()):
            fname = copied_files[fid]
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

    print(f"[*] Generated {gfx_out} with {len(copied_files)} unique base and shine definitions.")
    print(">>> 100% ZERO DUPLICATE GFX ACHIEVED! <<<")

if __name__ == "__main__":
    harvest_unique_icons()
