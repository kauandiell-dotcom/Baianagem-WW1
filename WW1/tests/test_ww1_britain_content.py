"""Static checks for generated UK content (wings 1-5: politics, economy, diplomacy, navy/aviation, army/operations).

Run from WW1/:  python -B -X utf8 -m unittest tests.test_ww1_britain_content
They prove references, localisation, art registration and safety rules. They do NOT prove
balance, AI behaviour or in-game rendering.
"""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = Path(r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV")
sys.path.insert(0, str(ROOT / "scripts"))
WINGS = ("politics", "economy", "diplomacy", "navy", "army")


def text(p):
    return (ROOT / p).read_text(encoding="utf-8-sig")


def keys(p):
    return dict(re.findall(r'^ ([\w.]+):0 "(.*)"$', text(p), re.M))


FOCUS = text("common/national_focus/uk.txt")
OWN_EVENTS = "\n".join(text(f"events/ww1_britain_{w}_events.txt") for w in WINGS)
EVENTS = OWN_EVENTS + text("events/ww1_britain_policy_events.txt")
IDEAS_NEW = "\n".join(text(f"common/ideas/ww1_britain_{w}_ideas.txt") for w in WINGS)
IDEAS_OLD = text("common/ideas/ww1_britain_ideas.txt")
DECISIONS = "\n".join(text(f"common/decisions/ww1_britain_{w}_decisions.txt") for w in WINGS)
CATEGORIES = text("common/decisions/categories/ww1_britain_politics_categories.txt")
ADMIN = text("common/scripted_effects/ww1_britain_administration.txt")
EN = {}
PT = {}
for w in WINGS:
    EN.update(keys(f"localisation/replace/zz_ww1_britain_{w}_l_english.yml"))
    PT.update(keys(f"localisation/replace/zz_ww1_britain_{w}_l_braz_por.yml"))
SPRITES = {}
for gfx in (ROOT / "interface").glob("*.gfx"):
    for name, tex in re.findall(r'name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', gfx.read_text(encoding="utf-8-sig", errors="ignore")):
        SPRITES[name] = tex
# multi-line sprite definitions (shine) keep the same texture
MANIFEST = json.loads(text("docs/britain_art_manifest.json"))


def block(t, fid):
    m = re.search(r"(?m)^ focus = \{\r?\n  id = " + re.escape(fid) + r"\r?\n", t)
    depth, i = 1, m.end()
    while depth:
        depth += (t[i] == "{") - (t[i] == "}")
        i += 1
    return t[m.start():i]


class BritainContent(unittest.TestCase):
    def test_braces_balance_in_generated_files(self):
        files = [f"events/ww1_britain_{w}_events.txt" for w in WINGS] + [f"common/ideas/ww1_britain_{w}_ideas.txt" for w in WINGS] \
            + [f"common/decisions/ww1_britain_{w}_decisions.txt" for w in WINGS] + ["common/national_focus/uk.txt"]
        for p in files:
            t = text(p)
            self.assertEqual(t.count("{"), t.count("}"), p)

    def test_every_called_event_exists_and_has_text(self):
        called = set(re.findall(r"id = (ww1_britain(?:_pol|_eco|_dip|_nav|_mil)?\.\d+)", FOCUS + OWN_EVENTS + DECISIONS))
        defined = set(re.findall(r"^\s*id = (ww1_britain(?:_pol|_eco|_dip|_nav|_mil)?\.\d+) title", OWN_EVENTS, re.M))
        self.assertTrue(called <= defined | set(re.findall(r"^\s*id = (ww1_britain\.\d+) title", EVENTS, re.M)), called - defined)
        for eid in defined:
            for suffix in ("t", "d", "a"):
                self.assertIn(f"{eid}.{suffix}", EN, eid)
        self.assertIn("ww1_britain.3", defined)

    def test_localisation_parity_and_no_raw_quotes(self):
        self.assertEqual(set(EN), set(PT))
        for k, v in list(EN.items()) + list(PT.items()):
            self.assertNotIn('"', v.replace('\\"', ""), k)
        for w in WINGS:
            for lang in ("english", "braz_por"):
                self.assertTrue((ROOT / f"localisation/replace/zz_ww1_britain_{w}_l_{lang}.yml").read_bytes().startswith(b"\xef\xbb\xbf"))

    def test_rewarded_focuses_have_distinct_descriptions_and_no_stub(self):
        from britain_politics_data import FOCI as F1
        from britain_economy_data import FOCI as F2
        from britain_diplomacy_data import FOCI as F3
        from britain_navy_data import FOCI as F4
        from britain_army_data import FOCI as F5
        self.assertEqual((len(F1), len(F2), len(F3), len(F4), len(F5)), (40, 39, 37, 40, 40))
        seen = set()
        for fid in list(F1) + list(F2) + list(F3) + list(F4) + list(F5):
            full = "ENG_ww1_" + fid
            self.assertIn(full + "_desc", EN)
            self.assertNotIn(EN[full + "_desc"], seen, fid)
            seen.add(EN[full + "_desc"])
            b = block(FOCUS, full)
            self.assertNotIn("_unlock_tt", b, fid)
            self.assertNotRegex(b, r"completion_reward = \{\s*set_country_flag = \w+_authorised\s*\}", fid)

    def test_added_ideas_are_defined_and_have_sprites(self):
        used = set(re.findall(r"add_ideas = (ENG_ww1_\w+)", FOCUS + OWN_EVENTS))
        new = set(re.findall(r"^\s*(ENG_ww1_\w+) = \{ picture", IDEAS_NEW, re.M))
        old = set(re.findall(r"^\s*(ENG_ww1_\w+) = \{ picture", IDEAS_OLD, re.M))
        self.assertTrue(used <= new | old, used - new - old)
        for name in new:
            self.assertIn("GFX_idea_" + name, SPRITES, name)
            self.assertIn(name, EN)
            self.assertIn(name + "_desc", EN)

    def test_idea_modifiers_exist_in_game_documentation(self):
        doc = (GAME / "documentation/modifiers_documentation.md").read_text(encoding="utf-8")
        for mod in re.findall(r"modifier = \{([^}]*)\}", IDEAS_NEW):
            for name in re.findall(r"(\w+)\s*=", mod):
                self.assertIn(name, doc, name)

    def test_variables_are_initialised_and_clamped(self):
        for v in ("ww1_britain_ulster_tension", "ww1_britain_dominion_consent"):
            self.assertIn("set_variable = { %s =" % v, ADMIN)
            self.assertIn("clamp_variable = { var = %s" % v, ADMIN)

    def test_peace_cleanup_removes_wartime_economy_ideas(self):
        for i in ("munitions_contracts", "shell_inspection", "labour_dilution", "food_control"):
            self.assertIn("remove_ideas = ENG_ww1_" + i, ADMIN)

    def test_exclusive_pair_is_symmetric(self):
        a, b = "ENG_ww1_the_labour_alternative", "ENG_ww1_the_conservative_settlement"
        self.assertIn("mutually_exclusive = { focus = %s }" % b, block(FOCUS, a))
        self.assertIn("mutually_exclusive = { focus = %s }" % a, block(FOCUS, b))

    def test_flags_consumed_are_set_somewhere(self):
        consumed = set(re.findall(r"has_country_flag = (ENG_ww1_\w+)", DECISIONS + OWN_EVENTS))
        setters = set(re.findall(r"set_country_flag = \{? ?(?:flag = )?(ENG_ww1_\w+)", FOCUS + OWN_EVENTS))
        setters |= {"ENG_ww1_consulted_" + s for s in ("canada", "australia", "new_zealand", "south_africa")}
        skip = {f for f in consumed if f.endswith(("_pending", "_cooldown", "_implemented"))}
        self.assertTrue(consumed - skip <= setters | {"ENG_ww1_military_service_authorised"}, consumed - skip - setters)

    def test_no_free_units_equipment_or_unsafe_effects(self):
        content = FOCUS + OWN_EVENTS + DECISIONS
        for banned in ("add_equipment_to_stockpile", "create_unit", "add_units_to_division_template", "declare_war_on", "annex_country"):
            self.assertNotIn(banned, content, banned)

    def test_irish_treaty_uses_existing_dominion_autonomy_level(self):
        self.assertIn("autonomy_dominion", OWN_EVENTS)
        self.assertRegex((GAME / "common/autonomous_states/dominion.txt").read_text(encoding="utf-8-sig"), r"id = autonomy_dominion")
        self.assertRegex((ROOT / "common/autonomous_states/dominion.txt").read_text(encoding="utf-8-sig"), r"id = autonomy_dominion")

    def test_ai_chances_cover_every_option(self):
        for ev in re.finditer(r"country_event = \{(.*?)\n\}\n", OWN_EVENTS, re.S):
            body = ev.group(1)
            self.assertEqual(body.count(" option = {"), body.count("ai_chance"), body[:60])

    # ---------------------------------------------------------------- GFX
    def test_every_wing12_focus_has_registered_sprite_and_texture(self):
        from britain_politics_data import FOCI as F1
        from britain_economy_data import FOCI as F2
        from britain_diplomacy_data import FOCI as F3
        from britain_navy_data import FOCI as F4
        from britain_army_data import FOCI as F5
        from PIL import Image
        for fid in list(F1) + list(F2) + list(F3) + list(F4) + list(F5):
            sprite = "GFX_goal_ww1_ENG_ww1_" + fid
            self.assertIn(sprite, SPRITES, fid)
            self.assertIn(sprite + "_shine", SPRITES, fid)
            tex = ROOT / SPRITES[sprite]
            self.assertTrue(tex.is_file(), tex)
            self.assertEqual(Image.open(tex).size, (82, 82), fid)
            self.assertIn("icon = " + sprite, block(FOCUS, "ENG_ww1_" + fid))

    def test_every_event_has_a_registered_picture_file(self):
        pics = set(re.findall(r"picture = (GFX_event_ww1_britain_\w+)", OWN_EVENTS))
        self.assertGreaterEqual(len(pics), 47)
        used = re.findall(r"picture = (GFX_event_ww1_britain_\w+)", OWN_EVENTS)
        self.assertEqual(len(used), len(set(used)), "two events share one picture")
        for p in pics:
            self.assertIn(p, SPRITES, p)
            self.assertTrue((ROOT / SPRITES[p]).is_file(), p)

    def test_decisions_and_category_have_icons(self):
        icons = set(re.findall(r"icon = (GFX_decision_\w+)", DECISIONS + CATEGORIES))
        self.assertGreaterEqual(len(icons), 10)
        for i in icons:
            self.assertIn(i, SPRITES, i)
            self.assertTrue((ROOT / SPRITES[i]).is_file(), i)

    def test_art_manifest_records_provenance_and_no_duplicates(self):
        focus = [m for m in MANIFEST if m["kind"] == "focus"]
        self.assertEqual(len(focus), 145)
        self.assertEqual(len({m["source_pixels_sha256"] for m in focus}), 145)
        for m in MANIFEST:
            if m["kind"] in ("focus", "event"):
                self.assertTrue(m["donor_id"] and m["source_relative"], m["id"])


if __name__ == "__main__":
    unittest.main()
