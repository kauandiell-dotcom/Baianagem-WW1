### Task 5: Multi-Front Russian Civil War Engine & Breakaway Powderkeg

**Files:**
- Create: `events/ww1_russia_civil_war_events.txt`
- Create: `history/units/SOV_red_army_civil_war.txt`
- Create: `history/units/WHT_white_army_civil_war.txt`
- Create: `history/units/UKR_civil_war.txt`
- Create: `history/units/FIN_civil_war.txt`
- Create: `history/units/POL_civil_war.txt`
- Create: `common/decisions/ww1_soviet_civil_war_decisions.txt`

**Interfaces:**
- Consumes: Event `ww1_russia.310` trigger.
- Produces: Tag partition (`SOV` vs `WHT`), breakaway war declarations (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`), fleet split, and combat OOBs.

- [ ] **Step 1: Create Dedicated Civil War OOBs**
  - `SOV_red_army_civil_war.txt`: 50 divisions of Red Guards, Workers' Battalions, Baltic Sailors.
  - `WHT_white_army_civil_war.txt`: 45 divisions of Siberian Riflemen, Volunteer Army, Cossack Cavalry.
  - Regional OOBs for `UKR` (14 divs), `FIN` (10 divs), `POL` (16 divs).

- [ ] **Step 2: Implement Civil War Eruption Script in `ww1_russia_civil_war_events.txt`**
  In `ww1_russia.310`:
  - Choice A: Player plays `SOV` (Soviets).
  - Choice B: Player plays `WHT` (Whites via `change_tag_from = SOV`).
  - Scripted immediate:
    - Disbands old imperial army via `delete_unit_template_and_units`.
    - Transfers Siberia, Urals, and South to `WHT`.
    - Splits fleet: Baltic Fleet to `SOV`, Black Sea Fleet to `WHT`.
    - Splits stockpiles 50/50.
    - Spawns breakaways (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`) and declares mutual war with `SOV` and `WHT`.
    - Sets `prevent_join_factions = yes` on `SOV` and `WHT`.

- [ ] **Step 3: Implement Map-Based War Communism & Kazan Gold Decisions**
  In `ww1_soviet_civil_war_decisions.txt`:
  - *Seize the Kazan Gold Reserves*, *Prodrazvyorstka Grain Expeditions*, *Mobilize Petrograd Workers*, *Trotsky's Armored Train Inspection*.

- [ ] **Step 4: Verify Civil War Mechanics & Bracket Balance**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_civil_war_spawns_and_oobs -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add events/ww1_russia_civil_war_events.txt history/units/ common/decisions/ww1_soviet_civil_war_decisions.txt
  git commit -m "feat(sov): implement multi-front Russian Civil War engine, breakaway nations, and combat OOBs"
  ```

---

