"""AUH institutions, recurrent administration, diplomacy and project compiler."""
from pathlib import Path
import json

P="AUH_ww1_"

def build_support(root, focuses, projects, locs):
 def put(path,text):
  p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+"\n",encoding="utf-8")
 def loc(key,pt,en):locs[key]=(pt,en)
 def v(name,n):return f"add_to_variable = {{ auh_ww1_{name} = {n} }}"
 def event(n,title_pt,title_en,desc_pt,desc_en,opts,picture="council"):
  key=f"ww1_auh.{n}";loc(key+".t",title_pt,title_en);loc(key+".d",desc_pt,desc_en)
  body=["country_event = {",f" id = {key}",f" title = {key}.t",f" desc = {key}.d",f" picture = GFX_event_AUH_ww1_{picture}"," is_triggered_only = yes"," fire_only_once = no"]
  for i,opt in enumerate(opts):
   pt,en,effect,*rest=opt;weight=rest[0] if rest else 50;condition=rest[1] if len(rest)>1 else ""
   k=key+"."+chr(97+i);loc(k,pt,en)
   body += [" option = {",f"  name = {k}",f"  ai_chance = {{ base = {weight} }}"]
   if condition:body.append("  trigger = { "+condition+" }")
   body += ["  "+effect,"  if = { limit = { tag = AUS } auh_ww1_clamp_counters = yes auh_ww1_update_pressure = yes }"," }"]
  body.append("}");events.extend(body)

 # Mutually replacing families; all bonuses bounded. Reinforcement is an absolute rate.
 ideas={
  "budget_unsettled":("Orçamento comum contestado","Contested Common Budget","budget", "consumer_goods_factor = .06 political_power_factor = -.08"),
  "budget_negotiated":("Orçamento comum negociado","Negotiated Common Budget","budget", "consumer_goods_factor = .04 political_power_factor = -.04"),
  "budget_settled":("As quotas do dualismo","Dualist Contributions","budget", "consumer_goods_factor = .025 political_power_factor = -.02"),
  "budget_trialist":("As quotas das três Coroas","Three Crowns Contributions","budget", "consumer_goods_factor = .035 political_power_factor = -.025"),
  "budget_federal":("Finanças federais pactuadas","Agreed Federal Finances","budget", "consumer_goods_factor = .04 political_power_factor = -.02"),
  "languages_untrained":("Comunicações regimentais insuficientes","Insufficient Regimental Communications","languages", "army_org_factor = -.08 land_reinforce_rate = -.005"),
  "languages_trained":("Instrutores regimentais","Regimental Instructors","languages", "army_org_factor = -.045 land_reinforce_rate = -.002"),
  "languages_staff":("Um corpo de oficiais comum","A Common Officer Corps","languages", "army_org_factor = -.02 land_reinforce_rate = -.001"),
  "languages_reformed":("Comunicações militares reformadas","Reformed Military Communications","languages", "training_time_army_factor = .02"),
  "arsenals_initial":("Arsenais especializados, padrões distintos","Specialised Arsenals, Different Standards","arsenals", "production_factory_efficiency_gain_factor = -.03"),
  "arsenals_standardised":("Padrões comuns dos arsenais","Common Arsenal Standards","arsenals", "industrial_capacity_factory = .025 production_factory_efficiency_gain_factor = .03"),
  "logistics_organised":("Despacho ferroviário comum","Common Railway Dispatch","logistics", "supply_consumption_factor = -.025"),
  "defensive_staff":("Estado-maior defensivo","Defensive Staff","staff", "dig_in_speed_factor = .05 planning_speed = -.05"),
  "offensive_staff":("Estado-maior ofensivo","Offensive Staff","staff", "planning_speed = .05 supply_consumption_factor = .025"),
  "council":("Conselho das províncias","Council of the Provinces","council", "political_power_factor = -.04"),
  "rationing":("Distribuição alimentar comum","Common Food Distribution","rationing", "consumer_goods_factor = .02"),
  "labour_compact":("Acordo de arbitragem trabalhista","Labour Arbitration Compact","labour", "industrial_capacity_factory = -.015"),
  "diplomatic_restraint":("Acomodação regional","Regional Accommodation","diplomacy", "justify_war_goal_time = .10"),
  "fleet_cautious":("Esquadra de preservação","Fleet Preservation","fleet", "naval_retreat_chance = .05 naval_speed_factor = -.025"),
  "naval_refit_priority":("Prioridade à reequipagem naval","Naval Refitting Priority","repair", "refit_speed = .05 industrial_capacity_dockyard = -.025"),
  "veterans":("Pensões dos veteranos","Veteran Pensions","veterans", "consumer_goods_factor = .025"),
  "peace_administration":("Serviços comuns na paz","Common Peacetime Services","administration", "consumer_goods_factor = .015"),
  "civil_cabinet":("Coordenação civil de guerra","Civil Wartime Coordination","cabinet", "industrial_capacity_factory = .025 consumer_goods_factor = .025"),
  "emergency_shifts":("Jornadas de emergência","Emergency Shifts","shifts", "industrial_capacity_factory = .04 stability_weekly = -.001"),
  "harvest_leave":("Contingentes liberados para a colheita","Contingents Released for Harvest","harvest", "mobilization_speed = -.05"),
  "rotation":("Rotação das unidades","Unit Rotation","rotation", "training_time_army_factor = .05"),
  "operation_exhausted":("Preparação consumida sem resultado","Preparation Spent Without Results","exhausted", "planning_speed = -.10 org_loss_when_moving = .10"),
  "food_pressure_1":("Reservas alimentares sob pressão","Food Reserves Under Pressure","food", "industrial_capacity_factory = -.025"),
  "food_pressure_2":("Abastecimento urbano crítico","Critical Urban Supply","food", "industrial_capacity_factory = -.05"),
  "food_pressure_3":("Ruptura do abastecimento urbano","Urban Supply Breakdown","food", "industrial_capacity_factory = -.08"),
  "debt_1":("Obrigações de guerra limitadas","Limited War Obligations","debt", "consumer_goods_factor = .02"),
  "debt_2":("Orçamento endividado","Indebted Budget","debt", "consumer_goods_factor = .04"),
  "debt_3":("Serviço pesado da dívida","Heavy Debt Service","debt", "consumer_goods_factor = .06"),
  "credit_expansion":("Crédito industrial temporário","Temporary Industrial Credit","credit", "industrial_capacity_factory = .025"),
  "reconstruction_credit":("Crédito de reconstrução temporário","Temporary Reconstruction Credit","credit", "production_speed_buildings_factor = .03"),
 }
 op_mods = {
  "serbia": ("Preparação da frente sérvia", "Serbian Front Preparation", "army_infantry_attack_factor = .08 breakthrough_factor = .08 supply_consumption_factor = .05"),
  "galicia": ("Preparação da frente galega", "Galician Front Preparation", "army_artillery_attack_factor = .10 breakthrough_factor = .08 planning_speed = .05"),
  "isonzo": ("Preparação do Isonzo", "Isonzo Preparation", "army_infantry_defence_factor = .08 dig_in_speed_factor = .10"),
  "carpathians": ("Preparação dos Cárpatos", "Carpathian Preparation", "winter_attrition_factor = -.20 max_dig_in = 3"),
 }
 for name, (pt, en, mod) in op_mods.items():
  ideas["operation_"+name] = (pt, en, "operation", mod)
 ib=["ideas = { country = {"]
 effects=[]
 families={}
 for name,(_,_,family,_) in ideas.items():families.setdefault(family,[]).append(name)
 for name,(pt,en,family,mod) in ideas.items():
  loc(P+name,pt,en)
  loc(P+name+"_desc","Esta instituição aplica os custos e benefícios mostrados abaixo. Reformas da mesma instituição substituem o estágio anterior; despesas de serviços distintos continuam somando.","This institution applies the costs and benefits listed below. Reforms of the same institution replace its previous stage; spending on different services still adds up.")
  ib.append(f" {P+name} = {{ picture = AUH_ww1_{family} allowed = {{ original_tag = AUS }} removal_cost = -1 modifier = {{ {mod} }} }}")
  old=" ".join("remove_ideas = "+P+x for x in families[family] if x!=name)
  legacy={"budget":"AUS_dual_monarchy_compromise","languages":"AUS_tower_of_babel_army","arsenals":"AUS_skoda_siege_arsenals","diplomacy":"AUS_balkan_destiny"}.get(family)
  if legacy:old+=" remove_ideas = "+legacy
  effects.append(f"auh_ww1_set_{name} = {{ {old} if = {{ limit = {{ NOT = {{ has_idea = {P+name} }} }} add_ideas = {P+name} }} }}")
 ib+= ["} }"];put("common/ideas/ww1_austria_hungary_ideas.txt","\n".join(ib))

 # Territory-local autonomy, deliberately no universal defence/manpower modifiers.
 put("common/dynamic_modifiers/ww1_austria_hungary_regions.txt",f"""
AUH_ww1_provincial_council = {{
 icon = GFX_idea_AUH_ww1_council
 enable = {{ always = yes }}
 local_resources_factor = -.04
 local_building_slots_factor = .05
}}
""")
 loc(P+"provincial_council","Conselho civil provincial","Provincial Civil Council")
 loc(P+"provincial_council_desc","Autonomia administrativa com menor extração de recursos e mais capacidade para serviços locais.","Administrative autonomy with lower resource extraction and more capacity for local services.")

 effects.append("""
auh_ww1_clamp_counters = {
 clamp_variable = { var = auh_ww1_consent min = 0 max = 100 }
 clamp_variable = { var = auh_ww1_cohesion min = 0 max = 100 }
 clamp_variable = { var = auh_ww1_provisions min = 0 max = 100 }
 clamp_variable = { var = auh_ww1_debt min = 0 max = 6 }
 clamp_variable = { var = auh_ww1_projects_active min = 0 max = 2 }
}
auh_ww1_initialise = {
 set_country_flag = auh_ww1_initialised
 set_variable = { auh_ww1_consent = 45 }
 set_variable = { auh_ww1_cohesion = 55 }
 set_variable = { auh_ww1_provisions = 70 }
 set_variable = { auh_ww1_debt = 0 }
 set_variable = { auh_ww1_projects_active = 0 }
 set_country_flag = auh_ww1_dualist_constitution
 set_grand_doctrine = grand_battleplan
 if = { limit = { has_character = AUS_conrad_von_hotzendorf }
  AUS_conrad_von_hotzendorf = { remove_unit_leader_trait = paratrooper }
 }
}
auh_ww1_update_pressure = {
 # Mutually exclusive food tiers. Existing multinational war-crisis tiers are not duplicated.
 if = { limit = { check_variable = { auh_ww1_provisions < 15 } }
  auh_ww1_set_food_pressure_3 = yes
 }
 else_if = { limit = { check_variable = { auh_ww1_provisions < 30 } }
  auh_ww1_set_food_pressure_2 = yes
 }
 else_if = { limit = { check_variable = { auh_ww1_provisions < 45 } }
  auh_ww1_set_food_pressure_1 = yes
 }
 else = { remove_ideas = AUH_ww1_food_pressure_1 remove_ideas = AUH_ww1_food_pressure_2 remove_ideas = AUH_ww1_food_pressure_3 }
 if = { limit = { check_variable = { auh_ww1_debt > 3 } } auh_ww1_set_debt_3 = yes }
 else_if = { limit = { check_variable = { auh_ww1_debt > 1 } } auh_ww1_set_debt_2 = yes }
 else_if = { limit = { check_variable = { auh_ww1_debt > 0 } } auh_ww1_set_debt_1 = yes }
 else = { remove_ideas = AUH_ww1_debt_1 remove_ideas = AUH_ww1_debt_2 remove_ideas = AUH_ww1_debt_3 }
}
auh_ww1_weekly = {
 if = { limit = { has_capitulated = no }
  if = { limit = { has_war = yes }
   set_country_flag = auh_ww1_fought_war
   add_to_variable = { auh_ww1_provisions = -.30 }
   if = { limit = { NOT = { controls_state = 43 } } add_to_variable = { auh_ww1_provisions = -.15 } }
   if = { limit = { NOT = { controls_state = 154 } } add_to_variable = { auh_ww1_provisions = -.10 } }
   if = { limit = { has_idea = AUH_ww1_rationing } add_to_variable = { auh_ww1_provisions = .08 } }
   if = { limit = { has_idea = AUH_ww1_labour_compact } add_to_variable = { auh_ww1_cohesion = .06 } }
   if = { limit = { OR = { has_idea = AUS_nationalities_fracture_crisis_1 has_idea = AUS_nationalities_fracture_crisis_2 has_idea = AUS_nationalities_fracture_crisis_3 } }
    add_to_variable = { auh_ww1_cohesion = -.15 }
   }
   if = { limit = { check_variable = { auh_ww1_provisions < 30 } } add_to_variable = { auh_ww1_cohesion = -.20 } }
   if = { limit = { NOT = { controls_state = 4 } } add_to_variable = { auh_ww1_cohesion = -.25 } }
  }
  else = {
   add_to_variable = { auh_ww1_provisions = .40 }
   remove_ideas = AUH_ww1_civil_cabinet
   remove_ideas = AUH_ww1_emergency_shifts
   remove_ideas = AUH_ww1_operation_exhausted
   if = { limit = { has_country_flag = auh_ww1_federal_constitution } add_to_variable = { auh_ww1_cohesion = .08 } }
  }
  if = { limit = { check_variable = { auh_ww1_cohesion < 25 } NOT = { has_country_flag = auh_ww1_constitutional_crisis_cooldown } }
   set_country_flag = { flag = auh_ww1_constitutional_crisis_cooldown days = 365 }
   country_event = { id = ww1_auh.28 days = 1 }
  }
  if = { limit = { check_variable = { auh_ww1_provisions < 30 } NOT = { has_country_flag = auh_ww1_food_warning_cooldown } }
   set_country_flag = { flag = auh_ww1_food_warning_cooldown days = 180 }
   country_event = { id = ww1_auh.29 days = 1 }
  }
 }
 if = { limit = { date > 1916.11.20 NOT = { has_country_flag = auh_ww1_karl_accession } NOT = { has_country_flag = auh_ww1_republic } }
  set_country_flag = auh_ww1_karl_accession
  if = { limit = { has_character = AUS_franz_joseph_i } retire_character = AUS_franz_joseph_i }
  if = { limit = { has_character = AUS_franz_ferdinand } retire_character = AUS_franz_ferdinand }
  recruit_character = AUH_ww1_karl
  promote_character = AUH_ww1_karl
  country_event = { id = ww1_auh.50 days = 1 }
 }
 if = { limit = { has_global_flag = sarajevo_assassination_occurred NOT = { has_country_flag = auh_ww1_sarajevo_noted } }
  set_country_flag = auh_ww1_sarajevo_noted
  if = { limit = { has_character = AUS_franz_ferdinand } retire_character = AUS_franz_ferdinand }
 }
 # Bilateral contracts expire in war or when a partner disappears; no permanent neutrality.
 if = { limit = { OR = { has_war_with = SER NOT = { country_exists = SER } } } clr_country_flag = auh_ww1_serbian_trade }
 if = { limit = { OR = { has_war_with = ROM NOT = { country_exists = ROM } } } clr_country_flag = auh_ww1_romanian_grain }
 if = { limit = { OR = { has_war_with = GER NOT = { country_exists = GER } } } clr_country_flag = auh_ww1_german_commission }
 if = { limit = { OR = { has_war_with = ITA NOT = { country_exists = ITA } } } clr_country_flag = auh_ww1_italian_consultation }
 auh_ww1_clamp_counters = yes
 auh_ww1_update_pressure = yes
}
auh_ww1_ratify_trialism = {
 clr_country_flag = auh_ww1_dualist_constitution
 clr_country_flag = auh_ww1_federal_constitution
 set_country_flag = auh_ww1_trialist_constitution
 set_cosmetic_tag = AUS_ww1_trialist
 auh_ww1_set_budget_trialist = yes
 add_to_variable = { auh_ww1_cohesion = 8 }
 add_to_variable = { auh_ww1_consent = -5 }
}
auh_ww1_ratify_federation = {
 clr_country_flag = auh_ww1_dualist_constitution
 clr_country_flag = auh_ww1_trialist_constitution
 set_country_flag = auh_ww1_federal_constitution
 set_cosmetic_tag = AUS_ww1_federal
 auh_ww1_set_budget_federal = yes
 add_to_variable = { auh_ww1_cohesion = 10 }
 add_to_variable = { auh_ww1_consent = -8 }
 add_ideas = AUH_ww1_council
}
auh_ww1_establish_republic = {
 if = { limit = { has_character = AUH_ww1_karl } retire_character = AUH_ww1_karl }
 if = { limit = { has_character = AUS_franz_joseph_i } retire_character = AUS_franz_joseph_i }
 set_country_flag = auh_ww1_republic
 clr_country_flag = auh_ww1_dualist_constitution
 clr_country_flag = auh_ww1_trialist_constitution
 set_country_flag = auh_ww1_federal_constitution
 set_politics = { ruling_party = democratic elections_allowed = yes election_frequency = 48 }
 set_popularities = { democratic = 55 neutrality = 25 communism = 20 fascism = 0 }
 recruit_character = AUH_ww1_seitz
 promote_character = AUH_ww1_seitz
 set_cosmetic_tag = AUS_ww1_republic
 auh_ww1_set_budget_federal = yes
 add_to_variable = { auh_ww1_cohesion = 8 }
 add_to_variable = { auh_ww1_consent = -10 }
}
""")
 put("common/scripted_effects/ww1_austria_hungary_effects.txt","\n".join(effects))
 put("common/on_actions/ww1_austria_hungary_on_actions.txt","""
on_actions = {
 on_startup = { effect = {
  if = { limit = { country_exists = AUS } AUS = {
   if = { limit = { NOT = { has_country_flag = auh_ww1_initialised } } auh_ww1_initialise = yes }
  } }
 } }
 # Country-specific native weekly callback, no global tag loop.
 on_weekly_AUS = { effect = { if = { limit = { has_country_flag = auh_ww1_initialised } auh_ww1_weekly = yes } } }
}
""")

 put("common/characters/ww1_austria_hungary_characters.txt","""
characters = {
 AUH_ww1_karl = {
  name = AUH_ww1_karl_name
  portraits = { civilian = { large = "gfx/hoi4tgw_portraits/AUH/country_leaders/AUH_karl_i.dds" } }
  country_leader = { ideology = despotism expire = "1935.1.1" }
 }
 AUH_ww1_seitz = {
  name = AUH_ww1_seitz_name
  portraits = { civilian = { large = "gfx/leaders/AUS/AUS_karl_seitz.dds" } }
  country_leader = { ideology = liberalism expire = "1935.1.1" }
 }
}
""")
 loc(P+"karl_name","Carlos I","Karl I")
 loc(P+"seitz_name","Karl Seitz","Karl Seitz")
 for tag,pt,en in [("AUS_ww1_trialist","Monarquia das Três Coroas","Monarchy of the Three Crowns"),("AUS_ww1_federal","Monarquia Federal Danubiana","Danubian Federal Monarchy"),("AUS_ww1_republic","República Federal Danubiana","Danubian Federal Republic")]:
  for suffix in ["","_DEF"]:loc(tag+suffix,pt,en)
  loc(tag+"_ADJ","Danubiano","Danubian")
  for folder in ["","/medium","/small"]:
   source=root/('gfx/flags'+folder+'/AUS.tga')
   if source.exists():
    dest=root/('gfx/flags'+folder+'/'+tag+'.tga');dest.write_bytes(source.read_bytes())

 put("history/units/ww1_auh_reserve_templates.txt","""
# Templates only: zero units, manpower or equipment are created.
division_template = {
 name = "k.u.k. Reserve-Infanterie"
 regiments = {
  infantry = { x = 0 y = 0 } infantry = { x = 0 y = 1 } infantry = { x = 0 y = 2 }
  infantry = { x = 1 y = 0 } infantry = { x = 1 y = 1 } infantry = { x = 1 y = 2 }
 }
}
""")

 categories={"crown":("A Coroa e as províncias","The Crown and the Provinces"),"economy":("A economia comum","The Common Economy"),"projects":("Obras e serviços da monarquia","Works and Services of the Monarchy"),"military":("Preparação das frentes","Preparing the Fronts"),"diplomacy":("Canais diplomáticos","Diplomatic Channels")}
 cb=[];decisions={k:[] for k in categories}
 for name,(pt,en) in categories.items():
  key=P+name;loc(key,pt,en)
  loc(key+"_desc","Consentimento das administrações: §Y[?auh_ww1_consent|0]/100§!\nConfiança das províncias: §Y[?auh_ww1_cohesion|0]/100§!\nReservas alimentares: §Y[?auh_ww1_provisions|0]/100§!\nObrigações de dívida: §Y[?auh_ww1_debt|0]/6§!\nProjetos civis ativos: §Y[?auh_ww1_projects_active|0]/2§!\n\nA escassez alimentar prejudica a produção. As crises militares existentes continuam respondendo à situação da guerra; não há colapso automático por data.","Administrative consent: §Y[?auh_ww1_consent|0]/100§!\nProvincial confidence: §Y[?auh_ww1_cohesion|0]/100§!\nFood reserves: §Y[?auh_ww1_provisions|0]/100§!\nDebt obligations: §Y[?auh_ww1_debt|0]/6§!\nActive civilian projects: §Y[?auh_ww1_projects_active|0]/2§!\n\nFood shortages hamper production. Existing military crises continue to respond to the war situation; there is no automatic calendar collapse.")
  cb.append(f"{key} = {{ icon = GFX_decision_AUH_ww1_{name} allowed = {{ original_tag = AUS }} visible = {{ has_country_flag = auh_ww1_initialised }} }}")
 put("common/decisions/categories/ww1_austria_hungary_categories.txt","\n".join(cb))

 def decision(cat,key,pt,en,descpt,descen,effect,visible,available="",pp=35,days=60,factories=0,once=False,reenable=120,complete="",cancel="",ai=1):
  did=P+key;loc(did,pt,en);loc(did+"_desc",descpt,descen)
  b=[f" {did} = {{",f"  icon = GFX_decision_AUH_ww1_{cat}","  allowed = { original_tag = AUS }",f"  visible = {{ {visible} }}",f"  available = {{ has_capitulated = no {available} }}",f"  cost = {pp}",f"  days_remove = {days}",f"  days_re_enable = {reenable}",f"  fire_only_once = {'yes' if once else 'no'}",f"  ai_will_do = {{ base = {ai} }}"]
  if factories:b.append(f"  civilian_factory_use = {factories}")
  b.append("  complete_effect = { "+complete+" }")
  b.append("  remove_effect = { "+effect+" auh_ww1_clamp_counters = yes auh_ww1_update_pressure = yes }")
  b.append("  cancel_trigger = { OR = { has_capitulated = yes "+cancel+" } }")
  b.append(" }");decisions[cat].extend(b)

 for key,p in projects.items():
  conditions=" ".join(f"owns_state = {s} controls_state = {s}" for s in p['states'])
  # A paid project cancelled by war/territory loss releases capacity, no free refund or output.
  vis=f"has_country_flag = auh_ww1_project_{key}_unlocked"
  av=conditions+" "+p['available']+" check_variable = { auh_ww1_projects_active < 2 } "+f"num_of_civilian_factories_available_for_projects > {p['factories']-1}"
  bad="OR = { has_capitulated = yes "+" ".join(f"NOT = {{ owns_state = {s} controls_state = {s} }}" for s in p['states'])+" }"
  did=P+"project_"+key;loc(did,p['pt'],p['en']);loc(did+"_desc",p['dpt'],p['den'])
  decisions['projects'].append(f"""
 {did} = {{
  icon = GFX_decision_AUH_ww1_projects
  allowed = {{ original_tag = AUS }} visible = {{ {vis} }}
  available = {{ has_capitulated = no {av} }}
  cost = {p['pp']} civilian_factory_use = {p['factories']} days_remove = {p['days']}
  fire_only_once = yes
  complete_effect = {{ add_to_variable = {{ auh_ww1_projects_active = 1 }} }}
  remove_effect = {{ add_to_variable = {{ auh_ww1_projects_active = -1 }}
   if = {{ limit = {{ has_capitulated = no {conditions} {p['available']} }} {p['effect']} }}
   auh_ww1_clamp_counters = yes auh_ww1_update_pressure = yes
  }}
  cancel_trigger = {{ {bad} }}
  cancel_effect = {{ add_to_variable = {{ auh_ww1_projects_active = -1 }} auh_ww1_clamp_counters = yes }}
  ai_will_do = {{ base = 1 modifier = {{ factor = 0 has_war = yes check_variable = {{ auh_ww1_provisions < 30 }} }} }}
 }}
""")

 decision("crown","delegation_session","Negociar com as delegações","Negotiate with the Delegations","Uma sessão de 60 dias custa influência e aumenta o consentimento em 6 pontos. Só é útil enquanto o apoio está abaixo de 85.","A 60-day session costs influence and raises consent by 6 points. It is useful only while support is below 85.",v("consent",6),"has_country_flag = auh_ww1_delegations_unlocked","check_variable = { auh_ww1_consent < 85 }",pp=40)
 decision("crown","provincial_hearings","Realizar audiências provinciais","Hold Provincial Hearings","Uma audiência de 60 dias aumenta a confiança em 5 pontos ao custo de influência política.","A 60-day hearing raises confidence by 5 points at a political influence cost.",v("cohesion",5),"has_country_flag = auh_ww1_hearings_unlocked","check_variable = { auh_ww1_cohesion < 85 }",pp=40)
 decision("crown","constitutional_session","Negociar a convenção","Negotiate the Convention","Uma sessão financia a convenção e aumenta consentimento e confiança em 4 pontos, consumindo capacidade civil por 90 dias.","A session funds the convention and raises consent and confidence by 4 points, consuming civilian capacity for 90 days.",v("cohesion",4)+" "+v("consent",4),"has_country_flag = auh_ww1_convention_unlocked","check_variable = { auh_ww1_consent < 80 } num_of_civilian_factories_available_for_projects > 0",days=90,factories=1,pp=50)
 decision("crown","ratify_trialism","Apresentar novamente a carta trialista","Resubmit the Trialist Charter","Uma nova votação permite ratificar a carta quando o consentimento chegou a 45 e a confiança a 50.","A new vote allows ratification once consent reaches 45 and confidence reaches 50.","country_event = { id = ww1_auh.6 days = 1 }","has_completed_focus = AUH_ww1_third_crown_charter NOT = { has_country_flag = auh_ww1_trialist_constitution }","check_variable = { auh_ww1_consent > 44 } check_variable = { auh_ww1_cohesion > 49 }",days=1,pp=20)
 decision("crown","ratify_federation","Apresentar novamente a constituição federal","Resubmit the Federal Constitution","A ratificação exige consentimento de 50 e confiança de 60. A votação poderá ser recusada.","Ratification requires consent of 50 and confidence of 60. The vote can be refused.","country_event = { id = ww1_auh.9 days = 1 }","has_completed_focus = AUH_ww1_federal_constitution NOT = { has_country_flag = auh_ww1_federal_constitution }","check_variable = { auh_ww1_consent > 49 } check_variable = { auh_ww1_cohesion > 59 }",days=1,pp=20)
 decision("crown","ombudsman_hearing","Atender reclamações da ouvidoria","Address Ombudsman Complaints","Resolver reclamações custa influência e recupera confiança. O efeito não altera a situação militar automaticamente.","Resolving complaints costs influence and restores confidence. It does not automatically change the military situation.",v("cohesion",4),"has_country_flag = auh_ww1_ombudsman_unlocked","check_variable = { auh_ww1_cohesion < 85 }",pp=30,days=90)
 decision("crown","civil_war_cabinet","Financiar o gabinete civil de guerra","Fund the Civil War Cabinet","Um gabinete de 180 dias custa influência e consumo civil, oferecendo apenas uma melhora limitada de coordenação produtiva.","A 180-day cabinet costs influence and civilian consumption, offering only limited production coordination.","","has_country_flag = auh_ww1_civil_cabinet_unlocked","has_war = yes check_variable = { auh_ww1_consent > 39 } NOT = { has_idea = AUH_ww1_civil_cabinet }",pp=60,days=1,reenable=180,complete="add_timed_idea = { idea = AUH_ww1_civil_cabinet days = 180 }")

 decision("economy","grain_purchase","Comprar e distribuir cereal húngaro","Purchase and Distribute Hungarian Grain","Duas fábricas civis por 60 dias compram e transportam cereal: +10 reservas alimentares e −2 consentimento. A região agrícola deve permanecer sob controle.","Two civilian factories for 60 days purchase and transport grain: +10 food reserves and −2 consent. The agricultural region must remain under control.",v("provisions",10)+" "+v("consent",-2),"has_country_flag = auh_ww1_grain_agreement_unlocked","controls_state = 43 controls_state = 154 check_variable = { auh_ww1_provisions < 85 } num_of_civilian_factories_available_for_projects > 1",factories=2,pp=40,days=60,reenable=90,cancel="OR = { NOT = { controls_state = 43 } NOT = { controls_state = 154 } }")
 decision("economy","harvest_leave_grant","Conceder licenças para a colheita","Grant Harvest Leave","Parte dos contingentes recebe licença: as reservas crescem 8 pontos após 90 dias, com mobilização mais lenta durante a temporada.","Part of the contingent receives leave: reserves rise by 8 after 90 days, with slower mobilisation during the season.",v("provisions",8),"has_country_flag = auh_ww1_harvest_leave_unlocked","has_war = yes controls_state = 154 check_variable = { auh_ww1_provisions < 85 }",days=90,reenable=180,pp=35,complete="add_timed_idea = { idea = AUH_ww1_harvest_leave days = 90 }",cancel="has_war = no")
 decision("economy","ration_distribution","Reforçar a distribuição de rações","Reinforce Ration Distribution","Uma fábrica civil por 60 dias melhora a distribuição: +5 reservas. A distribuição equitativa precisa ter sido adotada.","One civilian factory for 60 days improves distribution: +5 reserves. Equitable distribution must have been adopted.",v("provisions",5),"has_country_flag = auh_ww1_rationing_unlocked","has_war = yes check_variable = { auh_ww1_provisions < 85 } num_of_civilian_factories_available_for_projects > 0",factories=1,days=60,pp=25,cancel="has_war = no")
 decision("economy","labour_mediation","Financiar mediação trabalhista","Fund Labour Mediation","A mediação de 90 dias recupera 6 pontos de confiança, custando capacidade civil e influência.","A 90-day mediation restores 6 confidence points at a civilian capacity and influence cost.",v("cohesion",6),"has_country_flag = auh_ww1_labour_mediation_unlocked","check_variable = { auh_ww1_cohesion < 80 } check_variable = { auh_ww1_consent > 29 } num_of_civilian_factories_available_for_projects > 0",factories=1,pp=45,days=90)
 decision("economy","bond_issue","Emitir uma série de títulos de guerra","Issue a Series of War Bonds","Uma emissão financia a indústria por 180 dias: produção +2,5%, com dívida aumentada em um nível. O consumo civil do serviço da dívida persistirá até a amortização. Limite de seis séries.","An issue funds industry for 180 days: +2.5% output, with debt raised by one level. Civilian consumption for debt service persists until repayment. Six-series limit.","add_timed_idea = { idea = AUH_ww1_credit_expansion days = 180 } "+v("debt",1),"has_country_flag = auh_ww1_bond_issue_unlocked","has_war = yes check_variable = { auh_ww1_debt < 6 } NOT = { has_idea = AUH_ww1_credit_expansion }",pp=25,days=1,reenable=180,cancel="has_war = no",ai=.2)
 decision("economy","repay_debt","Amortizar obrigações comuns","Repay Common Obligations","Três fábricas civis por 180 dias e 70 de influência amortizam um nível de dívida. O serviço da dívida diminui conforme os limites mostrados no espírito.","Three civilian factories for 180 days and 70 political power repay one debt level. Debt service falls according to the thresholds shown by the spirit.",v("debt",-1),"OR = { has_country_flag = auh_ww1_debt_repayment_unlocked has_country_flag = auh_ww1_peace_accounts_unlocked }","check_variable = { auh_ww1_debt > 0 } num_of_civilian_factories_available_for_projects > 2",factories=3,pp=70,days=180,reenable=1)
 decision("economy","price_audit","Inspecionar o abastecimento municipal","Inspect Municipal Distribution","Uma inspeção recupera 3 pontos de reservas e 2 de confiança, com trabalho administrativo durante 90 dias.","An inspection restores 3 reserve and 2 confidence points, with administrative work for 90 days.",v("provisions",3)+" "+v("cohesion",2),"has_country_flag = auh_ww1_price_inspection_unlocked","check_variable = { auh_ww1_provisions < 85 }",pp=35,days=90)
 decision("economy","industrial_training","Financiar a formação de trabalhadores","Fund Worker Training","Uma fábrica civil por 90 dias aumenta a confiança em 3 pontos e concede um auxílio único de 15% à pesquisa industrial, sem antecipação tecnológica.","One civilian factory for 90 days raises confidence by 3 and grants one 15% industrial research bonus, without an ahead-of-time reduction.",v("cohesion",3)+" add_tech_bonus = { name = AUH_ww1_research_program bonus = .15 uses = 1 category = industry }","has_country_flag = auh_ww1_industrial_labour_unlocked","num_of_civilian_factories_available_for_projects > 0",factories=1,pp=35,days=90,once=True)

 # Training buys experience with actual stock, one active course of each type.
 courses=[("reserve_training","Formar quadros da reserva","Train Reserve Cadres", "army",6,"reserve_training",400,20),
 ("landwehr_course","Curso da Landwehr","Landwehr Course","army",5,"landwehr_training",300,20),
 ("honved_course","Curso do Honvéd","Honvéd Course","army",5,"honved_training",300,20),
 ("honved_contract","Cumprir o contrato do Honvéd","Fulfil the Honvéd Contract","army",6,"honved_contract",300,30),
 ("federal_course","Curso do exército federal","Federal Army Course","army",6,"federal_service",300,30),
 ("pilot_course","Curso de pilotagem","Pilot Course","air",6,"pilot_training",0,30),
 ("fleet_course","Exercícios da esquadra","Fleet Exercises","navy",6,"fleet_training",0,40),
 ("merchant_course","Curso da marinha mercante","Merchant Marine Course","navy",4,"merchant_training",0,20),
 ("naval_spares_course","Curso de manutenção naval","Naval Maintenance Course","navy",4,"naval_spares",0,30),
 ("coastal_course","Curso de observação costeira","Coastal Observation Course","navy",4,"coastal_observation",0,20)]
 for key,pt,en,kind,experience,flag,rifles,support in courses:
  av=f"num_of_civilian_factories_available_for_projects > 0 has_equipment = {{ support_equipment > {support-1}"
  if rifles:av+=f" infantry_equipment > {rifles-1}"
  av+=" }"
  if key.startswith("honved"):av+=" check_variable = { auh_ww1_consent > 39 }"
  spend=f"add_equipment_to_stockpile = {{ type = support_equipment amount = -{support} }}"
  if rifles:spend+=f" add_equipment_to_stockpile = {{ type = infantry_equipment amount = -{rifles} }}"
  decision("military",key,pt,en,f"Um curso de 90 dias ocupa uma fábrica civil, consome {rifles} rifles e {support} equipamentos de apoio e concede {experience} de experiência. Nenhuma divisão ou aeronave é criada.",f"A 90-day course occupies one civilian factory, consumes {rifles} rifles and {support} support equipment and grants {experience} experience. No divisions or aircraft are created.",f"{kind}_experience = {experience}",f"has_country_flag = auh_ww1_{flag}_unlocked",av,pp=25,days=90,factories=1,reenable=180,complete=spend)
 decision("military","rest_rotation","Organizar descanso e rotação","Organise Rest and Rotation","Duas fábricas civis por 60 dias organizam transporte e descanso: +5 confiança, com treinamento mais lento no período.","Two civilian factories for 60 days organise transport and rest: +5 confidence, with slower training during the period.",v("cohesion",5),"has_country_flag = auh_ww1_rest_rotation_unlocked","has_war = yes check_variable = { auh_ww1_cohesion < 85 } num_of_civilian_factories_available_for_projects > 1",factories=2,days=60,pp=30,complete="add_timed_idea = { idea = AUH_ww1_rotation days = 60 }",cancel="has_war = no")
 decision("military","winter_stores","Preparar os estoques de inverno","Prepare Winter Stores","Sessenta equipamentos de apoio e uma fábrica civil por 60 dias financiam instrução logística: +6 experiência terrestre.","Sixty support equipment and one civilian factory for 60 days fund logistics instruction: +6 land experience.","army_experience = 6","has_country_flag = auh_ww1_winter_stores_unlocked","has_war = yes num_of_civilian_factories_available_for_projects > 0 has_equipment = { support_equipment > 59 }",factories=1,days=60,pp=25,reenable=180,complete="add_equipment_to_stockpile = { type = support_equipment amount = -60 }",cancel="has_war = no")
 decision("military","staff_priority_review","Reavaliar a prioridade do estado-maior","Reassess Staff Priorities","Reabre a escolha entre preparo defensivo e ofensivo. Os espíritos substituem uns aos outros.","Reopens the choice between defensive and offensive preparation. The spirits replace each other.","country_event = { id = ww1_auh.16 days = 1 }","has_country_flag = auh_ww1_staff_review_unlocked","has_war = yes",pp=50,days=30,reenable=180,cancel="has_war = no")

 # Operational missions: no army attack/defence multipliers, no free equipment, no automatic win.
 ops=[("serbia","SER",107,"serbia_operation",False,"Ofensiva limitada na Sérvia","Limited Offensive in Serbia"),
      ("galicia","SOV",91,"galicia_operation",False,"Recuperar a Galícia oriental","Recover Eastern Galicia"),
      ("isonzo","ITA",736,"isonzo_operation",True,"Manter o setor do Isonzo","Hold the Isonzo Sector"),
      ("carpathians","SOV",73,"carpathian_defence",True,"Manter o setor dos Cárpatos","Hold the Carpathian Sector")]
 for key,enemy,state,flag,defence,pt,en in ops:
  did=P+"prepare_"+key;mid=P+"mission_"+key
  statecheck=f"{'controls_state' if defence else 'NOT = { controls_state'} = {state}"+(" }" if not defence else "")
  # Statecheck intentionally assembled as native trigger, no fake territorial achievement.
  loc(did,pt,en);loc(mid,pt+": objetivo",en+": objective")
  dpt=f"Preparar esta missão custa 40 de influência, 30 de comando, 30 peças de artilharia e 50 equipamentos de apoio. O prazo é de 90 dias. {'Mantenha' if defence else 'Conquiste'} o estado {state}. A preparação só melhora planejamento ou entrincheiramento em 8%; não concede força de combate. Fracasso reduz apoio à guerra em 2 pontos percentuais e atrasa o planejamento por 45 dias."
  den=f"Preparing this mission costs 40 political power, 30 command power, 30 artillery and 50 support equipment. The deadline is 90 days. {'Hold' if defence else 'Capture'} state {state}. Preparation only improves planning or entrenchment speed by 8%; it grants no combat strength. Failure lowers war support by 2 percentage points and slows planning for 45 days."
  for k in [did,mid]:loc(k+"_desc",dpt,den)
  success=f"controls_state = {state}"
  end=f"clr_country_flag = auh_ww1_{key}_active remove_ideas = AUH_ww1_operation_{key}"
  win=end+" army_experience = 6 add_war_support = .015 set_country_flag = auh_ww1_operation_success"
  fail=end+" add_war_support = -.02 add_timed_idea = { idea = AUH_ww1_operation_exhausted days = 45 }"
  cancelled=end
  cancellation=f"OR = {{ has_capitulated = yes NOT = {{ has_war_with = {enemy} }} }}"
  if defence:
   cancellation=f"OR = {{ has_capitulated = yes NOT = {{ has_war_with = {enemy} }} NOT = {{ controls_state = {state} }} }}"
   cancelled=f"if = {{ limit = {{ has_capitulated = no has_war_with = {enemy} NOT = {{ controls_state = {state} }} }} {fail} }} else = {{ {end} }}"
  decisions['military'].append(f"""
 {did} = {{
  icon = GFX_decision_AUH_ww1_military allowed = {{ original_tag = AUS }}
  visible = {{ has_country_flag = auh_ww1_{flag}_unlocked }}
  available = {{ has_capitulated = no has_war_with = {enemy} {statecheck}
   command_power > 29 has_equipment = {{ artillery_equipment > 29 support_equipment > 49 }}
   NOT = {{ has_country_flag = auh_ww1_{key}_active }}
   NOT = {{ has_country_flag = auh_ww1_operation_cooldown }}
  }}
  cost = 40 days_re_enable = 180
  complete_effect = {{ add_command_power = -30
   add_equipment_to_stockpile = {{ type = artillery_equipment amount = -30 }}
   add_equipment_to_stockpile = {{ type = support_equipment amount = -50 }}
   set_country_flag = auh_ww1_{key}_active
   set_country_flag = {{ flag = auh_ww1_operation_cooldown days = 180 }}
   add_timed_idea = {{ idea = AUH_ww1_operation_{key} days = 90 }} activate_mission = {mid}
  }}
  ai_will_do = {{ base = 1 modifier = {{ factor = 0 check_variable = {{ auh_ww1_provisions < 30 }} }} }}
 }}
 {mid} = {{
  icon = GFX_decision_AUH_ww1_military allowed = {{ original_tag = AUS }}
  activation = {{ has_country_flag = auh_ww1_{key}_active }}
  visible = {{ has_country_flag = auh_ww1_{key}_active }}
  available = {{ {'always = no' if defence else success} }}
  days_mission_timeout = 90 is_good = no
  cancel_trigger = {{ {cancellation} }}
  cancel_effect = {{ {cancelled} }}
  complete_effect = {{ {win} }}
  timeout_effect = {{ if = {{ limit = {{ {success} }} {win} }} else = {{ {fail} }} }}
 }}
""")

 # Diplomacy support decisions: each proposal is guarded for recipient existence and war.
 decision("diplomacy","romanian_purchase","Executar o contrato de cereal romeno","Execute the Romanian Grain Contract","Duas fábricas civis por 60 dias acrescentam 8 reservas alimentares. O contrato acaba se houver guerra com a Romênia ou se ela desaparecer.","Two civilian factories for 60 days add 8 food reserves. The contract ends during war with Romania or if it disappears.",v("provisions",8),"has_country_flag = auh_ww1_romanian_grain_unlocked","has_country_flag = auh_ww1_romanian_grain country_exists = ROM NOT = { has_war_with = ROM } check_variable = { auh_ww1_provisions < 85 } num_of_civilian_factories_available_for_projects > 1",factories=2,pp=35,days=60,reenable=90,cancel="OR = { has_war_with = ROM NOT = { country_exists = ROM } }")
 decision("diplomacy","serbian_trade","Executar a normalização comercial sérvia","Execute Serbian Trade Normalisation","Uma fábrica civil por 60 dias organiza compras civis e acrescenta 4 reservas alimentares. A normalização acaba se houver guerra com a Sérvia.","One civilian factory for 60 days organises civilian purchases and adds 4 food reserves. Normalisation ends during war with Serbia.",v("provisions",4),"has_country_flag = auh_ww1_serbian_trade","country_exists = SER NOT = { has_war_with = SER } check_variable = { auh_ww1_provisions < 85 } num_of_civilian_factories_available_for_projects > 0",factories=1,pp=30,days=60,reenable=120,cancel="OR = { has_war_with = SER NOT = { country_exists = SER } }")
 decision("diplomacy","german_exchange","Financiar a comissão militar alemã","Fund the German Military Commission","Uma fábrica civil por 90 dias gera 8 de experiência terrestre se a Alemanha aceitou a comissão e permanece em paz conosco.","One civilian factory for 90 days generates 8 land experience if Germany accepted the commission and remains at peace with us.","army_experience = 8","has_country_flag = auh_ww1_german_staff_exchange_unlocked","has_country_flag = auh_ww1_german_commission country_exists = GER NOT = { has_war_with = GER } num_of_civilian_factories_available_for_projects > 0",factories=1,pp=35,days=90,reenable=180,cancel="OR = { has_war_with = GER NOT = { country_exists = GER } }")
 decision("diplomacy","italian_consultations","Realizar a consulta adriática","Hold an Adriatic Consultation","Consultas de 60 dias dão 3 de confiança se o pacto com Roma permanece válido; não impedem que a Itália mude de política.","A 60-day consultation grants 3 confidence if the pact with Rome remains valid; it does not prevent Italy changing its policy.",v("cohesion",3),"has_country_flag = auh_ww1_italian_consultation_unlocked","has_country_flag = auh_ww1_italian_consultation country_exists = ITA NOT = { has_war_with = ITA } check_variable = { auh_ww1_cohesion < 85 }",pp=35,days=60,cancel="OR = { has_war_with = ITA NOT = { country_exists = ITA } }")
 decision("diplomacy","refugee_assistance","Financiar assistência aos refugiados","Fund Refugee Assistance","Duas fábricas civis por 90 dias fornecem assistência e recuperam 5 de confiança. Não há recrutamento gratuito de refugiados.","Two civilian factories for 90 days provide assistance and restore 5 confidence. There is no free refugee recruitment.",v("cohesion",5),"has_country_flag = auh_ww1_refugee_assistance_unlocked","num_of_civilian_factories_available_for_projects > 1 check_variable = { auh_ww1_cohesion < 85 }",factories=2,pp=40,days=90)
 decision("diplomacy","armistice_proposal","Enviar uma proposta de armistício","Send an Armistice Proposal","A proposta sem anexações será entregue a todos os inimigos atuais. Cada governo pode aceitar ou rejeitar. A guerra continua durante as conversações; autorizações expiram em 120 dias.","A proposal without annexations is delivered to every current enemy. Each government may accept or refuse. War continues during talks; authorisations expire in 120 days.","every_enemy_country = { country_event = { id = ww1_auh.46 days = 1 } }","has_country_flag = auh_ww1_armistice_proposal_unlocked","has_war = yes has_country_flag = auh_ww1_sixtus_channel",pp=100,days=1,reenable=180,cancel="has_war = no",ai=.5)
 decision("diplomacy","conclude_armistice","Concluir o armistício por acordo","Conclude the Agreed Armistice","Exige autorização vigente de todos os inimigos atuais. A monarquia deixa sua facção e conclui paz branca com os beligerantes; não concede anexações e não garante a paz de seus aliados.","Requires valid authorisation from every current enemy. The monarchy leaves its faction and concludes white peace with belligerents; it grants no annexations and does not guarantee its allies' peace.","if = { limit = { has_war = yes all_enemy_country = { has_country_flag = auh_ww1_armistice_consent } } leave_faction = yes every_enemy_country = { white_peace = AUS } set_country_flag = auh_ww1_negotiated_peace }","has_country_flag = auh_ww1_conference_unlocked","has_war = yes all_enemy_country = { has_country_flag = auh_ww1_armistice_consent }",pp=50,days=1,reenable=180,cancel="has_war = no",ai=.2)
 decision("crown","veteran_assistance","Organizar assistência aos veteranos","Organise Veteran Assistance","Uma fábrica civil por 90 dias recupera 4 de confiança em paz.","One civilian factory for 90 days restores 4 confidence in peace.",v("cohesion",4),"has_country_flag = auh_ww1_veterans_unlocked","has_war = no num_of_civilian_factories_available_for_projects > 0 check_variable = { auh_ww1_cohesion < 85 }",factories=1,pp=30,days=90,cancel="has_war = yes")
 decision("crown","danubian_reconciliation","Financiar a reconciliação das administrações","Fund Administrative Reconciliation","Uma fábrica civil por 90 dias recupera 4 de consentimento e 3 de confiança durante a paz.","One civilian factory for 90 days restores 4 consent and 3 confidence during peace.",v("consent",4)+" "+v("cohesion",3),"has_country_flag = auh_ww1_danubian_services_unlocked","has_war = no num_of_civilian_factories_available_for_projects > 0 check_variable = { auh_ww1_consent < 85 }",factories=1,pp=40,days=90,cancel="has_war = yes")
 decision("economy","peace_credit_line","Contratar crédito de reconstrução","Contract Reconstruction Credit","Uma linha de crédito acelera a construção em 3% durante 180 dias e cria uma obrigação de dívida. A contratação pode ser recusada deixando a decisão sem uso.","A credit line speeds construction by 3% for 180 days and creates a debt obligation. Credit may be declined by leaving the decision unused.","add_timed_idea = { idea = AUH_ww1_reconstruction_credit days = 180 } "+v("debt",1),"has_country_flag = auh_ww1_peace_credit_unlocked","has_war = no check_variable = { auh_ww1_debt < 4 }",pp=25,days=1,once=True,cancel="has_war = yes",ai=.2)

 # Country narrative: costs and state transitions, not celebratory empty events.
 events=["add_namespace = ww1_auh"]
 event(1,"Duas capitais, uma Coroa","Two Capitals, One Crown","A monarquia entra em 1911 com recursos importantes e administrações que disputam suas prioridades. Devemos obter apoio sem prometer que todas as diferenças desaparecerão.","The monarchy enters 1911 with significant resources and administrations competing over priorities. We must secure support without promising every difference will disappear.",[("Ouvir as duas delegações.","Hear both delegations.",v("consent",4)+" add_political_power = -25",80),("Convocar representantes provinciais.","Convene provincial representatives.",v("cohesion",4)+" add_political_power = -25",20)])
 event(2,"Reabrir o compromisso","Reopen the Compromise","Revisar o acordo de 1867 oferece caminhos diferentes. Um compromisso orçamentário agrada aos governos; uma consulta provincial dá voz a quem ficou de fora.","Revisiting the 1867 agreement offers different paths. A budget compromise pleases governments; a provincial consultation gives a voice to those excluded.",[("Priorizar o consentimento dos governos.","Prioritise government consent.",v("consent",5)+" "+v("cohesion",-2),70),("Priorizar a confiança das províncias.","Prioritise provincial confidence.",v("cohesion",5)+" "+v("consent",-2),30)])
 event(3,"Renovar o dualismo","Renew Dualism","Manter o pacto entre Viena e Budapeste evita uma ruptura institucional imediata, mas torna indispensável negociar os serviços comuns.","Retaining the compact between Vienna and Budapest avoids an immediate institutional rupture, but makes negotiating common services essential.",[("Firmar o compromisso com Budapeste.","Affirm the compact with Budapest.",v("consent",6)+" "+v("cohesion",-3),80),("Manter o pacto com consultas provinciais.","Retain the compact with provincial consultations.",v("cohesion",3)+" add_political_power = -40",20)])
 event(4,"Uma disputa entre administrações","A Dispute Between Administrations","Os dois governos discordam sobre uma despesa comum. Impor a decisão poupa tempo, mas prejudica a confiança; negociar consome influência.","The two governments disagree over common spending. Imposing a decision saves time but harms confidence; negotiating consumes influence.",[("Financiar uma mediação.","Fund mediation.",v("consent",4)+" add_political_power = -35",80),("A Coroa decidirá.","The Crown will decide.",v("consent",-5)+" add_political_power = 20",20)])
 event(5,"A proposta de uma terceira Coroa","The Third Crown Proposal","Uma nova unidade sul-eslava enfrenta oposição em Budapeste e desconfiança local. O projeto precisa de garantias e compensações antes da ratificação.","A new South Slav unit faces resistance in Budapest and local mistrust. The project needs safeguards and compensation before ratification.",[("Aceitar o custo da negociação.","Accept the cost of negotiation.",v("consent",-8)+" "+v("cohesion",5)+" add_political_power = -40",100)])
 event(6,"A votação da carta trialista","The Vote on the Trialist Charter","A terceira Coroa só se torna uma instituição quando as administrações e as províncias aceitam sua carta. Exigimos 45 de consentimento e 50 de confiança.","The third Crown becomes an institution only when administrations and provinces accept its charter. We require 45 consent and 50 confidence.",[("Ratificar a carta.","Ratify the charter.","auh_ww1_ratify_trialism = yes",90,"check_variable = { auh_ww1_consent > 44 } check_variable = { auh_ww1_cohesion > 49 }"),("Continuar as negociações.","Continue negotiations.",v("consent",2)+" add_political_power = -20",10)])
 event(7,"Um projeto federal","A Federal Project","Reconhecer as províncias como partes do pacto federal altera o equilíbrio entre os governos. A oposição terá de ser vencida por negociação, não por uma proclamação.","Recognising provinces as parties to a federal compact changes the balance between governments. Opposition must be overcome through negotiation, not a proclamation.",[("Preparar a convenção.","Prepare the convention.",v("consent",-10)+" "+v("cohesion",6)+" add_political_power = -50",100)])
 event(8,"A repartição fiscal federal","Federal Fiscal Distribution","As províncias pedem recursos para serviços próprios; os ministérios comuns pedem receitas estáveis. Nenhuma solução atende plenamente aos dois.","Provinces request resources for their own services; common ministries request stable revenue. No solution fully satisfies both.",[("Garantir receitas provinciais.","Guarantee provincial revenue.",v("cohesion",6)+" "+v("consent",-3),60),("Priorizar os ministérios comuns.","Prioritise common ministries.",v("consent",6)+" "+v("cohesion",-3),40)])
 event(9,"Ratificar a constituição federal","Ratify the Federal Constitution","A constituição exige consentimento de 50 e confiança de 60. A monarquia permanece sob a dinastia, com competências provinciais reconhecidas e custos comuns pactuados.","The constitution requires 50 consent and 60 confidence. The monarchy remains under the dynasty, with recognised provincial powers and agreed common costs.",[("Promulgar a constituição.","Promulgate the constitution.","auh_ww1_ratify_federation = yes",90,"check_variable = { auh_ww1_consent > 49 } check_variable = { auh_ww1_cohesion > 59 }"),("Adiar a ratificação.","Defer ratification.",v("consent",2)+" add_political_power = -25",10)])
 event(10,"Uma economia complementar e dividida","A Complementary but Divided Economy","Indústria e agricultura precisam ser coordenadas sem fingir que o orçamento comum domina todas as decisões de Viena e Budapeste.","Industry and agriculture must be coordinated without pretending the common budget controls every decision in Vienna and Budapest.",[("Reunir informações das duas administrações.","Gather information from both administrations.",v("consent",3)+" add_political_power = -25",80),("Priorizar os serviços de abastecimento.","Prioritise supply services.",v("provisions",4)+" add_political_power = -30",20)])
 event(11,"Quem paga pelo pão?","Who Pays for Bread?","A comissão alimentar pode negociar compras ou requisitar cereal. A requisição atende à urgência, mas amplia o conflito com a administração húngara.","The food commission may negotiate purchases or requisition grain. Requisition meets the emergency but deepens conflict with the Hungarian administration.",[("Comprar e compensar os produtores.","Purchase grain and compensate producers.",v("provisions",8)+" add_political_power = -50",85),("Requisitar os estoques.","Requisition stocks.",v("provisions",12)+" "+v("consent",-10)+" "+v("cohesion",-3),15)])
 event(12,"A produção e seus trabalhadores","Production and Its Workers","Uma emergência pode prolongar jornadas por 90 dias. A alternativa é financiar a negociação e preservar a confiança, com menos produção imediata.","An emergency may extend shifts for 90 days. The alternative is funding negotiations and preserving confidence, with less immediate output.",[("Negociar as condições de trabalho.","Negotiate working conditions.",v("cohesion",4)+" add_political_power = -40",75),("Adotar jornadas de emergência por 90 dias.","Adopt emergency shifts for 90 days.","add_timed_idea = { idea = AUH_ww1_emergency_shifts days = 90 } "+v("cohesion",-4),25,"has_war = yes")])
 event(13,"Uma emissão de crédito","A Credit Issue","Títulos podem financiar uma expansão industrial temporária de 2,5% por 180 dias, mas o serviço da dívida permanecerá na economia até a amortização.","Bonds can fund a temporary 2.5% industrial expansion for 180 days, but debt service remains in the economy until repayment.",[("Emitir uma série limitada.","Issue a limited series.","add_timed_idea = { idea = AUH_ww1_credit_expansion days = 180 } "+v("debt",1),35,"has_war = yes check_variable = { auh_ww1_debt < 6 } NOT = { has_idea = AUH_ww1_credit_expansion }"),("Conservar o limite de crédito.","Retain the credit limit.",v("consent",3)+" add_political_power = -20",65)])
 event(14,"O exército de várias administrações","An Army of Several Administrations","A unidade do exército depende de formação e abastecimento. Problemas de comunicação podem ser reformados; diversidade nacional não significa incapacidade militar.","Army unity depends on training and supply. Communication problems can be reformed; national diversity does not imply military incapacity.",[("Auditar a formação dos oficiais.","Audit officer training.","army_experience = 5 add_political_power = -20",80),("Consultar os comandos territoriais.","Consult territorial commands.",v("consent",3)+" add_political_power = -25",20)])
 event(15,"A prioridade do programa militar","The Military Programme's Priority","As escolas e os arsenais competem por recursos. Uma prioridade oferece auxílio de pesquisa limitado; outra dá experiência para reorganizar as reservas.","Schools and arsenals compete for resources. One priority offers limited research assistance; another provides experience to reorganise reserves.",[("Priorizar a pesquisa dos arsenais.","Prioritise arsenal research.","add_tech_bonus = { name = AUH_ww1_research_program bonus = .20 uses = 1 category = artillery }",50),("Priorizar a organização das reservas.","Prioritise reserve organisation.","army_experience = 8",50)])
 event(16,"A ofensiva e a reserva","Offensives and Reserves","O estado-maior deve escolher uma prioridade. Preparar ofensivas acelera o planejamento e aumenta o consumo de suprimentos. A escola defensiva favorece o entrincheiramento e planeja ofensivas mais lentamente.","The staff must choose a priority. Preparing offensives speeds planning and raises supply consumption. The defensive school favours entrenchment and plans offensives more slowly.",[("Adotar a escola defensiva.","Adopt the defensive school.","auh_ww1_set_defensive_staff = yes",70),("Adotar a escola ofensiva.","Adopt the offensive school.","auh_ww1_set_offensive_staff = yes",30)])
 event(17,"A política externa e seus limites","Foreign Policy and Its Limits","A posição balcânica da monarquia não garante uma guerra curta. A pressão externa pode ampliar o apoio à guerra, mas custa confiança das províncias.","The monarchy's Balkan position does not guarantee a short war. External pressure may raise war support, but costs provincial confidence.",[("Investir na acomodação.","Invest in accommodation.",v("cohesion",3)+" add_political_power = -30",60),("Sustentar uma postura de pressão.","Maintain a pressure policy.","add_war_support = .03 "+v("cohesion",-4),40)])
 event(18,"A casa imperial e a continuidade","The Imperial House and Continuity","A dinastia precisa preparar a continuidade dos serviços comuns. O protocolo não muda a cadeia internacional do atentado de Sarajevo; a sucessão de Carlos ocorrerá após a morte de Francisco José.","The dynasty must prepare continuity in common services. The protocol does not change the international Sarajevo assassination chain; Karl's accession follows Franz Joseph's death.",[("Preparar a administração da sucessão.","Prepare succession administration.",v("consent",3)+" add_political_power = -25",100)],picture="karl")
 event(19,"Coordenação sem submissão?","Coordination Without Submission?","A ligação alemã pode ajudar o estado-maior, mas maior coordenação cobra influência de Viena. A decisão não entrega territórios ou exércitos ao aliado.","The German connection can assist the staff, but deeper coordination costs Vienna influence. The decision cedes neither territory nor armies to the ally.",[("Preservar o controle de Viena.","Preserve Vienna's control.",v("consent",3)+" add_political_power = -30",70),("Financiar mais cursos conjuntos.","Fund more joint courses.","army_experience = 8 add_political_power = -50",30,"has_country_flag = auh_ww1_german_commission")])
 event(20,"Segurança civil na Bósnia","Civil Security in Bosnia","A presença imperial pode se apoiar em negociação civil ou em medidas repressivas. Nenhuma alternativa garante impedir atentados internacionais.","Imperial presence may rely on civil negotiation or repressive measures. Neither alternative guarantees preventing international assassinations.",[("Negociar garantias civis.","Negotiate civil guarantees.",v("cohesion",4)+" add_political_power = -40",80),("Impor medidas excepcionais.","Impose exceptional measures.",v("cohesion",-6)+" add_political_power = 20",20)])
 event(21,"Carlos e os objetivos da guerra","Karl and the War Aims","O novo imperador encontra um Estado que precisa sustentar várias frentes e negociar sua continuidade. Limitar objetivos custa apoio à guerra, mas ajuda a confiança interna.","The new emperor finds a state sustaining several fronts and negotiating its continuity. Limiting aims costs war support, but helps internal confidence.",[("Preparar uma solução negociada.","Prepare a negotiated solution.",v("cohesion",4)+" add_war_support = -.025",75),("Manter os objetivos existentes.","Retain existing aims.",v("consent",3)+" "+v("cohesion",-2),25)],picture="karl")
 event(22,"Uma marinha para o Adriático","A Navy for the Adriatic","Financiar os grandes cascos e preservar a frota são objetivos diferentes. O programa escolhe uma prioridade de pesquisa limitada, sem criar navios.","Funding large hulls and preserving the fleet are different aims. The programme chooses a limited research priority without creating ships.",[("Estudar os cascos de batalha.","Study battle hulls.","add_tech_bonus = { name = AUH_ww1_research_program bonus = .20 uses = 1 category = bb_tech }",30),("Priorizar navios leves e escolta.","Prioritise light ships and escorts.","add_tech_bonus = { name = AUH_ww1_research_program bonus = .20 uses = 1 category = dd_tech }",70)],picture="naval")
 event(23,"A paz e suas contas","Peace and Its Accounts","A paz interrompe a emergência militar, mas não apaga a dívida e a necessidade de reintegrar veteranos. Reconstruir serviços exige escolhas orçamentárias.","Peace ends the military emergency, but does not erase debt or the need to reintegrate veterans. Rebuilding services requires budget choices.",[("Priorizar a confiança dos sobreviventes.","Prioritise survivors' confidence.",v("cohesion",4)+" add_political_power = -35",70),("Priorizar o acordo entre administrações.","Prioritise the administrative agreement.",v("consent",4)+" add_political_power = -35",30)],picture="reconstruction")
 event(24,"Desmobilizar sem abandonar","Demobilise Without Abandoning","A reintegração tem um custo político e civil. A desmobilização real das divisões permanece nas mãos do jogador; não devolveremos mortos ao recrutamento.","Reintegration has a political and civilian cost. Actual division demobilisation remains in the player's hands; the dead are not returned to recruitment.",[("Financiar a reintegração civil.","Fund civilian reintegration.",v("cohesion",6)+" add_political_power = -60",80),("Adotar uma transição mais lenta.","Adopt a slower transition.",v("cohesion",3)+" add_political_power = -30",20)],picture="reconstruction")
 event(25,"O pacto depois da guerra","The Compact After the War","O Estado pode continuar sob a dinastia ou negociar uma constituição federal. A reforma precisa de consentimento de 50 e confiança de 60, mesmo depois da paz.","The state may continue under the dynasty or negotiate a federal constitution. Reform still requires 50 consent and 60 confidence, even after peace.",[("Manter a constituição vigente.","Retain the current constitution.",v("consent",3),70),("Ampliar o pacto federal.","Extend the federal compact.","auh_ww1_ratify_federation = yes",30,"NOT = { has_country_flag = auh_ww1_republic } check_variable = { auh_ww1_consent > 49 } check_variable = { auh_ww1_cohesion > 59 }")])
 event(26,"Representação vinculante ou consultiva","Binding or Consultative Representation","Uma assembleia republicana pode substituir a dinastia pela representação parlamentar. Essa alternativa exige paz, confiança provincial de 60 e uma concessão grande às administrações. Uma consulta preserva a monarquia.","A republican assembly may replace the dynasty with parliamentary representation. This alternative requires peace, provincial confidence of 60 and a major concession to administrations. A consultation preserves the monarchy.",[("Preservar a Coroa e ampliar consultas.","Preserve the Crown and expand consultations.",v("cohesion",4)+" add_political_power = -40",85),("Convocar uma assembleia republicana federal.","Convene a federal republican assembly.","auh_ww1_establish_republic = yes",15,"has_war = no check_variable = { auh_ww1_cohesion > 59 } NOT = { has_country_flag = auh_ww1_republic }")])
 event(27,"O futuro do Estado danubiano","The Future of the Danubian State","O resultado não é uma recompensa de vitória garantida. Manter o Estado exigiu controlar seus territórios e negociar alimentos, orçamento e representação. A continuidade ainda dependerá dessas escolhas.","The outcome is not a guaranteed victory reward. Retaining the state required controlling its territory and negotiating food, budgets and representation. Continuity still depends on those choices.",[("Renovar o pacto dos serviços comuns.","Renew the compact of common services.",v("consent",4)+" "+v("cohesion",4)+" add_political_power = -60",100)],picture="reconstruction")
 event(28,"O pacto interno está em risco","The Internal Compact Is at Risk","A confiança das províncias caiu abaixo de 25. O governo pode financiar uma concessão de emergência ou preservar o orçamento e aceitar a continuação da tensão. O evento não divide o país por data.","Provincial confidence has fallen below 25. The government may fund an emergency concession or preserve its budget and accept continuing tension. The event does not partition the country by date.",[("Financiar concessões de emergência.","Fund emergency concessions.",v("cohesion",8)+" "+v("consent",-4)+" add_political_power = -80",85),("Manter as atribuições existentes.","Retain existing powers.",v("cohesion",-3),15)])
 event(29,"O pão tornou-se uma urgência","Bread Has Become an Emergency","As reservas caíram abaixo de 30. As cidades pressionam a produção industrial, e a falta de distribuição prejudica a confiança. Retirar cereal exige manter a região agrícola sob controle.","Reserves have fallen below 30. Cities put pressure on industrial production and poor distribution undermines confidence. Obtaining grain requires retaining control of the agricultural region.",[("Comprar uma reserva de emergência.","Buy an emergency reserve.",v("provisions",8)+" add_political_power = -60",85,"controls_state = 43 controls_state = 154"),("Administrar a escassez com os recursos atuais.","Manage the shortage with current resources.",v("cohesion",-2),15)],picture="food")

 # Reciprocal proposals. Explicit AUS routing avoids nested ROOT/FROM mistakes.
 proposals=[(30,"GER","german_commission","comissão militar conjunta","joint military commission","military"),(32,"SER","serbian_trade","normalização comercial","trade normalisation","trade"),(34,"ALB","albanian_assistance","assistência civil","civil assistance","trade"),(36,"MNT","montenegrin_pact","pacto de não agressão","non-aggression pact","pact"),(38,"ITA","italian_consultation","consultas adriáticas","Adriatic consultations","pact"),(40,"ROM","romanian_grain","contrato de cereal","grain contract","trade"),(42,"SOV","russian_consultation","consultas diplomáticas","diplomatic consultations","pact"),(44,"FRA","sixtus_channel","mediação pelo canal de Sixtus","mediation through the Sixtus channel","peace")]
 for n,tag,flag,pt,en,kind in proposals:
  av=f"country_exists = {tag} NOT = {{ has_war_with = {tag} }}"
  if kind=="peace":av=f"country_exists = {tag} has_war_with = {tag}"
  event(n,"Uma proposta, dois governos","One Proposal, Two Governments",f"A proposta de {pt} só existe se o governo destinatário aceitar. Precisamos financiar a delegação e aguardar sua resposta.",f"The proposal for {en} exists only if the recipient government accepts. We must fund the delegation and await its reply.",[("Enviar uma proposta formal.","Send a formal proposal.",f"add_political_power = -35 {tag} = {{ country_event = {{ id = ww1_auh.{n+1} days = 3 }} }}",90,av),("Conservar os recursos diplomáticos.","Conserve diplomatic resources.",v("consent",1),10)])
  agree=f"AUS = {{ set_country_flag = auh_ww1_{flag} country_event = {{ id = ww1_auh.48 days = 1 }} }} add_opinion_modifier = {{ target = AUS modifier = AUH_ww1_agreement }}"
  if kind=="pact":agree+=" set_country_flag = { flag = auh_ww1_consultation_authorised days = 365 }"
  if kind=="peace":agree+=" set_country_flag = { flag = auh_ww1_mediation_authorised days = 180 }"
  if tag=="MNT":agree+=" diplomatic_relation = { country = AUS relation = non_aggression_pact active = yes }"
  if tag=="ALB":agree+=" add_political_power = 15 AUS = { add_political_power = -20 }"
  valid="country_exists = AUS NOT = { has_war_with = AUS }" if kind!="peace" else "country_exists = AUS has_war_with = AUS"
  event(n+1,"Uma proposta de Viena","A Proposal from Vienna",f"Viena propõe {pt}. Podemos aceitar o canal ou recusar. A aceitação não obriga a entrar em guerras e não muda fronteiras.",f"Vienna proposes {en}. We may accept the channel or refuse. Acceptance does not compel entry into wars or change borders.",[("Aceitar a proposta nas condições atuais.","Accept the proposal under current conditions.",agree,60,valid),("Recusar a proposta.","Refuse the proposal.","if = { limit = { country_exists = AUS } AUS = { country_event = { id = ww1_auh.49 days = 1 } } }",40)])
  # A rejected or withdrawn proposal can be revisited; refusal is not a permanent tree lock.
  fk={30:"berlin_mission",32:"belgrade_channel",34:"albanian_contacts",36:"montenegrin_channel",38:"rome_channel",40:"bucharest_channel",42:"russian_channel",44:"sixtus_channel"}[n]
  decision("diplomacy","renew_"+flag,"Reabrir: "+pt,"Reopen: "+en,"Após uma recusa, a delegação pode apresentar a proposta novamente. O destinatário mantém o direito de recusar; o envio custa mais 35 de influência.","After a refusal, the delegation may resubmit the proposal. The recipient retains the right to refuse; sending costs another 35 political power.",f"{tag} = {{ country_event = {{ id = ww1_auh.{n+1} days = 3 }} }}",f"has_country_flag = auh_ww1_consular_contacts_unlocked has_completed_focus = {P+fk}",av+f" NOT = {{ has_country_flag = auh_ww1_{flag} }}",pp=35,days=1,reenable=180,cancel="has_war_with = "+tag if kind!="peace" else "NOT = { has_war_with = "+tag+" }",ai=.5)
 event(46,"Uma proposta de armistício da monarquia","An Armistice Proposal from the Monarchy","Viena oferece paz sem anexações e pede autorização para uma conferência. A guerra continua enquanto qualquer beligerante recusar. A autorização, se concedida, vence em 120 dias.","Vienna offers peace without annexations and requests authorisation for a conference. War continues while any belligerent refuses. Authorisation, if granted, expires in 120 days.",[("Autorizar a conferência por 120 dias.","Authorise the conference for 120 days.","set_country_flag = { flag = auh_ww1_armistice_consent days = 120 } if = { limit = { country_exists = AUS } AUS = { country_event = { id = ww1_auh.48 days = 1 } } }",20,"country_exists = AUS has_war_with = AUS"),("Prosseguir a guerra.","Continue the war.","clr_country_flag = auh_ww1_armistice_consent if = { limit = { country_exists = AUS } AUS = { country_event = { id = ww1_auh.49 days = 1 } } }",80)])
 event(48,"A proposta foi aceita","The Proposal Was Accepted","O governo destinatário aceitou nosso canal de negociação. Os compromissos dependem de sua validade diplomática e não garantem o comportamento futuro de outro país.","The recipient government accepted our negotiation channel. Commitments depend on their diplomatic validity and do not guarantee another country's future behaviour.",[("Financiar a implementação do acordo.","Fund implementation of the agreement.",v("consent",2)+" add_political_power = -10",100)])
 event(49,"A proposta foi recusada","The Proposal Was Refused","O governo destinatário não aceitou nossa proposta. A despesa diplomática já foi realizada, e nenhuma garantia ou vantagem de tratado entrou em vigor.","The recipient government did not accept our proposal. Diplomatic expenditure has already occurred, and no guarantee or treaty advantage entered into force.",[("Reavaliar nossa posição.","Reassess our position.",v("consent",-1),100)])
 event(50,"A sucessão de Carlos","Karl's Accession","Francisco José morreu. Carlos assume a chefia da monarquia, com a constituição e as dificuldades deixadas pela campanha. Sua ascensão não remove dívida, fome ou crises militares.","Franz Joseph has died. Karl assumes leadership of the monarchy with the constitution and difficulties left by the campaign. His accession removes neither debt, hunger nor military crises.",[("Preservar a continuidade dos serviços.","Preserve continuity of services.",v("consent",2),100)],picture="karl")
 put("events/ww1_austria_hungary_events.txt","\n".join(events))
 put("common/opinion_modifiers/ww1_austria_hungary_opinions.txt","opinion_modifiers = { AUH_ww1_agreement = { value = 15 decay = 1 } }")
 loc(P+"agreement","Entendimento com Viena","Understanding with Vienna")

 # Separate services keep late focuses from merely unlocking a decision already available.
 services=[
 ("economy","economic_coordination","Coordenar as estatísticas comuns","Coordinate Common Statistics",v("consent",3),"",60,1,35),
 ("economy","investments","Avaliar os projetos de investimento","Evaluate Investment Projects","add_tech_bonus = { name = AUH_ww1_investment_review bonus = .15 uses = 1 category = construction_tech }","",90,1,40),
 ("military","artillery_supply","Preparar depósitos de artilharia","Prepare Artillery Depots","army_experience = 6","has_equipment = { artillery_equipment > 19 support_equipment > 29 }",60,1,35),
 ("military","defensive_sectors","Treinar comandos de defesa por setor","Train Sector Defence Commands","army_experience = 6 add_mastery_bonus = { name = AUH_ww1_sector_training bonus = .08 days = 90 folder = land }","has_war = yes",90,1,40),
 ("military","italian_contingency","Ensaiar a contingência italiana","Rehearse the Italian Contingency","army_experience = 6","has_war_with = ITA",60,1,35),
 ("military","eastern_contingency","Ensaiar a contingência oriental","Rehearse the Eastern Contingency","army_experience = 6","has_war_with = SOV",60,1,35),
 ("diplomacy","allied_liaison","Financiar a ligação com a frente aliada","Fund Liaison with the Allied Front","army_experience = 8","country_exists = GER has_war_together_with = GER has_country_flag = auh_ww1_german_commission",90,1,40),
 ("diplomacy","foreign_programme","Negociar o mandato diplomático comum","Negotiate a Common Diplomatic Mandate",v("consent",4),"check_variable = { auh_ww1_consent < 85 }",60,0,40),
 ("diplomacy","postwar_diplomacy","Organizar a delegação comercial de paz","Organise the Peacetime Trade Delegation",v("consent",3)+" "+v("provisions",3),"has_war = no",90,1,40),
 ("military","naval_programme","Financiar os quadros do Almirantado","Fund Admiralty Cadres","navy_experience = 5","",90,1,35),
 ("crown","reconstruction","Financiar a administração da reconstrução","Fund Reconstruction Administration",v("cohesion",4),"has_war = no check_variable = { auh_ww1_cohesion < 85 }",90,1,40),
 ("economy","peace_accounts","Auditar o orçamento da paz","Audit the Peacetime Budget",v("consent",5),"has_war = no check_variable = { auh_ww1_consent < 85 }",90,1,40)]
 for cat,flag,pt,en,eff,av,days,civs,pp in services:
  spend=""
  if flag=="artillery_supply":spend="add_equipment_to_stockpile = { type = artillery_equipment amount = -20 } add_equipment_to_stockpile = { type = support_equipment amount = -30 }"
  if civs:av+=f" num_of_civilian_factories_available_for_projects > {civs-1}"
  descpt=f"O serviço exige {pp} de influência, {civs} fábrica civil e {days} dias. Seu efeito só chega ao fim do trabalho."
  descen=f"The service requires {pp} political power, {civs} civilian factory and {days} days. Its effect arrives only when work finishes."
  if flag=="artillery_supply":descpt+=" Consome 20 peças de artilharia e 30 equipamentos de apoio na contratação.";descen+=" It consumes 20 artillery and 30 support equipment on commissioning."
  decision(cat,"service_"+flag,pt,en,descpt,descen,eff,f"has_country_flag = auh_ww1_{flag}_unlocked",av,pp=pp,days=days,factories=civs,once=flag in ["investments","artillery_supply","italian_contingency","eastern_contingency","naval_programme"],reenable=180,complete=spend)
 loc(P+"investment_review","Avaliação de investimentos","Investment Review")
 loc(P+"sector_training","Instrução dos comandos por setor","Sector Command Instruction")
 for a in focuses:
  if a['id'] in [P+x for x in ['bohemian_landtag','galician_autonomy','slovak_petitions','dalmatian_services']]:
   a['parent']=['dual_war_cabinet','trialist_war_cabinet','federal_war_cabinet']
  if a['id'] in [P+"common_customs",P+"trialist_war_cabinet"]:a['available']+=" has_country_flag = auh_ww1_trialist_constitution"
  if a['id'] in [P+"federal_common_army",P+"federal_war_cabinet"]:a['available']+=" has_country_flag = auh_ww1_federal_constitution"
  if a['id']==P+"german_staff_exchange":a['available']+=" has_country_flag = auh_ww1_german_commission"
  if a['id']==P+"romanian_grain":a['available']+=" has_country_flag = auh_ww1_romanian_grain"
  if a['id']==P+"adriatic_consultation":a['available']+=" has_country_flag = auh_ww1_italian_consultation"
 for cat,parts in decisions.items():put(f"common/decisions/ww1_auh_{cat}.txt",P+cat+" = {\n"+"\n".join(parts)+"\n}")
 for key,pt,en in [("research_program","Programa de pesquisa da monarquia","Monarchy Research Programme"),("operational_lessons","Aprendizado das operações","Operational Learning"),("air_training","Formação do serviço aéreo","Air Service Training"),("naval_training","Formação da esquadra","Fleet Training")]:loc(P+key,pt,en)
 put("docs/auh_project_catalogue.json",json.dumps(projects,ensure_ascii=False,indent=2))
