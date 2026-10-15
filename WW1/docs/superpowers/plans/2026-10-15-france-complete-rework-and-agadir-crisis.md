# French Republic Complete Rework & Agadir Crisis Escalation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform France (`FRA`) and the 1911 Agadir Crisis in *Baianagem-WW1* into an authentic, deeply interactive historical simulation featuring a multi-stage crisis escalation engine, 4 dynamic survival vectors (Union Sacrée, Poilu Morale, Coal & Steel, Demographic Pool), military and civil crises (1917 Mutinies, Munitionnettes, French *Endsieg*), and 4 divergent political destinies (Third Republic, Second Paris Commune, Action Française Orléanist Monarchy, GQG Military Directory).

**Architecture:** Gated Clausewitz event chains, dynamic tension variable (`global.ww1_agadir_crisis_tension`), clamped survival vector scripting, fast-failing decision categories, non-colliding focus DAGs, semantic oracle validated modifiers, and single UTF-8 BOM bilingual localization.

**Tech Stack:** Hearts of Iron IV Clausewitz Script, Python automated unit testing (`unittest`), Git, Steam Workshop staging pipeline.

**Spec:** `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`

## Global Constraints
- Bracket syntax must balance with net delta = 0 across all modified and created `.txt` files.
- All modifier tokens must exist in `data/hoi4_valid_country_modifiers.json` with 0 oracle errors.
- Every YAML localization file must begin with exactly one single UTF-8 BOM byte sequence (`\xef\xbb\xbf`).
- Absolute avoidance of dynamic `start_civil_war` spawns to prevent ghost tags; all breakaway dynamics use fixed tags and faction lockdowns (`can_join_factions = no`).
- Every changed or created file must be synchronized with the Steam Workshop mirror at `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.

## Review Focus
1. **Day 1 Crisis Immunity:** Crisis triggers (Mutinies, Commune, Endsieg) must NOT trigger on 1911.6.1; strictly gated behind wartime, threshold dates, and casualty/surrender metrics.
2. **Neukamerun Territorial Integrity:** The transfer of states 1086, 1087, 1088 during the Agadir Crisis Accord must cleanly execute state ownership/control transfer without phantom cores or CTDs.
3. **Agadir Crisis Pacing:** The crisis must escalate and resolve briskly within 6 to 12 in-game weeks without stalling the game.
4. **Mutiny Unlocking Fix:** Event `ww1_france.210` must properly apply `FRA_trench_mutiny_crisis_2` so that Pétain's leave reform decision is operable.
5. **Localization Parity:** English and Brazilian Portuguese files must have 100% identical key sets.

---

### Task 1: QA RED Test Baseline (`tests/test_ww1_france_rework.py`)

**Files:**
- Create: `tests/test_ww1_france_rework.py`
- Modify: `scripts/qa_audit_all.py`

- [x] **Step 1:** Create `tests/test_ww1_france_rework.py` with test class `TestFranceOverhaul` covering:
  - `test_agadir_crisis_mechanics`: Verifies existence of `global.ww1_agadir_crisis_tension`, decisions in `ww1_agadir_crisis`, Neukamerun transfers (1086, 1087, 1088), and 4 outcome branches.
  - `test_republic_dashboard_variables`: Verifies scripted effects `FRA_init_republic_dashboard`, `FRA_clamp_dashboard_variables`, and clamping of `FRA_union_sacree_cohesion`, `FRA_poilu_morale`, `FRA_charbon_et_acier`, `FRA_reserves_humaines`.
  - `test_four_political_destinies`: Verifies focuses in `common/national_focus/france.txt` for Third Republic (`FRA_presidence_poincare` / `FRA_clemenceau_je_fais_la_guerre`), Second Paris Commune (`FRA_republique_des_soviets_de_paris`), Action Française (`FRA_restauration_orleaniste_jean_iii`), and GQG Junta (`FRA_directoire_militaire_gqg`).
  - `test_mutinies_and_civil_crises`: Verifies `ww1_france.210` applies mutiny spirit, unlocks `FRA_petain_welfare_and_leave_reform`, and tests French Endsieg spirit `FRA_jusqu_au_bout_endsieg`.
  - `test_semantic_oracle_modifiers`: Runs `scripts/hoi4_semantic_oracle.py` on all French ideas and decisions to verify 0 invalid modifier errors.
  - `test_localisation_bom_and_parity`: Asserts single UTF-8 BOM on `localisation/english/ww1_france_rework_l_english.yml` and `localisation/braz_por/ww1_france_rework_l_braz_por.yml`, 0 double BOM, and 100% key parity.
- [x] **Step 2:** Register `tests.test_ww1_france_rework` as Suite 13 in `scripts/qa_audit_all.py`.
- [x] **Step 3:** Run `python -m unittest tests.test_ww1_france_rework -v` to confirm failure (RED phase).
- [x] **Step 4:** Commit baseline:
  `git add tests/test_ww1_france_rework.py scripts/qa_audit_all.py`  
  `git commit -m "test(fra): establish comprehensive RED QA test suite for France overhaul & Agadir Crisis"`

---

### Task 2: Agadir Crisis Interactive Escalation Engine (1911)

**Files:**
- Create: `common/decisions/categories/ww1_agadir_crisis_categories.txt`
- Create: `common/decisions/ww1_agadir_crisis_decisions.txt`
- Modify: `events/WW1_Agadir.txt`
- Modify: `common/on_actions/ww1_crisis_on_actions.txt`
- Modify: `common/national_focus/france.txt`
- Modify: `common/national_focus/germany.txt`

- [x] **Step 1:** Define decision category `ww1_agadir_crisis` in `common/decisions/categories/ww1_agadir_crisis_categories.txt` with fast-failing `allowed = { OR = { tag = GER tag = FRA tag = ENG } }` and visibility tied to `has_global_flag = agadir_crisis_active`.
- [x] **Step 2:** Implement interactive decisions in `common/decisions/ww1_agadir_crisis_decisions.txt`:
  - Germany: `GER_agadir_demand_naval_base`, `GER_agadir_demand_congo_compensation`, `GER_agadir_send_sms_berlin`, `GER_agadir_back_down_gracefully`.
  - France: `FRA_agadir_caillaux_secret_channel`, `FRA_agadir_delcasse_firm_resolve`, `FRA_agadir_financial_sanctions`, `FRA_agadir_concede_congo_accord`.
  - Britain: `ENG_agadir_mansion_house_speech`, `ENG_agadir_home_fleet_alert`, `ENG_agadir_urge_moderation`.
- [x] **Step 3:** Overhaul `events/WW1_Agadir.txt` into a multi-tiered event engine with namespaces `ww1_agadir`:
  - `ww1_agadir.1`: Arrival of SMS *Panther* (initializes tension at 25, sets `agadir_crisis_active`).
  - `ww1_agadir.10`: Historical Franco-German Accord & Treaty of Fez (transfers states 1086, 1087, 1088 to GER, gives FRA Moroccan Protectorate `FRA_morocco_treaty_of_fez`, triggers Caillaux leak).
  - `ww1_agadir.20`: Pan-German Naval Base Acquired (Agadir naval base granted to GER, stability hit to FRA).
  - `ww1_agadir.30`: German Humiliation & Withdrawal (Panther recalled empty-handed, -100 PP to GER, triggers 1912 German Army Bill rage).
  - `ww1_agadir.40`: Early Conflagration 1911 (Entente and Central Powers go to war).
- [x] **Step 4:** Hook weekly tension update in `common/on_actions/ww1_crisis_on_actions.txt`.
- [x] **Step 5:** Connect focuses `FRA_question_du_maroc_1911`, `FRA_fermete_diplomatique_agadir`, `FRA_compromis_colonial_allemand`, and `GER_agadir_crisis_gambit` to the dynamic engine.
- [x] **Step 6:** Verify with `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_agadir_crisis_mechanics -v`.
- [x] **Step 7:** Commit:
  `git add common/decisions/categories/ww1_agadir_crisis_categories.txt common/decisions/ww1_agadir_crisis_decisions.txt events/WW1_Agadir.txt common/on_actions/ww1_crisis_on_actions.txt common/national_focus/france.txt common/national_focus/germany.txt`  
  `git commit -m "feat(agadir): implement complete interactive Agadir Crisis escalation engine and 4 climax branches"`

---

### Task 3: Republic Dashboard & The 4 Dynamic Survival Vectors

**Files:**
- Create: `common/scripted_effects/ww1_france_dashboard_effects.txt`
- Modify: `common/on_actions/ww1_crisis_on_actions.txt`
- Create: `common/decisions/ww1_france_dashboard_decisions.txt`
- Create: `common/ideas/ww1_france_dashboard_ideas.txt`

- [x] **Step 1:** Implement scripted effects in `common/scripted_effects/ww1_france_dashboard_effects.txt`:
  - `FRA_init_republic_dashboard`: Initializes `FRA_union_sacree_cohesion = 80`, `FRA_poilu_morale = 75`, `FRA_charbon_et_acier = 70`, `FRA_reserves_humaines = 85`.
  - `FRA_clamp_dashboard_variables`: Clamps all 4 variables between 0 and 100 via `clamp_variable`.
  - `FRA_weekly_republic_tick`: Handles wartime weariness, frontline casualty deductions, coal/steel consumption, and checks crisis thresholds.
- [x] **Step 2:** Hook `FRA_weekly_republic_tick` under `on_weekly_FRA` in `common/on_actions/ww1_crisis_on_actions.txt`.
- [x] **Step 3:** Implement dynamic ideas in `common/ideas/ww1_france_dashboard_ideas.txt` reflecting vector states:
  - `FRA_union_sacree_strong` vs `FRA_union_sacree_fractured`.
  - `FRA_poilu_morale_high` vs `FRA_poilu_morale_demoralized`.
  - `FRA_charbon_et_acier_surplus` vs `FRA_charbon_et_acier_famine`.
- [x] **Step 4:** Implement emergency survival decisions in `common/decisions/ww1_france_dashboard_decisions.txt`:
  - `FRA_dec_british_channel_coal`: Requisitions British coal convoys (+20 charbon, costs trade/PP).
  - `FRA_dec_call_up_class_1917`: Mobilizes the *Bleuets* (+50k manpower, +15 reserves humaines, -5% stability).
  - `FRA_dec_colonial_recruitment_tirailleurs`: Recruits Senegalese and Algerian riflemen (+60k manpower).
  - `FRA_dec_union_sacree_cross_party_pact`: Convenes the Chamber of Deputies to restore political unity (+15 Union Sacrée).
- [x] **Step 5:** Run test: `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_republic_dashboard_variables -v`.
- [x] **Step 6:** Commit:
  `git add common/scripted_effects/ww1_france_dashboard_effects.txt common/on_actions/ww1_crisis_on_actions.txt common/decisions/ww1_france_dashboard_decisions.txt common/ideas/ww1_france_dashboard_ideas.txt`  
  `git commit -m "feat(fra): implement French Republic Dashboard, 4 survival vectors, and emergency decisions"`

---

### Task 4: Military Mutinies (1917) & Civil Crises Engine (*Jusqu'au Bout!*)

**Files:**
- Modify: `events/ww1_france_events.txt`
- Create: `common/ideas/ww1_france_crises_ideas.txt`
- Modify: `common/decisions/ww1_france_decisions.txt`

- [x] **Step 1:** In `common/ideas/ww1_france_crises_ideas.txt`, define ideas:
  - `FRA_trench_mutiny_crisis_2`: -25% army attack, -15% breakthrough, -10% division defense.
  - `FRA_poilus_reconcilies`: +10% division defense, +10% recovery rate.
  - `FRA_munitionnettes_strike`: -20% factory output, -10% stability.
  - `FRA_jusqu_au_bout_endsieg`: +20% core defense, +15% war support, +0.10 daily political power, -50% surrender limit factor.
- [x] **Step 2:** In `events/ww1_france_events.txt`:
  - Overhaul `ww1_france.210` to apply `FRA_trench_mutiny_crisis_2` and fire the mutiny narrative chain.
  - Implement `ww1_france.211` (Pétain's appointment & leave reform), `ww1_france.212` (Military tribunal executions), `ww1_france.213` (Mutineer fraternization).
  - Implement `ww1_france.215` (Munitionnettes strike in Paris) and `ww1_france.220` (Clemenceau's *Jusqu'au Bout!* speech).
- [x] **Step 3:** In `common/decisions/ww1_france_decisions.txt`, fix decision requirements for `FRA_petain_welfare_and_leave_reform` and populate category `FRA_mutinies_crisis_management`.
- [x] **Step 4:** Run test: `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_mutinies_and_civil_crises -v`.
- [x] **Step 5:** Commit:
  `git add events/ww1_france_events.txt common/ideas/ww1_france_crises_ideas.txt common/decisions/ww1_france_decisions.txt`  
  `git commit -m "feat(fra): overhaul 1917 French Army Mutinies, Munitionnettes strikes, and Clemenceau Endsieg"`

---

### Task 5: The 4 Divergent Political Destinies & Focus Tree Expansion

**Files:**
- Modify: `common/national_focus/france.txt`
- Create: `common/ideas/ww1_france_political_ideas.txt`
- Modify: `common/characters/FRA.txt`
- Modify: `history/countries/FRA - France.txt`

- [x] **Step 1:** Add historical character definitions to `common/characters/FRA.txt`:
  - `FRA_charles_maurras` (Action Française ideologue / advisor)
  - `FRA_king_jean_iii` (Prince Jean, Duke of Guise - Monarchist Head of State)
  - `FRA_jean_longuet` (Socialist/Communist Pacifist leader)
  - `FRA_fernand_loriot` (Revolutionary Syndicalist leader)
  - `FRA_georges_clemenceau` (Prime Minister / The Tiger)
- [x] **Step 2:** In `common/ideas/ww1_france_political_ideas.txt`, implement authentic national ideas:
  - `FRA_union_sacree_spirit` (Third Republic)
  - `FRA_commune_de_paris_spirit` (Second Paris Commune)
  - `FRA_action_francaise_monarchy` (Kingdom of France)
  - `FRA_gqg_military_directory` (Military Dictatorship)
- [x] **Step 3:** In `common/national_focus/france.txt`, expand the political wing (x = 0..25) with 4 mutually exclusive branches:
  - Branch 1: Third Republic & Union Sacrée (`FRA_republique_union_sacree`, `FRA_clemenceau_je_fais_la_guerre`).
  - Branch 2: Second Paris Commune (`FRA_republique_des_soviets_de_paris`, `FRA_comite_de_salut_public_1917`).
  - Branch 3: Action Française & Monarchy (`FRA_abattre_la_gueuse`, `FRA_restauration_orleaniste_jean_iii`).
  - Branch 4: GQG Military Directory (`FRA_directoire_militaire_gqg`, `FRA_etat_de_siege_permanent`).
- [x] **Step 4:** Verify coordinates, mutual exclusions, and bracket balance.
- [x] **Step 5:** Run test: `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_four_political_destinies -v`.
- [x] **Step 6:** Commit:
  `git add common/national_focus/france.txt common/ideas/ww1_france_political_ideas.txt common/characters/FRA.txt history/countries/FRA\ -\ France.txt`  
  `git commit -m "feat(fra): implement 4 divergent political destinies, Action Française, Commune, and GQG Directory"`

---

### Task 6: Industrial Relocation, Northeast Loss & Allied Convoys

**Files:**
- Modify: `common/decisions/ww1_france_decisions.txt`
- Modify: `common/decisions/categories/ww1_france_categories.txt`

- [x] **Step 1:** Populate `FRA_war_economy_and_munitions`:
  - `FRA_dec_evacuate_briey_machinery` (transfers industrial capacity from front states before occupation).
  - `FRA_dec_lyon_chemical_complex` (expands synthetic and gunpowder manufacturing in south/central France).
  - `FRA_dec_schneider_creusot_heavy_guns` (boosts heavy artillery production).
- [x] **Step 2:** Populate `FRA_defence_of_verdun`:
  - `FRA_dec_fort_douaumont_reinforcement`.
  - `FRA_dec_voix_sacree_truck_convoys`.
- [x] **Step 3:** Populate `FRA_entente_diplomacy`:
  - `FRA_dec_inter_allied_supreme_war_council`.
  - `FRA_dec_us_morgan_bank_credit_line`.
- [x] **Step 4:** Run test: `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_modifier_oracle_and_balance -v`.
- [x] **Step 5:** Commit:
  `git add common/decisions/ww1_france_decisions.txt common/decisions/categories/ww1_france_categories.txt`  
  `git commit -m "feat(fra): populate wartime industrial relocation, Verdun redoubts, and Allied cooperation decisions"`

---

### Task 7: Full Bilingual Localization Engine (English & Brazilian Portuguese)

**Files:**
- Create: `localisation/english/ww1_france_rework_l_english.yml`
- Create: `localisation/braz_por/ww1_france_rework_l_braz_por.yml`

- [x] **Step 1:** Generate `localisation/english/ww1_france_rework_l_english.yml` with single UTF-8 BOM (`\xef\xbb\xbf`).
- [x] **Step 2:** Generate `localisation/braz_por/ww1_france_rework_l_braz_por.yml` with single UTF-8 BOM (`\xef\xbb\xbf`).
- [x] **Step 3:** Include 100% key parity covering all focuses, ideas, decisions, events, variables, and tooltips introduced in Tasks 2 through 6.
- [x] **Step 4:** Run test: `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_localisation_bom_and_parity -v`.
- [x] **Step 5:** Commit:
  `git add localisation/english/ww1_france_rework_l_english.yml localisation/braz_por/ww1_france_rework_l_braz_por.yml`  
  `git commit -m "feat(loc): implement complete bilingual localization with single UTF-8 BOM for France rework"`

---

### Task 8: Master QA Audit, Staging Mirroring & Git Push

**Files:**
- All modified and created files
- Mirror Target: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

- [ ] **Step 1:** Run full master QA audit suite: `python scripts/qa_audit_all.py` (all 13 suites must pass 100%).
- [ ] **Step 2:** Synchronize all repository changes to Steam Workshop directory `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.
- [ ] **Step 3:** Check `git status` and `git diff` for clean repository state.
- [ ] **Step 4:** Push to remote: `git push origin main`.
- [ ] **Step 5:** Create France Rework completion report artifact.
