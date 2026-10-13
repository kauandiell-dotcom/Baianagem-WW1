# Italy Rework Task 2: 9 Missing National Ideas, 5-Gauge Dynamic Engine & GFX Fixes

**Files:**
- Modify: `common/ideas/ww1_italy_ideas.txt`
- Modify: `common/scripted_effects/ww1_italy_effects.txt`
- Modify: `interface/ww1_italy_ideas.gfx`
- Modify: `interface/ww1_italy_decisions.gfx`

## Step 1: Add the 9 Missing National Ideas & Fix Modifiers in `common/ideas/ww1_italy_ideas.txt`
1. Add the 9 missing ideas inside `ideas = { country = { ... } }`:
   - `ITA_terre_irredente_dream`:
     - `picture = ITA_ww1_idea_1`
     - `modifier = { war_support_factor = 0.05 justify_war_goal_time = -0.15 army_core_attack_factor = 0.05 }`
   - `ITA_alpini_tradition`:
     - `picture = ITA_ww1_idea_2`
     - `modifier = { special_forces_cap = 0.05 acclimatization_cold_climate_gain_factor = 0.15 terrain_penalty_reduction = 0.05 }`
   - `ITA_coal_iron_scarcity`:
     - `picture = ITA_ww1_idea_3`
     - `modifier = { industrial_capacity_factory = -0.10 production_speed_buildings_factor = -0.10 min_export = 0.05 }`
   - `ITA_southern_question_gap`:
     - `picture = ITA_ww1_idea_4`
     - `modifier = { stability_factor = -0.08 production_speed_buildings_factor = -0.08 conscription_factor = -0.10 }`
   - `ITA_sacro_egoismo_policy`:
     - `picture = ITA_ww1_idea_5`
     - `modifier = { political_power_factor = 0.05 improve_relations_maintain_cost_factor = -0.25 send_volunteers_tension = -0.10 }`
   - `ITA_isonzo_attrition_crisis_1`:
     - `picture = ITA_ww1_idea_6`
     - `modifier = { army_morale_factor = -0.05 army_org_factor = -0.05 war_support_factor = -0.03 }`
   - `ITA_isonzo_attrition_crisis_2`:
     - `picture = ITA_ww1_idea_7`
     - `modifier = { army_morale_factor = -0.10 army_org_factor = -0.10 war_support_factor = -0.06 }`
   - `ITA_isonzo_attrition_crisis_3`:
     - `picture = ITA_ww1_idea_8`
     - `modifier = { army_morale_factor = -0.15 army_org_factor = -0.15 war_support_factor = -0.10 }`
   - `ITA_vittorio_veneto_triumph`:
     - `picture = ITA_ww1_idea_9`
     - `modifier = { army_attack_factor = 0.10 army_morale_factor = 0.10 stability_factor = 0.08 war_support_factor = 0.08 }`

2. Fix the 2 documentation-incompatible modifiers in `common/ideas/ww1_italy_ideas.txt`:
   - In `ITA_carbone_bianco_hydro`: replace `production_speed_infrastructure_factor = 0.15` with `production_speed_buildings_factor = 0.08` and `local_resources_factor = 0.05`.
   - In `ITA_energy_independence_spirit`: replace `production_speed_industrial_complex_factor = 0.10` with `production_speed_buildings_factor = 0.10` and `local_resources_factor = 0.10`.
   - In `ITA_mezzogiorno_development_stage`: replace `production_speed_infrastructure_factor = 0.10` with `production_speed_buildings_factor = 0.05`.
   - Also update `picture = ...` on any idea in `ww1_italy_ideas.txt` that uses `generic_...` to use `ITA_ww1_idea_1` through `ITA_ww1_idea_32` so every idea uses a verified local texture in `interface/ww1_italy_ideas.gfx`!

## Step 2: Reactivate the 5-Gauge National Engine in `common/scripted_effects/ww1_italy_effects.txt`
Update `ita_ww1_update_gauges` in `common/scripted_effects/ww1_italy_effects.txt` so that after `ita_ww1_clean_legacy_gauges = yes` and `ita_ww1_clamp_counters = yes`, it evaluates all 5 gauges using `check_variable` and applies the dynamic gauge spirits:
- **Gauge 1 (`ita_ww1_interventionism`):**
  - `if = { limit = { check_variable = { ita_ww1_interventionism < 35 } } add_ideas = ITA_ww1_neutralist_predominance }`
  - `else_if = { limit = { check_variable = { ita_ww1_interventionism < 65 } } add_ideas = ITA_ww1_divided_public_opinion }`
  - `else = { add_ideas = ITA_ww1_radiant_fever }`
- **Gauge 2 (`ita_ww1_social_tension`):**
  - `if = { limit = { check_variable = { ita_ww1_social_tension < 30 } } add_ideas = ITA_ww1_social_truce }`
  - `else_if = { limit = { check_variable = { ita_ww1_social_tension < 65 } } add_ideas = ITA_ww1_labour_friction }`
  - `else = { add_ideas = ITA_ww1_revolutionary_ferment }`
- **Gauge 3 (`ita_ww1_army_morale`):**
  - `if = { limit = { check_variable = { ita_ww1_army_morale < 35 } } add_ideas = ITA_ww1_shattered_discipline }`
  - `else_if = { limit = { check_variable = { ita_ww1_army_morale < 70 } } add_ideas = ITA_ww1_stoic_endurance }`
  - `else = { add_ideas = ITA_ww1_victorious_ardor }`
- **Gauge 4 (`ita_ww1_southern_gap`):**
  - `if = { limit = { check_variable = { ita_ww1_southern_gap < 30 } } add_ideas = ITA_ww1_integrated_mezzogiorno }`
  - `else_if = { limit = { check_variable = { ita_ww1_southern_gap < 65 } } add_ideas = ITA_ww1_southern_disparity }`
  - `else = { add_ideas = ITA_ww1_acute_agrarian_crisis }`
- **Gauge 5 (`ita_ww1_irredentism`):**
  - `if = { limit = { check_variable = { ita_ww1_irredentism < 35 } } add_ideas = ITA_ww1_subdued_claims }`
  - `else_if = { limit = { check_variable = { ita_ww1_irredentism < 70 } } add_ideas = ITA_ww1_unredeemed_lands_call }`
  - `else = { add_ideas = ITA_ww1_irredentist_fervor }`

Also in `ita_ww1_initialise`, call `ita_ww1_update_gauges = yes` at the end so Italy starts with the initial gauge spirits active!

## Step 3: Fix `interface/ww1_italy_decisions.gfx` and `interface/ww1_italy_ideas.gfx`
- In `interface/ww1_italy_decisions.gfx`:
  - Replace all occurrences of `gfx/interface/decisions/decision_category_generic.dds` (which does not exist on disk) with existing `gfx/interface/decisions/ww1_italy/ITA_ww1_decision_1.dds`..`5.dds`.
  - Ensure all `texturefile` paths in `interface/ww1_italy_decisions.gfx` and `interface/ww1_italy_ideas.gfx` exist on disk!

## Verification & Commit
Run:
```bash
python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_italy_ideas.txt')) == 0"
```
Commit:
```bash
git add common/ideas/ww1_italy_ideas.txt common/scripted_effects/ww1_italy_effects.txt interface/ww1_italy_ideas.gfx interface/ww1_italy_decisions.gfx
git commit -m "feat(ita): restore 9 missing national ideas, reactivate 5-gauge engine, and fix GFX sprites"
```
Write your report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\ita-task-2-report.md`.
