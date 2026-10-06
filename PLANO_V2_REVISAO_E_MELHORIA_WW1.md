# Baianagem WW1 — Plano de revisão, balanceamento e conclusão (v2)

Data: 5 de outubro de 2026
Projeto analisado: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1` (commit base `0d137d4`, com muito trabalho ainda não gravado no Git)
Versão do jogo usada como referência: HOI4 1.19.3 (a que o próprio mod declara em `descriptor.mod`)
Natureza deste documento: **só análise e planejamento. Nenhum arquivo do mod foi alterado.**

---

## 0. Como ler este documento

Cada afirmação importante vem marcada:

- ✅ **Conferi agora** nos arquivos do mod (hoje, depois dos relatórios anteriores).
- 📄 **Vem dos seus relatórios anexados** (plano mestre, relatório consolidado, plano de rebalanceamento). Não refiz a conta.
- 🧪 **Só o jogo rodando prova.** É hipótese de balanceamento, não fato.

Importante: eu não consigo jogar o HOI4 daqui. Tudo que depende de "ficou equilibrado ou não" precisa de partidas de teste. Por isso o plano inclui um método de teste (seção 9), e não só uma lista de ajustes de número.

---

## 1. Veredito em poucas linhas

1. O mod tem uma **boa fundação técnica** (datas 1911–1924, regras de combate revisadas, frotas de época, crises com causa material, cadeias diplomáticas). Isso vale manter.
2. Mas só **5 países têm árvore própria** (Alemanha, França, Rússia, Reino Unido, Áustria-Hungria). ✅
3. **Todos os outros países** (Itália, Japão, Turquia, EUA, Sérvia, Bélgica… tudo) usam a árvore genérica moderna de 280 focos, que tem rádar, comando de bombardeiros, mecanização, forças especiais e doutrina aérea. Em 1911 isso quebra a imersão na hora. ✅
4. A árvore do **Reino Unido tem 200 focos, mas nenhum faz nada de verdade**: cada um só marca uma "bandeira" interna e mostra um texto. Zero ideias, zero decisões liberadas, 2 chamadas de evento. ✅
5. O conteúdo está **muito desigual**: Alemanha 85 eventos, França 67, Áustria-Hungria 49, **Rússia 12**, **Reino Unido 8**. ✅ Rússia tem a maior árvore (235 focos) e a menor narrativa. Isso prejudica justamente o país que deveria "não morrer fácil, mas poder cair".
6. Há **sobras do HOI4 de 1936/2ª Guerra** ainda ativas: um arquivo de 300 KB de decisões de formação de países do mundo moderno, variáveis de economia da Alemanha nazista (MEFO Bills etc.), tecnologias navais até 1944, um arquivo de país "Reichskommissariat Nordamerika". ✅
7. Não há prova de que o equilíbrio geral funcione (Alemanha com chance real contra a Entente, França se defendendo, Rússia resistindo). **Nunca foi medido em partida.** 🧪
8. O trabalho de hoje está **todo solto**: o Git ainda está no mesmo commit antigo e há 202 itens pendentes. ✅ Vários chats mexeram em paralelo. Risco real de perda ou conflito.

**Conclusão:** antes de "balancear números", o mod precisa de (a) proteção do que já existe, (b) integridade (nada quebrado nem prometendo o que não entrega), (c) todos os países com uma experiência do período, e só então (d) calibragem por partidas. Balancear em cima de árvores vazias ou com bônus falsos é retrabalho garantido.

---

## 2. Fotografia real do mod

### 2.1 Países com árvore própria ✅

| País | Focos | Eventos próprios | Decisões/projetos | O que realmente faz |
|---|---:|---:|---|---|
| Alemanha | 207 | 85 (+26 em arquivo de aprofundamento compartilhado com a Rússia) | ~9,7 KB + operações | Mais completa narrativamente. Falta fechar campanha, pós-guerra e medir equilíbrio. |
| França | 222 | 67 | ~10 KB | Recompensas corrigidas, 18 reformas limitadas. Faltam pós-guerra e teste de defesa. |
| Rússia (SOV) | 235 | **12** (+26 compartilhados) | ~3,3 KB de operações | Muito foco, pouca história ligada. Precisa do maior reforço de eventos. |
| Reino Unido | 200 | **8** | ~1,9 KB | **Esqueleto.** Os 200 focos só marcam bandeiras. Ícones de 145 focos faltando (📄). |
| Áustria-Hungria (AUS) | 200 | 49 | ~97 KB (5 arquivos) | Mais rica em mecânicas (consentimento, coesão, dívida). Nunca jogada. Duas falhas visuais abertas. |

Observação: 📄 o relatório consolidado dizia "zero eventos e zero decisões britânicas". Hoje já existem 8 eventos e um arquivo pequeno de decisões (`ww1_britain_policy_*`). Avançou, mas **os 200 focos continuam sem efeito** (✅ 200 "bandeiras", 0 ideias, 0 decisões liberadas).

### 2.2 Países sem árvore própria ✅

Itália, Japão, Turquia (Otomanos), EUA, Sérvia, Bélgica, Bulgária, Romênia, Grécia, Portugal, China, México, Brasil e todos os demais têm arquivo de foco **vazio de propósito** ("every country uses generic_focus"). Na prática jogam com a árvore `generic_focus_improved` (280 focos, prioridade padrão). Nela aparecem focos como rádar, bombardeiros, mecanização e forças especiais. É a 2ª Guerra Mundial vestida de 1911.

As árvores originais do HOI4 desses países foram guardadas como `.disabled` (56 focos cada). Isso é bom: o jogo moderno não vaza, mas também significa que **não existe nada do período no lugar**.

### 2.3 Tamanho das forças de abertura (1911) ✅

Divisões nos arquivos de abertura `*_1936_generic.txt` (o nome "1936" é só herança de arquivo):

| Potência | Divisões | | Potência | Divisões |
|---|---:|---|---|---:|
| Alemanha | 42 | | Sérvia | 11 |
| Rússia | 42 | | Bulgária | 11 |
| França | 34 | | Romênia | 10 |
| Áustria-Hungria | 32 | | Grécia | 8 |
| Turquia | 28 | | Bélgica | 7 |
| Itália | 26 | | EUA | 14 |
| Reino Unido | 22 | | | |

🧪 Leitura preliminar (a confirmar em jogo): Rússia igual à Alemanha em divisões parece pouco para o maior exército de reserva da época; o Reino Unido com 22 divisões faz sentido como força de pequeno porte terrestre, desde que a marinha compense. O que importa não é o número bruto, e sim equipamento, organização, apoio e reservas que cada país consegue convocar. Isso ainda não foi medido.

Estoque inicial de equipamento (exemplo Alemanha ✅): 6.000 fuzis, 120 artilharias, 80 equipamentos de apoio para 42 divisões. 🧪 Precisa de teste para saber se isso sustenta as unidades no primeiro mês ou se o jogador começa já com falta.

### 2.4 Base de regras ✅

`01_defines.lua` já está bem comentado e trata jogador e IA igual. Pontos positivos: datas 1911–1924, limite de forças especiais 5% com mínimo de 24, cobertura aérea limitada, suprimento nativo preservado.

### 2.5 Tecnologia ✅

- Infantaria, artilharia, apoio, indústria, aviação e blindados: datas entre 1889 e 1922. **Nenhuma passa de 1923.** Isso está correto.
- Marinha: `naval.txt`, `MTG_naval.txt` e `MTG_naval_Support.txt` ainda têm **24 tecnologias com data igual ou maior que 1925 (até 1944)**. O relatório cita 22 "guardas cronológicas" (📄) que escondem parte disso, mas as tecnologias continuam no arquivo. Risco de vazar para a campanha.
- `special_projects_tech.txt` tem 1 item em 1925.
- 🧪 Blindados vão de 1893 a 1920 com 47+29 tecnologias: precisa verificar se o que está ali é mesmo de época ou se são as tecnologias da 2ª Guerra apenas renumeradas.

---

## 3. Problemas encontrados, por gravidade

### P0 — Quebra o jogo ou a promessa principal

| # | Problema | Evidência | Correção | Critério de pronto |
|---|---|---|---|---|
| P0-1 | Trabalho não gravado no Git | ✅ HEAD `0d137d4`, 202 itens pendentes | Criar ponto de salvamento (commit em ramo de trabalho) antes de qualquer edição | Ramo `trabalho/ww1-v2` com tudo gravado |
| P0-2 | Reino Unido: 200 focos sem efeito | ✅ 200 flags, 0 `add_ideas`, 0 `unlock_decision` | Reconstruir recompensas (ver Fase 5) | Nenhum foco que só marca bandeira |
| P0-3 | Todos os outros países usam árvore moderna | ✅ `generic_focus_improved` | Árvore genérica WW1 nova (Fase 7); provisório: esconder os focos anacrônicos | Nenhum foco de rádar, mecanização ou bombardeiro visível antes do tempo |
| P0-4 | 8 chamadas de evento inexistentes | 📄 ex.: `ww1_britain.3`, `EST_events.3`, `GOE_RAJ.32` | Criar ou remover cada chamada | Verificador estático = 0 |
| P0-5 | 2 testes do conjunto geral falhando | 📄 arte `side_ww1_GER_austrian_integration` sem registro; foco `AUH_ww1_mannlicher_standards` com imagem repetida | Registrar a arte; trocar a imagem | 107/107 |
| P0-6 | 2 texturas inexistentes na árvore genérica | 📄 `focus_generic_sway_navy`, `focus_generic_sabotage` | Substituir ou remover | Verificador = 0 |
| P0-7 | ~1.647 usos de texto sem tradução cadastrada | 📄 (muito é conteúdo herdado) | Triagem: separar o que o jogador vê do que é código morto | 0 textos faltando no conteúdo acessível em 1911–1923 |

### P1 — Quebra a imersão ou o equilíbrio

| # | Problema | Evidência | Correção |
|---|---|---|---|
| P1-1 | Arquivo de decisões de formação de países moderno, 300 KB, ativo | ✅ `formable_nation_decisions.txt` (2.210 blocos), não tocado desde 28/09 | Desativar o que é de 1936+ e manter só formações plausíveis para 1911–1923 |
| P1-2 | Sobras da Alemanha nazista no arquivo de história | ✅ MEFO Bills, CGFF, variáveis de bens de consumo e de ouro soviético em `GER - Germany.txt` | Remover ou reaproveitar com sentido de época |
| P1-3 | Arquivo de país moderno sobrando | ✅ `RUS - Reichskommisariat Nordamerika.txt` | Remover do caminho de carga |
| P1-4 | Naval moderno escondido por data | ✅ 24 tecnologias ≥ 1925 | Remover de verdade do conjunto da campanha |
| P1-5 | Unidades fora de época | 📄 3 "ANZAC Expeditionary Corps" em 1911; desbloqueio dos Arditi | Renomear/retirar; liberar só por contexto |
| P1-6 | Empilhamento de buff não medido | 📄 Alemanha: 4 ideias somam +55% produção militar em teoria; França: 56 focos com modificador mal declarado | Orçamento de modificadores (Fase 3) |
| P1-7 | Guerra química e submarina aplicam penalidade ampla sem causa | 📄 | Operações limitadas, com preparação e contramedida |
| P1-8 | Desequilíbrio de narrativa entre países | ✅ Rússia 12 e Reino Unido 8 eventos | Metas mínimas de conteúdo por país (Fase 5 e 6) |
| P1-9 | Progressão naval incompleta | 📄 pesquisas gerais ainda apontam para cascos modernos | Concluir conversão (Fase 2) |

### P2 — Polimento necessário

| # | Problema |
|---|---|
| P2-1 | Pares de imagens repetidas (📄 171 grupos; parte é herdada) |
| P2-2 | 97 trocas de arte planejadas, nenhuma aplicada (📄) |
| P2-3 | Documentos antigos ainda citam árvore alemã de 32 focos e fluxo de Steam já descartado (📄) |
| P2-4 | Nomes de arquivo "1936" em toda a abertura; confunde manutenção futura |
| P2-5 | 408 tags de países do mundo de 1936 em `common/countries` (✅ contagem de arquivos; a maioria é inofensiva, mas deve ser auditada) |
| P2-6 | Os dois marcos de data do jogo têm nomes de bookmark herdados (`blitzkrieg.txt`, `the_gathering_storm.txt`). O segundo já está em 1911; conferir o primeiro |

### P3 — Depois de tudo estável
Cenário de 1914, música/sons extras, tutorial, telas novas opcionais.

---

## 4. Diagnóstico pelos seus critérios

### 4.1 Empilhamento de buffs
Hoje ninguém sabe o teto real de cada país. Isso é o maior risco para "todos têm chance de vencer".

Plano: criar uma **planilha automática** (script) que lista, para cada país e cada fase (1911, 1914, 1916, 1918, 1920), todas as fontes de bônus alcançáveis (ideias, focos, decisões, tecnologias, doutrinas, líderes, operações) e soma o total por tipo.

**Orçamento inicial sugerido** (ponto de partida, a calibrar 🧪):

| Tipo de bônus | Permanente (fontes nacionais) | Temporário (operação) |
|---|---|---|
| Produção militar | até +15% em 1914, +25% em 1918 | +10% por até 60 dias, com custo |
| Ataque/defesa terrestre | até +5% permanente | até +15% por 60 dias, só em frente definida |
| Velocidade de pesquisa | até +15% | — |
| Reposição/mano de obra | ganho só por reforma com custo civil | — |
| Suprimento | só por infraestrutura ou rota real | — |

Regras: etapas da mesma reforma **substituem** a anterior; vantagem temporária **expira**; nada de bônus geral de "vitória histórica".

### 4.2 Tropas fortes ou fracas demais 🧪
Não dá para julgar pelo arquivo. Método: tabela de **divisão completa** (custo, homens, organização, ataque, defesa, ruptura, suprimento) e combates simulados padronizados (ataque sem preparo, ataque preparado, defesa em trincheira, falta de suprimento). Alvo: **nenhuma composição substitui todas as outras**. Pontos a examinar primeiro:

- Tropas de elite com organização alta e consumo baixo (📄 `elite_inf`, assalto).
- Cavalaria ainda útil demais em posição preparada?
- Blindados: 1893–1920 com 76 tecnologias, verificar se tanques aparecem cedo demais.
- Artilharia como peça necessária para ofensiva (não só bônus).
- Unidades coloniais: barato, mas sem superioridade universal.

### 4.3 Consistência e jogabilidade
- Prometer menos e entregar mais: cada foco com **contrato** (o que diz, o que faz, quem recebe, quanto custa, como encerra).
- Cadeias diplomáticas sempre com: proposta → resposta → compromisso → execução → encerramento.
- Toda mecânica nova precisa de três coisas antes de entrar: texto EN/PT, comportamento da IA e limpeza quando a condição some (capitulação, paz, país desaparece).

### 4.4 Focos e eventos que não condizem ou não fazem nada
**Classificação obrigatória de cada foco**: Preservar · Corrigir · Fundir · Substituir · Remover.

Padrões a caçar em todas as árvores:

1. Foco que só marca bandeira ou mostra tooltip (**todo o Reino Unido**).
2. Foco que promete X e dá Y (ex.: "ajuda militar" que só altera opinião; 📄 armistício francês sem paz).
3. Evento chamado por foco errado (📄 OHL × Gorlice × Reichstag).
4. Bônus sem alvo (📄 24 pesquisas: 3 alemãs, 21 russas — parte já corrigida; reconferir).
5. Recompensa de construção no estado errado (📄 10 casos franceses; parte corrigida).
6. Foco "irrelevante": pequeno bônus repetido em sequência → fundir em uma reforma.
7. Foco de vitória/comemoração sem causa (nada de "vitória em Verdun" por clicar foco).
8. Efeito que ignora capitulação, guerra civil ou país inexistente.

### 4.5 Onde o mod está "arcade"
Padrões a eliminar ou reescrever:

- Bônus percentual grande e permanente como prêmio.
- Unidades ou equipamento surgindo do nada.
- Território virando "núcleo" por tempo passado.
- Penalidade global contra todos os inimigos (gás, submarino).
- Vantagem oculta para o jogador humano (📄 já removida; conferir).
- Crises por calendário fixo, resolvidas gastando poder político.
- Formação de países do mundo moderno em um clique.

---

## 5. Balanceamento exclusivo por país

Cada país precisa de: **identidade**, **ponto forte**, **ponto fraco**, **caminho de vitória**, **caminho de derrota** e **o que impede o colapso fácil**. Tudo abaixo é meta de projeto 🧪, a validar em partidas.

| País | Ponto forte | Ponto fraco | Como vence | Como perde | O que impede queda fácil |
|---|---|---|---|---|---|
| **Alemanha** | Indústria, ferrovias, estado-maior, qualidade | Duas frentes, bloqueio, aliados fracos, dívida | Preparar transporte e reservas até 1914, golpe rápido no oeste **ou** virada para o leste, depois paz negociada | Guerra longa sem suprimento; ofensiva sem preparo; crise alimentar | Linhas internas: transporte rápido entre frentes custa pouco |
| **França** | Defesa preparada, aliados, colônias | Menos população, indústria mais frágil, moral | Segurar a fronteira, poupar reservas, contra-ofensivas preparadas com apoio aliado | Atacar cedo demais (perdas e motins); perder polos industriais do norte | Fortificação e recuo organizado dão tempo; aliados cobrem buracos |
| **Rússia** | Reservas humanas, território, ferrovias longas | Equipamento, logística, política interna | Trocar espaço por tempo; mobilizar e modernizar; ofensiva específica (ex.: sudoeste) | Legitimidade cai, suprimento falha, revolução | Profundidade: avanço inimigo sofre desgaste e falta de suprimento; cair exige erros políticos acumulados |
| **Reino Unido** | Marinha, finanças, império | Exército pequeno no início, dependência de rotas | Manter o mar aberto, financiar aliados, crescer o exército a tempo | Perder rotas; recrutar tarde; crise irlandesa/trabalhista | Ilha + marinha: invasão quase impossível sem perder o mar |
| **Áustria-Hungria** | Posição central, indústria razoável | Nacionalidades, coesão, muitas frentes | Segurar Sérvia e Galícia com apoio alemão, reformas internas a tempo | Coesão e fome caem; frente italiana e russa juntas | Mecânica de coesão dá sinais e tempo de reação antes da dissolução |
| **Otomanos** | Estreitos, posição | Dívida, distância, pouca indústria | Fechar os estreitos, sustentar 1–2 frentes | Múltiplas frentes, revoltas | Estreitos e deserto encarecem o ataque inimigo |
| **Itália** | Entrada negociável | Indústria fraca, recursos, Alpes | Barganhar a entrada e objetivos limitados | Entrar mal preparada | Alpes defensivos |
| **EUA** | Economia enorme | Preparação lenta, transporte | Chegar tarde, mas com peso | Intervir sem preparo | Distância protege, custo de transporte limita |
| **Japão** | Marinha, foco asiático | Pouca interação europeia | Objetivos asiáticos e navais | Sobre-expansão | Isolamento geográfico |

Princípios:
- **Nenhum resultado obrigatório por data.**
- **Vitória de país pequeno** = cumprir objetivo proporcional (sobreviver, reconquistar porto, manter autonomia), não derrotar potência.
- **Entente e Potências Centrais** devem poder vencer ou empatar em partidas diferentes.

---

## 6. Visão do jogador (curto, médio, longo prazo) e imersão

| Fase | O jogador deve sentir | O mod precisa ter |
|---|---|---|
| **1911–1913** Preparação | Tempo para escolher: indústria, reservas, marinha, aliança. Tensão crescente. | Árvores de época para **todos**, decisões de preparação com custo real, crises diplomáticas claras, avisos. |
| **1914–1916** Guerra de desgaste | Logística e produção mandam; ofensivas custam caro. | Operações preparadas (35 dias de preparo, 60 de execução), suprimento como gargalo, reposição limitada. |
| **1917–1918** Crise e decisão | Sociedade e tropas cansadas; novas intervenções; revolução possível. | Crises com causa material, recuperação gradual, caminhos de paz. |
| **1919–1923** Pós-guerra | Converter resultado militar em sobrevivência política. | Tratados, desmobilização, dívida, veteranos, guerras sucessoras só se as condições existirem. |

Imersão (prioridade visual): retratos, bandeiras, ícones e unidades que o jogador vê **todo o tempo** vêm primeiro. Textos EN/PT com paridade. Nada de radar, "blitzkrieg" ou "divisão blindada" em 1911.

---

## 7. Padrões técnicos para programar "no jeito atual" (1.19.3)

1. Doutrinas com o sistema atual (grandes doutrinas, subdoutrinas, domínio), nunca os atributos antigos.
2. Forças especiais com `special_forces = yes` e limite nativo.
3. Instituições como **ideias com substituição** (sem acúmulo).
4. Processamento semanal/mensal por país envolvido; evitar varredura global frequente.
5. Efeitos de operação com prazo, custo, limpeza no fim.
6. IA com `ai_strategy_plans` históricos em vez de planos herdados do jogo moderno.
7. Marinha pelos módulos e cascos novos (Man the Guns) com caminho alternativo sem a DLC.
8. Cada DLC-dependência com alternativa explícita.
9. IDs com prefixo coerente por país e por sistema.
10. Antes de cada marco: reconferir a versão estável do jogo e os arquivos nativos (não confiar em memória).
11. Toda alteração passa pelos testes `tier1` a `tier4`, `test_ww1_gameplay_contracts` e novos testes do item alterado.

---

## 8. Plano por fases

Tamanho relativo: **P** pequeno, **M** médio, **G** grande. Não prometo datas: a duração real só se conhece depois das primeiras fases.

### Fase 0 — Proteger o trabalho (P) · **primeiro de tudo**
- Criar ramo de trabalho e gravar os 202 itens pendentes.
- Definir **um único dono por arquivo** quando houver mais de um chat trabalhando (lista de arquivos compartilhados: crises, diplomacia, ideias, tecnologias, localização).
- Inventário atualizado (o relatório das 15:38 já ficou velho).
- **Pronto quando:** tudo gravado e um arquivo `DONOS.md` definido.

### Fase 1 — Integridade (M)
- Corrigir P0-4, P0-5, P0-6.
- Triagem dos ~1.647 textos faltando (separar visível ao jogador de herdado).
- Remover sobras: `Reichskommisariat Nordamerika`, variáveis nazistas na história alemã, formáveis modernos, naval ≥1925.
- Atualizar testes antigos (árvore alemã de 32 focos etc.) e documentos obsoletos.
- **Pronto quando:** verificador estático sem erro bloqueador, testes 107/107.

### Fase 2 — Cenário de 1911 (M–G)
- Auditar abertura de cada potência: divisões, modelos, equipamento, estoque, reservas, líderes, frotas, aviação, ferrovias, suprimento.
- Corrigir anacronismos (ANZAC, Arditi, tanques e aviões inexistentes em 1911).
- Concluir progressão naval (pesquisas gerais ainda ligadas a cascos modernos).
- Confirmar fábricas iniciais em jogo (📄 GER 67, ENG 50, FRA 48, SOV 46, AUS 53, ITA 32, TUR 30, USA 85) — ✅ minha contagem rápida por estado não bate com todos esses números, portanto **conferir no jogo** antes de mexer.
- **Pronto quando:** cada potência inicia com abertura coerente, IA e humano iguais.

### Fase 3 — Economia, empilhamento e combate (G)
- Script do **orçamento de modificadores** por país/fase (seção 4.1).
- Tabela de divisões completas e testes de combate padronizados (4.2).
- Reescrever recompensas arcade: trocar bônus permanente por instituição com custo.
- Guerra química e submarina como operação limitada.
- **Pronto quando:** nenhum país ultrapassa o orçamento; nenhuma composição domina todos os testes.

### Fase 4 — Sistemas comuns (G)
Construir uma vez, usar em todos os países (seção 3 do plano mestre):
- Crises com causa material (já há base), recuperação e recaída.
- Operações preparadas (base alemã e russa já existe).
- Diplomacia: proposta → resposta → compromisso → execução.
- Mobilização e desmobilização.
- Paz e tratados: armistício, condições, aceitação, execução.
- **Pronto quando:** uma campanha de ponta a ponta (Alemanha vs. França) roda sem evento quebrado.

### Fase 5 — As quatro árvores grandes (G, uma por vez)
Ordem sugerida: **Reino Unido → Rússia → Alemanha → França → Áustria-Hungria** (Reino Unido tem mais a perder; Rússia tem menos história).

Para cada árvore:
1. Inventário foco por foco com classificação (Preservar/Corrigir/Fundir/Substituir/Remover).
2. Ligar cada foco a efeito real: ideia, decisão, evento, projeto.
3. Metas mínimas de narrativa (eventos de decisão e de situação; nada de notícia com bônus): **Reino Unido e Rússia ao menos ao nível da França (~60 eventos)**, sem encher linguiça.
4. Pós-guerra até 1923 para vencedor, derrotado e paz negociada.
5. IA histórica com peso coerente.
6. Teste de alcançabilidade (tempo real para percorrer cada rota exclusiva).

**Pronto quando:** nenhum foco só marca bandeira; promessa = entrega; textos EN/PT; testes verdes.

### Fase 6 — Itália, Otomanos, EUA, Japão (G)
Árvores dedicadas e pequenas em decisões significativas (não em contagem), cada uma com: preparação, neutralidade ou entrada, crise, paz, continuidade até 1923.

### Fase 7 — Países secundários e árvore genérica WW1 (G)
- **Árvore genérica WW1 nova**, no lugar de `generic_focus_improved` (desenvolvimento, instituições, defesa, comércio, neutralidade, aproximação externa, reconstrução).
- Módulos compactos: Sérvia, Bélgica, Bulgária, Romênia, Grécia, Portugal, China, México, Brasil.
- Módulos de domínios: Canadá, Austrália, Nova Zelândia, Índia, África do Sul.
- **Pronto quando:** nenhum país jogável vê foco anacrônico.

### Fase 8 — Pós-guerra completo (G)
Tratados, reparações, dívida, veteranos, revoluções e guerras sucessoras só quando as condições existem.

### Fase 9 — Calibragem, IA, interface e lançamento (G)
Rodadas de teste (seção 9), ajuste de números, multiplayer, tutorial, cenário de 1914.

**Dependências:** 0 → 1 → 2 → 3 → 4 → 5. As fases 6 e 7 só começam quando os sistemas comuns (4) estiverem estáveis. A Fase 9 roda em pequena escala desde a Fase 3, para não descobrir tudo no final.

---

## 9. Como medir equilíbrio (o que eu preciso de você)

Como não consigo rodar o jogo:

1. **Eu preparo o instrumento**: eventos de registro (log) que gravam, em datas fixas (1912, 1914, 1916, 1918, 1920, 1923), para cada potência: divisões, fábricas, equipamento em estoque, suprimento, estabilidade/apoio à guerra, crise ativa, baixas e situação de guerra. Mais um script que lê o log e monta tabelas.
2. **Você (ou seu amigo responsável pelos testes) roda** partidas de observador (só IA) e me devolve o arquivo de log.
3. **Eu analiso** e proponho ajustes de número e de design.

**Faixas-alvo iniciais** (hipóteses para a IA, a validar 🧪):

| Pergunta | Meta |
|---|---|
| Quanto dura a guerra? | Termina entre 1915 e 1920 na maior parte das partidas |
| Alguém colapsa em menos de 6 meses de guerra? | Raramente, só com erro grave |
| Resultado em 20 partidas automáticas | Nem todas iguais: Entente, Potências Centrais e empate/paz negociada todos aparecem |
| França cai antes de 1915? | Pouco frequente; possível se a Alemanha executar bem |
| Rússia sai da guerra por crise? | Possível, mas não automático |

As partidas da IA detectam **padrões**. Equilíbrio entre jogadores exige **testes humanos** alternando lados. Não vou impor 50% de vitória; o objetivo é "todos têm caminho de vitória e de derrota".

---

## 10. Decisões que preciso de você

1. **Posso criar o ponto de salvamento no Git (Fase 0)?** Só faço commit se você autorizar.
2. **Ordem das árvores (Fase 5):** concorda com Reino Unido primeiro, Rússia em segundo?
3. **Testes em jogo:** quem roda as partidas de observador e envia o log?
4. **Cenário de 1914:** deixar para depois da campanha principal estar estável (recomendado)?

---

## 11. Riscos

- **Memória do computador crítica** nesta sessão: fases pesadas (testes, builds) devem rodar uma de cada vez.
- **Vários chats mexendo nos mesmos arquivos**: risco de sobrescrever. Resolve com a Fase 0.
- **Arte** é muito volumosa; a prioridade é o que o jogador vê sempre.
- **Promessa de conteúdo sem mecânica** é o erro que mais se repete. Regra do plano: nenhuma árvore avança sem contrato de foco e teste.
- **DLCs**: toda mecânica de DLC precisa de caminho alternativo.
