import glob, re, os

print("=== CHECKING COUNTRY TAGS IN GERMANY FOCUSES ===")

# Collect all country tags from history/countries and common/country_tags
tags = set()
for f in glob.glob('history/countries/*.txt'):
    base = os.path.basename(f)
    match = re.match(r'^([A-Z]{3})\s*-', base)
    if match:
        tags.add(match.group(1))

for f in glob.glob('common/country_tags/*.txt'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        matches = re.findall(r'^([A-Z]{3})\s*=', fp.read(), re.MULTILINE)
        for m in matches:
            tags.add(m)

print(f"Total defined country tags: {len(tags)}")

with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for tags like: target = ENG, country_exists = FRA, has_war_with = RUS, TAG = { ... }
tag_refs = re.findall(r'(?:target\s*=\s*|country_exists\s*=\s*|has_war_with\s*=\s*|tag\s*=\s*|has_guaranteed\s*=\s*)([A-Z]{3})\b', text)
tag_blocks = re.findall(r'^\s*([A-Z]{3})\s*=\s*\{', text, re.MULTILINE)

all_refs = set(tag_refs + tag_blocks)
# Exclude known keywords if any
all_refs = {t for t in all_refs if t not in ('AND', 'NOT')}

print(f"Tags referenced in germany.txt: {all_refs}")
invalid_tags = [t for t in all_refs if t not in tags]
print(f"Invalid / undefined country tags: {invalid_tags}")
assert len(invalid_tags) == 0, f"Found invalid tags: {invalid_tags}"
print("All country tags are 100% valid!")
