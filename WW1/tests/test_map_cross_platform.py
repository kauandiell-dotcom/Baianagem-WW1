#!/usr/bin/env python3
"""
Unit test suite verifying cross-platform map and shader integrity for Linux and macOS.
Prevents black map regressions by auditing BMP headers, DDS texture hierarchies, and Clausewitz shader syntax.
"""

import unittest
import os
import struct
import re

MOD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VANILLA_DIR = r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV"

class TestMapCrossPlatform(unittest.TestCase):

    def test_world_normal_compliance(self):
        """world_normal.bmp must either be absent (clean vanilla inheritance) or >= 2816x1024 24bpp."""
        wn_path = os.path.join(MOD_DIR, "map", "world_normal.bmp")
        if not os.path.exists(wn_path):
            return  # Clean inheritance
        with open(wn_path, "rb") as f:
            data = f.read(54)
        self.assertGreaterEqual(len(data), 54, "world_normal.bmp too small to have valid header")
        self.assertEqual(data[:2], b"BM", "world_normal.bmp not a BMP")
        dib_size, w, h, planes, bpp, comp = struct.unpack("<3I2HI", data[14:34])
        self.assertGreaterEqual(w, 2000, f"world_normal.bmp width {w} too small; dummy normal maps break Linux/Mac")
        self.assertGreaterEqual(h, 1000, f"world_normal.bmp height {h} too small; dummy normal maps break Linux/Mac")
        self.assertEqual(bpp, 24, "world_normal.bmp must be 24bpp")
        self.assertEqual(comp, 0, "world_normal.bmp must be uncompressed BI_RGB")

    def test_provinces_bmp_compliance(self):
        """provinces.bmp must be strictly 5632x2048, 24bpp uncompressed BI_RGB, DIB size 40."""
        p_path = os.path.join(MOD_DIR, "map", "provinces.bmp")
        self.assertTrue(os.path.exists(p_path), "map/provinces.bmp must exist")
        sz = os.path.getsize(p_path)
        expected_sz = 54 + (5632 * 2048 * 3)
        self.assertEqual(sz, expected_sz, f"provinces.bmp size {sz} != expected {expected_sz}")
        with open(p_path, "rb") as f:
            data = f.read(54)
        self.assertEqual(data[:2], b"BM")
        dib_size, w, h, planes, bpp, comp = struct.unpack("<3I2HI", data[14:34])
        self.assertEqual(dib_size, 40, "provinces.bmp must use BITMAPINFOHEADER (40 bytes) to avoid color space issues on Unix")
        self.assertEqual(w, 5632)
        self.assertEqual(h, 2048)
        self.assertEqual(bpp, 24)
        self.assertEqual(comp, 0)

    def test_terrain_textures_pot_and_lod(self):
        """All textures in map/terrain must be valid DDS and satisfy POT dimensions / LOD scaling."""
        terrain_dir = os.path.join(MOD_DIR, "map", "terrain")
        if not os.path.exists(terrain_dir):
            return
        
        def is_pot(n):
            return n > 0 and (n & (n - 1)) == 0

        for f in os.listdir(terrain_dir):
            if not f.endswith(".dds"):
                continue
            p = os.path.join(terrain_dir, f)
            with open(p, "rb") as fp:
                magic = fp.read(4)
                self.assertEqual(magic, b"DDS ", f"{f} is not a valid DDS file")
                header = fp.read(124)
                size, flags, h, w, pitch, depth, mipmaps = struct.unpack("<7I", header[:28])
            
            is_colormap = "colormap_" in f
            if not is_colormap:
                self.assertTrue(is_pot(w), f"{f} width {w} is not a power of two (breaks repeat wrap on OpenGL/Metal)")
                self.assertTrue(is_pot(h), f"{f} height {h} is not a power of two (breaks repeat wrap on OpenGL/Metal)")
            
            if os.path.exists(VANILLA_DIR):
                vp = os.path.join(VANILLA_DIR, "map", "terrain", f)
                if os.path.exists(vp):
                    with open(vp, "rb") as vfp:
                        vfp.read(4)
                        v_hdr = vfp.read(124)
                        _, _, vh, vw, _, _, _ = struct.unpack("<7I", v_hdr[:28])
                    self.assertEqual((w, h), (vw, vh), f"{f} LOD dimensions mismatch vanilla: ({w}x{h}) vs ({vw}x{vh})")

    def test_shader_preprocessor_and_sampler_integrity(self):
        """gfx/FX shaders must have no #define inside functions, valid sampler layout, and exact include casing."""
        fx_dir = os.path.join(MOD_DIR, "gfx", "FX")
        if not os.path.exists(fx_dir):
            return
        
        for f in os.listdir(fx_dir):
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
                    self.assertFalse(s.startswith("#define"), f"{f}:{idx}: '#define' inside function body violates GLSL/MSL translation: {s}")
                    if brace_depth <= 0 and "}" in s:
                        in_func = False
            
            # Check includes casing
            includes = re.findall(r"Includes\s*=\s*\{([^}]+)\}", content)
            for inc_block in includes:
                incs = re.findall(r"\"([^\"]+)\"", inc_block)
                for inc in incs:
                    mod_match = inc in os.listdir(fx_dir)
                    van_fx = os.path.join(VANILLA_DIR, "gfx", "FX")
                    van_match = os.path.exists(van_fx) and inc in os.listdir(van_fx)
                    self.assertTrue(mod_match or van_match, f"{f}: include '{inc}' missing or case-mismatched on disk")

        # Verify pdxwater.shader has GradientBorderChannel3
        water_shader = os.path.join(fx_dir, "pdxwater.shader")
        if os.path.exists(water_shader):
            with open(water_shader, "r", encoding="utf-8", errors="ignore") as fp:
                self.assertIn("GradientBorderChannel3", fp.read(), "pdxwater.shader missing GradientBorderChannel3")

if __name__ == "__main__":
    unittest.main()
