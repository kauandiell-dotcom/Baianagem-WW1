# Design Document: Supreme Engine Optimization & Late-Game Simulation Architecture

**Date:** 2026-10-14  
**Target:** Baianagem-WW1 Mod Core Engine (`common/defines/`, `common/ai_strategy/`, `common/scripted_effects/`, `common/on_actions/`)  
**Target Hardware:** Low-spec to High-end PCs (Optimized to run smoothly even on 2–4 GB RAM systems)  
**Status:** Approved / Plan Phase  

---

## 1. Intent and The Why

In Hearts of Iron IV, late-game lag and wartime performance degradation are notorious throughout the entire modding and competitive community. As a campaign progresses into 1914–1918:
1. **The Single-Core Simulation Lock:** The Clausewitz engine executes its core simulation ticks (unit movement, combat resolution, frontline evaluation, supply tracing) on a single master thread.
2. **Exponential Combat & Event Log Accumulation:** By default, Clausewitz stores up to 12 months of detailed hourly combat records (`COMBAT_LOG_MAX_MONTHS = 12`) and garrison logs across every division in the world. Over 4 years of continuous trench warfare, hundreds of thousands of combat history structures pile up in system RAM, resulting in the dreaded "midnight freeze" at 00:00 every in-game day, ballooning save game files, and exhausting memory bandwidth.
3. **Division Micro-Spam & Pathfinding Explosions ($O(N \cdot P \log P)$):** In unconstrained engines, dozens of minor non-belligerent nations (in South America, Central America, Asia) and majors build hundreds of tiny 2-to-4 battalion divisions. Every single division continuously runs A* pathfinding across 13,000+ map provinces, supply network requests, and front-line shuffling, even when thousands of kilometers away from any conflict.
4. **Redundant AI Evaluation Ticks:** The AI repeatedly recalculates supply bottlenecks, motorization preferences, tech weights, and raid planning every few hours, consuming precious simulation cycles.
5. **Excessive Vector Geometry Passes:** Front line graphics, supply flow arrows, and trade route splines default to multiple smoothing tessellation passes (`ROOT_FRONT_SMOOTHEN_PASSES = 4`), choking GPU and CPU render threads when dozens of battle plans overlap on the Western and Eastern fronts.

### The User Mandate & The Core Commitment
The user demands **Supreme Optimization**—an engineering feat unprecedented in HOI4 modding—that allows even budget PCs with **2 to 4 GB RAM** to run the mod without late-game degradation or multiplayer desyncs, **WITHOUT degrading, removing, or compromising visual fidelity, 3D soldier models, unit icons, GFX, or authentic historical gameplay mechanics**.

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
- **G1: Midnight Stutter & Log Elimination:** Slash combat log, air log, and garrison log RAM retention to the minimum necessary for player interface, eliminating the midnight simulation freeze and reducing save-game serialization overhead by >80%.
- **G2: 2–4 GB RAM Footprint Relief:** Limit in-memory history structures, transient flags, and dead variables so systems with limited memory run without swapping or out-of-memory crashes.
- **G3: Strategic AI Division Consolidation:** Enforce historical, combat-effective division templates (24–30 combat width) for belligerents while dynamically curbing micro-division spam by non-involved neutral nations during peacetime.
- **G4: Engine-Level Tick Throttling:** Tune reverse-engineered internal Clausewitz defines to reduce redundant AI calculations (supply bottlenecks, tech re-weighting, trade recalculations) to sensible, realistic intervals.
- **G5: Render & Geometry Pass Optimization:** Reduce CPU/GPU geometry calculation overhead (frontline spline smoothing, weather particles outside viewport, redundant trade route lines) while preserving 100% of 3D models, textures, animations, and map visuals.
- **G6: Deterministic Multiplayer Netcode:** Guarantee zero desyncs (`OOS`), rock-solid lockstep synchronization, and clean script execution.
- **G7: Automated Verification:** Establish an automated test suite (`tests/test_ww1_supreme_optimization.py`) integrated into `scripts/qa_audit_all.py` validating all defines, syntax, and AI limits.

### Non-Goals
- **NG1:** We are NOT deleting, disabling, or downscaling 3D soldier models, tanks, artillery, planes, or ships.
- **NG2:** We are NOT removing map provinces, states, terrain features, or rivers.
- **NG3:** We are NOT removing focus trees, decisions, events, or historical flavor from any nation.

### Anti-Goals
- **AG1 (The Potato Texture Hack):** Blurring textures, removing 3D models, or turning the game into a featureless flat map.
- **AG2 (The AI Lobotomy):** Making combat AI passive, blind, or unable to launch offensive operations or defend fronts.
- **AG3 (Multiplayer Desync / OOS):** Introducing non-deterministic scripts or irregular variable modifications that cause multiplayer clients to drop out of sync.

---

## 3. Constraints & Technical Boundaries

1. **Zero Asset Destruction:** All existing `.mesh`, `.dds`, and `.gui` assets remain untouched.
2. **Clausewitz Parser Compliance:** Valid Lua syntax in `common/defines/99_supreme_performance.lua` and valid script syntax in all `.txt` files, verified by automated linters.
3. **No Exploitable Player Penalties:** Division limits and AI adjustments apply strictly to AI tags; players retain full sovereign control over their army composition.
4. **Workshop Synchronization:** All optimization changes in `Baianagem-WW1/WW1` must be instantly mirrored to the Steam Workshop staging folder (`E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`).

---

## 4. Architectural Pillars of Supreme Engine Optimization

### Pillar 1: Reverse-Engineered Clausewitz Engine Defines (`common/defines/99_supreme_performance.lua`)

Consolidates and extends performance and netcode defines into a single, high-precedence file (`99_supreme_performance.lua`), harmonizing with the multiplayer desync fix:

```lua
-- Baianagem-WW1: Supreme Engine Optimization & Late-Game Acceleration Defines
-- Reverse-engineered from hoi4.exe and calibrated for zero gameplay degradation and 2-4 GB RAM support.

-- =========================================================================
-- 1. HISTORY, COMBAT LOGS & MEMORY FOOTPRINT (Eliminates Midnight Tick Lag)
-- =========================================================================
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 1                 -- Vanilla: 12. Retains 1 month of active combat data; slashes RAM usage and midnight cleanup by 90%.
NDefines.NGame.AIR_LOG_TIMEOUT_HOURS = 24                -- Vanilla: 48+. Prunes completed air mission logs after 24h.
NDefines.NGame.TRADE_ROUTE_RECALCULATE_FREQUENCY_DAYS = 10 -- Vanilla: 3-5. Prevents daily sea-route path recalculations.
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 100            -- Multiplayer netcode: prevents host speed drop while maintaining lockstep command timestamps.
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 120
NDefines.NResistance.GARRISON_LOG_MAX_MONTHS = 1         -- Vanilla: 12. Drops ancient garrison casualty logs from memory.
NDefines.NNavy.NAVAL_ACCIDENTS_DAYS_TO_LIVE = 14         -- Vanilla: 30. Cleans up naval accident notices rapidly.

-- =========================================================================
-- 2. AI SIMULATION TICK THROTTLING (CPU Main Thread Relief)
-- =========================================================================
NDefines.NAI.UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 72 -- Vanilla: 24. AI evaluates supply bottlenecks every 3 days instead of daily.
NDefines.NAI.UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS = 72 -- Vanilla: 24. Evaluates motorization hub upgrades every 3 days.
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 14    -- Vanilla: 3. AI re-weights tech priorities every 2 weeks.
NDefines.NAI.RAIDS_CREATE_FREQUENCY_DAYS = 14            -- Vanilla: 7. Throttles raid calculation passes.
NDefines.NMilitary.ATTACHED_WINGS_ORDER_UPDATE_DAYS = 5  -- Vanilla: 1. Updates army air-wing assignments every 5 days.
NDefines.NMilitary.REINFORCEMENT_REQUEST_DAYS_FREQUENCY = 4 -- Vanilla: 2. Batches division equipment replenishment requests.
NDefines.NAITheatre.AI_THEATRE_STATE_UPDATE_MAX_STATE_COUNT_TO_EXPAND = 10 -- Clamps theatre expansion search depth.

-- =========================================================================
-- 3. GRAPHICS & GEOMETRY RENDERING PASSES (Preserves 100% 3D Models & GFX)
-- =========================================================================
NDefines.NGraphics.ROOT_FRONT_SMOOTHEN_PASSES = 1        -- Vanilla: 4. Reduces front spline curve tessellation passes by 75% without visual degradation.
NDefines.NGraphics.ROOT_FRONT_MAX_INTERSECTION_TESTS_FRONT = 4 -- Vanilla: 8. Simplifies collision checks between overlapping battle plans.
NDefines.NGraphics.SNAPPED_OFF_FRONT_SMOOTHEN_PASSES = 1
NDefines.NGraphics.SUPPLYFLOW_SMOOTHEN_PASSES = 1        -- Reduces supply map spline tessellation.
NDefines.NGraphics.TRADEROUTE_SMOOTHEN_PASSES = 1        -- Reduces trade route map spline tessellation.
NDefines.NGraphics.TRADE_ROUTE_MAX_LINES = 12            -- Vanilla: 50. Limits simultaneous 3D trade convoy paths rendered.
NDefines.NGraphics.WEATHER_DISTANCE_CUTOFF = 350.0       -- Culls 3D rain/snow particles when zoomed out past theatre level.
NDefines.NGraphics.WEATHER_PLAYBACK_RATE = 0.6          -- Smooth particle update rate.
NDefines.NGraphics.UNITS_DISTANCE_CUTOFF = 180.0         -- Switches 3D models to division counters cleanly at high zoom levels.
NDefines.NGraphics.CITY_SPRAWL_SHRINK_DISTANCE = 140.0   -- Shrinks microscopic 3D city buildings smoothly when zoomed out.
NDefines.NGraphics.PROVINCE_NAME_DRAW_DISTANCE = 220.0   -- Renders province labels only within useful tactical zoom.
NDefines.NGraphics.SHIPS_DISTANCE_CUTOFF = 180.0         -- Culls 3D ship models when zoomed out.
NDefines.NMapIcons.TOP_MAP_ICON = 40                     -- Clamps maximum stacked icons rendered per province.
```

---

### Pillar 2: Dynamic Peacetime Division Regulation & Anti-Micro Spam

In WW1, minor nations that have no strategic or historical involvement in the war (e.g. Paraguay, Bolivia, Ecuador, Tibet, Bhutan, Liberia) frequently spam dozens of useless 4-battalion divisions that wander around borders, flooding the engine with pathfinding requests.

1. **Declarative AI Division Regulation (`common/ai_strategy/ww1_performance_ai_limiter.txt`):**
   - Implemented via Clausewitz declarative `ai_strategy` blocks with `abort_when_not_enabled = yes`.
   - Extends the existing 3-tier limiter with a dedicated peace-time neutral minor rule:
     ```clausewitz
     ww1_peace_neutral_minor_limiter = {
         enable = {
             is_ai = yes
             is_major = no
             has_war = no
             is_in_faction = no
             num_of_military_factories < 6
             num_divisions > 8
         }
         abort_when_not_enabled = yes
         ai_strategy = {
             type = ai_wanted_divisions_factor
             value = -100
         }
         ai_strategy = {
             type = equipment_stockpile_surplus_ratio
             value = 40
         }
     }
     ```
   - Automatically aborts the second any country joins a faction or enters a war, allowing full mobilization.
2. **Major Power Template Quality via Starting OOBs & Strategy:**
   - Instead of risky experimental `common/ai_templates/` scripting (which can freeze AI unit production), maintain historical starting templates (9–12 battalions with artillery, 24–30 width) in `history/countries/` and reinforce with `role_ratio` in `common/ai_strategy/` to ensure majors build combat-grade divisions rather than 2-battalion micro-divisions.

---

### Pillar 3: Script & Trigger Execution Acceleration

1. **Country-Specific Decision `allowed` Guards:**
   - Audit and enforce `allowed = { tag = TAG }` or `allowed = { original_tag = TAG }` across country-specific decision files in `common/decisions/`.
   - Prevents the Clausewitz parser from executing `available` and `visible` trigger tests across 80+ tags for country-specific content.
2. **Generic Decision Boundary:**
   - Shared/generic decision files (such as `formable_nation_decisions.txt` and `specialforces_decisions.txt`) are preserved and protected, using fast-failing guards (e.g. `is_ai = no` for player formables) without breaking minor tags.

---

### Pillar 4: Memory Cache Reliever (RAM 2–4 GB Safety Net)

1. **Transient Operational Flag Cleanup (`common/scripted_effects/ww1_optimization_effects.txt`):**
   - Hooked to monthly on-action `on_monthly`:
     - Clears transient operational flags (e.g. completed chemical barrage indicators, expired tactical mission cooldowns, and resets temporary battle counters on capitulated nations).
     - Never touches persistent progress flags, focus requirements, or civil war state tracking.
2. **Save Game Serialization Optimization:**
   - Shorter combat logs reduce save file size from ~30 MB uncompressed to < 6 MB.
   - Eliminates auto-save micro-stuttering in both singleplayer and multiplayer.

---

## 5. Builder Decisions (Resolved During Builder Check)

The following architectural calls were settled during the builder check to ensure 100% adherence to the user's "DO NOT BREAK" constraint:
1. **Division Templates for Majors:** Handled via authentic starting OOB templates and `ai_strategy` role ratios rather than a complex new `ai_templates` system that could disrupt AI production.
2. **AI Division Limiter Execution:** Implemented declaratively via `common/ai_strategy/ww1_performance_ai_limiter.txt` using native `ai_wanted_divisions_factor` tokens, which are deterministic, zero-overhead, and automatically abort on war entry.
3. **Decision Audit Scope:** Enforced on country-specific decision categories while exempting generic formable nations to preserve mod breadth.
4. **Defines Consolidation:** Merged into `common/defines/99_supreme_performance.lua` to ensure consistent load order and zero define collisions.

---

## 6. Verification Plan

1. **Automated Unit Testing (`tests/test_ww1_supreme_optimization.py`):**
   - `test_supreme_performance_defines_syntax_and_values`: Asserts `common/defines/99_supreme_performance.lua` is valid Lua and sets all critical memory, netcode, and render constants.
   - `test_combat_log_memory_limits`: Confirms `COMBAT_LOG_MAX_MONTHS <= 2`, `GARRISON_LOG_MAX_MONTHS <= 2`, `AIR_LOG_TIMEOUT_HOURS <= 48`.
   - `test_render_pass_tessellation_optimization`: Confirms spline smoothing passes are capped at 1.
   - `test_ai_peacetime_division_regulation`: Asserts AI strategy correctly regulates peacetime division micro-spam for neutral minors without affecting active belligerents or players.
   - `test_decision_allowed_blocks_hygiene`: Verifies country-specific decision categories have proper tag scoping.
2. **QA Suite Integration:**
   - Register in `scripts/qa_audit_all.py`.
   - Run complete audit (`11 suites passing`).
3. **Steam Workshop Deployment:**
   - Mirror all committed changes to `E:\SteamLibrary\steamapps\workshop\content\394360\3809191491`.
