#!/usr/bin/env python3
"""Runs the typical operations of this project.

Run `python scripts/bootstrap-dev-environment.py` first to install the dependencies.

Usage:
  python scripts/devops.py lint
  python scripts/devops.py format
  python scripts/devops.py test
  python scripts/devops.py pack
  python scripts/devops.py check
  python scripts/devops.py --version
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from _cli_common import build_action_parser, print_help, print_version

PROG = "devops"
DESCRIPTION = "Runs format, test, and package operations of this project."
ACTIONS = ["lint", "format", "test", "pack", "check", "version", "help"]
EXIT_CODES = [(0, "Success"), (1, "An operation failed or dependencies are missing"), (2, "Invalid arguments")]
REPO_ROOT = Path(__file__).resolve().parent.parent


def get_project_version() -> str:
    """Resolves the current project version from package.json."""
    try:
        return json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    except (OSError, KeyError, ValueError):
        return "0.0.0+unknown"


def run(args: list) -> bool:
    """Runs one command in the repository root. Returns whether it succeeded."""
    print(f"[*] {' '.join(args)}", flush=True)
    return subprocess.run(args, cwd=str(REPO_ROOT), check=False).returncode == 0


def main() -> int:
    parser = build_action_parser(PROG, DESCRIPTION, ACTIONS, "help")
    args = parser.parse_args()
    version = get_project_version()

    if args.version or args.action == "version":
        print_version(PROG, version)
        return 0
    if args.help or args.action == "help":
        print_help(PROG, version, DESCRIPTION, parser, EXIT_CODES)
        return 0

    npm = shutil.which("npm")
    if npm is None or not (REPO_ROOT / "node_modules").exists():
        print("[!] npm or node_modules missing; run scripts/bootstrap-dev-environment.py first.", file=sys.stderr)
        return 1
    commands = {
        "lint": [[npm, "run", "lint"]],
        "format": [[npm, "run", "format"]],
        "test": [[npm, "test"]],
        "pack": [[npm, "pack", "--dry-run"]],
    }
    commands["check"] = commands["lint"] + commands["test"] + commands["pack"]
    return 0 if all(run(command) for command in commands[args.action]) else 1


if __name__ == "__main__":
    sys.exit(main())
