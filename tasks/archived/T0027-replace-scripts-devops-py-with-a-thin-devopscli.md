---
id: T0027
owner: ~
needs: []
branch: —
worktree: —
status: cancelled
started_at: —
ended_at: "2026-11-23T07:06:10Z"
review: agent
preview: none
protocol: standard
---
# T0027: Replace scripts/devops.py with a thin DevopsCli script on the NodeProject adapter, pinning the released support-python v2.0.0

## Goals
Needs the released support-python v2.0.0; see `docs/migration-v2.md` in support-python for the full mapping.
Replace `scripts/devops.py` with a thin script running `DevopsCli(NodeProject(REPO_ROOT)).run()`.
Pin `support-python @ git+https://github.com/gpellicciotta/support.python.git@v2.0.0` in `scripts/requirements.txt`.
Keep project-specific actions through `DevopsCli.add_action`.

## Task Execution Steps
- [ ] **[Implement]** Implement required changes for T0027.
- [ ] **[Verify]**    Verify implementation with automated test suites.
- [ ] **[Doc]**       Update documentation and CHANGELOG.md.
- [ ] **[Review]**    Obtain review approval of the finished work before completion.

## Execution Log
- [2026-11-10] **[Doc]**
  Companion task file scaffolded at task creation.

- [2026-11-23] **[Cancelled]**
  Superseded by T0029, which targets support-python v3.3.0.

