# Task 3 Completion Report: Map-Based State Securing Decisions Engine (`common/decisions/`)

## Status
**Completed Successfully**

## Git Commit
- **Commit:** `2316675` (or latest HEAD)
- **Message:** `feat(uk): implement map-based state securing decisions and crisis management actions`
- **Files Modified:**
  - `common/decisions/categories/ww1_britain_categories.txt`
  - `common/decisions/ww1_britain_decisions.txt`

---

## Changes Implemented

### 1. Decision Category (`common/decisions/categories/ww1_britain_categories.txt`)
- Added `ENG_ww1_irish_crisis_category`:
  - `icon = GFX_decision_ENG_ww1_empire_policy`
  - `allowed = { tag = ENG }`
  - `visible = { has_country_flag = ww1_britain_initialised }`

### 2. State-Targeted Decisions (`common/decisions/ww1_britain_decisions.txt`)
- **`ENG_deploy_crown_garrison`**:
  - `state_target = yes` targeting owned Irish states (113 Cork/Munster, 114 Galway/Connaught, 117 Dublin/Leinster, 119 Belfast/Ulster) that are not yet garrison secured.
  - Cost: 35 PP, 25,000 Manpower, 500 Infantry Equipment.
  - Duration: 60 days with concurrency lock flag `ENG_securing_irish_state_in_progress`.
  - Effect: Clears contested unrest & rebel stronghold flags, marks state with `ENG_state_garrison_secured`, lowers Irish tension by 10.
- **`ENG_raid_paramilitary_armories`**:
  - `state_target = yes` targeting Irish states.
  - Cost: 25 PP, 10 Command Power.
  - Effect: Lowers Irish tension by 5; 15% risk of civilian backlash damaging 1 infrastructure and reducing stability by 2%.
- **`ENG_emergency_curfew_lockdown`**:
  - `state_target = yes` targeting Irish states without active curfew.
  - Cost: 20 PP, 1 Civilian Factory for 90 days.
  - Effect: Imposes curfew (`ENG_curfew_active`) across the region to halt sabotage operations.

### 3. Strategic Crisis Decisions (`common/decisions/ww1_britain_decisions.txt`)
- **`ENG_larne_arms_interdiction`**: Interdicts UVF weapon smuggling. Costs 30 PP and 15 Navy XP; lowers Ulster tension by 15.
- **`ENG_appease_curragh_officers`**: Settles officer mutiny by compromising on Ulster. Lowers Ulster tension by 15 but increases Nationalist tension by 10.
- **`ENG_purge_curragh_officers`**: Enforces Westminster military discipline. Lowers Nationalist tension by 10, raises Ulster tension by 15, costs 35 PP and 10 Army XP.
- **`ENG_deploy_black_and_tans`**: Deploys auxiliary constabulary. Costs 50 PP and 10,000 Manpower; transitions Pillar 5 into `ENG_irish_martial_law` via clean `swap_ideas`.
- **`ENG_restore_order_in_ireland_act`** (Track B Capstone): Requires all 4 Irish states to have `ENG_state_garrison_secured`. Swaps Pillar 5 idea to `ENG_irish_union_secured`, resets Irish and Ulster tensions to 0, grants +10% stability and +50 PP.
- **`ENG_enact_irish_free_state_treaty`** (Track A Capstone): Requires Irish convention/treaty preconditions and peace. Releases `IRE` as an autonomous Dominion, retains Ulster (119) under the Crown, swaps Pillar 5 idea to `ENG_irish_home_rule_compromise`, grants +10% stability and +50 PP.

---

## Verification & Test Results

1. **Clausewitz Semantic Oracle Validation:**
   ```bash
   python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/decisions/ww1_britain_decisions.txt'); print(errs); assert len(errs) == 0"
   ```
   - **Result:** `[]` - 0 invalid modifier tokens. Assertion passed.

2. **Master Audit Test Suite (`tests/test_ww1_britain_complete_audit.py`):**
   ```bash
   python -m unittest tests/test_ww1_britain_complete_audit.py
   ```
   - **Result:**
     - `ENG_ww1_irish_crisis_category` category presence: **PASSED**
     - `ENG_deploy_crown_garrison` presence: **PASSED**
     - `ENG_raid_paramilitary_armories` presence: **PASSED**
     - Ghost ideas check: **PASSED** (0 ghost ideas)
     - Only 1 expected failure remains: `Civil war event 'ww1_britain_pol.irish_civil_war' missing from events/ww1_britain_events.txt` (to be addressed in Task 4).
