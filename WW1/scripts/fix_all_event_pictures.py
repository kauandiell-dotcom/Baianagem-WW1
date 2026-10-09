import re
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]

# 1. Parse sprite definitions
sprites = {}
for gfx_file in (ROOT / "interface").glob("*.gfx"):
    txt = gfx_file.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'spriteType\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', txt):
        sprites[m.group(1)] = (m.group(2).replace("\\", "/"), gfx_file)

# 2. Parse events
events = []
for ev_file in (ROOT / "events").glob("*.txt"):
    txt = ev_file.read_text(encoding="utf-8", errors="ignore")
    tokens = re.split(r'\b(country_event|news_event)\s*=\s*\{', txt)
    for i in range(1, len(tokens), 2):
        ev_type = tokens[i]
        body = tokens[i+1]
        id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_\.]+)', body)
        pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_\.]+)', body)
        if id_m:
            ev_id = id_m.group(1)
            pic = pic_m.group(1) if pic_m else None
            events.append((ev_type, ev_id, pic, ev_file.name))

# 3. Categorize texture usage
file_usage = {}
for ev_type, ev_id, pic, fname in events:
    if not pic or pic not in sprites:
        continue
    tex_path, gfx_file = sprites[pic]
    p = ROOT / tex_path
    if p.exists():
        file_usage.setdefault(p.resolve(), {"types": set(), "events": [], "path": p, "sprite": pic})["types"].add(ev_type)
        file_usage[p.resolve()]["events"].append((ev_type, ev_id, pic))

# Also include all files in gfx/event_pictures/ww1_* that might be in directories but not directly in events
for sub in ["ww1_alpha", "ww1_auh", "ww1_auh_extra", "ww1_britain", "ww1_britain_extra", "ww1_escalation", "ww1_ger_rus", "ww1_italy"]:
    for p in (ROOT / "gfx/event_pictures" / sub).glob("*.*"):
        if p.suffix.lower() in [".dds", ".png"]:
            res = p.resolve()
            if res not in file_usage:
                file_usage[res] = {"types": {"country_event"}, "events": [], "path": p, "sprite": ""}

print(f"Total event image files to process: {len(file_usage)}")

converted_country = 0
converted_news = 0
skipped = 0

for full_p, data in file_usage.items():
    p = data["path"]
    types = data["types"]
    
    # News event images: (397, 153)
    if types == {"news_event"} or p.name in ["great_war_dispatch.png", "sarajevo_assassination.png"]:
        target_size = (397, 153)
        is_news = True
    else:
        target_size = (210, 176)
        is_news = False
        
    try:
        im = Image.open(p)
        if im.size == target_size:
            skipped += 1
            im.close()
            continue
            
        im_rgba = im.convert("RGBA")
        fitted = ImageOps.fit(im_rgba, target_size, method=Image.Resampling.LANCZOS)
        im.close()
        
        # Save back in original format
        if p.suffix.lower() == ".dds":
            fitted.save(p, format="DDS")
        else:
            fitted.save(p, format="PNG")
            
        if is_news:
            converted_news += 1
        else:
            converted_country += 1
    except Exception as e:
        print(f"Error converting {p}: {e}")

print(f"Conversion complete!")
print(f"  Country events resized to (210, 176): {converted_country}")
print(f"  News events resized to (397, 153): {converted_news}")
print(f"  Already correct: {skipped}")
