import glob
import re

loc_states = {}
for f in glob.glob("localisation/english/*.yml"):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        for line in fp:
            m = re.match(r'^\s*(STATE_\d+):\d*\s*"([^"]+)"', line)
            if m:
                loc_states[m.group(1)] = m.group(2)

print("Total state locs found:", len(loc_states))

keywords = ["thessaloniki", "macedonia", "salonika", "thrace", "corfu", "epirus", "albania", "durres", "scutari", "montenegro", "belgrade", "morava", "kosovo", "vojvodina", "bosnia", "croatia", "slovenia", "dalmatia"]

matched_states = {}
for sid, sname in loc_states.items():
    slower = sname.lower()
    for kw in keywords:
        if kw in slower:
            num = sid.replace("STATE_", "")
            matched_states[int(num)] = sname
            break

for num in sorted(matched_states):
    print(f"State {num}: {matched_states[num]}")
