# Task 3 Report: Normal Tsarist Russia (1911–1917) Gameplay Mechanics, Shell Shortage & Strategic Depth

**Commit:** `e5773f135668e9c5a802392a8f518826e9335cf1`  
**Status:** Completed successfully  

---

## Deliverables Summary

### 1. Ideas in `common/ideas/ww1_russia_ideas.txt`
Configured the 5 required Tsarist Russia national ideas with verified Clausewitz country modifiers:
- **`SOV_strategic_depth_and_rasputitsa`**:
  - `picture = generic_mountain_artillery`
  - `allowed = { always = yes }`
  - `attrition = 0.20`
  - `winter_attrition_factor = 0.20`
  - `supply_consumption_factor = 0.05`
  - `army_core_defence_factor = 0.10`
- **`SOV_shell_shortage_crisis`**:
  - `picture = generic_production_bonus`
  - `allowed = { always = yes }`
  - `army_artillery_attack_factor = -0.25`
  - `breakthrough_factor = -0.15`
  - `army_attack_factor = -0.10`
  - `army_org_factor = -0.10`
  - `war_support_factor = -0.10`
- **`SOV_vpk_mobilization_spirit`**:
  - `picture = generic_economic_increase`
  - `allowed = { always = yes }`
  - `production_speed_arms_factory_factor = 0.10`
  - `industrial_capacity_factory = 0.05`
- **`SOV_rasputin_court_intrigues`**:
  - `picture = generic_disloyal_officers`
  - `allowed = { always = yes }`
  - `political_power_factor = -0.15`
  - `stability_factor = -0.05`
  - `political_power_cost = 0.20`
- **`SOV_order_restored_spirit`**:
  - `picture = generic_intel_bonus`
  - `allowed = { always = yes }`
  - `stability_factor = 0.10`
  - `war_support_factor = 0.10`
- Also corrected legacy non-standard modifier tokens in `common/ideas/ww1_russia_ideas.txt` (`compliance_growth` and `subjects_autonomy_gain`) to ensure 100% semantic oracle compliance.

### 2. Decision Categories in `common/decisions/categories/ww1_russia_tsarist_categories.txt`
Created category definitions:
- **`SOV_duma_and_court_politics`**:
  - `icon = generic_propaganda`, `picture = GFX_decision_cat_generic`, `priority = 90`, `allowed = { tag = SOV }`
- **`SOV_war_industry_mobilization`**:
  - `icon = generic_industry`, `picture = GFX_decision_cat_generic`, `priority = 80`, `allowed = { tag = SOV }`

### 3. Decisions in `common/decisions/ww1_russia_tsarist_decisions.txt`
Implemented all Pre-Revolutionary Tsarist political, industrial, and military actions:
- **Duma & Court Politics**:
  - `SOV_convene_imperial_duma`: grants PP and stability, cost 25 PP.
  - `SOV_prorogue_the_duma`: removes unrest and boosts stability, cost 50 PP.
  - `SOV_conspiracy_rasputin`: removes `SOV_rasputin_court_intrigues`, available after 1916.1.1, cost 75 PP.
- **War Industry Mobilization**:
  - `SOV_establish_vpk_committees`: adds `SOV_vpk_mobilization_spirit` and cures `SOV_shell_shortage_crisis`, cost 50 PP.
  - `SOV_mobilize_machine_shops`: conversion bonus and builds arms factory in Moscow (state 219), cost 50 PP.
  - `SOV_zemgor_medical_union`: improves casualty trickleback/experience loss, army morale, and war support, cost 40 PP.
  - `SOV_british_shell_presses`: available if allied or friendly with Great Britain, delivers 1,000 artillery equipment to stockpile, cost 50 PP.
  - `SOV_evacuate_industrial_machinery` (`state_target = yes`):
    - Targets vulnerable western frontier states (Warsaw 10, Lodz 87, Lublin 92, Wilejka 96, Bialystok 97, Mazurskie 98, Kaunas 189, Riga 808).
    - Evacuates arms/civilian factories to Moscow (219) or Southern Urals (582), damages local infrastructure.
  - `SOV_prepare_southwestern_offensive`:
    - Brusilov infiltration preparation against Austria-Hungary (AUS), granting breakthrough (+15%), army morale (+10%), and attack (+5%) for 90 days.

---

## Verification & QA

1. **Unit Test**:
   ```bash
   python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_tsarist_mechanics_and_ideas -v
   ```
   *Result:* Ran 1 test in 0.008s — **OK**.

2. **Semantic Oracle Audit**:
   ```bash
   python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; assert len(audit_file_modifiers('common/ideas/ww1_russia_ideas.txt')) == 0; assert len(audit_file_modifiers('common/decisions/ww1_russia_tsarist_decisions.txt')) == 0"
   ```
   *Result:* 0 errors across all idea modifiers and decision modifier blocks.

3. **Bracket Balance Audit**:
   - `common/ideas/ww1_russia_ideas.txt`: Open 243, Close 243 (Difference = 0).
   - `common/decisions/ww1_russia_tsarist_decisions.txt`: Open 83, Close 83 (Difference = 0).
   - `common/decisions/categories/ww1_russia_tsarist_categories.txt`: Open 4, Close 4 (Difference = 0).
