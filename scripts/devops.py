#!/usr/bin/env python3
"""Runs the typical operations of this project on the shared support-python `DevopsCli`.

Run `python scripts/bootstrap-dev-environment.py` first to create `.venv` with the pinned support-python.

Usage:
  python scripts/devops.py lint | format | test | build | check | clean
  python scripts/devops.py versions [VERSION] [--dry-run]
  python scripts/devops.py help [--verbose] | version

The `release` action is refused; see docs/devops.md for the manual release process.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent

# Rerun with the project-local .venv (created by bootstrap-dev-environment.py), which holds the pinned support-python.
VENV_DIR = REPO_ROOT / ".venv"
VENV_PYTHON = VENV_DIR / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
if __name__ == "__main__" and VENV_PYTHON.is_file() and Path(sys.prefix).resolve() != VENV_DIR.resolve():
    sys.exit(subprocess.run([str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]], check=False).returncode)

from support_python.devops import DevopsCli, NodeProject, read_version, resolve_executable  # noqa: E402

# Manifests that must carry the root version besides the root package.json.
WORKSPACE_VERSION_FILES = ("packages/words/package.json", "package-lock.json")


class SupportJsProject(NodeProject):
    """The root package and the `packages/*` workspaces, which share one lockstep version.

    - `build` packs the root package and every workspace into `dist/`.
    - `test` also runs the pytest suite of these scripts.
    - `versions VERSION` also sets the workspace manifests and `package-lock.json`.
    - `release` is refused: the shared pipeline would freeze only the root manifest.
    """

    def test(self, selection: Sequence[str] = ()) -> bool:
        """Runs `npm test`, then the script tests when no selection narrows the run."""
        if not super().test(selection):
            return False
        return bool(selection) or self.run_command([sys.executable, "-m", "pytest", "-q", "scripts/tests"])

    def build(self) -> bool:
        """Packs the root package and every workspace into `dist/`; return whether it succeeded."""
        npm = resolve_executable("npm")
        if npm is None:
            self.logger.error("npm not found on PATH; install Node.js with npm first.")
            return False
        self.remove_tree(self.dist_dir)
        self.dist_dir.mkdir(exist_ok=True)
        return self.run_command([npm, "pack", "--workspaces", "--include-workspace-root", "--pack-destination", "dist"])

    def set_version(self, version: str, *, dry_run: bool = False) -> bool:
        """Sets the root manifest and changelog, then the workspace manifests and lock file in lockstep."""
        if not super().set_version(version, dry_run=dry_run):
            return False
        if dry_run:
            self.logger.info(f"Would set {', '.join(WORKSPACE_VERSION_FILES)} to the same version.")
            return True
        target = read_version(self.root)
        try:
            for name in WORKSPACE_VERSION_FILES:
                path = self.root / name
                data = json.loads(path.read_text(encoding="utf-8"))
                data["version"] = target
                for key, entry in data.get("packages", {}).items():
                    if key == "" or key.startswith("packages/"):
                        entry["version"] = target
                path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        except (OSError, ValueError) as exc:
            self.logger.error(str(exc))
            return False
        return True

    def release(
        self, *, dry_run: bool = False, assume_yes: bool = False, skip_checks: bool = False, skip_github_release: bool = False
    ) -> Optional[bool]:
        """Refuses to release: follow the manual Release Process in docs/devops.md instead."""
        self.logger.error("release is not supported for this workspace monorepo; follow the Release Process in docs/devops.md.")
        return False


def main() -> int:
    return DevopsCli(SupportJsProject(REPO_ROOT)).run()


if __name__ == "__main__":
    sys.exit(main())
