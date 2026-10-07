from PIL import Image
import numpy as np
from pathlib import Path

def clean_letterbox(img_path: Path):
    try:
        im = Image.open(img_path)
        arr = np.array(im)
        if arr.shape[0] < 50 or arr.shape[1] < 100:
            return False
        
        # Check rows from top
        top_cut = 0
        for r in range(arr.shape[0] // 3):
            # If row is almost solid dark (mean RGB < 32 and std < 8)
            row = arr[r, :, :3]
            if row.mean() < 32 and row.std() < 8:
                top_cut = r + 1
            else:
                break
                
        bot_cut = arr.shape[0]
        for r in range(arr.shape[0] - 1, arr.shape[0] - arr.shape[0] // 3, -1):
            row = arr[r, :, :3]
            if row.mean() < 32 and row.std() < 8:
                bot_cut = r
            else:
                break
                
        if top_cut >= 10 or (arr.shape[0] - bot_cut) >= 10:
            print(f"Trimming {img_path}: top_cut={top_cut}, bot_cut={bot_cut} (original h={arr.shape[0]})")
            cropped = im.crop((0, top_cut, im.width, bot_cut))
            resized = cropped.resize((450, 250), Image.Resampling.LANCZOS)
            resized.save(img_path)
            return True
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
    return False

count = 0
for folder in ["gfx/event_pictures/ww1_alpha", "gfx/event_pictures/ww1_britain"]:
    for p in Path(folder).glob("*.png"):
        if clean_letterbox(p):
            count += 1

print(f"Total letterboxed event pictures fixed: {count}")
