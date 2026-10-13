# Italy Rework Task 3 Report: Map-Based State Decisions & Strategic Operations

## Summary of Changes
- **Modified `common/decisions/ww1_italy_decisions.txt`**:
  - Under `ITA_ww1_economic_mobilisation_category`:
    - `ITA_ww1_mezzogiorno_aqueduct_and_roads` (`state_target = yes`, targets states `117`, `849`, `156`, `115`, `114`, `157`, builds 1 infrastructure, reduces `ita_ww1_southern_gap` by 8, updates gauges).
    - `ITA_ww1_carabinieri_anti_brigandage_sweep` (`state_target = yes`, targets states `117`, `849`, `156`, `115`, `114`, `157`, consumes 250 `infantry_equipment`, sets `ITA_mezzogiorno_state_pacified`, grants +0.02 stability, reduces `ita_ww1_southern_gap` by 6 and `ita_ww1_social_tension` by 4, updates gauges).
    - `ITA_ww1_southern_agrarian_credit_consortium` (`fire_only_once = yes`, requires `ita_ww1_southern_gap < 40` and pacified states `117` & `115`, replaces `ITA_southern_question_gap` and `ITA_mezzogiorno_development_stage` with `ITA_mezzogiorno_integrated`, adds 1 civilian factory + slot in states `117` and `115`, reduces `ita_ww1_southern_gap` by 15, updates gauges).
  - Under `ITA_ww1_military_readiness_category`:
    - `ITA_ww1_alpine_mine_warfare_tunnel` (`state_target = yes`, targets states `160`, `159`, `850`, `39`, `736`, `852`, adds level 1 border bunkers, +15 army XP, +5 `ita_ww1_army_morale`, updates gauges).
    - `ITA_ww1_launch_isonzo_general_offensive` (repeatable every 60 days after 45-day duration; escalates `ITA_isonzo_attrition_crisis_1` -> `2` -> `3` under Cadorna or clears them and boosts morale/war support under Armando Diaz when `ita_ww1_diaz_appointed` is set).
    - `ITA_ww1_fortify_piave_and_monte_grappa` (`state_target = yes`, targets states `160` and `159`, builds level 2 border bunkers, +0.03 stability, +10 `ita_ww1_army_morale`, updates gauges).
    - `ITA_ww1_impresa_di_pola_raid` (`fire_only_once = yes`, requires war with `AUS` and `ITA_ww1_mas_boats`, grants +25 navy XP, +0.04 war support, `ITA_ww1_mignatta_special_raiders`, +10 `ita_ww1_army_morale`, updates gauges).
  - Under `ITA_ww1_diplomatic_initiatives_category`:
    - `ITA_ww1_fortify_libyan_coastal_oases` (`state_target = yes`, targets Libyan states `448`, `450`, `451`, `661`, `663`, adds 1 infrastructure, +10 compliance, +10 army XP, +5 `ita_ww1_irredentism`, updates gauges).
    - `ITA_ww1_integrate_irredenta_province` (`state_target = yes`, targets Irredenta states `850`, `39`, `736`, `852`, `163`, `164`, cores state for `ITA`, adds 1 infrastructure, +0.02 stability, -10 `ita_ww1_irredentism`, updates gauges).
- **Modified `common/decisions/categories/ww1_italy_categories.txt`**:
  - Added explicit `visible = { original_tag = ITA }` triggers across all 4 Italy decision categories.

## Verification
- **Semantic Oracle**: `audit_file_modifiers('common/decisions/ww1_italy_decisions.txt')` returned `0` errors.
- **Unit Test**: `python -m unittest tests.test_ww1_italy.TestItalyEventsAndDecisions.test_decisions_count_categories_and_costs` passed (`OK`, 34 total decisions across 4 categories, 6 `state_target = yes` decisions).

## Commit
- Commit hash: `5af32f2c84ad858fdc63d42bc0c3b80c533a86d6` (`5af32f2`)
