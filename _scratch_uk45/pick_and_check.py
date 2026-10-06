import json, os, re, subprocess, sys
from pathlib import Path

S = Path(os.environ['KIROCREW_SCRATCH'])
ROOT = Path('.').resolve()
cf = json.loads((S / 'sheets_focus/candidates.json').read_text(encoding='utf-8'))
ce = json.loads((S / 'sheets_event/candidates.json').read_text(encoding='utf-8'))

FOCUS = {
"territorial_force_camps": [0], "the_special_reserve": [2], "regular_army_mobilisation": [7],
"army_service_corps_offices": [6], "the_expeditionary_establishment": [1], "the_pals_battalion_system": [7],
"the_rifle_training_depots": [6, 0], "field_medical_organisation": [1, 0], "the_artillery_observation_school": [1, 3],
"machine_gun_corps_formation": [0], "trench_mortar_sections": [8, 9], "the_infantry_training_directorate": [0],
"combined_arms_staff_courses": [3, 0], "the_demobilisation_register": [8, 2], "a_smaller_professional_force": [7, 2],
"territorial_defence_renewal": [7], "battlecruiser_squadron_planning": [2, 1, 7], "destroyer_flotilla_planning": [0, 8],
"submarine_service_development": [8, 7], "naval_gunnery_calibration": [7, 0], "the_north_sea_watch": [5, 6],
"merchant_shipping_register": [6, 7], "maritime_blockade_coordination": [9, 5], "hydrophone_trials": [0, 1],
"depth_charge_trials": [7, 2], "escort_refit_contracts": [3, 0], "naval_signals_and_direction_finding": [5, 3],
"mediterranean_convoy_liaison": [2, 5], "the_postwar_fleet_review": [1, 9], "naval_budget_retrenchment": [1, 0],
"naval_technical_lessons": [4, 5], "the_air_battalion_experiments": [3, 0], "royal_flying_corps_organisation": [0],
"aerial_reconnaissance_reports": [6], "royal_naval_air_service_organisation": [1, 0],
"wireless_and_aircraft_observation": [1, 7], "bristol_scout_trials": [0, 1, 9], "naval_seaplane_stations": [0],
"aircraft_production_contracts": [9, 0], "fighter_squadron_instruction": [6], "artillery_spotting_liaison": [2, 3],
"night_flying_experiments": [0], "bomber_range_experiments": [3, 8], "aircraft_engine_reliability": [7, 0],
"home_air_defence_coordination": [2, 3], "the_independent_air_service_debate": [1], "postwar_aircraft_demobilisation": [7, 4],
"civil_aviation_research": [0, 5], "a_sustainable_air_establishment": [2], "the_channel_mobilisation_timetable": [3, 8],
"embarkation_depot_preparation": [7, 8], "the_bef_deployment_plan": [7], "the_flanders_supply_organisation": [2, 3],
"holding_the_continental_line": [7, 5], "artillery_ammunition_concentration": [1, 6], "a_limited_offensive_doctrine": [4, 3],
"the_dardanelles_staff_study": [4, 0], "mediterranean_landing_preparation": [1, 9], "mesopotamian_supply_review": [2, 0],
"the_western_offensive_staff_study": [4, 2], "the_creeping_barrage_school": [7, 6], "assault_coordination_exercises": [0, 5],
"palestine_railway_liaison": [7, 8], "the_spring_defence_plan": [6, 4], "the_allied_counteroffensive_plan": [4, 1],
"operational_reserve_restoration": [7, 3], "the_armistice_stand_down_plan": [2, 4], "lessons_for_the_general_staff": [2, 1],
}
# event art name -> (candidate subject, [indices])
EVENT = {
"convoy_debate": ("convoy_debate", [8, 3]), "jutland": ("jutland", [3, 5]), "zeppelins": ("zeppelins", [3, 2]),
"gotha_raids": ("gotha_raids", [6, 8]), "smuts_report": ("smuts_report", [7, 5]), "hunger_blockade": ("hunger_blockade", [0, 1]),
"orders_in_council": ("orders_in_council", [6, 8]), "med_escorts": ("med_escorts", [0, 5]),
"dardanelles_decision": ("dardanelles_decision", [3, 2]), "kut_siege": ("kut_siege", [0, 1]),
"somme_first_day": ("somme_first_day", [7, 5]), "demobilisation": ("demobilisation", [5, 7]),
"spring_offensive": ("spring_offensive", [6, 0]), "amiens_black_day": ("kut_siege", [3]),
"calais_mutinies": ("calais_mutinies", [5, 6]), "bef_arrives": ("bef_arrives", [2, 4, 1]),
"straits_fleet": ("straits_fleet", [0]), "german_black_day": ("german_black_day", [5, 3]),
"liaison_officers": ("liaison_officers", [4, 1]),
}
DERIVED_IDEAS = {
 "ENG_ww1_admiralty_war_staff": "admiralty_fleet_survey", "ENG_ww1_northern_patrol": "the_north_sea_watch",
 "ENG_ww1_grand_fleet_anchorage": "grand_fleet_maintenance", "ENG_ww1_convoy_system": "convoy_system_organisation",
 "ENG_ww1_royal_flying_corps": "royal_flying_corps_organisation", "ENG_ww1_engine_reliability": "aircraft_engine_reliability",
 "ENG_ww1_home_air_defence": "home_air_defence_coordination", "ENG_ww1_royal_air_force": "royal_air_force_unification",
 "ENG_ww1_haldane_reforms": "the_haldane_establishment", "ENG_ww1_kitchener_armies": "kitchener_new_armies",
 "ENG_ww1_pals_battalions": "the_pals_battalion_system", "ENG_ww1_flanders_supply": "the_flanders_supply_organisation",
 "ENG_ww1_training_directorate": "the_infantry_training_directorate", "ENG_ww1_combined_arms_staff": "combined_arms_staff_courses",
 "ENG_ww1_creeping_barrage": "the_creeping_barrage_school", "ENG_ww1_general_staff_lessons": "lessons_for_the_general_staff",
}
DERIVED_DECISIONS = {
 "ENG_ww1_services_policy": "the_haldane_establishment", "ENG_ww1_tighten_the_blockade": "maritime_blockade_coordination",
 "ENG_ww1_lend_escort_flotillas": "mediterranean_convoy_liaison", "ENG_ww1_fund_home_air_defence": "home_air_defence_coordination",
 "ENG_ww1_staff_college_course": "combined_arms_staff_courses", "ENG_ww1_send_liaison_officers": "the_bef_deployment_plan",
}

base = json.loads((ROOT / 'docs/britain_art_picks.json').read_text(encoding='utf-8'))
for k in list(base['focus']):
    pass
orig_focus = set(base['focus'])
orig_event = set(base['event'])
fo = {k: list(v) + [i for i in range(10) if i not in v] for k, v in FOCUS.items()}
ev = {k: (s, list(v) + [i for i in range(10) if i not in v]) for k, (s, v) in EVENT.items()}
fp = {k: 0 for k in fo}
ep = {k: 0 for k in ev}


def build():
    out = json.loads(json.dumps(base))
    for k, order in fo.items():
        lst = cf[k]
        idx = order[fp[k]]
        donor, rel = lst[idx] if idx < len(lst) else lst[0]
        out['focus'][k] = {"donor": donor, "source_relative": rel, "subject": k}
    for k, (subj, order) in ev.items():
        lst = ce[subj]
        idx = order[ep[k]]
        donor, rel = lst[idx] if idx < len(lst) else lst[0]
        out['event'][k] = {"donor": donor, "source_relative": rel, "subject": subj}
    out['derived_ideas'].update(DERIVED_IDEAS)
    out['derived_decisions'].update(DERIVED_DECISIONS)
    return out


tmp = S / 'picks_tmp.json'
for it in range(60):
    out = build()
    tmp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, 'scripts/build_britain_art.py', str(tmp), '--dry-run'], capture_output=True, text=True, encoding='utf-8')
    errs = [l[7:] for l in r.stdout.splitlines() if l.startswith('ERROR: ')]
    if not errs and r.returncode == 0:
        print('CLEAN after', it, 'rounds'); print(r.stdout.strip()); break
    print('round', it, len(errs), 'errors')
    for e in errs:
        print('  ', e[:160])
        if e.startswith('event '):
            name = e.split()[1].rstrip(':')
            if name in ep:
                ep[name] += 1
        else:
            name = e.split(':')[0]
            if name in fp:
                fp[name] += 1
    if not errs:
        print(r.stdout, r.stderr[-500:]); break
else:
    print('did not converge')
    sys.exit(1)
json.dump({'fp': fp, 'ep': ep}, open(S / 'state.json', 'w'))
(ROOT / 'docs/britain_art_picks.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('picks written to docs/britain_art_picks.json; focus', len(out['focus']), 'event', len(out['event']))
print('fallbacks used:', {k: fo[k][v] for k, v in fp.items() if v}, {k: ev[k][1][v] for k, v in ep.items() if v})
