# Baianagem-WW1 — Documento do Projeto

## 1. Visão Geral
- **Nome do Projeto**: Baianagem-WW1
- **Pasta Raiz**: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- **Repositório Git**: `https://github.com/kauandiell-dotcom/Baianagem-WW1.git`
- **Versão Alvo do Hearts of Iron IV**: **1.19.3** (compatível com a versão estável atual)
- **Modo de Desenvolvimento**: Multiagente com Governança Técnica Estrita

## 2. Objetivo do Mod
Criar uma experiência focada na Primeira Guerra Mundial (WW1), dinâmica, imersiva e balanceada para Hearts of Iron IV, combinando profundidade histórica com caminhos alternativos instigantes, mecânicas de trincheiras e desgaste industrial, sem comprometer a performance do jogo.

## 3. Estado Atual do Repositório (Pós-Auditoria Inicial)
O repositório atual foi inicializado a partir de uma base híbrida herdada (commit `e746c28` - *BrunoLindoRoludo*), derivada principalmente do *Modern Borders Redux (MBR)* combinada com submods externos (Better Mechanics, HostTool, Victorianization, Lag Optimization):
- **Identidade Temática em Conflito**: Líderes modernos de 2024 (ex.: Friedrich Merz, Edi Rama, Alexei Navalny) coexistem com referências monárquicas (Tsar Nicolau II, Guilherme II) e mecânicas da WW1 (Aliança das Potências Centrais).
- **Focos Nacionais**: Todas as árvores nacionais baunilha foram substituídas por stubs vazios de 68 bytes (`# MBR 2026: intentionally empty; every country uses generic_focus.`) e arquivos `.disabled`. Apenas árvores genéricas gigantes (`generic_improved.txt`, `rcp_vanilla_generic_tree.txt`) estão ativas.
- **Dívida Técnica Crítica**:
  - `MBR_grant_level_one_technologies = yes` é chamado em todos os 369 arquivos de países em `history/countries/`, mas o scripted effect **não existe**.
  - `MBR_recruit_generic_advisors = yes` é chamado em on_actions sem estar definido.
  - Chaves não fechadas (`specialforces_ideas.txt`, `history/units/`) e chaves extras em 18 países (`history/countries/`).
  - Unidades como helicópteros (`GEN_helicopter.txt`, `@bm-divisional.txt`) exigem equipamentos inexistentes (`helicopter_equipment`, `bm_transport_helicopter_equipment`).
  - Sprites e GUI quebrados: `GFX_ww_stateview_bg` em `countrystateview.gui` não possui declaração `.gfx`; `MBR_Central_Powers.png` está incorretamente alocado em `interface/ideas/`.
  - Localisation dispersa e arquivo com extensão errada (`bulgaria_germany_l_english.txt`).

## 4. Filosofia de Design e Governança
1. **Separação de Funções**: Quem implementa não aprova. Cada entrega passa por revisão de design, técnica e QA.
2. **Qualidade Técnica Paradox**: Nenhum código deve ser inventado. Tudo deve seguir sintaxe de triggers, effects, scopes e modifiers válidos do HOI4 1.19.3.
3. **Performance First**: Proibição de varreduras globais frequentes (`every_country`, `every_state`) em ticks diários/semanais desnecessários.
4. **Foco em Identidade**: Cada país relevante na WW1 terá sua própria árvore e mecânicas, evitando árvores genéricas genéricas infladas de 70 dias.
