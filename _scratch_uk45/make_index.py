import os
from pathlib import Path
W = Path('E:/SteamLibrary/steamapps/workshop/content/394360')
donors = ["3365515312", "3557031692", "2076426030", "2716194283", "2782465344", "3612841387", "2525366756", "2903857354"]
out = Path(os.environ['KIROCREW_SCRATCH']) / 'donor_index.tsv'
n = 0
with out.open('w', encoding='utf-8') as f:
    for d in donors:
        base = W / d
        for sub in ('gfx/interface/goals', 'gfx/event_pictures'):
            root = base / sub
            if not root.is_dir():
                continue
            for p in root.rglob('*'):
                if p.is_file() and p.suffix.lower() in ('.png', '.dds', '.tga'):
                    f.write(f"{d}\t{p.relative_to(base).as_posix()}\t{p.stat().st_size}\n")
                    n += 1
print(n, 'files indexed ->', out)
