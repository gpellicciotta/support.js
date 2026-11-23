"""End-to-end checks of the dev scripts: they must run on support-python instead of duplicating it."""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

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


def load_devops_module():
    """Imports scripts/devops.py in-process; needs support-python, so it skips outside the project venv."""
    pytest.importorskip("support_python")
    spec = importlib.util.spec_from_file_location("devops_script", SCRIPTS_DIR / "devops.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy_manifests(target: Path) -> None:
    """Copies the files that carry versions into an isolated temporary repository."""
    for name in ("package.json", "package-lock.json", "CHANGELOG.md", "packages/words/package.json"):
        (target / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / name, target / name)


def read_versions(root: Path) -> dict:
    """Returns the version recorded in each lockstep file."""
    lock = json.loads((root / "package-lock.json").read_text(encoding="utf-8"))
    return {
        "root": json.loads((root / "package.json").read_text(encoding="utf-8"))["version"],
        "words": json.loads((root / "packages/words/package.json").read_text(encoding="utf-8"))["version"],
        "lock": lock["version"],
        "lock-root": lock["packages"][""]["version"],
        "lock-words": lock["packages"]["packages/words"]["version"],
        "changelog": re.search(r"^## v(\S+)", (root / "CHANGELOG.md").read_text(encoding="utf-8"), re.MULTILINE).group(1),
    }


def test_changelog_has_separator_for_next_development_heading() -> None:
    release = pytest.importorskip("support_python.devops.release")
    text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## v9.9.9-pre" in release.open_dev_changelog(text, "9.9.9-pre")


def test_devops_release_is_refused() -> None:
    result = run_script("devops.py", "release", "--dry-run")
    assert result.returncode == 1
    assert "not supported" in result.stdout + result.stderr


def test_set_version_updates_all_lockstep_files(tmp_path: Path) -> None:
    devops = load_devops_module()
    copy_manifests(tmp_path)
    assert devops.SupportJsProject(tmp_path).set_version("7.8.9")
    assert set(read_versions(tmp_path).values()) == {"7.8.9-pre"}


def test_set_version_dry_run_changes_nothing(tmp_path: Path) -> None:
    devops = load_devops_module()
    copy_manifests(tmp_path)
    before = read_versions(tmp_path)
    assert devops.SupportJsProject(tmp_path).set_version("7.8.9", dry_run=True)
    assert read_versions(tmp_path) == before


def test_set_version_keeps_lock_file_format(tmp_path: Path) -> None:
    devops = load_devops_module()
    copy_manifests(tmp_path)
    original = (tmp_path / "package-lock.json").read_text(encoding="utf-8")
    current = read_versions(tmp_path)["root"]
    assert devops.SupportJsProject(tmp_path).set_version("7.8.9")
    updated = (tmp_path / "package-lock.json").read_text(encoding="utf-8")
    assert updated == original.replace(f'"version": "{current}"', '"version": "7.8.9-pre"')


def test_bootstrap_help_lists_actions_and_exit_codes() -> None:
    result = run_script("bootstrap-dev-environment.py", "--help")
    assert result.returncode == 0, result.stderr
    for text in ("setup", "--version", "Exit codes:", "2  Invalid arguments"):
        assert text in result.stdout
