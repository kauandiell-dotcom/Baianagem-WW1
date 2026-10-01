---
name: hoi4-gfx-asset-pipeline
description: >-
  Specialized asset pipeline for Hearts of Iron IV graphics, focus goal icons, national
  idea icons, .gfx sprite definitions with scrolling shine overlays, DDS/PNG texture
  validation, and automated icon harvesting from mods (Europe In Flames, TGWR).
---

# HOI4 GFX & Asset Pipeline

This skill provides the end-to-end graphical asset workflow for Hearts of Iron IV modding. It covers icon discovery, conversion, registration in `.gfx` interface files, shine animations, and preventing in-game missing textures (white boxes, pink squares, or black silhouettes).

Use this skill whenever adding or updating focus tree icons, national spirits, event pictures, or character portraits.

---

## 1. Texture Specifications & Dimensions

The Clausewitz engine requires specific image formats and dimensions depending on the asset category:

| Asset Type | Standard Dimensions | Preferred Format | Transparency | Storage Folder |
| :--- | :--- | :--- | :--- | :--- |
| **Focus Goal Icons** | `82 x 82` or `128 x 128` | DDS (DXT5/BC3) or PNG | 32-bit RGBA (Alpha channel required) | `gfx/interface/goals/` |
| **Idea / Spirit Icons**| `64 x 64` | DDS (DXT5) or PNG | 32-bit RGBA | `gfx/interface/ideas/` |
| **Event Pictures (Country)** | `450 x 250` | DDS (DXT1/BC1 or DXT5) | RGB / No alpha needed | `gfx/event_pictures/` |
| **Event Pictures (News)** | `400 x 140` | DDS (DXT1/BC1 or DXT5) | RGB / No alpha needed | `gfx/event_pictures/` |
| **Leader Portraits** | `156 x 210` | DDS (DXT5) | RGB | `gfx/leaders/<TAG>/` |

---

## 2. Icon Harvesting Sources

When looking for authentic period-accurate artwork, search these local repositories:
1. **Europe In Flames (EIF)**:
   - Path: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\2716194283\gfx\interface\goals\`
   - Rich collection of WW1 battle scenes, imperial emblems, trench warfare, and period uniforms.
2. **The Great War Redux (TGWR)**:
   - Path: `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3365515312\gfx\interface\goals\`
   - Thousands of authentic WW1 focus icons for all major and minor nations.
3. **Mod Active Repository**:
   - Path: `WW1/gfx/interface/goals/`

### Historical Theme & Anachronism Filter
> [!CAUTION]
> **Strict WW1 Authenticity**:
> - Never use WW2 iconography (swastikas, SS runes, Cold War jets, modern MBTs, AK-47s).
> - Use authentic WW1 symbols: Pickelhauben, Adrian helmets, Stahlhelm M1916, Maxim MG08, Vickers guns, Zeppelins, biplanes, Dreadnoughts, Paris Gun / Big Bertha.

---

## 3. The Sprite Registration Protocol (`.gfx`)

Every focus icon used in `common/national_focus/<country>.txt` (`icon = GFX_XYZ`) requires **TWO** entries in `interface/<country>_goals.gfx`:
1. The **Base Sprite**: Displays the static icon in the tree.
2. The **Shine Sprite** (`GFX_XYZ_shine`): Displays the luminous scrolling glow when hovered or selected.

### Complete `.gfx` Template:
```pdx
spriteTypes = {
    # 1. Base Sprite
    SpriteType = {
        name = "GFX_TAG_stormtrooper_offensive"
        texturefile = "gfx/interface/goals/TAG_stormtrooper_offensive.png"
    }

    # 2. Luminous Scrolling Shine Sprite
    SpriteType = {
        name = "GFX_TAG_stormtrooper_offensive_shine"
        texturefile = "gfx/interface/goals/TAG_stormtrooper_offensive.png"
        effectFile = "gfx/FX/buttonstate.lua"
        animation = {
            animationmaskfile = "gfx/interface/goals/TAG_stormtrooper_offensive.png"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = -90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = { x = 0.0 y = 0.0 }
            animationtexturescale = { x = 1.0 y = 1.0 }
        }
        legacy_lazy_load = no
    }
}
```

> [!IMPORTANT]
> If `_shine` is omitted, the Clausewitz engine will write error log entries to `error.log` every time the player mouses over the focus box in-game!

---

## 4. National Idea Sprite Registration (`interface/ideas.gfx`)

Unlike focus icons, ideas do not require a `_shine` animation:

```pdx
spriteTypes = {
    SpriteType = {
        name = "GFX_idea_TAG_krupp_industrial_complex"
        texturefile = "gfx/interface/ideas/TAG_krupp_industrial_complex.png"
    }
}
```

---

## 5. Automated GFX Pipeline Tooling

### A. Harvesting & Registering Icons
Run the automated harvester to search donor mod folders, copy assets, and register both base and shine sprites:
```powershell
python scripts/harvest_mod_icons.py --search "artillery" --tag "FRA" --output "WW1/gfx/interface/goals/" --gfx "WW1/interface/fra_goals.gfx"
```

### B. Checking for Missing Sprites
Run the texture checker to ensure 0 missing sprites and 0 unlinked physical files:
```powershell
python scripts/check_missing_gfx.py --tree "WW1/common/national_focus/germany.txt" --gfx "WW1/interface/ww1_germany_goals.gfx" --dir "WW1/gfx/interface/goals"
```
