import os, re, glob

repo = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1"

# 1. Parse all leader traits from common/country_leader/ and unit_leader_traits/
known_traits = set()
trait_dirs = [
    os.path.join(repo, "common", "country_leader"),
    os.path.join(repo, "common", "unit_leader_traits")
]

for td in trait_dirs:
    if not os.path.exists(td): continue
    for f in os.listdir(td):
        if not f.endswith(".txt"): continue
        p = os.path.join(td, f)
        with open(p, "r", encoding="utf-8", errors="ignore") as fl:
            txt = re.sub(r'#.*$', '', fl.read(), flags=re.MULTILINE)
        for m in re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', txt, re.MULTILINE):
            known_traits.add(m.group(1))
        for m in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*\{', txt):
            known_traits.add(m.group(1))

# Also standard HOI4 hardcoded vanilla traits
vanilla_traits = {
    "old_guard", "inspirational_leader", "offensive_doctrine", "defensive_doctrine",
    "trickster", "thorough_planner", "fast_planner", "unyielding_defender",
    "aggressive_assaulter", "organizer", "cavalry_officer", "infantry_officer",
    "panzer_leader", "fortress_buster", "commando", "winter_specialist",
    "trait_cautious", "trait_reckless", "media_personality", "harsh_leader",
    "naval_invader", "superior_tactician", "spotter", "fly_swatter", "ironside",
    "air_controller", "fleet_protector", "seawolf", "silent_workhorse",
    "captain_of_industry", "fortification_engineer", "war_industrialist",
    "armaments_organizer", "quartermaster_general", "popular_figurehead",
    "backroom_backstabber", "compassionate_gentleman", "ideological_crusader",
    "prince_of_terror", "smooth_talking_charmer", "armaments_minister",
    "army_chief_offensive_2", "army_chief_defensive_2", "army_chief_drill_2",
    "army_chief_maneuver_2", "army_chief_morale_2", "navy_chief_decisive_battle_2",
    "navy_chief_commerce_raiding_2", "navy_chief_naval_aviation_2",
    "air_chief_ground_support_2", "air_chief_air_superiority_2",
    "air_chief_all_weather_2", "army_commando_2", "army_cavalry_2",
    "army_infantry_2", "army_artillery_2", "army_logistics_2", "army_entrenchment_2",
    "army_armored_2", "navy_fleet_logistics_2", "navy_screen_2", "navy_capital_ship_2",
    "air_close_air_support_2", "air_tactical_bombing_2", "air_interception_2",
    "air_air_superiority_2", "cornered_fox", "skilled_staffer"
}
known_traits.update(vanilla_traits)

print(f"Total known traits database: {len(known_traits)}")

# 2. Check traits in SOV.txt and WHT.txt
chars_files = ["SOV.txt", "WHT.txt"]
unknown_traits = []

for cf in chars_files:
    p = os.path.join(repo, "common", "characters", cf)
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        txt = re.sub(r'#.*$', '', f.read(), flags=re.MULTILINE)
    
    matches = list(re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', txt, re.MULTILINE))
    for i, m in enumerate(matches):
        cid = m.group(1)
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(txt)
        chunk = txt[start:end]
        
        # find traits blocks
        trait_blocks = re.findall(r'\btraits\s*=\s*\{([^}]+)\}', chunk)
        for tb in trait_blocks:
            traits = tb.split()
            for t in traits:
                t = t.strip()
                if not t: continue
                if t not in known_traits:
                    unknown_traits.append((cf, cid, t))

if unknown_traits:
    print(f"Unknown traits found ({len(unknown_traits)}):")
    for cf, cid, t in unknown_traits:
        print(f"  [{cf}] {cid}: unknown trait '{t}'")
else:
    print("ALL character traits are 100% valid and recognized!")
