"""Import explicitly reviewed WW1 artwork, preserve provenance and refuse duplicates.

Requests name exact source paths; there is deliberately no generic/fuzzy fallback.
Works without modifying donor mods or any Steam installation. Pillow is required.
"""
from pathlib import Path
from collections import defaultdict
import argparse
import hashlib
import json
import re
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pixels(path):
    try:
        with Image.open(path) as im:
            im = im.convert("RGBA")
            return hashlib.sha256(str(im.size).encode() + im.tobytes()).hexdigest()
    except NotImplementedError:
        # Some inherited native DDS use DXGI variants unsupported by Pillow.
        # Their exact-byte identity is still tracked; reviewed new imports must decode.
        return "dds-bytes:" + digest(path)

def visual_signature(path):
    """128-bit difference hash, robust to DDS re-encoding and size conversions."""
    try:
        with Image.open(path) as image:
            image = image.convert("RGBA")
            background = Image.new("RGBA", image.size, (31, 31, 31, 255))
            background.alpha_composite(image)
            gray = list(background.convert("L").resize((17, 8), Image.Resampling.LANCZOS).getdata())
            value = 0
            for row in range(8):
                for col in range(16):
                    value = (value << 1) | int(gray[row * 17 + col] > gray[row * 17 + col + 1])
            return f"{value:032x}"
    except NotImplementedError:
        return None

def resembles(left, right):
    return left is not None and right is not None and (int(left, 16) ^ int(right, 16)).bit_count() <= 4

def sprites(base):
    out = {}
    for path in sorted((base / "interface").glob("*.gfx")):
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for m in re.finditer(r'(?is)\b(?:spriteType|frameAnimatedSpriteType)\s*=\s*\{\s*name\s*=\s*"([^"]+)".*?texturefile\s*=\s*"([^"]+)"', text):
            out[m[1]] = base / m[2]
    return out

def active_focus_images(game):
    registry = sprites(game) | sprites(ROOT)
    out = defaultdict(list)
    for path in sorted((ROOT / "common/national_focus").glob("*.txt")):
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for start in re.finditer(r'(?m)^\s*focus\s*=\s*\{', text):
            header = text[start.end():].split("completion_reward", 1)[0]
            fid = re.search(r'\bid\s*=\s*([^\s{}]+)', header)
            icon = re.search(r'\bicon\s*=\s*([^\s{}]+)', header)
            if fid and icon:
                source = registry.get(icon[1].strip('"'))
                if source and source.is_file():
                    out[source].append(fid[1])
    return out

def import_requests(request_file, workshop, game):
    requests = json.loads(request_file.read_text(encoding="utf-8"))
    existing = active_focus_images(game)
    active_hashes = {pixels(path): ids for path, ids in existing.items()}
    active_visuals = [(visual_signature(path), ids) for path, ids in existing.items()]
    request_sources = set()
    request_pixels = set()
    request_visuals = []
    records = []
    definitions = ["spriteTypes = {"]
    for request in requests:
        kind = request["kind"]
        donor_id = request["donor_id"]
        source = ROOT / request["source_project"] if "source_project" in request else workshop / donor_id / request["source_relative"]
        if not source.is_file():
            raise FileNotFoundError(source)
        source_hash, pixel_hash = digest(source), pixels(source)
        visual = visual_signature(source)
        if source_hash in request_sources or pixel_hash in request_pixels:
            raise ValueError(f"Repeated artwork in requests: {request['id']} / {source}")
        request_sources.add(source_hash)
        request_pixels.add(pixel_hash)
        if any(resembles(visual, previous) for previous in request_visuals):
            raise ValueError(f"Near-duplicate artwork (including DDS recompression): {request['id']}")
        request_visuals.append(visual)
        if request["kind"] == "focus" and pixel_hash in active_hashes:
            # Once a mapping was applied, rebuilding its own reviewed artwork is allowed.
            others = [x for x in active_hashes[pixel_hash] if x != request["id"]]
            if others:
                raise ValueError(f"Focus texture already used by {others}: {request['id']}")
        if kind == "focus":
            near = [fid for signature, ids in active_visuals if resembles(visual, signature) for fid in ids if fid != request["id"]]
            if near:
                raise ValueError(f"Focus visual already used by {near}: {request['id']}")
        kind = request["kind"]
        folder = {"focus": "gfx/interface/goals/ww1_alpha", "idea": "gfx/interface/ideas/ww1_alpha",
                  "decision": "gfx/interface/decisions/ww1_alpha", "category": "gfx/interface/decisions/ww1_alpha",
                  "event": "gfx/event_pictures/ww1_alpha"}[kind]
        destination = ROOT / folder / (request["id"] + ".png")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as im:
            im = im.convert("RGBA")
            if kind in ["idea", "decision", "category"]:
                im.thumbnail((64, 64), Image.Resampling.LANCZOS)
                canvas = Image.new("RGBA", (64, 64))
                canvas.alpha_composite(im, ((64 - im.width) // 2, (64 - im.height) // 2))
                im = canvas
            elif kind == "event":
                # Preserve all content; avoid cropping archival frames/faces.
                im = ImageOps.pad(im, (450, 250), method=Image.Resampling.LANCZOS, color=(26, 27, 27, 255))
            elif kind == "focus":
                # One readable game size; conversion does not recolor or replace the subject.
                im = ImageOps.contain(im, (82, 82), method=Image.Resampling.LANCZOS)
                canvas = Image.new("RGBA", (82, 82))
                canvas.alpha_composite(im, ((82 - im.width) // 2, (82 - im.height) // 2))
                im = canvas
            im.save(destination)
            size = list(im.size)
        texture = destination.relative_to(ROOT).as_posix()
        sprite = request["sprite"]
        definitions.extend(["\tspriteType = {", f'\t\tname = "{sprite}"', f'\t\ttexturefile = "{texture}"', "\t}"])
        if kind == "focus":
            definitions.extend([
                "\tspriteType = {", f'\t\tname = "{sprite}_shine"', f'\t\ttexturefile = "{texture}"',
                '\t\teffectFile = "gfx/FX/buttonstate.lua"', "\t\tanimation = {",
                f'\t\t\tanimationmaskfile = "{texture}"',
                '\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"',
                "\t\t\tanimationrotation = -90.0", "\t\t\tanimationlooping = no",
                "\t\t\tanimationtime = 0.75", "\t\t\tanimationdelay = 0",
                '\t\t\tanimationblendmode = "add"', '\t\t\tanimationtype = "scrolling"',
                "\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }",
                "\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }", "\t\t}", "\t\tlegacy_lazy_load = no", "\t}",
            ])
        records.append(request | {"texture": texture, "source_sha256": source_hash,
                                  "source_pixels_sha256": pixel_hash, "texture_sha256": digest(destination),
                                  "texture_pixels_sha256": pixels(destination), "size": size,
                                  "visual_signature": visual_signature(destination), "source_visual_signature": visual,
                                  "source_workshop_url": "https://steamcommunity.com/sharedfiles/filedetails/?id=" + donor_id if donor_id.isdecimal() else None})
    definitions.extend(["\tspriteType = {", '\t\tname = "GFX_event_ww1_great_war_dispatch"',
                        '\t\ttexturefile = "gfx/event_pictures/ww1_alpha/great_war_dispatch.png"', "\t}"])
    definitions.append("}")
    (ROOT / "interface/ww1_alpha_content_assets.gfx").write_text("\n".join(definitions) + "\n", encoding="utf-8")
    (ROOT / "docs/visual_asset_manifest.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(records)} distinct reviewed source images; focus shine sprites registered.")

def catalog(workshop, game):
    occupied = {pixels(path) for path in active_focus_images(game)}
    entries = []
    for donor_id in ["3365515312", "2716194283"]:
        donor = workshop / donor_id
        for path in sorted((donor / "gfx/interface/goals").rglob("*")):
            if path.suffix.lower() not in [".dds", ".png", ".tga"]:
                continue
            # Descriptor and paths are metadata, not evidence of historical suitability.
            entries.append({"donor_id": donor_id, "source_relative": path.relative_to(donor).as_posix(),
                            "source_sha256": digest(path), "name": path.stem,
                            "requires_visual_review": True})
    (ROOT / "docs/visual_donor_catalog.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Catalogued {len(entries)} candidates. Exact imports still require requests and review.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workshop", type=Path, default=Path("E:/SteamLibrary/steamapps/workshop/content/394360"))
    parser.add_argument("--game", type=Path, default=Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV"))
    parser.add_argument("--requests", type=Path)
    parser.add_argument("--catalog", action="store_true")
    args = parser.parse_args()
    if args.catalog:
        catalog(args.workshop, args.game)
    if args.requests:
        import_requests(args.requests, args.workshop, args.game)
    if not args.catalog and not args.requests:
        parser.error("Specify --requests or --catalog")
