import os
import sys
import re
import glob

REPO_ROOT = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def load_all_ideas():
    ideas = set()
    ideas_dir = os.path.join(REPO_ROOT, "common", "ideas")
    for f in os.listdir(ideas_dir):
        if not f.endswith(".txt"): continue
        with open(os.path.join(ideas_dir, f), "r", encoding="utf-8", errors="ignore") as file:
            c = file.read()
        # strip comments
        c = re.sub(r'#.*$', '', c, flags=re.MULTILINE)
        # matches top tokens inside country/hidden_ideas
        for m in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*\{', c):
            token = m.group(1)
            if token not in ["ideas", "country", "hidden_ideas", "character", "political_advisor", "tank_manufacturer", "naval_manufacturer", "aircraft_manufacturer", "industrial_concern", "materiel_manufacturer"]:
                ideas.add(token)
    return ideas

def load_all_scripted_effects():
    effects = set()
    effects_dir = os.path.join(REPO_ROOT, "common", "scripted_effects")
    for f in os.listdir(effects_dir):
        if not f.endswith(".txt"): continue
        with open(os.path.join(effects_dir, f), "r", encoding="utf-8", errors="ignore") as file:
            c = file.read()
        c = re.sub(r'#.*$', '', c, flags=re.MULTILINE)
        for m in re.finditer(r'^([A-Za-z0-9_]+)\s*=\s*\{', c, re.MULTILINE):
            effects.add(m.group(1))
    return effects

def load_all_events():
    events = set()
    events_dir = os.path.join(REPO_ROOT, "events")
    for f in os.listdir(events_dir):
        if not f.endswith(".txt"): continue
        with open(os.path.join(events_dir, f), "r", encoding="utf-8", errors="ignore") as file:
            c = file.read()
        c = re.sub(r'#.*$', '', c, flags=re.MULTILINE)
        for m in re.finditer(r'(?:country_event|news_event)\s*=\s*\{[^}]*?id\s*=\s*([A-Za-z0-9_.]+)', c, re.DOTALL):
            events.add(m.group(1))
    return events

def load_all_characters():
    characters = set()
    chars_dir = os.path.join(REPO_ROOT, "common", "characters")
    for f in os.listdir(chars_dir):
        if not f.endswith(".txt"): continue
        with open(os.path.join(chars_dir, f), "r", encoding="utf-8", errors="ignore") as file:
            c = file.read()
        c = re.sub(r'#.*$', '', c, flags=re.MULTILINE)
        for m in re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', c, re.MULTILINE):
            characters.add(m.group(1))
    return characters

def deep_audit():
    print("Loading global databases...")
    all_ideas = load_all_ideas()
    all_effects = load_all_scripted_effects()
    all_events = load_all_events()
    all_characters = load_all_characters()
    print(f"Loaded: {len(all_ideas)} ideas, {len(all_effects)} scripted effects, {len(all_events)} events, {len(all_characters)} characters.")

    trees = [
        os.path.join(REPO_ROOT, "common", "national_focus", "soviet.txt"),
        os.path.join(REPO_ROOT, "common", "national_focus", "soviet_russia.txt"),
        os.path.join(REPO_ROOT, "common", "national_focus", "white_russia.txt")
    ]

    issues = []

    for tpath in trees:
        tname = os.path.basename(tpath)
        print(f"\n--- Checking Tree: {tname} ---")
        with open(tpath, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()

        # extract focus blocks
        matches = list(re.finditer(r'focus\s*=\s*\{', raw))
        focuses = {}
        for i, m in enumerate(matches):
            start = m.start()
            end = matches[i+1].start() if i+1 < len(matches) else len(raw)
            chunk = raw[start:end]
            id_m = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', chunk)
            if id_m:
                fid = id_m.group(1)
                focuses[fid] = chunk

        # Check references in each focus
        for fid, block in focuses.items():
            # Check added ideas
            added_ideas = re.findall(r'(?:add_ideas|swap_ideas\s*=\s*\{[^}]*add_idea)\s*=\s*([A-Za-z0-9_]+)', block)
            for idea in added_ideas:
                if idea not in all_ideas:
                    # Ignore dynamic or scripted token if valid, but check if missing
                    issues.append(f"[{tname} / {fid}] Added idea '{idea}' not defined in common/ideas!")

            # Check recruited characters
            recruits = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', block)
            for r in recruits:
                if r not in all_characters:
                    issues.append(f"[{tname} / {fid}] Recruited character '{r}' not defined in common/characters!")

            # Check called events
            evs = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_.]+)', block)
            for ev in evs:
                if ev not in all_events:
                    issues.append(f"[{tname} / {fid}] Calls non-existent event '{ev}'!")

    # Check Decisions
    dec_files = glob.glob(os.path.join(REPO_ROOT, "common", "decisions", "*rus*.txt")) + \
                glob.glob(os.path.join(REPO_ROOT, "common", "decisions", "*sov*.txt"))
    for df in set(dec_files):
        dname = os.path.basename(df)
        print(f"\n--- Checking Decisions: {dname} ---")
        with open(df, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        evs = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_.]+)', raw)
        for ev in evs:
            if ev not in all_events:
                issues.append(f"[{dname}] Calls non-existent event '{ev}'!")

    # Check Events
    ev_files = glob.glob(os.path.join(REPO_ROOT, "events", "*rus*.txt")) + \
               glob.glob(os.path.join(REPO_ROOT, "events", "*sov*.txt"))
    for ef in set(ev_files):
        ename = os.path.basename(ef)
        print(f"\n--- Checking Events: {ename} ---")
        with open(ef, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        evs = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_.]+)', raw)
        for ev in evs:
            if ev not in all_events:
                issues.append(f"[{ename}] Calls non-existent event '{ev}'!")
        recruits = re.findall(r'recruit_character\s*=\s*([A-Za-z0-9_]+)', raw)
        for r in recruits:
            if r not in all_characters:
                issues.append(f"[{ename}] Recruited character '{r}' not defined in common/characters!")

    print("\n================== DEEP AUDIT RESULTS ==================")
    if not issues:
        print("ZERO issues found! All references are completely intact.")
    else:
        print(f"Found {len(issues)} issues:")
        for iss in issues:
            print("  ", iss)

if __name__ == "__main__":
    deep_audit()
