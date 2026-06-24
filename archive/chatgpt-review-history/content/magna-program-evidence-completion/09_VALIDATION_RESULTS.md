# Validation Results

Every validation used already-installed dependencies. Git status was recorded before and after; no reviewed repository gained tracked or unexpected files.

| Repository | Command | Result |
|---|---|---|
| Command Center | `npm run build` | PASS; Vite transformed 2,813 modules. Large-chunk warning only. |
| Command Center | `PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/tests` | PASS: **701 passed**, 7 deprecation warnings, 12.22s. |
| Command Center | `node scripts/verify_command_router.mjs` | PASS: **65/65**. |
| Enso | `python3 -m unittest discover -s tests/policy -v` | PASS: **49 tests**. |
| Enso | installed pytest runner against `tests/policy` | FAIL during collection: **7 errors**, no tests; `tests/policy/__init__.py` creates package `policy` and shadows root `policy/`. |
| Enso | system `python3 -m pytest ...` | Not runnable: pytest is not installed for system Python; no install attempted. |
| TRACE | installed pytest runner from repository root | PASS: **6 passed**. |
| TRACE UI | `npm run lint` | PASS. |
| TRACE UI | `npm run build` | BLOCKED by missing installed optional dependency `@rollup/rollup-darwin-arm64`; no install/repair attempted. |

The first sandboxed Command Center run is retained but invalid for product judgment: build metadata and SQLite writes were denied by sandbox permissions, yielding false build/test failures. The rerun with normal expected write access is authoritative.

Smallest proposed Enso correction: remove/rename `tests/policy/__init__.py` so pytest does not import the test directory as top-level `policy`, or introduce a pytest import-mode/config that guarantees the repository root production package wins. The first option is the narrowest candidate, but it was not applied or validated.

Raw outputs: `raw-command-output/mcc-frontend-build-escalated.txt`, `mcc-backend-pytest-escalated.txt`, `mcc-router-smoke-escalated.txt`, `enso-unittest.txt`, `enso-pytest-collection-with-installed-pytest.txt`, `trace-pytest-root.txt`, `trace-frontend-lint.txt`, `trace-frontend-build.txt`, plus before/after status records.

