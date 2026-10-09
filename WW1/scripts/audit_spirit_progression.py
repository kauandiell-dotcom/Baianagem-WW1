from pathlib import Path
import re

content = Path("common/national_focus/turkey.txt").read_text(encoding="utf-8")
focus_blocks = re.split(r'\n\s*focus\s*=\s*\{', content)

records = []
for b in focus_blocks[1:]:
    id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    if not id_m: continue
    fid = id_m.group(1)
    
    adds = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', b)
    rems = re.findall(r'remove_ideas\s*=\s*([a-zA-Z0-9_]+)', b)
    timeds = re.findall(r'add_timed_idea\s*=\s*\{\s*idea\s*=\s*([a-zA-Z0-9_]+)', b)
    
    if adds or rems or timeds:
        records.append((fid, adds, rems, timeds))

print(f"Total focuses interacting with ideas: {len(records)}")
for fid, adds, rems, timeds in records:
    print(f"  {fid}: adds={adds}, rems={rems}, timeds={timeds}")
