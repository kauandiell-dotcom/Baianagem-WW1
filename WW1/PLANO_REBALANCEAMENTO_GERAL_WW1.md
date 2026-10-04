# ⚖️ PLANO MESTRE DE REBALANCEAMENTO INTEGRAL: BAIANAGEM-WW1

> **Identidade do Mod**: *Baianagem-WW1* (Cenário Inicial: 1º de Junho de 1911 — *La Belle Époque*)  
> **Versão Alvo**: Hearts of Iron IV **1.19.3**  
> **Filosofia Fundamental**: **Defesa de Trincheiras, Desgaste Logístico e Combate Autêntico da WW1**, eliminando a hiperinflação de status e restaurando a proposta original de design: unidades especializadas de infiltração tática com baixa organização, tanques de apoio de infantaria viáveis, e fim do "efeito rolo compressor" invencível com Force Attack.

---

## 📋 Sumário Executivo do Diagnóstico

Após varredura técnica completa em `common/units/`, `common/units/equipment/`, `common/defines/`, `common/ideas/`, `common/national_focus/`, `history/units/` e `common/scripted_effects/`, foram identificadas **6 anomalias estruturais críticas** que desfiguraram o balanceamento do projeto:

| Problema Identificado | Causa Raiz Técnica | Consequência no Jogo |
| :--- | :--- | :--- |
| **1. Sturmtruppen Imparáveis ("Costuram o Fronte")** | `elite_inf` possui `breakthrough = 0.80` (+80%), `soft_attack = 0.40` (+40%), bônus de terreno positivos em TODOS os terrenos (+30% rio/montanha/pântano, +40% fortes/urbano) e `max_strength = 25` (HP de infantaria cheia). | Sob *Force Attack*, a unidade ignora dano de organização. Como seu breakthrough anula 90% dos tiros defensores e seu ataque com bônus de terreno é gigantesco, o defensor (com apenas 35 org) evapora em 2 horas sem causar dano de força (HP) ao atacante. |
| **2. Cisma e Batalhões Quebrados de Sub-unidades** | Existem duas unidades conflitantes: `elite_inf` (HP 25, stats de deus) e `german_stosstruppen` / `italian_arditi` / `anzac_corps` / `russian_opolcheniye` com `max_strength = 1.0 - 3.0` (HP de suporte). | Unidades em `ww1_special_subunits.txt` sofrem perda instantânea de 90% do equipamento/manpower por falta de HP, enquanto `elite_inf` em `elite_inf.txt` é um tanque disfarçado de infantaria. |
| **3. Tanques Mais Fracos que Infantaria** | `light_armor` e `heavy_armor` possuem `breakthrough = -0.75` e `-0.80` (-80%), `defense = -0.60`, penalidades de terreno de até -90%, enquanto canhões AT de 1914 possuem `ap_attack = 95` e `hard_attack = 45`. | Tanques têm breakthrough negativo e são vaporizados instantaneamente em 1914 por armas anti-tanque com status de 1943. |
| **4. Distorção de Organização e Defines** | `infantry` teve `max_organisation` reduzida para **35**, mas montanheses/marines/cavalaria ficaram em **70** e milícias em **50**; no define `01_defines.lua`, `LAND_COMBAT_ORG_DAMAGE_MODIFIER = 0.085` (+60% de dano de org) e `LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.045` (-25% de dano de força). | Linhas de infantaria regular desmoronam em 24h sob qualquer ataque; dano reduzido de força torna o *Force Attack* quase indolor para o atacante. |
| **5. Hiperinflação de Modificadores Nacionais** | Dezenas de ideias em `ww1_germany_ideas.txt` e `ww1_national_modifiers.txt` concedem entre +20% e +35% de ataque/defesa/breakthrough que se acumulam (Alemanha acumula +47% ataque e +100% breakthrough). | Inflação de combate quebra o motor do Clausewitz e anula qualquer possibilidade de atrito estático de trincheiras. |
| **6. Anacronismos Globais de 1911 & Ideias Fantasmas** | `MBR_contingency.txt` carrega `unlock_elite_inf` ("Sturmtruppen Division") para todos os 369 países do mundo no primeiro dia de 1911; `german_infiltration_assault_idea` e `GER_kaiserschlacht_idea` são chamadas na árvore alemã sem existirem em `common/ideas/`. | A Libéria e o Butão iniciam com divisões de tropas de choque de 1918 em 1911; focos alemães concedem ideias nulas. |

---

## 🛠️ Arquitetura Detalhada da Solução Proposta

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                PILARES DO NOVO BALANCEAMENTO                          │
├─────────────────────────────────────────┬──────────────────────────────────────────────┤
│ 1. TROPAS DE CHOQUE (STURMTRUPPEN)      │ • Org baixa (20) vs Infantaria Regular (50) │
│    Infiltração rápida, alcance limitado │ • HP calibrado (20), sem buffs em rios/morros│
│    Custo elevado em morteiros/suporte   │ • Sob Force Attack sofre atrito severo de HP │
├─────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 2. DEFESA DE TRINCHEIRAS & INFANTARIA   │ • Infantaria de Linha com Org 50             │
│    Frentes estáveis e custosas de romper│ • Cavalaria 45, Milícia 30, Montanheses 55   │
│    Artilharia como fonte de desgaste    │ • Defines de dano normalizados (0.060/0.065) │
├─────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 3. TANQUES WW1 (LANDSHIPS)              │ • Breakthrough positivo (+0.25 / +0.40)      │
│    Blindados lentos de ruptura de arame │ • Canhões AT 1914 ajustados (AP 20, Hard 12) │
│    Incapazes de blitzkrieg solitária    │ • Blindagem relevante contra fuzis/metralhas │
├─────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 4. HIGIENIZAÇÃO DE ESPÍRITOS NACIONAIS │ • Redução de modificadores inflados (5-10%)  │
│    Bônus autênticos, sem empilhamento   │ • Criação das ideias fantasmas ausentes      │
│    Fim da proliferação global em 1911   │ • Remoção do OOB global em MBR_contingency   │
└─────────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 📐 1. Calibração de Sub-unidades e Batalhões (`common/units/`)

### A. Tropa de Choque / Infiltração (`elite_inf` & `german_stosstruppen`)
- **Objetivo**: Unidade tática de ruptura pontual contra trincheiras entrincheiradas; possui alto Soft Attack relativo e Breakthrough moderado para abrir a brecha, mas baixa Organização (20), esgotando-se rapidamente se não vencer o combate no primeiro assalto. Sob *Force Attack*, sofre desgaste real e perda pesada de equipamentos caros.

| Atributo | Valor Atual (`elite_inf`) | Valor Atual (`german_stosstruppen`) | **Novo Valor Proposto** | Racional Técnico Paradox |
| :--- | :--- | :--- | :--- | :--- |
| **`max_organisation`** | 25 | 20 | **20** | Org reduzida (40% da infantaria regular). Sem fôlego para ofensivas prolongadas. |
| **`max_strength` (HP)** | 25 | 2.0 *(Bug Crítico)* | **20** | HP de batalhão combatente. Corrige o bug de 2 HP e garante perdas proporcionais. |
| **`breakthrough`** | +0.80 (+80%) | +0.60 (+60%) | **+0.25 (+25%)** | Bônus tático sólido sobre a infantaria (+10%), sem superar os tanques nem anular o fogo defensor. |
| **`soft_attack`** | +0.40 (+40%) | +0.40 (+40%) | **+0.20 (+20%)** | Força de choque em granadas e pistolas, sem deletar instantaneamente o defensor. |
| **`defense`** | -0.25 (-25%) | - | **-0.30 (-30%)** | Doutrina puramente ofensiva; altamente vulnerável a contra-ataques estáticos. |
| **`ap_attack`** | +0.60 (+60%) | - | **+0.15 (+15%)** | Capacidade de penetrar casamatas e blindagens leves, sem valores irreais. |
| **`hard_attack`** | +0.50 (+50%) | - | **+0.10 (+10%)** | Dano reduzido contra estruturas pesadas. |
| **Modificadores de Terreno** | +30% a +40% em TUDO | Fort +50%, Urb +30%, For +20% | **Fort +20%, Urb +15%, Morro +5%, Rio -15%, Montanha -10%, Pântano -15%** | Elimina a anomalia de ter bônus em rios e montanhas. Mantém especialização apenas em fortificações/trincheiras. |
| **Equipamentos Requeridos** | Fuzis 180, Sup 15, Art 5 | Fuzis 120, Sup 15 | **Fuzis 140, Sup 30, Art 12** | Demanda logística severa de morteiros de trincheira e equipamentos de suporte. |
| **`supply_consumption`** | 0.12 | 0.10 | **0.16** | Alto consumo de munição, explosivos e mantimentos especiais. |

### B. Unidades Especiais Globais de WW1 (`ww1_special_subunits.txt`)
Correção imediata do erro fatal de `max_strength = 1.0 - 3.0` em todos os batalhões de linha:

| Sub-unidade | `max_strength` Atual | **`max_strength` Corrigido** | `max_organisation` Corrigido | `soft_attack` / `breakthrough` |
| :--- | :--- | :--- | :--- | :--- |
| **`german_stosstruppen`** | 2.0 | **20.0** | **20** | soft +20%, brk +25%, def -30% |
| **`italian_arditi`** | 1.8 | **20.0** | **20** | soft +20%, brk +25%, def -30% |
| **`anzac_corps`** | 2.0 | **22.0** | **30** | soft +15%, brk +15%, amph +25% |
| **`kuk_gebirgsjaeger`**| 2.0 | **22.0** | **35** | soft +10%, mnt attack/def +30% |
| **`russian_opolcheniye`** | 1.5 | **22.0** | **25** | soft -10%, custo fuzis reduzido |
| **`us_doughboys_division`** | 3.0 | **25.0** | **40** | soft +15%, def +15%, cw = 3 |
| **`ottoman_ghazi_militia`** | 1.0 | **20.0** | **25** | soft -10%, desert attack +30% |

### C. Infantaria Regular, Milícias e Tropas Especiais (`infantry.txt`)
Eliminação da inversão onde infantaria de linha tem a pior organização militar do mod:

| Sub-unidade | `max_organisation` Atual | **`max_organisation` Corrigido** | `manpower` | `combat_width` |
| :--- | :--- | :--- | :--- | :--- |
| **`infantry`** (Linha) | **35** *(Excessivamente frágil)* | **50** *(Espinha dorsal de defesa)* | 1200 | 2 |
| **`mountaineers`** | **70** *(Dobro da infantaria)* | **55** | 1000 | 2 |
| **`marine`** | **70** | **55** | 1000 | 2 |
| **`cavalry`** | **70** (Vanilla não sobrescrita) | **45** | 1000 | 2 |
| **`militia`** | **50** (Maior que infantaria) | **30** | 1000 | 2 |
| **`irregular_infantry`** | **45** (Maior que infantaria) | **25** | 1000 | 2 |
| **`penal_battalion`** | **70** | **35** | 850 | 2 |
| **`bicycle_battalion`** | **60** | **45** | 1000 | 2 |

### D. Blindados e Tanques de Ruptura de Trincheira (`common/units/*armor.txt`)
Resgate da função histórica dos tanques na Primeira Guerra (baterias blindadas lentas para atravessar arame farpado e casamatas):

| Sub-unidade | `breakthrough` Atual | **`breakthrough` Corrigido** | `defense` Corrigido | `max_organisation` | `hardness` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`light_armor`** | -0.75 (-75%) | **+0.20 (+20%)** | **-0.20** | 15 | 55% |
| **`medium_armor`** | -0.75 (-75%) | **+0.30 (+30%)** | **-0.20** | 15 | 65% |
| **`heavy_armor`** | -0.80 (-80%) | **+0.40 (+40%)** | **-0.20** | 15 | 75% |
| **`super_heavy_armor_brigade`** | -0.80 (-80%) | **+0.45 (+45%)** | **-0.20** | 10 | 80% |

---

## ⚙️ 2. Calibração de Equipamentos (`common/units/equipment/`)

### A. Equipamento Anti-Tanque (`anti_tank.txt`)
Reescalonamento de valores do ano 1943 para armas autênticas de WW1 (fuzis Mauser T-Gewehr 1918 e canhões de campanha adaptados):

| Equipamento | Ano | `hard_attack` Atual | **`hard_attack` Proposto** | `ap_attack` Atual | **`ap_attack` Proposto** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `anti_tank_equipment` (Base) | 1914 | 45 | **12** | 95 | **20** |
| `anti_tank_equipment_1` | 1914 | 45 | **14** | 95 | **24** |
| `anti_tank_equipment_2` | 1916 | 65 | **20** | 135 | **35** |

*(Com blindagens de tanques WW1 variando entre 10 e 25 mm, um AP de 20-35 mm oferece combate tenso e disputado, em vez de aniquilação no primeiro tick).*

---

## 🕹️ 3. Ajuste dos Parâmetros de Motor de Combate (`common/defines/01_defines.lua`)

| Parâmetro no Engine | Valor Atual | **Novo Valor Proposto** | Efeito no Dinamismo de Jogo |
| :--- | :--- | :--- | :--- |
| **`LAND_COMBAT_ORG_DAMAGE_MODIFIER`** | 0.085 (+60% vs vanilla 0.053) | **0.060** | Permite que divisões em trincheiras segurem bombardeios sem dobrar em 24h. |
| **`LAND_COMBAT_STR_DAMAGE_MODIFIER`** | 0.045 (-25% vs vanilla 0.060) | **0.065** | **Punir o Force Attack**: ataques frontais descuidados provocam baixas sangrentas e perda pesada de equipamentos. |
| **`SPECIAL_FORCES_CAP_BASE`** | 0.10 (10% do exército) | **0.05 (5%)** | Limita a proliferação excessiva de divisões de choque, tornando-as um recurso tático valioso. |
| **`SPECIAL_FORCES_CAP_MIN`** | 48 batalhões | **24 batalhões** | Exércitos de tempo de paz não conseguem spamar batalhões de elite sem antes expandir o exército regular. |

---

## 🏛️ 4. Sanificação e Desinflação de Ideias e Modificadores (`common/ideas/`)

Redução de bônus cumulativos de combate para a faixa padrão recomendada Paradox (5% a 10%):

### A. Império Alemão (`ww1_germany_ideas.txt` & `ww1_national_modifiers.txt`)
- `GER_silent_dictatorship_ohl`: Reduzir `army_attack_factor` de +15% para **+5%**; `breakthrough_factor` de +15% para **+5%**.
- `GER_ohl_supreme_command`: Reduzir `breakthrough_factor` de +15% para **+5%**.
- `GER_schlieffen_momentum`: Reduzir `breakthrough_factor` de +20% para **+8%**; `army_attack_factor` de +10% para **+5%**.
- `GER_ludendorff_stormtrooper_assault`: Reduzir `breakthrough_factor` de +20% para **+8%**; `army_attack_factor` de +12% para **+5%**; `special_forces_attack_factor` de +20% para **+8%**.
- `GER_bruchmueller_artillery`: Reduzir `artillery_attack_factor` de +20% para **+10%**; `breakthrough_factor` de +15% para **+5%**.
- `GER_haber_bosch_nitrogen_miracle_idea`: Reduzir `army_artillery_attack_factor` de +15% para **+8%**.
- `GER_heavy_howitzers_production`: Reduzir `army_artillery_attack_factor` de +15% para **+8%**.
- **Criação das Ideias Fantasmas Ausentes**:
  - `german_infiltration_assault_idea`: `special_forces_attack_factor = 0.05`, `breakthrough_factor = 0.05`, `max_planning = 0.05`.
  - `GER_kaiserschlacht_idea`: Ideia temporária com timeout de 90 dias: `army_attack_factor = 0.10`, `breakthrough_factor = 0.10`, `supply_consumption_factor = 0.15`, `conscription_factor = -0.05`.

### B. Outras Potências (`ww1_national_modifiers.txt` & `ww1_russia_ideas.txt`)
- **Rússia**:
  - `SOV_the_steamroller`: Reduzir `conscription_factor` de +40% para **+15%**; `supply_consumption_factor` de -15% para **-5%**.
  - `brusilov_offensive_shock_idea`: Reduzir `army_infantry_attack_factor` de +25% para **+8%**; `army_artillery_attack_factor` de +20% para **+8%**; `breakthrough_factor` para **+8%**.
  - Adicionar `SOV_backward_agrarian_system` em `SOV - Soviet union.txt` para destravar a cadeia histórica da reforma de Stolypin.
- **França**:
  - `FRA_elan_vital_doctrine`: Reduzir `army_infantry_attack_factor` de +15% para **+5%**; `army_morale_factor` de +20% para **+8%**.
  - `FRA_canon_75mm_supremacy`: Reduzir `army_artillery_attack_factor` de +20% para **+8%**.
  - `landships_breakthrough_boost`: Reduzir `army_armor_attack_factor` de +35% para **+10%**; `breakthrough_factor` de +25% para **+10%**.
- **Reino Unido**:
  - `ENG_professional_bef`: Reduzir `army_infantry_attack_factor` de +15% para **+8%**.
- **Áustria-Hungria**:
  - `skoda_siege_bombardment_idea`: Reduzir `army_artillery_attack_factor` de +35% para **+12%**.
  - `AUS_skoda_siege_arsenals`: Reduzir `army_artillery_attack_factor` de +25% para **+8%**.
- **Itália**:
  - `arditi_infiltration_shock_idea`: Reduzir `army_infantry_attack_factor` de +30% para **+8%**; `breakthrough_factor` de +30% para **+10%**.
- **Império Otomano**:
  - `kemal_fanatic_defence_idea`: Reduzir `army_core_defence_factor` de +35% para **+12%**; `max_dig_in` de 8 para **4**; `army_morale_factor` de +30% para **+10%**.
  - `TUR_mehmetcik_tenacity`: Reduzir `army_core_defence_factor` de +25% para **+10%**.
- **Estados Unidos**:
  - `trench_sweeper_shotgun_idea`: Reduzir `army_infantry_attack_factor` de +30% para **+8%**; `breakthrough_factor` de +25% para **+8%**.

---

## 🗂️ 5. Sanitização de OOBs Iniciais e Desbloqueio Tecnológico

1. **Remoção do Desbloqueio Global de Sturmtruppen em 1911**:
   - Em `common/scripted_effects/MBR_contingency.txt`, remover as linhas 11-16 que executam `load_oob = "unlock_elite_inf"` para todos os 369 países no início do jogo.
2. **Sanitização do OOB Inicial da Alemanha (`history/units/GER_1936_generic.txt`)**:
   - Renomear o template de partida `Kaiserliche Garde-Stosstruppen` para a histórica `Kaiserliche Garde-Division` de tempo de paz (composta por infantaria de elite prussiana com Jäger, e não Sturmtruppen de 1918).
   - O template de `Sturmtruppen Division` será desbloqueado no momento histórico adequado através do foco `GER_stosstruppen_tactics` (1916).
3. **Correção de Tecnologias em `common/technologies/infantry.txt`**:
   - Linha 30: Remover `elite_inf` da tecnologia inicial de 1893 (`infantry_weapons`).
   - Linha 2666: Corrigir a chamada para `sturmtruppe_battalion` (inexistente) remapeando para `elite_inf`, ativada pelo foco alemão de 1916 ou tech equivalente de doutrina de choque de 1916.
4. **Doutrina de Partida da Alemanha**:
   - Ajustar `set_grand_doctrine = new_mobile_warfare` em `history/countries/GER - Germany.txt` para `grand_battleplan` (refletindo o planejamento estrito de horários ferroviários do Plano Schlieffen de 1911).

---

## 🧪 6. Matriz de Verificação e Testes de Balanceamento

Para validar o sucesso das alterações antes da entrega final:
1. **Teste do Combate de Trincheiras**: Uma divisão de infantaria regular de 9 batalhões entrincheirada (18 de largura) deve suportar um ataque frontal de infantaria equivalente por no mínimo 4 a 6 dias in-game sem desmoronar.
2. **Teste de Ruptura de Tropas de Choque**: Uma divisão com Sturmtruppen deve conseguir romper a linha entrincheirada com apoio de artilharia, mas perder sua organização rapidamente (em menos de 48h de combate consecutivo) se tentar avançar em profundidade sem consolidação de infantaria regular.
3. **Teste de Força com Force Attack**: Ativar *Force Attack* em divisões de Sturmtruppen deve resultar em baixas pesadas de efetivo e perda massiva de morteiros/suporte devido ao contra-ataque defensor, impedindo que o jogador avance indefinidamente por províncias consecutivas sem esgotar seus batalhões.
4. **Validação Estrutural e Sintática**: Executar o script `scratch/full_qa_audit.py` para assegurar 0 erros de chaves, 0 IDs inexistentes e 100% de conformidade com os padrões Paradox.
