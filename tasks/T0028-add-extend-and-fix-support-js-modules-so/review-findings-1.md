---
task: T0028
round: 1
verdict: approved
blocking: 0
reviewer: "@gemini"
reviewed_at: 2026-11-23T07:49:16Z
reviewed_commit: "3747182"
base_commit: "7e6a96a"
branch: main
session: antigravity-20261123-0185a4
session_agent: antigravity
session_created_at: 2026-11-23T07:45:04Z
---
# Review Findings: Task T0028 (Round 1)

## Summary
Approved commit `3747182`. All code changes cleanly close the Auth reuse gaps identified in `technical-spec.md` while preserving backward compatibility for `counters` and existing consumers:

- `src/changelog-parser.mjs`: Strips emphasized `**[breaking]**` / `*[breaking]*` markers without leaving asterisks or gluing adjacent words, exposes `isPreRelease`, adds opt-in `stripPreSuffix` (default `false`), preserves the `'in development'` tag when `-pre` is stripped, and requires a `v` prefix on `## ` headings so non-version headings like `## Version History` and `## Next Steps` are skipped.
- `src/component.mjs`: Adds `static errorIconSprite = null`, `static errorIconId = 'icon-alert'`, and `static waitUIDelayTime = 700` with `createErrorIconHtml()` (HTML-escaping the `href` and retaining `.logo` for `css/component.css` grid layout), and fixes the malformed `</h2>` closing tag on the error overlay title.
- `src/forms.mjs`: Adopts Auth's `isValidEmailAddress` pattern so plus addressing and TLDs longer than three letters validate identically.
- Parity across `events.mjs`, `logs.mjs`, `dates.mjs`, `strings.mjs`, `math.mjs`, `dom.mjs`, and `app-view.mjs` was independently verified against Auth's copies and matches `docs/specs/code-reuse-opportunities.md`.
- Lockstep versions across `package.json`, `packages/words/package.json`, `package-lock.json`, and `CHANGELOG.md` agree at `3.1.0-pre`.

Verification run during review:
- `npm test`: passed (29 test files, 279 tests).
- `npm run lint`: passed (0 errors; 7 pre-existing warnings in untouched files).
- `python scripts/devops.py check`: passed (ESLint, Vitest, 15 pytest script tests, and workspace `npm pack`).
- `python scripts/devops.py versions`: passed (`3.1.0-pre` in lockstep).
- `npm run release-notes -- v3.1.0-pre`: passed.
- `.venv/Scripts/lint-markdown.exe check CHANGELOG.md docs/specs/code-reuse-opportunities.md`: 0 issues in edited sections (1 pre-existing HTTP 404 on `CHANGELOG.md:5`).

## Defects
None.

## Process Gaps
- **Non-blocking — Changelog bullet style**: Four of the six new `CHANGELOG.md` entries use present tense (`strips`, `marks`/`drops`, `skips`, `accepts`) and `Fix:`/`Feature:` prefixes rather than the past-tense `{{area}}: {{past-tense-outcome}}` convention used in prior `v3.0.0` entries; the three `parseChangelog` bullets could also be consolidated.
- **Non-blocking — Test numbering order**: In `tests/changelog-parser.test.mjs`, newly added tests `9.`–`13.` sit above existing test `8.`.
- **Informational — Release step pending confirmation**: The task goal mentions releasing a new version; keeping `3.1.0-pre` until review approval and explicit user confirmation (`**[Feedback Needed]**` in `technical-spec.md`) is appropriate under outbound publishing gates.

## Required Rework
None.
