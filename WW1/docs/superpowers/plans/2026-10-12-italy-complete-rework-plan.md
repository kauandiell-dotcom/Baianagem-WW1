# Kingdom of Italy (`ITA`, 1911–1923) Complete Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute a complete structural, mechanical, visual, and localization rework of the Kingdom of Italy (`ITA`, 1911–1923), restoring all 9 missing national ideas, wiring all 18 unused ideas, reactivating the 5-gauge national engine, implementing map-based (`state_target = yes`) decisions for the Mezzogiorno, Alpine *Guerra Bianca*/Isonzo/Piave front, Libya, and Terre Irredente, fixing all 41 shallow focuses and coordinate collisions, and providing 100% bilingual EN/PT-BR localization parity.

**Architecture:**
1. **Task 1 (TDD RED Phase):** Expand `tests/test_ww1_italy.py` to enforce horizontal banner separation (`dx >= 2`), vertical prerequisite bounds (`1 <= dy <= 3`), zero shallow focuses, existence of all 9 missing ideas, active 5-gauge spirit assignment in `ww1_italy_effects.txt`, map-targeted decisions (`state_target = yes`), zero missing GFX textures on disk, zero orphan events, and 100% idea/decision localization coverage.
2. **Task 2 (Ideas, 5-Gauge Engine & GFX):** Define the 9 missing ideas in `common/ideas/ww1_italy_ideas.txt`, fix documentation-incompatible modifiers, reactivate `ita_ww1_update_gauges` in `common/scripted_effects/ww1_italy_effects.txt`, and register/fix all sprites in `interface/ww1_italy_ideas.gfx` and `interface/ww1_italy_decisions.gfx`.
3. **Task 3 (Map-Based State Decisions & Strategic Operations):** Implement state-targeted (`state_target = yes`) and strategic decisions for the Mezzogiorno (`117, 849, 156, 115, 114, 157`), Alpine/Isonzo/Piave front (`160, 159, 850, 39, 736, 852`), Libya (`448, 450, 451, 661, 663`), Terre Irredente (`850, 39, 736, 852, 163, 164`), and the *Impresa di Pola* naval raid in `common/decisions/ww1_italy_decisions.txt` and `common/decisions/categories/ww1_italy_categories.txt`.
4. **Task 4 (Focus Tree Spatial Fix, 41 Shallow Focus Upgrades & Event Connections):** Fix the `y=12` horizontal collision and 2 long vertical links (`dy > 3`), upgrade all 41 shallow focuses with concrete buildings/stockpiles/ideas/events while respecting balance ceilings (`total_pos_stab <= 0.15`, `total_pos_ws <= 0.20`), connect orphan events `ww1_italy.50` and `ww1_italy.63`, and delete `common/national_focus/italy.txt.disabled`.
5. **Task 5 (Complete Bilingual Localization EN & PT-BR):** Add bilingual localization (`KEY:0` and `KEY_desc:0`) for all 9 restored ideas and all new decisions/categories, translate identical EN/PT titles in `ww1_italy_l_braz_por.yml`, and verify single UTF-8 BOM.
6. **Task 6 (Master QA Verification — GREEN Phase):** Integrate `tests/test_ww1_italy.py` into `scripts/qa_audit_all.py` and run full verification (`0` issues, Exit Code 0).

---

### Task 1: Master QA Test Suite Expansion (`tests/test_ww1_italy.py` — RED Phase)

**Files:**
- Modify: `tests/test_ww1_italy.py`

- [ ] **Step 1: Add rework assertions to `tests/test_ww1_italy.py`**
  - In `test_non_overlapping_coordinates_and_descending_y`: assert `abs(x2 - x1) >= 2` for all pairs on the same `y` row, and `1 <= child_y - parent_y <= 3` for all prerequisite links; also assert `not (ROOT / "common/national_focus/italy.txt.disabled").exists()`.
  - Add `test_zero_shallow_focuses`: assert that no focus in `common/national_focus/italy.txt` has a `completion_reward` consisting solely of `add_political_power`, `add_stability`, `add_war_support`, `army_experience`, `navy_experience`, `air_experience`, `add_command_power`, `add_to_variable`, `set_country_flag`, `custom_effect_tooltip`, and `ita_ww1_clamp_counters`.
  - Add `test_all_referenced_ideas_defined_and_gauges_active`: assert that `ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, `ITA_southern_question_gap`, `ITA_isonzo_attrition_crisis_1`, `ITA_isonzo_attrition_crisis_2`, `ITA_isonzo_attrition_crisis_3`, `ITA_sacro_egoismo_policy`, and `ITA_vittorio_veneto_triumph` are defined in `common/ideas/ww1_italy_ideas.txt`, that `audit_file_modifiers` from `scripts.hoi4_semantic_oracle` returns 0 errors on `ww1_italy_ideas.txt` and `ww1_italy_decisions.txt`, and that `ita_ww1_update_gauges` in `common/scripted_effects/ww1_italy_effects.txt` contains `check_variable` logic for all 5 gauges.
  - Add `test_map_state_targeted_decisions_and_zero_orphan_events`: assert `common/decisions/ww1_italy_decisions.txt` defines `state_target = yes` decisions (`ITA_ww1_mezzogiorno_aqueduct_and_roads`, `ITA_ww1_carabinieri_anti_brigandage_sweep`, `ITA_ww1_southern_agrarian_credit_consortium`, `ITA_ww1_alpine_mine_warfare_tunnel`, `ITA_ww1_launch_isonzo_general_offensive`, `ITA_ww1_fortify_piave_and_monte_grappa`, `ITA_ww1_fortify_libyan_coastal_oases`, `ITA_ww1_integrate_irredenta_province`, `ITA_ww1_impresa_di_pola_raid`), and that `ww1_italy.50` and `ww1_italy.63` are triggered at least once.
  - In `test_localisation_bom_and_mirror_parity` and `test_gfx_sprite_definitions_and_shine`: assert single UTF-8 BOM (`b[:3] == b"\xef\xbb\xbf"` and `b[3:6] != b"\xef\xbb\xbf"`), assert all ideas in `ww1_italy_ideas.txt` and all decisions in `ww1_italy_decisions.txt` have `:0` and `_desc:0` keys in both EN and PT-BR, and assert all `texturefile` paths in `interface/ww1_italy_*.gfx` exist on disk.
- [ ] **Step 2: Run `python -m unittest tests/test_ww1_italy.py -v` and confirm expected RED failures**
- [ ] **Step 3: Commit (`test(ita): expand Italy QA test suite for complete rework (RED)`)**

---

### Task 2: 9 Missing National Ideas, 5-Gauge Dynamic Engine & GFX Fixes

**Files:**
- Modify: `common/ideas/ww1_italy_ideas.txt`
- Modify: `common/scripted_effects/ww1_italy_effects.txt`
- Modify: `interface/ww1_italy_ideas.gfx`
- Modify: `interface/ww1_italy_decisions.gfx`

- [ ] **Step 1: Add the 9 missing ideas and fix documentation-incompatible modifiers in `common/ideas/ww1_italy_ideas.txt`**
  - Add `ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, `ITA_southern_question_gap`, `ITA_sacro_egoismo_policy`, `ITA_isonzo_attrition_crisis_1`, `ITA_isonzo_attrition_crisis_2`, `ITA_isonzo_attrition_crisis_3`, `ITA_vittorio_veneto_triumph`.
  - Replace `production_speed_infrastructure_factor` and `production_speed_industrial_complex_factor` in `ITA_carbone_bianco_hydro`, `ITA_energy_independence_spirit`, and `ITA_mezzogiorno_development_stage` with `production_speed_buildings_factor` and `local_resources_factor` (valid in both `modifiers_documentation.md` and `hoi4_semantic_oracle.py`).
- [ ] **Step 2: Reactivate the 5-Gauge Engine in `common/scripted_effects/ww1_italy_effects.txt`**
  - Update `ita_ww1_update_gauges` so that after `ita_ww1_clean_legacy_gauges = yes` and `ita_ww1_clamp_counters = yes`, it evaluates `check_variable` on `ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, and `ita_ww1_irredentism` and applies the corresponding tier spirit for each gauge!
- [ ] **Step 3: Fix `interface/ww1_italy_decisions.gfx` and register new idea sprites in `interface/ww1_italy_ideas.gfx`**
  - In `interface/ww1_italy_decisions.gfx`, replace `gfx/interface/decisions/decision_category_generic.dds` with existing `gfx/interface/decisions/ww1_italy/ITA_ww1_decision_1.dds`..`5.dds` and add sprites for the 9 new decisions.
  - In `interface/ww1_italy_ideas.gfx`, ensure all ideas in `ww1_italy_ideas.txt` have valid sprites pointing to existing `.dds` files in `gfx/interface/ideas/ww1_italy/`.
- [ ] **Step 4: Commit (`feat(ita): restore 9 missing national ideas, reactivate 5-gauge engine, and fix GFX sprites`)**

---

### Task 3: Map-Based State Decisions & Strategic Operations (`common/decisions/ww1_italy_decisions.txt`)

**Files:**
- Modify: `common/decisions/categories/ww1_italy_categories.txt`
- Modify: `common/decisions/ww1_italy_decisions.txt`

- [ ] **Step 1: Add Mezzogiorno, Guerra Bianca/Isonzo, and Quarta Sponda/Irredenta decisions to `common/decisions/ww1_italy_decisions.txt`**
  - Under `ITA_ww1_economic_mobilisation_category` (or dedicated Mezzogiorno section):
    - `ITA_ww1_mezzogiorno_aqueduct_and_roads` (`state_target = yes`, `target_ trigger` on owned states `117, 849, 156, 115, 114, 157`)
    - `ITA_ww1_carabinieri_anti_brigandage_sweep` (`state_target = yes`, `target_trigger` on owned states `117, 849, 156, 115, 114, 157`)
    - `ITA_ww1_southern_agrarian_credit_consortium` (upgrades `ITA_southern_question_gap` / `ITA_mezzogiorno_development_stage` $\to$ `ITA_mezzogiorno_integrated`)
  - Under `ITA_ww1_military_readiness_category`:
    - `ITA_ww1_alpine_mine_warfare_tunnel` (`state_target = yes`, `target_trigger` on owned/controlled states `160, 159, 850, 39, 736, 852`)
    - `ITA_ww1_launch_isonzo_general_offensive` (wartime offensive decision managing `ITA_isonzo_attrition_crisis_1`..`3` under Cadorna vs. breakthrough under Diaz)
    - `ITA_ww1_fortify_piave_and_monte_grappa` (`state_target = yes`, `target_trigger` on `160, 159`)
    - `ITA_ww1_impresa_di_pola_raid` (Regia Marina frogmen/MAS raid against `AUS`)
  - Under `ITA_ww1_diplomatic_initiatives_category`:
    - `ITA_ww1_fortify_libyan_coastal_oases` (`state_target = yes`, `target_trigger` on owned states `448, 450, 451, 661, 663`)
    - `ITA_ww1_integrate_irredenta_province` (`state_target = yes`, `target_trigger` on owned states `850, 39, 736, 852, 163, 164`)
- [ ] **Step 2: Verify with Semantic Oracle and `tests/test_ww1_italy.py`**
- [ ] **Step 3: Commit (`feat(ita): implement map-based Mezzogiorno, Alpine Guerra Bianca, Libyan, and Irredenta decisions`)**

---

### Task 4: Focus Tree Spatial Fix, 41 Shallow Focus Upgrades & Orphan Event Connections

**Files:**
- Modify: `common/national_focus/italy.txt`
- Modify: `events/ww1_italy_war_events.txt`
- Delete: `common/national_focus/italy.txt.disabled`

- [ ] **Step 1: Fix spatial coordinates and remove `common/national_focus/italy.txt.disabled`**
  - Fix the `y = 12` horizontal collision (`abs(x2 - x1) >= 2` on every `y` row).
  - Fix the 2 long vertical prerequisite links (`1 <= dy <= 3` on every link) by adjusting parent links on `ITA_ww1_postwar_fleet_review` and `ITA_ww1_vittorio_veneto`.
  - Delete `common/national_focus/italy.txt.disabled`.
- [ ] **Step 2: Upgrade all 41 shallow focuses, wire the 18 unused ideas, and respect balance ceilings**
  - Wire the 18 unused ideas (`ITA_ww1_adriatic_naval_stations`, `ITA_ww1_adriatic_patrol_network`, `ITA_ww1_albanian_convoy_routes`, `ITA_ww1_arditi_shock_troops`, `ITA_ww1_battaglione_aviatori`, `ITA_ww1_complimentary_officer_academies`, `ITA_ww1_corpo_aeronautico_militare`, `ITA_ww1_dismounted_cavalry_regiments`, `ITA_ww1_frontier_fortress_belt`, `ITA_ww1_gas_respirators`, `ITA_ww1_independent_air_force_charter`, `ITA_ww1_military_flight_schools`, `ITA_ww1_motorized_shock_cadres`, `ITA_ww1_mountain_howitzers`, `ITA_ww1_otranto_barrage_net`, `ITA_ww1_railway_mobilisation_plan`, `ITA_ww1_strengthened_carabinieri`, `ITA_ww1_taranto_naval_arsenal`) into their thematic focuses.
  - Enrich all 41 shallow focuses with concrete buildings, infrastructure, fortifications, equipment stockpiles (`infantry_equipment_1`, `artillery_equipment_1`, `support_equipment_1`), tech bonuses (`<= 0.25`, `uses = 1`, unique `name`), or ideas.
  - Ensure `total_pos_stab <= 0.15` and `total_pos_ws <= 0.20` across all 200 focuses (reduce `add_war_support` on `ITA_ww1_treaty_of_london` from `0.10` to `0.02` so total positive war support is `<= 0.20`).
  - Trigger `ww1_italy.50` in `ITA_ww1_british_coal` (or `ITA_ww1_british_friendship`) and `ww1_italy.63` in `ITA_ww1_fiume_regency` (and `ww1_italy.62.a`).
- [ ] **Step 3: Commit (`feat(ita): fix focus coordinates, enrich 41 shallow focuses, wire 18 ideas, and connect orphan events`)**

---

### Task 5: Complete Bilingual Localization (`localisation/`)

**Files:**
- Modify: `localisation/english/ww1_italy_l_english.yml`
- Modify: `localisation/braz_por/ww1_italy_l_braz_por.yml`

- [ ] **Step 1: Add bilingual localization for all 9 restored ideas and 9 new decisions**
  - Add `:0` and `_desc:0` keys in both `ww1_italy_l_english.yml` and `ww1_italy_l_braz_por.yml` for all 9 restored ideas and all 9 new decisions.
  - Translate the 6 identical EN/PT strings in `ww1_italy_l_braz_por.yml` into Portuguese (`ITA_ww1_battaglione_aviatori`, `ITA_ww1_caporetto`, `ITA_ww1_corpo_aeronautico_militare`, `ITA_ww1_opera_nazionale_combattenti`, `ITA_ww1_saint_jean_de_maurienne`, `ITA_ww1_vittorio_veneto`).
  - Ensure strictly single UTF-8 BOM (`b"\xef\xbb\xbf"`).
- [ ] **Step 2: Commit (`feat(ita): add complete bilingual localization for restored ideas and map decisions`)**

---

### Task 6: Master QA Verification & Integration (`scripts/qa_audit_all.py`)

**Files:**
- Modify: `scripts/qa_audit_all.py`

- [ ] **Step 1: Add Italy Semantic Oracle & `tests/test_ww1_italy.py` to `scripts/qa_audit_all.py`**
- [ ] **Step 2: Run `python -m unittest tests/test_ww1_italy.py -v` and `python scripts/qa_audit_all.py` (must exit 0)**
- [ ] **Step 3: Commit (`test(qa): integrate Italy test suite and semantic oracle check into master QA audit`)**
