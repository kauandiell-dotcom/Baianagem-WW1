# scripts/fix_world_navies.py
import re
import os

COUNTRY_FILES = [
    'history/countries/AUS - Austria.txt',
    'history/countries/ENG - Britain.txt',
    'history/countries/FRA - France.txt',
    'history/countries/GER - Germany.txt',
    'history/countries/ITA - Italy.txt',
    'history/countries/JAP - Japan.txt',
    'history/countries/SOV - Soviet union.txt',
    'history/countries/TUR - Turkey.txt',
    'history/countries/USA - USA.txt',
]

MODULE_BLOCKS = {
    'ww1_1911_ironclad': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_heavy_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_old_heavy
\t\t\tfixed_ship_armor_slot = ww1_1911_old_belt
\t\t\tfixed_ship_secondaries_slot = ww1_1911_secondary_battery
\t\t}
''',
    'ww1_1911_pre_dreadnought': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_heavy_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_mixed_heavy
\t\t\tfixed_ship_armor_slot = ww1_1911_pre_belt
\t\t\tfixed_ship_secondaries_slot = ww1_1911_secondary_battery
\t\t\tmid_1_custom_slot = ww1_1911_secondary_battery
\t\t}
''',
    'ww1_1911_dreadnought': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_heavy_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_uniform_heavy
\t\t\tfixed_ship_armor_slot = ww1_1911_dread_belt
\t\t\tfixed_ship_secondaries_slot = ww1_1911_secondary_battery
\t\t\tmid_1_custom_slot = ww1_1911_secondary_battery
\t\t\trear_1_custom_slot = ww1_1911_uniform_heavy
\t\t}
''',
    'ww1_1911_battlecruiser': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_heavy_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_uniform_heavy
\t\t\tfixed_ship_armor_slot = ww1_1911_battlecruiser_belt
\t\t\tfixed_ship_secondaries_slot = ww1_1911_secondary_battery
\t\t\tmid_1_custom_slot = ww1_1911_secondary_battery
\t\t\trear_1_custom_slot = ww1_1911_uniform_heavy
\t\t}
''',
    'ww1_1911_armoured_cruiser': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_cruiser_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_medium
\t\t\tfixed_ship_armor_slot = ww1_1911_cruiser_belt
\t\t\tfixed_ship_secondaries_slot = ww1_1911_secondary_battery
\t\t\trear_1_custom_slot = ww1_1911_medium
\t\t}
''',
    'ww1_1911_protected_cruiser': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_cruiser_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_light_medium
\t\t\tfixed_ship_armor_slot = ww1_1911_protected_deck
\t\t\tmid_1_custom_slot = ww1_1911_torpedoes
\t\t}
''',
    'ww1_1911_torpedo_craft': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_light_coal
\t\t\tfixed_ship_battery_slot = ww1_1911_light
\t\t\tfixed_ship_torpedo_slot = ww1_1911_torpedoes
\t\t\tmid_1_custom_slot = ww1_1911_torpedoes
\t\t}
''',
    'ww1_1911_submarine': '''\t\tmodules = {
\t\t\tfixed_ship_engine_slot = ww1_1911_sub_engine
\t\t\tfixed_ship_torpedo_slot = ww1_1911_sub_torpedoes
\t\t}
'''
}

def fix_variants_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Find each create_equipment_variant block
    # Pattern to match create_equipment_variant = { ... }
    # We parse blocks by matching braces
    idx = 0
    new_text_parts = []
    total_fixed = 0

    while idx < len(text):
        m = re.search(r'\bcreate_equipment_variant\s*=\s*\{', text[idx:])
        if not m:
            new_text_parts.append(text[idx:])
            break
        
        start_pos = idx + m.start()
        open_pos = idx + m.end() - 1 # position of '{'
        
        # Add everything before this block
        new_text_parts.append(text[idx:start_pos])

        # Find matching closing brace
        depth = 1
        pos = open_pos + 1
        while pos < len(text) and depth > 0:
            if text[pos] == '{':
                depth += 1
            elif text[pos] == '}':
                depth -= 1
            pos += 1
        
        block = text[start_pos:pos]
        idx = pos

        # Check if this is a ww1_1911 MTG variant without modules
        m_type = re.search(r'\btype\s*=\s*(ww1_1911_\w+)', block)
        if m_type and not m_type.group(1).endswith('_legacy') and 'modules' not in block:
            hull_type = m_type.group(1)
            if hull_type in MODULE_BLOCKS:
                # Insert modules before closing brace
                # Find last '}'
                last_brace_idx = block.rfind('}')
                # Check indentation before last brace
                prefix = block[:last_brace_idx]
                suffix = block[last_brace_idx:]
                
                # Make sure prefix ends with newline
                if not prefix.endswith('\n'):
                    prefix += '\n'
                
                mod_code = MODULE_BLOCKS[hull_type]
                block = prefix + mod_code + '\t}'
                total_fixed += 1

        new_text_parts.append(block)

    updated_content = ''.join(new_text_parts)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Fixed {total_fixed} variants in {filepath}")
    return total_fixed

def main():
    grand_total = 0
    for cf in COUNTRY_FILES:
        grand_total += fix_variants_in_file(cf)
    print(f"\n==========================================")
    print(f"GRAND TOTAL VARIANTS ARMED WITH MODULES: {grand_total}")
    print(f"==========================================")

if __name__ == '__main__':
    main()
