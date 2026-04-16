#!/usr/bin/env python3
"""
Install the commit-msg git hook into this repository.
Usage: python install_hook.py
"""

import shutil
import os
import sys
import stat
from pathlib import Path


def install_hook():
    repo_root = Path(__file__).parent
    git_dir = repo_root / ".git"

    if not git_dir.exists():
        print("❌ No .git directory found. Are you inside a git repository?")
        sys.exit(1)

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)

    src = repo_root / "hooks" / "commit-msg"
    dst = hooks_dir / "commit-msg"

    if dst.exists():
        backup = hooks_dir / "commit-msg.bak"
        shutil.copy2(dst, backup)
        print(f"  📦 Backed up existing hook to: {backup}")

    shutil.copy2(src, dst)

    # Make executable
    st = os.stat(dst)
    os.chmod(dst, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    print(f"✅ commit-msg hook installed successfully at: {dst}")
    print("   Your commits will now be validated automatically.")


if __name__ == "__main__":
    install_hook()
