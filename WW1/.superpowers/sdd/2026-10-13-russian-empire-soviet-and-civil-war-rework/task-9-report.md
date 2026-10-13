# Task 9 Report: Tsarist Focus Tree Refactoring & Polish (`common/national_focus/soviet.txt`)

## Summary of Implementation
We have successfully refactored and polished the Russian Empire / Tsarist national focus tree (`russian_empire_focus` in `common/national_focus/soviet.txt`):

1. **Purged Obsolete Legacy Dead-End Bolshevik Branch (9 Focuses Removed):**
   - Because Soviet Russia now has its own comprehensive 80-focus dedicated tree (`soviet_russia.txt`), the legacy 7-focus dead-end Bolshevik path and its dangling successors were safely purged:
     - `SOV_all_power_to_the_soviets`
     - `SOV_storming_of_winter_palace`
     - `SOV_decree_on_peace`
     - `SOV_decree_on_land`
     - `SOV_founding_of_the_cheka`
     - `SOV_creation_of_the_red_army`
     - `SOV_war_communism_decrees`
     - `SOV_crush_the_white_armies`
     - `SOV_tambov_peasant_rebellion`
   - Cleaned up mutual exclusivity in `SOV_kornilov_iron_dictatorship` and `SOV_convene_constituent_assembly` so they cleanly oppose each other without referencing purged Bolshevik IDs.

2. **Added Imperial Salvation Capstone Focuses (2 Capstones Added):**
   - **`SOV_annexation_of_tsargrad` (*The Annexation of Tsargrad & The Turkish Straits*):**
     - Position: $x = 115, y = 9$ (Prerequisite: `SOV_hagia_sophia_cross_restored` at $x = 115, y = 8$).
     - Rewards: Grants idea `SOV_tsargrad_liberated` (+20% war support, +15% stability, +15% political power gain), cores states 341 (Istanbul/Tsargrad), 340 (Edirne), 339 (Canakkale/Dardanelles), level 2 dockyard, level 2 coastal bunker, level 2 naval base, +50 navy experience, +15% stability, +15% war support, +150 political power.
   - **`SOV_triumph_of_the_romanov_dynasty` (*Triumph of the Romanov Dynasty*):**
     - Position: $x = 27, y = 15$ (Prerequisite: `SOV_divine_right_unbroken` at $x = 27, y = 14$).
     - Rewards: Grants national spirit `SOV_order_restored_spirit`, 2 industrial complexes & slots in Petrograd (state 195), 2 arms factories & slots in Moscow (state 219), +50 army experience, +50 command power, +15% stability, +15% war support, +150 political power.

3. **Enriched Hollow / Shallow Focuses (54 Focuses Upgraded):**
   - All previously shallow focuses granting only flat political power, stability, war support, experience, flags, or events were upgraded with tangible gameplay rewards:
     - Building slots, military factories, civilian factories, dockyards, infrastructure, supply nodes, and coastal forts.
     - Equipment stockpiles (infantry weapons, artillery, support equipment, trains, convoys).
     - Unique technology bonuses across industry, land doctrine, artillery, naval doctrine, and air equipment.

4. **Spatial Geometry Verification:**
   - Total focuses in tree: **228 focuses** (235 original - 9 purged + 2 capstones).
   - **0 coordinate collisions** across all 228 focuses.
   - For every row $y$, adjacent focuses satisfy $|x_2 - x_1| \ge 2$.
   - Every prerequisite link satisfies parent existence, $dy > 0$, and $1 \le \Delta y \le 3$.

## Verification & Test Results
- `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_imperial_focus_tree_integrity -v`: **PASS** (OK, 0.032s).
- Semantic Oracle Check (`scripts/hoi4_semantic_oracle.py:audit_file_modifiers`): **0 modifier errors**.
- Clausewitz Bracket Balance: **100% balanced** (open=1862, close=1862, diff=0).
- Git Commit: `45ea2fb` (`refactor(sov): purge legacy stubs, enrich hollow focuses, and add Imperial Salvation capstones`).
