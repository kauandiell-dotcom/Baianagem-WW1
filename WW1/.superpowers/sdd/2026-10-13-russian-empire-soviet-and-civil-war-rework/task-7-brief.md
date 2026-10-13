### Task 7: Dedicated Soviet Russia Focus Tree (`common/national_focus/soviet_russia.txt` — 80 Focuses)

**Files:**
- Create: `common/national_focus/soviet_russia.txt`

**Interfaces:**
- Consumes: Loaded via `load_focus_tree = soviet_russia_focus` upon Bolshevik victory/takeover.
- Produces: 80 bespoke focuses across 5 wings (War Communism, Red Army, GOELRO/NEP, Comintern, Formation of USSR 1922).

- [ ] **Step 1: Construct 5-Wing Non-Colliding Layout Grid**
  Ensure all 80 focuses follow standard spatial grid mathematics:
  - Adjacent focuses on the same row: $|x_2 - x_1| \ge 2$.
  - Parent-child links: $1 \le child\_y - parent\_y \le 3$.
  - 0 coordinate collisions.

- [ ] **Step 2: Script Focuses with Tangible Rewards**
  - Wing 1: War Communism & Red Terror (16 focuses).
  - Wing 2: Red Army Doctrine & Military Commissars (18 focuses).
  - Wing 3: GOELRO & Economic Reconstruction - NEP vs Superindustrialization (16 focuses).
  - Wing 4: Comintern & World Revolution - Polish-Soviet War & Rapallo (16 focuses).
  - Wing 5: State Building & Formation of the USSR 1922 (14 focuses).

- [ ] **Step 3: Run Focus Grid & Syntax Audit**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_soviet_focus_tree_integrity -v`
  Expected: PASS (80 focuses, 0 collisions, 0 hollow rewards).

- [ ] **Step 4: Commit**
  ```bash
  git add common/national_focus/soviet_russia.txt
  git commit -m "feat(sov): implement dedicated 80-focus Soviet Russia national focus tree"
  ```

---

