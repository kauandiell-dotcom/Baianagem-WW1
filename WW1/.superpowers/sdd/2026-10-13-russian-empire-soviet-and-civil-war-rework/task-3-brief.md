### Task 3: Normal Tsarist Russia (1911–1917) Gameplay Mechanics, Shell Shortage & Strategic Depth

**Files:**
- Modify: `common/ideas/ww1_russia_ideas.txt`
- Create: `common/decisions/ww1_russia_tsarist_decisions.txt`
- Create: `common/decisions/categories/ww1_russia_tsarist_categories.txt`

**Interfaces:**
- Consumes: `SOV` original tag, state targets (Poland, Baltics, Galicia).
- Produces: `SOV_strategic_depth_and_rasputitsa`, shell shortage mobilization, Duma decisions, factory evacuation, and Brusilov infiltration.

- [ ] **Step 1: Add Tsarist ideas in `common/ideas/ww1_russia_ideas.txt`**
  Add `SOV_strategic_depth_and_rasputitsa` (enemy attrition +20%, enemy supply +15%, core defense +10%).
  Add `SOV_shell_shortage_crisis` (-25% artillery soft attack, -15% breakthrough).
  Add `SOV_vpk_mobilization_spirit` (+10% artillery production speed).
  Add `SOV_rasputin_court_intrigues` (+20% political decision cost, -5% stability).

- [ ] **Step 2: Implement Decision Categories & Gameplay Decisions**
  In `ww1_russia_tsarist_decisions.txt`:
  - `SOV_duma_and_court_politics`: *Convene the Imperial Duma*, *Prorogue the Duma*, *Conspiracy to Assassinate Rasputin*.
  - `SOV_war_industry_mobilization`: *Establish VPK Committees*, *Mobilize Machine Shops*, *Zemgor Medical Union*, *British Shell Presses*.
  - `SOV_evacuate_industrial_machinery` (`state_target = yes` for Warsaw, Bialystok, Riga, Grodno): evacuates factories to Moscow/Urals and scorches earth.
  - `SOV_prepare_southwestern_offensive`: Brusilov infiltration mission against Austria-Hungary.

- [ ] **Step 3: Verify with Semantic Oracle**
  Run: `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_russia_ideas.txt')) == 0; assert len(audit_file_modifiers('common/decisions/ww1_russia_tsarist_decisions.txt')) == 0"`
  Expected: 0 errors.

- [ ] **Step 4: Commit**
  ```bash
  git add common/ideas/ww1_russia_ideas.txt common/decisions/ww1_russia_tsarist_decisions.txt common/decisions/categories/ww1_russia_tsarist_categories.txt
  git commit -m "feat(sov): implement Tsarist 1911-1917 mechanics, shell shortage, and strategic depth"
  ```

---

