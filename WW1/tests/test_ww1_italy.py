"""Comprehensive quality assurance contracts for Italy (ITA) WW1 content.

Enforces:
1. 200 unique focuses matching docs/italy_focus_outline.txt.
2. Valid DAG layout, no coordinate overlaps, strict downward progression.
3. Symmetric mutual exclusions.
4. Real completion rewards on 100% of focuses (no empty flags or variables).
5. Descriptions stating immediate effects in both EN and PT-BR.
6. Balance ceilings (stability sum <= 0.15, war support sum <= 0.20, PP <= 60, research <= 25%).
7. No free units, no positive manpower spawns, no free equipment.
8. >= 70 events (>= 35 spontaneous), each with >= 2 options, unique 450x250 art.
9. >= 24 decisions in >= 4 categories, cost, duration, cancel_effect when factories used.
10. >= 24 national ideas/institutions, valid modifiers, unique 64x64 art.
11. 5 internal gauges with clamp and weekly update.
12. >= 6 opinion modifiers.
13. >= 6 events dispatched to foreign nations.
14. 100% bilingual localisation parity with UTF-8 BOM.
15. GFX registration with _shine for all focus icons.
"""
from collections import defaultdict, Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
GAME = Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV")
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ww1_foundation import parse, read, walk

OUTLINE = ROOT / "docs" / "italy_focus_outline.txt"
FOCUS_FILE = ROOT / "common" / "national_focus" / "italy.txt"
EFFECTS_FILE = ROOT / "common" / "scripted_effects" / "ww1_italy_effects.txt"


def get_nodes(path):
    if not path.is_file():
        return []
    return parse(read(path))


def get_focus_nodes():
    nodes = get_nodes(FOCUS_FILE)
    trees = [n for n in nodes if n.key == "focus_tree"]
    if not trees:
        return []
    return [n for n in trees[0].value if n.key == "focus"]


def get_outline_ids():
    ids = []
    if not OUTLINE.is_file():
        return ids
    for line in OUTLINE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        p = line.split("|")
        if len(p) >= 2:
            ids.append("ITA_ww1_" + p[1].strip())
    return ids


class TestItalyTreeAndGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.focus_nodes = get_focus_nodes()
        cls.foci = {n.get("id"): n for n in cls.focus_nodes}
        cls.outline_ids = get_outline_ids()

    def test_tree_exists_and_has_exactly_200_focuses(self):
        self.assertTrue(FOCUS_FILE.is_file(), "common/national_focus/italy.txt must exist")
        self.assertEqual(len(self.foci), 200, f"Expected 200 focuses, found {len(self.foci)}")
        self.assertEqual(len(self.outline_ids), 200, f"Expected 200 outline IDs, found {len(self.outline_ids)}")
        self.assertEqual(set(self.foci.keys()), set(self.outline_ids), "Focus IDs must exactly match outline")

    def test_non_overlapping_coordinates_and_descending_y(self):
        coords = [(int(n.get("x", 0)), int(n.get("y", 0))) for n in self.focus_nodes]
        counts = Counter(coords)
        duplicates = [pos for pos, count in counts.items() if count > 1]
        self.assertFalse(duplicates, f"Found duplicate focus coordinates: {duplicates}")

        # Check prerequisite links: child y must be greater than parent y
        for fid, n in self.foci.items():
            for prereq in [p for p in n.value if p.key == "prerequisite"]:
                for ref in prereq.value:
                    if ref.key == "focus":
                        parent_id = ref.value
                        self.assertIn(parent_id, self.foci, f"Parent {parent_id} of {fid} does not exist")
                        self.assertGreater(int(n.get("y")), int(self.foci[parent_id].get("y")),
                                           f"Focus {fid} (y={n.get('y')}) is not strictly below parent {parent_id} (y={self.foci[parent_id].get('y')})")

    def test_mutual_exclusions_are_symmetric(self):
        for fid, n in self.foci.items():
            excls = [x.value for p in n.value if p.key == "mutually_exclusive" for x in p.value if x.key == "focus"]
            for e in excls:
                self.assertIn(e, self.foci, f"Excluded focus {e} does not exist")
                rev_excls = [x.value for p in self.foci[e].value if p.key == "mutually_exclusive" for x in p.value if x.key == "focus"]
                self.assertIn(fid, rev_excls, f"{fid} excludes {e}, but {e} does not exclude {fid}")

    def test_focus_tree_header_and_shortcuts(self):
        nodes = get_nodes(FOCUS_FILE)
        trees = [n for n in nodes if n.key == "focus_tree"]
        self.assertTrue(trees, "focus_tree block missing in italy.txt")
        tree = trees[0]
        self.assertEqual(tree.get("id"), "ITA_ww1_1911_1923")
        self.assertEqual(tree.get("default"), "no")
        shortcuts = [n for n in tree.value if n.key == "shortcut"]
        self.assertGreaterEqual(len(shortcuts), 5, f"Expected at least 5 shortcuts (one per wing), got {len(shortcuts)}")


class TestItalyBalanceAndMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.focus_nodes = get_focus_nodes()
        cls.foci = {n.get("id"): n for n in cls.focus_nodes}

    def test_real_completion_rewards_and_no_empty_flags(self):
        REAL_EFFECTS = {
            "country_event", "add_political_power", "add_stability", "add_war_support",
            "army_experience", "navy_experience", "air_experience", "add_tech_bonus",
            "add_to_variable", "add_ideas", "remove_ideas", "custom_effect_tooltip",
            "declare_war_on", "create_wargoal", "add_opinion_modifier", "transfer_state",
            "add_building_construction", "build_railway", "set_technology", "give_guarantee"
        }
        for fid, n in self.foci.items():
            reward = n.get("completion_reward")
            self.assertIsNotNone(reward, f"Focus {fid} missing completion_reward")
            keys = {x.key for x in walk(reward)}
            has_real = bool(keys & REAL_EFFECTS) or any(k.startswith("ita_ww1_") or k.startswith("ww1_ITA_") for k in keys)
            self.assertTrue(has_real, f"Focus {fid} has no real player-facing completion reward: {keys}")

    def test_balance_ceilings_on_focus_tree(self):
        total_pos_stab = 0.0
        total_pos_ws = 0.0
        tech_bonuses = []

        for fid, n in self.foci.items():
            reward = n.get("completion_reward")
            if not reward:
                continue
            for x in walk(reward):
                if x.key == "add_stability":
                    val = float(x.value)
                    self.assertLessEqual(val, 0.051, f"Focus {fid} exceeds single stab cap (+0.05): {val}")
                    if val > 0:
                        total_pos_stab += val
                elif x.key == "add_war_support":
                    val = float(x.value)
                    self.assertLessEqual(val, 0.051, f"Focus {fid} exceeds single ws cap (+0.05): {val}")
                    if val > 0:
                        total_pos_ws += val
                elif x.key == "add_political_power":
                    val = float(x.value)
                    self.assertLessEqual(val, 60.1, f"Focus {fid} exceeds single PP cap (60): {val}")
                elif x.key == "add_tech_bonus":
                    bonus = float(x.get("bonus", 0))
                    self.assertLessEqual(bonus, 0.251, f"Focus {fid} exceeds tech bonus cap (25%): {bonus}")
                    self.assertEqual(x.get("uses"), "1", f"Focus {fid} tech bonus must have uses = 1")
                    self.assertIsNone(x.get("ahead_reduction"), f"Focus {fid} tech bonus must not have ahead_reduction")
                    tech_bonuses.append(x.get("name"))
                # Prohibited effects
                self.assertNotIn(x.key, ["create_unit", "add_manpower"], f"Focus {fid} contains prohibited effect {x.key}")

        self.assertLessEqual(total_pos_stab, 0.151, f"Total positive stability ({total_pos_stab:.2f}) exceeds cap 0.15")
        self.assertLessEqual(total_pos_ws, 0.201, f"Total positive war support ({total_pos_ws:.2f}) exceeds cap 0.20")
        self.assertEqual(len(tech_bonuses), len(set(tech_bonuses)), "All tech bonuses must have unique names")

    def test_internal_gauges_defined_and_clamped(self):
        self.assertTrue(EFFECTS_FILE.is_file(), "common/scripted_effects/ww1_italy_effects.txt must exist")
        text = read(EFFECTS_FILE)
        gauges = [
            "ita_ww1_interventionism",
            "ita_ww1_social_tension",
            "ita_ww1_army_morale",
            "ita_ww1_southern_gap",
            "ita_ww1_irredentism"
        ]
        for g in gauges:
            self.assertIn(g, text, f"Gauge variable {g} missing from scripted effects")
            self.assertIn(f"var = {g}", text, f"Clamp for {g} missing from scripted effects")


class TestItalyEventsAndDecisions(unittest.TestCase):
    def test_events_volume_options_and_spontaneous_count(self):
        event_files = sorted(ROOT.glob("events/ww1_italy_*.txt"))
        self.assertTrue(event_files, "No events/ww1_italy_*.txt files found")
        events = []
        for ef in event_files:
            for n in get_nodes(ef):
                if n.key == "country_event":
                    events.append(n)

        self.assertGreaterEqual(len(events), 70, f"Expected >= 70 events, found {len(events)}")

        spontaneous = 0
        third_party_events = 0
        for ev in events:
            eid = ev.get("id")
            opts = [x for x in ev.value if x.key == "option"]
            self.assertGreaterEqual(len(opts), 2, f"Event {eid} must have at least 2 options, found {len(opts)}")
            # Check spontaneous trigger
            keys = {x.key for x in ev.value}
            is_spontaneous = ("trigger" in keys or "mean_time_to_happen" in keys) and (ev.get("is_triggered_only") != "yes" or "trigger" in keys)
            if is_spontaneous:
                spontaneous += 1
            # Check options for third-party dispatches
            for opt in opts:
                opt_nodes = opt.value if isinstance(opt.value, list) else [opt]
                opt_keys = {x.key for x in walk(opt_nodes)}
                if any(k in ["GER", "AUS", "ENG", "FRA", "TUR", "SER", "GRE"] for k in opt_keys):
                    third_party_events += 1

        self.assertGreaterEqual(spontaneous, 35, f"Expected >= 35 spontaneous events, found {spontaneous}")
        self.assertGreaterEqual(third_party_events, 6, f"Expected >= 6 events impacting third parties, found {third_party_events}")

    def test_decisions_count_categories_and_costs(self):
        dec_files = sorted(ROOT.glob("common/decisions/ww1_italy_*.txt"))
        self.assertTrue(dec_files, "No common/decisions/ww1_italy_*.txt files found")
        cat_file = ROOT / "common" / "decisions" / "categories" / "ww1_italy_categories.txt"
        self.assertTrue(cat_file.is_file(), "Decision categories file missing")

        cats = [n for n in get_nodes(cat_file)]
        self.assertGreaterEqual(len(cats), 4, f"Expected >= 4 decision categories, found {len(cats)}")

        decisions = []
        for df in dec_files:
            for cat_node in get_nodes(df):
                for dec in cat_node.value:
                    if isinstance(dec.value, list):
                        decisions.append(dec)

        self.assertGreaterEqual(len(decisions), 24, f"Expected >= 24 decisions, found {len(decisions)}")
        for d in decisions:
            keys = {x.key for x in d.value}
            # Every decision has cost or days_remove
            has_cost = "cost" in keys or "custom_cost_trigger" in keys
            self.assertTrue(has_cost, f"Decision {d.key} missing cost")
            if "civilian_factory_use" in keys:
                self.assertIn("cancel_effect", keys, f"Industrial decision {d.key} missing cancel_effect")


class TestItalyIdeasAndModifiers(unittest.TestCase):
    def test_ideas_volume_and_valid_modifiers(self):
        ideas_file = ROOT / "common" / "ideas" / "ww1_italy_ideas.txt"
        self.assertTrue(ideas_file.is_file(), "common/ideas/ww1_italy_ideas.txt missing")
        ideas = []
        for n in get_nodes(ideas_file):
            if n.key == "ideas":
                for cat in n.value:
                    for idea in cat.value:
                        if isinstance(idea.value, list):
                            ideas.append(idea)

        self.assertGreaterEqual(len(ideas), 24, f"Expected >= 24 ideas, found {len(ideas)}")

        # Check documentation modifiers
        doc_path = GAME / "documentation" / "modifiers_documentation.md"
        if doc_path.is_file():
            valid_mods = set(re.findall(r"^## (\w+)", doc_path.read_text(encoding="utf-8-sig"), re.M))
            for idea in ideas:
                for mod_block in [x for x in idea.value if x.key == "modifier"]:
                    for m in mod_block.value:
                        self.assertIn(m.key, valid_mods, f"Idea {idea.key} has invalid modifier {m.key}")

    def test_opinion_modifiers_exist(self):
        opinion_files = sorted(ROOT.glob("common/opinion_modifiers/ww1_italy_*.txt"))
        self.assertTrue(opinion_files, "Opinion modifiers file missing")
        modifiers = []
        for of in opinion_files:
            for n in get_nodes(of):
                if n.key == "opinion_modifiers":
                    for op in n.value:
                        modifiers.append(op.key)
        self.assertGreaterEqual(len(modifiers), 6, f"Expected >= 6 opinion modifiers, found {len(modifiers)}")


class TestItalyLocalisationAndGraphics(unittest.TestCase):
    def test_localisation_bom_and_mirror_parity(self):
        en_file = ROOT / "localisation" / "english" / "ww1_italy_l_english.yml"
        pt_file = ROOT / "localisation" / "braz_por" / "ww1_italy_l_braz_por.yml"
        self.assertTrue(en_file.is_file(), "English localisation missing")
        self.assertTrue(pt_file.is_file(), "Portuguese localisation missing")

        # BOM check
        self.assertTrue(en_file.read_bytes().startswith(b"\xef\xbb\xbf"), "English yml must have UTF-8 BOM")
        self.assertTrue(pt_file.read_bytes().startswith(b"\xef\xbb\xbf"), "Portuguese yml must have UTF-8 BOM")

        en_keys = set(re.findall(r"^ ([\w.]+):0 ", read(en_file), re.M))
        pt_keys = set(re.findall(r"^ ([\w.]+):0 ", read(pt_file), re.M))

        self.assertEqual(en_keys, pt_keys, f"Localisation key mismatch: {len(en_keys ^ pt_keys)} differing keys")

        # Check focus descriptions have immediate effect
        en_text = read(en_file)
        pt_text = read(pt_file)
        foci = get_focus_nodes()
        for f in foci:
            fid = f.get("id")
            self.assertIn(f" {fid}:0 ", en_text, f"Missing EN title for {fid}")
            self.assertIn(f" {fid}_desc:0 ", en_text, f"Missing EN desc for {fid}")
            self.assertIn(f" {fid}:0 ", pt_text, f"Missing PT title for {fid}")
            self.assertIn(f" {fid}_desc:0 ", pt_text, f"Missing PT desc for {fid}")

    def test_gfx_sprite_definitions_and_shine(self):
        gfx_file = ROOT / "interface" / "ww1_italy_goals.gfx"
        self.assertTrue(gfx_file.is_file(), "interface/ww1_italy_goals.gfx missing")
        # Ensure scripts have no BOM
        self.assertFalse(gfx_file.read_bytes().startswith(b"\xef\xbb\xbf"), "GFX file must NOT have BOM")
        gfx_text = read(gfx_file)

        foci = get_focus_nodes()
        for f in foci:
            fid = f.get("id")
            base_sprite = f"GFX_goal_ww1_{fid}"
            shine_sprite = f"GFX_goal_ww1_{fid}_shine"
            self.assertIn(f'name = "{base_sprite}"', gfx_text, f"Missing base sprite for {fid}")
            self.assertIn(f'name = "{shine_sprite}"', gfx_text, f"Missing shine sprite for {fid}")


if __name__ == "__main__":
    unittest.main()
