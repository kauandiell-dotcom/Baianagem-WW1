import re
from pathlib import Path

italy_path = Path("common/national_focus/italy.txt")
txt = italy_path.read_text(encoding="utf-8")

replacements = [
    # 1. Ansaldo Expansion: arms factory in Genoa (158) + 120 artillery
    (
        r'(id = ITA_ww1_ansaldo_expansion\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant = yes } } add_equipment_to_stockpile = { type = artillery_equipment amount = 120 } add_political_power = 25 \3'
    ),
    # 2. Aero Engine Contracts: arms factory in Turin (117) + air XP
    (
        r'(id = ITA_ww1_aero_engine_contracts\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 117 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant = yes } } air_experience = 20 add_tech_bonus = { name = ITA_ww1_aero_tech bonus = 0.50 uses = 1 category = air_equipment } \3'
    ),
    # 3. Ilva Steel Consortium: civ factory in Tuscany/Latium (2)
    (
        r'(id = ITA_ww1_ilva_steel_consortium\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 2 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_political_power = 30 \3'
    ),
    # 4. Apulian Aqueduct: infrastructure in Apulia (843)
    (
        r'(id = ITA_ww1_apulian_aqueduct\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 843 = { add_building_construction = { type = infrastructure level = 1 instant = yes } } 2 = { add_building_construction = { type = infrastructure level = 1 instant = yes } } add_to_variable = { ita_ww1_southern_gap = -10 } \3'
    ),
    # 5. Genoa Shipyards: add 1 dockyard
    (
        r'(id = ITA_ww1_genoa_shipyards\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 158 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant = yes } } navy_experience = 15 \3'
    ),
    # 6. Turin Motor Industry: add 1 civ factory
    (
        r'(id = ITA_ww1_turin_motor_industry\b.*?completion_reward = \{)(.*?)(ita_ww1_clamp_counters = yes \})',
        r'\1 117 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_political_power = 25 \3'
    ),
]

for pat, repl in replacements:
    txt, n = re.subn(pat, repl, txt, flags=re.DOTALL)
    print(f"Italian pattern {pat[:30]} replaced: {n} times")

italy_path.write_text(txt, encoding="utf-8")
print("Italy focus tree rewards enriched successfully!")
