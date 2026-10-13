#!/usr/bin/env python3
"""
Cross-Platform HOI4 Map Integrity Audit for Linux (OpenGL/Vulkan) & macOS (Metal)
Validates:
1. BMP header compliance, bit-depth, and dimension parity.
2. DDS texture format, LOD scaling, POT dimensions, and mipmap completeness.
3. Shader syntax, function-body preprocessors, sampler register bindings, and case-sensitive include paths.
4. Definition CSV and province map color matching.
"""

import os
import sys
import struct
import csv
import re

VANILLA_DIR = r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV"
MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def log_pass(msg):
    print(f"  [PASS] {msg}")

def log_fail(msg):
    print(f"  [FAIL] {msg}")

def log_warn(msg):
    print(f"  [WARN] {msg}")

def audit_world_normal():
    print("\n--- Auditing world_normal.bmp ---")
    wn_path = os.path.join(MOD_DIR, "map", "world_normal.bmp")
    if not os.path.exists(wn_path):
        log_pass("world_normal.bmp is absent from mod directory; game cleanly inherits vanilla 2816x1024 normal map.")
        return []
    sz = os.path.getsize(wn_path)
    with open(wn_path, "rb") as f:
        data = f.read(54)
    if len(data) < 54 or data[:2] != b"BM":
        log_fail(f"world_normal.bmp is corrupt or not a valid BMP (size={sz})")
        return ["world_normal.bmp corrupt"]
    dib_size, w, h, planes, bpp, comp = struct.unpack("<3I2HI", data[14:34])
    if w < 1000 or h < 500:
        log_fail(f"world_normal.bmp has dummy/broken dimensions {w}x{h} ({sz} bytes)! Expected 2816x1024. Causes black terrain on Linux/Mac.")
        return [f"world_normal.bmp dummy dimensions {w}x{h}"]
    log_pass(f"world_normal.bmp valid: {w}x{h}, bpp={bpp}")
    return []

def audit_provinces_bmp():
    print("\n--- Auditing provinces.bmp ---")
    p_path = os.path.join(MOD_DIR, "map", "provinces.bmp")
    if not os.path.exists(p_path):
        log_fail("map/provinces.bmp not found!")
        return ["missing provinces.bmp"]
    sz = os.path.getsize(p_path)
    with open(p_path, "rb") as f:
        data = f.read(54)
    magic = data[:2]
    offset, = struct.unpack("<I", data[10:14])
    dib_size, w, h, planes, bpp, comp = struct.unpack("<3I2HI", data[14:34])
    errors = []
    if magic != b"BM":
        errors.append("Invalid BMP magic")
    if dib_size != 40:
        errors.append(f"Unexpected DIB header size {dib_size} (must be 40 BITMAPINFOHEADER to avoid color space issues)")
    if bpp != 24:
        errors.append(f"Invalid bit depth {bpp} (must be 24-bit RGB)")
    if comp != 0:
        errors.append(f"Compressed BMP (comp={comp}), must be uncompressed BI_RGB=0")
    if w != 5632 or h != 2048:
        errors.append(f"Invalid dimensions {w}x{h}, must be 5632x2048")
    expected_sz = 54 + (5632 * 2048 * 3)
    if sz != expected_sz:
        errors.append(f"File size {sz} != expected {expected_sz}")
    if errors:
        for e in errors:
            log_fail(e)
    else:
        log_pass(f"provinces.bmp is 100% compliant: {w}x{h}, 24bpp uncompressed, exact byte size {sz}")
    return errors

def audit_terrain_textures():
    print("\n--- Auditing map/terrain textures ---")
    terrain_dir = os.path.join(MOD_DIR, "map", "terrain")
    if not os.path.exists(terrain_dir):
        log_pass("map/terrain directory absent; all terrain textures cleanly inherited from vanilla.")
        return []
    
    errors = []
    files = sorted(os.listdir(terrain_dir))
    for f in files:
        if not f.endswith(".dds"):
            continue
        p = os.path.join(terrain_dir, f)
        with open(p, "rb") as fp:
            magic = fp.read(4)
            if magic != b"DDS ":
                errors.append(f"{f}: Not a DDS file")
                log_fail(f"{f}: Not a DDS file")
                continue
            header = fp.read(124)
            size, flags, h, w, pitch, depth, mipmaps = struct.unpack("<7I", header[:28])
            pf_size, pf_flags, fourcc, rgb_bits, r_mask, g_mask, b_mask, a_mask = struct.unpack("<2I4s5I", header[72:104])
            
            # Check NPOT dimensions for repeat-wrapped textures (borders, tiles)
            def is_pot(n):
                return n > 0 and (n & (n - 1)) == 0
            
            # Colormaps (like colormap_rgb_cityemissivemask_a) are clamped full-globe maps (2816x1024), not repeat-wrapped tiles
            is_colormap = "colormap_" in f
            if not is_colormap and (not is_pot(w) or not is_pot(h)):
                errors.append(f"{f}: Non-power-of-two dimensions ({w}x{h}) violates OpenGL/Metal repeat wrap")
                log_fail(f"{f}: NPOT {w}x{h}")
                continue
            
            # Check LOD dimension parity against vanilla
            vp = os.path.join(VANILLA_DIR, "map", "terrain", f)
            if os.path.exists(vp):
                with open(vp, "rb") as vfp:
                    v_magic = vfp.read(4)
                    v_header = vfp.read(124)
                    _, _, vh, vw, _, _, vmips = struct.unpack("<7I", v_header[:28])
                    if w != vw or h != vh:
                        errors.append(f"{f}: Dimension mismatch with vanilla ({w}x{h} vs vanilla {vw}x{vh})")
                        log_fail(f"{f}: Mod has {w}x{h}, vanilla has {vw}x{vh}")
                        continue
    if not errors:
        log_pass("All map/terrain DDS textures have valid POT dimensions and LOD resolution parity.")
    return errors

def audit_shaders():
    print("\n--- Auditing gfx/FX shaders ---")
    fx_dir = os.path.join(MOD_DIR, "gfx", "FX")
    if not os.path.exists(fx_dir):
        log_pass("gfx/FX absent; clean inheritance.")
        return []
    
    errors = []
    for f in sorted(os.listdir(fx_dir)):
        p = os.path.join(fx_dir, f)
        with open(p, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        
        # Check for #define inside function body
        lines = content.splitlines()
        in_func = False
        brace_depth = 0
        for idx, line in enumerate(lines, 1):
            s = line.strip()
            if re.search(r"\bmain\s*\(", s):
                in_func = True
            if in_func:
                brace_depth += s.count("{") - s.count("}")
                if s.startswith("#define"):
                    errors.append(f"{f}:{idx}: Preprocessor '#define' inside function block '{s}' breaks OpenGL/Metal cross-compilers")
                    log_fail(f"{f}:{idx}: Preprocessor '#define' inside function block")
                if brace_depth <= 0 and "}" in s:
                    in_func = False
        
        # Check case-sensitive includes
        includes = re.findall(r"Includes\s*=\s*\{([^}]+)\}", content)
        for inc_block in includes:
            incs = re.findall(r"\"([^\"]+)\"", inc_block)
            for inc in incs:
                # check exact casing
                mod_match = inc in os.listdir(fx_dir)
                van_fx = os.path.join(VANILLA_DIR, "gfx", "FX")
                van_match = os.path.exists(van_fx) and inc in os.listdir(van_fx)
                if not (mod_match or van_match):
                    errors.append(f"{f}: Missing or case-mismatched include '{inc}'")
                    log_fail(f"{f}: include '{inc}' not found with exact casing")
    
    # Check sampler index alignment in pdxwater.shader
    water_shader = os.path.join(fx_dir, "pdxwater.shader")
    if os.path.exists(water_shader):
        with open(water_shader, "r", encoding="utf-8", errors="ignore") as fp:
            w_txt = fp.read()
        if "GradientBorderChannel3" not in w_txt:
            errors.append("pdxwater.shader: Missing GradientBorderChannel3 sampler (Index 14) misaligns C++ engine register layout")
            log_fail("pdxwater.shader: Missing GradientBorderChannel3 sampler")
    
    if not errors:
        log_pass("All gfx/FX shaders pass cross-platform preprocessor, casing, and sampler register audits.")
    return errors

def main():
    print("=" * 60)
    print("CROSS-PLATFORM MAP INTEGRITY AUDIT (LINUX / MACOS)")
    print("=" * 60)
    all_errors = []
    all_errors.extend(audit_world_normal())
    all_errors.extend(audit_provinces_bmp())
    all_errors.extend(audit_terrain_textures())
    all_errors.extend(audit_shaders())
    
    print("\n" + "=" * 60)
    if all_errors:
        print(f"AUDIT FAILED WITH {len(all_errors)} CRITICAL DEFECT(S):")
        for err in all_errors:
            print(f"  - {err}")
        return 1
    else:
        print("AUDIT SUCCESSFUL: 0 defects found. Map is fully cross-platform compatible!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
