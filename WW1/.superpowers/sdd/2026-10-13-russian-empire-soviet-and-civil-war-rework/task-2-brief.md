### Task 2: Country Tag `WHT`, Historical Characters, Cosmetic Tags & GFX Sprites

**Files:**
- Create: `common/country_tags/01_ww1_tags.txt`
- Create: `common/countries/White Russia.txt`
- Create: `history/countries/WHT - White Russia.txt`
- Modify: `common/countries/colors.txt`
- Modify: `common/countries/cosmetic.txt`
- Modify: `common/characters/SOV.txt`
- Create: `common/characters/WHT.txt`
- Create: `interface/ww1_soviet_goals.gfx`
- Create: `interface/ww1_white_goals.gfx`

**Interfaces:**
- Consumes: Existing leader/idea texture assets in `gfx/leaders/SOV/` and `gfx/interface/goals/`.
- Produces: Valid tag `WHT`, 15+ recruited characters with traits, and animated `.gfx` goal sprites.

- [ ] **Step 1: Define `WHT` tag, history file, colors and cosmetic tags**
  Set `WHT = "countries/White Russia.txt"` in `common/country_tags/01_ww1_tags.txt`.
  Set color `rgb { 240 240 245 }` in `common/countries/colors.txt`.
  Create `history/countries/WHT - White Russia.txt` with Omsk capital (state 594), neutrality ideology, and character recruitment.

- [ ] **Step 2: Recruit Bolshevik and White historical characters**
  Add Trotsky, Stalin, Frunze, Dzerzhinsky, Budyonny, Tukhachevsky, Chicherin, Bukharin to `common/characters/SOV.txt`.
  Add Kolchak, Denikin, Wrangel, Yudenich, Kornilov, Kaledin, Savinkov to `common/characters/WHT.txt`.

- [ ] **Step 3: Create GFX sprite definitions for Soviet and White goals**
  Create `interface/ww1_soviet_goals.gfx` and `interface/ww1_white_goals.gfx` with `spriteType` and `_shine` definitions pointing to valid `.dds` textures.

- [ ] **Step 4: Verify with Semantic Oracle & Character Assertions**
  Run: `python -m unittest tests.test_ww1_russia_rework.TestRussiaOverhaul.test_characters_and_tags -v`
  Expected: PASS.

- [ ] **Step 5: Commit**
  ```bash
  git add common/country_tags/ common/countries/ history/countries/ common/characters/ interface/
  git commit -m "feat(sov): establish WHT country tag, historical character cast, and focus GFX sprites"
  ```

---

