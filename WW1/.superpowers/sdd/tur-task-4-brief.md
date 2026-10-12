# Ottoman Rework Task 4 Brief: Historical Events Overhaul, Great Arab Revolt & Libyan Resistance (`events/ww1_ottoman_events.txt`)

## Objective
Update `ww1_ottoman.19` and implement `ww1_ottoman.31` (Territorial Eruption of the Great Arab Revolt checking map state security flags `TUR_vilayet_garrison_secured`) and `ww1_ottoman.32` (The Tripolitanian Resistance: Enver Bey & Mustafa Kemal in Libya) in `events/ww1_ottoman_events.txt`.

## Target File
- `events/ww1_ottoman_events.txt`

## Requirements
1. **Update `ww1_ottoman.19` (Eruption of the Arab Revolt in Hejaz):**
   - In `ww1_ottoman.19` Option A (`ww1_ottoman.19.a`), add `country_event = { id = ww1_ottoman.31 days = 5 }`.
2. **Add `ww1_ottoman.31` (Territorial Eruption of the Great Arab Revolt on the Map):**
   - Must have `id = ww1_ottoman.31`, `title = ww1_ottoman.31.t`, `desc = ww1_ottoman.31.d`, `picture = GFX_report_event_report_event_arab_revolt`, `is_triggered_only = yes`.
   - `option = { name = ww1_ottoman.31.a ... }`:
     - For each Arab state (`679`, `856`, `554`, `454`, `291`, `1011`):
       ```txt
       if = {
           limit = { 679 = { is_owned_by = TUR NOT = { has_state_flag = TUR_vilayet_garrison_secured } } }
           679 = { damage_building = { type = infrastructure damage = 2 } }
       }
       ```
       (Repeat for `856`, `554`, `454`, `291`, `1011`).
     - Check whether the Holy Cities / Hejaz (`679` and `856`) were secured:
       ```txt
       if = {
           limit = {
               679 = { has_state_flag = TUR_vilayet_garrison_secured }
               856 = { has_state_flag = TUR_vilayet_garrison_secured }
           }
           if = {
               limit = { has_idea = TUR_arab_unrest_smoldering }
               swap_ideas = {
                   remove_idea = TUR_arab_unrest_smoldering
                   add_idea = TUR_imperial_vilayets_pacified
               }
           }
           add_stability = 0.10
           army_experience = 25
           set_country_flag = TUR_arab_revolt_crushed_by_garrisons
       }
       else = {
           if = {
               limit = { has_idea = TUR_arab_unrest_smoldering }
               swap_ideas = {
                   remove_idea = TUR_arab_unrest_smoldering
                   add_idea = TUR_arab_revolt_insurgency
               }
           }
           else = {
               add_ideas = TUR_arab_revolt_insurgency
           }
           add_manpower = -10000
           add_equipment_to_stockpile = { type = infantry_equipment_1 amount = -500 }
           set_country_flag = TUR_arab_insurgency_active
       }
       ```
3. **Add `ww1_ottoman.32` (The Tripolitanian Resistance: Enver Bey & Mustafa Kemal in Libya):**
   - Must have `id = ww1_ottoman.32`, `title = ww1_ottoman.32.t`, `desc = ww1_ottoman.32.d`, `picture = GFX_report_event_news_army_in_desert`, `is_triggered_only = yes`.
   - Option A (`ww1_ottoman.32.a`):
     - `add_ideas = TUR_senussi_desert_brotherhood`
     - `army_experience = 25`
     - `add_war_support = 0.05`
     - `448 = { if = { limit = { is_owned_by = TUR } add_building_construction = { type = bunker level = 1 instant_build = yes } } }`
     - `450 = { if = { limit = { is_owned_by = TUR } add_building_construction = { type = bunker level = 1 instant_build = yes } } }`
     - `set_country_flag = TUR_enver_kemal_in_libya`
   - Option B (`ww1_ottoman.32.b`):
     - `add_political_power = 50`
     - `add_manpower = 10000`
     - `341 = { if = { limit = { is_owned_by = TUR } add_building_construction = { type = bunker level = 1 instant_build = yes } } }`
     - `set_country_flag = TUR_balkan_priority_over_libya`

## Verification & Commit
1. Run `python -c "from scripts.hoi4_semantic_oracle import audit_file_modifiers; errs = audit_file_modifiers('events/ww1_ottoman_events.txt'); print(errs); assert len(errs) == 0"`
2. Commit:
   `git add events/ww1_ottoman_events.txt`
   `git commit -m "feat(tur): implement territorial Arab Revolt escalation and Libyan resistance events"`
3. Write report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\tur-task-4-report.md`.
