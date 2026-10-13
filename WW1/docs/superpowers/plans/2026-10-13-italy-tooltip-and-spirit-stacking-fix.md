# Italy (ITA) Decision Tooltip Clutter & National Spirit Stacking Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate the giant wall of `remove_ideas` in Italian decision tooltips, replace all 32 advisor-scroll idea icons with authentic Italian national spirit art, and prevent topbar spirit stacking through progressive idea swapping and tangible focus rewards.

**Architecture:** 
1. Scripted effects (`ita_ww1_update_gauges` and `ita_ww1_clean_legacy_gauges`) are enclosed in `hidden_effect = { ... }` so internal gauge recalculations execute silently without generating 20+ line tooltip clutter in decisions.
2. The 32 harvested idea textures (`ITA_ww1_idea_1.dds` to `32.dds`) are rebuilt using genuine Italian national spirit artwork (Arditi, Risorgimento, Questione Meridionale, Cantieri Navali, Ansaldo, Montecatini, etc.) from mod donor repositories without any minister scroll overlays.
3. The military, naval, and air focus trees in `common/national_focus/italy.txt` adopt progressive idea swapping (Pillar structure) and tangible rewards (equipment, dockyards, forts, XP, tech bonuses), preventing 20+ simultaneous spirits from stacking across multiple rows in the political view.

**Tech Stack:** Paradox Clausewitz Engine (HOI4 script), Python 3.11, PIL / Pillow, Microsoft `texconv.exe`, unittest.

**Spec:** User feedback on 16-spirit stacking ("EMPILhando (print 1)") and gigantic decision removal tooltips ("tem umas decisões da italia, que ta empilhando um monte de remove e os caramba, ta gigante essas decisões na descrições e tals dela").

## Global Constraints
- All 16 unit tests in `tests/test_ww1_italy.py` must pass.
- All 6 test suites in `scripts/qa_audit_all.py` must exit 0 with 0 errors.
- Both localization files (`ww1_italy_l_english.yml` and `ww1_italy_l_braz_por.yml`) must maintain mandatory single UTF-8 BOM (`\xef\xbb\xbf`).
- National spirits must never stack beyond 1 clean row (~5 to 7 spirits max).
- Decision tooltips must never expose raw internal gauge cleanup or raw `remove_ideas` blocks.

## Review Focus
1. `ita_ww1_update_gauges` hidden effect scoping must not break `check_variable` evaluation or variable clamping.
2. Focus tree rewards must not exceed balance ceilings (`total_pos_stab <= 0.15`, `total_pos_ws <= 0.20`, no free divisions).
3. Idea sprite definitions must point to valid 64x64 DDS textures with valid alpha channels.
4. Focus prerequisite DAG integrity (`1 <= dy <= 3`) and horizontal grid spacing (`dx >= 2`) must remain strictly intact.
5. All references in `events/`, `common/national_focus/`, `common/decisions/`, and `tests/` must remain valid and synchronized.

---

### Task 1: Clean Decision Tooltips & Hidden Gauge Calculations

**Files:**
- Modify: `common/scripted_effects/ww1_italy_effects.txt`
- Modify: `common/decisions/ww1_italy_decisions.txt`
- Test: `tests/test_ww1_italy.py`

- [ ] **Step 1: Write test asserting zero raw `remove_ideas` exposed in decision tooltips**
Add a test in `tests/test_ww1_italy.py` checking that `ita_ww1_clean_legacy_gauges` and `ita_ww1_update_gauges` are wrapped in `hidden_effect` and that `ITA_ww1_launch_isonzo_general_offensive` uses `hidden_effect` for crisis idea swaps.

- [ ] **Step 2: Run test to verify it fails**
Run: `python -m unittest tests.test_ww1_italy.TestItalyEventsAndDecisions -v`

- [ ] **Step 3: Enclose gauge cleanup and updates in `hidden_effect`**
In `common/scripted_effects/ww1_italy_effects.txt`:
Wrap the body of `ita_ww1_clean_legacy_gauges` and the idea manipulation of `ita_ww1_update_gauges` inside `hidden_effect = { ... }`.
In `common/decisions/ww1_italy_decisions.txt`:
Wrap the `remove_ideas = ITA_isonzo_attrition_crisis_*` in `ITA_ww1_launch_isonzo_general_offensive` inside `hidden_effect = { ... }` with a clean `custom_effect_tooltip`.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_italy.TestItalyEventsAndDecisions -v`

- [ ] **Step 5: Commit**
```bash
git add common/scripted_effects/ww1_italy_effects.txt common/decisions/ww1_italy_decisions.txt tests/test_ww1_italy.py
git commit -m "fix(ita): enclose internal gauge updates and idea cleanup in hidden_effect to eliminate decision tooltip clutter"
```

---

### Task 2: Authentic Italian National Spirit Art Pipeline (Zero Minister Scrolls)

**Files:**
- Modify: `gfx/interface/ideas/ww1_italy/ITA_ww1_idea_1.dds` through `32.dds`
- Modify: `interface/ww1_italy_ideas.gfx`
- Modify: `docs/ita_art_bindings.json`
- Test: `tests/test_ww1_italy.py`

- [ ] **Step 1: Select 32 genuine Italian period icons without advisor scrolls**
Harvest authentic WW1 Italian icons from TGWR / Kaiserredux / Europe In Flames:
`ITA_arditi.png`, `ITA_questione_meridionale.png`, `ITA_risorgimento.png`, `cantieri_navali_riuniti.png`, `idea_ansaldo.png`, `idea_societa_montecatini.png`, `idea_universita_torino.png`, `ITA_battle_land.png`, `ITA_death_before_surrender.png`, `ITA_emanuele_iii_idea.png`, `ITA_emigrazione_italiana.png`, `ITA_fruits_of_the_reforms.png`, `ITA_corporatism.png`, `camicie_nere_idea.png`, etc., plus authentic WW1 army, navy, and air insignias.

- [ ] **Step 2: Generate clean 64x64 DDS textures using `texconv.exe` or PIL**
Convert all 32 textures with DXT5 compression, proper mipmaps, and no minister scroll artifacts.

- [ ] **Step 3: Update `docs/ita_art_bindings.json` and verify `interface/ww1_italy_ideas.gfx`**
Record the new clean sources in `docs/ita_art_bindings.json`. Verify that all 32 spriteTypes in `interface/ww1_italy_ideas.gfx` resolve to valid files on disk.

- [ ] **Step 4: Run tests**
Run: `python -m unittest tests.test_ww1_italy.TestItalyLocalisationAndGraphics.test_gfx_sprite_definitions_and_shine -v`

- [ ] **Step 5: Commit**
```bash
git add gfx/interface/ideas/ww1_italy/ interface/ww1_italy_ideas.gfx docs/ita_art_bindings.json
git commit -m "fix(ita): replace advisor portrait textures with authentic WW1 Italian national spirit icons"
```

---

### Task 3: Focus Tree & National Spirits Anti-Stacking Architecture

**Files:**
- Modify: `common/national_focus/italy.txt`
- Modify: `common/ideas/ww1_italy_ideas.txt`
- Test: `tests/test_ww1_italy.py`

- [ ] **Step 1: Write anti-stacking test**
Add test in `tests/test_ww1_italy.py` verifying that:
1. Army doctrine wing swaps progressive ideas (`ITA_ww1_general_staff_corps` -> `ITA_ww1_cadorna_discipline` -> `ITA_ww1_diaz_humane_leadership` -> `ITA_ww1_badoglio_standing_army`).
2. Naval wing swaps doctrine ideas (`ITA_ww1_regia_marina_cadres` -> `ITA_ww1_dreadnought_fleet_in_being` / `insidious_flotilla_doctrine` -> `capital_fleet_modernisation`).
3. Air wing swaps aviation ideas (`ITA_ww1_battaglione_aviatori` -> `corpo_aeronautico_militare` -> `independent_air_force_charter`).
4. Intermediate focuses grant tangible rewards (dockyards, air bases, forts, artillery/infantry equipment, research bonuses) instead of creating separate permanent ideas.

- [ ] **Step 2: Run test to verify RED state**
Run: `python -m unittest tests/test_ww1_italy.py -v`

- [ ] **Step 3: Refactor focus tree rewards and idea definitions**
In `common/national_focus/italy.txt`:
Apply `remove_ideas` / `swap_ideas` for progressive doctrine tracks and replace redundant persistent ideas with concrete military rewards (equipment stockpiles, naval dockyards, air bases, doctrine bonuses).
In `common/ideas/ww1_italy_ideas.txt`:
Align starting ideas (`ITA_terre_irredente_dream`, `ITA_alpini_tradition`, etc.) so they do not conflict with or override core ideas with bad pictures.

- [ ] **Step 4: Run test to verify GREEN state**
Run: `python -m unittest tests/test_ww1_italy.py -v`
Verify all 16 tests pass with 0 errors.

- [ ] **Step 5: Commit**
```bash
git add common/national_focus/italy.txt common/ideas/ww1_italy_ideas.txt tests/test_ww1_italy.py
git commit -m "feat(ita): implement progressive idea swapping and tangible rewards to prevent topbar spirit stacking"
```

---

### Task 4: Master QA Audit & Verification

**Files:**
- All touched files
- Test: `scripts/qa_audit_all.py`

- [ ] **Step 1: Run complete repository QA audit**
Run: `python scripts/qa_audit_all.py`
Verify exit code 0 across all 6 audit suites (UK, Germany, France, Russia, Austria-Hungary, Ottoman, Italy).

- [ ] **Step 2: Verify BOM and encoding integrity**
Run: `python -c "for p in ['localisation/english/ww1_italy_l_english.yml', 'localisation/braz_por/ww1_italy_l_braz_por.yml']: b = open(p, 'rb').read(3); assert b == b'\xef\xbb\xbf', f'{p} missing BOM'"`

- [ ] **Step 3: Final verification and summary**
Ensure clean working tree, review git diff, and confirm that both issues reported by the user are completely resolved.
