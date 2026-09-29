import os
from pathlib import Path

repo_root = Path(r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1")
gfx_tech_dir = repo_root / "gfx" / "interface" / "technologies"
interface_dir = repo_root / "interface"

# 1. First, fix all 0-byte .gfx files to have clean spriteTypes = {}
zero_byte_files = [
    "aap_technologies.gfx", "aat_technologies.gfx", "atp_technologies.gfx",
    "bftb_technologies.gfx", "dod_technologies.gfx", "efpp_technologies.gfx",
    "lar_technologies.gfx", "mtg_technologies.gfx", "nsb_technologies.gfx",
    "pol_technologies.gfx", "tfv_technologies.gfx", "toa_technologies.gfx",
    "wtt_technologies.gfx"
]

for filename in zero_byte_files:
    file_path = interface_dir / filename
    if file_path.exists() and file_path.stat().st_size == 0:
        file_path.write_text("spriteTypes = {\n}\n", encoding="utf-8")
        print(f"Fixed empty .gfx file: {filename}")

# 2. Build exhaustive mapping dictionary: sprite_name -> relative_path
sprites = {}

def add_sprite(name, rel_path):
    # Verify file existence on disk
    full_path = repo_root / rel_path.replace("/", "\\")
    if not full_path.exists():
        # Fallback check
        alt_rel = rel_path.replace(".dds", ".png")
        if (repo_root / alt_rel.replace("/", "\\")).exists():
            rel_path = alt_rel
        else:
            alt_rel2 = rel_path.replace(".png", ".dds")
            if (repo_root / alt_rel2.replace("/", "\\")).exists():
                rel_path = alt_rel2
            else:
                print(f"WARNING: Texture not found: {rel_path} for sprite {name}")
                return
    sprites[name] = rel_path

### ARCHETYPES (CRITICAL FALLBACK FOR PRODUCTION & DESIGNERS) ###
add_sprite("GFX_archetype_infantry_equipment_medium", "gfx/interface/technologies/infantry_equipment_0.dds")
add_sprite("GFX_archetype_artillery_equipment_medium", "gfx/interface/technologies/artillery1.dds")
add_sprite("GFX_archetype_anti_tank_equipment_medium", "gfx/interface/technologies/AT_1.png")
add_sprite("GFX_archetype_anti_air_equipment_medium", "gfx/interface/technologies/AA_1.png")
add_sprite("GFX_archetype_rocket_artillery_equipment_medium", "gfx/interface/technologies/artillery2.dds")
add_sprite("GFX_archetype_light_tank_equipment_medium", "gfx/interface/technologies/basic_light_tank.dds")
add_sprite("GFX_archetype_medium_tank_equipment_medium", "gfx/interface/technologies/basic_medium_tank.dds")
add_sprite("GFX_archetype_heavy_tank_equipment_medium", "gfx/interface/technologies/basic_heavy_tank.dds")
add_sprite("GFX_archetype_super_heavy_tank_equipment_medium", "gfx/interface/technologies/GER/GER_ww1_super_heavy_tank.png")
add_sprite("GFX_archetype_armored_car_equipment_medium", "gfx/interface/technologies/basic_armored_car.png")
add_sprite("GFX_archetype_fighter_equipment_medium", "gfx/interface/technologies/early_fighter.dds")
add_sprite("GFX_archetype_heavy_fighter_equipment_medium", "gfx/interface/technologies/fighter2.dds")
add_sprite("GFX_archetype_CAS_equipment_medium", "gfx/interface/technologies/early_bomber.dds")
add_sprite("GFX_archetype_tactical_bomber_equipment_medium", "gfx/interface/technologies/early_bomber.dds")
add_sprite("GFX_archetype_strat_bomber_equipment_medium", "gfx/interface/technologies/airship_bomber_1.png")
add_sprite("GFX_archetype_naval_bomber_equipment_medium", "gfx/interface/technologies/early_bomber.dds")
add_sprite("GFX_archetype_scout_plane_equipment_medium", "gfx/interface/technologies/early_fighter.dds")
add_sprite("GFX_archetype_small_plane_airframe_medium", "gfx/interface/technologies/early_fighter.dds")
add_sprite("GFX_archetype_medium_plane_airframe_medium", "gfx/interface/technologies/early_bomber.dds")
add_sprite("GFX_archetype_large_plane_airframe_medium", "gfx/interface/technologies/airship_bomber_1.png")
add_sprite("GFX_archetype_destroyer_equipment_medium", "gfx/interface/technologies/early_destroyer.dds")
add_sprite("GFX_archetype_light_cruiser_equipment_medium", "gfx/interface/technologies/early_light_cruiser.dds")
add_sprite("GFX_archetype_heavy_cruiser_equipment_medium", "gfx/interface/technologies/early_heavy_cruiser.dds")
add_sprite("GFX_archetype_battleship_equipment_medium", "gfx/interface/technologies/early_battleship.dds")
add_sprite("GFX_archetype_battle_cruiser_equipment_medium", "gfx/interface/technologies/early_battlecruiser.dds")
add_sprite("GFX_archetype_submarine_equipment_medium", "gfx/interface/technologies/early_submarine.dds")
add_sprite("GFX_archetype_carrier_equipment_medium", "gfx/interface/technologies/early_carrier.dds")

### GENERIC INFANTRY & SUPPORT ###
inf_map = [
    ("GFX_infantry_weapons_medium", "gfx/interface/technologies/infantry_equipment_0.dds"),
    ("GFX_infantry_weapons1_medium", "gfx/interface/technologies/infantry1.dds"),
    ("GFX_infantry_weapons2_medium", "gfx/interface/technologies/infantry2.dds"),
    ("GFX_improved_infantry_weapons_medium", "gfx/interface/technologies/infantry2.dds"),
    ("GFX_improved_infantry_weapons_2_medium", "gfx/interface/technologies/infantry3.dds"),
    ("GFX_advanced_infantry_weapons_medium", "gfx/interface/technologies/infantry3.dds"),
    ("GFX_infantry1_medium", "gfx/interface/technologies/infantry1.dds"),
    ("GFX_infantry2_medium", "gfx/interface/technologies/infantry2.dds"),
    ("GFX_infantry3_medium", "gfx/interface/technologies/infantry3.dds"),
    ("GFX_infantry_equipment_0_medium", "gfx/interface/technologies/infantry_equipment_0.dds"),
    ("GFX_infantry_equipment_1_medium", "gfx/interface/technologies/infantry1.dds"),
    ("GFX_infantry_equipment_2_medium", "gfx/interface/technologies/infantry2.dds"),
    ("GFX_infantry_equipment_3_medium", "gfx/interface/technologies/infantry3.dds"),
    ("GFX_weapons4_medium", "gfx/interface/technologies/infantry3.dds"),
    ("GFX_support_weapons_medium", "gfx/interface/technologies/support_weapons.dds"),
    ("GFX_support_weapons2_medium", "gfx/interface/technologies/support_weapons2.dds"),
    ("GFX_support_weapons3_medium", "gfx/interface/technologies/support_weapons3.dds"),
    ("GFX_support_weapons4_medium", "gfx/interface/technologies/support_weapons4.dds"),
    ("GFX_tech_trucks_medium", "gfx/interface/technologies/GER/GER_ww1_armored_car_1.png"),
    ("GFX_motorised_infantry_medium", "gfx/interface/technologies/GER/GER_ww1_armored_car_1.png"),
    ("GFX_motorized_equipment_1_medium", "gfx/interface/technologies/GER/GER_ww1_armored_car_1.png"),
]
for k, v in inf_map:
    add_sprite(k, v)

### GENERIC ARTILLERY, AT, AA ###
arty_map = [
    ("GFX_gw_artillery_medium", "gfx/interface/technologies/artillery1.dds"),
    ("GFX_interwar_artillery_medium", "gfx/interface/technologies/artillery1.dds"),
    ("GFX_artillery1_medium", "gfx/interface/technologies/artillery1.dds"),
    ("GFX_artillery2_medium", "gfx/interface/technologies/artillery2.dds"),
    ("GFX_artillery3_medium", "gfx/interface/technologies/artillery3.dds"),
    ("GFX_artillery4_medium", "gfx/interface/technologies/artillery2.dds"),
    ("GFX_artillery5_medium", "gfx/interface/technologies/artillery3.dds"),
    ("GFX_artillery_equipment_1_medium", "gfx/interface/technologies/artillery1.dds"),
    ("GFX_artillery_equipment_2_medium", "gfx/interface/technologies/artillery2.dds"),
    ("GFX_artillery_equipment_3_medium", "gfx/interface/technologies/artillery3.dds"),
    ("GFX_interwar_antitank_medium", "gfx/interface/technologies/AT_1.png"),
    ("GFX_antitank1_medium", "gfx/interface/technologies/AT_1.png"),
    ("GFX_antitank2_medium", "gfx/interface/technologies/AT_2.png"),
    ("GFX_antitank3_medium", "gfx/interface/technologies/AT_3.png"),
    ("GFX_antitank4_medium", "gfx/interface/technologies/AT_3.png"),
    ("GFX_anti_tank_equipment_1_medium", "gfx/interface/technologies/AT_1.png"),
    ("GFX_anti_tank_equipment_2_medium", "gfx/interface/technologies/AT_2.png"),
    ("GFX_anti_tank_equipment_3_medium", "gfx/interface/technologies/AT_3.png"),
    ("GFX_interwar_antiair_medium", "gfx/interface/technologies/AA_1.png"),
    ("GFX_antiair1_medium", "gfx/interface/technologies/AA_1.png"),
    ("GFX_antiair2_medium", "gfx/interface/technologies/AA_2.png"),
    ("GFX_antiair3_medium", "gfx/interface/technologies/AA_3.png"),
    ("GFX_anti_air_equipment_1_medium", "gfx/interface/technologies/AA_1.png"),
    ("GFX_anti_air_equipment_2_medium", "gfx/interface/technologies/AA_2.png"),
    ("GFX_anti_air_equipment_3_medium", "gfx/interface/technologies/AA_3.png"),
    ("GFX_rocket_artillery_medium", "gfx/interface/technologies/artillery2.dds"),
    ("GFX_rocket_artillery2_medium", "gfx/interface/technologies/artillery2.dds"),
    ("GFX_rocket_artillery3_medium", "gfx/interface/technologies/artillery3.dds"),
    ("GFX_rocket_artillery4_medium", "gfx/interface/technologies/artillery3.dds"),
]
for k, v in arty_map:
    add_sprite(k, v)

### GENERIC TANKS & CHASSIS ###
tank_map = [
    ("GFX_gwtank_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_gwtank_chassis_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_basic_light_tank_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_basic_light_tank_chassis_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_improved_light_tank_medium", "gfx/interface/technologies/improved_light_tank.dds"),
    ("GFX_improved_light_tank_chassis_medium", "gfx/interface/technologies/improved_light_tank.dds"),
    ("GFX_advanced_light_tank_medium", "gfx/interface/technologies/advanced_light_tank.dds"),
    ("GFX_light_tank_chassis_0_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_light_tank_chassis_1_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_light_tank_chassis_2_medium", "gfx/interface/technologies/improved_light_tank.dds"),
    ("GFX_light_tank_chassis_3_medium", "gfx/interface/technologies/advanced_light_tank.dds"),
    ("GFX_light_tank_equipment_1_medium", "gfx/interface/technologies/basic_light_tank.dds"),
    ("GFX_light_tank_equipment_2_medium", "gfx/interface/technologies/improved_light_tank.dds"),
    ("GFX_light_tank_equipment_3_medium", "gfx/interface/technologies/advanced_light_tank.dds"),
    ("GFX_basic_medium_tank_medium", "gfx/interface/technologies/basic_medium_tank.dds"),
    ("GFX_basic_medium_tank_chassis_medium", "gfx/interface/technologies/basic_medium_tank.dds"),
    ("GFX_improved_medium_tank_medium", "gfx/interface/technologies/improved_medium_tank.dds"),
    ("GFX_improved_medium_tank_chassis_medium", "gfx/interface/technologies/improved_medium_tank.dds"),
    ("GFX_medium_tank_chassis_0_medium", "gfx/interface/technologies/basic_medium_tank.dds"),
    ("GFX_medium_tank_chassis_1_medium", "gfx/interface/technologies/basic_medium_tank.dds"),
    ("GFX_medium_tank_chassis_2_medium", "gfx/interface/technologies/improved_medium_tank.dds"),
    ("GFX_medium_tank_equipment_1_medium", "gfx/interface/technologies/basic_medium_tank.dds"),
    ("GFX_medium_tank_equipment_2_medium", "gfx/interface/technologies/improved_medium_tank.dds"),
    ("GFX_basic_heavy_tank_medium", "gfx/interface/technologies/basic_heavy_tank.dds"),
    ("GFX_basic_heavy_tank_chassis_medium", "gfx/interface/technologies/basic_heavy_tank.dds"),
    ("GFX_improved_heavy_tank_medium", "gfx/interface/technologies/improved_heavy_tank.dds"),
    ("GFX_improved_heavy_tank_chassis_medium", "gfx/interface/technologies/improved_heavy_tank.dds"),
    ("GFX_heavy_tank_chassis_0_medium", "gfx/interface/technologies/basic_heavy_tank.dds"),
    ("GFX_heavy_tank_chassis_1_medium", "gfx/interface/technologies/basic_heavy_tank.dds"),
    ("GFX_heavy_tank_chassis_2_medium", "gfx/interface/technologies/improved_heavy_tank.dds"),
    ("GFX_heavy_tank_equipment_1_medium", "gfx/interface/technologies/basic_heavy_tank.dds"),
    ("GFX_super_heavy_tank_chassis_0_medium", "gfx/interface/technologies/GER/GER_ww1_super_heavy_tank.png"),
    ("GFX_super_heavy_tank_chassis_medium", "gfx/interface/technologies/GER/GER_ww1_super_heavy_tank.png"),
    ("GFX_super_heavy_tank_equipment_1_medium", "gfx/interface/technologies/GER/GER_ww1_super_heavy_tank.png"),
    ("GFX_armored_car1_medium", "gfx/interface/technologies/basic_armored_car.png"),
    ("GFX_armored_car2_medium", "gfx/interface/technologies/advanced_armored_car.png"),
    ("GFX_armored_car_equipment_1_medium", "gfx/interface/technologies/basic_armored_car.png"),
    ("GFX_armored_car_equipment_2_medium", "gfx/interface/technologies/advanced_armored_car.png"),
]
for k, v in tank_map:
    add_sprite(k, v)

### GENERIC AIRCRAFT & AIRFRAMES ###
air_map = [
    ("GFX_early_fighter_medium", "gfx/interface/technologies/early_fighter.dds"),
    ("GFX_fighter1_medium", "gfx/interface/technologies/fighter1.dds"),
    ("GFX_fighter2_medium", "gfx/interface/technologies/fighter2.dds"),
    ("GFX_fighter3_medium", "gfx/interface/technologies/fighter3.dds"),
    ("GFX_fighter_equipment_0_medium", "gfx/interface/technologies/early_fighter.dds"),
    ("GFX_fighter_equipment_1_medium", "gfx/interface/technologies/fighter1.dds"),
    ("GFX_fighter_equipment_2_medium", "gfx/interface/technologies/fighter2.dds"),
    ("GFX_cv_early_fighter_medium", "gfx/interface/technologies/early_fighter.dds"),
    ("GFX_cv_fighter1_medium", "gfx/interface/technologies/fighter1.dds"),
    ("GFX_early_bomber_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_tactical_bomber1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_tactical_bomber2_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_tactical_bomber_equipment_0_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_tactical_bomber_equipment_1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_strategic_bomber1_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_strat_bomber_equipment_1_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_naval_bomber1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_naval_bomber_equipment_1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_CAS1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_CAS_equipment_1_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_heavy_fighter1_medium", "gfx/interface/technologies/fighter2.dds"),
    ("GFX_iw_small_airframe_medium", "gfx/interface/technologies/early_fighter.dds"),
    ("GFX_basic_small_airframe_medium", "gfx/interface/technologies/fighter1.dds"),
    ("GFX_small_plane_airframe_0_medium", "gfx/interface/technologies/early_fighter.dds"),
    ("GFX_small_plane_airframe_1_medium", "gfx/interface/technologies/fighter1.dds"),
    ("GFX_small_plane_airframe_2_medium", "gfx/interface/technologies/fighter2.dds"),
    ("GFX_iw_medium_airframe_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_basic_medium_airframe_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_medium_plane_airframe_0_medium", "gfx/interface/technologies/early_bomber.dds"),
    ("GFX_medium_plane_airframe_1_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_iw_large_airframe_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_basic_large_airframe_medium", "gfx/interface/technologies/airship_bomber_2.png"),
    ("GFX_large_plane_airframe_0_medium", "gfx/interface/technologies/airship_bomber_1.png"),
    ("GFX_large_plane_airframe_1_medium", "gfx/interface/technologies/airship_bomber_2.png"),
    ("GFX_scout_plane1_medium", "gfx/interface/technologies/early_fighter.dds"),
]
for k, v in air_map:
    add_sprite(k, v)

### GENERIC NAVAL & HULLS ###
nav_map = [
    ("GFX_early_destroyer_medium", "gfx/interface/technologies/early_destroyer.dds"),
    ("GFX_basic_destroyer_medium", "gfx/interface/technologies/basic_destroyer.dds"),
    ("GFX_destroyer_1_medium", "gfx/interface/technologies/early_destroyer.dds"),
    ("GFX_destroyer_2_medium", "gfx/interface/technologies/basic_destroyer.dds"),
    ("GFX_early_light_cruiser_medium", "gfx/interface/technologies/early_light_cruiser.dds"),
    ("GFX_basic_light_cruiser_medium", "gfx/interface/technologies/basic_light_cruiser.dds"),
    ("GFX_light_cruiser_1_medium", "gfx/interface/technologies/early_light_cruiser.dds"),
    ("GFX_light_cruiser_2_medium", "gfx/interface/technologies/basic_light_cruiser.dds"),
    ("GFX_early_heavy_cruiser_medium", "gfx/interface/technologies/early_heavy_cruiser.dds"),
    ("GFX_basic_heavy_cruiser_medium", "gfx/interface/technologies/basic_heavy_cruiser.dds"),
    ("GFX_heavy_cruiser_1_medium", "gfx/interface/technologies/early_heavy_cruiser.dds"),
    ("GFX_heavy_cruiser_2_medium", "gfx/interface/technologies/basic_heavy_cruiser.dds"),
    ("GFX_early_battlecruiser_medium", "gfx/interface/technologies/early_battlecruiser.dds"),
    ("GFX_basic_battlecruiser_medium", "gfx/interface/technologies/basic_battlecruiser.dds"),
    ("GFX_battlecruiser_1_medium", "gfx/interface/technologies/early_battlecruiser.dds"),
    ("GFX_early_battleship_medium", "gfx/interface/technologies/early_battleship.dds"),
    ("GFX_basic_battleship_medium", "gfx/interface/technologies/basic_battleship.dds"),
    ("GFX_battleship_1_medium", "gfx/interface/technologies/early_battleship.dds"),
    ("GFX_battleship_2_medium", "gfx/interface/technologies/basic_battleship.dds"),
    ("GFX_early_submarine_medium", "gfx/interface/technologies/early_submarine.dds"),
    ("GFX_basic_submarine_medium", "gfx/interface/technologies/basic_submarine.dds"),
    ("GFX_submarine_1_medium", "gfx/interface/technologies/early_submarine.dds"),
    ("GFX_submarine_2_medium", "gfx/interface/technologies/basic_submarine.dds"),
    ("GFX_early_carrier_medium", "gfx/interface/technologies/early_carrier.dds"),
    ("GFX_basic_carrier_medium", "gfx/interface/technologies/basic_carrier.dds"),
    ("GFX_carrier_1_medium", "gfx/interface/technologies/early_carrier.dds"),
    ("GFX_early_ship_hull_light_medium", "gfx/interface/technologies/early_destroyer.dds"),
    ("GFX_basic_ship_hull_light_medium", "gfx/interface/technologies/basic_destroyer.dds"),
    ("GFX_ship_hull_light_1_medium", "gfx/interface/technologies/early_destroyer.dds"),
    ("GFX_ship_hull_light_2_medium", "gfx/interface/technologies/basic_destroyer.dds"),
    ("GFX_early_ship_hull_cruiser_medium", "gfx/interface/technologies/early_light_cruiser.dds"),
    ("GFX_basic_ship_hull_cruiser_medium", "gfx/interface/technologies/basic_light_cruiser.dds"),
    ("GFX_ship_hull_cruiser_1_medium", "gfx/interface/technologies/early_light_cruiser.dds"),
    ("GFX_ship_hull_cruiser_2_medium", "gfx/interface/technologies/basic_light_cruiser.dds"),
    ("GFX_early_ship_hull_heavy_medium", "gfx/interface/technologies/early_battleship.dds"),
    ("GFX_basic_ship_hull_heavy_medium", "gfx/interface/technologies/basic_battleship.dds"),
    ("GFX_ship_hull_heavy_1_medium", "gfx/interface/technologies/early_battleship.dds"),
    ("GFX_ship_hull_heavy_2_medium", "gfx/interface/technologies/basic_battleship.dds"),
    ("GFX_early_ship_hull_submarine_medium", "gfx/interface/technologies/early_submarine.dds"),
    ("GFX_basic_ship_hull_submarine_medium", "gfx/interface/technologies/basic_submarine.dds"),
    ("GFX_ship_hull_submarine_1_medium", "gfx/interface/technologies/early_submarine.dds"),
    ("GFX_ship_hull_submarine_2_medium", "gfx/interface/technologies/basic_submarine.dds"),
    ("GFX_early_ship_hull_carrier_medium", "gfx/interface/technologies/early_carrier.dds"),
    ("GFX_basic_ship_hull_carrier_medium", "gfx/interface/technologies/basic_carrier.dds"),
    ("GFX_ship_hull_carrier_1_medium", "gfx/interface/technologies/early_carrier.dds"),
]
for k, v in nav_map:
    add_sprite(k, v)

### NATION SPECIFIC CONFIGURATIONS ###

def configure_nation(tag, folder_tag=None):
    ftag = folder_tag or tag
    fdir = gfx_tech_dir / ftag
    if not fdir.exists():
        return

    # 1. Infantry Weapons
    # Look for {ftag}_infantry_equipment_0..3
    eq0 = f"gfx/interface/technologies/{ftag}/{ftag}_infantry_equipment_0.png"
    eq1 = f"gfx/interface/technologies/{ftag}/{ftag}_infantry_equipment_1.png"
    eq2 = f"gfx/interface/technologies/{ftag}/{ftag}_infantry_equipment_2.png"
    eq3 = f"gfx/interface/technologies/{ftag}/{ftag}_infantry_equipment_3.png"

    # Fallback to general if specific doesn't exist
    if not (repo_root / eq0.replace("/", "\\")).exists():
        eq0 = "gfx/interface/technologies/infantry_equipment_0.dds"
    if not (repo_root / eq1.replace("/", "\\")).exists():
        eq1 = eq0
    if not (repo_root / eq2.replace("/", "\\")).exists():
        eq2 = eq1
    if not (repo_root / eq3.replace("/", "\\")).exists():
        eq3 = eq2

    # Map BOTH tech names AND equipment names AND vanilla numeric names!
    add_sprite(f"GFX_{tag}_infantry_weapons_medium", eq0)
    add_sprite(f"GFX_{tag}_infantry_weapons1_medium", eq1)
    add_sprite(f"GFX_{tag}_infantry_weapons2_medium", eq2)
    add_sprite(f"GFX_{tag}_improved_infantry_weapons_medium", eq2)
    add_sprite(f"GFX_{tag}_improved_infantry_weapons_2_medium", eq3)
    add_sprite(f"GFX_{tag}_advanced_infantry_weapons_medium", eq3)

    add_sprite(f"GFX_{tag}_infantry1_medium", eq1)
    add_sprite(f"GFX_{tag}_infantry2_medium", eq2)
    add_sprite(f"GFX_{tag}_infantry3_medium", eq3)

    add_sprite(f"GFX_{tag}_infantry_equipment_0_medium", eq0)
    add_sprite(f"GFX_{tag}_infantry_equipment_1_medium", eq1)
    add_sprite(f"GFX_{tag}_infantry_equipment_2_medium", eq2)
    add_sprite(f"GFX_{tag}_infantry_equipment_3_medium", eq3)

    # 2. Artillery / Field Gun
    fg1 = f"gfx/interface/technologies/{ftag}/{ftag}_field_gun_1.png"
    fg2 = f"gfx/interface/technologies/{ftag}/{ftag}_field_gun_2.png"
    fg3 = f"gfx/interface/technologies/{ftag}/{ftag}_field_gun_3.png"
    if not (repo_root / fg1.replace("/", "\\")).exists():
        fg1 = "gfx/interface/technologies/artillery1.dds"
    if not (repo_root / fg2.replace("/", "\\")).exists():
        fg2 = fg1
    if not (repo_root / fg3.replace("/", "\\")).exists():
        fg3 = fg2

    add_sprite(f"GFX_{tag}_gw_artillery_medium", fg1)
    add_sprite(f"GFX_{tag}_interwar_artillery_medium", fg1)
    add_sprite(f"GFX_{tag}_artillery1_medium", fg1)
    add_sprite(f"GFX_{tag}_artillery2_medium", fg2)
    add_sprite(f"GFX_{tag}_artillery4_medium", fg2)
    add_sprite(f"GFX_{tag}_artillery5_medium", fg3)
    add_sprite(f"GFX_{tag}_artillery_equipment_1_medium", fg1)
    add_sprite(f"GFX_{tag}_artillery_equipment_2_medium", fg2)
    add_sprite(f"GFX_{tag}_artillery_equipment_3_medium", fg3)

    # 3. Tanks
    lt1 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_light_tank_1.png"
    lt2 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_light_tank_2.png"
    lt3 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_light_tank_3.png"
    mt1 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_medium_tank_1.png"
    mt2 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_medium_tank_2.png"
    ht1 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_heavy_tank_1.png"
    ht2 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_heavy_tank_2.png"
    sht = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_super_heavy_tank.png"

    # fallbacks
    if not (repo_root / lt1.replace("/", "\\")).exists():
        lt1 = "gfx/interface/technologies/basic_light_tank.dds"
    if not (repo_root / lt2.replace("/", "\\")).exists():
        lt2 = lt1
    if not (repo_root / lt3.replace("/", "\\")).exists():
        lt3 = lt2

    if not (repo_root / mt1.replace("/", "\\")).exists():
        mt1 = "gfx/interface/technologies/basic_medium_tank.dds"
    if not (repo_root / mt2.replace("/", "\\")).exists():
        mt2 = mt1

    if not (repo_root / ht1.replace("/", "\\")).exists():
        ht1 = "gfx/interface/technologies/basic_heavy_tank.dds"
    if not (repo_root / ht2.replace("/", "\\")).exists():
        ht2 = ht1

    if not (repo_root / sht.replace("/", "\\")).exists():
        sht = "gfx/interface/technologies/GER/GER_ww1_super_heavy_tank.png"

    add_sprite(f"GFX_{tag}_gwtank_medium", lt1)
    add_sprite(f"GFX_{tag}_gwtank_chassis_medium", lt1)
    add_sprite(f"GFX_{tag}_basic_light_tank_medium", lt1)
    add_sprite(f"GFX_{tag}_basic_light_tank_chassis_medium", lt1)
    add_sprite(f"GFX_{tag}_improved_light_tank_medium", lt2)
    add_sprite(f"GFX_{tag}_improved_light_tank_chassis_medium", lt2)
    add_sprite(f"GFX_{tag}_light_tank_chassis_0_medium", lt1)
    add_sprite(f"GFX_{tag}_light_tank_chassis_1_medium", lt1)
    add_sprite(f"GFX_{tag}_light_tank_chassis_2_medium", lt2)
    add_sprite(f"GFX_{tag}_light_tank_equipment_1_medium", lt1)
    add_sprite(f"GFX_{tag}_light_tank_equipment_2_medium", lt2)

    add_sprite(f"GFX_{tag}_basic_medium_tank_medium", mt1)
    add_sprite(f"GFX_{tag}_basic_medium_tank_chassis_medium", mt1)
    add_sprite(f"GFX_{tag}_improved_medium_tank_medium", mt2)
    add_sprite(f"GFX_{tag}_improved_medium_tank_chassis_medium", mt2)
    add_sprite(f"GFX_{tag}_medium_tank_chassis_0_medium", mt1)
    add_sprite(f"GFX_{tag}_medium_tank_chassis_1_medium", mt1)
    add_sprite(f"GFX_{tag}_medium_tank_chassis_2_medium", mt2)
    add_sprite(f"GFX_{tag}_medium_tank_equipment_1_medium", mt1)
    add_sprite(f"GFX_{tag}_medium_tank_equipment_2_medium", mt2)

    add_sprite(f"GFX_{tag}_basic_heavy_tank_medium", ht1)
    add_sprite(f"GFX_{tag}_basic_heavy_tank_chassis_medium", ht1)
    add_sprite(f"GFX_{tag}_improved_heavy_tank_medium", ht2)
    add_sprite(f"GFX_{tag}_improved_heavy_tank_chassis_medium", ht2)
    add_sprite(f"GFX_{tag}_heavy_tank_chassis_0_medium", ht1)
    add_sprite(f"GFX_{tag}_heavy_tank_chassis_1_medium", ht1)
    add_sprite(f"GFX_{tag}_heavy_tank_chassis_2_medium", ht2)
    add_sprite(f"GFX_{tag}_heavy_tank_equipment_1_medium", ht1)

    add_sprite(f"GFX_{tag}_super_heavy_tank_chassis_0_medium", sht)
    add_sprite(f"GFX_{tag}_super_heavy_tank_chassis_medium", sht)
    add_sprite(f"GFX_{tag}_super_heavy_tank_equipment_1_medium", sht)

    # Armored Cars
    ac1 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_armored_car_1.png"
    ac2 = f"gfx/interface/technologies/{ftag}/{ftag}_ww1_armored_car_2.png"
    if not (repo_root / ac1.replace("/", "\\")).exists():
        ac1 = "gfx/interface/technologies/basic_armored_car.png"
    if not (repo_root / ac2.replace("/", "\\")).exists():
        ac2 = ac1
    add_sprite(f"GFX_{tag}_armored_car1_medium", ac1)
    add_sprite(f"GFX_{tag}_armored_car2_medium", ac2)
    add_sprite(f"GFX_{tag}_armored_car_equipment_1_medium", ac1)
    add_sprite(f"GFX_{tag}_armored_car_equipment_2_medium", ac2)

    # 4. Aircraft
    f1 = f"gfx/interface/technologies/{ftag}/{ftag}_fighter1.png"
    if not (repo_root / f1.replace("/", "\\")).exists():
        f1 = f"gfx/interface/technologies/{ftag}/{ftag}_fighter2.png"
    if not (repo_root / f1.replace("/", "\\")).exists():
        f1 = "gfx/interface/technologies/early_fighter.dds"

    f2 = f"gfx/interface/technologies/{ftag}/{ftag}_fighter2.png"
    if not (repo_root / f2.replace("/", "\\")).exists():
        f2 = f"gfx/interface/technologies/{ftag}/{ftag}_fighter3.png"
    if not (repo_root / f2.replace("/", "\\")).exists():
        f2 = f1

    b1 = f"gfx/interface/technologies/{ftag}/{ftag}_light_bomber1.png"
    if not (repo_root / b1.replace("/", "\\")).exists():
        b1 = f"gfx/interface/technologies/{ftag}/{ftag}_heavy_bomber1.png"
    if not (repo_root / b1.replace("/", "\\")).exists():
        b1 = "gfx/interface/technologies/early_bomber.dds"

    sb1 = f"gfx/interface/technologies/{ftag}/{ftag}_airship_bomber1.png"
    if not (repo_root / sb1.replace("/", "\\")).exists():
        sb1 = f"gfx/interface/technologies/{ftag}/{ftag}_airship_1.png"
    if not (repo_root / sb1.replace("/", "\\")).exists():
        sb1 = "gfx/interface/technologies/airship_bomber_1.png"

    add_sprite(f"GFX_{tag}_early_fighter_medium", f1)
    add_sprite(f"GFX_{tag}_fighter1_medium", f1)
    add_sprite(f"GFX_{tag}_fighter2_medium", f2)
    add_sprite(f"GFX_{tag}_fighter_equipment_0_medium", f1)
    add_sprite(f"GFX_{tag}_fighter_equipment_1_medium", f1)
    add_sprite(f"GFX_{tag}_fighter_equipment_2_medium", f2)
    add_sprite(f"GFX_{tag}_cv_early_fighter_medium", f1)
    add_sprite(f"GFX_{tag}_cv_fighter1_medium", f1)

    add_sprite(f"GFX_{tag}_early_bomber_medium", b1)
    add_sprite(f"GFX_{tag}_tactical_bomber1_medium", b1)
    add_sprite(f"GFX_{tag}_tactical_bomber_equipment_0_medium", b1)
    add_sprite(f"GFX_{tag}_tactical_bomber_equipment_1_medium", b1)
    add_sprite(f"GFX_{tag}_strategic_bomber1_medium", sb1)
    add_sprite(f"GFX_{tag}_strat_bomber_equipment_1_medium", sb1)
    add_sprite(f"GFX_{tag}_naval_bomber1_medium", b1)
    add_sprite(f"GFX_{tag}_CAS1_medium", b1)
    add_sprite(f"GFX_{tag}_heavy_fighter1_medium", f2)

    add_sprite(f"GFX_{tag}_iw_small_airframe_medium", f1)
    add_sprite(f"GFX_{tag}_basic_small_airframe_medium", f1)
    add_sprite(f"GFX_{tag}_small_plane_airframe_0_medium", f1)
    add_sprite(f"GFX_{tag}_small_plane_airframe_1_medium", f1)
    add_sprite(f"GFX_{tag}_small_plane_airframe_2_medium", f2)
    add_sprite(f"GFX_{tag}_iw_medium_airframe_medium", b1)
    add_sprite(f"GFX_{tag}_basic_medium_airframe_medium", sb1)
    add_sprite(f"GFX_{tag}_medium_plane_airframe_0_medium", b1)
    add_sprite(f"GFX_{tag}_medium_plane_airframe_1_medium", sb1)
    add_sprite(f"GFX_{tag}_iw_large_airframe_medium", sb1)
    add_sprite(f"GFX_{tag}_basic_large_airframe_medium", sb1)

    # 5. Naval
    add_sprite(f"GFX_{tag}_early_destroyer_medium", "gfx/interface/technologies/early_destroyer.dds")
    add_sprite(f"GFX_{tag}_basic_destroyer_medium", "gfx/interface/technologies/basic_destroyer.dds")
    add_sprite(f"GFX_{tag}_destroyer_1_medium", "gfx/interface/technologies/early_destroyer.dds")
    add_sprite(f"GFX_{tag}_early_light_cruiser_medium", "gfx/interface/technologies/early_light_cruiser.dds")
    add_sprite(f"GFX_{tag}_basic_light_cruiser_medium", "gfx/interface/technologies/basic_light_cruiser.dds")
    add_sprite(f"GFX_{tag}_light_cruiser_1_medium", "gfx/interface/technologies/early_light_cruiser.dds")
    add_sprite(f"GFX_{tag}_early_heavy_cruiser_medium", "gfx/interface/technologies/early_heavy_cruiser.dds")
    add_sprite(f"GFX_{tag}_basic_heavy_cruiser_medium", "gfx/interface/technologies/basic_heavy_cruiser.dds")
    add_sprite(f"GFX_{tag}_heavy_cruiser_1_medium", "gfx/interface/technologies/early_heavy_cruiser.dds")
    add_sprite(f"GFX_{tag}_early_battleship_medium", "gfx/interface/technologies/early_battleship.dds")
    add_sprite(f"GFX_{tag}_basic_battleship_medium", "gfx/interface/technologies/basic_battleship.dds")
    add_sprite(f"GFX_{tag}_battleship_1_medium", "gfx/interface/technologies/early_battleship.dds")
    add_sprite(f"GFX_{tag}_early_battlecruiser_medium", "gfx/interface/technologies/early_battlecruiser.dds")
    add_sprite(f"GFX_{tag}_early_submarine_medium", "gfx/interface/technologies/early_submarine.dds")
    add_sprite(f"GFX_{tag}_basic_submarine_medium", "gfx/interface/technologies/basic_submarine.dds")
    add_sprite(f"GFX_{tag}_submarine_1_medium", "gfx/interface/technologies/early_submarine.dds")

    add_sprite(f"GFX_{tag}_early_ship_hull_light_medium", "gfx/interface/technologies/early_destroyer.dds")
    add_sprite(f"GFX_{tag}_basic_ship_hull_light_medium", "gfx/interface/technologies/basic_destroyer.dds")
    add_sprite(f"GFX_{tag}_early_ship_hull_cruiser_medium", "gfx/interface/technologies/early_light_cruiser.dds")
    add_sprite(f"GFX_{tag}_basic_ship_hull_cruiser_medium", "gfx/interface/technologies/basic_light_cruiser.dds")
    add_sprite(f"GFX_{tag}_early_ship_hull_heavy_medium", "gfx/interface/technologies/early_battleship.dds")
    add_sprite(f"GFX_{tag}_basic_ship_hull_heavy_medium", "gfx/interface/technologies/basic_battleship.dds")
    add_sprite(f"GFX_{tag}_early_ship_hull_submarine_medium", "gfx/interface/technologies/early_submarine.dds")
    add_sprite(f"GFX_{tag}_basic_ship_hull_submarine_medium", "gfx/interface/technologies/basic_submarine.dds")

# Configure major nations
nations = [
    ("GER", "GER"),
    ("FRA", "FRA"),
    ("ENG", "ENG"),
    ("RUS", "RUS"),
    ("SOV", "RUS"),
    ("USA", "USA"),
    ("ITA", "ITA"),
    ("AUS", "AUH"),
    ("AUH", "AUH"),
    ("TUR", "TUR"),
    ("OTT", "TUR"),
    ("JAP", "JAP"),
    ("BEL", "BEL"),
    ("BUL", "BUL"),
    ("CAN", "CAN"),
    ("CHI", "CHI"),
    ("CHL", "CHL"),
    ("GRE", "GRE"),
    ("LIT", "LIT"),
    ("MEX", "MEX"),
]

for tag, ftag in nations:
    configure_nation(tag, ftag)

print(f"Total unique sprites configured: {len(sprites)}")

# Write out zz_ww1_technologies_adaptation.gfx
out_file = interface_dir / "zz_ww1_technologies_adaptation.gfx"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("spriteTypes = {\n")
    f.write("\t### MASTER WW1 EQUIPMENT & TECHNOLOGY SPRITE ADAPTATION ###\n")
    f.write("\t# Comprehensive coverage for Archetypes, Generics, Designers and Major Nations\n\n")
    for name, rel_path in sorted(sprites.items()):
        f.write("\tSpriteType = {\n")
        f.write(f'\t\tname = "{name}"\n')
        f.write(f'\t\ttexturefile = "{rel_path}"\n')
        f.write("\t}\n")
    f.write("}\n")

print(f"Successfully generated {out_file} with {len(sprites)} sprites!")
