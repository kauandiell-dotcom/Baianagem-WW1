# Task 3 Report: The Great Retreat, Salonika Sanctuary & 28-30 Division Mobilization Engine

## Execution Summary
- **Status:** COMPLETED (All 4 QA suites passing cleanly)
- **Commit:** `91c5e919aae0ec9d80bdbc77afabe11fa9b2e1c4`
- **Commit Message:** `feat(ser): implement Great Retreat sanctuary, 30-division mobilization, and core expansion`

---

## Deliverables & Key Technical Changes

### 1. Ideas (`common/ideas/ww1_serbia_ideas.txt`)
- **`SER_otadzbina_u_pokretu`**:
  - `surrender_limit = 0.40` (pushes capitulation threshold $\ge 95\%$, preventing early capitulation during retreat)
  - `army_core_defence_factor = 0.25`
  - `attrition = -0.15`
  - `out_of_supply_factor = -0.30`
  - `stability_factor = 0.10`
- **`SER_oath_of_corfu_martyrs`**:
  - `war_support_factor = 0.15`
  - `army_org_factor = 0.10`
  - `recruitable_population_factor = 0.10`
- **Modifier Semantic Oracle Fix**:
  - In `SER_yugoslav_brotherhood_charter`: replaced non-existent token `compliance_growth_focus_factor` with valid Clausewitz token `compliance_growth = 0.20`.
  - Zero oracle errors detected across all Serbian national ideas.

### 2. Events (`events/ww1_serbia_retreat_events.txt`)
- Namespace: `ww1_serbia_retreat`.
- **`ww1_serbia_retreat.1`** (*Albanska Golgota - A Grande Retirada através dos Alpes Albaneses*):
  - Trigger: `tag = SER`, `has_war = yes`, `NOT = { controls_state = 107 }`, `NOT = { has_country_flag = ser_executed_great_retreat }`.
  - Grants cores: `184 = { add_core_of = SER }`, `44 = { add_core_of = SER }`.
  - Awards national idea `SER_otadzbina_u_pokretu`.
  - Chains immediately to Salonika Sanctuary (`ww1_serbia_retreat.2`).
- **`ww1_serbia_retreat.2`** (*O Santuário de Salônica - A Frente Aliada dos Balcãs*):
  - Executes `transfer_state = 184` and `184 = { add_core_of = SER }`.
  - Establishes flag `ser_salonika_sanctuary_established`.
  - Schedules narrative events 10, 15, 20, and 25.
- **`ww1_serbia_retreat.10`** (*A Batalha de Mojkovac - A Retaguarda Montenegrina Heroica*):
  - Awards timed defensive spirit `SER_cer_counterstroke_glory` (30 days), army experience, and morale buffs.
- **`ww1_serbia_retreat.15`** (*O Pacto com Essad Pasha Toptani - O Corredor Albanês*):
  - Safe passage through Durrës and Tirana; re-asserts core on state 44, adds opinion with `ALB`.
- **`ww1_serbia_retreat.20`** (*O Cemitério Azul de Vido - Plava Grobnica*):
  - Awards national spirit `SER_oath_of_corfu_martyrs`.
  - Removes `SER_typhus_epidemic_crisis` if active, granting sanitary recovery and manpower replenishment.
- **`ww1_serbia_retreat.25`** (*A Divisão de Voluntários de Odessa*):
  - Grants 25,000 manpower, 5,000 infantry equipment, and army experience from South Slavic Austro-Hungarian POWs.

### 3. Decisions & Categories (`common/decisions/categories/ww1_serbia_decision_categories.txt` & `common/decisions/ww1_serbia_retreat_decisions.txt`)
- Category `ww1_serbia_great_retreat` created with fast-failing `allowed = { original_tag = SER }`.
- Decisions created with fast-failing `allowed = { original_tag = SER }` and `fire_only_once = yes`:
  1. `SER_spawn_conscript_regiments_1896_1899`: 8 Conscript Infantry Divisions (`Pesadijska Divizija III Poziva`) in states 184/44/105/107.
  2. `SER_spawn_yugoslav_volunteer_corps`: 8 Yugoslav Volunteer Divisions (`Jugoslovenska Dobrovoljacka Divizija`) in states 184/44/105/107.
  3. `SER_spawn_french_allied_brigades`: 6 Shock Artillery Divisions (`Udarna Divizija M1897`) equipped with French 75mm guns and equipment.
  4. `SER_spawn_toplica_chetnik_uprising`: 8 Chetnik Irregular Guerilla Divisions (`Cetnicki Odred`) behind enemy lines in occupied states 107 (4 divisions) and 108 (4 divisions).
  - **Total:** 30 divisions spawned across 4 waves.

### 4. AI Automation Hook (`common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`)
- Inside `on_weekly` under `original_tag = SER`:
  ```pdx
  if = {
      limit = {
          has_war = yes
          NOT = { controls_state = 107 }
          NOT = { has_country_flag = ser_executed_great_retreat }
      }
      country_event = { id = ww1_serbia_retreat.1 }
  }
  ```
  - Automatically triggers the Great Retreat and sanctuary establishment for AI Serbia without softlocking or hanging.

---

## Validation Evidence

### Test Suite Results:
```
test_great_retreat_and_sanctuary_mechanics (tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_great_retreat_and_sanctuary_mechanics) ... ok
test_salonika_thirty_divisions_spawns (tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_salonika_thirty_divisions_spawns) ... ok
test_vido_memorial_and_essad_pasha (tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_vido_memorial_and_essad_pasha) ... ok
test_semantic_oracle_modifiers (tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_semantic_oracle_modifiers) ... ok

Ran 4 tests in 0.040s
OK
```

### Bracket Balance Audit:
- `common/ideas/ww1_serbia_ideas.txt`: Open=56, Close=56, Diff=0
- `events/ww1_serbia_retreat_events.txt`: Open=40, Close=40, Diff=0
- `common/decisions/categories/ww1_serbia_decision_categories.txt`: Open=16, Close=16, Diff=0
- `common/decisions/ww1_serbia_retreat_decisions.txt`: Open=119, Close=119, Diff=0
- `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`: Open=47, Close=47, Diff=0

All modified and created Clausewitz `.txt` files exhibit net delta = 0 bracket balance.
