# scripts/verify_rework.py
import os, re

# 1. GFX audit
gfx_path = "interface/ww1_ottoman_goals.gfx"
with open(gfx_path, "r", encoding="utf-8") as f:
    gfx_text = f.read()

open_b = gfx_text.count("{")
close_b = gfx_text.count("}")
print(f"GFX Brackets: open={open_b}, close={close_b}, diff={open_b - close_b}")
assert open_b == close_b, "Mismatched brackets in GFX file!"

sprites = re.findall(r'name\s*=\s*"([^"]+)"', gfx_text)
normal_sprites = [s for s in sprites if not s.endswith("_shine")]
shine_sprites = [s for s in sprites if s.endswith("_shine")]
print(f"Total sprites: {len(sprites)}, Normal: {len(normal_sprites)}, Shine: {len(shine_sprites)}")
assert len(normal_sprites) == 256, f"Expected 256 normal sprites, got {len(normal_sprites)}"
assert len(shine_sprites) == 256, f"Expected 256 shine sprites, got {len(shine_sprites)}"

textures = re.findall(r'texturefile\s*=\s*"([^"]+)"', gfx_text)
missing_textures = [t for t in textures if not os.path.exists(t.replace("/", "\\"))]
print(f"Textures referenced: {len(textures)}, Missing on disk: {len(missing_textures)}")
assert len(missing_textures) == 0, f"Found {len(missing_textures)} missing textures!"

# 2. Localisation audit
for loc_path, lang in [("localisation/braz_por/ww1_ottoman_l_braz_por.yml", "PT-BR"),
                       ("localisation/english/ww1_ottoman_l_english.yml", "EN")]:
    with open(loc_path, "rb") as f:
        raw = f.read()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    print(f"{lang} has UTF-8 BOM: {has_bom}")
    assert has_bom, f"{lang} missing UTF-8 BOM!"
    
    text = raw.decode("utf-8")
    lines = text.splitlines()
    print(f"{lang} total lines: {len(lines)}")
    
    # Check for placeholder sentences
    placeholders = [l for l in lines if "Through the implementation of" in l or "Com a implementação de" in l]
    print(f"{lang} placeholder count: {len(placeholders)}")
    assert len(placeholders) == 0, f"Found placeholders in {lang}!"

# 3. Focus tree audit
with open("common/national_focus/turkey.txt", "r", encoding="utf-8") as f:
    tur_tree = f.read()

focus_ids = re.findall(r'^\s*id\s*=\s*(TUR_\w+)', tur_tree, re.M)
print(f"Focus tree total focuses: {len(focus_ids)}")
assert len(focus_ids) == 256, f"Expected 256 focuses in tree, got {len(focus_ids)}"

# Check that every focus in tree has normal and shine sprite
normal_set = set(normal_sprites)
shine_set = set(shine_sprites)
for fid in focus_ids:
    expected_normal = f"GFX_focus_{fid}"
    expected_shine = f"GFX_focus_{fid}_shine"
    assert expected_normal in normal_set, f"Missing {expected_normal}"
    assert expected_shine in shine_set, f"Missing {expected_shine}"

print("ALL OTTOMAN REWORK AUDITS PASSED WITH 100% SUCCESS!")
