# Task 3 Brief: Republic Dashboard & The 4 Dynamic Survival Vectors

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. **Scripted Effects File:**
   Create `common/scripted_effects/ww1_france_dashboard_effects.txt`:
   - `FRA_init_republic_dashboard`:
     ```clausewitz
     FRA_init_republic_dashboard = {
         set_variable = { FRA_union_sacree_cohesion = 80 }
         set_variable = { FRA_poilu_morale = 75 }
         set_variable = { FRA_charbon_et_acier = 70 }
         set_variable = { FRA_reserves_humaines = 85 }
     }
     ```
   - `FRA_clamp_dashboard_variables`:
     Must clamp all 4 variables between 0 and 100:
     ```clausewitz
     FRA_clamp_dashboard_variables = {
         clamp_variable = { var = FRA_union_sacree_cohesion min = 0 max = 100 }
         clamp_variable = { var = FRA_poilu_morale min = 0 max = 100 }
         clamp_variable = { var = FRA_charbon_et_acier min = 0 max = 100 }
         clamp_variable = { var = FRA_reserves_humaines min = 0 max = 100 }
     }
     ```
   - `FRA_weekly_republic_tick`:
     - When at war:
       - Consumes coal and steel: -1 per week (`subtract_from_variable = { FRA_charbon_et_acier = 1 }`). If enemy controls state 18 (Briey) or state 28 (Nord-Pas-de-Calais), extra -1 coal/steel.
       - Adjusts poilu morale based on casualties or enemy advances.
       - Adjusts Union Sacrée cohesion.
       - Executes `FRA_clamp_dashboard_variables = yes`.
       - Dynamically updates spirits:
         - If `FRA_union_sacree_cohesion < 30`: swap/add `FRA_union_sacree_fractured`; else remove it.
         - If `FRA_poilu_morale < 30`: trigger check for mutinies or apply `FRA_poilu_morale_demoralized`.
         - If `FRA_charbon_et_acier < 25`: add `FRA_charbon_et_acier_famine`; if >= 50 remove it.

2. **On-Actions Hook:**
   Modify `common/on_actions/ww1_crisis_on_actions.txt`:
   Under `on_weekly_FRA`:
   ```clausewitz
   on_weekly_FRA = {
       effect = {
           ww1_FRA_update_crisis = yes
           if = {
               limit = { tag = FRA }
               if = {
                   limit = { NOT = { has_country_flag = fra_dashboard_initialized } }
                   FRA_init_republic_dashboard = yes
                   set_country_flag = fra_dashboard_initialized
               }
               FRA_clamp_dashboard_variables = yes
               FRA_weekly_republic_tick = yes
           }
       }
   }
   ```

3. **Dashboard Dynamic Ideas File:**
   Create `common/ideas/ww1_france_dashboard_ideas.txt`:
   Ideas block:
   ```clausewitz
   ideas = {
       country = {
           FRA_union_sacree_strong = {
               picture = generic_democracy
               allowed = { always = no }
               modifier = {
                   stability_factor = 0.08
                   political_power_gain = 0.10
               }
           }
           FRA_union_sacree_fractured = {
               picture = generic_discontent
               allowed = { always = no }
               modifier = {
                   stability_factor = -0.15
                   political_power_gain = -0.15
               }
           }
           FRA_poilu_morale_high = {
               picture = generic_morale
               allowed = { always = no }
               modifier = {
                   army_morale_factor = 0.10
                   army_core_defence_factor = 0.10
               }
           }
           FRA_poilu_morale_demoralized = {
               picture = generic_intel_bonus
               allowed = { always = no }
               modifier = {
                   army_morale_factor = -0.20
                   army_attack_factor = -0.15
               }
           }
           FRA_charbon_et_acier_surplus = {
               picture = generic_production_bonus
               allowed = { always = no }
               modifier = {
                   industrial_capacity_factory = 0.10
               }
           }
           FRA_charbon_et_acier_famine = {
               picture = generic_economic_increase
               allowed = { always = no }
               modifier = {
                   industrial_capacity_factory = -0.25
                   consumer_goods_factor = 0.05
               }
           }
       }
   }
   ```
   Audit with `scripts/hoi4_semantic_oracle.py`: 0 errors!

4. **Emergency Survival Decisions File:**
   Create `common/decisions/ww1_france_dashboard_decisions.txt`:
   Category `FRA_war_economy_and_munitions` or `FRA_third_republic_politics` (both in `common/decisions/categories/ww1_france_categories.txt`):
   - `FRA_dec_british_channel_coal`:
     - Fast-failing `allowed = { original_tag = FRA }`, `visible = { has_war = yes country_exists = ENG }`
     - Cost: 25 PP
     - Adds 20 to `FRA_charbon_et_acier`, clamps variables.
   - `FRA_dec_call_up_class_1917`:
     - Fast-failing `allowed = { original_tag = FRA }`, `visible = { has_war = yes date > 1916.6.1 }`
     - Cost: 30 PP
     - Adds 50,000 manpower, adds 15 to `FRA_reserves_humaines`, -5% stability.
   - `FRA_dec_colonial_recruitment_tirailleurs`:
     - Fast-failing `allowed = { original_tag = FRA }`, `visible = { has_war = yes }`
     - Cost: 35 PP
     - Adds 60,000 manpower, +10 to `FRA_reserves_humaines`.
   - `FRA_dec_union_sacree_cross_party_pact`:
     - Fast-failing `allowed = { original_tag = FRA }`, `visible = { has_war = yes }`
     - Cost: 30 PP
     - Adds 15 to `FRA_union_sacree_cohesion`, +5% stability.

5. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_republic_dashboard_variables -v`. Must PASS!
   - Verify bracket balance across all files (Diff = 0).
   - Check modifier validity with `scripts/hoi4_semantic_oracle.py`.

6. **Commit:**
   `git add common/scripted_effects/ww1_france_dashboard_effects.txt common/on_actions/ww1_crisis_on_actions.txt common/ideas/ww1_france_dashboard_ideas.txt common/decisions/ww1_france_dashboard_decisions.txt`
   `git commit -m "feat(fra): implement French Republic Dashboard, 4 survival vectors, and emergency decisions"`

7. **Report:**
   Write report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-3-report.md`.
8. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
