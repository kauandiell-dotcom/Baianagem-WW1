"""
Adversarial DDS Stress Test Harness
Target: C:\\Users\\Usuário\\Pictures\\Baianagem-WW1\\WW1\\gfx\\interface\\goals

Empirically stress-tests every DDS texture asset:
1. Binary Magic & Struct Header Validation (DDS magic, dwSize=124, dwFlags, pixel format struct dwSize=32, etc.)
2. Pillow RGBA Decoding & Format Integrity
3. Visual & Pixel Distribution Analysis:
   - Non-empty bounding box check
   - Channel extrema & alpha range check
   - Pixel standard deviation / variance check
   - Unique RGBA color diversity (detecting solid/dummy placeholders)
   - Visible pixel ratio (alpha > 10)
4. Comprehensive Cross-Referencing:
   - Direct inspection of all files on disk
   - Cross-referencing with spec.py (32 expected focuses)
   - Cross-referencing with interface/ww1_germany_goals.gfx
"""

import os
import sys
import math
import struct
from PIL import Image

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GOALS_DIR = os.path.join(MOD_ROOT, "gfx", "interface", "goals")
GFX_FILE = os.path.join(MOD_ROOT, "interface", "ww1_germany_goals.gfx")

# DDSD flags
DDSD_CAPS = 0x1
DDSD_HEIGHT = 0x2
DDSD_WIDTH = 0x4
DDSD_PITCH = 0x8
DDSD_PIXELFORMAT = 0x1000
DDSD_MIPMAPCOUNT = 0x20000
DDSD_LINEARSIZE = 0x80000
DDSD_DEPTH = 0x800000

# DDPF flags
DDPF_ALPHAPIXELS = 0x1
DDPF_ALPHA = 0x2
DDPF_FOURCC = 0x4
DDPF_RGB = 0x40
DDPF_YUV = 0x200
DDPF_LUMINANCE = 0x20000


def analyze_dds_file(file_path: str):
    """Deep structural and statistical analysis of a single DDS file."""
    assert os.path.isfile(file_path), f"File not found: {file_path}"
    file_size = os.path.getsize(file_path)
    filename = os.path.basename(file_path)

    # 1. Binary checks
    if file_size < 128:
        raise ValueError(f"File too small for DDS header: {file_size} bytes")

    with open(file_path, "rb") as f:
        magic = f.read(4)
        if magic != b"DDS ":
            raise ValueError(f"Invalid magic: {magic!r}, expected b'DDS ' (0x20534444)")

        header_bytes = f.read(124)
        if len(header_bytes) < 124:
            raise ValueError(f"Truncated header ({len(header_bytes)} bytes)")

        (
            dw_size, dw_flags, dw_height, dw_width,
            dw_pitch_linear, dw_depth, dw_mipmaps
        ) = struct.unpack_from("<7I", header_bytes, 0)

        if dw_size != 124:
            raise ValueError(f"Invalid dwSize: {dw_size}, must be 124 (0x7C)")

        if dw_width <= 0 or dw_height <= 0:
            raise ValueError(f"Invalid dimensions: {dw_width}x{dw_height}")

        # DDS_PIXELFORMAT at offset 72
        (
            pf_size, pf_flags, pf_fourcc, pf_bitcount,
            pf_rmask, pf_gmask, pf_bmask, pf_amask
        ) = struct.unpack_from("<8I", header_bytes, 72)

        if pf_size != 32:
            raise ValueError(f"Invalid pixel format dwSize: {pf_size}, must be 32 (0x20)")

        fourcc_str = struct.pack("<I", pf_fourcc).decode("latin-1", errors="replace") if (pf_flags & DDPF_FOURCC) else "NONE"

        # dwCaps at offset 104
        dw_caps1, dw_caps2, dw_caps3, dw_caps4 = struct.unpack_from("<4I", header_bytes, 104)

    # 2. Pillow RGBA decode
    try:
        im = Image.open(file_path)
    except Exception as e:
        raise ValueError(f"Pillow Image.open failed: {e}")

    im_format = im.format
    im_size = im.size
    im_mode = im.mode

    if im_size != (dw_width, dw_height):
        raise ValueError(f"Pillow size {im_size} does not match DDS header ({dw_width}, {dw_height})")

    # Load image and ensure RGBA
    im_rgba = im.convert("RGBA")
    pixels = list(im_rgba.getdata())
    total_pixels = len(pixels)

    # 3. Adversarial Pixel Distribution Checks
    bbox = im_rgba.getbbox()
    if bbox is None:
        raise ValueError(f"Texture is completely empty/transparent (bbox is None)!")

    extrema = im_rgba.getextrema()
    r_ext, g_ext, b_ext, a_ext = extrema

    if a_ext[1] == 0:
        raise ValueError(f"Alpha channel is completely zero (100% invisible)!")

    # Check for flat solid colors
    if r_ext[0] == r_ext[1] and g_ext[0] == g_ext[1] and b_ext[0] == b_ext[1]:
        raise ValueError(f"Texture is a solid single flat color: {r_ext[0], g_ext[0], b_ext[0]}!")

    # Visible pixels (alpha > 10)
    visible_pixels = [p for p in pixels if p[3] > 10]
    visible_ratio = len(visible_pixels) / total_pixels

    if visible_ratio < 0.10:
        raise ValueError(f"Visible pixel ratio suspiciously low: {visible_ratio:.1%}")

    # Unique colors among visible pixels
    unique_colors = len(set(visible_pixels))
    if unique_colors < 16:
        raise ValueError(f"Extremely low unique color count ({unique_colors}), possible dummy asset!")

    # Calculate standard deviation of color channels for visible pixels
    avg_r = sum(p[0] for p in visible_pixels) / len(visible_pixels)
    avg_g = sum(p[1] for p in visible_pixels) / len(visible_pixels)
    avg_b = sum(p[2] for p in visible_pixels) / len(visible_pixels)

    var_r = sum((p[0] - avg_r) ** 2 for p in visible_pixels) / len(visible_pixels)
    var_g = sum((p[1] - avg_g) ** 2 for p in visible_pixels) / len(visible_pixels)
    var_b = sum((p[2] - avg_b) ** 2 for p in visible_pixels) / len(visible_pixels)

    std_r = math.sqrt(var_r)
    std_g = math.sqrt(var_g)
    std_b = math.sqrt(var_b)

    # Average standard deviation
    avg_std = (std_r + std_g + std_b) / 3.0
    if avg_std < 5.0:
        raise ValueError(f"Average color standard deviation is too low ({avg_std:.2f}), image lacks detail!")

    return {
        "filename": filename,
        "size_bytes": file_size,
        "width": dw_width,
        "height": dw_height,
        "flags": hex(dw_flags),
        "pf_flags": hex(pf_flags),
        "fourcc": fourcc_str,
        "bitcount": pf_bitcount,
        "pil_format": im_format,
        "pil_mode": im_mode,
        "bbox": bbox,
        "extrema": extrema,
        "visible_ratio": visible_ratio,
        "unique_colors": unique_colors,
        "std_rgb": (round(std_r, 2), round(std_g, 2), round(std_b, 2)),
        "avg_std": round(avg_std, 2),
    }


def parse_gfx_sprites():
    """Extract sprites from ww1_germany_goals.gfx."""
    assert os.path.isfile(GFX_FILE), f"GFX file missing: {GFX_FILE}"
    with open(GFX_FILE, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    import re
    sprite_pattern = re.compile(
        r'SpriteType\s*=\s*\{([^}]+(?:animation\s*=\s*\{[^}]*\}[^}]*)*)\}',
        re.MULTILINE | re.IGNORECASE
    )
    name_pat = re.compile(r'name\s*=\s*"([^"]+)"')
    tex_pat = re.compile(r'texturefile\s*=\s*"([^"]+)"')

    sprites = {}
    for m in sprite_pattern.finditer(content):
        blk = m.group(1)
        n = name_pat.search(blk)
        t = tex_pat.search(blk)
        if n and t:
            sprites[n.group(1).strip()] = t.group(1).strip()
    return sprites


def run_full_adversarial_suite():
    """Execute all adversarial checks and print comprehensive tabular report."""
    print("=" * 80)
    print("EMPIRICAL ADVERSARIAL STRESS TEST: GOAL DDS TEXTURES")
    print("=" * 80)

    if not os.path.isdir(GOALS_DIR):
        print(f"CRITICAL ERROR: Goals directory does not exist: {GOALS_DIR}")
        return False, []

    files = sorted(os.listdir(GOALS_DIR))
    print(f"Found {len(files)} items in {GOALS_DIR}")

    non_dds = [f for f in files if not f.lower().endswith(".dds")]
    if non_dds:
        print(f"WARNING: Non-DDS files found in goals directory: {non_dds}")

    dds_files = [f for f in files if f.lower().endswith(".dds")]
    print(f"Testing {len(dds_files)} DDS files...\n")

    results = []
    failures = []

    print(f"{'Filename':<46} {'Size':>7} {'Dim':>9} {'Fmt':>5} {'Vis%':>6} {'Uniq':>6} {'StdDev':>7} {'Status':>8}")
    print("-" * 100)

    for fname in dds_files:
        fpath = os.path.join(GOALS_DIR, fname)
        try:
            res = analyze_dds_file(fpath)
            results.append(res)
            dim_str = f"{res['width']}x{res['height']}"
            vis_str = f"{res['visible_ratio']*100:.1f}%"
            print(f"{fname:<46} {res['size_bytes']:>7} {dim_str:>9} {res['fourcc']:>5} {vis_str:>6} {res['unique_colors']:>6} {res['avg_std']:>7.2f} {'PASS':>8}")
        except Exception as e:
            failures.append((fname, str(e)))
            print(f"{fname:<46} {'FAILED: ' + str(e)}")

    print("\n" + "=" * 80)
    print("GFX SPRITE REGISTRATION & SPEC CROSS-REFERENCE")
    print("=" * 80)

    sprites = parse_gfx_sprites()
    print(f"Found {len(sprites)} SpriteTypes in ww1_germany_goals.gfx")

    unregistered_dds = []
    for dds in dds_files:
        expected_ref = f"gfx/interface/goals/{dds}"
        matching = [s_name for s_name, s_tex in sprites.items() if s_tex.replace("\\", "/") == expected_ref]
        if not matching:
            unregistered_dds.append(dds)

    if unregistered_dds:
        print(f"WARNING: The following DDS files are not referenced in GFX: {unregistered_dds}")
    else:
        print("PASS: All DDS files on disk are referenced by at least one SpriteType in GFX.")

    missing_textures = []
    for s_name, s_tex in sprites.items():
        rel_path = s_tex.replace("\\", "/")
        full_path = os.path.join(MOD_ROOT, rel_path)
        if not os.path.isfile(full_path):
            missing_textures.append((s_name, s_tex))

    if missing_textures:
        print(f"FAIL: The following GFX entries reference nonexistent files: {missing_textures}")
        failures.extend([("GFX:" + m[0], f"References missing file {m[1]}") for m in missing_textures])
    else:
        print(f"PASS: All {len(sprites)} SpriteType texturefile references exist on disk.")

    sys.path.insert(0, os.path.join(MOD_ROOT, "tests"))
    try:
        from spec import EXPECTED_FOCUSES
        missing_spec_dds = []
        missing_spec_sprites = []
        for fid, fmeta in EXPECTED_FOCUSES.items():
            dds_name = fmeta["dds"]
            icon_name = fmeta["icon"]
            if dds_name not in dds_files:
                missing_spec_dds.append((fid, dds_name))
            if icon_name not in sprites:
                missing_spec_sprites.append((fid, icon_name))
            if f"{icon_name}_shine" not in sprites:
                missing_spec_sprites.append((fid, f"{icon_name}_shine"))

        if missing_spec_dds:
            print(f"FAIL: Missing DDS files required by spec.py: {missing_spec_dds}")
            failures.extend([("SPEC_DDS:" + m[0], m[1]) for m in missing_spec_dds])
        else:
            print(f"PASS: All {len(EXPECTED_FOCUSES)} focuses from spec.py have matching DDS files on disk.")

        if missing_spec_sprites:
            print(f"FAIL: Missing SpriteTypes required by spec.py: {missing_spec_sprites}")
            failures.extend([("SPEC_GFX:" + m[0], m[1]) for m in missing_spec_sprites])
        else:
            print(f"PASS: All {len(EXPECTED_FOCUSES)} focuses have base and _shine SpriteTypes in GFX.")
    except Exception as e:
        print(f"Could not check spec.py: {e}")

    print("\n" + "=" * 80)
    print("STRESS TEST SUMMARY")
    print("=" * 80)
    print(f"Total DDS files inspected: {len(dds_files)}")
    print(f"Total passed: {len(results)}")
    print(f"Total failed: {len(failures)}")

    success = (len(failures) == 0 and len(dds_files) >= 32)
    verdict = "APPROVE" if success else "REJECT"
    print(f"EMPIRICAL VERDICT: {verdict}")
    print("=" * 80)
    return success, results, failures


if __name__ == "__main__":
    success, results, failures = run_full_adversarial_suite()
    sys.exit(0 if success else 1)
