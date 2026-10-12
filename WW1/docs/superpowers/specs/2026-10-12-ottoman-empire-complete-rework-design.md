# Design Specification: Ottoman Empire (TUR) Complete WW1 Rework (1911–1920)

**Date:** 2026-10-12  
**Topic:** Complete Architectural, Visual, Mechanical, Narrative & Localization Overhaul of the Ottoman Empire (`TUR`)  
**Status:** DRAFT (Ready for Builder Check & Human Partner Review)

---

## 1. Intent and the "Why"

In 1911, the Ottoman Empire (*Devlet-i Aliyye-i Osmâniyye*) stands at the most dramatic crossroads of its six-hundred-year history. Labeled the "Sick Man of Europe," its finances are mortgaged to the Anglo-French *Administration de la Dette Publique Ottomane* (OPDA), its commercial sovereignty is crippled by foreign Capitulations, its army is torn between partisan factions, and its outlying provinces—from Tripolitania and the Balkans to Yemen and the Arab Vilayets—are on the verge of rebellion or foreign invasion. Yet between 1911 and 1918, the Empire shocked the world by holding off the Allied powers at Gallipoli (*Çanakkale*), capturing an entire British army at Kut al-Amara, fighting across the frozen peaks of the Caucasus, and marching into Baku.

Forensic auditing of the current Ottoman codebase revealed severe structural defects that break the player experience:
1. **Total Localization Failure (Double UTF-8 BOM):** Both `localisation/english/ww1_ottoman_l_english.yml` and `localisation/braz_por/ww1_ottoman_l_braz_por.yml` start with a duplicated UTF-8 BOM (`\xef\xbb\xbf\xef\xbb\xbf`), causing the Clausewitz C++ parser to reject line 1 (`l_braz_por:` / `l_english:`) and ignore 100% of the localization file in-game. Furthermore, 36 keys in the Portuguese file remain in English, 58 descriptions are copy-pasted generic placeholders, and events `15`, `20`, `25`, and `30` have mismatched titles/descriptions.
2. **27 Horizontal Focus Collisions & 12 Cross-Cutting Arrows:** In `common/national_focus/turkey.txt`, 27 pairs of focuses on the same `y` row are placed at `dx = 1` (overlapping banners in the UI), wings lack horizontal separation margins, and 12 prerequisite lines span `dy = 4–6` or `dx = 7` across unrelated branches.
3. **Hollow Mechanics & Dead Variables:** Four variables (`tur_imperial_cohesion`, `tur_arab_unrest`, `tur_foreign_influence`, `tur_public_debt`) are modified 187 times across focuses and events, but `tur_foreign_influence` and `tur_public_debt` are checked **zero times** (`checked = 0`), and **81 out of 256 focuses** grant only flat Political Power/Stability plus dead variable changes.
4. **Ghost Ideas, Invalid Modifiers & Disabled Commanders:** `history/countries/TUR - Turkey.txt` attempts to load 3 undefined ideas (`TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`); 6 country modifier tokens in `ww1_ottoman_ideas.txt` and `ww1_ottoman_decisions.txt` are invalid in Clausewitz (`compliance_growth_focus_factor`, `navy_surface_detection_factor`, `naval_strike_defence_factor`, `air_recon_factor`, `casualty_trickleback`); 3 events (`ww1_ottoman.23`, `.26`, `.29`) are orphaned; `TUR_mehmed_v` is assigned `ideology = nazism`; and iconic commanders (`TUR_ismail_enver_pasha`, `TUR_fakhri_pasha`, `TUR_halil_kut`) are omitted from recruitment.

This rework resolves every technical bug and elevates the Ottoman Empire to a flagship Major Power with map-based state securing mechanics, dynamic multi-stage debt liberation, tangible rewards across all 256 focuses, and zero visual collisions.

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
1. **100% Localization Integrity & Bilingual Richness:**
   - Fix the Double UTF-8 BOM so both `.yml` files begin with a single `\xef\xbb\xbf` followed immediately by `l_english:` or `l_braz_por:`.
   - Translate all 36 untranslated English keys in `ww1_ottoman_l_braz_por.yml` into authentic Brazilian Portuguese.
   - Replace all 58 generic copy-pasted descriptions (`"Reflete as realidades estruturais..."`, `"Aplica medidas operacionais..."`, `"Iniciativa estratégica..."`) with unique, historically grounded descriptions in both languages.
   - Synchronize all event localization keys (`ww1_ottoman.1` through `ww1_ottoman.32`) with their exact script definitions in `events/ww1_ottoman_events.txt`.
2. **Collision-Free 5-Wing Spatial Grid (`common/national_focus/turkey.txt`):**
   - Enforce `dx >= 2` between any two focuses on the same `y` coordinate across all 256 focuses (0 horizontal collisions).
   - Separate the 5 wings with clear horizontal buffer zones:
     - **Wing 1: Imperial Politics & Constitutional Destiny** (`x = 2` to `x = 34`) — 4 distinct sub-paths: CUP Triumvirate (`x = 2..8`), Liberal Entente (`x = 10..16`), Sultanic Prerogative (`x = 18..24`), Turco-Arab Federation (`x = 26..34`).
     - **Wing 2: Economic Sovereignty, OPDA Debt & Imperial Railways** (`x = 38` to `x = 60`).
     - **Wing 3: Armed Forces, Naval Bastion & Aviation** (`x = 64` to `x = 86`).
     - **Wing 4: Great Power Diplomacy & Pre-War Crises** (`x = 90` to `x = 112`).
     - **Wing 5: Operational War Theaters & 1918 Survival** (`x = 116` to `x = 140`).
   - Fix all 12 long-distance/cross-cutting prerequisite links so every parent-child arrow obeys `1 <= dy <= 3` and clean local column alignment.
3. **5-Pillar Dynamic National Spirit Architecture (Anti-Stacking):**
   - Define all missing starting ideas in `common/ideas/ww1_ottoman_ideas.txt` and manage transitions strictly via `swap_ideas`:
     - **Pillar 1 (Political Regime):** `TUR_second_constitutional_era` $\to$ `TUR_cup_vanguard_centralization` | `TUR_hurriyet_ve_itilaf_governance` | `TUR_palace_autocracy_restored` | `TUR_arab_ottoman_federal_compact`.
     - **Pillar 2 (OPDA Debt & Capitulations):** `TUR_sick_man_debt` (1911 start: `consumer_goods_factor = 0.20`, `political_power_gain = -0.15`, `industrial_capacity_factory = -0.15`, `production_speed_buildings_factor = -0.15`) $\to$ `TUR_debt_renegotiated` $\to$ `TUR_capitulations_abrogated` $\to$ `TUR_financial_sovereignty` (or `TUR_debt_default_crisis`).
     - **Pillar 3 (Military Modernization):** `TUR_army_modernization_struggle` (1911 start: `army_org_factor = -0.10`, `planning_speed = -0.15`, `army_artillery_attack_factor = -0.10`, `experience_loss_factor = 0.15`) $\to$ `TUR_reformed_ottoman_corps` $\to$ `TUR_german_military_mission` | `TUR_kemalist_tactical_doctrine`.
     - **Pillar 4 (Straits & Martial Tenacity):** `TUR_straits_fortress_cannons` (1911 start: `amphibious_invasion_defence = 0.15`, `production_speed_coastal_bunker_factor = 0.15`, `army_core_defence_factor = 0.05`) $\to$ `TUR_canakkale_impenetrable_bastion` (and `TUR_mehmetcik_tenacity`: `army_morale_factor = 0.08`, `out_of_supply_factor = -0.10`).
     - **Pillar 5 (Arab Vilayets & Internal Cohesion):** `TUR_arab_unrest_smoldering` (1911 start: `stability_factor = -0.12`, `non_core_manpower = -0.15`, `resistance_target = 0.15`) $\to$ `TUR_arab_revolt_insurgency` (if Revolt erupts) | `TUR_arab_ottoman_federal_compact` / `TUR_imperial_vilayets_pacified` (when resolved).
4. **Map-Based Arab Vilayets & Hejaz Railway Security Engine (`state_target = yes`):**
   - Interactive state-securing system in `common/decisions/ww1_ottoman_decisions.txt` targeting the 6 strategic Arab states owned by `TUR`:
     - **Hejaz / Medina** (`679`), **Asir-Makkah / Mecca** (`856`), **Syria / Damascus** (`554`), **Palestine / Jerusalem** (`454`), **Mesopotamia / Baghdad** (`291`), **Al Basrah** (`1011`).
   - **Anti-Cheese Concurrency & Strategic Cost:**
     - Only **one** security garrison operation (`TUR_deploy_hejaz_armored_garrison`) can run at a time (`NOT = { has_country_flag = TUR_securing_arab_vilayet_in_progress }`).
     - Costs **30 PP, 15,000 Manpower, and 400 Infantry Equipment** over **50 days**, forcing a direct strategic trade-off against the Caucasian, Gallipoli, and Balkan fronts.
     - Sets state flag `TUR_vilayet_garrison_secured` and lowers `tur_arab_unrest` by 10.
   - **Counter-Insurgency & Tribal Diplomacy:**
     - `TUR_teskilat_counter_insurgency_sweep` (`state_target = yes`): Costs 25 PP and 10 Command Power; roots out secret cells in the target state, lowering `tur_arab_unrest` by 8.
     - `TUR_subsidize_bedouin_sheikhs` (`state_target = yes`): Costs 25 PP and 1 Civilian Factory for 60 days; grants state flag `TUR_vilayet_tribes_subsidized` and lowers `tur_arab_unrest` by 8.
   - **The Great Arab Revolt Outbreak (`ww1_ottoman.19` & `ww1_ottoman.31`):**
     - When `TUR` is at war with `ENG` (after 1915.6.1 or `tur_arab_unrest >= 75`) and has not completed the Turco-Arab Federal Compact:
       - Secured states (`TUR_vilayet_garrison_secured`) remain firmly under Ottoman control with zero railway damage.
       - Unsecured Arab states suffer railway/infrastructure sabotage (`damage_building = { type = infrastructure damage = 2 }`), and if Hejaz (`679`) or Asir-Makkah (`856`) is unsecured, Pillar 5 swaps to `TUR_arab_revolt_insurgency` (`stability_factor = -0.20`, `attrition = 0.12`, `supply_consumption_factor = 0.15`, `non_core_manpower = -0.25`) until pacified via `TUR_crush_the_hejaz_insurgency` or federal compromise.
5. **Tangible Rewards for All 81 Hollow Focuses & Active Variable Mechanics:**
   - Every focus in `common/national_focus/turkey.txt` that previously gave only flat PP/Stability + variable increments must now grant concrete gameplay effects: state building constructions (`industrial_complex`, `arms_factory`, `infrastructure`, `bunker`, `coastal_bunker`, `naval_base`), equipment stockpiles (`infantry_equipment_1`, `artillery_equipment_1`, `support_equipment_1`), tech bonuses (`add_tech_bonus`), doctrine cost reductions, or idea upgrades (`swap_ideas`).
   - All 4 variables (`tur_imperial_cohesion`, `tur_arab_unrest`, `tur_foreign_influence`, `tur_public_debt`) are actively checked in decisions (`TUR_debt_and_capitulations_category`, `TUR_imperial_cohesion_category`) to unlock OPDA debt liquidation steps and cohesion bonuses.
6. **Clausewitz Semantic Oracle, Characters & Icon Diversity:**
   - Replace all 6 invalid modifier tokens so `hoi4_semantic_oracle.py` reports **0 errors** across `turkey.txt`, `ww1_ottoman_ideas.txt`, `ww1_ottoman_decisions.txt`, and `ww1_ottoman_events.txt`.
   - Fix `TUR_mehmed_v` ideology in `common/characters/TUR.txt` and ensure key historical commanders (`TUR_ismail_enver_pasha`, `TUR_mehmed_esad_pasha`, `TUR_hasan_tahsin_pasha`, `TUR_fakhri_pasha`, `TUR_halil_kut`, `TUR_cemal_pasha`, `TUR_talat_pasha`) are defined and recruited in `history/countries/TUR - Turkey.txt`.
   - Re-map overused focus icons in `interface/ww1_ottoman_goals.gfx` across the repository's 1,100+ available `.dds` goal textures so no single icon is spammed excessively.

### Non-Goals & Anti-Goals
- **Anti-Goal (No Broken Peace Conferences):** Never spawn an external rebel tag that joins the Entente or Central Powers without faction rules, avoiding un-annexable global peace conference bugs.
- **Anti-Goal (No Idea Spam):** Never exceed 6 concurrent persistent national spirits on `TUR`; always use `swap_ideas` for pillar progression and `add_timed_idea` for temporary operational boosts.
- **Anti-Goal (No Placeholder Text):** Zero occurrences of generic copy-paste localization strings or untranslated English keys in `ww1_ottoman_l_braz_por.yml`.

---

## 3. Technical Architecture & Exact Specifications

### A. 5-Wing Spatial Coordinate Table (`common/national_focus/turkey.txt`)
All 256 focuses preserve their exact IDs and prerequisite logic (with long-distance arrows fixed) while being mapped onto a strict non-colliding grid (`dx >= 2` on every `y` row):

| Wing | Root Focus ID | Root `(x, y)` | X-Axis Span | Columns Used |
|---|---|---|---|---|
| **Wing 1: Imperial Politics** | `TUR_second_constitutional_era_politics` | `(18, 0)` | `x = 2 .. 34` | Even columns (`2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34`) |
| **Wing 2: Economic Sovereignty** | `TUR_economic_sovereignty_drive` | `(48, 0)` | `x = 38 .. 58` | Even columns (`38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58`) |
| **Wing 3: Armed Forces & Straits** | `TUR_reorganizing_the_imperial_army` | `(74, 0)` | `x = 64 .. 84` | Even columns (`64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84`) |
| **Wing 4: Great Power Diplomacy** | `TUR_sublime_porte_foreign_policy` | `(100, 0)` | `x = 90 .. 110` | Even columns (`90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110`) |
| **Wing 5: War Theaters & 1918** | `TUR_the_war_for_imperial_survival` | `(128, 0)` | `x = 116 .. 140` | Even columns (`116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140`) |

> **Mathematical Guarantee:** By placing all parallel nodes strictly on **even X coordinates** (`2, 4, 6, ...`) or centered odd merge nodes where no neighbor exists within `±1`, `|x1 - x2| >= 2` is mathematically guaranteed across the entire 256-focus tree!

### B. Clausewitz Modifier Fixes (`ww1_ottoman_ideas.txt` & `ww1_ottoman_decisions.txt`)
1. `TUR_deploy_gendarmerie_sweep` (`ww1_ottoman_decisions.txt`): Replace `compliance_growth_focus_factor = 0.10` with `compliance_gain = 0.02`.
2. `TUR_arab_ottoman_federal_compact` (`ww1_ottoman_ideas.txt`): Replace `compliance_growth_focus_factor = 0.20` with `compliance_gain = 0.03`.
3. `TUR_yavuz_and_midilli_supremacy` (`ww1_ottoman_ideas.txt`): Replace `navy_surface_detection_factor = 0.15` with `spotting_chance = 0.15`.
4. `TUR_canakkale_impenetrable_bastion` (`ww1_ottoman_ideas.txt`): Replace `naval_strike_defence_factor = 0.20` with `defence = 0.05` and `army_core_defence_factor = 0.10`.
5. `TUR_ottoman_aviation_detachment` (`ww1_ottoman_ideas.txt`): Replace `air_recon_factor = 0.15` with `recon_factor = 0.10`.
6. `TUR_red_crescent_logistics` (`ww1_ottoman_ideas.txt`): Replace `casualty_trickleback = 0.10` with `experience_loss_factor = -0.10` and `attrition = -0.08`.

### C. Event Chain & Orphan Integration (`events/ww1_ottoman_events.txt`)
- Connect `ww1_ottoman.23` (Ascension of Mehmed VI), `ww1_ottoman.26` (Treaty of Da'an in Yemen), and `ww1_ottoman.29` (Misak-ı Millî National Pact) directly to their corresponding focuses (`TUR_legacy_of_osman_eternal`, `TUR_red_sea_desert_patrols`, `TUR_national_pact_misak_i_milli`) and decisions.
- Add `ww1_ottoman.31` (Outbreak of the Great Arab Revolt on the Map — checking secured vs unsecured states `679, 856, 554, 454, 291, 1011`) and `ww1_ottoman.32` (The Tripolitanian Resistance: Enver & Mustafa Kemal in Libya).

---

## 4. Verification & Acceptance Criteria
1. **Single UTF-8 BOM Verification:** Both `ww1_ottoman_l_english.yml` and `ww1_ottoman_l_braz_por.yml` start with `b'\xef\xbb\xbfl_english:'` and `b'\xef\xbb\xbfl_braz_por:'` (never double BOM).
2. **Zero Collisions Audit:** Every pair of focuses on the same `y` row in `common/national_focus/turkey.txt` has `|x1 - x2| >= 2`.
3. **Zero Hollow Focuses:** 0 focuses in `turkey.txt` have only flat PP/Stability + dead variables.
4. **Clausewitz Semantic Oracle:** `audit_file_modifiers` returns `0` errors across all Ottoman files.
5. **Master QA Suite (`tests/test_ww1_ottoman.py` & `scripts/qa_audit_all.py`):** 100% PASS with Exit Code 0.
