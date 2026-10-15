# Task 1 Report: QA RED Test Baseline (tests/test_ww1_france_rework.py)

**Date:** 2026-10-15  
**Tag:** `FRA` / `GER` / `ENG`  
**Status:** COMPLETED (RED Phase Confirmed)  
**Commit:** `ecf7e3e100166a8344e5e6f3ef470ab5976de992`

---

## 1. Overview & Objectives

Established the comprehensive automated unit test suite `tests/test_ww1_france_rework.py` for the French Republic complete overhaul and 1911 Agadir Crisis escalation engine, and registered it as Suite 13 in `scripts/qa_audit_all.py`.

All 6 test methods strictly enforce TDD by asserting the mechanical, structural, and semantic requirements across the overhaul pillars before implementation begins.

---

## 2. Test Suite Architecture (`tests/test_ww1_france_rework.py`)

The test class `TestFranceOverhaul(unittest.TestCase)` implements the following 6 test methods:

| Test Method | Target System / Files | Assertions |
|-------------|----------------------|------------|
| `test_agadir_crisis_mechanics` | `events/WW1_Agadir.txt`<br>`common/decisions/ww1_agadir_crisis_decisions.txt` | Namespace `ww1_agadir`, tension variable `ww1_agadir_crisis_tension`, Neukamerun cession states (`1086`, `1087`, `1088`), interactive decisions for `GER`, `FRA`, `ENG`. |
| `test_republic_dashboard_variables` | `common/scripted_effects/ww1_france_dashboard_effects.txt` | Existence of `FRA_init_republic_dashboard`, `FRA_clamp_dashboard_variables`, and management/clamping (0–100) of the 4 survival vectors (`FRA_union_sacree_cohesion`, `FRA_poilu_morale`, `FRA_charbon_et_acier`, `FRA_reserves_humaines`). |
| `test_four_political_destinies` | `common/national_focus/france.txt` | The 4 divergent paths: Third Republic (`FRA_republique_union_sacree`, `FRA_clemenceau_je_fais_la_guerre`), Second Paris Commune (`FRA_republique_des_soviets_de_paris`), Action Française (`FRA_abattre_la_gueuse`, `FRA_restauration_orleaniste_jean_iii`), GQG Military Directory (`FRA_directoire_militaire_gqg`), mutual exclusivity among branches, and awarding distinct national ideas (`FRA_union_sacree_spirit`, `FRA_commune_de_paris_spirit`, `FRA_action_francaise_monarchy`, `FRA_gqg_military_directory`). |
| `test_mutinies_and_civil_crises` | `events/ww1_france_events.txt`<br>`common/decisions/ww1_france_decisions.txt` | Event `ww1_france.210` applies mutiny idea `FRA_trench_mutiny_crisis_2`, which unlocks Pétain leave reform decision `FRA_petain_welfare_and_leave_reform`, and event referencing French Endsieg spirit `FRA_jusqu_au_bout_endsieg`. |
| `test_semantic_oracle_modifiers` | `common/ideas/ww1_france_crises_ideas.txt`<br>`common/ideas/ww1_france_political_ideas.txt`<br>`common/ideas/ww1_france_dashboard_ideas.txt` | Verification via `scripts/hoi4_semantic_oracle.py` that all ideas exist, are populated, and contain 0 invalid/hallucinated Clausewitz modifier tokens. |
| `test_localisation_bom_and_parity` | `localisation/english/ww1_france_rework_l_english.yml`<br>`localisation/braz_por/ww1_france_rework_l_braz_por.yml` | Single mandatory UTF-8 BOM (`\xef\xbb\xbf`), 0 double BOM, and 100% key parity between English and Brazilian Portuguese dictionaries. |

---

## 3. Suite Registration (`scripts/qa_audit_all.py`)

- Updated `SUITES` in `scripts/qa_audit_all.py` to register Suite 13:
  ```python
  ("French Republic Complete Overhaul & Agadir Crisis Test Suite", "tests.test_ww1_france_rework"),
  ```
- Hooked test execution and failure tracking into `main()` of `scripts/qa_audit_all.py` as Suite 13.

---

## 4. Test Execution (RED Phase Verification)

Execution command:
```bash
python -m unittest tests.test_ww1_france_rework -v
```

Output:
```text
test_agadir_crisis_mechanics (tests.test_ww1_france_rework.TestFranceOverhaul.test_agadir_crisis_mechanics) ... FAIL
test_four_political_destinies (tests.test_ww1_france_rework.TestFranceOverhaul.test_four_political_destinies) ... FAIL
test_localisation_bom_and_parity (tests.test_ww1_france_rework.TestFranceOverhaul.test_localisation_bom_and_parity) ... FAIL
test_mutinies_and_civil_crises (tests.test_ww1_france_rework.TestFranceOverhaul.test_mutinies_and_civil_crises) ... FAIL
test_republic_dashboard_variables (tests.test_ww1_france_rework.TestFranceOverhaul.test_republic_dashboard_variables) ... FAIL
test_semantic_oracle_modifiers (tests.test_ww1_france_rework.TestFranceOverhaul.test_semantic_oracle_modifiers) ... FAIL

Ran 6 tests in 0.019s

FAILED (failures=6)
```

**Diagnostic Analysis:**
1. `test_agadir_crisis_mechanics`: Failed as expected (`ww1_agadir_crisis_tension` variable and Neukamerun transfer not yet implemented in `events/WW1_Agadir.txt`; decisions file missing).
2. `test_republic_dashboard_variables`: Failed as expected (`common/scripted_effects/ww1_france_dashboard_effects.txt` missing).
3. `test_four_political_destinies`: Failed as expected (focuses `FRA_republique_union_sacree`, `FRA_republique_des_soviets_de_paris`, `FRA_abattre_la_gueuse`, `FRA_directoire_militaire_gqg` missing).
4. `test_mutinies_and_civil_crises`: Failed as expected (`ww1_france.210` does not yet apply `FRA_trench_mutiny_crisis_2`, leaving Pétain decision locked).
5. `test_semantic_oracle_modifiers`: Failed as expected (idea files missing).
6. `test_localisation_bom_and_parity`: Failed as expected (localization rework files missing).

---

## 5. Deliverables & Git Audit

- Created: `tests/test_ww1_france_rework.py` (426 lines)
- Modified: `scripts/qa_audit_all.py` (+8 lines)
- Commit: `ecf7e3e100166a8344e5e6f3ef470ab5976de992`
  `test(fra): establish comprehensive RED QA test suite for France overhaul & Agadir Crisis`
