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

