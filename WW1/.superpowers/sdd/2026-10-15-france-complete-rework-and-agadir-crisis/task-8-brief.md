# Task 8 Brief: Master QA Audit, Staging Mirroring & Git Push

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`
Steam Workshop Mirror: `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`

## Deliverables
1. **Full Master QA Suite Execution:**
   - Run `python scripts/qa_audit_all.py`.
   - All 13 suites must pass cleanly (Exit code 0).
   - Verify Clausewitz syntax, bracket balance, BOM integrity, semantic modifier oracle, and all country test suites (Germany, Russia, Austria, France, Britain, Ottoman, Italy).

2. **Mirror Synchronization to Steam Workshop:**
   - Synchronize all files created/modified in this rework to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.
   - Files to sync:
     - `common/decisions/categories/ww1_agadir_crisis_categories.txt`
     - `common/decisions/categories/ww1_france_categories.txt`
     - `common/decisions/ww1_agadir_crisis_decisions.txt`
     - `common/decisions/ww1_france_dashboard_decisions.txt`
     - `common/decisions/ww1_france_decisions.txt`
     - `common/ideas/ww1_france_crises_ideas.txt`
     - `common/ideas/ww1_france_dashboard_ideas.txt`
     - `common/ideas/ww1_france_political_ideas.txt`
     - `common/scripted_effects/ww1_france_dashboard_effects.txt`
     - `common/on_actions/ww1_crisis_on_actions.txt`
     - `common/characters/FRA.txt`
     - `common/national_focus/france.txt`
     - `common/national_focus/germany.txt`
     - `events/WW1_Agadir.txt`
     - `events/ww1_france_events.txt`
     - `localisation/english/ww1_france_rework_l_english.yml`
     - `localisation/braz_por/ww1_france_rework_l_braz_por.yml`
     - `localisation/english/ww1_france_l_english.yml`
     - `localisation/braz_por/ww1_france_l_braz_por.yml`

3. **Git Status & Push:**
   - Verify `git status`.
   - Push commits to `origin main`: `git push origin main`.

4. **Report:**
   - Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-8-report.md`.
5. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
