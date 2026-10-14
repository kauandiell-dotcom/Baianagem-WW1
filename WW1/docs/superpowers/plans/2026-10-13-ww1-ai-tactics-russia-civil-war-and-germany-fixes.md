# WW1 Master AI Overhaul, Tag-Safe Russian Civil War, and German/Russian Mechanics Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform HOI4 AI from vanilla suicidal battle plan spam into a player-grade tactical engine (high planning, org conservation, encirclement defense, proper army grouping), eliminate the bugged dynamic `D01` Russian Civil War by wiring dedicated `SOV` vs `WHT` trees, reconcile Russian crisis variables, balance the Okhrana crackdown, fix Bulgarian and minor alliance entry, and verify all German mechanics.

**Architecture:** 
1. `common/defines/ww1_ai_defines.lua`: Inject engine-level `NAI` and `NMilitary` defines that stop suicidal attacks into trenches, raise planning requirements to 70%, force attack cancellation at low efficiency, enforce 24-division army consolidation, and protect retreating units.
2. `common/ai_strategy/`: Create comprehensive AI strategy modules (`ww1_grand_ai_strategy.txt` and `ww1_bulgaria_ai_strategy.txt`) instructing AI to hold frontline cohesion, request proper unit templates, and ensure Bulgaria, Romania, and Central Powers allies enter war directly.
3. `events/ww1_ger_rus_rework_events.txt` & `common/scripted_effects/`: Purge legacy `start_civil_war` dynamic tags (`D01`) and replace with the dedicated `SOV` vs `WHT` civil war transition, loading dedicated 80-focus (`soviet_russia.txt`) and 60-focus (`white_russia.txt`) trees with authentic flags and boundaries.
4. `common/decisions/` & `common/scripted_effects/`: Reconcile all Russian crisis variables (`SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`), unmask the hidden Okhrana requirement with a localized tooltip, and eliminate the 1-click trivialization.
5. `events/ww1_germany_events.txt`: Update `ww1_germany_events.33` so when Bulgaria accepts the alliance treaty, it directly joins the war against Serbia and the Entente.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Lua Defines (`NDefines.NAI`, `NDefines.NMilitary`), Paradox YAML Localization (UTF-8 BOM), Python `unittest`, `scripts/qa_audit_all.py`, `scripts/hoi4_semantic_oracle.py`.

**Spec:** System design established in conversation and verified through reverse-engineered Clausewitz runtime behavior.

## Global Constraints

- 100% bracket balance across all Clausewitz script files (`.txt`).
- Strictly single UTF-8 BOM (`\xef\xbb\xbf`) on all localization files (`.yml`). Zero double-BOM.
- 100% key parity between English (`l_english`) and Brazilian Portuguese (`l_braz_por`).
- Zero invalid modifiers verified against `scripts.hoi4_semantic_oracle`.
- No dynamic civil war tags (`start_civil_war = { ... }`) for Russia: all civil war operations must use historical tags `SOV` and `WHT`.
- Mirror all modified and newly created files to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus

1. **Dynamic Tag D01 Regression:** Ensure `ww1_russia.255`, `ww1_russia.220`, and any related civil war triggers never execute `start_civil_war`. They must transfer states and load trees between `SOV` and `WHT`.
2. **Variable Desync:** Ensure `SOV_unrest` and `SOV_hunger` are completely mapped to `SOV_worker_unrest` and `SOV_urban_hunger` across all decision files.
3. **Okhrana Decision Visibility:** Verify `SOV_dec_crush_bolsheviks_okhrana` has clear custom trigger tooltips for tension, stability, and demilitarization checks.
4. **AI Battleplan Restraint:** Verify `MIN_PLANNING_BONUS_TO_ATTACK` and `PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL` prevent AI suicide attacks.
5. **Bulgarian War Entry:** Verify `ww1_germany_events.33` adds Bulgaria to faction AND calls Bulgaria to war against Serbia and France/Britain/Russia.

---

### Task 1: QA RED Test Baseline (`tests/test_ww1_ai_and_russia_fixes.py`)

**Files:**
- Create: `tests/test_ww1_ai_and_russia_fixes.py`
- Modify: `scripts/qa_audit_all.py`

**Interfaces:**
- Produces: 5 automated unit tests:
  1. `test_ai_tactical_defines`: Verifies `ww1_ai_defines.lua` sets high planning thresholds, attack cancellation efficiency, and org conservation.
  2. `test_bulgaria_alliance_and_war_call`: Verifies `ww1_germany_events.33` calls Bulgaria into Central Powers wars, and Bulgaria AI strategy exists.
  3. `test_tag_safe_russian_civil_war`: Verifies zero `start_civil_war` commands exist in Russian events; asserts `SOV` and `WHT` tag transitions with respective trees.
  4. `test_russian_crisis_variable_reconciliation`: Verifies zero references to legacy `SOV_unrest` and `SOV_hunger` in decision files; all use `SOV_worker_unrest` and `SOV_urban_hunger`.
  5. `test_okhrana_crackdown_balance_and_tooltips`: Verifies `SOV_dec_crush_bolsheviks_okhrana` has explicit localized tooltips and non-trivial requirements.

- [ ] **Step 1: Write `tests/test_ww1_ai_and_russia_fixes.py` with the 5 test cases**
- [ ] **Step 2: Run test suite to verify RED phase failure on unimplemented features**
Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes -v`
Expected: FAIL on unimplemented components.
- [ ] **Step 3: Register test suite in `scripts/qa_audit_all.py`**
- [ ] **Step 4: Commit RED test baseline**
```bash
git add tests/test_ww1_ai_and_russia_fixes.py scripts/qa_audit_all.py
git commit -m "test(ai,rus): establish RED QA test suite for AI tactical overhaul, tag-safe civil war, and crisis fixes"
```

---

### Task 2: Player-Grade WW1 Combat & Army Management AI Defines

**Files:**
- Create: `common/defines/ww1_ai_defines.lua`
- Test: `tests/test_ww1_ai_and_russia_fixes.py::TestAIAndRussiaFixes::test_ai_tactical_defines`

**Interfaces:**
- Produces: Engine-level AI parameters for tactical battle plans, org conservation, and army consolidation:
  - `NDefines.NAI.MIN_PLANNING_BONUS_TO_ATTACK = 0.65` (Forces AI to accumulate 65%+ planning before launching major offensives).
  - `NDefines.NAI.PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL = 0.60` (Cancels attacks when combat efficiency falls below 60%, preventing meat-grinder losses).
  - `NDefines.NAI.PLAN_ATTACK_MAX_FRICTION = 0.25` (Halts attacks into muddy/fortified stalemates).
  - `NDefines.NAI.ORG_UNIT_WEAK = 0.45` (Forces AI to stop attacking and defend when organization drops below 45%).
  - `NDefines.NAI.STRENGTH_UNIT_WEAK = 0.60` (Conserves divisions below 60% equipment/strength).
  - `NDefines.NAI.ENTRENCHMENT_FACTOR_ATTACK = 2.0` (Heavily penalizes attacking heavily entrenched trenches without massive preparation).
  - `NDefines.NAI.MAX_NUM_DIVISIONS_TO_ATTACK_PER_PROVINCE = 6` (Prevents overcrowding and severe stacking penalties).
  - `NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 24` (Standardizes 24-division armies like human players).
  - `NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 5` (Standardizes 5 armies per army group).

- [ ] **Step 1: Create `common/defines/ww1_ai_defines.lua` with validated Lua syntax**
- [ ] **Step 2: Run unit test**
Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_ai_tactical_defines -v`
Expected: PASS
- [ ] **Step 3: Commit**
```bash
git add common/defines/ww1_ai_defines.lua
git commit -m "feat(ai): implement player-grade WW1 combat, org conservation, and army management defines"
```

---

### Task 3: Bulgaria & Minor Belligerents AI Strategy and War Entry Engine

**Files:**
- Modify: `events/ww1_germany_events.txt` (Event `ww1_germany_events.33`)
- Create: `common/ai_strategy/ww1_bulgaria_ai_strategy.txt`
- Create: `common/ai_strategy/ww1_grand_ai_strategy.txt`
- Test: `tests/test_ww1_ai_and_russia_fixes.py::TestAIAndRussiaFixes::test_bulgaria_alliance_and_war_call`

**Interfaces:**
- Consumes: Alliance treaty event `ww1_germany_events.33`
- Produces: Direct war entry for Bulgaria against Serbia and Entente; strategic AI priorities for minor allies.

- [ ] **Step 1: Refactor `ww1_germany_events.33` in `events/ww1_germany_events.txt`**
When Bulgaria accepts Option A:
- Adds Bulgaria to `Central_Powers` faction.
- Calls Bulgaria into existing wars against `SER` and any enemies of `GER`.
- If `SER` exists and `GER` is at war with `SER`, explicitly triggers:
  ```clausewitz
  BUL = {
      declare_war_on = { target = SER type = annex_everything }
  }
  ```
- [ ] **Step 2: Create `common/ai_strategy/ww1_bulgaria_ai_strategy.txt`**
Configures AI strategy for Bulgaria:
- Front unit priority against Serbia and Romania.
- High alliance weight towards Central Powers (`alliance id = GER value = 200`).
- High declare war weight towards Serbia (`declare_war id = SER value = 200`).
- [ ] **Step 3: Create `common/ai_strategy/ww1_grand_ai_strategy.txt`**
Configures major power AI front management:
- Trench holding cohesion, avoiding division clustering in dead ends.
- Anti-encirclement defensive retreat weight.
- [ ] **Step 4: Run unit test**
Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_bulgaria_alliance_and_war_call -v`
Expected: PASS
- [ ] **Step 5: Commit**
```bash
git add events/ww1_germany_events.txt common/ai_strategy/
git commit -m "feat(ai,bul): implement direct war entry, alliance call-to-arms, and strategic AI priorities for Bulgaria"
```

---

### Task 4: Tag-Safe Russian Civil War Engine (Eliminating Dynamic D01 Clones)

**Files:**
- Modify: `events/ww1_ger_rus_rework_events.txt` (Events `ww1_russia.255`, `ww1_russia.220`)
- Modify: `common/scripted_effects/ww1_ger_rus_rework_effects.txt`
- Test: `tests/test_ww1_ai_and_russia_fixes.py::TestAIAndRussiaFixes::test_tag_safe_russian_civil_war`

**Interfaces:**
- Consumes: Pre-revolutionary crisis triggers and revolutionary climax events.
- Produces: Pure tag-safe historical civil war:
  - Replaces all generic `start_civil_war = { ... }` with explicit state transfers and puppet/tag setups:
  - Tag `SOV` (Lenin/Trotsky, Bolsheviks) takes central heartland (Moscow, Petrograd, Nizhny Novgorod, Volga).
  - Tag `WHT` (White Movement under Kolchak/Denikin) takes South Russia, Don-Kuban, Urals, and Siberia with authentic White Russia flag and color `rgb { 30 75 140 }`.
  - Tag `SOV` loads `common/national_focus/soviet_russia.txt` (80 focuses).
  - Tag `WHT` loads `common/national_focus/white_russia.txt` (60 focuses).
  - Both sides are declared at war with each other. Zero dynamic `D01` tags!

- [ ] **Step 1: Refactor `ww1_russia.255` in `events/ww1_ger_rus_rework_events.txt`**
Purge `start_civil_war = { ideology = communism size = 0.45 }` and `start_civil_war = { ideology = neutrality size = 0.45 }`.
Implement tag-safe transfer to `WHT` and `SOV`.
- [ ] **Step 2: Refactor `ww1_russia.220` in `events/ww1_ger_rus_rework_events.txt`**
Replace dynamic civil war calls with scripted tag transitions.
- [ ] **Step 3: Update `common/scripted_effects/ww1_ger_rus_rework_effects.txt`**
Ensure `SOV_trigger_civil_war_climax` correctly partitions states between `SOV` and `WHT` without engine desync.
- [ ] **Step 4: Run unit test**
Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_tag_safe_russian_civil_war -v`
Expected: PASS
- [ ] **Step 5: Commit**
```bash
git add events/ww1_ger_rus_rework_events.txt common/scripted_effects/ww1_ger_rus_rework_effects.txt
git commit -m "fix(rus): replace dynamic D01 civil war clones with tag-safe SOV and WHT historical civil war engine"
```

---

### Task 5: Russian Crisis Variable Reconciliation & Okhrana Crackdown Rebalance

**Files:**
- Modify: `common/decisions/ww1_ger_rus_rework_decisions.txt`
- Modify: `common/scripted_effects/ww1_ger_rus_rework_effects.txt`
- Modify: `localisation/english/ww1_ger_rus_rework_l_english.yml`
- Modify: `localisation/braz_por/ww1_ger_rus_rework_l_braz_por.yml`
- Test: `tests/test_ww1_ai_and_russia_fixes.py::TestAIAndRussiaFixes::test_russian_crisis_variable_reconciliation`
- Test: `tests/test_ww1_ai_and_russia_fixes.py::TestAIAndRussiaFixes::test_okhrana_crackdown_balance_and_tooltips`

**Interfaces:**
- Consumes: Decision categories `SOV_home_front` and `SOV_civil_war_front`.
- Produces: Complete variable synchronization (`SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`), clear localized tooltips for Okhrana decision, and multi-step crackdown balance.

- [ ] **Step 1: Reconcile all variables in `common/decisions/ww1_ger_rus_rework_decisions.txt`**
Change all instances of `SOV_unrest` to `SOV_worker_unrest` and `SOV_hunger` to `SOV_urban_hunger`.
- [ ] **Step 2: Reconcile all variables in `common/scripted_effects/ww1_ger_rus_rework_effects.txt`**
Ensure clamps and calculations affect `SOV_worker_unrest` and `SOV_urban_hunger`.
- [ ] **Step 3: Rebalance and add custom trigger tooltip to `SOV_dec_crush_bolsheviks_okhrana`**
Add:
```clausewitz
custom_trigger_tooltip = {
    tooltip = SOV_dec_crush_bolsheviks_okhrana_req_tt
    check_variable = { SOV_revolutionary_tension < 20 }
    has_stability > 0.50
    195 = { is_demilitarized_zone = no }
    219 = { is_demilitarized_zone = no }
}
```
Add 90-day mission / investigation phase (`days_remove = 90`) rather than an instant 1-click victory, costing 100 PP and requiring high stability (>50%).
- [ ] **Step 4: Add localization keys with strictly single UTF-8 BOM in English and Portuguese**
Add `SOV_dec_crush_bolsheviks_okhrana_req_tt` and updated descriptions.
- [ ] **Step 5: Run unit tests**
Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_russian_crisis_variable_reconciliation tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_okhrana_crackdown_balance_and_tooltips -v`
Expected: PASS
- [ ] **Step 6: Commit**
```bash
git add common/decisions/ww1_ger_rus_rework_decisions.txt common/scripted_effects/ww1_ger_rus_rework_effects.txt localisation/
git commit -m "fix(rus): reconcile Russian crisis variables and rebalance Okhrana crackdown with transparent tooltips"
```

---

### Task 6: Master QA Verification, 100% Green Pipeline & Live Workshop Sync

**Files:**
- Test: All 10 mod test suites via `scripts/qa_audit_all.py`
- Mirror: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

**Interfaces:**
- Consumes: All completed tasks.
- Produces: Exit Code 0 across master QA suite and 100% verified files in the Steam Workshop directory.

- [ ] **Step 1: Audit all Clausewitz files with Semantic Oracle and syntax checks**
- [ ] **Step 2: Run Master QA Audit `python scripts/qa_audit_all.py`**
Expected: Exit Code 0 across all test suites.
- [ ] **Step 3: Run Python mirror script synchronizing all modified files to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`**
- [ ] **Step 4: Verify synced files exist and match byte sizes**
- [ ] **Step 5: Report completion to user**
