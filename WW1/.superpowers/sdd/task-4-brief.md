# Task 4 Brief: Historical Events & Territorial Civil War Engine (`events/ww1_britain_events.txt`)

## Objective
Implement historical escalation events (Curragh Mutiny, Gun-running, overhauled 1916 Easter Rising), the territorial Civil War outbreak event (`ww1_britain_pol.irish_civil_war`), and the immediate post-capitulation pacification event (`ww1_britain_pol.ireland_pacified`) in `events/ww1_britain_events.txt`.

## Context & File
- Target File: `events/ww1_britain_events.txt`
- Spec: `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-irish-crisis-insanity-plan.md`

## Requirements
1. **Curragh Mutiny & Gun-Running Events:**
   - `ww1_britain_pol.curragh_mutiny` (March 1914):
     - Trigger: `tag = ENG`, `date > 1914.3.1`, `date < 1914.8.1`, `has_capitulated = no`, `NOT = { has_country_flag = ENG_curragh_mutiny_happened }`.
     - Option A (Cede to Officers): `add_to_variable = { ww1_britain_ulster_tension = -20 }`, `add_to_variable = { ww1_britain_irish_tension = 15 }`, `add_political_power = -25`, `add_stability = -0.05`, `set_country_flag = ENG_curragh_officers_appeased`.
     - Option B (Purge Mutineers): `add_to_variable = { ww1_britain_ulster_tension = 25 }`, `add_to_variable = { ww1_britain_irish_tension = -5 }`, `add_command_power = -30`, `add_stability = 0.02`, `set_country_flag = ENG_curragh_officers_purged`.
   - `ww1_britain_pol.larne_howth_guns` (July 1914):
     - Trigger: `tag = ENG`, `date > 1914.7.1`, `date < 1914.9.1`, `has_capitulated = no`, `NOT = { has_country_flag = ENG_gunrunning_happened }`.
     - Smuggling escalates both nationalist and unionist tensions (`+10` each), `set_country_flag = ENG_gunrunning_happened`.

2. **Overhaul 1916 Easter Rising (`ww1_britain_pol.11`):**
   - Check status of Leinster (117):
     - If `117 = { has_state_flag = ENG_state_garrison_secured }`: Rebels swiftly contained by British garrison. Minor tension (`+5`), 0 damage.
     - If NOT secured: Armed seizure of Dublin GPO. Heavy urban fighting damaging infrastructure and arms factory, `add_to_variable = { ww1_britain_irish_tension = 25 }`, `add_stability = -0.08`.

3. **Civil War Eruption (`ww1_britain_pol.irish_civil_war`):**
   - Must have exact id `ww1_britain_pol.irish_civil_war` (tested by QA suite).
   - Trigger: `tag = ENG`, `has_capitulated = no`, `check_variable = { ww1_britain_irish_tension > 85 }`, `NOT = { has_country_flag = ENG_irish_civil_war_fired }`, `NOT = { has_country_flag = ENG_ww1_irish_union_secured }`, `NOT = { has_country_flag = ENG_ww1_irish_free_state }`.
   - Immediate actions:
     - `set_country_flag = ENG_irish_civil_war_fired`
     - Swaps Pillar 5 idea to `ENG_irish_civil_war_debacle` (using `swap_ideas` to safely replace `ENG_irish_home_rule_tension`, `ENG_irish_sabotage_wave`, or `ENG_irish_martial_law`).
     - State defection:
       - For states 113 (Munster), 114 (Connaught), 117 (Leinster):
         - If `NOT = { has_state_flag = ENG_state_garrison_secured }`: `transfer_state_to = IRE`.
       - State 119 (Ulster) stays with `ENG`.
     - IRE setup:
       - `IRE = { add_rule = { can_join_factions = no } }`
       - Ensure `ENG` declares war on `IRE`: `declare_war_on = { target = IRE type = civil_war }` (or appropriate wargoal).
     - Spawns rebel divisions for `IRE` (or uses `create_unit` if template exists, or gives equipment/manpower).

4. **Pacification & Capitulation Peace (`ww1_britain_pol.ireland_pacified`):**
   - Trigger: `tag = ENG`, `has_country_flag = ENG_irish_civil_war_fired`, `NOT = { has_country_flag = ENG_ww1_irish_union_secured }`, `country_exists = IRE`, `IRE = { has_capitulated = yes }`.
   - Immediate actions:
     - `annex_country = { target = IRE transfer_troops = no }`
     - Swaps Pillar 5 idea to `ENG_irish_union_secured`
     - `set_country_flag = ENG_ww1_irish_union_secured`
     - `add_stability = 0.10`

5. **Verify with QA Test Suite:**
   - Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`
   - All tests in `test_ww1_britain_complete_audit.py` must now PASS (0 failures!).

6. **Commit:**
   - `git add events/ww1_britain_events.txt`
   - `git commit -m "feat(uk): implement historical crisis events and localized territorial civil war engine"`

7. **Write report to:**
   - `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\task-4-report.md`
