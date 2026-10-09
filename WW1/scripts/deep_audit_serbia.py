# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ser_tree_path = ROOT / "common/national_focus/serbia.txt"
ser_tree = ser_tree_path.read_text(encoding="utf-8")

# 1. Parse all focuses
focuses = re.findall(r'focus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', ser_tree)
print(f"Total focuses parsed in Serbia: {len(focuses)}")

# 2. Extract referenced events
events_ref = re.findall(r'(?:country_event|news_event)\s*=\s*(?:\{\s*id\s*=\s*([a-zA-Z0-9_.]+)|([a-zA-Z0-9_.]+))', ser_tree)
events_called = set(e[0] or e[1] for e in events_ref if (e[0] or e[1]))
print(f"Events called from focus tree: {len(events_called)}")

# Collect all event IDs in mod
all_events = set()
for p in (ROOT / "events").glob("*.txt"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_.]+)', txt):
        all_events.add(m.group(1))

missing_events = [e for e in events_called if e not in all_events]
print(f"Missing events: {len(missing_events)} -> {missing_events}")

# 3. Extract ideas added and removed
ideas_added = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', ser_tree)
ideas_removed = re.findall(r'remove_ideas\s*=\s*([a-zA-Z0-9_]+)', ser_tree)
print(f"Total add_ideas: {len(ideas_added)} ({len(set(ideas_added))} unique)")
print(f"Total remove_ideas: {len(ideas_removed)} ({len(set(ideas_removed))} unique)")

# Check if ideas exist in common/ideas
all_ideas = set()
for p in (ROOT / "common/ideas").glob("*.txt"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    # match idea tokens
    for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[\s\S]*?allowed\s*=', txt):
        all_ideas.add(m.group(1))
    for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[\s\S]*?modifier\s*=', txt):
        all_ideas.add(m.group(1))

missing_ideas = [i for i in set(ideas_added) if i not in all_ideas]
print(f"Missing ideas: {len(missing_ideas)} -> {missing_ideas}")

# 4. Check localization
en_loc = (ROOT / "localisation/english/ww1_serbia_l_english.yml").read_text(encoding="utf-8", errors="ignore")
pt_loc = (ROOT / "localisation/braz_por/ww1_serbia_l_braz_por.yml").read_text(encoding="utf-8", errors="ignore")

missing_loc_en = []
missing_loc_pt = []

focus_ids = re.findall(r'id\s*=\s*(SER_[a-zA-Z0-9_]+)', ser_tree)
for fid in focus_ids:
    if f"{fid}:" not in en_loc:
        missing_loc_en.append(fid)
    if f"{fid}:" not in pt_loc:
        missing_loc_pt.append(fid)
    if f"{fid}_desc:" not in en_loc:
        missing_loc_en.append(f"{fid}_desc")
    if f"{fid}_desc:" not in pt_loc:
        missing_loc_pt.append(f"{fid}_desc")

print(f"Missing EN loc: {len(missing_loc_en)}")
print(f"Missing PT loc: {len(missing_loc_pt)}")

# 5. Check coordinates collisions
coords = Counter()
for m in re.finditer(r'x\s*=\s*(\d+)[\s\S]*?y\s*=\s*(\d+)', ser_tree):
    c = (int(m.group(1)), int(m.group(2)))
    coords[c] += 1

collisions = [c for c, count in coords.items() if count > 1]
print(f"Coordinate collisions: {len(collisions)} -> {collisions}")
