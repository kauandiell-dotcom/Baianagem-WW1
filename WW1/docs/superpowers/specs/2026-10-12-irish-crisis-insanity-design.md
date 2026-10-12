# Design Specification: Irish Crisis Escalation, Sabotage & Civil War Engine

**Date:** 2026-10-12  
**Topic:** UK Domestic Crisis Rework (Irish Question: Extreme Historical Tension, Paramilitary Sabotage, Martial Law & Territorial Civil War)  
**Status:** DRAFT (Pending Human Partner Approval)

---

## 1. Intent and the "Why"
Historically, between 1912 and 1914, the British Empire was on the literal precipice of civil war over Irish Home Rule. Half a million Ulstermen signed the Ulster Covenant; 100,000 Ulster Volunteers (UVF) armed themselves with 25,000 smuggled German rifles; nationalist Irish Volunteers mobilized in Dublin; and British Army officers at the Curragh camp mutinied rather than enforce parliamentary rule on Ulster. The crisis was only paused by the outbreak of World War I in August 1914, only to violently erupt in the 1916 Easter Rising and the 1919-1921 War of Independence.

In the current mod state, the starting idea `ENG_irish_home_rule_tension` gave a minor `-10%` stability and `-5%` war support, which felt trivial to the player. The user requested to make this crisis deeply intense ("mais insano"), featuring:
1. Brutal starting and escalating debuffs (`-35%` to `-45%` Stability, `-15%` War Support, `-20%` Political Power gain).
2. An escalating escalation curve: starting political deadlock $\to$ paramilitary sabotage & strikes $\to$ potential open territorial civil war.
3. Two distinct player-driven resolution tracks:
   - **The Political Compromise / Dominion Track** (Home Rule with Ulster exclusion, Irish Free State creation).
   - **The Hardline Coercion / Martial Law Track** (Black and Tans, martial law, aggressive suppression of rebel cells).

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
- **Massive Strategic Dilemma:** Force the British player to actively manage domestic crises and allocate political power, military attention, and factory capacity while simultaneously fighting the Great War against Germany.
- **Phase 1: Brutal Political Gridlock (1911-1913):**
  - `ENG_irish_home_rule_tension` updated to:
    - `stability_factor = -0.35`
    - `war_support_factor = -0.15`
    - `political_power_gain = -0.20`
    - `conscription_factor = -0.15`
- **Phase 2: Paramilitary Sabotage & General Strikes (Escalation >65 Tension):**
  - Paramilitary groups arm themselves (Larne and Howth gun-running).
  - General strikes in Dublin and transport networks damage infrastructure and temporarily impair factory output.
  - Stability drops to `-45%` during peak sabotage waves.
- **Phase 3: Territorial Civil War Outbreak (Escalation >85 Tension or Unchecked Easter Rising):**
  - If tensions boil over or the 1916 Easter Rising is mishandled, the Republic of Ireland (`IRE`) secedes in southern states (Leinster, Munster, Connaught).
  - Rebel divisions spawn with stockpiled infantry equipment, forcing Britain to divert army divisions from France to fight on home soil.
- **Two Complete Strategic Resolution Tracks:**
  - *Track A (Compromise):* Buckingham Palace conference $\to$ Ulster exclusion $\to$ Dominion status for Ireland (`IRE` puppet dominion, Ulster retained by `ENG`, tensions resolved with stability bonus).
  - *Track B (Coercion):* Curragh mutiny purge/appeasement $\to$ Restoration of Order in Ireland Act $\to$ Black and Tans deployment $\to$ Military curfews and suppression of rebel cells, maintaining direct union rule at the cost of high PP and casualties.
- **Zero Hallucinated Modifiers:** All tokens validated against `data/hoi4_valid_country_modifiers.json`.
- **100% Bilingual Parity:** English and Brazilian Portuguese with UTF-8 BOM (`\xef\xbb\xbf`).

### Non-Goals
- Modifying other nations' internal mechanics (France, Germany, Russia).
- Cluttering the topbar with dozens of unmanaged permanent ideas (strictly follows the 5 Pillar `swap_ideas` architecture).

### Anti-Goals
- **No Unwinnable Soft-Locks:** The player must always have active agency through decisions to navigate, prevent, or defeat the crisis with skill and preparation.
- **No Ghost Variables:** Every action and tension level change must be clearly communicated via custom effect tooltips and decision UI indicators.

---

## 3. Detailed Mechanical Architecture

### A. The Pillar 5 Ideas (`common/ideas/ww1_britain_ideas.txt`)
- `ENG_irish_home_rule_tension` (Initial State):
  - `stability_factor = -0.35`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.20`
  - `conscription_factor = -0.15`
- `ENG_irish_sabotage_wave` (Active during Phase 2 Sabotage):
  - `stability_factor = -0.45`
  - `war_support_factor = -0.15`
  - `political_power_gain = -0.25`
  - `conscription_factor = -0.25`
  - `industrial_capacity_factory = -0.05`
- `ENG_irish_martial_law` (Active during Hardline Coercion):
  - `stability_factor = -0.20`
  - `political_power_gain = -0.15`
  - `army_morale_factor = -0.05`
  - `conscription_factor = -0.10`
- `ENG_irish_home_rule_compromise` (Successful Compromise / Dominion):
  - `stability_factor = 0.05`
  - `political_power_gain = 0.05`
- `ENG_irish_union_secured` (Successful Coercion & Pacification):
  - `stability_factor = 0.05`
  - `war_support_factor = 0.05`
  - `conscription_factor = 0.05`

### B. Dedicated Decision Category (`ENG_ww1_irish_crisis_category`)
Tracked variables displayed in decision header:
- `ww1_britain_irish_tension` (Nationalist/Catholic resistance, 0 to 100)
- `ww1_britain_ulster_tension` (Loyalist/Protestant resistance, 0 to 100)

**Decisions:**
1. *Larne Arms Interdiction*: Dispatch Royal Navy destroyers to Belfast Lough to intercept Carson's German Mausers (lowers Ulster tension, costs PP/convoys).
2. *Dublin Curfew & Security*: Impose curfews to suppress the Irish Citizen Army and reduce nationalist strike disruption.
3. *Appease Curragh Officers*: Promise not to order soldiers against Ulster, preventing BEF army organization loss at the cost of nationalist fury.
4. *Purge Rebellious Officers*: Stand firm on parliamentary supremacy; eliminates loyalist leverage but causes `-10%` division organization for 180 days.
5. *Deploy Special Reserve / Black and Tans*: Mobilize aggressive auxiliary police units to smash rebel headquarters (lowers tension rapidly, causes `-5%` stability and civilian backlash).
6. *Buckingham Palace Conference*: Convene royal round-table to negotiate partition and County Option.
7. *Enact Irish Free State Treaty*: Release southern Ireland as autonomous dominion (`IRE`), pacifying Ireland forever and unlocking Irish trade/manpower.

### C. Narrative Events & Civil War Trigger (`events/ww1_britain_events.txt`)
1. **The Curragh Incident (March 1914)**:
   - General Paget and officers at Curragh refuse orders. Player must choose between military discipline vs political capitulation.
2. **The Gun-Running Crisis (July 1914)**:
   - Howth and Larne gun-running events arming the respective volunteer armies.
3. **The 1916 Easter Rising (April 1916)**:
   - Armed rebels seize Dublin General Post Office.
   - If dealt with heavy artillery: high immediate casualties, sets up massive guerilla backlash.
   - If handled with negotiation or restraint: lower immediate casualties, but tests government authority.
4. **Outbreak of Open Civil War (`ww1_britain_pol.irish_civil_war`)**:
   - Fires if `ww1_britain_irish_tension >= 85` during wartime, or if Easter Rising escalates out of control.
   - States 113 (Munster), 114 (Connaught), 117 (Leinster) are transferred to newly released hostile tag `IRE`.
   - State 119 (Northern Ireland / Ulster) remains in British hands.
   - Britain and `IRE` enter declared war (`declare_war_on`).
   - `IRE` receives 6 insurgent infantry divisions (`Irish Republican Army`) armed with equipment.
   - Britain receives temporary spirit `ENG_irish_civil_war_debacle` until Dublin is recaptured.

---

## 4. Verification and QA Acceptance Criteria
1. **Clausewitz Semantic Oracle Validation**: All modifier tokens in new and modified ideas/decisions pass `audit_file_modifiers` with 0 unknown tokens.
2. **Anti-Stacking Rule**: Pillar 5 ideas transition cleanly using `swap_ideas`, never adding unmanaged duplicate ideas to the topbar.
3. **Automated Test Coverage**:
   - `test_ww1_britain_complete_audit.py` updated to verify the new Irish crisis ideas, decisions, and event triggers.
   - `qa_audit_all.py` passes with 0 errors across all tiers.
4. **UTF-8 BOM Integrity**: Both `ww1_britain_l_english.yml` and `ww1_britain_l_braz_por.yml` maintain mandatory `\xef\xbb\xbf` header.
