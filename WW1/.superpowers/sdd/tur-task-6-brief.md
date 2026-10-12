# Task 6: Complete Bilingual Localization & Single UTF-8 BOM (`localisation/`)

**Files:**
- Modify: `localisation/english/ww1_ottoman_l_english.yml`
- Modify: `localisation/braz_por/ww1_ottoman_l_braz_por.yml`

**Interfaces:**
- Consumes: All 256 focus IDs, all ideas in `ww1_ottoman_ideas.txt`, all decisions in `ww1_ottoman_decisions.txt`, and all 32 events in `ww1_ottoman_events.txt`.
- Produces: 100% synchronized, single-BOM (`\xef\xbb\xbf`) English and Brazilian Portuguese localization files with 0 untranslated strings and 0 generic copy-paste descriptions.

## Step 1: Fix Double UTF-8 BOM and Synchronize Event Keys (`ww1_ottoman.1`–`ww1_ottoman.32`)
- **CRITICAL UTF-8 BOM RULE:** Both files currently have a double UTF-8 BOM (`\xef\xbb\xbf\xef\xbb\xbf`). When writing the files in Python:
  - Strip all leading `\ufeff` characters from the text string (`content = content.lstrip("\ufeff")`), and write using `encoding="utf-8-sig"` (or write raw bytes `b"\xef\xbb\xbf" + content.encode("utf-8")`).
  - Verify afterwards that `raw[:3] == b"\xef\xbb\xbf"` and `raw[3:6] != b"\xef\xbb\xbf"`!
- Synchronize event keys (`ww1_ottoman.1.t`, `.d`, `.a`, `.b` through `ww1_ottoman.32.t`, `.d`, `.a`, `.b`) so every event title, description, and option key referenced in `events/ww1_ottoman_events.txt` is present in both `ww1_ottoman_l_english.yml` and `ww1_ottoman_l_braz_por.yml` with accurate historical text matching each event!

## Step 2: Translate All 36 English Titles in `ww1_ottoman_l_braz_por.yml` and Replace All 58 Generic Copy-Paste Descriptions
- In `localisation/braz_por/ww1_ottoman_l_braz_por.yml`:
  - Translate all 36 untranslated English decision and idea titles (e.g. `"Subsidize Anatolian Grain"` -> `"Subsidiar Grãos da Anatólia"`, `"Second Constitutional Era"` -> `"Segunda Era Constitucional"`, `"Enver Pasha's Reform"` -> `"Reforma Militar de Enver Pasha"`, etc.) into authentic Brazilian Portuguese.
  - Replace all occurrences of the generic copy-paste descriptions in `ww1_ottoman_l_braz_por.yml` (`"Reflete as realidades estruturais e esforços administrativos do Estado Otomano."`, `"Aplica medidas operacionais especializadas para a defesa e prosperidade do império."`, `"Iniciativa estratégica entra em vigor nos territórios imperiais pertinentes."`) and their English equivalents in `ww1_ottoman_l_english.yml` (`"Reflects the structural realities and administrative efforts of the Ottoman state."`, `"Applies specialized operational measures for the defense and prosperity of the empire."`, `"Strategic initiative enacted across the relevant imperial territories."`) with unique, historically rich descriptions tailored to each specific idea, decision, or focus!
- Add complete bilingual localization keys (`KEY`, `KEY_desc` for focuses/ideas/decisions/categories) for:
  - New ideas: `TUR_sick_man_debt`, `TUR_mehmetcik_tenacity`, `TUR_straits_fortress_cannons`, `TUR_caliphate_global_banner`, `TUR_arab_revolt_insurgency`, `TUR_imperial_vilayets_pacified`, `TUR_senussi_desert_brotherhood`
  - New decisions: `TUR_deploy_hejaz_armored_garrison`, `TUR_teskilat_counter_insurgency_sweep`, `TUR_subsidize_bedouin_sheikhs`, `TUR_pacify_arab_insurgency_campaign`, `TUR_liquidate_opda_debt_tranche`, `TUR_curb_foreign_consular_courts`, `TUR_dispatch_officers_to_tripolitania`
  - New events: `ww1_ottoman.31.t`, `ww1_ottoman.31.d`, `ww1_ottoman.31.a`, `ww1_ottoman.31.b`, `ww1_ottoman.32.t`, `ww1_ottoman.32.d`, `ww1_ottoman.32.a`, `ww1_ottoman.32.b`
- Ensure 100% key parity between `ww1_ottoman_l_english.yml` and `ww1_ottoman_l_braz_por.yml`, and ensure every single focus (`f_id` and `f_id_desc`), idea, decision, and event key is present in both files.

## Step 3: Verification & Commit
Run:
```bash
python -c "for p in ['localisation/english/ww1_ottoman_l_english.yml', 'localisation/braz_por/ww1_ottoman_l_braz_por.yml']: b = open(p, 'rb').read(6); assert b[:3] == b'\xef\xbb\xbf' and b[3:6] != b'\xef\xbb\xbf', f'Bad BOM in {p}: {b}'"
python -m unittest tests/test_ww1_ottoman.py -v
```
Commit:
```bash
git add localisation/english/ww1_ottoman_l_english.yml localisation/braz_por/ww1_ottoman_l_braz_por.yml
git commit -m "feat(tur): fix double UTF-8 BOM bug and provide 100% bespoke bilingual Ottoman localization"
```
