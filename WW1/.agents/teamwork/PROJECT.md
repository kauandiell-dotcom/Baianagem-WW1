# Project: German Empire National Focus Tree (WW1 Mod)

## Architecture
- **Focus Tree Module**: `WW1/common/national_focus/germany.txt` — defines `focus_tree = { id = german_focus country = { factor = 0 modifier = { add = 10 tag = GER } } ... }` with 32 historical, alt-historical, and crisis national focuses.
- **GFX & Sprite Module**: `WW1/gfx/interface/goals/` (32 RGBA DDS textures) and `WW1/interface/ww1_germany_goals.gfx` (32 standard SpriteTypes + 32 animated shine SpriteTypes).
- **Ideas & Modifiers Module**: `WW1/common/ideas/ww1_national_modifiers.txt` (or `ww1_germany_ideas.txt`) — defines starting ideas, evolved General Staff ideas, Haber-Bosch chemical bonuses, and OHL military dictatorship spirits.
- **Events & Decisions Module**: `WW1/events/ww1_germany_events.txt` — defines 15 country events for political shifts, war crises, treaties (Brest-Litovsk, Björkö, Hajj Wilhelm), and tactical choices.
- **Characters & Cosmetic Tags**: `WW1/common/characters/GER.txt` (Hindenburg, Ludendorff, Bethmann-Hollweg, Luxemburg) and `WW1/common/countries/cosmetic.txt` (`GER_ober_ost`, `GER_socialist`).
- **Localization Module**: `WW1/localisation/english/ww1_germany_l_english.yml` and `WW1/localisation/braz_por/ww1_germany_l_braz_por.yml` with UTF-8 BOM encoding.
- **Steam Workshop Mirroring**: Robocopy synchronization to `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---|---|---|---|
| 1 | Focus Icon Assets Deployment | Copy & convert 32 DDS focus icons from source workshop | M1 | Survey |
| 2 | Sprite Definitions (.gfx) | 32 base and 32 shine sprite definitions in ww1_germany_goals.gfx | M1 | Survey |
| 3 | German National Ideas & Spirits | New ideas: OHL dictatorship, Haber-Bosch, Schlieffen momentum | M2 | Survey |
| 4 | German Historical & Crisis Events | 15 country events for politics, treaties, revolutions, Easter eggs | M2 | Survey |
| 5 | Leaders & Characters Integration | Hindenburg, Ludendorff, Bethmann-Hollweg, Rosa Luxemburg | M2 | Survey |
| 6 | Cosmetic Country Tags | GER_ober_ost and GER_socialist cosmetic definitions | M2 | Survey |
| 7 | Phase I Focuses (1911-1914) | 7 pre-war focuses (Agadir, Tirpitz, Baghdad, Army Bill, Leipzig, Howitzers, Blank Cheque) | M3 | Survey |
| 8 | Phase II Focuses (1914-1917) | 8 operational choices & Total War (Schlieffen, Liège, Tannenberg, Aufmarsch Ost, Haber-Bosch, Chemical, Hindenburg, Stosstruppen) | M3 | Survey |
| 9 | Phase III Historical OHL Path | 5 focuses (Ludendorff Dictatorship, Kreuznach, Brest-Litovsk, Kaiserschlacht, Siegfriedstellung) | M3 | Survey |
| 10 | Phase III Volkskaiserreich Path | 4 focuses (Reichstag Compromise, SPD Social Monarchy, Auxiliary Law, League of Nations) | M3 | Survey |
| 11 | Phase III Vaterlandspartei Path | 4 focuses (Tirpitz Coup, Radical Annexationism, Total Mobilization, Lebensraum) | M3 | Survey |
| 12 | Phase III Easter Egg Focuses | 4 focuses (Björkö 2.0, Hajj Wilhelm, Spartakusaufstand, Großdeutschland) | M3 | Survey |
| 13 | English Localization (UTF-8 BOM) | Full English localization for 32 focuses, descriptions, ideas, events | M4 | Survey |
| 14 | Brazilian Portuguese Localization (UTF-8 BOM) | Full PT-BR localization for 32 focuses, descriptions, ideas, events | M4 | Survey |
| 15 | Static Syntax & Brace Integrity | 100% balanced braces check across all .txt, .gfx, and .yml files | M5 | Survey |
| 16 | Graph & Reference Validation | Verify 0 circular dependencies, valid state IDs, valid icons/events | M5 | Survey |
| 17 | Steam Workshop Synchronization | Mirror all updated mod files to Steam workshop target directory | M5 | Survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | Icon Assets & Sprite Definitions | Copy 32 DDS icons to `gfx/interface/goals/` and generate `interface/ww1_germany_goals.gfx` | none | DONE (32 DDS + 64 sprites, gate passed) |
| M2 | Events, Ideas, Characters & Tags | Create `events/ww1_germany_events.txt`, `common/ideas/ww1_germany_ideas.txt`, update characters and cosmetic tags | none | IN_PROGRESS (worker_m2 ea999d10) |
| M3 | German National Focus Tree | Implement all 32 focuses in `common/national_focus/germany.txt` with verified coordinates, triggers, and effects | M1, M2 | PLANNED |
| M4 | Dual Localization (EN & PT-BR) | Create `localisation/english/ww1_germany_l_english.yml` and `localisation/braz_por/ww1_germany_l_braz_por.yml` (UTF-8 BOM) | M3 | PLANNED |
| M5 | Syntax Verification, Test Suite & Workshop Mirroring | Automated brace checking, graph validation, and Robocopy sync to Steam Workshop | M1, M2, M3, M4 | PLANNED |

## Interface Contracts
### Focus Tree ↔ GFX Sprites
- Every focus `icon = GFX_<name>` must correspond to an exact `spriteType = { name = "GFX_<name>" texturefile = "gfx/interface/goals/<name>.dds" }` in `interface/ww1_germany_goals.gfx`.
- Textures must exist in `gfx/interface/goals/` as valid RGBA DDS files.

### Focus Tree ↔ Events & Modifiers
- Every `country_event = { id = <event_id> }` must exist in `events/ww1_germany_events.txt` under `namespace = ww1_ger`.
- Every `add_ideas = <idea_id>` must be defined in `common/ideas/ww1_national_modifiers.txt` or `common/ideas/ww1_germany_ideas.txt`.
- Every state ID in effects must match verified IDs: Liège (34), French Lorraine (17), Westphalia (57), Rhineland (42), Berlin (64), Allenstein (5), Kiel (58), Wilhelmshaven (56), Cameroon (773), Neukamerun (1088).

### Localisation Contract
- File names: `localisation/english/ww1_germany_l_english.yml` and `localisation/braz_por/ww1_germany_l_braz_por.yml`.
- Header: `l_english:` on line 1 for English, `l_braz_por:` on line 1 for PT-BR.
- Encoding: UTF-8 with BOM (`\xef\xbb\xbf`).
- Keys: Every focus must have `<focus_id>:0 "Name"` and `<focus_id>_desc:0 "Description"`. Every idea must have `<idea_id>:0 "Name"` and `<idea_id>_desc:0 "Description"`. Every event must have `<event_id>.t:0 "Title"`, `<event_id>.d:0 "Desc"`, `<event_id>.a:0 "Option"`.

## Code Layout
- `WW1/common/national_focus/germany.txt`
- `WW1/interface/ww1_germany_goals.gfx`
- `WW1/gfx/interface/goals/*.dds`
- `WW1/common/ideas/ww1_germany_ideas.txt`
- `WW1/events/ww1_germany_events.txt`
- `WW1/common/characters/GER.txt`
- `WW1/common/countries/cosmetic.txt`
- `WW1/localisation/english/ww1_germany_l_english.yml`
- `WW1/localisation/braz_por/ww1_germany_l_braz_por.yml`
- Target Steam Mirror: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`
