# Task 5 Implementation Report: Focus Tree Integration (`common/national_focus/uk.txt`)

**Date:** 2026-10-12  
**Target Files:**
- `common/national_focus/uk.txt`
- `common/ideas/ww1_britain_ideas.txt`  
**Commit:** `f49d04a` (`feat(uk): align DORA wartime focus and post-war settlement with Irish crisis engine`)  
**Status:** COMPLETE (All QA tests and Semantic Oracle checks pass)

---

## 1. Summary of Changes

Integrated the British national focus tree with the Irish Crisis Escalation & State Securing Engine:

1. **Updated Idea Definition (`common/ideas/ww1_britain_ideas.txt`):**
   - Configured `ENG_irish_home_rule_suspended` as the wartime crisis suspension state (1914–1916):
     - `picture = generic_disruption`
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - Modifiers:
       - `stability_factor = -0.25`
       - `war_support_factor = -0.10`
       - `political_power_gain = -0.15`

2. **DORA Wartime Focus Alignment (`ENG_ww1_the_defence_of_the_realm` in `common/national_focus/uk.txt`):**
   - Swapped out bare idea replacement with safe anti-stacking `swap_ideas`:
     - Checks if `ENG_irish_sabotage_wave` is active -> swaps to `ENG_irish_home_rule_suspended`.
     - Checks if `ENG_irish_home_rule_tension` is active -> swaps to `ENG_irish_home_rule_suspended`.
   - Sets flags `ENG_ww1_dora_enacted` and `ENG_ww1_easter_rising_countdown_started`, starting the historical timer toward the 1916 Easter Rising without prematurely wiping out the Irish Crisis upon entering WW1.

3. **Post-War Settlement Focus Alignment (`ENG_ww1_dominion_status_for_ireland` in `common/national_focus/uk.txt`):**
   - Replaced bare `remove_ideas = ENG_irish_home_rule_tension` with exhaustive anti-stacking `swap_ideas`:
     - Safely transitions any active crisis state (`ENG_irish_home_rule_tension`, `ENG_irish_home_rule_suspended`, `ENG_irish_sabotage_wave`, `ENG_irish_martial_law`, or `ENG_irish_civil_war_debacle`) to `ENG_irish_home_rule_compromise`.
   - Retains post-war dominion release event trigger (`country_event = { id = ww1_britain_pol.10 }`), `+15%` stability, and `+75` PP.

---

## 2. Test Verification

1. **Anti-Stacking Limits Test:**
   - Command: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_anti_stacking_limits`
   - **Result:** PASS (0 raw `add_ideas` violations, <= 5 allowed).

2. **Clausewitz Semantic Oracle Audit:**
   - Command: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/ideas/ww1_britain_ideas.txt'); print(errs); assert len(errs) == 0"`
   - **Result:** PASS (0 invalid modifier tokens).

3. **Complete British Audit Suite:**
   - Command: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit`
   - **Result:** 6/6 tests PASS.

4. **Master QA Pipeline (`scripts/qa_audit_all.py`):**
   - Syntax & Brace Integrity: PASS (0 issues)
   - UTF-8 BOM Integrity: PASS (0 issues)
   - UK Semantic Oracle: PASS (0 issues)
   - Full Master Suite: **PASS (Exit Code 0)**
