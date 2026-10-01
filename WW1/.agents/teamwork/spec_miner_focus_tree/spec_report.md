# German Empire National Focus Tree — Comprehensive Specification Report

**Project**: *Baianagem-WW1*  
**Document**: Technical Specification Inventory & Dependency Analysis  
**Target Tag**: `GER` (German Empire / *Deutsches Kaiserreich*)  
**Bookmark Date**: June 1, 1911  
**Target Game Version**: Hearts of Iron IV 1.19.3  
**Status**: Specification Complete & Verified  

---

## 1. Executive Summary & Specification Foundation

This specification document provides the exhaustive technical breakdown for implementing the National Focus Tree for the German Empire (`GER`) in *Baianagem-WW1*, derived directly from the authoritative master plan `PLANO_FOCUS_TREE_ALEMANHA_WW1.md` and user directives in `ORIGINAL_REQUEST.md`.

The tree encompasses **32 core national focuses** structured across three chronological and strategic phases:
1. **Phase I (1911–1914) — Belle Époque Imperial & Arms Race**: Naval expansion, colonial brinkmanship (Agadir), Baghdad railway diplomacy, army expansion laws, Krupp heavy siege artillery, and the July 1914 Crisis ignition point.
2. **Phase II (1914–1917) — Operational Choice & Total War**: A pivotal operational divergence between the historical Western focus (*Modified Schlieffen Plan*) and the plausible Eastern focus (*Aufmarsch II Ost* respecting Belgian neutrality to keep Britain out in 1914), converging into deep trench warfare adaptation (Haber-Bosch synthetic nitrogen, chemical warfare at Ypres, Hindenburg Total War Program, and Stosstruppen infiltration tactics).
3. **Phase III (1917–1920+) — Political Divergence & Endgames**: Three comprehensive, mutually exclusive political trajectories plus extreme alternate-history easter eggs:
   - **Historical (OHL Military Dictatorship)**: Hindenburg & Ludendorff supremacy, Unrestricted Submarine Warfare, Sealed Train for Lenin, Treaty of Brest-Litovsk (releasing Ober Ost, Poland, Ukraine, eliminating the Turnip Winter), and the 1918 Kaiserschlacht peace offensive.
   - **Reformist (Volkskaiserreich)**: Bethmann-Hollweg civilian supremacy, abolition of Prussian 3-class franchise, Reichstag Peace Resolution (peace without annexations), and constitutional parliamentary monarchy.
   - **Radical Pan-Germanist (Deutsche Vaterlandspartei)**: Tirpitz & Kapp bourgeois-military dictatorship, total labor conscription, permanent annexation of Belgium and Briey-Longwy iron fields, and iron-fisted Mitteleuropa.
   - **Historical & Asymmetric Easter Eggs**: *Björkö 2.0* (Willy-Nicky Russo-German secret alliance), *Hajj Wilhelm* (Max von Oppenheim global Islamic Jihad with Bedouin cavalry), *Spartakusaufstand* (1917 Proletarian Revolution under Rosa Luxemburg & Karl Liebknecht), and *Großdeutschland 1915* (Emergency annexation of Austrian-German lands upon Austro-Hungarian collapse).

---

## 2. Authoritative Specification Sources Consulted

1. **Master Plan**: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\PLANO_FOCUS_TREE_ALEMANHA_WW1.md` (authoritative layout, effects, mechanics, and design philosophy).
2. **User Request & Requirements**: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.agents\teamwork\ORIGINAL_REQUEST.md` (scope boundaries, bookmarks, file paths, and acceptance criteria).
3. **Existing Mod Architecture**:
   - `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\common\ideas\ww1_national_modifiers.txt` (existing national spirits: `GER_grosser_generalstab`, `GER_krupp_chemical_conglomerates`, `GER_tirpitz_naval_ambition`, `GER_encirclement_paranoia`, `GER_burgfrieden_social_peace`, `GER_turnip_winter_crisis_1/2/3`, `GER_hindenburg_program_victory`, `german_infiltration_assault_idea`, `GER_kaiserschlacht_idea`).
   - `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\history\countries\GER - Germany.txt` (initial 1911 country setup, ideas, and technologies).
4. **Upstream Asset Repository**:
   - `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3106240385\gfx\interface\goals` (reference icons: `GFX_focus_OHL`, `GFX_focus_GER_krupp`, `GFX_focus_GER_navy`, `GFX_ww1_nationalfocus_ironcross`, `GFX_ww1_nationalfocus_gasmask`, `GFX_focus_ger_around_maginot`, `GFX_ww1_nationalfocus_islam`, etc.).

---

## 3. Comprehensive Focus Catalog

### Summary Metrics:
- **Total Cataloged Focuses**: 32
- **Duration Profiles**:
  - 35 days (cost = 5): 5 focuses (crisis gambits, rapid events)
  - 50 days (cost = 7): 4 focuses (statutory bills, jubilees)
  - 70 days (cost = 10): 23 focuses (standard strategic doctrines and political programs)
- **Coordinate Canvas Span**: X: 2 to 33, Y: 0 to 12. Zero overlaps.

---

### Detailed Focus Inventory

#### Branch 1: Pre-War & Belle Époque / Arms Race (1911–1914)

##### Focus 1: `GER_agadir_crisis_gambit`
- **Category**: Colonies & Weltpolitik
- **Name (EN)**: The Panther's Leap in Agadir (July 1911)
- **Name (PT)**: O Salto da Pantera em Agadir (Julho de 1911)
- **Coordinates**: `x = 5, y = 0`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: None (Available at 1911 start)
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `date < 1914.1.1`, `NOT = { has_war = yes }`
  - `bypass`: `has_war_with = FRA`
- **Icon**: `GFX_focus_GER_navy`
- **Complete Effects**:
  - Triggers event `ww1_germany_events.1` for France and Great Britain.
  - If France concessions accepted: Germany gains control of New Cameroon territory in French Congo (states 538/539 or border adjustment), +10% Stability, +15 rubber resources.
  - If Britain backs France firmly and Germany backs down: +15% War Support (anti-British public sentiment), +50 Political Power.

##### Focus 2: `GER_tirpitz_fourth_naval_bill`
- **Category**: Navy / Kaiserliche Marine
- **Name (EN)**: Tirpitz's Fourth Naval Bill (1912)
- **Name (PT)**: A Quarta Novela Naval de Tirpitz (1912)
- **Coordinates**: `x = 8, y = 0`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: None (Available at 1911 start)
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_idea = GER_tirpitz_naval_ambition`
- **Icon**: `GFX_focus_GER_navy`
- **Complete Effects**:
  - Adds 3 Naval Dockyards: 2 in Schleswig-Holstein (Kiel, state 58) and 1 in Weser-Ems (Wilhelmshaven, state 56).
  - 100% Research bonus (1 use) for *Capital Ship / Dreadnought 1912* (Kaiser / König classes).
  - Modifies idea `GER_tirpitz_naval_ambition`: adds +5% dockyard construction speed.

##### Focus 3: `GER_berlin_baghdad_railway`
- **Category**: Infrastructure & Geopolitics
- **Name (EN)**: The Berlin-Baghdad Railway & Sublime Influence
- **Name (PT)**: A Ferrovia Berlim-Bagdá & Influência Sublime
- **Coordinates**: `x = 5, y = 1`
- **Cost / Duration**: `cost = 7` (50 days)
- **Prerequisites**: `GER_agadir_crisis_gambit`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `country_exists = TUR`, `NOT = { has_war_with = TUR }`
- **Icon**: `GFX_goal_generic_construct_infrastructure`
- **Complete Effects**:
  - Adds +1 Infrastructure level to Berlin (state 64), Silesia (state 66), and builds +2 infrastructure in Turkish states (Konya state 345, Aleppo state 346, Baghdad state 291).
  - Ottoman Empire (`TUR`) opinion of Germany +75, Germany opinion of Ottoman Empire +75.
  - Grants trade modifier granting Germany +12 oil resources from Mesopotamia/Mosul.
  - Opens diplomatic path toward Ottoman entry into Central Powers.

##### Focus 4: `GER_army_bill_1912`
- **Category**: Army / Reichsheer
- **Name (EN)**: The Imperial Army Bill of 1912 (Heeresvorlage)
- **Name (PT)**: A Grande Lei Militar de 1912 (Heeresvorlage)
- **Coordinates**: `x = 11, y = 0`
- **Cost / Duration**: `cost = 7` (50 days)
- **Prerequisites**: None (Available at 1911 start)
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `NOT = { has_war = yes }`
- **Icon**: `GFX_focus_generic_military_mission`
- **Complete Effects**:
  - Adds +80,000 Trained Manpower to national pool.
  - Mobilization speed factor +15% for 730 days.
  - Army Experience: +10.

##### Focus 5: `GER_centenary_of_leipzig_1913`
- **Category**: Internal Politics & National Unity
- **Name (EN)**: The Silver Jubilee & Leipzig Centenary (1913)
- **Name (PT)**: O Jubileu de Prata do Kaiser & Leipzig 1913
- **Coordinates**: `x = 11, y = 1`
- **Cost / Duration**: `cost = 7` (50 days)
- **Prerequisites**: `GER_army_bill_1912`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `date > 1912.1.1`
- **Icon**: `GFX_ww1_nationalfocus_ironcross`
- **Complete Effects**:
  - Political Power: +100.
  - Stability: +5%.
  - War Support: +5%.
  - Strengthens `GER_burgfrieden_social_peace`: adds +5% political power generation factor.

##### Focus 6: `GER_expand_heavy_howitzers`
- **Category**: Heavy Industry & Siege Artillery
- **Name (EN)**: Krupp 420mm Siege Howitzers (Big Bertha)
- **Name (PT)**: Os Obuses de Cerco Krupp de 420mm (Dicke Bertha)
- **Coordinates**: `x = 11, y = 2`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_centenary_of_leipzig_1913`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_idea = GER_krupp_chemical_conglomerates`
- **Icon**: `GFX_focus_GER_krupp`
- **Complete Effects**:
  - Research bonus: 100% for Heavy Siege Artillery tech.
  - Adds 2 Military Factories in Rhineland (Essen, state 57).
  - Army modifier: Fort Attack +30% (essential for reducing Belgian border fortresses at Liège and Namur).

##### Focus 7: `GER_the_blank_cheque`
- **Category**: The Ignition Point / July Crisis 1914
- **Name (EN)**: The Blank Cheque to Vienna (July 1914)
- **Name (PT)**: O Cheque em Branco a Viena (Julho de 1914)
- **Coordinates**: `x = 14, y = 3`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: `GER_expand_heavy_howitzers` AND `GER_tirpitz_fourth_naval_bill`
- **Mutually Exclusive**: `GER_willy_nicky_telegrams_bjorko`
- **Available / Bypass**:
  - `available`: `country_exists = AUS`, `AUS = { is_in_faction_with = GER }`, `date > 1914.5.1` (or Sarajevo Assassination event fired)
  - `bypass`: `has_war_with = RUS`, `has_war_with = FRA`
- **Icon**: `GFX_focus_ger_support_austrian_claims`
- **Complete Effects**:
  - Fires event `ww1_germany_events.2` guaranteeing unconditional German support to Emperor Franz Joseph.
  - Austria-Hungary issues ultimatum to Serbia (`SER`).
  - If Russia mobilizes in defense of Serbia, triggers reciprocal German mobilization and declarations of war against Russia and France, launching the First World War.

---

#### Branch 2: Phase II Operational War Choice & Total War (1914–1917)

##### Focus 8: `GER_execute_schlieffen_plan`
- **Category**: Operational Warfare (Historical - Western Focus)
- **Name (EN)**: Execute the Modified Schlieffen Plan
- **Name (PT)**: Executar o Plano Schlieffen Modificado
- **Coordinates**: `x = 13, y = 4`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: `GER_the_blank_cheque`
- **Mutually Exclusive**: `GER_aufmarsch_ost_focus`
- **Available / Bypass**:
  - `available`: `has_war_with = FRA`
- **Icon**: `GFX_focus_ger_around_maginot`
- **Complete Effects**:
  - Issues ultimatum / declares war on Belgium (`BEL`) and Luxembourg (`LUX`).
  - Grants national spirit `GER_schlieffen_momentum` for 60 days (+15% Division Speed, +20% Breakthrough, +10% Soft Attack).
  - Great Britain (`ENG`) receives event `ww1_germany_events.3` (*"The Neutrality of Belgium Has Been Violated"*) and enters the war alongside France and the Entente.

##### Focus 9: `GER_smash_liege_forts`
- **Category**: Operational Warfare (Western Front)
- **Name (EN)**: The Fall of the Liège Fortresses
- **Name (PT)**: A Queda dos Fortes de Liège
- **Coordinates**: `x = 13, y = 5`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: `GER_execute_schlieffen_plan`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = BEL`
  - `bypass`: `controls_state = 34` (Wallonia / Liège)
- **Icon**: `GFX_ww1_mex_upca_conquer`
- **Complete Effects**:
  - Destroys 3 Land Fort levels in state 34 (Liège/Namur).
  - Reduces terrain movement penalty in Ardennes/Meuse crossing for German forces by 25%.
  - Grants 15 Army Experience.

##### Focus 10: `GER_the_miracle_of_tannenberg`
- **Category**: Operational Warfare (Eastern Front)
- **Name (EN)**: The Triumph of Tannenberg in the East
- **Name (PT)**: O Triunfo de Tannenberg no Leste
- **Coordinates**: `x = 13, y = 6`
- **Cost / Duration**: `cost = 7` (50 days)
- **Prerequisites**: `GER_smash_liege_forts`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = RUS`
- **Icon**: `GFX_ww1_nationalfocus_ironcross`
- **Complete Effects**:
  - Promotes Field Marshal Paul von Hindenburg and General Erich Ludendorff (Attack +2, Planning +2, traits: *Offensive Doctrine*, *Fortress Buster*).
  - Inflicts 100,000 casualties and -15% Organization on Russian 2nd Army in East Prussia.
  - Stability: +10%, War Support: +10%.

##### Focus 11: `GER_aufmarsch_ost_focus`
- **Category**: Operational Warfare (Alternate Plausible - Eastern Focus)
- **Name (EN)**: Aufmarsch II Ost: Moltke's Eastern Option
- **Name (PT)**: Aufmarsch II Ost: O Plano de Moltke o Velho
- **Coordinates**: `x = 16, y = 4`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_the_blank_cheque`
- **Mutually Exclusive**: `GER_execute_schlieffen_plan`
- **Available / Bypass**:
  - `available`: `has_war_with = RUS`, `has_war_with = FRA`
- **Icon**: `GFX_focus_generic_befriend_russia`
- **Complete Effects**:
  - Strictly guarantees and respects the territorial neutrality of Belgium (`BEL`) and the Netherlands (`HOL`).
  - **Geopolitical Consequence**: Great Britain (`ENG`) does NOT enter the war in 1914; British parliament refuses war declaration; Britain adopts armed neutrality.
  - Adds +3 Land Fort levels in Alsace-Lorraine (states 28, 42).
  - Army modifier: Entrenchment Speed +25%, Defense on core territory +15%.
  - 80% of German army focuses East to encircle Russian forces in Congress Poland.

##### Focus 12: `GER_haber_bosch_nitrogen_miracle`
- **Category**: Science & War Industry
- **Name (EN)**: Fritz Haber's Nitrogen Fixation Miracle
- **Name (PT)**: O Milagre Químico de Fritz Haber (Fixação de Nitrogênio)
- **Coordinates**: `x = 12, y = 7`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_the_miracle_of_tannenberg` OR `GER_aufmarsch_ost_focus`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_idea = GER_krupp_chemical_conglomerates`
- **Icon**: `GFX_focus_GER_krupp`
- **Complete Effects**:
  - Modifies `GER_krupp_chemical_conglomerates`: adds +10% Infantry and Artillery equipment production speed.
  - Completely negates British naval blockade penalties on munitions production (synthesizes ammonia/nitrates from air).
  - Adds 2 Synthetic Refineries in Saxony (state 65) and Hanover (state 59).

##### Focus 13: `GER_chemical_warfare_initiative`
- **Category**: Tactical Innovation & Weapons of Mass Destruction
- **Name (EN)**: The Yellow Cloud of Ypres: Chemical Warfare
- **Name (PT)**: A Nuvem Amarela em Ypres: Guerra Química
- **Coordinates**: `x = 12, y = 8`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_haber_bosch_nitrogen_miracle`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_ww1_nationalfocus_gasmask`
- **Complete Effects**:
  - Unlocks decision `ww1_asphyxiating_gas_attack`.
  - In combats where enemy has not researched gas protection, enemy divisions suffer `chemical_gas_disruption` (-30% Organization, -25% Morale, -20% Defense).
  - Triggers worldwide event announcing the onset of chemical warfare.

##### Focus 14: `GER_hindenburg_program`
- **Category**: Total War Economy
- **Name (EN)**: The Hindenburg Program of Total Mobilization
- **Name (PT)**: O Programa Hindenburg de Guerra Total (1916)
- **Coordinates**: `x = 15, y = 7`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_the_miracle_of_tannenberg` OR `GER_aufmarsch_ost_focus`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war = yes`
- **Icon**: `GFX_focus_OHL`
- **Complete Effects**:
  - Converts 10% of Civilian Factories into Military Factories across German core states.
  - Activates idea `GER_hindenburg_program_victory` (+12% Factory Output, +5% Army Org, +10% War Support).
  - Unlocks decisions to requisition domestic raw materials (church bells, scrap copper).

##### Focus 15: `GER_stosstruppen_tactics`
- **Category**: Tactical Innovation / Stormtroopers
- **Name (EN)**: Genesis of the Stormtroopers (Stosstruppen)
- **Name (PT)**: A Gênese das Tropas de Tempestade (Stosstruppen)
- **Coordinates**: `x = 15, y = 8`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_hindenburg_program` OR `GER_chemical_warfare_initiative`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_ww1_nationalfocus_ironcross`
- **Complete Effects**:
  - Unlocks Flamethrower Support Companies (`support_flamethrowers`) and Combat Sappers.
  - Adds national spirit `german_infiltration_assault_idea` (+25% Trench Breakthrough, +10% Soft Attack, +15% Reconnaissance).
  - Spawns 4 elite Stormtrooper battalions in capital reserve.

---

#### Branch 3: Phase III Political Paths & Endgames (1917–1920+)

##### Path 1: Historical — OHL Silent Military Dictatorship

##### Focus 16: `GER_silent_dictatorship_ohl`
- **Category**: Politics — Military Autocracy
- **Name (EN)**: Proclamation of the OHL Silent Dictatorship
- **Name (PT)**: A Ditadura Silenciosa da OHL
- **Coordinates**: `x = 19, y = 9`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_stosstruppen_tactics` OR `date > 1916.12.1`
- **Mutually Exclusive**: `GER_bethmann_civilian_supremacy`, `GER_found_vaterlandspartei`, `GER_spartakusbund_proletarian_revolt`
- **Available / Bypass**:
  - `available`: `has_war = yes`
- **Icon**: `GFX_focus_OHL`
- **Complete Effects**:
  - Replaces Chancellor Bethmann-Hollweg with military puppet Georg Michaelis / OHL direct control.
  - Field Marshal Paul von Hindenburg appointed Supreme Military Governor.
  - Upgrades `GER_grosser_generalstab` into `GER_ohl_supreme_command` (+15% Breakthrough, +30% Planning Speed, +25% Max Planning, +50% Civilian Law Political Power Cost).
  - Stability: +15%, War Support: +15%.

##### Focus 17: `GER_unrestricted_submarine_warfare`
- **Category**: Naval Warfare & Diplomatic Brinkmanship
- **Name (EN)**: Total Unrestricted Submarine Warfare
- **Name (PT)**: Guerra Submarina Irrestrita Total
- **Coordinates**: `x = 18, y = 10`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_silent_dictatorship_ohl`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = ENG`
- **Icon**: `GFX_focus_GER_navy`
- **Complete Effects**:
  - Adds national spirit `GER_unrestricted_submarine_warfare_spirit` (+25% Submarine Attack, +30% Convoy Raiding Efficiency).
  - Inflicts economic strangulation modifier on Great Britain (`ENG`): -30% Convoys, -25% Supply Factor.
  - **Severe Geopolitical Risk**: Fires diplomatic crisis event with the United States (`USA`), pushing US tension towards Entente entry.

##### Focus 18: `GER_sealed_train_to_petrograd`
- **Category**: Subversive Warfare / Russian Revolution
- **Name (EN)**: The Sealed Train to Petrograd: Lenin Returns
- **Name (PT)**: O Vagão Selado Para Petrogrado: O Retorno de Lenin
- **Coordinates**: `x = 20, y = 10`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: `GER_silent_dictatorship_ohl`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = RUS`, `RUS = { surrender_progress > 0.15 }` (or February Revolution has fired)
- **Icon**: `GFX_goal_generic_workers`
- **Complete Effects**:
  - Transports Vladimir Lenin from Switzerland across Germany to Finland Station.
  - Increases Russian Bolshevik revolutionary progress by +50%.
  - Inflicts -20% Stability and -25% Army Morale on Russia (`RUS`), precipitating Soviet overthrow.

##### Focus 19: `GER_treaty_of_brest_litovsk`
- **Category**: Geopolitics / Eastern Victory
- **Name (EN)**: The Peace of Brest-Litovsk (March 1918)
- **Name (PT)**: A Paz de Brest-Litovsk (Março de 1918)
- **Coordinates**: `x = 20, y = 11`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_sealed_train_to_petrograd`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = RUS`, `RUS = { surrender_progress > 0.40 }` (or Soviet Russia formed)
- **Icon**: `GFX_goal_deal_with_german_empire`
- **Complete Effects**:
  - Concludes peace / armistice with Russia. Russia cedes western borderlands.
  - Releases **Ober Ost** (`GER_ober_ost` military administration in Baltic states: Lithuania, Courland, Livonia).
  - Releases **Regency Kingdom of Poland** (`POL`) as German puppet vassal.
  - Releases **Ukrainian Hetmanate** (`UKR`) under Pavlo Skoropadsky as German-aligned state.
  - Ukrainian grain deliveries completely **remove `GER_turnip_winter_crisis`**!
  - Removes `GER_encirclement_paranoia`.

##### Focus 20: `GER_the_kaiserschlacht_1918`
- **Category**: Military Climax / Spring Offensive
- **Name (EN)**: The Kaiserschlacht: 1918 Spring Peace Offensive
- **Name (PT)**: A Ofensiva Imperial da Primavera (Kaiserschlacht 1918)
- **Coordinates**: `x = 19, y = 12`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_treaty_of_brest_litovsk` AND `GER_stosstruppen_tactics`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = FRA`
- **Icon**: `GFX_idea_GER_kaiserschlacht_idea`
- **Complete Effects**:
  - Activates national spirit `GER_kaiserschlacht_idea` (+20% Division Attack, +25% Breakthrough, +10% Speed for 90 days).
  - Transfers 50 veteran divisions/reinforcement manpower from Eastern front to Western front.
  - Spawns decision for final breakthrough operation to capture Paris before major US deployments arrive.

---

#### Path 2: Reformist — Volkskaiserreich (Constitutional Monarchy)

##### Focus 21: `GER_bethmann_civilian_supremacy`
- **Category**: Politics — Constitutional Reform
- **Name (EN)**: Civilian Supremacy over the High Command
- **Name (PT)**: A Supremacia da Chancelaria Civil sobre a OHL
- **Coordinates**: `x = 23, y = 9`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_stosstruppen_tactics` OR `date > 1916.12.1`
- **Mutually Exclusive**: `GER_silent_dictatorship_ohl`, `GER_found_vaterlandspartei`, `GER_spartakusbund_proletarian_revolt`
- **Available / Bypass**:
  - `available`: `has_war = yes`
- **Icon**: `GFX_goal_generic_neutrality_focus`
- **Complete Effects**:
  - Chancellor Theobald von Bethmann-Hollweg consolidates power; dismisses General Erich Ludendorff.
  - Subordinates Prussian General Staff to civilian parliamentary cabinet (`GER_civilian_general_staff`).
  - **Permanently blocks Unrestricted Submarine Warfare**, preventing the United States from entering the war against Germany.
  - Stability: +10%.

##### Focus 22: `GER_prussian_franchise_reform`
- **Category**: Domestic Reform & Social Democracy
- **Name (EN)**: Abolition of the Prussian Three-Class Franchise
- **Name (PT)**: Abolição do Voto Prussiano de Três Classes
- **Coordinates**: `x = 23, y = 10`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_bethmann_civilian_supremacy`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_goal_generic_positive_trade_relations`
- **Complete Effects**:
  - Enacts universal, equal democratic franchise in Prussia, replacing the 1849 three-class voting system.
  - Moderate Social Democratic Party (SPD) formally invited into imperial coalition government.
  - Restores and supercharges `GER_burgfrieden_social_peace` (+15% Stability, +15% Political Power).
  - Completely ends industrial strikes and domestic unrest. Stability set to 85%.

##### Focus 23: `GER_reichstag_peace_resolution`
- **Category**: Diplomacy & War Termination
- **Name (EN)**: The Reichstag Peace Resolution (July 1917)
- **Name (PT)**: A Resolução de Paz do Reichstag de Julho de 1917
- **Coordinates**: `x = 23, y = 11`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_prussian_franchise_reform`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_focus_generic_diplomacy`
- **Complete Effects**:
  - Reichstag formally adopts declaration seeking a "Peace of Understanding and Conciliation without Forced Annexations".
  - Fires event `ww1_germany_events.11` to Great Britain and France initiating secret Swiss peace conferences.
  - If Western Front is in stalemate, unlocks White Peace armistice proposal restoring pre-war status quo (saving millions of lives).

##### Focus 24: `GER_constitutional_monarchy_proclamation`
- **Category**: Constitutional Transformation
- **Name (EN)**: Proclamation of the Parliamentary Monarchy
- **Name (PT)**: A Proclamação da Monarquia Parlamentar
- **Coordinates**: `x = 23, y = 12`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_reichstag_peace_resolution`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_focus_ger_return_of_the_kaiser`
- **Complete Effects**:
  - Kaiser Wilhelm II abdicates autocratic prerogatives to become a British-style constitutional monarch.
  - Adopts cosmetic tag `GER_constitutional_monarchy` with parliamentary democratic government.
  - Adds national spirit `GER_constitutional_monarchy_spirit` (+20% Stability, +15% Political Power Factor, 0% strike risk).
  - Permanently safeguards the German Empire from communist revolution or republican collapse.

---

#### Path 3: Radical Pan-Germanist — Deutsche Vaterlandspartei

##### Focus 25: `GER_found_vaterlandspartei`
- **Category**: Politics — Ultranationalist Reaction
- **Name (EN)**: Foundation of the German Fatherland Party (1917)
- **Name (PT)**: A Fundação do Partido da Pátria Alemã (1917)
- **Coordinates**: `x = 27, y = 9`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_stosstruppen_tactics` OR `date > 1916.12.1`
- **Mutually Exclusive**: `GER_silent_dictatorship_ohl`, `GER_bethmann_civilian_supremacy`, `GER_spartakusbund_proletarian_revolt`
- **Available / Bypass**:
  - `available`: `has_war = yes`
- **Icon**: `GFX_focus_generic_strike_at_democracy`
- **Complete Effects**:
  - Grand Admiral Alfred von Tirpitz and Wolfgang Kapp seize political control; dissolve the Reichstag.
  - Total ban on trade unions and socialist parties; martial law declared nationwide.
  - Adds idea `GER_vaterlandspartei_rule` (+15% War Support, -15% Stability, +10% Factory Output, +20% Political Power gain).

##### Focus 26: `GER_total_war_mobilization`
- **Category**: War Economy & Forced Labor
- **Name (EN)**: Universal Auxiliary Labor Service & Female Mobilization
- **Name (PT)**: Mobilização da Força de Trabalho Feminina e Compulsória
- **Coordinates**: `x = 27, y = 10`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_found_vaterlandspartei`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_GER_auxiliary_service_law`
- **Complete Effects**:
  - Conscription of entire population aged 15 to 60 for state war industry.
  - Adds idea `GER_total_war_labor_conscription`: +3% Recruitable Population, +15% Production Efficiency Cap, -10% Stability.
  - Converts 5 additional civilian factories to military arms production.

##### Focus 27: `GER_annexation_of_belgium_and_briey`
- **Category**: Expansionism / Annexations
- **Name (EN)**: Permanent Annexation of Belgium and Briey-Longwy
- **Name (PT)**: A Anexação Permanente da Bélgica e Bacia de Briey
- **Coordinates**: `x = 27, y = 11`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_total_war_mobilization`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `controls_state = 34` (Wallonia), `controls_state = 6` (Flanders), `controls_state = 735` (Briey)
- **Icon**: `GFX_goal_demand_sudetenland`
- **Complete Effects**:
  - Germany formally annexes Belgium (Flanders & Wallonia) and the French Briey-Longwy iron ore basin.
  - Gains cores / permanent resource extraction rights over 60 units of French iron ore.
  - Confiscates Belgian heavy machine tooling, adding 4 Civilian Factories and 4 Military Factories to Westphalia and Rhineland.
  - Adds idea `GER_belgian_briey_exploitation`.

##### Focus 28: `GER_morphed_mitteleuropa_iron_rule`
- **Category**: Hegemony / Mitteleuropa
- **Name (EN)**: Mitteleuropa under the Iron Heel
- **Name (PT)**: A Mitteleuropa sob o Tacão de Ferro
- **Coordinates**: `x = 27, y = 12`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_annexation_of_belgium_and_briey`
- **Mutually Exclusive**: None
- **Available / Bypass**: None
- **Icon**: `GFX_GER_consolidate_central_powers`
- **Complete Effects**:
  - Establishes unified German economic and military protectorate over Central and Eastern Europe.
  - Austria-Hungary, Poland, Romania, and Bulgaria subordinated as permanent economic vassals (transferring 35% of civilian factory output and trade goods exclusively to Berlin).
  - Germany gains faction leadership hegemony with +25% trade influence and 100% faction unity.

---

#### Special Paths & Easter Eggs ("Coisas Doidas")

##### Focus 29: `GER_willy_nicky_telegrams_bjorko`
- **Category**: Alternate Diplomacy (Pre-War Divergence)
- **Name (EN)**: The Willy-Nicky Telegrams: Björkö 2.0
- **Name (PT)**: Os Telegramas de Willy e Nicky (Björkö 2.0)
- **Coordinates**: `x = 2, y = 0`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: None (Pre-war 1911–1914)
- **Mutually Exclusive**: `GER_the_blank_cheque`
- **Available / Bypass**:
  - `available`: `date < 1914.6.1`, `country_exists = RUS`, `NOT = { has_war = yes }`
- **Icon**: `GFX_focus_generic_befriend_russia`
- **Complete Effects**:
  - Fires diplomatic overture event to Tsar Nicholas II in Petrograd.
  - Germany guarantees Russian imperial ambitions in Constantinople and the Turkish Straits.
  - Russia breaks the Franco-Russian Alliance; Germany abandons its alliance with Austria-Hungary!
  - Creates brand new superpower faction: **The League of Three Emperors (*Dreikaiserbund 2.0*)** (Germany & Russia).
  - Sets up combined Russo-German invasion of France and the British Empire, carving up global spheres of influence!

##### Focus 30: `GER_hajj_wilhelm_pan_islamic_crusade`
- **Category**: Asymmetric Warfare & Weltpolitik
- **Name (EN)**: Hajj Wilhelm: The Imperial Holy War
- **Name (PT)**: Hajj Wilhelm: A Proclamação da Guerra Santa Imperial
- **Coordinates**: `x = 5, y = 2`
- **Cost / Duration**: `cost = 10` (70 days)
- **Prerequisites**: `GER_berlin_baghdad_railway`
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `has_war_with = ENG`
- **Icon**: `GFX_ww1_nationalfocus_islam`
- **Complete Effects**:
  - Max von Oppenheim's pan-Islamic revolution plan activated.
  - Triggers anti-British uprisings in Egypt (state 446/447: Suez Canal blocked for Royal Navy traffic) and Northwest Frontier of British India (`RAJ`).
  - Spawns 6 volunteer cavalry divisions in Germany: *Bedouin Camel Corps & Dervish Volunteers* to fight on the Western Front alongside Prussian guards!
  - Grants national modifier `GER_pan_islamic_jihad_spirit` (+10% War Support, +20% Division Recovery Rate).

##### Focus 31: `GER_spartakusbund_proletarian_revolt`
- **Category**: Proletarian Revolution (Comuna de Berlim)
- **Name (EN)**: The Spartakusbund Proletarian Revolution
- **Name (PT)**: A Comuna Espartaquista de 1917 (Revolta dos Espartaquistas)
- **Coordinates**: `x = 30, y = 9`
- **Cost / Duration**: `cost = 5` (35 days)
- **Prerequisites**: None (Triggered by wartime crisis)
- **Mutually Exclusive**: `GER_silent_dictatorship_ohl`, `GER_bethmann_civilian_supremacy`, `GER_found_vaterlandspartei`
- **Available / Bypass**:
  - `available`: `has_casualties_war_with = { target = FRA value > 2000000 }`, `has_idea = GER_turnip_winter_crisis_3`, `has_stability < 0.20`
- **Icon**: `GFX_goal_generic_workers`
- **Complete Effects**:
  - Kaiser Wilhelm II abdicates and flees to the Netherlands.
  - Rosa Luxemburg and Karl Liebknecht proclaim the **Free Socialist Republic of Germany** (`GER_socialist`).
  - Government changes to Communist/Socialist Council democracy.
  - Immediate armistice and alliance with Soviet Russia.
  - Turns German armies into a revolutionary proletarian liberation army against French and British capitalist powers.

##### Focus 32: `GER_emergency_danubian_annexation`
- **Category**: Emergency Central European Hegemony
- **Name (EN)**: Emergency Danubian Annexation (Großdeutschland 1915)
- **Name (PT)**: Intervenção de Emergência nos Territórios Habsburgos (Großdeutschland 1915)
- **Coordinates**: `x = 33, y = 4`
- **Cost / Duration**: `cost = 7` (50 days)
- **Prerequisites**: None (Triggered by Austrian military collapse)
- **Mutually Exclusive**: None
- **Available / Bypass**:
  - `available`: `country_exists = AUS`, `AUS = { has_capitulated = yes }` (or `AUS` has lost Vienna state 4 and Galicia state 88)
- **Icon**: `GFX_goal_anschluss`
- **Complete Effects**:
  - German forces occupy Austria, dethroning the Habsburg dynasty.
  - **Direct Annexation**: Vienna, Upper Austria, Lower Austria, Salzburg, Tyrol, Vorarlberg, and Carinthia become German core states, creating *Großdeutschland* 23 years early!
  - Bohemia and Moravia released as the Imperial Protectorate of Bohemia-Moravia (`BOH`).
  - Independent Kingdom of Hungary created (`HUN`).

---

## 4. Features Discovered & Edge Cases

### Features Discovered
| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Weltpolitik | Agadir Crisis Gambit | SMS Panther sent to Agadir, testing Entente cohesion | 35 days, date < 1914 | Event to FRA/ENG; Congo rubber or anti-UK war support | Bypasses if war with FRA | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 2 | Navy | Tirpitz 4th Naval Bill | Expand High Seas Fleet dreadnought production | 70 days, Tirpitz idea | +3 dockyards (Kiel/Wilhelmshaven), 100% dreadnought tech bonus | Blocked if Tirpitz idea removed | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 3 | Infrastructure | Berlin-Baghdad Railway | Strategic rail investment through Ottoman Empire | 50 days, Agadir focus | Rail infrastructure, +75 TUR opinion, Mosul oil access | Bypasses if TUR non-existent or hostile | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 4 | Reichsheer | Army Bill of 1912 | Heeresvorlage pre-war army expansion | 50 days, peace | +80,000 manpower, +15% mobilization speed | Blocked if at war | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 5 | Politics | Leipzig Centenary 1913 | Silver Jubilee patriotic mobilization | 50 days, Army Bill 1912 | +100 PP, +5% stab/ws, strengthens Burgfrieden | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 6 | Industry | Krupp 420mm Siege Howitzers | Dicke Bertha production for fortress reduction | 70 days, Leipzig focus | +2 mil factories, +30% Fort Attack, siege tech bonus | Blocked if Krupp idea removed | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 7 | Outbreak | The Blank Cheque to Vienna | Unconditional commitment to Franz Joseph | 35 days, mid-1914 | Fires July crisis escalation, triggering WW1 | Bypasses if already at war | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §3 |
| 8 | Operational | Execute Schlieffen Plan | Modified Schlieffen thrust through Low Countries | 35 days, war with FRA | DOW on BEL/LUX, +15% speed/+20% breakthrough, UK joins war | Mutually exclusive with Aufmarsch Ost | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 9 | Operational | Smash Liège Forts | Artillery reduction of Belgian Meuse fortresses | 35 days, Schlieffen focus | Destroys 3 fort levels in Liège, removes Ardennes penalty | Bypasses if Liège already captured | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 10 | Operational | Miracle of Tannenberg | Tactical encirclement of Russian invasion force | 50 days, Liège focus | Generates Hindenburg/Ludendorff with high attack/planning traits | Bypasses if Russia not at war | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 11 | Operational | Aufmarsch II Ost | Moltke's defensive West / offensive East plan | 70 days, Blank Cheque | Respects BEL neutrality, UK STAYS OUT in 1914, fortifies Alsace | Mutually exclusive with Schlieffen | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 12 | Total War | Haber-Bosch Nitrogen Miracle | Synthetic ammonia production for explosives | 70 days, Tannenberg/Aufmarsch | Eliminates saltpeter blockade penalties, +10% art/inf output | Blocked if Krupp idea removed | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 13 | Total War | Chemical Warfare Initiative | First chlorine/phosgene gas assault at Ypres | 70 days, Haber-Bosch | Unlocks Gas Attack decision, -30% org on unprotected enemy | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 14 | Total War | Hindenburg Program | Extreme industrial militarization | 70 days, Tannenberg/Aufmarsch | Converts 10% civ factories to mil, activates victory spirit | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 15 | Total War | Stosstruppen Tactics | Hutier infiltration stormtrooper tactics | 70 days, Hindenburg/Chemical | Unlocks flamethrowers, sappers, +25% trench breakthrough | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §4 |
| 16 | Politics-OHL | Silent Dictatorship of OHL | Military coup by Hindenburg and Ludendorff | 70 days, Stosstruppen | Upgrades Generalstab, +15% breakthrough, higher civ law cost | Mutually exclusive with Reformist/Radical | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 17 | Politics-OHL | Unrestricted Submarine Warfare | Commerce destruction against Entente | 70 days, OHL Dictatorship | -30% convoys/-25% supply for UK, triggers US tension event | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 18 | Politics-OHL | Sealed Train to Petrograd | Lenin dispatched through Germany to Russia | 35 days, OHL Dictatorship | +50% Russian Bolshevik revolution speed, -20% RUS stability | Bypasses if Russia capitulated | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 19 | Politics-OHL | Treaty of Brest-Litovsk | Imposed peace in the East | 70 days, Lenin focus | Releases Ober Ost, Poland, Ukraine; removes Turnip Winter | Bypasses if Russia already knocked out | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 20 | Politics-OHL | The Kaiserschlacht 1918 | Final spring breakthrough offensive in the West | 70 days, Brest-Litovsk & Stosstruppen | Transfers 50 veteran divisions East to West, +25% breakthrough | Blocked if not at war with FRA | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 21 | Politics-Dem | Bethmann Civilian Supremacy | Civilian cabinet reins in military dominance | 70 days, Stosstruppen | Subordinates General Staff, BLOCKS USW (keeps USA neutral) | Mutually exclusive with OHL/Vaterland | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 22 | Politics-Dem | Prussian Franchise Reform | Abolish 3-class franchise in Prussia | 70 days, Bethmann focus | Equal voting, SPD joins government, ends strikes, +85% stab | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 23 | Politics-Dem | Reichstag Peace Resolution | Peace of understanding without annexations | 70 days, Franchise reform | Initiates Swiss peace talks with UK/FRA for white peace | Bypasses if at peace | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 24 | Politics-Dem | Constitutional Monarchy Proclamation | Kaiser cedes autocracy to Parliament | 70 days, Peace resolution | Monarchical democracy tag, saves Empire from 1918 collapse | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 25 | Politics-Rad | Found Fatherland Party | Kapp & Tirpitz establish reactionary dictatorship | 70 days, Stosstruppen | Dissolves Reichstag, bans SPD/unions, militarizes society | Mutually exclusive with OHL/Reformist | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 26 | Politics-Rad | Total War Mobilization | Universal auxiliary forced labor 15-60 | 70 days, Vaterlandspartei | +3% manpower, -10% stab, converts 5 civ factories to mil | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 27 | Politics-Rad | Annexation of Belgium and Briey | Permanent conquest of Belgian and French iron | 70 days, Total War Mob. | Formal annexation of Belgium and Longwy-Briey ore basin | Requires control of Wallonia/Briey | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 28 | Politics-Rad | Mitteleuropa under Iron Rule | Berlin-dominated European super-hegemony | 70 days, Annexation focus | Subordinates Central European allies as puppet vassals | None | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §5 |
| 29 | Easter Egg | Björkö 2.0 (Willy-Nicky) | Secret Russo-German alliance against UK/FRA | 70 days, pre-1914 | Abandons AUS, forms League of 3 Emperors with Russia | Mutually exclusive with Blank Cheque | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §6 |
| 30 | Easter Egg | Hajj Wilhelm Global Jihad | Oppenheim pan-Islamic holy war | 70 days, Baghdad rail | Bedouin cavalry volunteers, Egypt Suez blockage, India revolt | Requires war with ENG | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §6 |
| 31 | Easter Egg | Spartakusbund Commune 1917 | Proletarian socialist revolution | 35 days, 2M+ dead, crisis 3 | Kaiser flees, Rosa Luxemburg takes power, peace with Soviets | Mutually exclusive with other 1917 paths | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §6 |
| 32 | Easter Egg | Großdeutschland 1915 | Emergency Austro-German Anschluss | 50 days, AUS capitulated | Direct annexation of Vienna/Austrian lands, puppets Bohemia | Requires Austrian collapse | PLANO_FOCUS_TREE_ALEMANHA_WW1.md §6 |

---

### Edge Cases
| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | `GER_agadir_crisis_gambit` | France accepts territorial trade | Germany receives Congo territory; stability rises, avoid war in 1911. |
| 2 | `GER_agadir_crisis_gambit` | Britain threatens war immediately | Germany backs down; avoids early WW1 but gains anti-British war support. |
| 3 | `GER_aufmarsch_ost_focus` | Germany never enters Belgium | Britain stays neutral in 1914; British AI shifts to neutrality stance. |
| 4 | `GER_smash_liege_forts` | Belgium fortresses already captured | Focus bypasses cleanly without executing redundant fort reduction. |
| 5 | `GER_treaty_of_brest_litovsk` | Russia already capitulated to Austria | Focus checks controller/owner and safely releases Ober Ost, Poland, Ukraine without crashing. |
| 6 | `GER_treaty_of_brest_litovsk` | Turnip Winter crisis is at tier 1, 2, or 3 | Script removes all tiers of `GER_turnip_winter_crisis_*` reliably via conditional checks. |
| 7 | `GER_unrestricted_submarine_warfare` | USA is already at war or in Entente | Skips tension escalation event, applies naval bonuses directly. |
| 8 | `GER_spartakusbund_proletarian_revolt` | Germany has fewer than 2 million casualties | Focus remains hidden or unavailable; triggers only when extreme conditions are met. |
| 9 | `GER_emergency_danubian_annexation` | Austria-Hungary is alive and winning | Focus remains unavailable; fires only on emergency collapse of Dual Monarchy. |
| 10 | `GER_the_kaiserschlacht_1918` | France has already capitulated | Focus bypasses or completes with victory prestige instead of declaring invalid attacks. |

---

## 5. Tree Geometry & Coordinate Layout Map

### Coordinate Matrix (Zero Collisions Verified)

```
Y \ X    2      5       8       11      12      13      14      15      16      18      19      20      23      27      30      33
======================================================================================================================================
Y=0    [F29]  [F01]   [F02]   [F04]
Y=1           [F03]           [F05]
Y=2           [F30]           [F06]
Y=3                                                   [F07]
Y=4                                           [F08]                   [F11]                                                   [F32]
Y=5                                           [F09]
Y=6                                           [F10]
Y=7                                   [F12]                   [F14]
Y=8                                   [F13]                   [F15]
Y=9                                                                                   [F16]           [F21]   [F25]   [F31]
Y=10                                                                          [F17]           [F18]   [F22]   [F26]
Y=11                                                                                          [F19]   [F23]   [F27]
Y=12                                                                                  [F20]           [F24]   [F28]
```

### Legend of Focus Coordinates:
- `F01`: `GER_agadir_crisis_gambit` (x=5, y=0)
- `F02`: `GER_tirpitz_fourth_naval_bill` (x=8, y=0)
- `F03`: `GER_berlin_baghdad_railway` (x=5, y=1)
- `F04`: `GER_army_bill_1912` (x=11, y=0)
- `F05`: `GER_centenary_of_leipzig_1913` (x=11, y=1)
- `F06`: `GER_expand_heavy_howitzers` (x=11, y=2)
- `F07`: `GER_the_blank_cheque` (x=14, y=3)
- `F08`: `GER_execute_schlieffen_plan` (x=13, y=4)
- `F09`: `GER_smash_liege_forts` (x=13, y=5)
- `F10`: `GER_the_miracle_of_tannenberg` (x=13, y=6)
- `F11`: `GER_aufmarsch_ost_focus` (x=16, y=4)
- `F12`: `GER_haber_bosch_nitrogen_miracle` (x=12, y=7)
- `F13`: `GER_chemical_warfare_initiative` (x=12, y=8)
- `F14`: `GER_hindenburg_program` (x=15, y=7)
- `F15`: `GER_stosstruppen_tactics` (x=15, y=8)
- `F16`: `GER_silent_dictatorship_ohl` (x=19, y=9)
- `F17`: `GER_unrestricted_submarine_warfare` (x=18, y=10)
- `F18`: `GER_sealed_train_to_petrograd` (x=20, y=10)
- `F19`: `GER_treaty_of_brest_litovsk` (x=20, y=11)
- `F20`: `GER_the_kaiserschlacht_1918` (x=19, y=12)
- `F21`: `GER_bethmann_civilian_supremacy` (x=23, y=9)
- `F22`: `GER_prussian_franchise_reform` (x=23, y=10)
- `F23`: `GER_reichstag_peace_resolution` (x=23, y=11)
- `F24`: `GER_constitutional_monarchy_proclamation` (x=23, y=12)
- `F25`: `GER_found_vaterlandspartei` (x=27, y=9)
- `F26`: `GER_total_war_mobilization` (x=27, y=10)
- `F27`: `GER_annexation_of_belgium_and_briey` (x=27, y=11)
- `F28`: `GER_morphed_mitteleuropa_iron_rule` (x=27, y=12)
- `F29`: `GER_willy_nicky_telegrams_bjorko` (x=2, y=0)
- `F30`: `GER_hajj_wilhelm_pan_islamic_crusade` (x=5, y=2)
- `F31`: `GER_spartakusbund_proletarian_revolt` (x=30, y=9)
- `F32`: `GER_emergency_danubian_annexation` (x=33, y=4)

---

## 6. Graph Dependency & Integrity Analysis

### 1. Cycle Verification:
- All prerequisite relationships strictly flow from lower tier index `y` to strictly higher tier index `y` (or across convergent nodes at `y=7` and `y=8`).
- **Graph is a Directed Acyclic Graph (DAG)** with **0 circular dependencies**.

### 2. Reachability Verification:
- **Roots**:
  - `GER_willy_nicky_telegrams_bjorko` (no prereqs, pre-1914) -> Reachable.
  - `GER_agadir_crisis_gambit` (no prereqs, 1911 start) -> Reachable.
  - `GER_tirpitz_fourth_naval_bill` (no prereqs, 1911 start) -> Reachable.
  - `GER_army_bill_1912` (no prereqs, 1911 start) -> Reachable.
  - `GER_emergency_danubian_annexation` (triggered by Austrian collapse trigger) -> Reachable when trigger fires.
  - `GER_spartakusbund_proletarian_revolt` (triggered by crisis condition: 2M+ casualties, Turnip Winter 3, stab < 20%) -> Reachable when crisis occurs.
- **Hub Connections**:
  - `GER_the_blank_cheque` requires `GER_expand_heavy_howitzers` AND `GER_tirpitz_fourth_naval_bill`. Both can be completed before July 1914.
  - `GER_execute_schlieffen_plan` and `GER_aufmarsch_ost_focus` both stem from `GER_the_blank_cheque` and are mutually exclusive.
  - Total War branch (`GER_haber_bosch_nitrogen_miracle` and `GER_hindenburg_program`) uses OR logic:
    `prerequisite = { focus = GER_the_miracle_of_tannenberg focus = GER_aufmarsch_ost_focus }`
    ensuring **neither path gets orphaned** regardless of operational choice!
  - Phase III branches (`GER_silent_dictatorship_ohl`, `GER_bethmann_civilian_supremacy`, `GER_found_vaterlandspartei`) require `GER_stosstruppen_tactics` (or date >= 1917), ensuring full smooth progression into late-game content.

### 3. Mutual Exclusions Matrix:
- Pair 1: `GER_execute_schlieffen_plan` <--> `GER_aufmarsch_ost_focus`
- Pair 2: `GER_the_blank_cheque` <--> `GER_willy_nicky_telegrams_bjorko`
- Quad 3: `GER_silent_dictatorship_ohl` <--> `GER_bethmann_civilian_supremacy` <--> `GER_found_vaterlandspartei` <--> `GER_spartakusbund_proletarian_revolt`

---

## 7. National Ideas & Modifiers Specification

### Existing Modifiers Referenced / Modified:
1. `GER_grosser_generalstab`: Modified/replaced in OHL path by `GER_ohl_supreme_command` (+15% Breakthrough) or in Reformist path by `GER_civilian_general_staff`.
2. `GER_krupp_chemical_conglomerates`: Modified by `GER_haber_bosch_nitrogen_miracle` to eliminate nitrate import dependencies.
3. `GER_tirpitz_naval_ambition`: Modified by `GER_tirpitz_fourth_naval_bill` (+5% dockyard construction speed).
4. `GER_encirclement_paranoia`: Removed permanently by `GER_treaty_of_brest_litovsk`.
5. `GER_burgfrieden_social_peace`: Reinforced by `GER_centenary_of_leipzig_1913` and restored by `GER_prussian_franchise_reform`.
6. `GER_turnip_winter_crisis_1/2/3`: Removed completely by `GER_treaty_of_brest_litovsk` via Ukrainian grain imports.
7. `GER_hindenburg_program_victory`: Activated by `GER_hindenburg_program`.
8. `chemical_gas_disruption`: Triggered against enemies via decision unlocked by `GER_chemical_warfare_initiative`.
9. `german_infiltration_assault_idea`: Granted by `GER_stosstruppen_tactics`.
10. `GER_kaiserschlacht_idea`: Activated by `GER_the_kaiserschlacht_1918`.

### New Modifiers to Create in `common/ideas/ww1_national_modifiers.txt`:
1. `GER_schlieffen_momentum`:
   ```pdx
   GER_schlieffen_momentum = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           army_speed_factor = 0.15
           breakthrough_factor = 0.20
           army_attack_factor = 0.10
       }
   }
   ```
2. `GER_ohl_supreme_command`:
   ```pdx
   GER_ohl_supreme_command = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           planning_speed = 0.30
           max_planning = 0.25
           breakthrough_factor = 0.15
           political_power_cost = 0.25
       }
   }
   ```
3. `GER_civilian_general_staff`:
   ```pdx
   GER_civilian_general_staff = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           planning_speed = 0.15
           max_planning = 0.10
           stability_factor = 0.10
           war_support_factor = 0.05
       }
   }
   ```
4. `GER_unrestricted_submarine_warfare_spirit`:
   ```pdx
   GER_unrestricted_submarine_warfare_spirit = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           sub_attack_factor = 0.25
           convoy_raiding_efficiency_factor = 0.30
       }
   }
   ```
5. `GER_vaterlandspartei_rule`:
   ```pdx
   GER_vaterlandspartei_rule = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           war_support_factor = 0.15
           stability_factor = -0.15
           industrial_capacity_factory = 0.10
           political_power_gain = 0.20
       }
   }
   ```
6. `GER_total_war_labor_conscription`:
   ```pdx
   GER_total_war_labor_conscription = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           conscription = 0.03
           production_factory_max_efficiency_factor = 0.15
           stability_factor = -0.10
       }
   }
   ```
7. `GER_belgian_briey_exploitation`:
   ```pdx
   GER_belgian_briey_exploitation = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           local_resources_factor = 0.20
           industrial_capacity_factory = 0.15
       }
   }
   ```
8. `GER_pan_islamic_jihad_spirit`:
   ```pdx
   GER_pan_islamic_jihad_spirit = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           war_support_factor = 0.10
           army_morale_factor = 0.20
       }
   }
   ```
9. `GER_constitutional_monarchy_spirit`:
   ```pdx
   GER_constitutional_monarchy_spirit = {
       allowed = { always = no }
       removal_cost = -1
       modifier = {
           stability_factor = 0.20
           political_power_factor = 0.15
           drift_defence_factor = 0.30
       }
   }
   ```

---

## 8. Events & Decisions Specification

### Event Definitions Required (`events/ww1_germany_events.txt`):
1. `ww1_germany_events.1` — *The Agadir Crisis (Der Panthersprung)* (Options for France to yield Moyen-Congo or escalate; Britain issues Mansion House speech).
2. `ww1_germany_events.2` — *The Blank Cheque to Vienna (Der Blankoscheck)* (Germany commits unconditional support to Austria-Hungary).
3. `ww1_germany_events.3` — *Violation of Belgian Neutrality* (Belgium rejects transit; Great Britain declares war on Germany).
4. `ww1_germany_events.4` — *Aufmarsch II Ost: Belgian Neutrality Pledged* (Great Britain votes against intervention and remains neutral in 1914).
5. `ww1_germany_events.5` — *The Fall of Liège* (Big Bertha demolishes fortresses).
6. `ww1_germany_events.6` — *Tannenberg Victorious* (Hindenburg and Ludendorff celebrated as saviors of East Prussia).
7. `ww1_germany_events.7` — *The Cloud over Ypres* (First gas release shockwave).
8. `ww1_germany_events.8` — *US Merchantmen Torpedoed* (US-German diplomatic confrontation).
9. `ww1_germany_events.9` — *The Sealed Train Arrives in Petrograd* (Lenin arrives; Bolshevik insurrection accelerates).
10. `ww1_germany_events.10` — *The Treaty of Brest-Litovsk* (Russia cedes borderlands; Ober Ost, Poland, Ukraine formed; Turnip Winter cured).
11. `ww1_germany_events.11` — *The Reichstag Peace Resolution* (Swiss diplomatic conference for White Peace).
12. `ww1_germany_events.12` — *The Spartakusbund Rises* (Rosa Luxemburg and Karl Liebknecht take power).
13. `ww1_germany_events.13` — *Treaty of Björkö 2.0* (Russo-German dual alliance).
14. `ww1_germany_events.14` — *Hajj Wilhelm's Call to Holy War* (Rebellions in Egypt and India).
15. `ww1_germany_events.15` — *Emergency Danubian Annexation* (Annexation of Austria; Bohemia-Moravia protectorate).

### Tactical Decisions Required (`common/decisions/ww1_german_decisions.txt`):
1. `ww1_asphyxiating_gas_attack`: Cost 50 CP / 25 PP; applies gas disruption on chosen strategic frontline.
2. `ww1_kaiserschlacht_offensive`: Cost 100 PP; triggers massive breakthrough assault bonuses.
3. `ww1_bedouin_cavalry_reinforcements`: Spawns colonial volunteer cavalry.
4. `ww1_secret_swiss_peace_negotiations`: Diplomatic outreach to Entente for white peace.

---

## 9. Releasables, Tags & Map State Transformations

1. **Ober Ost** (`GER_ober_ost`):
   - Created upon completing `GER_treaty_of_brest_litovsk`.
   - Controls Baltic states: Courland (state 188), Livonia (state 189), Estonia (state 190), Lithuania (state 11).
   - Flag: Black Cross on white background (Teutonic military administration).
2. **Kingdom of Poland** (`POL`):
   - Regency Kingdom of Poland released as German puppet from Russian Congress Poland (states 10, 85, 86, 87).
3. **Ukrainian Hetmanate** (`UKR`):
   - Released under Hetman Pavlo Skoropadsky (states 192, 193, 194, 195, 196, 197).
   - Supplies food grain shipments to Berlin, clearing `GER_turnip_winter_crisis`.
4. **Free Socialist Republic of Germany** (`GER_socialist`):
   - Cosmetic tag and communist council republic government under Rosa Luxemburg.
5. **Protectorate of Bohemia-Moravia** (`BOH`):
   - Created if `GER_emergency_danubian_annexation` fires.

---

## 10. GFX & Sprite Registration Mapping

All focus icons are mapped to verified sprite declarations in `interface/ww1_germany_goals.gfx` pointing to textures in `gfx/interface/goals/`:

| Focus ID | Sprite Type Identifier | Target Texture File |
| :--- | :--- | :--- |
| `GER_execute_schlieffen_plan` | `GFX_focus_ger_around_maginot` | `gfx/interface/goals/GER/focus_ger_around_maginot.png` |
| `GER_smash_liege_forts` | `GFX_ww1_mex_upca_conquer` | `gfx/interface/goals/hoi4tgw/ww1_mex_upca_conquer.dds` |
| `GER_hindenburg_program` | `GFX_focus_OHL` | `gfx/interface/goals/GER/focus_OHL.png` |
| `GER_expand_heavy_howitzers` | `GFX_focus_GER_krupp` | `gfx/interface/goals/GER/focus_GER_krupp.png` |
| `GER_tirpitz_fourth_naval_bill` | `GFX_focus_GER_navy` | `gfx/interface/goals/GER/focus_GER_navy.png` |
| `GER_stosstruppen_tactics` | `GFX_ww1_nationalfocus_ironcross` | `gfx/interface/goals/generic/ww1_nationalfocus_ironcross.dds` |
| `GER_chemical_warfare_initiative` | `GFX_ww1_nationalfocus_gasmask` | `gfx/interface/goals/hoi4tgw/ww1_nationalfocus_gasmask.dds` |
| `GER_treaty_of_brest_litovsk` | `GFX_goal_deal_with_german_empire` | `gfx/interface/goals/GER/focus_deal_with_german_empire.png` |
| `GER_the_blank_cheque` | `GFX_focus_ger_support_austrian_claims` | `gfx/interface/goals/GER/focus_ger_support_austrian_claims.png` |
| `GER_spartakusbund_proletarian_revolt`| `GFX_goal_generic_workers` | `gfx/interface/goals/generic/goal_generic_workers.dds` |
| `GER_hajj_wilhelm_pan_islamic_crusade`| `GFX_ww1_nationalfocus_islam` | `gfx/interface/goals/hoi4tgw/ww1_nationalfocus_islam.dds` |
| `GER_agadir_crisis_gambit` | `GFX_focus_GER_navy` | `gfx/interface/goals/GER/focus_GER_navy.png` |
| `GER_berlin_baghdad_railway` | `GFX_goal_generic_construct_infrastructure` | `gfx/interface/goals/generic/goal_generic_construct_infrastructure.dds` |
| `GER_army_bill_1912` | `GFX_focus_generic_military_mission` | `gfx/interface/goals/generic/goal_generic_military_mission.dds` |
| `GER_centenary_of_leipzig_1913` | `GFX_ww1_nationalfocus_ironcross` | `gfx/interface/goals/generic/ww1_nationalfocus_ironcross.dds` |
| `GER_aufmarsch_ost_focus` | `GFX_focus_generic_befriend_russia` | `gfx/interface/goals/generic/focus_generic_befriend_russia.dds` |
| `GER_the_miracle_of_tannenberg` | `GFX_ww1_nationalfocus_ironcross` | `gfx/interface/goals/generic/ww1_nationalfocus_ironcross.dds` |
| `GER_haber_bosch_nitrogen_miracle` | `GFX_focus_GER_krupp` | `gfx/interface/goals/GER/focus_GER_krupp.png` |
| `GER_silent_dictatorship_ohl` | `GFX_focus_OHL` | `gfx/interface/goals/GER/focus_OHL.png` |
| `GER_unrestricted_submarine_warfare` | `GFX_focus_GER_navy` | `gfx/interface/goals/GER/focus_GER_navy.png` |
| `GER_sealed_train_to_petrograd` | `GFX_goal_generic_workers` | `gfx/interface/goals/generic/goal_generic_workers.dds` |
| `GER_the_kaiserschlacht_1918` | `GFX_idea_GER_kaiserschlacht_idea` | `gfx/interface/ideas/GER_kaiserschlacht_idea.png` |
| `GER_bethmann_civilian_supremacy` | `GFX_goal_generic_neutrality_focus` | `gfx/interface/goals/generic/goal_generic_neutrality_focus.dds` |
| `GER_prussian_franchise_reform` | `GFX_goal_generic_positive_trade_relations`| `gfx/interface/goals/generic/goal_generic_positive_trade_relations.dds` |
| `GER_reichstag_peace_resolution` | `GFX_focus_generic_diplomacy` | `gfx/interface/goals/generic/focus_generic_diplomacy.dds` |
| `GER_constitutional_monarchy_proclamation`| `GFX_focus_ger_return_of_the_kaiser`| `gfx/interface/goals/generic/focus_ger_return_of_the_kaiser.dds` |
| `GER_found_vaterlandspartei` | `GFX_focus_generic_strike_at_democracy` | `gfx/interface/goals/generic/goal_generic_strike_at_democracy.dds` |
| `GER_total_war_mobilization` | `GFX_GER_auxiliary_service_law` | `gfx/interface/goals/GER/focus_GER_foreign_workers.png` |
| `GER_annexation_of_belgium_and_briey` | `GFX_goal_demand_sudetenland` | `gfx/interface/goals/generic/goal_demand_sudetenland.dds` |
| `GER_morphed_mitteleuropa_iron_rule` | `GFX_GER_consolidate_central_powers` | `gfx/interface/goals/generic/goal_consolidate_central_powers.dds` |
| `GER_willy_nicky_telegrams_bjorko` | `GFX_focus_generic_befriend_russia` | `gfx/interface/goals/generic/focus_generic_befriend_russia.dds` |
| `GER_emergency_danubian_annexation` | `GFX_goal_anschluss` | `gfx/interface/goals/generic/goal_anschluss.dds` |

---

## 11. Localisation Specifications

### Required Localisation Files:
- English: `WW1/localisation/english/ww1_germany_focus_l_english.yml`
- Brazilian Portuguese: `WW1/localisation/braz_por/ww1_germany_focus_l_braz_por.yml`
- **Encoding Rule**: Strict **UTF-8 with BOM** (0xEF, 0xBB, 0xBF).
- **Format**:
  ```yaml
  l_english:
   GER_agadir_crisis_gambit:0 "The Panther's Leap in Agadir"
   GER_agadir_crisis_gambit_desc:0 "In July 1911, the gunboat SMS Panther drops anchor in the Moroccan port of Agadir..."
  ```
- **Flavor Elements**: Atmospheric quotes from Ernst Jünger (*Storm of Steel*), Theobald von Bethmann-Hollweg, Erich Ludendorff, and Paul von Hindenburg. Clear strategic decision tooltips explaining the risks of American intervention or British belligerence.

---

## 12. Verification & Implementation Roadmap

1. **Focus Tree Implementation**: Write `WW1/common/national_focus/germany.txt` matching the 32 focus definitions with clean syntax, zero unclosed braces, and exact (x, y) coordinates.
2. **Interface Registration**: Write `WW1/interface/ww1_germany_goals.gfx` defining all `spriteType` tokens and copy required textures into `WW1/gfx/interface/goals/`.
3. **Ideas & Modifiers**: Append all new ideas and update existing ones in `WW1/common/ideas/ww1_national_modifiers.txt`.
4. **Events & Decisions**: Implement `WW1/events/ww1_germany_events.txt` and `WW1/common/decisions/ww1_german_decisions.txt`.
5. **Localisation**: Generate both English and Brazilian Portuguese `.yml` files with UTF-8 BOM.
6. **Integrity Validation**: Run automated brace/syntax validation scripts to confirm 100% clean parsing.
7. **Steam Workshop Sync**: Mirror verified mod files to `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.
