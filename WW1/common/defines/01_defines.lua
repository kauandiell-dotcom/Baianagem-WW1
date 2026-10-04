-- Baianagem-WW1: Core Engine & Military Defines (HOI4 1.19.3)
-- Optimized for Multiplayer (5-8 players) with High Command Capacity

-- ============================================================
-- Chronological Baseline: 1 de Junho de 1911 (1911.6.1.12)
-- ============================================================
NDefines.NGame.START_DATE = "1911.6.1.12"		-- Official campaign start in the Belle Époque
NDefines.NGame.END_DATE = "1924.1.1.1"			-- Post-Lausanne & post-Russian Civil War conclusion
NDefines.NTechnology.BASE_RESEARCH_YEAR = 1911	-- Base year for research penalty calculations
NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 2.0 -- Standard ahead-of-time factor
NDefines.NTechnology.MAX_AHEAD_RESEARCH_PENALTY = 2.5     -- Max penalty cap

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

-- ============================================================
-- Special Forces Capacity (Controlled Shock Troops)
-- ============================================================
NDefines.NMilitary.SPECIAL_FORCES_CAP_BASE = 0.05		-- 5% of total army to avoid elite spam
NDefines.NMilitary.SPECIAL_FORCES_CAP_MIN = 24			-- Baseline 24 battalions

-- ============================================================
-- Land Combat & Organization Damage Dynamics (Balanced WW1 Engine)
-- ============================================================
-- Normalizes org damage to prevent instant evaporation, while str damage punishes reckless Force Attack
NDefines.NMilitary.LAND_COMBAT_ORG_DAMAGE_MODIFIER = 0.055	-- Calibrated (Vanilla 0.053): defense holds against barrage
NDefines.NMilitary.LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.065	-- Punishes Force Attack: real casualties and equipment depletion

-- ============================================================
-- Combat Stacking Penalties (Anti-Division Spam System)
-- ============================================================
-- Heavily penalizes stuffing too many divisions into the same battle
NDefines.NMilitary.COMBAT_STACKING_START = 6			-- Penalties begin at 6 divisions per battle
NDefines.NMilitary.COMBAT_STACKING_PENALTY = -0.06		-- -6% efficiency per extra division (anti-spam)

-- ============================================================
-- Logistics & Supply Depletion (Destructive Out of Supply)
-- ============================================================
NDefines.NSupply.OUT_OF_SUPPLY_ATTRITION = 0.40			-- 40% attrition when unsupplied
NDefines.NSupply.OUT_OF_SUPPLY_ORG_FACTOR = -0.65		-- -65% org penalty for starving divisions

-- ============================================================
-- Air Warfare & Bombing Redirection (WW1 Doctrine)
-- ============================================================
-- CAS neutralization in land battles (Early aviation lacked tactical coordination)
NDefines.NMilitary.LAND_AIR_COMBAT_STR_DAMAGE_MODIFIER = 0.005	-- Vanilla 0.035 (85% reduction)
NDefines.NMilitary.LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER = 0.005	-- Vanilla 0.035 (85% reduction)
NDefines.NMilitary.LAND_COMBAT_CAS_PER_COMBAT = 10				-- Vanilla 60 (Severely limited tactical CAS participation)
NDefines.NMilitary.LAND_COMBAT_CAS_PLANES_PER_ENEMY_ARMY_LIMIT = 50 -- Lower limit for CAS in land combat

-- Ground Anti-Air inability to shoot down high-altitude strategic bombers
NDefines.NMilitary.ANTI_AIR_PLANE_DAMAGE_FACTOR = 0.0			-- Vanilla 0.8 (Provincial AA cannot damage strategic bombers)
NDefines.NMilitary.ANTI_AIR_PLANE_DAMAGE_CHANCE = 0.0			-- Vanilla 0.1 (Zero direct shoot-down chance from ground AA batteries)
NDefines.NMilitary.ANTI_AIR_MAXIMUM_DAMAGE_REDUCTION_FACTOR = 0.10 -- Static ground AA cannot shield factories/railways

-- Strategic & Logistics Bombing Buffs (Devastating infrastructure warfare)
NDefines.NMilitary.STRATEGIC_BOMBING_STATE_BUILDING_SCALE = 2.5	-- Vanilla 1.0 (2.5x factory destruction)
NDefines.NMilitary.STRATEGIC_BOMBING_RAILWAY_PRIORITY_SCALE = 1.0	-- Vanilla 0.2 (5x railway targeting, crippling supply)
NDefines.NAir.AIR_WING_BOMB_DAMAGE_FACTOR = 4.0					-- Vanilla 2.0 (Double damage impact per bombing run)

-- Fighter Interception Lethality (Fighters easily slaughter unescorted bombers)
NDefines.NAir.COMBAT_BETTER_AGILITY_DAMAGE_REDUCTION = 0.60		-- Vanilla 0.45 (Nimble fighters easily tear slow bombers)