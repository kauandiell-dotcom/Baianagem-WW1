# German Empire Phase 2: Eastern Order (Brest-Litovsk & Mitteleuropa) and 4 Political Paths Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the Brest-Litovsk territorial cessions and Mitteleuropa client states (Poland protectorate, Ukrainian Hetmanate, United Baltic Duchy `BAT`), and implement the 4 German political trajectories (Imperial, Vaterlandspartei, Weimar, Spartakusbund) with complete QA automation and live Steam Workshop synchronization.

**Architecture:** Extend existing Clausewitz scripted effects, events, and focus trees with proper tag-safe state transfer mechanisms that prevent silent Clausewitz scope failures, implement historical puppet releases, wire up political events and ideas, and validate via automated Python unit tests and Semantic Oracle.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Paradox YAML Localization (UTF-8 BOM), Python `unittest`, `scripts/qa_audit_all.py`, `scripts/hoi4_semantic_oracle.py`.

**Spec:** `docs/superpowers/specs/2026-10-13-german-empire-complete-rework-and-endsieg-design.md`

## Global Constraints

- 100% bracket balance across all Clausewitz script files (`.txt`).
- Strictly single UTF-8 BOM (`\xef\xbb\xbf`) on all localization files (`.yml`). Zero double-BOM.
- 100% key parity between English (`l_english`) and Brazilian Portuguese (`l_braz_por`).
- Zero invalid modifiers: validate all national spirits against `scripts.hoi4_semantic_oracle`.
- Tag-safe state transfers: never scope `TAG = { transfer_state = ... }` before `TAG` exists on the map. Transfer states to `GER` first, then call `GER = { release_puppet = TAG }` or `puppet = TAG`.
- Synchronize all files to active game directory `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus

1. **Tag Non-Existence Failure in Brest-Litovsk:** If Russia cedes states to a tag that doesn't yet exist (`POL`, `UKR`, `BAT`, `FIN`), Clausewitz drops the scope silently. Solution: Russia transfers all ceded borderlands to `GER`, and `GER` releases them as puppets/protectorates.
2. **Double Peace Conference Desync:** When Brest-Litovsk concludes, ensure white peace with Central Powers applies to all alliance members (`GER`, `AUS`, `TUR`, `BUL`) and prevents ongoing war states.
3. **Turnip Winter Hunger Crisis:** When the Ukrainian Hetmanate is established, food shipments must remove `GER_turnip_winter_crisis` ideas and grant consumer goods relief.
4. **United Baltic Duchy (`BAT`) Definition:** `BAT` must have capital in Riga (12), core states (188, 189, 190, 191), and authentic head of state.
5. **Political Path Mutexes:** Mutually exclusive political paths (Imperial vs Vaterlandspartei vs Weimar vs Spartakusbund) must have proper `mutually_exclusive = { focus = ... }` and political stability checks.

---

### Task 1: QA RED Baseline Suite Expansion (`tests/test_ww1_germany_rework.py`)

**Files:**
- Modify: `tests/test_ww1_germany_rework.py`

**Interfaces:**
- Consumes: Existing test class `TestGermanyOverhaul`
- Produces: 3 new unit tests:
  - `test_brest_litovsk_territorial_engine`: Asserts `ww1_conclude_eastern_settlement` and `ww1_russia_diplomacy.2` properly transfer Polish, Baltic, and Ukrainian states.
  - `test_mitteleuropa_protectorates`: Asserts `GER_regency_kingdom_of_poland`, `GER_liberate_the_ukrainian_hetmanate`, and `GER_establish_united_baltic_duchy` release `POL`, `UKR`, and `BAT` as puppets.
  - `test_four_political_paths`: Asserts focuses/events for Imperial Pax, Vaterlandspartei, Weimar Peace Resolution, and Spartakusbund.

- [x] **Step 1: Add new test methods to `tests/test_ww1_germany_rework.py`**
- [x] **Step 2: Run test suite to verify RED state on unimplemented features**
Run: `python -m unittest tests.test_ww1_germany_rework -v`
Expected: FAIL on the 3 new tests.
- [x] **Step 3: Commit RED test baseline**
```bash
git add tests/test_ww1_germany_rework.py
git commit -m "test(ger): add RED test cases for Brest-Litovsk territorial cessions, Mitteleuropa satellites, and political paths"
```

---

### Task 2: Brest-Litovsk Territorial Engine & Tag-Safe State Transfer

**Files:**
- Modify: `common/scripted_effects/zz_ww1_eastern_settlement.txt`
- Modify: `events/ww1_russia_diplomacy_events.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_brest_litovsk_territorial_engine`

**Interfaces:**
- Consumes: Events `ww1_diplomacy.31`, `ww1_diplomacy.32`, and `ww1_russia_diplomacy.2`
- Produces: Tag-safe transfer of all historical Brest-Litovsk states (Poland, Baltics, Ukraine, Finland, Kars/Batum to Ottomans)

- [x] **Step 1: Refactor `common/scripted_effects/zz_ww1_eastern_settlement.txt`**
Transfer all Brest-Litovsk ceded states from Russia to Germany regardless of frontline control, then execute puppet releases.
- [x] **Step 2: Refactor `events/ww1_russia_diplomacy_events.txt` (Option A of `ww1_russia_diplomacy.2`)**
Ensure option A transfers states safely to GER, sets up puppets `POL`, `UKR`, `BAT`, and guarantees `FIN`.
- [x] **Step 3: Run unit test**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_brest_litovsk_territorial_engine -v`
Expected: PASS
- [x] **Step 4: Commit**
```bash
git add common/scripted_effects/zz_ww1_eastern_settlement.txt events/ww1_russia_diplomacy_events.txt
git commit -m "fix(diplomacy): implement tag-safe territorial transfer and puppet creation for Brest-Litovsk"
```

---

### Task 3: Mitteleuropa Satellites Focuses & Protectorate Events

**Files:**
- Modify: `common/national_focus/germany.txt`
- Modify: `events/ww1_germany_events.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_mitteleuropa_protectorates`

**Interfaces:**
- Consumes: Focuses `GER_regency_kingdom_of_poland`, `GER_liberate_the_ukrainian_hetmanate`, `GER_establish_united_baltic_duchy`
- Produces: Authentic protectorates:
  - `POL` (Regency Kingdom of Poland)
  - `UKR` (Ukrainian Hetmanate under Skoropadsky with grain deliveries)
  - `BAT` (United Baltic Duchy in Riga, Courland, Livonia, Estonia)

- [x] **Step 1: Update `GER_regency_kingdom_of_poland` and `ww1_germany_events.41`**
Release `POL`, transfer states 10, 87, 92, 94, 95, 96, 97, 98, and puppet `POL`.
- [x] **Step 2: Update `GER_liberate_the_ukrainian_hetmanate` and `ww1_germany_events.42`**
Release `UKR`, puppet `UKR`, set flag `GER_ukrainian_grain_deliveries`, remove `GER_turnip_winter_crisis_*`.
- [x] **Step 3: Update `GER_establish_united_baltic_duchy`**
Release `BAT` as puppet, transfer states 188, 189, 190, 191 to `BAT`.
- [x] **Step 4: Run unit test**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_mitteleuropa_protectorates -v`
Expected: PASS
- [x] **Step 5: Commit**
```bash
git add common/national_focus/germany.txt events/ww1_germany_events.txt
git commit -m "feat(ger): implement authentic Mitteleuropa client kingdoms for Poland, Ukraine, and Baltics"
```

---

### Task 4: Four German Political Trajectories

**Files:**
- Modify: `common/national_focus/germany.txt`
- Create: `events/ww1_germany_political_events.txt`
- Create: `common/ideas/ww1_germany_political_ideas.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_four_political_paths`

**Interfaces:**
- Consumes: Political branches in `germany.txt`
- Produces: 4 playable ideological paths:
  1. Imperial Pax Germanica (constitutional monarchy & federal reforms)
  2. Vaterlandspartei Totalitarian Dictatorship (Kapp & Tirpitz)
  3. Weimar Parliamentary Republic (1917 Peace Resolution & Social Democracy)
  4. Spartakusbund Red Revolution (Liebknecht & Luxemburg Red Germany)

- [x] **Step 1: Define ideas in `common/ideas/ww1_germany_political_ideas.txt`**
- [x] **Step 2: Implement political event chain in `events/ww1_germany_political_events.txt`**
- [x] **Step 3: Wire focuses and mutual exclusivity in `common/national_focus/germany.txt`**
- [x] **Step 4: Run unit test**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_four_political_paths -v`
Expected: PASS
- [x] **Step 5: Commit**
```bash
git add common/national_focus/germany.txt events/ww1_germany_political_events.txt common/ideas/ww1_germany_political_ideas.txt
git commit -m "feat(ger): implement 4 political paths (Imperial, Vaterlandspartei, Weimar, Spartakusbund)"
```

---

### Task 5: Complete Bilingual Localization & Single UTF-8 BOM Parity

**Files:**
- Modify: `localisation/english/ww1_germany_rework_l_english.yml`
- Modify: `localisation/braz_por/ww1_germany_rework_l_braz_por.yml`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_localisation_bom_and_parity`

**Interfaces:**
- Consumes: All new focus, idea, and event keys from Tasks 2, 3, and 4
- Produces: 100% key parity with single UTF-8 BOM (`\xef\xbb\xbf`)

- [x] **Step 1: Add all keys to English and Brazilian Portuguese localization files**
- [x] **Step 2: Verify strictly single UTF-8 BOM**
- [x] **Step 3: Run localization unit test**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_localisation_bom_and_parity -v`
Expected: PASS with 100% parity
- [x] **Step 4: Commit**
```bash
git add localisation/
git commit -m "feat(loc): add complete bilingual localization for Brest-Litovsk satellites and political paths"
```

---

### Task 6: Master QA Full Pass & Live Steam Workshop Sync

**Files:**
- Test: All mod test suites via `scripts/qa_audit_all.py`
- Mirror: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

**Interfaces:**
- Consumes: All completed tasks
- Produces: Exit Code 0 on master QA audit and 100% updated files in the active game directory

- [x] **Step 1: Run Semantic Oracle and syntax checks**
- [x] **Step 2: Run Master QA Audit `python scripts/qa_audit_all.py`**
Expected: Exit Code 0 across all 9 test suites
- [x] **Step 3: Run Python sync script mirroring all modified files to the Steam Workshop directory**
- [x] **Step 4: Verify synced files exist and match in size**
- [x] **Step 5: Report completion to user**

