#!/usr/bin/env python3
"""Bootstraps a fresh checkout of this project: creates `.venv` with the pinned support-python,
installs the npm dependencies, then runs `devops.py check`.

Standard library only, so it runs on a bare checkout before support-python is installed.
Cross-platform; requires Python and Node.js with npm on the PATH.

Usage:
  python scripts/bootstrap-dev-environment.py
  python scripts/bootstrap-dev-environment.py --version
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

PROG = "bootstrap-dev-environment"
APP_AUTHOR = "Giovanni Pellicciotta"
REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS_FILE = REPO_ROOT / "scripts" / "requirements.txt"
VENV_DIR = REPO_ROOT / ".venv"
VENV_PYTHON = VENV_DIR / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


HELP = """{prog} v{version} - Copyright (c) {author}

Creates .venv with the pinned support-python, installs the npm dependencies, then runs `devops.py check`.

usage: {prog} [setup | version | help] [-h] [-v]

actions:
  setup          Bootstrap the checkout (default)
  version        Show version information and exit
  help           Show this help message and exit

options:
  -h, --help     Show this help message and exit
  -v, --version  Show version information and exit

Exit codes:
  0  Success
  1  One or more bootstrap steps failed
  2  Invalid arguments"""


def get_project_version() -> str:
    """Resolves the current project version from package.json."""
    try:
        return json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    except (OSError, KeyError, ValueError):
        return "0.0.0+unknown"


def run_step(description: str, args: list) -> bool:
    """Runs one bootstrap step, printing its outcome. Returns whether it succeeded."""
    print(f"\n[*] {description}", flush=True)
    print("=" * 60, flush=True)
    result = subprocess.run(args, cwd=str(REPO_ROOT), check=False)
    if result.returncode != 0:
        print(f"[!] {description} failed (exit code {result.returncode})", flush=True)
    return result.returncode == 0


def setup() -> int:
    npm = shutil.which("npm")
    if npm is None:
        print("[!] npm not found on the PATH; install Node.js LTS first.", file=sys.stderr)
        return 1
    ok = True
    if not VENV_PYTHON.is_file():
        ok = run_step("Creating .venv", [sys.executable, "-m", "venv", str(VENV_DIR)])
    ok = ok and run_step(
        "Installing scripts/requirements.txt into .venv",
        [str(VENV_PYTHON), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "-r", str(REQUIREMENTS_FILE)],
    )
    ok = ok and run_step("Installing dependencies (npm ci)", [npm, "ci"])
    ok = ok and run_step("Linting and testing", [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "devops.py"), "check"])
    return 0 if ok else 1


def main() -> int:
    args = sys.argv[1:]
    if args in (["-v"], ["--version"], ["version"]):
        print(f"{PROG} v{get_project_version()} - Copyright (c) {APP_AUTHOR}")
        return 0
    if args in (["-h"], ["--help"], ["help"]):
        print(HELP.format(prog=PROG, version=get_project_version(), author=APP_AUTHOR))
        return 0
    if args and args != ["setup"]:
        print(f"[!] Unknown arguments: {' '.join(args)}; see --help.", file=sys.stderr)
        return 2
    return setup()


if __name__ == "__main__":
    sys.exit(main())
