# scripts/apply_ottoman_rework.py
# Applies full GFX mapping and authentic bilingual localization for all 256 Ottoman focuses

import os, sys, re
sys.path.insert(0, ".")
from scripts.tur_data_wing1 import WING_1
from scripts.tur_data_wing2 import WING_2
from scripts.tur_data_wing3 import WING_3
from scripts.tur_data_wing4 import WING_4
from scripts.tur_data_wing5 import WING_5

ALL_DATA = {}
for w in [WING_1, WING_2, WING_3, WING_4, WING_5]:
    ALL_DATA.update(w)

print(f"Loaded {len(ALL_DATA)} focus definitions from wings 1-5.")

# Read focus order from all_tur_focuses.txt
with open("scripts/all_tur_focuses.txt", "r", encoding="utf-8") as f:
    focus_order = [line.strip().split("|")[0] for line in f if line.strip()]

assert len(focus_order) == 256, f"Expected 256 focuses, got {len(focus_order)}"
for fid in focus_order:
    assert fid in ALL_DATA, f"Missing definition for {fid}"

# 1. GENERATE interface/ww1_ottoman_goals.gfx
gfx_lines = []
gfx_lines.append("spriteTypes = {\n")
gfx_lines.append("\t# ==============================================================================\n")
gfx_lines.append("\t# OTTOMAN EMPIRE (TUR) WW1 DIVERSIFIED GOAL SPRITES & SHINE OVERLAYS (256 FOCUSES)\n")
gfx_lines.append("\t# Authentic, period-accurate textures with dual-pass scrolling shine overlays\n")
gfx_lines.append("\t# ==============================================================================\n\n")

for fid in focus_order:
    d = ALL_DATA[fid]
    tex = d["icon"].replace("\\", "/")
    
    gfx_lines.append(f"\t# Focus: {fid}\n")
    gfx_lines.append("\tSpriteType = {\n")
    gfx_lines.append(f'\t\tname = "GFX_focus_{fid}"\n')
    gfx_lines.append(f'\t\ttexturefile = "{tex}"\n')
    gfx_lines.append("\t}\n")
    
    gfx_lines.append("\tSpriteType = {\n")
    gfx_lines.append(f'\t\tname = "GFX_focus_{fid}_shine"\n')
    gfx_lines.append(f'\t\ttexturefile = "{tex}"\n')
    gfx_lines.append('\t\teffectFile = "gfx/FX/buttonstate.lua"\n')
    gfx_lines.append("\t\tanimation = {\n")
    gfx_lines.append(f'\t\t\tanimationmaskfile = "{tex}"\n')
    gfx_lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
    gfx_lines.append("\t\t\tanimationrotation = -90.0\n")
    gfx_lines.append("\t\t\tanimationlooping = no\n")
    gfx_lines.append("\t\t\tanimationtime = 0.75\n")
    gfx_lines.append("\t\t\tanimationdelay = 0\n")
    gfx_lines.append('\t\t\tanimationblendmode = "add"\n')
    gfx_lines.append('\t\t\tanimationtype = "scrolling"\n')
    gfx_lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n")
    gfx_lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n")
    gfx_lines.append("\t\t}\n")
    gfx_lines.append("\t\tanimation = {\n")
    gfx_lines.append(f'\t\t\tanimationmaskfile = "{tex}"\n')
    gfx_lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
    gfx_lines.append("\t\t\tanimationrotation = 90.0\n")
    gfx_lines.append("\t\t\tanimationlooping = no\n")
    gfx_lines.append("\t\t\tanimationtime = 0.75\n")
    gfx_lines.append("\t\t\tanimationdelay = 0\n")
    gfx_lines.append('\t\t\tanimationblendmode = "add"\n')
    gfx_lines.append('\t\t\tanimationtype = "scrolling"\n')
    gfx_lines.append("\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n")
    gfx_lines.append("\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n")
    gfx_lines.append("\t\t}\n")
    gfx_lines.append("\t\tlegacy_lazy_load = no\n")
    gfx_lines.append("\t}\n")

gfx_lines.append("}\n")

with open("interface/ww1_ottoman_goals.gfx", "w", encoding="utf-8") as f:
    f.writelines(gfx_lines)

print("Generated interface/ww1_ottoman_goals.gfx with 256 normal sprites and 256 shine sprites.")

# 2. SPLICING LOCALISATION FILES
# PT-BR
with open("localisation/braz_por/ww1_ottoman_l_braz_por.yml", "r", encoding="utf-8-sig") as f:
    pt_lines = f.readlines()

pt_header = pt_lines[:135]
pt_footer = pt_lines[647:]

pt_focus_lines = []
for fid in focus_order:
    d = ALL_DATA[fid]
    pt_t = d["pt_t"].replace('"', "'")
    pt_d = d["pt_d"].replace('"', "'")
    pt_focus_lines.append(f' {fid}:0 "{pt_t}"\n')
    pt_focus_lines.append(f' {fid}_desc:0 "{pt_d}"\n')

new_pt_content = "".join(pt_header + pt_focus_lines + pt_footer)
with open("localisation/braz_por/ww1_ottoman_l_braz_por.yml", "wb") as f:
    f.write(b"\xef\xbb\xbf" + new_pt_content.encode("utf-8"))

print(f"Updated localisation/braz_por/ww1_ottoman_l_braz_por.yml (UTF-8 BOM, {len(new_pt_content.splitlines())} lines).")

# ENGLISH
with open("localisation/english/ww1_ottoman_l_english.yml", "r", encoding="utf-8-sig") as f:
    en_lines = f.readlines()

en_header = en_lines[:135]
en_footer = en_lines[647:]

en_focus_lines = []
for fid in focus_order:
    d = ALL_DATA[fid]
    en_t = d["en_t"].replace('"', "'")
    en_d = d["en_d"].replace('"', "'")
    en_focus_lines.append(f' {fid}:0 "{en_t}"\n')
    en_focus_lines.append(f' {fid}_desc:0 "{en_d}"\n')

new_en_content = "".join(en_header + en_focus_lines + en_footer)
with open("localisation/english/ww1_ottoman_l_english.yml", "wb") as f:
    f.write(b"\xef\xbb\xbf" + new_en_content.encode("utf-8"))

print(f"Updated localisation/english/ww1_ottoman_l_english.yml (UTF-8 BOM, {len(new_en_content.splitlines())} lines).")
print("Rework execution finished successfully!")
