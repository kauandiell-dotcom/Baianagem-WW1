import re
from pathlib import Path

austria_path = Path("common/national_focus/austria.txt")
txt = austria_path.read_text(encoding="utf-8")

# Focus enrichments for Austria-Hungary:
replacements = [
    # 1. Delegations: add state slot + civ factory in Vienna (4)
    (
        r'(id = AUH_ww1_delegations\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_delegations_unlocked 4 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_to_variable = { auh_ww1_consent = 3 } add_political_power = 20 \3'
    ),
    # 2. Provincial Petitions: add railways and infrastructure connecting Vienna (4) to Prague (69) and Lemberg (91)
    (
        r'(id = AUH_ww1_provincial_petitions\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 69 = { add_building_construction = { type = infrastructure level = 1 instant = yes } } 91 = { add_building_construction = { type = infrastructure level = 1 instant = yes } } add_to_variable = { auh_ww1_cohesion = 6 } add_political_power = 20 \3'
    ),
    # 3. Hungarian Harvest: add infrastructure in Alföld (43) + provisions
    (
        r'(id = AUH_ww1_hungarian_harvest\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_grain_agreement_unlocked 43 = { add_building_construction = { type = infrastructure level = 1 instant = yes } } add_to_variable = { auh_ww1_provisions = 10 } add_to_variable = { auh_ww1_consent = 2 } \3'
    ),
    # 4. Granaries: add building slot and civ factory in Vienna (4) for food distribution
    (
        r'(id = AUH_ww1_granaries\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_project_granaries_unlocked 4 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_to_variable = { auh_ww1_provisions = 8 } add_political_power = 10 \3'
    ),
    # 5. Factory Canteens: add building slot in Bohemia (69)
    (
        r'(id = AUH_ww1_factory_canteens\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_project_canteens_unlocked 69 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_to_variable = { auh_ww1_provisions = 6 } add_to_variable = { auh_ww1_cohesion = 3 } \3'
    ),
    # 6. Skoda Contracts: add 1 arms factory in Bohemia (9) + artillery stockpile
    (
        r'(id = AUH_ww1_skoda_contracts\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 9 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant = yes } } add_equipment_to_stockpile = { type = artillery_equipment amount = 150 } add_tech_bonus = { name = AUH_ww1_skoda_contracts bonus = 0.50 uses = 1 category = artillery } army_experience = 10 \3'
    ),
    # 7. Steyr Small Arms: add 1 arms factory in Upper Austria (4) + infantry weapons stockpile
    (
        r'(id = AUH_ww1_steyr_small_arms\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 4 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = arms_factory level = 1 instant = yes } } add_equipment_to_stockpile = { type = infantry_equipment amount = 2500 } add_tech_bonus = { name = AUH_ww1_steyr_small_arms bonus = 0.50 uses = 1 category = infantry_weapons } \3'
    ),
    # 8. Carpathian Survey: add fortresses in Galicia (91, 154) to resist Russian attacks
    (
        r'(id = AUH_ww1_carpathian_survey\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_carpathian_defence_unlocked 91 = { add_building_construction = { type = bunker level = 2 instant = yes } } 154 = { add_building_construction = { type = bunker level = 2 instant = yes } } army_experience = 15 \3'
    ),
    # 9. Croatian Diet: add infrastructure in Croatia (103) and dockyard in Dalmatia (736)
    (
        r'(id = AUH_ww1_croatian_diet\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 set_country_flag = auh_ww1_project_sabor_unlocked 103 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = infrastructure level = 1 instant = yes } } 736 = { add_extra_state_shared_building_slots = 1 add_building_construction = { type = dockyard level = 1 instant = yes } } navy_experience = 10 add_to_variable = { auh_ww1_cohesion = 4 } \3'
    ),
    # 10. Trialist Compensation: industrial investment in Budapest (44) to pacify Hungarian magnates
    (
        r'(id = AUH_ww1_trialist_compensation\b.*?completion_reward = \{)(.*?)(auh_ww1_clamp_counters = yes \})',
        r'\1 44 = { add_extra_state_shared_building_slots = 2 add_building_construction = { type = industrial_complex level = 1 instant = yes } } add_to_variable = { auh_ww1_consent = 15 } add_political_power = 20 \3'
    ),
]

for pat, repl in replacements:
    txt, n = re.subn(pat, repl, txt, flags=re.DOTALL)
    print(f"Pattern {pat[:30]} replaced: {n} times")

austria_path.write_text(txt, encoding="utf-8")
print("Austria focus tree rewards enriched successfully!")
