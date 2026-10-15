import os, glob, sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))
import hoi4_semantic_oracle as oracle

base_dir = '.' if os.path.exists('common') else 'WW1'

files_to_check = [
    os.path.join(base_dir, 'common/ideas/ww1_russia_ideas.txt'),
    os.path.join(base_dir, 'common/ideas/ww1_ger_rus_rework_ideas.txt'),
    os.path.join(base_dir, 'common/ideas/side_ww1_ger_rus_depth.txt'),
    os.path.join(base_dir, 'common/decisions/ww1_ger_rus_rework_decisions.txt'),
    os.path.join(base_dir, 'common/decisions/ww1_russia_crisis_decisions.txt'),
    os.path.join(base_dir, 'common/decisions/ww1_russia_tsarist_decisions.txt'),
    os.path.join(base_dir, 'common/decisions/ww1_soviet_civil_war_decisions.txt'),
    os.path.join(base_dir, 'common/decisions/ww1_soviet_diplomacy_decisions.txt'),
    os.path.join(base_dir, 'common/decisions/side_ww1_ger_rus_depth.txt')
]

total_errors = 0
for f in files_to_check:
    errors = oracle.audit_file_modifiers(f)
    print(f"File: {f} -> {len(errors)} invalid modifier tokens")
    for line_num, token, ctx in errors:
        print(f"   Line {line_num} in [{ctx}]: invalid token '{token}'")
        total_errors += 1

print(f"\nTOTAL SEMANTIC ORACLE ERRORS: {total_errors}")
