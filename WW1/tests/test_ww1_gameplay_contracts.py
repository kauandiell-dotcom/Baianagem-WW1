"""Evaluate the shipped script contracts, not a second hard-coded implementation.
The small interpreter covers the documented subset used by the tested operations,
crisis episodes and eastern settlements. It is regression evidence; it cannot
replace launching HOI4 for engine timing, AI, UI or multiplayer verification.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import re
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ww1_foundation import Node, parse, walk, read

def children(node): return node.value if isinstance(node.value, list) else []
def value(nodes, key, default=None):
    return next((n.value for n in nodes if n.key == key), default)
def node(nodes, key): return next(n for n in nodes if n.key == key)
def cmp(a, op, b):
    return {"=":lambda:a==b, "==":lambda:a==b, ">":lambda:a>b,
            "<":lambda:a<b, ">=":lambda:a>=b, "<=":lambda:a<=b,
            "!=":lambda:a!=b}[op or "="]()

@dataclass
class Country:
    tag: str
    exists: bool = True
    major: bool = True
    capitulated: bool = False
    wars: set[str] = field(default_factory=set)
    flags: dict[str, float | None] = field(default_factory=dict)
    ideas: dict[str, float | None] = field(default_factory=dict)
    variables: dict[str, float] = field(default_factory=dict)
    stats: dict[str, float | str] = field(default_factory=lambda:{
        "command_power":80, "political_power":100, "casualties":0,
        "num_of_civilian_factories_available_for_projects":4,
        "has_stability":.70, "has_war_support":.70, "has_manpower":200000,
        "convoy_threat":0, "has_convoys_war_support":0, "surrender_progress":0,
        "num_target_equipment_in_armies@infantry_equipment":10000,
        "num_equipment_in_armies@infantry_equipment":10000, "date":"1911.6.1"})
    equipment: dict[str, float] = field(default_factory=lambda:{"support_equipment":100,"artillery_equipment":100})
    faction_leader: str | None = None

class Scripts:
    def __init__(self):
        self.effects={}; self.triggers={}; self.events={}; self.decisions={}
        for folder, dest in [("common/scripted_effects",self.effects),("common/scripted_triggers",self.triggers)]:
            for path in (ROOT/folder).glob("*.txt"):
                for entry in parse(read(path)): dest[entry.key]=children(entry)
        for path in (ROOT/"events").glob("*.txt"):
            for entry in parse(read(path)):
                if entry.key=="country_event":self.events[entry.get("id")]=entry
        for path in (ROOT/"common/decisions").glob("*.txt"):
            for category in parse(read(path)):
                for entry in children(category):
                    if isinstance(entry.value,list):self.decisions[entry.key]=entry
        self.callbacks=children(node(parse(read(ROOT/"common/on_actions/ww1_crisis_on_actions.txt")),"on_actions"))

class World:
    def __init__(self, scripts):
        self.s=scripts;self.day=0;self.global_flags={};self.missions=set();self.taken=set()
        self.countries={t:Country(t) for t in ["GER","SOV","RUS","AUS","FRA","ENG","TUR","BUL","ITA","USA"]}
        self.states={};self.queue=[];self.events=[];self.mastery=[];self.transfers=[];self.projects={}
    def scope(self, token, current, root, source):
        if token=="ROOT":return root
        if token=="FROM":return source
        if token=="faction_leader":
            c=self.countries.get(current);return c.faction_leader if c else None
        return token
    def number(self,v,current):
        try:return float(v)
        except (TypeError,ValueError):
            c=self.countries[current];return c.variables.get(v,c.stats.get(v,0))
    def country(self,current):return self.countries.get(current)
    def condition(self,nodes,current,root=None,source=None):
        root=root or current
        def one(n):
            k,v=n.key,n.value;c=self.country(current)
            if k in ("AND","OR","NOT"):
                outcomes=[one(x) for x in children(n)]
                return all(outcomes) if k=="AND" else any(outcomes) if k=="OR" else not all(outcomes)
            if k in self.s.triggers:return self.condition(self.s.triggers[k],current,root,source)==(v=="yes")
            if k in self.countries or k in ("ROOT","FROM","faction_leader") or k.isdigit():
                return self.condition(children(n),self.scope(k,current,root,source),root,source)
            if k=="always":return v=="yes"
            if k=="exists":return bool(c and c.exists)==(v=="yes")
            if k=="tag":return current==v
            if k=="original_tag":return current==v
            if k=="country_exists":return bool(self.countries.get(v) and self.countries[v].exists)
            if k=="has_country_flag":return bool(c and v in c.flags)
            if k=="has_global_flag":return v in self.global_flags
            if k=="has_idea":return bool(c and v in c.ideas)
            if k=="has_war":return bool(c and c.wars)==(v=="yes")
            if k=="has_capitulated":return bool(c and c.capitulated)==(v=="yes")
            if k=="is_major":return bool(c and c.major)==(v=="yes")
            if k=="has_war_with":return bool(c and self.scope(v,current,root,source) in c.wars)
            if k=="any_enemy_country":
                return bool(c and any(self.condition(children(n),t,root,source) for t in c.wars))
            if k=="controls_state":return self.states.get(str(v),{}).get("controller")==current
            if k in ("is_owned_by","is_controlled_by"):
                prop="owner" if k=="is_owned_by" else "controller"
                return self.states.get(str(current),{}).get(prop)==self.scope(v,current,root,source)
            if k=="is_in_faction":return bool(c and c.faction_leader)==(v=="yes")
            if k=="is_in_faction_with":
                other=self.country(self.scope(v,current,root,source))
                return bool(c and other and c.faction_leader and c.faction_leader==other.faction_leader)
            if k=="has_equipment":
                return all(cmp(c.equipment.get(x.key,0),x.operator,self.number(x.value,current)) for x in children(n))
            if k=="check_variable":
                return all(cmp(c.variables.get(x.key,0),x.operator,self.number(x.value,current)) for x in children(n))
            if c and k in c.stats:
                a=c.stats[k];b=self.number(v,current)
                if k=="date":a=tuple(map(int,str(a).split(".")));b=tuple(map(int,str(v).split(".")))
                return cmp(a,n.operator,b)
            raise AssertionError(f"Unmodelled trigger: {k} in {current}")
        return all(one(n) for n in nodes)
    def effect(self,nodes,current,root=None,source=None):
        root=root or current;chain=False
        for n in nodes:
            k,v=n.key,n.value;c=self.country(current)
            if k=="if":
                chain=self.condition(value(children(n),"limit",[]),current,root,source)
                if chain:self.effect([x for x in children(n) if x.key!="limit"],current,root,source)
                continue
            if k in ("else_if","else"):
                if not chain:
                    ok=k=="else" or self.condition(value(children(n),"limit",[]),current,root,source)
                    if ok:self.effect([x for x in children(n) if x.key!="limit"],current,root,source);chain=True
                continue
            chain=False
            if k in self.s.effects:self.effect(self.s.effects[k],current,root,source)
            elif k in self.countries or k in ("ROOT","FROM","faction_leader") or k.isdigit():
                target=self.scope(k,current,root,source)
                if target is not None:self.effect(children(n),target,root,source)
            elif k in ("name","ai_chance","trigger","custom_effect_tooltip"):pass
            elif k=="set_country_flag":
                flag=value(children(n),"flag") if isinstance(v,list) else v
                days=value(children(n),"days") if isinstance(v,list) else None
                c.flags[flag]=self.day+float(days) if days else None
            elif k=="clr_country_flag":c.flags.pop(v,None)
            elif k=="set_global_flag":self.global_flags[v]=None
            elif k=="add_ideas":c.ideas[v]=None
            elif k=="remove_ideas":c.ideas.pop(v,None)
            elif k=="swap_ideas":
                c.ideas.pop(value(children(n),"remove_idea"),None);c.ideas[value(children(n),"add_idea")]=None
            elif k=="add_timed_idea":c.ideas[value(children(n),"idea")]=self.day+float(value(children(n),"days"))
            elif k in ("set_variable","add_to_variable","divide_variable"):
                for x in children(n):
                    amount=self.number(x.value,current)
                    if k=="set_variable":c.variables[x.key]=amount
                    elif k=="add_to_variable":c.variables[x.key]=c.variables.get(x.key,0)+amount
                    else:
                        if amount==0:raise AssertionError("Division by zero in shipped script")
                        c.variables[x.key]=c.variables.get(x.key,0)/amount
            elif k=="clamp_variable":
                name=value(children(n),"var");c.variables[name]=max(float(value(children(n),"min")),min(float(value(children(n),"max")),c.variables[name]))
            elif k=="add_equipment_to_stockpile":
                typ=value(children(n),"type");c.equipment[typ]=c.equipment.get(typ,0)+float(value(children(n),"amount"))
            elif k=="add_command_power":c.stats["command_power"]+=float(v)
            elif k=="add_political_power":c.stats["political_power"]+=float(v)
            elif k in ("army_experience","navy_experience","air_experience","add_war_support","add_stability"):
                c.stats[k]=c.stats.get(k,0)+float(v)
            elif k=="add_mastery_bonus":self.mastery.append((current,dict((x.key,x.value) for x in children(n))))
            elif k=="activate_mission":self.missions.add((current,v))
            elif k=="country_event":
                self.queue.append((self.day+float(value(children(n),"days",0)),value(children(n),"id"),current,root))
            elif k=="remove_from_faction":self.countries[self.scope(v,current,root,source)].faction_leader=None
            elif k=="transfer_state":
                self.states[str(v)]["owner"]=current;self.transfers.append((str(v),current))
            elif k=="white_peace":
                target=self.scope(v,current,root,source);c.wars.discard(target)
                if target in self.countries:self.countries[target].wars.discard(current)
            else:raise AssertionError(f"Unmodelled effect: {k} in {current}")
    def fire(self,id,current,source=None,option=None):
        e=self.s.events[id]
        if not self.condition(e.get("trigger",[]),current,current,source):return False
        self.events.append((id,current,source))
        self.effect(e.get("immediate",[]),current,current,source)
        if option:
            o=next(x for x in children(e) if x.key=="option" and x.get("name")==id+"."+option)
            self.effect(children(o),current,current,source)
        return True
    def tick(self,days=0):
        self.day+=days
        for c in self.countries.values():
            c.flags={k:t for k,t in c.flags.items() if t is None or t>self.day}
            c.ideas={k:t for k,t in c.ideas.items() if t is None or t>self.day}
        ready=[x for x in self.queue if x[0]<=self.day];self.queue=[x for x in self.queue if x[0]>self.day]
        for _,id,target,source in ready:self.fire(id,target,source)
        for (current,id),(due,used) in list(self.projects.items()):
            d=self.s.decisions[id]
            cancelled=self.condition(d.get("cancel_trigger",[]),current) if d.get("cancel_trigger") else False
            if cancelled or self.day>=due:
                self.effect(d.get("cancel_effect" if cancelled else "remove_effect",[]),current)
                self.countries[current].stats["num_of_civilian_factories_available_for_projects"]+=used
                del self.projects[(current,id)]
    def war(self,a,b):self.countries[a].wars.add(b);self.countries[b].wars.add(a)
    def take(self,id,current):
        d=self.s.decisions[id];c=self.countries[current]
        if (current,id) in self.taken and d.get("fire_only_once")=="yes":return False
        if not self.condition(d.get("available",[]),current):return False
        if not self.condition(d.get("visible",[]),current):return False
        cost=float(d.get("cost",0))
        if c.stats["political_power"]<cost:return False
        c.stats["political_power"]-=cost;self.taken.add((current,id));self.effect(d.get("complete_effect",[]),current)
        if d.get("days_remove"):
            used=float(value(d.get("modifier",[]),"civilian_factory_use",0))
            c.stats["num_of_civilian_factories_available_for_projects"]-=used
            self.projects[(current,id)]=(self.day+float(d.get("days_remove")),used)
        return True
    def finish(self,id,current,kind):
        d=self.s.decisions[id]
        if (current,id) not in self.missions:raise AssertionError("Inactive mission cannot resolve")
        self.effect(d.get(kind,[]),current);self.missions.discard((current,id))

class ScriptRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.s=Scripts()
    def operation(self,tag):
        if tag=="GER":return ("GER_prepare_meuse_operation","GER_meuse_preparation_mission","GER_meuse_objective","GER_meuse","FRA",["18"],"ww1_germany_events.109")
        return ("SOV_prepare_southwestern_offensive","SOV_southwestern_preparation_mission","SOV_southwestern_objective","SOV_southwestern","AUS",["89","91"],"ww1_russia.101")
    def start_operation(self,tag):
        dec,prep,mission,prefix,enemy,states,event=self.operation(tag);w=World(self.s);w.war(tag,enemy)
        w.countries[tag].flags[prefix+"_plan_ready"]=None
        self.assertTrue(w.take(dec,tag))
        return w,(dec,prep,mission,prefix,enemy,states,event)
    def test_operations_consume_stores_and_cannot_be_repeated(self):
        for tag in ("GER","SOV"):
            with self.subTest(tag=tag):
                w,(dec,prep,mission,prefix,enemy,states,event)=self.start_operation(tag);c=w.countries[tag]
                self.assertEqual(c.stats["political_power"],70);self.assertEqual(c.stats["command_power"],40)
                self.assertEqual(c.equipment["support_equipment"],50);self.assertEqual(c.equipment["artillery_equipment"],100)
                self.assertFalse(w.take(dec,tag));self.assertNotIn((tag,mission),w.missions)
                self.assertIn(prefix+"_preparation",c.ideas)
    def test_preparation_reserves_and_command_are_required(self):
        for tag in ("GER","SOV"):
            dec,prep,mission,prefix,enemy,states,event=self.operation(tag)
            for key,val in [("command_power",39),("support_equipment",49),("artillery_equipment",39)]:
                with self.subTest(tag=tag,resource=key):
                    w=World(self.s);w.war(tag,enemy);c=w.countries[tag];c.flags[prefix+"_plan_ready"]=None
                    (c.stats if key=="command_power" else c.equipment)[key]=val
                    self.assertFalse(w.take(dec,tag));self.assertEqual(c.stats["political_power"],100)
    def test_operation_success_requires_actual_control_and_cleans_effects(self):
        for tag in ("GER","SOV"):
            with self.subTest(tag=tag):
                w,(dec,prep,mission,prefix,enemy,states,event)=self.start_operation(tag)
                w.finish(prep,tag,"timeout_effect")
                self.assertFalse(w.condition(self.s.decisions[mission].get("available"),tag))
                for state in states:w.states[state]={"owner":enemy,"controller":tag}
                self.assertTrue(w.condition(self.s.decisions[mission].get("available"),tag))
                w.finish(mission,tag,"complete_effect")
                self.assertNotIn(prefix+"_offensive",w.countries[tag].ideas)
                self.assertNotIn(prefix+"_active",w.countries[tag].flags)
                self.assertTrue(any(q[1]==event for q in w.queue))
                self.assertEqual(w.countries[tag].stats["army_experience"],15)
                self.assertFalse(w.condition(self.s.decisions[mission].get("activation"),tag))
    def test_failure_and_cancellation_have_distinct_consequences(self):
        for tag in ("GER","SOV"):
            for end in ("timeout_effect","cancel_effect"):
                with self.subTest(tag=tag,end=end):
                    w,(dec,prep,mission,prefix,enemy,states,event)=self.start_operation(tag)
                    w.finish(prep,tag,"timeout_effect");w.finish(mission,tag,end)
                    c=w.countries[tag];self.assertNotIn(prefix+"_offensive",c.ideas);self.assertNotIn(prefix+"_active",c.flags)
                    self.assertEqual(prefix+"_exhaustion" in c.ideas,end=="timeout_effect")
                    self.assertEqual(prefix+"_failed" in c.flags,end=="timeout_effect")
                    self.assertNotIn("army_experience",c.stats)
    def test_peace_during_preparation_never_launches_an_offensive(self):
        for tag in ("GER","SOV"):
            w,(dec,prep,mission,prefix,enemy,states,event)=self.start_operation(tag)
            w.countries[tag].wars.clear()
            self.assertTrue(w.condition(self.s.decisions[prep].get("cancel_trigger"),tag))
            w.finish(prep,tag,"cancel_effect")
            self.assertNotIn(prefix+"_preparation",w.countries[tag].ideas);self.assertNotIn((tag,mission),w.missions)
    def test_weekly_callbacks_do_not_multiply_with_country_count(self):
        w=World(self.s);w.war("SOV","GER")
        for i in range(30):w.countries[f"X{i}"]=Country(f"X{i}",major=False)
        for tag in w.countries:
            for cb in self.s.callbacks:
                if cb.key in ("on_weekly","on_weekly_"+tag):w.effect(cb.get("effect",[]),tag)
        self.assertEqual(w.countries["SOV"].variables["SOV_war_weeks"],1)
        self.assertEqual(w.countries["GER"].variables["GER_war_weeks"],1)
    def test_crisis_starts_mild_then_escalates_without_idea_stacking(self):
        w=World(self.s);w.war("SOV","GER");c=w.countries["SOV"]
        c.stats["casualties"]=250000;c.stats["num_equipment_in_armies@infantry_equipment"]=5000
        for _ in range(26):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertIn("SOV_rifle_famine_crisis_1",c.ideas)
        self.assertNotIn("SOV_rifle_famine_crisis_3",c.ideas)
        for _ in range(24):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertEqual([x for x in c.ideas if x.startswith("SOV_rifle_famine_crisis")],["SOV_rifle_famine_crisis_3"])
    def test_all_eight_countries_require_material_pressure_and_recover_when_it_ends(self):
        cases={
            "GER":("ENG",{"convoy_threat":.50}),
            "ENG":("GER",{"convoy_threat":.50}),
            "FRA":("GER",{"casualties":300000,"has_war_support":.30}),
            "SOV":("GER",{"casualties":300000,"num_equipment_in_armies@infantry_equipment":5000}),
            "AUS":("SOV",{"casualties":200000,"has_stability":.30}),
            "TUR":("ENG",{"casualties":100000,"num_equipment_in_armies@infantry_equipment":5000}),
            "ITA":("AUS",{"casualties":200000,"has_war_support":.30}),
            "USA":("GER",{"casualties":200000,"has_war_support":.30})}
        for tag,(enemy,pressure) in cases.items():
            with self.subTest(tag=tag):
                w=World(self.s);w.war(tag,enemy);c=w.countries[tag]
                effect=self.s.effects[f"ww1_{tag}_update_crisis"]
                for _ in range(30):w.effect(effect,tag);w.tick(7)
                self.assertNotIn(tag+"_crisis_active",c.flags)
                c.stats.update(pressure)
                for _ in range(4):w.effect(effect,tag);w.tick(7)
                self.assertIn(tag+"_crisis_active",c.flags)
                crisis_ideas=[n.value for n in walk(self.s.effects[f"ww1_{tag}_close_crisis_episode"]) if n.key=="remove_ideas"]
                self.assertEqual([i for i in crisis_ideas if i in c.ideas],[next(i for i in crisis_ideas if i.endswith("_1"))])
                c.stats.update({"convoy_threat":0,"has_war_support":.70,"has_stability":.70,"num_equipment_in_armies@infantry_equipment":10000})
                for _ in range(6):w.effect(effect,tag);w.tick(7)
                self.assertNotIn(tag+"_crisis_active",c.flags)
                self.assertFalse(any(i in c.ideas for i in crisis_ideas))
    def test_crisis_recovers_and_can_recur_after_material_relapse(self):
        w=World(self.s);w.war("SOV","GER");c=w.countries["SOV"];c.flags["SOV_crisis_active"]=None
        c.ideas["SOV_rifle_famine_crisis_3"]=None
        for _ in range(18):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertFalse(any(x.startswith("SOV_rifle_famine_crisis") for x in c.ideas))
        self.assertNotIn("SOV_crisis_active",c.flags)
        c.stats["casualties"]=250000;c.stats["num_equipment_in_armies@infantry_equipment"]=5000
        for _ in range(20):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertNotIn("SOV_crisis_active",c.flags)
        for _ in range(8):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertIn("SOV_rifle_famine_crisis_1",c.ideas)
    def test_zero_army_equipment_requirement_does_not_divide_by_zero(self):
        w=World(self.s);w.countries["SOV"].stats["num_target_equipment_in_armies@infantry_equipment"]=0
        w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV")
        self.assertEqual(w.countries["SOV"].variables["ww1_infantry_equipment_ratio"],1)
    def test_relief_uses_current_severity_and_never_erases_live_pressure(self):
        for stage in (1,2,3):
            with self.subTest(stage=stage):
                w=World(self.s);w.war("SOV","GER");c=w.countries["SOV"];c.flags["SOV_crisis_active"]=None
                c.ideas[f"SOV_rifle_famine_crisis_{stage}"]=None;c.stats["has_stability"]=.20;c.stats["has_war_support"]=.20
                c.variables["ww1_infantry_equipment_ratio"]=.5;c.variables["SOV_pressure_weeks"]=15
                w.effect(self.s.effects["ww1_SOV_apply_delivered_relief"],"SOV")
                self.assertIn(f"SOV_rifle_famine_crisis_{max(1,stage-1)}",c.ideas)
                self.assertIn("SOV_crisis_active",c.flags)
                self.assertEqual(c.variables["SOV_pressure_weeks"],0)
    def test_relief_requires_ninety_days_and_releases_reserved_civilian_factories(self):
        w=World(self.s);w.war("SOV","GER");c=w.countries["SOV"]
        c.flags["SOV_crisis_active"]=None;c.ideas["SOV_rifle_famine_crisis_3"]=None
        self.assertTrue(w.take("SOV_relief_step_1","SOV"))
        self.assertEqual(c.stats["political_power"],50)
        self.assertEqual(c.stats["num_of_civilian_factories_available_for_projects"],2)
        self.assertIn("SOV_rifle_famine_crisis_3",c.ideas)
        # Conditions improved while the project was running: execute the real recovery helper.
        for _ in range(6):w.effect(self.s.effects["ww1_SOV_update_crisis"],"SOV");w.tick(7)
        self.assertIn("SOV_rifle_famine_crisis_2",c.ideas)
        w.tick(47);self.assertIn("SOV_relief_project_active",c.flags)
        w.tick(1)
        self.assertIn("SOV_rifle_famine_crisis_1",c.ideas)
        self.assertNotIn("SOV_relief_project_active",c.flags)
        self.assertEqual(c.stats["num_of_civilian_factories_available_for_projects"],4)
    def test_peace_cancels_relief_without_awarding_a_stage_reduction(self):
        w=World(self.s);w.war("SOV","GER");c=w.countries["SOV"]
        c.flags["SOV_crisis_active"]=None;c.ideas["SOV_rifle_famine_crisis_3"]=None
        self.assertTrue(w.take("SOV_relief_step_1","SOV"));c.wars.clear();w.tick(1)
        self.assertEqual(c.stats["num_of_civilian_factories_available_for_projects"],4)
        self.assertNotIn("SOV_relief_project_active",c.flags)
        self.assertIn("SOV_rifle_famine_crisis_3",c.ideas)
    def test_settlement_returns_to_original_sender_and_only_occupied_borders_are_ceded(self):
        w=World(self.s);w.war("GER","SOV");w.war("GER","RUS");w.war("RUS","AUS")
        w.states={"10":{"owner":"RUS","controller":"GER"},"11":{"owner":"SOV","controller":"GER"},
                  "12":{"owner":"RUS","controller":"RUS"},"219":{"owner":"RUS","controller":"GER"}}
        self.assertTrue(w.fire("ww1_diplomacy.30","GER","RUS","a"))
        self.assertTrue(any(q[1:]==("ww1_diplomacy.32","RUS","GER") for q in w.queue))
        self.assertFalse(w.fire("ww1_diplomacy.32","SOV","GER","a"))
        self.assertTrue(w.fire("ww1_diplomacy.32","RUS","GER","a"))
        self.assertEqual(w.transfers,[("10","GER")])
        self.assertIn("SOV",w.countries["GER"].wars);self.assertNotIn("GER",w.countries["RUS"].wars)
        self.assertIn("AUS",w.countries["RUS"].wars)
        self.assertNotIn("ww1_eastern_terms_authorised",w.countries["GER"].flags)
    def test_peace_expiry_and_late_refusal_cannot_apply_stale_terms(self):
        w=World(self.s);w.war("GER","SOV");w.war("GER","RUS")
        w.fire("ww1_diplomacy.30","GER","SOV","a");w.fire("ww1_diplomacy.30","GER","RUS","a")
        w.fire("ww1_eastern.1","GER","SOV","a")
        self.assertIn("ww1_eastern_terms_for_RUS",w.countries["GER"].flags)
        w.tick(31);self.assertFalse(w.fire("ww1_diplomacy.32","RUS","GER","a"));self.assertFalse(w.transfers)
        w.fire("ww1_diplomacy.30","GER","RUS","a")
        w.countries["GER"].wars.discard("RUS");w.countries["RUS"].wars.discard("GER")
        w.effect(self.s.effects["ww1_GER_update_eastern_negotiations"],"GER")
        self.assertNotIn("ww1_eastern_terms_authorised",w.countries["GER"].flags)
        self.assertFalse(w.fire("ww1_diplomacy.32","RUS","GER","a"))

if __name__=="__main__":unittest.main()

