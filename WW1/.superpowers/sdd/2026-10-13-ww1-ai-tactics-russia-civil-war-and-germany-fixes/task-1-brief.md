# Task 1 Brief: QA RED Test Baseline

## Goal
Establish a comprehensive automated unit test suite in `tests/test_ww1_ai_and_russia_fixes.py` with 5 test cases covering:
1. `test_ai_tactical_defines`: Verifies `common/defines/ww1_ai_defines.lua` sets high planning threshold (0.65+), attack cancellation efficiency (0.60+), org preservation (0.45+), and army consolidation (24 divisions cap).
2. `test_bulgaria_alliance_and_war_call`: Verifies `ww1_germany_events.33` calls Bulgaria to arms against Serbia and Entente, and `common/ai_strategy/ww1_bulgaria_ai_strategy.txt` exists with positive alliance and declare war weights.
3. `test_tag_safe_russian_civil_war`: Verifies zero `start_civil_war` commands exist in Russian events; asserts `SOV` and `WHT` tag transitions with respective trees (80 focuses for SOV, 60 focuses for WHT).
4. `test_russian_crisis_variable_reconciliation`: Verifies zero references to legacy `SOV_unrest` and `SOV_hunger` in decision files; all use `SOV_worker_unrest` and `SOV_urban_hunger`.
5. `test_okhrana_crackdown_balance_and_tooltips`: Verifies `SOV_dec_crush_bolsheviks_okhrana` has explicit localized tooltips and non-trivial requirements.

## Requirements
- Suite class: `TestAIAndRussiaFixes(unittest.TestCase)`
- Must fail on unedited codebase (RED phase) for tests 1-5.
- Register suite in `scripts/qa_audit_all.py`.
- Commit with message: `test(ai,rus): establish RED QA test suite for AI tactical overhaul, tag-safe civil war, and crisis fixes`
