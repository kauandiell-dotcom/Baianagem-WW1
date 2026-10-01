import re, sys, os, glob

def audit_focus_tree(focus_file, gfx_dir="interface", loc_dir="localisation"):
    print(f"=== AUDITING FOCUS TREE: {focus_file} ===")
    
    if not os.path.exists(focus_file):
        print(f"ERROR: File {focus_file} not found!")
        return False
        
    with open(focus_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # 1. Brace check
    opens = text.count('{')
    closes = text.count('}')
    print(f"1. Brace Balance: Opens={opens}, Closes={closes} -> {'PASS' if opens == closes else 'FAIL'}")
    if opens != closes:
        return False

    # 2. Parse focuses
    blocks = text.split('focus = {')
    focuses = {}
    coords = {}
    collisions = []

    for b in blocks[1:]:
        f_id = re.search(r'id\s*=\s*([A-Za-z0-9_]+)', b)
        f_x = re.search(r'x\s*=\s*([0-9]+)', b)
        f_y = re.search(r'y\s*=\s*([0-9]+)', b)
        if not (f_id and f_x and f_y):
            continue
        fid = f_id.group(1)
        x = int(f_x.group(1))
        y = int(f_y.group(1))
        
        if (x, y) in coords:
            collisions.append((fid, coords[(x, y)], x, y))
        else:
            coords[(x, y)] = fid
            
        prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', b)
        all_p = []
        for p in prereqs:
            all_p.extend(re.findall(r'focus\s*=\s*([A-Za-z0-9_]+)', p))
            
        focuses[fid] = {'x': x, 'y': y, 'prereqs': all_p}

    print(f"Total Focuses Parsed: {len(focuses)}")
    print(f"2. Coordinate Collisions: {len(collisions)} {collisions}")

    # 3. Geometric edges
    backward_edges = []
    same_row_edges = []
    long_jumps = []

    for fid, data in focuses.items():
        for p in data['prereqs']:
            if p in focuses:
                parent = focuses[p]
                dy = data['y'] - parent['y']
                dx = abs(data['x'] - parent['x'])
                if dy < 0:
                    backward_edges.append((p, fid, dy))
                elif dy == 0:
                    same_row_edges.append((p, fid))
                elif dy > 2:
                    long_jumps.append((p, fid, dy))

    print(f"3. Backward Edges (dy < 0) [Upward Arrows]: {len(backward_edges)}")
    print(f"4. Same-Row Edges (dy == 0) [Horizontal Overlap]: {len(same_row_edges)}")
    print(f"5. Long Vertical Jumps (dy > 2): {len(long_jumps)}")

    # 4. Check DAG Cycles
    visited = {}
    def dfs(node):
        visited[node] = 1
        for p in focuses[node]['prereqs']:
            if p in focuses:
                if visited.get(p) == 1:
                    return False
                if visited.get(p) == 0:
                    if not dfs(p):
                        return False
        visited[node] = 2
        return True

    for f in focuses:
        visited[f] = 0

    no_cycles = True
    for f in focuses:
        if visited[f] == 0:
            if not dfs(f):
                no_cycles = False
                break
    print(f"6. Cycle Detection: {'PASS' if no_cycles else 'FAIL'}")

    return len(collisions) == 0 and len(backward_edges) == 0 and len(same_row_edges) == 0 and no_cycles

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'common/national_focus/germany.txt'
    res = audit_focus_tree(target)
    sys.exit(0 if res else 1)
