---
name: hoi4-qa-debug-automation
description: >-
  Specialized quality assurance and test automation suite for Hearts of Iron IV modding.
  Delivers sub-second bracket syntax auditing, full DAG tree graph validation, texture
  integrity checks, state/tag verification, and automated in-repository test suite execution.
---

# HOI4 QA, Fast Debug & Automated Testing Suite

This skill provides an ultra-fast automated quality assurance pipeline designed to eliminate trial-and-error debugging, prevent in-game crashes (CTD), and drastically cut down computational and manual iteration time across all national focus trees.

Use this skill continuously during development and as a mandatory pre-flight check before delivering any mod feature.

---

## 1. The Sub-Second Bracket & AST Auditor

Clausewitz scripting files (`.txt`) crash the game or corrupt downstream logic if a single curly brace `{` or `}` is unclosed or misplaced. 

Instead of manual visual inspection or slow game bootups, use `scripts/qa_audit_all.py` or unit tests:
- Parses 100,000+ lines of Paradox script in under 150 milliseconds.
- Tracks exact line, column, and parent block scope for unmatched braces.

### Usage:
```powershell
python scripts/qa_audit_all.py
python -m unittest discover tests
```

---

## 2. Master Pre-Flight QA Suite

Run the unified test runner before any commit or user presentation:
```powershell
python scripts/qa_audit_all.py
```

The master suite executes rigorous audit tiers in sequence:

| Tier | Audit Scope | Failure Criteria |
| :--- | :--- | :--- |
| **Tier 1: Syntax** | Bracket matching `{}` across all files | Any unbalanced brace `stack != 0` |
| **Tier 2: Focus Graph** | Wing coordinates, DAG cycles, backward edges | Duplicate `(x, y)`, cycle loops |
| **Tier 3: GFX Assets** | Sprite registration & physical textures | Unregistered sprite, missing `.dds`/`.png` file |
| **Tier 4: Localisation** | UTF-8 BOM, valid YAML syntax | Missing BOM header (`0xEF, 0xBB, 0xBF`) |
| **Tier 5: Database Keys**| State IDs, country TAGs, ideology groups | Target state ID not found in `history/states/` |
| **Tier 6: Decisions** | Decision categories, mission timers | Mission without category, invalid ideology |

---

## 3. Pure In-Repository Validation (Zero External Mirroring)

- **Proibição de Espelhamento na Steam:** NUNCA copiar ou espelhar arquivos para `steamapps/workshop/content/...` ou para a pasta local da Paradox.
- Todas as validações e artefatos de teste devem permanecer 100% contidos no repositório local (`Baianagem-WW1\WW1`).
- Commits permanecem locais. O fluxo do usuário delega testes remotos e upload na Oficina ao colaborador via GitHub.
