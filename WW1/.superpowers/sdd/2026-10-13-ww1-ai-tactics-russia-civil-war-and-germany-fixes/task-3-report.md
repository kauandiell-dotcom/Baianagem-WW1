# Task 3 Report: Bulgaria & Minor Belligerents AI Strategy and War Entry Engine

## Status: COMPLETE
- **Commit**: `6d2747a140c7fba1a622857151b2be631af4cf20`
- **Date**: 2026-10-13

## Summary of Changes

### 1. Direct Alliance War Entry Engine (`events/ww1_germany_events.txt`)
- Located and refactored `ww1_germany_events.33` (The Bulgarian Alliance Treaty).
- In Option A (`ww1_germany_events.33.a`):
  - Preserved Central Powers faction joining logic (`add_to_faction = ROOT`).
  - Added direct Clausewitz war declaration against Serbia (`SER`) if Germany is at war with Serbia.
  - Added dynamic enemy sweep (`every_enemy_country`) so Bulgaria enters the war against all active enemies of Germany (`FROM`) not already at war with Bulgaria.

### 2. Bulgaria Strategic AI Priorities (`common/ai_strategy/ww1_bulgaria_ai_strategy.txt`)
- Created strategic AI module for the Kingdom of Bulgaria (`BUL`):
  - `alliance id = GER value = 200`: Strong Central Powers diplomatic alignment.
  - `declare_war id = SER value = 200` & `antagonize id = SER value = 200`: Historical Balkan revanchism targeting Serbia.
  - `declare_war id = ROM value = 150`: Hostility towards Romania.
  - `front_unit_request id = SER tag = SER value = 100` and `ROM value = 75`: Border division prioritization to support the Serbian front campaign.

### 3. Grand War Front Management & Anti-Encirclement AI (`common/ai_strategy/ww1_grand_ai_strategy.txt`)
- Created frontline management rules for major powers and belligerents:
  - `ww1_major_frontline_cohesion`: Enforces `front_control` with `ratio = 0.50`, `ordertype = front`, and `execution_type = balanced`.
  - `ww1_anti_encirclement_defensive_priorities`: Triggers under pressure (`surrender_progress > 0.05`) with `ratio = 0.70`, `execution_type = careful`, and `manual_attack = no` to prevent reckless attacks and division loss.
  - `ww1_protect_capitals_and_victory_points`: Assigns increased garrison and European theater focus.

## Verification
- **Unit Test Execution**:
  ```bash
  python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_bulgaria_alliance_and_war_call -v
  ```
  Result: **OK** (PASSED in 0.002s).
- **Clausewitz Bracket Balance**:
  - `events/ww1_germany_events.txt`: `{`=497, `}`=497 (Diff = 0)
  - `common/ai_strategy/ww1_bulgaria_ai_strategy.txt`: `{`=18, `}`=18 (Diff = 0)
  - `common/ai_strategy/ww1_grand_ai_strategy.txt`: `{`=12, `}`=12 (Diff = 0)
