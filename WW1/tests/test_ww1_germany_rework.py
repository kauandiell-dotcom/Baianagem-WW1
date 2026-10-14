"""Master QA Test Suite for German Empire Complete Rework & Endsieg System.

Validates the full specification across:
1. Belgian Railway & Supply Graph Integrity (Liège/Namur supply hubs, level 3 railways to Aachen/Cologne).
2. Date-Gates Purge (Zero 'date >' in germany.txt, frontline operational missions).
3. Western Front Opening & Trench Stalemate Transition (Fused Schlieffen, momentum spirit, deep stalemate).
4. Industrial Cartels (Krupp, Thyssen, BASF Haber-Bosch, Buna rubber) & Chemical Warfare Escalation.
5. Battle of the Atlantic U-Boat Postures, US Tension Clamped Gauge & Zimmermann Telegram.
6. Strategic Air Warfare (Fokker Scourge, Aces Richthofen/Boelcke/Udet, Zeppelin terror raids).
7. OHL Military Dictatorship, Hindenburg Program, and Operation Alberich Strategic Retreat.
8. Asymmetric Colonial Warfare (Lettow-Vorbeck Askari guerrilla in Tanganyika, global subversion) & Tag BAT.
9. Hidden Endsieg Emergency Focus Tree (20 focuses, DAG layout, Volkssturm OOB) & Versailles Peace Engine.
10. Bilingual Localization Integrity (strictly single UTF-8 BOM, 100% key parity).
"""

from collections import defaultdict
import glob
import os
import re
import sys
import unittest

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_focus_tree(filepath):
    """Parses a Clausewitz national focus tree file and returns tree_id and focus dicts."""
    if not os.path.isfile(filepath):
        return None, []

    with open(filepath, "r", encoding="utf-8-sig", errors="replace") as f:
        text = f.read()

    # Strip single-line comments
    clean_lines = [re.sub(r"#[^\n]*", "", line) for line in text.splitlines()]
    clean = "\n".join(clean_lines)

    m_id = re.search(r"\bfocus_tree\s*=\s*\{[^{}]*?\bid\s*=\s*([a-zA-Z0-9_]+)", clean)
    tree_id = m_id.group(1) if m_id else None

    foci = []
    idx = 0
    while True:
        pos = clean.find("focus = {", idx)
        if pos == -1:
            break
        brace = clean.find("{", pos)
        depth = 1
        cur = brace + 1
        while cur < len(clean) and depth > 0:
            if clean[cur] == "{":
                depth += 1
            elif clean[cur] == "}":
                depth -= 1
            cur += 1
        block = clean[pos:cur]

        id_m = re.search(r"\bid\s*=\s*([a-zA-Z0-9_]+)", block)
        if id_m:
            fid = id_m.group(1)
            x_m = re.search(r"\bx\s*=\s*(-?[0-9]+)", block)
            y_m = re.search(r"\by\s*=\s*(-?[0-9]+)", block)
            rel_m = re.search(r"\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)", block)

            x = int(x_m.group(1)) if x_m else None
            y = int(y_m.group(1)) if y_m else None
            rel_id = rel_m.group(1) if rel_m else None

            prereqs = []
            for pr in re.findall(r"prerequisite\s*=\s*\{([^}]+)\}", block):
                for p in re.findall(r"focus\s*=\s*([a-zA-Z0-9_]+)", pr):
                    prereqs.append(p)

            mutually_exclusive = []
            for mex in re.findall(r"mutually_exclusive\s*=\s*\{([^}]+)\}", block):
                for m_id_target in re.findall(r"focus\s*=\s*([a-zA-Z0-9_]+)", mex):
                    mutually_exclusive.append(m_id_target)

            reward_m = re.search(r"completion_reward\s*=\s*\{", block)
            has_reward = False
            reward_body = ""
            if reward_m:
                r_start = reward_m.end()
                r_depth = 1
                r_cur = r_start
                while r_cur < len(block) and r_depth > 0:
                    if block[r_cur] == "{":
                        r_depth += 1
                    elif block[r_cur] == "}":
                        r_depth -= 1
                    r_cur += 1
                reward_body = block[r_start:r_cur - 1].strip()
                has_reward = len(reward_body) > 0

            foci.append({
                "id": fid,
                "x": x,
                "y": y,
                "relative_position_id": rel_id,
                "prereqs": prereqs,
                "mutually_exclusive": mutually_exclusive,
                "has_reward": has_reward,
                "reward_body": reward_body,
                "block": block,
            })
        idx = cur

    # Resolve relative coordinates
    foci_by_id = {f["id"]: f for f in foci}
    resolved = {}

    def get_pos(fid):
        if fid in resolved:
            return resolved[fid]
        f = foci_by_id[fid]
        if f["relative_position_id"] and f["relative_position_id"] in foci_by_id:
            px, py = get_pos(f["relative_position_id"])
            rx = px + (f["x"] if f["x"] is not None else 0)
            ry = py + (f["y"] if f["y"] is not None else 0)
        else:
            rx = f["x"] if f["x"] is not None else 0
            ry = f["y"] if f["y"] is not None else 0
        resolved[fid] = (rx, ry)
        return rx, ry

    for f in foci:
        rx, ry = get_pos(f["id"])
        f["abs_x"] = rx
        f["abs_y"] = ry

    return tree_id, foci


def extract_loc_keys(filepath):
    """Extracts localization keys from a Paradox YAML localization file."""
    keys = set()
    if not os.path.isfile(filepath):
        return keys
    with open(filepath, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            m = re.match(r"^\s*([a-zA-Z0-9_.\-]+):\d*\s+\"", line)
            if m:
                keys.add(m.group(1))
    return keys


def parse_railways(filepath):
    """Parses HOI4 map/railways.txt into list of dicts with level and provinces."""
    railways = []
    if not os.path.isfile(filepath):
        return railways
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            clean = line.split("#")[0].strip()
            if not clean:
                continue
            parts = clean.split()
            if len(parts) >= 3:
                try:
                    lvl = int(parts[0])
                    cnt = int(parts[1])
                    provs = [int(p) for p in parts[2:2 + cnt]]
                    railways.append({"level": lvl, "provinces": provs})
                except ValueError:
                    continue
    return railways


def check_supply_hub(province_id, mod_root=MOD_ROOT):
    """Checks whether a supply hub / node is defined in map/supply_nodes.txt or history/states/."""
    # 1. Check map/supply_nodes.txt
    sn_path = os.path.join(mod_root, "map", "supply_nodes.txt")
    if os.path.isfile(sn_path):
        with open(sn_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                clean = line.split("#")[0].strip()
                parts = clean.split()
                if parts and str(province_id) in parts:
                    return True

    # 2. Check history/states/
    states_dir = os.path.join(mod_root, "history", "states")
    if os.path.isdir(states_dir):
        for fname in os.listdir(states_dir):
            if fname.endswith(".txt"):
                fpath = os.path.join(states_dir, fname)
                with open(fpath, "r", encoding="utf-8-sig", errors="replace") as f:
                    content = f.read()
                    if str(province_id) in content:
                        # Matches: <prov> = { supply_node = 1 } or supply_node = <prov> or supply_hub = <prov>
                        if re.search(rf"\b{province_id}\s*=\s*\{{[^}}]*\bsupply_node\b", content):
                            return True
                        if re.search(rf"\b{province_id}\s*=\s*\{{[^}}]*\bsupply_hub\b", content):
                            return True
                        if re.search(rf"\bsupply_node\s*=\s*{province_id}\b", content):
                            return True
    return False


def check_railway_network_connection(from_provinces, to_provinces, min_level=3, mod_root=MOD_ROOT):
    """Checks if a railway network with level >= min_level connects any from_prov to any to_prov."""
    railways = parse_railways(os.path.join(mod_root, "map", "railways.txt"))
    if not railways:
        return False

    adj = defaultdict(set)
    for r in railways:
        if r["level"] >= min_level:
            provs = r["provinces"]
            for i in range(len(provs) - 1):
                p1, p2 = provs[i], provs[i + 1]
                adj[p1].add(p2)
                adj[p2].add(p1)

    for start in from_provinces:
        if start not in adj:
            continue
        visited = set()
        queue = [start]
        while queue:
            curr = queue.pop(0)
            if curr in to_provinces:
                return True
            visited.add(curr)
            for nxt in adj[curr]:
                if nxt not in visited and nxt not in queue:
                    queue.append(nxt)
    return False


class TestGermanyOverhaul(unittest.TestCase):
    """Comprehensive Master QA Test Suite for German Empire Complete Rework & Endsieg System."""

    def test_belgian_railways_and_supply(self):
        """1. Assert supply hubs exist in Liège/Namur and connect to Cologne/Aachen via level 3+ railways."""
        liege_prov = 11519
        namur_prov = 3516
        cologne_prov = 587
        aachen_prov = 9522

        # 1. Supply Hubs exist in Liège and Namur
        has_liege_hub = check_supply_hub(liege_prov, MOD_ROOT)
        has_namur_hub = check_supply_hub(namur_prov, MOD_ROOT)
        self.assertTrue(
            has_liege_hub,
            f"Supply hub must exist in Liège (province {liege_prov}) in history/states/ or map/supply_nodes.txt",
        )
        self.assertTrue(
            has_namur_hub,
            f"Supply hub must exist in Namur (province {namur_prov}) in history/states/ or map/supply_nodes.txt",
        )

        # 2. Railways file must exist and provide level 3+ connection from Rhineland to Belgium
        railways_file = os.path.join(MOD_ROOT, "map", "railways.txt")
        self.assertTrue(os.path.isfile(railways_file), "map/railways.txt must exist")

        connected = check_railway_network_connection(
            from_provinces={cologne_prov, aachen_prov},
            to_provinces={liege_prov, namur_prov},
            min_level=3,
            mod_root=MOD_ROOT,
        )
        self.assertTrue(
            connected,
            "Railways of level 3+ must connect Cologne/Aachen to Liège/Namur in map/railways.txt",
        )

        # 3. Luxembourg border state setup (state 8)
        lux_state = os.path.join(MOD_ROOT, "history", "states", "8-Luxemburg.txt")
        self.assertTrue(os.path.isfile(lux_state), "history/states/8-Luxemburg.txt must exist")
        with open(lux_state, "r", encoding="utf-8-sig", errors="replace") as f:
            lux_content = f.read()
        self.assertIn("infrastructure", lux_content, "Luxembourg must have valid infrastructure defined")

    def test_date_gates_eliminated(self):
        """2. Assert zero 'date >' triggers in common/national_focus/germany.txt and operational missions exist."""
        focus_file = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        self.assertTrue(os.path.isfile(focus_file), "common/national_focus/germany.txt must exist")

        with open(focus_file, "r", encoding="utf-8-sig", errors="replace") as f:
            raw_text = f.read()

        # Strip comments
        lines_no_comments = [re.sub(r"#[^\n]*", "", line) for line in raw_text.splitlines()]
        clean_text = "\n".join(lines_no_comments)

        date_triggers = re.findall(r"\bdate\s*>\s*[0-9.]+", clean_text)
        self.assertEqual(
            len(date_triggers),
            0,
            f"common/national_focus/germany.txt must contain 0 hardcoded 'date >' triggers, found {len(date_triggers)}: {date_triggers[:5]}",
        )

        # Operational decisions category and mission decisions must exist
        cat_file = os.path.join(MOD_ROOT, "common", "decisions", "categories", "ww1_germany_operational_categories.txt")
        self.assertTrue(
            os.path.isfile(cat_file),
            "common/decisions/categories/ww1_germany_operational_categories.txt must exist",
        )
        with open(cat_file, "r", encoding="utf-8-sig", errors="replace") as f:
            self.assertIn(
                "GER_high_command_operations",
                f.read(),
                "Operational categories must define GER_high_command_operations",
            )

        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_operational_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_operational_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()
        self.assertIn(
            "GER_operation_gericht",
            dec_text,
            "ww1_germany_operational_decisions.txt must define Operation Gericht (Verdun)",
        )
        self.assertIn(
            "GER_gorlice_tarnow_breakthrough",
            dec_text,
            "ww1_germany_operational_decisions.txt must define Gorlice-Tarnow breakthrough",
        )

    def test_schlieffen_and_stalemate(self):
        """3. Assert fused Schlieffen focus, momentum spirit, and stalemate defense transition event."""
        # 1. Fused Schlieffen focus in common/national_focus/germany.txt
        focus_file = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        self.assertTrue(os.path.isfile(focus_file), "common/national_focus/germany.txt must exist")
        with open(focus_file, "r", encoding="utf-8-sig", errors="replace") as f:
            focus_text = f.read()

        self.assertIn(
            "GER_schlieffen_maneuver",
            focus_text,
            "germany.txt must define fused focus GER_schlieffen_maneuver",
        )

        # 2. Western front ideas file
        ideas_file = os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_western_front_ideas.txt")
        self.assertTrue(
            os.path.isfile(ideas_file),
            "common/ideas/ww1_germany_western_front_ideas.txt must exist",
        )
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()

        self.assertIn(
            "GER_schlieffen_momentum",
            ideas_text,
            "ww1_germany_western_front_ideas.txt must define GER_schlieffen_momentum",
        )
        self.assertIn(
            "GER_western_trench_stalemate",
            ideas_text,
            "ww1_germany_western_front_ideas.txt must define GER_western_trench_stalemate",
        )

        # 3. Stalemate transition event
        events_file = os.path.join(MOD_ROOT, "events", "ww1_germany_western_front_events.txt")
        self.assertTrue(
            os.path.isfile(events_file),
            "events/ww1_germany_western_front_events.txt must exist",
        )
        with open(events_file, "r", encoding="utf-8-sig", errors="replace") as f:
            events_text = f.read()

        self.assertIn("ww1_germany.10", events_text, "ww1_germany_western_front_events.txt must define event ww1_germany.10")
        self.assertIn("GER_western_trench_stalemate", events_text, "Event ww1_germany.10 must grant GER_western_trench_stalemate")

    def test_cartels_and_chemical_warfare(self):
        """4. Assert Krupp, Thyssen, Haber-Bosch, Buna rubber, and chemical escalation decisions exist."""
        # 1. Industrial cartels in common/ideas/ww1_germany_ideas.txt
        ideas_file = os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_ideas.txt")
        self.assertTrue(os.path.isfile(ideas_file), "common/ideas/ww1_germany_ideas.txt must exist")
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()

        required_cartel_ideas = [
            "GER_krupp_siege_guns",
            "GER_thyssen_steel_syndicate",
            "GER_haber_bosch_synthesis",
            "GER_buna_rubber",
        ]
        for idea in required_cartel_ideas:
            self.assertIn(idea, ideas_text, f"ww1_germany_ideas.txt must define cartel idea '{idea}'")

        # 2. Chemical warfare category
        cat_file = os.path.join(MOD_ROOT, "common", "decisions", "categories", "ww1_germany_industry_categories.txt")
        self.assertTrue(
            os.path.isfile(cat_file),
            "common/decisions/categories/ww1_germany_industry_categories.txt must exist",
        )
        with open(cat_file, "r", encoding="utf-8-sig", errors="replace") as f:
            self.assertIn("GER_chemical_warfare_program", f.read(), "Industry categories must define GER_chemical_warfare_program")

        # 3. Chemical escalation decisions
        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_cartel_and_chemical_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_cartel_and_chemical_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        chemical_decisions = [
            "GER_chlorine_gas_release",
            "GER_phosgene_gas_shells",
            "GER_mustard_gas_deployment",
        ]
        for cdec in chemical_decisions:
            self.assertIn(cdec, dec_text, f"ww1_germany_cartel_and_chemical_decisions.txt must define '{cdec}'")

    def test_uboat_postures_and_us_tension(self):
        """5. Assert U-boat postures, clamped US tension gauge scripted effects, and Zimmermann telegram exist."""
        # 1. Scripted effects for gauge init and clamping
        effects_file = os.path.join(MOD_ROOT, "common", "scripted_effects", "ww1_germany_naval_effects.txt")
        self.assertTrue(
            os.path.isfile(effects_file),
            "common/scripted_effects/ww1_germany_naval_effects.txt must exist",
        )
        with open(effects_file, "r", encoding="utf-8-sig", errors="replace") as f:
            eff_text = f.read()

        self.assertIn("ger_init_naval_gauges", eff_text, "ww1_germany_naval_effects.txt must define ger_init_naval_gauges")
        self.assertIn("ger_clamp_naval_gauges", eff_text, "ww1_germany_naval_effects.txt must define ger_clamp_naval_gauges")
        self.assertIn("GER_us_intervention_tension", eff_text, "Naval effects must clamp variable GER_us_intervention_tension")

        # 2. U-Boat 3 Postures in naval decisions
        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_naval_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_naval_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        postures = [
            "GER_uboat_cruiser_rules",
            "GER_uboat_declared_war_zone",
            "GER_uboat_unrestricted_warfare",
        ]
        for p in postures:
            self.assertIn(p, dec_text, f"ww1_germany_naval_decisions.txt must define posture '{p}'")

        # 3. Zimmermann Telegram event chain
        events_file = os.path.join(MOD_ROOT, "events", "ww1_germany_naval_events.txt")
        self.assertTrue(
            os.path.isfile(events_file),
            "events/ww1_germany_naval_events.txt must exist",
        )
        with open(events_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ev_text = f.read()
        self.assertIn("MEX", ev_text, "ww1_germany_naval_events.txt must reference Mexico (MEX) in Zimmermann telegram")

    def test_air_warfare_and_zeppelins(self):
        """6. Assert Fokker scourge, historical ace recruitment, and Zeppelin terror raid decisions exist."""
        # 1. Historical Aces in common/characters/GER.txt
        chars_file = os.path.join(MOD_ROOT, "common", "characters", "GER.txt")
        self.assertTrue(os.path.isfile(chars_file), "common/characters/GER.txt must exist")
        with open(chars_file, "r", encoding="utf-8-sig", errors="replace") as f:
            chars_text = f.read()

        aces = [
            "GER_manfred_von_richthofen",
            "GER_oswald_boelcke",
            "GER_ernst_udet",
        ]
        for ace in aces:
            self.assertIn(ace, chars_text, f"common/characters/GER.txt must define ace character '{ace}'")

        # 2. Air decisions
        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_air_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_air_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        self.assertIn("GER_fokker_scourge", dec_text, "ww1_germany_air_decisions.txt must define Fokker Scourge decision")
        self.assertIn("GER_zeppelin_raids_london", dec_text, "ww1_germany_air_decisions.txt must define Zeppelin raid decision")

        # 3. Air ideas
        ideas_file = os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_air_ideas.txt")
        self.assertTrue(
            os.path.isfile(ideas_file),
            "common/ideas/ww1_germany_air_ideas.txt must exist",
        )
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()
        self.assertIn("GER_fokker_scourge_spirit", ideas_text, "ww1_germany_air_ideas.txt must define GER_fokker_scourge_spirit")

    def test_ohl_and_alberich(self):
        """7. Assert Hindenburg program idea and Operation Alberich strategic retreat decision exist."""
        # 1. Hindenburg Program in common/ideas/ww1_germany_ideas.txt
        ideas_file = os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_ideas.txt")
        self.assertTrue(os.path.isfile(ideas_file), "common/ideas/ww1_germany_ideas.txt must exist")
        with open(ideas_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ideas_text = f.read()
        self.assertIn("GER_hindenburg_program", ideas_text, "ww1_germany_ideas.txt must define GER_hindenburg_program")

        # 2. Operation Alberich and War Economy Decisions
        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_war_economy_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_war_economy_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        self.assertIn("GER_operation_alberich", dec_text, "ww1_germany_war_economy_decisions.txt must define GER_operation_alberich")
        self.assertIn("GER_kriegsanleihen", dec_text, "ww1_germany_war_economy_decisions.txt must define GER_kriegsanleihen")
        self.assertIn("GER_ploiesti_oil", dec_text, "ww1_germany_war_economy_decisions.txt must define GER_ploiesti_oil")

    def test_lettow_vorbeck_and_tag_bat(self):
        """8. Assert Askari colonial division in Tanganyika, subversion decisions, and tag BAT definition exist."""
        # 1. Askari colonial OOB in German East Africa (Tanganyika state 546)
        oob_file = os.path.join(MOD_ROOT, "history", "units", "GER_east_africa.txt")
        self.assertTrue(
            os.path.isfile(oob_file),
            "history/units/GER_east_africa.txt must exist",
        )
        with open(oob_file, "r", encoding="utf-8-sig", errors="replace") as f:
            oob_text = f.read()
        self.assertTrue(
            "546" in oob_text or "Tanganyika" in oob_text,
            "GER_east_africa.txt must reference Tanganyika (state 546)",
        )
        self.assertIn("Askari", oob_text, "GER_east_africa.txt must deploy authentic Askari units")

        # 2. Colonial and Global Subversion Decisions
        dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_colonial_and_subversion_decisions.txt")
        self.assertTrue(
            os.path.isfile(dec_file),
            "common/decisions/ww1_germany_colonial_and_subversion_decisions.txt must exist",
        )
        with open(dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            dec_text = f.read()

        self.assertIn("GER_deutsch_ostafrika_guerrilla", dec_text, "Colonial decisions must define East Africa guerrilla category")
        self.assertIn("GER_support_easter_rising", dec_text, "Subversion decisions must define Irish Easter Rising decision")
        self.assertIn("GER_ghadar_conspiracy", dec_text, "Subversion decisions must define Indian Ghadar conspiracy decision")

        # 3. Tag BAT (United Baltic Duchy)
        tag_file = os.path.join(MOD_ROOT, "common", "country_tags", "01_ww1_tags.txt")
        self.assertTrue(os.path.isfile(tag_file), "common/country_tags/01_ww1_tags.txt must exist")
        with open(tag_file, "r", encoding="utf-8-sig", errors="replace") as f:
            self.assertTrue(
                re.search(r"\bBAT\s*=\s*\"?[^\n\"]+\"?", f.read()) is not None,
                "01_ww1_tags.txt must register tag BAT",
            )

        bat_country = os.path.join(MOD_ROOT, "common", "countries", "United Baltic Duchy.txt")
        self.assertTrue(os.path.isfile(bat_country), "common/countries/United Baltic Duchy.txt must exist")

        bat_history = os.path.join(MOD_ROOT, "history", "countries", "BAT - United Baltic Duchy.txt")
        self.assertTrue(os.path.isfile(bat_history), "history/countries/BAT - United Baltic Duchy.txt must exist")

        colors_file = os.path.join(MOD_ROOT, "common", "countries", "colors.txt")
        self.assertTrue(os.path.isfile(colors_file), "common/countries/colors.txt must exist")
        with open(colors_file, "r", encoding="utf-8-sig", errors="replace") as f:
            self.assertTrue(
                re.search(r"\bBAT\s*=\s*\{", f.read()) is not None,
                "common/countries/colors.txt must define color for BAT",
            )

    def test_endsieg_and_versailles(self):
        """9. Assert hidden Endsieg tree (20 focuses, DAG layout), Volkssturm OOB, and Rhine crossing event."""
        # 1. Dedicated Endsieg emergency tree
        endsieg_tree_file = os.path.join(MOD_ROOT, "common", "national_focus", "ww1_germany_endsieg.txt")
        self.assertTrue(
            os.path.isfile(endsieg_tree_file),
            "common/national_focus/ww1_germany_endsieg.txt must exist",
        )

        tree_id, foci = parse_focus_tree(endsieg_tree_file)
        self.assertEqual(tree_id, "ww1_germany_endsieg_focus", "Endsieg tree ID must be 'ww1_germany_endsieg_focus'")
        self.assertEqual(len(foci), 20, f"Endsieg emergency tree must have exactly 20 focuses, found {len(foci)}")

        ids = [f["id"] for f in foci]
        self.assertEqual(len(ids), len(set(ids)), "Focus IDs in Endsieg tree must be unique")
        foci_by_id = {f["id"]: f for f in foci}

        # Spatial grid assertions: 0 coordinate collisions, dx >= 2 on same row, 1 <= dy <= 3
        coords = [(f["abs_x"], f["abs_y"]) for f in foci]
        self.assertEqual(len(coords), len(set(coords)), "Endsieg tree must have 0 coordinate collisions")

        rows = defaultdict(list)
        for f in foci:
            rows[f["abs_y"]].append((f["abs_x"], f["id"]))

        for y, row in sorted(rows.items()):
            row.sort(key=lambda item: item[0])
            for i in range(len(row) - 1):
                x1, id1 = row[i]
                x2, id2 = row[i + 1]
                self.assertGreaterEqual(
                    abs(x2 - x1),
                    2,
                    f"Endsieg banner collision on row y={y}: {id1} (x={x1}) and {id2} (x={x2}) have dx < 2",
                )

        for f in foci:
            self.assertTrue(f["has_reward"], f"Endsieg focus {f['id']} must have a substantive completion_reward")
            for p_id in f["prereqs"]:
                self.assertTrue(p_id in foci_by_id, f"Focus {f['id']} references non-existent parent {p_id}")
                dy = f["abs_y"] - foci_by_id[p_id]["abs_y"]
                self.assertGreater(dy, 0, f"Focus {f['id']} must be below parent {p_id}")
                self.assertTrue(1 <= dy <= 3, f"Focus {f['id']} to parent {p_id} spans {dy} rows (must be 1..3)")

        # 2. Volkssturm emergency OOB
        volkssturm_oob = os.path.join(MOD_ROOT, "history", "units", "GER_volkssturm_endsieg.txt")
        self.assertTrue(
            os.path.isfile(volkssturm_oob),
            "history/units/GER_volkssturm_endsieg.txt must exist",
        )
        with open(volkssturm_oob, "r", encoding="utf-8-sig", errors="replace") as f:
            v_text = f.read()
        self.assertTrue(
            "Volkssturm" in v_text or "Landsturm" in v_text,
            "GER_volkssturm_endsieg.txt must define Volkssturm/Landsturm emergency divisions",
        )

        # 3. Rhine crossing and crisis event
        events_file = os.path.join(MOD_ROOT, "events", "ww1_germany_endsieg_events.txt")
        self.assertTrue(
            os.path.isfile(events_file),
            "events/ww1_germany_endsieg_events.txt must exist",
        )
        with open(events_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ev_text = f.read()

        self.assertIn("ww1_germany_endsieg.1", ev_text, "ww1_germany_endsieg_events.txt must define event ww1_germany_endsieg.1")
        self.assertTrue(
            "42" in ev_text or "587" in ev_text or "55" in ev_text or "surrender_progress" in ev_text,
            "Event ww1_germany_endsieg.1 must check Rhine crossing / surrender progress",
        )
        self.assertIn("load_focus_tree = ww1_germany_endsieg_focus", ev_text, "Option B must load ww1_germany_endsieg_focus")

        # 4. Post-Versailles Weimar & Freikorps decisions
        weimar_dec_file = os.path.join(MOD_ROOT, "common", "decisions", "ww1_germany_weimar_and_freikorps_decisions.txt")
        self.assertTrue(
            os.path.isfile(weimar_dec_file),
            "common/decisions/ww1_germany_weimar_and_freikorps_decisions.txt must exist",
        )
        with open(weimar_dec_file, "r", encoding="utf-8-sig", errors="replace") as f:
            w_text = f.read()
        self.assertIn("GER_spartakist_uprising", w_text, "Weimar decisions must define Spartakist uprising")
        self.assertIn("GER_baltic_freikorps_defense", w_text, "Weimar decisions must define Baltic Freikorps defense")

    def test_localisation_bom_and_parity(self):
        """10. Assert strictly single UTF-8 BOM and key parity across German rework localization files."""
        loc_dir = os.path.join(MOD_ROOT, "localisation")
        self.assertTrue(os.path.isdir(loc_dir), "localisation/ directory must exist")

        en_rework_file = os.path.join(loc_dir, "english", "ww1_germany_rework_l_english.yml")
        pt_rework_file = os.path.join(loc_dir, "braz_por", "ww1_germany_rework_l_braz_por.yml")

        self.assertTrue(
            os.path.isfile(en_rework_file),
            "localisation/english/ww1_germany_rework_l_english.yml must exist",
        )
        self.assertTrue(
            os.path.isfile(pt_rework_file),
            "localisation/braz_por/ww1_germany_rework_l_braz_por.yml must exist",
        )

        for fpath in [en_rework_file, pt_rework_file]:
            rel = os.path.relpath(fpath, MOD_ROOT)
            with open(fpath, "rb") as bf:
                header = bf.read(6)
            self.assertEqual(
                header[:3],
                b"\xef\xbb\xbf",
                f"{rel} must begin with UTF-8 BOM (\\xef\\xbb\\xbf)",
            )
            self.assertNotEqual(
                header[3:6],
                b"\xef\xbb\xbf",
                f"{rel} has double UTF-8 BOM corruption",
            )

        en_keys = extract_loc_keys(en_rework_file)
        pt_keys = extract_loc_keys(pt_rework_file)

        self.assertGreater(
            len(en_keys),
            0,
            "ww1_germany_rework_l_english.yml must contain localization keys",
        )
        self.assertEqual(
            en_keys,
            pt_keys,
            f"Key mismatch between English and Portuguese localization for German rework: {en_keys ^ pt_keys}",
        )

    def test_brest_litovsk_territorial_engine(self):
        """11. Assert Brest-Litovsk territorial engine transfers Polish, Baltic, and Ukrainian states and creates puppets."""
        eff_file = os.path.join(MOD_ROOT, "common", "scripted_effects", "zz_ww1_eastern_settlement.txt")
        self.assertTrue(os.path.isfile(eff_file), "zz_ww1_eastern_settlement.txt must exist")
        with open(eff_file, "r", encoding="utf-8-sig", errors="replace") as f:
            e_text = f.read()

        # Must transfer Polish states (10, 87, 92), Baltic states (188, 189, 190, 191), and Ukrainian states (192, 193, 196)
        for st in ["10", "87", "92", "188", "189", "190", "191", "192", "193", "196"]:
            self.assertIn(f"transfer_state = {st}", e_text, f"Brest-Litovsk settlement must transfer state {st}")

        # Must puppet or release client tags
        self.assertTrue(
            "release_puppet = POL" in e_text or "puppet = POL" in e_text,
            "Brest-Litovsk settlement must puppet or release POL",
        )
        self.assertTrue(
            "release_puppet = UKR" in e_text or "puppet = UKR" in e_text,
            "Brest-Litovsk settlement must puppet or release UKR",
        )
        self.assertTrue(
            "release_puppet = BAT" in e_text or "puppet = BAT" in e_text,
            "Brest-Litovsk settlement must puppet or release BAT",
        )

    def test_mitteleuropa_protectorates(self):
        """12. Assert German focus tree and events properly release and puppet Poland, Ukraine, and United Baltic Duchy."""
        g_focus = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        self.assertTrue(os.path.isfile(g_focus), "germany.txt must exist")
        with open(g_focus, "r", encoding="utf-8-sig", errors="replace") as f:
            g_text = f.read()

        ev_file = os.path.join(MOD_ROOT, "events", "ww1_germany_events.txt")
        self.assertTrue(os.path.isfile(ev_file), "ww1_germany_events.txt must exist")
        with open(ev_file, "r", encoding="utf-8-sig", errors="replace") as f:
            ev_text = f.read()

        # Poland Regency
        self.assertTrue(
            "puppet = POL" in g_text or "release_puppet = POL" in g_text or "puppet = POL" in ev_text or "release_puppet = POL" in ev_text,
            "Regency Kingdom of Poland must puppet/release POL",
        )
        # Ukrainian Hetmanate
        self.assertTrue(
            "puppet = UKR" in g_text or "release_puppet = UKR" in g_text or "puppet = UKR" in ev_text or "release_puppet = UKR" in ev_text,
            "Ukrainian Hetmanate must puppet/release UKR",
        )
        # Baltic Duchy
        self.assertTrue(
            "puppet = BAT" in g_text or "release_puppet = BAT" in g_text or "puppet = BAT" in ev_text or "release_puppet = BAT" in ev_text,
            "Establish United Baltic Duchy must puppet/release BAT",
        )

    def test_four_political_paths(self):
        """13. Assert German focus tree or events implement the 4 political paths (Imperial, Vaterlandspartei, Weimar, Spartakusbund)."""
        g_focus = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        with open(g_focus, "r", encoding="utf-8-sig", errors="replace") as f:
            g_text = f.read()

        # 1. Imperial Pax Germanica
        self.assertIn("GER_pax_germanica", g_text, "germany.txt must define Imperial Pax Germanica focus")
        # 2. Vaterlandspartei Totalitarian Dictatorship
        self.assertIn("GER_vaterlandspartei_dictatorship", g_text, "germany.txt must define Vaterlandspartei dictatorship focus")
        # 3. Weimar Early Peace Resolution
        self.assertIn("GER_weimar_peace_resolution", g_text, "germany.txt must define Weimar peace resolution focus")
        # 4. Spartakusbund Red Revolution
        self.assertIn("GER_spartakusbund_revolution", g_text, "germany.txt must define Spartakusbund red revolution focus")


if __name__ == "__main__":
    unittest.main()

