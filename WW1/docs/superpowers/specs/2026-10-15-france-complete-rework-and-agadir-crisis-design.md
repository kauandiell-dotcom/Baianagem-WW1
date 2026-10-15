# Design Document: French Republic Complete Rework, The Agadir Crisis Escalation Engine & The 4 Political Destinies

**Date:** 2026-10-15  
**Target Tag(s):** `FRA` (French Third Republic / Second Paris Commune / Kingdom of France / GQG Military Directory), Interacting Tags: `GER`, `ENG`, `RUS`, `BEL`, `ITA`, `USA`  
**Bookmark:** 1911.6.1 (WW1 Baianagem Mod)  
**Status:** Approved for Implementation Planning  

---

## 1. Intent and The Why

The French Third Republic (`FRA`) is the beating heart of the Western Front and the diplomatic anchor of the Triple Entente in World War I. Forensic analysis of the current mod reveals that France suffers from the same systemic flatness that previously afflicted Germany, Russia, and Austria-Hungary before their respective overhauls:

1. **A Hollow, Trivialized Agadir Crisis (1911):**  
   The Second Moroccan Crisis is currently reduced to three superficial, linear events in `events/WW1_Agadir.txt` (`ww1_agadir.1`, `2`, `3`) where Germany clicks a button, gets 50 PP, and France and Britain receive 5% war support. There is zero tension, no negotiation over the French Congo (*Neukamerun*), no British *Mansion House* ultimatum, no French cabinet crisis over Joseph Caillaux’s secret backchannel talks, and zero danger of early war.
2. **A Static 200-Focus Tree with No Ideological Divergence:**  
   The political wing of `common/national_focus/france.txt` is entirely linear, offering only a cosmetic choice between two moderate democratic presidents (Poincaré vs. Pams). There is no path for the revolutionary syndicalist left (CGT / Second Paris Commune), no path for the integral nationalist monarchists (Charles Maurras / Action Française / Orléans Restoration), and no path for a military junta (GQG / Joffre / Pétain).
3. **Absence of French Wartime Survival Dynamics:**  
   In 1914, Germany occupied France's vital northeastern industrial belt (Briey-Longwy and Nord-Pas-de-Calais), stripping France of 70% of its coal and 80% of its iron ore. France survived only through heroic mobilization (*Comité des Forges*, British coal convoys, American credits). Furthermore, in 1917, the catastrophe of the Nivelle Offensive triggered the famous French Army Mutinies (*Mutineries de 1917*), while women munitions workers (*Munitionnettes*) went on strike in Paris. None of these dynamics exist in game mechanics—categories like `FRA_defence_of_verdun`, `FRA_mutinies_crisis_management`, and `FRA_war_economy_and_munitions` are completely empty.
4. **Disjointed Event Calls:**  
   Event `ww1_france.210` (mutinies) fires with flat penalties and does not apply the idea `FRA_trench_mutiny_crisis_2`, leaving decision `FRA_petain_welfare_and_leave_reform` permanently locked out and unclickable.

---

## 2. Core Architectural Pillars

### Pillar 1: The Agadir Crisis Escalation Engine (July – November 1911)
A brisk, high-tension diplomatic confrontation between **Germany (GER)**, **France (FRA)**, and **Great Britain (ENG)**:
- **Tension Variable:** `global.ww1_agadir_crisis_tension` (0 to 100), visualized in dedicated category `ww1_agadir_crisis_category`.
- **Pacing Standard:** Brisk, rapid escalation (~6 to 12 weeks, concluding by late autumn 1911). Decisions carry 7–14 day turnaround times.
- **The 4 Dynamic Climax Outcomes:**
  1. *Historical Resolution (Franco-German Accord of Nov 1911 & Treaty of Fez 1912):* France cedes *Neukamerun* (states 1086, 1087, 1088) to German Cameroon. Germany formally recognizes the French Protectorate over Morocco (`FRA_morocco_treaty_of_fez` spirit + Moroccan colonial manpower). Caillaux's secret diplomacy leaks, collapsing his ministry and bringing Raymond Poincaré to power.
  2. *Pan-German Triumph (Base Naval em Agadir):* Germany extracts a permanent Atlantic naval coaling station in Agadir (state 462). Severe blow to British maritime pride and French prestige.
  3. *German Humiliation (Recuo sem Concessões):* Entente holds an unbroken front. Under British naval threat, Germany recalls the *Panther* empty-handed. Kaiser Wilhelm II's authority is battered; German Army expands radically in reaction.
  4. *The Premature Conflagration (Guerra Geral de 1911):* If tension reaches 100% or an ultimatum is defied, World War I erupts in Autumn 1911.

### Pillar 2: The Republic Dashboard & The 4 Survival Vectors
Scripted effect system in `common/scripted_effects/ww1_france_dashboard_effects.txt` with clamping between 0 and 100:
1. **`FRA_union_sacree_cohesion` (0–100):** Political cohesion across socialists, radicals, and catholics. Drops with casualties, food inflation, and prolonged stalemate. Below 25% unlocks civil unrest and revolutionary risks.
2. **`FRA_poilu_morale` (0–100):** Trench morale of the front-line soldiers. Degrades during failed bloody offensives and chemical warfare; restored by Pétain's leave reforms, trench wine/soup rations, and defensive victories. Below 30% triggers the 1917 Mutinies.
3. **`FRA_charbon_et_acier` (0–100):** Fuel and metallurgical stockpiles. Depletes heavily if Briey (18) and Lille (28) are occupied; replenished by British Channel coal convoys, American raw imports, and *Comité des Forges* rationalization.
4. **`FRA_reserves_humaines` (0–100):** Demographic endurance. Reflects France's acute pre-war low birthrate. Replenished by calling up the young Class of 1917 (*Les Bleuets*), recruiting *Tirailleurs Sénégalais* and North African colonial troops, and mobilizing the *Munitionnettes*.

### Pillar 3: Military & Civil Crises Engine
1. **The 1917 Army Mutinies (*Chemin des Dames*):**
   - Triggered after the Nivelle Offensive failure or when `FRA_poilu_morale < 30` during wartime.
   - Soldiers sing *La Chanson de Craonne*, refusing suicidal frontal attacks while maintaining trench defense.
   - Player must choose between:
     - *Pétain's Reforms (Historical):* Sack Nivelle, institute leave, hot meals, rotation (*noria*), and minimal executions. Restores morale and shifts doctrine to firepower.
     - *Summary Decimation (Iron Fist):* Heavy executions, court martials. Destabilizes home front, risks mutiny spreading to Paris.
     - *Soldier Councils Fraternization:* Catalyzes the Second Paris Commune!
2. **Civil Home Front Crisis (*Munitionnettes Strikes & Malvy Affair*):**
   - Strike wave in Paris factories; subversion investigations.
3. **"Jusqu'au Bout!" — French Endsieg Mechanic:**
   - Georges Clemenceau appointed Premier (*"Le Tigre"*).
   - Activates when surrender progress exceeds 20% or Paris is threatened.
   - Total national mobilization, +20% core defense, refusal of defeatist compromise.

### Pillar 4: The 4 Divergent Political Destinies
1. **Third Republic & Union Sacrée (Democratic):**
   - Poincaré, Briand, and Clemenceau. Civilian supremacy over GQG, democratic resilience, allied coordination.
2. **Second Paris Commune / CGT Revolutionary State (Communism):**
   - Triggered by collapse of Union Sacrée or deliberate revolutionary focus path.
   - Red Paris vs. Bourgeois Bordeaux. Syndicalist worker councils, peace without annexations or revolutionary war.
3. **Action Française & Orléanist Monarchy (Neutrality / Monarchism):**
   - Charles Maurras, Léon Daudet, Camelots du Roi.
   - Restoration of King Jean III (House of Orléans). Integral nationalism, Catholic revival, ultra-revanchism.
4. **GQG Military Directory (Authoritarian / Non-Aligned):**
   - Council of Marshals (Joffre, Pétain, Foch).
   - Dissolution of parliament, martial law across the interior, militarized production.

---

## 3. Balance Standards (Single Player & Multiplayer)

1. **No Artificial Nerfs:** France retains its full historical industrial capacity (38-44 factories at start).
2. **Realistic Northeast Loss Compensation:** If Briey/Longwy (18) falls, decisions allow rapid emergency workshops in Lyon, Saint-Étienne, and Paris, supported by British coal imports.
3. **Modifier Oracle Compliance:** 100% of modifiers validated against `data/hoi4_valid_country_modifiers.json`. Values bounded strictly between +5% and +20%. Zero fantasy inflation.
4. **Tag Safety:** Zero dynamic `start_civil_war` bugs; all civil conflicts use fixed, safe tags and faction lockdowns.

---

## 4. Verification & QA Standards
- Comprehensive automated test suite: `tests/test_ww1_france_rework.py` registered as Suite 13 in `scripts/qa_audit_all.py`.
- 100% Clausewitz bracket balance across all new/modified files.
- Single UTF-8 BOM (`\xef\xbb\xbf`) on all bilingual localization files (English and Brazilian Portuguese).
- Immediate mirror sync to Steam Workshop staging directory `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.
