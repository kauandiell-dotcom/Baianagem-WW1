"""Foundation regression and validator adversarial tests (no Steam mirroring)."""
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ww1_foundation import effective_files, foundation, lua_native_keys, localisation, parse


class ParserTests(unittest.TestCase):
    def test_comments_and_escaped_string_delimiters(self):
        nodes = parse('thing={ text="A # { } \\"quote\\"" # ignored }\n value=2 }')
        self.assertEqual(nodes[0].get("value"), "2")
        self.assertIn("# { }", nodes[0].get("text"))

    def test_reports_unclosed_string_and_braces(self):
        for source in ('item={', 'item="unfinished', '}', 'item=}'): 
            with self.subTest(source=source), self.assertRaises(ValueError):
                parse(source)

    def test_native_typed_colours_and_anonymous_asset_lists(self):
        nodes = parse('color=rgb { 153 0 51 } optional_assets={ { icon="GFX_ship" } }')
        self.assertEqual(nodes[0].value[0].key, "153")
        self.assertEqual(nodes[1].value[0].get("icon"), "GFX_ship")

    def test_native_lua_colour_tables_do_not_change_namespace(self):
        keys = lua_native_keys('NDefines_Graphics={ NGraphics={ COLOR={1, 2, 3},\n WEATHER_DISTANCE_CUTOFF=400, OTHER={ nested=1 }, DRAW_FOW_CUTOFF=70 }}')
        self.assertIn("NDefines_Graphics.NGraphics.DRAW_FOW_CUTOFF", keys)
        self.assertNotIn("NDefines_Graphics.OTHER.nested", keys)

    def test_effective_overlay_and_replace_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            game, mod = root / "game", root / "mod"
            for target in (game / "common/test/a.txt", game / "common/test/b.txt", mod / "common/test/a.txt"):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("value = 1", encoding="utf-8")
            files = effective_files(mod, [game], "common", ".txt")
            self.assertEqual(files["common/test/a.txt"], mod / "common/test/a.txt")
            (mod / "descriptor.mod").write_text('replace_path="common/test"', encoding="utf-8")
            files = effective_files(mod, [game], "common", ".txt")
            self.assertNotIn("common/test/b.txt", files)
            self.assertIn("common/test/a.txt", files)

    def test_localisation_replace_files_use_header_language(self):
        with tempfile.TemporaryDirectory() as directory:
            mod = Path(directory)
            target = mod / "localisation/replace/z_custom_l_braz_por.yml"
            target.parent.mkdir(parents=True)
            target.write_text('l_braz_por:\n WW1_HEADER_TEST:0 "Texto"\n', encoding="utf-8-sig")
            registry, issues = localisation(mod, [])
            self.assertIn("WW1_HEADER_TEST", registry["braz_por"])
            self.assertNotIn("WW1_HEADER_TEST", registry["english"])
            self.assertEqual(issues, [])


class FoundationRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        game = Path(r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV")
        cls.game = game if (game / "common/defines/00_defines.lua").exists() else None

    def test_current_foundation_matches_installed_engine(self):
        if self.game is None:
            self.skipTest("Run validator --game against the target installation")
        self.assertEqual(foundation(ROOT, self.game), [])

    def test_validator_rejects_namespace_errors_and_fairness_regressions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            game, mod = root / "game", root / "mod"
            (game / "common/defines").mkdir(parents=True)
            (game / "common/defines/00_defines.lua").write_text("NDefines={ NCountry={ SPECIAL_FORCES_CAP_BASE=0.05 }}", encoding="utf-8")
            (mod / "common/defines").mkdir(parents=True)
            (mod / "common/defines/bad.lua").write_text("NDefines.NMilitary.SPECIAL_FORCES_CAP_BASE=0.05", encoding="utf-8")
            (mod / "common/on_actions").mkdir(parents=True)
            (mod / "common/on_actions/baianagem_player_on_actions.txt").write_text("on_actions={ on_startup={ effect={ army_experience=500 }}}", encoding="utf-8")
            (mod / "common/on_actions/Sv_core_claim.txt").write_text("on_actions={ on_monthly={ effect={ add_core_of=ROOT }}}", encoding="utf-8")
            (mod / "common/units").mkdir(parents=True)
            (mod / "common/units/special.txt").write_text("sub_units={ shock={ categories={ category_special_forces }}}", encoding="utf-8")
            codes = {i.code for i in foundation(mod, game)}
            self.assertEqual(codes, {"unknown_define", "campaign_fairness", "uncapped_special_unit"})


if __name__ == "__main__":
    unittest.main()
