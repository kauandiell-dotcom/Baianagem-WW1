from pathlib import Path

for p in Path('.').rglob('*.txt'):
    try:
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if 'auh_ww1_update_pressure' in txt:
            print(f"{p}: {txt.count('auh_ww1_update_pressure')} times")
    except Exception:
        pass
