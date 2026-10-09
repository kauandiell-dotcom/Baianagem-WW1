"""Static checks for the UK extra content (events ww1_britain_x, decisions, timed institutions, replacement focus art).

They prove references, localisation, art registration and small-number rules. They do NOT prove balance,
AI behaviour or in-game rendering.
"""
import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = Path(r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV")
sys.path.insert(0, str(ROOT / "scripts"))
import build_ww1_britain_extra as X  # noqa: E402


def text(p):
    return (ROOT / p).read_text(encoding="utf-8-sig")


def keys(p):
    return dict(re.findall(r'^ ([\w.]+):0 "(.*)"$', text(p), re.M))


FOCUS = text("common/national_focus/uk.txt")
EVENTS = text("events/ww1_britain_extra_events.txt")
DECISIONS = text("common/decisions/ww1_britain_extra_decisions.txt")
IDEAS = text("common/ideas/ww1_britain_extra_ideas.txt")
EN = keys("localisation/english/ww1_britain_extra_l_english.yml")
PT = keys("localisation/braz_por/ww1_britain_extra_l_braz_por.yml")
SPRITES = {}
for name, tex in re.findall(r'name = "([^"]+)" texturefile = "([^"]+)"', text("interface/ww1_britain_extra_assets.gfx")):
    SPRITES[name] = tex


class BritainExtraContent(unittest.TestCase):
    def test_generated_files_are_current_and_balanced(self):
        self.assertEqual(EVENTS, X.build_events())
        self.assertEqual(DECISIONS, X.build_decisions())
        self.assertEqual(IDEAS, X.build_ideas())
        for t in (EVENTS, DECISIONS, IDEAS):
            self.assertEqual(t.count("{"), t.count("}"))

    def test_counts(self):
        self.assertEqual((len(X.EVENTS), len(X.DECISIONS), len(X.IDEAS)), (10, 17, 5))

    def test_localisation_parity_and_bom(self):
        self.assertEqual(set(EN), set(PT))
        for lang in ("english", "braz_por"):
            self.assertTrue((ROOT / f"localisation/{lang}/ww1_britain_extra_l_{lang}.yml").read_bytes().startswith(b"\xef\xbb\xbf"))
        for k, v in list(EN.items()) + list(PT.items()):
            self.assertNotIn('"', v)
            self.assertTrue(v.strip(), k)

    def test_new_keys_do_not_collide_with_other_localisation_files(self):
        for path in (ROOT / "localisation").rglob("*.yml"):
            if "ww1_britain_extra" in path.name:
                continue
            other = set(re.findall(r'^ ([\w.]+):\d+ ', path.read_text(encoding="utf-8-sig"), re.M))
            self.assertFalse(other & set(EN), (path.name, sorted(other & set(EN))[:3]))

    def test_every_event_is_dated_localised_and_has_ai_for_each_option(self):
        for n in range(1, len(X.EVENTS) + 1):
            eid = f"ww1_britain_x.{n}"
            for suffix in ("t", "d", "a", "b", "c"):
                self.assertIn(f"{eid}.{suffix}", EN, eid)
        for ev in re.finditer(r"country_event = \{(.*?)\n\}\n", EVENTS, re.S):
            body = ev.group(1)
            self.assertIn("date >", body)
            self.assertIn("date <", body)
            self.assertIn("fire_only_once = yes", body)
            self.assertEqual(body.count(" option = {"), 3)
            self.assertEqual(body.count("ai_chance"), 3)

    def test_event_pictures_registered_unique_and_right_size(self):
        from PIL import Image
        pics = re.findall(r"picture = (GFX_event_ww1_britain_x_\w+)", EVENTS)
        self.assertEqual(len(pics), len(set(pics)))
        hashes = set()
        for p in pics:
            tex = ROOT / SPRITES[p]
            self.assertTrue(tex.is_file(), p)
            im = Image.open(tex)
            self.assertEqual(im.size, (210, 176))
            hashes.add(hashlib.sha256(im.convert("RGBA").tobytes()).hexdigest())
        self.assertEqual(len(hashes), len(pics))

    def test_every_decision_is_unlocked_by_a_flag_a_focus_sets(self):
        for (key, cat, flag, *_rest) in X.DECISIONS:
            self.assertRegex(FOCUS, r"set_country_flag = " + re.escape(flag) + r"\b", key)
            self.assertIn(f"has_country_flag = {flag}", DECISIONS)
            self.assertIn(cat, ("ENG_ww1_services_policy", "ENG_ww1_empire_policy"))
            self.assertIn(f"ENG_ww1_x_{key}", EN)
            self.assertIn(f"ENG_ww1_x_{key}_desc", EN)

    def test_decision_icons_and_idea_pictures_exist_and_are_unique(self):
        from PIL import Image
        seen = set()
        for key in [d[0] for d in X.DECISIONS]:
            s = f"GFX_decision_ENG_ww1_x_{key}"
            self.assertIn(f"icon = {s}", DECISIONS)
            tex = ROOT / SPRITES[s]
            self.assertEqual(Image.open(tex).size, (64, 64))
            seen.add(hashlib.sha256(Image.open(tex).convert("RGBA").tobytes()).hexdigest())
        for key in X.IDEAS:
            s = f"GFX_idea_ENG_ww1_x_{key}"
            tex = ROOT / SPRITES[s]
            self.assertEqual(Image.open(tex).size, (64, 64))
            seen.add(hashlib.sha256(Image.open(tex).convert("RGBA").tobytes()).hexdigest())
        self.assertEqual(len(seen), len(X.DECISIONS) + len(X.IDEAS))

    def test_timed_ideas_used_by_decisions_exist_and_use_documented_modifiers(self):
        used = set(re.findall(r"idea = (ENG_ww1_x_\w+)", DECISIONS))
        defined = set(re.findall(r"^\s*(ENG_ww1_x_\w+) = \{ picture", IDEAS, re.M))
        self.assertEqual(used, defined)
        doc = (GAME / "documentation/modifiers_documentation.md").read_text(encoding="utf-8")
        for mod in re.findall(r"modifier = \{([^}]*)\}", IDEAS):
            for name in re.findall(r"(\w+)\s*=", mod):
                self.assertIn(name, doc, name)

    def test_no_free_units_equipment_or_manpower_and_small_numbers(self):
        content = EVENTS + DECISIONS
        for banned in ("add_equipment_to_stockpile", "create_unit", "add_manpower", "declare_war_on", "annex_country", "add_units_to_division_template"):
            self.assertNotIn(banned, content, banned)
        for tokens_src in [o[2] for e in X.EVENTS for o in e[7]] + [d[9] for d in X.DECISIONS]:
            for tok in tokens_src.split():
                k, _, a = tok.partition(":")
                if k == "stab":
                    self.assertLessEqual(abs(float(a)), 0.02, tok)
                elif k == "ws":
                    self.assertLessEqual(abs(float(a)), 0.02, tok)
                elif k == "pp":
                    self.assertLessEqual(abs(float(a)), 25, tok)
                elif k in ("axp", "nxp", "fxp"):
                    self.assertLessEqual(float(a), 6, tok)
                elif k in X.V:
                    self.assertLessEqual(abs(float(a)), 6, tok)
                elif k == "idea":
                    self.assertLessEqual(int(a.split(":")[1]), 240, tok)

    def test_every_benefit_in_an_event_option_has_a_cost(self):
        # every option either spends political power/variables/stability/war support or gives up a variable
        for e in X.EVENTS:
            for (_en, _pt, tokens, _ai) in e[7]:
                costly = any(t.split(":")[0] in ("pp", "stab", "ws", "lab", "debt", "irish", "ulster", "dom") and float(t.split(":")[1]) != 0 for t in tokens.split())
                self.assertTrue(costly, tokens)
        for d in X.DECISIONS:
            self.assertGreaterEqual(d[4], 25)  # political power cost


class ReplacementFocusArt(unittest.TestCase):
    def test_no_two_focus_icons_share_a_file_or_pixels(self):
        from PIL import Image
        seen_bytes, seen_px = {}, {}
        for m in re.finditer(r"icon = (GFX_goal_ww1_ENG_ww1_\w+)", FOCUS):
            s = m.group(1)
            sprites = text("interface/ww1_britain_art.gfx") + text("interface/ww1_britain_goals.gfx")
            path = re.search(r'name\s*=\s*"' + s + r'"\s*texturefile\s*=\s*"([^"]+)"', sprites)
            self.assertTrue(path, s)
            p = ROOT / path.group(1)
            b = hashlib.sha256(p.read_bytes()).hexdigest()
            px = hashlib.sha256(Image.open(p).convert("RGBA").tobytes()).hexdigest()
            self.assertNotIn(b, seen_bytes, (s, seen_bytes.get(b)))
            self.assertNotIn(px, seen_px, (s, seen_px.get(px)))
            seen_bytes[b], seen_px[px] = s, s
        self.assertEqual(len(seen_bytes), 200)

    def test_bindings_record_provenance_for_every_new_image(self):
        rec = json.loads(text("docs/britain_extra_art_bindings.json"))
        self.assertEqual(len(rec), 10 + 5 + 17 + 7)
        for r in rec:
            self.assertTrue(r["donor_id"] and r["source_relative"] and r["source_sha256"], r["id"])
            self.assertTrue((ROOT / r["texture"]).is_file(), r["id"])
        self.assertEqual(len({r["source_sha256"] for r in rec}), len(rec))


if __name__ == "__main__":
    unittest.main()
