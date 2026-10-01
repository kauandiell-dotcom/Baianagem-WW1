# Test Infrastructure Documentation: German Empire National Focus Tree (WW1 Mod)

**Target Project**: *Baianagem-WW1* (Hearts of Iron IV)  
**Mod Root**: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`  
**Active Workshop Target**: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`  
**Architecture**: 4-Tier Automated E2E Verification Engine  
**Test Entrypoint**: `python C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\tests\test_runner.py`  

---

## 1. Architectural Philosophy & Dual Track Design

In complex Paradox Clausewitz engine modding, subtle syntax mistakes—such as an unclosed curly brace `{`, missing UTF-8 Byte Order Mark (BOM), unregistered sprite identifier, or circular prerequisite dependency—result in silent engine failures, blank focus trees, or fatal desktop crashes (CTD).

The **Baianagem-WW1 E2E Test Suite** implements a 4-tier verification pipeline operating in tandem with milestone progression:

```
+-----------------------------------------------------------------------------------+
|                           Unified Test Runner (test_runner.py)                    |
+-----------------------------------------------------------------------------------+
       |                          |                         |                     |
       v                          v                         v                     v
+---------------+          +---------------+         +---------------+     +---------------+
|    TIER 1     |          |    TIER 2     |         |    TIER 3     |     |    TIER 4     |
| Syntax &      |          | Boundary &    |         | Graph &       |     | Dual Loc &    |
| Brace Audit   |          | Asset Audit   |         | Logic Audit   |     | Mirror Audit  |
+---------------+          +---------------+         +---------------+     +---------------+
| - {} Balance  |          | - DDS Binary  |         | - 0 DAG Cycles|     | - 100% EN Loc |
| - Unclosed \" |          | - DXT/RGBA    |         | - Prereq Exist|     | - 100% PT Loc |
| - UTF-8 BOM   |          | - GFX Sprites |         | - (x,y) Clean |     | - Steam Copy  |
| - YAML Headers|          | - Shine Defs  |         | - HoI4 Refs   |     |   SHA256 Sync |
+---------------+          +---------------+         +---------------+     +---------------+
```

---

## 2. Test Suite Component Inventory

The test infrastructure is located under `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\tests\`:

| File | Purpose | Authoritative Spec Source |
| :--- | :--- | :--- |
| `tests/spec.py` | Authoritative specifications for all 32 focuses, coordinates, ideas, events, and states. | `PLANO_FOCUS_TREE_ALEMANHA_WW1.md` §3–§7, `PROJECT.md` |
| `tests/tier1_syntax.py` | Clausewitz parser and YAML BOM/header validator. | Clausewitz engine syntax standard & HoI4 YAML specification |
| `tests/tier2_assets.py` | Binary DDS header parser, Pillow verification, and GFX sprite cross-reference. | DirectDraw Surface header specification & `interface/*.gfx` format |
| `tests/tier3_graph.py` | DAG cycle detection, coordinate collision detector, and HoI4 database reference auditor. | HoI4 focus tree architecture, `history/states/`, `common/ideas/` |
| `tests/tier4_localization_mirror.py`| Dual localization key coverage analyzer and Steam Workshop mirror diff validator. | `ORIGINAL_REQUEST.md` R3/R5, Steam Workshop layout |
| `tests/test_adversarial.py` | Stress tests for edge cases, escaped characters, corrupted headers, and cycles. | Adversarial testing standards |
| `tests/test_runner.py` | Unified master runner with ANSI summary tables, JSON output, and milestone reporting. | Project operational requirements |

---

## 3. Tier-by-Tier Technical Specifications

### Tier 1: Syntax & Brace Integrity (`tests/tier1_syntax.py`)
- **Clausewitz Engine Parser**:
  - Handles line comments (`# ...`) outside strings.
  - Handles double-quoted strings (`"..."`) with escaped quotes (`\"`).
  - Tracks line and column numbers for every `{` and `}`.
  - Ensures depth never drops below zero (premature closing brace) and returns to exactly zero at EOF.
- **Paradox YAML Localization Parser**:
  - Verifies exact 3-byte UTF-8 BOM (`\xef\xbb\xbf`).
  - Validates language header on first non-empty line (e.g. `l_english:`, `l_braz_por:`).
  - Validates key syntax (`<key>:0 "Value"` or `<key>: "Value"`).
  - Handles inline comments after closing quotes (`"Value" # comment`).

### Tier 2: Boundary & Asset Integrity (`tests/tier2_assets.py`)
- **DDS Binary Header Validation**:
  - Verifies 4-byte magic signature `b'DDS '` (0x20534444).
  - Verifies `dwSize` header size of 124 bytes (0x7C).
  - Extracts and asserts non-zero width (`dwWidth`) and height (`dwHeight`).
  - Validates Pillow image decoding in RGBA mode.
- **GFX Sprite Declarations**:
  - Parses `interface/ww1_germany_goals.gfx`.
  - Ensures each focus icon defines both a base `SpriteType` and an animated `_shine` `SpriteType`.
  - Confirms every `texturefile = "..."` points to an actual file on disk in `gfx/interface/goals/`.
- **Focus Tree Cross-Reference**:
  - Cross-references every `icon = GFX_...` in `common/national_focus/germany.txt` against `ww1_germany_goals.gfx`.

### Tier 3: Graph & Mechanical Integrity (`tests/tier3_graph.py`)
- **DAG Cycle Detection**:
  - Constructs a directed graph of focus dependencies.
  - Implements Depth-First Search (DFS) with 3-color tagging (White, Gray, Black).
  - Proves the graph is acyclic with **0 circular dependencies**.
- **Coordinate Collision Detection**:
  - Resolves both absolute `(x, y)` and relative coordinates (`relative_position_id`).
  - Asserts that no two focuses occupy the same grid cell.
- **HoI4 Reference Validation**:
  - **State IDs**: Scans `history/states/*.txt` and asserts that every state referenced in focus rewards exists.
  - **Idea IDs**: Scans `common/ideas/*.txt` and asserts that every idea in `add_ideas`, `remove_ideas`, `has_idea`, or `swap_ideas` is declared.
  - **Event IDs**: Scans `events/*.txt` and asserts that every event triggered via `country_event` is declared.

### Tier 4: End-to-End Consistency & Mirroring Integrity (`tests/tier4_localization_mirror.py`)
- **Dual Localization Coverage**:
  - Scans `localisation/english/*.yml` and `localisation/braz_por/*.yml`.
  - Ensures 100% key coverage for:
    - Focus titles (`<focus_id>`) and descriptions (`<focus_id>_desc`).
    - National idea titles (`<idea_id>`) and descriptions (`<idea_id>_desc`).
    - Country event titles (`<event_id>.t`), descriptions (`<event_id>.d`), and options (`<event_id>.a`).
- **Steam Workshop Mirroring**:
  - Computes SHA-256 hashes of local project files and compares them against the Steam Workshop copy at `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.
  - Flags missing files or outdated targets.

---

## 4. How to Run the Tests

### 1. Default Unified Runner (All Tiers)
```powershell
python C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\tests\test_runner.py
```

### 2. Tier Selection
```powershell
# Run only Tier 1 (Syntax)
python tests/test_runner.py --tier 1

# Run Tier 1 and Tier 2
python tests/test_runner.py --tier 1,2
```

### 3. Machine-Readable JSON Output
```powershell
python tests/test_runner.py --json
```

### 4. Strict Mode (Full Production Audit)
```powershell
python tests/test_runner.py --strict
```

### 5. Standard Python Unittest Discovery
```powershell
python -m unittest discover tests
```

---

## 5. Milestone Integration Matrix

The test runner tracks progressive implementation across the project lifecycle:

| Milestone | Deliverables | Covered By |
| :--- | :--- | :--- |
| **M1** | 32 DDS icons + `ww1_germany_goals.gfx` | Tier 1 (GFX syntax), Tier 2 (DDS binary & sprites) |
| **M2** | `ww1_germany_events.txt` + German ideas | Tier 1 (Syntax), Tier 3 (Idea/Event references) |
| **M3** | `germany.txt` (32 focuses) | Tier 1 (Braces), Tier 3 (DAG, coords, states) |
| **M4** | EN & PT-BR Localization (UTF-8 BOM) | Tier 1 (BOM/YAML syntax), Tier 4 (100% coverage) |
| **M5** | Robocopy synchronization to Steam | Tier 4 (Steam Workshop SHA-256 mirror verification) |
