---
name: hoi4-ww1-architect
description: >-
  Master orchestrator and architectural guide for Hearts of Iron IV WW1 modding.
  Coordinates the 7 specialized skills (focus design, mechanics, events, GFX, localisation,
  QA automation, and historical database) to build bug-free, deep focus trees for all nations.
---

# Hearts of Iron IV: WW1 Master Modding Architecture & Orchestration

This skill serves as the **Master Orchestrator** for the Hearts of Iron IV World War I total conversion mod (*Baianagem-WW1*). 

To ensure supreme quality, zero delays, zero visual glitches, and maximum historical immersion without computational waste, the development pipeline is partitioned into **7 Specialized Skills**. Whenever executing any modding task, invoke and adhere to the specialized skill dedicated to that domain.

---

## The Specialized HOI4 Modding Skills Suite

Whenever working on a nation (France, Britain, Russia, Austria-Hungary, Ottoman Empire, Italy, USA, or minors), follow this execution flow:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. [hoi4-historical-ww1-database]                            │
│    Extract ministers, generals, 1911-1920 timeline & crises │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. [hoi4-focus-tree-designer]                               │
│    Architect 5-wing layout, (x,y) grid, allow_branch pruning │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. [hoi4-scripted-effects-mechanics]                        │
│    Script real regime changes, timed missions & ideas       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. [hoi4-events-narrative-engine]                           │
│    Author chain ultimatums, news events & dynamic tooltips  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. [hoi4-gfx-asset-pipeline]                                │
│    Harvest icons from EIF/TGWR & generate base+shine .gfx   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. [hoi4-localisation-bilingual]                            │
│    Generate English & Brazilian Portuguese with UTF-8 BOM   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. [hoi4-qa-debug-automation]                               │
│    Execute sub-second brace audit & sync to Steam Workshop  │
└─────────────────────────────────────────────────────────────┘
```

---

## Specialized Skills Reference Matrix

| Specialized Skill | Scope & Core Responsibility | Key Automated Tool / Script |
| :--- | :--- | :--- |
| **`hoi4-historical-ww1-database`** | Factions, political leaders, historical battles, territorial treaties, and plausible alt-history paths | Integrated reference library |
| **`hoi4-focus-tree-designer`** | 5-Wing coordinates (`x: 1-135`), DAG dependencies, `dy >= 1`, dynamic branch hiding via `allow_branch` | `scripts/validate_tree_layout.py` |
| **`hoi4-scripted-effects-mechanics`**| Real power transfers (`set_politics`), timed breakthrough missions (`days_mission_timeout`), ideas cascading | `scripts/verify_mechanics_syntax.py` |
| **`hoi4-events-narrative-engine`** | Multi-country diplomatic crises, ultimatums, newspaper reports, AI weights, and custom tooltips | `scripts/validate_events.py` |
| **`hoi4-gfx-asset-pipeline`** | Icon harvesting from Europe In Flames/TGWR, 32-bit RGBA texture checks, and `.gfx` shine animations | `scripts/check_missing_gfx.py`, `harvest_mod_icons.py` |
| **`hoi4-localisation-bilingual`**| English and Brazilian Portuguese (`l_braz_por`), mandatory UTF-8 BOM, text colors (`§Y`, `§G`, `§R`), path badges | `scripts/lint_yaml_bom.py` |
| **`hoi4-qa-debug-automation`** | Sub-second bracket checking, cycle detection, master QA runner, and automated Steam sync | `scripts/fast_brace_auditor.py`, `sync_steam_workshop.py` |

---

## Golden Rules for Development Across All Nations

1. **Never write static stat buffs alone**: Every operational focus must have real stakes, timed missions, or historical consequences.
2. **Never leave conflicting paths on screen**: Always use `allow_branch = { NOT = { has_country_flag = ... } }` so alternative paths completely vanish once the player commits.
3. **Never allow `dy <= 0`**: Children must strictly have `child.y > parent.y` to prevent backward or same-row arrow glitches.
4. **Never omit `_shine` sprites**: Every goal icon must have both a base and a scrolling shine definition in `.gfx`.
5. **Never omit UTF-8 BOM**: Every `.yml` file must strictly begin with `\xef\xbb\xbf` to preserve Portuguese accents.
6. **Always run the fast pre-flight suite before delivering**: Never wait for game launch to find a missing bracket or texture typo.
