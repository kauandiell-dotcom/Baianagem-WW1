# Task 6 Brief: Industrial Conglomerates (Škoda, Steyr, Ganz) & Military Rivalries (Conrad vs Boroević)

## Objective
Implement authentic historical industrial cartels and military high command doctrines for Austria-Hungary:
1. Škoda Works (30.5 cm M.11 siege howitzers).
2. Steyr Mannlicher (M1895 straight-pull service rifles and machine guns).
3. Ganz-Danubius (Rijeka/Fiume naval dockyards & Tegetthoff-class dreadnoughts).
4. Franz Conrad von Hötzendorf aggressive offensive doctrine vs Svetozar Boroević von Bojna alpine defensive redoubt doctrine.
5. Strategic decisions for Škoda siege artillery production, Galician oil extraction (Boryslav basin), and Karst/Isonzo defensive fortification lines.

## Context
- Working Directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- Spec: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Plan: `docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md`
- Oracle Tool: `scripts/hoi4_semantic_oracle.py`

## Deliverables
1. `common/ideas/ww1_austria_industry_and_military_ideas.txt`:
   ```clausewitz
   ideas = {
       country = {
           AUH_skoda_305_howitzer = {
               picture = generic_artillery_bonus
               allowed = { always = no }
               modifier = {
                   army_artillery_attack_factor = 0.15
                   breakthrough_factor = 0.10
               }
           }
           AUH_steyr_mannlicher = {
               picture = generic_infantry_bonus
               allowed = { always = no }
               modifier = {
                   production_factory_efficiency_gain_factor = 0.10
                   industrial_capacity_factory = 0.05
               }
           }
           AUH_ganz_danubius = {
               picture = generic_navy_bonus
               allowed = { always = no }
               modifier = {
                   industrial_capacity_dockyard = 0.10
                   navy_max_range_factor = 0.10
               }
           }
           AUH_conrad_offensive_doctrine = {
               picture = generic_militarism_drift_bonus
               allowed = { always = no }
               modifier = {
                   army_attack_factor = 0.10
                   breakthrough_factor = 0.15
                   attrition = 0.10
               }
           }
           AUH_borojevic_alpine_defense = {
               picture = generic_intel_bonus
               allowed = { always = no }
               modifier = {
                   army_core_defence_factor = 0.15
                   dig_in_speed_factor = 0.20
               }
           }
       }
   }
   ```
   *Note: Audit every modifier with `python scripts/hoi4_semantic_oracle.py` to ensure 0 invalid modifiers.*

2. `common/decisions/ww1_austria_skoda_decisions.txt`:
   - Decision category: `AUH_crown_dashboard` or `AUH_war_effort_category`
   - Include fast-failing `allowed = { original_tag = AUS }`
   - Decisions:
     - `AUH_dec_skoda_siege_howitzers`: commissions 30.5cm batteries (adds artillery to stockpile, grants `AUH_skoda_305_howitzer` or adds temporary siege bonus, costs factory output or PP).
     - `AUH_dec_galician_oil_extraction`: develops Boryslav oilfields in state 88 (adds synthetic refinery or resource extraction bonus).
     - `AUH_dec_steep_alpine_redoubts`: fortifies the Isonzo/Tyrol mountain passes (adds land forts in mountain border states, boosts dig-in).

3. `common/national_focus/austria.txt`:
   - Ensure military and industrial branches reference these ideas and decisions appropriately (or connect them cleanly without breaking existing layout).

4. Verification:
   - Run `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_skoda_and_three_armies_modifiers -v` -> MUST PASS!
   - Run `python -c "import scripts.hoi4_semantic_oracle as o; print(o.audit_file_modifiers('common/ideas/ww1_austria_industry_and_military_ideas.txt'))"` -> Empty list `[]` (0 errors).
   - Net bracket delta = 0 across all modified and created files.

5. Commit:
   - `git add common/ideas/ww1_austria_industry_and_military_ideas.txt common/decisions/ww1_austria_skoda_decisions.txt`
   - `git commit -m "feat(auh): implement Škoda 30.5cm artillery, Steyr arms, Conrad vs Boroević doctrines, and Galician oil"`
