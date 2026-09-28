-- Better Player Cooperation - faction tuning

-- Vanilla is 0.015 FI/day (scaled by manifest fulfillment and influence share),
-- which is roughly one rule change every 2-4 months of game time. Since this mod
-- hands the faction to players with a blank preset they are meant to configure
-- themselves, that is too slow. 5x puts a rule change at roughly two weeks.
NDefines.NFactions.PASSIVE_INITIATIVE_GENERATION = 0.075
