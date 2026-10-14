### Task 2: Belgian Supply Hubs, Railway Infrastructure & Luxembourg Integration

**Files:**
- Modify: `history/states/34-Flanders.txt`
- Modify: `history/states/35-Wallonia.txt`
- Modify: `history/states/8-Luxemburg.txt` (or valid Luxembourg state file)
- Modify: `map/railways.txt` (or state railway definitions if defined in history)
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_belgian_railways_and_supply`

**Interfaces:**
- Consumes: Valid province IDs for Liège (state 35) and Namur (state 34)
- Produces: Upgraded supply hubs and level 3 railway connections to Aachen and Cologne

- [ ] **Step 1: Inspect Belgian and border province IDs**
Identify valid victory point and province IDs in states 34, 35, 8, 42, 52 using Python script.

- [ ] **Step 2: Implement supply hubs and level 3 railways**
Add `supply_hub` entries in state 35 (Liège) and state 34 (Namur/Brussels), and configure railways connecting them directly to Rhineland hubs (Aachen/Cologne).

- [ ] **Step 3: Configure Luxembourg Day 1 integration**
Ensure state 8 has appropriate infrastructure and can be seamlessly absorbed on Day 1 of the Western March.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_belgian_railways_and_supply -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add history/states/ map/
git commit -m "feat(map): upgrade Belgian supply hubs, railway tiers, and Luxembourg border infrastructure"
```

---

