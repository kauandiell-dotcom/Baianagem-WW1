# Plano de execução — Itália, Reino Unido e Áustria-Hungria (depois Alemanha e Rússia)

Data: 5 de outubro de 2026
Meta: 3 árvores de ~200 focos cada, com conteúdo completo (eventos, decisões, ideias, personagens, mecânica própria), GFX distinta, textos EN/PT-BR, caminhos alternativos completos até 1923.
Este documento é só o plano. Nada foi alterado no mod.

---

## 1. Ponto de partida real (conferido hoje)

| | Árvore | Eventos | Decisões/projetos | GFX dos focos | Situação |
|---|---|---|---|---|---|
| **Áustria-Hungria** | 200 focos prontos | 49 | ~105 | 200 (1 imagem repetida) | Quase pronta. 2 testes falham. Nunca jogada. Faltam fechar alternativas e pós-guerra. |
| **Reino Unido** | 200 focos no grafo, **todos sem efeito** | 8 | 1 arquivo pequeno | 55 de 200 | O contrato de cada foco já existe em `docs/britain_focus_contracts.json` (título, posição, data, nome da decisão prevista). Falta tudo o que faz o foco "acontecer". |
| **Itália** | **nenhuma** (`italy.txt` vazio, usa a genérica moderna) | 0 | 0 | 0 | Começa do zero. |

Ferramentas que já existem e vou reaproveitar: gerador da Áustria (`scripts/build_ww1_austria_hungary.py`) e seus 24 testes de contrato, importador de arte com rastreio de origem e bloqueio de duplicatas (`scripts/visual_asset_pipeline.py`), verificadores de foco/evento/localização em `tests/`.

---

## 2. Regra de ouro: o que é um foco "pronto"

Um foco só conta como pronto se cumprir **tudo**:

1. **Faz algo real e coerente com o nome** (ideia/instituição com custo, decisão liberada, evento, projeto, construção no lugar certo). Nunca só uma bandeira.
2. **Data e condições históricas** (não existe "Gabinete de Guerra" em 1912).
3. **Custo de oportunidade**: nada de bônus grande e permanente de graça. Reformas viram instituições que substituem a anterior.
4. **Ramos alternativos completos**: cada escolha excludente leva até 1923, com consequências e saída (nada de ramo que acaba no meio).
5. **IA sabe usar** (pesos históricos, não escolhe caminhos absurdos).
6. **Ícone único** (nem igual, nem recolorido, nem parecido com outro do mod inteiro).
7. **Texto EN e PT-BR** com título, descrição histórica curta e o que o foco realmente faz.
8. **Passa nos testes** do país.

Eventos são de três tipos: **decisão** (o jogador escolhe), **situação** (nasce de algo que aconteceu no jogo) e **ambientação** (só narrativa, sem bônus). Só os dois primeiros mudam o jogo.

---

## 3. Conteúdo-alvo por país

| País | Focos | Eventos | Decisões/projetos | Ideias/instituições | Mecânica própria |
|---|---:|---:|---:|---:|---|
| Áustria-Hungria | 200 | 49 → ~65 | ~105 (ok) | 39 → ~45 | Consentimento, coesão, provisões, dívida (já existe) |
| Reino Unido | 200 | 8 → ~60 | 0 → ~45 | 28 → ~40 | Dívida de guerra, tensão irlandesa, apoio trabalhista, recrutamento (já rascunhadas) |
| Itália | 200 | ~55 | ~45 | ~30 | Intervencionismo × neutralismo, Norte × Sul, irredentismo |

Números são metas de qualidade, não cota. Se uma decisão não muda nada, ela não entra.

### 3.1 Reino Unido — temas e alternativas
Dez ramos já definidos: constituição, indústria/finanças, império e Irlanda, diplomacia, exército, marinha, aviação, operações, reconstrução, pesquisa.
Alternativas que precisam ficar **completas**:
- **Compromisso continental × neutralidade armada** (com caminho de reconsideração).
- **Acordo trabalhista × controle industrial de emergência.**
- **Irlanda**: Home Rule, partição ou repressão, cada uma com consequências até 1921–22.
- **Pós-guerra**: dívida, desmobilização, mandatos, Chanak/1922.
Eventos planejados (exemplos): Ulster e Curragh, Lei do Parlamento, sufragistas, Dardanelos, Jutland, Lusitânia, crise dos projéteis, crise do recrutamento, Lloyd George assume, Balfour, Guerra de Independência irlandesa.

### 3.2 Itália — do zero
Dez ramos: (1) política giolittiana e disputa com nacionalistas/socialistas; (2) **guerra ítalo-turca na Líbia** (acontece logo na abertura de 1911); (3) economia e abismo Norte–Sul; (4) exército (Cadorna, Alpini, artilharia, Arditi só em 1917); (5) marinha (couraçados, MAS, Adriático); (6) aviação (Caproni); (7) diplomacia (Tríplice Aliança, Tratado de Londres, Albânia, Bálcãs); (8) guerra (Isonzo, Caporetto, Piave, Vittorio Veneto); (9) frente interna (intervencionismo, Semana Vermelha, racionamento, gripe); (10) pós-guerra (Vitória Mutilada, Fiume, Biennio Rosso, 1922).
Alternativas completas:
- **Lealdade à Tríplice × Entente (Londres) × neutralidade armada/mediadora.**
- **Rumo político**: liberal restaurado, nacionalista-fascista, socialista.
Mecânica própria: pressão intervencionista × neutralista (sobe com propostas, perdas e eventos; força ou atrasa a entrada), ligada a objetivos territoriais reais (Trentino, Ístria, Dalmácia).

### 3.3 Áustria-Hungria — o que falta fechar
Corrigir 2 falhas (arte repetida, arte da ideia alemã de integração), completar: trialismo × federalização × manutenção do dualismo até 1923, paz separada e dissolução com países sucessores, pós-guerra do lado derrotado, mais eventos das frentes italiana, da Sérvia e da Galícia.

---

## 4. Plano de GFX (das suas mods da Workshop)

**Fontes encontradas** em `E:\SteamLibrary\steamapps\workshop\content\394360` (51 mods):

| Mod | Ícones de foco | Imagens de evento | Uso provável |
|---|---:|---:|---|
| KaiserreduX | 18.032 (983 da Áustria) | 8.837 | Principal para Áustria-Hungria, política, economia |
| Call of War | 1.762 (Itália 193, Inglaterra 70, Hungria 61) | 1.105 | Itália, exército, marinha |
| The Great War Redux | 1.028 (ENG 33, ITA 17, HUN 15, AUH 13) | 780 | **Mais fiel ao período**; prioridade máxima |
| Europe in Flames AGORA | 951 | 362 | Complemento |
| Baianagem Moderno / Burden of Hegemony / Youjo Senki | 369 / 600 / 289 | poucos | Genéricos |

**Processo (sem repetição):**
1. **Catálogo** dos candidatos com nome, tamanho e assinatura visual (hash) por país/tema, sem copiar nada ainda.
2. **Prancha de contato** (grades de miniaturas) por tema. Eu olho as imagens e escolho pelo assunto e pela época. Nada entra só pelo nome do arquivo.
3. **Pedido exato** por foco (foco → arquivo de origem). O importador recusa qualquer repetição contra **o mod inteiro** (hash do arquivo, hash dos pixels e assinatura visual) e registra a origem.
4. **Funil de substituição** quando não há arte do tema: (a) arte do assunto certo; (b) arte de assunto equivalente da época (ex.: outro couraçado, outra fábrica); (c) referenciar ícone do jogo base por nome, sem copiar arquivo; (d) **só com sua aprovação**, uma imagem gerada para focos realmente importantes. Nunca ícone genérico com nome trocado.
5. **Verificação**: teste automático de duplicatas (visual) no mod inteiro, mais sua revisão visual por prancha final.
Necessidade estimada: ~145 ícones novos para o Reino Unido, ~200 para a Itália, 1 troca na Áustria, mais imagens de evento para os eventos principais.

Fotos e pinturas de época para eventos: priorizar imagens históricas (Great War Redux e similares); evitar cenas claramente de 1936+ (uniformes, tanques, aviões modernos).

## 5. Localização
Para cada foco, evento, decisão, ideia e personagem: texto em `english` e `braz_por`, mesmo cabeçalho/BOM dos arquivos atuais, mesma chave. Descrição do foco = contexto histórico curto + **o que realmente faz**. Teste automático de paridade EN/PT e de chave faltando, como já existe na Áustria.

---

## 6. Ordem de trabalho e entregas

Faço **uma árvore por vez**, em fatias de ~25–40 focos. Cada fatia: escrever → testar → relatar o que foi feito e o que não foi provado.

| Etapa | O que | Pronto quando |
|---|---|---|
| **0. Preparação** | Ponto de salvamento do trabalho atual; combinar que nenhum outro chat edita `uk.txt`, `italy.txt`, `austria.txt` nem seus eventos/decisões/localização; catálogo de GFX e pranchas; molde de testes compartilhado (Reino Unido e Itália usarão o mesmo tipo de teste da Áustria) | Catálogo e pranchas prontos; testes-base rodando |
| **1. Áustria-Hungria** (fechamento) | Corrigir as 2 falhas; completar alternativas, dissolução e sucessores; +eventos; revisar empilhamento de bônus | Testes verdes, 200 ícones únicos, sem ramo sem saída |
| **2. Reino Unido** | Implementar as 200 recompensas a partir dos contratos existentes; ~45 decisões; ~50 eventos novos; ~12 instituições; 145 ícones; alternativas (continental/neutro, trabalhista, Irlanda) completas; IA histórica | Nenhum foco só marca bandeira; 200 ícones; testes verdes |
| **3. Itália** | Grafo de 200 focos; mecânica intervencionismo × neutralismo; guerra da Líbia na abertura; ~55 eventos; ~45 decisões; ~30 ideias; ~200 ícones; três alinhamentos e três rumos políticos até 1923; IA | Igual ao Reino Unido |
| **4. Integração** | Cadeias entre os três (Tríplice, Tratado de Londres, frente italiana, Bálcãs); evitar bônus somados entre árvores | Nenhum evento sem destinatário; campanha testada no papel |
| **5. Verificação geral** | Testes de todas as árvores, duplicatas de GFX no mod inteiro, textos, lista do que **não** foi provado em jogo | Relatório honesto |
| **6. Alemanha e Rússia** | Refinar as árvores existentes: Rússia ganha eventos (hoje só 12), alternativas e pós-guerra; Alemanha fecha campanha e pós-guerra. Mesmo padrão e mesmos testes | Mesmas regras de "foco pronto" |

Por que Áustria → Reino Unido → Itália: a Áustria está quase pronta e me dá as ferramentas e os testes corrigidos; o Reino Unido já tem estrutura e contratos; a Itália exige criar tudo e se beneficia do que for aprendido.

## 7. O que continua sem prova

Eu não jogo o HOI4. Os testes que faço são estáticos (sintaxe, referências, condições, localização, duplicatas). Não provam: equilíbrio da campanha, aparência correta dentro do jogo, comportamento da IA, multiplayer. Isso precisa de partidas suas ou do seu amigo; eu preparo os registros (logs) para analisar depois.

## 8. Limitações do ambiente
Memória do computador está crítica: trabalho pesado só em sequência, sem vários agentes ao mesmo tempo. Por isso o ritmo é fatia por fatia.
