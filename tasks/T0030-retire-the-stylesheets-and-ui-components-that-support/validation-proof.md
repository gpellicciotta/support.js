## Walkthrough & Validation

### Red-Phase Test Failure (Part 1 of 4: Summary and Failure 1)
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

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 4 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > package.json exports no CSS and omits css from files
AssertionError: package.json must not export ./*.css
+ actual - expected

+ './css/*.css'
- undefined

 ❯ tests/package-exports.test.mjs:56:12
     54|     assert.ok(pkg.exports, 'package.json should have exports field');
     55|     assert.equal(pkg.exports['./*.mjs'], './src/*.mjs');
     56|     assert.equal(pkg.exports['./*.css'], undefined, 'package.json must…
       |            ^
     57|     assert.equal(pkg.exports['./css/*.css'], undefined, 'package.json …
     58|     assert.ok(!pkg.files.includes('css'), 'package.json files must not…

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/4]⎯
[... 102 lines omitted ...]
```

### Red-Phase Test Failure (Part 2 of 4: Failures 2 and 3)
Command: `npx vitest run tests/package-exports.test.mjs` (exit code 1)

```text
[... 29 lines omitted ...]
 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > css/ and img/ directories and visual-style-guide.md are absent
AssertionError: css/ directory should be removed

true !== false


- Expected
+ Received

- false
+ true

 ❯ tests/package-exports.test.mjs:63:12
     61|
     62|   it('css/ and img/ directories and visual-style-guide.md are absent',…
     63|     assert.equal(fs.existsSync(path.join(rootDir, 'css')), false, 'css…
       |            ^
     64|     assert.equal(fs.existsSync(path.join(rootDir, 'img')), false, 'img…
     65|     assert.equal(

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/4]⎯

 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > retired UI modules are absent from src/
AssertionError: Retired module src/app-action-bar.mjs should not exist

true !== false


- Expected
+ Received

- false
+ true

 ❯ tests/package-exports.test.mjs:75:14
     73|     for (const mod of RETIRED_MODULES) {
     74|       const fullPath = path.join(rootDir, 'src', mod);
     75|       assert.equal(fs.existsSync(fullPath), false, `Retired module src…
       |              ^
     76|     }
     77|   });
[... 63 lines omitted ...]
```

### Red-Phase Test Failure (Part 3 of 4: Failure 4 Diff Part A)
Command: `npx vitest run tests/package-exports.test.mjs` (exit code 1)

```text
[... 68 lines omitted ...]
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[3/4]⎯

 FAIL  tests/package-exports.test.mjs > Non-UI Package Surface > src/forms.mjs exports only pure validation functions
AssertionError: Expected values to be strictly deep-equal:
+ actual - expected

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


- Expected
+ Received

  [
+   "disable",
+   "enable",
+   "handlePasswordDisclosure",
+   "isDisabled",
+   "isEnabled",
    "isValidEmailAddress",
    "isValidPassword",
+   "markInvalid",
[... 25 lines omitted ...]
```

### Red-Phase Test Failure (Part 4 of 4: Failure 4 Diff Part B and Final Summary)
Command: `npx vitest run tests/package-exports.test.mjs` (exit code 1)

```text
[... 106 lines omitted ...]
+   "markValid",
+   "removeValidityMarks",
+   "reset",
+   "setButtonLoading",
    "validPasswordDescription",
+   "validateEmailField",
+   "validateInputField",
+   "validatePasswordField",
  ]

 ❯ tests/package-exports.test.mjs:87:12
     85|
     86|   it('src/forms.mjs exports only pure validation functions', () => {
     87|     assert.deepEqual(Object.keys(forms).sort(), [
       |            ^
     88|       'isValidEmailAddress',
     89|       'isValidPassword',

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[4/4]⎯


 Test Files  1 failed (1)
      Tests  4 failed | 1 passed (5)
   Start at  10:24:53
   Duration  282ms (transform 47%, import 24%, tests 21%, worker 8%)
```

### Post-Change Full Check (Part 1 of 3: Lint and Fast Suite)
Command: `python scripts/devops.py check` (exit code 0)

```text
Command: "C:\Program Files\nodejs\npm.CMD" run lint
Process ID: 33536
> @gpellicciotta/support.js@4.0.0-pre lint
> eslint .
C:\Dev-Projects\support.js\src\colors.mjs
  37:7  warning  The value assigned to 'r' is not used in subsequent statements  no-useless-assignment
  38:7  warning  The value assigned to 'g' is not used in subsequent statements  no-useless-assignment
  39:7  warning  The value assigned to 'b' is not used in subsequent statements  no-useless-assignment
  96:7  warning  The value assigned to 'h' is not used in subsequent statements  no-useless-assignment
  97:7  warning  The value assigned to 's' is not used in subsequent statements  no-useless-assignment
✖ 5 problems (0 errors, 5 warnings)
Command: "C:\Program Files\nodejs\npm.CMD" test
Process ID: 27424
> @gpellicciotta/support.js@4.0.0-pre test
> vitest run
 RUN  v5.0.5 C:/Dev-Projects/support.js
 ✓ tests/changelog-parser.test.mjs (13 tests) 18ms
 ✓ tests/math.test.mjs (13 tests) 41ms
 ✓ tests/offline-storage.test.mjs (19 tests) 29ms
 ✓ tests/mock-dom.test.mjs (35 tests) 59ms
 ✓ tests/cli-log.test.mjs (21 tests) 25ms
 ✓ tests/http.test.mjs (8 tests) 157ms
 ✓ tests/scripts-lib.test.mjs (12 tests) 357ms
 ✓ tests/errors.test.mjs (5 tests) 16ms
 ✓ tests/page.test.mjs (11 tests) 16ms
 ✓ tests/dates.test.mjs (13 tests) 17ms
 ✓ tests/package-exports.test.mjs (5 tests) 13ms
 ✓ tests/local-usage-tracking.test.mjs (7 tests) 18ms
 ✓ tests/colors.test.mjs (7 tests) 14ms
 ✓ tests/auth-redirect.test.mjs (4 tests) 10ms
 ✓ tests/objects.test.mjs (5 tests) 10ms
 ✓ tests/forms.test.mjs (4 tests) 6ms
 ✓ tests/log.test.mjs (1 test) 8ms
 ✓ tests/strings.test.mjs (6 tests) 9ms
 ✓ tests/extract-release-notes.test.mjs (4 tests) 8ms
 ✓ packages/words/tests/words.test.mjs (2 tests) 6ms
 Test Files  20 passed (20)
      Tests  195 passed (195)
   Start at  10:34:48
   Duration  2.01s (import 43%, tests 30%, transform 18%, worker 9%)
[... 72 lines omitted ...]
```

### Post-Change Full Check (Part 2 of 3: Script Tests and Build Pack)
Command: `python scripts/devops.py check` (exit code 0)

```text
[... 40 lines omitted ...]
    Isolate  20 workers spawned · ~296ms startup each (spawn + environment, per file)
             at least ~550ms faster with isolate: false — reuses workers across files instead of one per file
Command: C:\Dev-Projects\support.js\.venv\Scripts\python.exe -m pytest -q scripts/tests
Process ID: 26484
...............                                                          [100%]
15 passed in 1.92s
npm script 'test:slow' is not defined in package.json; skipping.
Removing dist
Command: "C:\Program Files\nodejs\npm.CMD" pack --workspaces --include-workspace-root --pack-destination dist
Process ID: 32352
npm notice
npm notice package: @gpellicciotta/support.js@4.0.0-pre
npm notice Tarball Contents
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
[... 32 lines omitted ...]
```

### Post-Change Full Check (Part 3 of 3: Workspace Tarball Details)
Command: `python scripts/devops.py check` (exit code 0)

```text
[... 80 lines omitted ...]
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
npm notice
npm notice package: @gpellicciotta/support-words.js@4.0.0-pre
npm notice Tarball Contents
npm notice 696B README.md
npm notice 795B package.json
npm notice 2.7MB src/dutchwords.mjs
npm notice 3.4kB src/englishwords.mjs
npm notice Tarball Details
npm notice name: @gpellicciotta/support-words.js
npm notice version: 4.0.0-pre
npm notice filename: gpellicciotta-support-words.js-4.0.0-pre.tgz
npm notice package size: 654.5 kB
npm notice unpacked size: 2.7 MB
npm notice shasum: 8810ed313374e55dc9323b9fd5cbe1ec8ef2e897
npm notice integrity: sha512-62mOe3qhQbqp3[...]de/ys4L/cxo8g==
npm notice total files: 4
npm notice
gpellicciotta-support-words.js-4.0.0-pre.tgz
```
