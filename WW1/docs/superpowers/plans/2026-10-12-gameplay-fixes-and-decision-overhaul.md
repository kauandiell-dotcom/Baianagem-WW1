# Gameplay Fixes & Complete Decision/Focus Reward Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the 4 major gameplay bugs reported by the player (Central Powers inverted faction logic, repeated Libyan transfer ultimatums, missing opinion modifiers causing `Opinion 0`, and decisions/focuses lacking tangible gameplay rewards), delivering rich, impactful rewards across Britain, Ottoman Empire, and Italy.

**Architecture:** 
1. Re-structure faction joining commands in Clausewitz scripting so minors join the major's faction rather than disbanding/stealing the major's alliance.
2. Add state ownership guards (`448 = { is_owned_by = TUR }`) and `fire_only_once = yes` to diplomatic ultimatum chains.
3. Establish a master opinion modifier dictionary in `common/opinion_modifiers/` to prevent `Opinion 0` engine fallbacks.
4. Upgrade all shallow focuses and decisions across UK, TUR, and ITA with tangible state constructions (factories, infrastructure, bunkers), equipment stockpiles, experience, and custom tooltips.

**Tech Stack:** Hearts of Iron IV Clausewitz Scripting, Python Unittest QA Suite, Paradox YAML Localisation with Single UTF-8 BOM.

**Spec:** User feedback from 4 game screenshots:
- Print 1: `TUR_join_central_powers_faction` makes Germany leave Central Powers.
- Print 2: Italy repeatedly sends `Diplomatic Proposal on Libya` (3+ times) even after already owning Libya.
- Print 3: Decisions like `Emergency Curfew and Lockdown in Leinster` have no effect section or real impact in game.
- Print 4: Focuses show `Gains (Opinion of Bulgaria 0.)` due to missing opinion modifier definitions and shallow opinion-only rewards.

## Global Constraints
- Every modified `.yml` file MUST strictly maintain a SINGLE UTF-8 BOM (`\xef\xbb\xbf`).
- Decisions MUST enclose `civilian_factory_use` inside `modifier = { ... }`.
- Scripted variables and flags MUST be paired with `custom_effect_tooltip` or visible game effects (`add_stability`, `add_compliance`, `add_building_construction`).
- No focus or decision may have an empty or purely cosmetic effect.

## Review Focus
1. `TUR_join_central_powers_faction`: Germany stays leader of Central Powers; Turkey joins it.
2. `ww1_italy.51`: Never triggers if Italy already controls or owns Tripoli/Libya (state 448).
3. `common/opinion_modifiers/ww1_shared_opinion_modifiers.txt`: Contains all 251 previously missing keys (`positive_25`..`positive_100`, etc.).
4. Decisions in UK (`ww1_britain_decisions.txt`), Ottoman (`ww1_ottoman_decisions.txt`), and Italy (`ww1_italy_decisions.txt`): Display concrete in-game effects and modifiers in tooltips.
5. All 33+ unit tests in `tests/` pass with Exit Code 0.

---

### Task 1: Fix Central Powers Faction Joining Logic (Print 1)
**Files:**
- Modify: `common/national_focus/turkey.txt:2664-2678`
- Test: `tests/test_ww1_ottoman.py`

- [ ] **Step 1: Inspect `TUR_join_central_powers_faction` in `turkey.txt`**
  Ensure ROOT joins Germany's faction via `GER = { add_to_faction = ROOT }`.
- [ ] **Step 2: Add unit test assertion in `tests/test_ww1_ottoman.py`**
  Verify `TUR_join_central_powers_faction` does NOT contain bare `add_to_faction = GER`.
- [ ] **Step 3: Run test suite to verify**
  `python -m unittest tests/test_ww1_ottoman.py`
- [ ] **Step 4: Commit**
  `git commit -m "fix(tur): correct Central Powers faction joining logic"`

---

### Task 2: Fix Libya Repeating Diplomatic Ultimatum (Print 2)
**Files:**
- Modify: `common/national_focus/italy.txt:2880-2900`
- Modify: `common/decisions/ww1_italy_decisions.txt:130-155`
- Modify: `events/ww1_italy_war_events.txt:5-38`
- Test: `tests/test_ww1_italy.py`

- [ ] **Step 1: Add ownership guards to `ww1_italy.51`**
  Add `trigger = { tag = TUR 448 = { is_owned_by = TUR } NOT = { ITA = { controls_state = 448 } } }`.
- [ ] **Step 2: Guard Italy focus `ITA_ww1_ultimatum_to_the_porte` and decision `ITA_ww1_diplomatic_pressure_tripoli`**
  Ensure decision has `fire_only_once = yes` and requires `448 = { is_owned_by = TUR }`.
- [ ] **Step 3: Add test assertion in `tests/test_ww1_italy.py`**
  Verify `ITA_ww1_diplomatic_pressure_tripoli` is `fire_only_once = yes` and checks state 448 ownership.
- [ ] **Step 4: Commit**
  `git commit -m "fix(ita): prevent duplicate Libya ultimatums once acquired"`

---

### Task 3: Master Opinion Modifiers Database & Localization (Print 4)
**Files:**
- Create: `common/opinion_modifiers/ww1_shared_opinion_modifiers.txt`
- Create: `localisation/english/ww1_opinion_modifiers_l_english.yml`
- Create: `localisation/braz_por/ww1_opinion_modifiers_l_braz_por.yml`

- [ ] **Step 1: Audit all opinion modifier references across the mod**
  Ensure 0 undefined modifiers exist in `common/national_focus/`, `common/decisions/`, `events/`.
- [ ] **Step 2: Enforce strictly single UTF-8 BOM on localization files**
- [ ] **Step 3: Verify with Python audit script that missing count is 0**
- [ ] **Step 4: Commit**
  `git commit -m "feat(opinions): create master shared opinion modifiers and bilingual localization"`

---

### Task 4: Enrich Shallow Diplomatic Focuses Across All Nations (Print 4)
**Files:**
- Modify: `common/national_focus/turkey.txt`
- Modify: `common/national_focus/uk.txt`
- Modify: `common/national_focus/italy.txt`
- Modify: `common/national_focus/soviet.txt`
- Modify: `common/national_focus/serbia.txt`
- Modify: `common/national_focus/austria.txt`

- [ ] **Step 1: Upgrade the 27 shallow diplomatic focuses**
  Add concrete infrastructure, equipment, factories, army/navy XP, and stability rewards.
- [ ] **Step 2: Run semantic oracle and syntax audits on modified focus files**
- [ ] **Step 3: Commit**
  `git commit -m "feat(focus): enrich shallow diplomatic focuses with tangible gameplay rewards"`

---

### Task 5: Decision Overhaul with Tangible Effects & Tooltips (Print 3)
**Files:**
- Modify: `common/decisions/ww1_britain_decisions.txt`
- Modify: `common/decisions/ww1_ottoman_decisions.txt`
- Modify: `common/decisions/ww1_italy_decisions.txt`
- Modify: `localisation/*/*.yml`

- [ ] **Step 1: Audit all decisions for invisible flags/variables and bare civilian_factory_use**
- [ ] **Step 2: Implement tangible provincial and country effects (compliance, infrastructure, equipment, stability)**
- [ ] **Step 3: Ensure `modifier = { civilian_factory_use = ... }` and `custom_effect_tooltip` are present**
- [ ] **Step 4: Commit**
  `git commit -m "feat(decisions): overhaul UK, TUR, and ITA decisions with tangible effects and tooltips"`

---

### Task 6: Master Automated QA Verification & Audit
**Files:**
- Modify: `tests/test_ww1_ottoman.py`
- Modify: `tests/test_ww1_italy.py`
- Modify: `tests/test_ww1_britain_complete_audit.py`

- [ ] **Step 1: Run complete unittest test suite**
- [ ] **Step 2: Run `python scripts/qa_audit_all.py`**
- [ ] **Step 3: Verify 100% PASS with Exit Code 0**
- [ ] **Step 4: Commit**
  `git commit -m "test(qa): add regression assertions for faction join, libya events, and decisions"`
