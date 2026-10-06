# Regras Permanentes: Sintaxe e Compatibilidade HOI4 (v1.19.3)

## 1. Princípio da Verificação Obrigatória
- **Nunca inventar sintaxe**. Antes de utilizar um trigger, effect, modifier ou scope desconhecido:
  1. Localize exemplos funcionais nos arquivos da versão 1.19.3 do HOI4 ou na documentação oficial.
  2. Confirme o escopo exigido (`ROOT`, `FROM`, `PREV`, `THIS`, State scope vs Country scope).
  3. Só então implemente no mod.

## 2. Modifiers Modernos vs Legados
- **Bens de Consumo**:
  - Utilizar `consumer_goods_expected_value = X` (padrão moderno HOI4) ou `consumer_goods_factor = X` conforme suporte do motor.
- **Penalidades e Bônus**:
  - Verificar se o modifier opera com multiplicador ou valor absoluto na versão 1.19.3.

## 3. Sistema de Personagens (Characters)
- O sistema clássico de líderes em `history/countries/` via `create_country_leader` é obsoleto para mecânicas profundas.
- Todo líder político, conselheiro, general de corpo e marechal de campo deve ser definido em `common/characters/[TAG].txt`:
  - Utilizar blocos `country_leader`, `corps_commander`, `field_marshal` e `advisor`.
  - Recrutar via `recruit_character = [TAG_token]` na história do país ou por efeito.
  - Não deixar referências a personagens não declarados.

## 4. Arquivos de Localização e Sobrescrita
- Todos os arquivos `.yml` devem:
  - Ficar em `localisation/english/`, `localisation/braz_por/` ou `localisation/replace/` (quando prefixados com `zz_` para garantir precedência sobre chaves do jogo base).
  - Ter a primeira linha contendo exatamente a tag de linguagem (`l_english:` ou `l_braz_por:`).
  - Ser salvos obrigatoriamente em **UTF-8 com BOM** (Byte Order Mark: `0xEF, 0xBB, 0xBF`).
  - Nunca usar extensão `.txt` para arquivos de localização.

## 5. Interface Gráfica e Texturas (GFX & GUI)
- Cada sprite referenciado em um arquivo `.gui` ou em script (`picture = "..."`, `icon = "..."`) deve ter um `spriteType` registrado em `interface/*.gfx`.
- Texturas devem ser mantidas em formato DDS (DXT1 para opacos, DXT5 para transparência) ou PNG 32-bit com canal alfa limpo.
- Evitar caminhos de arquivos contendo espaços em branco.

## 6. Comentários em Scripts
- Em arquivos de script do Paradox (`.txt`, `.gui`, `.gfx`), comentários devem começar estritamente com `#`.
- Comentários estilo Lua (`--`) ou C (`//`) são inválidos e provocam erros de leitura do parser.
