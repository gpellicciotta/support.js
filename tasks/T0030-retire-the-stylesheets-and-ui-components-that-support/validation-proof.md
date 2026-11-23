## Walkthrough & Validation

### Red-Phase Test Failure (Failure 1 and 2 of 4)
Command: `npx vitest run tests/package-exports.test.mjs` (exit code 1)

```text
 RUN  v5.0.5 C:/Dev-Projects/support.js
 ❯ tests/package-exports.test.mjs (5 tests | 4 failed) 19ms
   ❯ Non-UI Package Surface (5)
     × package.json exports no CSS and omits css from files 7ms
     × css/ and img/ directories and visual-style-guide.md are absent 3ms
     × retired UI modules are absent from src/ 1ms
     ✓ retained modules remain present in src/ 3ms
     × src/forms.mjs exports only pure validation functions 3ms
[... 2 lines omitted ...]
⎯⎯⎯⎯⎯⎯⎯ Failed Tests 4 ⎯⎯⎯⎯⎯⎯⎯
[... 1 line omitted ...]
 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > package.json exports no CSS and omits css from files
AssertionError: package.json must not export ./*.css
+ actual - expected
[... 1 line omitted ...]
+ './css/*.css'
- undefined
[... 1 line omitted ...]
 ❯ tests/package-exports.test.mjs:56:12
     54|     assert.ok(pkg.exports, 'package.json should have exports field');
     55|     assert.equal(pkg.exports['./*.mjs'], './src/*.mjs');
     56|     assert.equal(pkg.exports['./*.css'], undefined, 'package.json must…
       |            ^
     57|     assert.equal(pkg.exports['./css/*.css'], undefined, 'package.json …
     58|     assert.ok(!pkg.files.includes('css'), 'package.json files must not…
[... 1 line omitted ...]
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/4]⎯
[... 1 line omitted ...]
 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > css/ and img/ directories and visual-style-guide.md are absent
AssertionError: css/ directory should be removed
[... 1 line omitted ...]
true !== false
[... 2 lines omitted ...]
- Expected
+ Received
[... 1 line omitted ...]
- false
+ true
[... 1 line omitted ...]
 ❯ tests/package-exports.test.mjs:63:12
     61|
     62|   it('css/ and img/ directories and visual-style-guide.md are absent',…
     63|     assert.equal(fs.existsSync(path.join(rootDir, 'css')), false, 'css…
       |            ^
     64|     assert.equal(fs.existsSync(path.join(rootDir, 'img')), false, 'img…
     65|     assert.equal(
[... 1 line omitted ...]
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/4]⎯
[... 67 lines omitted ...]
 Test Files  1 failed (1)
      Tests  4 failed | 1 passed (5)
   Start at  10:24:53
   Duration  282ms (transform 47%, import 24%, tests 21%, worker 8%)
```

### Red-Phase Test Failure (Failure 3 and 4 of 4)
Command: `npx vitest run tests/package-exports.test.mjs` (exit code 1)

```text
[... 48 lines omitted ...]
 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > retired UI modules are absent from src/
AssertionError: Retired module src/app-action-bar.mjs should not exist
[... 1 line omitted ...]
true !== false
[... 2 lines omitted ...]
- Expected
+ Received
[... 1 line omitted ...]
- false
+ true
[... 1 line omitted ...]
 ❯ tests/package-exports.test.mjs:75:14
     73|     for (const mod of RETIRED_MODULES) {
     74|       const fullPath = path.join(rootDir, 'src', mod);
     75|       assert.equal(fs.existsSync(fullPath), false, `Retired module src…
       |              ^
     76|     }
     77|   });
[... 1 line omitted ...]
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[3/4]⎯
[... 1 line omitted ...]
 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > src/forms.mjs exports only pure validation functions
AssertionError: Expected values to be strictly deep-equal:
+ actual - expected
[... 1 line omitted ...]
  [
+   'disable',
+   'enable',
+   'handlePasswordDisclosure',
+   'isDisabled',
+   'isEnabled',
    'isValidEmailAddress',
    'isValidPassword',
+   'markInvalid',
+   'markValid',
+   'removeValidityMarks',
+   'reset',
+   'setButtonLoading',
    'validPasswordDescription',
+   'validateEmailField',
+   'validateInputField',
+   'validatePasswordField'
  ]
[... 23 lines omitted ...]
 ❯ tests/package-exports.test.mjs:87:12
     85|
     86|   it('src/forms.mjs exports only pure validation functions', () => {
     87|     assert.deepEqual(Object.keys(forms).sort(), [
       |            ^
     88|       'isValidEmailAddress',
     89|       'isValidPassword',
[... 1 line omitted ...]
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[4/4]⎯
[... 2 lines omitted ...]
 Test Files  1 failed (1)
      Tests  4 failed | 1 passed (5)
   Start at  10:24:53
   Duration  282ms (transform 47%, import 24%, tests 21%, worker 8%)
```

### Green-Phase Affected Tests
Command: `npx vitest run tests/package-exports.test.mjs tests/forms.test.mjs` (exit code 0)

```text
 RUN  v5.0.5 C:/Dev-Projects/support.js

 ✓ tests/package-exports.test.mjs (5 tests) 15ms
 ✓ tests/forms.test.mjs (4 tests) 5ms

 Test Files  2 passed (2)
      Tests  9 passed (9)
```

### Green-Phase Lint Verification
Command: `npm run lint` (exit code 0)

```text
> @gpellicciotta/support.js@4.0.0-pre lint
> eslint .

C:\Dev-Projects\support.js\src\colors.mjs
  37:7  warning  The value assigned to 'r' is not used in subsequent statements  no-useless-assignment
  38:7  warning  The value assigned to 'g' is not used in subsequent statements  no-useless-assignment
  39:7  warning  The value assigned to 'b' is not used in subsequent statements  no-useless-assignment
  96:7  warning  The value assigned to 'h' is not used in subsequent statements  no-useless-assignment
  97:7  warning  The value assigned to 's' is not used in subsequent statements  no-useless-assignment

✖ 5 problems (0 errors, 5 warnings)
```

### Green-Phase Test Suite Run
Command: `npm test` (exit code 0)

```text
> @gpellicciotta/support.js@4.0.0-pre test
> vitest run

 RUN  v5.0.5 C:/Dev-Projects/support.js

 ✓ tests/changelog-parser.test.mjs (13 tests) 19ms
 ✓ tests/math.test.mjs (13 tests) 39ms
 ✓ tests/offline-storage.test.mjs (19 tests) 25ms
 ✓ tests/cli-log.test.mjs (21 tests) 24ms
 ✓ tests/mock-dom.test.mjs (35 tests) 45ms
 ✓ tests/http.test.mjs (8 tests) 127ms
 ✓ tests/scripts-lib.test.mjs (12 tests) 304ms
 ✓ tests/dates.test.mjs (13 tests) 17ms
 ✓ tests/local-usage-tracking.test.mjs (7 tests) 19ms
 ✓ tests/page.test.mjs (11 tests) 14ms
 ✓ tests/errors.test.mjs (5 tests) 16ms
 ✓ tests/colors.test.mjs (7 tests) 13ms
 ✓ tests/package-exports.test.mjs (5 tests) 15ms
 ✓ tests/auth-redirect.test.mjs (4 tests) 10ms
 ✓ tests/objects.test.mjs (5 tests) 9ms
 ✓ tests/extract-release-notes.test.mjs (4 tests) 7ms
 ✓ tests/log.test.mjs (1 test) 7ms
 ✓ tests/strings.test.mjs (6 tests) 8ms
 ✓ tests/forms.test.mjs (4 tests) 5ms
 ✓ packages/words/tests/words.test.mjs (2 tests) 3ms

 Test Files  20 passed (20)
      Tests  195 passed (195)
   Start at  10:29:28
   Duration  1.50s (import 42%, tests 32%, transform 15%, worker 11%)

    Isolate  20 workers spawned · ~257ms startup each (spawn + environment, per file)
             at least ~478ms faster with isolate: false — reuses workers across files instead of one per file
```

### Green-Phase Script Tests
Command: `C:\Dev-Projects\support.js\.venv\Scripts\python.exe -m pytest -q scripts/tests` (exit code 0)

```text
...............                                                          [100%]
15 passed in 1.94s
```

### Package Contents Verification
Command: `npm pack --dry-run` (exit code 0)

```text
[... 3 lines omitted ...]
npm notice 11.1kB CHANGELOG.md
npm notice 1.1kB LICENSE.md
npm notice 1.8kB README.md
npm notice 7.0kB docs/devops.md
npm notice 1.0kB docs/index.md
npm notice 4.3kB docs/requirements.md
npm notice 6.0kB docs/specs/client-upgrade-guide.md
npm notice 13.8kB docs/specs/code-reuse-opportunities.md
npm notice 1.2kB package.json
npm notice 8.9kB src/canvas.mjs
npm notice 6.3kB src/changelog-parser.mjs
npm notice 11.1kB src/collisions.mjs
npm notice 19.7kB src/colors.mjs
npm notice 20.3kB src/dates.mjs
npm notice 24.9kB src/dom.mjs
npm notice 4.5kB src/events.mjs
npm notice 30.2kB src/fireworks.mjs
npm notice 982B src/forms.mjs
npm notice 21.8kB src/logs.mjs
npm notice 7.1kB src/math.mjs
npm notice 14.3kB src/matrix.mjs
npm notice 47.1kB src/mock-dom.mjs
npm notice 7.6kB src/net.mjs
npm notice 7.8kB src/noise.mjs
npm notice 1.5kB src/objects.mjs
npm notice 5.2kB src/paging.mjs
npm notice 5.2kB src/snowflakes.mjs
npm notice 19.1kB src/storages.mjs
npm notice 1.5kB src/strings.mjs
npm notice 5.2kB src/vector.mjs
npm notice Tarball Details
npm notice name: @gpellicciotta/support.js
npm notice version: 4.0.0-pre
npm notice filename: gpellicciotta-support.js-4.0.0-pre.tgz
npm notice package size: 82.0 kB
npm notice unpacked size: 317.5 kB
npm notice shasum: 8793079d84bc1b9223a8e173a2b0612cee512938
npm notice integrity: sha512-BHsxt2cJJVONc[...]pbVXybBQmrZdw==
npm notice total files: 30
npm notice
gpellicciotta-support.js-4.0.0-pre.tgz
```
