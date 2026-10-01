## 2026-10-01T02:12:18Z
Your identity: Focus Tree Spec Miner (teamwork_preview_spec_miner).
Your working directory is: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\spec_miner_focus_tree

MANDATORY FIRST STEP:
Read C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\ORIGINAL_REQUEST.md before starting any work.

SPECIFICATION SOURCE:
Read the master plan: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\PLANO_FOCUS_TREE_ALEMANHA_WW1.md

YOUR TASK:
Exhaustively extract and structure the entire German Empire National Focus Tree specification:
1. Catalog every single focus in the plan across all branches:
   - Branch name / category (Industry, Infrastructure, Army/Reichsheer, Air, Navy/Kaiserliche Marine, Colonies/Weltpolitik, Internal Politics/Constitutional, Diplomacy & Foreign Policy, etc.)
   - Focus ID (e.g. GER_kaiserliche_marine, GER_expand_ruhr_industry, etc.)
   - Coordinates (x, y) relative to tree root or branch anchor
   - Cost / duration in days (e.g. 70 days, 35 days, 56 days, etc.)
   - Prerequisites (prerequisite = { focus = ... })
   - Mutually exclusive relationships (mutually_exclusive = { focus = ... })
   - Available / bypass triggers (available = { ... }, bypass = { ... })
   - Complete gameplay effects (ideas, research bonuses, building construction, equipment bonuses, war goals, event triggers, political power, stability, war support)
2. Verify dependency graph: check for circular dependencies, unreachable focuses, missing connections, or invalid coordinates.
3. List all national ideas / modifiers that must be created or referenced in common/ideas/.
4. List all events or decisions referenced by focuses.
5. Create a complete, structured specification inventory in C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\spec_miner_focus_tree\spec_report.md and produce your handoff in C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\spec_miner_focus_tree\handoff.md.
6. When finished, send a brief message with your handoff path back to your caller.
