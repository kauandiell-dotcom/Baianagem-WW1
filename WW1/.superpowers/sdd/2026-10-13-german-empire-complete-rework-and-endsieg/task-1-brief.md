### Task 1: QA Test Suite Baseline Expansion (RED Phase)

**Files:**
- Create: `tests/test_ww1_germany_rework.py`
- Modify: `scripts/qa_audit_all.py`

**Interfaces:**
- Consumes: `unittest`, `scripts.hoi4_semantic_oracle`, `scripts.mod_engine`
- Produces: Master test suite covering all 15 rework tasks

- [ ] **Step 1: Write the failing test suite**
Write `tests/test_ww1_germany_rework.py` with 10 comprehensive unit tests asserting:
1. `test_belgian_railways_and_supply`: Hubs exist in Liège/Namur and connect to Cologne/Aachen.
2. `test_date_gates_eliminated`: Zero `date >` triggers in `common/national_focus/germany.txt`.
3. `test_schlieffen_and_stalemate`: Fused Schlieffen focus, momentum spirit, and stalemate defense transition.
4. `test_cartels_and_chemical_warfare`: Krupp, Thyssen, Haber-Bosch, and gas escalation ideas.
5. `test_uboat_postures_and_us_tension`: Variable clamping and posture ideas.
6. `test_air_warfare_and_zeppelins`: Fokker scourge, aces, and Zeppelin raid decisions.
7. `test_ohl_and_alberich`: Hindenburg program and Operation Alberich retreat.
8. `test_lettow_vorbeck_and_tag_bat`: Askari division in Tanganyika and tag `BAT` definition.
9. `test_endsieg_and_versailles`: Hidden tree file, Volkssturm OOB, and Rhine crossing event.
10. `test_localisation_bom_and_parity`: Single UTF-8 BOM and key parity across German rework keys.

- [ ] **Step 2: Run test to verify it fails (RED Phase)**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul -v`
Expected: FAIL (files and features not yet implemented).

- [ ] **Step 3: Register test in `scripts/qa_audit_all.py`**
Add `tests.test_ww1_germany_rework` to `SUITES` in `scripts/qa_audit_all.py`.

- [ ] **Step 4: Commit**
```bash
git add tests/test_ww1_germany_rework.py scripts/qa_audit_all.py
git commit -m "test(ger): establish comprehensive RED test suite for German Empire and Endsieg rework"
```

---

