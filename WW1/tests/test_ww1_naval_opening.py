"""Opening fleet integrity against actual history, hulls, slots and ports.

Static compatibility evidence, not a naval combat or campaign-balance simulator.
"""
from pathlib import Path
from collections import Counter
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_ww1_foundation import parse, walk, read

def entries(path, key):
    root = next(n for n in parse(read(path)) if n.key == key)
    return {n.key: n for n in root.value}

class NavalOpening(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hulls = entries(ROOT / 'common/units/equipment/ww1_1911_naval_hulls.txt', 'equipments')
        cls.modules = entries(ROOT / 'common/units/equipment/modules/ww1_1911_naval_modules.txt', 'equipment_modules')
        cls.techs = entries(ROOT / 'common/technologies/ww1_1911_naval.txt', 'technologies')
        cls.ports = {}
        for path in (ROOT / 'history/states').glob('*.txt'):
            state = next(n for n in parse(read(path)) if n.key == 'state')
            history = next(n for n in state.value if n.key == 'history')
            for n in walk(history.get('buildings', [])):
                if isinstance(n.value, list) and any(x.key == 'naval_base' for x in n.value):
                    cls.ports[n.key] = history.get('owner')

    def test_both_dlc_branches_have_same_unique_operational_ships(self):
        for tag in ['ENG','GER','FRA','SOV','AUS','TUR','ITA','USA','JAP']:
            rosters = []
            for suffix in ['', '_legacy']:
                path = ROOT / 'history/units' / f'ww1_1911_{tag.lower()}_naval{suffix}.txt'
                ships = [n for n in walk(parse(read(path))) if n.key == 'ship']
                names = [n.get('name') for n in ships]
                with self.subTest(country=tag, branch=suffix):
                    self.assertGreater(len(ships), 0)
                    self.assertFalse([k for k,v in Counter(names).items() if v > 1])
                rosters.append(set(names))
            self.assertEqual(rosters[0], rosters[1], tag)

    def test_fleets_and_taskforces_use_existing_owned_ports(self):
        for tag in ['ENG','GER','FRA','SOV','AUS','TUR','ITA','USA','JAP']:
            history = next((ROOT / 'history/countries').glob(tag + ' - *.txt'))
            # An overlord has legitimate port access to its actual starting subjects.
            # Do not infer access from donor fleet positions or an arbitrary alliance.
            subjects = {n.value for n in parse(read(history)) if n.key == 'puppet'}
            path = ROOT / 'history/units' / f'ww1_1911_{tag.lower()}_naval.txt'
            for n in walk(parse(read(path))):
                if n.key in ['naval_base','location']:
                    self.assertIn(self.ports.get(n.value), {tag} | subjects, (tag,n.value))

    def test_opening_ships_reference_granted_types_and_real_variants(self):
        for tag in ['ENG','GER','FRA','SOV','AUS','TUR','ITA','USA','JAP']:
            history = next((ROOT / 'history/countries').glob(tag + ' - *.txt'))
            data = read(history)
            opening = data.split('# BEGIN WW1_1911_NAVAL_OPENING', 1)[1].split('# END WW1_1911_NAVAL_OPENING', 1)[0]
            nodes = list(walk(parse(opening)))
            variants = {(n.get('type'), n.get('name')) for n in nodes if n.key == 'create_equipment_variant'}
            unlocked = set()
            for n in nodes:
                if n.key == 'set_technology':
                    for tech in n.value:
                        if not tech.key.startswith('ww1_1911_'):
                            continue  # Separate land-opening grants do not unlock ships.
                        self.assertIn(tech.key, self.techs)
                        for item in self.techs[tech.key].get('enable_equipments', []):
                            unlocked.add(item.key)
            for suffix in ['', '_legacy']:
                oob = f'ww1_1911_{tag.lower()}_naval{suffix}'
                self.assertIn(f'set_naval_oob = "{oob}"', opening)
                for n in walk(parse(read(ROOT / 'history/units' / (oob + '.txt')))):
                    if n.key == 'equipment':
                        for equipment in n.value:
                            self.assertIn(equipment.key, unlocked, (tag,equipment.key))
                            self.assertIn((equipment.key,equipment.get('version_name')), variants)
                            self.assertEqual(equipment.get('owner'), tag)

    def test_period_modules_fit_their_required_slots_and_do_not_add_modern_systems(self):
        banned = {'ship_radar','ship_anti_air','ship_airplane_launcher'}
        for name, hull in self.hulls.items():
            self.assertLessEqual(int(hull.get('year')), 1911)
            slots = {n.key:n for n in hull.get('module_slots')}
            defaults = {n.key:n.value for n in hull.get('default_modules')}
            for slot, definition in slots.items():
                allowed = {n.key for n in definition.get('allowed_module_categories', [])}
                self.assertFalse(allowed & banned, name)
                module = defaults.get(slot,'empty')
                if allowed & {'ship_sonar','ship_depth_charge'}:
                    self.assertEqual(module, 'empty', (name,slot,'Future ASW gear fitted in 1911'))
                if definition.get('required') == 'yes':
                    self.assertNotEqual(module,'empty',(name,slot))
                if module != 'empty':
                    self.assertIn(module,self.modules)
                    self.assertIn(self.modules[module].get('category'),allowed,(name,slot,module))
            self.assertEqual(float(hull.get('anti_air_attack')),0)

    def test_default_designs_have_weapons_including_legacy_branch(self):
        for name,hull in self.hulls.items():
            attack = sum(float(hull.get(k,0)) for k in ['lg_attack','hg_attack','torpedo_attack'])
            for default in hull.get('default_modules'):
                if default.value != 'empty':
                    stats = self.modules[default.value].get('add_stats', [])
                    attack += sum(float(n.value) for n in stats if n.key in ['lg_attack','hg_attack','torpedo_attack'])
            self.assertGreater(attack,0,name)

    def test_native_capital_classifiers_recognise_our_armour(self):
        for filename,roles in [('battleship.txt',['ironclad','pre_dreadnought','dreadnought']),('battlecruiser.txt',['battlecruiser'])]:
            definition = read(ROOT / 'common/units' / filename)
            for role in roles:
                defaults = self.hulls['ww1_1911_' + role].get('default_modules')
                armor = next(n.value for n in defaults if n.key == 'fixed_ship_armor_slot')
                self.assertIn(armor + ' = 1',definition)

if __name__ == '__main__':
    unittest.main()
