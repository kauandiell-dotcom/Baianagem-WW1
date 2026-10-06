"""Checks the shipped British graph, chronology and genuine alternative routes."""
from pathlib import Path
from collections import Counter
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_ww1_foundation import parse, read, walk


class BritishTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tree = next(n for n in parse(read(ROOT / 'common/national_focus/uk.txt'))
                        if n.key == 'focus_tree')
        cls.nodes = [n for n in cls.tree.value if n.key == 'focus']
        cls.focus = {n.get('id'): n for n in cls.nodes}

    def test_two_hundred_unique_foci_with_non_overlapping_positions(self):
        self.assertEqual(len(self.nodes), 200)
        self.assertEqual(len(self.focus), 200)
        positions = Counter((n.get('x'), n.get('y')) for n in self.nodes)
        self.assertFalse([p for p, count in positions.items() if count > 1])

    def test_every_link_exists_and_progresses_downward(self):
        for ident, node in self.focus.items():
            for relation in [n for n in node.value if n.key == 'prerequisite']:
                for ref in relation.value:
                    self.assertIn(ref.value, self.focus, ident)
                    self.assertLess(int(self.focus[ref.value].get('y')), int(node.get('y')))
        # Strictly descending rows also prove the prerequisite graph is acyclic.

    def test_choices_are_symmetric_and_do_not_require_the_rival_path(self):
        for ident, node in self.focus.items():
            for rival in node.get('mutually_exclusive', []):
                self.assertIn(rival.value, self.focus)
                backwards = {n.value for n in self.focus[rival.value].get('mutually_exclusive', [])}
                self.assertIn(ident, backwards)
                parents = {n.value for rel in node.value if rel.key == 'prerequisite' for n in rel.value}
                self.assertNotIn(rival.value, parents)

    def test_wartime_government_and_air_service_have_period_dates(self):
        for ident, lower_bound in [('ENG_ww1_the_military_service_act', '1915.12.31'),
                                   ('ENG_ww1_the_war_cabinet', '1915.12.31'),
                                   ('ENG_ww1_royal_air_force_unification', '1917.12.31')]:
            conditions = self.focus[ident].get('available')
            self.assertTrue(any(n.key == 'date' and n.operator == '>' and n.value == lower_bound
                                for n in conditions), ident)
        raf = self.focus['ENG_ww1_royal_air_force_unification'].get('available')
        services = {n.value for n in raf if n.key == 'has_completed_focus'}
        self.assertTrue({'ENG_ww1_royal_flying_corps_organisation',
                         'ENG_ww1_royal_naval_air_service_organisation'} <= services)

    def test_neutral_country_has_peacetime_reform_routes(self):
        for ident, parent in [('ENG_ww1_austerity_and_public_credit', 'ENG_ww1_railway_freight_coordination'),
                              ('ENG_ww1_the_postwar_fleet_review', 'ENG_ww1_grand_fleet_maintenance'),
                              ('ENG_ww1_a_smaller_professional_force', 'ENG_ww1_combined_arms_staff_courses')]:
            paths = [n for n in self.focus[ident].value if n.key == 'prerequisite']
            self.assertEqual(len(paths), 1)  # One block is OR; separate blocks would require all.
            self.assertIn(parent, {n.value for n in paths[0].value})

    def test_both_languages_cover_all_focus_labels_descriptions_and_unlocks(self):
        for language in ['english', 'braz_por']:
            path = ROOT / f'localisation/{language}/ww1_britain_l_{language}.yml'
            self.assertTrue(path.read_bytes().startswith(b'\xef\xbb\xbf'))
            text = read(path)
            for ident in self.focus:
                for suffix in ['', '_desc', '_unlock_tt']:
                    self.assertIn(ident + suffix + ':0', text)


if __name__ == '__main__':
    unittest.main()
