import os
import re

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"
int_dir = os.path.join(repo, "interface")
goals = []
for f in os.listdir(int_dir):
    if not f.endswith(".gfx"): continue
    with open(os.path.join(int_dir, f), "r", encoding="utf-8", errors="ignore") as file:
        c = file.read()
    for m in re.finditer(r'name\s*=\s*"([^"]+)"', c):
        n = m.group(1)
        if any(k in n.lower() for k in ['factory', 'production', 'oil', 'trade', 'secret', 'research', 'purge']):
            if not n.endswith("_shine"):
                goals.append(n)

print(f"Found {len(set(goals))} matching goal sprites in interface:")
for g in sorted(list(set(goals)))[:35]:
    print(" ", g)
