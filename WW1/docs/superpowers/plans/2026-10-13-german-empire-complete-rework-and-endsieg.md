# German Empire Complete Rework & Endsieg System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a massive, historically authentic, and competitively balanced overhaul of the German Empire (`GER`) in *Baianagem-WW1*, fixing Belgian supply infrastructure, purging 51 calendar date-gates, introducing industrial cartels, U-boat postures, strategic air/gas warfare, asymmetric colonial guerrilla, 4 political paths, and the dynamic Versailles vs. hidden Endsieg emergency tree.

**Architecture:** Modular test-driven development starting from a comprehensive RED test suite (`tests/test_ww1_germany_rework.py`), followed by infrastructure/opening logistics fixes, date-gate elimination, core wartime gameplay mechanics, political branch expansions, the bespoke Versailles/Endsieg war termination engine, and bilingual single UTF-8 BOM localization.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Python 3.10+ (custom AST parsers, `scripts.hoi4_semantic_oracle`, `scripts.mod_engine`), YAML with UTF-8 BOM.

**Spec:** `docs/superpowers/specs/2026-10-13-german-empire-complete-rework-and-endsieg-design.md`

## Global Constraints

- 100% Clausewitz bracket balance and syntax integrity across all `.txt` script files.
- Zero invalid modifiers: all country/state modifiers must validate against `scripts.hoi4_semantic_oracle` and `data/hoi4_valid_country_modifiers.json`.
- Strict single UTF-8 BOM (`\xef\xbb\xbf`) on all localization `.yml` files with 100% key parity between English (`l_english`) and Brazilian Portuguese (`l_braz_por`).
- Spatial focus tree geometry: 0 coordinate collisions, `|x2 - x1| >= 2` on the same row, and `1 <= dy <= 3` for all parent-child connections.
- Multiplayer stability: deterministic daily/weekly variable evaluations without recursive trigger loops or desync risks.
- Bespoke war termination: avoid vanilla 100% surrender peace conferences to preserve post-Versailles and Endsieg gameplay.

## Review Focus

1. **Belgian Railway & Supply Graph Disconnect:** If railway connections or supply hubs in Liège (state 35) or Namur (state 34) reference non-existent province IDs, the HOI4 supply map engine will crash or leave provinces unsupplied. *Test: Verify all province IDs against map definitions in `test_belgian_railway_and_supply_nodes`.*
2. **Hidden Tree Swapping Desync:** When `load_focus_tree = ww1_germany_endsieg_focus` executes upon rejecting Versailles, ensure all active national ideas and ongoing military operations remain persistent and do not trigger CTD. *Test: Validate tree ID, country factor, and prerequisite links in `test_endsieg_emergency_tree_integrity`.*
3. **Double UTF-8 BOM Corruption:** Modifying `.yml` localization files must never insert `\xef\xbb\xbf\xef\xbb\xbf`. *Test: Assert byte prefix `b[:3] == b'\xef\xbb\xbf' and b[3:6] != b'\xef\xbb\xbf'` in `test_localisation_bom_and_parity`.*
4. **Invalid Clausewitz Modifiers:** Using non-country modifiers in ideas (e.g. `sub_detection` instead of naval tech, or `reinforce_rate` instead of `land_reinforce_rate`) causes silent engine failures. *Test: Run Semantic Oracle on all created ideas in `test_semantic_oracle_clean`.*
5. **Premature Surrender Engine Hijack:** If the Rhine crossing event fires after 100% surrender progress, vanilla HOI4 peace conference triggers and deletes the country before the event options can be clicked. *Test: Assert the event triggers at `surrender_progress > 0.25` or immediate loss of Cologne (42) / Mainz (55) in `test_versailles_trigger_bounds`.*

---

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

### Task 3: Western Front Opening, Fused Schlieffen & Trench Stalemate Transition

**Files:**
- Modify: `common/national_focus/germany.txt`
- Create: `common/ideas/ww1_germany_western_front_ideas.txt`
- Create: `events/ww1_germany_western_front_events.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_schlieffen_and_stalemate`

**Interfaces:**
- Consumes: Fused Schlieffen focus `GER_schlieffen_maneuver`
- Produces: `GER_schlieffen_momentum`, event `ww1_germany.10`, and `GER_western_trench_stalemate`

- [ ] **Step 1: Write idea definitions in `common/ideas/ww1_germany_western_front_ideas.txt`**
Define `GER_schlieffen_momentum` (+10% soft attack, +15% speed, +96h supply grace, 90 days) and `GER_western_trench_stalemate` (+15 max entrenchment, +30% entrenchment speed, +20% core/occupied defense).
Validate with `scripts.hoi4_semantic_oracle`.

- [ ] **Step 2: Fuse Belgian Ultimatum and Schlieffen in `common/national_focus/germany.txt`**
Create focus `GER_schlieffen_maneuver`, occupy Luxembourg on start, deliver Belgian ultimatum, and grant momentum idea.

- [ ] **Step 3: Implement stalemate transition event in `events/ww1_germany_western_front_events.txt`**
Event `ww1_germany.10`: triggers when `GER_schlieffen_momentum` expires without Paris captured (`NOT = { controls_state = 16 }`), removing momentum and adding `GER_western_trench_stalemate`.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_schlieffen_and_stalemate -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/national_focus/germany.txt common/ideas/ events/
git commit -m "feat(ger): fuse Schlieffen maneuver, add supply grace, and implement deep trench stalemate transition"
```

---

### Task 4: Date-Gates Purge & Conversion to Frontline Operational Missions

**Files:**
- Modify: `common/national_focus/germany.txt`
- Create: `common/decisions/categories/ww1_germany_operational_categories.txt`
- Create: `common/decisions/ww1_germany_operational_decisions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_date_gates_eliminated`

**Interfaces:**
- Consumes: 51 legacy focuses in `germany.txt`
- Produces: 0 date-gates in `germany.txt`, 35/42 day focus pacing, and operational decision category `GER_high_command_operations`

- [ ] **Step 1: Audit and eliminate all 51 `date >` triggers in `germany.txt`**
Remove hardcoded calendar gates from *Tannenberg*, *Gorlice-Tarnów*, *Verdun*, *Jutland*, *Caporetto*, *Cambrai*, *Kaiserschlacht*, etc. Replace with battlefield context triggers (e.g., `has_war_with = FRA`, `has_war_with = RUS`).

- [ ] **Step 2: Reduce tactical focus durations**
Reduce durations of tactical battle focuses from 70 days to 35/42 days.

- [ ] **Step 3: Create operational decisions in `common/decisions/ww1_germany_operational_decisions.txt`**
Implement dynamic operations: *Operation Gericht (Verdun Meatgrinder)*, *Gorlice-Tarnów Infiltration*, *Caporetto Mountain Shock*, and *Kaiserschlacht Spring Offensive*.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_date_gates_eliminated -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/national_focus/germany.txt common/decisions/
git commit -m "refactor(ger): purge all 51 date-gates, accelerate focus pacing, and implement operational missions"
```

---

### Task 5: Industrial Cartels (Krupp, Thyssen, BASF) & Chemical Warfare Escalation

**Files:**
- Modify: `common/ideas/ww1_germany_ideas.txt`
- Create: `common/decisions/categories/ww1_germany_industry_categories.txt`
- Create: `common/decisions/ww1_germany_cartel_and_chemical_decisions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_cartels_and_chemical_warfare`

**Interfaces:**
- Consumes: Krupp, Thyssen, BASF Haber-Bosch, and chemical escalation specs
- Produces: Valid Clausewitz ideas and 3-stage chemical escalation decisions

- [ ] **Step 1: Implement Cartel ideas in `common/ideas/ww1_germany_ideas.txt`**
Define `GER_krupp_siege_guns` (+artillery soft attack, siege efficiency), `GER_thyssen_steel_syndicate` (+factory construction and efficiency), `GER_haber_bosch_synthesis` (synthetic nitrates, munitions output), and `GER_buna_rubber`. Verify via Semantic Oracle.

- [ ] **Step 2: Implement Chemical Warfare Escalation decisions**
Category `GER_chemical_warfare_program`:
- `GER_chlorine_gas_release` (Ypres 1915): +15% breakthrough for 60 days.
- `GER_phosgene_gas_shells` (1916): Soft attack and casualty bonus.
- `GER_mustard_gas_deployment` (1917): Yellow Cross shells causing lingering organization attrition.
- Gas mask countermeasures for Entente counterplay.

- [ ] **Step 3: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_cartels_and_chemical_warfare -v`
Expected: PASS.

- [ ] **Step 4: Commit**
```bash
git add common/ideas/ common/decisions/
git commit -m "feat(ger): implement industrial cartels, Haber-Bosch synthesis, and 3-tier chemical warfare escalation"
```

---

### Task 6: Battle of the Atlantic U-Boat Postures, US Tension Gauge & Zimmermann Telegram

**Files:**
- Create: `common/scripted_effects/ww1_germany_naval_effects.txt`
- Create: `common/decisions/ww1_germany_naval_decisions.txt`
- Create: `events/ww1_germany_naval_events.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_uboat_postures_and_us_tension`

**Interfaces:**
- Consumes: Clamped variable `GER_us_intervention_tension` (0-100)
- Produces: 3 submarine postures, Zimmermann mini-game, and British counterplay ideas

- [ ] **Step 1: Script variable initialization and clamp in `ww1_germany_naval_effects.txt`**
Script `ger_init_naval_gauges` and `ger_clamp_naval_gauges` clamping `GER_us_intervention_tension` strictly between 0 and 100.

- [ ] **Step 2: Implement 3 Submarine Postures in `ww1_germany_naval_decisions.txt`**
- *Cruiser Rules*: 0 tension gain, modest commerce raiding.
- *Declared War Zone*: +1 weekly tension, solid convoy raiding.
- *Unrestricted Submarine Warfare*: +3 weekly tension, massive convoy destruction.

- [ ] **Step 3: Implement Zimmermann Telegram event chain in `ww1_germany_naval_events.txt`**
German proposal to Mexico (`MEX`); Room 40 British interception vs successful diversion of US troops.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_uboat_postures_and_us_tension -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/scripted_effects/ common/decisions/ events/ common/on_actions/
git commit -m "feat(ger): implement 3 U-boat postures, US tension gauge, and Zimmermann telegram mini-game"
```

---

### Task 7: Strategic Air Warfare (Fokker Scourge, Aces) & Zeppelin Bombing Raids

**Files:**
- Create: `common/decisions/ww1_germany_air_decisions.txt`
- Create: `common/ideas/ww1_germany_air_ideas.txt`
- Modify: `common/characters/GER.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_air_warfare_and_zeppelins`

**Interfaces:**
- Consumes: Manfred von Richthofen, Oswald Boelcke, Ernst Udet character data
- Produces: Fokker scourge air superiority, ace commander recruitment, and Zeppelin raid missions

- [ ] **Step 1: Recruit historical air aces in `common/characters/GER.txt`**
Add/enrich `GER_manfred_von_richthofen`, `GER_oswald_boelcke`, `GER_ernst_udet` with appropriate traits and portraits.

- [ ] **Step 2: Implement Fokker Scourge and Zeppelin decisions**
- *The Fokker Scourge*: grants `GER_fokker_scourge_spirit` (+air superiority factor, +interception) for 180 days.
- *Zeppelin Terror Raids*: targets London, Thames, and Hull, inflicting British war weariness and damaging factories.

- [ ] **Step 3: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_air_warfare_and_zeppelins -v`
Expected: PASS.

- [ ] **Step 4: Commit**
```bash
git add common/decisions/ common/ideas/ common/characters/
git commit -m "feat(ger): implement Fokker Scourge, ace commanders, and strategic Zeppelin terror raids"
```

---

### Task 8: OHL Military Dictatorship, The Hindenburg Program & Resource Logistics

**Files:**
- Modify: `common/ideas/ww1_germany_ideas.txt`
- Create: `common/decisions/ww1_germany_war_economy_decisions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_ohl_and_alberich`

**Interfaces:**
- Consumes: Hindenburg Program, Operation Alberich, Ploiești oil, and Kriegsanleihen specs
- Produces: `GER_hindenburg_program`, strategic retreat decisions, and war bond mechanics

- [ ] **Step 1: Define Hindenburg Program idea**
`GER_hindenburg_program`: +25% military factory output, +20% artillery efficiency, -10% consumer goods satisfaction.

- [ ] **Step 2: Implement Operation Alberich strategic retreat**
Decision `GER_operation_alberich`: available if at war with Entente in France. Withdraws 40km, shortens line, dismantles infrastructure in evacuated states, and grants 14 divisions instant organization recovery and entrenchment.

- [ ] **Step 3: Implement Ploiești Oil & Kriegsanleihen war bonds**
Decisions to secure Romanian oil and issue up to 9 tranches of debt bonds with escalating inflation penalties.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_ohl_and_alberich -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/ideas/ common/decisions/
git commit -m "feat(ger): implement OHL Hindenburg program, Operation Alberich retreat, and war bonds economics"
```

---

### Task 9: Paul von Lettow-Vorbeck Asymmetric East Africa Guerrilla & Global Subversion

**Files:**
- Create: `history/units/GER_east_africa.txt`
- Modify: `history/countries/GER - Germany.txt`
- Create: `common/decisions/ww1_germany_colonial_and_subversion_decisions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_lettow_vorbeck_and_tag_bat`

**Interfaces:**
- Consumes: Lettow-Vorbeck character and Tanganyika (546) setup
- Produces: Askari guerrilla division, Uganda railway raid missions, Easter Rising and Indian Ghadar decisions

- [ ] **Step 1: Define Askari colonial OOB in `history/units/GER_east_africa.txt`**
Create authentic Askari infantry and scout battalions with `GER_askari_guerrilla_doctrine` (supply consumption -90%, jungle defense +30%).

- [ ] **Step 2: Implement East African raid decisions**
Decision category `GER_deutsch_ostafrika_guerrilla`:
- *Raid the Uganda-Mombasa Railway*: damages British infrastructure and steals supplies.
- *Entente Attrition Drain*: applies passive off-map manpower and factory drain to `ENG` and `SAF`.

- [ ] **Step 3: Implement Global Subversion decisions**
- *Support the Irish Easter Rising (1916)*: smuggles arms via *SMS Libau* to Dublin.
- *The Ghadar Conspiracy in India*: funds anti-colonial unrest in the British Raj.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_lettow_vorbeck_and_tag_bat -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add history/units/ history/countries/ common/decisions/
git commit -m "feat(ger): implement Lettow-Vorbeck African guerrilla warfare and global subversion operations"
```

---

### Task 10: Eastern Order (*Ober Ost*), Austro-Hungarian Unified Command & Tag `BAT`

**Files:**
- Modify: `common/country_tags/01_ww1_tags.txt`
- Create: `common/countries/United Baltic Duchy.txt`
- Modify: `common/countries/colors.txt`
- Create: `history/countries/BAT - United Baltic Duchy.txt`
- Create: `common/decisions/ww1_germany_eastern_order_decisions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_lettow_vorbeck_and_tag_bat`

**Interfaces:**
- Consumes: Tag `BAT`, Brest-Litovsk treaty hook
- Produces: Sovereign puppet kingdoms (`POL`, `BAT`, `LIT`, `FIN`, `UKR`) and Ukrainian grain extraction

- [ ] **Step 1: Register tag `BAT` (United Baltic Duchy)**
Define `BAT = "countries/United Baltic Duchy.txt"` in `01_ww1_tags.txt`, assign color in `colors.txt`, create country and history files.

- [ ] **Step 2: Implement Austro-Hungarian Unified Command decisions**
Decisions to deploy German intervention armies to Galicia (Mackensen) and the Isonzo (Caporetto) to prevent Austrian collapse.

- [ ] **Step 3: Implement Brest-Litovsk Client Kingdoms release & Ukrainian Grain**
Decisions to establish puppet kingdoms and import Ukrainian grain trains to alleviate the *Steckrübenwinter*.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_lettow_vorbeck_and_tag_bat -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/country_tags/ common/countries/ history/countries/ common/decisions/
git commit -m "feat(ger): register tag BAT, implement Central Powers joint command, and Ober Ost client kingdoms"
```

---

### Task 11: The Four Expanded Political Trajectories

**Files:**
- Modify: `common/national_focus/germany.txt`
- Create: `events/ww1_germany_politics_events.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_cartels_and_chemical_warfare`

**Interfaces:**
- Consumes: 4 political paths in `germany.txt`
- Produces: Pax Germanica, Vaterlandspartei, Weimar Peace Resolution, and Spartakusbund Red Alliance

- [ ] **Step 1: Expand Imperial Pax Germanica path**
Constitutional reforms, Bethmann-Hollweg compromises, Bavarian federal harmony, and founding of the *Mitteleuropa* economic union.

- [ ] **Step 2: Implement Vaterlandspartei Totalitarian Dictatorship**
Kapp and Tirpitz military takeover, total war mobilization, annexationist war aims.

- [ ] **Step 3: Implement Weimar Early Peace Resolution (1917)**
Reichstag majority passes peace without annexations, opening diplomatic exit with Western Allies.

- [ ] **Step 4: Implement Spartakusbund Red Soviet Alliance**
Kiel mutiny, Liebknecht & Luxemburg red revolution, proclamation of the Free Socialist Republic, ideological pact with Soviet Russia.

- [ ] **Step 5: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul -v`
Expected: PASS.

- [ ] **Step 6: Commit**
```bash
git add common/national_focus/germany.txt events/
git commit -m "feat(ger): complete all 4 political paths from Imperial Pax Germanica to Spartakusbund"
```

---

### Task 12: The Fall of the Rhine, The Treaty of Versailles & Playable Post-War Republic

**Files:**
- Create: `events/ww1_germany_endsieg_events.txt`
- Create: `common/decisions/ww1_germany_weimar_and_freikorps_decisions.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_versailles_trigger_bounds`

**Interfaces:**
- Consumes: Rhine crossing or surrender threshold trigger
- Produces: Event `ww1_germany_endsieg.1`, Path A Versailles armistice, demilitarized Rhineland, Scapa Flow scuttle, and Freikorps playable defense

- [ ] **Step 1: Implement Rhine Crossing & Crisis Event in `ww1_germany_endsieg_events.txt`**
`ww1_germany_endsieg.1`: triggers when Cologne (42) or Mainz (55) is captured or `surrender_progress > 0.25` for non-communist Germany.
- Option A: Accept Armistice and Treaty of Versailles.
- Option B: Refuse and Fight to the Bitter End (Endsieg).

- [ ] **Step 2: Script Versailles Peace & Post-War Republic mechanics**
Bespoke scripted white peace with Entente tags, Kaiser abdicates to Doorn, Friedrich Ebert takes power, Rhineland demilitarized, Scapa Flow fleet scuttled.

- [ ] **Step 3: Implement Post-Versailles Playable Content (Weimar & Freikorps)**
- *The Spartakist Uprising (Jan 1919)*: street fighting decisions in Berlin using Freikorps.
- *The Baltic Freikorps Defense*: sending volunteer divisions under von der Goltz to defend Courland and East Prussia against the Red Army.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_versailles_trigger_bounds -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add events/ common/decisions/ common/on_actions/
git commit -m "feat(ger): implement dynamic Versailles armistice, Scapa Flow scuttling, and playable Weimar/Freikorps defense"
```

---

### Task 13: The Hidden Endsieg Emergency Focus Tree & Entente Exhaustion Clock

**Files:**
- Create: `common/national_focus/ww1_germany_endsieg.txt`
- Create: `history/units/GER_volkssturm_endsieg.txt`
- Create: `common/scripted_effects/ww1_germany_endsieg_effects.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_endsieg_emergency_tree_integrity`

**Interfaces:**
- Consumes: Option B of `ww1_germany_endsieg.1`
- Produces: Tree `ww1_germany_endsieg_focus` (20 focuses), Volkssturm emergency OOB, triple-front collapse, and Entente exhaustion clock

- [ ] **Step 1: Create dedicated 20-focus Endsieg tree `common/national_focus/ww1_germany_endsieg.txt`**
Define `ww1_germany_endsieg_focus` with 20 non-colliding emergency focuses across 3 wings:
- Wing 1: Total Militarization & Volkssturm (7 focuses)
- Wing 2: Festung Deutschland & Underground War Plants (7 focuses)
- Wing 3: The Last Stand & The Rhine Reconciliation (6 focuses)

- [ ] **Step 2: Create Volkssturm emergency OOB in `history/units/GER_volkssturm_endsieg.txt`**
Emergency militia templates spawning in Berlin, Weser, and Elbe river lines.

- [ ] **Step 3: Implement Triple-Front Peril & Entente Exhaustion Clock**
- Internal Worker Revolts / Civil War threat in Ruhr and Berlin.
- Austro-Hungarian dissolution event and southern flank exposure.
- Soviet breach of Brest-Litovsk and Red Army march on East Prussia.
- Clock: Holding out for 9-12 months triggers French trench mutinies and British general strikes, enforcing the *Peace of Reconciliation on the Rhine* (white peace preserving 1914 borders).

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_endsieg_emergency_tree_integrity -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/national_focus/ww1_germany_endsieg.txt history/units/ common/scripted_effects/
git commit -m "feat(ger): implement 20-focus hidden Endsieg emergency tree, Volkssturm OOB, and Entente exhaustion clock"
```

---

### Task 14: Bilingual Localization & Single UTF-8 BOM Parity

**Files:**
- Create: `localisation/english/ww1_germany_rework_l_english.yml`
- Create: `localisation/braz_por/ww1_germany_rework_l_braz_por.yml`
- Modify: `localisation/english/ww1_germany_focus_l_english.yml` (and braz_por counterpart)
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_localisation_bom_and_parity`

**Interfaces:**
- Consumes: All newly created focus, idea, decision, and event keys across Tasks 2 through 13
- Produces: 100% key parity in English and Brazilian Portuguese with single UTF-8 BOM (`\xef\xbb\xbf`)

- [ ] **Step 1: Author English localization `localisation/english/ww1_germany_rework_l_english.yml`**
Add all titles and descriptions with single UTF-8 BOM prefix.

- [ ] **Step 2: Author Brazilian Portuguese localization `localisation/braz_por/ww1_germany_rework_l_braz_por.yml`**
Mirror all keys with authentic Brazilian Portuguese translations and single UTF-8 BOM prefix.

- [ ] **Step 3: Run localization integrity test**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_localisation_bom_and_parity -v`
Expected: PASS with 100% parity and 0 double-BOM corruptions.

- [ ] **Step 4: Commit**
```bash
git add localisation/
git commit -m "feat(loc): provide complete bilingual localization with single UTF-8 BOM for German rework"
```

---

### Task 15: Master QA Integration, Semantic Oracle Audit & Full Test Pass

**Files:**
- Modify: `scripts/qa_audit_all.py`
- Test: All 9 test suites across the mod repository

**Interfaces:**
- Consumes: All 14 previous tasks
- Produces: Exit Code 0 on master QA audit with zero regressions

- [ ] **Step 1: Run Semantic Oracle across all modified files**
Audit all ideas, decisions, focuses, and events for modifier compliance.
Expected: 0 invalid modifier errors.

- [ ] **Step 2: Run complete unit test suite**
Run: `python -m unittest tests.test_ww1_germany_rework -v`
Expected: All 10 tests PASS!

- [ ] **Step 3: Run Master QA Audit**
Run: `python scripts/qa_audit_all.py`
Expected: Exit Code 0 across all 9 test suites (100+ tests).

- [ ] **Step 4: Commit**
```bash
git add scripts/qa_audit_all.py
git commit -m "chore(qa): integrate German rework into master QA pipeline with 100% green tests"
```
