# scripts/update_naval_hulls.py
import re

HULL_SLOT_DEFS = {
    'ironclad': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { heavy_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_heavy_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_heavy_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_light_medium_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_airplane_launcher } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_heavy_coal
			fixed_ship_battery_slot = ww1_1911_old_heavy
			fixed_ship_armor_slot = ww1_1911_old_belt
			fixed_ship_secondaries_slot = ww1_1911_secondary_battery
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = empty
			mid_2_custom_slot = empty
			rear_1_custom_slot = empty
		}'''),

    'pre_dreadnought': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { heavy_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_heavy_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_heavy_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_light_medium_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_airplane_launcher } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_heavy_coal
			fixed_ship_battery_slot = ww1_1911_mixed_heavy
			fixed_ship_armor_slot = ww1_1911_pre_belt
			fixed_ship_secondaries_slot = ww1_1911_secondary_battery
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = ww1_1911_secondary_battery
			mid_2_custom_slot = empty
			rear_1_custom_slot = empty
		}'''),

    'dreadnought': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { heavy_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_heavy_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_heavy_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_light_medium_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_airplane_launcher } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_heavy_coal
			fixed_ship_battery_slot = ww1_1911_uniform_heavy
			fixed_ship_armor_slot = ww1_1911_dread_belt
			fixed_ship_secondaries_slot = ww1_1911_secondary_battery
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = ww1_1911_secondary_battery
			mid_2_custom_slot = empty
			rear_1_custom_slot = ww1_1911_uniform_heavy
		}'''),

    'battlecruiser': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { heavy_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_heavy_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_heavy_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_light_medium_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_torpedo ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_heavy_battery ship_secondaries ship_light_battery ship_light_medium_battery ship_anti_air ship_airplane_launcher } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_heavy_coal
			fixed_ship_battery_slot = ww1_1911_uniform_heavy
			fixed_ship_armor_slot = ww1_1911_battlecruiser_belt
			fixed_ship_secondaries_slot = ww1_1911_secondary_battery
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = ww1_1911_secondary_battery
			mid_2_custom_slot = empty
			rear_1_custom_slot = ww1_1911_uniform_heavy
		}'''),

    'armoured_cruiser': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { cruiser_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_medium_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_cruiser_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_light_medium_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_medium_battery ship_light_medium_battery ship_secondaries ship_light_battery } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_torpedo ship_anti_air ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery ship_torpedo ship_anti_air ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_medium_battery ship_light_medium_battery ship_secondaries ship_torpedo ship_depth_charge ship_mine_layer } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_cruiser_coal
			fixed_ship_battery_slot = ww1_1911_medium
			fixed_ship_armor_slot = ww1_1911_cruiser_belt
			fixed_ship_secondaries_slot = ww1_1911_secondary_battery
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = empty
			mid_2_custom_slot = empty
			rear_1_custom_slot = ww1_1911_medium
		}'''),

    'protected_cruiser': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { cruiser_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_light_medium_battery ship_light_battery } }
			fixed_ship_armor_slot = { required = yes allowed_module_categories = { ship_cruiser_armor } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar ship_sonar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_light_medium_battery ship_light_battery } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_anti_air ship_secondaries ship_light_battery ship_airplane_launcher } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_anti_air ship_secondaries ship_light_battery ship_airplane_launcher } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_depth_charge ship_mine_layer ship_mine_sweeper ship_torpedo ship_light_battery ship_light_medium_battery } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_cruiser_coal
			fixed_ship_battery_slot = ww1_1911_light_medium
			fixed_ship_armor_slot = ww1_1911_protected_deck
			fixed_ship_secondaries_slot = empty
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = ww1_1911_torpedoes
			mid_2_custom_slot = empty
			rear_1_custom_slot = empty
		}'''),

    'torpedo_craft': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { light_ship_engine } }
			fixed_ship_battery_slot = { required = yes allowed_module_categories = { ship_light_battery } }
			fixed_ship_torpedo_slot = { required = yes allowed_module_categories = { ship_torpedo } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_light_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			fixed_ship_sonar_slot = { required = no allowed_module_categories = { ship_sonar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_light_battery ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_anti_air ship_light_battery } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_mine_layer ship_depth_charge ship_light_battery } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_depth_charge ship_mine_sweeper ship_torpedo ship_light_battery } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_light_coal
			fixed_ship_battery_slot = ww1_1911_light
			fixed_ship_torpedo_slot = ww1_1911_torpedoes
			fixed_ship_secondaries_slot = empty
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			fixed_ship_sonar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = ww1_1911_torpedoes
			mid_2_custom_slot = empty
			rear_1_custom_slot = empty
		}'''),

    'submarine': ('''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { sub_ship_engine } }
			fixed_ship_torpedo_slot = { required = yes allowed_module_categories = { ship_torpedo } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_light_battery } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_fire_control_system_slot = { required = no allowed_module_categories = { ship_fire_control_system } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_light_battery ship_torpedo } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_mine_layer } }
			mid_2_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_mine_layer } }
			rear_1_custom_slot = { required = no allowed_module_categories = { ship_torpedo ship_mine_layer } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1911_sub_engine
			fixed_ship_torpedo_slot = ww1_1911_sub_torpedoes
			fixed_ship_secondaries_slot = empty
			fixed_ship_anti_air_slot = empty
			fixed_ship_fire_control_system_slot = empty
			fixed_ship_radar_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = empty
			mid_2_custom_slot = empty
			rear_1_custom_slot = empty
		}''')
}

with open('common/units/equipment/ww1_1911_naval_hulls.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace for each hull and hull_legacy
for role, new_block in HULL_SLOT_DEFS.items():
    for suffix in ['', '_legacy']:
        hull_name = f"ww1_1911_{role}{suffix}"
        # Match module_slots = { ... } default_modules = { ... } inside this hull
        pattern = rf'({hull_name}\s*=\s*\{{.*?\n)(\t+module_slots\s*=\s*\{{.*?\n\t+\}}\s*\n\t+default_modules\s*=\s*\{{.*?\n\t+\}})'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content[:match.start(2)] + new_block + content[match.end(2):]
            print(f"Updated {hull_name}")
        else:
            print(f"WARNING: Could not find {hull_name}")

with open('common/units/equipment/ww1_1911_naval_hulls.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved common/units/equipment/ww1_1911_naval_hulls.txt")

# Now update ww1_early_carriers.txt
CARRIER_SLOTS = '''		module_slots = {
			fixed_ship_engine_slot = { required = yes allowed_module_categories = { carrier_ship_engine } }
			fixed_ship_deck_slot_1 = { required = yes allowed_module_categories = { ship_deck_space } }
			fixed_ship_deck_slot_2 = { required = no allowed_module_categories = { ship_deck_space } }
			fixed_ship_anti_air_slot = { required = no allowed_module_categories = { ship_anti_air } }
			fixed_ship_radar_slot = { required = no allowed_module_categories = { ship_radar } }
			fixed_ship_secondaries_slot = { required = no allowed_module_categories = { ship_secondaries ship_light_battery } }
			fixed_ship_armor_slot = { required = no allowed_module_categories = { ship_carrier_armor ship_cruiser_armor } }
			front_1_custom_slot = { required = no allowed_module_categories = { ship_anti_air ship_secondaries ship_light_battery } }
			mid_1_custom_slot = { required = no allowed_module_categories = { ship_deck_space ship_anti_air ship_secondaries ship_light_battery } }
		}
		default_modules = {
			fixed_ship_engine_slot = ww1_1917_carrier_machinery
			fixed_ship_deck_slot_1 = ww1_1917_flight_deck
			fixed_ship_deck_slot_2 = empty
			fixed_ship_anti_air_slot = empty
			fixed_ship_radar_slot = empty
			fixed_ship_secondaries_slot = ww1_1911_light
			fixed_ship_armor_slot = empty
			front_1_custom_slot = empty
			mid_1_custom_slot = empty
		}'''

with open('common/units/equipment/ww1_early_carriers.txt', 'r', encoding='utf-8') as f:
    ccontent = f.read()

for c_hull in ['ww1_1917_carrier', 'ww1_1917_carrier_legacy', 'ww1_1922_carrier', 'ww1_1922_carrier_legacy']:
    pattern = rf'({c_hull}\s*=\s*\{{.*?\n)(\s*module_slots\s*=\s*\{{.*?\n\s*\}}\s*\n\s*default_modules\s*=\s*\{{.*?\n\s*\}})'
    match = re.search(pattern, ccontent, re.DOTALL)
    if match:
        ccontent = ccontent[:match.start(2)] + CARRIER_SLOTS + ccontent[match.end(2):]
        print(f"Updated {c_hull}")
    else:
        print(f"WARNING: Could not find {c_hull}")

with open('common/units/equipment/ww1_early_carriers.txt', 'w', encoding='utf-8') as f:
    f.write(ccontent)
print("Saved common/units/equipment/ww1_early_carriers.txt")
