# Task 1 Report: QA RED Test Baseline

## Overview
- **Task**: Establish RED QA test suite for WW1 AI Tactical Overhaul, Tag-Safe Russian Civil War, and Crisis Balance Fixes.
- **Suite File**: `tests/test_ww1_ai_and_russia_fixes.py`
- **Runner Registration**: `scripts/qa_audit_all.py` (Suite #10)
- **Status**: Completed (RED phase confirmed with 5/5 targeted failures)
- **Git Commit**: `4a2689e842719fbc8b045c74a69e1b9f87547a37`

---

## Deliverables & Test Specifications

Class: `TestAIAndRussiaFixes(unittest.TestCase)`

### 1. `test_ai_tactical_defines`
- **File**: `common/defines/ww1_ai_defines.lua`
- **Checks**:
  - `MIN_PLANNING_BONUS_TO_ATTACK >= 0.65`
  - `PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL >= 0.60`
  - `ORG_UNIT_WEAK >= 0.40`
  - `STRENGTH_UNIT_WEAK >= 0.50`
  - `CORPS_COMMANDER_DIVISIONS_CAP == 24`
- **Initial Result**: `FAIL` (file not yet created).

### 2. `test_bulgaria_alliance_and_war_call`
- **Files**: `events/ww1_germany_events.txt` (`ww1_germany_events.33`), `common/ai_strategy/ww1_bulgaria_ai_strategy.txt`
- **Checks**:
  - `ww1_germany_events.33` Option A contains war declaration or call to arms against Serbia (`SER`).
  - `ww1_bulgaria_ai_strategy.txt` exists and configures strategies targeting `GER` and `SER`.
- **Initial Result**: `FAIL` (Bulgaria event option A currently lacks war call against `SER`).

### 3. `test_tag_safe_russian_civil_war`
- **File**: `events/ww1_ger_rus_rework_events.txt`
- **Checks**:
  - Asserts 0 occurrences of `start_civil_war` across the entire event file (mandates tag-safe `SOV`/`WHT` transitions).
  - Asserts `WHT` and `SOV` tags are referenced in `ww1_russia.255` and `ww1_russia.220`.
- **Initial Result**: `FAIL` (5 occurrences of legacy `start_civil_war` present in lines 699, 700, 2032, 2036, 2039).

### 4. `test_russian_crisis_variable_reconciliation`
- **File**: `common/decisions/ww1_ger_rus_rework_decisions.txt`
- **Checks**:
  - Asserts 0 occurrences of legacy exact variable names `SOV_unrest` and `SOV_hunger`.
  - Asserts presence of `SOV_worker_unrest` and `SOV_urban_hunger`.
- **Initial Result**: `FAIL` (12 legacy occurrences of `SOV_unrest` detected).

### 5. `test_okhrana_crackdown_balance_and_tooltips`
- **File**: `common/decisions/ww1_ger_rus_rework_decisions.txt`
- **Checks**:
  - `SOV_dec_crush_bolsheviks_okhrana` has explicit `custom_trigger_tooltip`.
  - References tension (`SOV_revolutionary_tension`) and stability triggers.
  - Implements non-instant duration (`days_remove >= 60` or multi-day mission timeout).
- **Initial Result**: `FAIL` (`custom_trigger_tooltip` missing, instant completion).

---

## RED Phase Verification Run

```
python -m unittest tests.test_ww1_ai_and_russia_fixes -v
```

Output:
```
test_ai_tactical_defines (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_ai_tactical_defines)
Verifies common/defines/ww1_ai_defines.lua configures tactical patience & corps limits. ... FAIL
test_bulgaria_alliance_and_war_call (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_bulgaria_alliance_and_war_call)
Verifies Bulgaria alliance event ww1_germany_events.33 calls war on SER and AI strategy exists. ... FAIL
test_okhrana_crackdown_balance_and_tooltips (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_okhrana_crackdown_balance_and_tooltips)
Verifies SOV_dec_crush_bolsheviks_okhrana has localized tooltips, non-instant duration, and tension/stability triggers. ... FAIL
test_russian_crisis_variable_reconciliation (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_russian_crisis_variable_reconciliation)
Verifies zero legacy SOV_unrest/SOV_hunger and confirms SOV_worker_unrest/SOV_urban_hunger in decisions. ... FAIL
test_tag_safe_russian_civil_war (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_tag_safe_russian_civil_war)
Verifies zero start_civil_war commands and asserts tag-safe SOV/WHT transition in ww1_russia.255 and 220. ... FAIL

======================================================================
Ran 5 tests in 0.046s

FAILED (failures=5)
```

---

## Git Commit

- **Commit**: `4a2689e842719fbc8b045c74a69e1b9f87547a37`
- **Message**: `test(ai,rus): establish RED QA test suite for AI tactical overhaul, tag-safe civil war, and crisis fixes`
- **Files Modified / Added**:
  - `tests/test_ww1_ai_and_russia_fixes.py` (added)
  - `scripts/qa_audit_all.py` (registered Suite #10 in `SUITES` and `main()`)
