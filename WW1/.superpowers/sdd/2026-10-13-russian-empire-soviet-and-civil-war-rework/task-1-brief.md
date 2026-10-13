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

