--Victorianization Graphical Defines

--NMapMode
NDefines_Graphics.NMapMode.MAP_MODE_TERRAIN_TRANSPARENCY = 1
NDefines_Graphics.NMapMode.MAP_MODE_NAVAL_TERRAIN_TRANSPARENCY = 1

--NMapIcons
NDefines_Graphics.NMapIcons.DEFAULT_PRIORITY_NAVAL_BASE = 12

--NAirGfx
NDefines_Graphics.NAirGfx.AIRPLANES_CURVE_POINT_DENSITY = 0.5

--NGraphics
NDefines_Graphics.NGraphics.MAP_BUILDINGS_SHRINK_DISTANCE = 180
NDefines_Graphics.NGraphics.CITY_SPRAWL_SHRINK_DISTANCE = 220.0
NDefines_Graphics.NGraphics.DRAW_MAP_OBJECTS_CUTOFF = 1100.0
NDefines_Graphics.NGraphics.PROVINCE_BORDER_FADE_NEAR = 350
NDefines_Graphics.NGraphics.PROVINCE_BORDER_FADE_FAR = 355
NDefines_Graphics.NGraphics.STATE_BORDER_FADE_NEAR = 500
NDefines_Graphics.NGraphics.STATE_BORDER_FADE_FAR = 505
NDefines_Graphics.NGraphics.ORDER_MOVE_SMOOTHNESS = 0.92
NDefines_Graphics.NGraphics.ORDER_MOVE_SMOOTHEN_PASSES = 1
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_STATE_A = 1.5
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_SUPPLY_AREA_R = 1.0
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_SUPPLY_AREA_G = 0.62
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_SUPPLY_AREA_B = 0.33
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_SUPPLY_AREA_A = 1.5
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_PROVINCE_G = 0.32
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_PROVINCE_B = 0.15
NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_PROVINCE_A = 1.5
--	BORDER_COLOR_CUSTOM_HIGHLIGHTS = {
		--[[ Groups of 4 numbers are RGBA.
			If two colors are both active on a border, (because one province is
				part of a group using one color, and the other province is part
				of another group), then the color that comes first in this list
				is the color that will be used. ]]
--		0.0, 0.61, 0.75, 1.0, -- 0: mouse hover
--		1.0, 0.06, 0.0, 1.0,  -- 1: bad, while active
--		0.1, 0.6, 0.2, 1.0,   -- 2: good, while active
--		0.8, 0.3, 0.0, 1.0,   -- 3: bad, while passive
--		0.0, 0.4, 0.8, 1.0,   -- 4: good, while passive
--		0.3, 0.9, 0.3, 0.8,   -- 5: controlled, neutral positive
--		0.7, 0.7, 0.0, 1.0,   -- 6: not ours, neutral negative
--		0.1, 0.6, 0.2, 1.0,   -- 7: construction: valid primary build target
--		1.0, 0.06, 0.0, 1.0,  -- 8: construction: invalid primary build target
--		0.3, 0.9, 0.3, 0.8,   -- 9: construction: foreign primary build target
--		0.0, 0.4, 0.8, 1.0,   -- 10: construction: valid secondary build target
--		0.8, 0.3, 0.0, 1.0,   -- 11: construction: invalid secondary build target
--		0.7, 0.7, 0.0, 1.0,   -- 12: construction: foreign secondary build target
--		0.2, 0.61, 0.75, 1.0, -- 13: FACTION_THEATER_COLOR_INDEX
--		0.2, 0.61, 0.75, 1.0, -- 14: FACTION_THEATER_HIGHLIGHT_COLOR_INDEX
--	}
NDefines_Graphics.NGraphics.DRAW_REFRACTIONS_CUTOFF = 180
NDefines_Graphics.NGraphics.DRAW_SHADOWS_CUTOFF = 150
NDefines_Graphics.NGraphics.DRAW_SHADOWS_FADE_LENGTH = 20
NDefines_Graphics.NGraphics.DRAW_FOW_CUTOFF = 70
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_FIELD_COUNTRY_LOW = 0.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_FIELD_COUNTRY_HIGH = 9000.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_COUNTRY_LOW = 0.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_COUNTRY_CENTER_THICKNESS = 0.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_COUNTRY_HIGH = 35.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_STATE = 1.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_STRATEGIC_REGIONS = 50.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_DIPLOMACY = 1.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_COUNTRY = 0.98
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_DIPLOMACY = 0.98
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_STATE = 0.98
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_SUPPLY_AREA = 0.995
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_RESISTANCE = 1.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_FACTIONS = 1.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_COUNTRY = 0.08
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_STATE = 1.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_SUPPLY_AREA = 0.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_RESISTANCE = 0.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_REFRESH_FREQ = 0.05
NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_GOOD = {76.0/255, 255.0/255, 0.0/255, 1}
NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_NEUTRAL = {0.0/255, 135.0/255, 255.0/255, 1}
NDefines_Graphics.NGraphics.STRATEGIC_NAVY_COLOR_NEUTRAL = {0.0/255, 55.0/255, 255.0/255, 1}
NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_CAPITAL_CUTOFF_MAX = 500.0
NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF_MAX = 500.0
NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_DOT_CUTOFF_MAX = 500.0
NDefines_Graphics.NGraphics.AIRBASE_ICON_DISTANCE_CUTOFF = 700
NDefines_Graphics.NGraphics.NAVALBASE_ICON_DISTANCE_CUTOFF = 700
NDefines_Graphics.NGraphics.RADAR_ICON_DISTANCE_CUTOFF = 800
NDefines_Graphics.NGraphics.CAPITAL_ICON_CUTOFF = 500
NDefines_Graphics.NGraphics.UNITS_DISTANCE_CUTOFF = 200.0
NDefines_Graphics.NGraphics.SHIPS_DISTANCE_CUTOFF = 220.0
NDefines_Graphics.NGraphics.UNIT_ARROW_DISTANCE_CUTOFF = 700
NDefines_Graphics.NGraphics.UNITS_ICONS_DISTANCE_CUTOFF = 500
NDefines_Graphics.NGraphics.NAVAL_COMBAT_DISTANCE_CUTOFF = 900
NDefines_Graphics.NGraphics.FACILITY_DISTANCE_CUTOFF = 700
NDefines_Graphics.NGraphics.LAND_COMBAT_DISTANCE_CUTOFF = 500
NDefines_Graphics.NGraphics.DECISION_MAP_ICON_DISTANCE_CUTOFF = 750
NDefines_Graphics.NGraphics.NAVAL_MISSION_ICONS_DISTANCE_CUTOFF = 1000
NDefines_Graphics.NGraphics.NAVAL_MINES_DISTANCE_CUTOFF = 600
NDefines_Graphics.NGraphics.CRYPTOLOGY_MAP_ICON_DISTANCE_CUTOFF = 750
NDefines_Graphics.NGraphics.MAP_ICONS_GROUP_CAM_DISTANCE = 50.0
NDefines_Graphics.NGraphics.MAP_ICONS_STATE_GROUP_CAM_DISTANCE = 150.0
NDefines_Graphics.NGraphics.MAP_ICONS_STRATEGIC_GROUP_CAM_DISTANCE = 280
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 4
NDefines_Graphics.NGraphics.MAP_ICONS_GROUP_SPLIT_SELECTED_LIMIT = 1
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE = 280
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC = 300
NDefines_Graphics.NGraphics.TOOLTIP_DELAYED_DELAY = 0.01
NDefines_Graphics.NGraphics.TOOLTIP_SHOW_DELAY = 0.01
NDefines_Graphics.NGraphics.TOOLTIP_HIDE_DELAY = 0.01
NDefines_Graphics.NGraphics.WEATHER_DISTANCE_CUTOFF = 400
NDefines_Graphics.NGraphics.WEATHER_DISTANCE_FADE_LENGTH = 150
NDefines_Graphics.NGraphics.WEATHER_PLAYBACK_RATE = 0.08
NDefines_Graphics.NGraphics.WEATHER_PLAYBACK_RATE_CUTOFF = 400
NDefines_Graphics.NGraphics.BLOOM_SCALE = 0.0
NDefines_Graphics.NGraphics.SUN_HEIGHT  = 1200
NDefines_Graphics.NGraphics.SUN_INTENSITY = 0.9
NDefines_Graphics.NGraphics.TREE_FADE_NEAR = 180.0
NDefines_Graphics.NGraphics.TREE_FADE_FAR = 220.0
NDefines_Graphics.NGraphics.SUPPLY_ICON_CUTOFF = 700.0
NDefines_Graphics.NGraphics.RAILWAY_ICON_CUTOFF = 700.0
NDefines_Graphics.NGraphics.FRIEND_COLOR  = {1.0, 1.0, 1.0}
NDefines_Graphics.NGraphics.NEUTRAL_COLOR = {0.8, 0.8, 0.8}
NDefines_Graphics.NGraphics.RAID_ARROW_BALLISTIC_MAX_SEGMENTS = 40
NDefines_Graphics.NGraphics.RAID_ARROW_AIR_MAX_SEGMENTS = 40
NDefines_Graphics.NGraphics.RAID_ARROW_NAVAL_SUBDIVISIONS = 6
NDefines_Graphics.NGraphics.RAID_ARROW_LAND_SUBDIVISIONS = 6

--NFrontend
NDefines_Graphics.NFrontend.CAMERA_MIN_HEIGHT = 45.0