# Italy Rework Task 4 Report: Focus Tree Spatial Fix, 41 Shallow Focus Upgrades & Orphan Event Connections

## Status
**COMPLETED** (Commit `9f28f1e3eed6e83892a3381ebb364de2fc0f3c4b`)

## Summary of Changes

1. **Removed Disabled Focus Tree File**
   - Deleted `common/national_focus/italy.txt.disabled`.

2. **Spatial & Dependency Fixes (`common/national_focus/italy.txt`)**
   - Fixed horizontal collision on `y = 12` by shifting `ITA_ww1_proportional_representation` from `x = 1` to `x = 6` (`dx >= 2` across all nodes on `y = 12`).
   - Fixed 2 vertical prerequisite jumps (`1 <= child_y - parent_y <= 3`):
     - `ITA_ww1_postwar_fleet_review` (`y = 7`): prerequisite updated from `ITA_ww1_battleship_fleet_in_being` (`y = 3`) to `ITA_ww1_adriatic_convoys` (`y = 4`).
     - `ITA_ww1_vittorio_veneto` (`y = 9`): prerequisite updated from `ITA_ww1_trentino_defence` (`y = 4`) to `ITA_ww1_piave_line` (`y = 6`).

3. **Balance Ceilings (`common/national_focus/italy.txt`)**
   - Reduced `ITA_ww1_treaty_of_london` war support reward from `0.10` to `0.05` (max single-focus war support `<= 0.05`).
   - Reduced `ITA_ww1_first_aerial_bombing` tech bonus from `0.50` to `0.25` (max `add_tech_bonus` bonus `<= 0.25`).
   - Calibrated positive stability and war support awards across the tree so total positive stability is `0.15` (`<= 0.15`) and total positive war support is `0.15` (`<= 0.20`).
   - Preserved unique `add_tech_bonus` names with `uses = 1`, `add_political_power <= 60`, and zero `create_unit` / `add_manpower` rewards.

4. **Wired All 18 Unused Ideas (`common/national_focus/italy.txt`)**
   - Wired all 18 unused ideas from `common/ideas/ww1_italy_ideas.txt` into their corresponding focuses (`ITA_ww1_strengthened_carabinieri`, `ITA_ww1_railway_mobilisation_plan`, `ITA_ww1_frontier_fortress_belt`, `ITA_ww1_mountain_howitzers`, `ITA_ww1_complimentary_officer_academies`, `ITA_ww1_dismounted_cavalry_regiments`, `ITA_ww1_gas_respirators`, `ITA_ww1_arditi_shock_troops`, `ITA_ww1_motorized_shock_cadres`, `ITA_ww1_taranto_naval_arsenal`, `ITA_ww1_adriatic_naval_stations`, `ITA_ww1_adriatic_patrol_network`, `ITA_ww1_otranto_barrage_net`, `ITA_ww1_albanian_convoy_routes`, `ITA_ww1_battaglione_aviatori`, `ITA_ww1_military_flight_schools`, `ITA_ww1_corpo_aeronautico_militare`, `ITA_ww1_independent_air_force_charter`).

5. **Enriched All 41 Shallow Focuses (`common/national_focus/italy.txt`)**
   - Added concrete completion rewards (buildings, state categories, equipment stockpiles, unique tech bonuses, national spirits, claims/cores, diplomatic opinions, and events) across all 41 shallow focuses so every focus in the 200-focus tree has substantive mechanical depth.

6. **Connected Orphan Events (`common/national_focus/italy.txt` & `events/ww1_italy_war_events.txt`)**
   - Connected `ww1_italy.50` to `ITA_ww1_british_coal` (`country_event = { id = ww1_italy.50 days = 2 }`).
   - Connected `ww1_italy.63` to `ITA_ww1_fiume_regency` (`country_event = { id = ww1_italy.63 days = 5 }`) and chained it from `ww1_italy.62.a` (`country_event = { id = ww1_italy.63 days = 2 }`).

## Verification Summary
- Ran `python -m unittest tests/test_ww1_italy.py -v`:
  - **15 / 16 tests PASS**:
    - `test_tree_exists_and_has_exactly_200_focuses` ... ok
    - `test_focus_tree_header_and_shortcuts` ... ok
    - `test_non_overlapping_coordinates_and_descending_y` ... ok
    - `test_mutual_exclusions_are_symmetric` ... ok
    - `test_real_completion_rewards_and_no_empty_flags` ... ok
    - `test_internal_gauges_defined_and_clamped` ... ok
    - `test_balance_ceilings_on_focus_tree` ... ok
    - `test_active_five_gauges_and_zero_unused_ideas` ... ok
    - `test_zero_shallow_focuses` ... ok
    - `test_ideas_volume_and_valid_modifiers` ... ok
    - `test_opinion_modifiers_exist` ... ok
    - `test_events_volume_options_and_spontaneous_count` ... ok
    - `test_decisions_count_categories_and_costs` ... ok
    - `test_map_state_targeted_decisions_and_zero_orphan_events` ... ok
    - `test_gfx_sprite_definitions_and_shine` ... ok
  - Only `test_localisation_bom_and_mirror_parity` remains for Task 5 as expected.
