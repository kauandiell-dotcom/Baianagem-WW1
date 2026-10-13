# Task 5 Report: Multi-Front Russian Civil War Engine & Breakaway Powderkeg

## 1. Executive Summary
Task 5 has been implemented and verified. The multi-front Russian Civil War engine models the collapse of the Russian Empire following the Storming of the Winter Palace (`ww1_russia.310`), the disbanding of the old imperial army, dedicated historical OOBs for all major factions, territorial partitioning (`SOV` vs `WHT` and breakaways), foreign faction intervention quarantine (`prevent_join_factions = yes`), and Soviet wartime administration decisions.

---

## 2. Deliverables & Implementations

### A. Dedicated Civil War Order of Battles (`history/units/`)
- **`SOV_red_army_civil_war.txt`** (50 divisions):
  - Templates: `Krasnaya Gvardiya` (Red Guards), `Rabochaya Druzhina` (Workers' Militia), `Revolyutsionnye Moryaki` (Revolutionary Sailors), `Krasnaya Kavalerie` (Red Cavalry).
  - Deployed in Petrograd, Moscow, Tula, Tver, Nizhny Novgorod, Yaroslavl, Ryazan, Penza, Samara, Kazan, Orel, Kursk, and Voronezh.
- **`WHT_white_army_civil_war.txt`** (45 divisions):
  - Templates: `Sibirskaya Strelkovaya Diviziya` (Siberian Riflemen), `Dobrovolcheskaya Armiya` (Volunteer Army), `Kazachya Kavaleriyskaya Diviziya` (Cossack Cavalry).
  - Deployed across Siberia/Omsk, the Urals/Perm, Kuban/South Russia, and Vladivostok.
- **`UKR_civil_war.txt`** (14 divisions):
  - Templates: `Haidamatsky Kish`, `Sichovi Striltsi`, `Vilne Kozatstvo`.
  - Deployed in Kiev, Kharkov, Odessa, Kherson, Vinnytsia, and Cherkasy.
- **`FIN_civil_war.txt`** (10 divisions):
  - Templates: `Suojeluskunta` (White Guards), `Rannikkojaakarit` (Coastal Jaegers).
  - Deployed in Helsinki, Viipuri, Turku, Vaasa, and Kuopio.
- **`POL_civil_war.txt`** (16 divisions):
  - Templates: `Legiony Polskie`, `Armia Hallera`, `Jazda Polska`.
  - Deployed in Warsaw, Lodz, Lublin, and Bialystok.
- Verified valid Clausewitz subunits used across all templates: `infantry`, `cavalry`, `artillery`, `engineer`, `recon`.

### B. Civil War Eruption Event Chain (`events/ww1_russia_civil_war_events.txt`)
- Namespace: `ww1_russia_civil_war`.
- Wired directly from `ww1_russia.310` in `events/ww1_russia_crisis_events.txt` (`country_event = { id = ww1_russia_civil_war.1 days = 1 }`).
- Event `ww1_russia_civil_war.1`:
  - **Quarantine:** Enforces `prevent_join_factions = yes` and `set_rule = { can_join_factions = no }` on both `SOV` and `WHT` to prevent foreign AI faction flooding.
  - **Army Disbandment:** Clears bloated imperial formations using `delete_unit_template_and_units` for `Pekhotnaya Diviziya`, `Kazachya Diviziya`, `Gornostrelkovaya Diviziya`, and `Leib-Gvardiya & Opolcheniye`.
  - **Territorial Transfers:**
    - `WHT` receives Siberia, Urals, and Southern territories (including Omsk 571 & 594, Ekaterinburg/Perm, Irkutsk, Vladivostok, Kuban, Novorossiysk, Crimea/Sevastopol, Astrakhan, Tsaritsyn).
    - `UKR` receives Ukraine states (Kiev 202, Odessa 192, Kharkov 221, etc.).
    - `FIN` receives Finland states (Helsinki 111, Viipuri 145, etc.).
    - `POL` receives Poland states (Warsaw 10, Lodz 87, etc.).
    - `GEO` receives Georgia (Tbilisi 231, Abkhazia 826).
    - `ARM` receives Armenia (Yerevan 229, 230).
    - `AZR` receives Azerbaijan (Baku 228, 229).
    - `DON` receives Don Cossack territory (Rostov 218, Taganrog 228).
  - **Fleet & Stockpile Split:** Baltic Fleet to `SOV`, Black Sea Fleet and naval bases to `WHT`, stockpiles split.
  - **Combat OOBs Loaded:** Loads dedicated OOBs for `SOV`, `WHT`, `UKR`, `FIN`, `POL`, `DON`, `GEO`, `ARM`, `AZR`.
  - **Mutual War Declarations:**
    - `SOV` vs `WHT` (Civil War)
    - `SOV` vs `UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`
    - `WHT` vs `UKR`, `FIN`, `POL`, `GEO`, `ARM`, `AZR`, `DON`
  - **Dual Player Options:**
    - Option A: Player commands Soviet Russia (`SOV`).
    - Option B: Player switches perspective to White Russia (`WHT`) via `change_tag_from = SOV`.

### C. War Administration Decisions (`common/decisions/ww1_soviet_civil_war_decisions.txt`)
- Category: `SOV_civil_war_management` in `common/decisions/categories/ww1_soviet_civil_war_categories.txt`.
- Decisions:
  1. `SOV_seize_kazan_gold_reserves`: Available when controlling Kazan (249); awards 150 PP, stability, +10% factory output, and -5% consumer goods.
  2. `SOV_prodrazvyorstka_grain_expeditions`: Emergency grain requisitioning yielding -15% supply consumption and -10% attrition at cost of stability.
  3. `SOV_mobilize_petrograd_workers`: Emergency worker levies in Petrograd providing +10% conscription factor, +20% mobilization speed, -10% training time.
  4. `SOV_trotsky_armored_train_inspection`: Trotsky's mobile inspection yielding +10% army morale, +10% org regain, +5% land reinforce rate.

### D. Bilingual Localization Parity
- Updated `localisation/english/ww1_russia_events_l_english.yml` and `localisation/braz_por/ww1_russia_events_l_braz_por.yml`.
- Strict single UTF-8 BOM verified (`\xef\xbb\xbf`).
- 100% key parity (0 mismatches across all 90 keys).

---

## 3. Verification & QA Results
- **Unit Test Execution:**
  `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_civil_war_spawns_and_oobs -v`
  **Result:** `PASS (OK, 1 test in 0.002s)`
- **Semantic Oracle:**
  `scripts.hoi4_semantic_oracle.audit_file_modifiers`
  **Result:** `0 errors on all files`
- **Clausewitz Bracket Balance:**
  `0 errors across all 9 modified/created files`
- **Git Commit:**
  Commit hash: `8b9bc64`
  Commit message: `feat(sov): implement multi-front Russian Civil War engine, breakaway nations, and combat OOBs`
