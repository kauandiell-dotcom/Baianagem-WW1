# Russian Empire, Revolution, Soviet & White Civil War Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a comprehensive overhaul of the Russian Empire (`SOV`), the Pre-Revolutionary Crisis Engine (1915–1917), the multi-front Russian Civil War (`SOV` vs `WHT` vs peripheral breakaways), and two full dedicated focus trees for Soviet Russia and the White Movement.

**Architecture:** Modular Clausewitz scripting architecture with separate national focus trees (`soviet.txt`, `soviet_russia.txt`, `white_russia.txt`), dedicated tag `WHT`, clamped decision-dashboard gauges (0–100%), decoupled on_actions for Brest-Litovsk and German armistice, custom civil war OOBs, and automated TDD test validation via `scripts/qa_audit_all.py`.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Python (QA test runners, Semantic Oracle, AST/coordinate linters), YAML (Single UTF-8 BOM Localization).

**Spec:** `docs/superpowers/specs/2026-10-13-russian-empire-soviet-and-civil-war-rework-design.md`

## Global Constraints

- 100% Clausewitz bracket balance and syntax integrity across all `.txt` and `.gui` files.
- All modifier names must exist in `data/hoi4_valid_country_modifiers.json` and pass `scripts/hoi4_semantic_oracle.py`.
- Strictly single UTF-8 BOM (`\xef\xbb\xbf`) on all localization files (`localisation/english/` and `localisation/braz_por/`) with 100% key parity.
- Focus tree spatial grid rules: adjacent focuses on the same row must satisfy $|x_2 - x_1| \ge 2$, parent-child prerequisite vertical links must satisfy $1 \le child\_y - parent\_y \le 3$, zero duplicate focus IDs, zero $(x, y)$ coordinate collisions.
- Dedicated tag `WHT` used for the White Movement, returning to `SOV` upon post-war reunification to preserve foreign event compatibility.
- Civil war uses `prevent_join_factions = yes` to prevent Entente AI from flooding divisions into Russia.
- All 8 test suites in `scripts/qa_audit_all.py` must pass with Exit Code 0.

## Review Focus

1. **Tag Desync / Missing Tag:** Ensure tag `WHT` is recognized across `common/country_tags/`, `common/countries/`, and `history/countries/` before any event references it.
2. **Double UTF-8 BOM:** Verify byte headers strictly equal `b"\xef\xbb\xbf"` at `[:3]` and `!= b"\xef\xbb\xbf"` at `[3:6]`.
3. **Ghost / Hollow Focuses:** Ensure every focus in all three trees grants concrete gameplay rewards (factories, equipment, ideas, tech bonuses, experience, or decisions).
4. **Civil War OOB Spawns:** Ensure old imperial units are cleanly cleared and new civil war OOBs spawn without crashing or leaving phantom divisions.
5. **Decoupled German Hooks:** Ensure decisions and events referencing Germany check `country_exists = GER` and work cleanly regardless of German AI or player choices.

---

### Task 1: QA Test Suite Baseline Expansion (`tests/test_ww1_russia_rework.py` — RED Phase)

**Files:**
- Create: `tests/test_ww1_russia_rework.py`

**Interfaces:**
- Produces: Test assertions for `WHT` country tag, characters, crisis variables, focus trees, ideas, decisions, and localization.

- [ ] **Step 1: Create `tests/test_ww1_russia_rework.py` with comprehensive assertions**
  Assert:
  - `WHT` tag defined in `common/country_tags/` and `history/countries/WHT - White Russia.txt`.
  - Characters recruited in `common/characters/SOV.txt` and `WHT.txt`: Trotsky, Stalin, Frunze, Dzerzhinsky, Budyonny, Tukhachevsky, Chicherin, Bukharin, Kolchak, Denikin, Wrangel, Yudenich.
  - Ideas exist: `SOV_strategic_depth_and_rasputitsa`, `SOV_shell_shortage_crisis`, `SOV_vpk_mobilization_spirit`, `SOV_order_restored_spirit`.
  - Focus trees `soviet_russia_focus` and `white_russia_focus` exist and have non-colliding coordinates.
  - Single UTF-8 BOM on all Russian localization files.

- [ ] **Step 2: Run test suite to verify RED phase failure**
  Run: `python -m unittest tests/test_ww1_russia_rework.py -v`
  Expected: FAIL (files and tags not yet implemented).

- [ ] **Step 3: Commit RED test baseline**
  ```bash
  git add tests/test_ww1_russia_rework.py
  git commit -m "test(sov): create master QA test suite baseline for Russia overhaul (RED)"
  ```

---

### Task 2: Country Tag `WHT`, Historical Characters, Cosmetic Tags & GFX Sprites

**Files:**
- Create: `common/country_tags/01_ww1_tags.txt`
- Create: `common/countries/White Russia.txt`
- Create: `history/countries/WHT - White Russia.txt`
- Modify: `common/countries/colors.txt`
- Modify: `common/countries/cosmetic.txt`
- Modify: `common/characters/SOV.txt`
- Create: `common/characters/WHT.txt`
- Create: `interface/ww1_soviet_goals.gfx`
- Create: `interface/ww1_white_goals.gfx`

**Interfaces:**
- Consumes: Existing leader/idea texture assets in `gfx/leaders/SOV/` and `gfx/interface/goals/`.
- Produces: Valid tag `WHT`, 15+ recruited characters with traits, and animated `.gfx` goal sprites.

- [ ] **Step 1: Define `WHT` tag, history file, colors and cosmetic tags**
  Set `WHT = "countries/White Russia.txt"` in `common/country_tags/01_ww1_tags.txt`.
  Set color `rgb { 240 240 245 }` in `common/countries/colors.txt`.
  Create `history/countries/WHT - White Russia.txt` with Omsk capital (state 594), neutrality ideology, and character recruitment.

- [ ] **Step 2: Recruit Bolshevik and White historical characters**
  Add Trotsky, Stalin, Frunze, Dzerzhinsky, Budyonny, Tukhachevsky, Chicherin, Bukharin to `common/characters/SOV.txt`.
  Add Kolchak, Denikin, Wrangel, Yudenich, Kornilov, Kaledin, Savinkov to `common/characters/WHT.txt`.

- [ ] **Step 3: Create GFX sprite definitions for Soviet and White goals**
  Create `interface/ww1_soviet_goals.gfx` and `interface/ww1_white_goals.gfx` with `spriteType` and `_shine` definitions pointing to valid `.dds` textures.

- [ ] **Step 4: Verify with Semantic Oracle & Character Assertions**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_characters_and_tags -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/country_tags/ common/countries/ history/countries/ common/characters/ interface/
  git commit -m "feat(sov): establish WHT country tag, historical character cast, and focus GFX sprites"
  ```

---

### Task 3: Normal Tsarist Russia (1911–1917) Gameplay Mechanics, Shell Shortage & Strategic Depth

**Files:**
- Modify: `common/ideas/ww1_russia_ideas.txt`
- Create: `common/decisions/ww1_russia_tsarist_decisions.txt`
- Create: `common/decisions/categories/ww1_russia_tsarist_categories.txt`

**Interfaces:**
- Consumes: `SOV` original tag, state targets (Poland, Baltics, Galicia).
- Produces: `SOV_strategic_depth_and_rasputitsa`, shell shortage mobilization, Duma decisions, factory evacuation, and Brusilov infiltration.

- [ ] **Step 1: Add Tsarist ideas in `common/ideas/ww1_russia_ideas.txt`**
  Add `SOV_strategic_depth_and_rasputitsa` (enemy attrition +20%, enemy supply +15%, core defense +10%).
  Add `SOV_shell_shortage_crisis` (-25% artillery soft attack, -15% breakthrough).
  Add `SOV_vpk_mobilization_spirit` (+10% artillery production speed).
  Add `SOV_rasputin_court_intrigues` (+20% political decision cost, -5% stability).

- [ ] **Step 2: Implement Decision Categories & Gameplay Decisions**
  In `ww1_russia_tsarist_decisions.txt`:
  - `SOV_duma_and_court_politics`: *Convene the Imperial Duma*, *Prorogue the Duma*, *Conspiracy to Assassinate Rasputin*.
  - `SOV_war_industry_mobilization`: *Establish VPK Committees*, *Mobilize Machine Shops*, *Zemgor Medical Union*, *British Shell Presses*.
  - `SOV_evacuate_industrial_machinery` (`state_target = yes` for Warsaw, Bialystok, Riga, Grodno): evacuates factories to Moscow/Urals and scorches earth.
  - `SOV_prepare_southwestern_offensive`: Brusilov infiltration mission against Austria-Hungary.

- [ ] **Step 3: Verify with Semantic Oracle**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_russia_ideas.txt')) == 0; assert len(audit_file_modifiers('common/decisions/ww1_russia_tsarist_decisions.txt')) == 0"`
  Expected: 0 errors.

- [ ] **Step 4: Commit**
  ```bash
  git add common/ideas/ww1_russia_ideas.txt common/decisions/ww1_russia_tsarist_decisions.txt common/decisions/categories/ww1_russia_tsarist_categories.txt
  git commit -m "feat(sov): implement Tsarist 1911-1917 mechanics, shell shortage, and strategic depth"
  ```

---

### Task 4: Pre-Revolutionary Crisis Engine & Visual Decisions Dashboard (Late 1915 – Mid 1917)

**Files:**
- Create: `common/scripted_effects/ww1_russia_crisis_effects.txt`
- Create: `common/decisions/ww1_russia_crisis_decisions.txt`
- Create: `common/decisions/categories/ww1_russia_crisis_categories.txt`
- Create: `events/ww1_russia_crisis_events.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

**Interfaces:**
- Consumes: German decisions (`GER_operation_sealed_train`), date triggers (1917.3.1 fallback).
- Produces: 4 clamped gauges (`SOV_revolutionary_tension`, `SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`), visual progress bars, and resolution events (`ww1_russia.305` or `ww1_russia.310`).

- [ ] **Step 1: Implement Scripted Effects & Clamped Gauge Math**
  In `ww1_russia_crisis_effects.txt`:
  - `sov_russia_init_crisis_gauges`: sets baseline variables.
  - `sov_russia_clamp_crisis_gauges`: clamps all 4 variables between 0 and 100.
  - `sov_russia_weekly_crisis_update`: evaluates unrest, hunger, and army morale.

- [ ] **Step 2: Implement Decisions Dashboard with Visual Progress Bars**
  In `ww1_russia_crisis_decisions.txt`:
  - Category `SOV_revolutionary_crisis_category` displaying formatted progress bars:
    `SOV_crisis_tension_bar_tt`: `§R[████████░░] [?SOV_revolutionary_tension|0%]§!`
  - Decisions: *Emergency Grain Requisitions*, *Bread Price Subsidies*, *Okhrana Raids on Agitators*, *Imperial Frontline Tour*.

- [ ] **Step 3: Implement Events & Dual Trigger for Lenin's Return**
  In `events/ww1_russia_crisis_events.txt`:
  - `ww1_russia.300`: Lenin arrives via German Sealed Train (fires from German decision).
  - `ww1_russia.301`: Autonomous March 1917 fallback event if Germany never sent the train.
  - `ww1_russia.305`: *Triumph of Order* (Imperial Salvation if tension < 50% in late 1917).
  - `ww1_russia.310`: *Storming of the Winter Palace* (Fires if tension >= 85%).

- [ ] **Step 4: Verify Crisis Engine Tests**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_crisis_engine_and_gauges -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/scripted_effects/ww1_russia_crisis_effects.txt common/decisions/ww1_russia_crisis_decisions.txt common/decisions/categories/ww1_russia_crisis_categories.txt events/ww1_russia_crisis_events.txt common/on_actions/
  git commit -m "feat(sov): implement real-time revolutionary crisis dashboard, visual progress bars, and dual catalyst"
  ```

---

### Task 5: Multi-Front Russian Civil War Engine & Breakaway Powderkeg

**Files:**
- Create: `events/ww1_russia_civil_war_events.txt`
- Create: `history/units/SOV_red_army_civil_war.txt`
- Create: `history/units/WHT_white_army_civil_war.txt`
- Create: `history/units/UKR_civil_war.txt`
- Create: `history/units/FIN_civil_war.txt`
- Create: `history/units/POL_civil_war.txt`
- Create: `common/decisions/ww1_soviet_civil_war_decisions.txt`

**Interfaces:**
- Consumes: Event `ww1_russia.310` trigger.
- Produces: Tag partition (`SOV` vs `WHT`), breakaway war declarations (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`), fleet split, and combat OOBs.

- [ ] **Step 1: Create Dedicated Civil War OOBs**
  - `SOV_red_army_civil_war.txt`: 50 divisions of Red Guards, Workers' Battalions, Baltic Sailors.
  - `WHT_white_army_civil_war.txt`: 45 divisions of Siberian Riflemen, Volunteer Army, Cossack Cavalry.
  - Regional OOBs for `UKR` (14 divs), `FIN` (10 divs), `POL` (16 divs).

- [ ] **Step 2: Implement Civil War Eruption Script in `ww1_russia_civil_war_events.txt`**
  In `ww1_russia.310`:
  - Choice A: Player plays `SOV` (Soviets).
  - Choice B: Player plays `WHT` (Whites via `change_tag_from = SOV`).
  - Scripted immediate:
    - Disbands old imperial army via `delete_unit_template_and_units`.
    - Transfers Siberia, Urals, and South to `WHT`.
    - Splits fleet: Baltic Fleet to `SOV`, Black Sea Fleet to `WHT`.
    - Splits stockpiles 50/50.
    - Spawns breakaways (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`) and declares mutual war with `SOV` and `WHT`.
    - Sets `prevent_join_factions = yes` on `SOV` and `WHT`.

- [ ] **Step 3: Implement Map-Based War Communism & Kazan Gold Decisions**
  In `ww1_soviet_civil_war_decisions.txt`:
  - *Seize the Kazan Gold Reserves*, *Prodrazvyorstka Grain Expeditions*, *Mobilize Petrograd Workers*, *Trotsky's Armored Train Inspection*.

- [ ] **Step 4: Verify Civil War Mechanics & Bracket Balance**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_civil_war_spawns_and_oobs -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_russia_civil_war_events.txt history/units/ common/decisions/ww1_soviet_civil_war_decisions.txt
  git commit -m "feat(sov): implement multi-front Russian Civil War engine, breakaway nations, and combat OOBs"
  ```

---

### Task 6: Central Powers Interaction, Brest-Litovsk & Entente Proxy Aid

**Files:**
- Create: `events/ww1_russia_diplomacy_events.txt`
- Create: `common/decisions/ww1_soviet_diplomacy_decisions.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

**Interfaces:**
- Consumes: `SOV` Soviet government, `GER` existence, German 1918 armistice trigger.
- Produces: Treaty of Brest-Litovsk exit from WW1, Operation Faustschlag, Entente proxy aid for `WHT`, and 1918 dissolution of Brest-Litovsk.

- [ ] **Step 1: Implement Brest-Litovsk Decision & Event Chain**
  - `SOV_decree_on_peace`: opens diplomatic delegation with Germany.
  - Germany offers terms: ceding western borderlands.
  - If accepted: `SOV` exits war with Central Powers; `GER` gains `GER_brest_litovsk_deliveries` trade bonuses.
  - If rejected ("Neither War nor Peace"): Germany executes *Operation Faustschlag*.

- [ ] **Step 2: Implement Entente Proxy Decisions for `WHT`**
  - *General Knox British Mission*, *French Odessa Convoys*, *Vladivostok Lend-Lease*.
  - Grants equipment, subsidies, and off-map factory bonuses without dragging the Entente into total war.

- [ ] **Step 3: Implement 1918 German Armistice Dissolution Hook**
  In `zz_ww1_ger_rus_rework_on_actions.txt`:
  When Germany signs armistice / capitulates in late 1918:
  - Voids Brest-Litovsk deliveries.
  - Collapses German occupation in Ukraine/Belarus/Baltics.
  - Triggers Soviet *Target Vistula* westward reclamation.

- [ ] **Step 4: Verify Diplomacy Events & Modifier Oracle**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_brest_litovsk_and_diplomacy -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_russia_diplomacy_events.txt common/decisions/ww1_soviet_diplomacy_decisions.txt common/on_actions/
  git commit -m "feat(sov): implement Treaty of Brest-Litovsk, Entente proxy intervention, and armistice dissolution"
  ```

---

### Task 7: Dedicated Soviet Russia Focus Tree (`common/national_focus/soviet_russia.txt` — 80 Focuses)

**Files:**
- Create: `common/national_focus/soviet_russia.txt`

**Interfaces:**
- Consumes: Loaded via `load_focus_tree = soviet_russia_focus` upon Bolshevik victory/takeover.
- Produces: 80 bespoke focuses across 5 wings (War Communism, Red Army, GOELRO/NEP, Comintern, Formation of USSR 1922).

- [ ] **Step 1: Construct 5-Wing Non-Colliding Layout Grid**
  Ensure all 80 focuses follow standard spatial grid mathematics:
  - Adjacent focuses on the same row: $|x_2 - x_1| \ge 2$.
  - Parent-child links: $1 \le child\_y - parent\_y \le 3$.
  - 0 coordinate collisions.

- [ ] **Step 2: Script Focuses with Tangible Rewards**
  - Wing 1: War Communism & Red Terror (16 focuses).
  - Wing 2: Red Army Doctrine & Military Commissars (18 focuses).
  - Wing 3: GOELRO & Economic Reconstruction - NEP vs Superindustrialization (16 focuses).
  - Wing 4: Comintern & World Revolution - Polish-Soviet War & Rapallo (16 focuses).
  - Wing 5: State Building & Formation of the USSR 1922 (14 focuses).

- [ ] **Step 3: Run Focus Grid & Syntax Audit**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_soviet_focus_tree_integrity -v`
  Expected: PASS (80 focuses, 0 collisions, 0 hollow rewards).

- [ ] **Step 4: Commit**
  ```bash
  git add common/national_focus/soviet_russia.txt
  git commit -m "feat(sov): implement dedicated 80-focus Soviet Russia national focus tree"
  ```

---

### Task 8: Dedicated White Movement Focus Tree (`common/national_focus/white_russia.txt` — 60 Focuses)

**Files:**
- Create: `common/national_focus/white_russia.txt`

**Interfaces:**
- Consumes: Assigned to tag `WHT` (`country = { factor = 0 modifier = { add = 10 tag = WHT } }`).
- Produces: 60 bespoke focuses across 4 wings (Omsk Directorate, AFSR, Entente Diplomacy, Post-War Restoration).

- [ ] **Step 1: Construct 4-Wing Non-Colliding Layout Grid**
  Ensure all 60 focuses follow spatial grid rules ($|x_2 - x_1| \ge 2$, $1 \le \Delta y \le 3$).

- [ ] **Step 2: Script Focuses with Tangible Rewards**
  - Wing 1: The Omsk Directorate & Supreme Ruler Kolchak (15 focuses).
  - Wing 2: Armed Forces of South Russia - Denikin, Wrangel & Cossacks (16 focuses).
  - Wing 3: Entente Intervention & Western Munitions (15 focuses).
  - Wing 4: Post-War Political Restoration - Constituent Assembly vs Military Crowned Regent (14 focuses).
  - Capstone: *Reunify the Russian State* (`change_tag_to = SOV`).

- [ ] **Step 3: Run Focus Grid & Syntax Audit**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_white_focus_tree_integrity -v`
  Expected: PASS.

- [ ] **Step 4: Commit**
  ```bash
  git add common/national_focus/white_russia.txt
  git commit -m "feat(wht): implement dedicated 60-focus White Movement national focus tree"
  ```

---

### Task 9: Tsarist Focus Tree Refactoring & Polish (`common/national_focus/soviet.txt`)

**Files:**
- Modify: `common/national_focus/soviet.txt`

**Interfaces:**
- Consumes: Existing 235-focus tree.
- Produces: Purged legacy broken branches, enriched 41 hollow focuses, added *Imperial Salvation* capstones (Tsargrad / Constantinople annexation).

- [ ] **Step 1: Remove legacy 7-focus dead-end Bolshevik branch**
  Safely purge obsolete legacy stubs that dead-end at `SOV_war_communism_decrees`.

- [ ] **Step 2: Enrich 41 hollow focuses with concrete rewards**
  Add factories, infrastructure, equipment, tech bonuses, and ideas to all previously shallow focuses.

- [ ] **Step 3: Add Imperial Salvation Capstones**
  Add *The Annexation of Tsargrad & The Turkish Straits* and *Triumph of the Romanov Dynasty*.

- [ ] **Step 4: Verify Focus Integrity**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_imperial_focus_tree_integrity -v`
  Expected: PASS (0 hollow focuses, 0 collisions).

- [ ] **Step 5: Commit**
  ```bash
  git add common/national_focus/soviet.txt
  git commit -m "refactor(sov): purge legacy stubs, enrich hollow focuses, and add Imperial Salvation capstones"
  ```

---

### Task 10: Complete Bilingual Localization & Single UTF-8 BOM

**Files:**
- Create: `localisation/english/ww1_soviet_l_english.yml`
- Create: `localisation/braz_por/ww1_soviet_l_braz_por.yml`
- Create: `localisation/english/ww1_white_l_english.yml`
- Create: `localisation/braz_por/ww1_white_l_braz_por.yml`
- Modify: `localisation/english/ww1_russia_focus_l_english.yml`
- Modify: `localisation/braz_por/ww1_russia_focus_l_braz_por.yml`
- Modify: `localisation/english/ww1_russia_events_l_english.yml`
- Modify: `localisation/braz_por/ww1_russia_events_l_braz_por.yml`

**Interfaces:**
- Consumes: All new focus IDs, idea IDs, decision IDs, and event IDs.
- Produces: 100% bilingual localization key parity with single UTF-8 BOM.

- [ ] **Step 1: Create Soviet and White localization files in English and Portuguese**
  Write keys for all 80 Soviet focuses, 60 White focuses, all decisions, ideas, and events.
  Enforce strictly single UTF-8 BOM (`\xef\xbb\xbf` at start).

- [ ] **Step 2: Update Tsarist Russia localization files**
  Add keys for all new decisions, ideas, and capstones.

- [ ] **Step 3: Verify UTF-8 BOM & Localization Parity**
  Run: `python -c "import glob; [assert open(f, 'rb').read(3) == b'\xef\xbb\xbf' and open(f, 'rb').read(6)[3:] != b'\xef\xbb\xbf' for f in glob.glob('localisation/**/*.yml', recursive=True) if 'sov' in f.lower() or 'russia' in f.lower() or 'white' in f.lower()]"`
  Expected: PASS.

- [ ] **Step 4: Commit**
  ```bash
  git add localisation/english/ localisation/braz_por/
  git commit -m "feat(loc): provide complete bilingual localization with single UTF-8 BOM for Russia overhaul"
  ```

---

### Task 11: Master QA Integration & Full Test Pass

**Files:**
- Modify: `scripts/qa_audit_all.py`

**Interfaces:**
- Consumes: All 10 completed rework tasks.
- Produces: 8/8 test suites passing in `scripts/qa_audit_all.py` with Exit Code 0.

- [ ] **Step 1: Register `tests/test_ww1_russia_rework.py` into `scripts/qa_audit_all.py`**
  Add test runner block for Russian Empire, Revolution, Soviet & White Civil War test suite.

- [ ] **Step 2: Run Master QA Audit**
  Run: `python scripts/qa_audit_all.py`
  Expected: All 8 test suites PASS with Exit Code 0.

- [ ] **Step 3: Commit**
  ```bash
  git add scripts/qa_audit_all.py
  git commit -m "ci(qa): integrate Russia overhaul test suite into master QA audit runner"
  ```
