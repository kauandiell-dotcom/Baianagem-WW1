"""Build the deterministic UI frame and convert the exclusive generated artwork.

Image conversion only; the illustration is generated with the built-in image tool.
No Steam game/workshop directory is ever modified.
"""
from pathlib import Path
import argparse
import hashlib
import json
from PIL import Image, ImageDraw, ImageOps, ImageFont

ROOT = Path(__file__).resolve().parents[1]

def build(source: Path, preview: Path | None = None) -> None:
    target = ROOT / "gfx/interface/super_events"
    target.mkdir(parents=True, exist_ok=True)
    # Keep a lossless master within the project, never a machine-specific reference.
    source_image = Image.open(source).convert("RGB")
    source_image.save(target / "ww1_great_war_outbreak_master.png")
    art = ImageOps.fit(source_image, (680, 370), method=Image.Resampling.LANCZOS)
    art.convert("RGBA").save(target / "ww1_great_war_outbreak_v2.dds")

    frame = Image.new("RGBA", (720, 600), (17, 22, 27, 250))
    draw = ImageDraw.Draw(frame)
    draw.rounded_rectangle((1, 1, 718, 598), radius=5, outline=(170, 143, 93), width=2)
    draw.rectangle((8, 8, 711, 591), outline=(84, 79, 63), width=1)
    draw.rectangle((18, 94, 701, 467), outline=(195, 166, 110), width=2)
    draw.line((50, 88, 670, 88), fill=(104, 91, 63), width=1)
    draw.line((50, 537, 670, 537), fill=(104, 91, 63), width=1)
    for x in [20, 700]:
        for y in [18, 582]:
            draw.polygon([(x, y - 4), (x + 4, y), (x, y + 4), (x - 4, y)], fill=(193, 162, 103))
    for x in [96, 624]:
        draw.line((x - 40, 32, x + 40, 32), fill=(117, 103, 72), width=1)
    frame.save(target / "super_event_frame_v2.dds")

    button = Image.new("RGBA", (960, 40), (0, 0, 0, 0))
    bd = ImageDraw.Draw(button)
    for i, fill in enumerate([(37, 47, 53), (57, 66, 66), (25, 32, 37)]):
        x = i * 320
        bd.rounded_rectangle((x + 1, 1, x + 318, 38), radius=3, fill=fill, outline=(162, 136, 91), width=1)
        bd.line((x + 14, 5, x + 305, 5), fill=(94, 88, 71), width=1)
    button.save(target / "super_event_btn_v2.dds")

    # Country news picture uses the same owned artwork; it is not another focus icon.
    event_dir = ROOT / "gfx/event_pictures/ww1_alpha"
    event_dir.mkdir(parents=True, exist_ok=True)
    ImageOps.fit(source_image, (450, 250), method=Image.Resampling.LANCZOS).save(event_dir / "great_war_dispatch.png")

    if preview:
        preview.parent.mkdir(parents=True, exist_ok=True)
        mock = frame.copy()
        mock.alpha_composite(art.convert("RGBA"), (20, 96))
        mock.alpha_composite(button.crop((0, 0, 320, 40)), (200, 547))
        md = ImageDraw.Draw(mock)
        fp = Path("C:/Windows/Fonts")
        small = ImageFont.truetype(str(fp / "georgia.ttf"), 15)
        header = ImageFont.truetype(str(fp / "georgiab.ttf"), 27)
        for y, text, font, color in [(23, "DESPACHO EXTRAORDINÁRIO", small, (184, 164, 126)),
                                     (49, "A GRANDE GUERRA", header, (223, 207, 169)),
                                     (487, "As ordens de mobilização atravessam o continente.", small, (210, 207, 193)),
                                     (510, "A paz agora depende daqueles que marcham.", small, (183, 179, 163)),
                                     (557, "O futuro está em nossas mãos.", small, (218, 208, 181))]:
            width = md.textlength(text, font=font)
            md.text(((720 - width) / 2, y), text, fill=color, font=font)
        mock.convert("RGB").save(preview)

    manifest = {
        "illustration": {
            "source": "Built-in image generation; historical illustration, not an archival photograph",
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "master": "gfx/interface/super_events/ww1_great_war_outbreak_master.png",
            "prompt": "Sober 1914 mobilization panorama: French blue coats/red trousers at a steam railway platform, German grey uniforms/Pickelhaube on a distant road, family farewell, muted navy/charcoal/gold, no WWII equipment, no titles or watermark.",
        },
        "frame_and_button": "Original deterministic Baianagem interface geometry; built by this script",
        "preview": "Layout mock only; actual game uses native hoi_24header and hoi_16mbs fonts.",
    }
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/super_event_art_provenance.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Built super-event v2: 720x600 frame, 680x370 art, 3-state 320x40 button.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--preview", type=Path)
    args = parser.parse_args()
    build(args.source, args.preview)
