import os, re

with open('common/national_focus/germany.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
focus_blocks = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip().startswith('focus = {'):
        depth = 1
        i += 1
        block = []
        while i < len(lines) and depth > 0:
            depth += lines[i].count('{') - lines[i].count('}')
            block.append(lines[i])
            i += 1
        focus_blocks.append('\n'.join(block))
    else:
        i += 1

pol_foci = []
for b in focus_blocks:
    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
    x = int(re.search(r'\bx\s*=\s*(\d+)', b).group(1))
    y = int(re.search(r'\by\s*=\s*(\d+)', b).group(1))
    if x <= 16 and y <= 11:
        # Get completion reward
        reward = ''
        if 'completion_reward = {' in b:
            rw_start = b.find('completion_reward = {') + len('completion_reward = {')
            rw_depth = 1
            idx = rw_start
            while idx < len(b) and rw_depth > 0:
                if b[idx] == '{': rw_depth += 1
                elif b[idx] == '}': rw_depth -= 1
                idx += 1
            reward = b[rw_start:idx-1].strip()
        pol_foci.append((fid, x, y, reward, b))

print(f'Total political foci found: {len(pol_foci)}')

# Group by branch
print('\n=== POLITICAL FOCI IN GERMANY ===')
for fid, x, y, rw, b in sorted(pol_foci, key=lambda it: (it[2], it[1])):
    prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', b)
    muts = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', b)
    pr_str = ' & '.join([p.strip().replace('focus = ', '') for p in prereqs])
    mut_str = ' | '.join([m.strip().replace('focus = ', '') for m in muts])
    print(f'({x:2d}, {y:2d}) {fid}')
    if pr_str: print(f'       Prereq: {pr_str}')
    if mut_str: print(f'       Mut: {mut_str}')
    print(f'       Reward: {rw[:80].replace(chr(10), " ")}...')
