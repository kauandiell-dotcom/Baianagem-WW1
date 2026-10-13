### Task 6: Central Powers Interaction, Brest-Litovsk & Entente Proxy Aid

**Files:**
- Create: `events/ww1_russia_diplomacy_events.txt`
- Create: `common/decisions/ww1_soviet_diplomacy_decisions.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

**Interfaces:**
- Consumes: `SOV` Soviet government, `GER` existence, German 1918 armistice trigger.
- Produces: Treaty of Brest-Litovsk exit from WW1, Operation Faustschlag, Entente proxy aid for `WHT`, and 1918 dissolution of Brest-Litovsk.

- [ ] **Step 1: Implement Brest-Litovsk Decision & Event Chain**
  - `SOV_decree_on_peace`: opens diplomatic delegation with Germany.
  - Germany offers terms: ceding western borderlands.
  - If accepted: `SOV` exits war with Central Powers; `GER` gains `GER_brest_litovsk_deliveries` trade bonuses.
  - If rejected ("Neither War nor Peace"): Germany executes *Operation Faustschlag*.

- [ ] **Step 2: Implement Entente Proxy Decisions for `WHT`**
  - *General Knox British Mission*, *French Odessa Convoys*, *Vladivostok Lend-Lease*.
  - Grants equipment, subsidies, and off-map factory bonuses without dragging the Entente into total war.

- [ ] **Step 3: Implement 1918 German Armistice Dissolution Hook**
  In `zz_ww1_ger_rus_rework_on_actions.txt`:
  When Germany signs armistice / capitulates in late 1918:
  - Voids Brest-Litovsk deliveries.
  - Collapses German occupation in Ukraine/Belarus/Baltics.
  - Triggers Soviet *Target Vistula* westward reclamation.

- [ ] **Step 4: Verify Diplomacy Events & Modifier Oracle**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_brest_litovsk_and_diplomacy -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_russia_diplomacy_events.txt common/decisions/ww1_soviet_diplomacy_decisions.txt common/on_actions/
  git commit -m "feat(sov): implement Treaty of Brest-Litovsk, Entente proxy intervention, and armistice dissolution"
  ```

---

