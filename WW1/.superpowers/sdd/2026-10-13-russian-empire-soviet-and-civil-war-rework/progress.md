# SDD ledger — plan: docs/superpowers/plans/2026-10-13-russian-empire-soviet-and-civil-war-rework.md

## Pre-flight Plan Scan
| Tasks | Produces vs Consumes | Findings & Rulings |
| :--- | :--- | :--- |
| Task 1 vs Task 2-11 | QA Test Suite assertions vs Implementation deliverables | Clean: Task 1 asserts full spec requirements; subsequent tasks satisfy them in order. |
| Task 2 vs Task 5, 8 | Tag `WHT` & characters vs Civil war spawning & White tree | Clean: Tag `WHT` and characters created in Task 2 before Task 5 spawns them and Task 8 gives them focuses. |
| Task 3, 4 vs Task 5 | Tsarist mechanics & Crisis Engine vs Civil War | Clean: Tsarist 1911-1917 and crisis engine fully set up before civil war event trigger. |
| Task 6 vs Task 7 | Brest-Litovsk mechanics vs Soviet focus tree Wing 4 | Clean: Diplomacy effects decoupled via events/decisions before focus integration. |
| Task 7, 8 vs Task 9 | New Soviet/White trees vs Tsarist tree refactoring | Clean: New trees created before legacy stubs are purged in Task 9. |
| Task 10 vs Task 1-9 | Localization vs All new content | Clean: All keys for focuses, ideas, decisions, events mapped with single UTF-8 BOM. |
| Task 11 vs Task 1-10 | Master QA integration vs Entire overhaul | Clean: Master audit updated and verified with Exit Code 0. |

Scan clean. Rulings: none needed. Starting Task 1.

## Task 1: QA Test Suite Baseline Expansion (`tests/test_ww1_russia_rework.py` — RED Phase)
- Status: COMPLETED & APPROVED
- Implementer Commit: `d403c6e` (`test(sov): create master QA test suite baseline for Russia overhaul (RED)`)
- Reviewer Verdict: ACCEPTED (`70b72704-b613-448c-ab72-d0d3ded28c40`)
- Follow-up Tightening Commit: `a19e07a` (`test(sov): tighten reviewer assertions on on-actions and Tsarist focus rewards`)
- Result: 9/9 tests failing cleanly on unbuilt entities (RED Phase established).
- Report: `task-1-report.md`

## Task 2: Country Tag WHT, Historical Characters, Cosmetic Tags & GFX Sprites
- Status: COMPLETED & APPROVED
- Implementer Commit: `d9300e0` (`feat(sov): establish WHT country tag, historical character cast, and focus GFX sprites`)
- Reviewer Verdict: APPROVED (`d01360d3-a8ad-444e-9a1e-b4fcb8cd1069`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_characters_and_tags -v` passed (OK, 0.021s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-2-report.md`
## Task 3: Normal Tsarist Russia (1911–1917) Gameplay Mechanics, Shell Shortage & Strategic Depth
- Status: COMPLETED & APPROVED
- Implementer Commit: `e5773f1` (`feat(sov): implement Tsarist 1911-1917 mechanics, shell shortage, and strategic depth`)
- Reviewer Verdict: APPROVED (`bbf47fcb-26bb-4c14-bce5-eb67f341a789`)
- Polish Commit: `44adace` (`feat(sov): polish Tsarist decision visibility, multi-stage cleanup, and Brusilov one-time flag`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_tsarist_mechanics_and_ideas -v` passed (OK, 0.005s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-3-report.md`## Task 4: Pre-Revolutionary Crisis Engine & Visual Decisions Dashboard (Late 1915 – Mid 1917)
- Status: COMPLETED & APPROVED
- Implementer Commit: `73587c4` (`feat(sov): implement real-time revolutionary crisis dashboard, visual progress bars, and dual catalyst`)
- Reviewer Verdict: APPROVED (`b8b684bd-2802-49fa-aec4-b1ea6b7e9029`)
- Polish Commit: `3e6758c` (`feat(sov): polish crisis lifecycle guards and resolution cleanup`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_crisis_engine_and_gauges -v` passed (OK, 0.035s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-4-report.md`## Task 5: Multi-Front Russian Civil War Engine & Breakaway Powderkeg
- Status: COMPLETED & APPROVED
- Implementer Commit: `8b9bc64` (`feat(sov): implement multi-front Russian Civil War engine, breakaway nations, and combat OOBs`)
- Reviewer Verdict: APPROVED (`937fee24-b98c-43e1-94ae-debffb44af0f`)
- Polish Commit: `d9660b4` (`feat(sov): polish civil war Caucasus state allocation, WHT stockpile grant, and AI choices`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_civil_war_spawns_and_oobs -v` passed (OK, 0.016s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-5-report.md`## Task 6: Central Powers Interaction, Brest-Litovsk & Entente Proxy Aid
- Status: COMPLETED & APPROVED
- Implementer Commit: `c393fd2` (`feat(sov): implement Treaty of Brest-Litovsk, Entente proxy intervention, and armistice dissolution`)
- Reviewer Verdict: APPROVED (`99be0a87-fb3c-423e-a341-4b95e6042f6d`)
- Polish Commit: `e415259` (`feat(sov): polish diplomacy idea icon and remove duplicate PP grant`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_brest_litovsk_and_diplomacy -v` passed (OK, 0.004s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-6-report.md`

## Task 7: Dedicated Soviet Russia Focus Tree (`common/national_focus/soviet_russia.txt` — 80 Focuses)
- Status: COMPLETED & APPROVED
- Implementer Commit: `45c656b` (`feat(sov): implement dedicated 80-focus Soviet Russia national focus tree`)
- Reviewer Verdict: APPROVED (`006de1a1-3bc7-452f-bd21-39e803316813`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_soviet_focus_tree_integrity -v` passed (OK, 0.054s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-7-report.md`



## Task 8: Dedicated White Movement Focus Tree (common/national_focus/white_russia.txt — 60 Focuses)
- Status: COMPLETED & APPROVED
- Implementer Commit: 629b48d (eat(wht): implement dedicated 60-focus White Movement national focus tree)
- Reviewer Verdict: APPROVED (281f919-9a4a-49e3-ad37-5782f16ea1a9)
- Verification: python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_white_focus_tree_integrity -v passed (OK, 0.042s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: 	ask-8-report.md

## Task 9: Tsarist Focus Tree Refactoring & Polish (`common/national_focus/soviet.txt`)
- Status: COMPLETED
- Implementer Commit: `45ea2fb` (`refactor(sov): purge legacy stubs, enrich hollow focuses, and add Imperial Salvation capstones`)
- Verification: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_imperial_focus_tree_integrity -v` passed (OK, 0.032s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal BOMs
- Report: `task-9-report.md`

## Task 9: Tsarist Focus Tree Refactoring & Polish (common/national_focus/soviet.txt)
- Status: COMPLETED & APPROVED
- Implementer Commit: 45ea2fb (
efactor(sov): purge legacy stubs, enrich hollow focuses, and add Imperial Salvation capstones)
- Reviewer Verdict: CHANGES REQUESTED -> FIXED (76ad683a-ffe5-42bb-96ea-f5a6871eb574)
- Polish Commit: b854e0 (eat(sov): polish Task 9 review feedback, strip script BOMs, ensure unique icon and sync legacy tests)
- Verification: python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_imperial_focus_tree_integrity -v passed (OK, 0.032s)
- Semantic Oracle: 0 modifier errors
- Braces & BOM: 100% balanced braces, 0 illegal script BOMs
- Report: 	ask-9-report.md

## Task 10: Complete Bilingual Localization & Single UTF-8 BOM
- Status: COMPLETED & APPROVED
- Implementer Commit: e1a7cd7 (eat(loc): provide complete bilingual localization with single UTF-8 BOM for Russia overhaul)
- Reviewer Verdict: APPROVED (9c52ab2f-ab17-453a-bea1-ff63a200870e)
- Verification: python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_localisation_integrity_and_bom -v passed (OK, 0.057s)
- Key Parity: 100% key parity across all 5 file pairs (symmetric difference = 0)
- Single UTF-8 BOM: 113/113 YAML files verified with strictly single UTF-8 BOM (0 double-BOMs)
- Report: 	ask-10-report.md

## Task 11: Master QA Integration & Full Test Pass
- Status: COMPLETED & APPROVED
- Implementer Commit: 5069dd5 (ci(qa): integrate Russia overhaul test suite into master QA audit runner)
- Reviewer Verdict: APPROVED (e1aedaf-ce64-4f40-b0df-29c98215ccf3)
- Master Audit Execution: python scripts/qa_audit_all.py passed with Exit Code 0 (8/8 test suites, 90 automated unit tests, 0 issues across all static audits).

## Overhaul Completion Summary
All 11 tasks of the Russian Empire, Revolution, Soviet & White Civil War Overhaul have been implemented, verified, reviewed, and approved via Subagent-Driven Development (SDD) with zero open defects.
