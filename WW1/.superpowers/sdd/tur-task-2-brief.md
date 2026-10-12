# Ottoman Rework Task 2 Brief: 5-Pillar National Ideas, Semantic Oracle Fixes, GFX & Historical Characters

## Objective
Implement all missing 5-Pillar Ottoman national ideas, fix all 5 invalid Clausewitz modifier tokens in `common/ideas/ww1_ottoman_ideas.txt`, register idea sprites in `interface/ww1_ottoman_ideas.gfx`, and restore historical commanders & leaders in `common/characters/TUR.txt` and `history/countries/TUR - Turkey.txt`.

## Target Files
- `common/ideas/ww1_ottoman_ideas.txt`
- `interface/ww1_ottoman_ideas.gfx`
- `common/characters/TUR.txt`
- `history/countries/TUR - Turkey.txt`

## Requirements
1. **Fix 5 Invalid Clausewitz Modifiers in `common/ideas/ww1_ottoman_ideas.txt`:**
   - In `TUR_arab_ottoman_federal_compact`: replace `compliance_growth_focus_factor = 0.20` with `compliance_gain = 0.03`.
   - In `TUR_yavuz_and_midilli_supremacy`: replace `navy_surface_detection_factor = 0.15` with `spotting_chance = 0.15`.
   - In `TUR_canakkale_impenetrable_bastion`: replace `naval_strike_defence_factor = 0.20` with `army_core_defence_factor = 0.10`.
   - In `TUR_ottoman_aviation_detachment`: replace `air_recon_factor = 0.15` with `recon_factor = 0.10`.
   - In `TUR_red_crescent_logistics`: replace `casualty_trickleback = 0.10` with `experience_loss_factor = -0.10` and `attrition = -0.08`.
   - Also in `TUR_arab_unrest_smoldering`: add `stability_factor = -0.12` so it reflects the 5-Pillar starting unrest penalty.

2. **Add 7 Missing Starting & Dynamic Ideas to `common/ideas/ww1_ottoman_ideas.txt`:**
   - `TUR_sick_man_debt`:
     ```txt
     TUR_sick_man_debt = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             consumer_goods_factor = 0.20
             political_power_gain = -0.15
             industrial_capacity_factory = -0.15
             production_speed_buildings_factor = -0.15
         }
     }
     ```
   - `TUR_mehmetcik_tenacity`:
     ```txt
     TUR_mehmetcik_tenacity = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             army_morale_factor = 0.08
             out_of_supply_factor = -0.10
             army_core_defence_factor = 0.05
         }
     }
     ```
   - `TUR_straits_fortress_cannons`:
     ```txt
     TUR_straits_fortress_cannons = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             amphibious_invasion_defence = 0.15
             production_speed_coastal_bunker_factor = 0.15
         }
     }
     ```
   - `TUR_caliphate_global_banner`:
     ```txt
     TUR_caliphate_global_banner = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             war_support_factor = 0.15
             conscription_factor = 0.10
             army_morale_factor = 0.10
         }
     }
     ```
   - `TUR_arab_revolt_insurgency`:
     ```txt
     TUR_arab_revolt_insurgency = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             stability_factor = -0.20
             attrition = 0.12
             supply_consumption_factor = 0.15
             non_core_manpower = -0.25
         }
     }
     ```
   - `TUR_imperial_vilayets_pacified`:
     ```txt
     TUR_imperial_vilayets_pacified = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             stability_factor = 0.10
             non_core_manpower = 0.15
             resistance_target = -0.20
         }
     }
     ```
   - `TUR_senussi_desert_brotherhood`:
     ```txt
     TUR_senussi_desert_brotherhood = {
         allowed = { always = no }
         removal_cost = -1
         modifier = {
             attrition = -0.10
             out_of_supply_factor = -0.15
             army_morale_factor = 0.05
         }
     }
     ```

3. **Register Sprite Definitions in `interface/ww1_ottoman_ideas.gfx`:**
   Add `spriteType` entries for `GFX_idea_TUR_sick_man_debt`, `GFX_idea_TUR_mehmetcik_tenacity`, `GFX_idea_TUR_straits_fortress_cannons`, `GFX_idea_TUR_caliphate_global_banner`, `GFX_idea_TUR_arab_revolt_insurgency`, `GFX_idea_TUR_imperial_vilayets_pacified`, and `GFX_idea_TUR_senussi_desert_brotherhood` pointing to valid existing textures in `gfx/interface/ideas/TUR/` (e.g. `TUR_opda.png`, `TUR_officers_struggle.png`, `TUR_minorities.png`, `TUR_caliphate.png`, etc. — verify the texture file exists on disk!).

4. **Fix `common/characters/TUR.txt` & `history/countries/TUR - Turkey.txt`:**
   - In `common/characters/TUR.txt`:
     - Remove `ideology=nazism` from `TUR_mehmed_v` (use `ideology=despotism` for `TUR_mehmed_v`, and add a `country_leader = { ideology = fascism_ideology expire = "1935.1.1.1" id = -1 }` to `TUR_ismail_enver_pasha` so when CUP takes power as `fascism`, Enver Pasha or the Triumvirate leads!).
     - Ensure `TUR_fakhri_pasha` (`gfx/leaders/TUR/TUR_omer_fahrettin.dds`) and `TUR_halil_kut` (`gfx/leaders/TUR/TUR_halil_kut.dds`) are defined as `corps_commander` in `common/characters/TUR.txt`.
   - In `history/countries/TUR - Turkey.txt`:
     - Uncomment/add `recruit_character = TUR_ismail_enver_pasha`, `recruit_character = TUR_mehmed_esad_pasha`, `recruit_character = TUR_hasan_tahsin_pasha`, `recruit_character = TUR_fakhri_pasha`, and `recruit_character = TUR_halil_kut` right under `# 1911 Country Leaders` (outside the DLC check so they are always recruited!).

## Verification & Commit
1. Run `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/ideas/ww1_ottoman_ideas.txt'); print(errs); assert len(errs) == 0"`
2. Commit:
   `git add common/ideas/ww1_ottoman_ideas.txt interface/ww1_ottoman_ideas.gfx common/characters/TUR.txt "history/countries/TUR - Turkey.txt"`
   `git commit -m "feat(tur): implement 5-pillar Ottoman ideas, fix invalid modifiers, and restore historical commanders"`
3. Write report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\tur-task-2-report.md`.
