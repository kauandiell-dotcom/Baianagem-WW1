# Baianagem WW1 — Análise profunda e plano de reestruturação: Alemanha e Rússia

Nada foi alterado no mod. Esta análise vem de varreduras automáticas nos arquivos (contagens, buscas de referência, somas de bônus). Não vem de partidas: eu não consigo rodar o HOI4.

## 0. O que esta análise NÃO prova

- Os números de bônus são **tetos teóricos**: somam todos os ramos, mesmo os que o jogador nunca pega junto.
- Uma "bandeira nunca lida" ou "ideia nunca usada" é **candidata** a problema. Ela pode ser lida por interface (GUI) ou por sintaxe rara que minha busca não pegou. Cada item marcado assim será reconferido antes de ser mexido.
- Li por inteiro só os 12 eventos da Rússia, o motor de crise e alguns focos. Os 85 eventos da Alemanha foram medidos (opções, imagens, textos), não lidos um a um.
- Equilíbrio, IA e aparência só se provam com partidas.

## 1. Estado real

| | Alemanha | Rússia (tag SOV) |
|---|---|---|
| Focos | 207 (todos com recompensa) | 235 (todos com recompensa) |
| Eventos próprios | 85 | 12 |
| Decisões próprias | 24 (+ 14 de uma categoria compartilhada) | 1 (+ 7 compartilhadas) |
| Ideias (espíritos) | 86 | 80 |
| Focos com data de liberação | 17 | 6 (todos de aviação ou fuzil) |
| Focos com peso de IA (`ai_will_do`) | 207 (quase todos entre 85 e 100) | 0 |
| Pares de focos excludentes | 13 | 4 (Stolypin e Bjorkö x Brest) |
| Última revisão de verdade | 04/10 (correção de crash) | 01/10 (reconstrução da árvore) |

Nenhuma das duas passou por um trabalho como o da Áustria e do Reino Unido.

## 2. Problemas que valem para as duas

**T1. Nada acontece sozinho.** Os 97 eventos das duas (85 + 12) só disparam quando um foco os chama. Só 1 evento alemão tem condição de data. Nenhum tem disparo por tempo médio. Sem o jogador clicar o foco, a Revolução de Fevereiro, o motim de Kiel e a Revolução Alemã nunca ocorrem.

**T2. A IA joga às cegas.**
- Alemanha: todos os focos têm peso quase igual (81 focos em 90, 64 em 95, 25 em 85) e nenhum tem condição. "Abdicação do Kaiser em Amerongen" (95), "Proclamar a República Socialista" (95), "Revolução Proletária Mundial" (95) e "Motim de Kiel" (90) pesam o mesmo que os focos de guerra. Hipótese: a IA alemã se derruba sozinha assim que as portas se abrem.
- Rússia: nenhum foco tem peso. A IA escolhe sem direção histórica.
- O mod inteiro tem 1 arquivo de estratégia de IA e ele não cita Alemanha nem Rússia.

**T3. Escolhas de mentira (bandeiras que não mudam nada).**
- Alemanha: 33 das 89 bandeiras nunca são lidas. Entre elas: Schlieffen deu certo ou falhou, cheque em branco, neutralidade belga respeitada, promessa de Sussex, Resolução de Paz do Reichstag aprovada ou rejeitada, aliança de Björkö formada, Brest concluído.
- Rússia: 22 das 53. Entre elas estão **todas as bandeiras do caminho revolucionário**: fevereiro em curso, abdicação, Kerensky no poder, caminho bolchevique, caminho Kornilov, caminho tsarista, governo provisório aberto. O evento do Caso Kornilov (duas opções) não muda nada no jogo.

**T4. Política inicial sem oposição.** As duas começam com 100% de popularidade "neutralidade". Não há SPD nem Reichstag de oposição na Alemanha. Não há SR, Kadets nem bolcheviques na Rússia. Agitação social não pode nascer de popularidade. Depois o foco troca o regime de uma vez (`set_politics`).

**T5. Ideias definidas e nunca usadas (candidatas).**
- Alemanha: 28 de 86. Exemplos: `GER_turnip_winter_crisis`, `GER_schlieffen_plan_failed`, `GER_skagerrak_naval_victory`, `GER_bruchmueller_artillery`.
- Rússia: 11 de 80. Exemplos: `SOV_shell_shortage_crisis`, `SOV_agrarian_collapse`, `SOV_dictatorship_of_the_proletariat`, `SOV_divine_autocracy`.

**T6. Qualidade dos eventos.**
- Alemanha: 72 dos 85 têm zero ou uma opção (ler e clicar). 54 usam só 5 imagens genéricas: `german_troops` ×15, `german_speech` ×12, `dead_soldiers` ×12, `generic_conference` ×9, `generic_strike` ×6. Isso contraria a regra de nada de GFX repetido.
- Eventos de "profundidade" (`side_ww1_ger_rus`, 26 eventos): 16 têm opção vazia, 19 não têm escolha, e 14 chaves de texto faltam em inglês e português (eventos 50, 52, 55). O jogador verá a chave crua na tela.
- Rússia: 9 dos 12 sem escolha, 2 totalmente vazios (`ww1_russia.101` e `.102`), `generic_parliament` repetida 4 vezes.
- Nenhum evento tem imagem inexistente.

**T7. Restos da Segunda Guerra.**
- O histórico da Rússia liga cerca de 60 variáveis de cartazes de propaganda stalinista e do sistema de "paranoia" da Grande Purga. Nada do mod as usa. Duas bandeiras `SOV_paranoia_*` são lidas e nunca definidas.
- A tag `RUS` é o "Reichskommissariat Nordamerika". O foco alemão de Brest e os eventos do Leste checam `country_exists = RUS`, que é uma condição morta.
- Existem arquivos mortos: `SOV_1936.txt` (48 KB), `SOV_night_witches*`, `soviet.txt.disabled` (44 KB), `GER_German_Civil_War_*`.
- `SOV_democratic` chama-se "Russian Federation", mas em 1917 é "República Russa". Dois textos alemães (`GER_democratic_*`) estão no arquivo de ideias da Rússia.

**T8. Textos dos focos.** Nenhum dos 207 focos alemães nem dos 235 russos diz o que faz. A Áustria e o Reino Unido já dizem. 23 descrições alemãs (inglês) e 31 (português) têm menos de 120 caracteres.

**T9. O motor de crise existe, mas não tem desfecho.** O arquivo `ww1_society_effects.txt` conta semanas de guerra e pressão. A partir de 25 semanas de guerra com uma grande potência e 3 de pressão, dispara a "crise" (`ww1_crisis.1` Alemanha, `.4` Rússia). Ela coloca 3 níveis de penalidade (Rússia: -25% de estabilidade e -30% de fábricas no nível 3) e recupera depois. Mas a crise é **uma escada de penalidades que se cura sozinha**. Nunca vira revolução, queda do governo, guerra civil ou paz separada. É o mesmo código copiado para todos os países, com outro nome.

## 3. Alemanha

**G1. Datas históricas erradas ou ausentes.** Só 17 focos têm data. Exemplos:
- Tratado de Brest libera em 01/01/1915 (histórico: março de 1918), condicionado só a estar em guerra com a Rússia.
- Operação Michael libera em 1916 (histórico: março de 1918).
- Verdun libera em 1915 (histórico: fevereiro de 1916).
- Motim de Kiel libera em 1917 (histórico: outubro e novembro de 1918).

**G2. Ícones repetidos e de outros países (contra a regra do mod).**
- 207 focos usam só 170 ícones. `GFX_focus_German_Crown` serve 4 focos; `military_dictatorship`, `attack_germany`, `German_Pilots` e `auftragstaktik` servem 3 cada.
- Há ícones de outros países ou de 1940: `GFX_SOV_two_red_flags`, `GFX_ENG_special_american_relationship`, `GFX_FRA_attaque__outrance`, `GFX_focus_BEL_eben_emael_fortress`, `GFX_focus_AUS_the_matzen_oil_fields`, `GFX_TUR_secret_treaty_with_germany`, `GFX_focus_GER_strike_eastward`, `GFX_focus_GER_ostwall`.
- 2 ícones também aparecem nas árvores genéricas.
- A Rússia não tem esse problema: 235 ícones, todos únicos.

**G3. Empilhamento de bônus (teto teórico, ignorando exclusões).**
- Das ideias dadas por foco, 18 de 20 nunca são removidas.
- Somadas: estabilidade +65%, apoio à guerra +45%, capacidade industrial +30%, ganho de poder político +25%, moral +15%, conscrição +10%.
- 13 das 20 ideias de foco não têm nenhum modificador negativo nos campos principais.
- Nos focos em si: apoio à guerra +5,58 contra -0,70 (8 para 1), estabilidade +3,28 contra -1,70, poder político +5.445 contra -80.
- Ideias de maior peso individual: `GER_siegfrieden_hegemony` (+15% guerra e +15% fábricas), `GER_stab_in_the_back_myth` (+15% guerra), `GER_volkskaiserreich_constitution` (+15% estabilidade), `GER_red_guards_militia` (+15% moral).
- Contenção: só 13 pares de focos são excludentes. Mão de obra total 425 mil, o maior foco dá 120 mil. Armazém e divisões: nenhum `create_unit`.
- Onde o equilíbrio quebra (hipótese): a estabilidade e o apoio à guerra sobem sem teto, o que elimina o efeito da "crise do nabo" e da fome do bloqueio.

**G4. Revolução Alemã só por foco.** Existem Spartakusbund, Kiel, agitação no Ruhr e um evento de guerra civil (`ww1_germany_events.51`, o único `start_civil_war` do mod). Todos são chamados por foco, nenhum tem condição. Na IA, isso cai no problema T2.

**G5. Começo.** Estabilidade 0,70 a 0,75, apoio à guerra 0,30, 5 ideias iniciais e 100% neutralidade.

**G6. OOB.** O arquivo chama-se `GER_1936_generic`, mas o conteúdo é de 1911 (Kaiserliche Garde-Division, Jäger). É nome enganoso, não bug. Tem 42 divisões, o mesmo número da Rússia (talvez placeholder). A marinha de 1911 tem 102 navios.

## 4. Rússia

**R1. A Revolução não acontece sozinha e pode vir cedo demais.** A corrente é Rasputin, Motins do Pão, Motim de Petrogrado, Abdicação em Pskov, Governo Provisório. Cada foco custa 5 semanas, não tem data, condição de guerra nem de estabilidade. Um jogador (ou a IA) pode abdicar o Tsar em 1912. Também pode nunca fazê-lo e permanecer imperador até 1924.

**R2. Ramos não são excludentes (confirmar na implementação).** Só há 4 pares excludentes em 235 focos e nenhum entre os regimes. Quatro `set_politics` existem (democrático, comunista, fascista do Kornilov, democrático de novo). Pelos dados do arquivo, todos podem ser pegos em sequência, trocando o regime várias vezes.

**R3. Não há guerra civil.** Nenhum `start_civil_war`, `declare_war_on`, `create_wargoal`, `release`, `transfer_state`, `create_faction` nos 235 focos. Existem focos chamados "Criação do Exército Vermelho" e "Esmagar os Exércitos Brancos", mas sem Brancos e Vermelhos como lados.

**R4. O Império não se desfaz.** A Rússia começa com **192 estados**, incluindo Finlândia, Polônia, Bálticos, Ucrânia e Cáucaso. As tags FIN, POL, UKR, LAT, LIT, EST, GEO, ARM e AZR existem com arquivos de história, mas **possuem 0 estados** e **nenhum script as libera**. A independência de 1917-1918 é impossível.

**R5. Brest-Litovsk existe, mas isolado.** Há um sistema compartilhado (`zz_ww1_eastern_settlement.txt`) em que as duas partes negociam e só se concedem distritos já ocupados. O foco russo acrescenta um espírito "Humilhação de Brest" e -15% de estabilidade. Não está ligado à revolução nem cria Estados-satélite.

**R6. Poucos eventos e sem datas.** 12 eventos para 235 focos (1 a cada 20). Faltam: greve de Lena (1912), Quarta Duma, caso Beilis (1913), Grande Retirada (1915), Bloco Progressista (agosto de 1915), Tsar assume o comando (setembro de 1915), assassinato de Rasputin (dezembro de 1916), Soviete de Petrogrado, Teses de Abril, Dias de Julho, Outubro, dissolução da Assembleia Constituinte (janeiro de 1918), Legião Tcheca, intervenção aliada, Kronstadt (1921), formação da URSS (1922).

**R7. Balanceamento invertido.**
- O "império instável" é o país mais premiado. Somando os focos: estabilidade +5,92 contra -1,25, poder político +6.550 contra -75, mão de obra 2.085.000 (cinco vezes a da Alemanha; focos de 250 mil, 150 mil, 150 mil, 150 mil).
- Ideias (teto teórico): estabilidade +175%, ganho de poder político +110%, apoio à guerra +75%, conscrição +35%. 22 de 45 ideias de foco sem custo.
- 4 `create_unit` (divisões de graça) e 21 `add_equipment_to_stockpile` (sinal e quantidade não verificados). As regras da Áustria proíbem os dois.
- Espíritos de maior peso: `SOV_absolute_autocracy_triumphant` (+25% poder político), `SOV_triumph_of_pan_slavism` (+20% guerra, +15% estabilidade), `SOV_unbreakable_union_victory` (+15% em três campos).

**R8. Decisões quase inexistentes.** Uma decisão própria (`SOV_southwestern_front`, custo 1). Nada sobre Duma, greves, requisições, deserção, fome, zemstvos ou Rasputin.

**R9. Sem motor próprio de instabilidade.** A Áustria tem consentimento, coesão e provisões. A Rússia não tem equivalente: nem lealdade do exército, nem fome, nem agitação operária, nem prestígio do Tsar. Só a escada genérica de "fome de fuzil".

## 5. Plano, em fatias (uma de cada vez, por causa da memória)

**Regras herdadas da Áustria e do Reino Unido:** ganhos pequenos e sempre com custo; nada de divisões, equipamento nem mão de obra grátis; todo conteúdo novo com imagem única (da Workshop, com origem registrada) e texto em inglês e português; testes de estrutura e validação de textos no fim de cada fatia. Preservo IDs, estrutura e gráficos das árvores.

### Fase 0 — Limpeza e segurança (leve)
1. Teste de codificação (BOM) cobrindo os arquivos da Alemanha e da Rússia.
2. Remover o lixo da Segunda Guerra: variáveis de propaganda e paranoia do histórico da Rússia, flags `SOV_paranoia_*`, trocar `RUS` por SOV nas condições, apagar arquivos mortos (`.disabled` e OOB 1936 não usados), conferindo que nada os lê.
3. Corrigir textos faltantes do `side_ww1_ger_rus` (14 chaves) e os 2 textos alemães fora do lugar.
4. Renomear "Russian Federation" para "República Russa".

### Fase 1 — Rússia: o motor do império instável (jogabilidade)
1. Criar variáveis próprias: lealdade do exército, fome, agitação operária, prestígio do Tsar, legitimidade. Sobem e descem por evento, decisão e situação da guerra (não só por foco).
2. Dar à Rússia popularidades iniciais realistas (conservadores, liberais, SR, bolcheviques), para o regime mudar por pressão, não só por clique.
3. Ligar o motor de crise a um **desfecho real**: no nível 3 por tempo suficiente, a revolução dispara.

### Fase 2 — Rússia: Revolução automática e com ramos excludentes
1. Revolução de Fevereiro como cadeia de eventos com data mínima e condições (guerra, fome, lealdade). O jogador pode adiar com custo, mas não impedir de graça.
2. Ramos excludentes: Governo Provisório, Bolcheviques, Kornilov e Restauração tsarista. Fazer as bandeiras mortas do caminho revolucionário finalmente controlarem algo.
3. Pesos de IA históricos (nenhum foco revolucionário antes de a situação permitir).

### Fase 3 — Rússia: Guerra civil e fim do Império
1. Liberar Finlândia, Polônia, Bálticos, Ucrânia e Cáucaso por evento, com data e condição, usando as tags já existentes.
2. Guerra civil Brancos x Vermelhos (ou tag nova) e ligação com o acordo de Brest já existente.
3. Decisões de guerra civil e pós-guerra.

### Fase 4 — Rússia: conteúdo e equilíbrio
1. De 12 para cerca de 50 eventos (lista da seção R6), decisões recorrentes (Duma, requisições, greves, fome, deserção) e espíritos temporários.
2. Preencher `ww1_russia.101`, `.102`, `.100` e `.103`.
3. Reequilibrar: teto de mão de obra por ramo, trocar as 4 divisões de graça por mão de obra com custo, conferir o equipamento dos 21 estoques, dar custo às ideias sem custo e definir tetos de estabilidade e poder político.
4. Texto de efeito em todas as descrições de focos.

### Fase 5 — Alemanha: a IA e a história
1. Pesos de IA com condições (nenhum foco de revolução, abdicação ou república antes de a situação de guerra permitir).
2. Datas históricas corrigidas nos focos (Brest, Michael, Verdun, Kiel, abdicação).
3. Bandeiras mortas (33) passam a mudar algo; ideias mortas (28) recebem gatilho ou são removidas.

### Fase 6 — Alemanha: vida própria e revolução
1. Eventos por data e por condição: eleições do Reichstag de 1912, Zabern (1913), fome do bloqueio e inverno do nabo (1916-1917), Programa Hindenburg, Kiel, Ebert, Weimar.
2. Revolução Alemã automática sob condição (guerra perdida, fome, apoio à guerra baixo), com o `start_civil_war` já existente.
3. SPD e oposição com popularidade inicial realista.

### Fase 7 — Alemanha: qualidade e equilíbrio
1. Dar escolhas aos 72 eventos sem escolha (começando pelos mais marcantes).
2. Trocar as 5 imagens genéricas usadas em 54 eventos por imagens únicas, e os 37 ícones repetidos ou de outros países.
3. Equilibrar: tetos de apoio à guerra, estabilidade e poder político; custos para as 13 ideias sem custo.
4. Textos de efeito nas descrições.

### Fase 8 — Integração e fechamento
1. Cadeias entre Alemanha, Rússia, Áustria e Reino Unido: Björkö, ultimato de 1914, Brest, armistício.
2. Registros de partidas de IA para você ou seu amigo rodarem e me devolverem.
3. Testes de estrutura e validação de textos; 0 erros nos arquivos que mexi. Os 1.656 erros antigos de texto nas árvores genéricas são de fora deste escopo e continuam separados.

## 6. Suposições que declaro
- Um foco por vez e 7 dias por ponto de custo (o mod não redefine `FOCUS_POINT_DAYS`). O jogo vai de 01/06/1911 a 01/01/1924, cerca de 657 semanas. Os custos somam 1.407 semanas (Alemanha) e 1.847 (Rússia), ou seja, o jogador vê cerca de 35 a 45% de cada árvore. Isso reduz o risco real de empilhar tudo.
- Datas, nomes e valores novos são palpites meus até haver partidas.
- Novos IDs usarão os prefixos já existentes (`ww1_russia.*`, `ww1_germany_events.*`) a partir de 200, sem reaproveitar números.
- Não haverá commit sem sua autorização.
