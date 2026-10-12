# Ottoman Rework Task 1 Brief: Master QA Test Suite Expansion (`tests/test_ww1_ottoman.py` — RED Phase)

## Objective
Expand `tests/test_ww1_ottoman.py` to catch every single structural, visual, mechanical, and localization defect identified in the Ottoman Empire audit, establishing the TDD RED baseline.

## Target File
- `tests/test_ww1_ottoman.py`
- Spec: `docs/superpowers/specs/2026-10-12-ottoman-empire-complete-rework-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-ottoman-empire-complete-rework-plan.md`

## Requirements
Update `tests/test_ww1_ottoman.py` so `OttomanContentReworkTests` includes the following assertions:
1. **In `test_focus_count_and_coordinate_collisions`:**
   - Assert `len(self.foci) == 256`.
   - Assert unique `(x, y)` coordinates.
   - Group focuses by `y` row and assert that for every adjacent pair on the same `y` row (`row_sorted[i]`, `row_sorted[i+1]`), `abs(f2["x"] - f1["x"]) >= 2` (0 horizontal banner collisions).
2. **In `test_prerequisite_integrity_and_downward_progression`:**
   - Assert all parent IDs exist in `self.foci`.
   - Assert `1 <= data["y"] - py <= 3` (no long vertical arrows cutting across 4+ rows).
3. **Add `test_zero_hollow_focuses`:**
   - For each focus in `self.foci`, extract its `completion_reward` block and assert that after stripping `add_political_power`, `add_stability`, `add_war_support`, `add_to_variable`, and `set_country_flag`, the remaining reward body is non-empty (every focus must grant tangible rewards such as buildings, ideas, events, equipment, XP, tech bonuses, etc.).
4. **Add `test_all_referenced_ideas_exist_and_oracle_clean`:**
   - Assert that `common/ideas/ww1_ottoman_ideas.txt` defines:
     `TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood`.
   - Assert that `audit_file_modifiers` from `scripts.hoi4_semantic_oracle` returns 0 errors on `common/ideas/ww1_ottoman_ideas.txt` and `common/decisions/ww1_ottoman_decisions.txt`.
5. **Add `test_arab_vilayet_state_securing_and_opda_decisions`:**
   - Assert `common/decisions/ww1_ottoman_decisions.txt` defines:
     `TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`, `TUR_pacify_arab_insurgency_campaign`, `TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`, `TUR_dispatch_officers_to_tripolitania`.
   - Assert `events/ww1_ottoman_events.txt` defines `ww1_ottoman.31` and `ww1_ottoman.32`, and that all events `ww1_ottoman.1` through `ww1_ottoman.32` with `is_triggered_only = yes` are triggered somewhere in `turkey.txt`, `ww1_ottoman_decisions.txt`, or `ww1_ottoman_events.txt` (0 orphan events).
   - Assert `history/countries/TUR - Turkey.txt` recruits `TUR_ismail_enver_pasha`, `TUR_fakhri_pasha`, `TUR_halil_kut`, and `common/characters/TUR.txt` does NOT contain `ideology=nazism`.
6. **In `test_bilingual_localization_parity_and_utf8_bom`:**
   - Assert `en_bytes[:3] == b"\xef\xbb\xbf"` and `en_bytes[3:6] != b"\xef\xbb\xbf"` (strictly single UTF-8 BOM, no double BOM!).
   - Assert `pt_bytes[:3] == b"\xef\xbb\xbf"` and `pt_bytes[3:6] != b"\xef\xbb\xbf"` (strictly single UTF-8 BOM, no double BOM!).
   - Assert `pt_text` does NOT contain the generic copy-paste placeholders `"Reflete as realidades estruturais e esforços administrativos do Estado Otomano."` or `"Aplica medidas operacionais especializadas para a defesa e prosperidade do império."` or `"Iniciativa estratégica entra em vigor nos territórios imperiais pertinentes."`.
   - Assert `pt_text` does NOT contain untranslated English titles `"Subsidize Anatolian Grain"` or `"Second Constitutional Era"`.

## Verification & Commit
1. Run `python -m unittest tests/test_ww1_ottoman.py` and confirm it FAILS for all the expected RED reasons.
2. Commit:
   `git add tests/test_ww1_ottoman.py`
   `git commit -m "test(tur): expand Ottoman QA test suite for complete rework (RED)"`
3. Write report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\tur-task-1-report.md`.
