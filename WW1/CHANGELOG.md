# Baianagem-WW1 — Registro de Alterações (Changelog)

Todas as alterações técnicas e de design relevantes deste projeto são documentadas neste arquivo de forma cronológica.

---

## [Unreleased] - Em Andamento

### Adicionado
- Criação dos documentos fundamentais de governança e engenharia:
  - `PROJECT.md`: Definição de escopo, objetivos e compatibilidade com HOI4 1.19.3.
  - `ARCHITECTURE.md`: Organização de diretórios, padrões técnicos e esteira multiagente.
  - `ROADMAP.md`: Cronograma e fases de desenvolvimento da Fase 0 à Fase 5.
  - `CHANGELOG.md`: Registro de versões e intervenções.
- Estrutura de governança multiagente em `.agents/`:
  - Regras permanentes em `.agents/rules/` (`hoi4-syntax-and-compatibility.md`, `git-workflow.md`, `performance-standards.md`, `qa-validation-rules.md`).
  - Skills operacionais em `.agents/skills/` (`hoi4-scripting`, `focus-tree-design`, `hoi4-events-decisions`, `hoi4-qa-validation`).
  - Definições de papéis de agentes em `.agents/agents/`.

### Auditoria e Diagnóstico (Fase 0)
- Mapeamento completo dos 3.486 arquivos herdados do commit `e746c28`:
  - Identificada dívida técnica grave decorrente de herança de mod anterior (*Modern Borders Redux* e submods agregados).
  - Diagnosticada ausência de scripted effect `MBR_grant_level_one_technologies` chamado em 369 países.
  - Identificadas 18 quebras de chaves em `history/countries/`, 1 em `common/ideas/specialforces_ideas.txt` e 3 em `history/units/`.
  - Mapeadas inconsistências de sprites (`GFX_ww_stateview_bg`, `MBR_Central_Powers`), comentários inválidos (`--`) e unidades com equipamentos inexistentes (`GEN_helicopter`, `@bm-divisional`).
  - Diagnosticada sobreposição de líderes modernos de 2024 em um mod temático de Primeira Guerra Mundial.

---

## [0.1.0-heritage] - 2026-09-28
- Commit inicial `e746c28` (*BrunoLindoRoludo*):
  - Cópia base de arquivos de mapa, história, interface e defines herdados.
