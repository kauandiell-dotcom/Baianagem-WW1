# Task 4 Brief: Real Danubian Mega-Federation Engine, Uniform Map Color & Division Spawners

## Objective
Implement the authentic Danubian Mega-Federation map emergence engine triggered by `AUH_ww1_proclaim_danubian_federation`.
The federation releases/puppets `HUN`, `CZE`, `CRO`, and `POL` as autonomous federal states under Vienna's high-centralization hegemony, applies the shared imperial map color (`rgb { 202 198 188 }`) so the empire remains visually cohesive on the map, attaches the high-siphon federal idea (`AUH_danubian_federal_member`), and spawns 4 to 18 divisions per member state via historical OOBs.

## Context
- Working Directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- Spec: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Plan: `docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md`
- Upstream Task: Task 3 (focus `AUH_ww1_proclaim_danubian_federation` calls `AUH_spawn_danubian_mega_federation = yes`)

## Deliverables
1. `common/scripted_effects/ww1_danubian_federation_effects.txt`:
   - Define `AUH_spawn_danubian_mega_federation = { ... }`
   - For `HUN`, `CZE`, `CRO`, `POL`:
     - Transfer core states / release as puppet:
       - `puppet = HUN`, `set_cosmetic_tag = HUN_AUS_danubian_state`, `HUN = { add_ideas = AUH_danubian_federal_member load_oob = "AUH_hun_federal" }`
       - `puppet = CZE`, `set_cosmetic_tag = CZE_AUS_danubian_state`, `CZE = { add_ideas = AUH_danubian_federal_member load_oob = "AUH_cze_federal" }`
       - `puppet = CRO`, `set_cosmetic_tag = CRO_AUS_danubian_state`, `CRO = { add_ideas = AUH_danubian_federal_member load_oob = "AUH_cro_federal" }`
       - `puppet = POL`, `set_cosmetic_tag = POL_AUS_danubian_state`, `POL = { add_ideas = AUH_danubian_federal_member load_oob = "AUH_pol_federal" }`
     - Transfer appropriate state controls:
       - `HUN`: 43, 44, 45, 664, 764
       - `CZE`: 9, 69, 74, 75
       - `CRO`: 109, 108, 163, 164
       - `POL`: 88, 89
     - Ensure each state is at peace with Austria, in Austria's faction if existing, or puppeted directly.
2. `common/countries/cosmetic.txt`:
   - Append cosmetic entries for each member:
     ```clausewitz
     HUN_AUS_danubian_state = {
         color = rgb { 202 198 188 }
         color_ui = rgb { 220 216 206 }
     }
     CZE_AUS_danubian_state = {
         color = rgb { 202 198 188 }
         color_ui = rgb { 220 216 206 }
     }
     CRO_AUS_danubian_state = {
         color = rgb { 202 198 188 }
         color_ui = rgb { 220 216 206 }
     }
     POL_AUS_danubian_state = {
         color = rgb { 202 198 188 }
         color_ui = rgb { 220 216 206 }
     }
     ```
3. OOB Files in `history/units/`:
   - `AUH_hun_federal.txt`: 16 divisions (Magyar Honvéd Infantry & Hussar cavalry).
   - `AUH_cze_federal.txt`: 10 divisions (Bohemian & Moravian infantry and artillery).
   - `AUH_cro_federal.txt`: 6 divisions (Croatian-Slavonian Domobranstvo infantry).
   - `AUH_pol_federal.txt`: 8 divisions (Galician Polish legionary infantry).
   - Each file defines valid division_template (e.g. `division_template = { name = "..." ... }`) and `units = { division = { ... } }` with division counts between 4 and 18.
4. Validation:
   - Run `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_danubian_mega_federation_setup -v`
   - Must PASS!
   - Run bracket balance check across all created/modified files (Diff = 0).
5. Commit:
   - `git add common/scripted_effects/ww1_danubian_federation_effects.txt common/countries/cosmetic.txt history/units/AUH_*_federal.txt`
   - `git commit -m "feat(auh): implement real Danubian Mega-Federation, uniform map colors, and 4-18 division spawns"`
