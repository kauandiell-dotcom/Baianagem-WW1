# Task 6 Brief: Military Vojvodas, Milunka Savić & Arms Industry

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`

## Objectives
1. **Characters (`common/characters/SER.txt` & `history/countries/SER - Serbia.txt`):**
   - Enhance the 4 legendary Vojvodas with authentic historical traits:
     * `SER_radomir_putnik`: `vojvoda_wheelchair_strategist` (Grand strategist, max planning factor, entrenchment)
     * `SER_zivojin_misic`: `vojvoda_kolubara_master` (Kolubara counter-offensive master, attack + defense)
     * `SER_stepa_stepanovic`: `vojvoda_hero_of_cer` (Cer Mountain victor, reconnaissance, core defense)
     * `SER_petar_bojovic`: `vojvoda_liberator_of_belgrade` (Frontline liberator, division speed, assault)
   - Add `SER_vojin_popovic_vuk`: Chetnik guerilla detachment commander (`chetnik_guerilla_leader`).
   - Add `SER_milunka_savic`: The most decorated female combatant in WW1 history (`national_heroine`, `iron_regiment_veteran` advisor).
   - Add `SER_dragutin_gavrilovic`: Hero of Belgrade defense.
   - Recruit characters in `history/countries/SER - Serbia.txt`.

2. **Decisions (`common/decisions/ww1_serbia_decisions.txt`):**
   - Fast-failing `allowed = { original_tag = SER }`.
   - `SER_dec_kragujevac_arms_manufactory`: Vojno-Tehnički Zavod Kragujevac expansion (Mauser-Koka rifles, +1 military factory in state 108).
   - `SER_dec_bor_copper_mines_concession`: French concessions at Bor copper mines (resource output / industrial bonus).
   - `SER_dec_gvozdeni_puk_iron_regiment`: Formal designation of the 2nd Infantry Regiment "Knjaz Mihailo" (*Gvozdeni Puk* - Iron Regiment) with Milunka Savić, giving elite division bonuses.

3. **Ideas (`common/ideas/ww1_serbia_ideas.txt`):**
   - `SER_kragujevac_arsenal`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { industrial_capacity_factory = 0.10 production_speed_arms_factory_factor = 0.15 }`
   - `SER_bor_copper_concession`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { local_resources_factor = 0.20 consumer_goods_factor = -0.03 }`
   - `SER_gvozdeni_puk_spirit`:
     - `allowed = { always = no }`
     - `removal_cost = -1`
     - `modifier = { army_org_factor = 0.08 army_morale_factor = 0.10 special_forces_attack_factor = 0.10 }`

4. **Validation:**
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers -v`.
   - Bracket balance delta = 0 across all files.

5. **Commit:**
   - `git add common/characters/SER.txt common/decisions/ww1_serbia_decisions.txt common/ideas/ww1_serbia_ideas.txt history/countries/SER\ -\ Serbia.txt`
   - `git commit -m "feat(ser): add Vojvoda traits, Milunka Savic, and Kragujevac arms industry"`
