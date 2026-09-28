-- HOI4 Lag Optimization: GPU/그래픽 부하 완화 (사용자 요청 "Ultimate FPS & CPU Booster" 항목 반영)
-- 00_graphics.lua(NDefines_Graphics.NGraphics) 뒤에 로드되어 특정 필드만 패치한다.
--
-- 아래 항목은 실제로 존재하는 그래픽 define만 반영했다. 모드 설명에 있던
-- "폭풍 파티클 밀도 -75%", "3D 유닛->2D 카운터 전환 거리 120->90",
-- "지형 텍스처를 16x16 단색 dds로 교체"는 defines.lua에서 노출된 수치가
-- 아니라(엔진 하드코딩 또는 실제 텍스처/파티클 애셋 교체가 필요한 영역)
-- 이 파일로는 구현하지 않았다. "항공전 3D 모델 1개=비행기 다수 표시"는
-- NAirGfx.AIRPLANES_*_ANIM 값으로 실제 구현했다 (파일 하단 참고).

-- UI 스터터 완화: 그라디언트 국경선 리페인트 주기 (카메라 패닝 시 끊김 방지)
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_REFRESH_FREQ = 0.30   -- 기본 0.12

-- 지도 아이콘 그룹핑 프레임당 처리량 축소 (반응성 대신 성능)
NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10              -- 기본 20

-- 포스트프로세싱 부하 완화: 블룸 비활성화
NDefines_Graphics.NGraphics.BLOOM_SCALE = 0                        -- 기본 0.9
NDefines_Graphics.NGraphics.EMISSIVE_BLOOM_STRENGTH = 0            -- 기본 1.0

-- 해상 굴절 효과 비활성화 (컷오프 거리를 0으로: 어떤 거리에서도 그리지 않음)
NDefines_Graphics.NGraphics.DRAW_REFRACTIONS_CUTOFF = 0            -- 기본 250

-- 전장의 안개(Fog of War) 시각효과 비활성화
NDefines_Graphics.NGraphics.DRAW_FOW_CUTOFF = 0                    -- 기본 400

-- (3D 도시/건물 스프롤은 게임 자체 그래픽 설정에 이미 끄는 옵션이 있어서 제거함 --
-- 모드가 강제로 끄면 그 설정을 쓰고 싶은 사람의 선택권을 뺏는 것이라 판단)

-- 지면 눈/진흙 동적 텍스처 페인팅 비활성화
NDefines_Graphics.NGraphics.POSTEFFECT_PER_PROVINCE_MIN_SNOW = 0   -- 기본 0.1
NDefines_Graphics.NGraphics.POSTEFFECT_PER_PROVINCE_MAX_SNOW = 0   -- 기본 0.2
NDefines_Graphics.NGraphics.POSTEFFECT_TOTAL_MIN_SNOW = 0          -- 기본 0.0 (변경 없음, 명시적 유지)
NDefines_Graphics.NGraphics.POSTEFFECT_TOTAL_MAX_SNOW = 0          -- 기본 0.05

-- ============================================================
-- 항공전 3D 모델 압축 (순수 렌더링, 유닛 스탯/밸런스는 전혀 안 건드림)
-- 각 값은 "이 애니메이션 인스턴스 1개가 실제로 대표하는 비행기 수"이다
-- (00_graphics.lua 주석: "Number of fighters needed for a single instance
-- of this animation"). 값을 올리면 같은 규모의 항공전(공역 위 수백 대)을
-- 훨씬 적은 3D 모델/애니메이션 인스턴스로 표시하게 되어, 후반부 유럽 상공
-- 같은 혼잡 공역에서의 렌더링 부하가 크게 줄어든다. 유닛 개수/전투력/비용은
-- 그대로이므로 밸런스에는 영향이 없다.
-- ============================================================

NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_PATROL_ANIM = 30            -- 기본 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_PATROL_ANIM = 90            -- 기본 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_BOMBER_BOMBING_ANIM = 30            -- 기본 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_BOMBER_BOMBING_ANIM = 90            -- 기본 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_VS_1_FIGHTER_ANIM = 30      -- 기본 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_VS_3_FIGHTER_ANIM = 90      -- 기본 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_TRANSPORT_SUPPLY_ANIM = 30          -- 기본 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_TRANSPORT_SUPPLY_ANIM = 90          -- 기본 3
NDefines_Graphics.NAirGfx.AIRPLANES_1_SCOUT_PLANE_PATROL_ANIM = 30        -- 기본 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_SCOUT_PLANE_PATROL_ANIM = 90        -- 기본 3
