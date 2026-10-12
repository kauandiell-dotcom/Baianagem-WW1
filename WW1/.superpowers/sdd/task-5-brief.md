# Task 5 Brief: Focus Tree Integration (`common/national_focus/uk.txt`)

## Objective
Update British national focus tree wartime focus `ENG_ww1_the_defence_of_the_realm` (DORA, 1914) and post-war settlement focus `ENG_ww1_dominion_status_for_ireland` in `common/national_focus/uk.txt`, and update `ENG_irish_home_rule_suspended` in `common/ideas/ww1_britain_ideas.txt`.

## Context & Files
- Target Focus File: `common/national_focus/uk.txt`
- Target Ideas File: `common/ideas/ww1_britain_ideas.txt`
- Spec: `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-irish-crisis-insanity-plan.md`

## Requirements
1. **In `common/ideas/ww1_britain_ideas.txt`:**
   Update `ENG_irish_home_rule_suspended`:
   ```txt
   ENG_irish_home_rule_suspended = {
       picture = generic_disruption
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           stability_factor = -0.25
           war_support_factor = -0.10
           political_power_gain = -0.15
       }
   }
   ```

2. **In `common/national_focus/uk.txt`:**
   - In focus `ENG_ww1_the_defence_of_the_realm` completion reward:
     Ensure it cleanly swaps active Pillar 5 idea (`ENG_irish_home_rule_tension` or `ENG_irish_sabotage_wave`) to `ENG_irish_home_rule_suspended`.
     Set country flags `ENG_ww1_dora_enacted` and `ENG_ww1_easter_rising_countdown_started`.
   - In focus `ENG_ww1_dominion_status_for_ireland` completion reward:
     Replace `remove_ideas = ENG_irish_home_rule_tension` with safe anti-stacking `swap_ideas`:
     Swapping `ENG_irish_home_rule_tension`, `ENG_irish_home_rule_suspended`, or `ENG_irish_sabotage_wave` to `ENG_irish_home_rule_compromise`.

3. **Verify anti-stacking test:**
   Run:
   `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_anti_stacking_limits`
   Must PASS.

4. **Verify Oracle:**
   `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/ideas/ww1_britain_ideas.txt'); print(errs); assert len(errs) == 0"`

5. **Commit:**
   `git add common/national_focus/uk.txt common/ideas/ww1_britain_ideas.txt`
   `git commit -m "feat(uk): align DORA wartime focus and post-war settlement with Irish crisis engine"`

6. **Write report to:**
   `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\task-5-report.md`
