"""Encoding and start-of-game regression checks for national spirits and the naval technology tabs.

Root cause recorded here (October 2026): UTF-8 byte-order marks were re-introduced into Clausewitz script files
(common/ideas, common/technologies, events, interface). The engine rejects those files, which silently dropped the
starting national spirits (ww1_national_modifiers.txt) and emptied the naval technology tabs (naval.txt,
MTG_naval.txt, MTG_naval_Support.txt). Localisation .yml files are the opposite: they REQUIRE the BOM.

Run: python -B -X utf8 -m unittest discover -s WW1/tests -p test_ww1_script_encoding.py
"""
from pathlib import Path
import re, sys, unittest

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('E:/SteamLibrary/steamapps/common/Hearts of Iron IV')
SCRIPT_DIRS = ('common', 'events', 'interface')
SCRIPT_EXT = ('.txt', '.gfx', '.gui')
# Modifier names that the engine logged as unknown and that were replaced with native equivalents.
BANNED_MODIFIERS = {'recovery_rate_factor', 'division_speed', 'production_speed_railway_factor', 'entrenchment',
                    'artillery_attack_factor', 'attrition_for_enemy', 'escort_efficiency_factor'}

def script_files():
    for d in SCRIPT_DIRS:
        for p in (ROOT / d).rglob('*'):
            if p.is_file() and p.suffix.lower() in SCRIPT_EXT:
                yield p

class ScriptEncoding(unittest.TestCase):
    def test_no_bom_in_script_files(self):
        bad = [p.relative_to(ROOT).as_posix() for p in script_files() if p.read_bytes().startswith(b'\xef\xbb\xbf')]
        self.assertEqual(bad, [], 'BOM breaks engine parsing of script files')

    def test_script_files_are_valid_utf8_without_mojibake(self):
        for p in script_files():
            data = p.read_bytes()
            try:
                text = data.decode('utf-8')
            except UnicodeDecodeError as e:
                self.fail(f'{p}: {e}')
            self.assertNotIn('\u00c3\u0192', text, f'{p} contains cp1252 mojibake')
            self.assertNotIn('\u00c3\u00a3', text, f'{p} contains cp1252 mojibake')

    def test_localisation_files_keep_their_bom(self):
        for p in (ROOT / 'localisation').rglob('*.yml'):
            self.assertTrue(p.read_bytes().startswith(b'\xef\xbb\xbf'), p.name)

    def test_banned_unknown_modifiers_are_gone_from_ideas(self):
        for p in (ROOT / 'common/ideas').glob('*.txt'):
            text = re.sub(r'#[^\n]*', '', p.read_text(encoding='utf-8'))
            for name in BANNED_MODIFIERS:
                self.assertIsNone(re.search(rf'\b{name}\s*=', text), f'{p.name}: {name}')

class NationalSpiritsAndNavalTabs(unittest.TestCase):
    def test_starting_spirits_are_defined_and_granted(self):
        defined = set()
        for p in (ROOT / 'common/ideas').glob('*.txt'):
            text = re.sub(r'#[^\n]*', '', p.read_text(encoding='utf-8'))
            defined |= set(re.findall(r'^\s*([A-Za-z0-9_]+)\s*=\s*\{', text, re.M))
        granted = 0
        for p in (ROOT / 'history/countries').glob('*.txt'):
            text = re.sub(r'#[^\n]*', '', p.read_text(encoding='utf-8-sig'))
            tag = p.name[:3]
            for block in re.findall(r'(?m)^add_ideas\s*=\s*(\{[^}]*\}|\S+)', text):
                for name in re.findall(r'[A-Za-z0-9_]+', block):
                    if name.startswith(tag + '_'):
                        granted += 1
                        self.assertIn(name, defined, f'{p.name}: {name}')
        self.assertGreaterEqual(granted, 40)

    def test_safety_net_matches_history_and_skips_scripted_countries(self):
        net = (ROOT / 'common/scripted_effects/zz_ww1_national_spirits.txt').read_text(encoding='utf-8')
        for tag in ('AUS', 'ENG', 'FRA', 'GER', 'SOV'):
            self.assertNotIn(f'tag = {tag} ', net)
        self.assertIn('ww1_ensure_starting_spirits = yes', (ROOT / 'common/on_actions/zz_ww1_national_spirits_on_actions.txt').read_text(encoding='utf-8'))

    def test_naval_tabs_are_populated_and_folders_exist(self):
        folders = {'naval_folder': 0, 'mtgnavalfolder': 0, 'mtgnavalsupportfolder': 0}
        for name in ('naval.txt', 'MTG_naval.txt', 'MTG_naval_Support.txt'):
            text = (ROOT / 'common/technologies' / name).read_text(encoding='utf-8')
            self.assertTrue(text.lstrip().startswith('technologies'), name)
            self.assertEqual(text.count('{'), text.count('}'), name)
            for f in re.findall(r'folder\s*=\s*\{\s*name\s*=\s*(\w+)', text):
                if f in folders:
                    folders[f] += 1
        self.assertGreaterEqual(folders['naval_folder'], 30)
        self.assertGreaterEqual(folders['mtgnavalfolder'], 35)
        self.assertGreaterEqual(folders['mtgnavalsupportfolder'], 40)
        gui = (ROOT / 'interface/countrytechtreeview.gui').read_text(encoding='utf-8-sig')
        for f in folders:
            self.assertIn(f'name = "{f}"', gui)

    def test_naval_mod_hooks_resolve(self):
        effects = set()
        for p in (ROOT / 'common/scripted_effects').glob('*.txt'):
            effects |= set(re.findall(r'^([A-Za-z0-9_]+)\s*=\s*\{', p.read_text(encoding='utf-8'), re.M))
        for name in ('naval.txt', 'MTG_naval.txt'):
            text = (ROOT / 'common/technologies' / name).read_text(encoding='utf-8')
            for hook in re.findall(r'\b(ww1_\w+_design\w*|ww1_asw_design_programme)\s*=\s*yes', text):
                self.assertIn(hook, effects, hook)

if __name__ == '__main__':
    unittest.main()
