import os
import shutil

DONORS = [
    r'E:\SteamLibrary\steamapps\workshop\content\394360\3365515312\gfx\event_pictures',
    r'E:\SteamLibrary\steamapps\workshop\content\394360\2716194283\gfx\event_pictures',
]

TARGET_DIR = os.path.abspath('gfx/event_pictures')
os.makedirs(TARGET_DIR, exist_ok=True)

copied = {}
for d in DONORS:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.lower().endswith(('.dds', '.png', '.tga')):
                src = os.path.join(d, f)
                dst = os.path.join(TARGET_DIR, f)
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
                copied[f] = dst

print(f"Copied {len(copied)} event pictures to {TARGET_DIR}")

# Build interface/ww1_france_eventpictures.gfx
gfx_path = os.path.abspath('interface/ww1_france_eventpictures.gfx')
with open(gfx_path, 'w', encoding='utf-8') as out:
    out.write('spriteTypes = {\n\n')
    for f in sorted(copied.keys()):
        base = os.path.splitext(f)[0]
        sprite_name = f"GFX_report_event_{base}"
        out.write('\tspriteType = {\n')
        out.write(f'\t\tname = "{sprite_name}"\n')
        out.write(f'\t\ttexturefile = "gfx/event_pictures/{f}"\n')
        out.write('\t}\n\n')
    out.write('}\n')

print(f"Generated {gfx_path} with {len(copied)} sprites.")
