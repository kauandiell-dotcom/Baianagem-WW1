---
name: hoi4-ww1-architect
description: >-
  Master orchestrator and architectural guide for Hearts of Iron IV WW1 modding.
  Coordinates the specialized skills (focus design, mechanics, events, GFX, localisation,
  QA automation, and historical database) to build bug-free, deep focus trees for all nations.
---

# Hearts of Iron IV: WW1 Master Modding Architecture & Orchestration

This skill serves as the **Master Orchestrator** for the Hearts of Iron IV World War I total conversion mod (*Baianagem-WW1*). 

To ensure supreme quality, zero delays, zero visual glitches, and maximum historical immersion without computational waste, the development pipeline is partitioned into specialized skills. Whenever executing any modding task, invoke and adhere to the specialized skill dedicated to that domain.

---

## The Specialized HOI4 Modding Skills Suite

Whenever working on a nation (Germany, Russia, France, Britain, Austria-Hungary, Italy, Ottoman Empire, USA, or minors), follow this execution flow:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. [hoi4-historical-ww1-database]                            │
│    Extract ministers, generals, 1911-1920 timeline & crises │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. [hoi4-focus-tree-designer]                               │
│    Architect 5-7 wing layout, diamondize runs, shortcuts     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. [hoi4-scripted-effects-mechanics]                        │
│    Script real regime changes, timed operations & crises    │
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
│    Harvest icons from Workshop mods & register .gfx         │
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
│    Execute sub-second brace audit & in-repo unit testing    │
└─────────────────────────────────────────────────────────────┘
```

---

## Specialized Skills Reference Matrix

| Specialized Skill | Scope & Core Responsibility | Key Automated Tool / Script |
| :--- | :--- | :--- |
| **`hoi4-historical-ww1-database`** | Factions, political leaders, historical battles, territorial treaties, and plausible alt-history paths | Integrated reference library |
| **`hoi4-focus-tree-designer`** | 5-7 Wing coordinates, diamondize fork/merge patterns, header shortcuts, continuous focus clearance | `scripts/focus_layout.py`, `relayout_wings.py` |
| **`hoi4-scripted-effects-mechanics`**| Real power transfers (`set_politics`), timed breakthrough operations, material crises & recovery | `scripts/verify_mechanics_syntax.py` |
| **`hoi4-events-narrative-engine`** | Multi-country diplomatic crises, ultimatums, newspaper reports, AI weights, and custom tooltips | `scripts/validate_events.py` |
| **`hoi4-gfx-asset-pipeline`** | Icon harvesting from Workshop mods (TGWR, FFU2), 32-bit RGBA checks, and visual policy adherence | `scripts/check_missing_gfx.py` |
| **`hoi4-localisation-bilingual`**| English and Brazilian Portuguese (`l_braz_por`, `localisation/replace/zz_...`), mandatory UTF-8 BOM | `scripts/lint_yaml_bom.py` |
| **`hoi4-qa-debug-automation`** | Sub-second bracket checking, cycle detection, master QA runner (`qa_audit_all.py`), 100% in-repo tests | `scripts/qa_audit_all.py`, `tests/test_runner.py` |

---

## Golden Rules for Development Across All Nations

1. **Sem buffs estáticos desbalanceados**: Focos e decisões devem ter apostas reais, custos de preparação (PP, apoio de guerra, fábricas civis) e penalidades por falha.
2. **Layout com Losangos (Anti-Ladder)**: Usar o padrão `diamondize` para transformar corredores verticais longos em bifurcações e junções paralelas.
3. **Navegação de UI e Focos Contínuos**: Incluir `initial_show_position` e `shortcut` para cada asa no cabeçalho. A coordenada `continuous_focus_position` deve ficar abaixo de todos os focos (`y = 3500+`).
4. **Política Visual de Época**: Priorizar ícones e quadros históricos da Workshop. Geração de IA estritamente restrita a super eventos e telas centrais. Proibido criar variações mascaradas com nomes repetidos.
5. **Localização em UTF-8 com BOM Obrigatória**: Todo arquivo `.yml` deve iniciar com `\xef\xbb\xbf` e conter versões emparelhadas em inglês e português.
6. **PROIBIÇÃO DE MODIFICAÇÃO EXTERNA E GIT PUSH**: NUNCA espelhar arquivos para a pasta da Steam Workshop ou documentos locais da Paradox. Nunca rodar `git push` autônomo. Todo trabalho permanece 100% contido no repositório local.
