# Task 6 Brief: Industrial Relocation, Northeast Loss & Allied Convoys

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. **Populate Decision Categories in `common/decisions/ww1_france_decisions.txt`:**
   In addition to existing decisions in `FRA_western_front_operations`, populate the remaining French categories:

   - **Category `FRA_war_economy_and_munitions`:**
     - `FRA_dec_evacuate_briey_machinery`:
       - Available when at war with Germany.
       - Adds 1 building slot and 1 arms factory in Lyon (state 20) or Massif Central (state 25).
       - Adds +15 to `FRA_charbon_et_acier` and executes `FRA_clamp_dashboard_variables = yes`.
       - Cost: 30 PP. Fire only once.
     - `FRA_dec_lyon_chemical_complex`:
       - Available when at war.
       - Adds 1 arms factory in Rhône (state 20) and temporary production buff.
       - Cost: 35 PP. Fire only once.
     - `FRA_dec_schneider_creusot_heavy_guns`:
       - Available when at war.
       - Grants 100% artillery research bonus or artillery attack boost.
       - Cost: 35 PP. Fire only once.

   - **Category `FRA_defence_of_verdun`:**
     - `FRA_dec_fort_douaumont_reinforcement`:
       - Available when at war with GER and FRA controls state 18.
       - Builds 1 land fort in state 18.
       - Cost: 25 PP.
     - `FRA_dec_voix_sacree_truck_convoys`:
       - Available when at war with GER and state 18 or 16 is contested.
       - Adds +10% division defense and +10 `FRA_poilu_morale`.
       - Cost: 25 PP.

   - **Category `FRA_entente_diplomacy`:**
     - `FRA_dec_inter_allied_supreme_war_council`:
       - Available when at war and in faction with ENG.
       - Adds +40 PP, +5% stability, and increases Entente army coordination.
       - Cost: 30 PP. Fire only once.
     - `FRA_dec_us_morgan_bank_credit_line`:
       - Available when at war and country_exists = USA.
       - Adds +60 PP and +10% factory output.
       - Cost: 20 PP. Fire only once.

   Ensure every decision block includes fast-failing:
   ```clausewitz
   allowed = { original_tag = FRA }
   ```

2. **Verify Modifier Semantic Integrity:**
   Ensure every modifier used inside decisions or ideas is 100% valid via `scripts/hoi4_semantic_oracle.py`.

3. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework -v`.
   - Run `python -m unittest tests.test_ww1_france -v`.
   - Verify bracket balance across `common/decisions/ww1_france_decisions.txt` (Diff = 0).

4. **Commit:**
   `git add common/decisions/ww1_france_decisions.txt common/decisions/categories/ww1_france_categories.txt`
   `git commit -m "feat(fra): populate wartime industrial relocation, Verdun redoubts, and Allied cooperation decisions"`

5. **Report:**
   Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-6-report.md`.
6. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
