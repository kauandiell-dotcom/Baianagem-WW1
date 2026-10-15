import os, re

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

files = ["SOV.txt", "WHT.txt"]
total_chars = 0
issues = []

for f in files:
    p = os.path.join(repo, "common", "characters", f)
    if not os.path.exists(p): continue
    with open(p, "r", encoding="utf-8", errors="ignore") as fl:
        raw = fl.read()
    clean = re.sub(r'#.*$', '', raw, flags=re.MULTILINE)

    # find top level characters
    matches = list(re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', clean, re.MULTILINE))
    print(f"=== {f}: {len(matches)} characters ===")
    total_chars += len(matches)

    for i, m in enumerate(matches):
        cid = m.group(1)
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(clean)
        block = clean[start:end]

        # 1. Check portraits
        portraits = re.findall(r'(?:large|small)\s*=\s*"([^"]+)"', block)
        for port in portraits:
            norm_p = os.path.normpath(os.path.join(repo, port.replace("/", os.sep).replace("\\", os.sep)))
            if not os.path.exists(norm_p):
                issues.append(f"[{f}] {cid}: Missing portrait texture -> {port}")

        # 2. Check roles
        has_role = False
        roles = ["country_leader", "advisor", "corps_commander", "field_marshal", "navy_leader"]
        for r in roles:
            if f"{r} = {{" in block or f"{r} = {{" in block.replace(" ", ""):
                has_role = True
        if not has_role:
            issues.append(f"[{f}] {cid}: No valid role defined!")

        # 3. Check country leader ideology
        cl_matches = re.finditer(r'country_leader\s*=\s*\{([^}]+)\}', block)
        for cl in cl_matches:
            cblock = cl.group(1)
            if "ideology" not in cblock:
                issues.append(f"[{f}] {cid}: country_leader has no ideology!")

        # 4. Check corps commander / field marshal skills
        for mil in ["corps_commander", "field_marshal"]:
            if mil in block:
                mil_m = re.search(rf'{mil}\s*=\s*\{{([^}}]+)\}}', block)
                if mil_m:
                    mblock = mil_m.group(1)
                    if "skill" not in mblock:
                        issues.append(f"[{f}] {cid}: {mil} has no skill defined!")

print(f"\nTotal characters audited: {total_chars}")
if issues:
    print(f"Found {len(issues)} character issues:")
    for iss in issues:
        print(" ", iss)
else:
    print("Characters: ALL 100% VALID (zero missing textures, all roles and skills defined)")
