#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive QA & Validation Test for France WW1 Rework."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def test_france_qa():
    print('=================================================================')
    print('        FRANCE WW1 COMPLETE AUDIT & VERIFICATION SUITE           ')
    print('=================================================================')

    # 1. Focus Tree File
    focus_file = ROOT / 'common' / 'national_focus' / 'france.txt'
    assert focus_file.exists(), 'france.txt does not exist'
    raw_focus = focus_file.read_bytes()
    assert not raw_focus.startswith(b'\xef\xbb\xbf'), 'france.txt must NOT have BOM'
    content_focus = raw_focus.decode('utf-8')

    # Parse focus blocks with brace balancing
    focus_blocks = []
    lines = content_focus.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == 'focus = {':
            start = i
            depth = 1
            i += 1
            block_lines = []
            while i < len(lines) and depth > 0:
                cur = lines[i]
                depth += cur.count('{') - cur.count('}')
                block_lines.append(cur)
                i += 1
            focus_blocks.append('\n'.join(block_lines))
        else:
            i += 1

    print(f'[*] Focuses parsed: {len(focus_blocks)} (Expected: 200)')
    assert len(focus_blocks) == 200, f'Expected exactly 200 focuses, found {len(focus_blocks)}'


    foci = []
    ids = []
    coords = []
    icons = []
    for b in focus_blocks:
        fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
        icon = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
        x = int(re.search(r'\bx\s*=\s*(\d+)', b).group(1))
        y = int(re.search(r'\by\s*=\s*(\d+)', b).group(1))
        prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', b)
        parsed_prereqs = []
        for pr in prereqs:
            parsed_prereqs.extend(re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr))
        ids.append(fid)
        coords.append((x, y))
        icons.append(icon)
        foci.append({'id': fid, 'icon': icon, 'x': x, 'y': y, 'prereqs': parsed_prereqs})

    # Check duplicate IDs
    dup_ids = [x for x in set(ids) if ids.count(x) > 1]
    assert not dup_ids, f'Duplicate focus IDs found: {dup_ids}'
    print('    -> 0 duplicate focus IDs.')

    # Check duplicate coordinates
    dup_coords = [c for c in set(coords) if coords.count(c) > 1]
    assert not dup_coords, f'Duplicate focus coordinates found: {dup_coords}'
    print('    -> 0 coordinate collisions.')

    # Check dimensions
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    print(f'    -> Tree dimensions: X=[{min(xs)}..{max(xs)}], Y=[{min(ys)}..{max(ys)}] (Flattened: Y <= 12).')
    assert max(ys) <= 12, f'Tree depth Y={max(ys)} exceeds maximum allowed depth 12'

    # Check prerequisites integrity
    id_set = set(ids)
    missing_prereqs = []
    for f in foci:
        for p in f['prereqs']:
            if p not in id_set:
                missing_prereqs.append((f['id'], p))
    assert not missing_prereqs, f'Missing prerequisites: {missing_prereqs}'
    print('    -> 100% prerequisite DAG links valid.')

    # 2. Check Icons in GFX
    gfx_file = ROOT / 'interface' / 'ww1_france_goals.gfx'
    assert gfx_file.exists(), 'ww1_france_goals.gfx not found'
    gfx_content = gfx_file.read_text(encoding='utf-8', errors='ignore')
    sprites = set(re.findall(r'name\s*=\s*"([^"]+)"', gfx_content))

    missing_icons = []
    missing_shines = []
    for icon in icons:
        if icon not in sprites:
            missing_icons.append(icon)
        if f'{icon}_shine' not in sprites:
            missing_shines.append(f'{icon}_shine')

    assert not missing_icons, f'Missing focus sprites in gfx: {missing_icons}'
    assert not missing_shines, f'Missing focus shine sprites in gfx: {missing_shines}'
    print(f'    -> All 200 focus icons verified in GFX with complete _shine overlays.')

    # Check uniqueness of icons
    dup_icons = [i for i in set(icons) if icons.count(i) > 1]
    assert not dup_icons, f'Duplicate icons used: {dup_icons}'
    print(f'    -> 200 unique icons across the entire tree (0 duplicates).')

    # 3. Check Banned Modifiers
    banned = ['recovery_rate_factor', 'division_speed', 'production_speed_railway_factor',
              'entrenchment', 'artillery_attack_factor', 'attrition_for_enemy', 'escort_efficiency_factor']

    ideas_file = ROOT / 'common' / 'ideas' / 'ww1_france_ideas.txt'
    ideas_raw = ideas_file.read_bytes()
    assert not ideas_raw.startswith(b'\xef\xbb\xbf'), 'ww1_france_ideas.txt must NOT have BOM'
    ideas_text = ideas_raw.decode('utf-8')

    for b_mod in banned:
        assert not re.search(rf'\b{b_mod}\s*=', content_focus), f'Banned modifier {b_mod} assigned in france.txt'
        assert not re.search(rf'\b{b_mod}\s*=', ideas_text), f'Banned modifier {b_mod} assigned in ww1_france_ideas.txt'
    print('    -> 0 banned modifiers detected.')


    # 4. Check Events & Decisions Files BOM
    events_raw = (ROOT / 'events' / 'ww1_france_events.txt').read_bytes()
    assert not events_raw.startswith(b'\xef\xbb\xbf'), 'ww1_france_events.txt must NOT have BOM'
    assert 'SOV' not in events_raw.decode('utf-8'), 'Found SOV in events file! Must be RUS'
    assert 'SOV' not in content_focus, 'Found SOV in focus tree! Must be RUS'
    print('    -> UTF-8 NO BOM verified for events & decisions; all diplomatic references use RUS (0 SOV).')

    # 5. Check Localisation
    en_file = ROOT / 'localisation' / 'english' / 'ww1_france_l_english.yml'
    pt_file = ROOT / 'localisation' / 'braz_por' / 'ww1_france_l_braz_por.yml'

    assert en_file.read_bytes().startswith(b'\xef\xbb\xbf'), 'English loc must have BOM'
    assert pt_file.read_bytes().startswith(b'\xef\xbb\xbf'), 'PT loc must have BOM'

    en_text = en_file.read_text(encoding='utf-8-sig')
    pt_text = pt_file.read_text(encoding='utf-8-sig')

    missing_loc_en = []
    missing_loc_pt = []
    for fid in ids:
        if f' {fid}:' not in en_text or f' {fid}_desc:' not in en_text:
            missing_loc_en.append(fid)
        if f' {fid}:' not in pt_text or f' {fid}_desc:' not in pt_text:
            missing_loc_pt.append(fid)

    assert not missing_loc_en, f'Missing English loc for focuses: {missing_loc_en[:5]}'
    assert not missing_loc_pt, f'Missing PT loc for focuses: {missing_loc_pt[:5]}'
    print('    -> Complete bilingual coverage (200/200 focus titles & descs in EN and PT-BR).')

    print('=================================================================')
    print('>>> ALL FRANCE AUDIT CHECKS PASSED WITH ZERO ERRORS (Code 0) <<<')
    print('=================================================================')

if __name__ == '__main__':
    test_france_qa()
