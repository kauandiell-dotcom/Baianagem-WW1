# Task 5: 5-Wing Focus Tree Spatial Reconstruction, Tangible Rewards & Icon Diversity

**Files:**
- Modify: `common/national_focus/turkey.txt`
- Modify: `interface/ww1_ottoman_goals.gfx`

**Interfaces:**
- Consumes: All 256 focus IDs, events `ww1_ottoman.1`–`ww1_ottoman.32`, 5-Pillar ideas, `.dds` goal textures.
- Produces: Collision-free `common/national_focus/turkey.txt` (`dx >= 2` on every row, `1 <= dy <= 3` on every link, 0 hollow focuses, 0 orphan events) and diversified `interface/ww1_ottoman_goals.gfx`.

## Step 1: Reconstruct 5-Wing Spatial Coordinates in `common/national_focus/turkey.txt`
- Preserve all 256 focus IDs (`len(foci) == 256`).
- Remap all 256 focuses onto non-colliding absolute coordinates so that on every `y` row, any two focuses satisfy `abs(x2 - x1) >= 2`:
  - Wing 1 (Politics): `x = 2 .. 34`, Root `TUR_1912_savior_officers_crisis` at `y = 0`
  - Wing 2 (Economy & Railways): `x = 38 .. 58`, Root `TUR_audit_opda_administration` at `y = 0`
  - Wing 3 (Armed Forces & Straits): `x = 64 .. 84`, Root `TUR_balkan_war_aftermath_inquiry` at `y = 0`
  - Wing 4 (Great Power Diplomacy): `x = 90 .. 110`, Root `TUR_sublime_porte_foreign_ministry` at `y = 0`
  - Wing 5 (War Theaters & 1918): `x = 116 .. 140`, Root `TUR_imperial_war_council_mobilization` at `y = 0`
- Fix the 8 long-distance prerequisite links (`dy > 3`):
  - Every parent-child prerequisite must satisfy `1 <= child_y - parent_y <= 3`.
  - For capstone focuses that previously had `y` far below a high-level parent (`y=3` -> `y=8`), adjust their `y` coordinates or re-chain their prerequisites to the immediate tier above them (`y - 1` or `y - 2` within the same wing/branch) so that `1 <= child_y - parent_y <= 3` holds for 100% of prerequisites across all 256 focuses!

## Step 2: Upgrade All 59+ Hollow Focuses with Tangible Rewards & Connect Orphan Events
- Every single focus in `common/national_focus/turkey.txt` MUST pass `test_zero_hollow_focuses` in `tests/test_ww1_ottoman.py` (which strips comments, `add_political_power`, `add_stability`, `add_war_support`, `add_to_variable`, and `set_country_flag`, and checks that the remaining `completion_reward` is non-empty).
- Connect the 3 orphan events so 0 events are orphaned:
  - `TUR_legacy_of_osman_eternal` -> add `country_event = { id = ww1_ottoman.23 }`
  - `TUR_red_sea_desert_patrols` -> add `country_event = { id = ww1_ottoman.26 }`
  - `TUR_national_pact_misak_i_milli` -> add `country_event = { id = ww1_ottoman.29 }`
- Connect `TUR_tripoli_coastal_fortifications` to trigger `country_event = { id = ww1_ottoman.32 }` (or ensure `ww1_ottoman.32` is triggered).
- Ensure Pillar 2 OPDA debt progression focuses use clean `swap_ideas` or tangible economic rewards:
  - `TUR_audit_opda_administration`: adds `add_political_power = 50` and `random_owned_controlled_state = { limit = { is_core_of = TUR } add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant_build = yes } }`
  - `TUR_renegotiate_creditor_coupons`: safe `if = { limit = { has_idea = TUR_sick_man_debt } swap_ideas = { remove_idea = TUR_sick_man_debt add_idea = TUR_debt_renegotiated } }`
  - `TUR_unilateral_abrogation_of_capitulations`: safe swap to `TUR_capitulations_abrogated`
  - `TUR_complete_fiscal_liberation`: safe swap to `TUR_financial_sovereignty`
- For all other hollow focuses, add thematic, historically grounded tangible rewards based on wing/focus name:
  - Political / Administrative / Vilayet focuses: `army_experience = 15`, `add_command_power = 25`, `add_manpower = 10000`, `add_equipment_to_stockpile = { type = infantry_equipment amount = 1000 producer = TUR }`, or infrastructure in `797`/`49`/`554`/`291`.
  - Economic / Railway / Agricultural focuses: `add_extra_state_shared_building_slots = 1`, `add_building_construction = { type = industrial_complex / arms_factory / infrastructure level = 1 instant_build = yes }` in Ottoman states (`797`, `340`, `339`, `49`, `346`, `344`, `554`, `291`, `679`), or `add_tech_bonus = { name = TUR_econ_bonus bonus = 0.5 uses = 1 category = industry }`.
  - Military / Naval / Aviation focuses: `army_experience = 25`, `navy_experience = 25`, `air_experience = 25`, `add_tech_bonus` (`infantry_weapons`, `artillery`, `land_doctrine`, `naval_equipment`, `air_equipment`), or `bunker` / `coastal_bunker` in `341`, `797`, `340`, `353`.
  - Diplomacy / War Theater focuses: `add_equipment_to_stockpile`, `army_experience`, `add_manpower`, `add_command_power = 25`, or border fortifications.

## Step 3: Diversify Focus Goal Icons in `interface/ww1_ottoman_goals.gfx`
- Distribute texture mappings across available `.dds` files in `gfx/interface/goals/` so every sprite points to an existing file on disk and variety is improved.

## Step 4: Verification & Commit
Run:
```bash
python -m unittest tests/test_ww1_ottoman.py -v
```
Verify that `test_focus_count_and_coordinate_collisions`, `test_prerequisite_integrity_and_downward_progression`, `test_zero_hollow_focuses`, `test_focus_gfx_all_defined_and_textures_exist`, and `test_no_duplicate_focus_ids` all PASS!

Commit:
```bash
git add common/national_focus/turkey.txt interface/ww1_ottoman_goals.gfx
git commit -m "feat(tur): reconstruct 5-wing non-colliding focus grid, enrich hollow focus rewards, and diversify icons"
```
