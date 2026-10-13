import os, sys, subprocess, re

def get_workspace(plan_path):
    # Use current working directory (WW1 mod root)
    root = os.getcwd()
    slug = os.path.splitext(os.path.basename(plan_path))[0]
    ws = os.path.join(root, '.superpowers', 'sdd', slug)
    os.makedirs(ws, exist_ok=True)
    marker = os.path.join(ws, 'plan-path')
    if not os.path.exists(marker):
        with open(marker, 'w', encoding='utf-8') as f:
            f.write(plan_path + '\n')
    return ws

def extract_task_brief(plan_path, task_num, out_file=None):
    ws = get_workspace(plan_path)
    if not out_file:
        out_file = os.path.join(ws, f"task-{task_num}-brief.md")
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    task_lines = []
    in_target = False
    in_fence = False
    
    target_header = re.compile(rf"^#+\s+Task\s+{task_num}(?:\:|\s|$)", re.IGNORECASE)
    next_header = re.compile(r"^#+\s+Task\s+\d+", re.IGNORECASE)
    
    for line in lines:
        if line.startswith('```'):
            in_fence = not in_fence
        if not in_fence and target_header.match(line):
            in_target = True
        elif not in_fence and in_target and next_header.match(line):
            break
        
        if in_target:
            task_lines.append(line)
            
    if not task_lines:
        raise ValueError(f"Task {task_num} not found in {plan_path}")
        
    with open(out_file, 'w', encoding='utf-8') as f:
        f.writelines(task_lines)
        
    print(f"wrote {out_file}: {len(task_lines)} lines")
    return out_file

def generate_review_package(plan_path, base, head, out_file=None):
    ws = get_workspace(plan_path)
    base_short = subprocess.check_output(['git', 'rev-parse', '--short', base], encoding='utf-8', errors='replace').strip()
    head_short = subprocess.check_output(['git', 'rev-parse', '--short', head], encoding='utf-8', errors='replace').strip()
    
    if not out_file:
        out_file = os.path.join(ws, f"review-{base_short}..{head_short}.diff")
        
    log = subprocess.check_output(['git', 'log', '--oneline', f"{base}..{head}"], encoding='utf-8', errors='replace')
    stat = subprocess.check_output(['git', 'diff', '--stat', f"{base}..{head}"], encoding='utf-8', errors='replace')
    diff = subprocess.check_output(['git', 'diff', '-U10', f"{base}..{head}"], encoding='utf-8', errors='replace')
    
    content = f"# Review package: {base}..{head}\n\n## Commits\n{log}\n## Files changed\n{stat}\n## Diff\n{diff}"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"wrote {out_file}: {len(content)} bytes")
    return out_file

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'workspace':
        print(get_workspace(sys.argv[2]))
    elif cmd == 'task-brief':
        extract_task_brief(sys.argv[2], sys.argv[3])
    elif cmd == 'review-package':
        generate_review_package(sys.argv[2], sys.argv[3], sys.argv[4])
