### Task 10: Complete Bilingual Localization & Single UTF-8 BOM

**Files:**
- Create: `localisation/english/ww1_soviet_l_english.yml`
- Create: `localisation/braz_por/ww1_soviet_l_braz_por.yml`
- Create: `localisation/english/ww1_white_l_english.yml`
- Create: `localisation/braz_por/ww1_white_l_braz_por.yml`
- Modify: `localisation/english/ww1_russia_focus_l_english.yml`
- Modify: `localisation/braz_por/ww1_russia_focus_l_braz_por.yml`
- Modify: `localisation/english/ww1_russia_events_l_english.yml`
- Modify: `localisation/braz_por/ww1_russia_events_l_braz_por.yml`

**Interfaces:**
- Consumes: All new focus IDs, idea IDs, decision IDs, and event IDs.
- Produces: 100% bilingual localization key parity with single UTF-8 BOM.

- [ ] **Step 1: Create Soviet and White localization files in English and Portuguese**
  Write keys for all 80 Soviet focuses, 60 White focuses, all decisions, ideas, and events.
  Enforce strictly single UTF-8 BOM (`\xef\xbb\xbf` at start).

- [ ] **Step 2: Update Tsarist Russia localization files**
  Add keys for all new decisions, ideas, and capstones.

- [ ] **Step 3: Verify UTF-8 BOM & Localization Parity**
  Run: `python -c "import glob; [assert open(f, 'rb').read(3) == b'\xef\xbb\xbf' and open(f, 'rb').read(6)[3:] != b'\xef\xbb\xbf' for f in glob.glob('localisation/**/*.yml', recursive=True) if 'sov' in f.lower() or 'russia' in f.lower() or 'white' in f.lower()]"`
  Expected: PASS.

- [ ] **Step 4: Commit**
  ```bash
  git add localisation/english/ localisation/braz_por/
  git commit -m "feat(loc): provide complete bilingual localization with single UTF-8 BOM for Russia overhaul"
  ```

---

