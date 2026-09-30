-- Baianagem-WW1: Supreme Graphics & VRAM/RAM Optimization Defines (HOI4 1.19.x)
-- Extreme frame-rate & video memory relief for low-spec PCs & integrated GPUs (2 GB RAM target)

-- UI stutter relief: gradient border refresh interval (prevents micro-stutters during camera pan)
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_REFRESH_FREQ = 0.35   -- default 0.12

-- Map icon grouping per frame
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10              -- default 20

-- Post-processing relief: disable bloom
NDefines_Graphics.NGraphics.BLOOM_SCALE = 0                        -- default 0.9
NDefines_Graphics.NGraphics.EMISSIVE_BLOOM_STRENGTH = 0            -- default 1.0

-- Sea refraction cutoff
NDefines_Graphics.NGraphics.DRAW_REFRACTIONS_CUTOFF = 0            -- default 250

-- Fog of War visual effect cutoff
NDefines_Graphics.NGraphics.DRAW_FOW_CUTOFF = 0                    -- default 400

-- Weather particle system cutoff (heavy clouds/rain/snow particles disabled across all distances)
NDefines_Graphics.NGraphics.WEATHER_DISTANCE_CUTOFF = 0            -- default 1500

-- Ground snow/mud dynamic texture painting disabled
NDefines_Graphics.NGraphics.POSTEFFECT_PER_PROVINCE_MIN_SNOW = 0   -- default 0.1
NDefines_Graphics.NGraphics.POSTEFFECT_PER_PROVINCE_MAX_SNOW = 0   -- default 0.2
NDefines_Graphics.NGraphics.POSTEFFECT_TOTAL_MIN_SNOW = 0          -- default 0.0
NDefines_Graphics.NGraphics.POSTEFFECT_TOTAL_MAX_SNOW = 0          -- default 0.05

-- 3D Mesh loading frame pacing
NDefines_Graphics.NGraphics.MAX_MESHES_LOADED_PER_FRAME = 10       -- default 10 (populates 3D figurines promptly without stutters)

-- Shadow rendering cutoff (eliminates dynamic cascading shadow maps in 2GB RAM / iGPU systems)
NDefines_Graphics.NGraphics.DRAW_SHADOWS_CUTOFF = 0                 -- default 150 (saves huge VRAM bandwidth)

-- Transition to 2D NATO counters at strategic zoom (renders full 3D models at tactical/operational zoom)
NDefines_Graphics.NGraphics.UNITS_DISTANCE_CUTOFF = 200.0           -- default 120.0-200.0 (renders 3D soldiers/horses/tanks at tactical zoom)
NDefines_Graphics.NGraphics.SHIPS_DISTANCE_CUTOFF = 220.0           -- default 120.0-220.0

-- Map icons & buildings draw distance optimization
NDefines_Graphics.NGraphics.MAP_BUILDINGS_SHRINK_DISTANCE = 120.0   -- default 180.0
NDefines_Graphics.NGraphics.CITY_SPRAWL_SHRINK_DISTANCE = 80.0     -- default 220.0
NDefines_Graphics.NGraphics.TREE_FADE_NEAR = 80.0                  -- default 250.0
NDefines_Graphics.NGraphics.TREE_FADE_FAR = 150.0                  -- default 350.0
NDefines_Graphics.NGraphics.AIRBASE_ICON_DISTANCE_CUTOFF = 450      -- default 700
NDefines_Graphics.NGraphics.NAVALBASE_ICON_DISTANCE_CUTOFF = 450    -- default 700
NDefines_Graphics.NGraphics.RADAR_ICON_DISTANCE_CUTOFF = 450        -- default 800

-- ============================================================
-- 3D Air Combat Animation Compression (saves huge GPU/CPU cycles in dense air zones)
-- ============================================================
NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_PATROL_ANIM = 40            -- default 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_PATROL_ANIM = 120           -- default 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_BOMBER_BOMBING_ANIM = 40            -- default 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_BOMBER_BOMBING_ANIM = 120           -- default 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_VS_1_FIGHTER_ANIM = 40      -- default 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_VS_3_FIGHTER_ANIM = 120      -- default 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_TRANSPORT_SUPPLY_ANIM = 40          -- default 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_TRANSPORT_SUPPLY_ANIM = 120          -- default 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_SCOUT_PLANE_PATROL_ANIM = 40        -- default 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_SCOUT_PLANE_PATROL_ANIM = 120        -- default 3
