# GOV-005 — Antigravity Independent Correction Validation Report

## Provenance and scope

- Validation task: `GOV-005-ANTIGRAVITY-VALIDATION` (packet [GOV-005-ANTIGRAVITY-VALIDATION.md](file:///Users/vinay/Projects/AI/Magna/magna-enso/trace/tasks/GOV-005-ANTIGRAVITY-VALIDATION.md))
- Instruction prepared by: ChatGPT / System Architect — approved by: Product Owner (Vinay)
- Independent validator: **Antigravity**
- Target correction PR: PR #17 (branch `claude/GOV-005-corrections`)
- Exact target head: `61098c04f7b98016a7ce17efc20cfa1d44bf7f6b`
- Validation branch: `antigravity/GOV-005-corrections-validation`
- Target base for validation PR: `claude/GOV-005-corrections`

## Synchronization verdict — `SYNC_PASS`

1. **Target PR #17 status:** OPEN/DRAFT, base branch is `codex/GOV-005-multi-agent-governance`, and the head is exactly `61098c04f7b98016a7ce17efc20cfa1d44bf7f6b`. (Confirmed via `gh pr view 17`).
2. **CI status:** Governance run `28130377771` completed successfully for that head. (Confirmed via `gh run view 28130377771` with SUCCESS conclusion).
3. **Branch state:** Local checkout is `antigravity/GOV-005-corrections-validation`, contains the validation packet, and is fully synchronized with remote `origin/antigravity/GOV-005-corrections-validation`.

## Executive Summary & Material Findings

### 1. Incomplete correction or bypass (Material Finding)
- **Finding:** **Union-of-Ownership & Broad Folder Allowlist Bypass**
  - **Component/File:** [check_changed_path_ownership.py](file:///Users/vinay/Projects/AI/Magna/magna-enso/scripts/check_changed_path_ownership.py)
  - **Severity:** High
  - **Impact:** Any active task branch can write to any other active task's exclusive writable paths (e.g., a branch representing one task can modify files inside another task's exclusive `docs/architecture/` directory). Additionally, any task branch can modify any task packet, review, or evidence file belonging to another task because `GOVERNANCE_ALLOWLIST` contains broad directory-level prefixes (`trace/reviews/`, `trace/tasks/`, `trace/evidence/`).
  - **Analysis:**
    1. The ownership check script merges all active tasks' paths via the `allowed_prefixes()` union:
       ```python
       for task in registry.get("active_tasks", []):
           allowed.update(task.get("writable_paths", []))
           allowed.update(task.get("shared_paths", []))
       ```
       This means the check does not verify *which* branch or task ID is executing.
    2. The folder-level prefixes in `GOVERNANCE_ALLOWLIST` allow any branch to modify, add, or delete files inside these folders without triggering a changed-path failure.
  - **Proof:**
    - Running `./venv/bin/python3 scripts/check_changed_path_ownership.py --paths trace/tasks/ARCH-001.md` (which belongs to ARCH-001, not the current task) results in `PASS`.
    - Running `./venv/bin/python3 scripts/check_changed_path_ownership.py --paths docs/architecture/spec.md` (exclusive to ARCH-001) results in `PASS`.
  - **Recommendation:** Implement branch-specific or task-specific filters inside the ownership checker (e.g., mapping `github.head_ref` or the current branch name to the task's allowed paths in `ACTIVE_WORK_REGISTRY.yaml` rather than using the union of all active tasks).

### 2. Confirmed corrections (CF-1..CF-4, CF-6)
- **CF-1: CI enforcement** (Confirmed): CI workflow successfully executes both the validation script and the changed-path ownership check on main and stacked PRs.
- **CF-2: Synchronization authority** (Confirmed): The live branch head is established as the authority. `final_commit` and `latest_known_commit` are correctly point-in-time pointers without self-referential paradoxes.
- **CF-3: Status authority** (Confirmed): The active work registry is the single source of truth for the status vocabulary. All other surfaces map to this.
- **CF-4: Status constraints** (Confirmed): Handoff and active work statuses are constrained to the status vocabulary, and the schema enum matches the registry vocabulary.
- **CF-6: Provenance semantics** (Confirmed): Provenance separates the intended reviewer from the completed review. Completed reviews require a valid reviewer name.

### 3. Nonblocking hardening
- **Dependency isolation:** Installing PyYAML 6.0.2 via `scripts/governance-requirements.txt` runs in a user-local space in CI and an isolated venv locally. This prevents global environment contamination.

### 4. Verified positive controls
- Running the positive control validator on the current workspace results in a complete `PASS` for all 5 registered active tasks.

## Validation Matrix (CF-1 … CF-6)

| Finding | Description | Verdict | Validation Method / Command |
|---|---|---|---|
| **CF-1** | CI validator enforcement | **Confirmed** | Inspected [.github/workflows/governance-validation.yml](file:///Users/vinay/Projects/AI/Magna/magna-enso/.github/workflows/governance-validation.yml) and verified successful run `28130377771` |
| **CF-2** | Commit semantics/Freshness | **Confirmed** | Inspected schema, policy, and registry definitions; verified point-in-time semantics |
| **CF-3** | Status synchronization | **Confirmed** | Inspected [ACTIVE_WORK_REGISTRY.yaml](file:///Users/vinay/Projects/AI/Magna/magna-enso/trace/ACTIVE_WORK_REGISTRY.yaml); verified status authority |
| **CF-4** | Task status validation | **Confirmed** | Mutated handoff task status to out-of-vocabulary value -> validation FAIL |
| **CF-5** | Handoff path ownership | **Bypass** | Mutated check with cross-task/allowlist paths -> validation PASS (leak detected) |
| **CF-6** | Provenance review state | **Confirmed** | Mutated provenance with invalid review states -> validation FAIL |

## Adversarial Test Record

All negative tests were executed programmatically against the validator functions using an isolated python script:

| ID | Test Name | Mutation Description | Expected Result | Actual Result | Exit Status |
|---|---|---|---|---|---|
| **N1** | Handoff Status Enum | Set `task.status` to `INVALID_STATUS_VALUE` | AssertionError | AssertionError | 1 (Expected) |
| **N1b**| Registry Status Enum | Set registry task status to `INVALID_STATUS_VALUE` | AssertionError | AssertionError | 1 (Expected) |
| **N2** | Legacy Provenance | Added `"reviewed_by": "ChatGPT"` to handoff | AssertionError | AssertionError | 1 (Expected) |
| **N2b**| Schema Shape | Added `"reviewed_by"` to schema required list | AssertionError | AssertionError | 1 (Expected) |
| **N3** | Completed review empty | Set status `COMPLETED` and `review_completed_by` null | AssertionError | AssertionError | 1 (Expected) |
| **N3b**| Pending review filled | Set status `PENDING` and `review_completed_by` "ChatGPT" | AssertionError | AssertionError | 1 (Expected) |
| **N4** | Forbidden changed path | Checked paths `src/runtime/app.py`, `policy/engine.py` | Fail (Exit 1) | Fail (Exit 1) | 1 (Expected) |
| **N5** | Allowed changed path | Checked paths in `GOVERNANCE_ALLOWLIST` | Pass (Exit 0) | Pass (Exit 0) | 0 (Expected) |
| **N6** | Cross-task bypass | Checked other task's packet `trace/tasks/ARCH-001.md` | **Blocked** | **Pass (Exit 0)** | 0 (**Bypass**) |
| **N7** | Union-of-ownership | Checked other task's path `docs/architecture/spec.md` | **Blocked** | **Pass (Exit 0)** | 0 (**Bypass**) |

## CI/Workflow Evidence

- Failed run `28130304161` (due to pip `--require-hashes=false` error): Verified that failure in dependency installation correctly blocks the job.
- Successful run `28130377771` (head `61098c0`): Verified all jobs completed successfully.
- Trigger matrix: Pull request targets `main`, `codex/**`, `claude/**`, `chatgpt/**`, `antigravity/**`, and `architect/**` are correctly handled.

## Changed-Path and Protected-Boundary Proof

- The PR changes 14 files, all within the governance and configuration directories.
- No files under `trace/tasks/GOV-005.md` (immutable), the historical Claude review evidence, runtime/product code, ARCH-001, Sprint 5, Hermes, HELIX, or SGN-01 were altered in PR #17.

## Residual Risks / Product Owner Decisions Required

1. **Governance Allowlist & Union Ownership:** The Product Owner must decide whether to harden [check_changed_path_ownership.py](file:///Users/vinay/Projects/AI/Magna/magna-enso/scripts/check_changed_path_ownership.py) to check branch-to-task mappings rather than the union of all active tasks.
2. **Review Namespace Exception:** The legacy `codex/` namespace exception for GOV-005 (retained to preserve history) remains a carry-over decision.
3. **Acceptance of Corrections:** While the core status, synchronization, and provenance bugs (CF-1..CF-4, CF-6) are fully corrected, the path ownership checker (CF-5) has a conceptual bypass. The Product Owner must decide whether to accept this implementation or require further hardening.

## Summary for ChatGPT Review

Antigravity has completed independent validation of PR #17 at head `61098c0`. The corrections for CF-1, CF-2, CF-3, CF-4, and CF-6 are correct and robust under negative testing. However, the path ownership checker (CF-5) suffers from a material bypass: it uses the union of all active tasks and has broad prefix allowlists, allowing any branch to modify files belonging to other tasks or general governance folders. We recommend hardening the ownership check to compare changed paths strictly against the running branch's task-assigned paths.
