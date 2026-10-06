# Progresso e Memória — Árvore de Focos da Itália (ITA) WW1

> Arquivo de persistência e auditoria de engenharia. Não apagar.
> Repositório: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1` — HOI4 1.19.3.

---

## 1. Portão de Entendimento (Slice 0)

### 1.1 O que foi pedido e critério numérico de pronto
Construção da árvore de focos nacional da Itália (`ITA`) completa, balanceada e imersiva para o período 1911–1923 no mod Baianagem WW1.
Critérios de pronto mínimos:
- **Focos:** 200 focos únicos, todos com `completion_reward` real, descrição imediata e contextual em EN e PT-BR, sem sobreposições e com filtros válidos.
- **Eventos novos:** ≥ 70 eventos (dos quais ≥ 35 disparados espontaneamente por data, limiar, MTTH ou `on_action`), todos com ≥ 2 opções com efeito e custo, e fotos 450×250 únicas.
- **Decisões:** ≥ 24 decisões em ≥ 4 categorias, com custo de PP, tempo de remoção e `cancel_effect` para uso industrial.
- **Ideias/espíritos:** ≥ 24 ideias com modificadores válidos da documentação do HOI4 e ícones próprios.
- **Medidores internos:** 5 variáveis (`ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, `ita_ww1_irredentism`) atualizadas semanalmente com clamp (0–100) e impacto mecânico.
- **Modificadores de opinião:** ≥ 6.
- **Eventos enviados a terceiros:** ≥ 6 (impactando Alemanha, Áustria, Reino Unido, França, Turquia, Sérvia/Grécia).
- **Ganchos externos:** 100% dos ganchos já existentes no mod respondidos.
- **Líbia e Dodecaneso:** Líbia e Dodecaneso sob controle e soberania otomana (`TUR`) no início de 1911, transferíveis via cadeia diplomática/Tratado de Ouchy, sem guerra violenta direta obrigatória.
- **Arte:** 200 ícones de foco únicos com variantes `_shine`, imagens de eventos e ícones de ideias sem repetição interna no mod, proveniência registrada em `docs/ita_art_bindings.json`.
- **Localização:** 100% espelhada em inglês (`l_english`) e português do Brasil (`l_braz_por`) com UTF-8 BOM.
- **Zero erros novos:** Linha de base estática rigorosamente mantida (1596 erros / 115 warnings pré-existentes no mod).

### 1.2 Fatos verificados diretamente no disco
1. `common/national_focus/italy.txt`: possui exatamente 67 bytes (stub de comentário informando uso de árvore genérica). Nenhuma árvore existia.
2. `docs/italy_focus_outline.txt`: contém 200 linhas de foco distribuídas em 5 asas (`pol`: 45, `eco`: 35, `dip`: 40, `mil`: 55, `war`: 25). `check_italy_outline.py` retorna `RESULT: OK` com 200 IDs únicos.
3. `history/countries/ITA - Italy.txt`: capital Roma (2), estabilidade inicial 0.6, OOB `ITA_1936_generic` (sem divisões na Líbia), 5 ideias iniciais ativas (`ITA_terre_irredente_dream`, `ITA_alpini_tradition`, `ITA_coal_iron_scarcity`, `ITA_southern_question_gap`, `ITA_sacro_egoismo_policy`) definidas em `common/ideas/ww1_national_modifiers.txt`.
4. Estados líbios (448, 449, 450, 451, 661, 662, 663, 1095, 273) e Dodecaneso (164): transferidos para `owner = TUR`, `add_core_of = TUR`, mantendo cores de `LBA` e `GRE` respectivamente.
5. Personagens e retratos: presentes em `common/characters/ITA.txt`, `gfx/hoi4tgw_portraits/ITA/` e ícones `gfx/interface/ideas/idea_ITA_*.dds` (Giolitti, Salandra, Nitti, Orlando, D'Annunzio, Gramsci, Diaz, Cadorna, Thaon di Revel, etc.).
6. Linha de base do script de validação (`validate_ww1_foundation.py --content`): 1596 erros estáticos e 115 advertências (erros herdados de árvores genéricas e outros países). Nossos scripts devem manter acréscimo 0.
7. Testes unitários do repositório (`test_ww1_*.py`): 134 testes passando com sucesso.

### 1.3 Lista completa de ganchos externos identificados (Integração Obrigatória)
- **Áustria-Hungria (`events/ww1_austria_hungary_events.txt` & `ww1_austria_hungary_extra_events.txt`):**
  - Evento `ww1_auh.39`: Consulta e renovação de acordos ítalo-austríacos enviada para a Itália (`id = ww1_auh.39`). Opção A ativa `auh_ww1_italian_consultation`, `auh_ww1_consultation_authorised` e evento `ww1_auh.48`; Opção B rejeita e dispara `ww1_auh.49`.
  - Decisões `AUH_ww1_italian_consultations` e `AUH_ww1_renew_italian_consultation`.
  - Evento `ww1_auh_extra.109` (renovação da Tríplice Aliança 1912–1913).
  - Garantia inicial em `history/countries/AUS - Austria.txt`: `give_guarantee = ITA`.
  - Frente de batalha: Isonzo e Trentino verificados na Áustria.
- **Reino Unido (`events/ww1_britain_diplomacy_events.txt` & `ww1_britain_navy_events.txt`):**
  - Evento `ww1_britain_dip.11`: Ofertas de Londres para a Itália. Opção A define `ITA_ww1_london_terms_open` e `ENG_ww1_italy_terms_open`; Opção B define `ITA_ww1_london_terms_refused` e `ENG_ww1_italy_terms_refused`.
  - Evento `ww1_britain_nav.12`: Cooperação naval e escoltas britânicas no Mediterrâneo oferecidas à Itália.
- **França (`events/ww1_france_events.txt`):**
  - Evento `ww1_france.220`: Tratado Secreto de Londres enviado à Itália (disparado pelo foco francês `FRA_ww1_treaty_of_london`). Opção A assina o tratado e cria wargoal contra a Áustria (`Trentino & Trieste`); Opção B escolhe estrita neutralidade; Opção C exige possessões francesas. Dispara respostas para a França (`ww1_france.221`, `ww1_france.222`, `ww1_france.223`).
  - Evento `ww1_france.270`: Entente Latina Mediterrânea (proposta de aliança enviada à Itália).
- **Alemanha (`events/ww1_germany_events.txt` & `common/decisions/ww1_germany_decisions.txt`):**
  - Evento `ww1_germany_events.39`: Efeito de choque de Caporetto (`GER_caporetto_momentum` e malus em ITA se existir).
  - Decisão `ger_weltpolitik_bribe_italian_press`: tentativa alemã de influenciar a imprensa e neutralidade italiana.
- **Crise do Isonzo (`common/decisions/ww1_national_decisions.txt`):**
  - Decisões `ITA_relief_step_1`, `ITA_relief_step_2`, `ITA_relief_step_3` já programadas para lidar com atrito de guerra se `ITA_crisis_active` estiver ativo.
- **Inscrição de Espíritos (`common/scripted_effects/zz_ww1_national_spirits.txt`):**
  - Preserva os 5 modificadores estruturais iniciais.

### 1.4 Dez riscos concretos mapeados
1. **Risco de Fila Reta e Visual Quebrado:** Se a árvore for disposta de forma linear em 200 focos, gerará filas com mais de 4 focos consecutivos e cruzamentos verticais de setas.
   *Mitigação:* Usar `focus_layout.py` e divisão em 5 asas autônomas com suas respectivas raízes e posições X/Y espaçadas.
2. **Risco de Exploração de Buffs Industriais/Militares:** Inflar poder de fábrica civil/militar sem contrapartida.
   *Mitigação:* Teto rígido: estabilidade positiva ≤ +0.15, apoio de guerra ≤ +0.20, PP ≤ 60 por foco, bônus de pesquisa ≤ 25% (uses=1), projetos industriais que ocupam fábricas civis reais.
3. **Risco de Flags Órfãs:** Escrever flags em opções de eventos ou focos que nunca são lidas posteriormente.
   *Mitigação:* Auditoria automática e supressão de flags decorativas. Toda flag registrada abre decisões, eventos ou ideias.
4. **Risco de Eventos Inalcançáveis:** Criar dezenas de eventos com `is_triggered_only = yes` sem nenhum foco ou evento chamador.
   *Mitigação:* Mínimo de 35 eventos orientados por gatilhos de tempo (`date > ...`), MTTH balanceado ou checagem semanal.
5. **Risco de Repetição de Arte (Ícones/Fotos):** Reutilizar texturas idênticas ou duplicadas em desacordo com as regras de assets.
   *Mitigação:* Pipeline automático com verificação de hash SHA256 dos pixels e registro de proveniência no JSON de bindings.
6. **Risco de Travamento da IA em Guerras Precipitadas:** Fazer a IA italiana entrar na guerra em 1914 ao lado dos Aliados antes do tempo histórico.
   *Mitigação:* Pesos de `ai_will_do` com gatilhos de data e fatores condicionais (priorizar neutralidade até a primavera de 1915).
7. **Risco de Desconexão da Cadeia Líbia/Ouchy:** Deixar a Líbia bloqueando a árvore econômica (`libya_colonisation`) se o acordo diplomático não ocorrer.
   *Mitigação:* Condicionar `libya_colonisation` à aquisição da Líbia OU alternativa de foco em caso de recusa otomana.
8. **Risco de BOM em Scripts Paradox:** Salvar acidentalmente arquivos `.txt` ou `.gfx` com UTF-8 BOM, corrompendo a leitura do motor Clausewitz.
   *Mitigação:* Scripts e effects salvos estritamente em UTF-8 sem BOM; apenas `.yml` com UTF-8 BOM.
9. **Risco de Ruptura de Linha de Base nos Testes Globais:** Adicionar novos erros ao `validate_ww1_foundation.py`.
   *Mitigação:* Validação contínua mantendo a contagem em 1596 erros pré-existentes.
10. **Risco de Assimetria Localizada:** Esquecer chaves em PT-BR ou deixar traduções literais em inglês.
    *Mitigação:* Geração simultânea e pareada de chaves `l_english` e `l_braz_por` via builder.

---

## 2. Suposições de Design Registradas
1. **Líbia e Dodecaneso:** Começam sob controle e núcleo otomano (`TUR`). A Itália inicia com foco na questão líbia (`libyan_question`), enviando uma embaixada diplomática à Sublime Porta. A Turquia recebe evento para ceder a soberania da Líbia e o penhor das ilhas do Dodecaneso em troca de alívio fiscal/financeiro (`ai_chance` alta a partir de outubro de 1912, devido à Primeira Guerra dos Bálcãs). Nenhuma guerra armada entre ITA e TUR é scriptada.
2. **Entrada na Primeira Guerra Mundial:** O caminho histórico transcorre pela neutralidade em agosto de 1914 (`declare_neutrality`), conversações do Tratado de Londres na primavera de 1915 (`treaty_of_london`), e declaração de guerra à Áustria-Hungria em maio de 1915 (`declare_war_on_austria`). O caminho alternativo da Tríplice Aliança (`honour_alliance` ou `central_concessions_accord`) permite entrada ao lado de Berlim e Viena ou neutralidade armada mediada (`armed_mediator`).
3. **Escala de Poder Político e Equilíbrio:** A Itália começa com 0.6 de estabilidade e tensões profundas (Questão Meridional, carência de carvão e ferro). Todos os focos benéficos possuem pequenos custos associados ou exigem compromissos políticos.

---

## 3. Rastreamento das Fatias de Trabalho

- [x] **Fatia 0: Reconhecimento, Auditoria e Infraestrutura**
  - Estados líbios e Dodecaneso regularizados para a Turquia.
  - Portão de Entendimento e ganchos catalogados.
  - Suite de testes inicial `tests/test_ww1_italy.py` e script `scripts/italy_audit.py` criados.
  - Construtor `scripts/build_ww1_italy.py` e módulos de dados estruturados.
- [x] **Fatia 1: Asa Política e Sociedade (`pol`, 45 focos) + Medidores Internos**
  - 45 focos políticos implementados e balanceados.
  - 5 medidores internos (`ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, `ita_ww1_irredentism`) com clamp [0-100] semanal em `common/scripted_effects/ww1_italy_effects.txt` e gatilhos em `common/on_actions/ww1_italy_on_actions.txt`.
- [x] **Fatia 2: Asa Diplomacia e Alinhamento (`dip`, 40 focos) + Integrações**
  - 40 focos diplomáticos com ramificações históricas e alternativas (Tratado de Londres, Tríplice Aliança, neutralidade armada).
  - Resolução pacífica da questão líbia/Dodecaneso via Tratado de Ouchy sem guerra direta.
  - Integrações completas com Reino Unido, França, Áustria-Hungria, Alemanha e Império Otomano.
- [x] **Fatia 3: Asa Campanhas e Pós-guerra (`war`, 25 focos)**
  - 25 focos de campanhas e crise pós-guerra (Isonzo, Piave, Solstício, Vittorio Veneto, Fiume, D'Annunzio).
- [x] **Fatia 4: Asa Forças Armadas (`mil`, 55 focos)**
  - 55 focos de Exército, Marinha e Aviação (Alpini, Arditi, MAS, Luigi Rizzo, Caproni, Baracca, Giulio Douhet).
- [x] **Fatia 5: Asa Economia e Mezzogiorno (`eco`, 35 focos)**
  - 35 focos de economia, indústria, questão meridional, carência de carvão/ferro e reconversão pós-guerra.
- [x] **Fatia 6: Fechamento, Arte, Balanceamento e Verificação Final**
  - 200 ícones de foco únicos com `_shine` registrados em `interface/ww1_italy_goals.gfx`.
  - 80 imagens de eventos únicas registradas em `interface/ww1_italy_events.gfx`.
  - 32 ícones de ideias únicas registrados em `interface/ww1_italy_ideas.gfx`.
  - 32 ícones de decisões únicas registrados em `interface/ww1_italy_decisions.gfx`.
  - 843 chaves de localização 100% espelhadas em inglês e português com UTF-8 BOM.
  - Painel de auditoria `scripts/italy_audit.py`: 19/19 metas cumpridas (100% OK).
  - 147 testes unitários do mod executados e aprovados (`test_ww1_*.py`).
  - Linha de base estática rigorosamente mantida: 1596 erros / 115 warnings (zero novos erros).

