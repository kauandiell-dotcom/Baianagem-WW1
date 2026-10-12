# Task 1: Q.A Audit Test Suite Expansion (RED Phase)

**Files:**
- Modify: `tests/test_ww1_britain_complete_audit.py`

**Interfaces:**
- Consumes: `tests/test_ww1_britain_complete_audit.py`, `scripts/hoi4_semantic_oracle.py`
- Produces: Failing unit tests proving that new ideas, state-securing mechanics, and civil war events are not yet present.

- [ ] **Step 1: Write failing tests in `tests/test_ww1_britain_complete_audit.py`**
  Add `test_irish_crisis_escalation_and_state_securing_mechanics`:
  - Assert `ENG_irish_home_rule_tension` in `common/ideas/ww1_britain_ideas.txt` has `stability_factor <= -0.30` and `war_support_factor <= -0.10`.
  - Assert `ENG_irish_sabotage_wave`, `ENG_irish_martial_law`, `ENG_irish_civil_war_debacle`, `ENG_irish_union_secured` exist in `ww1_britain_ideas.txt`.
  - Assert decision category `ENG_ww1_irish_crisis_category` exists in `common/decisions/categories/ww1_britain_categories.txt`.
  - Assert state securing decisions exist in `common/decisions/ww1_britain_decisions.txt` (`ENG_deploy_crown_garrison`, `ENG_raid_paramilitary_armories`).
  - Assert civil war event `ww1_britain_pol.irish_civil_war` exists in `events/ww1_britain_events.txt`.

- [ ] **Step 2: Run test suite to verify RED failure**
  Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`
  Expected: FAIL (identifying missing ideas and categories).

- [ ] **Step 3: Commit RED test changes**
  Run:
  ```bash
  git add tests/test_ww1_britain_complete_audit.py
  git commit -m "test(uk): add test cases for Irish crisis escalation and state securing engine (RED)"
  ```
