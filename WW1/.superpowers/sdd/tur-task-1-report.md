# Ottoman Rework Task 1 Report: Master QA Test Suite Expansion (RED Phase)

## Status
- **Status:** COMPLETE (RED baseline verified and committed)
- **Commit:** `da61a75` (`test(tur): expand Ottoman QA test suite for complete rework (RED)`)
- **Modified File:** `tests/test_ww1_ottoman.py`

## Implemented Assertions
1. **`test_focus_count_and_coordinate_collisions`**:
   - Asserts `len(self.foci) == 256` and unique `(x, y)` coordinates.
   - Groups focuses by `y` row and asserts `abs(f2["x"] - f1["x"]) >= 2` for every adjacent pair on the same `y` row.
2. **`test_prerequisite_integrity_and_downward_progression`**:
   - Asserts all parent IDs exist in `self.foci`.
   - Asserts `1 <= data["y"] - py <= 3` (no long vertical arrows cutting across 4+ rows).
3. **`test_zero_hollow_focuses`**:
   - Extracts each focus's `completion_reward` block and asserts that after stripping comments, `add_political_power`, `add_stability`, `add_war_support`, `add_to_variable`, and `set_country_flag`, the remaining reward body is non-empty.
4. **`test_all_referenced_ideas_exist_and_oracle_clean`**:
   - Asserts `common/ideas/ww1_ottoman_ideas.txt` defines `TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, and `TUR_senussi_desert_brotherhood`.
   - Asserts `audit_file_modifiers` from `scripts.hoi4_semantic_oracle` returns 0 errors on `common/ideas/ww1_ottoman_ideas.txt` and `common/decisions/ww1_ottoman_decisions.txt`.
5. **`test_arab_vilayet_state_securing_and_opda_decisions`**:
   - Asserts `common/decisions/ww1_ottoman_decisions.txt` defines `TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`, `TUR_pacify_arab_insurgency_campaign`, `TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`, and `TUR_dispatch_officers_to_tripolitania`.
   - Asserts `events/ww1_ottoman_events.txt` defines `ww1_ottoman.31` and `ww1_ottoman.32` and that all `ww1_ottoman.1`..`ww1_ottoman.32` events are triggered at least once across focuses, decisions, or events (0 orphan events).
   - Asserts `history/countries/TUR - Turkey.txt` recruits `TUR_ismail_enver_pasha`, `TUR_fakhri_pasha`, `TUR_halil_kut`, and `common/characters/TUR.txt` does not contain `ideology=nazism`.
6. **`test_bilingual_localization_parity_and_utf8_bom`**:
   - Asserts strictly single UTF-8 BOM (`b"\xef\xbb\xbf"` at `[:3]` and `!= b"\xef\xbb\xbf"` at `[3:6]`) on both English and PT-BR YAML files.
   - Asserts absence of generic copy-paste PT-BR placeholders and untranslated English titles (`"Subsidize Anatolian Grain"`, `"Second Constitutional Era"`).

## RED Verification Summary
Command: `python -m unittest tests/test_ww1_ottoman.py`
Result: `Ran 11 tests in 0.381s — FAILED (failures=6)`
- `test_focus_count_and_coordinate_collisions`: FAILED (27 horizontal banner collisions with `dx < 2`)
- `test_prerequisite_integrity_and_downward_progression`: FAILED (8 long vertical prerequisite arrows with `dy > 3`)
- `test_zero_hollow_focuses`: FAILED (59 hollow focuses with only flat PP/stability/war support/variables/flags)
- `test_all_referenced_ideas_exist_and_oracle_clean`: FAILED (7 missing ideas + Oracle errors)
- `test_arab_vilayet_state_securing_and_opda_decisions`: FAILED (7 missing decisions, missing events 31-32, orphan events, missing character recruitment)
- `test_bilingual_localization_parity_and_utf8_bom`: FAILED (double UTF-8 BOM `\xef\xbb\xbf\xef\xbb\xbf` detected)
