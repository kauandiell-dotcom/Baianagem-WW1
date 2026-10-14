# Supreme Engine Optimization & Late-Game Simulation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement an unprecedented engine-level performance optimization overhaul for Baianagem-WW1 based on reverse-engineered Clausewitz defines, eliminating midnight lag, log accumulation, and AI micro-spam to enable smooth gameplay even on 2–4 GB RAM PCs with zero visual or mechanical degradation.

**Architecture:** A multi-layered architecture combining high-precedence engine defines (`common/defines/99_supreme_performance.lua`), declarative peacetime AI division limits (`common/ai_strategy/ww1_performance_ai_limiter.txt`), monthly transient memory garbage collection (`common/scripted_effects/ww1_optimization_effects.txt`), and decision trigger pre-filtering to eliminate single-core bottlenecks and serialization overhead.

**Tech Stack:** Paradox Clausewitz Engine (HOI4 1.14+), Lua 5.1, Python 3.12 (unittest QA verification suite), Steam Workshop content mirroring.

**Spec:** `docs/superpowers/specs/2026-10-14-supreme-engine-optimization-design.md`

## Global Constraints

- **Zero Visual Degradation:** Zero removal or downscaling of 3D models, textures, unit icons, or GFX.
- **Zero Gameplay Removal:** All focus trees, events, decisions, and warfare mechanics remain fully functional.
- **Clausewitz Syntax Compliance:** 100% valid Lua and Paradox Clausewitz bracket matching (diff = 0).
- **RAM Target:** Calibrated to relieve memory pressure and prevent swapping on 2–4 GB RAM systems.
- **Multiplayer Netcode Integrity:** Deterministic lockstep synchronization, no OOS, and preservation of `LAG_DAYS_FOR_LOWER_SPEED = 100`.
- **Workshop Mirroring:** All changes committed to git must be immediately synchronized with `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus

1. **Host-Client Lockstep Desyncs:** Ensure `LAG_DAYS_FOR_LOWER_SPEED = 100` and `LAG_DAYS_FOR_PAUSE = 120` are preserved when consolidating defines, preventing the "frozen client" bug.
2. **AI Combat Production Stalling:** Ensure peacetime division caps only apply to non-major, non-faction, non-war AI tags and abort immediately when at war (`abort_when_not_enabled = yes`).
3. **Save Game Serialization Corruption:** Ensure combat log reduction (`COMBAT_LOG_MAX_MONTHS = 1`) preserves UI battle report readability while eliminating midnight freezes.
4. **Transient Flag Pruning Safety:** Ensure `ww1_clean_transient_memory` only clears transient operational flags and never touches persistent tree, civil war, or peace progression flags.
5. **Generic Formable Decisions Integrity:** Ensure decision `allowed` tag scoping only targets country-specific files, keeping generic formables and player mechanics accessible.

---

### Task 1: QA RED Test Baseline (`tests/test_ww1_supreme_optimization.py`)

**Files:**
- Create: `tests/test_ww1_supreme_optimization.py`
- Modify: `scripts/qa_audit_all.py`

**Steps:**
- [ ] Create `tests/test_ww1_supreme_optimization.py` defining `TestSupremeOptimization` with 5 test methods:
  1. `test_supreme_performance_defines_syntax_and_values`: Asserts `common/defines/99_supreme_performance.lua` exists, parses as valid Lua, and contains all critical log, tick, and render constants from the spec.
  2. `test_combat_log_memory_limits`: Confirms `COMBAT_LOG_MAX_MONTHS <= 2`, `GARRISON_LOG_MAX_MONTHS <= 2`, and `AIR_LOG_TIMEOUT_HOURS <= 48`.
  3. `test_render_pass_tessellation_optimization`: Confirms spline smoothing passes (`ROOT_FRONT_SMOOTHEN_PASSES`, `SUPPLYFLOW_SMOOTHEN_PASSES`, `TRADEROUTE_SMOOTHEN_PASSES`) are set to 1.
  4. `test_ai_peacetime_division_regulation`: Asserts `common/ai_strategy/ww1_performance_ai_limiter.txt` includes `ww1_peace_neutral_minor_limiter` targeting non-belligerent neutral minors.
  5. `test_transient_memory_cleanup_registered`: Asserts `ww1_clean_transient_memory` exists in `common/scripted_effects/` and is called in `on_monthly` within `common/on_actions/`.
- [ ] Register the new test suite in `scripts/qa_audit_all.py`.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization -v` and verify tests fail (RED phase) on unbuilt components.
- [ ] Commit: `git commit -m "test(perf): establish RED QA test suite for supreme engine optimization"`

---

### Task 2: Reverse-Engineered Engine Defines Consolidation (`common/defines/99_supreme_performance.lua`)

**Files:**
- Create: `common/defines/99_supreme_performance.lua`
- Delete: `common/defines/99_slowdown.lua`

**Steps:**
- [ ] Create `common/defines/99_supreme_performance.lua` containing all reverse-engineered engine defines:
  - History & memory: `COMBAT_LOG_MAX_MONTHS = 1`, `AIR_LOG_TIMEOUT_HOURS = 24`, `TRADE_ROUTE_RECALCULATE_FREQUENCY_DAYS = 10`, `GARRISON_LOG_MAX_MONTHS = 1`, `NAVAL_ACCIDENTS_DAYS_TO_LIVE = 14`.
  - Multiplayer netcode: `LAG_DAYS_FOR_LOWER_SPEED = 100`, `LAG_DAYS_FOR_PAUSE = 120`.
  - Simulation tick throttling: `UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 72`, `UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS = 72`, `RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 14`, `RAIDS_CREATE_FREQUENCY_DAYS = 14`, `ATTACHED_WINGS_ORDER_UPDATE_DAYS = 5`, `REINFORCEMENT_REQUEST_DAYS_FREQUENCY = 4`, `AI_THEATRE_STATE_UPDATE_MAX_STATE_COUNT_TO_EXPAND = 10`.
  - Geometry & render passes: `ROOT_FRONT_SMOOTHEN_PASSES = 1`, `ROOT_FRONT_MAX_INTERSECTION_TESTS_FRONT = 4`, `SNAPPED_OFF_FRONT_SMOOTHEN_PASSES = 1`, `SUPPLYFLOW_SMOOTHEN_PASSES = 1`, `TRADEROUTE_SMOOTHEN_PASSES = 1`, `TRADE_ROUTE_MAX_LINES = 12`, `WEATHER_DISTANCE_CUTOFF = 350.0`, `WEATHER_PLAYBACK_RATE = 0.6`, `UNITS_DISTANCE_CUTOFF = 180.0`, `CITY_SPRAWL_SHRINK_DISTANCE = 140.0`, `PROVINCE_NAME_DRAW_DISTANCE = 220.0`, `SHIPS_DISTANCE_CUTOFF = 180.0`, `TOP_MAP_ICON = 40`.
- [ ] Remove obsolete `common/defines/99_slowdown.lua` to prevent duplicate define definitions.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization.TestSupremeOptimization.test_supreme_performance_defines_syntax_and_values -v`.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization.TestSupremeOptimization.test_combat_log_memory_limits -v`.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization.TestSupremeOptimization.test_render_pass_tessellation_optimization -v`.
- [ ] Commit: `git commit -m "feat(defines): implement reverse-engineered supreme engine performance defines"`

---

### Task 3: Peacetime Neutral Minor Division Regulation (`common/ai_strategy/ww1_performance_ai_limiter.txt`)

**Files:**
- Modify: `common/ai_strategy/ww1_performance_ai_limiter.txt`

**Steps:**
- [ ] Append the declarative peacetime neutral minor division limiter to `common/ai_strategy/ww1_performance_ai_limiter.txt`:
  ```clausewitz
  ww1_peace_neutral_minor_limiter = {
      enable = {
          is_ai = yes
          is_major = no
          has_war = no
          is_in_faction = no
          num_of_military_factories < 6
          num_divisions > 8
      }
      abort_when_not_enabled = yes
      ai_strategy = {
          type = ai_wanted_divisions_factor
          value = -100
      }
      ai_strategy = {
          type = equipment_stockpile_surplus_ratio
          value = 40
      }
  }
  ```
- [ ] Verify bracket balance in `common/ai_strategy/ww1_performance_ai_limiter.txt`.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization.TestSupremeOptimization.test_ai_peacetime_division_regulation -v`.
- [ ] Commit: `git commit -m "feat(ai): curb peacetime neutral minor division spam via declarative ai_strategy"`

---

### Task 4: Transient Memory Garbage Collection & On-Action Hook (`common/scripted_effects/ww1_optimization_effects.txt`)

**Files:**
- Create: `common/scripted_effects/ww1_optimization_effects.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

**Steps:**
- [ ] Create `common/scripted_effects/ww1_optimization_effects.txt` defining `ww1_clean_transient_memory`:
  - Clears transient operational flags on capitulated nations.
  - Resets temporary local combat modifiers and expired tactical event cooldowns.
- [ ] In `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`, hook `ww1_clean_transient_memory` under `on_monthly`.
- [ ] Check bracket matching across both files.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization.TestSupremeOptimization.test_transient_memory_cleanup_registered -v`.
- [ ] Commit: `git commit -m "feat(perf): add monthly transient memory garbage collection effect and on-action hook"`

---

### Task 5: Decision Allowed Tag Scoping Audit

**Files:**
- Modify: Target country decision files in `common/decisions/` lacking top-level category `allowed` or explicit decision `allowed` guards.

**Steps:**
- [ ] Audit decision files in `common/decisions/` to ensure country-specific categories have explicit `allowed = { ... }` blocks.
- [ ] For any country-specific decision category lacking `allowed`, add fast-failing `allowed = { tag = TAG }` or `allowed = { original_tag = TAG }`.
- [ ] Verify bracket matching across all modified files.
- [ ] Run `python -m unittest tests.test_ww1_supreme_optimization -v`.
- [ ] Commit: `git commit -m "fix(decisions): enforce fast-failing tag guards to accelerate decision trigger evaluation"`

---

### Task 6: Master QA Verification, Workshop Mirroring & Deployment

**Files:**
- Modify: `scripts/qa_audit_all.py`
- Mirror Target: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

**Steps:**
- [ ] Run `python scripts/qa_audit_all.py` and verify all 11 test suites pass with 0 errors.
- [ ] Mirror all mod repository files from `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1` to Steam Workshop folder `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.
- [ ] Push all commits to `origin/main`.
- [ ] Present completion summary to user.
