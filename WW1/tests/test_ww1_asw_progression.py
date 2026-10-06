"""Period escort progression contracts; runtime/refit behaviour remains unverified."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_ww1_foundation import parse, read, walk


def entries(relative, root):
    return {n.key: n for n in next(n for n in parse(read(ROOT / relative)) if n.key == root).value}


class EscortProgression(unittest.TestCase):
    def test_research_unlocks_period_hardware_in_both_folder_modes(self):
        techs = entries('common/technologies/MTG_naval.txt', 'technologies')
        modules = entries('common/units/equipment/modules/ww1_asw_modules.txt', 'equipment_modules')
        expected = {'sonar': 1915, 'improved_sonar': 1918, 'advanced_sonar': 1921,
                    'basic_depth_charges': 1916, 'improved_depth_charges': 1918,
                    'advanced_depth_charges': 1922}
        for key, year in expected.items():
            with self.subTest(tech=key):
                node = techs[key]
                self.assertEqual(int(node.get('start_year')), year)
                self.assertEqual(len(node.get('enable_equipment_modules')), 1)
                self.assertIn(node.get('enable_equipment_modules')[0].key, modules)
                folders = {n.get('name') for n in node.value if n.key == 'folder'}
                self.assertTrue({'naval_folder', 'mtgnavalfolder'} <= folders)
                self.assertEqual(next(n.value for n in node.get('on_research_complete')
                                      if n.key == 'ww1_asw_design_programme'), 'yes')
        for key in ['modern_sonar', 'modern_depth_charges']:
            self.assertGreater(int(techs[key].get('start_year')), 1923)
            self.assertTrue(any(n.key == 'date' and n.value == '1934.12.31'
                                and n.operator == '>' for n in techs[key].get('allow')))

    def test_every_generated_design_fits_its_hull_without_free_ships(self):
        hulls = entries('common/units/equipment/ww1_1911_naval_hulls.txt', 'equipments')
        modules = entries('common/units/equipment/modules/ww1_1911_naval_modules.txt', 'equipment_modules')
        modules.update(entries('common/units/equipment/modules/ww1_asw_modules.txt', 'equipment_modules'))
        effect = parse(read(ROOT / 'common/scripted_effects/ww1_asw_designs.txt'))[0]
        guard = effect.value[0].get('limit')
        self.assertEqual(guard[0].value, 'ww1_1911_torpedo_craft_capability')
        variants = [n for n in walk(effect.value) if n.key == 'create_equipment_variant']
        self.assertEqual(len(variants), 32)  # 4 listening x 4 charge levels x 2 DLC modes.
        for design in variants:
            hull = hulls[design.get('type')]
            slots = {n.key: {c.key for c in n.get('allowed_module_categories')}
                     for n in hull.get('module_slots')}
            for fitted in design.get('modules'):
                self.assertIn(fitted.key, slots)
                if fitted.value != 'empty':
                    self.assertIn(modules[fitted.value].get('category'), slots[fitted.key])
        forbidden = {'create_ship', 'add_equipment_to_stockpile', 'add_ideas', 'set_technology'}
        self.assertFalse(forbidden & {n.key for n in walk(effect.value)})

    def test_module_visuals_and_design_names_are_registered_in_both_languages(self):
        modules = entries('common/units/equipment/modules/ww1_asw_modules.txt', 'equipment_modules')
        registry = read(ROOT / 'interface/ww1_asw_modules.gfx')
        designs = [n.get('name') for n in walk(parse(read(ROOT / 'common/scripted_effects/ww1_asw_designs.txt')))
                   if n.key == 'create_equipment_variant']
        for module in modules:
            self.assertIn('GFX_SMI_' + module, registry)
            self.assertIn('GFX_EMI_' + module, registry)
        for language in ['english', 'braz_por']:
            texts = read(ROOT / f'localisation/replace/zz_ww1_asw_l_{language}.yml')
            for key in set(designs) | set(modules):
                self.assertIn(key + ':0', texts)


if __name__ == '__main__':
    unittest.main()
