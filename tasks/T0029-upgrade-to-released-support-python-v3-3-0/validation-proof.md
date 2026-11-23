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
