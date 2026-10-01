#!/usr/bin/env python3
"""
HOI4 Steam Workshop High-Speed Synchronization
Uses Robocopy to mirror the verified mod files to the active Steam Workshop folder,
excluding developer artifacts (.git, tests, scratch, .py files).
"""

import sys
import subprocess
import argparse
from pathlib import Path

def sync_mod(src_dir, dest_dir):
    src = Path(src_dir).resolve()
    dest = Path(dest_dir).resolve()

    if not src.exists():
        print(f"Error: Source directory '{src}' does not exist.")
        sys.exit(1)

    dest.mkdir(parents=True, exist_ok=True)

    cmd = [
        "robocopy",
        str(src),
        str(dest),
        "/MIR",
        "/FFT",
        "/R:2",
        "/W:2",
        "/XD", ".git", ".agents", "tests", "scratch", "__pycache__", ".vscode",
        "/XF", "*.py", "*.pyc", "*.log", "*.tmp", ".gitignore"
    ]

    print(f"Mirroring mod files from '{src}' -> '{dest}'...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    # In Robocopy, exit codes 0 to 7 indicate successful synchronization (0=no change, 1=copied, etc.)
    # Exit codes 8 or higher indicate fatal error.
    if res.returncode >= 8:
        print(f"Robocopy failed with exit code {res.returncode}:")
        print(res.stdout)
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"Synchronization SUCCESSFUL! Robocopy exit code: {res.returncode}")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="HOI4 Steam Workshop Sync Tool")
    parser.add_argument("--src", required=True, help="Path to working mod directory")
    parser.add_argument("--dest", required=True, help="Path to Steam workshop content directory")
    args = parser.parse_args()

    sync_mod(args.src, args.dest)

if __name__ == "__main__":
    main()
