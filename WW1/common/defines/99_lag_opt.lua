-- Extreme Optimization Mod - Lite: AI computation frequency only (NO unit/resource/equipment changes)
-- Patches individual fields only, does not replace the whole defines file (loads after 00_defines.lua)

-- Front-line reassignment (AI Force Concentration) computation frequency
NDefines.NAI.AIFC_UPDATE_FREQUENCY_DAYS = 15               -- default 5
NDefines.NAI.AIFC_UNIT_NUDGE_FREQUENCY_DAYS = 45           -- default 15
NDefines.NAI.REASSIGN_TO_ANOTHER_FRONT_FACTOR = 0.25       -- default 0.5, lower = less eager to reassign

-- Other AI update frequency relief (air/navy/intel)
NDefines.NAI.AI_UPDATE_ROLES_FREQUENCY_HOURS = 96          -- default 48
NDefines.NAI.AI_NAVAL_GOALS_UPDATE_FREQUENCY_DAYS = 21     -- default 7
NDefines.NAI.RAIDS_CREATE_FREQUENCY_DAYS = 21              -- default 7
NDefines.NAI.CONVOY_RAIDING_TARGET_RECALC_DAYS = 30        -- default 15
NDefines.NAI.STRIKE_FORCE_TARGET_RECALC_DAYS = 15          -- default 5
NDefines.NAI.AI_OBJECTIVE_DEFAULT_TARGET_RECALC_DAYS = 15  -- default 5

-- Diplomacy/trade request interval relief: 24h -> 96h
NDefines.NDiplomacy.DIPLOMACY_HOURS_BETWEEN_REQUESTS = 96  -- default 24

-- How often the AI re-evaluates "is there a better template/equipment/doctrine to switch to"
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_TEMPLATE = 30         -- default 7
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_EQUIPMENT = 30        -- default 7
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_DOCTRINE = 90         -- default 30

-- Ship refit re-evaluation frequency
NDefines.NAI.REFIT_SHIP_RELUCTANCE = 90                    -- default 28

-- Number of state targets re-evaluated per hour (perf-critical, per the vanilla comment)
NDefines.NRaids.MAX_STATE_TARGETS_TO_EVALUATE_PER_HOUR = 20  -- default 50

-- Front-line reassignment (AIFC) pathfinding evaluation range (vanilla comment: raising this
-- causes stuttering/perf loss -> lowering it relieves that)
NDefines.NAI.AIFC_PATH_MAX_COST = 4.0                         -- default 7.0

-- Don't re-evaluate subject/ally shares every peace conference turn (vanilla comment: may
-- heavily affect performance on large peace conferences)
NDefines.NAI.PEACE_AI_EVALUATE_FOR_SUBJECTS = false           -- default true
NDefines.NAI.PEACE_AI_EVALUATE_FOR_ALLIES = false             -- default true

-- Raid target icon updates per frame (pure UI rendering, no gameplay impact)
NDefines.NRaids.MAX_TARGETS_TO_UPDATE_PER_FRAME = 40           -- default 100

-- ============================================================
-- Save file size / RAM: purge old logs & obsolete templates sooner
-- ============================================================

NDefines.NAI.REMOVE_OBSOLETE_TEMPLATE_DAYS = 90            -- default 180
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 3                   -- default 12
NDefines.NResistance.GARRISON_LOG_MAX_MONTHS = 3           -- default 12
NDefines.NNavy.NAVAL_ACCIDENTS_DAYS_TO_LIVE = 60            -- default 120 (days, ~2 months)

-- NOTE (Lite): this version intentionally does NOT touch any equipment file
-- (no build_cost_ic / resource / manpower / combat-stat scaling for planes,
-- ships or convoys), and does NOT touch AIRBASE_CAPACITY_MULT,
-- WANTED_*_PLANES_* or SUPPLY_CONVOY_FACTOR, since those exist only to
-- compensate for the Full version's x8 equipment compression. If you want
-- that (bigger FPS/entity-count win, but changes unit costs/stats and makes
-- convoys much more expensive), use the Full "Extreme Optimization Mod"
-- instead of this Lite version -- do not enable both at once.
