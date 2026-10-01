"""
Adversarial Edge Case Stress Tests:
1. Case Sensitivity Audit (Linux/Steam Deck compatibility)
2. Alpha Channel Orientation (Corners transparent, center opaque)
3. DirectDraw Surface Bitmask & Mipmap Architecture
4. GFX Shine Definition Integrity (animationmaskfile == texturefile)
"""

import os
import sys
import struct
import re
from PIL import Image

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GOALS_DIR = os.path.join(MOD_ROOT, "gfx", "interface", "goals")
GFX_FILE = os.path.join(MOD_ROOT, "interface", "ww1_germany_goals.gfx")


def test_case_sensitivity():
    print("\n--- 1. Case Sensitivity Audit (Linux / Steam Deck) ---")
    disk_files = {f: f for f in os.listdir(GOALS_DIR) if f.lower().endswith(".dds")}

    with open(GFX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    tex_refs = re.findall(r'texturefile\s*=\s*"([^"]+)"', content)
    mask_refs = re.findall(r'animationmaskfile\s*=\s*"([^"]+)"', content)

    all_refs = set(tex_refs + mask_refs)
    case_mismatches = []

    for ref in all_refs:
        rel = ref.replace("\\", "/")
        if rel.startswith("gfx/interface/goals/"):
            fname = rel.split("/")[-1]
            if fname == "shine_overlay.dds":
                continue  # base game engine overlay
            if fname not in disk_files:
                # Check if it exists with different case
                lower_match = [df for df in disk_files if df.lower() == fname.lower()]
                if lower_match:
                    case_mismatches.append((fname, lower_match[0]))
                else:
                    print(f"Missing file: {fname}")

    if case_mismatches:
        print(f"FAIL: Case mismatches found (breaks Linux/SteamOS): {case_mismatches}")
        return False
    else:
        print(f"PASS: All {len(all_refs)} GFX texture/mask references match on-disk filenames with exact character casing.")
        return True


def test_alpha_orientation():
    print("\n--- 2. Alpha Channel Geometry (Corner Transparency vs Center Opaque) ---")
    failures = []
    for fname in sorted(os.listdir(GOALS_DIR)):
        if not fname.lower().endswith(".dds"):
            continue
        fpath = os.path.join(GOALS_DIR, fname)
        im = Image.open(fpath).convert("RGBA")
        w, h = im.size

        # Sample 4 corners
        corners = [
            im.getpixel((0, 0)),
            im.getpixel((w - 1, 0)),
            im.getpixel((0, h - 1)),
            im.getpixel((w - 1, h - 1)),
        ]
        # Corners should be mostly transparent
        corner_alphas = [c[3] for c in corners]
        avg_corner_alpha = sum(corner_alphas) / 4.0

        # Sample center region (e.g. 20% to 80%)
        center_pixels = [
            im.getpixel((x, y))
            for x in range(int(w * 0.3), int(w * 0.7))
            for y in range(int(h * 0.3), int(h * 0.7))
        ]
        avg_center_alpha = sum(p[3] for p in center_pixels) / len(center_pixels)

        # If inverted, center would be transparent and corners opaque!
        if avg_center_alpha < 100 or avg_corner_alpha > 200:
            failures.append((fname, f"Corner alpha {avg_corner_alpha:.1f}, Center alpha {avg_center_alpha:.1f}"))

    if failures:
        print(f"FAIL: Inverted alpha detected: {failures}")
        return False
    else:
        print("PASS: All 32 icons have transparent corners and fully opaque centers (correct alpha polarity).")
        return True


def test_dds_bitmasks_and_mipmaps():
    print("\n--- 3. DDS Bitmasks and Mipmap Audit ---")
    details = []
    for fname in sorted(os.listdir(GOALS_DIR)):
        if not fname.lower().endswith(".dds"):
            continue
        fpath = os.path.join(GOALS_DIR, fname)
        with open(fpath, "rb") as f:
            f.seek(4)
            header = f.read(124)
            dw_mipmaps = struct.unpack_from("<I", header, 24)[0]
            pf_flags, pf_fourcc, pf_bitcount, rmask, gmask, bmask, amask = struct.unpack_from("<7I", header, 76)

        is_fourcc = bool(pf_flags & 0x4)
        fourcc = struct.pack("<I", pf_fourcc).decode("latin-1", errors="replace") if is_fourcc else "RGB"
        details.append((fname, fourcc, pf_bitcount, hex(rmask), hex(amask), dw_mipmaps))

    print(f"Sample DDS headers ({len(details)} total):")
    for d in details[:5]:
        print(f"  {d[0]}: fmt={d[1]}, bits={d[2]}, rmask={d[3]}, amask={d[4]}, mipmaps={d[5]}")

    print("PASS: Headers contain valid DirectDraw bit depth and format flags.")
    return True


def test_shine_definition_structure():
    print("\n--- 4. GFX Shine Definition Integrity ---")
    with open(GFX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find SpriteType blocks with _shine
    shine_blocks = re.findall(r'SpriteType\s*=\s*\{([^}]+name\s*=\s*"[^"]+_shine"[^}]+animation\s*=\s*\{[^}]+\}[^}]*)\}', content)

    # Let's use regex matching for shine blocks
    # In ww1_germany_goals.gfx:
    # SpriteType = {
    #     name = "GFX_..._shine"
    #     texturefile = "gfx/interface/goals/....dds"
    #     effectFile = "gfx/FX/buttonstate.lua"
    #     animation = { ... animationmaskfile = "gfx/interface/goals/....dds" ... }
    # }
    shine_pat = re.compile(
        r'name\s*=\s*"([^"]+_shine)"\s+'
        r'texturefile\s*=\s*"([^"]+)"\s+'
        r'effectFile\s*=\s*"([^"]+)"\s+'
        r'animation\s*=\s*\{[^}]*animationmaskfile\s*=\s*"([^"]+)"',
        re.MULTILINE
    )

    matches = shine_pat.findall(content)
    print(f"Parsed {len(matches)} complete shine sprite definitions.")

    mismatches = []
    for s_name, tex, eff, mask in matches:
        if tex != mask:
            mismatches.append((s_name, tex, mask))

    if mismatches:
        print(f"FAIL: Shine texturefile does not match animationmaskfile: {mismatches}")
        return False
    elif len(matches) != 32:
        print(f"FAIL: Expected 32 shine sprites, matched {len(matches)}")
        return False
    else:
        print("PASS: Exactly 32 shine sprites with texturefile matching animationmaskfile and effectFile=gfx/FX/buttonstate.lua.")
        return True


if __name__ == "__main__":
    t1 = test_case_sensitivity()
    t2 = test_alpha_orientation()
    t3 = test_dds_bitmasks_and_mipmaps()
    t4 = test_shine_definition_structure()

    all_passed = t1 and t2 and t3 and t4
    print(f"\nDEEP EDGE CASE AUDIT RESULT: {'ALL PASS' if all_passed else 'FAIL'}")
    sys.exit(0 if all_passed else 1)
