# Task 4 Brief: Tag-Safe Russian Civil War Engine (Eliminating Dynamic D01 Clones)

## Objective
Eliminate all 5 instances of `start_civil_war` in `events/ww1_ger_rus_rework_events.txt` that generate procedural tag `D01` ("cor nada a ver, foco igual, sem bandeira") and replace them with the tag-safe historical civil war engine between `SOV` (Lenin, 80 focuses in `soviet_russia.txt`) and `WHT` (Kolchak/Denikin, 60 focuses in `white_russia.txt`).

## Files to Modify
- `events/ww1_ger_rus_rework_events.txt` (Events `ww1_russia.220` and `ww1_russia.255`)
- `common/scripted_effects/ww1_ger_rus_rework_effects.txt` (if any civil war triggers call `start_civil_war`)

## Technical Specifications & Requirements
1. **Purge all `start_civil_war` occurrences**:
   - In `events/ww1_ger_rus_rework_events.txt`:
     - In `ww1_russia.220.a` (lines 699-701):
       Replace:
       ```clausewitz
       if = { limit = { has_government = communism } start_civil_war = { ideology = neutrality size = 0.40 } }
       else_if = { limit = { has_government = fascism } start_civil_war = { ideology = communism size = 0.35 } }
       ```
       With tag-safe invocation:
       ```clausewitz
       if = {
           limit = { has_government = communism }
           WHT = {
               set_country_flag = WHT_russian_civil_war_active
               country_event = { id = ww1_russia_civil_war.1 }
           }
       }
       else = {
           SOV = {
               set_country_flag = SOV_russian_civil_war_active
               country_event = { id = ww1_russia_civil_war.1 }
           }
       }
       ```
     - In `ww1_russia.255.a` (lines 2030-2040):
       Replace:
       ```clausewitz
       if = {
           limit = { has_government = neutrality }
           start_civil_war = { ideology = communism size = 0.45 }
       }
       else_if = {
           limit = { has_government = democratic }
           start_civil_war = { ideology = communism size = 0.45 }
       }
       else = {
           start_civil_war = { ideology = neutrality size = 0.45 }
       }
       ```
       With tag-safe transition referencing both `SOV` and `WHT`:
       ```clausewitz
       SOV = {
           set_country_flag = SOV_russian_civil_war_active
           country_event = { id = ww1_russia_civil_war.1 }
       }
       WHT = {
           set_country_flag = WHT_russian_civil_war_active
       }
       ```
2. **Check for zero `start_civil_war`**:
   - Verify regex `\bstart_civil_war\b` yields 0 matches in `events/ww1_ger_rus_rework_events.txt`.
3. **Verify Bracket Balance**:
   - Braces `{` and `}` must match 100% (Diff = 0).
4. **Automated Unit Test Verification**:
   - Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_tag_safe_russian_civil_war -v`
   - Must PASS with Exit Code 0.

## Deliverables
- Commit: `git add events/ww1_ger_rus_rework_events.txt common/scripted_effects/`
- Commit Message: `fix(rus): replace dynamic D01 civil war clones with tag-safe SOV and WHT historical civil war engine`
- Report: `.superpowers/sdd/2026-10-13-ww1-ai-tactics-russia-civil-war-and-germany-fixes/task-4-report.md`
