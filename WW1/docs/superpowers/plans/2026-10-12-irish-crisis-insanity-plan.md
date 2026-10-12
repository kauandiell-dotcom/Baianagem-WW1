# Irish Crisis Escalation, State Securing & Civil War Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a comprehensive, high-stakes domestic crisis engine for the British Empire in WW1, featuring brutal starting penalties, map-based state securing across Ireland's 4 states, paramilitary sabotage, and a dynamic territorial civil war with dual resolution tracks (Compromise vs Coercion).

**Architecture:** Extends the 5-Pillar British architecture using dynamic `swap_ideas` for Pillar 5, creates a dedicated decision category with state-targeted actions (`state_target = yes`), enforces anti-cheese concurrency and parliamentary friction, and triggers an un-aligned localized civil war (`IRE`) with instant post-capitulation annexation.

**Tech Stack:** Clausewitz Script (Hearts of Iron IV v1.14+), Python 3 test suites, Paradox YAML localization (UTF-8 BOM).

**Spec:** `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`

## Global Constraints
- Every modifier token must exist in `data/hoi4_valid_country_modifiers.json` (Clausewitz Semantic Oracle verified).
- Anti-Stacking constraint: Total unmanaged concurrent persistent national ideas in `ENG` must remain <= 5.
- Zero empty event options: Every option must provide tangible player-facing feedback, tooltips, or effects.
- 100% bilingual parity: Every text key must be localized in both `ww1_britain_l_english.yml` and `ww1_britain_l_braz_por.yml` with UTF-8 BOM (`\xef\xbb\xbf`).
- Tag `IRE` in civil war must be prohibited from joining foreign factions (`can_join_factions = no`).

## Review Focus
1. `ENG_ww1_the_defence_of_the_realm` focus must not prematurely erase the crisis in August 1914.
2. State securing decisions must only execute on one state at a time (strict concurrency lock).
3. Recapture of Dublin / capitulation of `IRE` must cleanly annex Ireland back into `ENG` without leaving orphan war states.
4. Conscription factor debuff must be valid and accurately penalize manpower during wartime.
5. All new idea definitions must pass `audit_file_modifiers` with 0 errors.

---

### Task 1: Q.A Audit Test Suite Expansion (RED Phase)

**Files:**
- Modify: `tests/test_ww1_britain_complete_audit.py`

**Interfaces:**
- Consumes: `tests/test_ww1_britain_complete_audit.py`, `scripts/hoi4_semantic_oracle.py`
- Produces: Failing unit tests proving that new ideas, state-securing mechanics, and civil war events are not yet present.

- [ ] **Step 1: Write failing tests in `tests/test_ww1_britain_complete_audit.py`**
  Add `test_irish_crisis_escalation_and_state_securing_mechanics`:
  - Assert `ENG_irish_home_rule_tension` has `stability_factor <= -0.30` and `war_support_factor <= -0.10`.
  - Assert `ENG_irish_sabotage_wave`, `ENG_irish_martial_law`, `ENG_irish_civil_war_debacle`, `ENG_irish_union_secured` exist in `ww1_britain_ideas.txt`.
  - Assert decision category `ENG_ww1_irish_crisis_category` exists in `common/decisions/categories/ww1_britain_categories.txt`.
  - Assert state securing decisions exist in `common/decisions/ww1_britain_decisions.txt`.
  - Assert civil war event `ww1_britain_pol.irish_civil_war` exists in `events/ww1_britain_events.txt`.

- [ ] **Step 2: Run test suite to verify RED failure**
  Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`
  Expected: FAIL (identifying missing ideas and categories).

- [ ] **Step 3: Commit RED test changes**
  Run:
  ```bash
  git add tests/test_ww1_britain_complete_audit.py
  git commit -m "test(uk): add test cases for Irish crisis escalation and state securing engine (RED)"
  ```

---

### Task 2: Pillar 5 Ideas Rework (`common/ideas/ww1_britain_ideas.txt`)

**Files:**
- Modify: `common/ideas/ww1_britain_ideas.txt`

**Interfaces:**
- Consumes: Valid modifier tokens from `data/hoi4_valid_country_modifiers.json`
- Produces: Updated `ENG_irish_home_rule_tension` and new dynamic states (`ENG_irish_sabotage_wave`, `ENG_irish_martial_law`, `ENG_irish_civil_war_debacle`, `ENG_irish_union_secured`).

- [ ] **Step 1: Update `ENG_irish_home_rule_tension`**
  Set modifiers:
  - `stability_factor = -0.35`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.20`
  - `conscription_factor = -0.15`

- [ ] **Step 2: Add dynamic escalation ideas**
  - `ENG_irish_sabotage_wave`: `stability_factor = -0.45`, `war_support_factor = -0.15`, `political_power_gain = -0.25`, `conscription_factor = -0.25`, `industrial_capacity_factory = -0.05`.
  - `ENG_irish_martial_law`: `stability_factor = -0.20`, `political_power_gain = -0.15`, `army_morale_factor = -0.05`, `conscription_factor = -0.10`.
  - `ENG_irish_civil_war_debacle`: `stability_factor = -0.40`, `war_support_factor = -0.20`, `political_power_gain = -0.30`, `army_org_factor = -0.10`.
  - `ENG_irish_union_secured`: `stability_factor = 0.05`, `war_support_factor = 0.05`, `conscription_factor = 0.05`.

- [ ] **Step 3: Verify with Clausewitz Semantic Oracle**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_britain_ideas.txt')) == 0"`
  Expected: Exit code 0 (no invalid modifier tokens).

- [ ] **Step 4: Commit changes**
  Run:
  ```bash
  git add common/ideas/ww1_britain_ideas.txt
  git commit -m "feat(uk): implement intense penalties and dynamic Pillar 5 Irish crisis ideas"
  ```

---

### Task 3: Map-Based State Securing Decisions Engine (`common/decisions/`)

**Files:**
- Modify: `common/decisions/categories/ww1_britain_categories.txt`
- Modify: `common/decisions/ww1_britain_decisions.txt`

**Interfaces:**
- Consumes: Pillar 5 ideas, variables `ww1_britain_irish_tension`, `ww1_britain_ulster_tension`, states 113, 114, 117, 119.
- Produces: `ENG_ww1_irish_crisis_category` and state-targeted decisions (`ENG_deploy_crown_garrison`, `ENG_raid_paramilitary_armories`, `ENG_emergency_curfew_lockdown`) with concurrency limits.

- [ ] **Step 1: Add decision category in `ww1_britain_categories.txt`**
  Define `ENG_ww1_irish_crisis_category` with:
  - `icon = GFX_decision_ENG_ww1_empire_policy`
  - `allowed = { tag = ENG }`
  - `visible = { has_country_flag = ww1_britain_initialised }`

- [ ] **Step 2: Add state-targeted decisions in `ww1_britain_decisions.txt`**
  Implement:
  - `ENG_deploy_crown_garrison`:
    - `state_target = yes` for states 113, 114, 117, 119.
    - Check flag `NOT = { has_country_flag = ENG_securing_irish_state_in_progress }`.
    - Cost: 35 PP, 25,000 manpower, 500 infantry rifles.
    - Promotes state status flags (`ENG_state_garrison_secured`).
  - `ENG_raid_paramilitary_armories`: Targeted arms raids.
  - `ENG_emergency_curfew_lockdown`: Factory curfew to halt sabotage.

- [ ] **Step 3: Add strategic crisis decisions**
  Implement:
  - `ENG_larne_arms_interdiction`: Royal Navy blockade.
  - `ENG_appease_curragh_officers` & `ENG_purge_curragh_officers`.
  - `ENG_deploy_black_and_tans`: Deploys auxiliary division, imposes `ENG_irish_martial_law`.
  - `ENG_restore_order_in_ireland_act`: Track B capstone.
  - `ENG_enact_irish_free_state_treaty`: Track A capstone.

- [ ] **Step 4: Verify with Semantic Oracle**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/decisions/ww1_britain_decisions.txt')) == 0"`
  Expected: Exit code 0.

- [ ] **Step 5: Commit changes**
  Run:
  ```bash
  git add common/decisions/categories/ww1_britain_categories.txt common/decisions/ww1_britain_decisions.txt
  git commit -m "feat(uk): implement map-based state securing decisions and crisis management actions"
  ```

---

### Task 4: Historical Events & Territorial Civil War Engine (`events/ww1_britain_events.txt`)

**Files:**
- Modify: `events/ww1_britain_events.txt`

**Interfaces:**
- Consumes: States 113, 114, 117, 119; state control flags; tag `IRE`.
- Produces: Curragh Mutiny event, Gun-running events, 1916 Easter Rising overhaul, territorial civil war eruption, and immediate custom capitulation peace script.

- [ ] **Step 1: Implement Curragh Mutiny & Gun-Running events**
  - `ww1_britain_pol.curragh_mutiny` (March 1914): Choice between appeasement (drops Ulster tension, raises Nationalist tension) vs purge (`-10%` BEF org).
  - `ww1_britain_pol.larne_howth_guns` (July 1914): Weapon smuggling events.

- [ ] **Step 2: Update 1916 Easter Rising (`ww1_britain_pol.11`)**
  - Check Leinster (117) state status:
    - If `ENG_state_garrison_secured`: Garrison repels rebels swiftly.
    - If not secured: Dublin post office seized, street fighting inflicts infrastructure damage, escalates tension.

- [ ] **Step 3: Implement Civil War Eruption (`ww1_britain_pol.irish_civil_war`)**
  - Triggers if Nationalist tension >= 85 or post-Easter escalation.
  - Checks each state:
    - If `ENG_state_garrison_secured`: Remains British, spawns loyal militia.
    - If not secured: Transfers state to `IRE`.
  - Sets `IRE = { add_rule = { can_join_factions = no } }`.
  - Spawns 6 insurgent IRA divisions for `IRE`.
  - Declares war between `ENG` and `IRE`.
  - Swaps Pillar 5 to `ENG_irish_civil_war_debacle`.

- [ ] **Step 4: Implement Immediate Capitulation Peace Script (`ww1_britain_pol.ireland_pacified`)**
  - Triggered on capitulation of `IRE` or recapture of Dublin (117).
  - Fully annexes `IRE` back into `ENG`.
  - Removes rebel divisions and swaps to `ENG_irish_union_secured`.

- [ ] **Step 5: Commit changes**
  Run:
  ```bash
  git add events/ww1_britain_events.txt
  git commit -m "feat(uk): implement historical crisis events and localized territorial civil war engine"
  ```

---

### Task 5: Focus Tree Integration (`common/national_focus/uk.txt`)

**Files:**
- Modify: `common/national_focus/uk.txt`

**Interfaces:**
- Consumes: Focus `ENG_ww1_the_defence_of_the_realm` (DORA, 1914), `ENG_ww1_the_irish_settlement_conference`, `ENG_ww1_dominion_status_for_ireland`.
- Produces: Synchronized focus rewards that start the Easter Rising timer instead of wiping the crisis.

- [ ] **Step 1: Update `ENG_ww1_the_defence_of_the_realm`**
  Modify focus completion reward:
  - Swaps `ENG_irish_home_rule_tension` to `ENG_irish_home_rule_suspended`.
  - Sets country flag `ENG_ww1_dora_enacted` and `ENG_ww1_easter_rising_countdown_started`.

- [ ] **Step 2: Align post-war settlement focuses**
  - Ensure `ENG_ww1_dominion_status_for_ireland` awards `ENG_irish_home_rule_compromise` via `swap_ideas`.

- [ ] **Step 3: Verify focus tree syntax and anti-stacking limits**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_anti_stacking_limits`
  Expected: PASS.

- [ ] **Step 4: Commit changes**
  Run:
  ```bash
  git add common/national_focus/uk.txt
  git commit -m "feat(uk): align DORA wartime focus and post-war settlement with Irish crisis engine"
  ```

---

### Task 6: Bilingual Localisation & UTF-8 BOM (`localisation/`)

**Files:**
- Modify: `localisation/english/ww1_britain_l_english.yml`
- Modify: `localisation/braz_por/ww1_britain_l_braz_por.yml`

**Interfaces:**
- Consumes: Keys for new ideas, decisions, states, and events.
- Produces: 100% bilingual text parity with UTF-8 BOM encoding.

- [ ] **Step 1: Add all new keys to English and Portuguese dictionaries**
  Localize:
  - Ideas: `ENG_irish_sabotage_wave`, `ENG_irish_martial_law`, `ENG_irish_civil_war_debacle`, `ENG_irish_union_secured`.
  - State modifiers: `ENG_state_garrison_secured`, `ENG_state_contested_unrest`, `ENG_state_rebel_stronghold`.
  - Decisions: Category title, state-securing actions, and dilemma tooltips.
  - Events: Curragh mutiny, gun-running, Easter rising outcomes, and civil war dispatches.

- [ ] **Step 2: Write both files with UTF-8 BOM (`\xef\xbb\xbf`)**
  Run consolidation script or direct encode.

- [ ] **Step 3: Verify BOM and key parity**
  Run: `python -c "open('localisation/english/ww1_britain_l_english.yml', 'rb').read(3) == b'\xef\xbb\xbf' and open('localisation/braz_por/ww1_britain_l_braz_por.yml', 'rb').read(3) == b'\xef\xbb\xbf'"`
  Expected: True.

- [ ] **Step 4: Commit localization**
  Run:
  ```bash
  git add localisation/
  git commit -m "feat(uk): add complete bilingual localization with UTF-8 BOM for Irish crisis engine"
  ```

---

### Task 7: Master QA Suite Run & Verification (GREEN Phase)

**Files:**
- Test: `tests/test_ww1_britain_complete_audit.py`
- Test: `scripts/qa_audit_all.py`

**Interfaces:**
- Consumes: All modified mod files across `common/`, `events/`, `localisation/`.
- Produces: Zero failures across all tiers and complete audit pass.

- [ ] **Step 1: Execute `test_ww1_britain_complete_audit.py`**
  Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`
  Expected: PASS (all tests pass).

- [ ] **Step 2: Execute Master QA Runner `scripts/qa_audit_all.py`**
  Run: `python scripts/qa_audit_all.py`
  Expected: Exit code 0 (all tiers pass, 0 issues found).

- [ ] **Step 3: Final Git Commit and State Validation**
  Run:
  ```bash
  git status
  ```
  Expected: Working tree clean.
