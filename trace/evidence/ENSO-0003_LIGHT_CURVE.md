# Light Curve — ENSO-0003

Task ID: ENSO-0003
Feature ID: ENSO-F-0301
Sprint: Sprint 3 — Capability Governance Design
Mode History: discovery → review → (acceptance closeout)
Evidence Level: Full
Date: 2026-06-17
Worker(s): Claude (governance-design author) · Antigravity (validation/safety review) · Human owner (acceptance)

---

## Goal

Design how Magna Enso will control every Hermes-derived capability under a default-deny model, before any
Sprint 4 fork — **design/report-only, no code** — and record the human owner's acceptance.

## Outcome

**ACCEPTED — design/report-only** by the human owner on 2026-06-17 (EH-0014). `ENSO-F-0301` is **DONE**.

## What was produced (local-only, outside Git)

17 design reports under `../../ChatGPTReview/sprint-3-capability-governance-design/`:
capability taxonomy (corrected), capability policy schema, default-deny model, disablement tiers, unified
approval engine concept, policy chokepoint map, memory/skill draft-only, scheduler report-only, browser/web
read-only, terminal/code approval-required, messaging/cloud disabled, plugin/MCP governance, delegation
recursion control, Hermes surface governance matrix, Sprint 4 readiness gates, Sprint 3 Light Curve,
final recommendation.

> Per the local-only review-memory policy, full report contents are **not** copied into the repo; this
> Light Curve references them by location.

## Validation & corrections

- **Antigravity validation completed** — verdict **ACCEPTED_FOR_HUMAN_REVIEW**, no blocking issues. Reports
  under `../../ChatGPTReview/sprint-3-antigravity-validation/`.
- **Corrections RC-01 … RC-05 applied** (C-01 split into safe-status vs. sensitive reads; C-10 web/network
  externally-sensitive note; explicit taxonomy Boundaries section; browser implementation-timing clarification;
  per-model acceptance-meaning clarification).

## Boundaries recorded (what acceptance does NOT authorize)

- Sprint 3 is accepted as **design/report-only**.
- **No implementation, no runtime code, no policy-engine code approved.**
- **No Hermes fork, build, run, source modification, or direct adoption approved.** No Hermes source copied
  into `magna-enso/`.
- **Sprint 4 remains blocked / NOT STARTED** and requires a **separate approval package** + explicit human
  approval against the Sprint 4 readiness gates. Accepting the design is a design input, not a Sprint 4 go-ahead.
- **EH-0005B remains PROPOSED**; Hermes Agent **not activated**.

## Files changed in magna-enso/ (this closeout)

- `trace/FEATURE_TRACKER.md` — `ENSO-F-0301` → DONE + detail entry.
- `trace/STAR_MAP.md` — Sprint 3 accepted (design-only); Sprint 4 blocked/not started.
- `trace/DECISION_LOG.md` — added EH-0014; updated pending/open.
- `trace/RISK_REGISTER.md` — added Sprint 3 note.
- `trace/evidence/ENSO-0003_LIGHT_CURVE.md` — this file.

No runtime/source code, no `src/`, no commits/pushes.

## Validation results (real)

| Check | Result |
|---|---|
| Sprint 3 recorded as accepted / DONE | PASS |
| Only trace/status/evidence Markdown modified | PASS |
| No runtime/source code; no `src/` | PASS |
| No Hermes source copied; Hermes not run/built | PASS |
| Sprint 4 not started / blocked | PASS |
| EH-0005B remains PROPOSED | PASS |
| No commit / no push | PASS (baseline `94d63ed`) |

## Risks

R-06 (policy bypass) now has an accepted mitigation **design** (default-deny + chokepoint map + disablement
tiers + bypass-resistance), but **no enforcement yet** — that is Sprint 4 (fork) + Sprint 5 (engine).
R-04, R-05, R-07, R-08, R-09, R-10 each have an accepted governance model, enforcement pending. R-01, R-02
remain OPEN. See `trace/RISK_REGISTER.md` Sprint 3 note.

## Final Status

**DONE — human-accepted (design/report-only).** Human owner is final authority (EH-0010).

## Next Steps

1. Sprint 4 (clean governed Hermes fork baseline) is **blocked**; prepare a **separate Sprint 4 approval
   package** when explicitly requested, mapped to the Sprint 4 readiness gates.
2. No commit/push without separate explicit human instruction.
