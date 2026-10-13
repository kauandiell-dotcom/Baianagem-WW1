# Italy Rework Task 1 Report: Master QA Test Suite Expansion (`tests/test_ww1_italy.py` — RED Phase)

## Status
- **Status:** COMPLETED (RED Phase Verified)
- **Commit:** `690b7d8` (`test(ita): expand Italy QA test suite for complete rework (RED)`)
- **Modified File:** `tests/test_ww1_italy.py`

## Implemented Assertions
1. **`TestItalyTreeAndGraph.test_non_overlapping_coordinates_and_descending_y`**:
   - Added row-by-row horizontal spacing assertion (`abs(x2 - x1) >= 2`) for adjacent focuses on the same `y` row.
   - Added prerequisite vertical span assertion (`1 <= dy <= 3`).
   - Added assertion that `common/national_focus/italy.txt.disabled` does not exist.
2. **`TestItalyBalanceAndMechanics.test_zero_shallow_focuses`**:
   - Added assertion that every focus has at least one tangible effect beyond flat `add_political_power`, `add_stability`, `add_war_support`, `army_experience`, `navy_experience`, `air_experience`, `add_command_power`, `add_to_variable`, `set_country_flag`, `custom_effect_tooltip`, and `ita_ww1_clamp_counters`.
3. **`TestItalyBalanceAndMechanics.test_active_five_gauges_and_zero_unused_ideas`**:
   - Extracted `ita_ww1_update_gauges` from `common/scripted_effects/ww1_italy_effects.txt`.
   - Asserted `check_variable` checks for all 5 gauges (`ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, `ita_ww1_irredentism`) and application of all 15 dynamic gauge ideas (`ITA_ww1_neutralist_predominance`, `ITA_ww1_social_truce`, `ITA_ww1_stoic_endurance`, `ITA_ww1_southern_disparity`, `ITA_ww1_unredeemed_lands_call`, etc.).
4. **`TestItalyIdeasAndModifiers.test_ideas_volume_and_valid_modifiers`**:
   - Added semantic oracle modifier validation (`audit_file_modifiers`) on `common/ideas/ww1_italy_ideas.txt` and `common/decisions/ww1_italy_decisions.txt`.
   - Asserted presence of all 9 restored ideas (`ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, `ITA_southern_question_gap`, `ITA_sacro_egoismo_policy`, `ITA_isonzo_attrition_crisis_1`, `ITA_isonzo_attrition_crisis_2`, `ITA_isonzo_attrition_crisis_3`, `ITA_vittorio_veneto_triumph`).
   - Asserted 0 unused ideas across `history/countries/ITA - Italy.txt`, `common/national_focus/italy.txt`, `common/decisions/ww1_italy_decisions.txt`, `common/scripted_effects/ww1_italy_effects.txt`, and `events/ww1_italy_*.txt`.
5. **`TestItalyEventsAndDecisions.test_map_state_targeted_decisions_and_zero_orphan_events`**:
   - Asserted presence of all 9 new decisions (`ITA_ww1_mezzogiorno_aqueduct_and_roads`, `ITA_ww1_carabinieri_anti_brigandage_sweep`, `ITA_ww1_southern_agrarian_credit_consortium`, `ITA_ww1_alpine_mine_warfare_tunnel`, `ITA_ww1_launch_isonzo_general_offensive`, `ITA_ww1_fortify_piave_and_monte_grappa`, `ITA_ww1_fortify_libyan_coastal_oases`, `ITA_ww1_integrate_irredenta_province`, `ITA_ww1_impresa_di_pola_raid`).
   - Asserted at least 6 `state_target = yes` blocks in `common/decisions/ww1_italy_decisions.txt`.
   - Asserted `ww1_italy.50` and `ww1_italy.63` are triggered across focuses, decisions, or event options/immediates.
6. **`TestItalyLocalisationAndGraphics`**:
   - Enforced strict single UTF-8 BOM (`raw[:3] == b"\xef\xbb\xbf"` and `raw[3:6] != b"\xef\xbb\xbf"`) on both `ww1_italy_l_english.yml` and `ww1_italy_l_braz_por.yml`.
   - Asserted title and `_desc` localisation parity for all ideas in `common/ideas/ww1_italy_ideas.txt` and all decisions in `common/decisions/ww1_italy_decisions.txt`.
   - Asserted all `texturefile` paths referenced in `interface/ww1_italy_goals.gfx`, `interface/ww1_italy_ideas.gfx`, `interface/ww1_italy_decisions.gfx`, and `interface/ww1_italy_events.gfx` (except `gfx/interface/goals/shine_overlay.dds`) exist on disk in the mod directory.

## RED Verification Summary
Command: `python -m unittest tests/test_ww1_italy.py -v`
Result: `Ran 16 tests in 0.486s — FAILED (failures=7)`

Expected RED Failures Observed:
1. `test_non_overlapping_coordinates_and_descending_y`: `Horizontal banner collision on row y=12: ITA_ww1_proportional_representation (x=7) and ITA_ww1_popular_party (x=8) have dx=1 < 2`
2. `test_zero_shallow_focuses`: `Found 41 shallow focuses with only flat PP/stab/ws/XP/gauge rewards`
3. `test_active_five_gauges_and_zero_unused_ideas`: `'check_variable' not found in ita_ww1_update_gauges`
4. `test_balance_ceilings_on_focus_tree`: `Focus ITA_ww1_treaty_of_london exceeds single ws cap (+0.05): 0.1`
5. `test_ideas_volume_and_valid_modifiers`: `Idea ITA_carbone_bianco_hydro has invalid modifier production_speed_infrastructure_factor`
6. `test_map_state_targeted_decisions_and_zero_orphan_events`: `Missing required new decisions: ['ITA_ww1_mezzogiorno_aqueduct_and_roads', ...]`
7. `test_gfx_sprite_definitions_and_shine`: `Missing texture files on disk in mod directory: [('ww1_italy_decisions.gfx', 'gfx/interface/decisions/decision_category_generic.dds'), ...]`
