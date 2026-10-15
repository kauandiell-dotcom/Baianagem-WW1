import os, re, glob

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

# 1. Parse all categories
categories = set()
for cf in glob.glob(os.path.join(repo, "common", "decisions", "categories", "*.txt")):
    with open(cf, "r", encoding="utf-8", errors="ignore") as f:
        txt = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    for m in re.finditer(r'^([A-Za-z0-9_]+)\s*=\s*\{', txt, re.MULTILINE):
        categories.add(m.group(1))

print(f"Total categories known: {len(categories)}")

# 2. Parse all ideas
all_ideas = set()
for idf in glob.glob(os.path.join(repo, "common", "ideas", "*.txt")):
    with open(idf, "r", encoding="utf-8", errors="ignore") as f:
        txt = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    for m in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*\{', txt):
        all_ideas.add(m.group(1))

# 3. Decision files to audit
target_files = [
    "ww1_ger_rus_rework_decisions.txt",
    "ww1_russia_crisis_decisions.txt",
    "ww1_russia_tsarist_decisions.txt",
    "ww1_soviet_civil_war_decisions.txt",
    "ww1_soviet_diplomacy_decisions.txt",
    "zz_ww1_sov_operations.txt",
    "side_ww1_ger_rus_depth.txt"
]

total_decisions = 0
missing_categories = []
missing_ideas = []

for tf in target_files:
    p = os.path.join(repo, "common", "decisions", tf)
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    clean = re.sub(r'#.*$', '', raw, flags=re.MULTILINE)

    # check bracket balance
    op = clean.count("{")
    cl = clean.count("}")
    delta = op - cl
    print(f"\n--- {tf} (Brackets: delta={delta}) ---")
    if delta != 0:
        print(f"  [ERROR] Unbalanced brackets! delta={delta}")

    # parse categories in file
    # Top-level blocks are categories: category_id = { decision_id = { ... } }
    cat_matches = list(re.finditer(r'^([A-Za-z0-9_]+)\s*=\s*\{', clean, re.MULTILINE))
    for i, cm in enumerate(cat_matches):
        cat_id = cm.group(1)
        if cat_id not in categories:
            missing_categories.append((tf, cat_id))
        
        # parse decisions inside this category block
        start = cm.start()
        end = cat_matches[i+1].start() if i+1 < len(cat_matches) else len(clean)
        block = clean[start:end]
        
        dec_matches = list(re.finditer(r'\t([A-Za-z0-9_]+)\s*=\s*\{', block))
        for dm in dec_matches:
            dec_id = dm.group(1)
            total_decisions += 1
            
            # check ideas inside
            added_ideas = re.findall(r'add_ideas\s*=\s*([A-Za-z0-9_]+)', block[dm.start():dm.start()+1500])
            for ida in added_ideas:
                if ida not in all_ideas:
                    missing_ideas.append((tf, dec_id, ida))

print(f"\nTotal Russian decisions audited: {total_decisions}")
if missing_categories:
    print(f"[MISSING CATEGORIES] ({len(missing_categories)}):")
    for tf, cat in missing_categories:
        print(f"  {tf}: category '{cat}' NOT defined in common/decisions/categories/")
else:
    print("Categories: ALL DEFINED")

if missing_ideas:
    print(f"[MISSING IDEAS IN DECISIONS] ({len(missing_ideas)}):")
    for tf, dec, ida in missing_ideas:
        print(f"  {tf}: {dec} adds non-existent idea: {ida}")
else:
    print("Added Ideas in decisions: ALL VALID")
