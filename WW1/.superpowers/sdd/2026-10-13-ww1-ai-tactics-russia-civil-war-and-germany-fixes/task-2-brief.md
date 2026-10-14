# Task 2 Brief: Player-Grade WW1 Combat & Army Management AI Defines

## Goal
Implement `common/defines/ww1_ai_defines.lua` to transform HOI4 AI from suicidal battle plan grinding into a disciplined, player-grade tactical engine:
1. High Planning Requirement:
   - `NDefines.NAI.MIN_PLANNING_BONUS_TO_ATTACK = 0.65` (forces AI to accumulate 65%+ planning bonus before executing major pushes).
2. Attack Cancellation & Anti-Attrition:
   - `NDefines.NAI.PLAN_ATTACK_MIN_EFFICIENCY_TO_CANCEL = 0.60` (cancels attacks when efficiency drops below 60%, preventing meat-grinder losses).
   - `NDefines.NAI.PLAN_ATTACK_MAX_FRICTION = 0.25` (halts attacks into muddy/fortified stalemates).
3. Organization & Strength Preservation:
   - `NDefines.NAI.ORG_UNIT_WEAK = 0.45` (forces AI to stop attacking and defend when organization drops below 45%).
   - `NDefines.NAI.STRENGTH_UNIT_WEAK = 0.60` (conserves divisions below 60% equipment/strength).
   - `NDefines.NAI.ENTRENCHMENT_FACTOR_ATTACK = 2.0` (penalizes attacking heavily entrenched lines without massive preparation).
4. Division Stacking & Frontline Management:
   - `NDefines.NAI.MAX_NUM_DIVISIONS_TO_ATTACK_PER_PROVINCE = 6` (prevents overcrowding and severe stacking penalties).
   - `NDefines.NAI.FRONT_LINE_CONSERVATIVE = 0.40` (maintains solid unbroken lines to prevent easy encirclements).
5. Army Group Consolidation (Human Player Style):
   - `NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 24` (standardizes 24-division armies like human players, eliminating 1-division micro-generals).
   - `NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 5` (standardizes 5 armies per army group).
   - `NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 24`

## Verification
- Run: `python -m unittest tests.test_ww1_ai_and_russia_fixes.TestAIAndRussiaFixes.test_ai_tactical_defines -v`
- Must PASS!
- Lua syntax check: ensure valid Lua without syntax errors.

## Commit
- `git add common/defines/ww1_ai_defines.lua`
- `git commit -m "feat(ai): implement player-grade WW1 combat, org conservation, and army management defines"`
- Write report to `task-2-report.md`.
