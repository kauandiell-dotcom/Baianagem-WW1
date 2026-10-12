# Task 6 Brief: Bilingual Localisation & UTF-8 BOM (`localisation/`)

## Objective
Provide complete bilingual localisation (English and Brazilian Portuguese) for all newly created Irish crisis ideas, decisions, categories, and events, strictly preserving UTF-8 BOM encoding.

## Context & Files
- English: `localisation/english/ww1_britain_l_english.yml`
- Portuguese: `localisation/braz_por/ww1_britain_l_braz_por.yml`
- Spec: `docs/superpowers/specs/2026-10-12-irish-crisis-insanity-design.md`
- Plan: `docs/superpowers/plans/2026-10-12-irish-crisis-insanity-plan.md`

## Requirements
1. **Keys to Localise in both English and Portuguese:**
   - Ideas:
     - `ENG_irish_sabotage_wave`, `ENG_irish_sabotage_wave_desc`
     - `ENG_irish_martial_law`, `ENG_irish_martial_law_desc`
     - `ENG_irish_civil_war_debacle`, `ENG_irish_civil_war_debacle_desc`
     - `ENG_irish_union_secured`, `ENG_irish_union_secured_desc`
     - `ENG_irish_home_rule_suspended`, `ENG_irish_home_rule_suspended_desc`
   - Category:
     - `ENG_ww1_irish_crisis_category`, `ENG_ww1_irish_crisis_category_desc`
   - Decisions:
     - `ENG_deploy_crown_garrison`, `ENG_deploy_crown_garrison_desc`
     - `ENG_raid_paramilitary_armories`, `ENG_raid_paramilitary_armories_desc`
     - `ENG_emergency_curfew_lockdown`, `ENG_emergency_curfew_lockdown_desc`
     - `ENG_larne_arms_interdiction`, `ENG_larne_arms_interdiction_desc`
     - `ENG_deploy_black_and_tans`, `ENG_deploy_black_and_tans_desc`
     - `ENG_restore_order_in_ireland_act`, `ENG_restore_order_in_ireland_act_desc`
     - `ENG_enact_irish_free_state_treaty`, `ENG_enact_irish_free_state_treaty_desc`
   - Events:
     - `ww1_britain_pol.curragh_mutiny.t`, `ww1_britain_pol.curragh_mutiny.d`, `ww1_britain_pol.curragh_mutiny.a`, `ww1_britain_pol.curragh_mutiny.b`
     - `ww1_britain_pol.larne_howth_guns.t`, `ww1_britain_pol.larne_howth_guns.d`, `ww1_britain_pol.larne_howth_guns.a`
     - `ww1_britain_pol.irish_civil_war.t`, `ww1_britain_pol.irish_civil_war.d`, `ww1_britain_pol.irish_civil_war.a`
     - `ww1_britain_pol.ireland_pacified.t`, `ww1_britain_pol.ireland_pacified.d`, `ww1_britain_pol.ireland_pacified.a`

2. **UTF-8 BOM Encoding:**
   Both files must begin with the byte sequence `\xef\xbb\xbf`.
   Verify with:
   `python -c "for p in ['localisation/english/ww1_britain_l_english.yml', 'localisation/braz_por/ww1_britain_l_braz_por.yml']: b = open(p, 'rb').read(3); assert b == b'\xef\xbb\xbf', f'{p} missing BOM'"`

3. **Verify with QA Audit:**
   Run: `python scripts/qa_audit_all.py`

4. **Commit:**
   `git add localisation/english/ww1_britain_l_english.yml localisation/braz_por/ww1_britain_l_braz_por.yml`
   `git commit -m "feat(uk): add complete bilingual localization with UTF-8 BOM for Irish crisis engine"`

5. **Write report to:**
   `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\task-6-report.md`
