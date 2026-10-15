# Kingdom of Serbia Complete Rework, Balance of Power & The Great Retreat Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the Kingdom of Serbia (`SER`) in *Baianagem-WW1* into an authentic, deeply interactive historical simulation featuring a native HOI4 Balance of Power (Parliamentary Cabinet vs Black Hand / Apis), an unbroken Great Retreat (*Albanska Golgota*) engine granting cores on Salonika/Durrës, near-impossible capitulation, 4-wave mass mobilization spawning 28–30 divisions, the defence of Belgrade (Major Gavrilović), the 1915 Typhus Epidemic (Dr. Elsie Inglis), Essad Pasha's Albanian corridor, Venizelos' Salonika Republic, the Blue Graveyard of Vido, the Russian Odessa volunteer division, the world's first AA shootdown, and 4 divergent endgames (Yugoslavia, Greater Serbia, Balkan Socialist Federation, Pretorian Military Junta).

**Architecture:** Native HOI4 Balance of Power (`common/bop/SER_bop.txt`), fallback scripted balance variables, emergency map sanctuary scripts granting temporary/wartime cores on states 184 and 44, extreme surrender limit reinforcement (`surrender_limit = +0.40`), multi-wave unit spawn scripts, fast-failing decisions, non-colliding focus DAGs, semantic oracle validated modifiers, and single UTF-8 BOM bilingual localization.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Python automated unit testing (`unittest`), Git, Steam Workshop staging pipeline.

**Spec:** `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`

## Global Constraints
- Bracket syntax must balance with net delta = 0 across all modified and created `.txt` files.
- All modifier tokens must exist in `data/hoi4_valid_country_modifiers.json` with 0 oracle errors.
- Every YAML localization file must begin with exactly one single UTF-8 BOM byte sequence (`\xef\xbb\xbf`).
- Montenegro (state 105) remains an integrated core state of Serbia from Day 1 (1911.6.1).
- Every changed or created file must be synchronized with the Steam Workshop mirror at `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus
1. **Unbroken Resistance & Near-Impossible Capitulation:** Serbia must NOT capitulate while holding Salonika (state 184) or Durrës/Corfu; `surrender_limit` must reach $\ge 95\%$ during wartime retreat.
2. **AI Bot Execution of the Great Retreat:** When Belgrade (state 107) or Niš (state 108) falls, the AI Bot must automatically trigger the retreat, claim the southern sanctuary, and execute the 28–30 division spawns without getting stuck.
3. **Native BoP vs Fallback Safety:** Native `common/bop/SER_bop.txt` must operate smoothly under *By Blood Alone* while synchronizing with `ser_civil_military_balance` for non-DLC / multiplayer compatibility.
4. **Mass Division Spawn Pacing:** The 28–30 divisions spawned across the 4 waves must have valid division templates, valid equipment, and sufficient supply in Salonika without causing instant attrition deaths.
5. **Localization Parity:** English and Brazilian Portuguese files must have 100% identical key sets.

---

### Task 1: QA RED Test Baseline (`tests/test_ww1_serbia_rework.py`)

**Files:**
- Create: `tests/test_ww1_serbia_rework.py`
- Modify: `scripts/qa_audit_all.py`

- [ ] **Step 1:** Create `tests/test_ww1_serbia_rework.py` with test class `TestSerbiaOverhaul` covering:
  - `test_native_bop_definition`: Checks existence of `common/bop/SER_bop.txt`, sides `bop_ser_pasic_parliament` and `bop_ser_apis_black_hand`, ranges and modifier validity.
  - `test_great_retreat_and_sanctuary_mechanics`: Checks scripted effects and events granting cores on state 184 (Salonika) and state 44 (Durrës/Albania), the surrender limit spirit `SER_otadzbina_u_pokretu` (`surrender_limit >= 0.35`), and retreat decisions.
  - `test_salonika_thirty_divisions_spawns`: Checks decision chains spawning the 4 waves of troops (Conscripts, Yugoslav Volunteers, Allied Brigades, Toplica Chetniks) totaling 28–30 divisions.
  - `test_belgrade_defense_and_typhus_crisis`: Checks Major Gavrilović's last stand decision/idea and the 1915 Typhus epidemic event chain.
  - `test_vido_memorial_and_essad_pasha`: Checks decision for Essad Pasha's Albanian corridor and the Vido Blue Graveyard (*Plava Grobnica*) memorial.
  - `test_four_yugoslav_destinies`: Checks focus branches and ideas for Kingdom of SHS / Yugoslavia, Greater Serbia, Balkan Socialist Federation, and Apis Military Junta.
  - `test_semantic_oracle_modifiers`: Audits all Serbian ideas and decisions for valid Clausewitz country modifiers.
  - `test_localisation_bom_and_parity`: Asserts single UTF-8 BOM on `localisation/english/ww1_serbia_l_english.yml` and `localisation/braz_por/ww1_serbia_l_braz_por.yml`, 0 double BOM, and 100% key parity.
- [ ] **Step 2:** Register `tests.test_ww1_serbia_rework` as Suite 14 in `scripts/qa_audit_all.py`.
- [ ] **Step 3:** Run `python -m unittest tests.test_ww1_serbia_rework -v` to confirm failure (RED phase).
- [ ] **Step 4:** Commit baseline:
  `git add tests/test_ww1_serbia_rework.py scripts/qa_audit_all.py`  
  `git commit -m "test(ser): establish comprehensive RED QA test suite for Serbia overhaul & Great Retreat"`

---

### Task 2: Native Balance of Power Engine (`common/bop/SER_bop.txt`)

**Files:**
- Create: `common/bop/SER_bop.txt`
- Create: `common/scripted_effects/ww1_serbia_bop_effects.txt`
- Modify: `history/countries/SER - Serbia.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

- [ ] **Step 1:** Create `common/bop/SER_bop.txt` defining:
  - `bop_ser_civil_military`: Initial value = 0.0, left side `bop_ser_pasic_parliament`, right side `bop_ser_apis_black_hand`.
  - Ranges:
    * `bop_ser_range_extreme_pasic` (-1.0 to -0.7): Stability +15%, PP +0.25, Army Org -10%.
    * `bop_ser_range_medium_pasic` (-0.69 to -0.2): Stability +8%, PP +0.15.
    * `bop_ser_range_balanced` (-0.19 to +0.19): PP -0.05, Decision Cost +10% (Priority Decree tension).
    * `bop_ser_range_medium_apis` (+0.2 to +0.69): Army Attack +8%, Core Defence +10%, Stability -10%.
    * `bop_ser_range_extreme_apis` (+0.7 to +1.0): Army Attack +15%, Org Recovery +15%, Stability -25%, Coup threat.
- [ ] **Step 2:** Create scripted effects in `common/scripted_effects/ww1_serbia_bop_effects.txt` to sync native BoP with fallback variable `ser_civil_military_balance` for non-DLC compatibility.
- [ ] **Step 3:** Hook BoP initialization in `history/countries/SER - Serbia.txt`:
  `if = { limit = { has_dlc = "By Blood Alone" } set_power_balance = { id = bop_ser_civil_military left_side = bop_ser_pasic_parliament right_side = bop_ser_apis_black_hand } }`.
- [ ] **Step 4:** Verify with `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_native_bop_definition -v`.
- [ ] **Step 5:** Commit:
  `git add common/bop/SER_bop.txt common/scripted_effects/ww1_serbia_bop_effects.txt history/countries/SER\ -\ Serbia.txt common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`  
  `git commit -m "feat(ser): implement native Balance of Power engine between Pasic and Black Hand"`

---

### Task 3: The Great Retreat, Salonika Sanctuary & 30-Division Mobilization Engine

**Files:**
- Create: `common/decisions/ww1_serbia_retreat_decisions.txt`
- Modify: `common/decisions/categories/ww1_serbia_decision_categories.txt`
- Create: `events/ww1_serbia_retreat_events.txt`
- Modify: `common/ideas/ww1_serbia_ideas.txt`
- Modify: `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`

- [ ] **Step 1:** Define the resistance national spirit in `common/ideas/ww1_serbia_ideas.txt`:
  - `SER_otadzbina_u_pokretu`: `surrender_limit = 0.40`, `army_core_defence_factor = 0.20`, `army_morale_factor = 0.15`, `attrition = -0.25`.
  - `SER_oath_of_corfu_martyrs`: `army_attack_factor = 0.10`, `army_org_regain = 0.15`.
- [ ] **Step 2:** Create `events/ww1_serbia_retreat_events.txt`:
  - `ww1_serbia_retreat.1`: *Naređenje o Odstupanju* (Proclamation of the Great Retreat). Grants cores on state 184 (Salonika) and state 44 (Durrës), adds `SER_otadzbina_u_pokretu`, establishes government-in-exile.
  - `ww1_serbia_retreat.2`: *The Allied Sanctuary at Salonika & Greek National Schism* (Event sent to GRE and FRA; transfers military control of port/naval base of Salonika to SER/Allies via Venizelos).
  - `ww1_serbia_retreat.10`: *The Mojkovac Rearguard Stand* (Montenegrin forces delay enemy advance).
  - `ww1_serbia_retreat.15`: *The Secret Pact with Essad Pasha Toptani* (Safe corridor through Albania state 44).
  - `ww1_serbia_retreat.20`: *The Blue Graveyard of Vido (Plava Grobnica)* (Sanitary regeneration, removes typhus, gives `SER_oath_of_corfu_martyrs`).
  - `ww1_serbia_retreat.25`: *The Odessa Volunteer Division* (Repatriation of South Slavic Austro-Hungarian POWs from Russia).
- [ ] **Step 3:** Implement decisions in `common/decisions/ww1_serbia_retreat_decisions.txt` for the 4 mobilization waves:
  - `SER_spawn_conscript_regiments_1896_1899`: Spawns 8 Infantry Divisions in Salonika.
  - `SER_spawn_yugoslav_volunteer_corps`: Spawns 8 Veteran Volunteer Divisions in Salonika.
  - `SER_spawn_french_allied_brigades`: Spawns 6 Shock 75mm Divisions in Salonika.
  - `SER_spawn_toplica_chetnik_uprising`: Spawns 6–8 Chetnik Irregular Divisions in states 107 and 108 behind enemy lines.
- [ ] **Step 4:** Hook automated AI trigger under `on_weekly` in `zz_ww1_ger_rus_rework_on_actions.txt`: If `tag = SER`, `has_war = yes`, and `NOT = { controls_state = 107 }`, AI instantly executes the retreat and spawns troops.
- [ ] **Step 5:** Verify with:
  `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_great_retreat_and_sanctuary_mechanics -v`  
  `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_salonika_thirty_divisions_spawns -v`  
  `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_vido_memorial_and_essad_pasha -v`
- [ ] **Step 6:** Commit:
  `git add common/decisions/ww1_serbia_retreat_decisions.txt common/decisions/categories/ww1_serbia_decision_categories.txt events/ww1_serbia_retreat_events.txt common/ideas/ww1_serbia_ideas.txt common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`  
  `git commit -m "feat(ser): implement Great Retreat sanctuary, 30-division mobilization, and core expansion"`

---

### Task 4: 1914 Crisis, Belgrade Defense (Major Gavrilović) & 1915 Typhus Epidemic

**Files:**
- Modify: `events/ww1_serbia_events.txt`
- Modify: `common/decisions/ww1_serbia_decisions.txt`
- Modify: `common/ideas/ww1_serbia_ideas.txt`

- [ ] **Step 1:** In `events/ww1_serbia_events.txt`:
  - Enhance `ww1_serbia.7` (Sarajevo Conspiracy): Choice between investigating/arresting conspirators (shifting BoP strongly to Pašić, risking military mutiny) or letting the plot proceed (shifting BoP to Apis).
  - Enhance `ww1_serbia.8` (Austrian Ultimatum): Comprehensive response options.
  - Create `ww1_serbia.20`: *The 1915 Typhus Epidemic* (inflicts casualty attrition and organization loss).
  - Create `ww1_serbia.21`: *Arrival of Dr. Elsie Inglis & Scottish Women's Hospitals* (mitigates typhus, restores manpower).
  - Create `ww1_serbia.22`: *Radoje Ljutovac's First Anti-Aircraft Shootdown in History* (Awards artillery tech bonus and PP).
- [ ] **Step 2:** In `common/decisions/ww1_serbia_decisions.txt`:
  - `SER_dec_major_gavrilovic_last_stand`: *Order of Major Gavrilović* (+30% core defense, +20% entrenchment in state 107 / Belgrade).
  - `SER_dec_scottish_women_hospitals`: Invites foreign sanitary missions.
- [ ] **Step 3:** In `common/ideas/ww1_serbia_ideas.txt`:
  - Add `SER_major_gavrilovic_spirit`, `SER_typhus_epidemic_crisis`, `SER_foreign_medical_missions_aid`.
- [ ] **Step 4:** Verify with `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_belgrade_defense_and_typhus_crisis -v`.
- [ ] **Step 5:** Commit:
  `git add events/ww1_serbia_events.txt common/decisions/ww1_serbia_decisions.txt common/ideas/ww1_serbia_ideas.txt`  
  `git commit -m "feat(ser): implement Major Gavrilovic defense, Sarajevo investigation, and typhus crisis"`

---

### Task 5: Focus Tree Expansion & The 4 Yugoslav/Serbian Destinies

**Files:**
- Modify: `common/national_focus/serbia.txt`
- Modify: `common/ideas/ww1_serbia_ideas.txt`

- [ ] **Step 1:** Expand political and post-war branches in `common/national_focus/serbia.txt`:
  - Political Wing: Connect with BoP triggers and the Salonika Trial (`SER_salonika_trial_of_apis`).
  - Military Wing: Add focuses for Major Gavrilović's defense, French rearmament, and Dobro Pole breakthrough (`SER_breakthrough_at_dobro_pole`).
  - The 4 Mutually Exclusive Destinies:
    * Path 1: `SER_proclamation_of_yugoslavia` (Kingdom of Serbs, Croats and Slovenes - awards `SER_yugoslav_kingdom_unification`).
    * Path 2: `SER_restored_sovereign_serbia` (Greater Serbia Centralism - awards `SER_greater_serbian_hegemony`).
    * Path 3: `SER_balkan_socialist_soviet_republic` (Balkan Socialist Federation - awards `SER_balkan_soviet_federation`).
    * Path 4: `SER_apis_pretorian_military_junta` (Black Hand Military State - awards `SER_black_hand_junta_rule`).
- [ ] **Step 2:** Ensure zero coordinate collisions ($\Delta x \ge 2$), valid DAG dependencies, and net bracket balance delta = 0.
- [ ] **Step 3:** Verify with `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_four_yugoslav_destinies -v`.
- [ ] **Step 4:** Commit:
  `git add common/national_focus/serbia.txt common/ideas/ww1_serbia_ideas.txt`  
  `git commit -m "feat(ser): expand Serbian focus tree with 4 distinct political and post-war destinies"`

---

### Task 6: Military Vojvodas, Milunka Savić & Arms Industry

**Files:**
- Modify: `common/characters/SER.txt`
- Modify: `common/decisions/ww1_serbia_decisions.txt`
- Modify: `common/ideas/ww1_serbia_ideas.txt`
- Modify: `history/countries/SER - Serbia.txt`

- [ ] **Step 1:** In `common/characters/SER.txt`:
  - Update the 4 legendary Vojvodas with unique traits:
    * `SER_radomir_putnik`: `vojvoda_wheelchair_strategist`
    * `SER_zivojin_misic`: `vojvoda_kolubara_master`
    * `SER_stepa_stepanovic`: `vojvoda_hero_of_cer`
    * `SER_petar_bojovic`: `vojvoda_liberator_of_belgrade`
  - Add `SER_vojin_popovic_vuk`: `chetnik_guerilla_leader`
  - Add character `SER_milunka_savic`: Advisor/Heroine with traits `national_heroine`, `iron_regiment_veteran` (+10% army morale, +10% trench defense).
  - Add character `SER_dragutin_gavrilovic`: Military commander / defensive specialist.
- [ ] **Step 2:** In `common/decisions/ww1_serbia_decisions.txt`:
  - Add industrial decisions for *Vojno-Tehnički Zavod Kragujevac* (Mauser-Koka production) and *Société des Mines de Bor* (French copper extraction).
  - Add decision to promote Milunka Savić and designate the *Iron Regiment* (*Gvozdeni Puk*).
- [ ] **Step 3:** Verify all modifier tokens via `scripts/hoi4_semantic_oracle.py`.
- [ ] **Step 4:** Verify with `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v`.
- [ ] **Step 5:** Commit:
  `git add common/characters/SER.txt common/decisions/ww1_serbia_decisions.txt common/ideas/ww1_serbia_ideas.txt history/countries/SER\ -\ Serbia.txt`  
  `git commit -m "feat(ser): add Vojvoda traits, Milunka Savic, and Kragujevac arms industry"`

---

### Task 7: Full Bilingual Localization Engine (English & Brazilian Portuguese)

**Files:**
- Modify: `localisation/english/ww1_serbia_l_english.yml`
- Modify: `localisation/braz_por/ww1_serbia_l_braz_por.yml`

- [ ] **Step 1:** Populate all new keys from Tasks 2 through 6 in `localisation/english/ww1_serbia_l_english.yml`:
  - BoP keys (`bop_ser_civil_military`, sides, ranges).
  - Great Retreat decisions, events, tooltips, and ideas (`SER_otadzbina_u_pokretu`).
  - Major Gavrilović, Milunka Savić, and Typhus crisis keys.
  - Vido Memorial, Essad Pasha, and Odessa Volunteer Division keys.
  - The 4 Yugoslav/Serbian destinies and focus descriptions.
- [ ] **Step 2:** Translate and synchronize 100% of keys into Brazilian Portuguese in `localisation/braz_por/ww1_serbia_l_braz_por.yml`.
- [ ] **Step 3:** Ensure single UTF-8 BOM byte sequence (`\xef\xbb\xbf`) on both files, 0 double BOM, and 100% key parity.
- [ ] **Step 4:** Verify with `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_localisation_bom_and_parity -v`.
- [ ] **Step 5:** Commit:
  `git add localisation/english/ww1_serbia_l_english.yml localisation/braz_por/ww1_serbia_l_braz_por.yml`  
  `git commit -m "feat(loc): implement complete bilingual localization with single UTF-8 BOM for Serbia rework"`

---

### Task 8: Master QA Audit, Staging Mirroring & Remote Push

**Files:**
- Modify: `scripts/qa_audit_all.py`
- Target: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

- [ ] **Step 1:** Run master QA audit: `python scripts/qa_audit_all.py`. All 14 suites must pass with exit code 0.
- [ ] **Step 2:** Synchronize all modified and created mod files to the Steam Workshop mirror directory (`E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`) using PowerShell.
- [ ] **Step 3:** Push all commits to remote: `git push origin main`.
- [ ] **Step 4:** Present completion report artifact to the user.
