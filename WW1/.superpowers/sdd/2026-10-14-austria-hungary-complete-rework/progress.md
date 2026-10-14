# SDD ledger — plan: docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md

## Pre-Flight Scan

| Tasks | Shared Interface / File | Finding | Ruling |
|-------|-------------------------|---------|--------|
| Task 1 & Task 2 | `tests/test_ww1_austria_hungary.py` / `AUH_war_weariness`, `AUH_cohesion`, `AUH_vienna_grain` | Consistent variable names & bounds (0-100) | Valid |
| Task 1 & Task 3 | `common/national_focus/austria.txt` / 4 constitutional focus ids | Exact focus IDs match (`AUH_ww1_dualism`, `AUH_ww1_trialism`, `AUH_ww1_federalism`, `AUH_ww1_military_dictatorship`) | Valid |
| Task 3 & Task 4 | Focus `AUH_ww1_proclaim_danubian_federation` / `AUH_spawn_danubian_mega_federation` | Clean effect trigger linkage | Valid |
| Task 2 & Task 5 | Simulation variables / Collapse triggers | Thresholds aligned (`AUH_war_weariness > 75`, `AUH_cohesion < 30`) | Valid |
| Task 3 & Task 5 | Constitutional paths / Secession branching | Path-dependent secessions: CZE under Dualism/AOK, HUN under Trialism, Peaceful Congress under Federation | Valid |
| Task 4 & Task 5 | Tags `HUN`, `CZE`, `CRO`, `POL` / `can_join_factions = no` | Rebel tags locked down from foreign alliances; federal states use uniform imperial color | Valid |
| Task 6 & Task 3 | `common/ideas/` / `common/national_focus/austria.txt` | Škoda, Steyr, Ganz, Conrad, Boroević ideas use valid Clausewitz modifiers | Valid |
| Task 7 & Task 3 | Events & decisions / Diplomatic focuses | Redl, Sixtus, Brotfrieden correctly scoped to 1913-1918 | Valid |
| Task 8 & All | Localization keys / English & Brazilian Portuguese | Single UTF-8 BOM (`\xef\xbb\xbf`), 100% key parity | Valid |
| Task 9 & All | Full Mod Validation / Workshop staging folder | All 12 QA suites, bracket check, and semantic oracle pass | Valid |

Pre-flight scan: CLEAN. Proceeding with execution.
Task 1: complete (commits 4438c44..c4a9f18, review clean)
Task 2: complete (commits c4a9f18..c225307, review clean)
Task 3: complete (commits c225307..cc8e624, review clean)
Task 4: complete (commits cc8e624..b646a34, review clean, refined f197f31)
Task 5: complete (commits f197f31..84e6f75, review clean)
Task 6: complete (commits 84e6f75..df906ca, review clean)
Task 7: complete (commits df906ca..03a741a, review clean)
Task 8: complete (commit 4df7d10, review clean)
Task 9: complete (all 12 QA suites PASS, git pushed to origin/main, 56 files mirrored to Steam Workshop)

