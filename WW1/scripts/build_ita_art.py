"""Art pipeline for Italy (ITA) WW1.

Imports period artwork from installed Workshop donor mods (TGWR, Kaiserreich, Kaiserredux),
converts textures to standard sizes (82x82 goals, 450x250 events, 64x64 ideas/decisions),
enforces zero duplicates against the existing mod assets and within this batch,
generates .gfx definitions with _shine overlays, and records provenance in docs/ita_art_bindings.json.

Run from WW1/: python -B -X utf8 scripts/build_ita_art.py
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import visual_asset_pipeline as vap
from check_italy_outline import load

WORKSHOP = Path("E:/SteamLibrary/steamapps/workshop/content/394360")
GAME = Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV")

GOALS_DIR = ROOT / "gfx" / "interface" / "goals" / "ww1_italy"
EVENTS_DIR = ROOT / "gfx" / "event_pictures" / "ww1_italy"
IDEAS_DIR = ROOT / "gfx" / "interface" / "ideas" / "ww1_italy"
DECISIONS_DIR = ROOT / "gfx" / "interface" / "decisions" / "ww1_italy"
BINDINGS_FILE = ROOT / "docs" / "ita_art_bindings.json"

SHINE_TEMPLATE = [
    "\t\teffectFile = \"gfx/FX/buttonstate.lua\"",
    "\t\tanimation = {",
    "\t\t\tanimationmaskfile = \"{tex}\"",
    "\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"",
    "\t\t\tanimationrotation = -90.0",
    "\t\t\tanimationlooping = no",
    "\t\t\tanimationtime = 0.75",
    "\t\t\tanimationdelay = 0",
    "\t\t\tanimationblendmode = \"add\"",
    "\t\t\tanimationtype = \"scrolling\"",
    "\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }",
    "\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }",
    "\t\t}",
    "\t\tlegacy_lazy_load = no"
]


def resize_and_pad(im, size):
    im = im.convert("RGBA")
    c = ImageOps.contain(im, size, Image.Resampling.LANCZOS)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.alpha_composite(c, ((size[0] - c.width) // 2, (size[1] - c.height) // 2))
    return out


def fit_exact(im, size):
    im = im.convert("RGBA")
    return ImageOps.fit(im, size, Image.Resampling.LANCZOS)


def get_active_hashes():
    active = vap.active_focus_images(GAME)
    hashes = set()
    for p in active:
        if p.is_file():
            hashes.add(vap.pixels(p))
    return hashes


def find_donor_files():
    # Indexed by mod and relative path
    donor_goals = []
    donor_events = []
    donor_ideas = []

    priority_mods = ["3365515312", "2076426030", "2782465344", "2716194283"]
    for mod in priority_mods:
        mpath = WORKSHOP / mod
        if not mpath.exists():
            continue
        gdir = mpath / "gfx" / "interface" / "goals"
        if gdir.exists():
            for f in sorted(gdir.rglob("*.*")):
                if f.suffix.lower() in (".dds", ".png"):
                    rel = f.relative_to(mpath).as_posix()
                    donor_goals.append((mod, rel, f))
        edir = mpath / "gfx" / "event_pictures"
        if edir.exists():
            for f in sorted(edir.rglob("*.*")):
                if f.suffix.lower() in (".dds", ".png"):
                    rel = f.relative_to(mpath).as_posix()
                    donor_events.append((mod, rel, f))
        idir = mpath / "gfx" / "interface" / "ideas"
        if idir.exists():
            for f in sorted(idir.rglob("*.*")):
                if f.suffix.lower() in (".dds", ".png"):
                    rel = f.relative_to(mpath).as_posix()
                    donor_ideas.append((mod, rel, f))
    return donor_goals, donor_events, donor_ideas


def build_art():
    print("Collecting donor artwork...")
    donor_goals, donor_events, donor_ideas = find_donor_files()
    print(f"Indexed {len(donor_goals)} donor goals, {len(donor_events)} donor events, {len(donor_ideas)} donor ideas.")

    active_hashes = get_active_hashes()
    print(f"Mod active focus hashes to avoid: {len(active_hashes)}")

    GOALS_DIR.mkdir(parents=True, exist_ok=True)
    EVENTS_DIR.mkdir(parents=True, exist_ok=True)
    IDEAS_DIR.mkdir(parents=True, exist_ok=True)
    DECISIONS_DIR.mkdir(parents=True, exist_ok=True)

    rows = load()
    foci_ids = ["ITA_ww1_" + r["id"] for r in rows]

    bindings = []
    used_pixel_hashes = set(active_hashes)
    used_visual_sigs = []

    # 1. Map 200 Focus Icons
    print("Assigning 200 unique focus icons...")
    goal_gfx = ["spriteTypes = {"]

    # Keyword scoring function for focus IDs
    def score_goal(name, fid):
        clean_fid = fid.replace("ITA_ww1_", "")
        s = 0
        fn = name.lower()
        if "ita" in fn or "ital" in fn or "rome" in fn or "savoy" in fn:
            s += 5
        parts = clean_fid.split("_")
        for p in parts:
            if len(p) >= 3 and p in fn:
                s += 10
        return s

    picked_goals = {}
    available_goals = list(donor_goals)

    for fid in foci_ids:
        # Sort available goals by score
        clean_fid = fid.replace("ITA_ww1_", "")
        candidates = sorted(available_goals, key=lambda x: score_goal(x[2].name, fid), reverse=True)
        chosen = None
        for mod, rel, path in candidates:
            try:
                pix = vap.pixels(path)
                if pix in used_pixel_hashes:
                    continue
                vs = vap.visual_signature(path)
                if any(vap.resembles(vs, prev) for prev in used_visual_sigs):
                    continue
                # Try opening and converting
                with Image.open(path) as im:
                    im_out = resize_and_pad(im, (82, 82))
                chosen = (mod, rel, path, pix, vs, im_out)
                break
            except Exception:
                continue

        if not chosen:
            raise RuntimeError(f"Could not find valid unique donor goal for {fid}")

        mod, rel, path, pix, vs, im_out = chosen
        available_goals.remove((mod, rel, path))
        used_pixel_hashes.add(pix)
        if vs:
            used_visual_sigs.append(vs)

        dest_file = GOALS_DIR / f"{fid}.dds"
        im_out.save(dest_file)

        rel_dest = f"gfx/interface/goals/ww1_italy/{fid}.dds"
        sprite_name = f"GFX_goal_ww1_{fid}"
        shine_name = f"GFX_goal_ww1_{fid}_shine"

        goal_gfx.append(f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"{rel_dest}\"\n\t}}")
        goal_gfx.append(f"\tspriteType = {{\n\t\tname = \"{shine_name}\"\n\t\ttexturefile = \"{rel_dest}\"")
        goal_gfx.extend([s.replace("{tex}", rel_dest) for s in SHINE_TEMPLATE])
        goal_gfx.append("\t}")

        bindings.append({
            "kind": "focus",
            "id": fid,
            "sprite": sprite_name,
            "texture": rel_dest,
            "donor_id": mod,
            "source_relative": rel,
            "pixel_hash": pix
        })

    goal_gfx.append("}\n")
    (ROOT / "interface" / "ww1_italy_goals.gfx").write_text("\n".join(goal_gfx), encoding="utf-8")
    print(f"Generated interface/ww1_italy_goals.gfx with {len(foci_ids)} icons and shines.")

    # 2. Map 80 Event Pictures
    print("Assigning 80 unique event pictures (450x250)...")
    event_gfx = ["spriteTypes = {"]
    picked_events = {}
    available_events = list(donor_events)

    for i in range(1, 81):
        eid = f"ww1_italy_{i}"
        chosen = None
        for mod, rel, path in available_events:
            try:
                pix = vap.pixels(path)
                if pix in used_pixel_hashes:
                    continue
                vs = vap.visual_signature(path)
                if any(vap.resembles(vs, prev) for prev in used_visual_sigs):
                    continue
                with Image.open(path) as im:
                    im_out = fit_exact(im, (450, 250))
                chosen = (mod, rel, path, pix, vs, im_out)
                break
            except Exception:
                continue

        if not chosen:
            raise RuntimeError(f"Could not find valid unique donor event for {eid}")

        mod, rel, path, pix, vs, im_out = chosen
        available_events.remove((mod, rel, path))
        used_pixel_hashes.add(pix)
        if vs:
            used_visual_sigs.append(vs)

        dest_file = EVENTS_DIR / f"{eid}.dds"
        im_out.save(dest_file)

        rel_dest = f"gfx/event_pictures/ww1_italy/{eid}.dds"
        sprite_name = f"GFX_event_{eid}"

        event_gfx.append(f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"{rel_dest}\"\n\t}}")

        bindings.append({
            "kind": "event",
            "id": eid,
            "sprite": sprite_name,
            "texture": rel_dest,
            "donor_id": mod,
            "source_relative": rel,
            "pixel_hash": pix
        })

    event_gfx.append("}\n")
    (ROOT / "interface" / "ww1_italy_events.gfx").write_text("\n".join(event_gfx), encoding="utf-8")
    print(f"Generated interface/ww1_italy_events.gfx with 80 event pictures.")

    # 3. Map 32 Ideas Icons
    print("Assigning 32 unique idea icons (64x64)...")
    idea_gfx = ["spriteTypes = {"]
    available_ideas = list(donor_ideas)

    for i in range(1, 33):
        iid = f"ITA_ww1_idea_{i}"
        chosen = None
        for mod, rel, path in available_ideas:
            try:
                pix = vap.pixels(path)
                if pix in used_pixel_hashes:
                    continue
                with Image.open(path) as im:
                    im_out = resize_and_pad(im, (64, 64))
                chosen = (mod, rel, path, pix, im_out)
                break
            except Exception:
                continue

        if not chosen:
            raise RuntimeError(f"Could not find valid unique donor idea for {iid}")

        mod, rel, path, pix, im_out = chosen
        available_ideas.remove((mod, rel, path))
        used_pixel_hashes.add(pix)

        dest_file = IDEAS_DIR / f"{iid}.dds"
        im_out.save(dest_file)

        rel_dest = f"gfx/interface/ideas/ww1_italy/{iid}.dds"
        sprite_name = f"GFX_idea_{iid}"

        idea_gfx.append(f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"{rel_dest}\"\n\t}}")

        bindings.append({
            "kind": "idea",
            "id": iid,
            "sprite": sprite_name,
            "texture": rel_dest,
            "donor_id": mod,
            "source_relative": rel,
            "pixel_hash": pix
        })

    idea_gfx.append("}\n")
    (ROOT / "interface" / "ww1_italy_ideas.gfx").write_text("\n".join(idea_gfx), encoding="utf-8")
    print(f"Generated interface/ww1_italy_ideas.gfx with 32 idea icons.")

    # 4. Map 32 Decision Icons
    print("Assigning 32 unique decision icons (64x64)...")
    dec_gfx = ["spriteTypes = {"]

    for i in range(1, 33):
        did = f"ITA_ww1_decision_{i}"
        chosen = None
        for mod, rel, path in available_ideas:
            try:
                pix = vap.pixels(path)
                if pix in used_pixel_hashes:
                    continue
                with Image.open(path) as im:
                    im_out = resize_and_pad(im, (64, 64))
                chosen = (mod, rel, path, pix, im_out)
                break
            except Exception:
                continue

        if not chosen:
            raise RuntimeError(f"Could not find valid unique donor decision for {did}")

        mod, rel, path, pix, im_out = chosen
        available_ideas.remove((mod, rel, path))
        used_pixel_hashes.add(pix)

        dest_file = DECISIONS_DIR / f"{did}.dds"
        im_out.save(dest_file)

        rel_dest = f"gfx/interface/decisions/ww1_italy/{did}.dds"
        sprite_name = f"GFX_decision_{did}"

        dec_gfx.append(f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"{rel_dest}\"\n\t}}")

        bindings.append({
            "kind": "decision",
            "id": did,
            "sprite": sprite_name,
            "texture": rel_dest,
            "donor_id": mod,
            "source_relative": rel,
            "pixel_hash": pix
        })

    # Also map category icons
    for cat in ["politics", "economy", "diplomacy", "military", "mezzogiorno"]:
        c_icon_name = f"GFX_decision_category_ita_{cat}"
        rel_c = f"gfx/interface/decisions/decision_category_generic.dds"
        dec_gfx.append(f"\tspriteType = {{\n\t\tname = \"{c_icon_name}\"\n\t\ttexturefile = \"{rel_c}\"\n\t}}")

    dec_gfx.append("}\n")
    (ROOT / "interface" / "ww1_italy_decisions.gfx").write_text("\n".join(dec_gfx), encoding="utf-8")
    print(f"Generated interface/ww1_italy_decisions.gfx with 32 decision icons.")

    # Save Provenance JSON
    BINDINGS_FILE.write_text(json.dumps(bindings, indent=2), encoding="utf-8")
    print(f"Recorded provenance bindings to {BINDINGS_FILE.relative_to(ROOT)} ({len(bindings)} assets).")


if __name__ == "__main__":
    build_art()
