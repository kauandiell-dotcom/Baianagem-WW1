from pathlib import Path
import re

ROOT = Path(".")
print("=== SEARCHING SCRIPT FILES FOR FILENAMES IN NAME/DESC/TITLE/TEXT ===")

script_dirs = ["common/national_focus", "common/ideas", "common/decisions", "events", "history/countries"]
matches = []

for sdir in script_dirs:
    for p in (ROOT / sdir).rglob("*.txt"):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            for lno, line in enumerate(f, 1):
                # match name = "..." or desc = "..." or title = "..."
                m = re.search(r'\b(name|desc|title|text)\s*=\s*\"?([^\s\"]+\.(txt|dds|yml|png|gfx|gui|csv))\b', line, re.IGNORECASE)
                if m:
                    matches.append((p.relative_to(ROOT), lno, line.strip()))

print(f"Total script references with filenames in text fields: {len(matches)}")
for p, lno, text in matches:
    print(f"  [{p}:{lno}] {text}")
