# Task 1 Report: QA RED Test Baseline (`tests/test_ww1_austria_hungary.py`)

## Status: COMPLETE (RED Phase Verified)

### Summary of Work Done
1. **Created Test Suite `tests/test_ww1_austria_hungary.py`**:
   - Implemented `TestAustriaHungaryOverhaul` with all 7 required test methods driving TDD for the entire Austria-Hungary overhaul:
     - `test_austria_no_day1_crisis`: Verifies that collapse events in `events/ww1_austria_collapse_events.txt` cannot trigger on Day 1 (1911 peacetime) by requiring `has_war = yes`, `date > 1915`, and either `surrender_progress > 0.40` or loss of core states (Vienna 4, Budapest 43, Galicia 88).
     - `test_constitutional_four_paths`: Verifies that the 4 constitutional paths (`AUH_ww1_dualism`, `AUH_ww1_trialism`, `AUH_ww1_federalism`, `AUH_ww1_military_dictatorship`) are defined in `common/national_focus/austria.txt`, are mutually exclusive, and award distinct ideas (`AUH_idea_dualism_iron`, `AUH_idea_habsburg_trialism`, `AUH_idea_danubian_federation_spirit`, `AUH_idea_aok_military_dictatorship`).
     - `test_danubian_mega_federation_setup`: Verifies `AUH_spawn_danubian_mega_federation` in `common/scripted_effects/ww1_danubian_federation_effects.txt`, releasing `HUN`, `CZE`, `CRO`, `POL` with imperial color matching `rgb { 202 198 188 }`, assigning high-centralization subject idea `AUH_danubian_federal_member`, and spawning 4 to 18 divisions per member.
     - `test_tag_safe_breakaway_rules`: Verifies 0 dynamic `start_civil_war` calls, mandatory `can_join_factions = no` on breakaway tags, and anti-faction AI strategy in `common/ai_strategy/ww1_auh_rebel_ai_strategy.txt`.
     - `test_crown_dashboard_and_grain`: Verifies the 3 survival vectors (`AUH_war_weariness`, `AUH_cohesion`, `AUH_vienna_grain`), 0–100 clamping, category `AUH_crown_dashboard`, decisions, and on-action hooks.
     - `test_skoda_and_three_armies_modifiers`: Connects with `scripts/hoi4_semantic_oracle.py` to ensure all modifier tokens in ideas `AUH_skoda_305_howitzer`, `AUH_steyr_mannlicher`, `AUH_ganz_danubius`, `AUH_conrad_offensive_doctrine`, and `AUH_borojevic_alpine_defense` are 100% valid Clausewitz modifiers.
     - `test_localisation_bom_and_parity`: Verifies single UTF-8 BOM (`\xef\xbb\xbf`), 0 double BOM, and 100% key parity between `ww1_austria_rework_l_english.yml` and `ww1_austria_rework_l_braz_por.yml`.

2. **Registered Suite in `scripts/qa_audit_all.py`**:
   - Added `"tests.test_ww1_austria_hungary"` as Suite 12 in `SUITES`.
   - Added execution block 12 in `main()`, returning `res_auh.returncode` and printing status.

3. **Verification (RED Phase)**:
   - Direct execution: `python -m unittest tests.test_ww1_austria_hungary -v`
     - Result: `Ran 7 tests in 0.042s` -> `FAILED (failures=7)`
     - All 7 tests fail cleanly on unbuilt components without syntax or import errors.
   - Master audit: `python scripts/qa_audit_all.py`
     - Result: Static checks (0 errors), Suites 1–11 passed (return code 0), Suite 12 ran and failed as expected (`AUH: 1`).

### Git Commit
- Hash: `c4a9f18`
- Message: `test(auh): establish RED QA test suite for Austria-Hungary complete rework`

### Concerns / Notes for Subsequent Tasks
- Task 2 can now proceed to implement the Crown Dashboard & 3 Survival Vectors (`test_crown_dashboard_and_grain`).
