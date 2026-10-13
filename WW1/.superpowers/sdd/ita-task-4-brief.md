# Italy Rework Task 4: Focus Tree Spatial Fix, 41 Shallow Focus Upgrades & Orphan Event Connections

**Files:**
- Modify: `common/national_focus/italy.txt`
- Modify: `events/ww1_italy_war_events.txt`
- Delete: `common/national_focus/italy.txt.disabled`

## Step 1: Delete `common/national_focus/italy.txt.disabled` & Fix Spatial Coordinates in `common/national_focus/italy.txt`
1. Remove `common/national_focus/italy.txt.disabled` (`git rm -f common/national_focus/italy.txt.disabled` or `os.remove`).
2. Fix the horizontal banner collision on row `y = 12` in `common/national_focus/italy.txt`:
   - Currently on `y = 12`, `ITA_ww1_proportional_representation` is at `x = 7` and `ITA_ww1_popular_party` is at `x = 8` (`dx = 1`).
   - Adjust `x` coordinates on `y = 12` (and any colliding neighbors on `y = 12`) so that EVERY pair of focuses on the same `y` row across all 200 focuses satisfies `abs(x2 - x1) >= 2`!
3. Fix the 2 long vertical prerequisite links (`dy > 3`) so that EVERY parent-child prerequisite across all 200 focuses satisfies `1 <= child_y - parent_y <= 3`:
   - `ITA_ww1_postwar_fleet_review` (`y = 7`) currently has prerequisite `ITA_ww1_battleship_fleet_in_being` (`y = 3`, `dy = 4`). Change that prerequisite in `ITA_ww1_postwar_fleet_review` from `focus = ITA_ww1_battleship_fleet_in_being` to `focus = ITA_ww1_adriatic_convoys` (`y = 5`, `dy = 2`), keeping `focus = ITA_ww1_anti_submarine_patrols` (`y = 6`) and `focus = ITA_ww1_human_torpedoes` (`y = 6`).
   - `ITA_ww1_vittorio_veneto` (`y = 6`) currently has prerequisite `ITA_ww1_trentino_defence` (`y = 1`, `dy = 5`) and `ITA_ww1_solstice_battle` (`y = 5`, `dy = 1`). Change `focus = ITA_ww1_trentino_defence` on `ITA_ww1_vittorio_veneto` to `focus = ITA_ww1_piave_line` (`y = 4`, `dy = 2`)!

## Step 2: Fix Balance Ceiling Violation & Wire All 18 Unused Ideas
**CRITICAL BALANCE CEILING RULES (`tests/test_ww1_italy.py`):**
- `total_pos_stab <= 0.15` across the entire focus tree (`add_stability <= 0.05` per focus). Do NOT add positive `add_stability` to any focus, and if `total_pos_stab > 0.15`, reduce positive `add_stability` so `total_pos_stab <= 0.15`!
- `total_pos_ws <= 0.20` across the entire focus tree (`add_war_support <= 0.05` per focus). Currently `ITA_ww1_treaty_of_london` has `add_war_support = 0.10` which makes `total_pos_ws = 0.23`! Change `add_war_support = 0.10` in `ITA_ww1_treaty_of_london` to `add_war_support = 0.02` (so `total_pos_ws` is `0.15 <= 0.20` and single focus cap `<= 0.05` is respected!).
- `add_political_power <= 60` per focus.
- `add_tech_bonus`: `bonus <= 0.25`, `uses = 1`, NO `ahead_reduction`, and every `name` must be unique across all focuses!
- Prohibited effects in focuses: NEVER use `create_unit` or `add_manpower` in `common/national_focus/italy.txt`!

**Wire All 18 Previously Unused Ideas into `common/national_focus/italy.txt`:**
Ensure every one of these 18 ideas is granted (`add_ideas = ...`) in its corresponding focus in `common/national_focus/italy.txt`:
1. `ITA_ww1_adriatic_naval_stations` -> add to `ITA_ww1_brindisi_venice_bases`
2. `ITA_ww1_adriatic_patrol_network` -> add to `ITA_ww1_adriatic_watch`
3. `ITA_ww1_albanian_convoy_routes` -> add to `ITA_ww1_adriatic_convoys`
4. `ITA_ww1_arditi_shock_troops` -> add to `ITA_ww1_assault_units`
5. `ITA_ww1_battaglione_aviatori` -> add to `ITA_ww1_aviators_battalion`
6. `ITA_ww1_complimentary_officer_academies` -> add to `ITA_ww1_reserve_officer_schools`
7. `ITA_ww1_corpo_aeronautico_militare` -> add to `ITA_ww1_aeronautical_corps`
8. `ITA_ww1_dismounted_cavalry_regiments` -> add to `ITA_ww1_dismounted_cavalry`
9. `ITA_ww1_frontier_fortress_belt` -> add to `ITA_ww1_frontier_fortifications`
10. `ITA_ww1_gas_respirators` -> add to `ITA_ww1_gas_defence`
11. `ITA_ww1_independent_air_force_charter` -> add to `ITA_ww1_air_autonomy_debate`
12. `ITA_ww1_military_flight_schools` -> add to `ITA_ww1_pilot_schools`
13. `ITA_ww1_motorized_shock_cadres` -> add to `ITA_ww1_motor_transport`
14. `ITA_ww1_mountain_howitzers` -> add to `ITA_ww1_mountain_artillery`
15. `ITA_ww1_otranto_barrage_net` -> add to `ITA_ww1_otranto_barrage`
16. `ITA_ww1_railway_mobilisation_plan` -> add to `ITA_ww1_north_east_mobilisation`
17. `ITA_ww1_strengthened_carabinieri` -> add to `ITA_ww1_carabinieri_reinforcement`
18. `ITA_ww1_taranto_naval_arsenal` -> add to `ITA_ww1_taranto_base`

## Step 3: Upgrade All 41 Shallow Focuses & Connect Orphan Events
1. Connect the 2 orphan events:
   - In `ITA_ww1_british_coal` (or `ITA_ww1_british_friendship`), add `country_event = { id = ww1_italy.50 days = 1 }`.
   - In `ITA_ww1_fiume_regency`, ensure `country_event = { id = ww1_italy.63 days = 1 }` is triggered (and in `events/ww1_italy_war_events.txt` under `ww1_italy.62.a`, also trigger `country_event = { id = ww1_italy.63 days = 2 }`).
2. For all 41 shallow focuses (which currently only have `add_political_power`, `add_stability`, `add_war_support`, `army_experience`, `navy_experience`, `air_experience`, `add_command_power`, `add_to_variable`, `set_country_flag`, `ita_ww1_clamp_counters`), add a concrete, tangible reward to every single one so `test_zero_shallow_focuses` passes 100%:
   - Use state building constructions (`158 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }`, `2 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }`, `117 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }`, `159 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }`, `160 = { add_building_construction = { type = bunker level = 1 instant_build = yes province = { all_provinces = yes limit_to_border = yes } } }`), equipment stockpile additions (`add_equipment_to_stockpile = { type = infantry_equipment_1 amount = 500 producer = ITA }`, `artillery_equipment_1`, `support_equipment_1`), `add_ideas`, `swap_ideas`, or `add_tech_bonus = { name = ITA_ww1_<unique_name> bonus = 0.25 uses = 1 category = ... }`.
   - Also clean up any duplicate `ita_ww1_clamp_counters = yes ita_ww1_clamp_counters = yes` calls.

## Verification & Commit
Run:
```bash
python -m unittest tests/test_ww1_italy.py -v
```
Confirm that all tree, coordinate, shallow focus, balance ceiling, idea, decision, and event tests PASS! (Only localization keys for Task 5 should remain).
Commit:
```bash
git add -A common/national_focus/ events/ww1_italy_war_events.txt
git commit -m "feat(ita): fix focus coordinates, enrich 41 shallow focuses, wire 18 ideas, and connect orphan events"
```
Write your report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\ita-task-4-report.md`.
