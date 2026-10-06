"""Troca os 37 icones de foco repetidos da Alemanha por icones unicos das copias da Workshop (somente leitura).

Cada escolha foi feita olhando a imagem (pranchas de miniaturas). Recusa pixels iguais ou aparencia quase igual
a qualquer outro icone de foco ativo do mod e aos outros icones deste lote.
"""
import hashlib
import json
import re
import sys
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import visual_asset_pipeline as vp
import relayout_tabbed_tree as rt

ROOT = HERE.parent
WORKSHOP = Path('E:/SteamLibrary/steamapps/workshop/content/394360')
GAME = Path('E:/SteamLibrary/steamapps/common/Hearts of Iron IV')
T, E, K = '3365515312', '2716194283', '2076426030'

PICKS = json.loads((HERE / 'ger_focus_icon_picks.json').read_text(encoding='utf-8'))


def main():
    active = vp.active_focus_images(GAME)
    own = {fid for fid in PICKS}
    active_sigs = [(vp.visual_signature(p), ids) for p, ids in active.items()]
    active_px = {vp.pixels(p): ids for p, ids in active.items()}
    seen_px, seen_sig, records, defs, problems = {}, [], [], ['spriteTypes = {'], []
    out_dir = ROOT / 'gfx/interface/goals/ww1_germany'
    out_dir.mkdir(parents=True, exist_ok=True)
    for fid, (mod, rel) in PICKS.items():
        src = WORKSHOP / mod / rel
        if not src.is_file():
            raise FileNotFoundError(src)
        px, sig = vp.pixels(src), vp.visual_signature(src)
        if px in seen_px:
            problems.append((fid, 'pixels iguais a', seen_px[px]))
        for other, osig in seen_sig:
            if vp.resembles(sig, osig):
                problems.append((fid, 'aparencia quase igual a', other))
        if px in active_px and [i for i in active_px[px] if i not in own]:
            problems.append((fid, 'pixels ja usados por', active_px[px]))
        for osig, ids in active_sigs:
            others = [i for i in ids if i not in own]
            if others and vp.resembles(sig, osig):
                problems.append((fid, 'aparencia quase igual a foco', others))
                break
        seen_px[px] = fid
        seen_sig.append((fid, sig))
        name = 'GFX_focus_{}_ww1_{}'.format(fid[:3], fid[4:])
        dest = out_dir / (fid[:3].lower() + '_' + fid[4:] + '.png')
        with Image.open(src) as im:
            im = im.convert('RGBA')
            im = ImageOps.contain(im, (82, 82), method=Image.Resampling.LANCZOS)
            canvas = Image.new('RGBA', (82, 82))
            canvas.alpha_composite(im, ((82 - im.width) // 2, (82 - im.height) // 2))
            canvas.save(dest)
        tex = dest.relative_to(ROOT).as_posix()
        defs += ['\tspriteType = {', f'\t\tname = "{name}"', f'\t\ttexturefile = "{tex}"', '\t}',
                 '\tspriteType = {', f'\t\tname = "{name}_shine"', f'\t\ttexturefile = "{tex}"',
                 '\t\teffectFile = "gfx/FX/buttonstate.lua"', '\t\tanimation = {',
                 f'\t\t\tanimationmaskfile = "{tex}"',
                 '\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"',
                 '\t\t\tanimationrotation = -90.0', '\t\t\tanimationlooping = no', '\t\t\tanimationtime = 0.75',
                 '\t\t\tanimationdelay = 0', '\t\t\tanimationblendmode = "add"', '\t\t\tanimationtype = "scrolling"',
                 '\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }',
                 '\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }', '\t\t}', '\t\tlegacy_lazy_load = no', '\t}']
        records.append(dict(focus=fid, sprite=name, donor_id=mod, source_relative=rel, texture=tex,
                            source_sha256=hashlib.sha256(src.read_bytes()).hexdigest()))
    defs.append('}')
    if problems:
        print(json.dumps(problems, ensure_ascii=False, indent=1))
        return 1
    (ROOT / 'interface/ww1_germany_focus_art.gfx').write_text('\n'.join(defs) + '\n', encoding='utf-8')
    (ROOT / 'docs/germany_focus_art_bindings.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # troca a linha icon = ... de cada foco (Alemanha e Russia)
    for tree, tag in (('germany', 'GER'), ('soviet', 'SOV')):
        p = ROOT / 'common/national_focus/{}.txt'.format(tree)
        raw = p.read_bytes()
        text = raw.decode('utf-8-sig')
        nodes, spans = rt.parse(text)
        out, last = [], 0
        for n, (s, e) in zip(nodes, spans):
            out.append(text[last:s])
            b = text[s:e]
            if n['id'] in PICKS:
                b = re.sub(r'(?m)^(\s*icon\s*=\s*)\S+', lambda m: m.group(1) + 'GFX_focus_{}_ww1_{}'.format(tag, n['id'][4:]), b, count=1)
            out.append(b)
            last = e
        out.append(text[last:])
        p.write_bytes((b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'') + ''.join(out).encode('utf-8'))
    print('icones trocados:', len(records))
    return 0


if __name__ == '__main__':
    sys.exit(main())
