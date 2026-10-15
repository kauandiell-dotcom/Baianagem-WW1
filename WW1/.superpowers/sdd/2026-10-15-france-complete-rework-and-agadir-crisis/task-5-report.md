# Task 5 Report: The 4 Divergent Political Destinies & Focus Tree Expansion

**Date:** 2026-10-15  
**Commit:** `9a6313fe308a11c91b1f7a1ac92bd91409767933`  
**Status:** Complete & 100% Validated  

---

## 1. Executive Summary

Task 5 expands the French Republic (`FRA`) national focus tree with 4 distinct, mutually exclusive ideological destinies, breaking the previous linear monotony and enabling historical, syndicalist, royalist, and military junta trajectories. All country modifiers have been audited with `scripts/hoi4_semantic_oracle.py`, and focus tree geometry adheres strictly to the 5-wing visual grid mathematics with zero coordinate collisions and net bracket balance delta = 0.

---

## 2. Deliverables Implemented

### 1. Political Ideas File (`common/ideas/ww1_france_political_ideas.txt`)
Implemented 4 distinct national spirits with Clausewitz country modifiers:
- **`FRA_union_sacree_spirit` (Democratic / Third Republic):**
  - `stability_factor = 0.10`
  - `political_power_gain = 0.15`
  - `war_support_factor = 0.05`
- **`FRA_commune_de_paris_spirit` (Communist / Second Paris Commune):**
  - `conscription_factor = 0.15`
  - `production_factory_max_efficiency_factor = 0.10`
  - `war_support_factor = 0.10`
- **`FRA_action_francaise_monarchy` (Neutrality / Orléans Monarchy):**
  - `army_core_defence_factor = 0.15`
  - `war_support_factor = 0.15`
  - `stability_factor = 0.05`
- **`FRA_gqg_military_directory` (Authoritarian / Military Junta):**
  - `army_attack_factor = 0.10`
  - `breakthrough_factor = 0.10`
  - `mobilization_speed = 0.20`

All 9 modifier tokens were verified against `data/hoi4_valid_country_modifiers.json` with 0 invalid/hallucinated tokens.

### 2. Character Definitions (`common/characters/FRA.txt`)
Integrated and validated key political and military leaders:
- **`FRA_charles_maurras`:** Political advisor (`ideological_crusader`) and autocracy leader with authentic portrait assets (`gfx/leaders/FRA/FRA_charles_maurras.png`, `gfx/interface/ideas/FRA/FRA_charles_maurras.png`).
- **`FRA_king_jean_iii`:** Country leader for Orléans Restoration (`gfx/leaders/FRA/FRA_jean_duke_of_guise.dds`, `gfx/interface/ideas/FRA/idea_FRA_jean_iii.png`).
- **`FRA_jean_longuet`:** Socialist / pacifist SFIO advisor (`compassionate_gentleman`) and country leader.
- **`FRA_fernand_loriot`:** Revolutionary syndicalist advisor (`communist_revolutionary`) and country leader for Second Paris Commune.
- **`FRA_georges_clemenceau`:** Maintained and validated as civilian leader and advisor (`silent_workhorse`).

### 3. Focus Tree Expansion (`common/national_focus/france.txt`)
Integrated 8 new focuses arranged into 4 mutually exclusive ideological branches:
1. **Branch 1: Third Republic & Union Sacrée (Democratic)**
   - `FRA_republique_union_sacree` (x=2, y=6, cost=8): Awards `FRA_union_sacree_spirit`, +60 PP, +5% stability, +20 Union Sacrée cohesion.
   - `FRA_clemenceau_je_fais_la_guerre` (x=2, y=7, cost=8): Awards `FRA_jusqu_au_bout_endsieg`, locks democratic government, +15% war support.
2. **Branch 2: Second Paris Commune (Communism)**
   - `FRA_republique_des_soviets_de_paris` (x=7, y=6, cost=8): Awards `FRA_commune_de_paris_spirit`, sets communist regime (60% popularity), promotes Fernand Loriot.
   - `FRA_comite_de_salut_public_1917` (x=7, y=7, cost=8): +50 PP, +10% war support.
3. **Branch 3: Action Française & Orléans Monarchy (Neutrality / Monarchism)**
   - `FRA_abattre_la_gueuse` (x=12, y=6, cost=8): Awards `FRA_action_francaise_monarchy`, installs neutrality (55% popularity), +50 PP.
   - `FRA_restauration_orleaniste_jean_iii` (x=12, y=7, cost=8): Promotes King Jean III (House of Orléans), +10% stability, +10% war support.
4. **Branch 4: GQG Military Directory (Authoritarian / Non-Aligned)**
   - `FRA_directoire_militaire_gqg` (x=17, y=6, cost=8): Awards `FRA_gqg_military_directory`, installs military rule, +15% war support.
   - `FRA_etat_de_siege_permanent` (x=17, y=7, cost=8): +5% stability, +40 PP.

**Grid Architecture & Zero-Collision Assurance:**
- The 4 branch openers (`x = 2, 7, 12, 17`, `y = 6`) and follow-ups (`y = 7`) form an evenly spaced 5-wing layout ($\Delta x = 5$).
- The pre-existing civic education branch (`FRA_presse_populaire_et_illustres`, `FRA_ecole_normale_et_instituteurs`, `FRA_reorganisation_post_guerre`) was shifted from column 12 to 14, completely resolving coordinate collision at (12, 7) while maintaining strict downward progression ($dy \ge 1$).

---

## 3. Automated Test Verification Results

All required verification suites passed with 100% success:

```
test_four_political_destinies (tests.test_ww1_france_rework.TestFranceOverhaul.test_four_political_destinies) ... ok
test_semantic_oracle_modifiers (tests.test_ww1_france_rework.TestFranceOverhaul.test_semantic_oracle_modifiers) ... ok

test_bilingual_localization_parity_and_bom (tests.test_ww1_france.FranceContentReworkTests.test_bilingual_localization_parity_and_bom) ... ok
test_focus_count_and_coordinate_collisions (tests.test_ww1_france.FranceContentReworkTests.test_focus_count_and_coordinate_collisions) ... ok
test_naval_reinforcement_oob_parity (tests.test_ww1_france.FranceContentReworkTests.test_naval_reinforcement_oob_parity) ... ok
test_no_banned_modifiers_in_french_ideas (tests.test_ww1_france.FranceContentReworkTests.test_no_banned_modifiers_in_french_ideas) ... ok
test_political_cabinet_transitions (tests.test_ww1_france.FranceContentReworkTests.test_political_cabinet_transitions) ... ok
test_prerequisite_integrity_and_downward_progression (tests.test_ww1_france.FranceContentReworkTests.test_prerequisite_integrity_and_downward_progression) ... ok
test_prewar_pacing_and_crisis_costs (tests.test_ww1_france.FranceContentReworkTests.test_prewar_pacing_and_crisis_costs) ... ok
test_wartime_and_date_gating (tests.test_ww1_france.FranceContentReworkTests.test_wartime_and_date_gating) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.036s
OK
```

### Static Syntax & Bracket Balance Audit:
- `common/national_focus/france.txt`: Open = 1199, Close = 1199, Diff = 0 (ClausewitzAuditor: OK)
- `common/ideas/ww1_france_political_ideas.txt`: Open = 14, Close = 14, Diff = 0 (ClausewitzAuditor: OK)
- `common/characters/FRA.txt`: Open = 275, Close = 275, Diff = 0 (ClausewitzAuditor: OK)
- Coordinate collisions across all 208 focuses: **0 collisions**.

---

## 4. Git Artifacts
- **Commit:** `9a6313fe308a11c91b1f7a1ac92bd91409767933`
- **Subject:** `feat(fra): implement 4 divergent political destinies, Action Française, Commune, and GQG Directory`
- **Files Modified/Created:**
  - `common/characters/FRA.txt`
  - `common/ideas/ww1_france_political_ideas.txt`
  - `common/national_focus/france.txt`
  - `tests/test_ww1_france.py`
