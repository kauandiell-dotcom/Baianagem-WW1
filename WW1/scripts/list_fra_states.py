import glob, os, re

locs = {}
for root, dirs, files in os.walk('localisation'):
    for f in files:
        if f.endswith('.yml'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    m = re.match(r'^\s*(STATE_\d+):\d*\s*"([^"]+)"', line)
                    if m:
                        locs[m.group(1)] = m.group(2)

target_ids = [1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 735, 785, 448, 449, 458, 459, 460, 461, 462, 513, 670, 671]
for sid in target_ids:
    key = f'STATE_{sid}'
    print(f'{sid:4d} | {key:10} | {locs.get(key, "Unknown")}')
