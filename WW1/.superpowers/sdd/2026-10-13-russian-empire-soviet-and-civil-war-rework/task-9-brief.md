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

