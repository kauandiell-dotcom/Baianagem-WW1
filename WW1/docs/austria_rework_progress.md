# Rework da Áustria-Hungria (AUS) — Baianagem WW1

## 1. Resumo Executivo da Missão
Rework completo, imersivo e rigorosamente balanceado da árvore de focos, espíritos nacionais iniciais e decisões operacionais da Áustria-Hungria (`AUS`).
- **Problema Inicial Identificado:**
  1. Todos os 5 espíritos nacionais históricos de abertura (`AUS_dual_monarchy_compromise`, `AUS_tower_of_babel_army`, `AUS_skoda_siege_arsenals`, `AUS_alpine_carpathian_bastion`, `AUS_balkan_destiny`) eram deletados no dia 1 por `auh_ww1_initialise` e substituídos por placeholders rasos ou descartados.
  2. As recompensas dos focos eram rasas e abstratas (`coh:2`, `cons:1`, flags internas), sem construção palpável do país no mapa do HoI4.
  3. As operações militares duravam 90 dias com bônus descontextualizados (`planning_speed = 0.08`), permitindo acúmulo desproporcional.

## 2. Mudanças Implementadas de Ponta a Ponta

### A. Restauração e Evolução dos 5 Espíritos Nacionais Iniciais
- **Preservação no Startup:** Removidas as exclusões prematuras em `common/scripted_effects/ww1_austria_hungary_effects.txt` (gerado por `scripts/auh_country_support.py`).
- **Relação Dinâmica com a Árvore de Focos:**
  - `AUS_dual_monarchy_compromise`: Permanece ativo na largada; é substituído apenas após ratificação das reformas constitucionais de Dualismo (`AUH_ww1_budget_settled`), Trialismo (`AUH_ww1_budget_trialist`) ou Federalismo (`AUH_ww1_budget_federal`).
  - `AUS_tower_of_babel_army`: Permanece ativo na largada; é gradualmente reformado via focos de instrução regimental e corpo comum de oficiais (`AUH_ww1_languages_trained`, `staff`, `reformed`).
  - `AUS_skoda_siege_arsenals`: Permanece ativo na largada; é atualizado via padronização de arsenais (`AUH_ww1_arsenals_standardised`).
  - `AUS_alpine_carpathian_bastion`: Permanece ativo como bastião defensivo histórico dos Cárpatos e Alpes.
  - `AUS_balkan_destiny`: Permanece ativo na largada; se o jogador optar por acomodação regional nos Bálcãs, é substituído por `AUH_ww1_diplomatic_restraint`.

### B. Recompensas Concretas de Construção Nacional no Mapa
Atualizado o compilador de efeitos (`scripts/auh_focus_effects.py`) para injetar efeitos nativos Clausewitz de construção física no mapa:
- **Ferrovias Físicas no Mapa (`build_railway`):**
  - Eixo Viena–Budapeste (estados 4 -> 43, nível 2)
  - Eixo Praga–Viena (estados 9 -> 4, nível 2)
  - Corredor da Galícia (estados 43 -> 89, nível 2)
  - Acesso à Bósnia (estados 43 -> 104, nível 2)
  - Corredor Adriático (estados 4 -> 736, nível 2)
- **Indústria e Recursos Estruturais Históricos:**
  - Plzeň (Boêmia, 9): +1 fábrica militar (Škoda) + espaço para construção.
  - Steyr (Alta Áustria, 152): +1 fábrica militar (Steyr-Mannlicher) + espaço para construção.
  - Csepel (Budapeste, 43): +1 fábrica militar (Manfréd Weiss) + espaço para construção.
  - Vítkovice (Morávia, 75): +4 aço + 1 fábrica civil + espaço para construção.
  - Trieste (Litoral, 736): +1 estaleiro naval (Stabilimento Tecnico Triestino) + espaço para construção.
  - Drohobych (Galícia Oriental, 91): +4 petróleo + 1 infraestrutura.
- **Fortificações e Infraestrutura Regional:**
  - Przemyśl (Galícia, 89): +2 fortificações terrestres (bunkers).
  - Aspern/Viena (Baixa Áustria, 4): +1 base aérea.
  - Dalmácia (163): +1 base naval.
  - Infraestrutura (+1): Alta Áustria (152), Bacia Danubiana (154), Tirol (153), Sarajevo (104), Tirol Meridional (39).
- **Desenvolvimento das Terras da Coroa:**
  - Todas as 13 regiões/terras da coroa recebem +1 espaço compartilhado de construção ao ouvir seus Landtags/dietas (Boêmia, Morávia, Silésia, Galícia, Rutênia, Bucovina, Eslováquia, Transilvânia, Banato, Dalmácia, Trentino, Croácia, Bósnia).

### C. Operações Militares Temporárias e Balanceadas
- **Duração Restrita:** Tempo limite reduzido de 90 para 45 dias máximos de missão e ideia ativa.
- **Modificadores Táticos Setoriais (Dentro da API nativa do HoI4):**
  - `AUH_ww1_operation_serbia`: `army_infantry_attack_factor = +8%`, `breakthrough_factor = +8%`, `supply_consumption_factor = +5%`.
  - `AUH_ww1_operation_galicia`: `army_artillery_attack_factor = +10%`, `breakthrough_factor = +8%`, `planning_speed = +5%`.
  - `AUH_ww1_operation_isonzo`: `army_infantry_defence_factor = +8%`, `dig_in_speed_factor = +10%`.
  - `AUH_ww1_operation_carpathians`: `winter_attrition_factor = -20%`, `max_dig_in = +3`.
  - Falha / Exaustão (`AUH_ww1_operation_exhausted`): `planning_speed = -10%`, `org_loss_when_moving = +10%` por 45 dias com recarga de 180 dias.

## 3. Evidências de Validação e Testes
1. `tests/test_ww1_austria_hungary.py`:
   - 30/30 testes passando (`OK`).
   - Verifica preservação dos 5 espíritos de abertura, contratos de recompensa, paridade de localização EN e PT-BR com UTF-8 BOM, e inexistência de bônus militares abusivos empilhados.
2. `tests/test_ww1_script_encoding.py`:
   - 8/8 testes passando (`OK`).
3. `scripts/qa_audit_all.py`:
   - 0 erros de sintaxe, 0 erros de chaves, 0 erros de BOM, 21/21 tiers passando.
4. `scripts/validate_ww1_foundation.py`:
   - AUH issues: 0.
