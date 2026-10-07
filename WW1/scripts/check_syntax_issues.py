from pathlib import Path
import re

ROOT = Path(".")
print("=== CHECKING PICTURE EXTENSIONS IN SCRIPTS ===")
for d in ['common/ideas', 'common/decisions', 'common/national_focus', 'events']:
    for p in (ROOT / d).rglob('*.txt'):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            for lno, line in enumerate(f, 1):
                if re.search(r'\b(picture|icon)\s*=\s*[\"a-zA-Z0-9_\-]+\.(dds|png|tga)', line, re.IGNORECASE):
                    print(f"{p.name}:{lno} -> {line.strip()}")

print("\n=== CHECKING EVENTS FOR BROKEN PICTURES / MISSING LOC ===")
for p in (ROOT / "events").rglob("*.txt"):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # check for picture = GFX_... or event picture
    event_blocks = re.findall(r'(country_event|news_event)\s*=\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content)
    for etype, eb in event_blocks:
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.\-]+)', eb)
        pic_m = re.search(r'\bpicture\s*=\s*([a-zA-Z0-9_\.\-]+)', eb)
        title_m = re.search(r'\btitle\s*=\s*([a-zA-Z0-9_\.\-]+)', eb)
        desc_m = re.search(r'\bdesc\s*=\s*([a-zA-Z0-9_\.\-]+)', eb)
        if pic_m and ("." in pic_m.group(1)):
            print(f"Event {id_m.group(1) if id_m else 'unknown'} has raw filename in picture: {pic_m.group(1)}")
        if title_m and ("." in title_m.group(1)) and not re.match(r'^[a-zA-Z0-9_]+\.\d+$', title_m.group(1)):
            print(f"Event {id_m.group(1) if id_m else 'unknown'} has file-like title: {title_m.group(1)}")
