"""End-to-end checks of the dev scripts: they must run on support-python instead of duplicating it."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
PIN = "support-python @ git+https://github.com/gpellicciotta/support.python.git@v3.3.0"


def run_script(name: str, *args: str) -> subprocess.CompletedProcess:
    """Runs one script through its real entry point and captures its output."""
    return subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / name), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )


def test_requirements_pin_released_support_python() -> None:
    lines = (SCRIPTS_DIR / "requirements.txt").read_text(encoding="utf-8").splitlines()
    assert PIN in lines


def test_cli_common_duplicate_is_removed() -> None:
    assert not (SCRIPTS_DIR / "_cli_common.py").exists()


def test_devops_version_reports_package_version() -> None:
    expected = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    result = run_script("devops.py", "version")
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout


def test_devops_help_lists_shared_actions() -> None:
    result = run_script("devops.py", "help")
    assert result.returncode == 0, result.stderr
    for action in ("lint", "format", "test", "build", "check", "clean", "versions", "release"):
        assert action in result.stdout


def test_devops_unknown_action_exits_2() -> None:
    assert run_script("devops.py", "no-such-action").returncode == 2


def test_devops_versions_checks_package_and_changelog() -> None:
    result = run_script("devops.py", "versions")
    assert result.returncode == 0, result.stdout + result.stderr


def test_bootstrap_version_reports_package_version() -> None:
    expected = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))["version"]
    result = run_script("bootstrap-dev-environment.py", "--version")
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout
