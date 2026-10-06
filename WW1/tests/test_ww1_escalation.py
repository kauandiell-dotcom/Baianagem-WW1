"""Regression contracts for consent, neutrality and already-issued transit rights."""
from pathlib import Path
import json
import re
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_ww1_foundation import parse,walk,read

def events(filename):
    return {n.get('id'):n for n in parse(read(ROOT/'events'/filename)) if n.key=='country_event'}
def option(event,suffix):
    return next(n for n in event.value if n.key=='option' and n.get('name')==event.get('id')+'.'+suffix)
def keys(nodes):
    return {n.key for n in walk(nodes)}

class EscalationContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new=events('ww1_escalation_events.txt')
        cls.ger=events('ww1_germany_events.txt')
        cls.shared=events('ww1_diplomatic_chains.txt')

    def test_belgian_refusal_requests_british_consent_instead_of_forcing_british_war(self):
        refusal=option(self.ger['ww1_germany_events.22'],'a')
        eng=[n for n in walk(refusal.value) if n.key=='ENG']
        self.assertTrue(eng)
        self.assertFalse(any('declare_war_on' in keys(n.value) for n in eng))
        self.assertTrue(any(n.key=='country_event' and n.get('id')=='ww1_escalation.1' for n in walk(refusal.value)))

    def test_british_neutrality_blocks_automatic_intervention_and_decline_has_no_war(self):
        a=option(self.new['ww1_escalation.1'],'a');b=option(self.new['ww1_escalation.1'],'b')
        self.assertTrue(any(n.key=='has_country_flag' and n.value=='ENG_ww1_armed_neutrality_selected' for n in walk(a.get('trigger'))))
        self.assertTrue(any(n.key=='NOT' for n in a.get('trigger')))
        self.assertIn('declare_war_on',keys(a.value))
        self.assertNotIn('declare_war_on',keys(b.value))
        self.assertTrue(any(n.key=='has_war_with' and n.value=='GER' for n in walk(self.new['ww1_escalation.1'].get('trigger'))))

    def test_authorised_transit_is_recorded_and_respected_by_the_operation(self):
        accepted=option(self.ger['ww1_germany_events.22'],'b')
        self.assertTrue(any(n.key=='set_country_flag' and n.value=='ww1_belgian_transit_authorised' for n in walk(accepted.value)))
        operation=option(self.ger['ww1_germany_events.3'],'a')
        gates=[n for n in walk(operation.value) if n.key=='if' and any(x.key=='declare_war_on' and x.get('target')=='BEL' for x in (n.value or []))]
        self.assertEqual(len(gates),1)
        self.assertTrue(any(n.key=='has_country_flag' and n.value=='ww1_belgian_transit_authorised' for n in walk(gates[0].get('limit'))))

    def test_russian_intervention_is_real_and_german_response_returns_to_its_sender(self):
        a=option(self.shared['ww1_diplomacy.5'],'a');b=option(self.shared['ww1_diplomacy.5'],'b')
        self.assertNotIn('create_wargoal',keys(a.value))
        self.assertTrue(any(n.key=='declare_war_on' and n.get('target')=='AUS' for n in walk(a.value)))
        self.assertNotIn('declare_war_on',keys(b.value))
        german=option(self.new['ww1_escalation.2'],'a')
        self.assertTrue(any(n.key=='declare_war_on' and n.get('target')=='FROM' for n in walk(german.value)))
        self.assertNotIn('declare_war_on',keys(option(self.new['ww1_escalation.2'],'b').value))

    def test_regional_war_and_concessions_do_not_fake_worldwar_or_annex_serbia(self):
        serbia=self.shared['ww1_diplomacy.2']
        self.assertNotIn('news_event',keys(serbia.value))
        self.assertNotIn('puppet',keys(option(serbia,'b').value))
        for event in self.new.values():
            self.assertIn('news_event',keys(option(event,'a').value))
            self.assertNotIn('news_event',keys(option(event,'b').value))

    def test_new_country_decisions_have_bilingual_text_and_real_workshop_art(self):
        for lang in ['english','braz_por']:
            p=ROOT/'localisation/replace'/f'zz_ww1_escalation_l_{lang}.yml'
            self.assertTrue(p.read_bytes().startswith(b'\xef\xbb\xbf'))
            loc=read(p)
            for event in self.new.values():
                for key in ['t','d','a','b']:
                    self.assertIn(event.get('id')+'.'+key+':0',loc)
        manifest=json.loads(read(ROOT/'docs/escalation_visual_manifest.json'))
        self.assertEqual(len({n['source_sha256'] for n in manifest}),len(manifest))
        for entry in manifest:
            self.assertTrue((ROOT/entry['texture']).is_file())
            self.assertEqual(entry['donor_id'],'3365515312')

if __name__=='__main__':unittest.main()
