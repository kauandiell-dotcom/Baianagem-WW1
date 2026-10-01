import os

dest_dir = r"gfx/interface/goals"
gfx_file = r"interface/ww1_germany_goals.gfx"

with open(gfx_file, "r", encoding="utf-8", errors="ignore") as f:
    gfx_content = f.read()

new_files = [
    'GER_Reichstag.png', 'GER_Deutsches_Heer.png', 'GER_Kaiserliche_Marine.png',
    'GER_Deutsche_Luftstreitkrafte.png', 'GER_Deutsche_Luftflotte.png', 'GER_Krupp_Artillery.png',
    'GER_Sturmtruppen.png', 'GER_red_baron.png', 'GER_German_Pilots.png',
    'GER_Empower_the_Reichsbank.png', 'GER_mitteleuropa.png', 'GER_colonial_administration.png',
    'GER_SPD.png', 'GER_Zentrum.png', 'GER_Prussian_Zentrum.png', 'GER_DkP.png', 'GER_DVLP.png',
    'GER_Thyssen_Pact.png', 'GER_Ufa_War_Propaganda.png', 'GER_Winterhilfe.png',
    'GER_Binnenwirtschaft.png', 'GER_Rathenauplan.png', 'GER_Helfferichplan.png',
    'GER_Expand_Kriegsschule.png', 'GER_renewed_militarism.png', 'GER_rights_for_service.png',
    'GER_Freiwilliger_Arbeitsdienst.png', 'GER_our_continent.png', 'align_germany.png',
    'attack_germany.png', 'flag_germany.png', 'ENG_issue_gas_masks.png', 'doctrine_tank_warfare.png',
    'generic_german_construction.png', 'generic_air_CAS_german.png', 'generic_air_tactical_bomber_german.png',
    'z_goal_gas.dds', 'z_goal_return_power_wilhelm.dds', 'z_goal_german_red_army.dds',
    'z_goal_true_german_socialism.dds', 'z_goal_federalization_of_germany.dds',
    'z_goal_elections_to_reichstag.dds', 'z_goal_ger_sabmarine.dds', 'z_goal_german_vmf.dds',
    'z_goal_german_air_force.dds', 'z_goal_germany_air_bomber.dds',
    'z_goal_war_is_mother_of_german_statehood.dds', 'z_goal_unite_germans_under_one_roof.dds',
    'z_dangerous_laws.dds', 'z_focus_habsburg_great_german_way.dds',
    'focus_German_Crown.png', 'focus_ger_kaiserreich.png', 'focus_GER_army_officer.png',
    'focus_GER_navy_ww1.png', 'focus_GER_reichstag.png', 'focus_ger_weltpolitik_ww1.png',
    'focus_GER_zeppelin_company.png', 'focus_ger_support_austrian_claims.png',
    'focus_dreadnought_GER.png', 'focus_ger_romanian_pact.png'
]

new_entries = []
for fname in new_files:
    base = os.path.splitext(fname)[0]
    sprite_name = f"GFX_{base}"
    if f'"{sprite_name}"' not in gfx_content:
        entry = f"""\tSpriteType = {{
\t\tname = "{sprite_name}"
\t\ttexturefile = "gfx/interface/goals/{fname}"
\t}}
\tSpriteType = {{
\t\tname = "{sprite_name}_shine"
\t\ttexturefile = "gfx/interface/goals/{fname}"
\t\teffectFile = "gfx/FX/buttonstate.lua"
\t\tanimation = {{
\t\t\tanimationmaskfile = "gfx/interface/goals/{fname}"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"
\t\t\tanimationrotation = -90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}
\t\tanimation = {{
\t\t\tanimationmaskfile = "gfx/interface/goals/{fname}"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"
\t\t\tanimationrotation = 90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}
\t}}
"""
        new_entries.append(entry)

print(f"Generated {len(new_entries)} new spriteType blocks.")

last_brace = gfx_content.rfind("}")
if last_brace != -1 and new_entries:
    updated_content = gfx_content[:last_brace] + "\n\t### NEW WW1 KAISERREICH / EUROPE IN FLAMES SPRITES\n" + "".join(new_entries) + "\n}\n"
    with open(gfx_file, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Successfully updated ww1_germany_goals.gfx!")
