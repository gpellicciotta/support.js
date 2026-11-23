#!/usr/bin/env python3
"""Runs the typical operations of this project on the shared support-python `DevopsCli`.

Run `python scripts/bootstrap-dev-environment.py` first to create `.venv` with the pinned support-python.

Usage:
  python scripts/devops.py lint | format | test | build | check | clean
  python scripts/devops.py versions [VERSION] [--dry-run]
  python scripts/devops.py release [--dry-run] [--skip-checks] [--skip-github-release] [--yes]
  python scripts/devops.py help [--verbose] | version
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Rerun with the project-local .venv (created by bootstrap-dev-environment.py), which holds the pinned support-python.
VENV_DIR = REPO_ROOT / ".venv"
VENV_PYTHON = VENV_DIR / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
if __name__ == "__main__" and VENV_PYTHON.is_file() and Path(sys.prefix).resolve() != VENV_DIR.resolve():
    sys.exit(subprocess.run([str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]], check=False).returncode)

from support_python.devops import DevopsCli, NodeProject, resolve_executable  # noqa: E402


class SupportJsProject(NodeProject):
    """The root package and the `packages/*` workspaces, packed together into `dist/` by `build`."""

    def build(self) -> bool:
        """Packs the root package and every workspace into `dist/`; return whether it succeeded."""
        npm = resolve_executable("npm")
        if npm is None:
            self.logger.error("npm not found on PATH; install Node.js with npm first.")
            return False
        self.remove_tree(self.dist_dir)
        self.dist_dir.mkdir(exist_ok=True)
        return self.run_command([npm, "pack", "--workspaces", "--include-workspace-root", "--pack-destination", "dist"])


def main() -> int:
    return DevopsCli(SupportJsProject(REPO_ROOT)).run()


if __name__ == "__main__":
    sys.exit(main())
