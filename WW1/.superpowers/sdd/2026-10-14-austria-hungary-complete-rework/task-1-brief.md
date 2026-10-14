### Task 1: QA RED Test Baseline (`tests/test_ww1_austria_hungary.py`)

**Files:**
- Create: `tests/test_ww1_austria_hungary.py`
- Modify: `scripts/qa_audit_all.py`
- Test: `tests/test_ww1_austria_hungary.py`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Produces: Test class `TestAustriaHungaryOverhaul` with 7 comprehensive test methods to drive TDD.

- [ ] **Step 1: Write the failing test suite `tests/test_ww1_austria_hungary.py`**
  ```python
  import os
  import re
  import unittest

  REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  class TestAustriaHungaryOverhaul(unittest.TestCase):
      def test_austria_no_day1_crisis(self):
          """Verify that collapse and crisis events cannot trigger on Day 1 (1911)."""
          ...
      def test_constitutional_four_paths(self):
          """Verify that the 4 constitutional paths (Dualism, Trialism, Danubian Mega-Federation, Military Dictatorship) are properly defined and mutually exclusive."""
          ...
      def test_danubian_mega_federation_setup(self):
          """Verify that Danubian federation releases HUN, CZE, CRO, POL with imperial color matching and 4-18 divisions."""
          ...
      def test_tag_safe_breakaway_rules(self):
          """Verify that seceding tags have can_join_factions = no and 0 dynamic start_civil_war calls."""
          ...
      def test_crown_dashboard_and_grain(self):
          """Verify the 3 survival vectors (weariness, cohesion, grain) and their decisions."""
          ...
      def test_skoda_and_three_armies_modifiers(self):
          """Verify that all ideas use valid Clausewitz modifiers via semantic oracle."""
          ...
      def test_localisation_bom_and_parity(self):
          """Verify single UTF-8 BOM and 100% key parity between English and Portuguese."""
          ...
  ```

- [ ] **Step 2: Run test to verify it fails (RED phase)**
  Run: `python -m unittest tests.test_ww1_austria_hungary -v`
  Expected: FAIL on unbuilt components.

- [ ] **Step 3: Register test suite in `scripts/qa_audit_all.py` as Suite 12**
  Add `tests.test_ww1_austria_hungary` to the test runner array in `scripts/qa_audit_all.py`.

- [ ] **Step 4: Verify test runner executes `test_ww1_austria_hungary`**
  Run: `python scripts/qa_audit_all.py`
  Expected: Suite 12 fails with expected missing features.

- [ ] **Step 5: Commit**
  ```bash
  git add tests/test_ww1_austria_hungary.py scripts/qa_audit_all.py
  git commit -m "test(auh): establish RED QA test suite for Austria-Hungary complete rework"
  ```

---

