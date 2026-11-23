## Walkthrough & Validation

### Key Changes
- `parseChangelog` strips `**[breaking]**`, adds `isPreRelease`, and takes an opt-in `stripPreSuffix`.
- Second-level headings need a `v` prefix, so `## Next Steps` no longer opens a release.
- `Component` has static `errorIconSprite`, `errorIconId`, and `waitUIDelayTime`; defaults are unchanged.
- The `Component` error title now closes with `</h1>`, not `</h2>`.
- `isValidEmailAddress` uses Auth's pattern, the only parity gap found.
- Versions moved to 3.1.0-pre with `python scripts/devops.py versions 3.1.0-pre`.

### Red Phase: Parser Tests
Command (summary lines filtered by `Select-String -Pattern "FAIL|Tests |Test Files|❯ tests/"`):
`npx vitest run tests/changelog-parser.test.mjs` exit code 1

```text
 ❯ tests/changelog-parser.test.mjs (13 tests | 5 failed) 29ms
 FAIL  tests/changelog-parser.test.mjs > Changelog Parser Suite > 9. Strips a bold **[breaking]** marker without leaving asterisks behind
 ❯ tests/changelog-parser.test.mjs:133:12
 Test Files  1 failed (1)
      Tests  5 failed | 8 passed (13)
 FAIL  tests/changelog-parser.test.mjs > Changelog Parser Suite > 10. Marks -pre versions with isPreRelease and keeps the suffix in version by default
 ❯ tests/changelog-parser.test.mjs:155:12
 FAIL  tests/changelog-parser.test.mjs > Changelog Parser Suite > 11. Strips the -pre suffix from version when stripPreSuffix is set
 ❯ tests/changelog-parser.test.mjs:165:12
 FAIL  tests/changelog-parser.test.mjs > Changelog Parser Suite > 12. Accepts second-level headings only with a v prefix and a digit or Next
 ❯ tests/changelog-parser.test.mjs:186:12
 FAIL  tests/changelog-parser.test.mjs > Changelog Parser Suite > 13. Parses the Auth CHANGELOG.md fixture without leaving asterisks in entry text
 ❯ tests/changelog-parser.test.mjs:194:12
```

### Red Phase: Component Tests
Command (same filter): `npx vitest run tests/component.test.mjs` exit code 1

```text
 ❯ tests/component.test.mjs (18 tests | 5 failed) 30ms
 FAIL  tests/component.test.mjs > configurable error icon > the default error overlay shows the text logo, and its title heading closes properly
 ❯ tests/component.test.mjs:271:12
 FAIL  tests/component.test.mjs > configurable error icon > a subclass with errorIconSprite shows the sprite's alert icon instead of the text logo
 ❯ tests/component.test.mjs:280:12
 FAIL  tests/component.test.mjs > configurable error icon > errorIconId selects another symbol from the sprite
 ❯ tests/component.test.mjs:291:12
 FAIL  tests/component.test.mjs > configurable error icon > the base class defaults keep the current behavior
 ❯ tests/component.test.mjs:295:12
 FAIL  tests/component.test.mjs > configurable wait overlay delay > a subclass with waitUIDelayTime shows the wait overlay after its own delay
 ❯ tests/component.test.mjs:330:12
 Test Files  1 failed (1)
      Tests  5 failed | 13 passed (18)
```

### Parity Check Against Auth
A scratch script called Auth's and support.js functions with identical inputs.
Inputs covered `formatDateTime`, `formatRelativeDateTime`, `formatTimespan`, `dateAfterDays`, the form validators, the string helpers, and the log level helpers.
Command: `node behavior.mjs C:/Dev-Projects/auth C:/Dev-Projects/support.js` exit code 0, before the fix:

```text
DIFF isValidEmailAddress("user+tag@example.com"): auth=true support=false
DIFF isValidEmailAddress("first.last@sub.example.info"): auth=true support=false
DIFF isValidEmailAddress("x@example.technology"): auth=true support=false
behavior diffs: 3
```

A source comparison of `events`, `log`, and `dom` exports found only style differences (`let` versus `const`, quotes, `Object.hasOwn`).
`AppView`'s constructor and default `routeRegex` match by reading; support.js only adds `ctxActionBarId`.

### Red Phase: Email Parity Test
Command (same filter): `npx vitest run tests/forms.test.mjs` exit code 1

```text
 ❯ tests/forms.test.mjs (24 tests | 1 failed) 38ms
 FAIL  tests/forms.test.mjs > validation helpers > isValidEmailAddress accepts plus addressing and long top-level domains, like Auth
 ❯ tests/forms.test.mjs:354:12
 Test Files  1 failed (1)
      Tests  1 failed | 23 passed (24)
```

After the fix, the same parity command exited 0:

```text
behavior diffs: 0
```

### Consumer Compatibility
Auth's and counters' own parser tests were copied to the scratchpad with imports pointed at `src/changelog-parser.mjs`.
Auth's copy passes `{ stripPreSuffix: true }`; counters' copy uses the defaults.
Command (filtered with `grep -E "^# |^not ok|^ok"`): `node --test auth-parser.test.mjs counters-parser.test.mjs` exit code 0

```text
# Subtest: Changelog Parser Suite
ok 1 - Changelog Parser Suite
# Subtest: Changelog Parser Suite
ok 2 - Changelog Parser Suite
# tests 16
# suites 2
# pass 16
# fail 0
# cancelled 0
# skipped 0
# todo 0
```

### Green Phase: Completion Check
Command: `npm test` exit code 0

```text
> @gpellicciotta/support.js@3.1.0-pre test
> vitest run


 RUN  v5.0.5 C:/Dev-Projects/support.js


 Test Files  29 passed (29)
      Tests  279 passed (279)
   Start at  08:43:54
   Duration  2.06s (import 44%, tests 29%, transform 17%, worker 10%)

    Isolate  29 workers spawned · ~290ms startup each (spawn + environment, per file)
             at least ~911ms faster with isolate: false — reuses workers across files instead of one per file
```

Command: `npm run lint` exit code 0

```text
> @gpellicciotta/support.js@3.1.0-pre lint
> eslint .

C:\Dev-Projects\support.js\src\app-internals-view.mjs
  544:9  warning  The value assigned to 'appInstallState' is not used in subsequent statements  no-useless-assignment

C:\Dev-Projects\support.js\src\colors.mjs
  37:7  warning  The value assigned to 'r' is not used in subsequent statements  no-useless-assignment
  38:7  warning  The value assigned to 'g' is not used in subsequent statements  no-useless-assignment
  39:7  warning  The value assigned to 'b' is not used in subsequent statements  no-useless-assignment
  96:7  warning  The value assigned to 'h' is not used in subsequent statements  no-useless-assignment
  97:7  warning  The value assigned to 's' is not used in subsequent statements  no-useless-assignment

C:\Dev-Projects\support.js\src\dialog.mjs
  135:7  warning  The value assigned to 'attachedOverlay' is not used in subsequent statements  no-useless-assignment

✖ 7 problems (0 errors, 7 warnings)
```

The 7 warnings predate this task and sit in files it does not touch.
