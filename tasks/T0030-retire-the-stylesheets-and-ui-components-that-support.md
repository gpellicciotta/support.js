---
id: T0030
owner: "@gemini"
needs: []
branch: —
worktree: —
status: active
started_at: "2026-11-23T09:24:26Z"
ended_at: —
review: agent
preview: none
protocol: standard
review_status: pending
review_round: 1
review_requested_at: "2026-11-23T09:27:57Z"
---
# T0030: Retire the stylesheets and UI components that support.webapp provides, keeping support.js non-UI only

## Goals
Make support.js a non-UI package: remove every stylesheet and UI component that support.webapp now provides.
Start only after counters, auth, and hinolugi-utils load none of the retired files; the consumer inventory proves it.
Keep the non-UI parts of mixed modules, such as the validators in `src/forms.mjs`.
Decide each graphics, DOM-helper, and image module with the user before removing it.
Release the result as support.js v4.0.0, with a migration note mapping each removal to its support.webapp replacement.
Size estimate: 8 files, 300 lines.

## Task Execution Steps
- [x] **[Read]**      Read the removal list in the technical specification and the support.webapp catalog it maps to.
- [x] **[Verify]**    Inventory sibling repositories importing each retired file; stop if any consumer remains.
- [x] **[Decide]**    Confirm with the user the fate of each module marked "Decide" in the specification.
- [x] **[Implement]** Author a failing package test asserting no CSS export, `css/` folder, or retired module.
- [x] **[Verify]**    Run the package test and record the expected failures.
- [x] **[Implement]** Delete the retired stylesheets, modules, tests, and exports until the package test passes.
- [x] **[Implement]** Split `src/forms.mjs`, keeping the validators and their tests, and dropping the DOM helpers.
- [x] **[Doc]**       Update README, requirements, devops guide, and specs; drop the visual style guide.
- [x] **[Doc]**       Write the migration note and the breaking CHANGELOG entry, then bump to v4.0.0.
- [x] **[Verify]**    Run `python scripts/devops.py check` and pack the package to confirm its file list.
- [ ] **[Review]**    Obtain review approval of the finished work before completion.

## Execution Log
- [2026-11-23] **[Doc]**
  Companion task file scaffolded at task creation.

- [2026-11-23] **[Decided]**
  Confirmed removal of reorder.mjs, installer.mjs, and img/, while keeping dom.mjs, canvas.mjs, fireworks.mjs, and snowflakes.mjs.
  - Skipped sibling prerequisite checks per user instruction as v3.1.0 remains available.

- [2026-11-23] **[Implement]**
  Removed retired CSS, img, and UI modules, split forms.mjs to retain pure validators, and added package surface test.

- [2026-11-23] **[Doc]**
  Updated documentation, added v4.0.0 migration table, and bumped version to 4.0.0-pre across workspaces.

- [2026-11-23] **[Verify]**
  Verified devops check, markdown table alignment, and npm pack output.
  - 20 test files (195 tests) and 15 script tests passed.
  - Tarball contains 25 files with no css/, img/, or retired UI modules.

- [2026-11-23] **[Verify]**
  Recorded task outcomes.
  - Files touched: 9.
  - Lines touched: 721.
  - Reopenings: 0.
  - Size note: 9 modified files and 721 lines due to 607 deleted lines in forms.mjs.

- [2026-11-23] **[Review]**
  Round 1 requested (mode: agent).

