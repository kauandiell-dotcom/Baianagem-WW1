"""Contratos de estrutura da Alemanha e da Russia (arvores reorganizadas + conteudo novo).

Checam sintaxe, referencias, textos EN/PT-BR, arte unica e calendario. NAO provam equilibrio, IA nem o
comportamento dentro do jogo.
"""
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import focus_layout as fl
import relayout_tabbed_tree as rt
from PIL import Image

GAME = Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV")


def rd(rel):
    return (ROOT / rel).read_bytes().decode("utf-8-sig")


def nocomment(t):
    return re.sub(r"#[^\n]*", "", t)


def tree(name):
    t = rd("common/national_focus/%s.txt" % name)
    nodes, spans = rt.parse(t)
    rt.resolve_absolute(nodes)
    return t, nodes, spans


def balanced(t):
    d = 0
    for c in nocomment(t):
        d += (c == "{") - (c == "}")
        if d < 0:
            return False
    return d == 0


def loc_keys(lang):
    keys = set()
    for p in (ROOT / "localisation").rglob("*.yml"):
        if ("l_" + lang) in p.name:
            for line in p.read_bytes().decode("utf-8-sig", "replace").split("\n"):
                m = re.match(r"\s*([^\s:#][^\s:]*):\d*\s+\"", line)
                if m:
                    keys.add(m.group(1))
    return keys


EN, PT = loc_keys("english"), loc_keys("braz_por")
NEW_FILES = ["events/ww1_ger_rus_rework_events.txt", "common/ideas/ww1_ger_rus_rework_ideas.txt",
             "common/decisions/ww1_ger_rus_rework_decisions.txt", "common/decisions/categories/ww1_ger_rus_rework_categories.txt",
             "common/scripted_effects/ww1_ger_rus_rework_effects.txt", "common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt"]


class Trees(unittest.TestCase):
    EXPECT = {"germany": (245, 7, "GER_ww1_shortcut_"), "soviet": (235, 6, "SOV_ww1_shortcut_")}

    def test_focus_counts_and_integrity(self):
        for name, (count, wings, _) in self.EXPECT.items():
            t, nodes, _ = tree(name)
            ids = [n["id"] for n in nodes]
            self.assertEqual(len(ids), count, name)
            self.assertEqual(len(set(ids)), count, name)
            s = set(ids)
            for n in nodes:
                for g in n["groups"]:
                    for p in g:
                        self.assertIn(p, s, (n["id"], p))
                for x in n["excl"]:
                    self.assertIn(x, s, (n["id"], x))
            self.assertTrue(balanced(t), name)

    def test_layout_is_organised(self):
        for name in self.EXPECT:
            _, nodes, _ = tree(name)
            ln = rt.to_layout_nodes(nodes)
            pos = {n["id"]: (n["x"], n["y"]) for n in ln}
            self.assertEqual(len(pos), len(set(pos.values())), name + " tem focos sobrepostos")
            for n in ln:
                for p in n["parents"] + n["also"]:
                    self.assertLess(pos[p][1], pos[n["id"]][1], (name, p, n["id"]))
            rows = fl.report(ln, pos)
            self.assertLessEqual(max(r["longest_straight"] for r in rows), 4, name)
            self.assertLessEqual(max(y for _, y in pos.values()), 26, name)
            self.assertLessEqual(max(r["crossings"] for r in rows), 3, name)

    def test_header_shortcuts_and_texts(self):
        for name, (_, wings, prefix) in self.EXPECT.items():
            t, nodes, _ = tree(name)
            head = t[:t.find("focus = {")]
            self.assertIn("initial_show_position", head)
            ids = {n["id"] for n in nodes}
            blocks = re.findall(r"shortcut\s*=\s*\{\s*name\s*=\s*(\S+)\s*target\s*=\s*(\S+)", head)
            self.assertEqual(len(blocks), wings, name)
            for key, target in blocks:
                self.assertIn(target, ids)
                self.assertIn(key, EN)
                self.assertIn(key, PT)
                self.assertTrue(key.startswith(prefix))

    def test_no_invalid_filters_and_every_focus_has_one(self):
        for name in self.EXPECT:
            t, nodes, spans = tree(name)
            for bad in ("FOCUS_FILTER_ARMY ", "FOCUS_FILTER_NAVY ", "FOCUS_FILTER_AIRFORCE "):
                self.assertNotIn(bad, t)
            for n, (s, e) in zip(nodes, spans):
                self.assertRegex(t[s:e], r"search_filters\s*=\s*\{\s*FOCUS_FILTER_", n["id"])
        self.assertNotRegex(rd("common/national_focus/uk.txt"), r"FOCUS_FILTER_(ARMY|NAVY|AIRFORCE)\s")

    def test_focus_icons_are_unique_and_defined(self):
        gfx = rd("interface/ww1_germany_focus_art.gfx")
        for name in self.EXPECT:
            t, nodes, spans = tree(name)
            icons = []
            for n, (s, e) in zip(nodes, spans):
                icons.append(re.search(r"(?m)^\s*icon\s*=\s*(\S+)", t[s:e]).group(1))
            dup = [k for k, v in Counter(icons).items() if v > 1]
            self.assertEqual(dup, [], name)
        import json
        rec = json.loads(rd("docs/germany_focus_art_bindings.json"))
        self.assertGreaterEqual(len(rec), 70)
        self.assertEqual(len({r["source_sha256"] for r in rec}), len(rec))
        for r in rec:
            self.assertIn('name = "%s"' % r["sprite"], gfx)
            self.assertIn('name = "%s_shine"' % r["sprite"], gfx)
            self.assertTrue((ROOT / r["texture"]).is_file(), r["texture"])

    def test_russian_events_patch_is_well_formed(self):
        t = rd("events/ww1_russia_events.txt")
        self.assertTrue(t.startswith("add_namespace = ww1_russia"))
        self.assertTrue(balanced(t))
        for flag in ("SOV_path_bolshevik", "SOV_path_kornilov", "SOV_path_democratic"):
            self.assertIn(flag, t)
        self.assertIn("ww1_russia.20.c", EN)
        self.assertIn("ww1_russia.20.c", PT)

    def test_every_focus_has_ai_weight_in_russia(self):
        t, nodes, spans = tree("soviet")
        for n, (s, e) in zip(nodes, spans):
            self.assertIn("ai_will_do", t[s:e], n["id"])

    def test_historical_date_gates(self):
        t, nodes, spans = tree("germany")
        blk = {n["id"]: t[s:e] for n, (s, e) in zip(nodes, spans)}
        for fid, date in (("GER_treaty_of_brest_litovsk", "1917.11.30"), ("GER_operation_michael_st_quentin", "1918.2.1"),
                          ("GER_kiel_sailors_mutiny", "1918.10.1"), ("GER_battle_of_verdun_attrition", "1916.1.1")):
            self.assertIn("date > " + date, blk[fid], fid)
        self.assertIn("GER_republic_proclaimed", blk["GER_kaiser_abdication_amerongen"])
        t, nodes, spans = tree("soviet")
        blk = {n["id"]: t[s:e] for n, (s, e) in zip(nodes, spans)}
        for fid in ("SOV_february_bread_riots_1917", "SOV_mutiny_of_petrograd_garrison", "SOV_abdication_at_pskov"):
            self.assertIn("SOV_revolution_window_open", blk[fid], fid)
            self.assertIn("bypass", blk[fid], fid)

    def test_russian_regimes_are_exclusive(self):
        _, nodes, _ = tree("soviet")
        by = {n["id"]: n for n in nodes}
        roots = ["SOV_all_power_to_the_soviets", "SOV_kornilov_iron_dictatorship", "SOV_convene_constituent_assembly"]
        for r in roots:
            self.assertEqual(set(by[r]["excl"]), set(roots) - {r}, r)


class Content(unittest.TestCase):
    def setUp(self):
        self.ev = rd("events/ww1_ger_rus_rework_events.txt")

    def test_new_files_balanced_and_without_bom(self):
        for rel in NEW_FILES:
            raw = (ROOT / rel).read_bytes()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"), rel)
            self.assertTrue(balanced(raw.decode("utf-8")), rel)

    def test_events_unique_localised_and_illustrated(self):
        ids = re.findall(r"(?m)^\tid = (\S+)", self.ev)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 60)
        sprites = dict(re.findall(r'name = "(GFX_event_WW1_\w+)" texturefile = "([^"]+)"', rd("interface/ww1_ger_rus_rework_assets.gfx")))
        pics = re.findall(r"(?m)^\tpicture = (\S+)", self.ev)
        for p in pics:
            self.assertIn(p, sprites, p)
            self.assertTrue((ROOT / sprites[p]).is_file(), p)
            self.assertEqual(Image.open(ROOT / sprites[p]).size, (450, 250))
        self.assertEqual(len(set(sprites)), len(sprites))
        for i in ids:
            for suf in (".t", ".d"):
                self.assertIn(i + suf, EN, i)
                self.assertIn(i + suf, PT, i)
        for m in re.finditer(r"name = (ww1_\w+\.\d+\.[a-f])", self.ev):
            self.assertIn(m.group(1), EN)
            self.assertIn(m.group(1), PT)

    def test_event_pictures_are_not_reused_between_events(self):
        pics = re.findall(r"(?m)^\tpicture = (\S+)", self.ev)
        self.assertEqual(len(pics), len(set(pics)))

    def test_art_has_provenance_and_no_duplicate_pixels(self):
        import json
        rec = json.loads(rd("docs/ger_rus_art_bindings.json"))
        self.assertGreaterEqual(len(rec), 60)
        self.assertEqual(len({r["source_sha256"] for r in rec}), len(rec))
        for r in rec:
            self.assertTrue(r["donor_id"] and r["source_relative"])

    def test_every_event_reference_resolves(self):
        all_ids = set()
        for p in (ROOT / "events").rglob("*.txt"):
            all_ids.update(re.findall(r"\bid\s*=\s*([\w]+\.\d+)\s+(?:title|desc)\s*=", p.read_bytes().decode("utf-8-sig", "replace")))
        refs = set()
        for rel in NEW_FILES + ["common/national_focus/germany.txt", "common/national_focus/soviet.txt"]:
            refs.update(re.findall(r"country_event\s*=\s*\{\s*id\s*=\s*([\w\.]+)", nocomment(rd(rel))))
        for r in refs:
            self.assertIn(r, all_ids, r)

    def test_ideas_exist_and_have_valid_modifiers(self):
        defined = set()
        for p in (ROOT / "common/ideas").rglob("*.txt"):
            defined.update(re.findall(r"(?m)^\t\t([A-Za-z_]\w*)\s*=\s*\{", p.read_bytes().decode("utf-8-sig", "replace")))
        used = set()
        for rel in NEW_FILES:
            t = nocomment(rd(rel))
            used.update(re.findall(r"(?:add_ideas|remove_ideas|has_idea)\s*=\s*(\w+)", t))
            used.update(re.findall(r"add_timed_idea\s*=\s*\{\s*idea\s*=\s*(\w+)", t))
        for i in used:
            self.assertIn(i, defined, i)
        doc = (GAME / "documentation/modifiers_documentation.md").read_text(encoding="utf-8", errors="replace")
        ideas = nocomment(rd("common/ideas/ww1_ger_rus_rework_ideas.txt"))
        for mod in set(re.findall(r"(?m)^\t\t\t\t(\w+)\s*=", ideas)):
            self.assertRegex(doc, r"(?m)^#?\s*\**" + re.escape(mod) + r"\b|\b" + re.escape(mod) + r"\b", mod)
        for idea in re.findall(r"(?m)^\t\t(\w+) = \{", ideas):
            self.assertIn(idea, EN)
            self.assertIn(idea + "_desc", PT)
            self.assertRegex(ideas, r"picture = \w+")

    def test_decisions_categories_and_texts(self):
        cats = set(re.findall(r"(?m)^(\w+) = \{", rd("common/decisions/categories/ww1_ger_rus_rework_categories.txt")))
        dec = rd("common/decisions/ww1_ger_rus_rework_decisions.txt")
        top = set(re.findall(r"(?m)^(\w+) = \{", dec))
        self.assertEqual(top, cats)
        names = re.findall(r"(?m)^\t(\w+_dec_\w+) = \{", dec)
        self.assertGreaterEqual(len(names), 20)
        for n in names:
            for k in (n, n + "_desc"):
                self.assertIn(k, EN)
                self.assertIn(k, PT)
        for c in cats:
            self.assertIn(c, EN)
            self.assertIn(c, PT)

    def test_flags_read_are_set_somewhere(self):
        texts = ""
        for sub in ("common", "events", "history"):
            for p in (ROOT / sub).rglob("*.txt"):
                texts += nocomment(p.read_bytes().decode("utf-8-sig", "replace"))
        for flag in ("SOV_path_bolshevik", "SOV_path_kornilov", "SOV_path_democratic", "SOV_path_tsarist",
                     "SOV_revolution_window_open", "SOV_provisional_gov_in_power", "SOV_tsar_abdicated",
                     "GER_republic_proclaimed", "GER_kiel_mutiny_underway", "GER_kaiser_abdicated", "SOV_rasputin_dead"):
            self.assertRegex(texts, r"set_country_flag\s*=\s*(\{\s*flag\s*=\s*)?" + flag + r"\b", flag)

    def test_released_nations_exist(self):
        for tag in ("FIN", "UKR", "EST", "LAT", "LIT", "GEO", "ARM", "AZR", "POL"):
            self.assertTrue(list((ROOT / "history/countries").glob(tag + " - *.txt")), tag)

    def test_russian_revolution_chain_and_civil_war_are_wired(self):
        eff = rd("common/scripted_effects/ww1_ger_rus_rework_effects.txt")
        for eid in (210, 211, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 230, 231, 232, 233, 234):
            self.assertIn("ww1_russia.%d" % eid, self.ev + eff + rd("common/national_focus/soviet.txt"), eid)
        self.assertIn("start_civil_war", self.ev)
        self.assertIn("release = FIN", self.ev)
        self.assertIn("ww1_germany_events.214", eff)

    def test_no_free_divisions_or_manpower_in_new_content(self):
        for rel in NEW_FILES:
            t = nocomment(rd(rel))
            self.assertNotIn("create_unit", t)
            self.assertNotIn("add_manpower", t)
            self.assertNotIn("add_equipment_to_stockpile", t)

    def test_loc_files_have_bom_and_parity(self):
        a = ROOT / "localisation/english/ww1_ger_rus_rework_l_english.yml"
        b = ROOT / "localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml"
        for p in (a, b):
            self.assertTrue(p.read_bytes().startswith(b"\xef\xbb\xbf"))
        ka = re.findall(r"(?m)^ (\S+):0 ", a.read_bytes().decode("utf-8-sig"))
        kb = re.findall(r"(?m)^ (\S+):0 ", b.read_bytes().decode("utf-8-sig"))
        self.assertEqual(ka, kb)
        self.assertEqual(len(ka), len(set(ka)))

    def test_starting_popularities_have_opposition(self):
        for fn in ("GER - Germany.txt", "SOV - Soviet union.txt"):
            t = nocomment(rd("history/countries/" + fn))
            m = re.search(r"set_popularities\s*=\s*\{([^}]*)\}", t)
            self.assertIsNotNone(m, fn)
            vals = [int(v) for v in re.findall(r"=\s*(\d+)", m.group(1))]
            self.assertEqual(sum(vals), 100)
            self.assertGreaterEqual(len(vals), 4)


if __name__ == "__main__":
    unittest.main()
