# Ottoman Rework Task 2 Report: 5-Pillar National Ideas, Semantic Oracle Fixes, GFX & Historical Characters

## Status
**COMPLETED** — Commit `acf804b` (`acf804b68ab6901ad9ea39827c5619992d2664cc`)

## Summary of Changes

### 1. `common/ideas/ww1_ottoman_ideas.txt`
- **Added 7 Starting & Dynamic National Ideas:**
  - `TUR_sick_man_debt` (`consumer_goods_factor = 0.20`, `political_power_gain = -0.15`, `industrial_capacity_factory = -0.15`, `production_speed_buildings_factor = -0.15`)
  - `TUR_mehmetcik_tenacity` (`army_morale_factor = 0.08`, `out_of_supply_factor = -0.10`, `army_core_defence_factor = 0.05`)
  - `TUR_straits_fortress_cannons` (`amphibious_invasion_defence = 0.15`, `production_speed_coastal_bunker_factor = 0.15`)
  - `TUR_caliphate_global_banner` (`war_support_factor = 0.15`, `conscription_factor = 0.10`, `army_morale_factor = 0.10`)
  - `TUR_arab_revolt_insurgency` (`stability_factor = -0.20`, `attrition = 0.12`, `supply_consumption_factor = 0.15`, `non_core_manpower = -0.25`)
  - `TUR_imperial_vilayets_pacified` (`stability_factor = 0.10`, `non_core_manpower = 0.15`, `resistance_target = -0.20`)
  - `TUR_senussi_desert_brotherhood` (`attrition = -0.10`, `out_of_supply_factor = -0.15`, `army_morale_factor = 0.05`)
- **Fixed 5 Invalid Clausewitz Modifiers & Updated Starting Unrest:**
  - `TUR_arab_ottoman_federal_compact`: replaced `compliance_growth_focus_factor = 0.20` with `compliance_gain = 0.03`.
  - `TUR_yavuz_and_midilli_supremacy`: replaced `navy_surface_detection_factor = 0.15` with `spotting_chance = 0.15`.
  - `TUR_canakkale_impenetrable_bastion`: replaced `naval_strike_defence_factor = 0.20` with `army_core_defence_factor = 0.10`.
  - `TUR_ottoman_aviation_detachment`: replaced `air_recon_factor = 0.15` with `recon_factor = 0.10`.
  - `TUR_red_crescent_logistics`: replaced `casualty_trickleback = 0.10` with `experience_loss_factor = -0.10` and `attrition = -0.08`.
  - `TUR_arab_unrest_smoldering`: added `stability_factor = -0.12`.

### 2. `interface/ww1_ottoman_ideas.gfx`
- Registered `SpriteType` entries for all 7 new ideas pointing to verified existing textures in `gfx/interface/ideas/TUR/`:
  - `GFX_idea_TUR_sick_man_debt` -> `gfx/interface/ideas/TUR/TUR_tur_opda.png`
  - `GFX_idea_TUR_mehmetcik_tenacity` -> `gfx/interface/ideas/TUR/TUR_turkic_warrior_tradition.png`
  - `GFX_idea_TUR_straits_fortress_cannons` -> `gfx/interface/ideas/TUR/TUR_homeland_security.png`
  - `GFX_idea_TUR_caliphate_global_banner` -> `gfx/interface/ideas/TUR/TUR_caliphate.png`
  - `GFX_idea_TUR_arab_revolt_insurgency` -> `gfx/interface/ideas/TUR/TUR_arab_minority.png`
  - `GFX_idea_TUR_imperial_vilayets_pacified` -> `gfx/interface/ideas/TUR/TUR_millet_system.png`
  - `GFX_idea_TUR_senussi_desert_brotherhood` -> `gfx/interface/ideas/TUR/tur_sufi_integrated.png`

### 3. `common/characters/TUR.txt` & `history/countries/TUR - Turkey.txt`
- Removed anachronistic `ideology=nazism` country_leader block from `TUR_mehmed_v` (leaving `ideology=despotism`).
- Added `country_leader = { ideology = fascism_ideology expire = "1935.1.1.1" id = -1 }` and civilian portrait to `TUR_ismail_enver_pasha`.
- Added `TUR_fakhri_pasha` (`gfx/leaders/TUR/TUR_omer_fahrettin.dds`) and `TUR_halil_kut` (`gfx/leaders/TUR/TUR_halil_kut.dds`) as `corps_commander` entries in `common/characters/TUR.txt`.
- Recruited `TUR_ismail_enver_pasha`, `TUR_mehmed_esad_pasha`, `TUR_hasan_tahsin_pasha`, `TUR_fakhri_pasha`, and `TUR_halil_kut` directly under `# 1911 Country Leaders` in `history/countries/TUR - Turkey.txt` outside any DLC block.

## Verification
- **Semantic Oracle (`scripts.hoi4_semantic_oracle.audit_file_modifiers`):** `[]` (0 errors on `common/ideas/ww1_ottoman_ideas.txt`).
- **Bracket Balance:** Verified balanced `{` and `}` across all 4 modified files.
- **Asset Verification:** Verified all referenced `.png` and `.dds` textures exist on disk.
