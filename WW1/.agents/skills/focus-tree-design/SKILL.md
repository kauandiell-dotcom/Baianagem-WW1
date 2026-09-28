---
name: focus-tree-design
description: Princípios de design, balanceamento, pacing e estrutura de árvores de foco para HOI4 sem fillers.
---

# Skill: Design de Árvores de Foco (National Focus Trees)

Esta skill orienta os agentes na criação de árvores de foco significativas, dinâmicas e com forte identidade temática.

## 1. Princípios de Não-Proliferação de "Fillers"
- **Evitar durações padrão de 70 dias para tudo**: Focos diplomáticos urgentes, crises ou reorganizações menores devem durar 28, 35 ou 56 dias. Focos estruturais profundos (grandes reformas constitucionais ou industrialização maciça) justificam 70 dias.
- **Evitar bônus triviais isolados**: Nunca criar cadeias verticais de 4 focos consecutivos que concedem apenas "+5% de estabilidade" ou "1 fábrica civil". Cada foco deve introduzir uma escolha, desbloquear decisões, alterar dinâmicas de poder ou avançar a narrativa geopolítica.

## 2. Padrão Estrutural de Árvore
Uma árvore bem estruturada organiza-se em blocos modulares:
1. **Branch Política / Diplomática**:
   - Gestão de tensões internas, alianças da WW1 (Potências Centrais vs Entente vs Neutralidade Armada).
   - Uso de `mutually_exclusive = { focus = ... }` para escolhas reais com consequências irrevogáveis.
2. **Branch de Guerra e Exército**:
   - Doutrina de trincheiras, artilharia pesada, mobilização de reservas e logística.
3. **Branch Industrial e Econômica**:
   - Mobilização civil, economia de guerra, gestão de recursos escassos e rações.
4. **Branch Naval e Aviação**:
   - Bloqueio marítimo, guerra submarina, reconhecimento aéreo inicial e caças pioneiros.

## 3. Posicionamento e Relacionamento Visual
- Usar coordenadas relativas (`relative_position_id = <foco_pai>`, `x = 0`, `y = 1`) para manter alinhamento consistente e evitar que branches colidam visualmente.
- Utilizar `search_filters` apropriados (`FOCUS_FILTER_POLITICAL`, `FOCUS_FILTER_INDUSTRY`, `FOCUS_FILTER_WAR_SUPPORT`, `FOCUS_FILTER_RESEARCH`, etc.).
- Utilizar `custom_effect_tooltip` quando o efeito real for complexo demais para exibir cru ao jogador.
