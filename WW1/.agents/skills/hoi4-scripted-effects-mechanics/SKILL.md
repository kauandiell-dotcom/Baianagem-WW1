---
name: hoi4-scripted-effects-mechanics
description: >-
  Specialized engineering manual for Hearts of Iron IV advanced scripting, dynamic mechanics,
  timed missions, cascading national spirits, scripted civil wars, real regime change protocols,
  decision categories, and war/peace state transitions.
---

# HOI4 Scripted Effects & Dynamic Game Mechanics

This skill provides the comprehensive implementation guidelines, Paradox script syntax standards, and verified code patterns for game mechanics that move far beyond static stat buffs. 

Use this skill whenever designing or implementing political revolutions, civil wars, timed operational breakthroughs, decision systems, national ideas, or scripted military/diplomatic crises.

---

## 1. Real Regime Changes & Power Transfer Protocol

Never write a political focus that merely adds political power or stability without changing the actual government structure.

### A. Valid Ideology Group Names (Clausewitz Core)
HoI4 vanilla and total conversion mods structure ideologies into 4 core parent groups unless custom groups are registered in `common/ideologies/`:
- `democratic`
- `communism`
- `fascism`
- `neutrality` (used for monarchies, military juntas, non-aligned oligarchies)

> [!CAUTION]
> Using tokens like `liberalism`, `socialism`, `monarchy`, or `authoritarian` inside `set_politics = { ruling_party = ... }` or `start_civil_war = { ideology = ... }` will cause a game crash or silent script failure if they are sub-ideologies (types) rather than root ideology groups!

### B. Complete Regime Transition Code Block
When a focus or event changes the country's government:
```pdx
completion_reward = {
    # 1. Update Ruling Party and Electoral Status
    set_politics = {
        ruling_party = democratic
        elections_allowed = yes
    }
    
    # 2. Rebalance Popularities (Must sum up cleanly)
    set_popularities = {
        democratic = 65
        neutrality = 20
        communism = 10
        fascism = 5
    }
    
    # 3. Promote Leader Character
    promote_character = TAG_friedrich_ebert
    
    # 4. Set Country Cosmetic Flag / Dynamic Name & Flag
    set_cosmetic_tag = TAG_weimar_republic
    
    # 5. Swap National Spirits
    if = {
        limit = { has_idea = TAG_imperial_autocracy }
        swap_ideas = {
            remove_idea = TAG_imperial_autocracy
            add_idea = TAG_republican_constitution
        }
    }
    
    # 6. Notify World or Country
    country_event = { id = TAG_politics.republic_proclaimed days = 1 }
}
```

---

## 2. Operational Timed Missions & Breakthrough Mechanics

Missions place high-stakes countdown timers in the player's Decisions tab, driving dynamic gameplay with rewards for success and penalties for stagnation.

### A. Activating the Mission from a Focus
```pdx
focus = {
    id = TAG_operation_michael_offensive
    icon = GFX_focus_offensive
    cost = 5   # 35 days
    
    completion_reward = {
        set_country_flag = TAG_michael_offensive_active
        add_timed_idea = {
            idea = TAG_shock_offensive_buff
            days = 60
        }
        activate_mission = TAG_capture_amiens_mission
    }
}
```

### B. Defining the Mission in `common/decisions/<tag>_decisions.txt`
```pdx
TAG_capture_amiens_mission = {
    icon = generic_assault
    days_mission_timeout = 45
    is_good = no                  # Makes timer red/urgent if it's a deadline
    
    activation = {
        has_country_flag = TAG_michael_offensive_active
    }
    
    available = {
        controls_state = 18       # Amiens / Somme objective
    }
    
    cancel_trigger = {
        has_capitulated = yes
    }
    
    # SUCCESS: Objective captured before timer ran out
    complete_effect = {
        clr_country_flag = TAG_michael_offensive_active
        remove_ideas = TAG_shock_offensive_buff
        add_ideas = TAG_breakthrough_momentum
        add_stability = 0.10
        add_war_support = 0.10
        country_event = { id = TAG_offensive.amiens_captured }
    }
    
    # FAILURE: Timer expired without capturing objective
    timeout_effect = {
        clr_country_flag = TAG_michael_offensive_active
        remove_ideas = TAG_shock_offensive_buff
        add_timed_idea = {
            idea = TAG_exhausted_assault_divisions
            days = 90
        }
        add_stability = -0.15
        add_war_support = -0.15
        country_event = { id = TAG_offensive.offensive_stalled }
    }
}
```

---

## 3. Dynamic Idea Swapping & Escalation (National Spirits)

Never leave national spirits static. As war progresses, economic blockade tightens, or political reforms pass, spirits should evolve through cascading tiers.

### A. The `swap_ideas` Mechanism
Directly replacing an idea with `swap_ideas` preserves GUI ordering and prevents frame drops caused by removing and re-adding ideas in separate steps:
```pdx
swap_ideas = {
    remove_idea = TAG_food_rationing_tier_1
    add_idea = TAG_food_rationing_tier_2
}
```

### B. Tiered Idea Definition in `common/ideas/<category>.txt`
```pdx
ideas = {
    country = {
        TAG_food_rationing_tier_1 = {
            picture = GFX_idea_food_rationing
            allowed = { always = yes }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = 0.03
                stability_factor = -0.05
            }
        }
        
        TAG_food_rationing_tier_2 = {
            picture = GFX_idea_food_rationing_strict
            allowed = { always = yes }
            removal_cost = -1
            modifier = {
                consumer_goods_factor = 0.07
                stability_factor = -0.12
                weekly_stability = -0.002
                surrender_limit = -0.05
            }
        }
    }
}
```

### C. Commonly Used Engine Modifiers
- `industrial_capacity_factory = 0.10` (Factory output +10%)
- `industrial_capacity_dockyard = 0.15` (Dockyard output +15%)
- `production_speed_buildings_factor = 0.10` (Construction speed +10%)
- `consumer_goods_factor = -0.05` (-5% consumer goods needed)
- `army_org_factor = 0.08` (Army max organization +8%)
- `army_attack_factor = 0.05` (Division attack +5%)
- `army_defence_factor = 0.10` (Division defense +10%)
- `training_time_army_factor = -0.10` (Recruitment speed +10%)
- `conscription_factor = 0.05` (+5% recruitable population)
- `political_power_gain = 0.20` (+0.20 daily political power)
- `stability_weekly = 0.001` (+0.1% stability weekly)

---

## 4. Scripted Civil Wars without Infinite Stalemates

A frequent bug in HoI4 modding is a scripted civil war that drags on for 5 in-game years because the rebel nation has high surrender limit and no frontline movement.

### A. Robust Civil War Template
```pdx
start_civil_war = {
    ruling_party = communism           # The faction player or AI will now lead
    ideology = neutrality              # The opposing reactionary faction
    size = 0.35                        # 35% of states/army split to the rebels
    capital = 64                       # Specific capital state for rebel tag (D1)
    keep_unit_leaders = { 101 102 }    # IDs of generals who remain loyal
}

# Apply emergency wartime focus buffs to force decisive battle:
hidden_effect = {
    add_timed_idea = {
        idea = TAG_revolutionary_fervor_temporary
        days = 120
    }
}
```

### B. Preventing Permanent Stalemates
1. Set low surrender limits on rebel tag via cosmetic/scripted ideas:
   `surrender_limit = -0.30`
2. Implement a timeout white peace or automatic collapse event after 180 days if neither side has capitulated.

---

## 5. Decisions & Decision Categories Setup

Decisions allow granular player interactions on the map (infrastructure investments, foreign loans, propaganda campaigns).

### A. Register Category (`common/decisions/categories/<tag>_categories.txt`)
```pdx
TAG_mitteleuropa_investments = {
    icon = GFX_decision_category_economy
    priority = 80
    allowed = {
        tag = TAG
    }
    visible = {
        has_completed_focus = TAG_mitteleuropa_charter
    }
}
```

### B. Standard Decision (`common/decisions/<tag>_decisions.txt`)
```pdx
TAG_invest_in_romanian_oil = {
    icon = generic_oil
    
    cost = 50
    fire_only_once = no
    days_re_enable = 120
    
    allowed = { tag = TAG }
    
    visible = {
        ROM = { exists = yes }
        NOT = { has_war_with = ROM }
    }
    
    available = {
        has_political_power > 50
        num_of_civilian_factories_available_for_projects > 2
    }
    
    complete_effect = {
        add_political_power = -50
        ROM = {
            add_extra_state_shared_building_slots = 2
            add_building_construction = {
                type = synthetic_refinery
                level = 1
                instant_build = yes
            }
            country_event = { id = TAG_trade.investment_received }
        }
    }
    
    ai_will_do = {
        factor = 10
        modifier = {
            factor = 2
            has_war = yes
        }
    }
}
```

---

## 6. Verification and Syntax Safety Checklist

Before committing any mechanics script:
1. Verify that `ruling_party` matches an existing parent ideology (`democratic`, `communism`, `fascism`, `neutrality`).
2. Verify that every idea referenced in `swap_ideas` or `add_ideas` exists in `common/ideas/`.
3. Verify that all target state IDs exist in `history/states/`.
4. Ensure all decisions belong to an existing category defined in `common/decisions/categories/`.
5. Run the syntax validator:
```powershell
python scripts/verify_mechanics_syntax.py --dir common/
```
