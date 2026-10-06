# Regras Permanentes: Política de Ativos Visuais e GFX

## 1. Ordem de Prioridade de Arte
1. **Arte de Época da Steam Workshop (Prioridade 1):**
   - Buscar e colher ícones de foco, ideias e quadros de eventos nos mods WW1 instalados/doadores (TGWR, FFU2).
   - Verificar correspondência temática e integridade visual.
2. **Geração de Imagem por IA (Estritamente Restrita):**
   - Reservada EXCLUSIVAMENTE para marcos narrativos centrais, como super eventos e telas de apresentação de abertura.
   - Proibido gerar lotes de dezenas de ícones de focos ou ideias por IA para evitar consumo inútil de quota e inconsistência de estilo.

## 2. Invariantes de Interface e Texturas
- **Proibição de Mascaramento:** Nunca criar falsas variedades recolorindo minimamente um mesmo ícone ou renomeando o mesmo asset com nomes diferentes.
- **Registro Obrigatório em .gfx:** Todo ícone referenciado em código (`icon = GFX_...`, `picture = GFX_...`) DEVE ter sua entrada `spriteType` correspondente em um arquivo `.gfx` dentro de `interface/`.
- **Formato e Resolução Padrão:**
   - Ícones de foco: 88x88 px (DDS DXT5 ou PNG 32-bit com canal alfa limpo).
   - Quadros de evento: 450x250 px (DDS ou PNG).
   - Ideias e espíritos nacionais: 64x64 px.
   - Retratos de generais/líderes: 156x210 px (formato Paradox DDS/PNG).
