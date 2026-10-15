import os, re, glob
repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

candidates = []
for gf in glob.glob(os.path.join(repo, "interface", "*.gfx")):
    with open(gf, "r", encoding="utf-8", errors="ignore") as f:
        txt = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    for m in re.finditer(r'name\s*=\s*["\'](GFX_(?:event|report_event)[^"\']*)["\']', txt, re.IGNORECASE):
        sname = m.group(1)
        if any(k in sname.lower() for k in ["rus", "sov", "protest", "strike", "worker", "march", "palace", "riot"]):
            candidates.append(sname)

print(f"Unique candidates: {len(set(candidates))}")
for c in sorted(set(candidates)):
    print(f"  {c}")
