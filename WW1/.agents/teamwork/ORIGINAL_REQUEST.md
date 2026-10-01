# Original User Request

## 2026-10-01T02:08:55Z

Implement the complete, immersive, and visually rich National Focus Tree for the German Empire (Deutsches Kaiserreich) in the WW1 Hearts of Iron IV mod *Baianagem-WW1*, exactly following the master plan in `PLANO_FOCUS_TREE_ALEMANHA_WW1.md`.

Working directory: `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1`  
Integrity mode: development  

## Context & Existing Systems
- Mod starts on **June 1, 1911**.
- Germany starts with 5 core national modifiers in `WW1/common/ideas/ww1_national_modifiers.txt`: `GER_grosser_generalstab`, `GER_krupp_chemical_conglomerates`, `GER_tirpitz_naval_ambition`, `GER_encirclement_paranoia`, and `GER_burgfrieden_social_peace`.
- Crisis modifiers already exist: `GER_turnip_winter_crisis_1/2/3`, `GER_hindenburg_program_victory`, `german_infiltration_assault_idea`, and `GER_kaiserschlacht_idea`.
- Focus icons repository: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3106240385\gfx\interface\goals` contains dedicated WW1 icons (`GFX_focus_OHL`, `GFX_focus_GER_krupp`, `GFX_focus_GER_navy`, `GFX_ww1_nationalfocus_ironcross`, `GFX_ww1_nationalfocus_gasmask`, `GFX_focus_ger_around_maginot`, etc.).
- Steam active copy: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.

---

## Requirements

### R1. German National Focus Tree (`WW1/common/national_focus/germany.txt`)
Implement a comprehensive, multi-branching tree with clean UI coordinates (`x`, `y` layout avoiding overlaps):
1. **Phase I (1911–1914) — Belle Époque Imperial & Arms Race**:
   - Agadir Crisis gambit (`GER_agadir_crisis_gambit`), Tirpitz 4th Naval Bill (`GER_tirpitz_fourth_naval_bill`), Berlin-Baghdad Railway (`GER_berlin_baghdad_railway`), Krupp 420mm Howitzers (`GER_expand_heavy_howitzers`), Army Bill of 1912 (`GER_army_bill_1912`), Leipzig Centenary (`GER_centenary_of_leipzig_1913`), and The Blank Cheque to Vienna (`GER_the_blank_cheque`).
2. **Phase II (1914–1917) — Operational Choice & Total War**:
   - **Branch A**: Modified Schlieffen Plan (`GER_execute_schlieffen_plan` -> Liège forts -> Race to the Sea -> Western Front stagnation).
   - **Branch B**: *Aufmarsch II Ost* (`GER_aufmarsch_ost_focus` -> respect Belgian neutrality keeping UK out in 1914 -> Eastern focus against Russia).
   - **Total War Reforms**: Haber-Bosch nitrogen fixation (`GER_haber_bosch_nitrogen_miracle`), Chemical warfare in Ypres (`GER_chemical_warfare_initiative`), Hindenburg Total War Program (`GER_hindenburg_program`), and Stosstruppen infiltration tactics (`GER_stosstruppen_tactics`).
3. **Phase III (1917–1920+) — Political Paths & Endgames**:
   - **Historical (OHL Military Dictatorship)**: Hindenburg & Ludendorff supremacy, Unrestricted Submarine Warfare, Sealed train for Lenin, Treaty of Brest-Litovsk (liberating Ober Ost, Regency Poland, Ukrainian Hetmanate, removing Turnip Winter), and 1918 Kaiserschlacht.
   - **Reformist (Volkskaiserreich)**: Bethmann-Hollweg civilian supremacy, abolition of Prussian 3-class franchise, Reichstag Peace Resolution (peace without annexations), and constitutional parliamentary monarchy.
   - **Radical Pan-Germanist**: Vaterlandspartei (Tirpitz/Kapp), total forced labor, permanent annexation of Belgium and Longwy-Briey, and iron-fisted Mitteleuropa.
   - **Easter Eggs & Alt-History**:
     - *Björkö 2.0*: Secret Willy-Nicky Russo-German alliance against Britain and France.
     - *Hajj Wilhelm*: Max von Oppenheim's global jihad initiative with Bedouin cavalry volunteers.
     - *Spartakusaufstand*: Proletarian socialist revolution in 1917 under Rosa Luxemburg.
     - *Großdeutschland 1915*: Emergency annexation of Austrian German lands if Austria-Hungary collapses.

### R2. Interface & Sprite Definitions (`WW1/interface/ww1_germany_goals.gfx`)
- Create sprite definitions mapping each focus `icon = GFX_...` to actual texture files copied or referenced from the TGWR/custom goal library into `WW1/gfx/interface/goals/`.
- Ensure no focus displays a missing texture or white box.

### R3. Immersion & Localisation (English & Brazilian Portuguese)
- Create `WW1/localisation/english/ww1_germany_focus_l_english.yml` and `ww1_germany_focus_l_braz_por.yml` with **UTF-8 BOM**.
- Provide atmospheric historical descriptions, quotes from Ernst Jünger and Bethmann-Hollweg, and clear gameplay tooltips explaining the strategic trade-offs of each choice.

### R4. Inter-Connectivity & Event Triggers
- Wire triggers and events so that:
  - If Germany does `GER_the_blank_cheque`, Austria-Hungary and Serbia receive their escalation events.
  - If Germany does `GER_execute_schlieffen_plan`, Belgium and the UK receive their declaration events.
  - If Germany does `GER_treaty_of_brest_litovsk`, Russia gets the capitulation/peace event, and the map releases `GER_ober_ost`, `POL`, and `UKR`.
  - Focuses update and interact with the existing national spirits (`GER_turnip_winter_crisis`, `GER_hindenburg_program_victory`, etc.).

### R5. Verification and Synchronization
- Validate 100% of braces `{}` and syntax via automated script.
- Mirror the working mod repository to the Steam Workshop target folder `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491` using Robocopy.

---

## Acceptance Criteria

### Syntax & Game Stability
- [ ] `WW1/common/national_focus/germany.txt` passes automated parser with zero unmatched braces.
- [ ] Every prerequisite and mutually_exclusive reference points to a valid existing focus ID.
- [ ] No focus coordinates overlap (`x`, `y` ranges are clean and readable).
- [ ] No game crash on loading or selecting Germany in the 1911 bookmark.

### Visual & Audio Quality
- [ ] Every focus icon has a valid `spriteType` registered in `ww1_germany_goals.gfx`.
- [ ] Zero missing textures (`placeholder` or question mark boxes).
- [ ] Cosmetic tags (`GER_ober_ost`, `GER_socialist`, etc.) and map puppets fire correctly upon focus completion.

### Integration
- [ ] National modifiers (`GER_turnip_winter_crisis`, `GER_grosser_generalstab`, `GER_burgfrieden_social_peace`) are properly modified/removed as specified in the tree.
- [ ] Both English and Brazilian Portuguese localization files have valid YAML syntax and UTF-8 BOM encoding.
- [ ] All files are mirrored to `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491`.
