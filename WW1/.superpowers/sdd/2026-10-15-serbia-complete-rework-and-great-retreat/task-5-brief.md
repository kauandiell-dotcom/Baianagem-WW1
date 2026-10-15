# Task 5 Brief: Focus Tree Expansion & The 4 Yugoslav/Serbian Destinies

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`

## Objectives
1. **Focus Tree (`common/national_focus/serbia.txt`):**
   - Expand the tree with clear visual layout (5-wing architecture, non-colliding coordinates $\Delta x \ge 2$, DAG dependency integrity).
   - Integrate the Salonika Trial (`SER_salonika_trial_of_apis`) and military reorganization (`SER_breakthrough_at_dobro_pole`).
   - Implement the 4 Mutually Exclusive Post-War Destinies:
     * `SER_proclamation_of_yugoslavia` (Kingdom of SHS / South Slavic Unification):
       - Mutually exclusive with `SER_restored_sovereign_serbia`, `SER_balkan_socialist_soviet_republic`, `SER_apis_pretorian_military_junta`.
       - Adds idea `SER_yugoslav_kingdom_unification`.
     * `SER_restored_sovereign_serbia` (Greater Serbia Centralism):
       - Mutually exclusive with `SER_proclamation_of_yugoslavia`, `SER_balkan_socialist_soviet_republic`, `SER_apis_pretorian_military_junta`.
       - Adds idea `SER_greater_serbian_hegemony`.
     * `SER_balkan_socialist_soviet_republic` (Balkan Socialist Federation):
       - Mutually exclusive with `SER_proclamation_of_yugoslavia`, `SER_restored_sovereign_serbia`, `SER_apis_pretorian_military_junta`.
       - Adds idea `SER_balkan_soviet_federation`.
     * `SER_apis_pretorian_military_junta` (Black Hand Military State):
       - Mutually exclusive with `SER_proclamation_of_yugoslavia`, `SER_restored_sovereign_serbia`, `SER_balkan_socialist_soviet_republic`.
       - Adds idea `SER_black_hand_junta_rule`.

2. **Ideas (`common/ideas/ww1_serbia_ideas.txt`):**
   - `SER_yugoslav_kingdom_unification`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { stability_factor = 0.10 political_power_gain = 0.15 compliance_growth = 0.20 army_core_defence_factor = 0.10 }`
   - `SER_greater_serbian_hegemony`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { war_support_factor = 0.15 core_defence_factor = 0.15 conscription_factor = 0.10 political_power_gain = 0.10 }`
   - `SER_balkan_soviet_federation`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { communism_drift = 0.10 production_factory_max_efficiency_factor = 0.10 industrial_capacity_factory = 0.10 recruitable_population_factor = 0.10 }`
   - `SER_black_hand_junta_rule`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { neutrality_drift = 0.10 army_attack_factor = 0.15 army_org_factor = 0.10 command_power_gain_mult = 0.25 }`

3. **Validation:**
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_four_yugoslav_destinies -v`.
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v`.
   - Net bracket balance delta = 0 across all files.

4. **Commit:**
   - `git add common/national_focus/serbia.txt common/ideas/ww1_serbia_ideas.txt`
   - `git commit -m "feat(ser): expand Serbian focus tree with 4 distinct political and post-war destinies"`
