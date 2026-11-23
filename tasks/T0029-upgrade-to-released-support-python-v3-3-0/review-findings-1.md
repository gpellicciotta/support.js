---
task: T0029
round: 1
verdict: rejected
blocking: 2
reviewer: "@gemini"
reviewed_at: 2026-11-23T07:09:48Z
reviewed_commit: "51144c8"
base_commit: "7738fab"
branch: main
---
# Review Findings: Task T0029 (Round 1)

## Summary
Reviewed commit `51144c8` on `main` (base `7738fab`, clean working tree).
Pinning `support-python` v3.3.0 in `scripts/requirements.txt`, removing `scripts/_cli_common.py`, adding `.venv` re-execution in `scripts/devops.py`, and running `lint`, `test`, and workspace `build` work cleanly:
- `.venv/Scripts/python.exe -m pytest scripts/tests -v`: 7 passed.
- `python scripts/devops.py check`: ESLint (0 errors, 7 pre-existing warnings), Vitest (29 files, 267 tests passed), and `npm pack --workspaces --include-workspace-root --pack-destination dist` all passed.
- `lint-markdown check --offline`: 12 files passed.

Rejected because the newly exposed `versions` and `release` actions in `scripts/devops.py` are broken for this workspace monorepo: `release` crashes mid-release on `CHANGELOG.md` and leaves `@gpellicciotta/support-words.js` at `-pre` during release freeze and publication.

## Defects
1. **[Blocking] `devops.py release` crashes mid-release because `CHANGELOG.md` lacks a `---` separator.**
   - `scripts/devops.py` exposes `release` via `DevopsCli`, which delegates to `support_python.devops.ReleasePipeline`.
   - After freezing, tagging, pushing `main` and the tag, and publishing the GitHub Release, `ReleasePipeline` calls `open_dev_changelog()`, which requires a `^---` line in `CHANGELOG.md`.
   - `CHANGELOG.md` has no `---` separator between its preamble and `## v3.0.1-pre`. Calling `open_dev_changelog(Path('CHANGELOG.md').read_text(encoding='utf-8'), '3.0.2-pre')` directly raises `ValueError: No '---' separator line in CHANGELOG.md`.
   - `python scripts/devops.py release --dry-run` exits `0` without evaluating `open_dev_changelog`, masking this failure until an irreversible real release fails partway through.

2. **[Blocking] `devops.py versions` and `devops.py release` break lockstep versioning across `packages/words/package.json` and `package-lock.json`.**
   - `support.js` is an npm workspaces monorepo with two lockstep packages (`package.json` and `packages/words/package.json`, both tracked in `package-lock.json`), packed together by `SupportJsProject.build()` and published together by `.github/workflows/publish.yml` (`npm publish --workspaces --include-workspace-root`).
   - Both `docs/devops.md` (line 68) and `change-management-guidelines` require lockstep version synchronization and pre-flight parity checks across all package manifests.
   - `SupportJsProject` only overrides `build()`, leaving `versions` and `release` on stock `NodeProject` / `ReleasePipeline`, which only inspect and edit root `package.json`:
     - `devops.py versions` does not check `packages/words/package.json` for version drift.
     - `devops.py versions VERSION` updates only `package.json` and `CHANGELOG.md`, leaving `packages/words/package.json` and `package-lock.json` stale and breaking lockstep.
     - `devops.py release` freezes and commits only `CHANGELOG.md` and `package.json`; post-freeze `build()` then packs `gpellicciotta-support-words.js-<ver>-pre.tgz` alongside `gpellicciotta-support.js-<ver>.tgz`, attaches the `-pre` tarball to the release, and causes `.github/workflows/publish.yml` to publish `@gpellicciotta/support-words.js` at a `-pre` version on a stable release tag. Reopening the next `-pre` version likewise skips `packages/words/package.json` and `package-lock.json`.

## Process Gaps
- `CHANGELOG.md` formatting (`change-management-guidelines`): bullet 1 under `## v3.0.1-pre` is 28 words (cap is 20 words), and existing local files `scripts/requirements.txt` and `bootstrap-dev-environment.py` use code spans instead of Markdown links.
- `scripts/bootstrap-dev-environment.py --help` (`cli-guidelines`): prints only `__doc__`, omitting the version header, subcommands (`setup`, `version`, `help`), options (`-h`, `--help`, `-v`, `--version`), and exit codes (`0`, `1`, `2`) previously printed by `_cli_common.print_help`.
- `docs/devops.md` synchronization (`project-setup-guidelines`): `Development Workflows` advertises `python scripts/devops.py release`, while `## Release Process` still describes only the manual 5-step procedure without reconciling `devops.py release` and `devops.py versions`.
- Test coverage: `python scripts/devops.py test` and `check` do not run `scripts/tests/test_scripts.py`, and script tests do not cover `SupportJsProject.build()`, lockstep `versions`, or `release` planning/changelog editing.

## Required Rework
1. Add the `---` separator between the `CHANGELOG.md` preamble and `## v3.0.1-pre` so `support_python.devops.open_dev_changelog` succeeds, and verify with `lint-markdown check --offline`.
2. Make `scripts/devops.py` enforce lockstep versioning across `package.json`, `packages/words/package.json`, and `package-lock.json`:
   - `versions` (check mode) must detect and fail (exit `1`) on drift in `packages/words/package.json` (and `package-lock.json` root/workspace versions if tracked).
   - `versions VERSION [--dry-run]` must update `package.json`, `packages/words/package.json`, `package-lock.json`, and `CHANGELOG.md` together (and report all targets in `--dry-run`).
   - `release` must update and stage `packages/words/package.json` (and `package-lock.json`) in both the freeze commit and the next `-pre` development commit so post-freeze `build()` and `publish.yml` never package or publish a `-pre` workspace tarball.
3. Add automated tests in `scripts/tests/test_scripts.py` (using isolated temp copies or stubs) proving:
   - `open_dev_changelog` succeeds on the real `CHANGELOG.md`.
   - `versions` detects drift in `packages/words/package.json`, and `versions VERSION` updates all manifests in lockstep.
   - `release` plans/performs lockstep updates on both freeze and reopen commits.
4. Address the changelog style issues in `CHANGELOG.md` (<= 20-word bullets, Markdown links for existing repo files) and align `docs/devops.md` `## Release Process` and `scripts/bootstrap-dev-environment.py --help` with the new CLI behavior.
