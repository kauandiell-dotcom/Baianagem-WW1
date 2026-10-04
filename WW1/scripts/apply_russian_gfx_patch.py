import re

mapping = {
    'GFX_focus_RUS_stolypin': 'RUS_Stolypin.png',
    'GFX_focus_RUS_stolypin_shot': 'GFX_SOV_dissolve_the_duma-45146.dds',
    'GFX_focus_RUS_stolypin_dead': 'focus_rus_resist_the_duma.png',
    'GFX_focus_RUS_kokovtsov': 'GFX_SOV_address_economic_stagnation-45112.dds',
    'GFX_focus_RUS_elderly_minister': 'GFX_SOV_reformation_of_the_empire-45115.dds',
    'GFX_focus_RUS_rasputin': 'GFX_SOV_investigations_into_grigori_rasputin-45142.dds',
    'GFX_focus_RUS_stolypin_victory': 'GFX_SOV_stolypins_land_reform-45113.dds',
    'GFX_focus_RUS_duma_compromise': 'focus_rus_loyal_duma.png',
    'GFX_focus_RUS_iron_hand': 'focus_rus_resist_the_duma.png',
    'GFX_focus_RUS_guchkov': 'GFX_SOV_war_industries_committees-45150.dds',
    'GFX_focus_RUS_milyukov': 'RUS_An_Example_Of_Liberal_Democracy.png',
    'GFX_focus_RUS_progressive_bloc': 'GFX_SOV_emergency_fourth_state_duma_meetings-45137.dds',
    'GFX_focus_RUS_rodzianko_speech': 'focus_rus_duma_elections.png',
    'GFX_focus_RUS_rasputin_murder': 'GFX_SOV_investigations_into_grigori_rasputin-45142.dds',
    'GFX_focus_RUS_bread_riots': 'RUS_Combat_Army_Mutiny.png',
    'GFX_focus_RUS_garrison_mutiny': 'RUS_Combat_Army_Mutiny.png',
    'GFX_focus_RUS_tsar_abdication': 'GFX_SOV_limit_tsar_influence-45140.dds',
    'GFX_focus_RUS_provisional_gov': 'focus_RUS_duma.png',
    'GFX_focus_RUS_lvov_cabinet': 'SOV_taurida_palace.dds',
    'GFX_focus_RUS_kerensky_speech': 'GFX_SOV_strengthen_third_state_duma-45137.dds',
    'GFX_focus_SOV_july_days': 'focus_SOV_the_path_of_marxism_leninism.dds',
    'GFX_focus_RUS_kornilov': 'focus_RUS_Kaledin_Alekseev_Kornilov_triumvirate.png',
    'GFX_focus_SOV_storming_winter_palace': 'SOV_taurida_palace.dds',
    'GFX_focus_SOV_decree_peace': 'SOV_Peace_Commisar.png',
    'GFX_focus_SOV_decree_land': 'focus_SOV_first_decrees.png',
    'GFX_focus_RUS_firing_squad': 'RUS_Ingraining_Combat_Squads.png',
    'GFX_focus_RUS_democratic_coat_of_arms': 'RUS_An_Example_Of_Liberal_Democracy.png',
    'GFX_focus_RUS_federal_autonomy': 'GFX_SOV_free_political_prisoners-45148.dds',
    'GFX_focus_RUS_citizens_army': 'focus_rus_volunteer_army.png',
    'GFX_focus_RUS_victory_cross': 'ww1_nationalfocus_orthodoxy_triumphant.png',
    'GFX_focus_RUS_tsar_resolute': 'GFX_SOV_tsar_supremacy-45134.dds',
    'GFX_focus_RUS_imperial_eagle': 'RUS_Imperial_Benevolence.png',
    'GFX_focus_RUS_putilov': 'focus_RUS_Garford_Putilov_armoured_car.png',
    'GFX_focus_RUS_murmansk_rail': 'RUS_Privatize_Railroad.png',
    'GFX_focus_RUS_sikorsky_bomber': 'GFX_SOV_main_directorate_of_the_general_staff-45127.dds',
    'GFX_focus_RUS_grand_duke': 'GFX_SOV_promote_competent_generals-45143.dds',
    'GFX_focus_RUS_shell_famine': 'BRY_Every_Hand_A_Rifle.png',
    'GFX_focus_RUS_great_retreat': 'GFX_SOV_address_economic_stagnation-45112.dds',
    'GFX_SOV_tula_arms_plant-45144': 'GFX_SOV_tula_arms_plant-45144.dds',
    'GFX_focus_RUS_zelinsky_mask': 'ww1_nationalfocus_gasmask.dds',
    'GFX_focus_RUS_brusilov': 'GFX_SOV_promote_competent_generals-45143.dds',
    'GFX_focus_RUS_shock_battalion': 'GFX_AUS_german_empire_shock_trooper_tactiics-46526.dds',
    'GFX_focus_RUS_womens_battalion': 'GER_womens_rights_and_equality.dds',
    'GFX_focus_RUS_serbia_shield': 'GFX_SOV_support_serbia-45156.dds',
    'GFX_focus_RUS_mobilization_order': 'GFX_SOV_increased_military_budget-45119.dds',
    'GFX_focus_RUS_france_alliance': 'GFX_FRA_investment_in_russia-45149.dds',
    'GFX_focus_RUS_army': 'GFX_SOV_army_reform-45143.dds',
    'GFX_focus_RUS_orthodox_cross': 'GFX_SOV_orthodox_brotherhood-45155.dds',
    'GFX_focus_RUS_aid_serbia': 'GFX_SOV_support_serbia-45156.dds'
}

with open('interface/ww1_russia_goals.gfx', 'r', encoding='utf-8') as f:
    content = f.read()

updated = 0
for sprite_name, target_file in mapping.items():
    new_tex = f"gfx/interface/goals/{target_file}"
    shine_name = f"{sprite_name}_shine"
    
    # 1. Replace base sprite block:
    # SpriteType = {\n\tname = "sprite_name"\n\ttexturefile = "..."\n}
    pattern_base = rf'(SpriteType\s*=\s*\{{\s*name\s*=\s*"{re.escape(sprite_name)}"\s*\n\s*texturefile\s*=\s*")[^"]+("\s*\n\s*\}})'
    if re.search(pattern_base, content, re.IGNORECASE):
        content = re.sub(pattern_base, rf'\g<1>{new_tex}\g<2>', content, count=1, flags=re.IGNORECASE)
        updated += 1
    
    # 2. Replace shine sprite block:
    # We want to replace texturefile and animationmaskfile inside the shine sprite for sprite_name_shine
    pattern_shine = rf'(SpriteType\s*=\s*\{{\s*name\s*=\s*"{re.escape(shine_name)}"[^}}]*?\}}\s*\}})'
    # Alternatively find the block directly
    shine_match = re.search(rf'SpriteType\s*=\s*\{{\s*name\s*=\s*"{re.escape(shine_name)}".*?legacy_lazy_load\s*=\s*no\s*\n\s*\}}', content, re.DOTALL | re.IGNORECASE)
    if shine_match:
        old_block = shine_match.group(0)
        new_block = re.sub(r'texturefile\s*=\s*"[^"]+"', f'texturefile = "{new_tex}"', old_block, count=1)
        new_block = re.sub(r'animationmaskfile\s*=\s*"[^"]+"', f'animationmaskfile = "{new_tex}"', new_block)
        content = content.replace(old_block, new_block)

with open('interface/ww1_russia_goals.gfx', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated {updated} base Russian sprites and their shine animations in ww1_russia_goals.gfx!")
