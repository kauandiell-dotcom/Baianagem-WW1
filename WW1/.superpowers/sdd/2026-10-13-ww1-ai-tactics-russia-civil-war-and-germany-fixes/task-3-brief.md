# Task 3 Brief: Bulgaria & Minor Belligerents AI Strategy and War Entry Engine

## Goal
Fix the Bulgarian alliance entry so Bulgaria actually enters the war against Serbia and the Entente, and create dedicated AI strategy modules for Bulgaria and Grand War front holding.

## Deliverables
1. Modify `events/ww1_germany_events.txt` (Event `ww1_germany_events.33`):
   - In Option A (`ww1_germany_events.33.a`):
     - Keep adding to faction: `add_to_faction = ROOT`
     - Add explicit war entry against Serbia and Central Powers enemies:
       ```clausewitz
       if = {
           limit = {
               country_exists = SER
               has_war_with = SER
           }
           ROOT = {
               declare_war_on = {
                   target = SER
                   type = annex_everything
               }
           }
       }
       if = {
           limit = {
               has_war = yes
           }
           every_enemy_country = {
               limit = {
                   NOT = { has_war_with = ROOT }
               }
               ROOT = {
                   declare_war_on = {
                       target = PREV
                       type = annex_everything
                   }
               }
           }
       }
       ```
2. Create `common/ai_strategy/ww1_bulgaria_ai_strategy.txt`:
   - AI strategy plan/rules for `BUL`:
     - `alliance id = GER value = 200`
     - `declare_war id = SER value = 200`
     - `declare_war id = ROM value = 150`
     - `front_unit_request` focusing on Serbian and Romanian borders.
     - `antagonize id = SER value = 200`
3. Create `common/ai_strategy/ww1_grand_ai_strategy.txt`:
   - Major power front management rules:
     - `front_control` with balanced commitment.
     - Anti-encirclement defensive priorities.
     - Protect capitals and victory points.

## Verification
- Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_bulgaria_alliance_and_war_call -v`
- Must PASS!
- Clausewitz bracket balance check: 100%.

## Commit
- `git add events/ww1_germany_events.txt common/ai_strategy/`
- `git commit -m "feat(ai,bul): implement direct war entry, alliance call-to-arms, and strategic AI priorities for Bulgaria"`
- Write report to `task-3-report.md`.
