---
id: T0028
owner: "@claude-code"
needs: []
branch: —
worktree: —
status: completed
started_at: "2026-11-23T07:35:24Z"
ended_at: "2026-11-23T09:04:33Z"
review: agent
preview: none
protocol: standard
review_status: approved
review_round: 2
review_requested_at: "2026-11-23T09:02:32Z"
review_session: antigravity-20261123-4257c1
reviewed_by: "@gemini"
completion-commit: f8cabb7a2ba1610c37ed04b4793e7f6ba2c84eee
---
# T0028: Add, extend, and fix support.js modules so Auth can reuse them, starting with the changelog parser

## Goals
Close the gaps that stop Auth from replacing its copied JS utilities with support.js modules; Auth task T0246 consumes the result.
Port Auth's newer changelog parser features and fix the `**[breaking]**` marker bug that leaves `****` in help text.
Make `Component` configurable for the error-icon sprite and wait delay, which Auth hard-codes today.
Prove parity of events, logs, dates, forms, strings, and math against Auth's copies, fixing only real gaps.
Release the result as a new support.js version.
Size estimate: 5 files, 250 lines.
Combined task: Auth cannot start T0246 until all gaps ship in one released version.

## Task Execution Steps
- [x] **[Read]**      Read the gap list in the technical specification and the Auth copies it names.
- [x] **[Implement]** Author failing parser tests: bold breaking marker, `-pre` suffix, and `## v` headings.
- [x] **[Verify]**    Run the parser tests and record the expected failures.
- [x] **[Implement]** Fix and extend `src/changelog-parser.mjs` until its tests pass.
- [x] **[Implement]** Author failing Component tests for configurable error-icon markup and wait delay.
- [x] **[Verify]**    Run the Component tests and record the expected failures.
- [x] **[Implement]** Add the Component hooks with backward-compatible defaults until the tests pass.
- [x] **[Verify]**    Run Auth-derived parity tests for events, logs, dates, forms, strings, and math.
- [x] **[Implement]** Fix each parity gap found, test first, and log each gap.
- [x] **[Verify]**    Run `npm test` and `npm run lint` and confirm both pass.
- [x] **[Doc]**       Update CHANGELOG.md and the code-reuse specification.
- [x] **[Review]**    Obtain review approval of the finished work before completion.

## Execution Log
- [2026-11-23] **[Doc]**
  Companion task file scaffolded at task creation.

- [2026-11-23] **[Decided]**
  Kept version suffix by default for counters; added isPreRelease and opt-in stripPreSuffix for Auth's stripped versions.

- [2026-11-23] **[Decided]**
  Second-level headings now need a v prefix, so '## Next Steps' no longer starts a release; no sibling changelog relied on that.

- [2026-11-23] **[Implement]**
  Fixed the Component error title closing tag, which nested the description inside the title; found while adding the sprite hook.

- [2026-11-23] **[Implement]**
  Parity gap: isValidEmailAddress rejected plus addressing and long TLDs; adopted Auth's pattern.
  - Undeclared files: src/forms.mjs, tests/forms.test.mjs.
  - Other modules: style differences only.

- [2026-11-23] **[Implement]**
  Bumped versions to 3.1.0-pre with devops.py versions, declared as a mechanical change.

- [2026-11-23] **[Review]**
  Dispatched agy review round 1 in background.
  - Command: plan agents review T0028 --agent agy --yes --timeout 45m.
  - Task ID: bgykke3yo.

- [2026-11-23] **[Review]**
  Round 1 requested (mode: agent).

- [2026-11-23] **[Review]**
  Relaunched agy review without --yes, which requires --complete.
  - Command: plan agents review T0028 --agent agy --timeout 45m.
  - Task ID: bc8xf60mh.

- [2026-11-23] **[Review]**
  Round 1 approved by @gemini: Approved commit `3747182`.
  - Findings: [review-findings-1.md](T0028-add-extend-and-fix-support-js-modules-so/review-findings-1.md).

- [2026-11-23] **[Review]**
  agy approved round 1 with no defects; applied both non-blocking notes on changelog tense and test order.
  - npm test: 279 passed; lint: 0 errors.

- [2026-11-23] **[Verify]**
  Recorded task outcomes.
  - Files touched: 7.
  - Lines touched: 246.
  - Reopenings: 0.

- [2026-11-23] **[Review]**
  Round 2 requested (mode: agent); the work changed after the round 1 approval of commit 3747182.

- [2026-11-23] **[Review]**
  Round 2 approved by @gemini: Approved commits `3747182` and `f8cabb7`.
  - Findings: [review-findings-2.md](T0028-add-extend-and-fix-support-js-modules-so/review-findings-2.md).

- [2026-11-23] **[Complete]**
  Task completed successfully.

