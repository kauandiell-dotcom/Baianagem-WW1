"""Import art for the UK extra content and replace the seven focus icons that duplicated another focus.

Donors are read-only Workshop copies; picks were chosen by looking at contact sheets (scripts/britain_extra_art_picks.json).
Writes DDS/PNG textures, interface/ww1_britain_extra_assets.gfx and docs/britain_extra_art_bindings.json, and refuses
exact or near-identical images against every other image of the same kind already in the mod.
"""
from pathlib import Path
import hashlib, json, sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
WORKSHOP = Path('E:/SteamLibrary/steamapps/workshop/content/394360')
PICKS = json.loads((ROOT / 'scripts/britain_extra_art_picks.json').read_text(encoding='utf-8'))


def ahash(im):
    g = ImageOps.grayscale(im.convert('RGBA')).resize((16, 16), Image.Resampling.LANCZOS)
    px = list(g.getdata()); avg = sum(px) / len(px)
    return int(''.join('1' if p > avg else '0' for p in px), 2)


def ham(a, b):
    return bin(a ^ b).count('1')


def existing(folder, exclude=()):
    res = []
    for p in (ROOT / folder).rglob('*'):
        if p.suffix.lower() in ('.png', '.dds', '.tga') and not any(x in p.as_posix() for x in exclude):
            try:
                im = Image.open(p).convert('RGBA')
                res.append((p, hashlib.sha256(im.tobytes()).hexdigest(), ahash(im)))
            except Exception:
                pass
    return res


def fit(im, size, cover):
    if cover:
        return ImageOps.fit(im, size, Image.Resampling.LANCZOS)
    c = ImageOps.contain(im, size, Image.Resampling.LANCZOS)
    out = Image.new('RGBA', size); out.alpha_composite(c, ((size[0] - c.width) // 2, (size[1] - c.height) // 2))
    return out


def main():
    problems, records, sprites = [], [], ['spriteTypes = {']
    pools = {
        'event': existing('gfx/event_pictures', ('ww1_britain_extra',)),
        'idea': existing('gfx/interface/ideas/ww1_britain') + existing('gfx/interface/ideas/ww1_auh_extra'),
        'decision': existing('gfx/interface/decisions/ww1_britain') + existing('gfx/interface/decisions/ww1_auh_extra'),
        'focus': existing('gfx/interface/goals/ww1_britain'),
    }
    seen = {k: [] for k in pools}
    def take(kind, name, mod_rel, size, cover, dest, sprite=None, thr=6):
        mod, rel = mod_rel
        src = WORKSHOP / mod / rel
        im = Image.open(src).convert('RGBA')
        out = fit(im, size, cover)
        px, h = hashlib.sha256(out.tobytes()).hexdigest(), ahash(out)
        for p, ppx, ph in pools[kind]:
            if p.resolve() == dest.resolve():
                continue
            if ppx == px:
                problems.append((kind, name, 'exact duplicate of', p.relative_to(ROOT).as_posix()))
            elif ham(h, ph) <= thr:
                problems.append((kind, name, 'near-duplicate of', p.relative_to(ROOT).as_posix()))
        for label, sh in seen[kind]:
            if ham(h, sh) <= thr:
                problems.append((kind, name, 'near-duplicate of', label))
        seen[kind].append((f'{kind}:{name}', h))
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest)
        tex = dest.relative_to(ROOT).as_posix()
        if sprite:
            sprites.append(f' spriteType = {{ name = "{sprite}" texturefile = "{tex}" }}')
        records.append(dict(kind=kind, id=name, sprite=sprite, donor_id=mod, source_relative=rel,
                            source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(), source_pixels_sha256=hashlib.sha256(im.tobytes()).hexdigest(), texture=tex))
    for k, v in PICKS['events'].items():
        take('event', k, v, (450, 250), True, ROOT / f'gfx/event_pictures/ww1_britain_extra/{k}.dds', f'GFX_event_ww1_britain_x_{k}', 6)
    for k, v in PICKS['ideas'].items():
        take('idea', k, v, (64, 64), False, ROOT / f'gfx/interface/ideas/ww1_britain_extra/ENG_ww1_x_{k}.dds', f'GFX_idea_ENG_ww1_x_{k}', 8)
    for k, v in PICKS['decisions'].items():
        take('decision', k, v, (64, 64), False, ROOT / f'gfx/interface/decisions/ww1_britain_extra/ENG_ww1_x_{k}.dds', f'GFX_decision_ENG_ww1_x_{k}', 8)
    for k, v in PICKS['focus'].items():
        take('focus', 'ENG_ww1_' + k, v, (82, 82), True, ROOT / f'gfx/interface/goals/ww1_britain/ENG_ww1_{k}.png', None, 3)
    sprites.append('}')
    if problems:
        print(json.dumps(problems, ensure_ascii=False, indent=1))
        return 1
    (ROOT / 'interface/ww1_britain_extra_assets.gfx').write_text('\n'.join(sprites) + '\n', encoding='utf-8')
    (ROOT / 'docs/britain_extra_art_bindings.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # keep the main manifest truthful for the replaced focus icons
    mp = ROOT / 'docs/britain_art_manifest.json'
    man = json.loads(mp.read_text(encoding='utf-8-sig'))
    rep = {r['id']: r for r in records if r['kind'] == 'focus'}
    for m in man:
        r = rep.get(m.get('id'))
        if r and m.get('kind') == 'focus':
            m.update(donor_id=r['donor_id'], source_relative=r['source_relative'], source_sha256=r['source_sha256'],
                     source_pixels_sha256=r['source_pixels_sha256'])
    mp.write_text(json.dumps(man, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: len(v) for k, v in PICKS.items()}), 'duplicates: 0')
    return 0


if __name__ == '__main__':
    sys.exit(main())
