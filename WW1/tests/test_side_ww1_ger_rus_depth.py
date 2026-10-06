"""Execute the shipped GER/RUS institutional, procurement and project contracts.

The interpreter models only this subset; engine timing, AI and balance need games.
"""
from pathlib import Path
import itertools
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_ww1_gameplay_contracts import Scripts, World, children, value
from validate_ww1_foundation import parse, read, walk


class DepthWorld(World):
    def condition(self, nodes, current, root=None, source=None):
        root = root or current
        def one(n):
            k, v = n.key, n.value
            if k in ('AND', 'OR', 'NOT'):
                outcomes = [self.condition([x], current, root, source) for x in children(n)]
                return all(outcomes) if k == 'AND' else any(outcomes) if k == 'OR' else not all(outcomes)
            if k in self.countries or k in ('ROOT', 'FROM', 'faction_leader') or k.isdigit():
                return self.condition(children(n), self.scope(k, current, root, source), root, source)
            if k == 'owns_state':
                return self.states.get(str(v), {}).get('owner') == current
            if k == 'is_neighbor_of':
                return frozenset((current, self.scope(v, current, root, source))) in self.neighbours
            return super(DepthWorld, self).condition([n], current, root, source)
        return all(one(n) for n in nodes)

    def effect(self, nodes, current, root=None, source=None):
        root = root or current
        chain = False
        for n in nodes:
            k = n.key
            if k == 'if':
                chain = self.condition(n.get('limit', []), current, root, source)
                if chain:
                    self.effect([x for x in children(n) if x.key != 'limit'], current, root, source)
                continue
            if k in ('else_if', 'else'):
                if not chain and (k == 'else' or self.condition(n.get('limit', []), current, root, source)):
                    self.effect([x for x in children(n) if x.key != 'limit'], current, root, source)
                    chain = True
                continue
            chain = False
            if k == 'send_equipment':
                receiver = self.scope(n.get('target'), current, root, source)
                equipment = n.get('equipment')
                amount = float(n.get('amount'))
                donor = self.countries[current]
                assert donor.equipment.get(equipment, 0) >= amount, 'Cannot conjure unavailable stock'
                donor.equipment[equipment] -= amount
                recipient = self.countries[receiver]
                recipient.equipment[equipment] = recipient.equipment.get(equipment, 0) + amount
            else:
                super().effect([n], current, root, source)


class CountryDepth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Scripts()
        cls.families = json.loads(read(ROOT / 'docs/side_ww1_institution_families.json'))

    def world(self):
        w = DepthWorld(self.s)
        w.neighbours = {frozenset(('GER', 'AUS'))}
        return w

    def procurement(self, donor='FRA'):
        w = self.world()
        w.war('SOV', 'GER')
        for tag in ['SOV', 'FRA', 'ENG']:
            w.countries[tag].faction_leader = 'ENG'
        w.states['214'] = {'owner': 'SOV', 'controller': 'SOV'}
        r = w.countries['SOV']
        r.flags['side_ww1_SOV_imports_open'] = None
        d = w.countries[donor]
        d.equipment.update(infantry_equipment=14000, artillery_equipment=400)
        self.assertTrue(w.take('side_ww1_SOV_request_' + donor + '_arms', 'SOV'))
        self.assertTrue(w.fire('side_ww1_ger_rus.20', donor, 'SOV', 'a'))
        return w

    def test_acquisition_order_never_stacks_or_downgrades_an_institution(self):
        for family, tiers in self.families.items():
            rank = {x: i for i, tier in enumerate(tiers) for x in tier}
            for sequence in itertools.permutations(rank, 2):
                w = self.world()
                tag = family[:3]
                for idea in sequence:
                    w.effect(self.s.effects['side_ww1_set_' + idea], tag)
                active = set(w.countries[tag].ideas) & set(rank)
                self.assertEqual(len(active), 1, (family, sequence, active))
                self.assertEqual(rank[next(iter(active))], max(rank[x] for x in sequence))

    def test_save_normalization_removes_all_conflicting_stages(self):
        for family, tiers in self.families.items():
            w = self.world()
            tag = family[:3]
            w.countries[tag].ideas.update({k: None for k in sum(tiers, [])})
            w.effect(self.s.effects['side_ww1_normalize_' + family], tag)
            self.assertEqual(len(set(w.countries[tag].ideas) & set(sum(tiers, []))), 1)

    def test_allocation_cost_delay_exclusion_and_expiration(self):
        for tag, priority, rival in [('GER', 'armaments_priority', 'naval_priority'),
                                    ('SOV', 'state_contracts', 'civic_contracts')]:
            w = self.world()
            w.war(tag, 'FRA' if tag == 'GER' else 'GER')
            c = w.countries[tag]
            c.flags['side_ww1_' + tag + '_industry_open'] = None
            decision = 'side_ww1_' + tag + '_' + priority + '_project'
            self.assertTrue(w.take(decision, tag))
            self.assertEqual(c.stats['political_power'], 60)
            self.assertEqual(c.stats['num_of_civilian_factories_available_for_projects'], 2)
            self.assertFalse(w.take('side_ww1_' + tag + '_' + rival + '_project', tag))
            self.assertNotIn('side_ww1_' + tag + '_' + priority, c.ideas)
            w.tick(60)
            self.assertEqual(c.stats['num_of_civilian_factories_available_for_projects'], 4)
            self.assertIn('side_ww1_' + tag + '_' + priority, c.ideas)
            self.assertFalse(w.take('side_ww1_' + tag + '_' + rival + '_project', tag))
            w.tick(180)
            self.assertNotIn('side_ww1_' + tag + '_' + priority, c.ideas)

    def test_peace_cancels_preparation_and_releases_factories_without_reward(self):
        w = self.world()
        w.war('GER', 'FRA')
        c = w.countries['GER']
        c.flags['side_ww1_GER_industry_open'] = None
        self.assertTrue(w.take('side_ww1_GER_armaments_priority_project', 'GER'))
        c.wars.clear()
        w.tick(1)
        self.assertEqual(c.stats['num_of_civilian_factories_available_for_projects'], 4)
        self.assertNotIn('side_ww1_GER_priority_preparing', c.flags)
        self.assertNotIn('side_ww1_GER_armaments_priority', c.ideas)

    def test_delivery_conserves_equipment_and_adds_only_one_credit_tranche(self):
        for donor in ['FRA', 'ENG']:
            w = self.procurement(donor)
            before = sum(c.equipment.get('infantry_equipment', 0) for c in w.countries.values())
            w.fire('side_ww1_ger_rus.21', 'SOV', donor)
            self.assertEqual(w.countries[donor].equipment['infantry_equipment'], 8000)
            self.assertEqual(w.countries['SOV'].equipment['infantry_equipment'], 6000)
            self.assertEqual(w.countries['SOV'].variables['side_ww1_SOV_supply_debt'], 1)
            self.assertEqual(sum(c.equipment.get('infantry_equipment', 0) for c in w.countries.values()), before)
            w.fire('side_ww1_ger_rus.21', 'SOV', donor)
            self.assertEqual(w.countries['SOV'].variables['side_ww1_SOV_supply_debt'], 1)
            self.assertEqual(w.countries['SOV'].equipment['infantry_equipment'], 6000)

    def test_late_delivery_rechecks_stock_port_alliance_expiry_and_government(self):
        for reason in ['stock', 'port', 'alliance', 'expiry', 'recipient', 'peace']:
            w = self.procurement()
            if reason == 'stock':
                w.countries['FRA'].equipment['infantry_equipment'] = 100
            elif reason == 'port':
                w.states['214']['controller'] = 'GER'
            elif reason == 'alliance':
                w.countries['SOV'].faction_leader = None
            elif reason == 'expiry':
                w.day = 61
                w.countries['SOV'].flags.clear()
            elif reason == 'recipient':
                self.assertTrue(w.fire('side_ww1_ger_rus.21', 'RUS', 'FRA'))
                self.assertNotIn('infantry_equipment', w.countries['RUS'].equipment)
                continue
            else:
                w.countries['SOV'].wars.clear()
            stock = dict(w.countries['FRA'].equipment)
            w.fire('side_ww1_ger_rus.21', 'SOV', 'FRA')
            self.assertEqual(w.countries['FRA'].equipment, stock, reason)
            self.assertNotIn('infantry_equipment', w.countries['SOV'].equipment, reason)

    def test_postwar_settlement_retires_each_obligation_without_negative_debt(self):
        w = self.world()
        c = w.countries['SOV']
        c.ideas['side_ww1_SOV_allied_supply_credit'] = None
        c.variables['side_ww1_SOV_supply_debt'] = 1
        self.assertTrue(w.take('side_ww1_SOV_settle_supply_credit', 'SOV'))
        w.tick(90)
        self.assertEqual(c.variables['side_ww1_SOV_supply_debt'], 0)
        self.assertNotIn('side_ww1_SOV_allied_supply_credit', c.ideas)
        self.assertFalse(w.take('side_ww1_SOV_settle_supply_credit', 'SOV'))

    def test_empty_armies_and_deteriorating_reserves_fail_the_supply_audit(self):
        for empty in [True, False]:
            w = self.world()
            c = w.countries['SOV']
            c.flags['side_ww1_SOV_supply_audit_open'] = None
            c.ideas['SOV_rifle_famine_scar'] = None
            c.equipment.update(infantry_equipment=4000, artillery_equipment=150)
            c.stats.update({'num_target_equipment_in_armies@artillery_equipment': 1000,
                            'num_equipment_in_armies@artillery_equipment': 900})
            self.assertTrue(w.take('side_ww1_SOV_supply_audit', 'SOV'))
            if empty:
                c.stats['num_target_equipment_in_armies@infantry_equipment'] = 0
            else:
                c.equipment['artillery_equipment'] = 5
            w.tick(90)
            self.assertIn('SOV_rifle_famine_scar', c.ideas)
            self.assertNotIn('side_ww1_SOV_supply_certified', c.flags)

    def test_successful_audit_does_not_delete_current_national_crisis(self):
        w = self.world()
        c = w.countries['SOV']
        c.flags['side_ww1_SOV_supply_audit_open'] = None
        c.flags['SOV_crisis_active'] = None
        c.ideas.update(SOV_rifle_famine_scar=None, SOV_rifle_famine_crisis_1=None)
        c.equipment.update(infantry_equipment=4000, artillery_equipment=150)
        c.stats.update({'num_target_equipment_in_armies@artillery_equipment': 1000,
                        'num_equipment_in_armies@artillery_equipment': 900})
        self.assertTrue(w.take('side_ww1_SOV_supply_audit', 'SOV'))
        w.tick(90)
        self.assertNotIn('SOV_rifle_famine_scar', c.ideas)
        self.assertIn('SOV_rifle_famine_crisis_1', c.ideas)
        self.assertIn('SOV_crisis_active', c.flags)

    def test_new_ui_has_bilingual_texts_and_registered_idea_art(self):
        texts = [read(ROOT / f'localisation/replace/zz_side_ww1_ger_rus_depth_l_{lang}.yml')
                 for lang in ['english', 'braz_por']]
        gfx = read(ROOT / 'interface/side_ww1_ger_rus_depth.gfx')
        for n in walk(parse(read(ROOT / 'common/ideas/side_ww1_ger_rus_depth.txt'))):
            if n.get('picture') is not None:
                self.assertIn('GFX_idea_' + n.get('picture'), gfx)
                for t in texts:
                    self.assertIn(n.key + ':0', t)
                    self.assertIn(n.key + '_desc:0', t)
        for event in self.s.events.values():
            if str(event.get('id')).startswith('side_ww1_ger_rus.'):
                keys = [event.get('title'), event.get('desc')]
                keys += [n.get('name') for n in event.value if n.key == 'option']
                for key in keys:
                    for t in texts:
                        self.assertIn(key + ':0', t)


if __name__ == '__main__':
    unittest.main()
