### Task 8: Dedicated White Movement Focus Tree (`common/national_focus/white_russia.txt` — 60 Focuses)

**Files:**
- Create: `common/national_focus/white_russia.txt`

**Interfaces:**
- Consumes: Assigned to tag `WHT` (`country = { factor = 0 modifier = { add = 10 tag = WHT } }`).
- Produces: 60 bespoke focuses across 4 wings (Omsk Directorate, AFSR, Entente Diplomacy, Post-War Restoration).

- [ ] **Step 1: Construct 4-Wing Non-Colliding Layout Grid**
  Ensure all 60 focuses follow spatial grid rules ($|x_2 - x_1| \ge 2$, $1 \le \Delta y \le 3$).

- [ ] **Step 2: Script Focuses with Tangible Rewards**
  - Wing 1: The Omsk Directorate & Supreme Ruler Kolchak (15 focuses).
  - Wing 2: Armed Forces of South Russia - Denikin, Wrangel & Cossacks (16 focuses).
  - Wing 3: Entente Intervention & Western Munitions (15 focuses).
  - Wing 4: Post-War Political Restoration - Constituent Assembly vs Military Crowned Regent (14 focuses).
  - Capstone: *Reunify the Russian State* (`change_tag_to = SOV`).

- [ ] **Step 3: Run Focus Grid & Syntax Audit**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_white_focus_tree_integrity -v`
  Expected: PASS.

- [ ] **Step 4: Commit**
  ```bash
  git add common/national_focus/white_russia.txt
  git commit -m "feat(wht): implement dedicated 60-focus White Movement national focus tree"
  ```

---

