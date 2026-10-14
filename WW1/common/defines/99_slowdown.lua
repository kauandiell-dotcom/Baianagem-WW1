-- Baianagem-WW1: Multiplayer Game Speed & Client Lag Synchronization
-- Resolves the "Frozen in Time" bug where non-host clients cannot click or give orders.
--
-- TECHNICAL EXPLANATION:
-- In HOI4 lockstep netcode, if a client falls behind the host, the host server silently
-- discards all command packets (clicks, orders, focus picks) with past timestamps.
-- If LAG_DAYS_FOR_LOWER_SPEED is set to 100, the game NEVER slows down to allow the lagging
-- client to catch up, trapping the player in "Ghost Mode" where time moves but clicks do nothing.
-- Furthermore, LAG_DAYS_FOR_PAUSE must always be GREATER than LAG_DAYS_FOR_LOWER_SPEED.

-- Threshold of client lag (in game days) before the host automatically reduces speed to let clients catch up:
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 15

-- Threshold of client lag (in game days) before the game forces a pause so lagging clients fully resynchronize:
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 30

-- RAM & Savegame serialization relief: Purge combat & garrison logs faster to eliminate midnight tick lag spikes
NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 2
NDefines.NResistance.GARRISON_LOG_MAX_MONTHS = 2
NDefines.NNavy.NAVAL_ACCIDENTS_DAYS_TO_LIVE = 30
