import os
import re

country_file = 'history/countries/GER - Germany.txt'
with open(country_file, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

oobs = re.findall(r'oob\s*=\s*"([^"]+)"', text)
print(f'Starting OOBs in {country_file}: {oobs}')

# Count factories across GER states
ger_states = []
total_civ = 0
total_mil = 0
total_dock = 0

for root, dirs, files in os.walk('history/states'):
    for file in files:
        if file.endswith('.txt'):
            path = os.path.join(root, file)
            content = open(path, 'r', encoding='utf-8', errors='ignore').read()
            if 'owner = GER' in content:
                civ = sum(int(x) for x in re.findall(r'industrial_complex\s*=\s*(\d+)', content))
                mil = sum(int(x) for x in re.findall(r'arms_factory\s*=\s*(\d+)', content))
                dock = sum(int(x) for x in re.findall(r'dockyard\s*=\s*(\d+)', content))
                total_civ += civ
                total_mil += mil
                total_dock += dock
                ger_states.append((file, civ, mil, dock))

print(f'Total GER states: {len(ger_states)}')
print(f'Total Civ: {total_civ}, Total Mil: {total_mil}, Total Dock: {total_dock}')
print(f'Total Factories (civ + mil + dock): {total_civ + total_mil + total_dock}')

# Check divisions in OOB
for oob_name in oobs:
    oob_path = f'history/units/{oob_name}.txt'
    if os.path.exists(oob_path):
        oob_content = open(oob_path, 'r', encoding='utf-8', errors='ignore').read()
        divs = len(re.findall(r'division\s*=\s*\{', oob_content))
        print(f'OOB {oob_name}: {divs} divisions')
    else:
        print(f'OOB {oob_name} not found at {oob_path}')
