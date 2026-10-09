import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def clean_en_text(val):
    clean = val.strip()
    clean = re.sub(r'^(?:Immediate effect:\s*)+', '', clean, flags=re.IGNORECASE).strip()
    parts = re.split(r'\s*Immediate effect:\s*', clean, flags=re.IGNORECASE)
    if len(parts) > 1:
        if len(parts[0].strip()) > 15:
            clean = parts[0].strip()
        else:
            clean = parts[1].strip()
            
    clean = re.sub(r'\s*\(\+[^)]+\)', '', clean)
    clean = re.sub(r'\s*\(-[^)]+\)', '', clean)
    clean = re.sub(r';\s*\+?\d+\s+(?:army|navy|air)\s+XP[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r';\s*grants\s+[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r',\s*grants\s+[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'\s+', ' ', clean)
    clean = clean.replace('\\n ', '\\n').replace(' \\n', '\\n')
    if not clean.endswith('.'):
        clean += '.'
    return clean

def clean_pt_text(val):
    clean = val.strip()
    clean = re.sub(r'^(?:Efeito imediato:\s*|Immediate effect:\s*)+', '', clean, flags=re.IGNORECASE).strip()
    parts = re.split(r'\s*(?:Efeito imediato|Immediate effect):\s*', clean, flags=re.IGNORECASE)
    if len(parts) > 1:
        if len(parts[0].strip()) > 15:
            clean = parts[0].strip()
        else:
            clean = parts[1].strip()
            
    clean = re.sub(r'\s*\(\+[^)]+\)', '', clean)
    clean = re.sub(r'\s*\(-[^)]+\)', '', clean)
    clean = re.sub(r';\s*\+?\d+\s+de\s+XP[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r';\s*concede\s+[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r',\s*concede\s+[^.\n]*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'\s+', ' ', clean)
    clean = clean.replace('\\n ', '\\n').replace(' \\n', '\\n')
    if not clean.endswith('.'):
        clean += '.'
    return clean

def fix_data_files():
    # 1. ita_economy_data.py
    eco_file = ROOT / "scripts" / "ita_economy_data.py"
    eco_txt = eco_file.read_text(encoding="utf-8")
    eco_txt = eco_txt.replace("category = weapons", "category = infantry_weapons")
    eco_file.write_text(eco_txt, encoding="utf-8")
    print("Fixed ita_economy_data.py")

    # 2. ita_military_data.py
    mil_file = ROOT / "scripts" / "ita_military_data.py"
    mil_txt = mil_file.read_text(encoding="utf-8")
    mil_txt = re.sub(r'"ai":\s*"base = (\d+)"', r'"ai": "factor = \1"', mil_txt)
    mil_txt = mil_txt.replace("category = special_forces", "category = infantry_weapons")
    mil_txt = mil_txt.replace("category = engineering", "category = industry")
    mil_txt = mil_txt.replace("category = heavy_armor", "category = naval_equipment")
    mil_txt = mil_txt.replace("category = cl_tech", "category = naval_equipment")
    mil_txt = mil_txt.replace("category = scout_plane", "category = air_equipment")
    mil_file.write_text(mil_txt, encoding="utf-8")
    print("Fixed ita_military_data.py")

    # 3. ita_politics_data.py
    pol_file = ROOT / "scripts" / "ita_politics_data.py"
    pol_txt = pol_file.read_text(encoding="utf-8")
    pol_txt = re.sub(r'"ai":\s*"base = (\d+)"', r'"ai": "factor = \1"', pol_txt)
    pol_file.write_text(pol_txt, encoding="utf-8")
    print("Fixed ita_politics_data.py")

def fix_build_ww1_italy():
    b_file = ROOT / "scripts" / "build_ww1_italy.py"
    b_txt = b_file.read_text(encoding="utf-8")

    # Replace AI generation logic
    old_ai = '''        ai_val = data.get("ai", "factor = 10")
        if isinstance(ai_val, (int, float)):
            ai_str = f"factor = {ai_val}"
        elif str(ai_val).isdigit():
            ai_str = f"factor = {ai_val}"
        elif "factor" in str(ai_val):
            ai_str = str(ai_val)
        else:
            ai_str = f"factor = {ai_val}"
        lines.append(f"\t\tai_will_do = {{ {ai_str} }}")'''

    new_ai = '''        ai_val = data.get("ai", "factor = 10")
        if isinstance(ai_val, (int, float)):
            ai_str = f"factor = {ai_val}"
        elif str(ai_val).isdigit():
            ai_str = f"factor = {ai_val}"
        elif str(ai_val).startswith("base ="):
            ai_str = str(ai_val).replace("base =", "factor =").strip()
        elif "factor" in str(ai_val):
            ai_str = str(ai_val)
        else:
            ai_str = f"factor = {ai_val}"
        lines.append(f"\t\tai_will_do = {{ {ai_str} }}")'''

    if old_ai in b_txt:
        b_txt = b_txt.replace(old_ai, new_ai)
    else:
        print("Warning: old_ai block not found exactly in build_ww1_italy.py")

    # Replace localisation description prepending
    old_loc = '''        desc_pt = data.get("desc_pt") or data.get("pt_desc") or ""
        desc_en = data.get("desc_en") or data.get("en_desc") or ""

        if not desc_pt.startswith("Efeito imediato:"):
            desc_pt = f"Efeito imediato: {desc_pt}"
        if not desc_en.startswith("Immediate effect:"):
            desc_en = f"Immediate effect: {desc_en}"'''

    new_loc = '''        desc_pt = data.get("desc_pt") or data.get("pt_desc") or ""
        desc_en = data.get("desc_en") or data.get("en_desc") or ""

        from apply_italy_fixes import clean_pt_text, clean_en_text
        desc_pt = clean_pt_text(desc_pt)
        desc_en = clean_en_text(desc_en)'''

    if old_loc in b_txt:
        b_txt = b_txt.replace(old_loc, new_loc)
    else:
        print("Warning: old_loc block not found exactly in build_ww1_italy.py")

    b_file.write_text(b_txt, encoding="utf-8")
    print("Fixed build_ww1_italy.py")

def fix_ger_characters():
    ger_file = ROOT / "common" / "characters" / "GER.txt"
    ger_txt = ger_file.read_text(encoding="utf-8")
    
    # Fix Schlieffen traits
    old_schlieffen = "traits={ logistics_wizard thorough_planner skilled_staffer expert_delegator brilliant_strategist }"
    new_schlieffen = "traits={ organizer brilliant_strategist }"
    
    if old_schlieffen in ger_txt:
        ger_txt = ger_txt.replace(old_schlieffen, new_schlieffen)
        ger_file.write_text(ger_txt, encoding="utf-8")
        print("Fixed GER_von_schlieffen in common/characters/GER.txt")
    else:
        print("Warning: old_schlieffen traits not found in GER.txt")

def fix_ita_history():
    ita_hist = ROOT / "history" / "countries" / "ITA - Italy.txt"
    ita_txt = ita_hist.read_text(encoding="utf-8")
    
    old_advisor = "recruit_character = advisor\n"
    if old_advisor in ita_txt:
        ita_txt = ita_txt.replace(old_advisor, "")
        ita_hist.write_text(ita_txt, encoding="utf-8")
        print("Fixed recruit_character = advisor in history/countries/ITA - Italy.txt")
    else:
        print("Warning: recruit_character = advisor not found in ITA history")

if __name__ == "__main__":
    fix_data_files()
    fix_build_ww1_italy()
    fix_ger_characters()
    fix_ita_history()
    
    # Rebuild focus tree and localisation
    import build_ww1_italy
    print("Rebuilding Italy tree and localisation...")
    build_ww1_italy.build_tree()
    build_ww1_italy.build_localisation()
    print("Done applying all Italy fixes!")
