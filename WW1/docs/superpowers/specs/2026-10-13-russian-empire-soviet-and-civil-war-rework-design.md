# Design Document: Russian Empire, Russian Revolution & Soviet/White Civil War Overhaul

**Date:** 2026-10-13  
**Target Tag(s):** `SOV` (Russian Empire / Soviet Russia), `WHT` (All-Russian Provisional Government / White Movement)  
**Bookmark:** 1911.6.1 (WW1 Baianagem Mod)  
**Status:** Approved by User  

---

## 1. Intent and The Why

The Russian Empire (`SOV`) in Baianagem-WW1 is currently plagued by critical architectural flaws:
1. **Broken Revolution Trigger & Bogus Events:** The Russian Revolution script in `ww1_ger_rus_rework_events.txt` relies on generic HOI4 `start_civil_war`, spawning an unplayable dynamic revolter (`D01`) without historical generals or orders of battle. If Russia goes democratic (Kerensky), the civil war fails to trigger entirely. Key historical events for Alexander Kolchak and Pyotr Wrangel are mere text buttons granting flat army experience or winning the war in two days by text flag (`set_country_flag = SOV_civil_war_won`), without real map fighting.
2. **Dead-End Soviet Progression:** The Bolshevik path in `common/national_focus/soviet.txt` contains only 7 focuses and terminates abruptly at `SOV_war_communism_decrees`. There is no dedicated Soviet focus tree, no GOELRO electrification, no Red Army doctrine, and no post-revolution content.
3. **Missing Leadership Cast:** 15+ vital historical Bolshevik and White leaders (Leon Trotsky, Joseph Stalin, Mikhail Frunze, Felix Dzerzhinsky, Semyon Budyonny, Mikhail Tukhachevsky, Georgy Chicherin, Pyotr Wrangel, etc.) are unrecruited in `common/characters/SOV.txt`, despite graphics assets existing on disk.
4. **Fragile Economy & Attrition Imbalance:** Imperial Russia is treated as an empty punchbag that either collapses helplessly to German blitzkrieg or lacks industrial autonomy. Conversely, if buffed carelessly, it risks rolling over the Central Powers and starving the Western Front of action.

This rework replaces the broken legacy scripts from scratch, delivering:
- A functional, interactive **Pre-Revolutionary Crisis Engine (Late 1915 – Mid 1917)** with dynamic visual UI indicators in the Decisions tab.
- Player/bot agency to **avert the revolution** through skilled imperial reforms, or let it erupt and **choose between the Red Army (Soviet Russia) or the White Movement**.
- A dual trigger for Lenin's return: early proactive **German Sealed Train Decision (late 1915/1916)** with an autonomous **Early 1917 Historical Fallback Event** if Germany did not take the decision.
- A multi-front **Russian Civil War Engine** with dedicated country tag `WHT`, authentic regional fronts (Kolchak in Siberia, Denikin/Wrangel in the South, Yudenich in the Northwest), robust OOBs, and initial neutral independence for peripheral states (Finland, Ukraine, Poland, Caucasus).
- Clean, decoupled diplomatic mechanics with the Central Powers: historical **Treaty of Brest-Litovsk** option for the Soviets to exit WW1 and focus on the civil war, while the Whites fight on with non-belligerent Entente proxy intervention backing.
- Distinct, complete focus trees for the **Russian Empire**, **Soviet Russia**, and the **White Movement**, complete with bilingual localization (EN & PT-BR, UTF-8 BOM), GFX shine icons, and automated QA test suite verification.

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
- **G1: Crisis & Revolution Agency:** Averting or triggering the Revolution must be a dynamic, skill-driven process based on 4 bounded gauges (`SOV_revolutionary_tension`, `SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`), influenced by German subversive decisions starting in late 1915 or the 1917 domestic fallback.
- **G2: Meaningful Player Choice:** Upon revolution eruption, the player receives an event prompt to take command of either **Soviet Russia (`SOV`)** or the **White Movement (`WHT`)**.
- **G3: Strategic Depth & Anti-Blitz Attrition:** Harsh terrain, *Rasputitsa* mud seasons, and scorched earth mechanics must prevent the Central Powers from easily overrunning Russia during 1914–1918. Foreign invasion of Russia must be a grueling, high-attrition quagmire requiring heavy garrisons.
- **G4: Western Front Primacy:** Russia must possess sufficient industrial autonomy (coal, steel, ammunition, rifles) to maintain its front line, but offensive stats must be carefully bounded so Russia cannot single-handedly crush Germany/Austria-Hungary or ruin the Western Front balance in multiplayer.
- **G5: Dedicated Bespoke Focus Trees:**
  - Base Russian Empire tree in `soviet.txt` purged of legacy 1917 broken stubs, streamlined to 1911–1917 Imperial governance with real economic rewards.
  - Dedicated Soviet Russia tree (`soviet_russia_focus`, ~75-85 focuses) loaded upon Bolshevik victory/takeover.
  - Dedicated White Movement tree (`white_russia_focus`, ~55-65 focuses) for `WHT`.
- **G6: Visual Transparency & UI:** The player and AI must always see the exact state of unrest, hunger, and revolutionary danger via decision-tab progress bars and tooltips. No surprise hidden thresholds.
- **G7: Historical Flavor & Cast:** Full character recruitment and traits for Trotsky, Stalin, Frunze, Dzerzhinsky, Budyonny, Tukhachevsky, Chicherin, Bukharin, Kolchak, Denikin, Wrangel, and Yudenich.

### Non-Goals
- **NG1:** We are not extending the mod's timeline into the late 1930s or WW2. All Soviet and White content is strictly focused on the WW1 bookmark, Civil War (1917–1922), and post-war reconstruction/stabilization.
- **NG2:** We are not rewriting the German focus tree in this phase; interactions with Germany (Sealed Train, Brest-Litovsk, Faustschlag) will be implemented via clean scripted effects, decisions, and on_actions so Germany's upcoming rework hooks into them seamlessly.

### Anti-Goals (What would make this a failure)
- **AG1 (The Fragile Punchbag):** Russia collapsing to a quick 1915 German rush because it ran out of guns and has zero defenses.
- **AG2 (The Eastern Juggernaut):** Russia steamrolling into Berlin and Vienna by 1915–1916, rendering the Western Front pointless and ruining multiplayer games.
- **AG3 (The Instant / Fake Civil War):** Repeating the legacy bug where the civil war ends in 2 days via a text pop-up, or spawns a generic `D01` tag with no generals or fronts.
- **AG4 (Invisible / Unavoidable Traps):** The revolution triggering without player warning, with no buttons or decisions to mitigate it.

---

## 3. Constraints & Technical Boundaries

1. **Clausewitz Engine Syntax Integrity:** 100% bracket and syntax validity across all files. Zero errors in `python scripts/qa_audit_all.py`.
2. **Semantic Oracle Compliance:** All modifiers in ideas, focuses, and decisions must exist in `data/hoi4_valid_country_modifiers.json` and pass `scripts/hoi4_semantic_oracle.py`.
3. **Bilingual Localization & Single UTF-8 BOM:** All new keys in `localisation/english/` and `localisation/braz_por/` must start strictly with single UTF-8 BOM (`\xef\xbb\xbf`). 100% key parity between English and Brazilian Portuguese.
4. **GFX & Asset Fidelity:** Every focus icon, national spirit idea, and character portrait must point to a valid texture file existing on disk, with corresponding sprite definitions in `interface/` including shine overlays.
5. **Multiplayer Stability:** No desyncs or unhandled dynamic scope crashes. Tag changes (`change_tag_from`) and state transfers must be handled safely within event immediate blocks.

---

## 4. Architectural Pillars of the Rework

### Pillar 1: Base Russian Empire (1911–1917) Rebalance & Strategic Depth
- **Industrial Autonomy:**
  - Enhance `common/national_focus/soviet.txt` industrial branches (*Donbass Coal & Iron*, *Urals Metallurgical Basin*, *Putilov Works Expansion*, *Broad-Gauge Trans-Siberian Network*).
  - Russia starts with enough base civilian and military factories (adding +6 MIC and +4 CIC to historical states 195 Petrograd, 219 Moscow, 228 Taganrog/Donbass) to produce basic `infantry_equipment_0` and `artillery_equipment_1` without total foreign dependency.
- **Offensive Ceiling:**
  - Russian units have standard combat stats but limited high-tier motorized/tank research bonuses. Breakthrough and soft attack buffs in Tsarist army doctrines are capped to +10% max.
- **Strategic Depth & Defensive Mud:**
  - Add national idea `SOV_strategic_depth_and_rasputitsa`:
    - Enemy attrition on Russian core states: +20%
    - Supply consumption for enemies in Russian territory: +15%
    - Division defense on core territory: +10%
    - Division entrenchment speed: +15%
  - This ensures that if the Central Powers push into Belarus, Ukraine, and the Baltics, German logistical lines stretch thin, preventing an effortless blitz.

---

### Pillar 2: Dynamic Russian Crisis & Revolution Engine (Late 1915 – Mid 1917)
- **The Dual Catalyst for Lenin's Return:**
  1. *German Proactive Decision:* In `common/decisions/ww1_ger_rus_rework_decisions.txt` for Germany: `GER_operation_sealed_train` (*Der plombierte Wagen*) & `GER_fund_russian_revolutionaries`. Available from November 1915 if Russia has war exhaustion or stability < 65%. Fires `ww1_russia.300` (*Lenin Returns via the Sealed Train*).
  2. *Autonomous Historical Fallback:* In `common/on_actions/ww1_russia_on_actions.txt`, if date reaches `1917.3.1` and `GER_operation_sealed_train` was never taken, event `ww1_russia.301` (*Lenin Returns from Swiss Exile*) fires automatically, ensuring the crisis engine is never locked out by an inactive Germany.
- **The 4 Dynamic Crisis Gauges:**
  Managed via scripted effects in `common/scripted_effects/ww1_russia_crisis_effects.txt` clamped between 0 and 100:
  1. `SOV_revolutionary_tension`: Overall threat of uprising.
  2. `SOV_worker_unrest`: Industrial strikes and worker soviet mobilization in Petrograd and Moscow.
  3. `SOV_urban_hunger`: Food supply failures, bread shortages, railway breakdown.
  4. `SOV_army_loyalty`: Discipline of frontline peasant soldiers vs anti-war agitation.
- **Visual Feedback in Decisions Tab:**
  - Decision category `SOV_revolutionary_crisis_category` featuring dynamic scripted localization displaying colored visual progress bars:
    - `[████████░░] 82% - Perigo Crítico de Insurreição`
    - Dynamic status descriptions showing the exact effects of the current tier (Tier 1: Whispers of Dissent, Tier 2: Mass Strikes, Tier 3: Dual Power, Tier 4: Armed Insurrection).
- **Interactive Crisis Management Decisions:**
  - `SOV_emergency_grain_requisition`: Decreases hunger in cities at the cost of stability and peasant unrest.
  - `SOV_convene_duma_consultation`: Increases stability and lowers unrest at the cost of political power and Tsarist prestige.
  - `SOV_okhrana_anti_bolshevik_raids`: Arrests agitators, lowering revolutionary tension at the cost of temporary strikes.
  - `SOV_frontline_imperial_tour`: Increases army loyalty at the cost of political power.
  - `SOV_subsidize_urban_bakeries`: Consumes civilian factories for 90 days to decrease urban hunger.
- **Divergence Outcomes:**
  - **Path A (Imperial Salvation):** If the player keeps `SOV_revolutionary_tension < 50` until late 1917, the revolutionary threat collapses. Nicholas II or the Constitutional Duma issues the *Triumph of Order* proclamation (`SOV_order_restored_spirit`), granting +10% stability, +10% factory output, and preventing the civil war entirely.
  - **Path B (The Revolution Erupts):** If `SOV_revolutionary_tension >= 85` (or triggered deliberately via a focus/event option), Event `ww1_russia.310` (*The Storming of the Winter Palace*) fires.
    - Prompts the player with a direct choice:
      1. *"All Power to the Soviets!"* -> Play as **Soviet Russia (`SOV`)**.
      2. *"For Russia One and Indivisible!"* -> Switch tag to **White Movement (`WHT`)**.

---

### Pillar 3: Multi-Front Russian Civil War Engine (Reds vs Whites)
- **Tag Architecture:**
  - `SOV`: Soviet Russia (Crimson cosmetic tag `SOV_communism_IDEO`, revolutionary leadership, capital in Moscow/Petrograd).
  - `WHT`: White Movement / All-Russian Provisional Government (Azure/White cosmetic tag, led by Supreme Ruler Alexander Kolchak, Supreme Commander Anton Denikin, Pyotr Wrangel, Nikolai Yudenich).
- **Troop & Fleet Transition Mechanics:**
  - On civil war outbreak (`ww1_russia.310`), the fractured Imperial Army is cleared via `delete_unit_template_and_units`, and replaced with balanced, dedicated combat OOBs:
    - `SOV_red_army_civil_war`: 50 divisions of Red Guards, Revolutionary Riflemen, Baltic Sailors, and Worker Battalions.
    - `WHT_white_army_civil_war`: 45 divisions of Siberian Riflemen, Volunteer Army Officers, Don/Kuban Cossacks, and Czech Legionnaires.
  - **Fleet Partition:** Baltic Fleet stays with `SOV` (Kronstadt sailors); Black Sea Fleet transfers to `WHT` (Crimea/Sevastopol).
  - **Stockpiles:** Split 50/50 between both factions.
- **Territorial Partitioning & Spawning:**
  - **Soviet Core:** Controls central industrial heartland: Moscow (219), Petrograd (195), Yaroslavl, Nizhny Novgorod, Tula, Vladimir, Ivanovo.
  - **White Siberian Front (Kolchak):** Controls Omsk, Tomsk, Irkutsk, Vladivostok, and the Trans-Siberian corridor with the Czech Legion.
  - **White Southern Front (Denikin/Wrangel):** Controls Rostov, Kuban (228), Crimea, North Caucasus.
  - **White Northwestern Front (Yudenich):** Controls Pskov and northern borderlands.
  - **Peripheral Breakaways (Initial Neutrality):**
    - Finland (`FIN`), Ukraine (`UKR`), Poland (`POL`), and Transcaucasia (`GEO`/`ARM`/`AZR`) spawn initially as autonomous non-belligerents. This avoids encircling `SOV` in a 6-front war on Day 1, enabling historical diplomatic friction and subsequent border clashes via focus trees.
- **Post-War White Victory Reunification:**
  - If `WHT` wins the civil war and annexes `SOV`, an on-action reunification event triggers `change_tag_to = SOV` (restoring cores and loading a White/Restoration cosmetic tag and post-war focus tree). This ensures 100% compatibility with all external mod trees (Germany, Britain, Ottomans) that reference tag `SOV`.

---

### Pillar 4: Central Powers Interaction & The Brest-Litovsk Dilemma
- **Soviet Russia (`SOV`) Strategy:**
  - Gains decision/event `SOV_decree_on_peace`:
    - Dispatches diplomatic delegation to Brest-Litovsk to negotiate with Germany (`GER`).
    - Germany offers terms: Peace in exchange for renouncing sovereignty over Ukraine, Belarus, Poland, and the Baltic states.
    - **Acceptance:** Peace treaty signed. `SOV` exits WW1. Germany gains a massive grain/oil trade agreement (`GER_brest_litovsk_deliveries`), demobilizes eastern divisions, and transfers combat units to the Western Front. `SOV` can now focus 100% of its military might on crushing the White Army.
    - **Rejection ("Neither War nor Peace" / Trotsky):** Germany declares unrestricted resumption of hostilities (*Operation Faustschlag*). German motorized and infantry divisions sweep across Ukraine and Livonia, threatening Petrograd until the Soviets are forced to sign under harsher terms.
- **White Movement (`WHT`) Strategy & Entente Proxy Intervention:**
  - Rejects separate peace under the doctrine of *"Russia One and Indivisible"*.
  - Remains at war with the Central Powers, but **the Entente acts exclusively via Proxy Intervention**:
    - `prevent_join_factions = yes` ensures the Whites cannot call the entire Entente alliance directly into the civil war, preventing Allied AI from flooding 100 divisions into Russia.
    - Allies provide lend-lease munitions, naval escorts to Odessa/Vladivostok, financial credits, and volunteer expeditionary divisions in Murmansk/Arkhangelsk.
- **Dissolution of Brest-Litovsk upon 1918 German Collapse:**
  - When Germany signs the Armistice / capitulates in late 1918, an `on_action` hook voids all Brest-Litovsk deliveries, collapses German puppet regimes in the east, and triggers the historical Soviet westward offensive (*Target Vistula* / Polish-Soviet War prelude).

---

### Pillar 5: Dedicated Soviet Russia Focus Tree (`soviet_russia_focus`)
Structure: ~75–85 focuses organized into 5 logical wings:
1. **Wing 1: War Communism & Red Terror (16 focuses):**
   - *Decrees of the Sovnarkom*, *Establishment of the Cheka (Iron Felix)*, *Prodrazvyorstka Grain Confiscation*, *Committees of the Poor (Kombedy)*, *Suppression of Left SRs*, *Nationalization of Banks & Heavy Industry*.
2. **Wing 2: Red Army Doctrine & Military Commissars (18 focuses):**
   - *Trotsky's Revolutionary Military Council*, *Institute Political Commissars*, *Enlist Tsarist Military Specialists (Voenspetsy)*, *Budyonny's 1st Cavalry Army*, *Tukhachevsky's Deep Battle Prelude*, *Frunze's Unified Military Doctrine*.
3. **Wing 3: Soviet Economic Reconstruction & GOELRO (16 focuses):**
   - *Electrification of Russia (GOELRO Plan)*, *Gosplan State Planning Committee*, *The NEP Compromise (Bukharin)* vs *War Communism Continuity (Preobrazhensky)*, *Kuznetsk & Urals Industrial Basins*.
4. **Wing 4: Comintern & World Revolution (14 focuses):**
   - *Founding of the Third International (Comintern)*, *Export of Revolutionary Propaganda*, *The Miracle on the Vistula (Polish-Soviet War)*, *Treaty of Rapallo (Secret Cooperation with Germany)*, *Establish Soviet Diplomatic Ties*.
5. **Wing 5: State Building & The Soviet Union (12 focuses):**
   - *1918 RSFSR Constitution*, *Abolition of Class Distinctions*, *Subjugate the Cossack Hosts*, *Reincorporate Ukraine & Caucasus*, *Declaration of the USSR (1922)*.

---

### Pillar 6: Dedicated White Movement Focus Tree (`white_russia_focus`)
Structure: ~55–65 focuses organized into 4 logical wings:
1. **Wing 1: The Omsk Directorate & Supreme Ruler (15 focuses):**
   - *The Provisional All-Russian Government*, *Kolchak's Coup at Omsk*, *The Gold Reserve of the Russian Empire*, *Martial Law & White Terror*, *Pacify Siberian Partisans*.
2. **Wing 2: Armed Forces of South Russia (16 focuses):**
   - *The Volunteer Army*, *General Kornilov's Legacy & Denikin's Command*, *Alliance with the Don & Kuban Cossacks*, *Wrangel's Crimean Bastion*, *Agrarian Land Guarantees for Peasants*.
3. **Wing 3: Entente Intervention & Western Diplomacy (14 focuses):**
   - *Honor Allied Treaties*, *General Knox's British Supply Mission*, *French Naval Munitions in Odessa*, *Japanese Railway Protection in Vladivostok*, *Repayment of Imperial War Debts*.
4. **Wing 4: Political Restoration & Post-War Russia (12 focuses):**
   - *Reconvene the All-Russian Constituent Assembly* (Democratic Republic) vs *The Crowned Regent / Military Strongman* (Restored Autocracy/Military Rule).

---

### Pillar 7: Historical Character Cast & Graphics
- **Soviet Characters (`SOV`):**
  - Vladimir Lenin (Head of Government / Leader)
  - Leon Trotsky (War Commissar / Field Marshal)
  - Joseph Stalin (Commissar for Nationalities / General)
  - Mikhail Frunze (Chief of Staff / General)
  - Felix Dzerzhinsky (Cheka Security Chief / Advisor)
  - Semyon Budyonny (Cavalry General)
  - Mikhail Tukhachevsky (General / Theorist)
  - Georgy Chicherin (Foreign Commissar)
  - Nikolai Bukharin (Economic Advisor)
  - Lev Kamenev & Grigory Zinoviev (Political Advisors)
- **White Characters (`WHT`):**
  - Alexander Kolchak (Supreme Ruler / Admiral)
  - Anton Denikin (Supreme Commander / Field Marshal)
  - Pyotr Wrangel (Black Baron / Cavalry General)
  - Nikolai Yudenich (Northwest Army Commander)
  - Lavr Kornilov (Volunteer Army General)
  - Alexei Kaledin (Ataman of Don Cossacks)
  - Boris Savinkov (Political Advisor)
- **GFX Asset Pipeline:**
  - Ensure all portraits in `gfx/leaders/SOV/` are mapped with valid `.dds` / `.png` definitions.
  - Sprite definitions with animated shines in `interface/ww1_soviet_goals.gfx` and `interface/ww1_white_goals.gfx`.
  - Bilingual localization (`ww1_russia_l_english.yml`, `ww1_russia_l_braz_por.yml`, `ww1_soviet_l_english.yml`, `ww1_white_l_english.yml`) with mandatory single UTF-8 BOM.

---

### Pillar 8: AI Logic, Automated Testing & Verification
- AI weighting configured so AI Russia behaves historically under typical conditions, but handles crisis decisions intelligently without crashing.
- Master unit test suite: `tests/test_ww1_russia_rework.py` covering:
  - Clausewitz syntax & brace integrity across all new Russian files.
  - Modifier oracle auditing against `data/hoi4_valid_country_modifiers.json`.
  - Coordinate non-collision check for both focus trees.
  - Single UTF-8 BOM verification across all Russian localization files.
  - OOB template integrity and character recruitment validation.

---

## 5. What is Left to the Builder
- Detailed exact coordinates $(x, y)$ of individual focuses in the new trees (following the standard 5-wing layout rules: $1 \le \Delta y \le 3$, $|x_2 - x_1| \ge 2$).
- Specific numerical balancing of factory additions and equipment stockpile deductions for civil war decisions.
- Exact breakdown of state IDs transferred between `SOV` and `WHT` during the civil war outbreak.
