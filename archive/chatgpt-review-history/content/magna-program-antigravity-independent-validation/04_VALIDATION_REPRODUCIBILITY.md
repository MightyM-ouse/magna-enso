# 04 — Validation Reproducibility

This report documents the validation execution results across the three repositories, verifying their builds, tests, and smoke test suites, and classifying any failure modes.

## 1. Test and Build Execution Results

All commands were run using already-installed dependencies and standard local Python/Node runners. No new dependencies were installed.

| Repository | Scope / Target | Command | Result / Exit Code | Findings |
| :--- | :--- | :--- | :--- | :--- |
| **Command Center** | Frontend Build | `npm run build` | **PASS** (0) | Successfully compiled 2,813 modules. Vite large-chunk warning observed (1.85 MB minified). |
| **Command Center** | Backend Pytest | `PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/tests` | **PASS** (0) | **701 tests passed**; 7 deprecation warnings. |
| **Command Center** | Router Smoke | `node scripts/verify_command_router.mjs` | **PASS** (0) | **65/65 tests passed**. |
| **Magna Enso** | Official Unittest | `python3 -m unittest discover -s tests/policy -v` | **PASS** (0) | **49 tests passed** (enforcing gate, schema, audit, canonical, and structure). |
| **Magna Enso** | Pytest Collection | `pytest tests/policy` | **FAIL** (4) | Collection failed with **7 import errors**. |
| **TRACE** | Pytest | `pytest` | **PASS** (0) | **6 tests passed** (testing server ingestion and endpoints). |
| **TRACE UI** | Frontend Lint | `npm run lint` | **PASS** (0) | Passed with no errors. |
| **TRACE UI** | Frontend Build | `npm run build` | **BLOCKED** (1) | Failed due to missing `@rollup/rollup-darwin-arm64` binary. |

## 2. Git Status and Working Tree Verification

For all three repositories, git status was recorded immediately before and after the validation runs. 
- **Command Center:** Git status remained exactly the same (`ahead 1`, modified `.codex/config.toml` and `AGENTS.md`). No new files were staged or committed.
- **Magna Enso:** Git status remained unchanged (untracked `policy/`, `tests/`, and evidence file). No files were modified or staged.
- **TRACE:** Git status remained clean with only untracked `proposed-governed-loop/`.

No repository state changed. Only expected temporary cache directories (e.g., `.pytest_cache/`, `tsconfig.app.tsbuildinfo`, and frontend `dist/` chunks) were written or updated.

## 3. Failure Mode Classification

To prevent incorrect product quality verdicts, validation failures must be correctly classified:

- **Enso Pytest Collection Failure: Source Layout/Design Defect.**
  The file [tests/policy/__init__.py](file://<MAGNA_LOCAL_ROOT>/magna-enso/tests/policy/__init__.py) creates a top-level package called `policy` that shadows the actual production [policy/](file://<MAGNA_LOCAL_ROOT>/magna-enso/policy/) package. When pytest attempts to run tests, it imports the test folder's package namespace, causing imports of production modules (like `policy.evaluator` or `policy.gate`) to raise `ModuleNotFoundError`. This is a genuine structure defect, not a runner or dependency problem.
- **TRACE UI Build Failure: Local Environment / Dependency Block.**
  The failure is caused by a missing Rollup optional native binary (`@rollup/rollup-darwin-arm64`) in the pre-existing node_modules folder. This is a local npm installation gap (mismatched OS/architecture packages installed), not a defect in the TRACE source code.
- **Sandbox Write Denial:**
  We verified Codex's note: running validation inside a restricted sandbox that blocks SQLite writes or build directory compilation will yield false test failures. Standard, expected local-write execution is required for authentic validation.
