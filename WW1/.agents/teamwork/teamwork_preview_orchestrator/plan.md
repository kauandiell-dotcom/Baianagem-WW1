# Master Plan: German Empire National Focus Tree (WW1)

## Overview
Implement the complete German Empire (GER) focus tree for Hearts of Iron IV WW1 mod according to PLANO_FOCUS_TREE_ALEMANHA_WW1.md and ORIGINAL_REQUEST.md.

## Phased Execution Strategy
1. **Survey (Phase 0)**:
   - Explorer 1 (Spec Miner): Extract all focus IDs, prereqs, mutually exclusive sets, positions (x,y), costs, effects from PLANO_FOCUS_TREE_ALEMANHA_WW1.md.
   - Explorer 2 (Icon & Assets Specialist): Inspect source icon library `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3106240385\gfx\interface\goals` and existing mod `gfx/interface/goals` to map every focus to a matching DDS icon.
   - Explorer 3 (Codebase & Integration Specialist): Inspect existing mod root `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`, check `common/national_focus/germany.txt`, check existing events, ideas, decisions, localisation to identify dependencies, conflicts, and state/country IDs.

2. **Synthesis & Project Baseline (PROJECT.md)**:
   - Synthesize feature inventory and milestone scopes.
   - Set up interface contracts and code layouts.

3. **Milestone Executions (Iteration Loops)**:
   - Worker implements.
   - Reviewers inspect logic, syntax, completeness.
   - Challenger runs brace checking scripts & static tests.
   - Auditor verifies authenticity & absence of placeholders/stubs.

4. **Final Integration & Mirroring**:
   - Verify 100% brace integrity and UTF-8 BOM encoding on localisation files.
   - Robocopy sync to Steam Workshop target `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.
   - Report completion to Sentinel.
