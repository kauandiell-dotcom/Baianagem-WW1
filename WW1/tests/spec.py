"""
Authoritative specification for the German Empire National Focus Tree (Baianagem-WW1).
Derived directly from PLANO_FOCUS_TREE_ALEMANHA_WW1.md, PROJECT.md, and ORIGINAL_REQUEST.md.
"""

import os
from typing import Dict, List, Set, Any

# Total number of national focuses in the German tree
EXPECTED_FOCUS_COUNT = 32

# All 32 focus definitions with coordinates, prerequisites, mutual exclusions, and references
EXPECTED_FOCUSES: Dict[str, Dict[str, Any]] = {
    # Phase I (1911-1914) - Belle Époque & Pre-War Arms Race
    "GER_agadir_crisis_gambit": {
        "phase": "Phase I (1911-1914)",
        "x": 5, "y": 0,
        "cost": 5,
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_agadir_crisis_gambit",
        "dds": "focus_GER_agadir_crisis_gambit.dds",
        "events": ["ww1_germany_events.1"],
        "ideas": [],
        "states": [773, 1088],  # Cameroon / New Cameroon
    },
    "GER_tirpitz_fourth_naval_bill": {
        "phase": "Phase I (1911-1914)",
        "x": 8, "y": 0,
        "cost": 10,
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_navy",
        "dds": "focus_GER_navy.dds",
        "events": [],
        "ideas": ["GER_tirpitz_naval_ambition"],
        "states": [58, 56],  # Kiel, Wilhelmshaven
    },
    "GER_berlin_baghdad_railway": {
        "phase": "Phase I (1911-1914)",
        "x": 5, "y": 1,
        "cost": 7,
        "prerequisites": ["GER_agadir_crisis_gambit"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_berlin_baghdad_railway",
        "dds": "focus_GER_berlin_baghdad_railway.dds",
        "events": [],
        "ideas": [],
        "states": [64, 66],  # Berlin, Silesia
    },
    "GER_army_bill_1912": {
        "phase": "Phase I (1911-1914)",
        "x": 11, "y": 0,
        "cost": 7,
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_army_bill_1912",
        "dds": "focus_GER_army_bill_1912.dds",
        "events": [],
        "ideas": [],
        "states": [],
    },
    "GER_centenary_of_leipzig_1913": {
        "phase": "Phase I (1911-1914)",
        "x": 11, "y": 1,
        "cost": 7,
        "prerequisites": ["GER_army_bill_1912"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_centenary_of_leipzig_1913",
        "dds": "focus_GER_centenary_of_leipzig_1913.dds",
        "events": [],
        "ideas": ["GER_burgfrieden_social_peace"],
        "states": [],
    },
    "GER_expand_heavy_howitzers": {
        "phase": "Phase I (1911-1914)",
        "x": 11, "y": 2,
        "cost": 10,
        "prerequisites": ["GER_centenary_of_leipzig_1913"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_krupp",
        "dds": "focus_GER_krupp.dds",
        "events": [],
        "ideas": ["GER_krupp_chemical_conglomerates"],
        "states": [57],  # Westphalia (Essen)
    },
    "GER_the_blank_cheque": {
        "phase": "Phase I (1911-1914)",
        "x": 14, "y": 3,
        "cost": 5,
        "prerequisites": ["GER_expand_heavy_howitzers", "GER_tirpitz_fourth_naval_bill"],
        "mutually_exclusive": ["GER_willy_nicky_telegrams_bjorko"],
        "icon": "GFX_focus_ger_support_austrian_claims",
        "dds": "focus_ger_support_austrian_claims.dds",
        "events": ["ww1_germany_events.2"],
        "ideas": [],
        "states": [],
    },

    # Phase II (1914-1917) - Operational Choice & Total War
    "GER_execute_schlieffen_plan": {
        "phase": "Phase II - Schlieffen",
        "x": 13, "y": 4,
        "cost": 5,
        "prerequisites": ["GER_the_blank_cheque"],
        "mutually_exclusive": ["GER_aufmarsch_ost_focus"],
        "icon": "GFX_focus_ger_around_maginot",
        "dds": "focus_ger_around_maginot.dds",
        "events": ["ww1_germany_events.3"],
        "ideas": ["GER_schlieffen_momentum"],
        "states": [34],  # Belgium / Liège
    },
    "GER_smash_liege_forts": {
        "phase": "Phase II - Schlieffen",
        "x": 13, "y": 5,
        "cost": 5,
        "prerequisites": ["GER_execute_schlieffen_plan"],
        "mutually_exclusive": [],
        "icon": "GFX_ww1_mex_upca_conquer",
        "dds": "ww1_mex_upca_conquer.dds",
        "events": ["ww1_germany_events.5"],
        "ideas": [],
        "states": [34],  # Liège
    },
    "GER_the_miracle_of_tannenberg": {
        "phase": "Phase II - Schlieffen",
        "x": 13, "y": 6,
        "cost": 7,
        "prerequisites": ["GER_smash_liege_forts"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_the_miracle_of_tannenberg",
        "dds": "focus_GER_the_miracle_of_tannenberg.dds",
        "events": ["ww1_germany_events.6"],
        "ideas": [],
        "states": [5],  # Allenstein / East Prussia
    },
    "GER_aufmarsch_ost_focus": {
        "phase": "Phase II - Aufmarsch Ost",
        "x": 16, "y": 4,
        "cost": 10,
        "prerequisites": ["GER_the_blank_cheque"],
        "mutually_exclusive": ["GER_execute_schlieffen_plan"],
        "icon": "GFX_focus_GER_aufmarsch_ost_focus",
        "dds": "focus_GER_aufmarsch_ost_focus.dds",
        "events": ["ww1_germany_events.4"],
        "ideas": [],
        "states": [42, 28],  # Rhineland, Alsace-Lorraine
    },
    "GER_haber_bosch_nitrogen_miracle": {
        "phase": "Phase II - Total War",
        "x": 12, "y": 7,
        "cost": 10,
        "prerequisites_or": ["GER_the_miracle_of_tannenberg", "GER_aufmarsch_ost_focus"],
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_haber_bosch_nitrogen_miracle",
        "dds": "focus_GER_haber_bosch_nitrogen_miracle.dds",
        "events": [],
        "ideas": ["GER_krupp_chemical_conglomerates"],
        "states": [],
    },
    "GER_chemical_warfare_initiative": {
        "phase": "Phase II - Total War",
        "x": 12, "y": 8,
        "cost": 10,
        "prerequisites": ["GER_haber_bosch_nitrogen_miracle"],
        "mutually_exclusive": [],
        "icon": "GFX_ww1_nationalfocus_gasmask",
        "dds": "ww1_nationalfocus_gasmask.dds",
        "events": ["ww1_germany_events.7"],
        "ideas": ["chemical_gas_disruption"],
        "states": [],
    },
    "GER_hindenburg_program": {
        "phase": "Phase II - Total War",
        "x": 15, "y": 7,
        "cost": 10,
        "prerequisites_or": ["GER_the_miracle_of_tannenberg", "GER_aufmarsch_ost_focus"],
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_OHL",
        "dds": "focus_OHL.dds",
        "events": [],
        "ideas": ["GER_hindenburg_program_victory"],
        "states": [],
    },
    "GER_stosstruppen_tactics": {
        "phase": "Phase II - Total War",
        "x": 15, "y": 8,
        "cost": 10,
        "prerequisites_or": ["GER_hindenburg_program", "GER_chemical_warfare_initiative"],
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_ww1_nationalfocus_ironcross",
        "dds": "ww1_nationalfocus_ironcross.dds",
        "events": [],
        "ideas": ["german_infiltration_assault_idea"],
        "states": [],
    },

    # Phase III - Political Route 1: OHL Military Dictatorship (Historical)
    "GER_silent_dictatorship_ohl": {
        "phase": "Phase III - OHL Dictatorship",
        "x": 19, "y": 9,
        "cost": 10,
        "prerequisites": ["GER_stosstruppen_tactics"],
        "mutually_exclusive": [
            "GER_bethmann_civilian_supremacy",
            "GER_found_vaterlandspartei",
            "GER_spartakusbund_proletarian_revolt",
        ],
        "icon": "GFX_focus_GER_silent_dictatorship_ohl",
        "dds": "focus_GER_silent_dictatorship_ohl.dds",
        "events": [],
        "ideas": ["GER_grosser_generalstab", "GER_ohl_supreme_command"],
        "states": [],
    },
    "GER_unrestricted_submarine_warfare": {
        "phase": "Phase III - OHL Dictatorship",
        "x": 18, "y": 10,
        "cost": 10,
        "prerequisites": ["GER_silent_dictatorship_ohl"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_unrestricted_submarine_warfare",
        "dds": "focus_GER_unrestricted_submarine_warfare.dds",
        "events": ["ww1_germany_events.8"],
        "ideas": ["GER_unrestricted_submarine_warfare_spirit"],
        "states": [],
    },
    "GER_sealed_train_to_petrograd": {
        "phase": "Phase III - OHL Dictatorship",
        "x": 20, "y": 10,
        "cost": 5,
        "prerequisites": ["GER_silent_dictatorship_ohl"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_sealed_train_to_petrograd",
        "dds": "focus_GER_sealed_train_to_petrograd.dds",
        "events": ["ww1_germany_events.9"],
        "ideas": [],
        "states": [],
    },
    "GER_treaty_of_brest_litovsk": {
        "phase": "Phase III - OHL Dictatorship",
        "x": 20, "y": 11,
        "cost": 10,
        "prerequisites": ["GER_sealed_train_to_petrograd"],
        "mutually_exclusive": [],
        "icon": "GFX_goal_deal_with_german_empire",
        "dds": "focus_deal_with_german_empire.dds",
        "events": ["ww1_germany_events.10"],
        "ideas": ["GER_turnip_winter_crisis", "GER_encirclement_paranoia"],
        "states": [11, 188, 189, 190, 10, 85, 86, 87, 192, 193, 194],  # Ober Ost, Poland, Ukraine
    },
    "GER_the_kaiserschlacht_1918": {
        "phase": "Phase III - OHL Dictatorship",
        "x": 19, "y": 12,
        "cost": 10,
        "prerequisites": ["GER_treaty_of_brest_litovsk", "GER_unrestricted_submarine_warfare"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_the_kaiserschlacht_1918",
        "dds": "focus_GER_the_kaiserschlacht_1918.dds",
        "events": [],
        "ideas": ["GER_kaiserschlacht_idea"],
        "states": [],
    },

    # Phase III - Political Route 2: Volkskaiserreich (Reformist Monarchy)
    "GER_bethmann_civilian_supremacy": {
        "phase": "Phase III - Volkskaiserreich",
        "x": 23, "y": 9,
        "cost": 10,
        "prerequisites": ["GER_stosstruppen_tactics"],
        "mutually_exclusive": [
            "GER_silent_dictatorship_ohl",
            "GER_found_vaterlandspartei",
            "GER_spartakusbund_proletarian_revolt",
        ],
        "icon": "GFX_focus_GER_bethmann_civilian_supremacy",
        "dds": "focus_GER_bethmann_civilian_supremacy.dds",
        "events": [],
        "ideas": ["GER_civilian_general_staff"],
        "states": [],
    },
    "GER_prussian_franchise_reform": {
        "phase": "Phase III - Volkskaiserreich",
        "x": 23, "y": 10,
        "cost": 10,
        "prerequisites": ["GER_bethmann_civilian_supremacy"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_prussian_franchise_reform",
        "dds": "focus_GER_prussian_franchise_reform.dds",
        "events": [],
        "ideas": ["GER_burgfrieden_social_peace"],
        "states": [],
    },
    "GER_reichstag_peace_resolution": {
        "phase": "Phase III - Volkskaiserreich",
        "x": 23, "y": 11,
        "cost": 10,
        "prerequisites": ["GER_prussian_franchise_reform"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_reichstag_peace_resolution",
        "dds": "focus_GER_reichstag_peace_resolution.dds",
        "events": ["ww1_germany_events.11"],
        "ideas": [],
        "states": [],
    },
    "GER_constitutional_monarchy_proclamation": {
        "phase": "Phase III - Volkskaiserreich",
        "x": 23, "y": 12,
        "cost": 10,
        "prerequisites": ["GER_reichstag_peace_resolution"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_constitutional_monarchy_proclamation",
        "dds": "focus_GER_constitutional_monarchy_proclamation.dds",
        "events": [],
        "ideas": ["GER_constitutional_monarchy_spirit"],
        "states": [],
    },

    # Phase III - Political Route 3: Deutsche Vaterlandspartei (Radical Annexationist)
    "GER_found_vaterlandspartei": {
        "phase": "Phase III - Vaterlandspartei",
        "x": 27, "y": 9,
        "cost": 10,
        "prerequisites": ["GER_stosstruppen_tactics"],
        "mutually_exclusive": [
            "GER_silent_dictatorship_ohl",
            "GER_bethmann_civilian_supremacy",
            "GER_spartakusbund_proletarian_revolt",
        ],
        "icon": "GFX_focus_GER_found_vaterlandspartei",
        "dds": "focus_GER_found_vaterlandspartei.dds",
        "events": [],
        "ideas": ["GER_vaterlandspartei_rule"],
        "states": [],
    },
    "GER_total_war_mobilization": {
        "phase": "Phase III - Vaterlandspartei",
        "x": 27, "y": 10,
        "cost": 10,
        "prerequisites": ["GER_found_vaterlandspartei"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_total_war_mobilization",
        "dds": "focus_GER_total_war_mobilization.dds",
        "events": [],
        "ideas": ["GER_total_war_labor_conscription"],
        "states": [57, 42],  # Westphalia, Rhineland
    },
    "GER_annexation_of_belgium_and_briey": {
        "phase": "Phase III - Vaterlandspartei",
        "x": 27, "y": 11,
        "cost": 10,
        "prerequisites": ["GER_total_war_mobilization"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_annexation_of_belgium_and_briey",
        "dds": "focus_GER_annexation_of_belgium_and_briey.dds",
        "events": [],
        "ideas": ["GER_belgian_briey_exploitation"],
        "states": [34, 6, 17],  # Wallonia, Flanders, Briey/French Lorraine
    },
    "GER_morphed_mitteleuropa_iron_rule": {
        "phase": "Phase III - Vaterlandspartei",
        "x": 27, "y": 12,
        "cost": 10,
        "prerequisites": ["GER_annexation_of_belgium_and_briey"],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_morphed_mitteleuropa_iron_rule",
        "dds": "focus_GER_morphed_mitteleuropa_iron_rule.dds",
        "events": [],
        "ideas": [],
        "states": [],
    },

    # Special Paths & Easter Eggs
    "GER_willy_nicky_telegrams_bjorko": {
        "phase": "Easter Eggs & Alt-History",
        "x": 2, "y": 0,
        "cost": 10,
        "prerequisites": [],
        "mutually_exclusive": ["GER_the_blank_cheque"],
        "icon": "GFX_focus_GER_willy_nicky_telegrams_bjorko",
        "dds": "focus_GER_willy_nicky_telegrams_bjorko.dds",
        "events": ["ww1_germany_events.13"],
        "ideas": [],
        "states": [],
    },
    "GER_hajj_wilhelm_pan_islamic_crusade": {
        "phase": "Easter Eggs & Alt-History",
        "x": 5, "y": 2,
        "cost": 10,
        "prerequisites": ["GER_berlin_baghdad_railway"],
        "mutually_exclusive": [],
        "icon": "GFX_ww1_nationalfocus_islam",
        "dds": "ww1_nationalfocus_islam.dds",
        "events": ["ww1_germany_events.14"],
        "ideas": ["GER_pan_islamic_jihad_spirit"],
        "states": [],
    },
    "GER_spartakusbund_proletarian_revolt": {
        "phase": "Easter Eggs & Alt-History",
        "x": 30, "y": 9,
        "cost": 5,
        "prerequisites": [],
        "mutually_exclusive": [
            "GER_silent_dictatorship_ohl",
            "GER_bethmann_civilian_supremacy",
            "GER_found_vaterlandspartei",
        ],
        "icon": "GFX_goal_generic_workers",
        "dds": "focus_socialist_worker.dds",
        "events": ["ww1_germany_events.12"],
        "ideas": [],
        "states": [],
    },
    "GER_emergency_danubian_annexation": {
        "phase": "Easter Eggs & Alt-History",
        "x": 33, "y": 4,
        "cost": 7,
        "prerequisites": [],
        "mutually_exclusive": [],
        "icon": "GFX_focus_GER_emergency_danubian_annexation",
        "dds": "focus_GER_emergency_danubian_annexation.dds",
        "events": ["ww1_germany_events.15"],
        "ideas": [],
        "states": [4, 152, 153],  # Vienna, Lower Austria, Upper Austria
    },
}

# 15 Event IDs specified for German events
EXPECTED_EVENT_IDS: List[str] = [
    "ww1_germany_events.1",
    "ww1_germany_events.2",
    "ww1_germany_events.3",
    "ww1_germany_events.4",
    "ww1_germany_events.5",
    "ww1_germany_events.6",
    "ww1_germany_events.7",
    "ww1_germany_events.8",
    "ww1_germany_events.9",
    "ww1_germany_events.10",
    "ww1_germany_events.11",
    "ww1_germany_events.12",
    "ww1_germany_events.13",
    "ww1_germany_events.14",
    "ww1_germany_events.15",
]

# New German ideas required by the focus tree
EXPECTED_NEW_IDEAS: List[str] = [
    "GER_schlieffen_momentum",
    "GER_ohl_supreme_command",
    "GER_civilian_general_staff",
    "GER_unrestricted_submarine_warfare_spirit",
    "GER_vaterlandspartei_rule",
    "GER_total_war_labor_conscription",
    "GER_belgian_briey_exploitation",
    "GER_pan_islamic_jihad_spirit",
    "GER_constitutional_monarchy_spirit",
]

# Starting German ideas already present in the mod
EXPECTED_STARTING_IDEAS: List[str] = [
    "GER_grosser_generalstab",
    "GER_krupp_chemical_conglomerates",
    "GER_tirpitz_naval_ambition",
    "GER_encirclement_paranoia",
    "GER_burgfrieden_social_peace",
    "GER_turnip_winter_crisis_3",
    "GER_turnip_winter_crisis_2",
    "GER_turnip_winter_crisis_1",
    "GER_hindenburg_program_victory",
    "chemical_gas_disruption",
    "german_infiltration_assault_idea",
    "GER_kaiserschlacht_idea",
]

# Verified state IDs referenced in tree effects
EXPECTED_REFERENCED_STATES: List[int] = [
    4,    # Vienna
    5,    # Allenstein
    6,    # Flanders
    10,   # Warsaw
    11,   # Lithuania
    17,   # French Lorraine / Briey
    28,   # Alsace-Lorraine
    34,   # Wallonia / Liège
    42,   # Rhineland
    56,   # Weser-Ems / Wilhelmshaven
    57,   # Westphalia
    58,   # Schleswig-Holstein / Kiel
    64,   # Berlin
    66,   # Silesia
    85,   # Radom
    86,   # Kielce
    87,   # Lodz
    152,  # Lower Austria
    153,  # Upper Austria
    188,  # Courland
    189,  # Livonia
    190,  # Estonia
    192,  # Kiev
    193,  # Poltava
    194,  # Chernigov
    773,  # Cameroon
    1088, # German Congo / New Cameroon
]

# Target Steam Workshop directory
STEAM_WORKSHOP_TARGET = r"E:\SteamLibrary\steamapps\workshop\content\394360\3809191491" if os.path.isdir(r"E:\SteamLibrary\steamapps\workshop\content\394360\3809191491") else r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\3809191491"
