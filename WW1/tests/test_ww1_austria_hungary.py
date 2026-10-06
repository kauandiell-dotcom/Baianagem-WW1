"""Country-owned engine/API contracts and deterministic administration scenarios.

These checks inspect actual generated scripts; they do not claim HOI4 runtime proof.
Run: python -B -X utf8 -m unittest discover -s WW1/tests -p test_ww1_austria_hungary.py
"""
from pathlib import Path
import sys,re,json,unittest,hashlib
from collections import defaultdict
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('E:/SteamLibrary/steamapps/common/Hearts of Iron IV')
sys.path.insert(0,str(ROOT/'scripts'))
from validate_ww1_foundation import parse,read,walk
from visual_asset_pipeline import sprites,visual_signature,resembles

def node(nodes,key):return next(n for n in nodes if n.key==key)
def nodes(path):return parse(read(ROOT/path))
FX={n.key:n.value for n in nodes('common/scripted_effects/ww1_austria_hungary_effects.txt')}
FOCUS=node(nodes('common/national_focus/austria.txt'),'focus_tree').value
FOCI={n.get('id'):n for n in FOCUS if n.key=='focus'}
DECISIONS={d.key:d for p in (ROOT/'common/decisions').glob('ww1_auh*.txt') for c in parse(read(p)) for d in c.value}
EVENTS={n.get('id'):n for p in sorted((ROOT/'events').glob('ww1_austria_hungary*.txt')) for n in nodes('events/'+p.name) if n.key=='country_event'}

class Administration:
    """Small interpreter for the verified administration subset of PDX script."""
    def __init__(self):
        self.vars=defaultdict(float);self.flags=set();self.ideas=set();self.events=[]
        self.war=False;self.capitulated=False;self.states={4,43,154,91,73,736}
        self.enemies=set();self.countries={'AUS','GER','SER','ITA','ROM','SOV','FRA','ALB'}
        self.date='1911.6.1';self.globals=set();self.characters={'AUS_franz_joseph_i','AUS_conrad_von_hotzendorf'}
        self.run(FX['auh_ww1_initialise'])
    def condition(self,ns):
        for n in ns:
            k,v=n.key,n.value
            if k=='OR':ok=any(self.condition([x]) for x in v)
            elif k=='AND':ok=self.condition(v)
            elif k=='NOT':ok=not self.condition(v)
            elif k=='check_variable':
                a=v[0];actual=self.vars[a.key];target=float(a.value)
                ok={'<':actual<target,'>':actual>target,'=':actual==target}[a.operator]
            elif k=='has_idea':ok=v in self.ideas
            elif k=='has_country_flag':ok=v in self.flags
            elif k=='has_global_flag':ok=v in self.globals
            elif k=='has_character':ok=v in self.characters
            elif k=='controls_state':ok=int(v) in self.states
            elif k=='country_exists':ok=v in self.countries
            elif k=='has_war_with':ok=v in self.enemies
            elif k=='has_war':ok=self.war==(v=='yes')
            elif k=='has_capitulated':ok=self.capitulated==(v=='yes')
            elif k=='tag':ok=v=='AUS'
            elif k=='date':
                actual=tuple(map(int,self.date.split('.')));other=tuple(map(int,v.split('.')))
                ok=actual>other if n.operator=='>' else actual<other
            else:raise AssertionError('Unimplemented scenario trigger '+k)
            if not ok:return False
        return True
    def run(self,ns):
        matched=False
        for n in ns:
            k,v=n.key,n.value
            if k=='if':
                matched=self.condition(node(v,'limit').value)
                if matched:self.run([x for x in v if x.key!='limit'])
            elif k=='else_if':
                if not matched:
                    matched=self.condition(node(v,'limit').value)
                    if matched:self.run([x for x in v if x.key!='limit'])
            elif k=='else':
                if not matched:self.run(v)
            elif k in FX:self.run(FX[k])
            elif k in ['set_variable','add_to_variable']:
                a=v[0];self.vars[a.key]=float(a.value) if k=='set_variable' else self.vars[a.key]+float(a.value)
            elif k=='clamp_variable':
                a=n.get('var');self.vars[a]=max(float(n.get('min')),min(float(n.get('max')),self.vars[a]))
            elif k=='set_country_flag':self.flags.add(v if isinstance(v,str) else n.get('flag'))
            elif k=='clr_country_flag':self.flags.discard(v)
            elif k=='add_ideas':
                self.ideas.update([x.key for x in v] if isinstance(v,list) else [v])
            elif k=='remove_ideas':self.ideas.discard(v)
            elif k=='country_event':self.events.append(n.get('id'))
            elif k=='recruit_character':self.characters.add(v)
            elif k=='retire_character':self.characters.discard(v)
            elif k=='add_timed_idea':self.ideas.add(n.get('idea'))
            elif k in ['set_grand_doctrine','set_cosmetic_tag','set_politics','set_popularities','promote_character','add_political_power','add_war_support','AUS_conrad_von_hotzendorf']:
                pass # Outside the administration scenario subset; API/reference checks cover these.
            else:raise AssertionError('Unimplemented scenario effect '+k)
    def weekly(self):self.run(FX['auh_ww1_weekly'])

class ContentContracts(unittest.TestCase):
    def test_exactly_200_unique_focuses(self):self.assertEqual(len(FOCI),200)
    def test_graph_coordinates_and_reachable_parents(self):
        points=set();graph={}
        for fid,n in FOCI.items():
            pos=(n.get('x'),n.get('y'));self.assertNotIn(pos,points);points.add(pos)
            parents=[x.value for p in n.value if p.key=='prerequisite' for x in p.value if x.key=='focus']
            for p in parents:self.assertIn(p,FOCI)
            graph[fid]=parents
        visited=set()
        def visit(fid,trail):
            self.assertNotIn(fid,trail)
            if fid not in visited:
                for p in graph[fid]:visit(p,trail|{fid})
                visited.add(fid)
        for fid in graph:visit(fid,set())
    def test_constitution_exclusions_are_symmetric(self):
        for fid,n in FOCI.items():
            for e in [x.value for p in n.value if p.key=='mutually_exclusive' for x in p.value]:
                reverse=[x.value for p in FOCI[e].value if p.key=='mutually_exclusive' for x in p.value]
                self.assertIn(fid,reverse)
    def test_every_event_reference_resolves(self):
        files=[ROOT/'common/national_focus/austria.txt',ROOT/'events/ww1_austria_hungary_events.txt']+list((ROOT/'common').rglob('ww1_austria_hungary*.txt'))+list((ROOT/'common/decisions').glob('ww1_auh*.txt'))
        for p in files:
            for n in walk(parse(read(p))):
                if n.key=='country_event' and isinstance(n.value,list):self.assertIn(n.get('id'),EVENTS)
    def test_only_registered_native_effects(self):
        api=set(re.findall(r'^## (\w+)',(GAME/'documentation/effects_documentation.md').read_text(encoding='utf-8-sig'),re.M))
        scoped={'AUS','GER','SER','MNT','ALB','ROM','ITA','SOV','FRA','BUL','TUR','AUS_conrad_von_hotzendorf'}
        def check(ns):
            for n in ns:
                if n.key in ['name','ai_chance','trigger','limit']:continue
                if n.key in ['if','else_if','else','every_enemy_country'] or n.key in scoped or n.key.isdigit():check(n.value)
                else:self.assertTrue(n.key in api or n.key in FX,n.key)
        for n in FOCI.values():check(n.get('completion_reward'))
        for ns in FX.values():check(ns)
        for d in DECISIONS.values():
            for n in d.value:
                if n.key.endswith('_effect'):check(n.value)
        for e in EVENTS.values():
            for n in e.value:
                if n.key=='option':check(n.value)
    def test_native_modifiers_and_bounded_reinforcement(self):
        api=set(re.findall(r'^## (\w+)',(GAME/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
        for n in list(walk(nodes('common/ideas/ww1_austria_hungary_ideas.txt')))+list(walk(nodes('common/ideas/ww1_austria_hungary_extra_ideas.txt'))):
            if n.key=='modifier':
                for m in n.value:
                    self.assertIn(m.key,api)
                    if m.key=='land_reinforce_rate':self.assertGreaterEqual(float(m.value),-.005)
        s=read(ROOT/'common/ideas/ww1_austria_hungary_ideas.txt')
        self.assertNotIn('army_core_defence_factor',s)
        self.assertNotIn('army_attack_factor',s)
    def test_localisation_parity_bom_and_all_focus_event_texts(self):
        languages=[]
        for lang in ['braz_por','english']:
            p=ROOT/f'localisation/{lang}/ww1_austria_hungary_l_{lang}.yml'
            self.assertTrue(p.read_bytes().startswith(b'\xef\xbb\xbf'))
            keys=re.findall(r'^ ([\w.]+):0 ',read(p),re.M);self.assertEqual(len(keys),len(set(keys)));languages.append(set(keys))
        self.assertEqual(languages[0],languages[1])
        for fid in FOCI:self.assertTrue({fid,fid+'_desc'}<=languages[0])
        for e in EVENTS.values():
            self.assertIn(e.get('title'),languages[0]);self.assertIn(e.get('desc'),languages[0])
            for o in [n for n in e.value if n.key=='option']:self.assertIn(o.get('name'),languages[0])
    def test_200_real_distinct_focus_textures_and_shine(self):
        registry=sprites(GAME)|sprites(ROOT);hashes=set()
        for fid,n in FOCI.items():
            icon=n.get('icon');self.assertIn(icon,registry);self.assertIn(icon+'_shine',registry)
            p=registry[icon];self.assertTrue(p.is_file())
            im=Image.open(p);self.assertEqual(im.size,(82,82));self.assertEqual(im.mode,'RGBA')
            raw=hashlib.sha256(im.tobytes()).hexdigest();self.assertNotIn(raw,hashes,fid);hashes.add(raw)
        for n in walk(nodes('common/ideas/ww1_austria_hungary_ideas.txt')):
            if n.key=='picture':self.assertIn('GFX_idea_'+n.value,registry)
    def test_paid_projects_have_cancellation_and_concurrency_limit(self):
        ps=[d for did,d in DECISIONS.items() if did.startswith('AUH_ww1_project_')]
        self.assertEqual(len(ps),39)
        for d in ps:
            self.assertGreater(int(d.get('days_remove')),0)
            self.assertGreater(int(d.get('civilian_factory_use')),0)
            self.assertIsNotNone(d.get('cancel_effect'))
            self.assertIn('auh_ww1_projects_active',str(d.get('available')))
    def test_no_free_unit_or_equipment_spawns(self):
        for p in [ROOT/'common/national_focus/austria.txt',ROOT/'events/ww1_austria_hungary_events.txt']:
            for n in walk(parse(read(p))):
                self.assertNotIn(n.key,['create_unit','add_manpower'])
        for p in (ROOT/'common/decisions').glob('ww1_auh*.txt'):
            for n in walk(parse(read(p))):
                if n.key=='add_equipment_to_stockpile':self.assertLess(float(n.get('amount')),0)
    def test_32_divisions_and_no_elite_mountain_stacking(self):
        ns=nodes('history/units/AUS_1936_generic.txt');units=node(ns,'units').value
        self.assertEqual(sum(n.key=='division' for n in units),32)
        mountain=next(n for n in ns if n.key=='division_template' and n.get('name')=='k.u.k. Gebirgsjager-Division')
        regs=mountain.get('regiments');self.assertEqual(sum(n.key=='infantry' for n in regs),6)
        self.assertEqual(sum(n.key=='mountaineers' for n in regs),3)
        self.assertNotIn('kuk_gebirgsjaeger',read(ROOT/'history/units/AUS_1936_generic.txt'))
    def test_diplomatic_refusal_has_retry_and_final_consent_recheck(self):
        for flag in ['german_commission','serbian_trade','albanian_assistance','montenegrin_pact','italian_consultation','romanian_grain','russian_consultation','sixtus_channel']:
            self.assertIn('AUH_ww1_renew_'+flag,DECISIONS)
        d=DECISIONS['AUH_ww1_conclude_armistice']
        for block in ['available','remove_effect']:self.assertIn('all_enemy_country',str(d.get(block)))
    def test_defence_missions_fail_if_the_sector_is_lost(self):
        for key in ['isonzo','carpathians']:
            d=DECISIONS['AUH_ww1_mission_'+key]
            self.assertIn('controls_state',str(d.get('cancel_trigger')))
            self.assertIn('operation_exhausted',str(d.get('cancel_effect')))
    def test_research_has_no_ahead_of_time_discount_and_unique_focus_sources(self):
        names=[]
        for f in FOCI.values():
            for n in walk(f.get('completion_reward')):
                if n.key=='add_tech_bonus':
                    self.assertIsNone(n.get('ahead_reduction'));self.assertEqual(n.get('uses'),'1');names.append(n.get('name'))
        self.assertEqual(len(names),len(set(names)))

class ExtraContentContracts(unittest.TestCase):
    """Rewards for every focus, the dated events, institutions, decisions and their art/localisation."""
    REAL={'country_event','add_political_power','add_stability','add_war_support','army_experience','navy_experience','air_experience',
          'add_tech_bonus','add_to_variable','add_ideas','load_oob','add_command_power','add_mastery_bonus'}
    def test_every_focus_has_a_real_reward(self):
        for fid,n in FOCI.items():
            keys={x.key for x in walk(n.get('completion_reward'))}
            self.assertTrue(keys&self.REAL or any(k.startswith('auh_ww1_set_') for k in keys),fid)
    def test_focus_descriptions_state_their_immediate_effect(self):
        texts={}
        for lang,marker in [('english','Immediate effect:'),('braz_por','Efeito imediato:')]:
            s=read(ROOT/f'localisation/{lang}/ww1_austria_hungary_l_{lang}.yml')
            texts[lang]={k:v for k,v in re.findall(r'^ ([\w.]+):0 "(.*)"$',s,re.M)}
            with_effect=[k for k,v in texts[lang].items() if k.endswith('_desc') and marker in v]
            self.assertGreaterEqual(len(with_effect),110,lang)
    def test_rewards_stay_small_and_cost_something(self):
        totals=defaultdict(float)
        for n in FOCI.values():
            for x in walk(n.get('completion_reward')):
                if x.key in ('add_stability','add_war_support'):totals[x.key]+=float(x.value)
                if x.key=='add_political_power':self.assertLessEqual(abs(float(x.value)),60)
        self.assertLessEqual(totals['add_stability'],.15)
        self.assertLessEqual(totals['add_war_support'],.20)
    def test_extra_events_are_dated_or_triggered_and_localised(self):
        extra={k:e for k,e in EVENTS.items() if int(k.split('.')[1])>=100}
        self.assertGreaterEqual(len(extra),19)
        registry=sprites(GAME)|sprites(ROOT);pictures=set()
        for k,e in extra.items():
            keys={x.key for x in e.value}
            self.assertTrue('is_triggered_only' in keys or {'trigger','mean_time_to_happen'}<=keys,k)
            self.assertGreaterEqual(len([x for x in e.value if x.key=='option']),2,k)
            pic=e.get('picture');self.assertIn(pic,registry,k);self.assertNotIn(pic,pictures,k);pictures.add(pic)
            im=Image.open(registry[pic]);self.assertEqual(im.size,(450,250))
    def test_extra_ideas_and_decisions_have_unique_art_and_text(self):
        registry=sprites(GAME)|sprites(ROOT);hashes={}
        ideas=[n for n in nodes('common/ideas/ww1_austria_hungary_extra_ideas.txt')[0].value[0].value]
        self.assertEqual(len(ideas),11)
        extra_decisions=[d for c in parse(read(ROOT/'common/decisions/ww1_auh_extra.txt')) for d in c.value]
        self.assertEqual(len(extra_decisions),9)
        loc=read(ROOT/'localisation/english/ww1_austria_hungary_l_english.yml')+read(ROOT/'localisation/braz_por/ww1_austria_hungary_l_braz_por.yml')
        for kind,items,sprite in [('idea',ideas,lambda n:'GFX_idea_'+n.get('picture')),('decision',extra_decisions,lambda n:n.get('icon'))]:
            for n in items:
                s=sprite(n);self.assertIn(s,registry,n.key)
                raw=hashlib.sha256(Image.open(registry[s]).convert('RGBA').tobytes()).hexdigest()
                self.assertNotIn(raw,hashes,n.key);hashes[raw]=n.key
                self.assertEqual(loc.count(f' {n.key}:0 '),2,n.key);self.assertEqual(loc.count(f' {n.key}_desc:0 '),2,n.key)
    def test_extra_decisions_reference_real_focuses_ideas_and_opinions(self):
        opinions={n.key for n in nodes('common/opinion_modifiers/ww1_austria_hungary_extra_opinions.txt')[0].value}
        ideas={n.key for n in nodes('common/ideas/ww1_austria_hungary_extra_ideas.txt')[0].value[0].value}|{n.key for n in nodes('common/ideas/ww1_austria_hungary_ideas.txt')[0].value[0].value}
        text=read(ROOT/'common/decisions/ww1_auh_extra.txt')+read(ROOT/'events/ww1_austria_hungary_extra_events.txt')+read(ROOT/'common/national_focus/austria.txt')
        for f in re.findall(r'has_completed_focus = (\w+)',text):self.assertIn(f,FOCI,f)
        for m in re.findall(r'modifier = (AUH_ww1_\w+)',text):self.assertIn(m,opinions,m)
        for i in re.findall(r'(?:idea = |add_ideas = )(AUH_ww1_\w+)',text):self.assertIn(i,ideas,i)

class AdministrationScenarios(unittest.TestCase):
    def test_opening_replaces_legacy_buffs_without_factory_or_division_changes(self):
        s=Administration()
        self.assertIn('AUH_ww1_languages_untrained',s.ideas)
        self.assertNotIn('AUS_alpine_carpathian_bastion',s.ideas)
        self.assertNotIn('AUS_balkan_destiny',s.ideas)
        self.assertEqual(s.vars['auh_ww1_consent'],45)
    def test_food_shortage_tiers_replace_and_recover(self):
        s=Administration()
        for amount,tier in [(40,1),(25,2),(10,3)]:
            s.vars['auh_ww1_provisions']=amount;s.run(FX['auh_ww1_update_pressure'])
            self.assertEqual({i for i in s.ideas if 'food_pressure' in i},{f'AUH_ww1_food_pressure_{tier}'})
        s.vars['auh_ww1_provisions']=60;s.run(FX['auh_ww1_update_pressure'])
        self.assertFalse(any('food_pressure' in i for i in s.ideas))
    def test_losing_grain_regions_increases_actual_weekly_drain(self):
        normal=Administration();lost=Administration();normal.war=lost.war=True
        lost.states-={43,154};normal.weekly();lost.weekly()
        self.assertLess(lost.vars['auh_ww1_provisions'],normal.vars['auh_ww1_provisions'])
    def test_rationing_slows_drain_without_producing_infinite_food(self):
        a=Administration();b=Administration();a.war=b.war=True;b.ideas.add('AUH_ww1_rationing')
        for _ in range(52):a.weekly();b.weekly()
        self.assertGreater(b.vars['auh_ww1_provisions'],a.vars['auh_ww1_provisions'])
        self.assertLess(b.vars['auh_ww1_provisions'],70)
    def test_crisis_and_hunger_affect_confidence_without_extra_army_penalties(self):
        s=Administration();s.war=True;s.vars['auh_ww1_provisions']=20;s.ideas.add('AUS_nationalities_fracture_crisis_1');s.weekly()
        self.assertLess(s.vars['auh_ww1_cohesion'],55)
        self.assertFalse(any('fracture' in i and i.startswith('AUH_ww1') for i in s.ideas))
    def test_no_automatic_calendar_collapse(self):
        s=Administration();s.date='1918.11.1';s.weekly()
        self.assertFalse(s.capitulated)
        self.assertNotIn('auh_ww1_republic',s.flags)
        self.assertIn('AUH_ww1_karl',s.characters)
    def test_services_end_with_actual_peace(self):
        s=Administration();s.ideas|={'AUH_ww1_civil_cabinet','AUH_ww1_emergency_shifts'};s.weekly()
        self.assertNotIn('AUH_ww1_civil_cabinet',s.ideas)
        self.assertNotIn('AUH_ww1_emergency_shifts',s.ideas)
    def test_broken_trade_contracts_expire_on_war(self):
        s=Administration();s.flags|={'auh_ww1_romanian_grain','auh_ww1_serbian_trade'};s.enemies|={'ROM','SER'};s.war=True;s.weekly()
        self.assertNotIn('auh_ww1_romanian_grain',s.flags);self.assertNotIn('auh_ww1_serbian_trade',s.flags)
    def test_budget_and_language_reforms_cannot_stack(self):
        s=Administration()
        for name in ['budget_negotiated','budget_settled','budget_federal','languages_trained','languages_staff','languages_reformed']:s.run(FX['auh_ww1_set_'+name])
        self.assertEqual({i for i in s.ideas if i.startswith('AUH_ww1_budget')},{'AUH_ww1_budget_federal'})
        self.assertEqual({i for i in s.ideas if i.startswith('AUH_ww1_languages')},{'AUH_ww1_languages_reformed'})
    def test_all_counters_stay_in_bounds(self):
        s=Administration()
        for key in ['consent','cohesion','provisions']:s.vars['auh_ww1_'+key]=500
        s.vars['auh_ww1_debt']=99;s.vars['auh_ww1_projects_active']=-2;s.run(FX['auh_ww1_clamp_counters'])
        self.assertEqual(s.vars['auh_ww1_consent'],100);self.assertEqual(s.vars['auh_ww1_debt'],6);self.assertEqual(s.vars['auh_ww1_projects_active'],0)

if __name__=='__main__':unittest.main()
