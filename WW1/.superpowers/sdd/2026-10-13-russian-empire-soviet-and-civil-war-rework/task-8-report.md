# Task 8 Report: Dedicated White Movement Focus Tree (`common/national_focus/white_russia.txt` — 60 Focuses)

## Summary of Implementation
We have constructed and verified the complete dedicated national focus tree for White Russia (`white_russia_focus`), featuring exactly 60 substantive, non-colliding focuses across 4 distinct visual wings:

1. **Focus Tree Header & Entry Conditions:**
   - ID: `white_russia_focus`
   - Country trigger: `country = { factor = 0 modifier = { add = 10 tag = WHT } }`
   - `default = no`, `reset_on_civilwar = no`
   - Continuous focus position: `{ x = 20 y = 1400 }`
   - Shortcuts for all 4 wings:
     - `WHT_ww1_shortcut_omsk` -> `WHT_ufa_state_conference`
     - `WHT_ww1_shortcut_afsr` -> `WHT_first_kuban_campaign`
     - `WHT_ww1_shortcut_entente` -> `WHT_allied_supreme_war_council_appeal`
     - `WHT_ww1_shortcut_restoration` -> `WHT_russia_one_and_indivisible`

2. **4-Wing Non-Colliding Layout Grid Architecture (60 Focuses):**
   - **Wing 1: The Omsk Directorate & Supreme Ruler Kolchak (15 focuses, x: 2..6)**:
     - Root: `WHT_ufa_state_conference` (x=4, y=0)
     - Focuses: `WHT_czechoslovak_legion_alliance` (x=2, y=1), `WHT_omsk_directorate` (x=4, y=1), `WHT_trans_siberian_logistics` (x=6, y=1), `WHT_seize_kazan_gold` (x=2, y=2), `WHT_kolchak_supreme_ruler` (x=4, y=2), `WHT_pepelyayev_siberian_corps` (x=6, y=2), `WHT_ural_industrial_complex` (x=2, y=3), `WHT_siberian_mobilization` (x=4, y=3), `WHT_siberian_river_flotillas` (x=6, y=3), `WHT_siberian_fortifications` (x=2, y=4), `WHT_purge_socialist_revolutionaries` (x=4, y=4), `WHT_omsk_cadet_corps` (x=6, y=4), `WHT_ural_offensive` (x=2, y=5), `WHT_great_siberian_march` (x=6, y=5).
   - **Wing 2: Armed Forces of South Russia - Denikin, Wrangel & Cossacks (16 focuses, x: 12..16)**:
     - Root: `WHT_first_kuban_campaign` (x=14, y=0)
     - Focuses: `WHT_volunteer_army_mobilization` (x=12, y=1), `WHT_denikin_assumes_command` (x=14, y=1), `WHT_cossack_hosts_federation` (x=16, y=1), `WHT_colored_officer_regiments` (x=12, y=2), `WHT_armed_forces_of_south_russia` (x=14, y=2), `WHT_don_and_kuban_cavalry_corps` (x=16, y=2), `WHT_armored_train_flotillas` (x=12, y=3), `WHT_moscow_directive` (x=14, y=3), `WHT_tarki_and_terek_pacification` (x=16, y=3), `WHT_black_sea_squadron` (x=12, y=4), `WHT_wrangel_land_reform` (x=14, y=4), `WHT_black_baron_offensive` (x=16, y=4), `WHT_crimean_redoubt` (x=12, y=5), `WHT_tsaritsyn_bridgehead` (x=14, y=5), `WHT_russian_army_reorganization` (x=16, y=5).
   - **Wing 3: Entente Intervention & Western Munitions (15 focuses, x: 22..26)**:
     - Root: `WHT_allied_supreme_war_council_appeal` (x=24, y=0)
     - Focuses: `WHT_general_knox_british_mission` (x=22, y=1), `WHT_french_black_sea_mission` (x=24, y=1), `WHT_japanese_siberian_liaison` (x=26, y=1), `WHT_british_vickers_and_enfield_supplies` (x=22, y=2), `WHT_murmansk_and_arkhangelsk_bridgehead` (x=24, y=2), `WHT_american_railroad_corps` (x=26, y=2), `WHT_heavy_mark_v_tanks` (x=22, y=3), `WHT_royal_navy_black_sea_escorts` (x=24, y=3), `WHT_renault_ft_tanks` (x=26, y=3), `WHT_air_service_sopwith_camels` (x=22, y=4), `WHT_paris_peace_conference_delegation` (x=24, y=4), `WHT_trans_pacific_credit_lines` (x=26, y=4), `WHT_western_military_academies` (x=22, y=5), `WHT_entente_arsenal_of_liberation` (x=26, y=5).
   - **Wing 4: Post-War Political Restoration - Constituent Assembly vs Crowned Regent (14 focuses, x: 32..36)**:
     - Root: `WHT_russia_one_and_indivisible` (x=34, y=0)
     - Branching Ideological Divergence: `WHT_constituent_assembly` (x=32, y=1, democratic) vs `WHT_military_dictatorship` (x=36, y=1, autocratic/monarchist).
     - Branching Progressions: `WHT_broad_coalition_duma` (x=32, y=2), `WHT_zemstvo_self_governance` (x=32, y=3), `WHT_free_peasant_proprietorship` (x=32, y=4) vs `WHT_restoration_of_the_monarchy` (x=36, y=2), `WHT_crowned_regency_council` (x=36, y=3), `WHT_loyalist_officer_privileges` (x=36, y=4).
     - State Security & Reconstruction Trunk: `WHT_okhrana_restoration` (x=34, y=2), `WHT_reconstruction_of_devastated_lands` (x=34, y=3), `WHT_national_reconciliation_decree` (x=34, y=4).
     - Convergence: `WHT_all_russian_reunification` (x=34, y=5).
     - Capstone: `WHT_reunify_the_russian_state` (x=34, y=6), which restores Russian statehood by executing `change_tag_to = SOV`!

3. **Spatial Geometry Verification:**
   - **0 coordinate collisions** across all 60 focuses.
   - For every row $y$, adjacent focuses strictly satisfy $|x_2 - x_1| \ge 2$.
   - All 4 wings have 6 units of horizontal clearance ($x \in [2..6]$, $[12..16]$, $[22..26]$, $[32..36]$).
   - Every prerequisite link satisfies parent existence, $dy > 0$, and $1 \le \Delta y \le 3$.

4. **Concrete, Tangible Rewards (Zero Hollow Focuses):**
   - Every focus provides meaningful gameplay value:
     - Building slots, arms factories, civilian factories, infrastructure, naval bases, dockyards, land/coastal bunkers.
     - Equipment infusions (rifles, support gear, artillery, convoys, aircraft).
     - Tech bonuses across infantry, artillery, armor, land doctrine, naval doctrine, and air doctrine.
     - Experience grants (army, navy, air) and command power.
     - Stability, war support, political power, and manpower grants.
     - 22 dedicated White Movement national spirits implemented in `common/ideas/ww1_russia_ideas.txt`.

## Verification & Test Results
- `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_white_focus_tree_integrity -v`: **PASS** (OK, 0.013s)
- Clausewitz Semantic Oracle (`audit_file_modifiers`): **0 errors** across `white_russia.txt` and `ww1_russia_ideas.txt`.
- Clausewitz Bracket Balance: **100% balanced** (open=277, close=277 in focus tree; open=339, close=339 in ideas).
- Sprite Icon Coverage: **100% verified** (all 60 icons exist in `interface/*.gfx`).
- Git Commit: `629b48d` (`feat(wht): implement dedicated 60-focus White Movement national focus tree`).
