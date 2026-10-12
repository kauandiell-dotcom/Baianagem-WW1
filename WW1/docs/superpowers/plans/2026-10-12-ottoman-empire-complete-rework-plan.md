# Ottoman Empire (TUR) Complete WW1 Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the Ottoman Empire (`TUR`, 1911–1920) with a collision-free 256-focus 5-wing tree, tangible rewards on every focus, 5-pillar dynamic national ideas, map-based Arab Vilayet security & Hejaz Railway counter-insurgency mechanics, active OPDA debt liquidation, restored historical commanders, and 100% clean single-BOM bilingual localization.

**Architecture:** Eliminates the double UTF-8 BOM localization bug, maps all 256 focuses onto an even-column spatial grid (`dx >= 2`, `1 <= dy <= 3`), enforces 5-pillar anti-stacking `swap_ideas` transitions, introduces `state_target = yes` counter-insurgency decisions across the 6 Arab vilayets (`679, 856, 554, 454, 291, 1011`), connects all 4 imperial variables (`tur_imperial_cohesion`, `tur_arab_unrest`, `tur_foreign_influence`, `tur_public_debt`) to active decisions/events, and validates all modifiers against the Clausewitz Semantic Oracle.

**Tech Stack:** Clausewitz Script (Hearts of Iron IV v1.14+), Python 3 unittest & QA automation suites, Paradox YAML localization (Single UTF-8 BOM `\xef\xbb\xbf`).

**Spec:** `docs/superpowers/specs/2026-10-12-ottoman-empire-complete-rework-design.md`

## Global Constraints
- **Single UTF-8 BOM Mandatory:** `ww1_ottoman_l_english.yml` and `ww1_ottoman_l_braz_por.yml` must begin with exactly one `\xef\xbb\xbf` (never `\xef\xbb\xbf\xef\xbb\xbf`).
- **Spatial Grid Invariant:** Every pair of focuses sharing the same `y` coordinate in `common/national_focus/turkey.txt` must satisfy `|x1 - x2| >= 2`, and every parent-child prerequisite must satisfy `1 <= dy <= 3`.
- **Clausewitz Semantic Oracle:** 0 invalid modifier tokens allowed across `common/ideas/ww1_ottoman_ideas.txt`, `common/decisions/ww1_ottoman_decisions.txt`, `common/national_focus/turkey.txt`, and `events/ww1_ottoman_events.txt`.
- **Zero Hollow Focuses:** Every focus in `common/national_focus/turkey.txt` must grant tangible gameplay effects beyond flat PP/Stability/War Support and variable changes.
- **Zero Generic Copy-Paste Localization:** No repeated placeholder descriptions or untranslated English titles in `ww1_ottoman_l_braz_por.yml`.

## Review Focus
1. **Double BOM Prevention:** Writing with `encoding="utf-8-sig"` in Python automatically writes `\xef\xbb\xbf`; never prepend `"\ufeff"` to the string when using `utf-8-sig`, or verify raw bytes `raw[:3] == b"\xef\xbb\xbf" and raw[3:6] != b"\xef\xbb\xbf"`.
2. **Same-Row Focus Spacing (`dx >= 2`):** Any two focuses on the same `y` row with `dx < 2` overlap visually in the HOI4 UI; test must check all pairs on every `y` row.
3. **Starting & Event Idea Existence:** Every idea referenced in `history/countries/TUR - Turkey.txt`, `turkey.txt`, `ww1_ottoman_decisions.txt`, and `ww1_ottoman_events.txt` must exist in `common/ideas/ww1_ottoman_ideas.txt` and have a valid sprite in `interface/ww1_ottoman_ideas.gfx`.
4. **Event Localization Synchronization:** Event IDs `ww1_ottoman.1` through `ww1_ottoman.32` must match their exact titles, descriptions, and option keys in both English and Brazilian Portuguese.
5. **Orphan Event Elimination:** Every event with `is_triggered_only = yes` in `events/ww1_ottoman_events.txt` must be triggered by at least one focus, decision, or event.

---

### Task 1: Master QA Test Suite Expansion (`tests/test_ww1_ottoman.py` — RED Phase)

**Files:**
- Modify: `tests/test_ww1_ottoman.py`

**Interfaces:**
- Consumes: `scripts.hoi4_semantic_oracle.audit_file_modifiers`
- Produces: Expanded `OttomanContentReworkTests` asserting single BOM, `dx >= 2` spacing, `1 <= dy <= 3` links, 0 hollow focuses, 0 invalid Clausewitz modifiers, all starting/event ideas defined, state-securing Arab decisions, and 0 untranslated/copy-pasted localization strings.

- [ ] **Step 1: Expand `tests/test_ww1_ottoman.py` with comprehensive audit assertions**
  Add/update test methods in `OttomanContentReworkTests`:
  - `test_focus_count_and_coordinate_collisions`: Assert `len(self.foci) == 256`, unique `(x, y)`, AND for every `y` row, sorted `x` coordinates satisfy `x[i+1] - x[i] >= 2`.
  - `test_prerequisite_integrity_and_downward_progression`: Assert `1 <= data["y"] - py <= 3` for all parent-child links.
  - `test_zero_hollow_focuses`: Assert every focus in `turkey.txt` contains tangible rewards beyond flat `add_political_power`/`add_stability`/`add_war_support`/`add_to_variable`/`set_country_flag`.
  - `test_all_referenced_ideas_exist_and_oracle_clean`: Assert `TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood` exist in `common/ideas/ww1_ottoman_ideas.txt`, and `audit_file_modifiers` returns 0 errors on `ww1_ottoman_ideas.txt` and `ww1_ottoman_decisions.txt`.
  - `test_arab_vilayet_state_securing_and_opda_decisions`: Assert `TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`, `TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`, and `TUR_dispatch_officers_to_tripolitania` exist in `common/decisions/ww1_ottoman_decisions.txt`, and `ww1_ottoman.31` & `ww1_ottoman.32` exist in `events/ww1_ottoman_events.txt` with 0 orphan events.
  - `test_bilingual_localization_parity_and_utf8_bom`: Assert `en_bytes[:3] == b"\xef\xbb\xbf"` and `en_bytes[3:6] != b"\xef\xbb\xbf"`, `pt_bytes[:3] == b"\xef\xbb\xbf"` and `pt_bytes[3:6] != b"\xef\xbb\xbf"`, 0 generic placeholder descriptions (`"Reflete as realidades estruturais"` or `"Aplica medidas operacionais"`), and 0 untranslated decision/idea titles in `ww1_ottoman_l_braz_por.yml`.

- [ ] **Step 2: Run test suite to verify RED failure**
  Run: `python -m unittest tests/test_ww1_ottoman.py`
  Expected: FAIL on double BOM, horizontal collisions, missing ideas, oracle errors, missing decisions/events, hollow focuses, and generic localization.

- [ ] **Step 3: Commit RED test suite**
  ```bash
  git add tests/test_ww1_ottoman.py
  git commit -m "test(tur): expand Ottoman QA test suite for complete rework (RED)"
  ```

---

### Task 2: 5-Pillar National Ideas, Semantic Oracle Fixes, GFX & Historical Characters

**Files:**
- Modify: `common/ideas/ww1_ottoman_ideas.txt`
- Modify: `interface/ww1_ottoman_ideas.gfx`
- Modify: `common/characters/TUR.txt`
- Modify: `history/countries/TUR - Turkey.txt`

**Interfaces:**
- Consumes: Valid modifier tokens from `data/hoi4_valid_country_modifiers.json`
- Produces: Complete 5-Pillar Ottoman ideas (`TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood`), 0 Oracle errors in `ww1_ottoman_ideas.txt`, valid idea GFX sprites, and historical commanders recruited in `TUR - Turkey.txt`.

- [ ] **Step 1: Fix 5 invalid Clausewitz modifiers in `common/ideas/ww1_ottoman_ideas.txt`**
  - In `TUR_arab_ottoman_federal_compact`: replace `compliance_growth_focus_factor = 0.20` with `compliance_gain = 0.03`.
  - In `TUR_yavuz_and_midilli_supremacy`: replace `navy_surface_detection_factor = 0.15` with `spotting_chance = 0.15`.
  - In `TUR_canakkale_impenetrable_bastion`: replace `naval_strike_defence_factor = 0.20` with `army_core_defence_factor = 0.10`.
  - In `TUR_ottoman_aviation_detachment`: replace `air_recon_factor = 0.15` with `recon_factor = 0.10`.
  - In `TUR_red_crescent_logistics`: replace `casualty_trickleback = 0.10` with `experience_loss_factor = -0.10` and `attrition = -0.08`.

- [ ] **Step 2: Add missing starting & dynamic ideas to `common/ideas/ww1_ottoman_ideas.txt` and `interface/ww1_ottoman_ideas.gfx`**
  - `TUR_sick_man_debt`: `consumer_goods_factor = 0.20`, `political_power_gain = -0.15`, `industrial_capacity_factory = -0.15`, `production_speed_buildings_factor = -0.15`.
  - `TUR_mehmetcik_tenacity`: `army_morale_factor = 0.08`, `out_of_supply_factor = -0.10`, `army_core_defence_factor = 0.05`.
  - `TUR_straits_fortress_cannons`: `amphibious_invasion_defence = 0.15`, `production_speed_coastal_bunker_factor = 0.15`.
  - `TUR_caliphate_global_banner`: `war_support_factor = 0.15`, `conscription_factor = 0.10`, `army_morale_factor = 0.10`.
  - `TUR_arab_revolt_insurgency`: `stability_factor = -0.20`, `attrition = 0.12`, `supply_consumption_factor = 0.15`, `non_core_manpower = -0.25`.
  - `TUR_imperial_vilayets_pacified`: `stability_factor = 0.10`, `non_core_manpower = 0.15`, `resistance_target = -0.20`.
  - `TUR_senussi_desert_brotherhood`: `attrition = -0.10`, `out_of_supply_factor = -0.15`, `army_morale_factor = 0.05`.
  - Register `GFX_idea_TUR_...` sprites for each new idea in `interface/ww1_ottoman_ideas.gfx` pointing to existing textures in `gfx/interface/ideas/TUR/`.

- [ ] **Step 3: Fix `common/characters/TUR.txt` and `history/countries/TUR - Turkey.txt`**
  - In `common/characters/TUR.txt`: change `TUR_mehmed_v` fascism country_leader `ideology=nazism` to `ideology=rexism` or keep `despotism` and add `TUR_ismail_enver_pasha` as `fascism_ideology` leader; ensure `TUR_fakhri_pasha` and `TUR_halil_kut` exist as `corps_commander`.
  - In `history/countries/TUR - Turkey.txt`: recruit `TUR_ismail_enver_pasha`, `TUR_mehmed_esad_pasha`, `TUR_hasan_tahsin_pasha`, `TUR_fakhri_pasha`, and `TUR_halil_kut`.

- [ ] **Step 4: Verify Oracle & Idea Tests**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_ottoman_ideas.txt')) == 0"`
  Expected: Exit code 0.

- [ ] **Step 5: Commit changes**
  ```bash
  git add common/ideas/ww1_ottoman_ideas.txt interface/ww1_ottoman_ideas.gfx common/characters/TUR.txt "history/countries/TUR - Turkey.txt"
  git commit -m "feat(tur): implement 5-pillar Ottoman ideas, fix invalid modifiers, and restore historical commanders"
  ```

---

### Task 3: Map-Based Arab Vilayet Security Engine & Dynamic OPDA Debt Decisions

**Files:**
- Modify: `common/decisions/ww1_ottoman_decisions.txt`
- Modify: `common/decisions/categories/ww1_ottoman_decision_categories.txt`

**Interfaces:**
- Consumes: States `679, 856, 554, 454, 291, 1011`, variables `tur_imperial_cohesion`, `tur_arab_unrest`, `tur_foreign_influence`, `tur_public_debt`, Pillar 2 & Pillar 5 ideas.
- Produces: State-targeted Arab security decisions (`TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`), active OPDA debt liquidation decisions (`TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`), and Libyan resistance decision (`TUR_dispatch_officers_to_tripolitania`).

- [ ] **Step 1: Fix invalid modifier in `TUR_deploy_gendarmerie_sweep`**
  Replace `compliance_growth_focus_factor = 0.10` with `compliance_gain = 0.02`.

- [ ] **Step 2: Add Map-Based Arab Vilayet Security Decisions (`state_target = yes`) in `TUR_imperial_cohesion_category`**
  Target owned states in `{ 679 856 554 454 291 1011 }`:
  - `TUR_deploy_hejaz_armored_garrison`:
    - `state_target = yes`, `target_array = owned_states`
    - `target_trigger = { FROM = { is_owned_by = ROOT OR = { state = 679 state = 856 state = 554 state = 454 state = 291 state = 1011 } NOT = { has_state_flag = TUR_vilayet_garrison_secured } } }`
    - `available = { NOT = { has_country_flag = TUR_securing_arab_vilayet_in_progress } has_manpower > 15000 has_equipment = { type = infantry_equipment_1 amount > 400 } }`
    - `cost = 30`, `days_remove = 50`
    - `complete_effect`: sets `TUR_securing_arab_vilayet_in_progress`, deducts 15,000 manpower and 400 infantry rifles.
    - `remove_effect`: clears `TUR_securing_arab_vilayet_in_progress`, sets state flag `TUR_vilayet_garrison_secured`, `add_to_variable = { tur_arab_unrest = -10 }`, `add_to_variable = { tur_imperial_cohesion = 5 }`.
  - `TUR_teskilat_counter_insurgency_sweep`:
    - `state_target = yes` for `{ 679 856 554 454 291 1011 }`, costs 25 PP and 10 Command Power, `days_re_enable = 90`, lowers `tur_arab_unrest` by 8.
  - `TUR_subsidize_bedouin_sheikhs`:
    - `state_target = yes` for `{ 679 856 554 454 291 1011 }`, costs 25 PP, `civilian_factory_use = 1`, `days_remove = 60`, sets state flag `TUR_vilayet_tribes_subsidized`, lowers `tur_arab_unrest` by 8.
  - `TUR_pacify_arab_insurgency_campaign`:
    - Available when `has_idea = TUR_arab_revolt_insurgency` and states `679` and `554` have `TUR_vilayet_garrison_secured`; swaps `TUR_arab_revolt_insurgency` to `TUR_imperial_vilayets_pacified`.

- [ ] **Step 3: Add Active OPDA Debt & Foreign Influence Decisions in `TUR_debt_and_capitulations_category` and Libyan Decision in `TUR_war_theaters_category`**
  - `TUR_liquidate_opda_debt_tranche`: Checks `check_variable = { tur_public_debt > 15 }`, costs 45 PP, `days_re_enable = 120`, reduces `tur_public_debt` by 15 and `tur_foreign_influence` by 10; if `tur_public_debt < 40` and `has_idea = TUR_sick_man_debt`, swaps to `TUR_debt_renegotiated`.
  - `TUR_curb_foreign_consular_courts`: Checks `check_variable = { tur_foreign_influence > 15 }`, costs 35 PP, `days_re_enable = 120`, reduces `tur_foreign_influence` by 15, grants `add_stability = 0.04` and `add_political_power = 40`.
  - `TUR_dispatch_officers_to_tripolitania`: In `TUR_war_theaters_category`, costs 25 PP, `fire_only_once = yes`, triggers `country_event = { id = ww1_ottoman.32 }`.

- [ ] **Step 4: Verify Semantic Oracle on `ww1_ottoman_decisions.txt`**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/decisions/ww1_ottoman_decisions.txt')) == 0"`
  Expected: Exit code 0.

- [ ] **Step 5: Commit changes**
  ```bash
  git add common/decisions/ww1_ottoman_decisions.txt common/decisions/categories/ww1_ottoman_decision_categories.txt
  git commit -m "feat(tur): implement map-based Arab vilayet security engine and active OPDA debt decisions"
  ```

---

### Task 4: Historical Events Overhaul, Great Arab Revolt & Libyan Resistance (`events/ww1_ottoman_events.txt`)

**Files:**
- Modify: `events/ww1_ottoman_events.txt`

**Interfaces:**
- Consumes: State flags `TUR_vilayet_garrison_secured`, ideas `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood`.
- Produces: Overhauled `ww1_ottoman.19`, new `ww1_ottoman.31` (Great Arab Revolt Map Eruption), and new `ww1_ottoman.32` (Tripolitanian Resistance).

- [ ] **Step 1: Upgrade `ww1_ottoman.19` and implement `ww1_ottoman.31` (Territorial Eruption of the Great Arab Revolt)**
  - In `ww1_ottoman.19`, Option A triggers follow-up `country_event = { id = ww1_ottoman.31 days = 5 }`.
  - In `ww1_ottoman.31`:
    - Checks each Arab state (`679, 856, 554, 454, 291, 1011`):
      - If state does NOT have `TUR_vilayet_garrison_secured`, damages infrastructure (`damage_building = { type = infrastructure damage = 2 }`).
    - If `679` (Hejaz) or `856` (Asir-Makkah) is NOT secured, swaps `TUR_arab_unrest_smoldering` to `TUR_arab_revolt_insurgency` and inflicts `-10,000` manpower & `-500` rifles from desert raids.
    - If both `679` and `856` ARE secured (`has_state_flag = TUR_vilayet_garrison_secured`), the revolt is crushed immediately, swapping `TUR_arab_unrest_smoldering` to `TUR_imperial_vilayets_pacified` and granting `+0.10` stability and `+25` army experience!

- [ ] **Step 2: Implement `ww1_ottoman.32` (The Tripolitanian Resistance: Enver & Mustafa Kemal in Libya)**
  - Triggered by decision `TUR_dispatch_officers_to_tripolitania` or focus `TUR_tripoli_coastal_fortifications`.
  - Option A (Send Enver Bey, Mustafa Kemal & Mauser Rifles to Derna and Tobruk): adds idea `TUR_senussi_desert_brotherhood`, adds level 1 coastal bunker/bunker in `448` (Tripoli) and `450` (Benghazi), grants `+25` army experience and `+0.05` war support.
  - Option B (Focus Reserves on the Balkan Frontier): grants `+50` PP, `+10,000` manpower, and fortifies Edirne (`341`).

- [ ] **Step 3: Commit changes**
  ```bash
  git add events/ww1_ottoman_events.txt
  git commit -m "feat(tur): implement territorial Arab Revolt escalation and Libyan resistance events"
  ```

---

### Task 5: 5-Wing Focus Tree Spatial Reconstruction, Tangible Rewards & Icon Diversity

**Files:**
- Modify: `common/national_focus/turkey.txt`
- Modify: `interface/ww1_ottoman_goals.gfx`

**Interfaces:**
- Consumes: All 256 focus IDs, events `ww1_ottoman.1`–`ww1_ottoman.32`, 5-Pillar ideas, `.dds` goal textures.
- Produces: Collision-free `common/national_focus/turkey.txt` (`dx >= 2` on every row, `1 <= dy <= 3` on every link, 0 hollow focuses, 0 orphan events) and diversified `interface/ww1_ottoman_goals.gfx`.

- [ ] **Step 1: Reconstruct 5-Wing Spatial Coordinates in `common/national_focus/turkey.txt`**
  - Remap all 256 focuses onto non-colliding coordinates (`dx >= 2` between any two focuses on the same `y` row):
    - Wing 1 (Politics): `x = 2 .. 34`, Root at `(18, 0)`
    - Wing 2 (Economy & Railways): `x = 38 .. 58`, Root at `(48, 0)`
    - Wing 3 (Armed Forces & Straits): `x = 64 .. 84`, Root at `(74, 0)`
    - Wing 4 (Great Power Diplomacy): `x = 90 .. 110`, Root at `(100, 0)`
    - Wing 5 (War Theaters & 1918): `x = 116 .. 140`, Root at `(128, 0)`
  - Fix the 12 long-distance prerequisite links so every parent-child link satisfies `1 <= dy <= 3` (moving capstone focuses or using intermediate prerequisites/flags where needed).

- [ ] **Step 2: Upgrade all 81 hollow focuses with tangible rewards and connect orphan events**
  - Ensure `ww1_ottoman.23`, `ww1_ottoman.26`, and `ww1_ottoman.29` are triggered by focuses (`TUR_legacy_of_osman_eternal`, `TUR_red_sea_desert_patrols`, `TUR_national_pact_misak_i_milli`).
  - Ensure `TUR_audit_opda_administration`, `TUR_renegotiate_creditor_coupons`, `TUR_unilateral_abrogation_of_capitulations`, and `TUR_complete_fiscal_liberation` perform clean `swap_ideas` transitions along Pillar 2 (`TUR_sick_man_debt` $\to$ `TUR_debt_renegotiated` $\to$ `TUR_capitulations_abrogated` $\to$ `TUR_financial_sovereignty`).
  - Add concrete rewards (infrastructure/factories/bunkers/stockpiles/tech bonuses/timed ideas) to every focus that previously only gave flat PP/Stability/War Support + variable changes.

- [ ] **Step 3: Diversify focus goal icons in `interface/ww1_ottoman_goals.gfx`**
  - Distribute texture mappings across available `.dds` files in `gfx/interface/goals/` so no single texture is used more than 12 times across the 256 focuses.

- [ ] **Step 4: Commit changes**
  ```bash
  git add common/national_focus/turkey.txt interface/ww1_ottoman_goals.gfx
  git commit -m "feat(tur): reconstruct 5-wing non-colliding focus grid, enrich 81 focus rewards, and diversify icons"
  ```

---

### Task 6: Complete Bilingual Localization & Single UTF-8 BOM (`localisation/`)

**Files:**
- Modify: `localisation/english/ww1_ottoman_l_english.yml`
- Modify: `localisation/braz_por/ww1_ottoman_l_braz_por.yml`

**Interfaces:**
- Consumes: All 256 focus IDs, all ideas in `ww1_ottoman_ideas.txt`, all decisions in `ww1_ottoman_decisions.txt`, and all 32 events in `ww1_ottoman_events.txt`.
- Produces: 100% synchronized, single-BOM (`\xef\xbb\xbf`) English and Brazilian Portuguese localization files with 0 untranslated strings and 0 generic copy-paste descriptions.

- [ ] **Step 1: Fix Double UTF-8 BOM and Synchronize Event Keys (`ww1_ottoman.1`–`ww1_ottoman.32`)**
  - Ensure every event `ww1_ottoman.1` through `ww1_ottoman.32` has exact matching `.t`, `.d`, `.a`, `.b` keys in both files matching the script in `events/ww1_ottoman_events.txt`.

- [ ] **Step 2: Translate all 36 English Titles in `ww1_ottoman_l_braz_por.yml` and Replace All 58 Generic Descriptions**
  - Translate all decision and idea titles in `ww1_ottoman_l_braz_por.yml` into authentic Brazilian Portuguese.
  - Replace every instance of `"Reflete as realidades estruturais e esforços administrativos do Estado Otomano."`, `"Aplica medidas operacionais especializadas para a defesa e prosperidade do império."`, and `"Iniciativa estratégica entra em vigor nos territórios imperiais pertinentes."` (and their English counterparts) with unique historical descriptions.
  - Add localization keys for all new ideas (`TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood`), decisions (`TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`, `TUR_pacify_arab_insurgency_campaign`, `TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`, `TUR_dispatch_officers_to_tripolitania`), and events (`ww1_ottoman.31`, `ww1_ottoman.32`).

- [ ] **Step 3: Verify Single UTF-8 BOM Byte Prefix**
  Run: `python -c "for p in ['localisation/english/ww1_ottoman_l_english.yml', 'localisation/braz_por/ww1_ottoman_l_braz_por.yml']: b = open(p, 'rb').read(6); assert b[:3] == b'\xef\xbb\xbf' and b[3:6] != b'\xef\xbb\xbf', f'Bad BOM in {p}: {b}'"`
  Expected: Exit code 0.

- [ ] **Step 4: Commit changes**
  ```bash
  git add localisation/english/ww1_ottoman_l_english.yml localisation/braz_por/ww1_ottoman_l_braz_por.yml
  git commit -m "feat(tur): fix double UTF-8 BOM bug and provide 100% bespoke bilingual Ottoman localization"
  ```

---

### Task 7: Master QA Verification & Full Audit (GREEN Phase)

**Files:**
- Test: `tests/test_ww1_ottoman.py`
- Test: `scripts/qa_audit_all.py`

- [ ] **Step 1: Run Ottoman Complete Test Suite**
  Run: `python -m unittest tests/test_ww1_ottoman.py -v`
  Expected: All tests PASS (Exit code 0).

- [ ] **Step 2: Run Master QA Audit Suite**
  Run: `python scripts/qa_audit_all.py`
  Expected: All tiers and unit test suites PASS with 0 issues (Exit code 0).
