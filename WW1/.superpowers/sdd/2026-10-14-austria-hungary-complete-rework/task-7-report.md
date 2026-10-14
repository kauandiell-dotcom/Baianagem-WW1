# Task 7 Report: Pre-War Espionage (Colonel Redl), Sixtus Affair & Danubian Hegemony

## 1. Overview
- **Task**: Task 7 of Austria-Hungary Complete Rework & Fragmentation System.
- **Commit**: `03a741a` (`feat(auh): implement Colonel Redl espionage affair, Sixtus peace negotiations, and Danubian hegemony`)
- **Status**: Completed & Verified.

## 2. Deliverables Implemented
1. `events/ww1_austria_diplomacy_events.txt`:
   - Namespace: `ww1_austria_diplomacy`
   - `ww1_austria_diplomacy.1`: The Colonel Redl Espionage Affair (May 1913).
     - Gated: `tag = AUS`, `date > 1913.5.1`, `date < 1913.12.1`, `NOT = { has_war = yes }`.
     - Option A: Overhaul mobilization Plan B/R (costs 50 PP, removes Russian intel advantage, adds stability).
     - Option B: Cover up suicide to preserve Evidenzbureau honor (-10% army defense vs Russia in 1914).
   - `ww1_austria_diplomacy.10`: The Sixtus Affair (March 1917).
     - Gated: `tag = AUS`, `date > 1917.3.1`, `has_war = yes`, `country_exists = FRA`.
     - Emperor Karl I initiates clandestine peace feelers to France via Prince Sixte of Bourbon-Parma.
     - Option A: Pursue honorable separate peace feelers (reduces war weariness by 10 points, dispatches event `ww1_austria_diplomacy.11` to France).
     - Option B: Reaffirm loyalty to the German alliance (Pact of Spring 1917, increases war support, dispatches event `ww1_austria_diplomacy.12` to Germany).
   - `ww1_austria_diplomacy.20`: The Austro-Polish Solution.
     - Gated: `tag = AUS`, `OR = { controls_state = 10 has_global_flag = poland_liberated }`.
     - Option A: Crown Archduke Karl Stephan as King of Poland (creates Polish client state under Vienna, assigns cosmetic tag `POL_AUS_danubian_state`, applies `can_join_factions = no`).
     - Option B: Yield administration to German General Government of Warsaw.
   - `ww1_austria_diplomacy.30`: The Brotfrieden (Bread Peace, February 1918).
     - Gated: `tag = AUS`, `has_war = yes`, `date > 1918.1.1`, `check_variable = { AUH_vienna_grain < 40 }`.
     - Option A: Conclude agricultural deliveries from Ukraine (adds 40 `AUH_vienna_grain`, clamps variables, relieves food pressure).
     - Option B: Refuse diplomatic concessions (inflicts stability loss and increases war weariness).

2. `common/decisions/ww1_austria_diplomacy_decisions.txt`:
   - Integrated into category `AUH_crown_dashboard`.
   - Includes fast-failing `allowed = { original_tag = AUS }` and `visible = { tag = AUS }`.
   - Decisions:
     - `AUH_dec_prince_wied_albania`: Backing Prince Wilhelm of Wied in Albania (+5 cohesion, +0.05 stability).
     - `AUH_dec_danubian_customs_union`: Establishing preferential tariff zone across the Balkans (+15 grain, +5 cohesion).

## 3. QA & Verification Results
- **Clausewitz Bracket Balance**:
  - `events/ww1_austria_diplomacy_events.txt`: 100% Balanced (`ClausewitzAuditor.audit_braces: True OK`, Diff = 0).
  - `common/decisions/ww1_austria_diplomacy_decisions.txt`: 100% Balanced (`ClausewitzAuditor.audit_braces: True OK`, Diff = 0).
- **Unit Test**:
  - Command: `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_diplomacy_events_and_redl -v`
  - Result: `OK` (1 passed in 0.018s).
- **Master Regression Status**:
  - 7 out of 8 tests in `tests.test_ww1_austria_hungary` passing. The remaining test is `test_localisation_bom_and_parity`, which belongs to Task 8.
