---
name: hoi4-focus-tree-designer
description: >-
  Specialized architect for Hearts of Iron IV National Focus Trees. Covers 5-wing
  visual grid mathematics, DAG dependency topologies, non-colliding coordinates, dynamic
  tree pruning via allow_branch, mutually_exclusive logic, pacing standards (1911-1918),
  and layout validation.
---

# HOI4 Focus Tree Designer & Spatial Architecture

This skill provides the comprehensive structural guidelines, spatial coordinate algorithms, visual rendering rules, and execution templates required to design professional, crash-free, visually stunning National Focus Trees for Hearts of Iron IV.

---

## 1. The 5-Wing Spatial Architecture Standard

To avoid the "spaghetti tree" phenomenon where arrows cross entire screens and sub-branches intertwine, all national focus trees must strictly adhere to the **5-Wing Spatial Coordinate Grid**.

Every nation's focus file (`common/national_focus/<country>.txt`) must divide the horizontal X-axis into five discrete zones:

| Wing | Theme & Scope | Recommended X Range | Typical Column Width |
| :--- | :--- | :--- | :--- |
| **Wing 1** | **Internal Politics & Ideology** (Constitutional, Monarchist, Socialist, Democratic, Fascist/Reactionary) | `x = 1 to 24` | 4–6 columns per path |
| **Wing 2** | **Economy, Industry & Resources** (Infrastructure, Factories, Agriculture, Rationing, Raw Materials) | `x = 25 to 48` | 4–5 parallel columns |
| **Wing 3** | **Navy & Aviation** (Battlefleet, Submarines, Naval Aviation, Zeppelins, Air Doctrines) | `x = 49 to 72` | 4–6 parallel columns |
| **Wing 4** | **Army, General Staff & Land Doctrines** (Infantry, Artillery, Armor/Tanks, Stormtroopers, Doctrines) | `x = 73 to 105` | 6–8 parallel columns |
| **Wing 5** | **Foreign Policy, Diplomacy & Treaties** (Alliances, Crisis Management, Ultimatums, Regional Expansions) | `x = 106 to 135` | 4–6 columns |

> [!IMPORTANT]
> **Strict Wing Separation**: Never link a focus in Wing 4 directly to a focus in Wing 1 via `prerequisite = { ... }` across the UI. If an Army focus depends on a Political focus, use a country flag (`trigger = { has_country_flag = ... }` or `available = { ... }`) instead of a prerequisite line to prevent horizontal arrows from cutting through Wings 2 and 3!

---

## 2. Geometric Layout Mathematics & Connection Rules

The Clausewitz UI renderer draws connection arrows between parent and child foci. Incompatible coordinates trigger severe visual glitches:

### A. The Golden Coordinate Rules
1. **Strict Downward Progression (`dy >= 1`)**:
   - `child.y` MUST ALWAYS be greater than `parent.y`.
   - `dy = child.y - parent.y >= 1`.
   - **Critical Engine Bug**: If `dy < 0` (child above parent), the engine renders an arrow pointing backward/upward.
   - **Critical Engine Bug**: If `dy == 0` (child on same row as parent), the engine renders a horizontal line straight through intermediate focus icons!
2. **Vertical Step Limit (`1 <= dy <= 2`)**:
   - Optimal spacing is `dy = 1` for immediate subsequent steps.
   - Use `dy = 2` only when skipping an intermediate tier or synchronizing with a parallel branch.
   - Never use `dy >= 3` without an intermediate node, as long vertical lines look unanchored and cut across adjacent branch text.
3. **Horizontal Delta & Offset (`|dx| <= 2`)**:
   - Direct descendants should ideally be on the same column (`dx = 0`) or branched out by 1 column (`dx = ±1` or `dx = ±2`).
   - If two parents merge into one child, place the child centrally:
     - Parent A at `x = 10, y = 3`
     - Parent B at `x = 12, y = 3`
     - Merged Child at `x = 11, y = 4`
4. **Collision Prevention**:
   - No two foci can ever share the exact same `(x, y)` coordinate.
   - Maintain at least `dx >= 2` between independent parallel vertical paths so focus name banners do not visually overlap.

---

## 3. Dynamic Branch Isolation (`allow_branch`) vs `mutually_exclusive`

In standard HoI4 modding, many developers only use `mutually_exclusive = { focus = <other_focus> }`. 

### The Problem:
`mutually_exclusive` disables the other branch, but leaves all 30–50 mutually exclusive foci visible on the screen forever, greyed out, creating massive visual clutter.

### The Solution (`allow_branch` Dynamic Pruning):
By placing `allow_branch` on the root node of an alternative ideological or strategic branch, HoI4's engine dynamically collapses and completely hides that entire branch (root and all its children) once the player commits to an opposing path!

```pdx
# =========================================================================
# WING 1: HISTORICAL MONARCHY ROOT
# =========================================================================
focus = {
    id = TAG_preserve_the_monarchy
    icon = GFX_TAG_kaiser_crown
    x = 14
    y = 0
    cost = 10
    
    allow_branch = {
        NOT = { has_country_flag = TAG_socialist_path_chosen }
        NOT = { has_country_flag = TAG_republican_path_chosen }
    }
    
    completion_reward = {
        set_country_flag = TAG_monarchist_path_chosen
        add_political_power = 100
    }
}

# =========================================================================
# WING 1: ALTERNATIVE SOCIALIST REPUBLIC ROOT
# =========================================================================
focus = {
    id = TAG_proclaim_the_peoples_republic
    icon = GFX_TAG_red_banner
    x = 4
    y = 0
    cost = 10
    
    allow_branch = {
        NOT = { has_country_flag = TAG_monarchist_path_chosen }
        NOT = { has_country_flag = TAG_republican_path_chosen }
    }
    
    completion_reward = {
        set_country_flag = TAG_socialist_path_chosen
        set_country_flag = TAG_alt_path_active
        # Regime change effects handled here
    }
}
```

> [!NOTE]
> When `allow_branch` evaluates to `false` on a focus, any child focus that has it as a prerequisite is automatically pruned from the GUI as well. You only need `allow_branch` on the root of each branch!

---

## 4. Pacing & Time Budgeting (1911–1918 Timeline)

In WW1 mods (starting 1910/1911), tree pacing must correspond to real historical mobilization phases:

### Focus Duration Hierarchy
- **28 Days (4 Weeks)**:
  - Crisis management (e.g., Sarajevo ultimatum, Agadir crisis response, emergency strikes).
  - Rapid operational choices (e.g., choosing Eastern vs Western deployment).
- **35 Days (5 Weeks)**:
  - Wartime operational initiatives (e.g., artillery preparatory barrage, local offensive).
  - Urgent cabinet reshuffles, wartime rationing measures.
- **56 Days (8 Weeks)**:
  - Standard national focuses (e.g., construction programs, legislative bills, research treaty).
- **70 Days (10 Weeks)**:
  - Deep institutional transformations (e.g., full constitutional overhaul, Army modernization programs, Dreadnought naval expansion acts).

### Timeline Pacing Targets
A standard major power focus tree should contain:
- **Pre-War Era (1911 – mid 1914)**: ~15 to 20 available focuses to prepare the nation.
- **Wartime Era (mid 1914 – 1917)**: ~25 to 35 operational and economic adaptation focuses.
- **Late-War / Endgame (1917 – 1919+)**: ~20 to 30 victory, crisis resolution, or post-war rebuilding focuses.

---

## 5. Prerequisite & Exclusivity Dependency Patterns

### A. Simple Linear
```pdx
focus = {
    id = TAG_step_two
    prerequisite = { focus = TAG_step_one }
    x = 10
    y = 1
}
```

### B. "OR" Branching (Any Parent Unlocks Child)
```pdx
focus = {
    id = TAG_combined_arms_doctrine
    # Unlocked if player completed EITHER offensive OR defensive doctrine
    prerequisite = { focus = TAG_offensive_focus focus = TAG_defensive_focus }
    x = 80
    y = 4
}
```

### C. "AND" Branching (Both Parents Required)
```pdx
focus = {
    id = TAG_mechanized_shocktroops
    # Unlocked ONLY if BOTH parents are completed
    prerequisite = { focus = TAG_tank_prototypes }
    prerequisite = { focus = TAG_stormtrooper_training }
    x = 82
    y = 5
}
```

### D. Symmetric Mutual Exclusivity
Always declare mutual exclusivity bidirectionally:
```pdx
# In Focus A:
mutually_exclusive = { focus = TAG_focus_B }

# In Focus B:
mutually_exclusive = { focus = TAG_focus_A }
```

---

## 6. Focus Definition Specification Template

```pdx
focus = {
    id = TAG_focus_identifier
    icon = GFX_TAG_focus_icon_name
    cost = 10                  # 10 cost = 70 days, 5 cost = 35 days, 4 cost = 28 days
    x = 10                     # Absolute column in 5-wing system
    y = 1                      # Absolute row in 5-wing system
    
    prerequisite = { focus = TAG_parent_focus }
    mutually_exclusive = { focus = TAG_rival_focus }
    
    available = {
        # Trigger conditions required to START or FINISH the focus
        date > 1914.8.1
        has_war = yes
    }
    
    cancel_if_invalid = yes
    continue_if_invalid = no
    available_if_capitulated = no
    
    search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_RESEARCH }
    
    select_effect = {
        # Instant effects when focus is clicked
    }
    
    completion_reward = {
        # Effects upon completion
    }
}
```

---

## 7. Fast Automated Tree Validation

Always run the dedicated layout validator before testing in-game:
```powershell
python scripts/validate_tree_layout.py --tree common/national_focus/<country>.txt
```

The script verifies:
1. Exact coordinate duplicates `(x, y)`.
2. Any backward edges (`dy < 0`).
3. Any same-row edges (`dy == 0`).
4. Broken focus ID references in `prerequisite` or `mutually_exclusive`.
5. Missing symmetric exclusivity declarations.
6. Cycle loops in DAG (Directed Acyclic Graph).
