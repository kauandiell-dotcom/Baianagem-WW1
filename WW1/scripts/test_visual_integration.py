"""Validate the artwork actually bound to new content and super-event presentation."""
from pathlib import Path
import json
import re
import sys
import unittest
from PIL import Image
from visual_asset_pipeline import ROOT, pixels, visual_signature, resembles, sprites

class VisualIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads((ROOT / "docs/visual_asset_manifest.json").read_text(encoding="utf-8"))
        cls.registry = sprites(ROOT)

    def test_registered_textures_and_appropriate_dimensions(self):
        for record in self.records:
            with self.subTest(sprite=record["sprite"]):
                source = self.registry.get(record["sprite"])
                self.assertEqual(source, ROOT / record["texture"])
                with Image.open(source) as image:
                    self.assertEqual(image.format, "PNG")
                    self.assertEqual(list(image.size), record["size"])
                    image.load()
                if record["kind"] == "event":
                    self.assertIn(record["size"], ([210, 176], [397, 153]))
                elif record["kind"] in ["idea", "decision", "category"]:
                    self.assertEqual(record["size"], [64, 64])
                elif record["kind"] == "focus":
                    self.assertIn(record["sprite"] + "_shine", self.registry)

    def test_distinct_source_and_visible_texture_content(self):
        self.assertEqual(len(self.records), len({r["source_sha256"] for r in self.records}))
        self.assertEqual(len(self.records), len({r["source_pixels_sha256"] for r in self.records}))
        self.assertEqual(len(self.records), len({pixels(ROOT / r["texture"]) for r in self.records}))
        for i, left in enumerate(self.records):
            for right in self.records[i + 1:]:
                self.assertFalse(resembles(left["source_visual_signature"], right["source_visual_signature"]),
                                 (left["id"], right["id"]))

    def test_super_event_dimensions_and_valid_numeric_ids(self):
        sizes = {"super_event_frame_v2.dds": (720, 600), "ww1_great_war_outbreak_v2.dds": (680, 370),
                 "super_event_btn_v2.dds": (960, 40)}
        for filename, size in sizes.items():
            with Image.open(ROOT / "gfx/interface/super_events" / filename) as image:
                self.assertEqual(image.size, size)
                image.load()
        event = (ROOT / "events/ww1_outbreak_events.txt").read_text(encoding="utf-8-sig")
        self.assertIn("id = ww1_outbreak.1", event)
        self.assertIn("id = ww1_outbreak.2", event)
        self.assertNotRegex(event, r"id\s*=\s*ww1_news\.1914_")
        self.assertNotIn('play_song = "maintheme"', event)
        self.assertNotRegex(event, r"add_(war_support|stability|political_power)")

    def test_multiplayer_dismissal_and_audio_are_scoped_per_human(self):
        gui = (ROOT / "common/scripted_guis/ww1_super_events.txt").read_text(encoding="utf-8-sig")
        effect = (ROOT / "common/scripted_effects/ww1_super_event_effects.txt").read_text(encoding="utf-8-sig")
        self.assertIn("has_country_flag = ww1_super_event_outbreak_active", gui)
        self.assertIn("clr_country_flag = ww1_super_event_outbreak_active", gui)
        self.assertNotIn("clr_global_flag", gui)
        self.assertIn("ww1_great_war_broadcast_seen", effect)
        self.assertIn("limit = { is_ai = no }", effect)
        self.assertIn('scoped_play_song = "ww1_great_war_dispatch"', effect)
        song = ROOT / "music/ww1_great_war_dispatch.ogg"
        self.assertTrue(song.is_file())
        self.assertGreater(song.stat().st_size, 100000)
        self.assertTrue(song.read_bytes().startswith(b"OggS"))
        music = (ROOT / "music/ww1_super_event_music.asset").read_text(encoding="utf-8-sig")
        self.assertIn('file = "ww1_great_war_dispatch.ogg"', music)

    def test_localization_parity_and_all_ui_event_keys(self):
        locales = {}
        for language in ["english", "braz_por"]:
            path = ROOT / f"localisation/{language}/ww1_super_events_l_{language}.yml"
            self.assertTrue(path.read_bytes().startswith(b"\xef\xbb\xbf"))
            text = path.read_text(encoding="utf-8-sig")
            self.assertTrue(text.startswith(f"l_{language}:\n"))
            locales[language] = set(re.findall(r'(?m)^ ([^ :]+):0 "', text))
        self.assertEqual(locales["english"], locales["braz_por"])
        gui = (ROOT / "interface/ww1_super_events.gui").read_text(encoding="utf-8-sig")
        keys = re.findall(r'(?:text|buttonText)\s*=\s*"([^"]+)"', gui)
        for key in keys:
            self.assertIn(key, locales["english"])
        for suffix in ["1.t", "1.d", "1.a", "1.b", "1.c", "2.t", "2.d", "2.a", "2.b"]:
            self.assertIn("ww1_outbreak." + suffix, locales["english"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
