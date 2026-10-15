# Task 3 Report: French Republic Dashboard & The 4 Dynamic Survival Vectors

**Date:** 2026-10-15  
**Commit:** `bc8fe00913e2ff790b6a154b845326918020412a`  
**Status:** Completed & Validated  

---

## 1. Executive Summary

Task 3 of the French Republic overhaul has been implemented and verified. The French Republic Dashboard introduces 4 dynamic survival vectors tracking wartime endurance, social cohesion, and material readiness, paired with an automated weekly callback hook, dynamic spirit transitions, and emergency survival decisions.

---

## 2. Deliverables Implemented

### A. Scripted Effects (`common/scripted_effects/ww1_france_dashboard_effects.txt`)
- **`FRA_init_republic_dashboard`**:
  - `FRA_union_sacree_cohesion = 80`
  - `FRA_poilu_morale = 75`
  - `FRA_charbon_et_acier = 70`
  - `FRA_reserves_humaines = 85`
- **`FRA_clamp_dashboard_variables`**:
  - Clamps all 4 survival vectors strictly between 0 and 100 via `clamp_variable = { var = ... min = 0 max = 100 }`.
- **`FRA_weekly_republic_tick`**:
  - Self-initialization fallback on missing variables.
  - Wartime burn rate:
    - Coal & Steel: -1/week base consumption.
    - Loss of Northeastern industrial heartland (Briey-Longwy state 18 or Nord-Pas-de-Calais state 28): additional -1/week.
    - Demographic & morale strain: base weariness on morale (-0.20/week), Union Sacrée (-0.15/week), and human reserves (-0.10/week).
    - Frontline collapse penalties based on surrender progress (>10% and >25%).
  - Dynamic spirit management:
    - `FRA_union_sacree_cohesion`: applies `FRA_union_sacree_fractured` if < 30; removes and applies `FRA_union_sacree_strong` if >= 75.
    - `FRA_poilu_morale`: applies `FRA_poilu_morale_demoralized` if < 30; removes and applies `FRA_poilu_morale_high` if >= 70.
    - `FRA_charbon_et_acier`: applies `FRA_charbon_et_acier_famine` if < 25; clears famine if >= 50; applies `FRA_charbon_et_acier_surplus` if >= 75.

### B. On-Actions Integration (`common/on_actions/ww1_crisis_on_actions.txt`)
- Hooked under `on_weekly_FRA`:
  - Tag check (`tag = FRA`).
  - Flag check (`fra_dashboard_initialized`) initializing the dashboard on the first tick.
  - Calls `FRA_clamp_dashboard_variables = yes` and `FRA_weekly_republic_tick = yes`.

### C. Dashboard Dynamic Ideas (`common/ideas/ww1_france_dashboard_ideas.txt`)
- `FRA_union_sacree_strong`: +8% stability, +0.10 political power gain.
- `FRA_union_sacree_fractured`: -15% stability, -0.15 political power gain.
- `FRA_poilu_morale_high`: +10% army morale factor, +10% army core defence factor.
- `FRA_poilu_morale_demoralized`: -20% army morale factor, -15% army attack factor.
- `FRA_charbon_et_acier_surplus`: +10% industrial capacity factory.
- `FRA_charbon_et_acier_famine`: -25% industrial capacity factory, +5% consumer goods factor.
- **Modifier Compliance:** 100% valid Clausewitz modifiers verified via `scripts/hoi4_semantic_oracle.py` (0 errors).

### D. Emergency Survival Decisions (`common/decisions/ww1_france_dashboard_decisions.txt`)
- Category `FRA_war_economy_and_munitions`:
  - `FRA_dec_british_channel_coal`: Requisitions British coal convoys (+20 charbon, 25 PP, 60-day cooldown).
  - `FRA_dec_call_up_class_1917`: Mobilizes the *Bleuets* (+50k manpower, +15 human reserves, -5% stability, 30 PP, once).
  - `FRA_dec_colonial_recruitment_tirailleurs`: Recruits Senegalese and Algerian riflemen (+60k manpower, +10 human reserves, 35 PP, 120-day cooldown).
- Category `FRA_third_republic_politics`:
  - `FRA_dec_union_sacree_cross_party_pact`: Convenes the Chamber of Deputies (+15 Union Sacrée cohesion, +5% stability, 30 PP, 90-day cooldown).
- All decisions include fast-failing `allowed = { original_tag = FRA }`.

---

## 3. QA & Validation Results

1. **Unit Test:**
   ```
   python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_republic_dashboard_variables -v
   test_republic_dashboard_variables (tests.test_ww1_france_rework.TestFranceOverhaul.test_republic_dashboard_variables) ... ok
   Ran 1 test in 0.001s
   OK
   ```
2. **Semantic Oracle Modifier Audit:**
   - Target: `common/ideas/ww1_france_dashboard_ideas.txt`
   - Errors: 0
3. **Bracket Balance Audit:**
   - `common/scripted_effects/ww1_france_dashboard_effects.txt`: Open = 80, Close = 80, Diff = 0
   - `common/on_actions/ww1_crisis_on_actions.txt`: Open = 34, Close = 34, Diff = 0
   - `common/ideas/ww1_france_dashboard_ideas.txt`: Open = 20, Close = 20, Diff = 0
   - `common/decisions/ww1_france_dashboard_decisions.txt`: Open = 47, Close = 47, Diff = 0

---

## 4. Git Commit
- **Hash:** `bc8fe00` (`bc8fe00913e2ff790b6a154b845326918020412a`)
- **Message:** `feat(fra): implement French Republic Dashboard, 4 survival vectors, and emergency decisions`
- **Files Committed:**
  - `common/scripted_effects/ww1_france_dashboard_effects.txt`
  - `common/on_actions/ww1_crisis_on_actions.txt`
  - `common/ideas/ww1_france_dashboard_ideas.txt`
  - `common/decisions/ww1_france_dashboard_decisions.txt`
