## Walkthrough & Validation

Red phase, before implementation: `python -m pytest scripts/tests -q`, exit 1.
```text
FAILED scripts/tests/test_scripts.py::test_requirements_pin_released_support_python
FAILED scripts/tests/test_scripts.py::test_cli_common_duplicate_is_removed
FAILED scripts/tests/test_scripts.py::test_devops_help_lists_shared_actions
FAILED scripts/tests/test_scripts.py::test_devops_versions_checks_package_and_changelog
4 failed, 3 passed in 0.55s
```

Green phase: `.venv/Scripts/python -m pytest scripts/tests -q`, exit 0.
```text
.......                                                                  [100%]
7 passed in 0.96s
```

`python scripts/devops.py versions`:
```text
Version file: 3.0.1-pre
CHANGELOG.md: 3.0.1-pre
Versions agree.
```

`python scripts/devops.py check` (lint, vitest, pack), exit 0; tail and test summary:
```text
✖ 7 problems (0 errors, 7 warnings)
 Test Files  29 passed (29)
      Tests  267 passed (267)
npm notice total files: 55
npm notice total files: 4
```

## Review round 1 rework

Red phase of the added tests against the previous scripts: `.venv/Scripts/python -m pytest scripts/tests -q`, exit 1.
```text
FAILED scripts/tests/test_scripts.py::test_changelog_has_separator_for_next_development_heading
FAILED scripts/tests/test_scripts.py::test_set_version_updates_all_lockstep_files
FAILED scripts/tests/test_scripts.py::test_set_version_keeps_lock_file_format
FAILED scripts/tests/test_scripts.py::test_bootstrap_help_lists_actions_and_exit_codes
4 failed, 9 passed in 1.67s
```

Green phase: `.venv/Scripts/python -m pytest scripts/tests -q`, exit 0.
```text
.............                                                            [100%]
13 passed in 1.47s
```

`python scripts/devops.py check`, exit 0 (now also runs the script tests):
```text
✖ 7 problems (0 errors, 7 warnings)
 Test Files  29 passed (29)
      Tests  267 passed (267)
13 passed in 1.49s
```

`python scripts/devops.py release --dry-run`, exit 1:
```text
**[ERROR]** release is not supported for this workspace monorepo; follow the Release Process in docs/devops.md.
**[ERROR]** Finished devops release in 0.0s with status: failed
```
