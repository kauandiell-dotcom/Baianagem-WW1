# Task 8 Brief: Full Bilingual Localization Engine (English & Brazilian Portuguese)

## Objective
Provide 100% complete bilingual localization in both English (`l_english`) and Brazilian Portuguese (`l_braz_por`) for all focuses, ideas, decisions, events, cosmetic tags, and tooltips introduced in the Austria-Hungary rework.
Strictly enforce single UTF-8 BOM encoding (`\xef\xbb\xbf`), zero double BOM, and 100% key parity.

## Context
- Working Directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`
- Spec: `docs/superpowers/specs/2026-10-14-austria-hungary-complete-rework-and-collapse-design.md`
- Plan: `docs/superpowers/plans/2026-10-14-austria-hungary-complete-rework.md`
- Skill: `hoi4-localisation-bilingual`

## Deliverables
1. `localisation/english/ww1_austria_rework_l_english.yml`
2. `localisation/braz_por/ww1_austria_rework_l_braz_por.yml`
3. Both files must begin with single UTF-8 BOM byte sequence: `\xef\xbb\xbf`.
4. 100% key parity between English and Portuguese files.
5. All keys from Tasks 2 through 7 localized:
   - Focuses (Constitutional, military, industrial, diplomatic)
   - Ideas (Constitutional spirits, Škoda, Steyr, Ganz, Conrad, Boroević, Federal member)
   - Decisions (Dashboard, grain rationing, Škoda artillery, oil, alpine redoubts, diplomacy)
   - Events (Collapse crises 1-3, reunification 10, Redl affair 1, Sixtus affair 10, Poland 20, Brotfrieden 30)
   - Cosmetic tags (Danubian member states)
6. Verification:
   - `python -m unittest tests.test_ww1_austria_hungary.TestAustriaHungaryOverhaul.test_localisation_bom_and_parity -v` -> MUST PASS!
7. Commit:
   - `git add localisation/english/ww1_austria_rework_l_english.yml localisation/braz_por/ww1_austria_rework_l_braz_por.yml`
   - `git commit -m "feat(loc): provide complete bilingual localization with single UTF-8 BOM for Austria-Hungary rework"`
