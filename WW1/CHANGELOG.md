# Baianagem-WW1 — Registro de Alterações (Changelog)

Todas as alterações técnicas e de design relevantes deste projeto são documentadas neste arquivo de forma cronológica.

---

## [Unreleased] - Em Andamento

### Adicionado
- **Mecânicas de MP Exclusivas para Jogadores Humanos (`is_ai = no`)**:
  - `common/ideas/baianagem_mp_player.txt`: Ideia `baianagem_player_buff` fornecendo -75% tempo de treinamento, +25% velocidade de construção, +25% conscrição, +100 max command power e +50% XP militar.
  - `common/on_actions/baianagem_player_on_actions.txt`: No `on_startup`, jogadores humanos recebem automaticamente 4 slots de pesquisa, o buff de MP e 500 de XP em Exército, Marinha e Aeronáutica.
  - `common/decisions/categories/baianagem_player_categories.txt` & `common/decisions/baianagem_player_decisions.txt`: Decisões exclusivas para jogadores reabastecerem 500 XP a cada 7 dias (templates e módulos 100% gratuitos) e acionarem reserva emergencial de 250k manpower.
  - `localisation/english/baianagem_player_l_english.yml`: Localização completa em inglês codificada em UTF-8 com BOM.
  - `common/scripted_effects/MBR_contingency.txt`: Stub de contingência para `MBR_grant_level_one_technologies`, silenciando 369 erros de efeito desconhecido na inicialização.
- **Migração Cronológica — Fase 1 (Fundação de Motor & Isolamento)**:
  - `common/defines/01_defines.lua`: Injetado `START_DATE = "1911.6.1.12"`, `END_DATE = "1924.1.1.1"`, `BASE_RESEARCH_YEAR = 1911` e `MAX_AHEAD_RESEARCH_PENALTY = 2.5`.
  - `descriptor.mod`: Adicionado `replace_path = "events"` para blindar o mod contra o carregamento acidental de eventos vanilla de WW2.
  - `common/bookmarks/the_gathering_storm.txt`: Reconstruído integralmente para o cenário oficial de 1911 (*La Belle Époque*), com potências imperiais e constitucionais corretas.
  - `common/scripted_effects/MBR_contingency.txt`: Atualizado pacote inicial de tecnologias para fuzis históricos básicos e suporte de 1911.
- **Migração Cronológica — Fase 2 (Saneamento Territorial em `history/states/`)**:
  - `history/states/*.txt` (216 arquivos modificados): Purgados integralmente todos os 234 blocos datados de WW2 (`1939.1.1`, `1938.10.25`, `1938.3.12`, `1939.3.14`, `1938.9.30`, `1939.4.12`, `1936.3.7`, `1936.11.9`, `1936.6.1`, `1939.3.22`).
  - Realinhamento territorial de 1911: Líbia Otomana (8 estados) e Dodecaneso transferidos para `TUR` com reivindicação italiana; Rumélia Balcânica (Albânia, Macedônia, Kosovo, Trácia, Epiro, Ilhas do Egeu) transferida para `TUR`; Montenegro estabelecido como reino soberano (`MNT`); Galícia Oriental transferida para `AUS`; norte da China desmarcado de tags comunistas para autoridade imperial `CHI`.
  - Validação estrita de chaves (`{ }`): zero erros de balanceamento em todos os 1.101 estados do jogo.
- **Migração Cronológica — Fase 3 (Saneamento Diplomático e Histórico de Países)**:
  - `history/countries/*.txt` (337 arquivos modificados, 18.212 linhas deletadas):
    - Purgados todos os blocos datados anacrônicos de `2029.1.1 = { }` e `2026.1.1 = { }` herdados do Blitzkrieg/MBR modern mod.
    - Corrigidas anomalias estruturais de chaves órfãs (`}`) em 18 arquivos de países herdados (`ALB`, `BEL`, `BRM`, `CAM`, `CYP`, `EST`, `HOL`, `IRE`, `KYR`, `LAT`, `LUX`, `MAC`, `MAL`, `MOL`, `MON`, `NEP`, `SLV`, `TAJ`).
    - Alinhamento diplomático de 1911: Tríplice Aliança configurada com Alemanha, Áustria-Hungria e Itália (`add_to_faction = ITA`); removidos prematuramente Bulgária e Império Otomano da facção inicial.
    - Remoção de tratados de não-agressão de WW2 e bandeiras anacrônicas (`olympics_1936`).
    - Capitais históricas de 1911 restauradas: Império Otomano em Constantinopla (`capital = 797`) e Império Russo em São Petersburgo (`capital = 195`).
    - Removida declaração de guerra prematura do Japão contra a China (`JAP` vs `CHI`).
    - Purgadas ideias órfãs do MBR (`MBR_Central_Powers` em TUR/BUL, `MBR_USA_fast_food_monopoly` nos EUA).
    - Validação sintática: 100% dos 369 arquivos de países verificados com zero erros de chaves (`diff = 0`).
- **Migração Cronológica — Fase 4 (Líderes Históricos de 1911 & Saneamento Eleitoral)**:
  - `history/countries/*.txt` (369 arquivos modificados):
    - Substituição integral de chefes de Estado modernos (Trump, Macron, Starmer, Merz, Hitler, Van Der Bellen, Putin, Meloni, Erdogan, Ishiba, Lula, Milei, Lai Ching-te, etc.) por líderes históricos de 1911:
      - EUA: William Howard Taft (`1908.11.3`)
      - Reino Unido: H. H. Asquith / Jorge V (`1910.12.19`)
      - França: Armand Fallières (`1910.5.8`)
      - Alemanha: Kaiser Wilhelm II (`1907.1.25`)
      - Áustria-Hungria: Imperador Franz Joseph I (`1911.1.1`)
      - Rússia: Czar Nicolau II (`1907.11.14`)
      - Itália: Giovanni Giolitti / Vítor Emanuel III (`1909.3.7`)
      - Império Otomano: Sultão Mehmed V (`1908.12.1`)
      - Japão: Imperador Meiji (`1908.5.15`)
      - Brasil: Marechal Hermes da Fonseca (`1910.3.1`)
      - Argentina: Roque Sáenz Peña (`1910.3.13`)
      - China: Regência do Príncipe Zaifeng / Dinastia Qing (`1911.1.1`)
      - Potências regionais atualizadas: Sérvia (Pedro I), Grécia (Venizelos), Bulgária (Fernando I), Romênia (Carol I), Montenegro (Nicolau I), Bélgica (Alberto I), Holanda (Guilhermina), Suíça (Marc Ruchet), Noruega (Haakon VII), Dinamarca (Frederico VIII), Portugal (Teófilo Braga), México (León de la Barra), Canadá (Wilfrid Laurier), Austrália (Andrew Fisher), Nova Zelândia (Joseph Ward), África do Sul (Louis Botha), Índia/Raj (Lord Hardinge), Pérsia (Ahmad Shah), Sião (Rama VI), Etiópia (Menelik II), Cuba (José Miguel Gómez).
    - Saneamento eleitoral global: 100% das 378 datas de eleições anacrônicas de 2024 remapeadas para o período coerente de 1907–1911.
    - Condição temporal de inicialização da Suíça atualizada para `has_start_date < 1912.01.01`.
  - `common/characters/TUR.txt`:
    - Adicionado papel de general de corpo de exército (`corps_commander`) para Mustafa Kemal Atatürk em 1911.
    - Purgados recrutamentos prematuros de personagens não nascidos em 1911 (Sabiha Gökçen, Adnan Menderes).
    - Validação de chaves: 0 erros em todos os 369 arquivos de países e em `TUR.txt`.

### Otimizado & Corrigido
- **Defines & Pacing de Rede (Multiplayer)** (`c92c0a8`):
  - Inversão fatal corrigida em `01_defines.lua`: `LAG_DAYS_FOR_LOWER_SPEED = 3` e `LAG_DAYS_FOR_PAUSE = 10`.
  - Adicionado atraso de 0.02s à Velocidade 5 para impedir host runaway e catch-up lag.
  - Distribuído o processamento de eventos com `EVENT_PROCESS_OFFSET = 20`.
  - Revertido `MAX_SHARED_SLOTS = 25` em `59_defines.lua` para estancar hiperinflação de fábricas pela IA.
  - Normalizado `BASE_DEPLOYMENT_TRAINING = 1.0` em `fast_training_defines.lua` (eliminando spam de divisões pela IA).
  - Removidos arquivos quebrados `dumm_defines_copy.lua` e `NoTempCost_defines.lua`.
  - Ajustados limites de generais para suportar grandes exércitos de jogadores: `CORPS_COMMANDER_DIVISIONS_CAP = 30`, `FIELD_MARSHAL_ARMIES_CAP = 7`, `FIELD_MARSHAL_DIVISIONS_CAP = 30`.
- **Personagens & Escopos Globais** (`9b45ab9`):
  - Deletado `common/characters/MBR_generic_advisors.txt` (206.390 linhas, 14.560 conselheiros desnecessários).
  - Removido `common/on_actions/MBR_generic_advisors_on_actions.txt`.
  - Substituídos 15 escopos globais `every_character` e `any_character` por `every_country_character` e `any_country_character` em `generic_improved.txt` e `events/generic_ft.txt`.
- **Focos Nacionais, Decisões e Unidades**:
  - `common/national_focus/generic_improved.txt`: Removidas 7 chamadas destrutivas a `load_focus_tree` e `mark_focus_tree_layout_dirty = yes`. Desativado foco órfão `HABSBURG_part_of_something_bigger`.
  - `common/on_actions/4rs_on_actions.txt`: Removido script que concedia 4 slots globalmente para a IA.
  - `common/decisions/formable_nation_decisions.txt`: Adicionado `is_ai = no` a todas as 148 decisões de nações formáveis, eliminando mais de 9.700 verificações diárias da IA e preservando acesso integral aos jogadores.
  - `common/decisions/generic_ft_decisions.txt`: Adicionado `allowed = { is_ai = no }` em `generic_ft_claim_state_decision` e corrigido bug de flag `coring_state_generic` -> `claiming_state_generic`.
  - `common/on_actions/Sv_core_claim.txt`: Adicionado filtro de jogador humano (`CONTROLLER = { is_ai = no }`) na varredura mensal de coring, eliminando o congelamento mensal de 1.100 estados.
  - `common/units/`: Removido `GEN_helicopter.txt` e desativada sub-unidade `air_assault` em `@bm-divisional.txt` que requisitavam equipamentos inexistentes (`helicopter_equipment`).
  - `common/ideas/specialforces_ideas.txt` & `specialforces_decisions.txt`: Corrigidas 2 chaves não fechadas, convertidos comentários `--` para `#` e restrito acesso à IA.

---

## [0.1.0-heritage] - 2026-09-28
- Commit inicial `e746c28` (*BrunoLindoRoludo*):
  - Cópia base de arquivos de mapa, história, interface e defines herdados.
