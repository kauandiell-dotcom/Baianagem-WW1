# Design Document: Russian Empire, Russian Revolution & Soviet/White Civil War Overhaul

**Date:** 2026-10-13  
**Target Tag(s):** `SOV` (Russian Empire / Soviet Russia), `WHT` (All-Russian Provisional Government / White Movement), Breakaway Republics (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`)  
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
- **Rich Normal Gameplay Mechanics for Tsarist Russia (1911–1917):**
  - *Duma vs. Autocratic Court Tension Engine* (Rasputin, Ministerial Leapfrog, Rodzianko's Progressive Bloc).
  - *The 1915 Great Shell Shortage (Snaryadny Golod) & VPK Industrial Mobilization*.
  - *Broad-Gauge Rail Logistics & Strategic Factory Evacuation* (relocating western plants to the Volga/Urals).
  - *The Brusilov Offensive Preparation & Infiltration System* (decision-based breakthrough operations vs Austria-Hungary).
- **A Dynamic Pre-Revolutionary Crisis Engine (Late 1915 – Mid 1917):**
  - 4 bounded visual gauges (`SOV_revolutionary_tension`, `SOV_worker_unrest`, `SOV_urban_hunger`, `SOV_army_loyalty`) in the Decisions tab with colored progress bars.
  - Early proactive German Sealed Train decision (late 1915/1916) with an autonomous early 1917 historical fallback event if Germany fails to trigger it.
- **A Fully Chaotic Russian Civil War (Multi-Front Powderkeg):**
  - Dedicated tag `WHT` (White Movement under Kolchak, Denikin, Wrangel, Yudenich) vs `SOV` (Red Army under Lenin, Trotsky, Stalin, Frunze).
  - **Peripheral Breakaway Nations Spawning AT WAR with BOTH Reds and Whites:** Ukraine (`UKR`), Finland (`FIN`), Poland (`POL`), Transcaucasia (`GEO`, `ARM`, `AZR`), and Don Cossacks (`DON`) spawn with authentic regional troops and declared hostilities against both `SOV` and `WHT`, turning the former empire into a realistic, challenging, multi-front war.
- **Diplomatic Pacing with Central Powers:**
  - Historical **Treaty of Brest-Litovsk** option for Soviet Russia to exit WW1 and focus on the civil war.
  - **Entente Proxy Intervention** for the Whites (lend-lease, munitions, subsidies, port garrisons) without full direct war.
  - Automatic on-action dissolution of Brest-Litovsk upon the late 1918 German armistice, initiating post-war border reclamation.
- **Three Dedicated Focus Trees:**
  - Modernized Imperial Russian Tree (1911–1917).
  - Full Soviet Russia Tree (`soviet_russia_focus`, ~80 focuses).
  - Full White Movement Tree (`white_russia_focus`, ~60 focuses).

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
- **G1: Tsarist Depth (1911–1917):** Imperial Russia must feel rich, active, and engaging before the revolution ever happens, with interactive Duma management, overcoming the shell shortage, and executing planned offensives.
- **G2: Real Historical Chaos:** When the revolution erupts, the country fractures into a massive, multi-faction conflict. Peripheral states (`UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`) break away with troops and are at war with both Reds and Whites.
- **G3: Skill-Driven Divergence:** Player/AI can avert the revolution through skilled management of the crisis gauges, or let it erupt and choose between Soviet Russia (`SOV`) or the White Movement (`WHT`).
- **G4: Western Front Balance:** Russian defense is resilient (*Rasputitsa*, scorched earth, strategic depth), preventing German blitzkrieg, but Russian offensive power is bounded so it cannot crush Germany/Austria single-handedly.
- **G5: Dedicated Bespoke Trees & Content:** Bespoke focus trees for Empire, Soviets, and Whites, complete with character recruitment, GFX shine overlays, and bilingual UTF-8 BOM localization.

### Non-Goals
- **NG1:** We are not modeling post-1925 Soviet history (no 1930s Great Purge or WW2 tanks). Content is focused on 1911–1923.
- **NG2:** We are not rewriting the German focus tree in this phase; interactions with Germany (Sealed Train, Brest-Litovsk, Faustschlag) are cleanly decoupled.

### Anti-Goals
- **AG1 (The Boring Waiting Game):** Tsarist Russia having nothing to do from 1911 to 1917 except waiting for the revolution.
- **AG2 (The Two-Day Civil War):** Repeating the legacy bug of an instant text-only civil war or generic `D01` tag.
- **AG3 (The Trivial Re-conquest):** Breakaway nations being 0-division pushovers that are annexed in 3 days.

---

## 3. Constraints & Technical Boundaries

1. **Clausewitz Syntax & Modifier Oracle:** 100% bracket balance. All modifiers must be validated against `data/hoi4_valid_country_modifiers.json`. Zero errors in `python scripts/qa_audit_all.py`.
2. **Bilingual Localization & Single UTF-8 BOM:** All files in `localisation/english/` and `localisation/braz_por/` must start strictly with `\xef\xbb\xbf` (single UTF-8 BOM) with 100% key parity.
3. **GFX Integrity:** All referenced portraits, idea icons, and focus goals must exist on disk with valid shine definitions.
4. **Multiplayer Stability:** Dynamic tag switches (`change_tag_from`), OOB spawns, and state transfers must be handled in clean, safe event blocks without desync risk.

---

## 4. Architectural Pillars of the Rework

### Pillar 1: Mechanics for Normal Tsarist Russia (1911–1917)
1. **Duma Politics vs. Court Autocracy:**
   - Visual gauge `SOV_duma_tension` (0–100%) and Court Influence ideas (`SOV_rasputin_court_intrigues`, `SOV_stolypin_reforms`, `SOV_progressive_bloc`).
   - Decisions: *Convene the Imperial Duma*, *Prorogue the Duma*, *Dismiss Incompetent Ministers (Ministerial Leapfrog)*, *Grant Concessions to Octobrists and Kadets*.
   - Balancing: Keeping the Duma cooperative grants political power and civilian factory output; proroguing it gives short-term autocratic control but increases unrest and destabilizes the empire.
2. **The 1915 Great Shell Shortage (*Snaryadny Golod*):**
   - At war outbreak against the Central Powers, Russia suffers from `SOV_shell_shortage_crisis` (-25% artillery soft attack, -15% division breakthrough).
   - Overcome through decision category `SOV_war_industry_mobilization`:
     - *Establish the War Industries Committees (VPK)*.
     - *Mobilize Private Machine Shops*.
     - *Zemgor Medical and Supply Union*.
     - *Import Cordite and Shell Presses from Britain*.
     - Completing these decisions transitions the idea to `SOV_vpk_mobilization_spirit` (+10% artillery production speed).
3. **Broad-Gauge Rail Logistics & Strategic Factory Evacuation:**
   - Western borderland states (Warsaw, Grodno, Bialystok, Riga) contain valuable factories.
   - Decision system: *Evacuate Industrial Machinery from Poland and Baltics*. If German troops threaten these states, the Russian player can dismantle factories and reconstruct them in Moscow, Nizhny Novgorod, and the Urals, preventing Germany from capturing free industrial capacity.
4. **The Brusilov Infiltration Doctrine (1916):**
   - Decision-based operational planning against Austria-Hungary (`SOV_prepare_southwestern_offensive`): grants tailored shock tactics and localized breakthrough bonuses along the Galician front without permanently unbalancing the entire Eastern Front.

---

### Pillar 2: Strategic Depth & Anti-Blitz Defensive Resilience
- National Idea: `SOV_strategic_depth_and_rasputitsa`:
  - Enemy attrition on Russian core states: +20%
  - Enemy supply consumption on Russian core states: +15%
  - Division core defense: +10%
  - Division entrenchment speed: +15%
- Precludes early German/Austrian steamrolling and forces invaders into logistical quagmires.

---

### Pillar 3: Visual Revolutionary Crisis Engine (Late 1915 – Mid 1917)
- Dual Catalyst for Lenin's Return:
  - *German Proactive Decision:* `GER_operation_sealed_train` (late 1915 / 1916).
  - *Autonomous Historical Fallback:* On-action event `ww1_russia.301` in March 1917 if Germany never triggers the decision.
- 4 Real-Time Decisions Gauges with Colored Progress Bars:
  - `SOV_revolutionary_tension` [████████░░] (0–100%)
  - `SOV_worker_unrest` (0–100%)
  - `SOV_urban_hunger` (0–100%)
  - `SOV_army_loyalty` (0–100%)
- Decisions to mitigate or steer the crisis: bread subsidies, Duma concessions, Okhrana raids, frontline tours.
- Outcomes:
  - **Imperial Salvation:** If tension is kept below 50% until late 1917, the revolution is defeated, granting `SOV_order_restored_spirit`.
  - **Revolutionary Outbreak:** Event `ww1_russia.310` fires if tension exceeds 85%, prompting the player to choose between **Soviet Russia (`SOV`)** or the **White Movement (`WHT`)**.

---

### Pillar 4: The Multi-Front Russian Civil War & Breakaway Powderkeg
- **The Belligerents:**
  - `SOV`: Soviet Russia (Petrograd, Moscow, industrial core, Baltic fleet).
  - `WHT`: White Movement (Kolchak in Siberia, Denikin/Wrangel in the South, Yudenich in Pskov, Black Sea fleet).
  - **Peripheral Breakaways (AT WAR with BOTH Reds and Whites):**
    - `UKR` (Ukrainian People's Republic / Petliura & Central Rada): Spawns with 12–16 divisions in Kiev/Kharkov, defending sovereignty against Red expansion and White centralization.
    - `FIN` (Finland): Spawns with 8–12 divisions under Mannerheim, securing Karelian borders.
    - `POL` (Poland): Second Polish Republic under Piłsudski, spawns with 15–20 divisions contesting western frontiers.
    - `GEO`, `ARM`, `AZR` (Transcaucasia): Spawn with 4–6 regional divisions each, fighting for Caucasian autonomy and Baku oil.
    - `DON` (Don Cossack Host): Allied with the Whites, holding the Rostov basin against Red cavalry incursions.
- **Unit and Fleet Transition:**
  - Old imperial army disbanded via `delete_unit_template_and_units`.
  - Dedicated civil war OOBs spawn for all factions:
    - `SOV`: 50 divisions of Red Guards, Workers' Battalions, Baltic Sailors.
    - `WHT`: 45 divisions of Siberian Riflemen, Volunteer Army, Cossack Cavalry.
    - Breakaway nations spawn with authentic regional defense divisions.
  - Baltic Fleet -> `SOV`; Black Sea Fleet -> `WHT`. Stockpiles split 50/50.

---

### Pillar 5: Central Powers Interaction, Brest-Litovsk & Entente Proxy Aid
- **Soviet Russia (`SOV`):**
  - Decision: *Decree on Peace* -> Negotiations at Brest-Litovsk.
  - Option to accept peace (ceding western borderlands to Germany and exiting WW1) or reject ("Neither war nor peace", prompting German *Operation Faustschlag*).
  - Dissolution of Brest-Litovsk on German Armistice (late 1918): on-action cancels German occupation, opening Soviet westward reclamation (*Target Vistula* / Polish-Soviet War 1920).
- **White Movement (`WHT`):**
  - "Russia One and Indivisible": Refuses separate peace with Central Powers.
  - **Entente Proxy Intervention:** Non-belligerent aid (Allied volunteers, French munitions in Odessa, British shipments via Vladivostok, Murmansk garrisons, financial credits). Whites cannot drag the full Entente into the civil war (`prevent_join_factions = yes`), preserving delicate MP balance.
- **Post-War White Reunification:**
  - If `WHT` defeats `SOV`, an on-action reunification fires `change_tag_to = SOV`, restoring cores, cosmetic tag, and international compatibility with mod trees referencing `SOV`.

---

### Pillar 6: Dedicated Soviet Russia Focus Tree (`soviet_russia_focus` — 80 Focuses)
- **Wing 1: War Communism & Red Terror (16 focuses):** Cheka under Dzerzhinsky, grain requisitions (*Prodrazvyorstka*), Kombedy committees, labor militarization.
- **Wing 2: The Red Army & Military Doctrine (18 focuses):** Trotsky's Revvoyensovyet, political commissars, Tsarist Voenspetsy officers, Budyonny's 1st Cavalry Army, Tachanka mobile warfare, Tukhachevsky's Deep Battle, Frunze's unified doctrine.
- **Wing 3: GOELRO & Economic Reconstruction (16 focuses):** Lenin's electrification plan, Volkhov dam, Shatura plants, Mutual Exclusivity: **NEP (Bukharin)** vs. **Superindustrialization (Preobrazhensky/Trotsky)**, Donbass coal and Kuznetsk heavy industry.
- **Wing 4: Comintern & World Revolution (16 focuses):** Third International, Brest-Litovsk diplomacy, Treaty of Rapallo (1922) with Germany, Polish-Soviet War (1920), Turkish Kemalist pact.
- **Wing 5: State Building & Formation of the USSR (14 focuses):** Rights of Peoples, Caucasian pacification, Ukrainian SSR integration, Basmachi suppression, Treaty of the Creation of the USSR (1922), 1924 Constitution.

---

### Pillar 7: Dedicated White Movement Focus Tree (`white_russia_focus` — 60 Focuses)
- **Wing 1: The Omsk Directorate & Supreme Ruler (15 focuses):** Ufa state conference, Kolchak's Omsk coup, Kazan imperial gold reserves, Czech Legion alliance, Siberian anti-partisan law.
- **Wing 2: Armed Forces of South Russia (16 focuses):** Volunteer Army, Ice March, Don/Kuban Cossack alliance, Moscow Directive (1919), Wrangel's land reforms, Crimean redoubt.
- **Wing 3: Entente Diplomacy & Foreign Aid (15 focuses):** Russia One and Indivisible, General Knox British mission, French Odessa convoys, Japanese Pacific liaison, imperial debt recognition.
- **Wing 4: Post-War Political Restoration (14 focuses):** Mutual Exclusivity: **Constituent Assembly (Democratic Federation)** vs. **Military Strongman / Restored Autocracy (Crowned Tsar)**.

---

### Pillar 8: Character Cast, GFX & Master QA Verification
- Full recruitment of 15+ Bolshevik and White characters with bespoke traits in `common/characters/SOV.txt`.
- Complete GFX sprite definitions with shines in `interface/ww1_soviet_goals.gfx` and `interface/ww1_white_goals.gfx`.
- Single UTF-8 BOM bilingual localization (`english` and `braz_por`).
- Master unit test suite `tests/test_ww1_russia_rework.py` ensuring 0 syntax/brace errors, 0 invalid modifiers, valid coordinates, and 100% test pass in `scripts/qa_audit_all.py`.
