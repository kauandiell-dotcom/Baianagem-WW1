# Task 3 Brief: The Great Retreat, Salonika Sanctuary & 28-30 Division Mobilization Engine

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`

## Objectives
1. **Ideas (`common/ideas/ww1_serbia_ideas.txt`):**
   - Implement `SER_otadzbina_u_pokretu`:
     ```pdx
     SER_otadzbina_u_pokretu = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             surrender_limit = 0.40
             army_core_defence_factor = 0.25
             attrition = -0.15
             out_of_supply_factor = -0.30
             stability_factor = 0.10
         }
     }
     ```
   - Implement `SER_oath_of_corfu_martyrs`:
     ```pdx
     SER_oath_of_corfu_martyrs = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             war_support_factor = 0.15
             army_org_factor = 0.10
             recruitable_population_factor = 0.10
         }
     }
     ```
   - Fix pre-existing semantic issue in `SER_yugoslav_brotherhood_charter`: replace invalid token `compliance_growth_focus_factor` with valid token `compliance_growth`.

2. **Events (`events/ww1_serbia_retreat_events.txt`):**
   - Declare `add_namespace = ww1_serbia_retreat`.
   - Event `ww1_serbia_retreat.1` (*The Great Retreat across the Albanian Alps - Albanska Golgota*):
     - Trigger: `tag = SER`, `has_war = yes`, `NOT = { controls_state = 107 }`, `NOT = { has_country_flag = ser_executed_great_retreat }`.
     - Effects:
       - `set_country_flag = ser_executed_great_retreat`
       - `184 = { add_core_of = SER }`
       - `44 = { add_core_of = SER }`
       - `add_ideas = SER_otadzbina_u_pokretu`
       - Calls `country_event = { id = ww1_serbia_retreat.2 days = 1 }`
   - Event `ww1_serbia_retreat.2` (*The Sanctuary of Salonika - Allied Balkan Front*):
     - Provides military/control integration of Salonika base (state 184).
   - Event `ww1_serbia_retreat.10` (*The Battle of Mojkovac - The Montenegrin Rearguard*):
     - Morale and defensive buffs delaying enemy advance.
   - Event `ww1_serbia_retreat.15` (*Essad Pasha Toptani's Corridor*):
     - Diplomatic safe passage through Durrës and Tirana (state 44).
   - Event `ww1_serbia_retreat.20` (*The Blue Graveyard of Vido - Plava Grobnica*):
     - Corfu memorial for the fallen; awards `SER_oath_of_corfu_martyrs`.
   - Event `ww1_serbia_retreat.25` (*The Odessa Volunteer Division*):
     - Arrival of South Slavic volunteer forces from Russia.

3. **Decisions (`common/decisions/categories/ww1_serbia_decision_categories.txt` & `common/decisions/ww1_serbia_retreat_decisions.txt`):**
   - Ensure category `ww1_serbia_great_retreat` exists with fast-failing `allowed = { original_tag = SER }`.
   - In `ww1_serbia_retreat_decisions.txt`, include fast-failing `allowed = { original_tag = SER }`.
   - Implement the 4 mass mobilization decisions:
     * `SER_spawn_conscript_regiments_1896_1899`: Spawns 8 Conscript Infantry Divisions (prioritizing capital or controlled states: 184, 44, 105, 107).
     * `SER_spawn_yugoslav_volunteer_corps`: Spawns 8 Yugoslav Volunteer Divisions.
     * `SER_spawn_french_allied_brigades`: Spawns 6 French-equipped Shock Artillery Divisions.
     * `SER_spawn_toplica_chetnik_uprising`: Spawns 6-8 Chetnik Irregular Divisions in states 107 and 108.

4. **Automated AI Fallback in `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`:**
   - Under `SER` block in `on_weekly`:
     - If `tag = SER`, `has_war = yes`, `NOT = { controls_state = 107 }`, and `NOT = { has_country_flag = ser_executed_great_retreat }`:
       - Trigger `ww1_serbia_retreat.1` and execute mobilization decisions automatically so AI Bot never gets stuck.

5. **Validation:**
   - Run tests:
     `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_great_retreat_and_sanctuary_mechanics -v`
     `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_salonika_thirty_divisions_spawns -v`
     `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_vido_memorial_and_essad_pasha -v`
     `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v`
   - Check bracket balance across all files (Diff = 0).
   - Commit: `git add ...` and `git commit -m "feat(ser): implement Great Retreat sanctuary, 30-division mobilization, and core expansion"`
   - Output summary and commit hash.
