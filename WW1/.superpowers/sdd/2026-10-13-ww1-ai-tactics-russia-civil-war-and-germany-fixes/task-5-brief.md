# Task 5 Brief: Russian Crisis Variable Reconciliation & Okhrana Crackdown Rebalance

## Objective
Reconcile all legacy/mismatched Russian crisis variables (`SOV_unrest` -> `SOV_worker_unrest`, `SOV_hunger` -> `SOV_urban_hunger`) across decisions, events, and scripted effects so that decisions interact with the crisis UI dashboard. Rebalance the Okhrana crackdown decision (`SOV_dec_crush_bolsheviks_okhrana`) from a trivial, opaque 1-click button into a transparent 90-day operation with localized prerequisite tooltips.

## Files to Modify
- `common/decisions/ww1_ger_rus_rework_decisions.txt`
- `common/scripted_effects/ww1_ger_rus_rework_effects.txt`
- `events/ww1_ger_rus_rework_events.txt` (any remaining occurrences of `SOV_unrest` / `SOV_hunger`)
- `localisation/english/ww1_ger_rus_rework_l_english.yml`
- `localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml`

## Technical Specifications & Requirements

### 1. Variable Synchronization
- In `common/decisions/ww1_ger_rus_rework_decisions.txt`:
  - Replace ALL occurrences of `SOV_unrest` with `SOV_worker_unrest`.
  - Replace ALL occurrences of `SOV_hunger` with `SOV_urban_hunger`.
  - Verify regex `\bSOV_unrest\b` and `\bSOV_hunger\b` return 0 matches in the decisions file.
- In `common/scripted_effects/ww1_ger_rus_rework_effects.txt`:
  - Replace any legacy `SOV_unrest` and `SOV_hunger` with `SOV_worker_unrest` and `SOV_urban_hunger`.
- In `events/ww1_ger_rus_rework_events.txt`:
  - Replace any legacy `SOV_unrest` and `SOV_hunger` with `SOV_worker_unrest` and `SOV_urban_hunger`.

### 2. Okhrana Crackdown Rebalance (`SOV_dec_crush_bolsheviks_okhrana`)
- In `common/decisions/ww1_ger_rus_rework_decisions.txt`:
  - Decision `SOV_dec_crush_bolsheviks_okhrana`:
    - `cost = 100` (balanced political capital requirement).
    - `days_remove = 90` (requires a 90-day operation rather than an instant resolution).
    - Add `modifier = { political_power_factor = -0.10 }` while active.
    - Prerequisite conditions wrapped in `custom_trigger_tooltip`:
      ```clausewitz
      available = {
          custom_trigger_tooltip = {
              tooltip = SOV_dec_crush_bolsheviks_okhrana_req_tt
              check_variable = { SOV_revolutionary_tension < 20 }
              has_stability > 0.50
              195 = { is_demilitarized_zone = no }
              219 = { is_demilitarized_zone = no }
          }
      }
      ```
    - Execute completion/removal effect on `remove_effect`:
      ```clausewitz
      remove_effect = {
          SOV_clear_revolutionary_crisis = yes
          country_event = { id = ww1_russia.254 days = 1 }
      }
      ```

### 3. Bilingual Localization & Single UTF-8 BOM
- Add key `SOV_dec_crush_bolsheviks_okhrana_req_tt` in both:
  - `localisation/english/ww1_ger_rus_rework_l_english.yml`:
    `SOV_dec_crush_bolsheviks_okhrana_req_tt:0 "§YRequirements for Okhrana General Purge:§!\n • Revolutionary Tension is below §G20%§!\n • National Stability is greater than §G50%§!\n • Both Petrograd and Moscow are under loyal Imperial military control"`
  - `localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml`:
    `SOV_dec_crush_bolsheviks_okhrana_req_tt:0 "§YRequisitos para a Purga Geral da Okhrana:§!\n • Tensão Revolucionária abaixo de §G20%§!\n • Estabilidade Nacional superior a §G50%§!\n • Petrogrado e Moscou sob controle militar Imperial leal"`
- Strictly single UTF-8 BOM (`\xef\xbb\xbf`) on both files. Zero double-BOM (`\xef\xbb\xbf\xef\xbb\xbf`).

### 4. Unit Test Verification
- Run:
  `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_russian_crisis_variable_reconciliation -v`
  Must PASS!
- Run:
  `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_okhrana_crackdown_balance_and_tooltips -v`
  Must PASS!

## Deliverables
- Commit: `git add common/decisions/ common/scripted_effects/ events/ localisation/`
- Commit Message: `fix(rus): reconcile Russian crisis variables and rebalance Okhrana crackdown with transparent tooltips`
- Report: `.superpowers/sdd/2026-10-13-ww1-ai-tactics-russia-civil-war-and-germany-fixes/task-5-report.md`
