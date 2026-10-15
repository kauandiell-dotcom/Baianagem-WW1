# Task 1 Brief: QA RED Test Baseline (tests/test_ww1_france_rework.py)

## Objective
Establish the automated unit testing suite `tests/test_ww1_france_rework.py` that validates all features of the France overhaul and Agadir Crisis, and register it as Suite 13 in `scripts/qa_audit_all.py`.

## Requirements
1. Create `tests/test_ww1_france_rework.py` containing test class `TestFranceOverhaul(unittest.TestCase)` with tests:
   - `test_agadir_crisis_mechanics`: Checks that `events/WW1_Agadir.txt` contains namespace `ww1_agadir`, crisis events, tension variable references (`ww1_agadir_crisis_tension`), decisions in `common/decisions/ww1_agadir_crisis_decisions.txt`, and proper state references for Neukamerun (1086, 1087, 1088).
   - `test_republic_dashboard_variables`: Checks scripted effects in `common/scripted_effects/ww1_france_dashboard_effects.txt` for `FRA_init_republic_dashboard`, `FRA_clamp_dashboard_variables`, and all 4 survival vectors (`FRA_union_sacree_cohesion`, `FRA_poilu_morale`, `FRA_charbon_et_acier`, `FRA_reserves_humaines`).
   - `test_four_political_destinies`: Checks focuses in `common/national_focus/france.txt` for:
     - Third Republic / Union Sacrée (`FRA_republique_union_sacree`, `FRA_clemenceau_je_fais_la_guerre`)
     - Second Paris Commune (`FRA_republique_des_soviets_de_paris`)
     - Action Française / Orléans Monarchy (`FRA_abattre_la_gueuse`, `FRA_restauration_orleaniste_jean_iii`)
     - GQG Military Directory (`FRA_directoire_militaire_gqg`)
     - Verifies mutual exclusivity and distinct ideas.
   - `test_mutinies_and_civil_crises`: Checks that `events/ww1_france_events.txt` has mutiny chain (`ww1_france.210` applying `FRA_trench_mutiny_crisis_2`), Pétain leave reform unlock, and French Endsieg (`FRA_jusqu_au_bout_endsieg`).
   - `test_semantic_oracle_modifiers`: Verifies that all French ideas in `common/ideas/ww1_france_crises_ideas.txt`, `ww1_france_political_ideas.txt`, and `ww1_france_dashboard_ideas.txt` use 100% valid Clausewitz modifiers via `scripts/hoi4_semantic_oracle.py`.
   - `test_localisation_bom_and_parity`: Checks single UTF-8 BOM (`\xef\xbb\xbf`) on `localisation/english/ww1_france_rework_l_english.yml` and `localisation/braz_por/ww1_france_rework_l_braz_por.yml`, 0 double BOM, and 100% key parity.
2. Register `tests.test_ww1_france_rework` in `scripts/qa_audit_all.py` as Suite 13.
3. Run `python -m unittest tests.test_ww1_france_rework -v` to confirm failure (RED phase).
4. Commit:
   `git add tests/test_ww1_france_rework.py scripts/qa_audit_all.py`
   `git commit -m "test(fra): establish comprehensive RED QA test suite for France overhaul & Agadir Crisis"`
