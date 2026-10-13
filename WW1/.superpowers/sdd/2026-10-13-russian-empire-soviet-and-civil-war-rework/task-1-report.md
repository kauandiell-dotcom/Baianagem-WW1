# Task 1 Report: QA Test Suite Baseline Expansion (RED Phase)

**Date:** 2026-10-13  
**Status:** Completed (RED Baseline Established)  
**Commit:** `d403c6ecbcfb9eb8e1c8d906eab4d56ff20c25e9` (`test(sov): create master QA test suite baseline for Russia overhaul (RED)`)  
**File Created:** `tests/test_ww1_russia_rework.py`

---

## 1. Objectives & Scope

Task 1 establishes the Test-Driven Development (TDD) RED phase baseline for the full Russian Empire, Revolution, Soviet & White Civil War Overhaul.
The test suite implements the `TestRussiaOverhaul` test case with exact interface contracts to guide and validate Tasks 2 through 10.

---

## 2. Test Suite Architecture

The test file `tests/test_ww1_russia_rework.py` contains 9 comprehensive automated tests:

1. **`test_characters_and_tags`**
   - Asserts definition of `WHT` tag in `common/country_tags/`.
   - Asserts existence of `common/countries/White Russia.txt`.
   - Asserts `history/countries/WHT - White Russia.txt` sets capital to state 594 (Omsk) with neutrality ideology.
   - Asserts `common/countries/colors.txt` defines RGB color for `WHT`.
   - Asserts Bolshevik character recruitment in `common/characters/SOV.txt` (Trotsky, Stalin, Frunze, Dzerzhinsky, Budyonny, Tukhachevsky, Chicherin, Bukharin).
   - Asserts White leader character recruitment in `common/characters/WHT.txt` (Kolchak, Denikin, Wrangel, Yudenich, Kornilov, Kaledin, Savinkov).
   - Asserts GFX sprite definition files `interface/ww1_soviet_goals.gfx` and `interface/ww1_white_goals.gfx`.

2. **`test_tsarist_mechanics_and_ideas`**
   - Asserts Tsarist ideas in `common/ideas/ww1_russia_ideas.txt`: `SOV_strategic_depth_and_rasputitsa`, `SOV_shell_shortage_crisis`, `SOV_vpk_mobilization_spirit`, `SOV_rasputin_court_intrigues`, `SOV_order_restored_spirit`.
   - Asserts decision files `ww1_russia_tsarist_decisions.txt` and categories `ww1_russia_tsarist_categories.txt`.
   - Asserts categories `SOV_duma_and_court_politics`, `SOV_war_industry_mobilization`.
   - Asserts evacuation decision `SOV_evacuate_industrial_machinery` and Brusilov offensive `SOV_prepare_southwestern_offensive`.

3. **`test_crisis_engine_and_gauges`**
   - Asserts scripted effects in `common/scripted_effects/ww1_russia_crisis_effects.txt`: `sov_russia_init_crisis_gauges`, `sov_russia_clamp_crisis_gauges`, `sov_russia_weekly_crisis_update`.
   - Asserts crisis gauge variables: `SOV_revolutionary_tension`, `SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`.
   - Asserts crisis decisions `ww1_russia_crisis_decisions.txt` and category `SOV_revolutionary_crisis_category`.
   - Asserts crisis events in `events/ww1_russia_crisis_events.txt`: `ww1_russia.300`, `ww1_russia.301`, `ww1_russia.305`, `ww1_russia.310`.

4. **`test_civil_war_spawns_and_oobs`**
   - Asserts civil war event chain `events/ww1_russia_civil_war_events.txt` enforcing `prevent_join_factions = yes` and spawning breakaways (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`).
   - Asserts dedicated civil war OOBs in `history/units/`: `SOV_red_army_civil_war.txt`, `WHT_white_army_civil_war.txt`, `UKR_civil_war.txt`, `FIN_civil_war.txt`, `POL_civil_war.txt`.
   - Asserts War Communism and Kazan gold decisions in `common/decisions/ww1_soviet_civil_war_decisions.txt`.

5. **`test_brest_litovsk_and_diplomacy`**
   - Asserts diplomacy events in `events/ww1_russia_diplomacy_events.txt` (Treaty of Brest-Litovsk, separate peace, Faustschlag).
   - Asserts diplomacy decisions in `common/decisions/ww1_soviet_diplomacy_decisions.txt` (`SOV_decree_on_peace`, Entente proxy aid).
   - Asserts on-actions in `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt` for 1918 German armistice voiding Brest-Litovsk.

6. **`test_soviet_focus_tree_integrity`**
   - Asserts tree file `common/national_focus/soviet_russia.txt` exists with ID `soviet_russia_focus`.
   - Asserts exactly 80 focuses.
   - Asserts zero duplicate focus IDs.
   - Asserts zero coordinate collisions: unique $(x, y)$ coordinates.
   - Asserts horizontal banner spacing: $|x_2 - x_1| \ge 2$ on same row $y$.
   - Asserts parent-child prerequisite vertical links: child strictly below parent, $1 \le child\_y - parent\_y \le 3$.
   - Asserts zero hollow focuses: every focus grants substantive `completion_reward`.

7. **`test_white_focus_tree_integrity`**
   - Asserts tree file `common/national_focus/white_russia.txt` exists with ID `white_russia_focus`.
   - Asserts exactly 60 focuses.
   - Asserts zero duplicate focus IDs, zero coordinate collisions.
   - Asserts $|x_2 - x_1| \ge 2$ on same row, $1 \le child\_y - parent\_y \le 3$.
   - Asserts zero hollow focuses with substantive `completion_reward`.
   - Asserts reunification capstone executing `change_tag_to = SOV`.

8. **`test_imperial_focus_tree_integrity`**
   - Asserts tree file `common/national_focus/soviet.txt` exists with ID `russian_empire_focus`.
   - Asserts legacy dead-end Bolshevik focus `SOV_war_communism_decrees` is purged.
   - Asserts Imperial Salvation capstones `SOV_annexation_of_tsargrad` and `SOV_triumph_of_the_romanov_dynasty`.
   - Asserts spatial grid integrity ($|x_2 - x_1| \ge 2$, $1 \le child\_y - parent\_y \le 3$).

9. **`test_localisation_integrity_and_bom`**
   - Scans all Russian localization files (`sov`, `russia`, `white`) in `localisation/**/*.yml`.
   - Asserts strictly single UTF-8 BOM (`\xef\xbb\xbf` at `[:3]`, and `!= \xef\xbb\xbf` at `[3:6]`).
   - Asserts presence of required new localization files (`ww1_soviet_l_english.yml`, `ww1_soviet_l_braz_por.yml`, `ww1_white_l_english.yml`, `ww1_white_l_braz_por.yml`, etc.).
   - Asserts 100% key parity between English and Brazilian Portuguese.

---

## 3. Verification & Execution Results (RED Phase)

Command executed:
```bash
python -m unittest tests/test_ww1_russia_rework.py -v
```

Output summary:
```
Ran 9 tests in 0.049s
FAILED (failures=9)
```

Detailed failure reasons (all expected on unedited files):
| Test Method | Failure Reason | Associated Implementation Task |
|---|---|---|
| `test_characters_and_tags` | Tag WHT not defined in `common/country_tags/` | Task 2 |
| `test_tsarist_mechanics_and_ideas` | `SOV_strategic_depth_and_rasputitsa` not found in `ww1_russia_ideas.txt` | Task 3 |
| `test_crisis_engine_and_gauges` | `common/scripted_effects/ww1_russia_crisis_effects.txt` does not exist | Task 4 |
| `test_civil_war_spawns_and_oobs` | `events/ww1_russia_civil_war_events.txt` does not exist | Task 5 |
| `test_brest_litovsk_and_diplomacy` | `events/ww1_russia_diplomacy_events.txt` does not exist | Task 6 |
| `test_soviet_focus_tree_integrity` | `common/national_focus/soviet_russia.txt` does not exist | Task 7 |
| `test_white_focus_tree_integrity` | `common/national_focus/white_russia.txt` does not exist | Task 8 |
| `test_imperial_focus_tree_integrity` | Legacy dead-end `SOV_war_communism_decrees` still present in `soviet.txt` | Task 9 |
| `test_localisation_integrity_and_bom` | `localisation/english/ww1_soviet_l_english.yml` does not exist | Task 10 |

---

## 4. Next Steps

With Task 1 complete and the RED baseline committed, the implementation can proceed to **Task 2**: `Country Tag WHT, Historical Characters, Cosmetic Tags & GFX Sprites`.
