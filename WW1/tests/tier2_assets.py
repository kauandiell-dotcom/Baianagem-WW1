"""
Tier 2: Boundary & Asset Integrity Validator.

Validates that:
- Every DDS icon referenced in interface/ww1_germany_goals.gfx exists in gfx/interface/goals/.
- Every DDS file has a valid DirectDraw Surface (DDS) binary header:
    * Magic number: b'DDS ' (0x20534444)
    * Header size: 124 bytes (0x7C)
    * Positive non-zero width and height
    * Decodable by Pillow without corruption
- All 32 expected focus sprites from the specification exist in the .gfx file.
- Both standard SpriteType and animated _shine SpriteType are defined for each goal icon.
- Cross-references focus icons from common/national_focus/germany.txt against registered sprites.
"""

import os
import sys
import re
import struct
import unittest
from typing import Dict, List, Tuple, Any, Optional

from PIL import Image

# Add current dir to path to import spec
sys.path.insert(0, os.path.dirname(__file__))
from spec import EXPECTED_FOCUSES, EXPECTED_FOCUS_COUNT

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parse_gfx_sprites(gfx_path: str) -> List[Dict[str, str]]:
    """
    Parses an HoI4 .gfx file and extracts all SpriteType blocks.
    Returns list of dicts with 'name' and 'texturefile'.
    """
    if not os.path.exists(gfx_path):
        raise FileNotFoundError(f"GFX file not found: {gfx_path}")

    with open(gfx_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Regex to find SpriteType blocks
    # Handles SpriteType = { name = "..." texturefile = "..." ... }
    sprites = []
    sprite_pattern = re.compile(
        r'SpriteType\s*=\s*\{([^}]+(?:animation\s*=\s*\{[^}]*\}[^}]*)*)\}',
        re.MULTILINE | re.IGNORECASE
    )

    name_pattern = re.compile(r'name\s*=\s*"([^"]+)"')
    texture_pattern = re.compile(r'texturefile\s*=\s*"([^"]+)"')

    for match in sprite_pattern.finditer(content):
        block = match.group(1)
        name_match = name_pattern.search(block)
        tex_match = texture_pattern.search(block)

        if name_match and tex_match:
            sprites.append({
                "name": name_match.group(1).strip(),
                "texturefile": tex_match.group(1).strip(),
            })

    return sprites


def validate_dds_header(dds_path: str) -> Dict[str, Any]:
    """
    Validates binary DirectDraw Surface (DDS) header:
    - 4-byte Magic: b'DDS ' (0x20534444)
    - dwSize: 124 (0x7C)
    - dwFlags: uint32
    - dwHeight: uint32 > 0
    - dwWidth: uint32 > 0
    - dwPitchOrLinearSize: uint32
    - dwDepth: uint32
    - dwMipMapCount: uint32
    """
    if not os.path.exists(dds_path):
        raise FileNotFoundError(f"DDS file not found: {dds_path}")

    size_bytes = os.path.getsize(dds_path)
    if size_bytes < 128:
        raise ValueError(f"DDS file is too small ({size_bytes} bytes), header truncated: {dds_path}")

    with open(dds_path, "rb") as f:
        magic = f.read(4)
        if magic != b"DDS ":
            raise ValueError(f"Invalid DDS magic bytes: expected b'DDS ', found {magic!r} in {dds_path}")

        header_bytes = f.read(124)
        if len(header_bytes) < 124:
            raise ValueError(f"Incomplete DDS header in {dds_path}")

        # Unpack header fields:
        # dwSize (4), dwFlags (4), dwHeight (4), dwWidth (4), dwPitchOrLinearSize (4), dwDepth (4), dwMipMapCount (4)
        dw_size, dw_flags, dw_height, dw_width = struct.unpack_from("<IIII", header_bytes, 0)

        if dw_size != 124:
            raise ValueError(f"Invalid DDS header dwSize: expected 124, got {dw_size} in {dds_path}")

        if dw_height == 0 or dw_width == 0:
            raise ValueError(f"Invalid DDS dimensions ({dw_width}x{dw_height}) in {dds_path}")

        # Also verify with Pillow
        try:
            with Image.open(dds_path) as im:
                pil_format = im.format
                pil_size = im.size
                pil_mode = im.mode
        except Exception as e:
            raise ValueError(f"Pillow failed to decode DDS image {dds_path}: {e}")

    return {
        "filepath": dds_path,
        "valid": True,
        "file_size": size_bytes,
        "width": dw_width,
        "height": dw_height,
        "pil_format": pil_format,
        "pil_size": pil_size,
        "pil_mode": pil_mode,
    }


class TestTier2Assets(unittest.TestCase):
    """Automated Unit Tests for Tier 2: Boundary & Asset Integrity."""

    def setUp(self):
        self.gfx_path = os.path.join(MOD_ROOT, "interface", "ww1_germany_goals.gfx")
        self.goals_dir = os.path.join(MOD_ROOT, "gfx", "interface", "goals")

    def test_goals_directory_exists(self):
        """Verify gfx/interface/goals directory exists."""
        self.assertTrue(
            os.path.isdir(self.goals_dir),
            f"Goals texture directory does not exist: {self.goals_dir}"
        )

    def test_all_expected_dds_files_exist_and_valid(self):
        """Verify all 32 expected DDS focus icons exist and have valid binary headers."""
        if not os.path.isdir(self.goals_dir):
            self.skipTest("goals directory not yet created")

        checked_files = set()
        for focus_id, meta in EXPECTED_FOCUSES.items():
            dds_filename = meta["dds"]
            dds_path = os.path.join(self.goals_dir, dds_filename)

            self.assertTrue(
                os.path.isfile(dds_path),
                f"Missing DDS icon file for focus '{focus_id}': {dds_path}"
            )

            if dds_filename not in checked_files:
                header_info = validate_dds_header(dds_path)
                self.assertTrue(header_info["valid"])
                self.assertGreater(header_info["width"], 0)
                self.assertGreater(header_info["height"], 0)
                self.assertGreater(header_info["file_size"], 1024)
                checked_files.add(dds_filename)

        self.assertGreaterEqual(len(checked_files), 25, "Expected at least 25 unique DDS files")

    def test_gfx_sprite_definitions(self):
        """Verify interface/ww1_germany_goals.gfx defines all expected base and shine sprites."""
        if not os.path.isfile(self.gfx_path):
            self.skipTest("ww1_germany_goals.gfx not yet implemented")

        sprites = parse_gfx_sprites(self.gfx_path)
        sprite_dict = {s["name"]: s["texturefile"] for s in sprites}

        # Check total sprites (at least 64: 32 base + 32 shines)
        self.assertGreaterEqual(len(sprites), 64, f"Found only {len(sprites)} sprite definitions, expected >= 64")

        # Check every expected focus icon is registered
        for focus_id, meta in EXPECTED_FOCUSES.items():
            sprite_name = meta["icon"]
            shine_name = f"{sprite_name}_shine"

            self.assertIn(
                sprite_name,
                sprite_dict,
                f"Base sprite '{sprite_name}' for focus '{focus_id}' is not declared in {self.gfx_path}"
            )
            self.assertIn(
                shine_name,
                sprite_dict,
                f"Shine sprite '{shine_name}' for focus '{focus_id}' is not declared in {self.gfx_path}"
            )

            # Check that referenced texture file exists
            tex_relative = sprite_dict[sprite_name].replace("\\", "/")
            tex_full_path = os.path.join(MOD_ROOT, tex_relative)
            self.assertTrue(
                os.path.isfile(tex_full_path),
                f"Sprite '{sprite_name}' references nonexistent texturefile: {tex_relative}"
            )

    def test_focus_tree_icon_references(self):
        """Verify all icons referenced in common/national_focus/germany.txt exist in GFX."""
        focus_path = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        if not os.path.isfile(focus_path):
            self.skipTest("common/national_focus/germany.txt does not exist")

        with open(focus_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # If it's the empty placeholder, skip
        if "focus_tree" not in content:
            self.skipTest("germany.txt is currently placeholder (Milestone 3 pending)")

        icon_pattern = re.compile(r'icon\s*=\s*([a-zA-Z0-9_]+)')
        found_icons = set(icon_pattern.findall(content))

        self.assertGreater(len(found_icons), 0, "No icons found in germany.txt")

        # Load sprites from GFX
        sprites = parse_gfx_sprites(self.gfx_path)
        sprite_names = {s["name"] for s in sprites}

        missing_icons = []
        for icon in found_icons:
            if icon not in sprite_names:
                missing_icons.append(icon)

        self.assertEqual(
            missing_icons,
            [],
            f"The following focus icons in germany.txt are missing from {self.gfx_path}: {missing_icons}"
        )


def run_tier2(verbose: bool = True) -> bool:
    """Entry point for standalone Tier 2 test execution."""
    print("=" * 70)
    print("TIER 2: Boundary & Asset Integrity Audit")
    print("=" * 70)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTier2Assets)
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tier2()
    sys.exit(0 if success else 1)
