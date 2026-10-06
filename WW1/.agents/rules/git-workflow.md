# Regras Permanentes: Fluxo Git & Colaboração

## 1. Verificação Prévia Obrigatória
Antes de iniciar qualquer alteração em arquivos:
1. Executar `git status` para assegurar que não há arquivos modificados externamente por outro desenvolvedor ou pelo usuário.
2. Executar `git log -n 5` para conhecer o estado recente do branch.
3. Se houver alterações não comitadas, NÃO sobrescrever nem reverter sem antes analisar a procedência.

## 2. Proibição Absoluta de Modificação Externa (Steam & Paradox)
- **NUNCA COPIAR ARQUIVOS PARA A STEAM:** É expressamente proibido criar scripts ou executar comandos (`robocopy`, `Copy-Item`) para transferir arquivos para `E:\SteamLibrary\...`, `Program Files (x86)\Steam\...` ou qualquer diretório da Steam Workshop.
- Alterar arquivos diretamente na pasta da Workshop invalida os hashes do manifesto `appworkshop_394360.acf`, travando a fila de download da Steam do usuário em validação infinita ou gerando erros de gravação em disco.
- **NUNCA TOCAR NA PASTA DE MODS DO USUÁRIO:** Não criar descritores locais ou backups em `Documents/Paradox Interactive/Hearts of Iron IV/mod`.
- **PROIBIÇÃO DE `git push` AUTÔNOMO:** Nunca executar `git push`. Todos os commits ficam exclusivamente no repositório Git local. O fluxo do usuário define que um colaborador externo puxa as alterações do GitHub, testa e publica na Steam Workshop, enquanto o usuário baixa a versão oficial pela Steam.

## 3. Granularidade de Commits
- Cada commit deve ter escopo único, atômico e claro.
- Mensagens de commit no padrão Conventional Commits (`feat(...)`, `fix(...)`, `refactor(...)`, `chore(...)`).
- Nunca misturar alterações de múltiplos subsistemas independentes em um único commit monstruoso.

## 4. Prevenção de Ações Destrutivas
- Proibido executar `git reset --hard` ou deleções em lote sem salvaguarda explícita.
- Ao refatorar ou remover arquivos herdados em desuso, garantir que não existam dependências ativas em `common/`, `events/` ou `interface/`.
