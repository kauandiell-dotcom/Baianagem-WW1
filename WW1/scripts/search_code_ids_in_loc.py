from pathlib import Path
import re

ROOT = Path(".")
print("=== SEARCHING LOCALISATION VALUES FOR CODE IDENTIFIERS / SNAKE_CASE ===")

matches = []
for p in (ROOT / "localisation").rglob("*.yml"):
    with open(p, "r", encoding="utf-8-sig", errors="ignore") as f:
        for lno, line in enumerate(f, 1):
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            m = re.match(r'^\s*([\w\.\-]+):\d*\s*\"(.*)\"\s*$', line)
            if not m:
                continue
            k, v = m.group(1), m.group(2)
            # If the value is a single word with underscores like "GER_some_thing" or "ita_idea_xyz"
            if re.match(r'^[A-Z0-9]{3}_[a-zA-Z0-9_]+$', v) or re.match(r'^[a-z0-9]+_[a-z0-9_]+$', v):
                matches.append((p.relative_to(ROOT), lno, k, v))

print(f"Total entries where translated text is raw code identifier: {len(matches)}")
for p, lno, k, v in matches[:40]:
    print(f"  [{p}:{lno}] {k} -> \"{v}\"")
