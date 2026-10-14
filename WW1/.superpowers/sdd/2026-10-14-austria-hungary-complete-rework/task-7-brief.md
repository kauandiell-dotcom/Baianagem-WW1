# Task 7 Brief: Pre-War Espionage (Colonel Redl), Sixtus Affair & Danubian Hegemony

## Objective
Implement deep historical diplomacy events, covert espionage crises, and separate peace initiatives for Austria-Hungary:
1. **The Colonel Redl Espionage Affair (May 1913)** (`ww1_austria_diplomacy.1`):
   - Evidenzbureau counter-espionage unmasks Colonel Alfred Redl selling mobilization plans (Plan B - Balkans, Plan R - Russia) to the Russian Okhrana.
   - Option A: Overhaul General Staff mobilization war books (costs 50 PP, removes Russian strategic planning advantage).
   - Option B: Cover up suicide to preserve Evidenzbureau honor (-10% army defense vs Russia in 1914).
2. **The Sixtus Affair (March 1917)** (`ww1_austria_diplomacy.10`):
   - Emperor Karl I initiates clandestine peace feelers to France via Prince Sixte of Bourbon-Parma.
   - If Germany refuses negotiated peace, Austria can explore separate exit conditions without capitulation.
3. **The Austro-Polish Solution** (`ww1_austria_diplomacy.20`):
   - Proclamation of Archduke Karl Stephan as King of Poland, creating an autonomous client kingdom aligned with Vienna instead of Berlin.
4. **The Brotfrieden / Bread Peace (February 1918)** (`ww1_austria_diplomacy.30`):
   - Concludes agricultural treaty with Ukraine, transferring massive grain shipments to Vienna (+40 `AUH_vienna_grain`), averting urban bread riots.
5. **Danubian Hegemony Decisions** in `common/decisions/ww1_austria_diplomacy_decisions.txt`:
   - Decision category: `AUH_crown_dashboard` or `AUH_danubian_diplomacy`
   - Include fast-failing `allowed = { original_tag = AUS }`
   - Decisions for:
     - `AUH_dec_prince_wied_albania`: Backing Prince Wilhelm of Wied in Albania.
     - `AUH_dec_danubian_customs_union`: Establishing preferential tariff zone across the Balkans.

## Context
- Working Directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- Spec: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Plan: `docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md`

## Deliverables
1. `events/ww1_austria_diplomacy_events.txt`:
   - Namespace: `ww1_austria_diplomacy`
   - Events `ww1_austria_diplomacy.1`, `ww1_austria_diplomacy.10`, `ww1_austria_diplomacy.20`, `ww1_austria_diplomacy.30`.
2. `common/decisions/ww1_austria_diplomacy_decisions.txt`:
   - Fast-failing `allowed = { original_tag = AUS }`.
   - Decisions `AUH_dec_prince_wied_albania` and `AUH_dec_danubian_customs_union`.
3. Bracket balance check: 100% (Diff = 0).
4. Commit:
   - `git add events/ww1_austria_diplomacy_events.txt common/decisions/ww1_austria_diplomacy_decisions.txt`
   - `git commit -m "feat(auh): implement Colonel Redl espionage affair, Sixtus peace negotiations, and Danubian hegemony"`
