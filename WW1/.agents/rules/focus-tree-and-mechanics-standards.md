# Regras Permanentes: Padrão de Focus Trees e Mecânicas WW1

## 1. Arquitetura e Layout da Árvore de Focos
- **Dimensão de Grandes Potências:** Árvores de potências maiores (Alemanha, Rússia, França, Reino Unido, Áustria-Hungria) devem possuir entre 200 e 235 focos organizados em 5 a 7 asas temáticas.
- **Proibição de Escadas Retas (Anti-Ladder):** Proibido criar sequências verticais de 4 ou mais focos em linha reta sem escolhas. Utilizar o padrão `diamondize` (âncora -> opções paralelas -> convergência).
- **Navegação de Interface:**
   - Todo cabeçalho de árvore deve declarar `initial_show_position = { focus = ... }`.
   - Incluir blocos `shortcut = { name = ... target = ... }` apontando para o topo de cada asa temática.
   - A coordenada `continuous_focus_position` deve ser posicionada abaixo de todos os focos (`y = 3500+` conforme a altura máxima da árvore) para nunca sobrepor focos regulares.

## 2. Calibração de Recompensas e Balanceamento
- **Sem Spawn Mágico de Unidades:** Focos e decisões militares não devem criar exércitos completos ou equipamentos modernos do nada. Recompensas devem exigir custos (PP, apoio de guerra, fábricas civis, consumo de suprimento).
- **Bônus de Pesquisa:** Bônus de tecnologia devem ser de uso único (`uses = 1`, ~25-50%), sem redução antecipada de anos para impedir tecnologia de 1936 em 1912.
- **Limpeza de Fim de Guerra:** Modificadores temporários de guerra ou mobilização devem ser limpos ao término do conflito (`on_peaceconference_ended`, capitulação ou por eventos).

## 3. Segurança em Negociações e Tratados
- Em cadeias de paz ou concessão territorial (ex.: Brest-Litovsk), as propostas devem ser amarradas ao interlocutor original (`FROM`), com prazo de expiração (30 dias) e validação de controle militar antes de qualquer transferência de estado.
