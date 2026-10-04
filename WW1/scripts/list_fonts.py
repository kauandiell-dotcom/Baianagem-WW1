import os, re

vg = r'E:\SteamLibrary\steamapps\common\Hearts of Iron IV\interface'
fonts = set()
for f in os.listdir(vg):
    if f.endswith('.gui'):
        fp = os.path.join(vg, f)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as fo:
            fonts.update(re.findall(r'font\s*=\s*"([^"]+)"', fo.read()))

print('Found', len(fonts), 'fonts:')
for f in sorted(list(fonts)):
    if any(k in f.lower() for k in ['hoi', 'header', 'map', 'cg', 'aldriche']):
        print('  ', f)
