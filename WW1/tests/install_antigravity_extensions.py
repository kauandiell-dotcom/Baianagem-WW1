#!/usr/bin/env python3
"""
Installer for HOI4 Extensions in Antigravity IDE
Downloads and registers:
1. HOI4 Mod Utilities (Chaofan.hoi4modutilities)
2. CWTools - Paradox Language Support (tboby.cwtools-vscode)
into C:\\Users\\Usuário\\.antigravity-ide\\extensions\\
"""

import os
import io
import json
import time
import zipfile
import urllib.request
from pathlib import Path

EXTENSIONS_DIR = Path(r"C:\Users\Usuário\.antigravity-ide\extensions")
EXT_JSON_PATH = EXTENSIONS_DIR / "extensions.json"

EXTENSIONS_TO_INSTALL = [
    {
        "id": "chaofan.hoi4modutilities",
        "publisher": "Chaofan",
        "name": "hoi4modutilities",
        "version": "0.18.1",
        "url": "https://chaofan.gallery.vsassets.io/_apis/public/gallery/publisher/Chaofan/extension/hoi4modutilities/0.18.1/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage",
        "folder_name": "chaofan.hoi4modutilities-0.18.1"
    },
    {
        "id": "tboby.cwtools-vscode",
        "publisher": "tboby",
        "name": "cwtools-vscode",
        "version": "0.10.31",
        "url": "https://tboby.gallery.vsassets.io/_apis/public/gallery/publisher/tboby/extension/cwtools-vscode/0.10.31/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage",
        "folder_name": "tboby.cwtools-vscode-0.10.31"
    }
]

def install_extension(ext_info):
    target_folder = EXTENSIONS_DIR / ext_info["folder_name"]
    print(f"\n--- Installing {ext_info['id']} (v{ext_info['version']}) ---")
    
    if target_folder.exists():
        print(f"Target directory {target_folder} already exists. Skipping download.")
    else:
        print(f"Downloading from {ext_info['url']}...")
        req = urllib.request.Request(ext_info["url"], headers={"User-Agent": "VSCode"})
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
        print(f"Downloaded {len(data)} bytes. Extracting VSIX...")
        
        zf = zipfile.ZipFile(io.BytesIO(data))
        target_folder.mkdir(parents=True, exist_ok=True)
        
        prefix = "extension/"
        for member in zf.namelist():
            if member.startswith(prefix) and len(member) > len(prefix):
                rel_path = member[len(prefix):]
                dest_file = target_folder / rel_path
                if member.endswith("/"):
                    dest_file.mkdir(parents=True, exist_ok=True)
                else:
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(dest_file, "wb") as f_out:
                        f_out.write(zf.read(member))
        print(f"Successfully extracted to: {target_folder}")

    # Register in extensions.json
    register_in_json(ext_info)

def register_in_json(ext_info):
    if not EXT_JSON_PATH.exists():
        entries = []
    else:
        with open(EXT_JSON_PATH, "r", encoding="utf-8") as f:
            try:
                entries = json.load(f)
            except Exception:
                entries = []

    # Check if already present
    for e in entries:
        if e.get("identifier", {}).get("id", "").lower() == ext_info["id"].lower():
            print(f"Extension '{ext_info['id']}' is already registered in extensions.json.")
            return

    new_entry = {
        "identifier": {
            "id": ext_info["id"]
        },
        "version": ext_info["version"],
        "location": {
            "$mid": 1,
            "path": f"/c:/Users/Usuário/.antigravity-ide/extensions/{ext_info['folder_name']}",
            "scheme": "file"
        },
        "relativeLocation": ext_info["folder_name"],
        "metadata": {
            "installedTimestamp": int(time.time() * 1000),
            "pinned": False,
            "source": "gallery",
            "publisherDisplayName": ext_info["publisher"],
            "updated": False,
            "private": False,
            "isPreReleaseVersion": False,
            "hasPreReleaseVersion": False
        }
    }
    entries.append(new_entry)

    with open(EXT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print(f"Registered '{ext_info['id']}' in extensions.json.")

def main():
    EXTENSIONS_DIR.mkdir(parents=True, exist_ok=True)
    for ext in EXTENSIONS_TO_INSTALL:
        try:
            install_extension(ext)
        except Exception as e:
            print(f"Failed to install {ext['id']}: {e}")

    print("\nAll extensions processed successfully!")

if __name__ == "__main__":
    main()
