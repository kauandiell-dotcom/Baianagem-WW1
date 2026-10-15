# Task 4 Report: Military Mutinies (1917) & Civil Crises Engine (Jusqu'au Bout!)

**Date:** 2026-10-15  
**Commit:** `524ba4ac56cfc75b375d4d099e77222665102ba5`  
**Status:** Completed & Validated  

---

## 1. Executive Summary

Task 4 of the French Republic complete overhaul has been fully implemented, integrated, and validated for *Baianagem-WW1*. It establishes the complete 1917 French Army Mutinies crisis chain, Pétain's Generalissimo appointment and leave/welfare reforms, the Paris Munitionnettes home front strikes, and Georges Clemenceau's iconic *"Jusqu'au Bout!"* French *Endsieg* mechanic. All modifiers are 100% compliant with the Clausewitz engine semantic oracle, with zero bracket imbalances, zero duplicate event IDs, and single UTF-8 BOM integrity preserved.

---

## 2. Deliverables Implemented

### A. Crises National Ideas File (`common/ideas/ww1_france_crises_ideas.txt`)
Defined 4 bounded, authentic crisis national ideas:
- **`FRA_trench_mutiny_crisis_2`**:
  - `army_attack_factor = -0.25` (-25% army attack)
  - `breakthrough_factor = -0.15` (-15% breakthrough)
  - `army_core_defence_factor = -0.10` (-10% core defense)
- **`FRA_poilus_reconcilies`**:
  - `army_core_defence_factor = 0.10` (+10% core defense)
  - `army_morale_factor = 0.10` (+10% army morale)
- **`FRA_munitionnettes_strike`**:
  - `industrial_capacity_factory = -0.20` (-20% factory output)
  - `stability_factor = -0.10` (-10% stability)
- **`FRA_jusqu_au_bout_endsieg`**:
  - `army_core_defence_factor = 0.20` (+20% core defense)
  - `war_support_factor = 0.15` (+15% war support)
  - `political_power_gain = 0.10` (+0.10 daily political power)
  - `surrender_limit = 0.20` (+20% surrender limit endurance)
- **Modifier Compliance:** 100% verified via `scripts/hoi4_semantic_oracle.py` (0 errors).

### B. Events Engine Overhaul (`events/ww1_france_events.txt`)
1. **`ww1_france.210` (*The 1917 Army Mutinies*):**
   - Triggered when `tag = FRA`, `has_war = yes`, `date > 1916.12.1`, `check_variable = { FRA_poilu_morale < 40 }` or called on Nivelle offensive mission timeout.
   - Option `ww1_france.210.a`:
     - Applies `FRA_trench_mutiny_crisis_2` **strictly before** any child event calls.
     - Subtracts 25 from `FRA_poilu_morale`.
     - Inflicts -10% stability and -10% war support.
     - Calls `FRA_clamp_dashboard_variables = yes`.
     - Dispatches child event `ww1_france.211` with a 2-day delay.
2. **`ww1_france.211` (*Pétain Appointed Generalissimo / Reforms*):**
   - Option A (*Implement Welfare and Leave Reforms*): Unlocks decision `FRA_petain_welfare_and_leave_reform` (`FRA_petain_welfare_reforms_unlocked_tt`), grants +5% stability and +20 PP (AI weight 90).
   - Option B (*Draconian Tribunals*): Summary execution of ringleaders, -10% stability, -5% war support, -15 Union Sacrée cohesion, risking home-front revolution (AI weight 10).
3. **`ww1_france.215` (*Munitionnettes Strike in Paris*):**
   - Triggered when `tag = FRA`, `has_war = yes`, `date > 1917.4.1`, `check_variable = { FRA_union_sacree_cohesion < 50 }`.
   - Option A (*Concede Wage Increases*): Costs 30 PP, +5% stability, restores +10 Union Sacrée cohesion (AI weight 75).
   - Option B (*Police Repression*): Adds `FRA_munitionnettes_strike`, -5% stability, loses 10 Union Sacrée cohesion (AI weight 25).
4. **`ww1_france.220` (*Clemenceau's Jusqu'au Bout! Endsieg Speech*):**
   - Triggered when `tag = FRA`, `has_war = yes`, `surrender_progress > 0.15` OR `date > 1917.11.1`.
   - Option A (*"Je fais la guerre!"*): Adds `FRA_jusqu_au_bout_endsieg`, +20% war support, +5% stability, +15 poilu morale, +15 Union Sacrée cohesion, and clamps variables.
5. **Architectural Event ID Deconfliction:**
   - The legacy 1915 bilateral diplomacy event for the Italian Secret Treaty of London originally occupied `ww1_france.220`. To eliminate duplicate event ID collisions in the Clausewitz engine while honoring the requirement for Clemenceau's Endsieg to be `ww1_france.220`, the Italian proposal event was renumbered to `ww1_france.218`, national focus line 3155 in `common/national_focus/france.txt` was synchronized, and bilingual localization was updated.

### C. Decisions Integration (`common/decisions/ww1_france_decisions.txt`)
- Overhauled `FRA_petain_welfare_and_leave_reform`:
  - `allowed = { tag = FRA }`
  - `available = { has_idea = FRA_trench_mutiny_crisis_2 }`
  - `visible = { has_idea = FRA_trench_mutiny_crisis_2 }`
  - `complete_effect`:
    - `remove_ideas = FRA_trench_mutiny_crisis_2`
    - `add_ideas = FRA_poilus_reconcilies`
    - `add_to_variable = { FRA_poilu_morale = 30 }`
    - `add_stability = 0.08`
    - `add_war_support = 0.05`
    - `FRA_clamp_dashboard_variables = yes`

---

## 3. QA & Verification Results

1. **Task Primary Unit Test:**
   ```
   python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_mutinies_and_civil_crises -v
   test_mutinies_and_civil_crises (tests.test_ww1_france_rework.TestFranceOverhaul.test_mutinies_and_civil_crises)
   Verify the 1917 French Army Mutinies chain, Pétain leave reform, and Endsieg. ... ok
   Ran 1 test in 0.003s
   OK
   ```

2. **Full French Republic Unit Test Suite:**
   - `test_agadir_crisis_mechanics`: **PASS**
   - `test_republic_dashboard_variables`: **PASS**
   - `test_mutinies_and_civil_crises`: **PASS**

3. **Existing French Content Test Suite (`tests/test_ww1_france.py`):**
   - 8 / 8 tests: **PASS** (100%)

4. **German Empire E2E Test Suite (`tests/test_runner.py`):**
   - 21 / 21 tests: **PASS** (100%, Exit Code 0)

5. **Clausewitz Brace Balance Audit:**
   - `common/ideas/ww1_france_crises_ideas.txt`: (True, 'OK')
   - `events/ww1_france_events.txt`: (True, 'OK')
   - `common/decisions/ww1_france_decisions.txt`: (True, 'OK')
   - `common/national_focus/france.txt`: (True, 'OK')
   - Overall Diff = 0 across all files.

6. **BOM Integrity Audit:**
   - Zero BOM errors across all localisation and project files (`audit_bom_integrity()` = `[]`).

7. **Semantic Oracle Modifier Audit:**
   - `common/ideas/ww1_france_crises_ideas.txt`: 0 errors.

---

## 4. Git Commit Details

- **Commit Hash:** `524ba4ac56cfc75b375d4d099e77222665102ba5`
- **Commit Message:** `feat(fra): overhaul 1917 French Army Mutinies, Munitionnettes strikes, and Clemenceau Endsieg`
- **Files Committed:**
  - `WW1/common/ideas/ww1_france_crises_ideas.txt`
  - `WW1/events/ww1_france_events.txt`
  - `WW1/common/decisions/ww1_france_decisions.txt`
  - `WW1/common/national_focus/france.txt`
  - `WW1/localisation/english/ww1_france_l_english.yml`
  - `WW1/localisation/braz_por/ww1_france_l_braz_por.yml`
