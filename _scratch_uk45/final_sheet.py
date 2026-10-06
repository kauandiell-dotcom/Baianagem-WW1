import json, os
from pathlib import Path
from PIL import Image, ImageDraw
ROOT = Path('.').resolve()
S = Path(os.environ['KIROCREW_SCRATCH'])
new = json.loads((S / 'picks_tmp.json').read_text(encoding='utf-8'))
foc = [k for k in new['focus'] if (ROOT / f'gfx/interface/goals/ww1_britain/ENG_ww1_{k}.png').is_file()]
from itertools import islice
import sys
part = sys.argv[1]
if part == 'focus':
    items = [(k, ROOT / f'gfx/interface/goals/ww1_britain/ENG_ww1_{k}.png') for k in new['focus'] if k in json.load(open(S / 'sheets_focus/candidates.json'))]
    cell = (120, 110)
else:
    items = [(k, ROOT / f'gfx/event_pictures/ww1_britain/{k}.png') for k in json.load(open(S / 'sheets_event/candidates.json')) if k in new['event'] or True]
    items = [(k, p) for k, p in items if p.is_file()] + [('amiens_black_day', ROOT / 'gfx/event_pictures/ww1_britain/amiens_black_day.png')]
    seen = set(); items = [(k, p) for k, p in items if not (k in seen or seen.add(k))]
    cell = (230, 150)
cols = 8 if part == 'focus' else 5
rows = (len(items) + cols - 1) // cols
sheet = Image.new('RGB', (cols * cell[0], rows * (cell[1] + 14)), (28, 28, 28))
d = ImageDraw.Draw(sheet)
for n, (k, p) in enumerate(items):
    x, y = (n % cols) * cell[0], (n // cols) * (cell[1] + 14)
    try:
        im = Image.open(p).convert('RGBA'); im.thumbnail((cell[0] - 6, cell[1] - 6))
        sheet.paste(im, (x + 3, y + 3), im)
    except Exception as e:
        d.text((x + 4, y + 30), 'missing', fill=(255, 80, 80))
    d.text((x + 2, y + cell[1]), k[:22], fill=(255, 255, 255))
half = len(items) // 2 if part == 'focus' else len(items)
sheet.save(S / f'final_{part}.png')
print(len(items), 'items ->', S / f'final_{part}.png', sheet.size)
