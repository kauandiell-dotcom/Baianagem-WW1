# Task 2 Brief: Agadir Crisis Interactive Escalation Engine (1911)

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. **Decision Category:**
   Create `common/decisions/categories/ww1_agadir_crisis_categories.txt`:
   ```clausewitz
   ww1_agadir_crisis = {
       icon = generic_diplomacy
       picture = decision_cat_generic
       priority = 100
       allowed = {
           OR = {
               tag = GER
               tag = FRA
               tag = ENG
           }
       }
       visible = {
           has_global_flag = agadir_crisis_active
       }
   }
   ```
2. **Interactive Decisions:**
   Create `common/decisions/ww1_agadir_crisis_decisions.txt` in category `ww1_agadir_crisis`:
   - **Germany (`GER_agadir_`):**
     - `GER_agadir_demand_naval_base`: Demands coaling station / naval base in Agadir (state 462). Costs 30 PP, increases tension `add_to_variable = { global.ww1_agadir_crisis_tension = 25 }`, sets country flag `ger_agadir_demanded_naval_base`.
     - `GER_agadir_demand_congo_compensation`: Demands French Congo (*Neukamerun*, states 1086, 1087, 1088). Costs 25 PP, `add_to_variable = { global.ww1_agadir_crisis_tension = 10 }`, sets flag `ger_agadir_demanded_congo`.
     - `GER_agadir_send_sms_berlin`: Dispatches SMS *Berlin* to reinforce *Panther*. Costs 20 PP, `add_to_variable = { global.ww1_agadir_crisis_tension = 15 }`, adds 5% war support.
     - `GER_agadir_back_down_gracefully`: Recalls *Panther* empty-handed. Lowers tension by 30, triggers `ww1_agadir.30` (German Humiliation).
   - **France (`FRA_agadir_`):**
     - `FRA_agadir_caillaux_secret_channel`: Caillaux's secret backchannel talks. Costs 30 PP, `subtract_from_variable = { global.ww1_agadir_crisis_tension = 20 }`, sets country flag `fra_caillaux_secret_talks`.
     - `FRA_agadir_delcasse_firm_resolve`: Hardline nationalist defiance. Costs 25 PP, `add_to_variable = { global.ww1_agadir_crisis_tension = 20 }`, adds 10% war support, appeals to Britain.
     - `FRA_agadir_financial_sanctions`: Withdraws French bank short-term credit from Berlin. Costs 20 PP, hits GER stability and PP (-50 PP).
     - `FRA_agadir_concede_congo_accord`: Formally concludes Treaty of Fez and Congo Accord (fires `ww1_agadir.10`).
   - **Britain (`ENG_agadir_`):**
     - `ENG_agadir_mansion_house_speech`: Lloyd George's speech. Costs 25 PP, `add_to_variable = { global.ww1_agadir_crisis_tension = 15 }`, gives guarantee to France, draws red line against German Atlantic base.
     - `ENG_agadir_home_fleet_alert`: Ready the Home Fleet at Portland. Costs 30 PP, `add_to_variable = { global.ww1_agadir_crisis_tension = 15 }`, alarms Berlin.
     - `ENG_agadir_urge_moderation`: Advises Paris to offer colonial compensation. Costs 15 PP, `subtract_from_variable = { global.ww1_agadir_crisis_tension = 15 }`.

   Ensure all decisions have fast-failing `allowed = { tag = ... }` or `allowed = { original_tag = ... }` and `visible = { has_global_flag = agadir_crisis_active }`.

3. **Overhaul Events in `events/WW1_Agadir.txt`:**
   - Define namespace: `add_namespace = ww1_agadir`
   - `ww1_agadir.1`: *Panthersprung* (SMS Panther anchors at Agadir). Sets `has_global_flag = agadir_crisis_active`, initializes `set_variable = { global.ww1_agadir_crisis_tension = 25 }`. Fires notification to FRA and ENG.
   - `ww1_agadir.10`: *The Morocco-Congo Accord & Treaty of Fez (Historical Climax)*:
     - Germany recognizes French Protectorate over Morocco (`FRA = { add_ideas = FRA_morocco_treaty_of_fez }`).
     - France transfers Neukamerun:
       ```clausewitz
       773 = { add_extra_state_shared_building_slots = 2 }
       GER = {
           transfer_state = 1086
           transfer_state = 1087
           transfer_state = 1088
       }
       ```
     - Leaks Caillaux's secret diplomacy: Caillaux cabinet falls, Raymond Poincaré becomes Premier.
     - Clears `agadir_crisis_active`, sets `agadir_crisis_resolved_historical`.
   - `ww1_agadir.20`: *Pan-German Triumph: Naval Station at Agadir*:
     - Germany secures naval rights in Agadir: state 462 gets coastal fort and naval base, GER gets Atlantic base.
     - France loses 10% stability and 50 PP. Clears `agadir_crisis_active`.
   - `ww1_agadir.30`: *The German Retreat (Panther Withdrawn)*:
     - Germany recalls Panther with zero colonial gains.
     - Germany loses 100 PP and 5% stability. Furthers military rage and the 1912/1913 Army Expansion Bills.
     - France retains 1086, 1087, 1088 and proclaims Moroccan protectorate. Clears `agadir_crisis_active`.
   - `ww1_agadir.40`: *The Premature Conflagration: World War I in 1911*:
     - Triggers if tension hits 100.
     - Germany and France/Britain go to war: `GER = { declare_war_on = { target = FRA type = annex_everything } }`.
     - Clears `agadir_crisis_active`.

4. **On-Actions Hook:**
   - In `common/on_actions/ww1_crisis_on_actions.txt`:
     - Under `on_weekly_GER`:
       Ensure that when `has_global_flag = agadir_crisis_active`, it checks if `global.ww1_agadir_crisis_tension >= 100`, firing `ww1_agadir.40`. Also clamps `global.ww1_agadir_crisis_tension` min 0 max 100 via `clamp_variable = { var = global.ww1_agadir_crisis_tension min = 0 max = 100 }`.

5. **Focus Tree Integration:**
   - In `common/national_focus/france.txt`:
     - `FRA_question_du_maroc_1911`, `FRA_fermete_diplomatique_agadir`, `FRA_compromis_colonial_allemand`: align completion rewards with the crisis tension variable and decisions.
   - In `common/national_focus/germany.txt`:
     - `GER_agadir_crisis_gambit`: add +15 to `global.ww1_agadir_crisis_tension` and set `agadir_crisis_active = yes` if not already fired.

6. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_agadir_crisis_mechanics -v`. Must PASS!
   - Verify bracket balance across all files (Diff = 0).
   - Check with `python -m unittest tests.test_runner -v` to ensure Germany focus tree spec is intact.

7. **Commit:**
   - `git add common/decisions/categories/ww1_agadir_crisis_categories.txt common/decisions/ww1_agadir_crisis_decisions.txt events/WW1_Agadir.txt common/on_actions/ww1_crisis_on_actions.txt common/national_focus/france.txt common/national_focus/germany.txt`
   - `git commit -m "feat(agadir): implement complete interactive Agadir Crisis escalation engine and 4 climax branches"`

8. **Report:**
   Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-2-report.md`.
