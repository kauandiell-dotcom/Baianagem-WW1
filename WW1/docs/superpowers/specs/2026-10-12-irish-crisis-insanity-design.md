# Design Specification: Irish Crisis Escalation, Sabotage & Civil War Engine

**Date:** 2026-10-12  
**Topic:** UK Domestic Crisis Rework (Irish Question: Extreme Historical Tension, Paramilitary Sabotage, Martial Law & Territorial Civil War)  
**Status:** DRAFT (Architectural Review Complete, Pending Human Partner Approval)

---

## 1. Intent and the "Why"
Historically, between 1912 and 1914, the British Empire was on the literal precipice of civil war over Irish Home Rule. Half a million Ulstermen signed the Ulster Covenant; 100,000 Ulster Volunteers (UVF) armed themselves with 25,000 smuggled German rifles; nationalist Irish Volunteers mobilized in Dublin; and British Army officers at the Curragh camp mutinied rather than enforce parliamentary rule on Ulster. The crisis was only paused by the outbreak of World War I in August 1914, only to violently erupt in the 1916 Easter Rising and the 1919-1921 War of Independence.

In the current mod state, the starting idea `ENG_irish_home_rule_tension` gave a minor `-10%` stability and `-5%` war support, which felt trivial. The user requested to make this crisis deeply intense ("mais insano"), featuring:
1. Brutal starting and escalating debuffs (`-35%` to `-45%` Stability, `-15%` War Support, `-20%` Political Power gain).
2. An escalating escalation curve: starting political deadlock $\to$ paramilitary sabotage & strikes $\to$ potential open territorial civil war on the map.
3. Two distinct player-driven resolution tracks:
   - **The Political Compromise / Dominion Track** (Home Rule with Ulster exclusion, Irish Free State creation).
   - **The Hardline Coercion / Martial Law Track** (Black and Tans, martial law, aggressive suppression of rebel cells).

---

## 2. Architectural Answers (Builder Review Settlements)

### 1. Focus Tree Integration (`uk.txt`)
- In 1914, the focus `ENG_ww1_the_defence_of_the_realm` (DORA) will NOT wipe out the crisis. Instead, it swaps `ENG_irish_home_rule_tension` to `ENG_irish_home_rule_suspended` (`-25%` stability, `-10%` war support), which starts the countdown to the **1916 Easter Rising**.
- Post-war focuses `ENG_ww1_the_irish_settlement_conference` and `ENG_ww1_dominion_status_for_ireland` are the historical capstones of Track A (Compromise).

### 2. Tag `IRE` Insurrection & Localized Peace Resolution
- Tag `IRE` revolts with rule `can_join_factions = no` to prevent it from joining the Central Powers (Germany) and blocking the game in an un-annexable global peace conference.
- When Dublin (state 117) is retaken and `IRE` capitulates, an immediate custom peace event fires: `ENG` fully annexes `IRE`, clears rebel divisions, and swaps `ENG_irish_civil_war_debacle` to `ENG_irish_union_secured`.

### 3. Crisis Escalation Engine: Periodic Mission Loop
- In the decision category `ENG_ww1_irish_crisis_category`, a 120-day mission **"The Gathering Storm in Ireland"** monitors the tensions:
  - If `ww1_britain_irish_tension > 65`: Triggers railway/factory sabotage events and swaps Pillar 5 to `ENG_irish_sabotage_wave` (`-45%` stability).
  - If `ww1_britain_irish_tension >= 85`: Triggers the armed Civil War event.

### 4. Role and Consequence of `ww1_britain_ulster_tension`
- If Ulster tension exceeds 70: Triggers the **Curragh Army Mutiny** event, hitting the British Army with `-15%` division organization and planning speed, and locking Track A compromise decisions until Ulster is reassured.

### 5. Timing and Gating of Track A (Compromise)
- Track A's final treaty decision (*Enact Irish Free State Treaty*) is gated behind `date > 1917.1.1` or post-war conditions, preventing players from cheesing the entire wartime dilemma in 1912.

### 6. Track B (Coercion) Resolution
- Can be achieved either by winning the Civil War on the map OR by maintaining Martial Law and driving nationalist tension below 15 for 180 days via the decision "Restore Order in Ireland Act".

---

## 3. Detailed Mechanical Architecture

### A. Pillar 5 Ideas (`common/ideas/ww1_britain_ideas.txt`)
- `ENG_irish_home_rule_tension` (Initial State 1911):
  - `stability_factor = -0.35`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.20`
  - `conscription_factor = -0.15`
- `ENG_irish_sabotage_wave` (Phase 2 Escalation >65):
  - `stability_factor = -0.45`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.25`
  - `conscription_factor = -0.25`
  - `industrial_capacity_factory = -0.05`
- `ENG_irish_home_rule_suspended` (Wartime Suspension 1914-1916):
  - `stability_factor = -0.25`
  - `war_support_factor = -0.10`
  - `political_power_gain = -0.15`
- `ENG_irish_martial_law` (Hardline Coercion):
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

### B. Dedicated Decision Category (`ENG_ww1_irish_crisis_category`)
- Tracked variables displayed in decision header:
  - `ww1_britain_irish_tension` (Nationalist/Catholic resistance, 0 to 100)
  - `ww1_britain_ulster_tension` (Loyalist/Protestant resistance, 0 to 100)
- Decisions:
  1. *Larne Arms Interdiction*: Royal Navy destroyers patrol Belfast Lough.
  2. *Dublin Curfew & Security*: Impose curfews, reducing sabotage risk.
  3. *Appease Curragh Officers*: Pacify Ulster tension, but angers Nationalists.
  4. *Purge Mutinous Officers*: Reasserts Westminster authority, hits BEF org by `-10%`.
  5. *Deploy Black and Tans (Auxiliary Division)*: Ruthlessly suppresses nationalist cells, costs stability.
  6. *Buckingham Palace Conference*: Diplomatic summit to lower both tensions.
  7. *Restore Order in Ireland (Track B Capstone)*: Available under Martial Law if tension < 15.
  8. *Enact Irish Free State Treaty (Track A Capstone)*: Gated post-1917 or post-war.

### C. Narrative Events & Civil War Trigger (`events/ww1_britain_events.txt`)
1. **The Curragh Incident (March 1914)**: Mutiny of cavalry officers.
2. **Larne & Howth Gun-Running (July 1914)**: German Mausers smuggled ashore.
3. **1916 Easter Rising (April 1916)**: Dublin GPO seized; player chooses military shelling vs containment.
4. **Outbreak of Irish Civil War (`ww1_britain_pol.irish_civil_war`)**:
   - Secession of states 113, 114, 117 to `IRE`.
   - Ulster (119) remains British; UVF militias spawn in Belfast.
   - 6 insurgent IRA divisions spawn in Dublin/Cork.
   - Britain must divert divisions from France to retake Dublin.
   - Capitulation of `IRE` immediately annexes Ireland back and grants `ENG_irish_union_secured`.

---

## 4. Verification and QA Acceptance Criteria
1. **Clausewitz Semantic Oracle Validation**: All modifier tokens pass `audit_file_modifiers` with 0 errors.
2. **Anti-Stacking Rule**: Pillar 5 ideas transition cleanly using `swap_ideas`, never exceeding 5 concurrent ideas.
3. **Automated Test Coverage**:
   - `test_ww1_britain_complete_audit.py` updated to cover Irish crisis ideas, decisions, and event triggers.
   - `qa_audit_all.py` passes with exit code 0.
4. **UTF-8 BOM Integrity**: Both language files maintain `\xef\xbb\xbf`.
