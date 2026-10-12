# Task 4 Implementation Report: Historical Events & Territorial Civil War Engine

**Date:** 2026-10-12  
**Target File:** `events/ww1_britain_events.txt`  
**Commit:** `3a8b8cc` (`feat(uk): implement historical crisis events and localized territorial civil war engine`)  
**Status:** COMPLETE (All QA tests pass)

---

## 1. Summary of Changes

Implemented the 5 historical escalation and territorial civil war events for the British Empire's Irish Crisis:

1. **Curragh Mutiny (`ww1_britain_pol.curragh_mutiny`):**
   - Fires between March and August 1914 (`date > 1914.3.1`, `date < 1914.8.1`).
   - **Option A (Cede to Officers):** Lowers Ulster tension (`-20`), increases Irish Nationalist tension (`+15`), `-25` PP, `-5%` stability, sets `ENG_curragh_officers_appeased`.
   - **Option B (Purge Mutineers):** Spikes Ulster tension (`+25`), drops Irish Nationalist tension (`-5`), `-30` Command Power, `+2%` stability, sets `ENG_curragh_officers_purged`.

2. **Gun-Running Crisis (`ww1_britain_pol.larne_howth_guns`):**
   - Fires between July and September 1914 (`date > 1914.7.1`, `date < 1914.9.1`).
   - Escalates both Nationalist and Ulster tension by `+10` each, with tangible stability (`-2%`) and PP (`-10`) penalties.

3. **Overhauled 1916 Easter Rising (`ww1_britain_pol.11`):**
   - Dynamically evaluates garrison status of Leinster / Dublin (State 117):
     - **Secured (`ENG_state_garrison_secured`):** Rising swiftly contained by British garrison; minimal tension increase (`+5`), zero infrastructural damage, positive stability & PP.
     - **Not Secured:** Armed seizure of Dublin GPO; heavy street fighting damaging infrastructure (`level = 2`) and arms factory (`level = 1`), `+25` Nationalist tension, `-8%` stability, `-20` PP.

4. **Territorial Irish Civil War Eruption (`ww1_britain_pol.irish_civil_war`):**
   - Triggers when `ww1_britain_irish_tension > 85` if Irish Question remains unresolved.
   - Sets country flag `ENG_irish_civil_war_fired`.
   - Transitions Pillar 5 spirit to `ENG_irish_civil_war_debacle` via `swap_ideas`.
   - Executes territorial defection: unsecured southern states (113 Munster, 114 Connaught, 117 Leinster) defect to tag `IRE`; secured states and Ulster (119) remain with `ENG`.
   - Applies `can_join_factions = no` rule to `IRE` preventing world war entanglement.
   - Spawns rebel army via OOB loading (`IRE_1936_generic`), granting manpower and weapons stockpile.
   - Executes declaration of war (`declare_war_on = { target = IRE type = civil_war }`).

5. **Post-Capitulation Pacification & Immediate Annexation (`ww1_britain_pol.ireland_pacified`):**
   - Triggers upon capitulation of `IRE` when `has_country_flag = ENG_irish_civil_war_fired`.
   - Annexes `IRE` cleanly back into `ENG` (`annex_country = { target = IRE transfer_troops = no }`).
   - Transitions Pillar 5 idea to `ENG_irish_union_secured`.
   - Resets Irish tensions to 0, sets permanent pacification flags, and awards `+10%` stability and `+50` PP.

---

## 2. Test Verification

1. **`python -m unittest tests/test_ww1_britain_complete_audit.py`**:
   - `test_zero_invalid_modifiers_in_uk_ideas`: **PASS**
   - `test_anti_stacking_limits`: **PASS**
   - `test_decisions_have_no_invalid_modifiers_or_ghost_ideas`: **PASS**
   - `test_events_have_tangible_effects_and_no_empty_options`: **PASS** (Zero empty options found)
   - `test_shortcuts_and_root_focus_localisation`: **PASS**
   - `test_irish_crisis_escalation_and_state_securing_mechanics`: **PASS**
   - **Result:** 6/6 tests PASS.

2. **`python scripts/qa_audit_all.py`**:
   - Clausewitz Syntax & Braces: **PASS** (0 issues)
   - UTF-8 BOM Integrity: **PASS** (0 issues)
   - Mechanical Defines & Subunits: **PASS** (0 issues)
   - Semantic Oracle Audit: **PASS** (0 issues)
   - Full Master Suite: **PASS (Exit Code 0)**
