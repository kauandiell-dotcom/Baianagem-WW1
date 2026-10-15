import os, re, glob

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def load_loc(lang):
    keys = {}
    loc_dir = os.path.join(repo, "localisation", lang)
    if not os.path.exists(loc_dir):
        return keys
    for f in os.listdir(loc_dir):
        if not (f.endswith(".yml") or f.endswith(".yaml")):
            continue
        p = os.path.join(loc_dir, f)
        with open(p, "r", encoding="utf-8", errors="ignore") as fl:
            for line in fl:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):\d*\s*"([^"]*)"', line)
                if m:
                    keys[m.group(1)] = m.group(2)
    rep_dir = os.path.join(repo, "localisation", "replace")
    if os.path.exists(rep_dir):
        for f in os.listdir(rep_dir):
            if f.endswith(f"_{lang}.yml") or f.endswith(f"_{lang}.yaml"):
                p = os.path.join(rep_dir, f)
                with open(p, "r", encoding="utf-8", errors="ignore") as fl:
                    for line in fl:
                        m = re.match(r'^\s*([A-Za-z0-9_.\-]+):\d*\s*"([^"]*)"', line)
                        if m:
                            keys[m.group(1)] = m.group(2)
    return keys

eng_keys = load_loc("english")
por_keys = load_loc("braz_por")

target_decision_files = [
    "ww1_ger_rus_rework_decisions.txt",
    "ww1_russia_crisis_decisions.txt",
    "ww1_russia_tsarist_decisions.txt",
    "ww1_soviet_civil_war_decisions.txt",
    "ww1_soviet_diplomacy_decisions.txt",
    "zz_ww1_sov_operations.txt"
]

missing_dec_eng = []
missing_dec_por = []
real_decs = []

# Keywords that are NOT decisions
reserved = {"icon", "cost", "days_re_enable", "available", "visible", "complete_effect", "ai_will_do", "modifier", "limit", "if", "else", "NOT", "OR", "AND", "check_variable", "has_country_flag", "original_tag", "tag", "fire_only_once", "days_remove", "remove_effect"}

for df in target_decision_files:
    p = os.path.join(repo, "common", "decisions", df)
    if not os.path.exists(p): continue
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        clean = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    
    # Decisions are defined at indentation level 1 (1 tab) inside categories
    matches = re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', clean, re.MULTILINE)
    for m in matches:
        dec_id = m.group(1)
        if dec_id in reserved or dec_id.isdigit():
            continue
        real_decs.append((df, dec_id))
        if dec_id not in eng_keys:
            missing_dec_eng.append((df, dec_id))
        if dec_id not in por_keys:
            missing_dec_por.append((df, dec_id))

print(f"Audited {len(real_decs)} real Russian decisions.")
print(f"Missing in English: {len(missing_dec_eng)}")
if missing_dec_eng:
    for df, d in missing_dec_eng:
        print(f"  ENG missing: {df} -> {d}")

print(f"Missing in Portuguese: {len(missing_dec_por)}")
if missing_dec_por:
    for df, d in missing_dec_por:
        print(f"  POR missing: {df} -> {d}")
