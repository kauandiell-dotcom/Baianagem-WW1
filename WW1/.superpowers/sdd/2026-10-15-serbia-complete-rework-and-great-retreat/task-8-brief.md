# Task 8 Brief: Master QA Audit, Staging Mirroring & Remote Push

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`
Mirror Target: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

## Objectives
1. **Master QA Audit:**
   - Execute `python scripts/qa_audit_all.py`.
   - Verify that all 14 test suites pass with 100% exit code 0 (including the new Suite 14: Kingdom of Serbia Complete Overhaul & The Great Retreat).
   - Verify bracket balance across the whole mod.

2. **Mirror Synchronization:**
   - Synchronize all files created or modified during the Serbian overhaul to the Steam Workshop mirror directory (`E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`).
   - Relevant directories/files:
     * `common/bop/SER_bop.txt`
     * `common/characters/SER.txt`
     * `common/decisions/categories/ww1_serbia_decision_categories.txt`
     * `common/decisions/ww1_serbia_decisions.txt`
     * `common/decisions/ww1_serbia_retreat_decisions.txt`
     * `common/ideas/ww1_serbia_ideas.txt`
     * `common/national_focus/serbia.txt`
     * `common/on_actions/zz_ww1_ger_rus_rework_on_actions.txt`
     * `common/scripted_effects/ww1_serbia_bop_effects.txt`
     * `events/ww1_serbia_events.txt`
     * `events/ww1_serbia_retreat_events.txt`
     * `history/countries/SER - Serbia.txt`
     * `localisation/english/ww1_serbia_l_english.yml`
     * `localisation/braz_por/ww1_serbia_l_braz_por.yml`
   - Use PowerShell copying commands ensuring target directories exist.

3. **Remote Push:**
   - Verify git status is clean.
   - Execute `git push origin main`.

4. **Completion Report:**
   - Output summary of all 8 tasks, git commit hashes, and verification evidence.
