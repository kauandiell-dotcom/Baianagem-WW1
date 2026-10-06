"""Candidate finder for Workshop artwork (review aid only; it copies nothing into the mod).

    python scripts/art_candidates.py SUBJECTS.json OUT_DIR [--kind goals|event_pictures]

SUBJECTS.json: {"subject_id": "regex of name keywords", ...}
Builds index-numbered contact sheets (OUT_DIR/sheet_N.png) and OUT_DIR/candidates.json so a
reviewer can pick by (subject, number). Selection is a human/agent visual decision; names only
narrow the search.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

WORKSHOP = Path("E:/SteamLibrary/steamapps/workshop/content/394360")
PRIORITY = {"3365515312": 0, "3557031692": 1, "2076426030": 2, "2716194283": 3, "2782465344": 4, "3612841387": 5,
            "2525366756": 6, "2903857354": 6}
INDEX = Path(os.environ.get("KIROCREW_SCRATCH", ".")) / "donor_index.tsv"


def load(kind):
    rows = []
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        donor, rel, size = line.split("\t")
        if f"/{kind}/" in "/" + rel and donor in PRIORITY and rel.lower().endswith((".png", ".dds", ".tga")):
            rows.append((donor, rel))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("subjects")
    ap.add_argument("out")
    ap.add_argument("--kind", default="goals")
    ap.add_argument("--per", type=int, default=10)
    ap.add_argument("--rows", type=int, default=6)
    a = ap.parse_args()
    subjects = json.loads(Path(a.subjects).read_text(encoding="utf-8-sig"))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = load(a.kind)
    cell_w, cell_h = (104, 104) if a.kind == "goals" else (152, 108)
    result = {}
    sheets, cur = [], []
    for sid, rx in subjects.items():
        pat = re.compile(rx, re.I)
        hits = [(PRIORITY[d], rel, d) for d, rel in rows if pat.search(Path(rel).stem)]
        hits.sort(key=lambda h: (h[0], h[1]))
        seen, picks = set(), []
        for _, rel, d in hits:
            stem = Path(rel).stem.lower()
            if stem in seen:
                continue
            seen.add(stem)
            picks.append((d, rel))
            if len(picks) >= a.per:
                break
        result[sid] = picks
        cur.append((sid, picks))
        if len(cur) == a.rows:
            sheets.append(cur)
            cur = []
    if cur:
        sheets.append(cur)
    for n, group in enumerate(sheets, 1):
        W = 130 + a.per * cell_w
        H = len(group) * (cell_h + 22)
        sheet = Image.new("RGBA", (W, H), (28, 28, 28, 255))
        draw = ImageDraw.Draw(sheet)
        for r, (sid, picks) in enumerate(group):
            y = r * (cell_h + 22)
            draw.text((4, y + 4), sid[:22], fill=(255, 220, 120, 255))
            draw.text((4, y + 18), f"{len(picks)} hits", fill=(160, 160, 160, 255))
            for c, (d, rel) in enumerate(picks):
                x = 130 + c * cell_w
                try:
                    im = Image.open(WORKSHOP / d / rel).convert("RGBA")
                    im.thumbnail((cell_w - 6, cell_h - 6))
                    sheet.alpha_composite(im, (x + 3, y + 3))
                except Exception:
                    draw.text((x + 4, y + 40), "n/a", fill=(255, 80, 80, 255))
                draw.text((x + 3, y + cell_h), f"{c}:{Path(rel).stem[:16]}", fill=(255, 255, 255, 255))
        sheet.convert("RGB").save(out / f"sheet_{n}.png")
    (out / "candidates.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(subjects)} subjects, {len(sheets)} sheets -> {out}")


if __name__ == "__main__":
    sys.exit(main())
