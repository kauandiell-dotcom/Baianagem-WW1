# Task 5 Brief: Tag-Safe Scripted Secession & Crisis Containment Engine

## Objective
Implement Hearts of Iron IV collapse, rebellion, and crisis mechanics for Austria-Hungary that strictly simulate historical and constitutional fragmentation under intolerable war weariness without broken vanilla peace conferences, without dynamic `start_civil_war` D01 clone bugs, and with 100% fail-safe protection against Day 1 fires.

## Context
- Working Directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- Spec: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Plan: `docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md`
- Relevant Skills: `hoi4-events-narrative-engine`, `hoi4-scripted-effects-mechanics`, `hoi4-qa-debug-automation`

## Key Directives (From User & QA Baseline)
1. **NO Day 1 Crises**: All collapse and secession triggers MUST require:
   - `has_war = yes`
   - `date > 1915` (or `date > 1914.12`)
   - `surrender_progress > 0.40` OR loss of core states: `NOT = { controls_state = 4 }` (Vienna), `NOT = { controls_state = 43 }` (Budapest), or `NOT = { controls_state = 88 }` (Galicia)
   - Weariness trigger: `check_variable = { AUH_war_weariness > 70 }`
2. **ZERO Dynamic `start_civil_war` Calls**: Must use fixed historical tags (`CZE`, `HUN`, `CRO`, `POL`).
3. **Anti-Faction Lockdown**: Breakaways must execute `can_join_factions = no`, `prevent_join_factions = yes`, and `leave_faction = yes`.
4. **Scripted Reunification**: Instant re-integration events upon Austria retaking rebel capitals (Prague state 9, Budapest state 43, Zagreb state 109). Cleanly executes `annex_country = { target = <TAG> transfer_troops = yes }`, zero broken peace conferences!
5. **Path-Dependent Secession**:
   - `ww1_austria_collapse.1`: Czech Secession (fires if Austria took Dualism or Military Dictatorship, when Bohemia rises up). Releases `CZE` (states 9, 69), locks factions, declares `civil_war`.
   - `ww1_austria_collapse.2`: Hungarian Secession (fires if Austria took Trialism or Dictatorship and Budapest revolts). Releases `HUN` (states 43, 44, 45), locks factions, declares `civil_war`.
   - `ww1_austria_collapse.3`: South Slav Rebellion (fires if Austria took Dualism or Dictatorship and Zagreb revolts). Releases `CRO` (state 109, 108), locks factions, declares `civil_war`.
   - `ww1_austria_collapse.10`: Imperial Authority Restored (Reunification). Fired when Austria controls the rebel capitals, cleanly annexes them back, restores stability.
6. **Anti-Faction AI Strategy**:
   - Create `common/ai_strategy/ww1_auh_rebel_ai_strategy.txt` for `CZE`, `HUN`, `CRO`, `POL` with `type = join_faction value = -5000` and `type = alliance value = -5000`.

## Verification
- `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_austria_no_day1_crisis -v` -> PASS
- `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_tag_safe_breakaway_rules -v` -> PASS
- Net bracket delta = 0 across all modified and created files.

## Deliverables
1. `events/ww1_austria_collapse_events.txt`
2. `common/ai_strategy/ww1_auh_rebel_ai_strategy.txt`
3. Unit test pass & git commit:
   `git add events/ww1_austria_collapse_events.txt common/ai_strategy/ww1_auh_rebel_ai_strategy.txt`
   `git commit -m "feat(auh): implement tag-safe scripted secession crises and instant imperial reunification engine"`
