import json, os, subprocess, sys
from pathlib import Path
S = Path(os.environ['KIROCREW_SCRATCH'])
ROOT = Path('.').resolve()
cf = json.loads((S / 'sheets_focus/candidates.json').read_text(encoding='utf-8'))
ce2 = json.loads((S / 'sheets_event2/candidates.json').read_text(encoding='utf-8'))
base = json.loads((ROOT / 'docs/britain_art_picks.json').read_text(encoding='utf-8'))

FOC = {
 "maritime_blockade_coordination": [("maritime_blockade_coordination", 0), ("maritime_blockade_coordination", 2), ("maritime_blockade_coordination", 8)],
 "the_dardanelles_staff_study": [("the_dardanelles_staff_study", 4)],
 "lessons_for_the_general_staff": [("lessons_for_the_general_staff", 1), ("lessons_for_the_general_staff", 8), ("lessons_for_the_general_staff", 4)],
 "civil_aviation_research": [("bristol_scout_trials", 1), ("bristol_scout_trials", 0), ("civil_aviation_research", 4)],
 "regular_army_mobilisation": [("regular_army_mobilisation", 8), ("regular_army_mobilisation", 4), ("regular_army_mobilisation", 3)],
 "territorial_force_camps": [("territorial_force_camps", 6), ("territorial_force_camps", 5)],
 "fighter_squadron_instruction": [("bristol_scout_trials", 0), ("bristol_scout_trials", 1), ("fighter_squadron_instruction", 7), ("fighter_squadron_instruction", 8), ("the_air_battalion_experiments", 0)],
 "artillery_spotting_liaison": [("the_artillery_observation_school", 3), ("the_creeping_barrage_school", 8), ("the_creeping_barrage_school", 7), ("artillery_spotting_liaison", 3)],
 "holding_the_continental_line": [("holding_the_continental_line", 5), ("holding_the_continental_line", 7), ("holding_the_continental_line", 8)],
 "the_spring_defence_plan": [("the_spring_defence_plan", 7), ("the_spring_defence_plan", 8)],
}
EV = {"amiens_black_day": [("demob_a", 3)]}
ptr = {k: 0 for k in FOC}
eptr = {k: 0 for k in EV}
tmp = S / 'picks_tmp2.json'
for it in range(30):
    out = json.loads(json.dumps(base))
    for k, alts in FOC.items():
        s, i = alts[min(ptr[k], len(alts) - 1)]
        d, rel = cf[s][i]
        out['focus'][k] = {"donor": d, "source_relative": rel, "subject": s}
    for k, alts in EV.items():
        s, i = alts[min(eptr[k], len(alts) - 1)]
        d, rel = ce2[s][i]
        out['event'][k] = {"donor": d, "source_relative": rel, "subject": s}
    tmp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, 'scripts/build_britain_art.py', str(tmp), '--dry-run'], capture_output=True, text=True, encoding='utf-8')
    errs = [l[7:] for l in r.stdout.splitlines() if l.startswith('ERROR: ')]
    if not errs and r.returncode == 0:
        print('CLEAN', it); break
    for e in errs:
        print(' ', e[:150])
        n = e.split()[1].rstrip(':') if e.startswith('event ') else e.split(':')[0]
        if n in ptr: ptr[n] += 1
        elif n in eptr: eptr[n] += 1
    if not errs:
        print(r.stdout, r.stderr[-300:]); sys.exit(1)
else:
    sys.exit('no converge')
(ROOT / 'docs/britain_art_picks.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print({k: FOC[k][min(ptr[k], len(FOC[k]) - 1)] for k in FOC})
