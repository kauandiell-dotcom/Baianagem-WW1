-- Baianagem-WW1: Supreme Simulation & AI Optimization Defines (HOI4 1.19.x)
-- Extreme performance relief for CPU & RAM (2 GB target) with ZERO impact on player mechanics or unit balance

-- Front-line reassignment (AI Force Concentration) computation frequency
NDefines.NAI.AIFC_UPDATE_FREQUENCY_DAYS = 15               -- default 5
NDefines.NAI.AIFC_UNIT_NUDGE_FREQUENCY_DAYS = 45           -- default 15
NDefines.NAI.REASSIGN_TO_ANOTHER_FRONT_FACTOR = 0.25       -- default 0.5, lower = less eager to reassign (less frontline shuffling)

-- Other AI update frequency relief (air/navy/intel)
NDefines.NAI.AI_UPDATE_ROLES_FREQUENCY_HOURS = 96          -- default 48
NDefines.NAI.AI_NAVAL_GOALS_UPDATE_FREQUENCY_DAYS = 21     -- default 7
NDefines.NAI.RAIDS_CREATE_FREQUENCY_DAYS = 21              -- default 7
NDefines.NAI.CONVOY_RAIDING_TARGET_RECALC_DAYS = 30        -- default 15
NDefines.NAI.STRIKE_FORCE_TARGET_RECALC_DAYS = 15          -- default 5
NDefines.NAI.AI_OBJECTIVE_DEFAULT_TARGET_RECALC_DAYS = 15  -- default 5

-- Diplomacy/trade request interval relief: 24h -> 96h
NDefines.NDiplomacy.DIPLOMACY_HOURS_BETWEEN_REQUESTS = 96  -- default 24

-- How often the AI re-evaluates templates, equipment, doctrines and research
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_TEMPLATE = 60         -- default 7, was 30
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_EQUIPMENT = 60        -- default 7, was 30
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_DOCTRINE = 90         -- default 30
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 30      -- default 7 (75% less research weight recalculations)
NDefines.NAI.AI_UPDATE_THEATRE_DEFENSE_ORDERS_HOURS = 24   -- default 6 (4x less theatre defense churning)
NDefines.NAI.MIN_INVASION_PLAN_VALUE = 0.5                 -- prevents AI suicide micro-invasions
NDefines.NAI.DIVISION_UPGRADE_MIN_XP = 20                  -- prevents constant template editing on 1 XP
NDefines.NAI.ARMY_UPGRADE_MIN_XP = 20
NDefines.NAI.AIR_UPGRADE_MIN_XP = 20
NDefines.NAI.NAVY_UPGRADE_MIN_XP = 20

-- Ship refit re-evaluation frequency
NDefines.NAI.REFIT_SHIP_RELUCTANCE = 90                    -- default 28

-- Number of state targets re-evaluated per hour
NDefines.NRaids.MAX_STATE_TARGETS_TO_EVALUATE_PER_HOUR = 20  -- default 50

-- Front-line pathfinding evaluation range limit
NDefines.NAI.AIFC_PATH_MAX_COST = 4.0                         -- default 7.0

-- Don't re-evaluate subject/ally shares every peace conference turn (eliminates massive peace conference stalls)
NDefines.NAI.PEACE_AI_EVALUATE_FOR_SUBJECTS = false           -- default true
NDefines.NAI.PEACE_AI_EVALUATE_FOR_ALLIES = false             -- default true

-- Raid target icon updates per frame (pure UI rendering)
NDefines.NRaids.MAX_TARGETS_TO_UPDATE_PER_FRAME = 30           -- default 100

-- ============================================================
-- Save file size & RAM Relief: purge old logs & obsolete templates
-- ============================================================
NDefines.NAI.REMOVE_OBSOLETE_TEMPLATE_DAYS = 30            -- default 180 (cleans deleted AI templates rapidly)
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 2                   -- default 12 (83% smaller combat log history in RAM/saves)
NDefines.NResistance.GARRISON_LOG_MAX_MONTHS = 2           -- default 12
NDefines.NNavy.NAVAL_ACCIDENTS_DAYS_TO_LIVE = 30            -- default 120 (cleans naval wrecks/logs sooner)
