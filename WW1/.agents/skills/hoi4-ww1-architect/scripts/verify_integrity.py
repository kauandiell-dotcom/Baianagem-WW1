import glob, re, os, sys

def verify_mod_integrity(mod_root=".", target_focus_file="common/national_focus/germany.txt"):
    print(f"=== VERIFYING MOD INTEGRITY AT: {os.path.abspath(mod_root)} ===")
    print(f"Target Focus Tree: {target_focus_file}")
    has_errors = False

    # 1. Localization YAML Integrity & UTF-8 BOM
    yaml_files = glob.glob(os.path.join(mod_root, 'localisation/**/*.yml'), recursive=True)
    yaml_errors = []
    for yf in yaml_files:
        with open(yf, 'rb') as fp:
            raw = fp.read()
            if not raw.startswith(b'\xef\xbb\xbf'):
                yaml_errors.append(f"{yf}: Missing UTF-8 BOM!")
        with open(yf, 'r', encoding='utf-8-sig', errors='replace') as fp:
            for idx, line in enumerate(fp, 1):
                s = line.strip()
                if not s or s.startswith('#'):
                    continue
                if s.startswith('--'):
                    yaml_errors.append(f"{yf}:{idx}: Invalid Lua comment '--'")
                q_count = s.count('"')
                if q_count % 2 != 0:
                    yaml_errors.append(f"{yf}:{idx}: Unbalanced quotes in line")

    print(f"1. Localization YAML Integrity: {len(yaml_files)} files checked, {len(yaml_errors)} errors.")
    if yaml_errors:
        has_errors = True
        for e in yaml_errors[:5]:
            print("  ", e)

    # 2. Interface SpriteTypes indexed
    sprite_to_file = {}
    for gf in glob.glob(os.path.join(mod_root, 'interface/*.gfx')):
        with open(gf, 'r', encoding='utf-8', errors='ignore') as fp:
            matches = re.findall(r'name\s*=\s*"([^"]+)"[\s\S]*?texturefile\s*=\s*"([^"]+)"', fp.read())
            for name, tex in matches:
                sprite_to_file[name] = tex

    print(f"2. Interface SpriteTypes indexed: {len(sprite_to_file)}")

    # 3. Check Target Focus Tree Icons & Textures
    focus_path = os.path.join(mod_root, target_focus_file)
    missing_textures = []
    if os.path.exists(focus_path):
        with open(focus_path, 'r', encoding='utf-8', errors='ignore') as fp:
            icons = set(re.findall(r'icon\s*=\s*([A-Za-z0-9_]+)', fp.read()))
            for icon in icons:
                if icon not in sprite_to_file:
                    missing_textures.append(f"SpriteType not found: {icon}")
                else:
                    rel_path = sprite_to_file[icon].replace('/', os.sep).replace('\\\\', os.sep)
                    full_path = os.path.join(mod_root, rel_path)
                    # If texture is defined in mod interface, check if file exists
                    if not os.path.exists(full_path):
                        missing_textures.append(f"Texture file missing on disk: {rel_path} for {icon}")
        print(f"3. Focus Icon & Texture Integrity ({len(icons)} unique icons): {len(missing_textures)} errors.")
    else:
        print(f"3. Focus file {target_focus_file} not found!")
        missing_textures.append(f"Target focus file missing: {target_focus_file}")

    if missing_textures:
        has_errors = True
        for m in missing_textures[:5]:
            print("  ", m)

    # 4. Check Decisions & Missions
    dec_errors = []
    for df in glob.glob(os.path.join(mod_root, 'common/decisions/*.txt')):
        with open(df, 'r', encoding='utf-8', errors='ignore') as fp:
            txt = fp.read()
            if txt.count('{') != txt.count('}'):
                dec_errors.append(f"Mismatched braces in {df}")

    print(f"4. Decisions & Missions Brace Check: {len(dec_errors)} errors.")
    if dec_errors:
        has_errors = True

    print(f"=== RESULT: {'ALL SYSTEMS OPERATIONAL (PASS)' if not has_errors else 'INTEGRITY ERRORS DETECTED (FAIL)'} ===")
    return not has_errors

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    target_f = sys.argv[2] if len(sys.argv) > 2 else 'common/national_focus/germany.txt'
    ok = verify_mod_integrity(root, target_f)
    sys.exit(0 if ok else 1)
