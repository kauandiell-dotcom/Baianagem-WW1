# Task 5 Report: Russian Crisis Variable Reconciliation & Okhrana Crackdown Rebalance

**Execution Date:** 2026-10-14  
**Author Subagent:** Task 5 Implementer  
**Commit Hash:** `7a4cb786edaaeff3bf9dbba0950efe9d04cc6957`  
**Status:** COMPLETED (All Tests Passing)

---

## 1. Summary of Changes

Task 5 reconciled all mismatched and legacy Russian crisis variable references across decisions, scripted effects, and events to align with the core Russian Crisis GUI and mechanics engine (`SOV_worker_unrest` and `SOV_urban_hunger`). In addition, the Okhrana crackdown decision (`SOV_dec_crush_bolsheviks_okhrana`) was thoroughly overhauled from an instantaneous, low-cost shortcut into a balanced 90-day police-state operation with transparent localized prerequisite tooltips and increased stability/tension thresholds.

---

## 2. Variable Synchronization Details

All occurrences of legacy variables were systematically migrated:
- `SOV_unrest` $\rightarrow$ `SOV_worker_unrest`
- `SOV_hunger` $\rightarrow$ `SOV_urban_hunger`

### Files Audited and Updated:
1. `common/decisions/ww1_ger_rus_rework_decisions.txt`
   - 12 occurrences of `SOV_unrest` replaced with `SOV_worker_unrest`
   - 7 occurrences of `SOV_hunger` replaced with `SOV_urban_hunger`
   - Regex check `\bSOV_unrest\b` and `\bSOV_hunger\b`: **0 matches**
2. `common/scripted_effects/ww1_ger_rus_rework_effects.txt`
   - 14 occurrences of `SOV_unrest` replaced with `SOV_worker_unrest`
   - 8 occurrences of `SOV_hunger` replaced with `SOV_urban_hunger`
   - Regex check `\bSOV_unrest\b` and `\bSOV_hunger\b`: **0 matches**
3. `events/ww1_ger_rus_rework_events.txt`
   - 46 occurrences of `SOV_unrest` replaced with `SOV_worker_unrest`
   - 12 occurrences of `SOV_hunger` replaced with `SOV_urban_hunger`
   - Regex check `\bSOV_unrest\b` and `\bSOV_hunger\b`: **0 matches**

---

## 3. Okhrana Crackdown Rebalance (`SOV_dec_crush_bolsheviks_okhrana`)

Located in `common/decisions/ww1_ger_rus_rework_decisions.txt`:
- **Cost:** Increased from 60 to **100 Political Power**.
- **Execution Model:** Replaced instant resolution with `days_remove = 90` active operation.
- **Active Modifier:** Added `modifier = { political_power_factor = -0.10 }` reflecting state resources dedicated to widespread security sweeps.
- **Trigger Clarity & Balancing:**
  - Wrapped prerequisites in `custom_trigger_tooltip = { tooltip = SOV_dec_crush_bolsheviks_okhrana_req_tt ... }`.
  - Tension check: `SOV_revolutionary_tension < 20`.
  - Stability check: Increased required stability from > 40% to **> 50%**.
  - Territorial control: Petrograd (195) and Moscow (219) must NOT be demilitarized zones.
- **Resolution Timing:** Moved crisis clearing effects (`SOV_clear_revolutionary_crisis = yes` and `country_event = { id = ww1_russia.254 days = 1 }`) from `complete_effect` to `remove_effect` so they trigger upon successful completion of the 90-day operation.

---

## 4. Bilingual Localization & Single UTF-8 BOM Verification

Added key `SOV_dec_crush_bolsheviks_okhrana_req_tt` in both localization files:

- **English (`localisation/english/ww1_ger_rus_rework_l_english.yml`):**
  ```yaml
   SOV_dec_crush_bolsheviks_okhrana_req_tt:0 "§YRequirements for Okhrana General Purge:§!\n • Revolutionary Tension is below §G20%§!\n • National Stability is greater than §G50%§!\n • Both Petrograd and Moscow are under loyal Imperial military control"
  ```
- **Brazilian Portuguese (`localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml`):**
  ```yaml
   SOV_dec_crush_bolsheviks_okhrana_req_tt:0 "§YRequisitos para a Purga Geral da Okhrana:§!\n • Tensão Revolucionária abaixo de §G20%§!\n • Estabilidade Nacional superior a §G50%§!\n • Petrogrado e Moscou sob controle militar Imperial leal"
  ```
- **Encoding Integrity:**
  - Both files verified for strictly single UTF-8 BOM (`\xef\xbb\xbf`).
  - Zero double-BOM (`\xef\xbb\xbf\xef\xbb\xbf`) detected.

---

## 5. Test Suite Verification

### Targeted Unit Tests:
```
python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_russian_crisis_variable_reconciliation -v
test_russian_crisis_variable_reconciliation (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_russian_crisis_variable_reconciliation)
Verifies zero legacy SOV_unrest/SOV_hunger and confirms SOV_worker_unrest/SOV_urban_hunger in decisions. ... ok

python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_okhrana_crackdown_balance_and_tooltips -v
test_okhrana_crackdown_balance_and_tooltips (tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_okhrana_crackdown_balance_and_tooltips)
Verifies SOV_dec_crush_bolsheviks_okhrana has localized tooltips, non-instant duration, and tension/stability triggers. ... ok
```

### Overall Suite Regression Checks:
- `tests.test_ww1_ai_and_russia_fixes`: **5/5 tests passing**
- `tests.test_ww1_russia_rework`: **9/9 tests passing**

---

## 6. Git Commit

- **Staged Paths:**
  - `common/decisions/ww1_ger_rus_rework_decisions.txt`
  - `common/scripted_effects/ww1_ger_rus_rework_effects.txt`
  - `events/ww1_ger_rus_rework_events.txt`
  - `localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml`
  - `localisation/english/ww1_ger_rus_rework_l_english.yml`
- **Commit Message:**
  `fix(rus): reconcile Russian crisis variables and rebalance Okhrana crackdown with transparent tooltips`
- **Commit Hash:** `7a4cb786edaaeff3bf9dbba0950efe9d04cc6957`
