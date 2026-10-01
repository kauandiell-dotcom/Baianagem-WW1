import re, sys

print("=== CHECKING FOCUS TREE GRAPH INTEGRITY ===")

with open('common/national_focus/germany.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Check total braces
opens = text.count('{')
closes = text.count('}')
print(f"Braces in germany.txt: Opens={opens}, Closes={closes}")
assert opens == closes, "Mismatched braces in germany.txt!"

focus_blocks = text.split('focus = {')
focus_dict = {}
for b in focus_blocks[1:]:
    fid = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', b).group(1)
    x = int(re.search(r'x\s*=\s*([0-9]+)', b).group(1))
    y = int(re.search(r'y\s*=\s*([0-9]+)', b).group(1))
    prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', b)
    all_prereqs = []
    for p in prereqs:
        f_in_p = re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', p)
        all_prereqs.append(f_in_p)
    
    mut_ex = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', b)
    all_mut = []
    for m in mut_ex:
        all_mut += re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', m)
    
    focus_dict[fid] = {
        'x': x,
        'y': y,
        'prereqs': all_prereqs,
        'mutually_exclusive': all_mut
    }

print(f"Parsed {len(focus_dict)} focuses.")

# 1. Check prerequisite existence
missing_prereqs = []
for fid, data in focus_dict.items():
    for p_group in data['prereqs']:
        for p in p_group:
            if p not in focus_dict:
                missing_prereqs.append((fid, p))

print(f"Missing prerequisites: {missing_prereqs}")
assert len(missing_prereqs) == 0, f"Found missing prerequisites: {missing_prereqs}"

# 2. Check mutually exclusive existence
missing_mut = []
for fid, data in focus_dict.items():
    for m in data['mutually_exclusive']:
        if m not in focus_dict:
            missing_mut.append((fid, m))

print(f"Missing mutually_exclusive: {missing_mut}")
assert len(missing_mut) == 0, f"Found missing mutually_exclusive: {missing_mut}"

# 3. Check for cycles (DFS)
def check_cycles():
    visited = {}
    
    def dfs(node, path):
        visited[node] = 1 # in progress
        for p_group in focus_dict[node]['prereqs']:
            for parent in p_group:
                if parent in visited:
                    if visited[parent] == 1:
                        print(f"CYCLE DETECTED: {' -> '.join(path + [parent])}")
                        return False
                else:
                    if not dfs(parent, path + [parent]):
                        return False
        visited[node] = 2 # finished
        return True

    for node in focus_dict:
        if node not in visited:
            if not dfs(node, [node]):
                return False
    return True

has_no_cycles = check_cycles()
print(f"Cycle check: {'PASS (No cycles found)' if has_no_cycles else 'FAIL (Cycle found)'}")
assert has_no_cycles, "Cycle detected in focus tree!"

print("Graph validation completed successfully with 0 errors!")
