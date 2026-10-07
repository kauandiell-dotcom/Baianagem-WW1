import re, os

with open('interface/ww1_national_mechanics.gfx', 'r', encoding='utf-8', errors='ignore') as f:
    gfx_text = f.read()

targets = [
    'AUS_dual_monarchy_compromise', 'AUS_tower_of_babel_army', 'AUS_skoda_siege_arsenals', 'AUS_alpine_carpathian_bastion', 'AUS_balkan_destiny',
    'FRA_wound_of_1870', 'FRA_elan_vital_doctrine', 'FRA_canon_75mm_supremacy', 'FRA_demographic_stagnation', 'FRA_third_republic_instability'
]

for t in targets:
    m = re.search(r'name\s*=\s*"GFX_idea_' + t + r'"[^}]*texturefile\s*=\s*"([^"]+)"', gfx_text, re.DOTALL)
    if m:
        path = m.group(1).replace('/', os.sep)
        exists = os.path.isfile(path)
        print(f'{t:32}: path={path} | exists={exists}')
    else:
        print(f'{t:32}: GFX entry NOT FOUND!')
