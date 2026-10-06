"""Import reviewed UK artwork (focus icons, event pictures) and derive idea/decision icons.

    python scripts/build_britain_art.py docs/britain_art_picks.json [--dry-run]

The picks file is produced by a human/agent visual review (see scripts/art_candidates.py):
    {"focus": {focus_id: {"donor": "...", "source_relative": "gfx/..."}},
     "event": {name: {...}},
     "derived_ideas": {idea_name: focus_id},        # 64x64 icon made from that focus image
     "derived_decisions": {decision_name: focus_id}}
Rules: a focus icon may not repeat (file hash, pixel hash or near-identical look) another
focus icon in the whole mod or in this batch. Nothing is recoloured. Sprites go to
interface/ww1_britain_art.gfx (owned by this script) with provenance in docs/britain_art_manifest.json.
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
import visual_asset_pipeline as vap  # noqa: E402

ROOT = vap.ROOT
WORKSHOP = Path("E:/SteamLibrary/steamapps/workshop/content/394360")
GAME = Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV")
GOALS_DIR = "gfx/interface/goals/ww1_britain"
IDEAS_DIR = "gfx/interface/ideas/ww1_britain"
DECISIONS_DIR = "gfx/interface/decisions/ww1_britain"
EVENTS_DIR = "gfx/event_pictures/ww1_britain"
SHINE = [
    "\t\teffectFile = \"gfx/FX/buttonstate.lua\"", "\t\tanimation = {",
    "\t\t\tanimationmaskfile = \"{tex}\"", "\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"",
    "\t\t\tanimationrotation = -90.0", "\t\t\tanimationlooping = no", "\t\t\tanimationtime = 0.75",
    "\t\t\tanimationdelay = 0", "\t\t\tanimationblendmode = \"add\"", "\t\t\tanimationtype = \"scrolling\"",
    "\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }", "\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }",
    "\t\t}", "\t\tlegacy_lazy_load = no"]


def prefixed(fid):
    return "ENG_ww1_" + fid


def fit(image, size, pad=False, color=(0, 0, 0, 0)):
    if pad:
        return ImageOps.pad(image, size, method=Image.Resampling.LANCZOS, color=color)
    image = ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size)
    canvas.alpha_composite(image, ((size[0] - image.width) // 2, (size[1] - image.height) // 2))
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("picks", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    picks = json.loads(a.picks.read_text(encoding="utf-8"))
    mine = {prefixed(f) for f in picks["focus"]}
    # every other focus image already active in the mod (except the ones this batch owns)
    existing = {path: ids for path, ids in vap.active_focus_images(GAME).items()
                if not set(ids) <= mine}
    used_hash = {vap.pixels(p): ids for p, ids in existing.items()}
    used_vis = [(vap.visual_signature(p), ids) for p, ids in existing.items()]
    batch_src, batch_pix, batch_vis, errors = set(), set(), [], []
    sprites, manifest = ["spriteTypes = {"], []

    for fid, src in picks["focus"].items():
        path = WORKSHOP / src["donor"] / src["source_relative"]
        if not path.is_file():
            errors.append(f"{fid}: missing source {path}")
            continue
        sh, ph, vs = vap.digest(path), vap.pixels(path), vap.visual_signature(path)
        if sh in batch_src or ph in batch_pix or any(vap.resembles(vs, v) for v in batch_vis):
            errors.append(f"{fid}: repeats another pick in this batch ({path.name})")
            continue
        if ph in used_hash:
            errors.append(f"{fid}: pixel-identical to existing focus icon of {used_hash[ph]}")
            continue
        near = [i for sig, ids in used_vis if vap.resembles(vs, sig) for i in ids]
        if near:
            errors.append(f"{fid}: looks like existing focus icon of {near}")
            continue
        batch_src.add(sh)
        batch_pix.add(ph)
        batch_vis.append(vs)
        name = prefixed(fid)
        dest = ROOT / GOALS_DIR / f"{name}.png"
        if not a.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with Image.open(path) as im:
                fit(im.convert("RGBA"), (82, 82)).save(dest)
        tex = f"{GOALS_DIR}/{name}.png"
        sprites += ["\tspriteType = {", f'\t\tname = "GFX_goal_ww1_{name}"', f'\t\ttexturefile = "{tex}"', "\t}",
                    "\tspriteType = {", f'\t\tname = "GFX_goal_ww1_{name}_shine"', f'\t\ttexturefile = "{tex}"']
        sprites += [s.replace("{tex}", tex) for s in SHINE] + ["\t}"]
        manifest.append(dict(kind="focus", id=name, sprite=f"GFX_goal_ww1_{name}", texture=tex, donor_id=src["donor"],
                             source_relative=src["source_relative"], source_sha256=sh, source_pixels_sha256=ph))

    for ename, src in picks["event"].items():
        path = WORKSHOP / src["donor"] / src["source_relative"]
        if not path.is_file():
            errors.append(f"event {ename}: missing source {path}")
            continue
        sh, ph = vap.digest(path), vap.pixels(path)
        if sh in batch_src or ph in batch_pix:
            errors.append(f"event {ename}: repeats another image in this batch ({path.name})")
            continue
        batch_src.add(sh)
        batch_pix.add(ph)
        dest = ROOT / EVENTS_DIR / f"{ename}.png"
        if not a.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with Image.open(path) as im:
                fit(im.convert("RGBA"), (450, 250), pad=True, color=(26, 27, 27, 255)).save(dest)
        tex = f"{EVENTS_DIR}/{ename}.png"
        sprites += ["\tspriteType = {", f'\t\tname = "GFX_event_ww1_britain_{ename}"', f'\t\ttexturefile = "{tex}"', "\t}"]
        manifest.append(dict(kind="event", id=ename, sprite=f"GFX_event_ww1_britain_{ename}", texture=tex,
                             donor_id=src["donor"], source_relative=src["source_relative"], source_sha256=sh))

    def derived(kind, mapping, folder, sprite_prefix):
        for name, fid in mapping.items():
            src = ROOT / GOALS_DIR / f"{prefixed(fid)}.png"
            if not src.is_file() and not a.dry_run:
                errors.append(f"{kind} {name}: focus image {fid} not available")
                continue
            dest = ROOT / folder / f"{name}.png"
            if not a.dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                with Image.open(src) as im:
                    fit(im.convert("RGBA"), (64, 64)).save(dest)
            tex = f"{folder}/{name}.png"
            sprites.extend(["\tspriteType = {", f'\t\tname = "{sprite_prefix}{name}"', f'\t\ttexturefile = "{tex}"', "\t}"])
            manifest.append(dict(kind=kind, id=name, sprite=sprite_prefix + name, texture=tex, derived_from=prefixed(fid)))

    derived("idea", picks.get("derived_ideas", {}), IDEAS_DIR, "GFX_idea_")
    derived("decision", picks.get("derived_decisions", {}), DECISIONS_DIR, "GFX_decision_")
    sprites.append("}")
    print(f"focus {len(picks['focus'])}  events {len(picks['event'])}  ideas {len(picks.get('derived_ideas', {}))} "
          f"decisions {len(picks.get('derived_decisions', {}))}")
    for e in errors:
        print("ERROR:", e)
    if errors:
        sys.exit(1)
    if a.dry_run:
        print("dry run OK: no file written")
        return
    (ROOT / "interface/ww1_britain_art.gfx").write_text("\n".join(sprites) + "\n", encoding="utf-8")
    (ROOT / "docs/britain_art_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("written interface/ww1_britain_art.gfx and docs/britain_art_manifest.json")


if __name__ == "__main__":
    main()
