#!/usr/bin/env python3
"""Bootstraps a fresh checkout of this project: installs dependencies, checks formatting, and runs tests.

Cross-platform; requires only Python and Node.js with npm on the PATH.

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

from _cli_common import build_action_parser, print_help, print_version

PROG = "bootstrap-dev-environment"
DESCRIPTION = "Installs npm dependencies, checks formatting, and runs the unit tests."
EXIT_CODES = [(0, "Success"), (1, "One or more bootstrap steps failed"), (2, "Invalid arguments")]
REPO_ROOT = Path(__file__).resolve().parent.parent


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
    ok = run_step("Installing dependencies (npm ci)", [npm, "ci"])
    ok = ok and run_step("Linting", [npm, "run", "lint"])
    ok = ok and run_step("Running unit tests", [npm, "test"])
    return 0 if ok else 1


def main() -> int:
    version = get_project_version()
    parser = build_action_parser(PROG, DESCRIPTION, ["setup", "version", "help"], "setup")
    args = parser.parse_args()

    if args.version or args.action == "version":
        print_version(PROG, version)
        return 0
    if args.help or args.action == "help":
        print_help(PROG, version, DESCRIPTION, parser, EXIT_CODES)
        return 0
    return setup()


if __name__ == "__main__":
    sys.exit(main())
