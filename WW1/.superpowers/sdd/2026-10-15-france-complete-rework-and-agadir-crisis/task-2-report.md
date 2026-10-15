# Task 2 Report: Agadir Crisis Interactive Escalation Engine (1911)

## Summary
Successfully implemented the complete, interactive Agadir Crisis diplomatic escalation engine for World War I (1911) in Baianagem-WW1, providing dynamic tension tracking between Germany (`GER`), France (`FRA`), and Great Britain (`ENG`), supported by 11 interactive decisions and 4 divergent climax outcomes.

## Deliverables Completed
1. **Decision Category (`common/decisions/categories/ww1_agadir_crisis_categories.txt`):**
   - Created category `ww1_agadir_crisis` with fast-failing `allowed = { OR = { tag = GER tag = FRA tag = ENG } }` and visibility conditioned on `has_global_flag = agadir_crisis_active`.
2. **Interactive Decision Engine (`common/decisions/ww1_agadir_crisis_decisions.txt`):**
   - Implemented German decisions:
     * `GER_agadir_demand_naval_base`: Demands coaling station / naval base at Agadir (state 462), tension +25.
     * `GER_agadir_demand_congo_compensation`: Demands French Congo (*Neukamerun*, states 1086, 1087, 1088), tension +10.
     * `GER_agadir_send_sms_berlin`: Dispatches SMS *Berlin* to reinforce *Panther*, tension +15, +5% war support.
     * `GER_agadir_back_down_gracefully`: Recalls *Panther*, tension -30, triggers `ww1_agadir.30`.
   - Implemented French decisions:
     * `FRA_agadir_caillaux_secret_channel`: Caillaux's secret backchannel talks, tension -20.
     * `FRA_agadir_delcasse_firm_resolve`: Hardline nationalist defiance, tension +20, +10% war support, British diplomatic alignment.
     * `FRA_agadir_financial_sanctions`: Withdraws French bank short-term credit from Berlin, inflicting -5% stability and -50 PP on GER.
     * `FRA_agadir_concede_congo_accord`: Concludes the Treaty of Fez and Congo Accord, triggering historical resolution `ww1_agadir.10`.
     * `FRA_agadir_concede_naval_station`: Concedes Agadir port to Germany, triggering `ww1_agadir.20`.
   - Implemented British decisions:
     * `ENG_agadir_mansion_house_speech`: Lloyd George's speech, tension +15, grants British guarantee to France.
     * `ENG_agadir_home_fleet_alert`: Readies Home Fleet at Portland, tension +15, +5% war support.
     * `ENG_agadir_urge_moderation`: Advises colonial compensation in Central Africa, tension -15.
3. **Event Engine Overhaul (`events/WW1_Agadir.txt`):**
   - Declared namespace: `add_namespace = ww1_agadir`.
   - `ww1_agadir.1` (*Panthersprung*): SMS *Panther* arrives in Agadir. Initializes `global.ww1_agadir_crisis_tension = 25`, sets `agadir_crisis_active`, and triggers notifications for FRA and ENG.
   - `ww1_agadir.10` (*Treaty of Fez & Congo Accord - Historical Climax*):
     * Awards France `FRA_morocco_treaty_of_fez` and `FRA_poincare_national_firmness`.
     * Transfers *Neukamerun* states (1086, 1087, 1088) to Germany and adds 2 shared building slots to Cameroon (state 773).
     * Simulates the leak of Caillaux's secret diplomacy and fall of cabinet (`fra_caillaux_fallen`), leading to Poincaré's premiership.
     * Clears `agadir_crisis_active` and sets `agadir_crisis_resolved_historical`.
   - `ww1_agadir.20` (*Pan-German Triumph: Naval Station at Agadir*):
     * Grants naval base (level 2) and coastal bunker (level 2) in Agadir (state 462).
     * Awards Germany PP and war support; France loses 10% stability and 50 PP.
     * Clears `agadir_crisis_active` and sets `agadir_crisis_resolved_german_base`.
   - `ww1_agadir.30` (*The German Retreat: Panther Withdrawn*):
     * Germany recalls *Panther* empty-handed (-100 PP, -5% stability).
     * France secures Moroccan protectorate (`FRA_morocco_treaty_of_fez`) without ceding territory.
     * Clears `agadir_crisis_active` and sets `agadir_crisis_resolved_humiliation`.
   - `ww1_agadir.40` (*The Premature Conflagration: World War I in 1911*):
     * Fired when tension reaches 100 or an ultimatum is defied.
     * Central Powers and Entente enter full-scale war (`GER = { declare_war_on = { target = FRA type = annex_everything } }`).
     * Clears `agadir_crisis_active` and sets `agadir_crisis_war_1911`.
4. **On-Actions Hook (`common/on_actions/ww1_crisis_on_actions.txt`):**
   - Configured `on_weekly_GER`:
     * Clamps `global.ww1_agadir_crisis_tension` between 0 and 100 via `clamp_variable`.
     * Evaluates `global.ww1_agadir_crisis_tension >= 100`, triggering `ww1_agadir.40`.
5. **Focus Tree Integration:**
   - In `common/national_focus/germany.txt`: Updated `GER_agadir_crisis_gambit` to activate `agadir_crisis_active` and add +15 tension while strictly preserving states 773 and 1088 references and spec compliance.
   - In `common/national_focus/france.txt`: Connected `FRA_question_du_maroc_1911` (crisis initiation / tension set), `FRA_fermete_diplomatique_agadir` (+15 tension, Delcassé flag), and `FRA_compromis_colonial_allemand` (-15 tension, Caillaux secret talks flag).

## Verification Results
- `tests.test_ww1_france_rework.TestFranceOverhaul.test_agadir_crisis_mechanics`: **PASS** (OK)
- `tests.test_runner` (Tier 1-4 German Empire Mod suite): **21 / 21 PASS** (OK)
- `tests.test_ww1_france` (French Republic Rework suite): **8 / 8 PASS** (OK)
- Bracket Balance Verification: **Diff = 0 across all 6 files** (100% matched braces verified via AST parser)

## Git Commit
- Commit Hash: `1346a44`
- Commit Message: `feat(agadir): implement complete interactive Agadir Crisis escalation engine and 4 climax branches`
