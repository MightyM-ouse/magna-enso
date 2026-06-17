# Light Curve — ENSO-0002

Task ID: ENSO-0002
Feature ID: ENSO-F-0201
Sprint: Sprint 2 — Hermes Read-Only Audit
Mode History: read-only audit → validation → correction → human acceptance
Evidence Level: Full audit closeout
Date: 2026-06-17
Worker(s): Codex (primary source inspector) · Antigravity (validation) · Human owner (final acceptance)

---

## Goal

Close Sprint 2 as human accepted after a read-only audit of Hermes Agent. The audit evaluated whether Hermes is suitable as a future Sprint 4 clean governed fork baseline candidate for Magna Enso.

No implementation, fork, activation, build, run, dependency install, or Hermes source copy was approved or performed.

## Source Audited

- Hermes repository: `https://github.com/nousresearch/hermes-agent`
- Audited Hermes SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Scratch clone location used by the audit: `/Users/vinay/Projects/AI/Magna/_scratch/hermes-readonly-audit/hermes-clone/`
- Local-only Codex audit reports: `../../ChatGPTReview/sprint-2-hermes-audit/`
- Local-only Antigravity validation reports: `../../ChatGPTReview/sprint-2-antigravity-validation/`

## Files Inspected

- Sprint 2 approval package under `../../ChatGPTReview/sprint-2-approval-package/` (read-only).
- Magna Enso trace files under `trace/` (read-only before closeout updates).
- Hermes source under approved scratch clone path (read-only).
- Codex Sprint 2 audit reports under `../../ChatGPTReview/sprint-2-hermes-audit/`.
- Antigravity Sprint 2 validation reports under `../../ChatGPTReview/sprint-2-antigravity-validation/`.

## Files Changed

Sprint 2 acceptance closeout updated only trace/status/evidence Markdown files:

| File | Change |
|---|---|
| `trace/FEATURE_TRACKER.md` | Marked ENSO-F-0201 as DONE and added Sprint 2 feature detail. |
| `trace/STAR_MAP.md` | Updated current project state to Sprint 2 accepted and next action to Sprint 3 approval preparation only. |
| `trace/DECISION_LOG.md` | Added EH-0013 recording Sprint 2 acceptance and Hermes conditional suitability. |
| `trace/RISK_REGISTER.md` | Added Sprint 2 risk posture note. |
| `trace/evidence/ENSO-0002_LIGHT_CURVE.md` | Added this Sprint 2 evidence closeout. |

## Audit Reports

Codex created the following local-only audit reports under `../../ChatGPTReview/sprint-2-hermes-audit/`:

- `HERMES_PROVENANCE.md`
- `LICENSE_AND_DEPENDENCY_REVIEW.md`
- `HERMES_CODE_MAP.md`
- `ACTION_DISPATCH_MAP.md`
- `AUTONOMY_ENTRY_POINT_MAP.md`
- `EXTERNAL_SURFACE_MAP.md`
- `CAPABILITY_GATING_FEASIBILITY.md`
- `MAGNA_ENSO_REUSE_RECOMMENDATION.md`
- `SPRINT_2_LIGHT_CURVE.md`

These reports remain outside Git and outside `magna-enso/`. Their contents were not copied into the repo.

## Antigravity Validation Outcome

Antigravity validation accepted Sprint 2 for human review with no blocking issues.

Two non-blocking corrections were applied to the local-only Sprint 2 audit reports:

- `SPRINT_2_LIGHT_CURVE.md` received a format note explaining its audit-specific structure.
- `AUTONOMY_ENTRY_POINT_MAP.md` received a count clarification that the audit identifies 13 autonomy entry points.

## Findings

- Hermes is a substantial agent platform with core agent orchestration, tool registry, toolsets, skills, memory, scheduler, terminal/code execution, browser tooling, messaging/API gateways, cloud/provider integrations, plugin/MCP extension points, and UI/runtime shells.
- Hermes has useful architecture for future governed fork consideration.
- Hermes also has broad autonomy and external-action surfaces.
- Hermes lacks one complete policy chokepoint today.
- Hermes is therefore accepted only as **conditionally suitable** for future governed fork consideration.

## Governance Boundaries Preserved

- Hermes is not approved for direct adoption.
- Hermes is not approved for activation.
- Hermes is not approved for build or run.
- Hermes is not approved for fork or implementation.
- Hermes source was not copied into `magna-enso/`.
- No `docs/audit/` folder was created.
- No runtime/source code was created.
- EH-0005B remains **PROPOSED**.
- Sprint 3 remains **NOT STARTED**.
- Sprint 4 remains **NOT STARTED**.

## Validation Results

| Check | Result |
|---|---|
| Codex read-only audit completed | PASS |
| Antigravity validation completed | PASS |
| Light Curve correction completed | PASS |
| Autonomy count correction completed | PASS |
| Hermes audited SHA recorded | PASS |
| Hermes source copied into `magna-enso/` | PASS — not copied |
| Hermes direct adoption / activation / build / run / fork / implementation | PASS — not approved or performed |
| EH-0005B remains PROPOSED | PASS |
| Sprint 3 not started | PASS |
| Sprint 4 not started | PASS |

## Risks / Gaps

| ID | Item | Status |
|---|---|---|
| R-01 | Hermes reuse / coupling | OPEN — conditional suitability only |
| R-02 | License / dependency / ToS | OPEN — top-level MIT verified; deeper dependency/plugin review remains future work |
| R-06 | Policy bypass | OPEN — Sprint 3 governance design must address missing central policy chokepoint |
| EH-0005B | Hermes Agent as candidate UI/E2E worker | PROPOSED — not promoted |

## Human Authority Statement

- Codex does not self-approve.
- Antigravity does not self-approve.
- The human owner (Vinay) explicitly accepted Sprint 2 and remains final authority under EH-0010.

## Final Status

**ACCEPTED / DONE** — Sprint 2 is human accepted. ENSO-F-0201 is DONE.

## Next Steps

1. Prepare Sprint 3 approval package when explicitly requested.
2. Sprint 3 execution begins only after separate human approval.
3. Sprint 4 remains not started and is not approved.
4. Do not adopt, activate, build, run, fork, or implement Hermes without future explicit approval.
