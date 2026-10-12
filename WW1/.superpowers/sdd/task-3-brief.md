# Task 3 Brief: Map-Based State Securing Decisions Engine (`common/decisions/`)

## Objective
Implement the dedicated Irish crisis decision category `ENG_ww1_irish_crisis_category` in `common/decisions/categories/ww1_britain_categories.txt` and the state-targeted & strategic decisions in `common/decisions/ww1_britain_decisions.txt`.

## Context & Files
- Category file: `common/decisions/categories/ww1_britain_categories.txt`
- Decisions file: `common/decisions/ww1_britain_decisions.txt`
- Spec: `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-irish-crisis-insanity-plan.md`

## Requirements
1. **In `common/decisions/categories/ww1_britain_categories.txt`:**
   Add:
   ```txt
   ENG_ww1_irish_crisis_category = {
   	icon = GFX_decision_ENG_ww1_empire_policy
   	allowed = { tag = ENG }
   	visible = { has_country_flag = ww1_britain_initialised }
   }
   ```

2. **In `common/decisions/ww1_britain_decisions.txt`:**
   Add `ENG_ww1_irish_crisis_category = { ... }` with the following decisions:
   
   ### State-Targeted Decisions:
   - `ENG_deploy_crown_garrison`:
     - `icon = GFX_decision_generic_military` (or appropriate)
     - `state_target = yes`
     - `target_array = owned_states`
     - `target_trigger = { FROM = { is_owned_by = ROOT OR = { state = 113 state = 114 state = 117 state = 119 } NOT = { has_state_flag = ENG_state_garrison_secured } } }`
     - `visible = { has_country_flag = ww1_britain_initialised }`
     - `available = { NOT = { has_country_flag = ENG_securing_irish_state_in_progress } has_manpower > 25000 has_equipment = { type = infantry_equipment_0 amount > 500 } }`
     - `cost = 35`
     - `days_remove = 60`
     - `days_re_enable = 30`
     - `complete_effect = { set_country_flag = ENG_securing_irish_state_in_progress add_manpower = -25000 add_equipment_to_stockpile = { type = infantry_equipment_0 amount = -500 } }`
     - `remove_effect = { clr_country_flag = ENG_securing_irish_state_in_progress FROM = { set_state_flag = ENG_state_garrison_secured clr_state_flag = ENG_state_contested_unrest clr_state_flag = ENG_state_rebel_stronghold } add_to_variable = { ww1_britain_irish_tension = -10 } }`
     - `ai_will_do = { base = 1 modifier = { factor = 2 check_variable = { ww1_britain_irish_tension > 50 } } }`

   - `ENG_raid_paramilitary_armories`:
     - `icon = GFX_decision_generic_assassination` (or appropriate)
     - `state_target = yes`
     - `target_array = owned_states`
     - `target_trigger = { FROM = { is_owned_by = ROOT OR = { state = 113 state = 114 state = 117 state = 119 } } }`
     - `visible = { has_country_flag = ww1_britain_initialised }`
     - `available = { NOT = { has_country_flag = ENG_irish_raid_in_progress } command_power > 10 }`
     - `cost = 25`
     - `days_re_enable = 90`
     - `complete_effect = { add_command_power = -10 add_to_variable = { ww1_britain_irish_tension = -5 } random_list = { 85 = { } 15 = { add_stability = -0.02 FROM = { damage_building = { type = infrastructure damage = 1 } } } } }`
     - `ai_will_do = { base = 1 }`

   - `ENG_emergency_curfew_lockdown`:
     - `icon = GFX_decision_police_state`
     - `state_target = yes`
     - `target_array = owned_states`
     - `target_trigger = { FROM = { is_owned_by = ROOT OR = { state = 113 state = 114 state = 117 state = 119 } NOT = { has_state_flag = ENG_curfew_active } } }`
     - `visible = { has_country_flag = ww1_britain_initialised }`
     - `available = { num_of_civilian_factories_available_for_projects > 0 }`
     - `cost = 20`
     - `days_remove = 90`
     - `civilian_factory_use = 1`
     - `complete_effect = { FROM = { set_state_flag = ENG_curfew_active } }`
     - `remove_effect = { FROM = { clr_state_flag = ENG_curfew_active } }`
     - `ai_will_do = { base = 1 }`

   ### Strategic Crisis Decisions:
   - `ENG_larne_arms_interdiction`:
     - Interdicts UVF smuggling, lowering Ulster tension by 15. Cost: 30 PP, 15 Navy Experience.
   - `ENG_deploy_black_and_tans`:
     - Deploys auxiliary constabulary. Cost: 50 PP, 10,000 Manpower. Swaps Pillar 5 idea to `ENG_irish_martial_law`.
   - `ENG_restore_order_in_ireland_act`:
     - Track B Hardline Capstone. Requires all 4 Irish states to have `ENG_state_garrison_secured` (or pacification flag). Swaps idea to `ENG_irish_union_secured`.
   - `ENG_enact_irish_free_state_treaty`:
     - Track A Compromise Capstone. Requires Irish convention / treaty preconditions. Releases `IRE` as dominion, retains Ulster 119, restores stability.

3. **Verify with Clausewitz Semantic Oracle:**
   `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/decisions/ww1_britain_decisions.txt'); print(errs); assert len(errs) == 0"`
   Must pass with 0 errors.

4. **Verify partial progress in test suite:**
   `python -m unittest tests/test_ww1_britain_complete_audit.py`
   Category and decisions assertions in `test_irish_crisis_escalation_and_state_securing_mechanics` must pass.

5. **Commit:**
   `git add common/decisions/categories/ww1_britain_categories.txt common/decisions/ww1_britain_decisions.txt`
   `git commit -m "feat(uk): implement map-based state securing decisions and crisis management actions"`

6. **Write report to:**
   `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\task-3-report.md`
