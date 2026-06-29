# GOV-005-CF5 — Task-Specific Ownership Hardening (Correction Report)

## Provenance and scope
- Task: `GOV-005-CF5` (packet `trace/tasks/GOV-005-CLAUDE-CF5-HARDENING.md`, Issue #26)
- Instruction authority: ChatGPT / System Architect — Product Owner authority required before merge
- Implementer: Claude (correction implementer — not the independent validator; **Antigravity** validates after)
- Branch: `claude/GOV-005-cf5-hardening`, base `claude/GOV-005-corrections` @ `9120017`
- PR base: `claude/GOV-005-corrections` — **do not merge; do not self-approve**
- **Focused CF-5 hardening only.** No GOV-005 redesign; no runtime/product/ARCH-001/PAR-001/HERMES/SGN-01/Sprint-5 change.

## Synchronization verdict — `SYNC_PASS`
Repo `MightyM-ouse/magna-enso`; base branch present @ `9120017` (CF-1…CF-6 lineage + Antigravity evidence,
not behind `codex/GOV-005`); no existing `claude/GOV-005-cf5-hardening` branch/PR; clean worktree before edits;
PRs #13/#17/#24 inspected as context only (not modified).

## Problem
The prior CF-5 checker authorized a changed path if it was in **the union of every active task's**
`writable_paths` **or** a **broad governance allowlist** (`docs/governance/`, `trace/reviews/`,
`trace/evidence/`, `trace/tasks/`, …). That let task A's branch legitimately touch task B's owned paths and
let broad directories override explicit ownership.

## Corrections (finding → correction)

| Requirement | Correction | Proof |
|---|---|---|
| Task-specific ownership (only the active task; no union) | `check_changed_path_ownership.py` now identifies **one accountable active task** from the branch and builds `allowed` from **only that task's** `writable_paths` + `shared_paths` + declared `correction_phase_modifies.files` + the single self-registration file. The cross-task union and the broad `GOVERNANCE_ALLOWLIST` are **removed**. | tests: `test_cannot_combine_multiple_task_paths`, `test_broad_governance_dir_does_not_bypass`, `test_task_a_cannot_edit_task_b_handoff` |
| Fail-closed identity detection | `identify_active_task` fails on: missing branch; no registered task for branch (mismatch/unregistered); >1 task for a branch (ambiguous); task status not active (`MERGED`/`CLOSED`/`REJECTED`). `evaluate` returns not-ok on any identity error. | tests: `test_missing_identity_fails`, `test_ambiguous_identity_fails`, `test_inactive_task_fails` |
| Governed handoff validation (all changed, not hard-coded) | `validate_changed_handoffs` schema-validates **every** changed `trace/evidence/*HANDOFF.json` via the validator's `validate_handoff` (rejects out-of-vocabulary status / bad provenance). Handoffs changed outside the task envelope already fail ownership. | tests: `test_governed_handoff_detection`, `test_handoff_rejects_arbitrary_status` |
| Explicit, validated exception for legitimate cross-cutting edits | A task may declare `correction_phase_modifies.files` (a per-task, validated sequential-phase exception); those paths are allowed for that task only — not a broad allowlist. | test: `test_correction_phase_modifies_allowed` |
| CI wiring | The workflow passes `--branch "${{ github.head_ref }}"` so CI evaluates the change set against the accountable task. | `.github/workflows/governance-validation.yml` |
| Minimal surface | Changed only the checker, the workflow, the policy CF-5 paragraph, the registry (CF-5 task entry), the packet copy, tests, and CF-5 evidence. Validator/schema/requirements unchanged. | change set |

## Adversarial test results (local)
`python tests/test_changed_path_ownership.py` → **11/11 PASS**, including: task A cannot edit task B handoff;
no multi-task union; broad dir no bypass; missing/ambiguous/inactive identity fails; governed-handoff detection;
arbitrary-status rejection; self-registration allowed; correction-phase exception allowed; and the real CF-5
task envelope passes.

## Validation (local)
- `python scripts/validate_multi_agent_governance.py` → **PASS** (6 active tasks; schema enum matches vocabulary).
- `python scripts/check_changed_path_ownership.py --branch claude/GOV-005-cf5-hardening --paths <change set>` →
  **PASS** (all within the accountable task envelope; changed governed handoff validated).
- Local validator dependency: **PyYAML 6.0.2** (PyPI, MIT) in an isolated venv; CI installs the same pinned
  version from `scripts/governance-requirements.txt`. GitHub CI result is recorded on the PR.

## Residual risks
- The active task is identified by an exact branch match; a task with no/incorrect `branch` field fails closed
  (intended). A future hardening could add signed task identity.
- An active task may edit the self-registration file `trace/ACTIVE_WORK_REGISTRY.yaml`; registry tampering is
  caught by the validator's overlap/vocabulary checks and human PR review, not by this path check.
- `correction_phase_modifies` is an explicit, reviewed exception; misuse is caught at PR review.

## Boundaries honored
No merge, no self-approval, push only to `claude/GOV-005-cf5-hardening`. No change to runtime/product, ARCH-001,
PAR-001 evidence, HERMES activation, SGN-01, Sprint 5, `main`, or protected paths. Issue #26 not closed.
Independent CF-5 validation delegated to Antigravity.

## Decisions required
ChatGPT/System Architect file review; Antigravity focused CF-5 validation; Product Owner merge authorization
into the GOV-005 correction path.
