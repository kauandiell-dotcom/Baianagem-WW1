-- Baianagem-WW1: Core Engine & Military Defines (HOI4 1.19.3)
-- Optimized for Multiplayer (5-8 players) with High Command Capacity

-- ============================================================
-- Network & Simulation Tick Pacing (Multiplayer Fix)
-- ============================================================
-- Lowers speed progressively before pausing so lagging clients can catch up
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 3		-- Vanilla is 10; 3 prevents huge desync gaps in MP
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 10			-- Pauses only after speed reduction fails to recover
NDefines.NGame.GAME_SPEED_SECONDS = { 1.0, 0.25, 0.1, 0.05, 0.02 } -- Speed 5 capped at 0.02s to prevent host runaway
NDefines.NCountry.EVENT_PROCESS_OFFSET = 20		-- Smooth 20-day distribution of event checks (prevents 30-day lag spikes)

-- ============================================================
-- Military Command Caps (High Capacity for MP Players)
-- ============================================================
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 30	-- 30 divisions per general (generous capacity for players)
NDefines.NMilitary.CORPS_COMMANDER_ARMIES_CAP = -1		-- Corps commander cannot command armies
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 30		-- 30 divisions under direct field marshal
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 7			-- 7 armies per field marshal (210 divisions per theater)