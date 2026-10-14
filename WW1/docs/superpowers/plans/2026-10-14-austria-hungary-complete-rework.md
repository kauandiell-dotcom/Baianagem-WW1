# Austria-Hungary Complete Rework, The 4 Constitutional Destinies & The Dynamic Fragmentation System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Overhaul the Austro-Hungarian Monarchy (`AUS`) in *Baianagem-WW1* (1911–1923), implementing 4 authentic constitutional paths (Dualism, Trialism, Danubian Mega-Federation, AOK Military Dictatorship), a live Crown Dashboard with grain stockpiles and war weariness, a real multi-tag Mega-Federation with unified imperial map colors and 4–18 division spawns, tag-safe scripted collapse and reunification wars, historical industrial and military giants (Škoda 30.5cm, Steyr, Conrad vs Boroević), pre-war espionage (Colonel Redl), and single-BOM bilingual localization.

**Architecture:** A robust Clausewitz script architecture driven by a 3-vector simulation (`AUH_war_weariness`, `AUH_cohesion`, `AUH_vienna_grain`), cleanly integrated into `common/national_focus/austria.txt`. The Danubian Mega-Federation spawns real constituent nations (`HUN`, `CZE`, `CRO`, `POL`) on the map with shared imperial cosmetic colors (`rgb { 202 198 188 }`), custom subject spirits siphoning 75% of factories and manpower to Vienna, and 4–18 divisions per member. Secessions are strictly gated behind active war (`has_war = yes`), core state losses, and weariness thresholds, using fixed tags with `can_join_factions = no` to prevent broken peace conferences or world war cascades.

**Tech Stack:** Paradox Clausewitz Script, HOI4 Engine Defines, Python 3.10+ (for `unittest`, `scripts/qa_audit_all.py`, and `scripts/hoi4_semantic_oracle.py`), YAML (single UTF-8 BOM `\xef\xbb\xbf` for English & Brazilian Portuguese).

**Spec:** `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`

## Global Constraints

- **Clausewitz Syntax Integrity:** 100% balanced brackets across all modified `.txt` and `.lua` files (Diff = 0).
- **Zero Day 1 Premature Crises:** All collapse, secession, or rebellion events strictly require `has_war = yes`, date > 1915.1.1, core state checks (`controls_state = 4` for Vienna), and high surrender progress (`> 0.40`).
- **Faction Lockdown on Secessionists:** All breakaway tags (`CZE`, `HUN`, `CRO`) must execute `set_rule = { can_join_factions = no }` and AI strategies forbidding faction alliances.
- **Zero Dynamic Clones:** Absolutely zero `start_civil_war` dynamic tag generation (no `D01/D02`).
- **Visual Uniformity in Federation:** All federal constituent tags receive cosmetic tags matching Austria's imperial map color (`rgb { 202 198 188 }`).
- **High Centralization Guarantee:** Custom autonomy/spirit siphons 75% of civilian and military factories and up to 70% subject manpower pool to Vienna; subject states retain 25% factories and sufficient manpower to maintain territorial forces.
- **Audited Semantic Modifiers:** 100% of modifiers must exist in `data/hoi4_valid_country_modifiers.json` verified via `scripts/hoi4_semantic_oracle.py`.
- **Localization BOM & Parity:** Strictly single UTF-8 BOM (`\xef\xbb\xbf`) on both `l_english.yml` and `l_braz_por.yml`, with 100% key parity and zero double-BOM (`\xef\xbb\xbf\xef\xbb\xbf`).
- **Steam Workshop Mirroring:** Synchronize all changes to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus

1. **Day 1 Crisis Prevention:** Event triggers evaluating TRUE in 1911 peacetime causing early collapse or civil war. *Expectation:* Triggers must evaluate FALSE until 1915 with active war and core state losses.
2. **Entente Diplomatic Leak:** Breakaway rebel tags (`CZE`, `HUN`, `CRO`) joining the Entente faction and turning an internal imperial crisis into an unresolvable world war conference. *Expectation:* Scripted `can_join_factions = no` and anti-faction AI rules prevent all faction entry.
3. **Overlord Economic Depletion in Federation:** Releasing federal member states stripping Vienna of industry and manpower, crippling the player/AI during WW1. *Expectation:* `AUH_danubian_federal_member` transfers 75% factory output and 70% manpower back to Vienna.
4. **Focus Grid Coordinate Collisions:** New or modified focuses overlapping coordinates or having broken prerequisites. *Expectation:* `scripts/mod_engine.py` validates `abs(x2 - x1) >= 2` for same-row focuses and `1 <= dy <= 3` for prerequisite links.
5. **Localization Encoding Corruption:** Double UTF-8 BOMs or missing localization keys producing raw strings like `AUH_skoda_305_howitzer` in the UI. *Expectation:* Single BOM validator and key parity check in unit tests confirm 100% coverage.

---

### Task 1: QA RED Test Baseline (`tests/test_ww1_austria_hungary.py`)

**Files:**
- Create: `tests/test_ww1_austria_hungary.py`
- Modify: `scripts/qa_audit_all.py`
- Test: `tests/test_ww1_austria_hungary.py`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Produces: Test class `TestAustriaHungaryOverhaul` with 7 comprehensive test methods to drive TDD.

- [ ] **Step 1: Write the failing test suite `tests/test_ww1_austria_hungary.py`**
  ```python
  import os
  import re
  import unittest

  REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  class TestAustriaHungaryOverhaul(unittest.TestCase):
      def test_austria_no_day1_crisis(self):
          """Verify that collapse and crisis events cannot trigger on Day 1 (1911)."""
          ...
      def test_constitutional_four_paths(self):
          """Verify that the 4 constitutional paths (Dualism, Trialism, Danubian Mega-Federation, Military Dictatorship) are properly defined and mutually exclusive."""
          ...
      def test_danubian_mega_federation_setup(self):
          """Verify that Danubian federation releases HUN, CZE, CRO, POL with imperial color matching and 4-18 divisions."""
          ...
      def test_tag_safe_breakaway_rules(self):
          """Verify that seceding tags have can_join_factions = no and 0 dynamic start_civil_war calls."""
          ...
      def test_crown_dashboard_and_grain(self):
          """Verify the 3 survival vectors (weariness, cohesion, grain) and their decisions."""
          ...
      def test_skoda_and_three_armies_modifiers(self):
          """Verify that all ideas use valid Clausewitz modifiers via semantic oracle."""
          ...
      def test_localisation_bom_and_parity(self):
          """Verify single UTF-8 BOM and 100% key parity between English and Portuguese."""
          ...
  ```

- [ ] **Step 2: Run test to verify it fails (RED phase)**
  Run: `python -m unittest tests.test_ww1_austria_hungary -v`
  Expected: FAIL on unbuilt components.

- [ ] **Step 3: Register test suite in `scripts/qa_audit_all.py` as Suite 12**
  Add `tests.test_ww1_austria_hungary` to the test runner array in `scripts/qa_audit_all.py`.

- [ ] **Step 4: Verify test runner executes `test_ww1_austria_hungary`**
  Run: `python scripts/qa_audit_all.py`
  Expected: Suite 12 fails with expected missing features.

- [ ] **Step 5: Commit**
  ```bash
  git add tests/test_ww1_austria_hungary.py scripts/qa_audit_all.py
  git commit -m "test(auh): establish RED QA test suite for Austria-Hungary complete rework"
  ```

---

### Task 2: The Crown Dashboard & The 3 Survival Vectors

**Files:**
- Create: `common/scripted_effects/ww1_auh_dashboard_effects.txt`
- Create: `common/decisions/categories/ww1_auh_dashboard_categories.txt`
- Create: `common/decisions/ww1_auh_dashboard_decisions.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_crown_dashboard_and_grain`

**Interfaces:**
- Consumes: Task 1 test assertions.
- Produces: `AUH_war_weariness`, `AUH_cohesion`, and `AUH_vienna_grain` simulation variables, clamped between 0 and 100, managed via imperial decisions.

- [ ] **Step 1: Write test assertions in `test_crown_dashboard_and_grain`**
  Assert files exist, variables `AUH_war_weariness`, `AUH_cohesion`, and `AUH_vienna_grain` are referenced in scripted effects, and fast-failing tag checks `allowed = { original_tag = AUS }` are present.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_crown_dashboard_and_grain -v`
  Expected: FAIL.

- [ ] **Step 3: Implement Crown Dashboard effects and decisions**
  - In `common/scripted_effects/ww1_auh_dashboard_effects.txt`:
    - `AUH_init_crown_dashboard`: sets `AUH_cohesion = 65`, `AUH_vienna_grain = 70`, `AUH_war_weariness = 0`.
    - `AUH_clamp_dashboard_variables`: clamps each variable between 0 and 100.
    - `AUH_weekly_grain_tick`: if at war, reduces grain by 1 unless rationed or supplemented.
  - In `common/decisions/categories/ww1_auh_dashboard_categories.txt`:
    - Category `AUH_crown_dashboard` with `allowed = { original_tag = AUS }`.
  - In `common/decisions/ww1_auh_dashboard_decisions.txt`:
    - Decisions: `AUH_dec_requisition_banat_grain`, `AUH_dec_bread_rationing_cards`, `AUH_dec_appease_budapest_diet`, `AUH_dec_galician_food_corps`.
  - In `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`:
    - Hook `AUH_clamp_dashboard_variables = yes` into `on_weekly`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_crown_dashboard_and_grain -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/scripted_effects/ww1_auh_dashboard_effects.txt common/decisions/categories/ww1_auh_dashboard_categories.txt common/decisions/ww1_auh_dashboard_decisions.txt common/on_actions/
  git commit -m "feat(auh): implement Crown Dashboard, Vienna grain stockpiles, and 3 survival vectors"
  ```

---

### Task 3: The 4 Divergent Constitutional Destinies & Focus Tree Overhaul

**Files:**
- Modify: `common/national_focus/austria.txt`
- Create: `common/ideas/ww1_austria_constitutional_ideas.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_constitutional_four_paths`

**Interfaces:**
- Consumes: Focus grid topology standards from `hoi4-focus-tree-designer` skill.
- Produces: 4 mutually exclusive constitutional branches: Dualism of Iron (`AUH_ww1_dualism`), Habsburg Trialism (`AUH_ww1_trialism`), Danubian Mega-Federation (`AUH_ww1_federalism`), and AOK Military Dictatorship (`AUH_ww1_military_dictatorship`).

- [ ] **Step 1: Write test assertions in `test_constitutional_four_paths`**
  Assert `AUH_ww1_dualism`, `AUH_ww1_trialism`, `AUH_ww1_federalism`, and `AUH_ww1_military_dictatorship` exist in `common/national_focus/austria.txt`, are mutually exclusive, have distinct valid ideas (`AUH_idea_dualism_iron`, `AUH_idea_habsburg_trialism`, `AUH_idea_danubian_federation_spirit`, `AUH_idea_aok_military_dictatorship`), and have 0 coordinate collisions.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_constitutional_four_paths -v`
  Expected: FAIL (`AUH_ww1_military_dictatorship` not found or mutual exclusivity incomplete).

- [ ] **Step 3: Implement the 4 constitutional branches and national ideas**
  - In `common/national_focus/austria.txt`:
    - Restructure the political opening under `AUH_ww1_constitutional_audit`.
    - Branch 1: `AUH_ww1_dualism` -> `AUH_ww1_tisza_alliance` -> `AUH_ww1_magyar_cavalry_corps`.
    - Branch 2: `AUH_ww1_trialism` -> `AUH_ww1_zagreb_coronation` -> `AUH_ww1_pacify_south_slavs`.
    - Branch 3: `AUH_ww1_federalism` -> `AUH_ww1_popovici_manifesto` -> `AUH_ww1_proclaim_danubian_federation`.
    - Branch 4: `AUH_ww1_military_dictatorship` -> `AUH_ww1_conrad_supreme_command` -> `AUH_ww1_war_surveillance_office`.
    - Set mutual exclusivity across all 4 branches.
  - In `common/ideas/ww1_austria_constitutional_ideas.txt`:
    - Define ideas with verified Clausewitz modifiers from `data/hoi4_valid_country_modifiers.json`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_constitutional_four_paths -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/national_focus/austria.txt common/ideas/ww1_austria_constitutional_ideas.txt
  git commit -m "feat(auh): implement 4 divergent constitutional paths and authentic national ideas"
  ```

---

### Task 4: Real Danubian Mega-Federation Engine, Uniform Map Color & Division Spawners

**Files:**
- Create: `common/scripted_effects/ww1_danubian_federation_effects.txt`
- Modify: `common/countries/cosmetic.txt`
- Create: `history/units/AUH_hun_federal.txt`
- Create: `history/units/AUH_cze_federal.txt`
- Create: `history/units/AUH_cro_federal.txt`
- Create: `history/units/AUH_pol_federal.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_danubian_mega_federation_setup`

**Interfaces:**
- Consumes: Focus `AUH_ww1_proclaim_danubian_federation` from Task 3.
- Produces: Tag-safe multi-country spawner releasing `HUN`, `CZE`, `CRO`, `POL`, setting imperial cosmetic tags (`color = rgb { 202 198 188 }`), adding high-centralization subject spirits (`AUH_danubian_federal_member`), and spawning historical 4–18 divisions per member.

- [ ] **Step 1: Write test assertions in `test_danubian_mega_federation_setup`**
  Assert `ww1_danubian_federation_effects.txt` exists, defines `AUH_spawn_danubian_mega_federation`, references tags `HUN`, `CZE`, `CRO`, `POL`, assigns cosmetic tags sharing `rgb { 202 198 188 }`, loads federal unit files, and assigns `AUH_danubian_federal_member`.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_danubian_mega_federation_setup -v`
  Expected: FAIL.

- [ ] **Step 3: Implement Danubian Mega-Federation release and division spawners**
  - In `common/scripted_effects/ww1_danubian_federation_effects.txt`:
    - `AUH_spawn_danubian_mega_federation`:
      - Releases `HUN` with core states (43, 44, 45, etc.), sets cosmetic tag `HUN_AUS_danubian_state`, sets puppet/subject status, applies `AUH_danubian_federal_member`, spawns `history/units/AUH_hun_federal.txt` (16 divisions).
      - Releases `CZE` with core states (9, 69), sets cosmetic tag `CZE_AUS_danubian_state`, applies `AUH_danubian_federal_member`, spawns `history/units/AUH_cze_federal.txt` (10 divisions).
      - Releases `CRO` with core states (109, 108, 163, 164), sets cosmetic tag `CRO_AUS_danubian_state`, applies `AUH_danubian_federal_member`, spawns `history/units/AUH_cro_federal.txt` (6 divisions).
      - Releases `POL` with Galicia (88, 89), sets cosmetic tag `POL_AUS_danubian_state`, applies `AUH_danubian_federal_member`, spawns `history/units/AUH_pol_federal.txt` (8 divisions).
  - In `common/countries/cosmetic.txt`:
    - Ensure `HUN_AUS_danubian_state`, `CZE_AUS_danubian_state`, `CRO_AUS_danubian_state`, `POL_AUS_danubian_state` all have:
      ```clausewitz
      color = rgb { 202 198 188 }
      color_ui = rgb { 220 216 206 }
      ```
  - In `history/units/`:
    - Create authentic historical division templates and OOBs for `AUH_hun_federal.txt`, `AUH_cze_federal.txt`, `AUH_cro_federal.txt`, `AUH_pol_federal.txt`.
  - In `common/ideas/ww1_austria_constitutional_ideas.txt`:
    - Define `AUH_danubian_federal_member`:
      - `extra_trade_to_overlord_factor = 0.75`
      - `cic_to_overlord_factor = 0.75`
      - `mic_to_overlord_factor = 0.75`
      - `overlord_manpower_factor = 0.70`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_danubian_mega_federation_setup -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/scripted_effects/ww1_danubian_federation_effects.txt common/countries/cosmetic.txt history/units/AUH_*_federal.txt common/ideas/
  git commit -m "feat(auh): implement real Danubian Mega-Federation, uniform map colors, and 4-18 division spawns"
  ```

---

### Task 5: Tag-Safe Scripted Secession & Crisis Containment Engine

**Files:**
- Create: `events/ww1_austria_collapse_events.txt`
- Create: `common/ai_strategy/ww1_auh_rebel_ai_strategy.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_austria_no_day1_crisis`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_tag_safe_breakaway_rules`

**Interfaces:**
- Consumes: Constitutional state and weariness simulation.
- Produces: Tag-safe secession crises (`ww1_austria_collapse.1`, `ww1_austria_collapse.2`, etc.) and instant imperial reunification upon capturing rebel capitals.

- [ ] **Step 1: Write test assertions in `test_austria_no_day1_crisis` and `test_tag_safe_breakaway_rules`**
  Assert zero occurrences of `start_civil_war` in `events/ww1_austria_collapse_events.txt`. Assert every collapse event trigger requires `has_war = yes`, date > 1915, surrender_progress > 0.40 or loss of Vienna/Budapest/Galicia. Assert rebel tags execute `can_join_factions = no`.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_austria_no_day1_crisis tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_tag_safe_breakaway_rules -v`
  Expected: FAIL (`events/ww1_austria_collapse_events.txt` missing).

- [ ] **Step 3: Implement collapse events and reunification mechanics**
  - In `events/ww1_austria_collapse_events.txt`:
    - Namespace: `ww1_austria_collapse`
    - Event `ww1_austria_collapse.1`: Czech Secession (under Dualism/Dictatorship when weariness > 75 and fronts collapse). Transfers states 9 & 69 to `CZE`, executes `set_rule = { can_join_factions = no }`, declares internal civil war.
    - Event `ww1_austria_collapse.2`: Hungarian Secession (under Trialism when Hungary rejects loss of Croatia). Transfers Hungarian cores to `HUN`, executes `set_rule = { can_join_factions = no }`.
    - Event `ww1_austria_collapse.3`: South Slav Secession (under Dualism/Dictatorship). Transfers 109 to `CRO`, executes `set_rule = { can_join_factions = no }`.
    - Event `ww1_austria_collapse.10`: Imperial Authority Restored (triggers when Austria controls rebel capital Prague, Budapest, or Zagreb; cleanly annexes rebel tag, restores +20% stability, zero broken peace conferences).
  - In `common/ai_strategy/ww1_auh_rebel_ai_strategy.txt`:
    - Set AI strategy forbidding breakaway tags from seeking foreign alliances or joining factions (`antagonize id = FRA value = -100`, `alliance id = ENG value = -1000`).

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_austria_no_day1_crisis tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_tag_safe_breakaway_rules -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_austria_collapse_events.txt common/ai_strategy/ww1_auh_rebel_ai_strategy.txt
  git commit -m "feat(auh): implement tag-safe scripted secession crises and instant imperial reunification engine"
  ```

---

### Task 6: Industrial Conglomerates (Škoda, Steyr, Ganz) & Military Rivalries (Conrad vs Boroević)

**Files:**
- Create: `common/ideas/ww1_austria_industry_and_military_ideas.txt`
- Modify: `common/national_focus/austria.txt`
- Create: `common/decisions/ww1_austria_skoda_decisions.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_skoda_and_three_armies_modifiers`

**Interfaces:**
- Consumes: Semantic modifier oracle from `scripts/hoi4_semantic_oracle.py`.
- Produces: Industrial ideas for Škoda, Steyr, Ganz-Danubius, military doctrine ideas for Conrad vs Boroević, and Galician oil decisions.

- [ ] **Step 1: Write test assertions in `test_skoda_and_three_armies_modifiers`**
  Assert `AUH_skoda_305_howitzer`, `AUH_steyr_mannlicher`, `AUH_ganz_danubius`, `AUH_three_armies_friction`, `AUH_conrad_offensive_doctrine`, and `AUH_borojevic_alpine_defense` exist and contain 100% valid modifiers.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_skoda_and_three_armies_modifiers -v`
  Expected: FAIL.

- [ ] **Step 3: Implement industrial ideas, military doctrines, and decisions**
  - In `common/ideas/ww1_austria_industry_and_military_ideas.txt`:
    - `AUH_skoda_305_howitzer`: `army_artillery_attack_factor = 0.15`, `breakthrough_factor = 0.10`.
    - `AUH_steyr_mannlicher`: `production_factory_efficiency_gain_factor = 0.10`, `industrial_capacity_factory = 0.05`.
    - `AUH_ganz_danubius`: `naval_strike_attack_factor = 0.10`, `dockyard_range_factor = 0.10`.
    - `AUH_three_armies_friction`: `army_org_factor = -0.10`, `experience_gain_army_factor = -0.15` (can be reformed).
    - `AUH_conrad_offensive_doctrine`: `army_attack_factor = 0.10`, `breakthrough_factor = 0.15`, `attrition = 0.10`.
    - `AUH_borojevic_alpine_defense`: `defence = 0.15`, `terrain_penalty_factor = -0.15`, `dig_in_speed_factor = 0.20`.
  - In `common/decisions/ww1_austria_skoda_decisions.txt`:
    - Decisions: `AUH_dec_skoda_siege_howitzers`, `AUH_dec_galician_oil_extraction`, `AUH_dec_steep_alpine_redoubts`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_skoda_and_three_armies_modifiers -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/ideas/ww1_austria_industry_and_military_ideas.txt common/decisions/ww1_austria_skoda_decisions.txt common/national_focus/austria.txt
  git commit -m "feat(auh): implement Škoda 30.5cm artillery, Steyr arms, Conrad vs Boroević doctrines, and Galician oil"
  ```

---

### Task 7: Pre-War Espionage (Colonel Redl), Sixtus Affair & Danubian Hegemony

**Files:**
- Create: `events/ww1_austria_diplomacy_events.txt`
- Create: `common/decisions/ww1_austria_diplomacy_decisions.txt`
- Modify: `common/national_focus/austria.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_localisation_bom_and_parity`

**Interfaces:**
- Consumes: Historical timeline (1911–1923) from `hoi4-historical-ww1-database` skill.
- Produces: Colonel Redl 1913 espionage scandal, Sixtus peace negotiations, Austro-Polish solution, and Ukrainian Bread Peace.

- [ ] **Step 1: Write test assertions for diplomacy events and decisions**
  Assert `events/ww1_austria_diplomacy_events.txt` contains `ww1_austria_diplomacy.1` (Colonel Redl affair), `ww1_austria_diplomacy.10` (Sixtus Affair), `ww1_austria_diplomacy.20` (Austro-Polish solution), and `ww1_austria_diplomacy.30` (Brotfrieden).

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul -k "test_crown_dashboard_and_grain" -v`
  Expected: FAIL on diplomacy assertions.

- [ ] **Step 3: Implement diplomacy events and decisions**
  - In `events/ww1_austria_diplomacy_events.txt`:
    - Event `ww1_austria_diplomacy.1`: The Colonel Redl Affair (May 1913). Option A: Overhaul mobilization Plan B/R (costs 50 PP, removes Russian intel advantage); Option B: Cover up suicide to preserve Evidenzbureau honor (-10% defense vs Russia in 1914).
    - Event `ww1_austria_diplomacy.10`: The Sixtus Affair (March 1917). Karl I approaches France via Prince Sixte of Bourbon-Parma. If Germany refuses peace, Austria can explore exit or separate peace.
    - Event `ww1_austria_diplomacy.20`: The Austro-Polish Solution. Archduke Karl Stephan crowned King of Poland, creating client kingdom aligned with Vienna.
    - Event `ww1_austria_diplomacy.30`: The Brotfrieden (February 1918). Requisitions Ukrainian grain (+40 Vienna Grain Stockpile, ending bread riots).
  - In `common/decisions/ww1_austria_diplomacy_decisions.txt`:
    - Add decisions for Prince Wilhelm of Wied's Albanian throne and Danubian Customs Union.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_austria_diplomacy_events.txt common/decisions/ww1_austria_diplomacy_decisions.txt common/national_focus/austria.txt
  git commit -m "feat(auh): implement Colonel Redl espionage affair, Sixtus peace negotiations, and Danubian hegemony"
  ```

---

### Task 8: Full Bilingual Localization Engine (English & Brazilian Portuguese)

**Files:**
- Create: `localisation/english/ww1_austria_rework_l_english.yml`
- Create: `localisation/braz_por/ww1_austria_rework_l_braz_por.yml`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_localisation_bom_and_parity`

**Interfaces:**
- Consumes: All focus, event, decision, idea, and cosmetic tag keys created in Tasks 2–7.
- Produces: 100% key parity with strictly single UTF-8 BOM (`\xef\xbb\xbf`) on both files.

- [ ] **Step 1: Write test assertions in `test_localisation_bom_and_parity`**
  Assert both English and Portuguese files exist, start with exact single byte sequence `\xef\xbb\xbf`, have ZERO double BOM `\xef\xbb\xbf\xef\xbb\xbf`, and 100% of keys in English exist in Portuguese.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_localisation_bom_and_parity -v`
  Expected: FAIL (`localisation/` files missing).

- [ ] **Step 3: Implement complete English and Brazilian Portuguese localization**
  - Create `localisation/english/ww1_austria_rework_l_english.yml` with single UTF-8 BOM.
  - Create `localisation/braz_por/ww1_austria_rework_l_braz_por.yml` with single UTF-8 BOM.
  - Translate all keys:
    - Focuses (4 constitutional paths, economic, military, and diplomatic focuses).
    - Ideas (Škoda, Steyr, Ganz, Conrad, Boroević, 4 constitutional spirits, `AUH_danubian_federal_member`).
    - Decisions (Grain rationing, Banat requisitions, Diet appeasement, Sixtus affair).
    - Events (Secession crises, reunification, Redl affair, Sixtus affair, Brotfrieden).
    - Cosmetic tags and divisions.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_localisation_bom_and_parity -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add localisation/english/ww1_austria_rework_l_english.yml localisation/braz_por/ww1_austria_rework_l_braz_por.yml
  git commit -m "feat(loc): provide complete bilingual localization with single UTF-8 BOM for Austria-Hungary rework"
  ```

---

### Task 9: Master QA Audit, GitHub Commit/Push & Steam Workshop Synchronization

**Files:**
- Test: `scripts/qa_audit_all.py`
- Modify: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491` (mirrored files)

**Interfaces:**
- Consumes: The entire codebase.
- Produces: 12/12 passing test suites, 0 Clausewitz bracket errors, 0 invalid semantic modifiers, clean git push to `origin/main`, and complete Steam Workshop staging synchronization.

- [ ] **Step 1: Run Clausewitz bracket validator**
  Run: `python scripts/mod_engine.py`
  Expected: Diff = 0 across all files.

- [ ] **Step 2: Run Semantic Modifier Oracle**
  Run: `python scripts/hoi4_semantic_oracle.py`
  Expected: 0 invalid modifier errors.

- [ ] **Step 3: Run Master QA Test Suite (All 12 Suites)**
  Run: `python scripts/qa_audit_all.py`
  Expected: 100% PASS (12/12 suites passing).

- [ ] **Step 4: Push all changes to GitHub**
  ```bash
  git push origin main
  ```

- [ ] **Step 5: Synchronize all modified files to Steam Workshop staging folder**
  Copy all modified and newly created directories (`common/`, `events/`, `history/`, `localisation/`) to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

- [ ] **Step 6: Commit and verify final status**
  Confirm git status is clean and workshop files are 100% in sync.
