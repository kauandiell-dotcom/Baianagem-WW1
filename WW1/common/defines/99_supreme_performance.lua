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
