-- Baianagem WW1 engine foundation, checked against HOI4 1.19.3.
-- Country differences belong in equipment, doctrine and national mechanics.
-- Global values below apply equally to human and AI countries.

-- Campaign chronology. Technology dates provide the ahead-of-time baseline;
-- BASE_RESEARCH_YEAR is not an engine define in this version.
NDefines.NGame.START_DATE = "1911.6.1.12"
NDefines.NGame.END_DATE = "1924.1.1.1"
NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 2.0

-- Keep the campaign's existing command capacities during the foundation pass.
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 30
NDefines.NMilitary.CORPS_COMMANDER_ARMIES_CAP = -1
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 30
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 7

-- These caps are COUNTRY defines; category membership alone does not make a
-- battalion special forces. Subunits also need special_forces = yes.
NDefines.NCountry.SPECIAL_FORCES_CAP_BASE = 0.05
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 24

-- Existing WW1 land-combat baseline, retained pending controlled combat tests.
NDefines.NMilitary.LAND_COMBAT_ORG_DAMAGE_MODIFIER = 0.055
NDefines.NMilitary.LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.065
NDefines.NMilitary.COMBAT_STACKING_START = 6
NDefines.NMilitary.COMBAT_STACKING_PENALTY = -0.06

-- Native supply baseline. Correcting the former wrong namespace must not
-- silently introduce double attrition. The organisation CAP is a multiplier
-- at zero supply, not a negative organisation modifier.
NDefines.NMilitary.OUT_OF_SUPPLY_ATTRITION = 0.20
NDefines.NMilitary.SUPPLY_ORG_MAX_CAP = 0.35

-- Limited early close-air support. Retain the existing reduced damage model;
-- request limits are NAI defines and do not cap a player's own assigned wings.
NDefines.NMilitary.LAND_AIR_COMBAT_STR_DAMAGE_MODIFIER = 0.005
NDefines.NMilitary.LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER = 0.005
NDefines.NAI.LAND_COMBAT_CAS_PER_COMBAT = 10
NDefines.NAI.LAND_COMBAT_CAS_PLANES_PER_ENEMY_ARMY_LIMIT = 50

-- Keep native interception, AA and strategic-bombing mechanics until the
-- period-specific aircraft/equipment progression is tested. These priority
-- scales select targets; they do not multiply factory destruction.
NDefines.NAir.ANTI_AIR_PLANE_DAMAGE_FACTOR = 0.8
NDefines.NAir.ANTI_AIR_PLANE_DAMAGE_CHANCE = 0.1
NDefines.NAir.ANTI_AIR_MAXIMUM_DAMAGE_REDUCTION_FACTOR = 0.75
NDefines.NAir.STRATEGIC_BOMBING_STATE_BUILDING_SCALE = 1.0
NDefines.NAir.STRATEGIC_BOMBING_RAILWAY_PRIORITY_SCALE = 0.2
NDefines.NAir.AIR_WING_BOMB_DAMAGE_FACTOR = 2.0
NDefines.NAir.COMBAT_BETTER_AGILITY_DAMAGE_REDUCTION = 0.45
