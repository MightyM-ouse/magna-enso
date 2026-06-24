# INDEPENDENT_VALIDATION_BRIEF.md
# Magna Enso — Sprint 5 Independent Validation Brief
# Type: Local-only approval package
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started.

---

## 1. Purpose

Brief the independent validator(s) on what to check **after** Sprint 5 is implemented and **before** human
acceptance. Independent validation is mandatory for this HIGH-risk, R-06-critical sprint.

## 2. Recommended reviewer

- **Primary: Antigravity** (Validation / Safety — Spectrometer). Runs adversarial bypass testing and the
  universal governance gates. Does not author code; does not approve its own validation.
- **Secondary: Grok** — independent second opinion / edge-case challenge on the threat model and chokepoint
  completeness.
- **Human owner** is final authority (EH-0010); validators *recommend*, never accept.

## 3. What the validator must independently confirm

1. **Default-deny holds:** unknown capability / no policy / uncovered path ⇒ DENY (T-1 harness, T-2, F-8).
2. **Bypass coverage by category (not a blanket "no bypass"):** independently exercise the **testable**
   classes (T-2, T-3, T-5, T-7, T-9, harness-level T-1/T-4/T-8) ⇒ deny; confirm **absence** classes (T-6, T-11)
   are truly absent; confirm **review** classes (T-10 tampering, T-12); confirm the **P-01…P-13 matrix** labels
   deferred boundaries and does **not** claim end-to-end coverage. Confirm the package nowhere claims real
   entry points cannot bypass the gate.
3. **Decision-provider boundary:** Sprint 5 uses programmatically simulated decisions through a test-only
   `HumanDecisionProvider`; human-only approval is a future production invariant; no authenticated production
   provider exists; a missing/default production provider ⇒ DENY; worker/self/config bypasses are rejected.
4. **Fail-closed:** store/evaluator/log/approval failures ⇒ DENY (F-2…F-7); **audit sink built before any ALLOW**.
5. **Audit durability & honesty:** atomic append + flush, corruption detection, malformed-tail recovery,
   duplicate handling (D-8); confirm it is **integrity-detecting, NOT tamper-proof**, and that the package
   states it does **not** protect against a local admin editing audit files.
6. **Single-use / no replay:** approvals expire and cannot be reused; restart ⇒ default-deny (T-8, T-9, F-10).
7. **No Hermes import/run/build; vendor baseline inert/untouched** (EH-0015); runtime policy records are JSON (D-3).
8. **No out-of-scope surface:** no network, cloud, scheduler, UI, remote, memory/skill subsystem.
9. **Honesty of claims:** evidence states "harness-level enforcement core; **not** runtime-protected, **no**
   authenticated human approval, **not** tamper-proof, **no** end-to-end bypass proof"; **R-06 remains OPEN**;
   end-to-end validation recurs per real capability.
10. **No auto-commit/push;** change is on an isolated branch; merge only via reviewed review-package. Confirm
    **PRQ-1** was cleared by `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` before implementation.

## 4. Evidence the validator consumes

- The `policy/` engine + `tests/policy/` (run logs).
- The draft `ENSO-0005_LIGHT_CURVE.md`.
- This package's threat model, failure modes, and human-authority docs as the checklist basis.
- `trace/VALIDATION_CHECKLIST.md` (Spectrometer) universal gates.

## 5. Validator output

A Spectrometer validation package with: gate-by-gate results, independent bypass-test results, risk/gap list,
and a final **acceptance recommendation** (accept / accept-with-corrections / block). Blocking issues must be
resolved before human acceptance. A blocked gate is expected behaviour, not a failure.

## 6. Boundaries

Brief only. No validation runs now (nothing is implemented). This defines the bar the separately-approved
implementation must clear.
