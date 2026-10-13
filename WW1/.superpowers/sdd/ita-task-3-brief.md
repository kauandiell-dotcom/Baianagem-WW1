# Italy Rework Task 3: Map-Based State Decisions & Strategic Operations (`common/decisions/ww1_italy_decisions.txt`)

**Files:**
- Modify: `common/decisions/ww1_italy_decisions.txt`
- Modify: `common/decisions/categories/ww1_italy_categories.txt`

## Requirements
Add the 9 new map-based (`state_target = yes`) and strategic decisions to `common/decisions/ww1_italy_decisions.txt`.
**IMPORTANT CONTRACT:** In `tests/test_ww1_italy.py`, `test_decisions_count_categories_and_costs` asserts that every decision has `cost` (or `custom_cost_trigger`), and if it uses `civilian_factory_use`, it MUST have `cancel_effect`. Also `audit_file_modifiers('common/decisions/ww1_italy_decisions.txt')` must return 0 errors!

### 1. Under `ITA_ww1_economic_mobilisation_category`:
- **`ITA_ww1_mezzogiorno_aqueduct_and_roads`**:
  - `icon = generic_construction`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_owned_and_controlled_by = ITA OR = { state = 117 state = 849 state = 156 state = 115 state = 114 state = 157 } NOT = { has_state_flag = ITA_mezzogiorno_roads_built } } }`
  - `available = { has_completed_focus = ITA_ww1_mezzogiorno_programme }`
  - `visible = { original_tag = ITA }`
  - `cost = 30`, `days_remove = 90`
  - `remove_effect = { FROM = { set_state_flag = ITA_mezzogiorno_roads_built add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -8 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`
- **`ITA_ww1_carabinieri_anti_brigandage_sweep`**:
  - `icon = generic_police_action`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_owned_and_controlled_by = ITA OR = { state = 117 state = 849 state = 156 state = 115 state = 114 state = 157 } NOT = { has_state_flag = ITA_mezzogiorno_state_pacified } } }`
  - `available = { has_equipment = { infantry_equipment > 249 } }`
  - `visible = { original_tag = ITA }`
  - `cost = 25`, `days_remove = 60`
  - `complete_effect = { add_equipment_to_stockpile = { type = infantry_equipment amount = -250 producer = ITA } }`
  - `remove_effect = { FROM = { set_state_flag = ITA_mezzogiorno_state_pacified } add_stability = 0.02 add_to_variable = { ita_ww1_southern_gap = -6 } add_to_variable = { ita_ww1_social_tension = -4 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`
- **`ITA_ww1_southern_agrarian_credit_consortium`**:
  - `icon = generic_agrarian_reform`
  - `available = { check_variable = { ita_ww1_southern_gap < 40 } 117 = { has_state_flag = ITA_mezzogiorno_state_pacified } 115 = { has_state_flag = ITA_mezzogiorno_state_pacified } }`
  - `visible = { original_tag = ITA NOT = { has_idea = ITA_mezzogiorno_integrated } }`
  - `fire_only_once = yes`, `cost = 50`, `days_remove = 120`
  - `remove_effect = { remove_ideas = ITA_southern_question_gap remove_ideas = ITA_mezzogiorno_development_stage add_ideas = ITA_mezzogiorno_integrated 117 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } 115 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } } add_to_variable = { ita_ww1_southern_gap = -15 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`

### 2. Under `ITA_ww1_military_readiness_category`:
- **`ITA_ww1_alpine_mine_warfare_tunnel`**:
  - `icon = generic_fortification`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_controlled_by = ITA OR = { state = 160 state = 159 state = 850 state = 39 state = 736 state = 852 } NOT = { has_state_flag = ITA_alpine_sector_fortified } } }`
  - `available = { has_completed_focus = ITA_ww1_alpini_expansion }`
  - `visible = { original_tag = ITA }`
  - `cost = 30`, `days_remove = 60`
  - `remove_effect = { FROM = { set_state_flag = ITA_alpine_sector_fortified add_building_construction = { type = bunker level = 1 instant_build = yes province = { all_provinces = yes limit_to_border = yes } } } army_experience = 15 add_to_variable = { ita_ww1_army_morale = 5 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`
- **`ITA_ww1_launch_isonzo_general_offensive`**:
  - `icon = generic_prepare_civil_war`
  - `available = { has_war_with = AUS }`
  - `visible = { original_tag = ITA }`
  - `cost = 35`, `days_remove = 45`, `days_re_enable = 60`
  - `remove_effect`:
    - If `NOT = { has_country_flag = ita_ww1_diaz_appointed }`:
      - Escalates `ITA_isonzo_attrition_crisis_1` -> `ITA_isonzo_attrition_crisis_2` -> `ITA_isonzo_attrition_crisis_3` (if none is active yet, `add_ideas = ITA_isonzo_attrition_crisis_1`), grants `army_experience = 20`, and adjusts `add_to_variable = { ita_ww1_army_morale = -8 }`.
    - Else (under Armando Diaz):
      - Removes `ITA_isonzo_attrition_crisis_1`, `ITA_isonzo_attrition_crisis_2`, `ITA_isonzo_attrition_crisis_3`, grants `army_experience = 25`, `add_war_support = 0.03`, and `add_to_variable = { ita_ww1_army_morale = 10 }`.
    - Calls `ita_ww1_clamp_counters = yes` and `ita_ww1_update_gauges = yes`.
- **`ITA_ww1_fortify_piave_and_monte_grappa`**:
  - `icon = generic_fortification`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_owned_and_controlled_by = ITA OR = { state = 160 state = 159 } NOT = { has_state_flag = ITA_piave_grappa_fortified } } }`
  - `available = { has_war = yes }`
  - `visible = { original_tag = ITA }`
  - `cost = 35`, `days_remove = 60`
  - `remove_effect = { FROM = { set_state_flag = ITA_piave_grappa_fortified add_building_construction = { type = bunker level = 2 instant_build = yes province = { all_provinces = yes limit_to_border = yes } } } add_stability = 0.03 add_to_variable = { ita_ww1_army_morale = 10 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`
- **`ITA_ww1_impresa_di_pola_raid`**:
  - `icon = generic_naval`
  - `available = { has_war_with = AUS has_completed_focus = ITA_ww1_mas_boats }`
  - `visible = { original_tag = ITA }`
  - `fire_only_once = yes`, `cost = 40`, `days_remove = 45`
  - `remove_effect = { navy_experience = 25 add_war_support = 0.04 add_ideas = ITA_ww1_mignatta_special_raiders add_to_variable = { ita_ww1_army_morale = 10 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`

### 3. Under `ITA_ww1_diplomatic_initiatives_category`:
- **`ITA_ww1_fortify_libyan_coastal_oases`**:
  - `icon = generic_fortification`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_owned_and_controlled_by = ITA OR = { state = 448 state = 450 state = 451 state = 661 state = 663 } NOT = { has_state_flag = ITA_libya_oasis_secured } } }`
  - `available = { has_completed_focus = ITA_ww1_libyan_question }`
  - `visible = { original_tag = ITA }`
  - `cost = 25`, `days_remove = 60`
  - `remove_effect = { FROM = { set_state_flag = ITA_libya_oasis_secured add_building_construction = { type = infrastructure level = 1 instant_build = yes } add_compliance = 10 } army_experience = 10 add_to_variable = { ita_ww1_irredentism = 5 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`
- **`ITA_ww1_integrate_irredenta_province`**:
  - `icon = generic_nationalism`
  - `state_target = yes`
  - `target_trigger = { FROM = { is_owned_and_controlled_by = ITA OR = { state = 850 state = 39 state = 736 state = 852 state = 163 state = 164 } NOT = { has_state_flag = ITA_irredenta_integrated } } }`
  - `available = { always = yes }`
  - `visible = { original_tag = ITA }`
  - `cost = 35`, `days_remove = 75`
  - `remove_effect = { FROM = { set_state_flag = ITA_irredenta_integrated add_core_of = ITA add_building_construction = { type = infrastructure level = 1 instant_build = yes } } add_stability = 0.02 add_to_variable = { ita_ww1_irredentism = -10 } ita_ww1_clamp_counters = yes ita_ww1_update_gauges = yes }`

## Verification & Commit
Run:
```bash
python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/decisions/ww1_italy_decisions.txt')) == 0"
```
Commit:
```bash
git add common/decisions/ww1_italy_decisions.txt common/decisions/categories/ww1_italy_categories.txt
git commit -m "feat(ita): implement map-based Mezzogiorno, Alpine Guerra Bianca, Libyan, and Irredenta decisions"
```
Write your report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\ita-task-3-report.md`.
