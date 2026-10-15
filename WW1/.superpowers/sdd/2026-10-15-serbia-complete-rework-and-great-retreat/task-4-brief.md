# Task 4 Brief: 1914 Crisis, Belgrade Defense (Major Gavrilović) & 1915 Typhus Epidemic

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`

## Objectives
1. **Events (`events/ww1_serbia_events.txt`):**
   - Enhance `ww1_serbia.7` (Sarajevo Conspiracy):
     - Option A: Suppress Black Hand plot and warn Vienna (shifts BoP towards Pašić, risks military discontent).
     - Option B: Tacit support / look away (shifts BoP towards Apis, boosts war support).
   - Enhance `ww1_serbia.8` (Austrian Ultimatum):
     - Options for conditional acceptance (historical Pašić response) vs outright defiant rejection.
   - Implement `ww1_serbia.20`: *The 1915 Typhus Epidemic*:
     - Trigger: `tag = SER`, `date > 1915.1.1`, `has_war = yes`.
     - Adds idea `SER_typhus_epidemic_crisis`.
   - Implement `ww1_serbia.21`: *Arrival of Dr. Elsie Inglis & Scottish Women's Hospitals*:
     - Removes `SER_typhus_epidemic_crisis`, adds `SER_foreign_medical_missions_aid`, restores manpower.
   - Implement `ww1_serbia.22`: *Radoje Ljutovac's Anti-Aircraft Shootdown in Kragujevac*:
     - Historic first anti-aircraft gun kill (30 September 1915).
     - Awards artillery research bonus and PP.

2. **Decisions (`common/decisions/ww1_serbia_decisions.txt`):**
   - Ensure category `SER_military_operations` or dedicated Serbian category exists with fast-failing `allowed = { original_tag = SER }`.
   - Implement `SER_dec_major_gavrilovic_last_stand`:
     - Available when at war, enemy controls neighboring states or attacks state 107 (Belgrade).
     - Adds idea `SER_major_gavrilovic_spirit`.
   - Implement `SER_dec_scottish_women_hospitals`:
     - Available when `has_idea = SER_typhus_epidemic_crisis`.
     - Triggers `ww1_serbia.21`.

3. **Ideas (`common/ideas/ww1_serbia_ideas.txt`):**
   - `SER_major_gavrilovic_spirit`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { army_core_defence_factor = 0.20 dig_in_speed_factor = 0.25 max_dig_in = 5 }`
   - `SER_typhus_epidemic_crisis`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { attrition = 0.15 army_org_factor = -0.15 monthly_population = -0.30 }`
   - `SER_foreign_medical_missions_aid`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { attrition = -0.10 army_org_factor = 0.05 monthly_population = 0.10 }`

4. **Validation:**
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_belgrade_defense_and_typhus_crisis -v`.
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v`.
   - Net bracket balance delta = 0 across all files.

5. **Commit:**
   - `git add events/ww1_serbia_events.txt common/decisions/ww1_serbia_decisions.txt common/ideas/ww1_serbia_ideas.txt`
   - `git commit -m "feat(ser): implement Major Gavrilovic defense, Sarajevo investigation, and typhus crisis"`
