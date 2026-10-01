---
name: hoi4-events-narrative-engine
description: >-
  Specialized authoring manual for Hearts of Iron IV event chains, diplomatic ultimatums,
  news dispatches, historical narrative pacing, AI weighting, dynamic tooltips, and
  Clausewitz event namespace integrity.
---

# HOI4 Events & Narrative Engine

This skill provides the architectural guidelines, Paradox script standards, narrative frameworks, and validation tools for building immersive historical and alternative-history event systems in Hearts of Iron IV.

Use this skill whenever authoring country events, global news bulletins, diplomatic negotiations, crisis escalations, or historical character storylines.

---

## 1. Event Architecture & Namespace Integrity

Every event file in `events/<country>_events.txt` must declare its namespace at the very first line before any event blocks are opened:

```pdx
add_namespace = ww1_germany
add_namespace = ww1_news
```

### Critical Namespace Rules
1. **Never Reuse Namespaces**: A namespace must be unique across all active mod files.
2. **Naming Convention**:
   - Country Events: `<namespace>.<number>` (e.g. `ww1_germany.100`) or `<namespace>.<subsystem>_<id>` (e.g. `ww1_germany.agadir_crisis`).
   - News Events: `ww1_news.<number>`.
3. **Localisation Key Binding**:
   - Title: `<event_id>.t`
   - Description: `<event_id>.d`
   - Options: `<event_id>.a`, `<event_id>.b`, `<event_id>.c`, etc.

---

## 2. The Chain-Reaction Event Pattern (Diplomatic Ultimatums & Crises)

In multi-nation historical events (e.g. The July Crisis, Ultimatum to Belgium, Brest-Litovsk Negotiations), events must never occur in isolation. They form a closed causal loop:

```
[National Focus]
      │
      ▼
Event 1: Sender issues ultimatum (GER)
      │ (fires via country_event = { id = ww1_belgium.1 days = 1 })
      ▼
Event 2: Target receives ultimatum (BEL)
      ├── Option A: Capitulate / Grant Military Access
      │     └── Fires Event 3 to GER: "Belgium Yields"
      │
      └── Option B: Defy / Defend Neutrality (Historical)
            ├── Fires Event 4 to GER: "Belgium Resists" -> War declared
            └── Fires Event 5 to ENG: "Scrap of Paper Violated" -> UK intervenes
```

### Complete Code Implementation:
```pdx
# -------------------------------------------------------------
# STEP 1: GERMANY SENDS ULTIMATUM
# -------------------------------------------------------------
country_event = {
    id = ww1_germany.ultimatum_belgium
    title = ww1_germany.ultimatum_belgium.t
    desc = ww1_germany.ultimatum_belgium.d
    picture = GFX_report_event_german_troops
    
    is_triggered_only = yes
    
    option = {
        name = ww1_germany.ultimatum_belgium.a  # "Send the ultimatum to Brussels"
        BEL = {
            country_event = { id = ww1_belgium.german_ultimatum days = 1 }
        }
        custom_effect_tooltip = ww1_germany_ultimatum_sent_tt
    }
}

# -------------------------------------------------------------
# STEP 2: BELGIUM RECEIVES DEMAND
# -------------------------------------------------------------
country_event = {
    id = ww1_belgium.german_ultimatum
    title = ww1_belgium.german_ultimatum.t
    desc = ww1_belgium.german_ultimatum.d
    picture = GFX_report_event_belgian_king
    
    is_triggered_only = yes
    
    # Historical Choice: Refuse
    option = {
        name = ww1_belgium.german_ultimatum.refuse
        ai_chance = {
            factor = 95
            modifier = {
                factor = 0
                is_historical_focus_on = no
                has_government = fascism
            }
        }
        GER = {
            country_event = { id = ww1_germany.belgium_refused days = 1 }
        }
        ENG = {
            country_event = { id = ww1_britain.belgian_neutrality_violated days = 1 }
        }
    }
    
    # Alternative Choice: Accept German Transit
    option = {
        name = ww1_belgium.german_ultimatum.accept
        ai_chance = {
            factor = 5
        }
        GER = {
            give_military_access = yes
            country_event = { id = ww1_germany.belgium_accepted days = 1 }
        }
        add_stability = -0.20
    }
}
```

---

## 3. Country Events vs Global News Events

### A. Country Event (Targeted Popup)
Pops up only for the recipient nation:
```pdx
country_event = {
    id = ww1_germany.spartakus_uprising
    title = ww1_germany.spartakus_uprising.t
    desc = ww1_germany.spartakus_uprising.d
    picture = GFX_report_event_spartakus_revolt
    
    is_triggered_only = yes
    
    option = {
        name = ww1_germany.spartakus_uprising.crush
        start_civil_war = {
            ideology = communism
            size = 0.35
            capital = 64
        }
    }
}
```

### B. Global News Event (Worldwide Broadcast)
Appears in the newspaper popup for all or relevant world powers:
```pdx
news_event = {
    id = ww1_news.archduke_assassinated
    title = ww1_news.archduke_assassinated.t
    desc = ww1_news.archduke_assassinated.d
    picture = GFX_news_event_sarajevo_assassination
    
    major = yes
    is_triggered_only = yes
    
    option = {
        name = ww1_news.archduke_assassinated.a
        trigger = { tag = AUS }
        add_war_support = 0.15
    }
    
    option = {
        name = ww1_news.archduke_assassinated.b
        trigger = { tag = SER }
        add_war_support = 0.10
    }
    
    option = {
        name = ww1_news.archduke_assassinated.c
        trigger = {
            NOT = { tag = AUS }
            NOT = { tag = SER }
        }
    }
}
```

---

## 4. Trigger Optimization (`is_triggered_only` vs Periodic)

> [!TIP]
> **Performance Optimization**: Always set `is_triggered_only = yes` for events called from focuses, decisions, or other events. Periodic tick checks (`mean_time_to_happen`) degrade game tick speed when multiplied across hundreds of events.

If an event MUST fire independently without a focus, use strict `trigger` conditions and reasonable MTTH:
```pdx
country_event = {
    id = ww1_germany.turnip_winter_starts
    title = ww1_germany.turnip_winter_starts.t
    desc = ww1_germany.turnip_winter_starts.d
    picture = GFX_report_event_food_shortage
    
    fire_only_once = yes
    
    trigger = {
        tag = GER
        has_war = yes
        date > 1916.11.1
        date < 1917.4.1
        NOT = { has_country_flag = turnip_winter_avoided }
    }
    
    mean_time_to_happen = {
        days = 15
        modifier = {
            factor = 0.5
            has_war_with = ENG
        }
    }
    
    option = {
        name = ww1_germany.turnip_winter_starts.a
        add_ideas = GER_turnip_winter_crisis_1
    }
}
```

---

## 5. Immersion & Narrative Tooltips

Clausewitz scripts often produce ugly, cluttered automated tooltips (e.g., exposing variable modifications, cosmetic tag resets, and dummy idea removals). 

Use `custom_effect_tooltip` and `hidden_effect` to present clean, immersive text to the player:

```pdx
option = {
    name = ww1_russia.treaty_of_brest_litovsk.accept
    
    # Custom narrative tooltip visible to the player
    custom_effect_tooltip = ww1_russia_brest_litovsk_consequences_tt
    
    # Internal execution hidden from messy GUI
    hidden_effect = {
        transfer_state = 188
        transfer_state = 189
        GER = { puppet = UKR }
        GER = { puppet = POL }
        clr_country_flag = wartime_emergency_powers
        set_cosmetic_tag = SOV_soviet_russia
    }
}
```

---

## 6. Pre-Flight Checklist for Events

Before shipping an event script:
1. Verify `add_namespace = <namespace>` is at the top of the file.
2. Ensure every event ID matches `<namespace>.<name>`.
3. Check that every `option` has a localized name key (`<event_id>.<option_letter>`).
4. Ensure every referenced country tag (`BEL`, `ENG`, `GER`, etc.) exists.
5. Run the events validator:
```powershell
python scripts/validate_events.py --events events/<country>_events.txt
```
