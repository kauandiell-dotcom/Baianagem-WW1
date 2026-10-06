# PROMPT 2 — MISSÃO: FOCUS TREE COMPLETA DA ITÁLIA (ITA) — Baianagem WW1

> Cole isto DEPOIS do PROMPT 1 (ou com o PROMPT 1 salvo como regra do workspace).
> Repositório: `C:\Users\Usuário\Pictures\Baianagem-WW1` — mod em `WW1/` — HOI4 1.19.3 — jogo em `E:\SteamLibrary\steamapps\common\Hearts of Iron IV`.
> Execute tudo dentro de `WW1/` salvo quando dito o contrário.

---

## 1. Missão

Construir a **árvore de focos da Itália (tag `ITA`) completa, jogável e balanceada**, com 200 focos, no mesmo nível de acabamento que já foram feitos a **Áustria-Hungria** e o **Reino Unido**: efeitos reais, eventos, decisões, ideias/espíritos, medidores próprios, imagens (GFX) únicas e textos em **inglês e português do Brasil** em TUDO.

Você tem liberdade de design. Você NÃO tem liberdade de entregar raso. O critério de pronto é numérico (seção 9).

**O usuário NÃO quer scriptar guerra com a Líbia.** A Líbia começa com os otomanos (seção 4).

---

## 2. Comece verificando o disco (não confie neste texto)

Faça o PORTÃO DE ENTENDIMENTO do PROMPT 1 e registre em `WW1/docs/italy_progress.md`. Estes são os fatos que eu encontrei; **confirme cada um por comando** e corrija o que mudou:

1. `common/national_focus/italy.txt` tem **67 bytes** e só diz "intentionally empty; every country uses generic_focus". **A Itália NÃO tem árvore nenhuma hoje.** `italy.txt.disabled` (45 KB) é o arquivo do jogo base: **ignore**, não é ponto de partida.
2. O que existe é só o **esboço estrutural** `docs/italy_focus_outline.txt`: 200 linhas no formato `asa | id (sem o prefixo ITA_ww1_) | ano | pais | excludentes | título EN | título PT-BR`.
   - Asas: `pol` 45, `eco` 35, `dip` 40, `mil` 55, `war` 25.
   - Validação: `python -B -X utf8 scripts/check_italy_outline.py` (hoje dá `RESULT: OK`, 200 ids únicos). **Esse esboço não tem nenhum efeito, evento, decisão, ícone nem texto de corpo.**
3. `history/countries/ITA - Italy.txt`: capital Roma, estabilidade 0.6, OOB `ITA_1936_generic` (verifique se é adequado a 1911), 5 ideias iniciais (`ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, `ITA_southern_question_gap`, `ITA_sacro_egoismo_policy`) definidas em `common/ideas/ww1_national_modifiers.txt`. Isso tem que continuar funcionando.
4. Estados da Líbia (`history/states/448-Tripoli`, `449-Libyan Coast`, `450-Benghasi`, `451-Derna`, `661-Tripolitania`, `662-Sirte`, `663-Cyrenaica`, `1095-Southern Cyrenaica`, e possivelmente `273-Italian Africa`) estão com `owner = ITA`. Confirme olhando os nomes de estado e o mapa.
5. Já existe muita arte de personagens italianos: `gfx/interface/ideas/idea_ITA_*.dds` (Giolitti, Salandra, Nitti, D'Annunzio, Gramsci, Diaz, Duca degli Abruzzi...), retratos em `gfx/hoi4tgw_portraits/ITA/` e `common/characters/ITA.txt`. **Reaproveite para ministros/conselheiros**, respeitando "sem repetição dentro do mod".
6. Outros países já **mandam eventos para a Itália ou deixam marcas (flags) esperando a árvore italiana**: o Reino Unido (ofertas de Londres: Trentino, Trieste, Dalmácia; ouvir ou recusar fica em flags; escolta no Mediterrâneo), a Áustria (contingência italiana, minorias italianas, renovação da Tríplice Aliança, `give_guarantee = ITA`), a França (entrada da Itália). **Faça um `grep` por `ITA` e `tag = ITA` em `events/`, `common/decisions/`, `common/scripted_effects/`, `history/` e liste TODOS os ganchos** em `italy_progress.md`. Cada um precisa ter resposta/efeito na Itália. Esta é a parte mais importante da integração.
7. Modelos (LEIA antes de escrever qualquer coisa):
   - **Áustria-Hungria:** `scripts/build_ww1_austria_hungary.py`, `auh_country_support.py`, `auh_focus_effects.py`, `auh_content_extra.py`, `build_auh_extra_art.py`, `tests/test_ww1_austria_hungary.py` (contém os TETOS DE EQUILÍBRIO), `common/national_focus/austria.txt`.
   - **Reino Unido:** `scripts/build_ww1_britain_*.py` e `britain_*_data.py` (dados por asa), `build_britain_art.py`, `tests/test_ww1_britain_*.py`, `common/national_focus/uk.txt` (tem `shortcut`, `focus_tree` com `country = { factor = 0 modifier = { add = 100 original_tag = ENG } }`, `default = no`).
   - **Alemanha/Rússia:** `scripts/relayout_wings.py`, `build_ger_rus_content.py`, `tests/test_ww1_ger_rus.py` (regras de layout e IA).
   - Layout de asas: `scripts/focus_layout.py`, `relayout_wings.py`.
   - Escalada/entrada na guerra: `tests/test_ww1_escalation.py` e o sistema que ele testa. **Descubra como os países entram na guerra neste mod e use o mesmo mecanismo.** Não invente um sistema paralelo.
8. Localização: siga o nome de arquivos da Áustria (`localisation/english/ww1_austria_hungary_l_english.yml` e o par em `braz_por`; confirme na pasta). `.yml` com BOM; scripts sem BOM.
9. Rode e **guarde a contagem** de `validate_ww1_foundation.py ... --content` ANTES de mexer (linha de base).

---

## 3. Arquitetura (gerador + dados, como na Áustria e no Reino Unido)

Nunca escreva à mão os arquivos finais. Crie:

```
scripts/ita_politics_data.py      scripts/ita_economy_data.py
scripts/ita_diplomacy_data.py     scripts/ita_military_data.py
scripts/ita_war_data.py           (dados dos focos, eventos, decisões, ideias por asa)
scripts/build_ww1_italy.py        (único construtor; roda tudo e é determinístico)
scripts/build_ita_art.py          (arte: importa, converte, valida duplicata, registra proveniência)
scripts/italy_audit.py            (painel de números; falha se faltar algo)
tests/test_ww1_italy.py           (escreva PRIMEIRO)
docs/italy_progress.md            (sua memória)
docs/ita_art_bindings.json        (proveniência das imagens)
```

Saídas do construtor (nomes seguindo o padrão do projeto):
- `common/national_focus/italy.txt` (substitui o stub; `focus_tree = { id = ITA_ww1_1911_1923 default = no country = {...original_tag = ITA} shortcut... }`)
- `events/ww1_italy_*.txt`, `common/decisions/ww1_italy_*.txt` (+ `common/decisions/categories/`), `common/ideas/ww1_italy_ideas.txt`, `common/scripted_effects/ww1_italy_effects.txt`, `common/on_actions/` (`on_weekly_ITA`, `on_startup` se precisar), `common/opinion_modifiers/ww1_italy_*.txt`
- `interface/ww1_italy_*.gfx`, `gfx/interface/goals/ww1_italy/`, `gfx/event_pictures/ww1_italy/`, `gfx/interface/ideas/ww1_italy/`, `gfx/interface/decisions/ww1_italy/`
- `localisation/english/...` e `localisation/braz_por/...`

Rode o construtor duas vezes: a segunda não pode gerar diferença (determinismo).

Prefixo dos ids: focos `ITA_ww1_<id_do_esboço>`, eventos `ww1_italy.N`, ícones `GFX_goal_ww1_ITA_ww1_<id>` (confirme o padrão exato copiando `ENG_`).

---

## 4. Decisão já tomada: Líbia otomana, sem guerra

1. Transfira os estados da Líbia para `owner = TUR` com `add_core_of = TUR` (mantendo o core `LBA` que já existe). Remova cores italianos neles, se houver. Ajuste guarnições/OOB da Turquia e da Itália se o jogo reclamar.
2. **Não crie nenhuma guerra ítalo-turca.** A Itália pode receber a Líbia por **via diplomática** controlada por eventos (sem guerra). Sugestão de desenho (ajuste à vontade):
   - Foco italiano "pressionar a questão de Trípoli" libera uma cadeia de eventos entre ITA e TUR.
   - Evento para TUR (jogador ou IA): aceitar um acordo (reconhecer soberania italiana sobre Líbia; em troca, TUR recebe dívida aliviada/benefício; a Itália recebe o Dodecaneso como penhor) ou recusar (tensão, opinião cai, fecha a via diplomática por um tempo).
   - `ai_chance` da Turquia AI deve favorecer aceitar a partir da data da Primeira Guerra dos Bálcãs (outubro de 1912) e ser bem baixa antes.
   - Se a Itália nunca pegar o foco, a Líbia simplesmente continua otomana. Está tudo bem.
3. **Dodecaneso (estado 164):** ponha com a Turquia também, dentro do mesmo pacote diplomático. **Esta é uma suposição minha**; registre e diga ao usuário no relatório.
4. No esboço, o foco `eco|libya_colonisation` ("Colonizar a Quarta Margem") pressupõe Líbia italiana. **Redesenhe-o** para só liberar depois do acordo (`has_country_flag` ou posse de estado), ou troque por outro foco. Mantenha o total de 200.
5. Atenção à interação com a Turquia e o Reino Unido/França (eventos existentes que mencionam Líbia): `grep -ri "libya\|tripol\|cyrenaic" events common history` e corrija inconsistências.

---

## 5. Regras de design da árvore

- **Preserve os 200 ids e a lógica de dependência do esboço** (`docs/italy_focus_outline.txt`). Pode trocar título, ano e pai se encontrar erro histórico ou de layout, e pode redesenhar `libya_colonisation`. Se mudar algo, registre em `italy_progress.md` e atualize o esboço (o `check_italy_outline.py` tem que continuar `OK`).
- **Layout:** 5 asas, cada uma começando numa raiz; a árvore abre na asa política; `shortcut` por asa; molde visual da Áustria/Reino Unido/França. Use `scripts/focus_layout.py`/`relayout_wings.py`. Regras testadas: fila reta ≤ 4, cruzamentos ≤ 3, altura ≤ 26, filho sempre abaixo do pai.
- **Datas:** `available = { date > ... }` com o ano REAL de cada fato. Exemplos: Pacto Gentiloni 1913; Semana Vermelha jun. 1914; neutralidade ago. 1914; Tratado de Londres abr. 1915; "Maio Radiante" maio 1915; guerra à Áustria 23 mai. 1915; Caporetto out. 1917; Vittorio Veneto/Villa Giusti out.–nov. 1918; Fiume (D'Annunzio) set. 1919; Tratado de Rapallo nov. 1920; Biênio Vermelho 1919–20; Marcha sobre Roma out. 1922.
- **Custo de foco:** copie a escala do Reino Unido/Áustria (não invente escala).
- **Excludentes** reais e simétricos (os do esboço: `interventionist_press`×`neutralist_coalition`; `liberal_restoration`×`nationalist_order`×`socialist_turn`; `tariff_protection`×`free_trade_opening`; etc.). Cada desfecho muda eventos, medidores e finais.
- **IA (`ai_will_do`) em TODO foco:** a IA italiana deve seguir a história: neutra até 1915, entrar ao lado da Entente, ter o Biênio Vermelho e a crise liberal. Focos de revolução/ruptura (`socialist_turn`, `march_on_rome`, etc.) com peso 0 e só abrem pelo evento. **Nada de todos os focos com peso 85–100** (foi o erro da Alemanha).

---

## 6. Mecânica própria da Itália (medidores internos)

Crie 4–5 variáveis do país, com `clamp`, atualização semanal em `on_weekly_ITA` e consequência visível (espírito em 3 níveis, evento, decisão liberada). Sugestão (ajuste e justifique):

| Medidor | Faixa | O que representa | Sobe com | Desce com | Consequência |
|---|---|---|---|---|---|
| `ita_ww1_interventionism` | 0–100 | peso da opinião pró-guerra x neutralista | imprensa, Quarto, Maio Radiante, ofertas de Londres | neutralismo de Giolitti, perdas | abre/fecha entrada na guerra |
| `ita_ww1_social_tension` | 0–100 | greves, Semana Vermelha, Biênio Vermelho | carestia, perdas, desemprego | reformas, pacto social | eventos de greve, ocupação de fábricas, espírito |
| `ita_ww1_army_morale` | 0–100 | moral do Regio Esercito (Cadorna, Isonzo, Caporetto) | vitórias, suprimentos | ofensivas falhas, disciplina dura | Caporetto, Diaz, espíritos |
| `ita_ww1_southern_gap` | 0–100 | Questão Meridional, emigração | Programa do Mezzogiorno, aqueduto | abandono | economia, migração, remessas |
| `ita_ww1_irredentism` | 0–100 | Terre Irredente, Trentino/Trieste/Dalmácia | propaganda, Londres | derrota, concessões | pressão para entrar na guerra e por Fiume/"vitória mutilada" |

---

## 7. Integração com os outros países (obrigatória)

Use a lista de ganchos do passo 2.6. No mínimo:
- **Tríplice Aliança:** a Itália pode honrar, ficar neutra (histórico, 1914) ou trocar de lado (Tratado de Londres, 1915). Responda aos eventos da Áustria e da Alemanha.
- **Ofertas de Londres (Reino Unido):** leia as flags que o Reino Unido já grava e dê efeito real (Trentino, Trieste, Dalmácia; "Vitória Mutilada" se a promessa não for cumprida).
- **França:** entrada da Itália, frente Alpina, cooperação naval no Mediterrâneo (o Reino Unido já oferece escolta a Itália: aceite/recuse com efeitos).
- **Áustria:** frente do Isonzo, minorias italianas, Caporetto (impacta a Áustria também: evento recíproco), Vittorio Veneto.
- **Turquia:** cadeia da Líbia (seção 4).
- **Eventos para outros países:** pelo menos 6 eventos novos que a Itália MANDA para terceiros (Alemanha, Áustria, Reino Unido, França, Turquia, Sérvia/Grécia), com `ai_chance` e consequência.
- **Jamais quebre** o comportamento dos outros países. Se precisar alterar um arquivo deles, mude o mínimo e rode os testes deles.

---

## 8. Fatias de trabalho (cada uma vertical e completa; não pule portões)

**Fatia 0 — Reconhecimento e ferramentas**
- Portão de entendimento (PROMPT 1 §1), lista de ganchos, linha de base dos erros, resolução da Líbia nos estados.
- Escreva `tests/test_ww1_italy.py` e `scripts/italy_audit.py` **primeiro**, com todos os tetos/metas das seções 5 e 9. Eles devem falhar hoje (prova de que medem algo).
- Esqueleto do construtor que já gera uma árvore de 200 focos válida (estrutura, ids, posições, ícones provisórios NÃO entram no commit).

**Fatia 1 — Asa Política e Sociedade (`pol`, 45 focos) + medidores**
Giolitti, sufrágio, Pacto Gentiloni, Semana Vermelha, intervencionismo x neutralismo, Maio Radiante, gabinetes Boselli/Orlando, Vitória Mutilada, Biênio Vermelho, ramos liberal/nacionalista/socialista, Marcha sobre Roma. Medidores, espíritos em 3 níveis, eventos por data, decisões.

**Fatia 2 — Asa Diplomacia e Alinhamento (`dip`, 40 focos)**
A mais importante para o jogo: Tríplice Aliança, neutralidade, Tratado de Londres, entrada na guerra (via o sistema de escalada do mod), Libya/Ouchy (seção 4), Fiume, Rapallo. Todas as integrações da seção 7.

**Fatia 3 — Asa Campanhas e Pós-guerra (`war`, 25 focos)**
Isonzo, Caporetto, Piave, Vittorio Veneto, armistício, desmobilização, veteranos.

**Fatia 4 — Asa Forças Armadas (`mil`, 55 focos)**
Exército (Cadorna/Diaz, alpini, artilharia de montanha), Marinha (Regia Marina, Mediterrâneo, MAS, dreadnoughts), aviação (Caproni), tecnologia. Sem divisões/equipamento de graça. Reaproveite o sistema de projetos/decisões que o Reino Unido e a Áustria usam.

**Fatia 5 — Asa Economia e Mezzogiorno (`eco`, 35 focos)**
Triângulo industrial, Ansaldo/FIAT/Ilva, hidrelétricas, Mezzogiorno, mobilização industrial, empréstimos de guerra, carvão britânico (dependência real de `ITA_coal_iron_scarcity`), reconstrução. Fábricas via decisão/ocupação de capacidade civil como no Reino Unido.

**Fatia 6 — Fechamento**
Passe final de arte (zero repetição em todo o mod), equilíbrio total (tabela de somas), checklist visual completo (PROMPT 1 §7), autocrítica global, relatório final.

> A cada fatia: ciclo PLANEJAR → CONSTRUIR → VERIFICAR → CRITICAR → CORRIGIR → REGISTRAR, com commit da fatia. **Imagens e textos fazem parte da fatia**, não ficam para o fim.

---

## 9. Critério de pronto (metas mínimas; o audit tem que mostrar isto)

| Item | Meta mínima |
|---|---|
| Focos | 200, todos com efeito real, descrição que diz o efeito (EN e PT) |
| Eventos novos | ≥ 70 (dos quais ≥ 35 disparam sem o jogador clicar foco: data, limiar, MTTH, on_action) |
| Eventos | todos com ≥ 2 opções, cada opção com efeito e custo; cada um com imagem única 450×250 |
| Decisões | ≥ 24, em ≥ 4 categorias, com custo, limite e `cancel_effect` quando ocupam fábrica |
| Ideias/espíritos novos | ≥ 24 (≥ 6 instituições permanentes, resto temporárias por medidor/evento) |
| Medidores | 4–5, com clamp, atualização semanal e consequência visível |
| Modificadores de opinião | ≥ 6 |
| Eventos enviados a terceiros | ≥ 6 |
| Ganchos existentes | 100% atendidos (lista do passo 2.6) |
| Ícones de foco | 200 únicos, com `_shine` |
| Imagens de evento / ícones de ideia / de decisão | únicos, 100% dos itens, proveniência registrada |
| Flags e variáveis órfãs | 0 |
| `ai_will_do` | em 100% dos focos, com pesos históricos |
| Localização | 100% EN e PT-BR, sem chave crua, sem PT = EN em frase longa |
| BOM em scripts | 0 (só `.yml` tem) |
| Erros novos no validate (`--content`) | 0 (comparar com a linha de base) |
| Testes `test_ww1_*.py`, `tier1–4`, `check_yaml_syntax` | todos verdes |
| Determinismo do construtor | 2ª execução sem diferença |
| Layout | fila reta ≤ 4, cruzamentos ≤ 3, altura ≤ 26, sem sobreposição; imagem renderizada e OLHADA |
| Tetos de equilíbrio (PROMPT 1 §5) | respeitados, com tabela de somas |

---

## 10. Entrega

1. Tudo commitado no ramo `feat/italy-focus-tree` (um commit por fatia). Não faça push na `main`.
2. `docs/italy_progress.md` atualizado (fatias, suposições, ganchos, linha de base).
3. Relatório final no formato do PROMPT 1 §10, em português simples, com a tabela da seção 9 preenchida com os números do audit.
4. Lista do que **não** foi provado (jogo rodando, equilíbrio, datas, aparência).

**Comece agora pelo portão de entendimento e pela Fatia 0. Não me faça perguntas; decida, registre a suposição e continue até fechar a Fatia 6.**
