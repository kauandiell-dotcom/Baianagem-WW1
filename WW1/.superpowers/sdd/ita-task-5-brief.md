# Italy Rework Task 5: Complete Bilingual Localization (`localisation/`)

**Files:**
- Modify: `localisation/english/ww1_italy_l_english.yml`
- Modify: `localisation/braz_por/ww1_italy_l_braz_por.yml`

## Step 1: Add Bilingual Keys (`:0` and `_desc:0`) for All 9 Restored Ideas & 9 New Decisions
Ensure both `localisation/english/ww1_italy_l_english.yml` and `localisation/braz_por/ww1_italy_l_braz_por.yml` contain ` {id}:0 "..."` and ` {id}_desc:0 "..."` (with a leading single space and `:0` format matching the rest of the file!) for:
1. **9 Restored Ideas:**
   - `ITA_terre_irredente_dream` / `ITA_terre_irredente_dream_desc`
   - `ITA_alpini_tradition` / `ITA_alpini_tradition_desc`
   - `ITA_coal_iron_scarcity` / `ITA_coal_iron_scarcity_desc`
   - `ITA_southern_question_gap` / `ITA_southern_question_gap_desc`
   - `ITA_sacro_egoismo_policy` / `ITA_sacro_egoismo_policy_desc`
   - `ITA_isonzo_attrition_crisis_1` / `ITA_isonzo_attrition_crisis_1_desc`
   - `ITA_isonzo_attrition_crisis_2` / `ITA_isonzo_attrition_crisis_2_desc`
   - `ITA_isonzo_attrition_crisis_3` / `ITA_isonzo_attrition_crisis_3_desc`
   - `ITA_vittorio_veneto_triumph` / `ITA_vittorio_veneto_triumph_desc`
2. **9 New Map & Strategic Decisions:**
   - `ITA_ww1_mezzogiorno_aqueduct_and_roads` / `ITA_ww1_mezzogiorno_aqueduct_and_roads_desc`
   - `ITA_ww1_carabinieri_anti_brigandage_sweep` / `ITA_ww1_carabinieri_anti_brigandage_sweep_desc`
   - `ITA_ww1_southern_agrarian_credit_consortium` / `ITA_ww1_southern_agrarian_credit_consortium_desc`
   - `ITA_ww1_alpine_mine_warfare_tunnel` / `ITA_ww1_alpine_mine_warfare_tunnel_desc`
   - `ITA_ww1_launch_isonzo_general_offensive` / `ITA_ww1_launch_isonzo_general_offensive_desc`
   - `ITA_ww1_fortify_piave_and_monte_grappa` / `ITA_ww1_fortify_piave_and_monte_grappa_desc`
   - `ITA_ww1_fortify_libyan_coastal_oases` / `ITA_ww1_fortify_libyan_coastal_oases_desc`
   - `ITA_ww1_integrate_irredenta_province` / `ITA_ww1_integrate_irredenta_province_desc`
   - `ITA_ww1_impresa_di_pola_raid` / `ITA_ww1_impresa_di_pola_raid_desc`
3. Check every idea in `common/ideas/ww1_italy_ideas.txt` and every decision in `common/decisions/ww1_italy_decisions.txt` and ensure 100% of them have `:0` and `_desc:0` keys in both files, and that `en_keys == pt_keys` (100% key parity).

## Step 2: Translate Identical EN/PT Titles in `ww1_italy_l_braz_por.yml` & Enforce Single UTF-8 BOM
- In `localisation/braz_por/ww1_italy_l_braz_por.yml`, translate the 6 keys that had identical EN/PT strings:
  - `ITA_ww1_battaglione_aviatori:0 "Batalhão de Aviadores"`
  - `ITA_ww1_caporetto:0 "A Retirada de Caporetto"`
  - `ITA_ww1_corpo_aeronautico_militare:0 "Corpo Aeronáutico Militar"`
  - `ITA_ww1_opera_nazionale_combattenti:0 "Obra Nacional dos Combatentes"`
  - `ITA_ww1_saint_jean_de_maurienne:0 "Acordo de Saint-Jean-de-Maurienne"`
  - `ITA_ww1_vittorio_veneto:0 "A Ofensiva de Vittorio Veneto"`
- **CRITICAL UTF-8 BOM RULE:** Strip any leading `\ufeff` before writing with `encoding="utf-8-sig"`, and verify that `raw[:3] == b"\xef\xbb\xbf"` and `raw[3:6] != b"\xef\xbb\xbf"`.

## Verification & Commit
Run:
```bash
python -m unittest tests/test_ww1_italy.py -v
```
All tests in `tests/test_ww1_italy.py` MUST PASS!
Commit:
```bash
git add localisation/english/ww1_italy_l_english.yml localisation/braz_por/ww1_italy_l_braz_por.yml
git commit -m "feat(ita): add complete bilingual localization for restored ideas and map decisions"
```
Write your report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\ita-task-5-report.md`.
