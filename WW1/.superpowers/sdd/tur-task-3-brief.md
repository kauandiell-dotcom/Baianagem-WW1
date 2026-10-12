# Ottoman Rework Task 3 Brief: Map-Based Arab Vilayet Security Engine & Dynamic OPDA Debt Decisions

## Objective
Fix the invalid modifier in `common/decisions/ww1_ottoman_decisions.txt`, implement the Map-Based Arab Vilayet Security Engine (`state_target = yes` for states `679, 856, 554, 454, 291, 1011`), and implement active variable-driven OPDA Debt & Foreign Influence decisions plus the Libyan officer dispatch decision.

## Target Files
- `common/decisions/ww1_ottoman_decisions.txt`
- `common/decisions/categories/ww1_ottoman_decision_categories.txt`

## Requirements
1. **Fix Invalid Clausewitz Modifier in `common/decisions/ww1_ottoman_decisions.txt`:**
   - In `TUR_deploy_gendarmerie_sweep`: replace `compliance_growth_focus_factor = 0.10` with `compliance_gain = 0.02`.

2. **Add Map-Based Arab Vilayet Security Decisions (`state_target = yes`) in `TUR_imperial_cohesion_category`:**
   - `TUR_deploy_hejaz_armored_garrison`:
     ```txt
     TUR_deploy_hejaz_armored_garrison = {
         icon = GFX_decision_generic_military
         state_target = yes
         target_array = owned_states
         target_trigger = {
             FROM = {
                 is_owned_by = ROOT
                 OR = {
                     state = 679
                     state = 856
                     state = 554
                     state = 454
                     state = 291
                     state = 1011
                 }
                 NOT = { has_state_flag = TUR_vilayet_garrison_secured }
             }
         }
         visible = {
             tag = TUR
         }
         available = {
             NOT = { has_country_flag = TUR_securing_arab_vilayet_in_progress }
             has_manpower > 15000
             has_equipment = { type = infantry_equipment_1 amount > 400 }
         }
         cost = 30
         days_remove = 50
         complete_effect = {
             set_country_flag = TUR_securing_arab_vilayet_in_progress
             add_manpower = -15000
             add_equipment_to_stockpile = { type = infantry_equipment_1 amount = -400 }
         }
         remove_effect = {
             clr_country_flag = TUR_securing_arab_vilayet_in_progress
             FROM = {
                 set_state_flag = TUR_vilayet_garrison_secured
             }
             add_to_variable = { tur_arab_unrest = -10 }
             add_to_variable = { tur_imperial_cohesion = 5 }
         }
         ai_will_do = {
             factor = 2.0
         }
     }
     ```
   - `TUR_teskilat_counter_insurgency_sweep`:
     ```txt
     TUR_teskilat_counter_insurgency_sweep = {
         icon = GFX_decision_generic_police_action
         state_target = yes
         target_array = owned_states
         target_trigger = {
             FROM = {
                 is_owned_by = ROOT
                 OR = {
                     state = 679
                     state = 856
                     state = 554
                     state = 454
                     state = 291
                     state = 1011
                 }
             }
         }
         visible = {
             tag = TUR
         }
         available = {
             command_power > 10
             check_variable = { tur_arab_unrest > 10 }
         }
         cost = 25
         days_re_enable = 90
         complete_effect = {
             add_command_power = -10
             add_to_variable = { tur_arab_unrest = -8 }
             add_to_variable = { tur_imperial_cohesion = 3 }
         }
         ai_will_do = {
             factor = 1.5
         }
     }
     ```
   - `TUR_subsidize_bedouin_sheikhs`:
     ```txt
     TUR_subsidize_bedouin_sheikhs = {
         icon = GFX_decision_generic_political_discourse
         state_target = yes
         target_array = owned_states
         target_trigger = {
             FROM = {
                 is_owned_by = ROOT
                 OR = {
                     state = 679
                     state = 856
                     state = 554
                     state = 454
                     state = 291
                     state = 1011
                 }
                 NOT = { has_state_flag = TUR_vilayet_tribes_subsidized }
             }
         }
         visible = {
             tag = TUR
         }
         available = {
             num_of_civilian_factories_available_for_projects > 0
         }
         cost = 25
         days_remove = 60
         civilian_factory_use = 1
         complete_effect = {
             FROM = {
                 set_state_flag = TUR_vilayet_tribes_subsidized
             }
             add_to_variable = { tur_arab_unrest = -8 }
         }
         remove_effect = {
             add_stability = 0.03
             add_to_variable = { tur_imperial_cohesion = 5 }
         }
         ai_will_do = {
             factor = 1.5
         }
     }
     ```
   - `TUR_pacify_arab_insurgency_campaign`:
     ```txt
     TUR_pacify_arab_insurgency_campaign = {
         icon = GFX_decision_generic_military_operation
         visible = {
             has_idea = TUR_arab_revolt_insurgency
         }
         available = {
             has_idea = TUR_arab_revolt_insurgency
             679 = { has_state_flag = TUR_vilayet_garrison_secured }
             554 = { has_state_flag = TUR_vilayet_garrison_secured }
         }
         cost = 50
         fire_only_once = yes
         complete_effect = {
             swap_ideas = {
                 remove_idea = TUR_arab_revolt_insurgency
                 add_idea = TUR_imperial_vilayets_pacified
             }
             add_stability = 0.10
             add_war_support = 0.05
             set_variable = { tur_arab_unrest = 10 }
         }
         ai_will_do = {
             factor = 5.0
         }
     }
     ```

3. **Add Active OPDA Debt & Foreign Influence Decisions in `TUR_debt_and_capitulations_category`:**
   - `TUR_liquidate_opda_debt_tranche`:
     ```txt
     TUR_liquidate_opda_debt_tranche = {
         icon = GFX_decision_generic_economy
         visible = {
             tag = TUR
             check_variable = { tur_public_debt > 0 }
         }
         available = {
             check_variable = { tur_public_debt > 15 }
         }
         cost = 45
         days_re_enable = 120
         complete_effect = {
             add_to_variable = { tur_public_debt = -15 }
             add_to_variable = { tur_foreign_influence = -10 }
             add_stability = 0.03
             if = {
                 limit = {
                     check_variable = { tur_public_debt < 45 }
                     has_idea = TUR_sick_man_debt
                 }
                 swap_ideas = {
                     remove_idea = TUR_sick_man_debt
                     add_idea = TUR_debt_renegotiated
                 }
             }
         }
         ai_will_do = {
             factor = 2.0
         }
     }
     ```
   - `TUR_curb_foreign_consular_courts`:
     ```txt
     TUR_curb_foreign_consular_courts = {
         icon = GFX_decision_generic_trade
         visible = {
             tag = TUR
             check_variable = { tur_foreign_influence > 0 }
         }
         available = {
             check_variable = { tur_foreign_influence > 15 }
         }
         cost = 35
         days_re_enable = 120
         complete_effect = {
             add_to_variable = { tur_foreign_influence = -15 }
             add_to_variable = { tur_imperial_cohesion = 5 }
             add_political_power = 50
             add_stability = 0.04
         }
         ai_will_do = {
             factor = 1.5
         }
     }
     ```

4. **Add Libyan Resistance Decision in `TUR_war_theaters_category`:**
   - `TUR_dispatch_officers_to_tripolitania`:
     ```txt
     TUR_dispatch_officers_to_tripolitania = {
         icon = GFX_decision_generic_military_operation
         visible = {
             tag = TUR
             NOT = { has_country_flag = TUR_libyan_mission_sent }
         }
         available = {
             OR = {
                 448 = { is_owned_by = TUR }
                 450 = { is_owned_by = TUR }
                 has_war_with = ITA
             }
         }
         cost = 25
         fire_only_once = yes
         complete_effect = {
             set_country_flag = TUR_libyan_mission_sent
             country_event = { id = ww1_ottoman.32 }
         }
         ai_will_do = {
             factor = 5.0
         }
     }
     ```

## Verification & Commit
1. Run `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('common/decisions/ww1_ottoman_decisions.txt'); print(errs); assert len(errs) == 0"`
2. Commit:
   `git add common/decisions/ww1_ottoman_decisions.txt common/decisions/categories/ww1_ottoman_decision_categories.txt`
   `git commit -m "feat(tur): implement map-based Arab vilayet security engine and active OPDA debt decisions"`
3. Write report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\tur-task-3-report.md`.
