# Task 6 Implementation Report: Bilingual Localisation & UTF-8 BOM (`localisation/`)

**Date:** 2026-10-12  
**Target Files:**
- `localisation/english/ww1_britain_l_english.yml`
- `localisation/braz_por/ww1_britain_l_braz_por.yml`  
**Commit:** `c134996` (`feat(uk): add complete bilingual localization with UTF-8 BOM for Irish crisis engine`)  
**Status:** COMPLETE (All QA audits, unit tests, and BOM integrity validations pass)

---

## 1. Summary of Changes

Delivered complete, high-flavor, historically immersive bilingual localisation for both English (`l_english`) and Brazilian Portuguese (`l_braz_por`), strictly maintaining the mandatory Paradox Clausewitz UTF-8 BOM encoding (`\xef\xbb\xbf`), 1-to-1 key parity, and lexicographical sort order.

### Localised Keys Overview (49 Keys Added/Refined across both languages)

1. **Ideas (Pillar 5 Dynamic States):**
   - `ENG_irish_sabotage_wave`, `ENG_irish_sabotage_wave_desc` ("Wave of Irish Sabotage" / "Onda de Sabotagem Irlandesa")
   - `ENG_irish_martial_law`, `ENG_irish_martial_law_desc` ("Martial Law in Ireland" / "Lei Marcial na Irlanda")
   - `ENG_irish_civil_war_debacle`, `ENG_irish_civil_war_debacle_desc` ("Irish Civil War Debacle" / "Desastre da Guerra Civil Irlandesa")
   - `ENG_irish_union_secured`, `ENG_irish_union_secured_desc` ("The Union Secured" / "A União Assegurada")
   - `ENG_irish_home_rule_suspended`, `ENG_irish_home_rule_suspended_desc` (verified and retained in both languages)

2. **Decision Category:**
   - `ENG_ww1_irish_crisis_category`, `ENG_ww1_irish_crisis_category_desc` ("The Irish Crisis" / "A Crise Irlandesa")

3. **Decisions & Strategic Actions:**
   - `ENG_deploy_crown_garrison`, `ENG_deploy_crown_garrison_desc`
   - `ENG_raid_paramilitary_armories`, `ENG_raid_paramilitary_armories_desc`
   - `ENG_emergency_curfew_lockdown`, `ENG_emergency_curfew_lockdown_desc`
   - `ENG_larne_arms_interdiction`, `ENG_larne_arms_interdiction_desc`
   - `ENG_appease_curragh_officers`, `ENG_appease_curragh_officers_desc`
   - `ENG_purge_curragh_officers`, `ENG_purge_curragh_officers_desc`
   - `ENG_deploy_black_and_tans`, `ENG_deploy_black_and_tans_desc`
   - `ENG_restore_order_in_ireland_act`, `ENG_restore_order_in_ireland_act_desc`
   - `ENG_enact_irish_free_state_treaty`, `ENG_enact_irish_free_state_treaty_desc`

4. **State Status Flags & Tooltips:**
   - `ENG_state_garrison_secured`, `ENG_state_garrison_secured_desc` ("Garrison Secured by the Crown" / "Guarnição Assegurada pela Coroa")
   - `ENG_state_contested_unrest`, `ENG_state_contested_unrest_desc` ("Contested Sectarian Unrest" / "Conflito Sectário Contestado")
   - `ENG_state_rebel_stronghold`, `ENG_state_rebel_stronghold_desc` ("Rebel Paramilitary Stronghold" / "Bastião Paramilitar Rebelde")
   - `ENG_curfew_active`, `ENG_curfew_active_desc` ("Emergency Curfew Active" / "Toque de Recolher Ativo")

5. **Historical Events & Diplomatic Ultimatums:**
   - Curragh Mutiny: `ww1_britain_pol.curragh_mutiny.t`, `ww1_britain_pol.curragh_mutiny.d`, `ww1_britain_pol.curragh_mutiny.a`, `ww1_britain_pol.curragh_mutiny.b`
   - Larne & Howth Gun-Running: `ww1_britain_pol.larne_howth_guns.t`, `ww1_britain_pol.larne_howth_guns.d`, `ww1_britain_pol.larne_howth_guns.a`
   - Outbreak of Civil War: `ww1_britain_pol.irish_civil_war.t`, `ww1_britain_pol.irish_civil_war.d`, `ww1_britain_pol.irish_civil_war.a`
   - Pacification & Capitulation: `ww1_britain_pol.ireland_pacified.t`, `ww1_britain_pol.ireland_pacified.d`, `ww1_britain_pol.ireland_pacified.a`

---

## 2. Technical Standards & Engine Validation

1. **UTF-8 BOM Integrity:**
   - Both files verified starting with exact 3-byte BOM sequence `\xef\xbb\xbf`.
   - Verified via:
     `python -c "for p in ['localisation/english/ww1_britain_l_english.yml', 'localisation/braz_por/ww1_britain_l_braz_por.yml']: b = open(p, 'rb').read(3); assert b == b'\xef\xbb\xbf', f'{p} missing BOM'"`
   - Result: PASS.

2. **Bilingual Key Parity & Ordering:**
   - Exactly 974 localized keys in both files.
   - Exact 1-to-1 key alignment between `ww1_britain_l_english.yml` and `ww1_britain_l_braz_por.yml`.
   - Zero missing keys, zero untranslated tokens.

3. **Paradox YAML Syntax Standards:**
   - All entries formatted with standard straight quotes (`""`) and version index `:0`.
   - Replaced accidental non-ASCII curly quotation marks (`\u2019`) with standard ASCII apostrophes (`'`).
   - Zero forbidden Lua comments (`--`).

---

## 3. Test Verification Results

1. **Master QA Pipeline (`scripts/qa_audit_all.py`):**
   - Syntax & Braces: **[PASS] (0 issues)**
   - BOM Integrity: **[PASS] (0 issues)**
   - Defines Balance: **[PASS] (0 issues)**
   - Subunits & Equipment: **[PASS] (0 issues)**
   - Balkan Minors Viability: **[PASS] (0 issues)**
   - De-inflation & Guide: **[PASS] (0 issues)**
   - UK Semantic Oracle Integrity: **[PASS] (0 issues)**
   - German E2E Automated Suite (21/21): **[PASS]**
   - **Overall QA Audit Result: ALL QA AUDITS & UNIT TESTS PASSED SUCCESSFULLY! (Code 0)**

2. **British Complete Audit Suite (`tests/test_ww1_britain_complete_audit.py`):**
   - Ran 6 tests in 0.026s: **OK (6/6 PASS)**
