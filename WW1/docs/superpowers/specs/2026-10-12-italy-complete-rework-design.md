# Kingdom of Italy (`ITA`, 1911–1923) Complete Rework — Design Specification

## 1. Executive Summary & Architectural Goals

This specification defines the complete structural, mechanical, visual, and localization rework for the **Kingdom of Italy (`ITA`, 1911–1923)** in **Baianagem-WW1**.

### Root Causes Identified in Forensic Audit
1. **9 Ghost National Ideas (100% Missing 1911 Starting Spirits & Wartime Crisis Progression):**
   - `history/countries/ITA - Italy.txt` loads `ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, and `ITA_southern_question_gap`, none of which exist in `common/ideas/ww1_italy_ideas.txt`, `interface/ww1_italy_ideas.gfx`, or `localisation/`.
   - `common/national_focus/italy.txt` references 5 additional undefined ideas: `ITA_isonzo_attrition_crisis_1`, `ITA_isonzo_attrition_crisis_2`, `ITA_isonzo_attrition_crisis_3`, `ITA_sacro_egoismo_policy`, and `ITA_vittorio_veneto_triumph`.
2. **18 Orphaned National Ideas in `common/ideas/ww1_italy_ideas.txt`:**
   - 18 defined ideas (`ITA_ww1_adriatic_naval_stations`, `ITA_ww1_adriatic_patrol_network`, `ITA_ww1_albanian_convoy_routes`, `ITA_ww1_arditi_shock_troops`, `ITA_ww1_battaglione_aviatori`, `ITA_ww1_complimentary_officer_academies`, `ITA_ww1_corpo_aeronautico_militare`, `ITA_ww1_dismounted_cavalry_regiments`, `ITA_ww1_frontier_fortress_belt`, `ITA_ww1_gas_respirators`, `ITA_ww1_independent_air_force_charter`, `ITA_ww1_military_flight_schools`, `ITA_ww1_motorized_shock_cadres`, `ITA_ww1_mountain_howitzers`, `ITA_ww1_otranto_barrage_net`, `ITA_ww1_railway_mobilisation_plan`, `ITA_ww1_strengthened_carabinieri`, `ITA_ww1_taranto_naval_arsenal`) are never granted by any focus, decision, or event.
3. **Disconnected 5-Gauge Engine (`common/scripted_effects/ww1_italy_effects.txt`):**
   - `ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, and `ita_ww1_irredentism` are modified 178 times across focuses, decisions, and events, but `ita_ww1_update_gauges` currently only strips all gauge ideas without evaluating thresholds or applying dynamic spirits.
4. **41 Shallow/Hollow Focuses, Visual Collisions & Balance Ceiling Violations (`common/national_focus/italy.txt`):**
   - 41 out of 200 focuses grant only flat PP/Stability/War Support/XP + variable changes.
   - Row `y = 12` has a horizontal banner collision (`dx = 1`) between `ITA_ww1_proportional_representation` (`x = 7`) and `ITA_ww1_popular_party` (`x = 8`).
   - 2 prerequisite links span 4–5 vertical rows (`dy = 4` on `ITA_ww1_battleship_fleet_in_being` $\to$ `ITA_ww1_postwar_fleet_review` and `dy = 5` on `ITA_ww1_trentino_defence` $\to$ `ITA_ww1_vittorio_veneto`).
   - `ITA_ww1_treaty_of_london` grants `add_war_support = 0.10`, violating the `<= 0.05` single-focus cap and `<= 0.20` tree-wide war support cap in `tests/test_ww1_italy.py`.
   - `common/national_focus/italy.txt.disabled` is a stale backup cluttering `common/national_focus/`.
5. **Zero Map-Based State Decisions (`state_target = yes`), Missing Decision Textures & Orphan Events:**
   - `common/decisions/ww1_italy_decisions.txt` has 0 `state_target = yes` map decisions.
   - `interface/ww1_italy_decisions.gfx` references `gfx/interface/decisions/decision_category_generic.dds` (5x), which does not exist on disk.
   - Events `ww1_italy.50` (London Escort Agreement) and `ww1_italy.63` (Italian Regency of Carnaro in Fiume) have `is_triggered_only = yes` but are never triggered anywhere.

---

## 2. Core Mechanical Systems

### 2.1 Restoring the 9 Missing Ideas & Connecting All 18 Orphaned Ideas
1. **9 Restored Ideas in `common/ideas/ww1_italy_ideas.txt` & `interface/ww1_italy_ideas.gfx`:**
   - `ITA_terre_irredente_dream`: `war_support_factor = 0.05`, `justify_war_goal_time = -0.15`, `army_core_attack_factor = 0.05`
   - `ITA_alpini_tradition`: `special_forces_cap = 0.05`, `acclimatization_cold_climate_gain_factor = 0.15`, `terrain_penalty_reduction = 0.05`
   - `ITA_coal_iron_scarcity`: `industrial_capacity_factory = -0.10`, `production_speed_buildings_factor = -0.10`, `min_export = 0.05`
   - `ITA_southern_question_gap`: `stability_factor = -0.08`, `production_speed_buildings_factor = -0.08`, `conscription_factor = -0.10`
   - `ITA_sacro_egoismo_policy`: `political_power_factor = 0.05`, `improve_relations_maintain_cost_factor = -0.25`, `send_volunteers_tension = -0.10`
   - `ITA_isonzo_attrition_crisis_1`: `army_morale_factor = -0.05`, `army_org_factor = -0.05`, `war_support_factor = -0.03`
   - `ITA_isonzo_attrition_crisis_2`: `army_morale_factor = -0.10`, `army_org_factor = -0.10`, `war_support_factor = -0.06`
   - `ITA_isonzo_attrition_crisis_3`: `army_morale_factor = -0.15`, `army_org_factor = -0.15`, `war_support_factor = -0.10`
   - `ITA_vittorio_veneto_triumph`: `army_attack_factor = 0.10`, `army_morale_factor = 0.10`, `stability_factor = 0.08`, `war_support_factor = 0.08`
2. **Modifier Documentation Compatibility:**
   - Replace `production_speed_infrastructure_factor` and `production_speed_industrial_complex_factor` in `ITA_carbone_bianco_hydro`, `ITA_energy_independence_spirit`, and `ITA_mezzogiorno_development_stage` with `production_speed_buildings_factor` and `local_resources_factor` so that both `scripts/hoi4_semantic_oracle.py` and `tests/test_ww1_italy.py` (`modifiers_documentation.md` check) pass with 0 errors.
3. **Connecting All 18 Orphaned Ideas to Focuses & Decisions:**
   - Every one of the 18 unused ideas in `ww1_italy_ideas.txt` is wired into its corresponding military, naval, aviation, or political focus/decision.

### 2.2 Reactivating the 5-Gauge National Engine (`common/scripted_effects/ww1_italy_effects.txt`)
`ita_ww1_update_gauges` will actively evaluate the 5 national variables (`0..100`) and apply threshold-driven effects:
- **Gauge 1 (`ita_ww1_interventionism`):**
  - `< 35` (peacetime): applies `ITA_ww1_neutralist_predominance`
  - `35 .. 65` (peacetime): applies `ITA_ww1_divided_public_opinion`
  - `> 65` (peacetime): applies `ITA_ww1_radiant_fever`
- **Gauge 2 (`ita_ww1_social_tension`):**
  - `< 30`: applies `ITA_ww1_social_truce`
  - `30 .. 65`: applies `ITA_ww1_labour_friction`
  - `> 65`: applies `ITA_ww1_revolutionary_ferment`
- **Gauge 3 (`ita_ww1_army_morale`):**
  - `< 35`: applies `ITA_ww1_shattered_discipline`
  - `35 .. 70`: applies `ITA_ww1_stoic_endurance`
  - `> 70`: applies `ITA_ww1_victorious_ardor`
- **Gauge 4 (`ita_ww1_southern_gap`):**
  - `< 30`: applies `ITA_ww1_integrated_mezzogiorno` (and upgrades `ITA_southern_question_gap` / `ITA_mezzogiorno_development_stage` $\to$ `ITA_mezzogiorno_integrated`)
  - `30 .. 65`: applies `ITA_ww1_southern_disparity`
  - `> 65`: applies `ITA_ww1_acute_agrarian_crisis`
- **Gauge 5 (`ita_ww1_irredentism`):**
  - `< 35`: applies `ITA_ww1_subdued_claims`
  - `35 .. 70`: applies `ITA_ww1_unredeemed_lands_call`
  - `> 70`: applies `ITA_ww1_irredentist_fervor`

### 2.3 Map-Based State Decisions Engine (`common/decisions/ww1_italy_decisions.txt`)
Add 3 new thematic map/strategic decision groups (`state_target = yes` and strategic operations):
1. **Mezzogiorno State-by-State Integration (`state_target = yes` on `117` Napoli, `849` Puglia, `156` Calabria, `115` Sicily, `114` Sardinia, `157` Abruzzo):**
   - `ITA_ww1_mezzogiorno_aqueduct_and_roads`: builds 1 infrastructure, sets `ITA_mezzogiorno_roads_built`, reduces `ita_ww1_southern_gap = -8`.
   - `ITA_ww1_carabinieri_anti_brigandage_sweep`: costs command power + infantry equipment, sets `ITA_mezzogiorno_state_pacified`, reduces `ita_ww1_southern_gap = -6` and `ita_ww1_social_tension = -4`.
   - `ITA_ww1_southern_agrarian_credit_consortium`: once all core southern states (`117`, `849`, `156`, `115`) are pacified or `ita_ww1_southern_gap < 30`, upgrades `ITA_southern_question_gap` / `ITA_mezzogiorno_development_stage` to `ITA_mezzogiorno_integrated` and adds 1 civilian factory in `117` (Napoli) and `115` (Sicily).
2. **Alpine *Guerra Bianca*, Isonzo Offensives & Piave Line (`state_target = yes` on `160` Veneto, `159` Lombardy, `850` Trentino, `39` South Tyrol, `736` Litorale, `852` Istria):**
   - `ITA_ww1_alpine_mine_warfare_tunnel`: (`state_target = yes` on owned/controlled Alpine border states) detonates sapping mines and builds level 1 bunker, grants `+15` army XP, sets `ITA_alpine_sector_fortified`.
   - `ITA_ww1_launch_isonzo_general_offensive`: wartime offensive decision against `AUS`. Under Cadorna (`NOT = { has_country_flag = ita_ww1_diaz_appointed }`), escalates `ITA_isonzo_attrition_crisis_1` $\to$ `ITA_isonzo_attrition_crisis_2` $\to$ `ITA_isonzo_attrition_crisis_3` while granting temporary attack momentum and army XP; under Armando Diaz, grants clean breakthrough support.
   - `ITA_ww1_fortify_piave_and_monte_grappa`: (`state_target = yes` on `160` Veneto and `159` Lombardy) constructs level 2 bunkers along the Piave/Grappa defense line and boosts `ita_ww1_army_morale = 10`.
3. **Quarta Sponda (Libya) & Terre Irredente Map Integration (`state_target = yes`):**
   - `ITA_ww1_fortify_libyan_coastal_oases`: (`state_target = yes` on `448` Tripoli, `450` Benghazi, `451` Derna, `661` Tripolitania, `663` Cyrenaica) builds level 1 infrastructure + bunker, sets `ITA_libya_oasis_secured`, and boosts compliance.
   - `ITA_ww1_integrate_irredenta_province`: (`state_target = yes` on `850` Trentino, `39` South Tyrol, `736` Litorale, `852` Istria, `163` Dalmatia, `164` Dodecanese) establishes Italian civil administration, adds core/compliance, sets `ITA_irredenta_integrated`, and reduces `ita_ww1_irredentism = -10`.
   - `ITA_ww1_impresa_di_pola_raid`: Regia Marina special frogmen (*Mignatta*) & *MAS* strike in the Adriatic against `AUS`, granting `+25` navy XP, `+5%` war support, and applying `ITA_ww1_mignatta_special_raiders`.

---

## 3. Focus Tree Spatial & Reward Rework (`common/national_focus/italy.txt`)
1. **Eliminate Coordinate Collisions & Long Arrows:**
   - Shift `ITA_ww1_popular_party` on row `y = 12` (and adjacent row `y = 12` nodes in Wing 1) so `abs(x2 - x1) >= 2` across all 200 focuses on every `y` row.
   - Re-chain `ITA_ww1_postwar_fleet_review` (`y = 7`) to intermediate `y = 5..6` parents (`ITA_ww1_anti_submarine_patrols` / `ITA_ww1_human_torpedoes`) and `ITA_ww1_vittorio_veneto` (`y = 6`) to `ITA_ww1_solstice_battle` (`y = 5`) and `ITA_ww1_piave_line` (`y = 4`) so that `1 <= dy <= 3` holds for 100% of prerequisite links.
   - Remove stale `common/national_focus/italy.txt.disabled`.
2. **Upgrade All 41 Shallow Focuses & Respect Balance Ceilings:**
   - Replace every shallow focus (`only PP/Stab/WS/XP/CP/vars/clamp`) with concrete rewards: building constructions (`industrial_complex`, `arms_factory`, `dockyard`, `infrastructure`, `bunker`, `coastal_bunker`, `naval_base`), equipment stockpiles (`infantry_equipment_1`, `artillery_equipment_1`, `support_equipment_1`), opinion modifiers, events, or the 18 previously unused national ideas!
   - Keep `total_pos_stab <= 0.15`, `total_pos_ws <= 0.20` (fixing `ITA_ww1_treaty_of_london` from `0.10` to `0.02` and shifting extra war support into `ITA_patto_di_londra_spirit`), single PP `<= 60`, and tech bonuses `<= 0.25` with unique names.
3. **Connect All Orphan Events:**
   - `ITA_ww1_british_friendship` or `ITA_ww1_british_coal` triggers `country_event = { id = ww1_italy.50 days = 1 }`.
   - `ITA_ww1_fiume_regency` (or `ww1_italy.62.a`) triggers `country_event = { id = ww1_italy.63 days = 2 }`.

---

## 4. Bilingual Localization & GFX Integrity (`localisation/` & `interface/`)
1. **Fix Missing Decision Textures (`interface/ww1_italy_decisions.gfx`):**
   - Replace non-existent `gfx/interface/decisions/decision_category_generic.dds` with existing `gfx/interface/decisions/ww1_italy/ITA_ww1_decision_1.dds`..`5.dds` and register sprites for all new decisions and the 9 restored ideas in `interface/ww1_italy_ideas.gfx`.
2. **100% Bilingual Localization Parity (`localisation/english/ww1_italy_l_english.yml` & `localisation/braz_por/ww1_italy_l_braz_por.yml`):**
   - Add English and Brazilian Portuguese titles and descriptions (`KEY:0` and `KEY_desc:0`) for all 9 restored ideas, all new map/strategic decisions, and custom tooltips.
   - Translate the identical EN/PT strings in `ww1_italy_l_braz_por.yml` (`Battaglione Aviatori` $\to$ `"Batalhão de Aviadores"`, `Corpo Aeronautico Militare` $\to$ `"Corpo Aeronáutico Militar"`, `Opera Nazionale Combattenti` $\to$ `"Obra Nacional dos Combatentes"`, `Saint-Jean-de-Maurienne` $\to$ `"Acordo de Saint-Jean-de-Maurienne"`, `Caporetto` $\to$ `"A Retirada de Caporetto"`, `Vittorio Veneto` $\to$ `"A Ofensiva de Vittorio Veneto"`).
   - Enforce strictly single UTF-8 BOM (`b"\xef\xbb\xbf"`).
