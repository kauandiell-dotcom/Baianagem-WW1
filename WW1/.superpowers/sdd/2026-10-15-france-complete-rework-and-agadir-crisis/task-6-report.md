# Task 6 Report: Industrial Relocation, Northeast Loss & Allied Convoys

**Date:** 2026-10-15  
**Commit:** `5c5b4f3`  
**Status:** Completed & 100% Validated  

---

## 1. Executive Summary

Task 6 implements the wartime industrial adaptation and emergency logistics decisions for the French Republic (`FRA`) in *Baianagem-WW1*. When Germany occupies or threatens the northeastern industrial basin (Briey, Longwy, Lille), France can relocate machinery to southern rear hubs (Lyon/Rhône), expand chemical and gunpowder facilities, mobilize Schneider-Creusot heavy artillery production, reinforce the Verdun fortifications at Fort Douaumont, institute the *Voie Sacrée* emergency truck convoys, convene the Inter-Allied Supreme War Council, and open J.P. Morgan credit lines in New York. All decisions feature fast-failing `allowed = { original_tag = FRA }`, bounded bonuses, zero banned modifiers, and complete semantic oracle compliance.

---

## 2. Deliverables Implemented

### 1. Decision Categories (`common/decisions/categories/ww1_france_categories.txt`)
All 6 French decision categories configured with `visible_when_empty = no` to ensure UI cleanliness:
- `FRA_third_republic_politics` (Priority 90)
- `FRA_western_front_operations` (Priority 95)
- `FRA_defence_of_verdun` (Priority 98)
- `FRA_mutinies_crisis_management` (Priority 99)
- `FRA_war_economy_and_munitions` (Priority 85)
- `FRA_entente_diplomacy` (Priority 80)

### 2. Wartime Industrial & Diplomatic Decisions (`common/decisions/ww1_france_decisions.txt`)

#### A. Category `FRA_war_economy_and_munitions`
1. **`FRA_dec_evacuate_briey_machinery`:**
   - **Cost:** 30 PP | `fire_only_once = yes`
   - **Trigger:** Available when at war with Germany (`has_war_with = GER`) and controls Lyon/Rhône (`controls_state = 20`).
   - **Effects:** Adds 1 shared building slot and 1 arms factory in Lyon (state 20); replenishes +15 `FRA_charbon_et_acier`; executes `FRA_clamp_dashboard_variables = yes`.
2. **`FRA_dec_lyon_chemical_complex`:**
   - **Cost:** 35 PP | `fire_only_once = yes` | `days_remove = 180`
   - **Trigger:** Available when at war (`has_war = yes`) and controls Lyon/Rhône (`controls_state = 20`).
   - **Effects:** Adds 1 shared building slot and 1 arms factory in state 20; applies 180-day production boost (`industrial_capacity_factory = 0.10`, `production_factory_max_efficiency_factor = 0.05`).
3. **`FRA_dec_schneider_creusot_heavy_guns`:**
   - **Cost:** 35 PP | `fire_only_once = yes` | `days_remove = 180`
   - **Trigger:** Available when at war (`has_war = yes`).
   - **Effects:** Grants 100% artillery research bonus (`bonus = 1.0`, `uses = 1`, `category = artillery`), +15 army experience, and 180-day artillery attack boost (`army_artillery_attack_factor = 0.10`).

#### B. Category `FRA_defence_of_verdun`
1. **`FRA_dec_fort_douaumont_reinforcement`:**
   - **Cost:** 25 PP | `fire_only_once = yes`
   - **Trigger:** Available when at war with Germany (`has_war_with = GER`) and controls Champagne/Verdun (`controls_state = 18`).
   - **Effects:** Instantly constructs +1 land fort (`type = bunker`) in Verdun redoubt sector (province 9490 in state 18).
2. **`FRA_dec_voix_sacree_truck_convoys`:**
   - **Cost:** 25 PP | `fire_only_once = yes` | `days_remove = 180`
   - **Trigger:** Available when at war with Germany (`has_war_with = GER`) and frontline contested (`OR = { controls_state = 18 controls_state = 16 }`).
   - **Effects:** Adds +10 `FRA_poilu_morale`, clamps dashboard variables, and applies 180-day core defense boost (`army_core_defence_factor = 0.10`).

#### C. Category `FRA_entente_diplomacy`
1. **`FRA_dec_inter_allied_supreme_war_council`:**
   - **Cost:** 30 PP | `fire_only_once = yes` | `days_remove = 360`
   - **Trigger:** Available when at war and in faction with Great Britain (`is_in_faction_with = ENG`).
   - **Effects:** Grants +40 PP, +5% stability, and 360-day Allied army coordination boost (`coordination_bonus = 0.05`, `planning_speed = 0.10`).
2. **`FRA_dec_us_morgan_bank_credit_line`:**
   - **Cost:** 20 PP | `fire_only_once = yes` | `days_remove = 360`
   - **Trigger:** Available when at war, USA exists, and not at war with USA.
   - **Effects:** Grants +60 PP and 360-day industrial factory output buff (`industrial_capacity_factory = 0.10`).

#### D. Fast-Failing Performance Assurance
- Every single decision in `common/decisions/ww1_france_decisions.txt` (both newly introduced and legacy operations) enforces fast-failing:
  ```clausewitz
  allowed = {
      original_tag = FRA
  }
  ```

---

## 3. QA & Automated Verification Results

### 1. Test Suite Execution (`tests/test_ww1_france_rework.py`)
```
test_agadir_crisis_mechanics ... ok
test_four_political_destinies ... ok
test_localisation_bom_and_parity ... skipped 'Rework localization files not yet created (scheduled for Task 7)'
test_mutinies_and_civil_crises ... ok
test_republic_dashboard_variables ... ok
test_semantic_oracle_modifiers ... ok
test_wartime_industrial_and_allied_decisions ... ok

Ran 7 tests in 0.030s
OK (skipped=1)
```

### 2. General French Content Test Suite (`tests/test_ww1_france.py`)
```
test_bilingual_localization_parity_and_bom ... ok
test_focus_count_and_coordinate_collisions ... ok
test_naval_reinforcement_oob_parity ... ok
test_no_banned_modifiers_in_french_ideas ... ok
test_political_cabinet_transitions ... ok
test_prerequisite_integrity_and_downward_progression ... ok
test_prewar_pacing_and_crisis_costs ... ok
test_wartime_and_date_gating ... ok

Ran 8 tests in 0.028s
OK
```

### 3. Clausewitz Semantic Oracle Modifier Audit
- Checked `common/decisions/ww1_france_decisions.txt` via `scripts/hoi4_semantic_oracle.py`:
  - `industrial_capacity_factory`: Valid
  - `production_factory_max_efficiency_factor`: Valid
  - `army_artillery_attack_factor`: Valid
  - `army_core_defence_factor`: Valid
  - `coordination_bonus`: Valid
  - `planning_speed`: Valid
  - **Oracle Audit Output:** `Errors in ww1_france_decisions.txt: []` (0 invalid tokens).

### 4. Bracket Balance Audit
- `common/decisions/ww1_france_decisions.txt`: 154 open / 154 close, Diff = 0.
- `common/decisions/categories/ww1_france_categories.txt`: 12 open / 12 close, Diff = 0.

---

## 4. Git Artifacts

- **Commit Hash:** `5c5b4f3`
- **Commit Message:** `feat(fra): populate wartime industrial relocation, Verdun redoubts, and Allied cooperation decisions`
- **Files Committed:**
  - `WW1/common/decisions/categories/ww1_france_categories.txt`
  - `WW1/common/decisions/ww1_france_decisions.txt`
  - `WW1/tests/test_ww1_france_rework.py`
