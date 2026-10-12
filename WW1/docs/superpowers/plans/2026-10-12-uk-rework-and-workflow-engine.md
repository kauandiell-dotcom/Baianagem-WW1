# Rework Completo do Reino Unido e Oráculo Semântico de Modding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminar de forma permanente as causas-raiz de alucinações na esteira de modding de Hearts of Iron IV construindo um Oráculo Semântico conectado ao jogo base e reestruturar completamente o Reino Unido (`ENG`) para solucionar todos os 4 defeitos reportados no Q.A do Bruno (modificadores vazios, empilhamento de 70 espíritos, eventos sem efeito e atalhos sem localização).

**Architecture:** A solução divide-se em duas camadas: (1) Uma esteira de governança semântica automatizada que extrai 673 modificadores válidos da instalação local do HOI4 em `E:\SteamLibrary` e barra qualquer token inválido em testes automatizados; (2) Consolidação radical dos arquivos britânicos nos 5 Pilares Nacionais com evolução via `swap_ideas`, conversão de 106 `add_ideas` em recompensas materiais tangíveis (fábricas, dockyards, armas, XP, bônus de pesquisa válidos), preenchimento das 19 opções de eventos vazias e cobertura bilíngue 100% com UTF-8 BOM.

**Tech Stack:** Python 3.10+ (scripts de validação, unittests, oráculo semântico), Paradox Clausewitz Scripting Language (HOI4 .txt), YAML com UTF-8 BOM (`l_english`, `l_braz_por`).

**Spec:** Relatório de Q.A do Bruno e capturas de tela arquivadas em `PLANO_REWORK_COMPLETO_REINO_UNIDO_WW1.md`.

## Global Constraints

- **Single Source of Truth:** Nenhum token de modificador de país pode ser utilizado sem estar presente no oráculo semântico gerado a partir de `E:\SteamLibrary\steamapps\common\Hearts of Iron IV`.
- **Regra Anti-Stacking Estrita:** O Reino Unido não pode acumular mais de 5 espíritos nacionais simultâneos na interface do jogador ao longo de toda a campanha (1911-1920). Todo aprimoramento de espírito deve utilizar `swap_ideas`.
- **Regra Anti-Ghost:** É proibido criar opções de eventos ou decisões que apenas alterem variáveis invisíveis sem conceder tooltip descritivo ou recompensas de jogabilidade tangíveis (PP, estabilidade, fábricas, XP ou divisões).
- **Consolidação de Arquivos:** Eliminar o sprawl de 9 arquivos de ideias e 7 arquivos de eventos. Centralizar em arquivos únicos e canônicos: `common/ideas/ww1_britain_ideas.txt`, `common/decisions/ww1_britain_decisions.txt`, `events/ww1_britain_events.txt`.
- **Localização Obrigatória:** 100% dos focos, ideias, decisões, eventos e atalhos devem conter localização pareada em inglês e português com cabeçalho UTF-8 BOM (`\xef\xbb\xbf`).
- **Isolamento de Modding:** Nenhuma alteração pode ser escrita fora do repositório local `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`.

## Review Focus

1. **Tokens de modificador desconhecidos gerando `grants ()` in-game:** O teste do oráculo deve varrer 100% dos arquivos de ideias e decisões e falhar caso encontre qualquer token fora da lista permitida.
2. **Empilhamento de mais de 5 espíritos nacionais simultâneos:** O teste estrutural deve simular o caminho de focos e verificar que o número máximo de espíritos ativos nunca excede 5.
3. **Eventos de escolha nula (Imperial Conference):** Opções do evento devem conceder benefícios navais claros (comboios, dockyards, XP naval) ou estabilidade/autonomia com tooltips explícitos.
4. **Opções de evento vazias:** Nenhuma opção em `events/` pode conter um bloco de código vazio (`option = { name = ... }` sem efeitos).
5. **Atalhos e foco raiz sem texto:** Os atalhos de navegação (`ENG_ww1_shortcut_*`) e o foco raiz `ENG_ww1_1911_1923` devem estar traduzidos em PT-BR e EN.

---

### Task 1: Oráculo Semântico de Modificação da Clausewitz (`scripts/hoi4_semantic_oracle.py`)

**Files:**
- Create: `scripts/hoi4_semantic_oracle.py`
- Create: `data/hoi4_valid_country_modifiers.json`
- Test: `tests/test_hoi4_semantic_oracle.py`

**Interfaces:**
- Produces: `get_valid_modifiers() -> Set[str]`, `audit_idea_file(filepath: str) -> List[Dict]`, `audit_all_mod_ideas() -> List[str]`

- [ ] **Step 1: Write failing test in `tests/test_hoi4_semantic_oracle.py`**
  O teste deve verificar que o oráculo rejeita tokens alucinados (`carrier_traffic_factor`, `sub_attack`, `production_cost_max_armor_factor`) e aceita modificadores reais do HOI4 (`industrial_capacity_factory`, `army_org_factor`, `research_speed_factor`).

- [ ] **Step 2: Run test to verify it fails**
  Run: `python -m unittest tests/test_hoi4_semantic_oracle.py`  
  Expected: FAIL (ModuleNotFoundError: No module named 'scripts.hoi4_semantic_oracle')

- [ ] **Step 3: Implement `scripts/hoi4_semantic_oracle.py`**
  Extrai os modificadores do diretório `E:\SteamLibrary\steamapps\common\Hearts of Iron IV\common\ideas` e `common\modifiers`, salva cache em `data/hoi4_valid_country_modifiers.json` e expõe a API de validação semântica.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python -m unittest tests/test_hoi4_semantic_oracle.py`  
  Expected: PASS

- [ ] **Step 5: Commit**
  ```bash
  git add scripts/hoi4_semantic_oracle.py data/hoi4_valid_country_modifiers.json tests/test_hoi4_semantic_oracle.py
  git commit -m "feat(qa): implement authoritative HOI4 Clausewitz semantic oracle"
  ```

---

### Task 2: Suíte de Testes Automatizada do Reino Unido (Ciclo RED)

**Files:**
- Create: `tests/test_ww1_britain_complete_audit.py`

**Interfaces:**
- Consumes: `scripts/hoi4_semantic_oracle.py`
- Produces: Testes automatizados cobrindo os 4 bugs do relatório do Bruno

- [ ] **Step 1: Write `tests/test_ww1_britain_complete_audit.py`**
  Implementa 4 testes fundamentais:
  1. `test_zero_invalid_modifiers_in_uk_ideas`: Audita todos os arquivos de ideias da Grã-Bretanha contra o Oráculo Semântico.
  2. `test_anti_stacking_limits`: Audita `common/national_focus/uk.txt` garantindo que o número de `add_ideas` avulsas não ultrapassa o limite e que `swap_ideas` é utilizado para os 5 Pilares.
  3. `test_events_have_tangible_effects_and_no_empty_options`: Varre todos os eventos britânicos garantindo que nenhuma opção é vazia e que o evento Imperial Conference tem efeitos navais reais.
  4. `test_shortcuts_and_root_focus_localisation`: Verifica a existência de `ENG_ww1_shortcut_*` e `ENG_ww1_1911_1923` nos arquivos `.yml` de PT-BR e EN com UTF-8 BOM.

- [ ] **Step 2: Run test to verify it FAILS (Ciclo RED Comprovado)**
  Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`  
  Expected: FAIL com múltiplos erros acusando os 46 tokens inválidos, 106 ideias avulsas, 19 opções vazias e chaves de atalho ausentes.

- [ ] **Step 3: Commit do Teste RED**
  ```bash
  git add tests/test_ww1_britain_complete_audit.py
  git commit -m "test(uk): add comprehensive QA audit test suite for British Empire (RED)"
  ```

---

### Task 3: Consolidação e Definição dos 5 Pilares Centrais (`common/ideas/ww1_britain_ideas.txt`)

**Files:**
- Modify: `common/ideas/ww1_britain_ideas.txt`
- Remove: `common/ideas/ww1_britain_army_ideas.txt`, `common/ideas/ww1_britain_diplomacy_ideas.txt`, `common/ideas/ww1_britain_economy_ideas.txt`, `common/ideas/ww1_britain_extra_ideas.txt`, `common/ideas/ww1_britain_navy_ideas.txt`, `common/ideas/ww1_britain_politics_ideas.txt`, `common/ideas/ww1_britain_rework_ideas.txt`

**Interfaces:**
- Produces: 5 Pilares Nacionais com Tiers 1-3 verificados semanticamente:
  - Pilar 1: `ENG_two_power_standard_t1`, `ENG_two_power_standard_t2`, `ENG_two_power_standard_t3`
  - Pilar 2: `ENG_city_of_london_credit_t1`, `ENG_city_of_london_credit_t2`, `ENG_city_of_london_credit_t3`
  - Pilar 3: `ENG_professional_bef_t1`, `ENG_professional_bef_t2`, `ENG_professional_bef_t3`
  - Pilar 4: `ENG_the_imperial_web_t1`, `ENG_the_imperial_web_t2`, `ENG_the_imperial_web_t3`
  - Pilar 5: `ENG_irish_home_rule_tension`, `ENG_irish_home_rule_suspended`, `ENG_irish_home_rule_compromise`

- [ ] **Step 1: Consolidar e reescrever `common/ideas/ww1_britain_ideas.txt`**
  Escrever os 5 Pilares com tokens 100% validados no Oráculo Semântico (ex: `navy_submarine_attack_factor`, `navy_sub_detection_factor`, `industrial_capacity_factory`, `army_org_factor`). Remover todos os 7 arquivos fragmentados de ideias redundantes.

- [ ] **Step 2: Atualizar `history/countries/ENG - Britain.txt`**
  Garantir que a Grã-Bretanha inicializa com exatamente os Tiers 1 dos 5 Pilares:
  ```clausewitz
  add_ideas = {
      ENG_two_power_standard_t1
      ENG_city_of_london_credit_t1
      ENG_professional_bef_t1
      ENG_the_imperial_web_t1
      ENG_irish_home_rule_tension
  }
  ```

- [ ] **Step 3: Run partial test verification**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_zero_invalid_modifiers_in_uk_ideas`  
  Expected: PASS para a validação semântica das ideias.

- [ ] **Step 4: Commit**
  ```bash
  git add common/ideas/ history/countries/ENG\ -\ Britain.txt
  git commit -m "feat(uk): consolidate British ideas into 5 core tiered national pillars"
  ```

---

### Task 4: Reestruturação da Árvore de Focos (`common/national_focus/uk.txt`)

**Files:**
- Modify: `common/national_focus/uk.txt`

**Interfaces:**
- Consumes: 5 Pilares Nacionais de `common/ideas/ww1_britain_ideas.txt`
- Produces: Árvore de 201 focos convertida para recompensas materiais e `swap_ideas`

- [ ] **Step 1: Substituir os 106 `add_ideas` na árvore de focos**
  - Os focos que aprimoram as instituições imperiais trocam os espíritos via `swap_ideas`:
    - Foco da Grand Fleet: `swap_ideas = { remove_idea = ENG_two_power_standard_t1 add_idea = ENG_two_power_standard_t2 }`
    - Foco da Guerra Submarina/ASDIC: `swap_ideas = { remove_idea = ENG_two_power_standard_t2 add_idea = ENG_two_power_standard_t3 }`
    - Foco de Munições de Lloyd George: `swap_ideas = { remove_idea = ENG_city_of_london_credit_t1 add_idea = ENG_city_of_london_credit_t2 }`
    - Foco de Mobilização Total: `swap_ideas = { remove_idea = ENG_city_of_london_credit_t2 add_idea = ENG_city_of_london_credit_t3 }`
    - Foco dos Novos Exércitos de Kitchener: `swap_ideas = { remove_idea = ENG_professional_bef_t1 add_idea = ENG_professional_bef_t2 }`
    - Foco do Martelo Continental: `swap_ideas = { remove_idea = ENG_professional_bef_t2 add_idea = ENG_professional_bef_t3 }`
    - Foco do Esforço Colonial/ANZAC: `swap_ideas = { remove_idea = ENG_the_imperial_web_t1 add_idea = ENG_the_imperial_web_t2 }`
    - Foco do Gabinete de Guerra Imperial: `swap_ideas = { remove_idea = ENG_the_imperial_web_t2 add_idea = ENG_the_imperial_web_t3 }`
    - Focos irlandeses: realizam `swap_ideas` reduzindo a tensão e removendo ao final do acordo.
  - Todos os outros focos recebem **recompensas tangíveis**:
    - Fábricas e estaleiros históricos em Lancashire, Yorkshire, Birmingham, Clyde, Belfast e Portsmouth.
    - Estoques de fuzis Lee-Enfield, artilharia 18-pounder, tanques Mark I e comboios.
    - Bônus de tecnologia válidos (`add_tech_bonus = { category = infantry_weapons uses = 1 bonus = 1.0 }`).
    - Experiência militar (Army, Navy e Air XP).

- [ ] **Step 2: Corrigir o foco raiz e atalhos de navegação**
  Garantir que os atalhos usam `ENG_ww1_shortcut_politics`, `ENG_ww1_shortcut_economy`, `ENG_ww1_shortcut_diplomacy`, `ENG_ww1_shortcut_navy`, `ENG_ww1_shortcut_army` e o foco raiz é `ENG_ww1_1911_1923`.

- [ ] **Step 3: Run test verification**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_anti_stacking_limits`  
  Expected: PASS

- [ ] **Step 4: Commit**
  ```bash
  git add common/national_focus/uk.txt
  git commit -m "feat(uk): convert focus tree to tangible material rewards and swap_ideas architecture"
  ```

---

### Task 5: Rework das Decisões e Remoção de Modificadores Vazios (`common/decisions/`)

**Files:**
- Modify: `common/decisions/ww1_britain_decisions.txt`
- Remove: `common/decisions/ww1_britain_army_decisions.txt`, `common/decisions/ww1_britain_diplomacy_decisions.txt`, `common/decisions/ww1_britain_economy_decisions.txt`, `common/decisions/ww1_britain_extra_decisions.txt`, `common/decisions/ww1_britain_navy_decisions.txt`, `common/decisions/ww1_britain_policy_decisions.txt`, `common/decisions/ww1_britain_politics_decisions.txt`

**Interfaces:**
- Produces: Decisões limpas sem modificadores vazios `()`

- [ ] **Step 1: Consolidar decisões e reformular as 4 decisões reportadas pelo Bruno**
  - "Place District Contracts": Concede +10% de velocidade de construção militar por 180 dias com custo de 1 fábrica civil temporária.
  - "Call the Indian Corps": Desdobra imediatamente 2 divisões indianas treinadas no Egito/Suez + 40k manpower + 3k fuzis.
  - "Set the Seaplane Patrol Rota": Concede bônus de patrulha anti-submarina e detecção naval válidos por 120 dias.
  - "Discount Industrial Bills in the City": Fornece 50 de poder político e reduz bens de consumo por 150 dias.

- [ ] **Step 2: Run test verification**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_zero_invalid_modifiers_in_uk_decisions`  
  Expected: PASS

- [ ] **Step 3: Commit**
  ```bash
  git add common/decisions/
  git commit -m "feat(uk): eliminate empty decision modifiers and consolidate decisions"
  ```

---

### Task 6: Rework dos Eventos e Preenchimento das 19 Opções Vazias (`events/`)

**Files:**
- Modify: `events/ww1_britain_events.txt`
- Remove: `events/ww1_britain_army_events.txt`, `events/ww1_britain_diplomacy_events.txt`, `events/ww1_britain_economy_events.txt`, `events/ww1_britain_extra_events.txt`, `events/ww1_britain_navy_events.txt`, `events/ww1_britain_policy_events.txt`, `events/ww1_britain_politics_events.txt`

**Interfaces:**
- Produces: Eventos com escolhas históricas de impacto tangível

- [ ] **Step 1: Reformular o evento Imperial Conference (`ww1_britain_pol.6`)**
  - Opção A (Contribuição Direta à Royal Navy): +200 comboios, +30 Navy XP, bônus de construção de couraçados.
  - Opção B (Esquadras Regionais nos Domínios): +75 PP, +5% estabilidade, estaleiros adicionados no Canadá e Austrália, bônus diplomático.

- [ ] **Step 2: Preencher todas as 19 opções vazias**
  Adicionar efeitos históricos (ganho de experiência, divisões de voluntários, ajustes de apoio de guerra e popularidade partidária).

- [ ] **Step 3: Run test verification**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_events_have_tangible_effects_and_no_empty_options`  
  Expected: PASS

- [ ] **Step 4: Commit**
  ```bash
  git add events/
  git commit -m "feat(uk): provide meaningful choices for Imperial Conference and eliminate empty event options"
  ```

---

### Task 7: Localização Bilíngue Completa com UTF-8 BOM

**Files:**
- Modify: `localisation/english/ww1_britain_l_english.yml`
- Modify: `localisation/braz_por/ww1_britain_l_braz_por.yml`
- Remove: `localisation/replace/zz_ww1_britain_*_l_*.yml` (arquivos obsoletos que causavam conflitos)

**Interfaces:**
- Produces: 100% das chaves traduzidas em PT-BR e EN com byte header `\xef\xbb\xbf`

- [ ] **Step 1: Inserir localização dos atalhos e foco raiz**
  Adicionar `ENG_ww1_shortcut_politics`, `ENG_ww1_shortcut_economy`, `ENG_ww1_shortcut_diplomacy`, `ENG_ww1_shortcut_navy`, `ENG_ww1_shortcut_army` e `ENG_ww1_1911_1923`.

- [ ] **Step 2: Inserir localização dos 5 Pilares Centrais e decisões reformuladas**
  Traduzir os Tiers 1-3 de cada um dos 5 pilares com descrições históricas imersivas.

- [ ] **Step 3: Gravar ambos os arquivos com UTF-8 BOM estrito**
  Garantir que os primeiros 3 bytes são `\xef\xbb\xbf`.

- [ ] **Step 4: Run test verification**
  Run: `python -m unittest tests.test_ww1_britain_complete_audit.TestBritainCompleteAudit.test_shortcuts_and_root_focus_localisation`  
  Expected: PASS

- [ ] **Step 5: Commit**
  ```bash
  git add localisation/
  git commit -m "feat(uk): complete 100% bilingual localization with UTF-8 BOM and navigation shortcuts"
  ```

---

### Task 8: Integração no Master QA e Verificação Final (Ciclo GREEN)

**Files:**
- Modify: `scripts/qa_audit_all.py`

**Interfaces:**
- Produces: Master QA audit suite integrando o Oráculo Semântico e a suíte completa da Grã-Bretanha

- [ ] **Step 1: Atualizar `scripts/qa_audit_all.py` para incluir a auditoria semântica e os testes da Grã-Bretanha**
  Adicionar verificação de modificadores válidos e execução de `test_ww1_britain_complete_audit.py` no runner master.

- [ ] **Step 2: Executar a suíte de testes completa**
  Run: `python -m unittest tests/test_ww1_britain_complete_audit.py`  
  Run: `python scripts/qa_audit_all.py`  
  Expected: ALL TESTS PASS (Exit code 0, 0 falhas)

- [ ] **Step 3: Commit Final**
  ```bash
  git add scripts/qa_audit_all.py
  git commit -m "feat(qa): integrate semantic oracle and British Empire validation into master QA runner"
  ```
