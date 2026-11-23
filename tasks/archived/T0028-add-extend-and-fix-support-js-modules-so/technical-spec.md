## Technical Specifications
Source: analysis task T0245 in the Auth repository, 2026-11-23.
Auth compares against `support.js` 3.0.0 (Auth's `webapp/package.json` range `^3.0.0`).

### Gap List
1. **Changelog parser: breaking marker bug.**
   - Auth CHANGELOG.md uses `- SPA: **[breaking]** Removed ...` since Auth commit 762a9d3.
   - Both parsers strip only `[breaking]`, leaving `**` `**` and showing `**** Removed ...` in the Help view.
   - Fix: strip `\*{0,2}\[breaking\]\*{0,2}`; keep accepting the bare form.
2. **Changelog parser: Auth features missing in support.js.**
   - `isPreRelease` field and `-pre` suffix stripped from `version`.
   - Heading form `## v1.1.2-pre` (`v` plus a digit; `## Version History` must not match).
   - Tag `in development` for pre-releases, `Released` otherwise.
   - counters consumes the support.js parser: keep its fields and output backward compatible.
3. **Component: Auth-specific constants.**
   - Auth's `component.mjs` reads `constants.LOOK_SPRITE` for the error icon and `constants.WAIT_UI_DELAY_TIME` for the wait overlay.
   - support.js hard-codes `DEFAULT_WAIT_UI_DELAY_TIME = 700` and has no sprite hook.
   - Add configuration (static or instance property) with the current behavior as default.
4. **Parity checks (expected equal; prove with tests; fix real gaps only).**
   - `events.mjs`: Auth copy differs by style only.
   - `logs.mjs`: superset of Auth's `log.mjs`. Auth uses `config`, `addLogHandler`, `defaultHandler`, `levelToLevelName`, `levelNameToLevel`, `INFO_LEVEL`, `Logger`, `error`, `warn`, `info`, `trace`.
   - `dates.mjs`: Auth uses `formatDateTime`, `formatRelativeDateTime`, `formatTimespan`, `dateAfterDays`; compare output for identical inputs.
   - `forms.mjs`: `isValidEmailAddress`, `isValidPassword`, `validPasswordDescription`.
   - `strings.mjs`: `escapeHtml`, `capitalize`, `uncapitalize`, `escapeRegex`.
   - `math.mjs`: `random`, `randomBoolean`.
   - `dom.mjs`: `htmlToElement`, `onDomReady`.
   - `app-view.mjs`: Auth's `AppView` constructor and default `routeRegex` must match.
5. **Out of scope.**
   - `AppBase` extraction from Auth's `app.mjs`.
   - Auth's `field-markup.mjs` and `relying-party.mjs` (Auth-specific).
   - Admin `api.mjs` and `real-api-server.mjs` fetch wrappers versus `net.mjs`: evaluate only if T0246 asks.

### Declared Files
- src/changelog-parser.mjs
- src/component.mjs
- tests/changelog-parser.test.mjs
- tests/component.test.mjs
- docs/specs/code-reuse-opportunities.md
- src/forms.mjs (parity gap, added during execution)
- tests/forms.test.mjs (parity gap, added during execution)
- tests/fixtures/auth-changelog.md (new fixture, uncounted)

Undeclared files are possible: parity gaps in other modules are unknown until the checks run. Log each one.

Mechanical command: python scripts/devops.py versions 3.1.0-pre
Mechanical files: package.json, packages/words/package.json, package-lock.json

### Tests
- Unit: `- SPA: **[breaking]** Text` parses to `isBreaking` true and text `Text` with no asterisks; `## v1.1.2-pre` yields `isPreRelease` true and version `1.1.2` with `stripPreSuffix` (counters keeps `1.1.2-pre` by default); Component honors a custom sprite and delay.
- Integration: parse Auth's real CHANGELOG.md, copied as a fixture, and assert no entry text contains `**`.

Completion check: `npm test` and `npm run lint` in the support.js root.

### Release and Consumption
- **[Feedback Needed]** Auth consumes `@gpellicciotta/support.js` from npm. Release a new version (suggest 3.1.0) before T0246 starts, or let T0246 resolve a sibling checkout like counters' Gradle fallback.
