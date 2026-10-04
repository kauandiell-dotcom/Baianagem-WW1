import os, re, glob

subunits_used = set()
for f in glob.glob('history/units/*_1936_generic.txt'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    matches = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*\d+\s+y\s*=\s*\d+\s*\}', content)
    for m in matches:
        subunits_used.add(m)

print("Subunits used in all generic OOBs:")
for s in sorted(subunits_used):
    print(f"  {s}")
