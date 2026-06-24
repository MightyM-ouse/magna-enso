# CODEX_PROMPT_READINESS_VALIDATION.md
# Magna Enso — Sprint 5 Codex Implementation Prompt Readiness Validation

## 1. Codex Prompt Preflight Checks

The draft prompt in `PROPOSED_CODEX_IMPLEMENTATION_PROMPT.md` enforces a strict preflight safety sequence (Step 0) that Codex must execute before changing any code:

1. **Verify Main Branch:** Expects and asserts current branch is `main`.
2. **Verify Baseline HEAD:** Expects and asserts HEAD is exactly `4d5c203cc236be84bd4b9bd8004cb88e8797a34d`.
3. **Verify Clean Tree:** Asserts no modified or untracked files exist.
4. **Verify Trace Gates:** Asserts `R-06` is `OPEN`, `EH-0005B` is `PROPOSED`, features are `PLANNED`, and `STAR_MAP.md` is updated.

If any check fails, Codex is instructed to **STOP** immediately and report back. This prevents starting the work from an incorrect baseline or a dirty state.

## 2. Allowed and Forbidden Path Boundaries

The prompt defines clear, rigid boundaries for directory access to prevent unauthorized side-effects or leakage:

- **Allowed Paths (modification permitted):**
  - `policy/**` (new engine source code)
  - `tests/policy/**` (new unit/integration tests)
  - `trace/evidence/ENSO-0005_LIGHT_CURVE.md` (draft evidence document, status `IN_REVIEW`)
- **Forbidden Paths (modification strictly prohibited):**
  - `vendor/**` (vendor directories must remain quarantined and untouched)
  - `src/**`, `ui/**`, `scheduler/**`, `gateway/**`, `providers/**`, `plugins/**` (out of scope surfaces)
  - Status files under `trace/` (except the draft light curve)
  - Project planning and Charters (`planning/**`)

This guarantees that Codex cannot modify existing files or inadvertently activate dormant Hermes capabilities.

## 3. Implementation Sequence & Tests-First Constraints

The prompt embeds the required implementation sequence from `IMPLEMENTATION_SEQUENCE.md`:
- Enforces writing failing tests in `tests/policy/` **prior** to the core implementation.
- Requires building and verifying the audit sink (atomic write, flush sync, hash-chain head, corruption detection) **before** introducing any gate allowances, ensuring the gate remains deny-only during testing until logging is complete.
- Forbids external dependencies (stdlib json only, no YAML parsers in runtime code).

## 4. Honesty Requirements and Stop Conditions

- **Honesty Clause:** Codex must draft `trace/evidence/ENSO-0005_LIGHT_CURVE.md` (Full) containing an explicit section stating:
  - The implementation is harness-level only.
  - The system is not runtime-protected.
  - No authenticated human-approval provider exists.
  - The audit log is not tamper-proof against local admins.
  - `R-06` remains open.
- **Stop Invariant:** The prompt instructs Codex to **STOP** immediately after completing the test validation run. 
- **No Git side-effects:** Codex is forbidden from committing, pushing, or merging the branch. Branch merging is a human-gated action that can only occur after Antigravity validation and explicit human owner sign-off.

## 5. Baseline Drift and Risk Assessment

- **Risk:** Could the draft prompt modify unapproved paths or drift from the baseline?
- **Finding:** No. The branch switch command `git switch -c sprint/05-policy-engine` is executed from clean `main` HEAD `4d5c203`, and Step 2 re-verifies that the base SHA remains unchanged. The path boundaries prevent any edits outside `policy/`, `tests/policy/`, and the draft Light Curve file.
- **Verdict:** The prompt is **ready** and secure for execution once human approval is granted.
