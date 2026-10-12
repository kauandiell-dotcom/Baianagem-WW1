#!/usr/bin/env python3
"""
Consolidates all British WW1 localization into:
- localisation/english/ww1_britain_l_english.yml
- localisation/braz_por/ww1_britain_l_braz_por.yml

Enforces:
1. UTF-8 BOM encoding (\xef\xbb\xbf)
2. 100% bilingual parity between EN and PT-BR
3. Inclusion of all shortcuts, 5 pillars, decisions, and events
"""
import glob
import os
import re

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def parse_kv(fpath):
    if not os.path.exists(fpath):
        return {}
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    res = {}
    for line in text.splitlines():
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):\d*\s*"(.*)"\s*$', line)
        if m:
            res[m.group(1)] = m.group(2)
    return res

def main():
    en_target = os.path.join(MOD_ROOT, "localisation", "english", "ww1_britain_l_english.yml")
    pt_target = os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_britain_l_braz_por.yml")

    en_dict = parse_kv(en_target)
    pt_dict = parse_kv(pt_target)

    # Ingest extra
    en_extra = parse_kv(os.path.join(MOD_ROOT, "localisation", "english", "ww1_britain_extra_l_english.yml"))
    pt_extra = parse_kv(os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_britain_extra_l_braz_por.yml"))
    for k, v in en_extra.items():
        if k not in en_dict:
            en_dict[k] = v
    for k, v in pt_extra.items():
        if k not in pt_dict:
            pt_dict[k] = v

    # Ingest replace
    for f in sorted(glob.glob(os.path.join(MOD_ROOT, "localisation", "replace", "*britain*english.yml"))):
        d = parse_kv(f)
        for k, v in d.items():
            if k not in en_dict:
                en_dict[k] = v

    for f in sorted(glob.glob(os.path.join(MOD_ROOT, "localisation", "replace", "*britain*braz_por.yml"))):
        d = parse_kv(f)
        for k, v in d.items():
            if k not in pt_dict:
                pt_dict[k] = v

    # Ensure any missing keys in one are matched in the other
    all_keys = sorted(set(en_dict.keys()) | set(pt_dict.keys()))
    for k in all_keys:
        if k not in en_dict:
            en_dict[k] = pt_dict[k]
        if k not in pt_dict:
            pt_dict[k] = en_dict[k]

    # Add custom tooltips if missing
    custom_tooltips = {
        "ENG_call_indian_corps_tt": (
            "Mobilises 40,000 Indian Corps troops with infantry equipment from the British Raj.",
            "Mobiliza 40.000 soldados do Corpo Indiano com equipamento de infantaria do Raj Britânico."
        ),
        "ENG_ww1_continental_commitment_tt": (
            "Britain commits fully to the continental alliance with France and Russia.",
            "A Grã-Bretanha se compromete plenamente com a aliança continental com a França e a Rússia."
        ),
        "ENG_ww1_armed_neutrality_tt": (
            "Britain maintains armed neutrality, safeguarding the Empire without continental entanglements.",
            "A Grã-Bretanha mantém neutralidade armada, protegendo o Império sem envolvimento continental."
        )
    }
    for k, (en_val, pt_val) in custom_tooltips.items():
        if k not in en_dict:
            en_dict[k] = en_val
        if k not in pt_dict:
            pt_dict[k] = pt_val

    # Write EN file with UTF-8 BOM
    with open(en_target, "wb") as f:
        f.write(b"\xef\xbb\xbf")
        header = "l_english:\n"
        f.write(header.encode("utf-8"))
        for k in sorted(en_dict.keys()):
            val = en_dict[k].replace('"', '\\"')
            line = f' {k}:0 "{val}"\n'
            f.write(line.encode("utf-8"))

    # Write PT file with UTF-8 BOM
    with open(pt_target, "wb") as f:
        f.write(b"\xef\xbb\xbf")
        header = "l_braz_por:\n"
        f.write(header.encode("utf-8"))
        for k in sorted(pt_dict.keys()):
            val = pt_dict[k].replace('"', '\\"')
            line = f' {k}:0 "{val}"\n'
            f.write(line.encode("utf-8"))

    print(f"Successfully consolidated {len(all_keys)} keys with UTF-8 BOM into EN and PT-BR.")

if __name__ == "__main__":
    main()
