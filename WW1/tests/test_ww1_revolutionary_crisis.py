import unittest
import os
import re

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestWW1RevolutionaryCrisis(unittest.TestCase):

    def test_german_decision_exists(self):
        dec_path = os.path.join(MOD_ROOT, 'common', 'decisions', 'ww1_ger_rus_rework_decisions.txt')
        with open(dec_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('GER_operation_sealed_train = {', content)
        self.assertIn('date > 1915.11.1', content)
        self.assertIn('id = ww1_russia.250', content)

    def test_russian_crisis_decisions_exist(self):
        dec_path = os.path.join(MOD_ROOT, 'common', 'decisions', 'ww1_ger_rus_rework_decisions.txt')
        with open(dec_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('SOV_revolutionary_crisis_management = {', content)
        self.assertIn('SOV_dec_raise_opolcheniye_militias = {', content)
        self.assertIn('SOV_dec_emergency_grain_relief = {', content)
        self.assertIn('SOV_dec_retake_petrograd = {', content)
        self.assertIn('SOV_dec_retake_moscow = {', content)
        self.assertIn('SOV_dec_crush_bolsheviks_okhrana = {', content)

    def test_crisis_ideas_exist(self):
        ideas_path = os.path.join(MOD_ROOT, 'common', 'ideas', 'ww1_ger_rus_rework_ideas.txt')
        with open(ideas_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('SOV_revolutionary_subversion = {', content)
        self.assertIn('SOV_patriotic_trench_resilience = {', content)
        self.assertIn('SOV_arsenal_strikes_spirit = {', content)
        self.assertIn('SOV_iron_order_triumph = {', content)

    def test_crisis_events_exist(self):
        events_path = os.path.join(MOD_ROOT, 'events', 'ww1_ger_rus_rework_events.txt')
        with open(events_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for ev in ['ww1_russia.250', 'ww1_russia.251', 'ww1_russia.252', 'ww1_russia.253', 'ww1_russia.254', 'ww1_russia.255']:
            self.assertIn(f'id = {ev}', content)

    def test_scripted_effects_and_cleanup(self):
        effects_path = os.path.join(MOD_ROOT, 'common', 'scripted_effects', 'ww1_ger_rus_rework_effects.txt')
        with open(effects_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('SOV_clear_revolutionary_crisis = {', content)
        self.assertIn('SOV_revolutionary_tension = 0', content)
        self.assertIn('SOV_revolutionary_crisis_active', content)

    def test_localisation_keys_and_bom(self):
        en_path = os.path.join(MOD_ROOT, 'localisation', 'english', 'ww1_ger_rus_rework_l_english.yml')
        pt_path = os.path.join(MOD_ROOT, 'localisation', 'braz_por', 'ww1_ger_rus_rework_l_braz_por.yml')

        for path in [en_path, pt_path]:
            with open(path, 'rb') as f:
                header = f.read(3)
                self.assertEqual(header, b'\xef\xbb\xbf', f"{path} must have UTF-8 BOM")

            with open(path, 'r', encoding='utf-8-sig') as f:
                text = f.read()
                self.assertIn('GER_operation_sealed_train:0', text)
                self.assertIn('SOV_revolutionary_crisis_management:0', text)
                self.assertIn('SOV_dec_raise_opolcheniye_militias:0', text)
                self.assertIn('SOV_revolutionary_subversion:0', text)
                self.assertIn('SOV_patriotic_trench_resilience:0', text)
                self.assertIn('SOV_iron_order_triumph:0', text)
                self.assertIn('ww1_russia.250.t:0', text)
                self.assertIn('ww1_russia.254.t:0', text)

if __name__ == '__main__':
    unittest.main()
