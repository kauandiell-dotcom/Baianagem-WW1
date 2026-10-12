# Design Specification: Irish Crisis Escalation, State Securing & Civil War Engine

**Date:** 2026-10-12  
**Topic:** UK Domestic Crisis Rework (Irish Question: Extreme Historical Tension, Map-Based State Securing, Paramilitary Sabotage, Martial Law & Territorial Civil War)  
**Status:** DRAFT (Ready for Human Partner Approval)

---

## 1. Intent and the "Why"
Historically, between 1912 and 1914, the British Empire was on the literal precipice of civil war over Irish Home Rule. Half a million Ulstermen signed the Ulster Covenant; 100,000 Ulster Volunteers (UVF) armed themselves with 25,000 smuggled German rifles; nationalist Irish Volunteers mobilized in Dublin; and British Army officers at the Curragh camp mutinied rather than enforce parliamentary rule on Ulster. The crisis was only paused by the outbreak of World War I in August 1914, only to violently erupt in the 1916 Easter Rising and the 1919-1921 War of Independence.

The user requested an intense, high-stakes system ("deixa mais insano isso aqui"):
1. **Severe national penalties:** `-35%` to `-45%` Stability, `-15%` War Support, `-20%` Political Power gain.
2. **Map-Based State Securing Mechanics (inspired by the Spanish Civil War / MTG US Civil War):** Players interact directly with the 4 Irish states on the map to contain unrest and secure garrisons.
3. **High-Price Strategic Anti-Cheese:** The player cannot simply spam clicks to resolve the crisis in 1911. Securing states demands massive commitments of manpower, infantry rifles, political power, and parliamentary capital, forcing a brutal trade-off against the Western Front war effort in France.
4. **Escalating Crisis:** Political gridlock $\to$ paramilitary sabotage and strikes $\to$ territorial civil war if unsecured.
5. **Two Historical Resolution Tracks:** Political Compromise (Dominion status) vs Hardline Coercion (Martial law and Union preserved).

---

## 2. Map-Based State Securing Engine (The 4 States of Ireland)

### A. The 4 Target States
1. **Ulster / Belfast** (State 119)
2. **Leinster / Dublin** (State 117)
3. **Munster / Cork** (State 113)
4. **Connaught / Galway** (State 114)

### B. State Statuses (Visual State Modifiers & Flags)
- 🟢 **Garrison Secured by the Crown (`ENG_state_garrison_secured`)**:
  - Full British military control; 0% sabotage risk.
  - If Civil War erupts, this state **remains British** and spawns local loyalist defense militia.
- 🟡 **Contested Unrest (`ENG_state_contested_unrest`)**:
  - Active street clashes and paramilitary drilling.
  - Suffers periodic railway/factory sabotage events (`damage_building`).
  - If Civil War erupts, state is fought over; infrastructure takes heavy damage.
- 🔴 **Rebel Stronghold (`ENG_state_rebel_stronghold`)**:
  - Underground Republican/UVF councils hold de facto control.
  - If Civil War erupts, the state **instantly defects to `IRE`**, spawning armed insurgent divisions.

### C. State-Targeted Decisions (`state_target = yes`)
Located in category `ENG_ww1_irish_crisis_category`:
1. **Deploy Crown Garrison & Consolidate Control**:
   - *Cost:* 35 Political Power, 25,000 Manpower, 500 Infantry Equipment.
   - *Duration:* 60 days.
   - *Effect:* Promotes state status (Rebel $\to$ Contested, or Contested $\to$ Secured).
2. **Raid Paramilitary Armories**:
   - *Cost:* 25 Political Power, 10 Army Experience / Command Power.
   - *Effect:* Lowers local rebellion progress; 15% chance to trigger violent street protests.
3. **Emergency Curfew & Constabulary Lockdown**:
   - *Cost:* 20 Political Power, 1 Civilian Factory for 90 days.
   - *Effect:* Halts sabotage in the state for 120 days.

### D. Anti-Cheese & High-Price Strategic Constraints
To prevent players from trivially securing all 4 states before 1912:
- **Strict Concurrency Limit:** Britain can only run a security operation in **one state at a time**.
- **The Westminster Coalition Constraint (1911-1914):**
  - Asquith's Liberal government relies on John Redmond's Irish Parliamentary Party for its majority.
  - Militarily locking down southern states (Leinster/Munster/Connaught) before 1914 damages government stability (`-10%` per premature armed crackdown) due to parliamentary boycotts.
- **The Seesaw / Balloon Effect:**
  - Crackdowns in the South cause Carson and Ulster lealists to suspect Home Rule is being enforced, spiking `ww1_britain_ulster_tension`.
  - Reassuring Ulster spikes `ww1_britain_irish_tension` in the South.
- **The Great War Dilemma (1914-1918):**
  - Once WW1 begins in August 1914, every rifle and soldier kept on garrison duty in Ireland is desperately missed at Mons, the Marne, and Ypres.
  - It is **theoretically possible** to secure Dublin (Leinster) and Belfast (Ulster), but only if the player deliberately sacrifices reserves needed on the French front.

---

## 3. Pillar 5 Dynamic Ideas (`common/ideas/ww1_britain_ideas.txt`)

Following the strict 5 Pillar anti-stacking rule, Pillar 5 evolves via `swap_ideas`:
- `ENG_irish_home_rule_tension` (Initial State 1911):
  - `stability_factor = -0.35`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.20`
  - `conscription_factor = -0.15`
- `ENG_irish_sabotage_wave` (Escalation Phase 2 when Tension > 65):
  - `stability_factor = -0.45`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.25`
  - `conscription_factor = -0.25`
  - `industrial_capacity_factory = -0.05`
- `ENG_irish_home_rule_suspended` (Wartime Suspension 1914-1916 via DORA focus):
  - `stability_factor = -0.25`
  - `war_support_factor = -0.10`
  - `political_power_gain = -0.15`
- `ENG_irish_martial_law` (Active during Hardline Coercion):
  - `stability_factor = -0.20`
  - `political_power_gain = -0.15`
  - `army_morale_factor = -0.05`
  - `conscription_factor = -0.10`
- `ENG_irish_civil_war_debacle` (Active during Civil War):
  - `stability_factor = -0.40`
  - `war_support_factor = -0.20`
  - `political_power_gain = -0.30`
  - `army_org_factor = -0.10`
- `ENG_irish_home_rule_compromise` (Track A Victory):
  - `stability_factor = 0.05`
  - `political_power_gain = 0.05`
- `ENG_irish_union_secured` (Track B Victory):
  - `stability_factor = 0.05`
  - `war_support_factor = 0.05`
  - `conscription_factor = 0.05`

---

## 4. Narrative Events & Civil War Trigger (`events/ww1_britain_events.txt`)

1. **Curragh Mutiny (March 1914)**:
   - British cavalry officers at Curragh camp refuse orders to march on Ulster.
   - *Option A (Cede to Officers):* Ulster tension drops, but government authority takes a hit and Nationalist tension rises.
   - *Option B (Purge Mutineers):* Reasserts Westminster authority, but inflicts `-10%` organization on the British Army (BEF) on the eve of WW1.
2. **Gun-Running Crisis (July 1914)**:
   - Larne gun-running (Ulster) and Howth gun-running (Nationalists) flood Ireland with German Mauser rifles.
3. **Easter Rising (April 1916)**:
   - Dublin Post Office seized by armed rebels.
   - If Dublin (State 117) is 🟢 *Secured*, the garrison swiftly repels the rebels with minimal collateral damage.
   - If Dublin is 🟡 *Contested* or 🔴 *Rebel*, heavy street fighting damages the capital and triggers immediate escalation toward civil war.
4. **Outbreak of the Irish Civil War (`ww1_britain_pol.irish_civil_war`)**:
   - Triggers if Nationalist tension reaches 85+ or if the Easter Rising escalates out of control.
   - Any state with status 🔴 *Rebel Stronghold* or unmanaged 🟡 *Contested* defects to tag `IRE`.
   - States with status 🟢 *Secured* stay under British control.
   - `IRE` receives 6-8 insurgent divisions with German weaponry.
   - `IRE` is blocked from joining foreign factions (`can_join_factions = no`).
   - Retaking Dublin (117) and capitulating `IRE` triggers an immediate peace event that annexes Ireland back into `ENG` and rewards `ENG_irish_union_secured`.

---

## 5. Verification and Quality Assurance
1. **Clausewitz Semantic Oracle Validation**: All country and state modifier tokens pass `audit_file_modifiers` with 0 errors.
2. **Pillar 5 Anti-Stacking Integrity**: Pillar 5 ideas transition exclusively through `swap_ideas`.
3. **Automated Master QA Test Suite**: `test_ww1_britain_complete_audit.py` and `qa_audit_all.py` pass with Exit Code 0.
4. **UTF-8 BOM Bilingual Localisation**: Complete text in English and Brazilian Portuguese with mandatory `\xef\xbb\xbf` encoding.
