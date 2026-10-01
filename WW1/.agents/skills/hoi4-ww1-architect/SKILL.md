---
name: hoi4-ww1-architect
description: >-
  Master framework, design methodology, scripts, and debugging runbook for creating
  massive, bug-free, historically authentic Hearts of Iron IV National Focus Trees
  for WW1 mods (Baianagem-WW1). Covers 5-wing layout architecture, dynamic path isolation
  (allow_branch), political power transfers, timed missions, decision integration,
  GFX sprite registration, and bilingual UTF-8 BOM localization.
---

# Hearts of Iron IV: WW1 Focus Tree Architect & Fast Debug Pipeline

This skill contains the unified architectural principles, design patterns, automated scripts, and debugging runbooks learned from developing the German Empire (Deutsches Kaiserreich) focus tree. Use this skill whenever creating or overhauling focus trees for major powers (France, Britain, Russia, Austria-Hungary, Ottoman Empire, Italy, USA) or important regional minors (Serbia, Romania, Bulgaria, Belgium, Greece, Portugal, etc.).

---

## 1. The 5-Wing Spatial Architecture (Visual Layout Standard)

To prevent visual clutter, overlapping horizontal lines, and spaghetti branches across columns, every national focus tree MUST be partitioned into **5 distinct thematic wings** along the X-axis:

Wing | Theme | Recommended X-Range | Key Sub-branches
:--- | :--- | :--- | :---
**Wing 1** | Internal Politics & Ideologies | `x: 1 - 25` | Monarchism, Socialism, Liberal Democracy, Ultranationalism
**Wing 2** | Economy, Infrastructure & Food | `x: 26 - 49` | Heavy Industry, Railways, Rationing, Raw Materials, Blockade
**Wing 3** | Navy & Air Forces | `x: 50 - 74` | Battlefleet (Dreadnoughts), Submarines (U-Boats), Zeppelins, Fighters
**Wing 4** | Army, General Staff & Fronts | `x: 75 - 110` | General Staff, Western Front, Eastern Front, Doctrines, Stormtroopers
**Wing 5** | Diplomacy, Weltpolitik & Alliances | `x: 111 - 135` | Major Treaties, Regional Pacts, Neutral Relations, Colonial Fronts

### Geometric Layout Rules
1. **Forward Progression Only**: `child.y > parent.y` strictly (`dy >= 1`).
2. **Never Backward Edges**: `dy < 0` causes arrows pointing upwards on the screen — this is a critical visual bug.
3. **Never Same-Row Horizontal Edges**: `dy == 0` causes line rendering directly through other focus boxes on the same horizontal row.
4. **Vertical Jump Limit**: Keep `dy <= 2` (ideally `dy = 1`). Never jump `dy > 2` as it cuts across intermediate rows.
5. **Horizontal Spread**: Keep column connections tight (`dx <= 3`). Avoid cross-wing spaghetti lines (`dx > 4`).

---

## 2. Dynamic Gating & Branch Isolation Pattern (`allow_branch`)

In HoI4, `mutually_exclusive = { focus = B }` prevents selecting B if A is taken, but B **remains on screen forever**, cluttering the view.

To achieve clean, professional trees where choosing a path dynamically collapses incompatible branches:

```pdx
focus = {
    id = TAG_historical_path_root
    x = 15
    y = 4
    allow_branch = {
        NOT = { has_country_flag = TAG_alt_political_path_chosen }
    }
    completion_reward = {
        set_country_flag = TAG_historical_path_chosen
        # ...
    }
}

focus = {
    id = TAG_socialist_path_root
    x = 3
    y = 4
    allow_branch = {
        NOT = { has_country_flag = TAG_historical_path_chosen }
        NOT = { has_country_flag = TAG_democratic_path_chosen }
        NOT = { has_country_flag = TAG_nationalist_path_chosen }
    }
    completion_reward = {
        set_country_flag = TAG_socialist_path_chosen
        set_country_flag = TAG_alt_political_path_chosen
        # ...
    }
}
```

*When an `allow_branch` on a root focus evaluates to false, HoI4 automatically hides that focus AND all of its descendant children!*

---

## 3. Real Political Power Transfers & Ideology Mechanics

Never just add political power or stability. Foci must execute real regime changes:

### A. Valid Ideology Names in HoI4
* `democratic` (NOT `liberalism`)
* `communism` (NOT `marxism`)
* `fascism` (NOT `fascism_ideology`)
* `neutrality` (NOT `despotism`)

### B. Standard Power Transfer Block
```pdx
completion_reward = {
    set_politics = {
        ruling_party = democratic
        elections_allowed = yes
    }
    set_popularities = {
        democratic = 65
        neutrality = 25
        communism = 10
    }
    promote_character = TAG_democratic_leader
    set_cosmetic_tag = TAG_democratic_cosmetic
}
```

### C. Civil War Target Rule
When a focus sparks a revolution to play as the new regime, the opponent must be the old regime:
```pdx
start_civil_war = {
    ideology = neutrality   # Reactionary monarchists rebel
    size = 0.35
    capital = <rebel_state_id>
}
```

---

## 4. Operational War Mechanics (Missions, Timers & Penalties)

Never use boring flat "+10% attack" buffs as the foundation of military design. Link operations to real operational challenges:

### The Timed Mission Pattern
1. Focus grants operational idea (`TAG_offensive_momentum`) and activates mission:
   `activate_mission = TAG_mission_capture_objective`
2. In `common/decisions/TAG_decisions.txt`:
```pdx
TAG_mission_capture_objective = {
    days_mission_timeout = 25
    available = { controls_state = <target_state_id> }
    activation = { has_country_flag = TAG_offensive_launched }
    complete_effect = {
        remove_ideas = TAG_offensive_momentum
        add_ideas = TAG_victory_triumph
        country_event = { id = TAG_events.victory }
    }
    timeout_effect = {
        remove_ideas = TAG_offensive_momentum
        add_timed_idea = { idea = TAG_offensive_hangover days = 30 }
        country_event = { id = TAG_events.failure_trench_stalemate }
    }
}
```

---

## 5. GFX Sprite Pipeline

1. **Sources**:
   - `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2716194283` (Europe In Flames)
   - `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3365515312` (The Great War Redux)
2. **Naming Convention**: `GFX_<TAG>_<focus_name>`
3. **Registration Template in `interface/<TAG>_goals.gfx`**:
```pdx
SpriteType = {
    name = "GFX_GER_Sturmtruppen"
    texturefile = "gfx/interface/goals/GER_Sturmtruppen.png"
}
SpriteType = {
    name = "GFX_GER_Sturmtruppen_shine"
    texturefile = "gfx/interface/goals/GER_Sturmtruppen.png"
    effectFile = "gfx/FX/buttonstate.lua"
    animation = {
        animationmaskfile = "gfx/interface/goals/GER_Sturmtruppen.png"
        animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
        animationrotation = -90.0
        animationlooping = no
        animationtime = 0.75
        animationdelay = 0
        animationblendmode = "add"
        animationtype = "scrolling"
        animationrotationoffset = { x = 0.0 y = 0.0 }
        animationtexturescale = { x = 1.0 y = 1.0 }
    }
    legacy_lazy_load = no
}
```

---

## 6. Bilingual Localization Rules (UTF-8 BOM Mandatory)

1. **Files**:
   - `localisation/english/<TAG>_focus_l_english.yml`
   - `localisation/braz_por/<TAG>_focus_l_braz_por.yml`
2. **Encoding**: Must start with byte order mark `\xef\xbb\xbf` (UTF-8 with BOM).
3. **Comment Rule**: Only use `#` for comments. Never use Lua `--` comments.
4. **Quotation Rule**: Only use ASCII `"` (U+0022). Never use curly quotes `”` or `“` (U+201D / U+201C).
5. **Path Badges**:
   - `[Historical]` / `[Histórico]`
   - `[Alternative - Democratic]` / `[Alternativo - Democrático]`
   - `[Alternative - Socialist]` / `[Alternativo - Socialista]`
   - `[Alternative - Nationalist]` / `[Alternativo - Nacionalista]`

---

## 7. Fast Automated Pre-Flight Check Suite

Before delivering any focus tree, run the standardized audit scripts:
1. `python tests/audit_visual_bugs.py` — Check (x, y) coordinates, upward edges, row collisions.
2. `python tests/check_textures.py` — Ensure 0 missing spriteTypes and 0 missing physical files.
3. `python tests/check_focus_graph.py` — Check 100% DAG integrity, 0 cycles, valid prerequisites.
4. `python tests/check_yaml_syntax.py` — Verify BOM, quote balancing, and comment syntax.
5. `python tests/check_decisions.py` — Verify decision categories and missions.
6. `python tests/test_runner.py` — Run the master test runner (must achieve 100% PASS).
7. `robocopy <mod_dir> <steam_dir> /MIR ...` — Sync to active Steam workshop folder.
