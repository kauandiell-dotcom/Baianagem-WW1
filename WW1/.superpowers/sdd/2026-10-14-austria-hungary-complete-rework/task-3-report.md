# Task 3 Report: The 4 Divergent Constitutional Destinies & Focus Tree Overhaul

## Summary
Successfully implemented the 4 divergent constitutional destinies for Austria-Hungary in `common/national_focus/austria.txt` and their authentic national ideas in `common/ideas/ww1_austria_constitutional_ideas.txt`. All 4 paths feature bidirectional mutual exclusivity, zero coordinate collisions (`abs(x2 - x1) >= 2` on all rows), full DAG downward progression (`dy >= 1`), authentic historical sub-focuses, and 0 invalid modifier errors against the HOI4 Semantic Oracle.

---

## Files Implemented / Modified

1. **`common/ideas/ww1_austria_constitutional_ideas.txt`** (Created)
   - `AUH_idea_dualism_iron`: Dualism of Iron spirit (+15% cavalry attack, +10% breakthrough, +10% political power).
   - `AUH_idea_habsburg_trialism`: Habsburg Trialism spirit (+10% stability, +15% army core defense, +10% surrender limit).
   - `AUH_idea_danubian_federation_spirit`: Danubian Mega-Federation spirit (+15% max factory efficiency, -5% consumer goods, +5% research speed).
   - `AUH_idea_aok_military_dictatorship`: Conrad AOK Military Dictatorship spirit (+10% army attack, +15% breakthrough, +15% war support, -15% stability).
   - `AUH_danubian_federal_member`: High-centralization imperial subject spirit (+75% civilian factories to overlord, +75% military factories to overlord, +75% extra trade to overlord, 70% subject manpower share).

2. **`common/national_focus/austria.txt`** (Modified)
   - Restructured the constitutional opening under `AUH_ww1_constitutional_audit` (x = 5, y = 2):
     - **Branch 1 (Dualism of Iron)**:
       - `AUH_ww1_dualism` (x = 2, y = 3, mutually exclusive with Trialism, Federalism, Military Dictatorship; adds `AUH_idea_dualism_iron`).
       - `AUH_ww1_tisza_alliance` (x = 2, y = 4, Magyar alliance, adds +30 grain, +8 consent, +30 PP).
       - `AUH_ww1_magyar_cavalry_corps` (x = 2, y = 5, unlocks Honvéd arms contracts, +15 army XP, +5% war support).
     - **Branch 2 (Habsburg Trialism)**:
       - `AUH_ww1_trialism` (x = 6, y = 3, mutually exclusive with Dualism, Federalism, Military Dictatorship; adds `AUH_idea_habsburg_trialism`).
       - `AUH_ww1_zagreb_coronation` (x = 6, y = 4, Sabor autonomy, infrastructure & dockyards in Dalmatia/Croatia).
       - `AUH_ww1_pacify_south_slavs` (x = 6, y = 5, +5% stability, +10 cohesion, +8 consent).
     - **Branch 3 (Danubian Mega-Federation)**:
       - `AUH_ww1_federalism` (x = 8, y = 3, mutually exclusive with Dualism, Trialism, Military Dictatorship; adds `AUH_idea_danubian_federation_spirit`).
       - `AUH_ww1_popovici_manifesto` (x = 8, y = 4, Popovici United States of Greater Austria constitutional plan).
       - `AUH_ww1_proclaim_danubian_federation` (x = 8, y = 5, calls `AUH_spawn_danubian_mega_federation = yes`, sets federal language reform).
     - **Branch 4 (AOK Military Dictatorship)**:
       - `AUH_ww1_military_dictatorship` (x = 12, y = 3, mutually exclusive with Dualism, Trialism, Federalism; adds `AUH_idea_aok_military_dictatorship`).
       - `AUH_ww1_conrad_supreme_command` (x = 12, y = 4, Conrad von Hötzendorf martial law, +30 CP, +15 army XP, arms factory).
       - `AUH_ww1_war_surveillance_office` (x = 12, y = 5, *Kriegsüberwachungsamt* total industrial mobilization, 2 arms factories).
   - Linked all 4 paths cleanly into the provincial landtags (`AUH_ww1_bohemian_landtag`, `AUH_ww1_galician_autonomy`, `AUH_ww1_slovak_petitions`, `AUH_ww1_dalmatian_services`).

3. **`interface/ww1_austria_hungary_extra_assets.gfx`** (Modified)
   - Registered 9 new goal sprites: `GFX_focus_AUH_ww1_tisza_alliance`, `GFX_focus_AUH_ww1_magyar_cavalry_corps`, `GFX_focus_AUH_ww1_zagreb_coronation`, `GFX_focus_AUH_ww1_pacify_south_slavs`, `GFX_focus_AUH_ww1_popovici_manifesto`, `GFX_focus_AUH_ww1_proclaim_danubian_federation`, `GFX_focus_AUH_ww1_military_dictatorship`, `GFX_focus_AUH_ww1_conrad_supreme_command`, `GFX_focus_AUH_ww1_war_surveillance_office`.

4. **`tests/test_ww1_austria_hungary.py`** (Modified)
   - Step 1 TDD expansion of `test_constitutional_four_paths`: verified presence of all 4 paths, bidirectional mutual exclusivity across all pairs, presence of all 8 sub-focuses, invocation of `AUH_spawn_danubian_mega_federation`, 0 coordinate collisions across all 203 focuses, and 0 semantic modifier errors.

---

## Validation & Verification

1. **Clausewitz Bracket Balance Audit**:
   - `common/national_focus/austria.txt`: opens=1787, closes=1787 (Net Delta = 0)
   - `common/ideas/ww1_austria_constitutional_ideas.txt`: opens=17, closes=17 (Net Delta = 0)
   - `interface/ww1_austria_hungary_extra_assets.gfx`: opens=49, closes=49 (Net Delta = 0)

2. **HOI4 Semantic Modifier Oracle**:
   - Audited `common/ideas/ww1_austria_constitutional_ideas.txt` with `scripts/hoi4_semantic_oracle.py`: 0 errors.

3. **Focus Grid Spatial & DAG Audit**:
   - 203 unique coordinates in tree.
   - 0 coordinate collisions.
   - 0 backward edges (`dy >= 1` universally).
   - Horizontal spacing `abs(x2 - x1) >= 2` on all rows.

4. **Unit Test Suite**:
   - Executed:
     `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_constitutional_four_paths -v`
   - Result: `OK` (1 test passed in 0.029s).

---

## Git Commit
- Commit: `cc8e624`
- Message: `feat(auh): implement 4 divergent constitutional paths and authentic national ideas`
- Files:
  - `common/national_focus/austria.txt`
  - `common/ideas/ww1_austria_constitutional_ideas.txt`
  - `interface/ww1_austria_hungary_extra_assets.gfx`
  - `tests/test_ww1_austria_hungary.py`

## Downstream Interface Notes (Task 4)
- `AUH_ww1_proclaim_danubian_federation` is wired to call `AUH_spawn_danubian_mega_federation = yes`.
- `AUH_danubian_federal_member` idea is defined in `common/ideas/ww1_austria_constitutional_ideas.txt` with validated modifiers (`cic_to_overlord_factor = 0.75`, `mic_to_overlord_factor = 0.75`, `extra_trade_to_overlord_factor = 0.75`, `autonomy_manpower_share = 0.70`).
- Ready for Task 4 to implement `common/scripted_effects/ww1_danubian_federation_effects.txt`, cosmetic tags, and federal OOB units.
