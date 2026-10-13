# Task 4 Report: Pre-Revolutionary Crisis Engine & Visual Decisions Dashboard (Late 1915 – Mid 1917)

## Summary of Completed Work
Successfully implemented the pre-revolutionary crisis engine, visual decision dashboard, 4 clamped gauges, dual catalysts for Lenin's return, and crisis resolution paths (Imperial Salvation vs Storming of the Winter Palace).

### 1. Scripted Effects (`common/scripted_effects/ww1_russia_crisis_effects.txt`)
- `sov_russia_init_crisis_gauges`:
  - `SOV_revolutionary_tension = 15`
  - `SOV_worker_unrest = 20`
  - `SOV_urban_hunger = 10`
  - `SOV_army_loyalty = 80`
  - Sets `SOV_crisis_gauges_initialized`
- `sov_russia_clamp_crisis_gauges`:
  - Clamps all 4 variables strictly between 0 and 100 via Clausewitz `clamp_variable`.
- `sov_russia_weekly_crisis_update`:
  - Evaluates war weariness, casualties, stability, surrender progress, and shell shortage effects on unrest, hunger, and army loyalty.
  - Recomputes pressure on `SOV_revolutionary_tension` from `0.40 * unrest + 0.30 * hunger + 0.30 * (100 - loyalty)`, plus a +15 pressure boost if Lenin has returned.
  - Adjusts tension towards calculated pressure.
  - Enforces `sov_russia_clamp_crisis_gauges = yes`.
  - Revolution trigger: If `SOV_revolutionary_tension >= 85`, sets flag `SOV_revolution_triggered` and fires `ww1_russia.310` (*Storming of the Winter Palace*).
  - Autonomous fallback: If `date > 1917.3.1` and Lenin has not returned yet, fires `ww1_russia.301`.
  - Order restored: If `date > 1917.11.1` and `SOV_revolutionary_tension < 50`, fires `ww1_russia.305` (*Triumph of Order*).

### 2. Visual Decision Dashboard & Categories (`common/decisions/categories/ww1_russia_crisis_categories.txt` & `common/decisions/ww1_russia_crisis_decisions.txt`)
- Category `SOV_revolutionary_crisis_category`:
  - Priority 100, visible for SOV when crisis variables are active and government is not communist.
  - Displays dynamic gauge status and formatted progress bar `SOV_crisis_tension_bar_tt`: `§R[████████░░] [?SOV_revolutionary_tension|0%]§!`.
- 4 Decision actions:
  - `SOV_crisis_emergency_grain_requisitions`: Hunger -10, Unrest +5, Cost 25 PP.
  - `SOV_crisis_bread_price_subsidies`: Hunger -15, Tension -5, Cost 30 PP.
  - `SOV_crisis_okhrana_sweeps`: Unrest -15, Tension -10, Cost 50 PP.
  - `SOV_crisis_imperial_frontline_tour`: Loyalty +15, Tension -5, Cost 40 PP.
  - All decisions call `sov_russia_clamp_crisis_gauges = yes`.

### 3. Events (`events/ww1_russia_crisis_events.txt`)
- `ww1_russia.300`: Lenin Arrives via German Sealed Train (fired from German decision `GER_operation_sealed_train`). Sets `SOV_lenin_returned`, Tension +25, Unrest +20. Clamps gauges.
- `ww1_russia.301`: Autonomous March 1917 Fallback. Sets `SOV_lenin_returned`, Tension +20. Clamps gauges.
- `ww1_russia.305`: Triumph of Order. Adds `SOV_order_restored_spirit`, sets flag `SOV_order_restored`, grants +15% stability & war support.
- `ww1_russia.310`: Storming of the Winter Palace. Sets flag `SOV_revolution_triggered`, paving the way for the Civil War.

### 4. Integration & On-Actions (`common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt` & `common/decisions/ww1_ger_rus_rework_decisions.txt`)
- Hooked `sov_russia_weekly_crisis_update` into `on_weekly_SOV` with safe auto-initialization of gauges.
- Updated German decision `GER_operation_sealed_train` to dispatch `ww1_russia.300` to Russia in addition to `ww1_russia.250`.
- Documented 1918 armistice hook for Brest-Litovsk dissolution.

### 5. Localization
- Updated English and Brazilian Portuguese event & decision localizations (`ww1_russia_events_l_english.yml` and `ww1_russia_events_l_braz_por.yml`) with 100% key parity (72 keys each) and strictly single UTF-8 BOM encoding.

## Verification Summary
- **Unit Test**: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_crisis_engine_and_gauges -v` -> **PASS** (`ok` in 0.007s).
- **Semantic Oracle**: `audit_file_modifiers` returned **0 errors** across all modified/created files.
- **Bracket Audit**: All Clausewitz braces strictly balanced across all modified and newly created files.
- **BOM Audit**: Confirmed single UTF-8 BOM header (`\xef\xbb\xbf`) without double BOM across English and Brazilian Portuguese localization files.

## Git Commit
- Commit: `73587c4`
- Message: `feat(sov): implement real-time revolutionary crisis dashboard, visual progress bars, and dual catalyst`
