#!/usr/bin/env python3
"""
HOI4 Image & Texture Converter (PNG <-> DDS)
Converts images between PNG and DDS with automatic dimensions and alpha channels for HOI4.
Dimensions:
  - focus: 82x82
  - idea: 64x64
  - leader: 156x210
  - event: 450x250
"""

import sys
import argparse
from pathlib import Path
from PIL import Image

PRESETS = {
    "focus": (82, 82),
    "idea": (64, 64),
    "leader": (156, 210),
    "event": (450, 250),
    "news": (400, 140)
}

def convert_image(input_path, output_path, preset=None):
    src = Path(input_path)
    if not src.exists():
        print(f"Error: File '{src}' not found.")
        sys.exit(1)

    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    img = Image.open(src)
    
    # Ensure RGBA for transparency
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Resize if preset specified
    if preset and preset in PRESETS:
        target_size = PRESETS[preset]
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        print(f"Resized image to preset '{preset}': {target_size}")

    # Determine format
    ext = dest.suffix.lower()
    fmt = "DDS" if ext == ".dds" else ("PNG" if ext == ".png" else "PNG")

    img.save(dest, format=fmt)
    print(f"Successfully converted: {src.name} -> {dest.name} ({dest.stat().st_size} bytes)")

def main():
    parser = argparse.ArgumentParser(description="HOI4 Texture Converter")
    parser.add_argument("--in", dest="input_file", required=True, help="Input image file")
    parser.add_argument("--out", dest="output_file", required=True, help="Output image file")
    parser.add_argument("--preset", choices=["focus", "idea", "leader", "event", "news"], help="Auto-resize preset")
    args = parser.parse_args()

    convert_image(args.input_file, args.output_file, args.preset)

if __name__ == "__main__":
    main()
