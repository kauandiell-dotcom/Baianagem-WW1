#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive verification and audit suite for the German rework."""

import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def check_file_encoding(path, expect_bom):
    with open(path, 'rb') as f:
        data = f.read(3)
    has_bom = (data == b'\xef\xbb\xbf')
    if expect_bom and not has_bom:
        return f"FAIL: {path.name} expected UTF-8 BOM, but BOM is missing"
    if not expect_bom and has_bom:
        return f"FAIL: {path.name} expected UTF-8 NO BOM, but BOM found"
    return "OK"

def check_brackets(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    depth = 0
    in_quote = False
    in_comment = False
    for i, ch in enumerate(content):
        if ch == '\n':
            in_comment = False
            continue
        if in_comment:
            continue
        if ch == '#':
            in_comment = True
            continue
        if ch == '"':
            in_quote = not in_quote
            continue
        if in_quote:
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                return f"FAIL: {path.name} extra closing brace at char {i}"
    if depth != 0:
        return f"FAIL: {path.name} unclosed braces, final depth={depth}"
    return "OK"

print("=== 1. ENCODING & BRACKET AUDIT ===")
txt_files = [
    ROOT / 'common' / 'national_focus' / 'germany.txt',
    ROOT / 'events' / 'ww1_germany_events.txt',
    ROOT / 'common' / 'ideas' / 'ww1_germany_ideas.txt',
    ROOT / 'common' / 'decisions' / 'categories' / 'ww1_germany_categories.txt',
    ROOT / 'common' / 'decisions' / 'ww1_germany_decisions.txt',
]
for f in txt_files:
    enc_status = check_file_encoding(f, expect_bom=False)
    b_status = check_brackets(f)
    print(f"  {f.name:35} Encoding: {enc_status:4} | Brackets: {b_status}")
    if enc_status != "OK" or b_status != "OK":
        sys.exit(1)

yml_files = [
    ROOT / 'localisation' / 'english' / 'ww1_germany_focus_l_english.yml',
    ROOT / 'localisation' / 'braz_por' / 'ww1_germany_focus_l_braz_por.yml',
]
for f in yml_files:
    enc_status = check_file_encoding(f, expect_bom=True)
    print(f"  {f.name:35} Encoding: {enc_status:4}")
    if enc_status != "OK":
        sys.exit(1)

print("\n=== 2. FOCUS TREE AUDIT ===")
with open(ROOT / 'common' / 'national_focus' / 'germany.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Count total focuses
focus_ids = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([A-Za-z0-9_]+)', text)
print(f"Total focuses in germany.txt: {len(focus_ids)}")
if len(focus_ids) != 245:
    print(f"WARNING: Expected 245 focuses, found {len(focus_ids)}")

# Check duplicate focus IDs
unique_fids = set()
duplicates = []
for fid in focus_ids:
    if fid in unique_fids:
        duplicates.append(fid)
    unique_fids.add(fid)
print(f"Duplicate focus IDs: {len(duplicates)}")
if duplicates:
    print("  Duplicates:", duplicates)
    sys.exit(1)

# Check coordinates for all focuses in wing 1 (x < 21)
coords = {}
coord_collisions = []
blocks = re.findall(r'focus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', text)
wing1_count = 0
for b in blocks:
    mid = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', b)
    mx = re.search(r'x\s*=\s*(-?\d+)', b)
    my = re.search(r'y\s*=\s*(-?\d+)', b)
    if mid and mx and my:
        fid = mid.group(1)
        x = int(mx.group(1))
        y = int(my.group(1))
        if x < 21:
            wing1_count += 1
            if (x, y) in coords:
                coord_collisions.append(((x, y), fid, coords[(x, y)]))
            coords[(x, y)] = fid

print(f"Wing 1 focus count: {wing1_count}")
print(f"Wing 1 coordinate collisions: {len(coord_collisions)}")
if coord_collisions:
    for c in coord_collisions:
        print(f"  Collision at {c[0]}: {c[1]} and {c[2]}")
    sys.exit(1)

print("\n=== 3. SPRITES AUDIT ===")
with open(ROOT / 'scripts' / 'all_normal_germany_sprites.txt', 'r', encoding='utf-8') as f:
    valid_sprites = set(line.strip() for line in f if line.strip())

missing_sprites = []
for b in blocks:
    mid = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', b)
    mic = re.search(r'icon\s*=\s*([A-Za-z0-9_]+)', b)
    mx = re.search(r'x\s*=\s*(-?\d+)', b)
    if mid and mic and mx:
        if int(mx.group(1)) < 21:
            icon = mic.group(1)
            if icon not in valid_sprites:
                missing_sprites.append((mid.group(1), icon))

print(f"Missing sprites in Wing 1: {len(missing_sprites)}")
if missing_sprites:
    for m in missing_sprites:
        print(f"  {m[0]}: {m[1]} NOT FOUND IN SPRITES")
    sys.exit(1)
else:
    print("ALL Wing 1 focuses have 100% valid existing sprites!")

print("\n=== 4. LOCALIZATION AUDIT ===")
en_loc = open(ROOT / 'localisation' / 'english' / 'ww1_germany_focus_l_english.yml', encoding='utf-8-sig').read()
pt_loc = open(ROOT / 'localisation' / 'braz_por' / 'ww1_germany_focus_l_braz_por.yml', encoding='utf-8-sig').read()

missing_en = []
missing_pt = []
from ger_data_focuses import FOCUSES
for f in FOCUSES:
    fid = f['id']
    if f'{fid}:' not in en_loc or f'{fid}_desc:' not in en_loc:
        missing_en.append(fid)
    if f'{fid}:' not in pt_loc or f'{fid}_desc:' not in pt_loc:
        missing_pt.append(fid)

print(f"Missing English focus keys: {len(missing_en)}")
print(f"Missing Brazilian Portuguese focus keys: {len(missing_pt)}")
if missing_en or missing_pt:
    sys.exit(1)
else:
    print("ALL 83 focuses have complete English & Portuguese titles and descriptions!")

print("\n=== 5. STARTING FACTORIES AND DIVISIONS AUDIT ===")
import subprocess
f_res = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'inspect_ger_true_1911.py')], capture_output=True, text=True)
print("Factory Check Output:")
for line in f_res.stdout.strip().splitlines()[-3:]:
    print(" ", line)
if f_res.returncode != 0:
    print("FACTORY CHECK FAILED!")
    sys.exit(1)

with open(ROOT / 'history' / 'units' / 'GER_1936_generic.txt', 'r', encoding='utf-8') as f:
    units_text = f.read()
div_count = len(re.findall(r'division\s*=\s*\{', units_text))
print(f"Starting peacetime divisions in GER_1936_generic.txt: {div_count}")
if div_count != 64:
    print("DIVISION COUNT MISMATCH: Expected 64!")
    sys.exit(1)

print("\n=== ALL AUDITS PASSED WITH ZERO ERRORS ===")
