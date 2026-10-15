# Kingdom of Serbia Complete Overhaul & The Great Retreat Specification

## 1. Vision & Core Philosophy
The Kingdom of Serbia (`SER`) was the crucible of the First World War. Despite suffering the highest proportional casualties of any nation in the war (nearly 28% of its total population and over 60% of its male population), Serbia fought with legendary tenacity, achieving the first Allied victory of the war at the Battle of Cer (August 1914), breaking three Austro-Hungarian invasions in 1914, enduring the epic winter trek of the *Albanian Golgotha* (1915–1916), and returning via the Salonika Front to spearhead the breakthrough at Dobro Pole (1918) that collapsed the Central Powers' southern flank.

This rework delivers:
1. **Native HOI4 Balance of Power (`bop_ser_civil_military`)**: Constitutional Parliament (Pašić) vs Military Intelligence Conspirators (*Crna Ruka* / Apis).
2. **The Great Retreat & Salonika Sanctuary Engine**: Complete immunity to early softlock, granting cores on operational sanctuary territories (states 184 and 44), massive surrender limit reinforcement (`surrender_limit = +0.40`), and multi-wave mobilizations spawning 25–30 divisions.
3. **Heroic Resistance**: Major Gavrilović's last stand in Belgrade, the 1915 Typhus Epidemic (Dr. Elsie Inglis), and national heroine Milunka Savić (*Iron Regiment*).
4. **4 Divergent Endgames**: Kingdom of Serbs, Croats and Slovenes (Yugoslavia), Greater Serbia Centralism, Balkan Socialist Soviet Republic, and the Black Hand Pretorian Military Junta.

---

## 2. Balance of Power Architecture (`bop_ser_civil_military`)

### Sides:
- **Left Side:** `bop_ser_pasic_parliament` (Gabinete Parlamentar & Dinastia Karađorđević)
- **Right Side:** `bop_ser_apis_black_hand` (Comitê Central da Mão Negra / Apis)

### Ranges:
1. `bop_ser_range_extreme_pasic` (-1.0 to -0.7):
   - `stability_factor = 0.15`
   - `political_power_gain = 0.25`
   - `army_org_factor = -0.10`
2. `bop_ser_range_medium_pasic` (-0.69 to -0.2):
   - `stability_factor = 0.08`
   - `political_power_gain = 0.15`
   - `army_core_defence_factor = 0.05`
3. `bop_ser_range_balanced` (-0.19 to +0.19):
   - `political_power_gain = -0.05`
4. `bop_ser_range_medium_apis` (+0.2 to +0.69):
   - `army_attack_factor = 0.08`
   - `army_core_defence_factor = 0.10`
   - `stability_factor = -0.10`
5. `bop_ser_range_extreme_apis` (+0.7 to +1.0):
   - `army_attack_factor = 0.15`
   - `army_org_regain = 0.15`
   - `stability_factor = -0.25`

---

## 3. The Great Retreat & 30-Division Spawn Specification

### Trigger Conditions:
- Country is `SER`.
- `has_war = yes` against `AUS` or `BUL` or `GER`.
- Enemy controls state 107 (Belgrade) OR state 108 (Niš) OR `surrender_progress > 0.50`.

### Map & Territorial Cores:
- `add_core_of = SER` on state 184 (Central Macedonia / Salonika).
- `add_core_of = SER` on state 44 (Albania / Durrës).
- Transfer military control of port/naval base in state 184 to `SER`.
- Idea `SER_otadzbina_u_pokretu`:
  - `surrender_limit = 0.40` (pushing threshold to $\ge 99\%$)
  - `army_core_defence_factor = 0.20`
  - `army_morale_factor = 0.15`
  - `attrition = -0.25`

### 4-Wave Mobilization:
1. Wave 1: 8 Conscript Divisions in Salonika.
2. Wave 2: 8 Yugoslav Volunteer Veteran Divisions in Salonika.
3. Wave 3: 6 Allied Shock 75mm Divisions in Salonika.
4. Wave 4: 6–8 Chetnik Irregular Guerilla Divisions behind enemy lines in states 107 & 108.
Total: 28 to 30 divisions.

---

## 4. Characters & National Heroes
- `SER_milunka_savic`: Heroine of the Iron Regiment (`national_heroine`, `army_morale_factor = 0.10`, `army_core_defence_factor = 0.10`).
- `SER_dragutin_gavrilovic`: Major of the Kalemegdan Last Stand (`defence_specialist`, `entrenchment_factor = 0.15`).

---

## 5. Verification Plan
- Unit tests in `tests/test_ww1_serbia_rework.py`.
- Integration in `scripts/qa_audit_all.py` (Suite 14).
- Clausewitz syntax and Semantic Oracle verification.
