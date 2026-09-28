# Regras Permanentes: Sintaxe e Compatibilidade HOI4 (v1.19.3)

## 1. Princípio da Verificação Obrigatória
- **Nunca inventar sintaxe**. Antes de utilizar um trigger, effect, modifier ou scope desconhecido:
  1. Localize exemplos funcionais nos arquivos da versão 1.19.3 do HOI4 ou na documentação oficial.
  2. Confirme o escopo exigido (`ROOT`, `FROM`, `PREV`, `THIS`, State scope vs Country scope).
  3. Só então implemente no mod.

## 2. Modifiers Modernos vs Legados
- **Bens de Consumo**:
  - PROIBIDO: `consumer_goods_factor = X` (obsoleto).
  - OBRIGATÓRIO: `consumer_goods_expected_value = X` (padrão moderno do HOI4).
- **Penalidades e Bônus**:
  - Verificar se o modifier ainda opera com multiplicador ou valor absoluto na versão 1.19.3.

## 3. Sistema de Personagens (Characters)
- O sistema clássico de líderes em `history/countries/` via `create_country_leader` é obsoleto para mecânicas profundas.
- Todo líder político, conselheiro, general de corpo e marechal de campo deve ser definido em `common/characters/[TAG].txt`:
  - Utilizar blocos `country_leader`, `corps_commander`, `field_marshal` e `advisor`.
  - Recrutar via `recruit_character = [TAG_token]` na história do país ou por efeito.
  - Não deixar referências a personagens não declarados.

## 4. Arquivos de Localização
- Todos os arquivos `.yml` devem:
  - Ficar exclusivamente na subpasta do idioma: `localisation/english/` (ou `braz_por/`).
  - Ter a primeira linha contendo exatamente a tag de linguagem (`l_english:`).
  - Ser salvos em **UTF-8 com BOM** (Byte Order Mark: `0xEF, 0xBB, 0xBF`).
  - Nunca usar extensão `.txt` para arquivos de localização.

## 5. Interface Gráfica e Texturas (GFX & GUI)
- Cada sprite referenciado em um arquivo `.gui` ou em script (`picture = "..."`, `icon = "..."`) deve ter um `spriteType` registrado em `interface/*.gfx`.
- Texturas devem ser mantidas em formato DDS (DXT1 para opacos, DXT5 para transparência) ou TGA para bandeiras, ou PNG 32-bit quando compatível.
- Evitar caminhos de arquivos contendo espaços em branco (ex.: evitar pastas como `gfx/host tool/`).

## 6. Comentários em Scripts
- Em arquivos de script do Paradox (`.txt`, `.gui`, `.gfx`), comentários devem começar estritamente com `#`.
- Comentários estilo Lua (`--`) ou C (`//`) são inválidos e provocam erros de leitura do parser.
