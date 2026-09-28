# Regras Permanentes: Garantia de Qualidade e Validação (QA)

## 1. Regra Fundamental da Separação de Funções
> **Quem implementa NÃO aprova seu próprio trabalho.**

Nenhum desenvolvedor ou agente especializado pode mesclar código ou declarar uma tarefa concluída sem a validação formal de um agente revisor independente (Tech Lead, Performance Reviewer e QA Agent).

## 2. Checklist Obrigatório de Pré-Integração
Antes de qualquer submissão para merge, o agente deve validar:
1. **Integridade de Sintaxe**:
   - Chaves balanceadas (número de `{` igual a `}`).
   - Ausência de comentários inválidos (`--`, `//`).
2. **Resolução de Identificadores (IDs)**:
   - IDs de focos, eventos, decisões e ideias são únicos e não colidem com IDs baunilha indesejados.
   - Namespaces declarados em eventos antes do uso (`add_namespace = ...`).
3. **Localização**:
   - Cada ID de foco, evento, decisão e ideia possui sua chave de texto em arquivo `.yml` com codificação UTF-8 com BOM.
   - Nenhum texto cru em inglês técnico aparece na interface do usuário (ex.: `GER_schlieffen_plan_desc` sem tradução).
4. **Texturas & Sprites**:
   - Todo ícone referenciado (`icon = GFX_...`, `picture = GFX_...`) existe em um arquivo `.gfx` e o arquivo de imagem correspondente está presente no disco.
5. **Comportamento da IA**:
   - Decisões e focos críticos devem ter pesos de IA (`ai_will_do`, `ai_chance`) bem calibrados para evitar paralisia do bot ou escolhas absurdas.
