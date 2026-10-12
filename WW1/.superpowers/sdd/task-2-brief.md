# Task 2 Brief: Pillar 5 Ideas Rework (`common/ideas/ww1_britain_ideas.txt`)

## Objective
Implement intense penalties for the initial Irish crisis and define the dynamic Pillar 5 escalation ideas in `common/ideas/ww1_britain_ideas.txt`.

## Context & File
- Target File: `common/ideas/ww1_britain_ideas.txt`
- Spec: `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-irish-crisis-insanity-plan.md`

## Requirements
1. **Update `ENG_irish_home_rule_tension`:**
   Modify the existing idea so its modifier block contains:
   ```txt
   modifier = {
       stability_factor = -0.35
       war_support_factor = -0.15
       political_power_gain = -0.20
       conscription_factor = -0.15
   }
   ```
2. **Add dynamic escalation ideas to `country = { ... }` block in `ww1_britain_ideas.txt`:**
   - `ENG_irish_sabotage_wave`:
     ```txt
     ENG_irish_sabotage_wave = {
         picture = generic_disruption
         allowed = { tag = ENG }
         modifier = {
             stability_factor = -0.45
             war_support_factor = -0.15
             political_power_gain = -0.25
             conscription_factor = -0.25
             industrial_capacity_factory = -0.05
         }
     }
     ```
   - `ENG_irish_martial_law`:
     ```txt
     ENG_irish_martial_law = {
         picture = generic_manpower_bonus
         allowed = { tag = ENG }
         modifier = {
             stability_factor = -0.20
             political_power_gain = -0.15
             army_morale_factor = -0.05
             conscription_factor = -0.10
         }
     }
     ```
   - `ENG_irish_civil_war_debacle`:
     ```txt
     ENG_irish_civil_war_debacle = {
         picture = generic_morale_bonus
         allowed = { tag = ENG }
         modifier = {
             stability_factor = -0.40
             war_support_factor = -0.20
             political_power_gain = -0.30
             army_org_factor = -0.10
         }
     }
     ```
   - `ENG_irish_union_secured`:
     ```txt
     ENG_irish_union_secured = {
         picture = generic_victors_of_ww1
         allowed = { tag = ENG }
         modifier = {
             stability_factor = 0.05
             war_support_factor = 0.05
             conscription_factor = 0.05
         }
     }
     ```
3. **Verify with Clausewitz Semantic Oracle:**
   Run:
   `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/ideas/ww1_britain_ideas.txt'); print(errs); assert len(errs) == 0"`
   Must pass with 0 errors.

4. **Verify partial progress in test suite:**
   Run:
   `python -m unittest tests/test_ww1_britain_complete_audit.py`
   Confirm that the idea-related assertions in `test_irish_crisis_escalation_and_state_securing_mechanics` now PASS (leaving only category, decisions, and event missing).

5. **Commit:**
   `git add common/ideas/ww1_britain_ideas.txt`
   `git commit -m "feat(uk): implement intense penalties and dynamic Pillar 5 Irish crisis ideas"`

6. **Write report to:**
   `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\task-2-report.md`
