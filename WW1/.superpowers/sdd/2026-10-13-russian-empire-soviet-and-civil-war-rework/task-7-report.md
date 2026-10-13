# Task 7 Report: Dedicated Soviet Russia Focus Tree (`common/national_focus/soviet_russia.txt` — 80 Focuses)

## Summary of Implementation
We have constructed and verified the complete dedicated national focus tree for Soviet Russia (`soviet_russia_focus`), featuring exactly 80 substantive, non-colliding focuses across 5 distinct visual wings:

1. **Focus Tree Header & Entry Conditions:**
   - ID: `soviet_russia_focus`
   - Weight trigger: `country = { factor = 0 modifier = { add = 10 AND = { tag = SOV has_government = communism } } }`
   - `default = no`, `reset_on_civilwar = no`
   - Continuous focus position: `{ x = 25 y = 1400 }`
   - Shortcuts for all 5 wings (`SOV_ww1_shortcut_war_communism`, `SOV_ww1_shortcut_red_army`, `SOV_ww1_shortcut_goelro`, `SOV_ww1_shortcut_comintern`, `SOV_ww1_shortcut_ussr`)

2. **5-Wing Non-Colliding Layout Grid Architecture:**
   - **Wing 1: War Communism & Red Terror (16 focuses, x: 2..6)**:
     - Root: `SOV_all_power_to_the_soviets`
     - Focuses: `SOV_decree_on_land`, `SOV_establish_the_vecheka`, `SOV_war_communism_decrees`, `SOV_grain_requisition_detachments`, `SOV_revolutionary_tribunals`, `SOV_militarization_of_labor`, `SOV_communist_subbotniks`, `SOV_the_red_terror`, `SOV_nationalization_of_heavy_industry`, `SOV_worker_food_rationing_cards`, `SOV_eradicate_counter_revolutionary_cells`, `SOV_central_transport_board_glavtrans`, `SOV_smash_the_tambov_rebellion`, `SOV_kronstadt_reckoning`, `SOV_triumph_of_the_proletarian_dictatorship`
   - **Wing 2: Red Army Doctrine & Military Commissars (18 focuses, x: 12..18)**:
     - Root: `SOV_workers_and_peasants_red_army`
     - Focuses: `SOV_the_revvoyensovyet`, `SOV_recruit_tsarist_voenspetsy`, `SOV_institution_of_political_commissars`, `SOV_armored_train_command`, `SOV_red_officer_courses_vystrel`, `SOV_conscription_of_the_toilers`, `SOV_the_first_cavalry_army`, `SOV_tachanka_warfare`, `SOV_arsenals_of_tula_and_izhevsk`, `SOV_partisan_detachments_and_red_guards`, `SOV_mass_artillery_concentration`, `SOV_red_baltic_fleet_defenses`, `SOV_revolutionary_red_air_fleet`, `SOV_frunze_military_reforms`, `SOV_tukhachevsky_operational_art`, `SOV_field_communications_and_logistics`, `SOV_rkka_victorious_red_colossus`
   - **Wing 3: GOELRO & Economic Reconstruction - NEP vs Superindustrialization (16 focuses, x: 22..28)**:
     - Root: `SOV_the_goelro_plan`
     - Focuses: `SOV_shaturskaya_power_station`, `SOV_founding_of_gosplan`, `SOV_kashira_and_volkhov_turbines`, `SOV_reopen_the_donbass_coalfields`, `SOV_baku_oil_syndicate`, `SOV_the_new_economic_policy` (mutually exclusive with `SOV_primitive_socialist_accumulation`), `SOV_primitive_socialist_accumulation`, `SOV_the_prodnalog_tax_in_kind`, `SOV_stabilize_the_soviet_chervonets`, `SOV_state_industrial_monopolies`, `SOV_forced_grain_procurements`, `SOV_nepmen_and_cooperatives`, `SOV_foreign_concessions_krupp_hammer`, `SOV_dnieper_hydroelectric_project`, `SOV_ural_kuznetsk_combine`
   - **Wing 4: Comintern & World Revolution - Polish-Soviet War & Rapallo (16 focuses, x: 32..36)**:
     - Root: `SOV_the_third_international`
     - Focuses: `SOV_twenty_one_conditions`, `SOV_support_the_bavarian_and_hungarian_soviets`, `SOV_ignite_the_western_flame`, `SOV_the_target_vistula_offensive`, `SOV_anti_imperialist_eastern_bureau`, `SOV_the_treaty_of_riga_settlement`, `SOV_proclaim_the_curzon_line`, `SOV_aid_to_anatolian_nationalists`, `SOV_the_genoa_conference_diplomacy`, `SOV_treaty_of_rapallo`, `SOV_alliance_with_kuomintang`, `SOV_secret_lipetsk_fighter_school`, `SOV_kama_tank_proving_grounds`, `SOV_tomka_chemical_weapons_testing`, `SOV_break_the_capitalist_encirclement`
   - **Wing 5: State Building & Formation of the USSR 1922 (14 focuses, x: 42..46)**:
     - Root: `SOV_peoples_commissariat_of_nationalities`
     - Focuses: `SOV_sovietization_of_ukraine`, `SOV_sovietization_of_belarus`, `SOV_red_army_in_the_caucasus`, `SOV_pacify_the_basmachi_in_turkestan`, `SOV_the_georgian_affair_debate`, `SOV_korenizatsiya_indigenization_policy`, `SOV_treaty_on_the_creation_of_the_ussr`, `SOV_autonomous_soviet_republics`, `SOV_the_likbez_literacy_campaign`, `SOV_the_1924_soviet_constitution`, `SOV_emancipation_of_women_zhenotdel`, `SOV_sovnarkom_central_bureaucracy`, `SOV_the_socialist_fatherland_triumphant`

3. **Spatial Geometry Verification:**
   - 0 coordinate collisions across all 80 focuses.
   - For any two focuses on the same row $y$, $|x_2 - x_1| \ge 2$.
   - All parent-child prerequisite connections satisfy $1 \le \Delta y \le 3$.
   - All wing columns are strictly separated ($x \in [2..6]$, $[12..18]$, $[22..28]$, $[32..36]$, $[42..46]$) with at least 4 units of horizontal clearance between adjacent wings.

4. **Concrete, Tangible Rewards (Zero Hollow Focuses):**
   - Every single one of the 80 focuses grants substantive gameplay rewards:
     - Building slots, military factories, civilian factories, infrastructure, supply nodes, coastal forts.
     - Equipment stockpiles (infantry weapons, support equipment, artillery, trains).
     - Technology bonuses (land doctrine, industry, artillery, armor, naval doctrine, air doctrine).
     - Army, navy, and air experience.
     - Manpower grants and command power.
     - 10 dedicated national ideas implemented in `common/ideas/ww1_russia_ideas.txt`.

## Verification & Test Results
- `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_soviet_focus_tree_integrity -v`: **PASS** (OK, 0.054s)
- All 6 completed rework unit tests (`test_characters_and_tags`, `test_tsarist_mechanics_and_ideas`, `test_crisis_engine_and_gauges`, `test_civil_war_spawns_and_oobs`, `test_brest_litovsk_and_diplomacy`, `test_soviet_focus_tree_integrity`): **PASS** (OK)
- Clausewitz Semantic Oracle (`audit_file_modifiers`): **0 errors** across `soviet_russia.txt` and `ww1_russia_ideas.txt`.
- Clausewitz Brace Auditor (`ClausewitzAuditor.audit_braces`): **100% balanced**.
- UTF-8 BOM Auditor: Verified strictly NO BOM on `.txt` files.
- Commit hash: `45c656b` (`feat(sov): implement dedicated 80-focus Soviet Russia national focus tree`).
