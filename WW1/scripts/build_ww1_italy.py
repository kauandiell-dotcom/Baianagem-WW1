"""Master Builder for Italy (ITA) WW1 Focus Tree and Content.
Coordinates all 5 vertical wings, builds common/national_focus/italy.txt,
and produces full bilingual localisation with UTF-8 BOM.
"""
from collections import defaultdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import focus_layout as fl
from check_italy_outline import load as load_outline

from ita_politics_data import POLITICS_FOCI
from ita_economy_data import ECONOMY_FOCI
from ita_diplomacy_data import DIPLOMACY_FOCI
import ita_military_data
MILITARY_FOCI = getattr(ita_military_data, "MILITARY_FOCI", getattr(ita_military_data, "FOCI", {}))
from ita_war_data import WAR_FOCI

P = "ITA_ww1_"

# Combine all focus data
ALL_FOCI = {}
ALL_FOCI.update(POLITICS_FOCI)
ALL_FOCI.update(ECONOMY_FOCI)
ALL_FOCI.update(DIPLOMACY_FOCI)
ALL_FOCI.update(MILITARY_FOCI)
ALL_FOCI.update(WAR_FOCI)

def build_tree():
    rows = load_outline()
    assert len(rows) == 200, f"Expected 200 outline rows, got {len(rows)}"

    nodes = []
    for r in rows:
        nodes.append({
            "id": P + r["id"],
            "parents": [P + p for p in r["parents"]] if r["mode"] == "OR" else ([P + r["parents"][0]] if r["parents"] else []),
            "also": [P + p for p in r["parents"][1:]] if r["mode"] == "AND" and len(r["parents"]) > 1 else [],
            "excl": [P + e for e in r["excl"]],
            "x": 0,
            "y": 0
        })

    pos = fl.layout(nodes, gap_x=2, wing_gap=4)

    # Focus filters per wing
    FILTERS = {
        "pol": "FOCUS_FILTER_POLITICAL",
        "eco": "FOCUS_FILTER_INDUSTRY",
        "dip": "FOCUS_FILTER_POLITICAL",
        "mil": "FOCUS_FILTER_ARMY_XP",
        "war": "FOCUS_FILTER_WAR_SUPPORT"
    }

    SHORTCUTS = [
        ("pol", "giolitti_ministry"),
        ("eco", "industrial_triangle"),
        ("dip", "triple_alliance"),
        ("mil", "army_staff_reorganisation"),
        ("war", "libyan_question")
    ]

    lines = [
        "# Kingdom of Italy (ITA) WW1 Focus Tree (1911-1923)",
        "# Generated deterministically by scripts/build_ww1_italy.py",
        "focus_tree = {",
        "	id = ITA_ww1_1911_1923",
        "	country = { factor = 0 modifier = { add = 100 original_tag = ITA } }",
        "	default = no",
        "	initial_show_position = { focus = ITA_ww1_giolitti_ministry }",
        "	continuous_focus_position = { x = 50 y = 3500 }",
        ""
    ]

    for wing, target in SHORTCUTS:
        lines.append("	shortcut = {")
        lines.append(f"		name = {P}shortcut_{wing}")
        lines.append(f"		target = {P}{target}")
        lines.append("		scroll_wheel_factor = 0.5")
        lines.append("	}")

    lines.append("")

    for r in rows:
        fid = r["id"]
        full_id = P + fid
        data = ALL_FOCI.get(fid)
        if not data:
            raise SystemExit(f"Missing focus data for {fid}")

        x, y = pos[full_id]
        cost = data["cost"]
        search_filter = FILTERS.get(r["wing"], "FOCUS_FILTER_POLITICAL")

        lines.append("	focus = {")
        lines.append(f"		id = {full_id}")
        lines.append(f"		icon = GFX_goal_ww1_{full_id}")
        lines.append(f"		x = {x}")
        lines.append(f"		y = {y}")
        lines.append(f"		cost = {cost}")
        lines.append(f"		search_filters = { search_filter }")

        # Prerequisites
        if r["parents"]:
            if r["mode"] == "OR":
                par_str = " ".join(f"focus = {P}{p}" for p in r["parents"])
                lines.append(f"		prerequisite = {{ {par_str} }}")
            else:
                for p in r["parents"]:
                    lines.append(f"		prerequisite = {{ focus = {P}{p} }}")

        # Mutually exclusive
        if r["excl"]:
            excl_str = " ".join(f"focus = {P}{e}" for e in r["excl"])
            lines.append(f"		mutually_exclusive = {{ {excl_str} }}")

        # Available
        av_parts = ["has_capitulated = no"]
        if data.get("available"):
            av_parts.append(data["available"])
        lines.append(f"		available = {{ {' '.join(av_parts)} }}")

        lines.append("		cancel_if_invalid = yes")
        lines.append("		continue_if_invalid = no")
        lines.append("		available_if_capitulated = no")
        
        ai_val = data.get("ai", "factor = 10")
        if isinstance(ai_val, (int, float)):
            ai_str = f"factor = {ai_val}"
        elif str(ai_val).isdigit():
            ai_str = f"factor = {ai_val}"
        elif str(ai_val).startswith("base ="):
            ai_str = str(ai_val).replace("base =", "factor =").strip()
        elif "factor" in str(ai_val):
            ai_str = str(ai_val)
        else:
            ai_str = f"factor = {ai_val}"
        lines.append(f"		ai_will_do = {{ {ai_str} }}")

        lines.append(f"		completion_reward = {{ {data['effect']} ita_ww1_clamp_counters = yes }}")
        lines.append("	}")
        lines.append("")

    lines.append("}")

    tree_file = ROOT / "common" / "national_focus" / "italy.txt"
    tree_file.parent.mkdir(parents=True, exist_ok=True)
    tree_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {tree_file} with {len(rows)} focuses.")


def build_localisation():
    rows = load_outline()

    LOC_PT = {}
    LOC_EN = {}

    # Shortcuts
    SHORTCUT_TITLES = {
        "pol": ("Asa: Política e Sociedade", "Wing: Politics & Society"),
        "eco": ("Asa: Economia e Mezzogiorno", "Wing: Economy & Mezzogiorno"),
        "dip": ("Asa: Diplomacia e Alinhamento", "Wing: Diplomacy & Alignment"),
        "mil": ("Asa: Forças Armadas", "Wing: Armed Forces"),
        "war": ("Asa: Campanhas e Pós-Guerra", "Wing: Campaigns & Postwar")
    }

    for w, (pt, en) in SHORTCUT_TITLES.items():
        LOC_PT[f"{P}shortcut_{w}"] = pt
        LOC_EN[f"{P}shortcut_{w}"] = en

    # Focuses
    for r in rows:
        fid = r["id"]
        full_id = P + fid
        data = ALL_FOCI[fid]

        LOC_PT[full_id] = r["pt"]
        LOC_EN[full_id] = r["en"]

        desc_pt = data.get("desc_pt") or data.get("pt_desc") or ""
        desc_en = data.get("desc_en") or data.get("en_desc") or ""

        from apply_italy_fixes import clean_pt_text, clean_en_text
        desc_pt = clean_pt_text(desc_pt)
        desc_en = clean_en_text(desc_en)

        LOC_PT[f"{full_id}_desc"] = desc_pt
        LOC_EN[f"{full_id}_desc"] = desc_en

    # Support content
    from ita_support_loc import SUPPORT_LOC_PT, SUPPORT_LOC_EN
    LOC_PT.update(SUPPORT_LOC_PT)
    LOC_EN.update(SUPPORT_LOC_EN)

    # Military Wing Ideas
    import ita_military_data
    for idea_id, idata in ita_military_data.IDEAS.items():
        LOC_PT[idea_id] = idata["pt_name"]
        LOC_EN[idea_id] = idata["en_name"]
        LOC_PT[f"{idea_id}_desc"] = idata["pt_desc"]
        LOC_EN[f"{idea_id}_desc"] = idata["en_desc"]

    # Ensure 100% key parity
    assert set(LOC_PT.keys()) == set(LOC_EN.keys()), f"Mismatch in keys: {set(LOC_PT.keys()) ^ set(LOC_EN.keys())}"

    # Write files with UTF-8 BOM
    for lang, loc_dict in [("braz_por", LOC_PT), ("english", LOC_EN)]:
        out_file = ROOT / "localisation" / lang / f"ww1_italy_l_{lang}.yml"
        out_file.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"l_{lang}:"]
        for k in sorted(loc_dict.keys()):
            val = loc_dict[k].replace('"', '\\"').replace("\r\n", "\\n").replace("\n", "\\n")
            lines.append(f' {k}:0 "{val}"')
        content = "\n".join(lines) + "\n"
        out_file.write_bytes(b"\xef\xbb\xbf" + content.encode("utf-8"))
        print(f"Generated {out_file} with {len(loc_dict)} keys.")


if __name__ == "__main__":
    build_tree()
    build_localisation()
