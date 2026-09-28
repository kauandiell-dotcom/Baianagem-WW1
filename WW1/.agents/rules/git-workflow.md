# Regras Permanentes: Fluxo Git & Colaboração

## 1. Verificação Prévia Obrigatória
Antes de iniciar qualquer alteração em arquivos:
1. Executar `git status` para assegurar que não há arquivos modificados externamente por outro desenvolvedor ou pelo usuário.
2. Executar `git log -n 5` para conhecer o estado recente do branch.
3. Se houver alterações não comitadas, NÃO sobrescrever nem reverter sem antes analisar a procedência.

## 2. Granularidade de Commits
- Cada commit deve ter escopo único, atômico e claro.
- Mensagens de commit devem seguir o padrão:
  - `feat(focus): adicionar branch naval da Alemanha 1914`
  - `fix(history): corrigir chaves desbalanceadas no arquivo da Albânia`
  - `refactor(defines): ajustar tick de cálculo de IA para otimização`
  - `docs(roadmap): atualizar status da Fase 0`
- Nunca misturar alterações de múltiplos subsistemas independentes em um único commit monstruoso.

## 3. Prevenção de Ações Destrutivas
- Proibido executar `git reset --hard` ou deleções em lote sem salvaguarda explícita.
- Ao refatorar ou remover arquivos herdados em desuso, garantir que não existam dependências ativas em `common/`, `events/` ou `interface/`.
