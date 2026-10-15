# Task 5 Brief: The 4 Divergent Political Destinies & Focus Tree Expansion

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. **Political Ideas File:**
   Create `common/ideas/ww1_france_political_ideas.txt`:
   ```clausewitz
   ideas = {
       country = {
           FRA_union_sacree_spirit = {
               picture = generic_democracy
               allowed = { always = no }
               modifier = {
                   stability_factor = 0.10
                   political_power_gain = 0.15
                   war_support_factor = 0.05
               }
           }
           FRA_commune_de_paris_spirit = {
               picture = generic_communism
               allowed = { always = no }
               modifier = {
                   conscription_factor = 0.15
                   production_factory_max_efficiency_factor = 0.10
                   war_support_factor = 0.10
               }
           }
           FRA_action_francaise_monarchy = {
               picture = generic_monarchism
               allowed = { always = no }
               modifier = {
                   army_core_defence_factor = 0.15
                   war_support_factor = 0.15
                   stability_factor = 0.05
               }
           }
           FRA_gqg_military_directory = {
               picture = generic_junta
               allowed = { always = no }
               modifier = {
                   army_attack_factor = 0.10
                   breakthrough_factor = 0.10
                   mobilization_speed = 0.20
               }
           }
       }
   }
   ```
   Audit with `scripts/hoi4_semantic_oracle.py`: 0 errors!

2. **Characters Integration (`common/characters/FRA.txt`):**
   Add or verify characters:
   - `FRA_charles_maurras` (political advisor / ideologue for Action Française)
   - `FRA_king_jean_iii` (Monarchist country leader, House of Orléans)
   - `FRA_jean_longuet` (Communist / SFIO pacifist leader)
   - `FRA_fernand_loriot` (Revolutionary Syndicalist leader)
   - `FRA_georges_clemenceau` (Prime Minister / Political advisor)
   Ensure portraits use existing valid assets (e.g. `GFX_portrait_...` or generic equivalents).

3. **Expand Focus Tree (`common/national_focus/france.txt`):**
   Expand the Political Wing (x = 0..25) with the 4 mutually exclusive branches:
   - **Branch 1: Third Republic & Union Sacrée (Democratic)**
     - `FRA_republique_union_sacree`:
       `x = 2`, `y = 6`, `cost = 8`
       `prerequisite = { focus = FRA_presidence_poincare focus = FRA_presidence_pams }`
       `mutually_exclusive = { focus = FRA_republique_des_soviets_de_paris focus = FRA_abattre_la_gueuse focus = FRA_directoire_militaire_gqg }`
       `completion_reward = { add_ideas = FRA_union_sacree_spirit add_political_power = 60 add_stability = 0.05 add_to_variable = { FRA_union_sacree_cohesion = 20 } FRA_clamp_dashboard_variables = yes }`
     - `FRA_clemenceau_je_fais_la_guerre`:
       `x = 2`, `y = 7`, `cost = 8`
       `prerequisite = { focus = FRA_republique_union_sacree }`
       `completion_reward = { add_ideas = FRA_jusqu_au_bout_endsieg set_politics = { ruling_party = democratic elections_allowed = yes } add_war_support = 0.15 }`
   - **Branch 2: Second Paris Commune (Communism)**
     - `FRA_republique_des_soviets_de_paris`:
       `x = 7`, `y = 6`, `cost = 8`
       `prerequisite = { focus = FRA_essor_de_la_sfio }`
       `mutually_exclusive = { focus = FRA_republique_union_sacree focus = FRA_abattre_la_gueuse focus = FRA_directoire_militaire_gqg }`
       `completion_reward = { add_ideas = FRA_commune_de_paris_spirit set_politics = { ruling_party = communism elections_allowed = no } set_popularities = { communism = 60 democratic = 20 neutrality = 15 fascism = 5 } promote_character = FRA_fernand_loriot add_stability = -0.10 }`
     - `FRA_comite_de_salut_public_1917`:
       `x = 7`, `y = 7`, `cost = 8`
       `prerequisite = { focus = FRA_republique_des_soviets_de_paris }`
       `completion_reward = { add_political_power = 50 add_war_support = 0.10 }`
   - **Branch 3: Action Française & Orléans Monarchy (Neutrality / Monarchism)**
     - `FRA_abattre_la_gueuse`:
       `x = 12`, `y = 6`, `cost = 8`
       `prerequisite = { focus = FRA_preserver_la_republique }`
       `mutually_exclusive = { focus = FRA_republique_union_sacree focus = FRA_republique_des_soviets_de_paris focus = FRA_directoire_militaire_gqg }`
       `completion_reward = { add_ideas = FRA_action_francaise_monarchy set_politics = { ruling_party = neutrality elections_allowed = no } set_popularities = { neutrality = 55 democratic = 25 fascism = 15 communism = 5 } add_political_power = 50 }`
     - `FRA_restauration_orleaniste_jean_iii`:
       `x = 12`, `y = 7`, `cost = 8`
       `prerequisite = { focus = FRA_abattre_la_gueuse }`
       `completion_reward = { promote_character = FRA_king_jean_iii add_stability = 0.10 add_war_support = 0.10 }`
   - **Branch 4: GQG Military Directory (Authoritarian / Non-Aligned)**
     - `FRA_directoire_militaire_gqg`:
       `x = 17`, `y = 6`, `cost = 8`
       `prerequisite = { focus = FRA_preserver_la_republique }`
       `mutually_exclusive = { focus = FRA_republique_union_sacree focus = FRA_republique_des_soviets_de_paris focus = FRA_abattre_la_gueuse }`
       `completion_reward = { add_ideas = FRA_gqg_military_directory set_politics = { ruling_party = neutrality elections_allowed = no } add_war_support = 0.15 }`
     - `FRA_etat_de_siege_permanent`:
       `x = 17`, `y = 7`, `cost = 8`
       `prerequisite = { focus = FRA_directoire_militaire_gqg }`
       `completion_reward = { add_stability = 0.05 add_political_power = 40 }`

   *Note on Coordinates:* All 4 branches use non-colliding coordinates (`x = 2, 7, 12, 17`, `y = 6, 7`). Check that no other focuses in `france.txt` occupy these positions.
   *Net bracket balance must be 0!*

4. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_four_political_destinies -v`. Must PASS!
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_semantic_oracle_modifiers -v`. Must PASS!
   - Run `python -m unittest tests.test_ww1_france -v`. 8/8 PASS!
   - Check bracket balance across `france.txt` and `ww1_france_political_ideas.txt`.

5. **Commit:**
   `git add common/national_focus/france.txt common/ideas/ww1_france_political_ideas.txt common/characters/FRA.txt`
   `git commit -m "feat(fra): implement 4 divergent political destinies, Action Française, Commune, and GQG Directory"`

6. **Report:**
   Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-5-report.md`.
7. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
