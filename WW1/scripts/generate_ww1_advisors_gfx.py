# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# 1. Load existing sprites in interface/*.gfx
existing_sprites = set()
for p in (ROOT / "interface").glob("*.gfx"):
    if p.name == "ww1_advisors_portraits.gfx":
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"', txt):
        existing_sprites.add(m.group(1))

print(f"Loaded {len(existing_sprites)} existing sprites across interface/*.gfx.")

# 2. Index all textures on disk
textures_by_stem = {}
for p in (ROOT / "gfx").glob("**/*"):
    if p.suffix.lower() in [".dds", ".png", ".tga"]:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        stem = p.stem.lower()
        if stem not in textures_by_stem:
            textures_by_stem[stem] = []
        textures_by_stem[stem].append(rel)

print(f"Indexed {len(textures_by_stem)} unique texture stems on disk.")

# 3. Known specific sprite-to-texture mappings for authentic WW1 accuracy
SPECIFIC_MAPPINGS = {
    # Russia
    "GFX_idea_SOV_pyotr_stolypin": "gfx/interface/ideas/RUS/idea_RUS_pyotr_stolypin.png",
    "GFX_idea_SOV_alexander_kerensky": "gfx/interface/ideas/RUS/idea_RUS_alexander_kerensky_army.png",
    "GFX_idea_SOV_mikhail_rodzianko": "gfx/leaders/SOV/SOV_mikhail_rodzianko.png",
    "GFX_idea_SOV_sergei_sazonov": "gfx/leaders/SOV/SOV_sergei_sazonov.png",
    "GFX_idea_SOV_vladimir_sukhomlinov": "gfx/hoi4tgw_portraits/RUS/advisor/RUS_vladimir_sukhomlinov.dds",
    "GFX_idea_SOV_grigori_rasputin": "gfx/interface/ideas/RUS/idea_RUS_grigori_rasputin.png",
    "GFX_idea_SOV_boris_savinkov": "gfx/interface/ideas/RUS/idea_RUS_boris_savinkov.png",
    "GFX_idea_SOV_grand_duke_nicholas": "gfx/leaders/SOV/SOV_grand_duke_nicholas.png",
    "GFX_idea_SOV_alexei_brusilov": "gfx/interface/ideas/RUS/idea_RUS_alexei_brusilov.png",
    "GFX_idea_SOV_mikhail_alekseyev": "gfx/hoi4tgw_portraits/RUS/army_generals/RUS_alekseyev.dds",
    "GFX_idea_SOV_lavr_kornilov": "gfx/interface/ideas/RUS/idea_RUS_lavr_kornilov.png",
    "GFX_idea_SOV_nicholas_yudenich": "gfx/interface/ideas/RUS/idea_RUS_nicholas_yudenich.png",
    "GFX_idea_SOV_anton_denikin": "gfx/hoi4tgw_portraits/RUS/army_generals/RUS_Anton_Denikin.dds",
    "GFX_idea_SOV_nikolay_rouzski": "gfx/interface/ideas/RUS/idea_RUS_generic_land_1.png",
    "GFX_idea_SOV_alexander_kolchak": "gfx/interface/ideas/RUS/idea_RUS_alexander_kolchak.png",
    "GFX_idea_SOV_nikolai_essen": "gfx/interface/ideas/RUS/idea_RUS_Nikolai_von_Essen.png",
    "GFX_idea_SOV_andrei_eberhardt": "gfx/interface/ideas/RUS/idea_RUS_generic_navy_1.png",
    "GFX_idea_SOV_maria_bochkareva": "gfx/leaders/SOV/SOV_maria_bochkareva_small.png",

    # Austria-Hungary
    "GFX_idea_rudolf_hess": "gfx/leaders/AUS/AUS_Franz_Ferdinand.dds",
    "GFX_idea_AUH_franz_conrad_von_hotzendorf": "gfx/interface/ideas/idea_AUH_franz_conrad_von_hotzendorf.dds",
    "GFX_idea_AUH_artur_arz_von_straussenberg": "gfx/interface/ideas/idea_AUH_artur_arz_von_straussenberg.dds",
    "GFX_idea_AUH_anton_haus": "gfx/interface/ideas/idea_AUH_anton_haus.dds",
    "GFX_idea_AUH_hermann_von_spaun": "gfx/interface/ideas/idea_AUH_hermann_von_spaun.dds",
    "GFX_idea_AUH_blasius_schemua": "gfx/interface/ideas/idea_AUH_blasius_schemua.dds",
    "GFX_idea_AUH_friedrich_von_beck_rzikowsky": "gfx/interface/ideas/idea_AUH_friedrich_von_beck_rzikowsky.dds",
    "GFX_idea_AUH_august_urbanski": "gfx/interface/ideas/idea_AUH_august_urbanski.dds",
    "GFX_idea_AUH_franz_von_holub": "gfx/interface/ideas/idea_AUH_franz_von_holub.dds",
    "GFX_idea_AUH_rudolf_montecuccoli": "gfx/interface/ideas/idea_AUH_rudolf_montecuccoli.dds",
    "GFX_idea_AUH_maximilian_njegovan": "gfx/interface/ideas/idea_AUH_maximilian_njegovan.dds",
    "GFX_idea_AUH_karl_kailer_von_kagenfels": "gfx/interface/ideas/idea_AUH_karl_kailer_von_kagenfels.dds",
    "GFX_idea_AUH_maximilian_daublebsky_von_sterneck": "gfx/interface/ideas/idea_AUH_maximilian_daublebsky_von_sterneck.dds",
    "GFX_idea_AUH_emil_uzelac": "gfx/interface/ideas/idea_AUH_emil_uzelac.dds",
    "GFX_idea_AUH_agenor_goluchowski": "gfx/interface/ideas/idea_AUH_agenor_goluchowski.dds",
    "GFX_idea_AUH_oskar_von_hranilovic_czvetassin": "gfx/interface/ideas/idea_AUH_oskar_von_hranilovic_czvetassin.dds",
    "GFX_idea_AUH_alois_lexa_von_aehrenthal": "gfx/interface/ideas/idea_AUH_alois_lexa_von_aehrenthal.dds",
    "GFX_idea_AUS_istvan_tisza": "gfx/interface/ideas/idea_AUH_istvan_tisza.dds",
    "GFX_idea_AUH_gyula_andrassy": "gfx/interface/ideas/idea_AUH_gyula_andrassy.dds",
    "GFX_idea_AUH_ottokar_czernin": "gfx/interface/ideas/idea_AUH_ottokar_czernin.dds",
    "GFX_idea_AUH_gabor_ugron": "gfx/interface/ideas/idea_AUH_gabor_ugron.dds",
    "GFX_idea_AUH_leon_von_bilinski": "gfx/interface/ideas/idea_AUH_leon_von_bilinski.dds",
    "GFX_idea_AUH_eugen_hordliczka": "gfx/interface/ideas/idea_AUH_eugen_hordliczka.dds",
    "GFX_idea_AUS_charles_i": "gfx/interface/ideas/idea_AUH_charles_i.dds",

    # Belgium
    "GFX_idea_BEL_rucqouy": "gfx/interface/ideas/idea_BEL_rucqouy.dds",
    "GFX_idea_BEL_ridder_de_selliers_de_moranville": "gfx/interface/ideas/idea_BEL_ridder_de_selliers_de_moranville.dds",
    "GFX_idea_BEL_henry_h_maglinse": "gfx/interface/ideas/idea_BEL_henry_h_maglinse.dds",
    "GFX_idea_BEL_felix_wielemans": "gfx/interface/ideas/idea_BEL_felix_wielemans.dds",
    "GFX_idea_BEL_jules_davignon": "gfx/interface/ideas/idea_BEL_jules_davignon.dds",
    "GFX_idea_BEL_baron_beyens": "gfx/interface/ideas/idea_BEL_baron_beyens.dds",
    "GFX_idea_BEL_geraard_cooreman": "gfx/interface/ideas/idea_BEL_geraard_cooreman.dds",
    "GFX_idea_BEL_baron_wahis": "gfx/interface/ideas/idea_BEL_baron_wahis.dds",
    "GFX_idea_BEL_joseph_hellebaut": "gfx/interface/ideas/idea_BEL_joseph_hellebaut.dds",
    "GFX_idea_BEL_marcel_de_crombrugghe": "gfx/interface/ideas/idea_BEL_marcel_de_crombrugghe.dds",
    "GFX_idea_BEL_edwart_anseele": "gfx/interface/ideas/idea_BEL_edwart_anseele.dds",
    "GFX_idea_BEL_leon_delacroix": "gfx/interface/ideas/idea_BEL_leon_delacroix.dds",

    # United Kingdom
    "GFX_idea_ENG_jfc_fuller": "gfx/interface/ideas/ENG/idea_ENG_J_F_C_Fuller.png",
    "GFX_idea_ENG_navy_churchill": "gfx/admiral/ENG_churchill.dds",
    "GFX_idea_EGY_edmund_allenby": "gfx/generals/ENG_Allenby.dds",

    # Germany
    "GFX_idea_GER_von_lettowvorbeck": "gfx/interface/ideas/GER/GER_paul_von_lettow_vorbeck.png",
    "GFX_idea_GER_von_quast": "gfx/interface/ideas/GER/idea_german_generic_land_1.dds",
    "GFX_idea_GER_von_bothmer": "gfx/interface/ideas/GER/idea_german_generic_land_5.dds",

    # Generic fallbacks
    "GFX_idea_generic_political_advisor_europe_3": "gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds",
        "GFX_idea_BEL_georges_moulaert": "gfx/interface/ideas/idea_GER_generic_navy_1.dds",
    "GFX_idea_POL_swirski": "gfx/interface/ideas/idea_GER_generic_navy_2.dds",
    "GFX_idea_POL_porebski": "gfx/interface/ideas/idea_GER_generic_navy_3.dds",
    "GFX_idea_POL_steyer": "gfx/interface/ideas/idea_GER_generic_navy_1.dds",
    "GFX_idea_POL_roman_dmowski": "gfx/hoi4tgw_portraits/POL/advisor/POL_roman_dmowski.dds",
    "GFX_idea_ROM_general_genner": "gfx/interface/ideas/idea_generic_army_europe_4.dds",
    "GFX_idea_SWE_theodor_carl_adam_sandstrom": "gfx/interface/ideas/idea_GER_generic_navy_2.dds",
    "GFX_idea_generic_navy_europe_1": "gfx/interface/ideas/idea_GER_generic_navy_1.dds",
    "GFX_idea_generic_navy_europe_3": "gfx/interface/ideas/idea_GER_generic_navy_3.dds",
    "GFX_idea_generic_navy_europe_3": "gfx/interface/ideas/idea_generic_navy_europe_2.dds",
}

# 4. Parse all characters to collect small portrait references
char_advisors = []
for p in sorted((ROOT / "common/characters").glob("*.txt")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    tag = p.stem
    clean_txt = re.sub(r'#.*', '', txt)
    m = re.search(r'characters\s*=\s*\{([\s\S]*)\}', clean_txt)
    if not m:
        continue
    body = m.group(1)
    
    depth = 0
    token_start = None
    curr_char_id = None
    i = 0
    n = len(body)
    while i < n:
        c = body[i]
        if c == '{':
            if depth == 0:
                prefix = body[token_start:i].strip()
                m_id = re.search(r'([a-zA-Z0-9_]+)\s*=$', prefix)
                curr_char_id = m_id.group(1) if m_id else "UNKNOWN"
                block_start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and curr_char_id:
                char_body = body[block_start:i+1]
                slots = re.findall(r'\bslot\s*=\s*([a-zA-Z0-9_]+)', char_body)
                smalls = re.findall(r'\bsmall\s*=\s*(?:\"([^\"]+)\"|([a-zA-Z0-9_]+))', char_body)
                small_list = [s[0] or s[1] for s in smalls]
                is_adv = bool(re.search(r'\b(advisor|corps_commander|field_marshal|navy_leader)\s*=\s*\{', char_body))
                char_advisors.append({
                    'id': curr_char_id,
                    'tag': tag,
                    'smalls': small_list,
                    'slots': slots,
                    'is_advisor': is_adv
                })
                curr_char_id = None
                token_start = i + 1
        elif depth == 0 and not body[i].isspace() and token_start is None:
            token_start = i
        i += 1

# 5. Resolve sprites to generate
new_sprites = {}

generic_fallbacks = {
    'political_advisor': 'gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds',
    'army_chief': 'gfx/interface/ideas/idea_generic_army_europe_1.dds',
    'high_command': 'gfx/interface/ideas/idea_generic_army_europe_2.dds',
    'navy_chief': 'gfx/interface/ideas/idea_GER_generic_navy_1.dds',
    'air_chief': 'gfx/interface/ideas/idea_generic_air_europe_1.dds',
    'theorist': 'gfx/interface/ideas/idea_generic_army_europe_3.dds',
}

for c in char_advisors:
    tag = c['tag']
    cid = c['id']
    slot = c['slots'][0] if c['slots'] else 'political_advisor'
    
    for s in c['smalls']:
        if not s or s in existing_sprites:
            continue
        if s in new_sprites:
            continue
            
        # Check specific mappings
        if s in SPECIFIC_MAPPINGS:
            tex = SPECIFIC_MAPPINGS[s]
            if (ROOT / tex).exists():
                new_sprites[s] = tex
                continue
                
        # Check if s is already a direct path
        if s.lower().endswith(".dds") or s.lower().endswith(".png"):
            if (ROOT / s).exists():
                new_sprites[s] = s
                continue
                
        # Try finding on disk
        s_clean = s.replace("GFX_", "")
        s_clean_no_idea = s_clean.replace("idea_", "")
        candidates = [
            s_clean.lower(),
            s_clean_no_idea.lower(),
            "idea_" + s_clean_no_idea.lower(),
            s.lower(),
            cid.lower(),
            "idea_" + cid.lower(),
            cid.replace(tag + "_", "").lower(),
            "idea_" + cid.replace(tag + "_", "").lower(),
            "idea_" + tag.lower() + "_" + cid.replace(tag + "_", "").lower(),
            "idea_auh_" + cid.replace(tag + "_", "").lower()
        ]
        
        found_path = None
        for cand in candidates:
            if cand in textures_by_stem:
                matches = textures_by_stem[cand]
                idea_matches = [m for m in matches if 'idea' in m.lower()]
                found_path = idea_matches[0] if idea_matches else matches[0]
                break
                
        if found_path:
            new_sprites[s] = found_path
        else:
            fb = generic_fallbacks.get(slot, 'gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds')
            new_sprites[s] = fb

print(f"Total new sprite definitions to register: {len(new_sprites)}")

# 6. Generate interface/ww1_advisors_portraits.gfx
lines = [
    "spriteTypes = {",
    "\t# Auto-registered WW1 Advisor Small Portraits and Idea Icons",
]

# Group by TAG
by_tag = {}
for s, tex in sorted(new_sprites.items()):
    # try extract tag
    tag_match = re.search(r'([A-Z]{3})', s)
    group = tag_match.group(1) if tag_match else "GENERIC"
    if group not in by_tag:
        by_tag[group] = []
    by_tag[group].append((s, tex))

for group, items in sorted(by_tag.items()):
    lines.append(f"\n\t### {group} ###")
    for s, tex in sorted(items):
        lines.append("\tspriteType = {")
        lines.append(f'\t\tname = "{s}"')
        lines.append(f'\t\ttexturefile = "{tex}"')
        lines.append("\t}")

lines.append("}\n")

p_gfx = ROOT / "interface" / "ww1_advisors_portraits.gfx"
p_gfx.write_text("\n".join(lines), encoding="utf-8")
print(f"Written {p_gfx} successfully!")
