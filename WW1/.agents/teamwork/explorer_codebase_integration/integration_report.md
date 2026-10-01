# WW1 Mod: German Empire Codebase & Integration Baseline Report

**Date**: 2026-10-01  
**Author**: Mod Codebase & Integration Explorer (`explorer_codebase_integration`)  
**Mod Root**: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`  
**Active Steam Target**: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`  
**Master Plan Reference**: `PLANO_FOCUS_TREE_ALEMANHA_WW1.md`  

---

## 1. Executive Summary

This report establishes the complete technical and structural baseline for integrating the new **German Empire National Focus Tree** (*Deutsches Kaiserreich*) into the Hearts of Iron IV mod *Baianagem-WW1*.

All seven core subsystems—national focus files, national spirits/ideas, diplomatic/historical events, map state IDs and provinces, localization conventions, character definitions, and Steam Workshop synchronization—have been thoroughly audited.

Key positive baseline findings:
- The mod's existing crisis, tactical decisions, and on-action architecture (`ww1_crisis_on_actions.txt`, `ww1_tactical_decisions.txt`, `ww1_national_decisions.txt`) already contains native mechanics for Turnip Winter relief, chemical gas warfare, Stosstruppen assault, unrestricted submarine warfare, and the Kaiserschlacht offensive.
- `common/national_focus/germany.txt` is an intentionally placed 67-byte placeholder stub (`# MBR 1911: intentionally empty; every country uses generic_focus.`) ready to be replaced with the custom German focus tree.
- Map state boundaries for all key German metropolitan territories, European border regions (Liège, French Lorraine, Luxembourg), and all German colonial possessions in Africa, China (Kiautschou/Qingdao), and the Pacific are cleanly identified with exact IDs and victory points.

---

## 2. National Focus Files (`common/national_focus/`)

### 2.1 Current State of `germany.txt`
- **File**: `WW1/common/national_focus/germany.txt`
- **Size**: 67 bytes
- **Content**:
  ```pdx
  # MBR 1911: intentionally empty; every country uses generic_focus.
  ```
- **Context**: The mod author disabled all vanilla country trees by replacing them with 67-byte comment stubs, forcing countries to use generic trees until unique WW1 trees are implemented. A backup file `germany.txt.disabled` (45,381 bytes) exists in the directory.

### 2.2 Active Focus Trees in the Mod
The only active focus trees currently loaded in `common/national_focus/` are:
1. `generic.txt` (45,887 bytes, `id = generic_focus`, `default = no`)
2. `generic_improved.txt` (325,057 bytes, `default = yes`)
3. `improved_generic_tree.txt` (120,628 bytes, `default = yes`)
4. `rcp_vanilla_generic_tree.txt` (47,789 bytes)
5. `habsburg_joint.txt` (78,787 bytes, Austro-Hungarian joint tree)

### 2.3 Focus Tree Integration Header Requirement
To activate the new German focus tree specifically for Germany (`GER`) and override generic trees, `germany.txt` must declare:
```pdx
focus_tree = {
	id = german_focus
	country = {
		factor = 0
		modifier = {
			add = 10
			tag = GER
		}
	}
	default = no
	reset_on_civilwar = no

	initial_show_position = {
		focus = GER_agadir_crisis_gambit
	}

	# Focuses follow here...
}
```

### 2.4 Bookmark Preview Synchronization
In `WW1/common/bookmarks/the_gathering_storm.txt` (date `1911.6.1.12`), Germany currently displays generic focuses in the bookmark screen:
```pdx
focuses = {
	generic_army_effort
	generic_industrial_effort
	generic_naval_effort
	political_sphere
}
```
**Recommendation**: Update this block to highlight key starting German focuses:
```pdx
focuses = {
	GER_agadir_crisis_gambit
	GER_tirpitz_fourth_naval_bill
	GER_execute_schlieffen_plan
	GER_aufmarsch_ost_focus
}
```

---

## 3. National Spirits & Ideas (`common/ideas/`)

### 3.1 Existing German Ideas
In `WW1/common/ideas/ww1_national_modifiers.txt` and `MBR_Central_Powers.txt`, Germany's starting and crisis ideas are fully defined with valid modifiers:

| Idea ID | Defined In | Initial Status | Key Modifiers / Effects |
| :--- | :--- | :--- | :--- |
| `MBR_Central_Powers` | `MBR_Central_Powers.txt` | Active at start | `-15% Consumer Goods, +20% Construction Speed` |
| `GER_grosser_generalstab` | `ww1_national_modifiers.txt` (L9) | Active at start | `+25% Plan Speed, +20% Max Planning, +10% Army Org` |
| `GER_krupp_chemical_conglomerates` | `ww1_national_modifiers.txt` (L20) | Active at start | `+15% Factory Output, +15% Mil Factory Speed, +8% Research` |
| `GER_tirpitz_naval_ambition` | `ww1_national_modifiers.txt` (L30) | Active at start | `+15% Dockyard Output, +10% Capital Ship Attack` |
| `GER_encirclement_paranoia` | `ww1_national_modifiers.txt` (L40) | Active at start | `+15% War Support, +8% Supply Consumption` |
| `GER_burgfrieden_social_peace` | `ww1_national_modifiers.txt` (L51) | Active at start | `+10% Stability, +10% Political Power` |
| `GER_turnip_winter_crisis_3` | `ww1_national_modifiers.txt` (L61) | Triggered via event | `-15% Stability, -10% War Support, -20% Factory Output, +10% CG, -15% Org` |
| `GER_turnip_winter_crisis_2` | `ww1_national_modifiers.txt` (L74) | Stage 2 relief | `-8% Stability, -5% War Support, -10% Factory Output, +5% CG, -8% Org` |
| `GER_turnip_winter_crisis_1` | `ww1_national_modifiers.txt` (L86) | Stage 1 relief | `-3% Stability, -5% Factory Output, +2% CG` |
| `GER_hindenburg_program_victory` | `ww1_national_modifiers.txt` (L96) | Final victory | `+12% Factory Output, +5% Army Org, +10% War Support` |
| `chemical_gas_disruption` | `ww1_national_modifiers.txt` (L106)| Tactical gas | `-30% Army Org, -25% Army Morale, -20% Defense` |
| `german_infiltration_assault_idea`| `ww1_national_modifiers.txt` (L869)| Stosstruppen | `+15% Breakthrough, +10% Soft Attack, +0.5 Recon, +10% Initiative` |
| `GER_kaiserschlacht_idea` | `ww1_national_modifiers.txt` (L883)| Spring Offensive | `+15% Attack, +20% Breakthrough, +15% Soft Attack, +10% Speed, +25% Plan` |
| `jihad_holy_call_idea` | `ww1_national_modifiers.txt` (L911)| Pan-Islamic | `+10% War Support, +15% Morale, +5% Recruitable Pop` |

### 3.2 Dynamic Modifiers (`common/dynamic_modifiers/ww1_dynamic_modifiers.txt`)
- `GER_u_boat_economic_stranglehold_modifier`:
  Applies `-15% industrial_capacity_factory` and `+10% consumer_goods_factor` to `ENG` when flag `suffering_u_boat_blockade` is set.
- `ENG_distant_blockade_modifier`:
  Applies `-10% industrial_capacity_factory` and `+8% consumer_goods_factor` to blockade targets.

### 3.3 Missing Ideas Required by the Focus Tree Plan
The following ideas are referenced in the focus tree plan and need to be defined:
1. `GER_schlieffen_momentum`:
   ```pdx
   GER_schlieffen_momentum = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           army_speed_factor = 0.15
           breakthrough_factor = 0.20
       }
   }
   ```
2. `GER_silent_dictatorship_ohl`:
   ```pdx
   GER_silent_dictatorship_ohl = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           stability_factor = 0.15
           political_power_gain = -0.10
       }
   }
   ```

---

## 4. Events System (`events/`)

### 4.1 Existing Events
1. `WW1_Agadir.txt` (1,216 bytes):
   - Namespace: `ww1_agadir`
   - `ww1_agadir.1`: German gunboat SMS Panther arrives in Agadir. Triggered when `tag = GER` and `NOT = { has_global_flag = agadir_crisis_happened }`. Fires events to `FRA` (`ww1_agadir.2`) and `ENG` (`ww1_agadir.3`).
2. `ww1_national_crises.txt` (5,902 bytes):
   - Namespace: `ww1_crisis`
   - `ww1_crisis.1`: German Turnip Winter & Entente Blockade crisis event. Adds `GER_turnip_winter_crisis_3` and sets flag `GER_crisis_active`.
3. `Germany.txt` and `WUW_Germany.txt`:
   - Both are 0-byte blank files placed to disable vanilla WW2 events.

### 4.2 Event Integration Requirements for Focus Tree
To support the diplomatic and military decisions in the German tree, custom events should be placed in `events/ww1_germany_events.txt` (or added to `events/Germany.txt`) with namespace `ww1_ger`:
1. `ww1_ger.1` — **The Blank Cheque to Vienna**:
   - Informs Austria-Hungary (`AUS`) of unconditional German backing; escalates Sarajevo crisis.
2. `ww1_ger.2` — **Schlieffen Ultimatum to Belgium**:
   - Belgium refuses transit -> Germany declares war on Belgium & Luxembourg -> Great Britain (`ENG`) receives treaty violation event.
3. `ww1_ger.3` — **Aufmarsch Ost Reassurance to London**:
   - Germany guarantees Belgian neutrality -> Britain remains neutral in 1914.
4. `ww1_ger.4` — **Treaty of Brest-Litovsk**:
   - Peace with Russia -> Releases Ober Ost (`GER_ober_ost`), Poland (`POL`), and Ukraine (`UKR`).
5. `ww1_ger.5` — **Björkö 2.0 Proposal to Russia**:
   - Re-establishes Russo-German alliance, breaks with Vienna, creates Berlin-St. Petersburg pact.
6. `ww1_ger.6` — **Reichstag Peace Resolution**:
   - Diplomatic peace conference in Switzerland for white peace.
7. `ww1_ger.7` — **Spartakusaufstand**:
   - Wilhelm II abdicates; proclamation of socialist republic (`GER_socialist`).
8. `ww1_ger.8` — **Hajj Wilhelm Jihad**:
   - Ottoman Sultan proclaims global holy war in coordination with Berlin.

---

## 5. Comprehensive Map State & Province Index

The following table provides verified state IDs, state names, victory points, and current owners/cores from `history/states/` for all areas affected by the German tree:

### 5.1 German Metropolitan Core States
| Region | State ID | File | Key VPs / Cities | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Capital (Berlin / Brandenburg)** | `64` | `64-Brandenburg.txt` | Berlin (VP 6463, 50 VP) | National Capital |
| **Ruhr & Westphalia** | `57` | `57-Westfalen.txt` | Dortmund, Essen | Industrial Heart, Krupp |
| **Rhineland** | `42` | `42-Rhineland.txt` | Cologne (Köln - VP 6554) | Heavy Industry |
| **Moselland** | `51` | `51-Moselland.txt` | Koblenz, Trier | Western defense |
| **Nassau / Hesse** | `55` | `55-Nassau.txt` | Frankfurt am Main | Central Germany |
| **Eupen-Malmedy** | `1085` | `1085-Eupen-Malmedy.txt`| Malmedy | Border with Belgium |
| **Bavaria (Upper)** | `53` | `53-Oberbayern.txt` | Munich (München - VP 693) | Southern command |
| **Bavaria (Franconia)** | `54` | `54-Bayreuth.txt` | Nuremberg (Nürnberg) | Industry |
| **Baden** | `50`, `978` | `50-Baden.txt`, `978` | Karlsruhe, Mannheim | Rhine border |
| **Württemberg** | `52` | `52-Wuttemberg.txt` | Stuttgart | South-West |
| **Weser-Ems / Wilhelmshaven** | `56` | `56-Weser-Ems.txt` | Wilhelmshaven (VP 241, 5 VP), Münster | High Seas Fleet base |
| **Schleswig-Holstein / Kiel** | `58` | `58-Schleswig - Holstein.txt`| Kiel (VP 6389, 10 VP), Hamburg (VP 9347, 20 VP) | Imperial naval shipyards |
| **South Schleswig** | `909` | `909-South Schleswig.txt` | Flensburg | Border with Denmark |
| **North Schleswig (Sønderjylland)** | `912` | `912-Sonderjylland.txt` | Aabenraa | German in 1911 |
| **East Hannover** | `59` | `59-Ost - Hannover.txt` | Hannover | North |
| **South Hannover** | `60` | `60-Sud-Hannover.txt` | Göttingen, Braunschweig | Center |
| **Mecklenburg** | `61` | `61-Mecklenburg.txt` | Rostock, Schwerin | Baltic Coast |
| **Pomerania** | `62` | `62-Pommern.txt` | Stettin, Stralsund | Baltic Coast |
| **Saxony** | `65` | `65-Sachsen.txt` | Leipzig (VP 6484), Dresden | Centenary of Leipzig 1913 |
| **Lower Silesia (Niederschlesien)**| `66` | `66-Niederschlesien.txt` | Breslau (Wrocław) | Coal & Industry |
| **Upper Silesia (Oberschlesien)**| `67` | `67-Oberschlesien.txt` | Oppeln (Opole) | Silesian coalfields |
| **Katowice (Upper Silesia border)**| `762` | `762-Katowice.txt` | Katowice | German core in 1911 |
| **West Prussia** | `63` | `63-WestPrussen.txt` | Thorn (Toruń), Bromberg | Vistula Valley |
| **Danzig** | `85` | `85-Danzig.txt` | Danzig (Gdańsk) | Imperial port |
| **Gdynia** | `807` | `807-Gdynia.txt` | Gdynia | Baltic coast |
| **Posen / Wartheland** | `68`, `86` | `68-Wartheland.txt`, `86` | Posen (Poznań) | Eastern borderland |
| **East Prussia (South - Warmia)** | `5` | `5-Germany.txt` | Allenstein (VP 6375, 3 VP) | Battle of Tannenberg |
| **East Prussia (North - Königsberg)**| `763` | `763-Konigsberg.txt` | Königsberg (VP 6342) | Baltic stronghold |
| **Memel (Klaipėda)** | `188` | `188-Memel.txt` | Memel (VP 3341) | Northernmost German city |
| **Alsace-Lorraine (Reichsland)** | `28` | `28-Alcase.txt` | Strasbourg, Metz (VP 9559) | Fortified border with France |

### 5.2 Western Front Target States (Schlieffen Plan & Borders)
| Region / State | State ID | Current Owner | Strategic Role in Focus Tree |
| :--- | :--- | :--- | :--- |
| **Wallonie (Liège)** | `34` | `BEL` | Contains Liège (VP 11519, 10 VP, level 10 fort). Target of `GER_smash_liege_forts`. |
| **Flanders (Brussels)** | `6` | `BEL` | Brussels (Capital of Belgium). Target of Schlieffen sweep. |
| **Antwerp** | `977` | `BEL` | Major Belgian naval port and fortress. |
| **Ardennes** | `980` | `BEL` | Southern Belgian forested approach. |
| **Luxembourg** | `8` | `LUX` | Luxembourg City (VP 6583). Target of initial invasion. |
| **French Lorraine (Briey-Longwy / Nancy)**| `17` | `FRA` | Nancy (VP 11516), Briey iron basin. Target of Vaterlandspartei annexation. |
| **Pas-de-Calais** | `29` | `FRA` | Channel ports (Dunkirk, Calais). Race to the Sea. |
| **Champagne** | `18`, `27` | `FRA` | Reims, Verdun sector. Trench warfare stagnation. |
| **Île-de-France (Paris)** | `16` | `FRA` | Paris (French Capital). Target of Kaiserschlacht 1918. |

### 5.3 German Overseas Colonies
| Territory | State ID | In-Game Name / File | Historical Context |
| :--- | :--- | :--- | :--- |
| **Deutsch-Ostafrika (Tanganyika)** | `546` | `546-Tanganyika.txt` | Lettow-Vorbeck guerrilla resistance theater |
| **Ruanda** | `768` | `768-Rwanda.txt` | Part of Deutsch-Ostafrika |
| **Urundi (Burundi)** | `769` | `769-Burundi.txt` | Part of Deutsch-Ostafrika |
| **Deutsch-Südwestafrika (Namibia)** | `541` | `541-South West Africa.txt` | Windhoek, diamond/copper deposits |
| **Kamerun** | `773` | `773-Cameroon.txt` | Douala port (naval base), rubber |
| **Neukamerun (French Congo border)** | `1088` | `1088-German Congo.txt` | Ceded by France after Agadir Crisis 1911 |
| **Neukamerun (Gabon border)** | `1086` | `1086-German Gabon.txt` | Ceded by France after Agadir Crisis 1911 |
| **Neukamerun (Chad border)** | `1087` | `1087-German Chad.txt` | Ceded by France after Agadir Crisis 1911 |
| **Neukamerun (Oubangui-Chari border)**| `1089` | `1089-German Central Africa.txt`| Ceded by France after Agadir Crisis 1911 |
| **Northern Cameroon (Nigeria border)** | `1084` | `1084-German Nigeria.txt`| Northern savanna border |
| **Togoland** | `777` | `777-Togo.txt` | Kamina wireless radio station |
| **German Ghana (Togoland border)** | `1097` | `1097-German Ghana.txt` | Western Togoland strip |
| **Kiautschou (Qingdao / Tsingtau)** | `743` | `743-Qingdao.txt` | East Asia Squadron naval base (von Spee) |
| **Kaiser-Wilhelmsland (New Guinea)** | `1101` | `1101 - Interior New Guinea.txt`| Pacific colony |
| **Bismarck Archipelago (Neu-Pommern)**| `737` | `737-New Britain.txt` | Rabaul harbor |
| **Bougainville (Solomon Islands)** | `1070` | `1070 - Bougainville.txt` | German Solomon Islands |
| **German Samoa** | `726` | `726-Samoa.txt` | Apia naval station |
| **Nauru** | `725` | `725-Nauru.txt` | Phosphate mining |
| **Marshall Islands** | `633` | `633-Marshall Islands.txt`| Pacific Micronesia |
| **Caroline Islands** | `684` | `684-Caroline Islands.txt`| Pacific Micronesia |
| **Mariana Islands (Saipan)** | `646` | `646-Saipan.txt` | Pacific Micronesia |
| **Palau** | `647` | `647-Palau.txt` | Western Pacific |

### 5.4 Eastern European Target States (Brest-Litovsk & Puppet Release)
| Entity | Country Tag | Key State IDs |
| :--- | :--- | :--- |
| **Kingdom of Poland** | `POL` | `10` (Warsaw), `87` (Lodz), `88` (Kielce), `92` (Lublin), `98` (Mazurskie) |
| **Ukrainian Hetmanate** | `UKR` | `193` (Kiev), `192` (Odessa), `221` (Kharkov), `201` (Zhytomyr), `227` (Stalino) |
| **Ober Ost / Baltic States** | `GER_ober_ost` / `LIT` / `LAT` / `EST` | Lithuania: `11`, `189`, `814`, `815`<br>Latvia: `12`, `190`, `808`, `809`, `810`<br>Estonia: `13`, `191`, `811`, `812`, `813` |

### 5.5 Austrian German Lands (Großdeutschland 1915 Annexation)
| Region | State ID | Name / File |
| :--- | :--- | :--- |
| **Lower Austria / Vienna** | `4` | `4-Austria.txt` (Vienna VP 6632) |
| **Upper Austria (Linz)** | `152` | `152-Upper Austria.txt` (Linz VP 9662) |
| **Tyrol & Salzburg** | `153` | `153-Tyrol.txt` (Innsbruck, Salzburg) |
| **Vorarlberg** | `848` | `848-Voralberg.txt` (Bregenz) |
| **Styria & Carinthia** | `976` | `976 - Steiermark Karnten.txt` (Graz, Klagenfurt) |
| **Burgenland** | `975` | `975 - Burgenland.txt` (Eisenstadt) |

---

## 6. Localisation System (`localisation/`)

### 6.1 Format & Directory Conventions
- English localisation directory: `WW1/localisation/english/`
- Brazilian Portuguese localisation directory: `WW1/localisation/braz_por/`
- Target file names:
  - `ww1_germany_focus_l_english.yml`
  - `ww1_germany_focus_l_braz_por.yml`

### 6.2 Encoding Requirements
- **Encoding**: UTF-8 with BOM (Byte Order Mark: `0xEF, 0xBB, 0xBF`).
- Line 1 declaration:
  - English: `l_english:`
  - Portuguese: `l_braz_por:`
- Key indent: exactly 1 space before key name.
- Standard pattern:
  ```yaml
  l_english:
   GER_agadir_crisis_gambit:0 "The Panther's Leap in Agadir"
   GER_agadir_crisis_gambit_desc:0 "In July 1911, the deployment of the gunboat SMS Panther..."
  ```

---

## 7. Characters & Cosmetic Tags

### 7.1 Existing Characters (`common/characters/GER.txt`)
Only 4 leaders are currently defined:
1. `GER_wilhelm_ii` (ideology: `despotism`, trait: `autocrat`)
2. `GER_friedrich_ebert` (ideology: `liberalism`)
3. `GER_karl_liebknecht` (ideology: `marxism`)
4. `GER_wolfgang_kapp` (ideology: `fascism_ideology`)

### 7.2 Missing Characters Required by Focus Tree
The following characters should be added to `common/characters/GER.txt`:
1. `GER_paul_von_hindenburg`: Field Marshal & Head of Government for OHL Silent Dictatorship.
2. `GER_erich_ludendorff`: General / Corps Commander (Offensive Doctrine, Planner).
3. `GER_theobald_von_bethmann_hollweg`: Civilian Chancellor for Reformist Volkskaiserreich.
4. `GER_rosa_luxemburg`: Country leader for Spartakusbund Socialist Republic.

### 7.3 Cosmetic Tags Status (`common/countries/cosmetic.txt`)
- Existing German tags: `GER_german_empire`, `GER_german_monarchy`, `GER_german_kaiserreich`, `GER_german_monarchy_liberal`, `GER_german_monarchy_democratic`, `GER_peoples_republic`, `GER_german_socialist_union`.
- Missing tags:
  - `GER_ober_ost`: Military administration flag/name for Baltic territories.
  - `GER_socialist`: Proletarian republic under Spartakusbund.
  - Integration recommendation: Add definitions for `GER_ober_ost` and `GER_socialist` in `cosmetic.txt`.

---

## 8. Steam Workshop Active Mirror (`3809191491`)

### 8.1 Current Status
- Target directory: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`
- `descriptor.mod` verified:
  ```mod
  version="1.19"
  tags={ "Alternative History" }
  name="Baianagem WW1"
  supported_version="1.19.3.0"
  remote_file_id="3809191491"
  ```
- Subdirectories present: `common`, `events`, `gfx`, `history`, `interface`, `localisation`, `map`, `music`.
- `common/national_focus/germany.txt` in the Steam directory is currently identical to the local development copy (68 bytes, comment stub).

### 8.2 Synchronization Strategy
Whenever files are updated in the local development repository (`C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`), Robocopy mirroring must be executed to keep the Steam copy 100% in sync without corrupting `descriptor.mod` or Steam metadata.

---

## 9. Actionable Integration Checklist for Downstream Implementers

| Subsystem | File Target | Required Action |
| :--- | :--- | :--- |
| **Focus Tree** | `common/national_focus/germany.txt` | Replace 67-byte stub with full German tree with `id = german_focus` and `tag = GER`. |
| **Bookmark** | `common/bookmarks/the_gathering_storm.txt` | Replace generic focus previews under GER with key WW1 German focus IDs. |
| **Ideas** | `common/ideas/ww1_national_modifiers.txt` | Add `GER_schlieffen_momentum` and `GER_silent_dictatorship_ohl`. |
| **Events** | `events/ww1_germany_events.txt` | Add diplomatic events for Agadir resolution, Belgian ultimatum, Blank Cheque, and Brest-Litovsk. |
| **Characters** | `common/characters/GER.txt` | Add Hindenburg, Ludendorff, Bethmann-Hollweg, and Rosa Luxemburg. |
| **Cosmetics** | `common/countries/cosmetic.txt` | Add `GER_ober_ost` and `GER_socialist`. |
| **Interface** | `interface/ww1_germany_goals.gfx` | Register all `GFX_...` sprite entries. |
| **Graphics** | `gfx/interface/goals/` | Copy required WW1 focus icon textures from workshop repository `3106240385`. |
| **Localisation**| `localisation/english/ww1_germany_focus_l_english.yml`<br>`localisation/braz_por/ww1_germany_focus_l_braz_por.yml` | Write complete English & Portuguese focus descriptions in UTF-8 BOM. |
| **Sync** | Steam directory `3809191491` | Mirror all changes to active Steam Workshop directory. |
