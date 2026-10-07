import os
import re

majors = ['FRA', 'ENG', 'RUS', 'AUH', 'ITA', 'GER', 'USA', 'TUR', 'OTT']

country_facs = {tag: {'civ': 0, 'mil': 0, 'dock': 0, 'states': 0} for tag in majors}

for root, dirs, files in os.walk('history/states'):
    for file in files:
        if file.endswith('.txt'):
            path = os.path.join(root, file)
            content = open(path, 'r', encoding='utf-8', errors='ignore').read()
            m = re.search(r'owner\s*=\s*([A-Z]{3})', content)
            if m and m.group(1) in country_facs:
                tag = m.group(1)
                civ = sum(int(x) for x in re.findall(r'industrial_complex\s*=\s*(\d+)', content))
                mil = sum(int(x) for x in re.findall(r'arms_factory\s*=\s*(\d+)', content))
                dock = sum(int(x) for x in re.findall(r'dockyard\s*=\s*(\d+)', content))
                country_facs[tag]['civ'] += civ
                country_facs[tag]['mil'] += mil
                country_facs[tag]['dock'] += dock
                country_facs[tag]['states'] += 1

print('Major Factory counts in history/states:')
for tag, data in country_facs.items():
    total = data['civ'] + data['mil'] + data['dock']
    if total > 0 or data['states'] > 0:
        print(f'{tag}: Civ={data["civ"]}, Mil={data["mil"]}, Dock={data["dock"]} -> Total={total} (States={data["states"]})')
