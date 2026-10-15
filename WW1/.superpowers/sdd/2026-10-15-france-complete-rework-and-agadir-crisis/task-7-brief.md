# Task 7 Brief: Full Bilingual Localization Engine (English & Brazilian Portuguese)

## Context
Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
Spec: `docs/superpowers/specs/2026-10-15-france-complete-rework-and-agadir-crisis-design.md`
Plan: `docs/superpowers/plans/2026-10-15-france-complete-rework-and-agadir-crisis.md`

## Deliverables
1. Create `localisation/english/ww1_france_rework_l_english.yml` with single UTF-8 BOM (`\xef\xbb\xbf`).
   Must begin with `l_english:` on line 1 after BOM.
2. Create `localisation/braz_por/ww1_france_rework_l_braz_por.yml` with single UTF-8 BOM (`\xef\xbb\xbf`).
   Must begin with `l_braz_por:` on line 1 after BOM.
3. Zero double BOM (`\xef\xbb\xbf\xef\xbb\xbf`).
4. 100% key parity between English and Brazilian Portuguese. Every single key in English must exist in Brazilian Portuguese.
5. Keys to include and translate with deep historical immersion:
   - **Agadir Crisis:**
     - Categories: `ww1_agadir_crisis`, `ww1_agadir_crisis_desc`
     - Decisions:
       - `GER_agadir_demand_naval_base`, `GER_agadir_demand_naval_base_desc`
       - `GER_agadir_demand_congo_compensation`, `GER_agadir_demand_congo_compensation_desc`
       - `GER_agadir_send_sms_berlin`, `GER_agadir_send_sms_berlin_desc`
       - `GER_agadir_back_down_gracefully`, `GER_agadir_back_down_gracefully_desc`
       - `FRA_agadir_caillaux_secret_channel`, `FRA_agadir_caillaux_secret_channel_desc`
       - `FRA_agadir_delcasse_firm_resolve`, `FRA_agadir_delcasse_firm_resolve_desc`
       - `FRA_agadir_financial_sanctions`, `FRA_agadir_financial_sanctions_desc`
       - `FRA_agadir_concede_congo_accord`, `FRA_agadir_concede_congo_accord_desc`
       - `FRA_agadir_concede_naval_station`, `FRA_agadir_concede_naval_station_desc`
       - `ENG_agadir_mansion_house_speech`, `ENG_agadir_mansion_house_speech_desc`
       - `ENG_agadir_home_fleet_alert`, `ENG_agadir_home_fleet_alert_desc`
       - `ENG_agadir_urge_moderation`, `ENG_agadir_urge_moderation_desc`
     - Events:
       - `ww1_agadir.1.t`, `ww1_agadir.1.d`, `ww1_agadir.1.a`, `ww1_agadir.1.b`
       - `ww1_agadir.10.t`, `ww1_agadir.10.d`, `ww1_agadir.10.a`
       - `ww1_agadir.20.t`, `ww1_agadir.20.d`, `ww1_agadir.20.a`
       - `ww1_agadir.30.t`, `ww1_agadir.30.d`, `ww1_agadir.30.a`
       - `ww1_agadir.40.t`, `ww1_agadir.40.d`, `ww1_agadir.40.a`
     - Variables / Tooltips:
       - `ww1_agadir_crisis_tension`, `ww1_agadir_tension_increase_tt`, `ww1_agadir_tension_decrease_tt`
   - **Republic Dashboard & Survival Vectors:**
     - Variables: `FRA_union_sacree_cohesion`, `FRA_poilu_morale`, `FRA_charbon_et_acier`, `FRA_reserves_humaines`
     - Ideas:
       - `FRA_union_sacree_strong`, `FRA_union_sacree_strong_desc`
       - `FRA_union_sacree_fractured`, `FRA_union_sacree_fractured_desc`
       - `FRA_poilu_morale_high`, `FRA_poilu_morale_high_desc`
       - `FRA_poilu_morale_demoralized`, `FRA_poilu_morale_demoralized_desc`
       - `FRA_charbon_et_acier_surplus`, `FRA_charbon_et_acier_surplus_desc`
       - `FRA_charbon_et_acier_famine`, `FRA_charbon_et_acier_famine_desc`
     - Decisions:
       - `FRA_dec_british_channel_coal`, `FRA_dec_british_channel_coal_desc`
       - `FRA_dec_call_up_class_1917`, `FRA_dec_call_up_class_1917_desc`
       - `FRA_dec_colonial_recruitment_tirailleurs`, `FRA_dec_colonial_recruitment_tirailleurs_desc`
       - `FRA_dec_union_sacree_cross_party_pact`, `FRA_dec_union_sacree_cross_party_pact_desc`
   - **Crises & Endsieg:**
     - Ideas:
       - `FRA_trench_mutiny_crisis_2`, `FRA_trench_mutiny_crisis_2_desc`
       - `FRA_poilus_reconcilies`, `FRA_poilus_reconcilies_desc`
       - `FRA_munitionnettes_strike`, `FRA_munitionnettes_strike_desc`
       - `FRA_jusqu_au_bout_endsieg`, `FRA_jusqu_au_bout_endsieg_desc`
     - Events:
       - `ww1_france.210.t`, `ww1_france.210.d`, `ww1_france.210.a`
       - `ww1_france.211.t`, `ww1_france.211.d`, `ww1_france.211.a`, `ww1_france.211.b`
       - `ww1_france.215.t`, `ww1_france.215.d`, `ww1_france.215.a`, `ww1_france.215.b`
       - `ww1_france.220.t`, `ww1_france.220.d`, `ww1_france.220.a`
       - `FRA_petain_welfare_reforms_unlocked_tt`
   - **Political Branches & Characters:**
     - Focuses:
       - `FRA_republique_union_sacree`, `FRA_republique_union_sacree_desc`
       - `FRA_clemenceau_je_fais_la_guerre`, `FRA_clemenceau_je_fais_la_guerre_desc`
       - `FRA_republique_des_soviets_de_paris`, `FRA_republique_des_soviets_de_paris_desc`
       - `FRA_comite_de_salut_public_1917`, `FRA_comite_de_salut_public_1917_desc`
       - `FRA_abattre_la_gueuse`, `FRA_abattre_la_gueuse_desc`
       - `FRA_restauration_orleaniste_jean_iii`, `FRA_restauration_orleaniste_jean_iii_desc`
       - `FRA_directoire_militaire_gqg`, `FRA_directoire_militaire_gqg_desc`
       - `FRA_etat_de_siege_permanent`, `FRA_etat_de_siege_permanent_desc`
     - Ideas:
       - `FRA_union_sacree_spirit`, `FRA_union_sacree_spirit_desc`
       - `FRA_commune_de_paris_spirit`, `FRA_commune_de_paris_spirit_desc`
       - `FRA_action_francaise_monarchy`, `FRA_action_francaise_monarchy_desc`
       - `FRA_gqg_military_directory`, `FRA_gqg_military_directory_desc`
     - Characters:
       - `FRA_charles_maurras`, `FRA_king_jean_iii`, `FRA_jean_longuet`, `FRA_fernand_loriot`, `FRA_georges_clemenceau`
   - **Industrial & Allied Decisions:**
     - `FRA_dec_evacuate_briey_machinery`, `FRA_dec_evacuate_briey_machinery_desc`
     - `FRA_dec_lyon_chemical_complex`, `FRA_dec_lyon_chemical_complex_desc`
     - `FRA_dec_schneider_creusot_heavy_guns`, `FRA_dec_schneider_creusot_heavy_guns_desc`
     - `FRA_dec_fort_douaumont_reinforcement`, `FRA_dec_fort_douaumont_reinforcement_desc`
     - `FRA_dec_voix_sacree_truck_convoys`, `FRA_dec_voix_sacree_truck_convoys_desc`
     - `FRA_dec_inter_allied_supreme_war_council`, `FRA_dec_inter_allied_supreme_war_council_desc`
     - `FRA_dec_us_morgan_bank_credit_line`, `FRA_dec_us_morgan_bank_credit_line_desc`
     - Categories:
       - `FRA_war_economy_and_munitions`, `FRA_war_economy_and_munitions_desc`
       - `FRA_defence_of_verdun`, `FRA_defence_of_verdun_desc`
       - `FRA_entente_diplomacy`, `FRA_entente_diplomacy_desc`
       - `FRA_mutinies_crisis_management`, `FRA_mutinies_crisis_management_desc`
       - `FRA_third_republic_politics`, `FRA_third_republic_politics_desc`

6. **Validation:**
   - Run `python -m unittest tests.test_ww1_france_rework.TestFranceOverhaul.test_localisation_bom_and_parity -v`. Must PASS!
   - Run `python -m unittest tests.test_ww1_france_rework -v`. All 7/7 tests must PASS!
   - Run `scripts/qa_audit_all.py`. Check BOM audit passes cleanly!

7. **Commit:**
   `git add localisation/english/ww1_france_rework_l_english.yml localisation/braz_por/ww1_france_rework_l_braz_por.yml`
   `git commit -m "feat(loc): implement complete bilingual localization with single UTF-8 BOM for France rework"`

8. **Report:**
   Write full report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\2026-10-15-france-complete-rework-and-agadir-crisis\task-7-report.md`.
9. Contract: NEVER dispatch any subagents. Report status, commit hash, and summary when done.
