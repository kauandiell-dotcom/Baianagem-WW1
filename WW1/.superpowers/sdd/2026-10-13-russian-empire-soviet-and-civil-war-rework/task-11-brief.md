### Task 11: Master QA Integration & Full Test Pass

**Files:**
- Modify: `scripts/qa_audit_all.py`

**Interfaces:**
- Consumes: All 10 completed rework tasks.
- Produces: 8/8 test suites passing in `scripts/qa_audit_all.py` with Exit Code 0.

- [ ] **Step 1: Register `tests/test_ww1_russia_rework.py` into `scripts/qa_audit_all.py`**
  Add test runner block for Russian Empire, Revolution, Soviet & White Civil War test suite.

- [ ] **Step 2: Run Master QA Audit**
  Run: `python scripts/qa_audit_all.py`
  Expected: All 8 test suites PASS with Exit Code 0.

- [ ] **Step 3: Commit**
  ```bash
  git add scripts/qa_audit_all.py
  git commit -m "ci(qa): integrate Russia overhaul test suite into master QA audit runner"
  ```
