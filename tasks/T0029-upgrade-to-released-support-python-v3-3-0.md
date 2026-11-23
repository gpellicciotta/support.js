---
id: T0029
owner: "@claude-code"
needs: []
branch: —
worktree: —
status: active
started_at: "2026-11-23T07:06:12Z"
ended_at: —
review: agent
preview: none
protocol: standard
review_status: pending
review_round: 1
review_requested_at: "2026-11-23T07:09:40Z"
---
# T0029: Upgrade to released support-python v3.3.0 and replace duplicated script code with its shared modules

## Goals
Supersedes T0027, which pins the outdated v2.0.0; migrate through `docs/migration-v2.md` and `docs/migration-v3.md` in support-python.
Pin `support-python @ git+https://github.com/gpellicciotta/support.python.git@v3.3.0` in `scripts/requirements.txt`.
Replace `scripts/devops.py`, `scripts/_cli_common.py`, and `scripts/bootstrap-dev-environment.py` with thin scripts on `DevopsCli(NodeProject(REPO_ROOT))`.
Keep project-specific actions through `DevopsCli.add_action`; delete all duplicated boilerplate.
Completion check: `python scripts/devops.py check`
Size estimate: 4 files, 200 lines

## Task Execution Steps
- [x] **[Read]**      Inventory duplicated code in scripts/ against support-python v3.3.0 modules.
- [x] **[Implement]** Replace the script boilerplate with DevopsCli and pin v3.3.0.
- [x] **[Verify]**    Run `python scripts/devops.py check` and confirm lint, tests, and pack pass.
- [x] **[Doc]**       Update documentation and CHANGELOG.md.
- [ ] **[Review]**    Obtain review approval of the finished work before completion.

## Execution Log
- [2026-11-23] **[Doc]**
  Companion task file scaffolded at task creation.

- [2026-11-23] **[Implement]**
  Moved devops.py onto DevopsCli and NodeProject, pinned v3.3.0, and removed _cli_common.py.

- [2026-11-23] **[Verify]**
  Pytest script tests and devops check passed.
  - 7 pytest tests passed.
  - 267 vitest tests passed.

- [2026-11-23] **[Review]**
  Round 1 requested (mode: agent).

