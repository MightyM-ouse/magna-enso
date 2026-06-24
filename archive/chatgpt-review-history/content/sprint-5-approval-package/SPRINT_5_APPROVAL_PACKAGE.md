# SPRINT_5_APPROVAL_PACKAGE.md
# Magna Enso — Sprint 5 Approval Package (overview / brief)
# Type: Local-only approval package (planning / approval-preparation)
# Prepared by: Claude (architecture & governance planning worker)
# Date: 2026-06-20
# Status: FOR HUMAN APPROVAL. Sprint 5 NOT started. No implementation. No commits.

---

## 1. One-paragraph summary

Sprint 5 — **Policy Engine Foundation** — would implement the capability-policy engine designed in Sprint 3:
**default-deny capability gating** (`ENSO-F-0501`) and the **approval-request flow + decision/evidence
logging** (`ENSO-F-0502`), with `tests/` proving allow / deny / approve paths and **no bypass at the harness
level** (R-06 stays OPEN; real entry points are validated per-capability later). It is the
first sprint that turns the accepted governance *design* into enforceable *code* — it directly addresses the
project's only CRITICAL open risk, **R-06 (policy bypass)**. This package is **approval preparation only**;
it authorizes nothing and starts nothing.

## 2. Baseline (verified at preflight)

| Item | Value |
|---|---|
| Implementation baseline | `main` @ `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` |
| Accepted Sprint 4 baseline commit | `c7bb2b2d695f5ad1ce9c7e22d7dd6f22312c0f46` |
| Working tree | clean (`## main`, no changes) |
| Sprint 4 | accepted (EH-0015); inert metadata-only vendor baseline |
| Sprint 5 | NOT STARTED (`ENSO-F-0501`, `ENSO-F-0502` = PLANNED) |
| Runtime enforcement | NOT IMPLEMENTED |
| R-06 | **OPEN** (CRITICAL) |
| EH-0005B | **PROPOSED** |
| Hermes Agent | inactive |
| PRQ-1 | **CLEARED** by `4d5c203cc236be84bd4b9bd8004cb88e8797a34d` |

## 3. Canonical scope (from repository source of truth)

From `planning/MAGNA_ENSO_SPRINT_PLAN.md` §SPRINT_5 ("Policy Engine Foundation") and the
`planning/MAGNA_ENSO_FEATURE_TRACKER_TEMPLATE.md` ENSO-F-0501 detail card:

- **Purpose:** implement the Sprint 3 capability-policy engine — report-and-approve, default-deny.
- **Features:** policy loading, capability gating, approval-request flow, decision/evidence logging,
  reversibility checks. **No auto-execution.**
- **Non-Goals:** no remote control, no scheduler, no UI.
- **Deliverables:** `policy/` engine + integration into the runtime gate path; `tests/` for allow/deny/approve.
- **Acceptance:** no-policy ⇒ denied; approve-required ⇒ HOLD pending a decision-provider result; Sprint 5
  tests use programmatically simulated decisions, while an absent production provider always ⇒ DENY; all outcomes logged;
  **no path bypasses the gate** — provable in Sprint 5 only at the **harness level** (R-06 stays OPEN; real
  entry points re-validated per-capability later).
- **Evidence:** Light Curve (Full); Spectrometer checklist; Antigravity adversarial test report.
- **Worker / Risk:** Codex (engine) + Antigravity (validation) + Grok (edge cases); **HIGH**.

See `CANONICAL_SCOPE_AND_NON_GOALS.md` for the full feature mapping and the key architecture clarification.

## 4. Key architecture finding (must read)

The Sprint 4 vendor baseline (`vendor/hermes/`) is **inert metadata only** — per
`vendor/hermes/RETAINED_SURFACE_STATES.yaml` (`runtime_enforcement: not_implemented`, `executable: false`)
**no executable capability runtime exists** to gate. Therefore Sprint 5 builds the policy engine + gate +
approval flow + logging as **Magna-owned standalone enforcement-core code**, proven against a **Magna-owned
gate interface / test harness** — not against live Hermes execution. This is the central open decision
(D-1) in `RISKS_OPEN_QUESTIONS_AND_DECISIONS.md`.

## 5. Files in this package

1. `SPRINT_5_APPROVAL_PACKAGE.md` (this) · 2. `CANONICAL_SCOPE_AND_NON_GOALS.md` ·
3. `ENFORCEMENT_ARCHITECTURE.md` · 4. `THREAT_MODEL_AND_BYPASS_ANALYSIS.md` ·
5. `HUMAN_AUTHORITY_AND_APPROVAL_BOUNDARIES.md` · 6. `FAILURE_MODES_AND_FAIL_CLOSED_BEHAVIOR.md` ·
7. `IMPLEMENTATION_SEQUENCE.md` · 8. `TEST_AND_VALIDATION_PLAN.md` · 9. `ROLLBACK_AND_RECOVERY_PLAN.md` ·
10. `RISKS_OPEN_QUESTIONS_AND_DECISIONS.md` · 11. `INDEPENDENT_VALIDATION_BRIEF.md` ·
12. `PROPOSED_CODEX_IMPLEMENTATION_PROMPT.md` (draft, **blocked** pending approval).

## 6. Headline recommendation

**Approve Sprint 5 as the policy-engine enforcement core (ENSO-F-0501 + ENSO-F-0502), scoped to a
Magna-owned engine + gate interface + test harness, in an isolated branch, no auto-commit/push** — after you
sign the decision block in §8 and resolve open decisions **D-1…D-8** (`RISKS_OPEN_QUESTIONS_AND_DECISIONS.md`
is the consolidated decision register; this overview §8 carries the sign-off form). There is **no separate
`FINAL_RECOMMENDATION.md`** in this 12-file package — the recommendation lives here and in the risks/decisions
file. Until you sign, Sprint 5 stays blocked.

## 7. What approval does NOT authorize

No runtime/production execution of real capabilities; no scheduler/remote/UI (Non-Goals); no Hermes
run/build/import/activation; no EH-0005B promotion; no Hermes Agent activation; no Sprint 6; and **no claim
that runtime enforcement is "done"** until Antigravity validation + human acceptance.

## 8. Human approval decision (sign here — none of this is started yet)

```text
PREREQUISITE:
  [x] PRQ-1 CLEARED: STAR_MAP refreshed through the controlled trace commit
      4d5c203cc236be84bd4b9bd8004cb88e8797a34d. This clears only the trace prerequisite;
      it does not approve or start Sprint 5.

Decision (choose one):
  [ ] APPROVE Sprint 5 — policy-engine enforcement core (ENSO-F-0501 + ENSO-F-0502), as scoped below
  [ ] APPROVE WITH CONDITIONS: ____________________________________________
  [ ] HOLD — resolve D-1 through D-8 / conditions first
  [ ] REJECT

Confirmed scope & conditions (recommended defaults):
  - D-1 harness scope: engine + gate interface + test harness (no real runtime exists)        [ ]
  - D-2 approval model: in-memory decision + append-only audit log, single-use,
        restart => fresh human decision                                                       [ ]
  - D-3 policy format: JSON for RUNTIME policy records (stdlib json); YAML reference-only      [ ]
  - D-4 stack: Python stdlib only (no new dependency without separate approval)               [ ]
  - D-5 R-06 stays OPEN; end-to-end chokepoint validation RECURS per real capability           [ ]
  - D-6 Codex lead; Antigravity validation (mandatory); Grok edge-case                         [ ]
  - D-7 HumanDecisionProvider interface; TEST-ONLY provider uses programmatically simulated
        decisions; human-only is a future production invariant; NO authenticated production
        provider exists; missing/default production provider => DENY                           [ ]
  - D-8 Audit durability: append-only JSONL, atomic append + flush, corruption detection
        (hash-chain), malformed-tail recovery — NOT tamper-proof vs a local admin              [ ]
  - Isolated branch sprint/05-policy-engine; NO auto-commit/push; merge only via reviewed pkg  [ ]
  - No Hermes import/run/build; EH-0005B stays PROPOSED; Hermes Agent inactive; no Sprint 6    [ ]

Approved by (human owner): ____________________   Date: __________
```

PRQ-1 is cleared, but D-1 through D-8 remain pending human confirmation. Until this decision block is
signed and those decisions are confirmed, Sprint 5 remains **NOT STARTED**. This package changed no
`magna-enso/` files.
