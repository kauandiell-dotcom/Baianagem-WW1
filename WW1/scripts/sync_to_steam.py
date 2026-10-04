import os
import shutil

src_root = os.path.abspath('.')
dst_root = r'E:\SteamLibrary\steamapps\workshop\content\394360\3809191491'

print(f'Syncing from {src_root} to {dst_root}...')

if not os.path.isdir(dst_root):
    print(f'Error: Destination {dst_root} does not exist!')
    exit(1)

# Folders to sync
folders = [
    'common',
    'events',
    'interface',
    'gfx',
    'history',
    'localisation'
]

copied = 0
for folder in folders:
    src_dir = os.path.join(src_root, folder)
    dst_dir = os.path.join(dst_root, folder)
    if not os.path.exists(src_dir):
        continue
    for root, dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_root)
        target_dir = os.path.join(dst_root, rel)
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            src_f = os.path.join(root, f)
            dst_f = os.path.join(target_dir, f)
            
            # Check if needs copy (doesn't exist or size/mtime different)
            if not os.path.exists(dst_f) or os.path.getmtime(src_f) > os.path.getmtime(dst_f) or os.path.getsize(src_f) != os.path.getsize(dst_f):
                shutil.copy2(src_f, dst_f)
                copied += 1

print(f'Sync complete! Successfully updated/copied {copied} files to Steam Workshop directory.')
