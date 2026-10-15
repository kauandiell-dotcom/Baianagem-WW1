# Task 4 Brief: Military Mutinies (1917) & Civil Crises Engine (Jusqu'au Bout!)

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. **Crisis National Ideas File:**
   Create `common/ideas/ww1_france_crises_ideas.txt`:
   ```clausewitz
   ideas = {
       country = {
           FRA_trench_mutiny_crisis_2 = {
               picture = generic_discontent
               allowed = { always = no }
               modifier = {
                   army_attack_factor = -0.25
                   breakthrough_factor = -0.15
                   army_core_defence_factor = -0.10
               }
           }
           FRA_poilus_reconcilies = {
               picture = generic_victors_of_ww1
               allowed = { always = no }
               modifier = {
                   army_core_defence_factor = 0.10
                   army_morale_factor = 0.10
               }
           }
           FRA_munitionnettes_strike = {
               picture = generic_production_bonus
               allowed = { always = no }
               modifier = {
                   industrial_capacity_factory = -0.20
                   stability_factor = -0.10
               }
           }
           FRA_jusqu_au_bout_endsieg = {
               picture = generic_war_support
               allowed = { always = no }
               modifier = {
                   army_core_defence_factor = 0.20
                   war_support_factor = 0.15
                   political_power_gain = 0.10
                   surrender_limit = 0.20
               }
           }
       }
   }
   ```
   Audit with `scripts/hoi4_semantic_oracle.py`: 0 errors!

2. **Overhaul Events in `events/ww1_france_events.txt`:**
   - Overhaul `ww1_france.210` (The 1917 Army Mutinies):
     - Trigger: `tag = FRA`, `has_war = yes`, `date > 1916.12.1`, `check_variable = { FRA_poilu_morale < 40 }` (or Nivelle offensive timeout).
     - **CRITICAL**: In `option = { name = ww1_france.210.a ... }`, place `add_ideas = FRA_trench_mutiny_crisis_2` BEFORE any child `country_event` calls:
       ```clausewitz
       option = {
           name = ww1_france.210.a
           add_ideas = FRA_trench_mutiny_crisis_2
           subtract_from_variable = { FRA_poilu_morale = 25 }
           add_stability = -0.10
           add_war_support = -0.10
           country_event = { id = ww1_france.211 days = 2 }
       }
       ```
   - Implement `ww1_france.211` (Pétain Appointed Generalissimo):
     - Option A: Implement Welfare and Leave Reforms (unlocks decision `FRA_petain_welfare_and_leave_reform`).
     - Option B: Draconian tribunals (executes mutineers, -10% stability, risks revolution).
   - Implement `ww1_france.215` (Munitionnettes Strike in Paris):
     - Trigger: `tag = FRA`, `has_war = yes`, `date > 1917.4.1`, `check_variable = { FRA_union_sacree_cohesion < 50 }`.
     - Option A: Concede wage increases (costs 30 PP, restores stability).
     - Option B: Police repression (adds `FRA_munitionnettes_strike`).
   - Implement `ww1_france.220` (Clemenceau's *Jusqu'au Bout!* Speech):
     - Trigger: `tag = FRA`, `has_war = yes`, `surrender_progress > 0.15` OR `date > 1917.11.1`.
     - Option A: *"Je fais la guerre!"* Adds `FRA_jusqu_au_bout_endsieg`, +20% war support.

3. **Decisions File Integration (`common/decisions/ww1_france_decisions.txt`):**
   - Ensure decision `FRA_petain_welfare_and_leave_reform` has:
     - `available = { has_idea = FRA_trench_mutiny_crisis_2 }`
     - `complete_effect = { remove_ideas = FRA_trench_mutiny_crisis_2 add_ideas = FRA_poilus_reconcilies add_to_variable = { FRA_poilu_morale = 30 } add_stability = 0.08 add_war_support = 0.05 }`
   - Include fast-failing `allowed = { tag = FRA }` or `allowed = { original_tag = FRA }`.

4. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_mutinies_and_civil_crises -v`. Must PASS!
   - Verify bracket balance across all modified files (Diff = 0).

5. **Commit:**
   `git add common/ideas/ww1_france_crises_ideas.txt events/ww1_france_events.txt common/decisions/ww1_france_decisions.txt`
   `git commit -m "feat(fra): overhaul 1917 French Army Mutinies, Munitionnettes strikes, and Clemenceau Endsieg"`

6. **Report:**
   Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-4-report.md`.
7. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
