# Task 7 Brief: Full Bilingual Localization Engine (English & Brazilian Portuguese)

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Plan: `docs/superpowers/plans/2026-10-15-serbia-complete-rework-and-great-retreat.md`
Spec: `docs/superpowers/specs/2026-10-15-serbia-complete-rework-and-great-retreat-design.md`
Skill: `hoi4-localisation-bilingual`

## Objectives
1. **Localization Files:**
   - `localisation/english/ww1_serbia_l_english.yml`
   - `localisation/braz_por/ww1_serbia_l_braz_por.yml`

2. **Mandatory Encoding Standards:**
   - Single UTF-8 BOM (`\xef\xbb\xbf`) at byte 0 of both files.
   - Exact 0 double BOM (`\xef\xbb\xbf\xef\xbb\xbf`).
   - Line 1 headers: `l_english:` and `l_braz_por:` immediately following BOM.
   - 100% key parity (every key in English must exist in Brazilian Portuguese, and vice versa).

3. **Key Coverage across Tasks 2 through 6:**
   - **Balance of Power:** `bop_ser_civil_military`, `bop_ser_pasic_parliament`, `bop_ser_apis_black_hand`, all 5 ranges, tooltips.
   - **The Great Retreat & Salonika Sanctuary:**
     - Decision category `ww1_serbia_great_retreat`, `ww1_serbia_great_retreat_desc`.
     - 4 mobilization decisions: `SER_spawn_conscript_regiments_1896_1899`, `SER_spawn_yugoslav_volunteer_corps`, `SER_spawn_french_allied_brigades`, `SER_spawn_toplica_chetnik_uprising` and descs.
     - Ideas: `SER_otadzbina_u_pokretu`, `SER_otadzbina_u_pokretu_desc`, `SER_oath_of_corfu_martyrs`, `SER_oath_of_corfu_martyrs_desc`.
     - Events: `ww1_serbia_retreat.1.t`, `ww1_serbia_retreat.1.d`, `ww1_serbia_retreat.1.a`, `ww1_serbia_retreat.2.*`, `ww1_serbia_retreat.10.*`, `ww1_serbia_retreat.15.*`, `ww1_serbia_retreat.20.*`, `ww1_serbia_retreat.25.*`.
   - **Belgrade Defense & Typhus Crisis:**
     - `SER_dec_major_gavrilovic_last_stand`, `SER_dec_scottish_women_hospitals` and descs.
     - Ideas: `SER_major_gavrilovic_spirit`, `SER_typhus_epidemic_crisis`, `SER_foreign_medical_missions_aid` and descs.
     - Events: `ww1_serbia.7.*`, `ww1_serbia.8.*`, `ww1_serbia.20.*`, `ww1_serbia.21.*`, `ww1_serbia.22.*`.
   - **The 4 Destinies & Focuses:**
     - Focuses: `SER_proclamation_of_yugoslavia`, `SER_restored_sovereign_serbia`, `SER_balkan_socialist_soviet_republic`, `SER_apis_pretorian_military_junta`, `SER_salonika_trial_of_apis`, `SER_breakthrough_at_dobro_pole` and descs.
     - Ideas: `SER_yugoslav_kingdom_unification`, `SER_greater_serbian_hegemony`, `SER_balkan_soviet_federation`, `SER_black_hand_junta_rule` and descs.
   - **Characters & Industry:**
     - Traits: `vojvoda_wheelchair_strategist`, `vojvoda_kolubara_master`, `vojvoda_hero_of_cer`, `vojvoda_liberator_of_belgrade`, `chetnik_guerilla_leader`, `national_heroine`, `iron_regiment_veteran`.
     - Characters: `SER_milunka_savic`, `SER_dragutin_gavrilovic`, `SER_vojin_popovic_vuk`.
     - Decisions & Ideas: `SER_dec_kragujevac_arms_manufactory`, `SER_dec_bor_copper_mines_concession`, `SER_dec_gvozdeni_puk_iron_regiment`, `SER_kragujevac_arsenal`, `SER_bor_copper_concession`, `SER_gvozdeni_puk_spirit`.

4. **Validation:**
   - Run `python -m unittest tests.test_ww1_serbia_rework.TestSerbiaOverhaul.test_localisation_bom_and_parity -v`. MUST PASS!
   - 0 missing keys.

5. **Commit:**
   - `git add localisation/english/ww1_serbia_l_english.yml localisation/braz_por/ww1_serbia_l_braz_por.yml`
   - `git commit -m "feat(loc): implement complete bilingual localization with single UTF-8 BOM for Serbia rework"`
