### Task 3: The 4 Divergent Constitutional Destinies & Focus Tree Overhaul

**Files:**
- Modify: `common/national_focus/austria.txt`
- Create: `common/ideas/ww1_austria_constitutional_ideas.txt`
- Test: `tests/test_ww1_austria_hungary.py:TestAustriaHungaryOverhaul.test_constitutional_four_paths`

**Interfaces:**
- Consumes: Focus grid topology standards from `hoi4-focus-tree-designer` skill.
- Produces: 4 mutually exclusive constitutional branches: Dualism of Iron (`AUH_ww1_dualism`), Habsburg Trialism (`AUH_ww1_trialism`), Danubian Mega-Federation (`AUH_ww1_federalism`), and AOK Military Dictatorship (`AUH_ww1_military_dictatorship`).

- [ ] **Step 1: Write test assertions in `test_constitutional_four_paths`**
  Assert `AUH_ww1_dualism`, `AUH_ww1_trialism`, `AUH_ww1_federalism`, and `AUH_ww1_military_dictatorship` exist in `common/national_focus/austria.txt`, are mutually exclusive, have distinct valid ideas (`AUH_idea_dualism_iron`, `AUH_idea_habsburg_trialism`, `AUH_idea_danubian_federation_spirit`, `AUH_idea_aok_military_dictatorship`), and have 0 coordinate collisions.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_constitutional_four_paths -v`
  Expected: FAIL (`AUH_ww1_military_dictatorship` not found or mutual exclusivity incomplete).

- [ ] **Step 3: Implement the 4 constitutional branches and national ideas**
  - In `common/national_focus/austria.txt`:
    - Restructure the political opening under `AUH_ww1_constitutional_audit`.
    - Branch 1: `AUH_ww1_dualism` -> `AUH_ww1_tisza_alliance` -> `AUH_ww1_magyar_cavalry_corps`.
    - Branch 2: `AUH_ww1_trialism` -> `AUH_ww1_zagreb_coronation` -> `AUH_ww1_pacify_south_slavs`.
    - Branch 3: `AUH_ww1_federalism` -> `AUH_ww1_popovici_manifesto` -> `AUH_ww1_proclaim_danubian_federation`.
    - Branch 4: `AUH_ww1_military_dictatorship` -> `AUH_ww1_conrad_supreme_command` -> `AUH_ww1_war_surveillance_office`.
    - Set mutual exclusivity across all 4 branches.
  - In `common/ideas/ww1_austria_constitutional_ideas.txt`:
    - Define ideas with verified Clausewitz modifiers from `data/hoi4_valid_country_modifiers.json`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_constitutional_four_paths -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/national_focus/austria.txt common/ideas/ww1_austria_constitutional_ideas.txt
  git commit -m "feat(auh): implement 4 divergent constitutional paths and authentic national ideas"
  ```

---

