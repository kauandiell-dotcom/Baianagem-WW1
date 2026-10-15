# Task 5 Report: Focus Tree Expansion & The 4 Yugoslav/Serbian Destinies

**Status:** COMPLETED  
**Commit:** `400acbffcce14c5a828428e7795f600bf8854f95`  
**Date:** 2026-10-15  

---

## 1. Summary of Changes

### A. Post-War Destination National Ideas (`common/ideas/ww1_serbia_ideas.txt`)
Implemented the four distinct post-war destination national ideas with 100% verified Clausewitz modifiers audited via `scripts/hoi4_semantic_oracle.py`:

1. **`SER_yugoslav_kingdom_unification`** (Kingdom of Serbs, Croats and Slovenes / South Slavic Unification):
   - `stability_factor = 0.10`
   - `political_power_gain = 0.15`
   - `compliance_growth = 0.20`
   - `army_core_defence_factor = 0.10`
2. **`SER_greater_serbian_hegemony`** (Greater Serbia Centralism / Velika Srbija):
   - `war_support_factor = 0.15`
   - `army_core_defence_factor = 0.15`
   - `conscription_factor = 0.10`
   - `political_power_gain = 0.10`
3. **`SER_balkan_soviet_federation`** (Balkan Socialist Federation):
   - `communism_drift = 0.10`
   - `production_factory_max_efficiency_factor = 0.10`
   - `industrial_capacity_factory = 0.10`
   - `recruitable_population_factor = 0.10`
4. **`SER_black_hand_junta_rule`** (Black Hand Pretorian Military State):
   - `neutrality_drift = 0.10`
   - `army_attack_factor = 0.15`
   - `army_org_factor = 0.10`
   - `command_power_gain_mult = 0.25`

### B. Focus Tree Expansion (`common/national_focus/serbia.txt`)
Expanded the late-game political endgame section with full mutual exclusivity and strict visual layout standards:

- **`SER_proclamation_of_yugoslavia`** (x = 39, y = 11, cost = 5):
  - Prerequisites: `SER_armistice_on_the_danube`, `SER_podgorica_assembly_unification`
  - Mutually Exclusive: `SER_restored_sovereign_serbia`, `SER_balkan_socialist_soviet_republic`, `SER_apis_pretorian_military_junta`
  - Awards: `SER_yugoslav_kingdom_unification`, cosmetic tag `YUG`, +15% stability, +150 PP.
- **`SER_restored_sovereign_serbia`** (x = 41, y = 11, cost = 5):
  - Prerequisites: `SER_armistice_on_the_danube`
  - Mutually Exclusive: `SER_proclamation_of_yugoslavia`, `SER_balkan_socialist_soviet_republic`, `SER_apis_pretorian_military_junta`
  - Awards: `SER_greater_serbian_hegemony`, +15% stability, +15% war support, +150 PP, civilian factory in Belgrade.
- **`SER_balkan_socialist_soviet_republic`** (x = 43, y = 11, cost = 5):
  - Prerequisites: `SER_armistice_on_the_danube`
  - Mutually Exclusive: `SER_proclamation_of_yugoslavia`, `SER_restored_sovereign_serbia`, `SER_apis_pretorian_military_junta`
  - Awards: `SER_balkan_soviet_federation`, shifts ruling party to communism, arms factory in Belgrade, +10% stability, +120 PP.
- **`SER_apis_pretorian_military_junta`** (x = 45, y = 11, cost = 5):
  - Prerequisites: `SER_armistice_on_the_danube`
  - Mutually Exclusive: `SER_proclamation_of_yugoslavia`, `SER_restored_sovereign_serbia`, `SER_balkan_socialist_soviet_republic`
  - Awards: `SER_black_hand_junta_rule`, shifts ruling party to non-aligned (junta), +20% war support, +100 PP, +30 Army XP, +40 CP.

### C. Visual Layout & DAG Geometry
- Non-colliding coordinates: Row 11 has focuses at x = 36, 39, 41, 43, 45.
- Distance between adjacent focuses: $\Delta x \ge 2$ everywhere ($39-36=3$, $41-39=2$, $43-41=2$, $45-43=2$).
- Zero cycles (DFS cycle check passed).
- Parent-child vertical ordering: $dy \ge 1$ for all prerequisites ($y=11 > \text{parent } y=9, 10$).

---

## 2. Verification Results

1. **`test_four_yugoslav_destinies`**:
   - `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_four_yugoslav_destinies -v` -> **PASS**
2. **`test_semantic_oracle_modifiers`**:
   - `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v` -> **PASS** (0 invalid modifier tokens)
3. **Full Serbia Overhaul Suite (`tests/test_ww1_serbia_rework.py`)**:
   - 8/8 tests -> **PASS**
4. **Clausewitz Syntax & Bracket Balance**:
   - Checked with `ClausewitzAuditor.audit_braces`: 0 syntax or brace errors (net balance delta = 0).
