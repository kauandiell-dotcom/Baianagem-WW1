# Regras Permanentes: Diretrizes de Performance

## 1. Princípios Gerais
Performance é um requisito de primeira classe no projeto Baianagem-WW1. Mods de HOI4 frequentemente sofrem com travamentos e lentidão no mid/late game causados por scripts ineficientes.

## 2. Padrões de Varredura e Loops
- **Proibição de Polling Frequente**:
  - NUNCA usar `every_country`, `every_other_country` ou `every_state` dentro de `on_daily` ou em triggers de eventos com MTTH (Mean Time To Happen) baixo.
- **Alternativa Orientada a Eventos**:
  - Preferir gatilhos pontuais (`on_ruling_party_change`, `on_war_relation_added`, `on_capitulation`, `on_peaceconference_ended`, conclusão de foco ou decisão do jogador).
- **Varreduras Mensais/Semanais**:
  - Se uma varredura for estritamente indispensável, executá-la em `on_monthly` com filtros rígidos (`limit = { ... }`) logo no topo do escopo para abortar iterações o mais cedo possível.

## 3. Triggers Otimizados
- Ordem de avaliação de triggers importa: coloque verificações booleanas baratas primeiro (`has_war = yes`, `tag = GER`, `has_country_flag = ...`) antes de checagens caras de cálculo (`num_of_factories > X`, contagem de divisões ou variáveis).

## 4. Revisão Obrigatória
- Todo novo subsistema que introduzir variáveis dinâmicas, `on_actions` periódicos ou `scripted_guis` com atualização contínua deve ser submetido à auditoria do **Performance Reviewer** antes da aprovação final.
