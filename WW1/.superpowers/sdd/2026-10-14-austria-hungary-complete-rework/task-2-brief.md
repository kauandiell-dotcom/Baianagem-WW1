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

