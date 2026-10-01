---
name: hoi4-localisation-bilingual
description: >-
  Specialized localisation engine for Hearts of Iron IV bilingual text (English and
  Brazilian Portuguese l_braz_por). Enforces mandatory UTF-8 BOM encoding, Paradox YAML
  syntax, text styling color codes, path badges, and automated missing key detection.
---

# HOI4 Bilingual Localisation & Text Engineering

This skill provides the mandatory syntax rules, character encoding standards, text styling codes, and automated validation tools for authoring dual-language (English and Brazilian Portuguese) localisation in Hearts of Iron IV.

Use this skill whenever creating or editing names, descriptions, and tooltips for focus trees, events, decisions, ideas, characters, or country names.

---

## 1. The Clausewitz YAML & UTF-8 BOM Mandate

Paradox's Clausewitz engine uses a custom YAML variant with strict, non-negotiable rules:

### A. The Byte Order Mark (BOM) Rule
> [!CAUTION]
> **Mandatory UTF-8 with BOM (`\xef\xbb\xbf`)**:
> Every single `.yml` file in `localisation/` MUST start with the 3-byte sequence `0xEF, 0xBB, 0xBF`.
> - If saved as standard UTF-8 (without BOM), all accented characters (`ã`, `ç`, `é`, `ô`, `ü`, `ö`) will render as corrupted gibberish in-game (e.g., `Ã©`, `Ã§`) or cause the game engine to discard the entire file!

### B. Header Declaration
The very first line must contain the language identifier, followed by a colon and immediate newline, with **NO leading whitespace**:
- For English: `l_english:`
- For Brazilian Portuguese: `l_braz_por:`

### C. Key-Value Formatting
```yaml
l_english:
 FOCUS_ID:0 "Focus Title Text"
 FOCUS_ID_desc:0 "Long historical description text goes here in quotes."
```
- Indentation: Exactly 1 or 2 spaces before the key.
- Version index: `:0` (or `:1`) is required directly after the key name.
- Text content: Must be enclosed in straight double quotes `""`.

---

## 2. Forbidden Syntax & Common Traps

1. **Never Use Lua Comments (`--`)**:
   - Lua comments like `-- comment` will break the YAML parser, causing all subsequent keys to be ignored!
   - Only standard hash comments `# comment` are supported.
2. **Never Use "Smart" or Curly Quotes (`“`, `”`, `‘`, `’`)**:
   - Copy-pasting text from Google Docs, Word, or AI outputs frequently introduces curly quotes (`U+201C`, `U+201D`).
   - The engine does not recognize curly quotes as delimiters. Always use standard ASCII double quotes `"` (`U+0022`).
3. **Escaping Internal Quotes**:
   - If a quote appears inside a description, escape it with a backslash:
     `FOCUS_ID_desc:0 "\"Gentlemen, we are at war!\" declared the Chancellor."`

---

## 3. In-Game Text Styling & Color Codes

Clausewitz supports inline color formatting codes. Always close colored text blocks with `§!` to restore default text color:

| Code | Color | Purpose | Example |
| :--- | :--- | :--- | :--- |
| `§Y` | **Yellow** | Key numbers, country names, focal concepts | `§YAlemanha§!` |
| `§G` | **Green** | Positive effects, buffs, increased stability | `§G+10% de Estabilidade§!` |
| `§R` | **Red** | Warnings, penalties, enemy nations, dangers | `§RPenalidade de -15%§!` |
| `§W` | **White** | Highlighting important quotes or formal titles | `§WTratado de Versalhes§!` |
| `§C` | **Cyan** | Research bonuses, industrial terms | `§CBônus de Pesquisa§!` |
| `§O` | **Orange** | Secondary warnings, political changes | `§OMudança de Governo§!` |
| `§!` | **Reset** | **Mandatory** closing tag for any color block | (Restores default color) |

---

## 4. Visual Path Badges (Player Clarity)

To ensure the player immediately understands the strategic implication of every focus, prepend explicit path badges in focus titles:

| Path Type | English Badge | Brazilian Portuguese Badge |
| :--- | :--- | :--- |
| **Historical Imperial** | `[Historical]` | `[Histórico]` |
| **Democratic Republic** | `[Alternative - Democratic]` | `[Alternativo - Democrático]` |
| **Socialist / Soviet** | `[Alternative - Socialist]` | `[Alternativo - Socialista]` |
| **Military Dictatorship** | `[Alternative - Military Junta]` | `[Alternativo - Junta Militar]` |
| **Colonial / Foreign** | `[Colonial]` | `[Colonial]` |

### Example Comparison:
```yaml
l_english:
 GER_found_vaterlandspartei:0 "[Alternative - Nationalist] Found the Deutsche Vaterlandspartei"
 GER_found_vaterlandspartei_desc:0 "Tired of parliamentary weakness and defeatist talk, Admiral von Tirpitz and Wolfgang Kapp rally the radical right..."

l_braz_por:
 GER_found_vaterlandspartei:0 "[Alternativo - Nacionalista] Fundar o Deutsche Vaterlandspartei"
 GER_found_vaterlandspartei_desc:0 "Cansados da fraqueza parlamentar e do discurso derrotista, o Almirante von Tirpitz e Wolfgang Kapp unem a direita radical..."
```

---

## 5. Automated Localisation Linter & Mirror Check

Always run the bilingual linter before committing changes:
```powershell
python scripts/lint_yaml_bom.py --loc "localisation/"
```

The script audits:
1. Valid UTF-8 BOM byte marker (`\xef\xbb\xbf`) on 100% of files.
2. Zero Lua comments (`--`).
3. Zero curly/smart quotes (`“`, `”`).
4. Key parity between `english` and `braz_por` (reports untranslated or missing keys).
