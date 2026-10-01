---
name: hoi4-qa-debug-automation
description: >-
  Specialized quality assurance and test automation suite for Hearts of Iron IV modding.
  Delivers sub-second bracket syntax auditing, full DAG tree graph validation, texture
  integrity checks, state/tag verification, and automated Steam Workshop synchronization.
---

# HOI4 QA, Fast Debug & Automated Testing Suite

This skill provides an ultra-fast automated quality assurance pipeline designed to eliminate trial-and-error debugging, prevent in-game crashes (CTD), and drastically cut down computational and manual iteration time across all national focus trees.

Use this skill continuously during development and as a mandatory pre-flight check before delivering any mod feature.

---

## 1. The Sub-Second Bracket & AST Auditor

Clausewitz scripting files (`.txt`) crash the game or corrupt downstream logic if a single curly brace `{` or `}` is unclosed or misplaced. 

Instead of manual visual inspection or slow game bootups, use `scripts/fast_brace_auditor.py`:
- Parses 100,000+ lines of Paradox script in under 150 milliseconds.
- Tracks exact line, column, and parent block scope for unmatched braces.

### Usage:
```powershell
python scripts/fast_brace_auditor.py --path "common/national_focus/germany.txt"
```

---

## 2. Master Pre-Flight QA Suite

Run the unified test runner before any commit or user presentation:
```powershell
python scripts/master_qa_suite.py --mod-root "WW1"
```

The master suite executes six rigorous audit tiers in sequence:

| Tier | Audit Scope | Tool / Script | Failure Criteria |
| :--- | :--- | :--- | :--- |
| **Tier 1: Syntax** | Bracket matching `{}` across all files | `fast_brace_auditor.py` | Any unbalanced brace `stack != 0` |
| **Tier 2: Focus Graph** | 5-Wing coordinates, DAG cycles, backward edges | `validate_tree_layout.py` | `dy < 0`, duplicate `(x, y)`, cycle loops |
| **Tier 3: GFX Assets** | Sprite registration & physical textures | `check_missing_gfx.py` | Unregistered sprite, missing `.dds`/`.png` file |
| **Tier 4: Localisation** | UTF-8 BOM, smart quotes, Lua comments | `lint_yaml_bom.py` | Missing BOM header, curly quote, `--` comment |
| **Tier 5: Database Keys**| State IDs, country TAGs, ideology groups | Database cross-ref | Target state ID not found in `history/states/` |
| **Tier 6: Decisions** | Decision categories, mission timers | `verify_mechanics_syntax.py` | Mission without category, invalid ideology |

---

## 3. Steam Workshop High-Speed Synchronization

Once the QA suite passes with 0 errors, mirror the mod repository to the active Steam Workshop content folder:

```powershell
python scripts/sync_steam_workshop.py --src "WW1" --dest "C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491"
```

### Mirroring Exclusions:
The sync script strictly excludes non-game files to prevent Workshop bloat and file lock conflicts:
- `.git/` and `.gitignore`
- `.agents/`
- `tests/`
- `scratch/`
- `*.py`, `*.pyc`, `__pycache__`

---

## 4. Clausewitz Engine Crash Runbook & Diagnostics

When encountering issues in `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`:

| Error Message in log | Root Cause | Immediate Fix |
| :--- | :--- | :--- |
| `Unexpected token: focus in file...` | An extra or missing curly brace `{}` in the preceding focus block | Run `fast_brace_auditor.py` on the file; the error is typically 1–5 lines above the logged token. |
| `Missing texture for SpriteType: GFX_XYZ` | Sprite declared in `.gfx` points to a non-existent path, or DDS header is corrupt | Run `check_missing_gfx.py`; verify image exists in `gfx/interface/goals/` and is 32-bit RGBA. |
| `Could not find decision category...` | Decision uses a category name not present in `common/decisions/categories/` | Add category block in `common/decisions/categories/<tag>_categories.txt`. |
| `Graphic error: focus line points upward` | Focus has `child.y < parent.y` (`dy < 0`) | Adjust child `y` coordinate to be strictly greater than parent `y` (`dy >= 1`). |
| `Accented characters garbled in GUI (Ã©)` | Localisation file saved as UTF-8 without BOM | Run `lint_yaml_bom.py --fix-bom` to inject `\xef\xbb\xbf`. |
| `Event window cannot be closed` | Event has `is_triggered_only = yes` but 0 `option = { ... }` blocks | Add at least one valid `option` block with localized title. |
