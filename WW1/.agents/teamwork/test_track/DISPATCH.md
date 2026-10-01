## 2026-10-01T02:22:14Z
Your identity: E2E Test Suite Creator (teamwork_preview_test_writer).
Your working directory is: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\test_track

MANDATORY FIRST STEP:
Read C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\ORIGINAL_REQUEST.md before starting any work.

RELEVANT PATHS:
- Master Plan: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\PLANO_FOCUS_TREE_ALEMANHA_WW1.md
- Project Definition: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\PROJECT.md
- Mod Root: C:\Users\Usuário\Pictures\Baianagem-WW1\WW1
- Steam Active Copy Target: C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491

YOUR TASK:
Design and build the comprehensive, automated E2E test suite for the German Empire National Focus Tree mod per the Dual Track principles:
1. Develop Python test scripts in C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\tests\ (e.g. test_runner.py):
   - Tier 1: Syntax & Brace Integrity. Parses all Clausewitz .txt, .gfx, and .yml files. Ensures every '{' has a matching '}', string quotes are closed, and YAML files begin with exact UTF-8 BOM bytes (\xef\xbb\xbf) and proper localization keys (l_english:, l_braz_por:).
   - Tier 2: Boundary & Asset Integrity. Validates that every DDS icon referenced in interface/ww1_germany_goals.gfx exists in gfx/interface/goals/, has valid DDS header/dimensions, and has matching focus icon references.
   - Tier 3: Graph & Mechanical Integrity. Analyzes common/national_focus/germany.txt. Ensures:
     * 0 circular dependencies
     * All prerequisite focus IDs exist in the tree
     * All mutual exclusion focus IDs exist
     * Coordinates (x, y) have 0 collisions
     * All state IDs in focus effects exist in history/states/
     * All idea IDs referenced exist in common/ideas/
     * All event IDs referenced exist in events/
   - Tier 4: End-to-End Consistency & Mirroring Integrity. Verifies that dual localization (EN and PT-BR) covers 100% of focus IDs, idea IDs, and event IDs with zero missing keys, and verifies that the Steam Workshop directory is mirrored accurately.
2. Provide a single runner command: python C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\tests\test_runner.py that executes all tiers and returns exit code 0 on success.
3. Write C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\TEST_INFRA.md and publish C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\TEST_READY.md when ready.
4. Report completion and handoff in C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\test_track\handoff.md.
