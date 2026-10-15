import os
import re

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

def check_gfx():
    sprites = set()
    interface_dir = os.path.join(repo, "interface")
    for gfxf in os.listdir(interface_dir):
        if not gfxf.endswith(".gfx"): continue
        with open(os.path.join(interface_dir, gfxf), "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        for m in re.finditer(r'name\s*=\s*"([^"]+)"', c):
            sprites.add(m.group(1))

    print(f"Total sprites registered in interface/*.gfx: {len(sprites)}")

    trees = ["soviet.txt", "soviet_russia.txt", "white_russia.txt"]
    for t in trees:
        tp = os.path.join(repo, "common", "national_focus", t)
        with open(tp, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        icons = re.findall(r'icon\s*=\s*([^\s{}]+)', c)
        missing = []
        for ic in set(icons):
            if ic not in sprites:
                # check file
                norm = os.path.normpath(os.path.join(repo, ic.replace("/", os.sep)))
                if not os.path.exists(norm) and not os.path.exists(norm + ".dds") and not os.path.exists(norm + ".png"):
                    missing.append(ic)
        if missing:
            print(f"[MISSING GFX] {t} has {len(missing)} missing goal icons: {missing}")
        else:
            print(f"-> {t}: 100% of {len(set(icons))} goal icons exist!")

if __name__ == "__main__":
    check_gfx()
