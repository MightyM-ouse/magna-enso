# SPRINT_3_LIGHT_CURVE.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 16 of 17 — Light Curve (evidence package)
# Type: Design-only governance evidence. No code.
# Date: 2026-06-17

---

Task ID: ENSO-0003
Feature ID: ENSO-F-0301 (Capability taxonomy + policy schema / governance design)
Sprint: Sprint 3 — Capability Governance Design
Mode History: discovery → review
Evidence Level: Full
Worker(s): Claude (governance-design author). Inputs from Sprint 2 audit (Codex) + validation (Antigravity).

## Goal

Design how Magna Enso will control every Hermes-derived capability under a default-deny model, before any
Sprint 4 fork — design/report only, no code.

## Context Route Used

`capability-governance` (planned area) — Sprint 3 approval package
(`ChatGPTReview/sprint-3-approval-package/`) + Sprint 2 audit & validation references
(`ChatGPTReview/sprint-2-hermes-audit/`, `ChatGPTReview/sprint-2-antigravity-validation/`). Hermes @ `33b1d144`.

## Inputs Inspected (read-only)

- Sprint 2 audit: `ACTION_DISPATCH_MAP`, `AUTONOMY_ENTRY_POINT_MAP`, `EXTERNAL_SURFACE_MAP`,
  `CAPABILITY_GATING_FEASIBILITY`, `MAGNA_ENSO_REUSE_RECOMMENDATION` (+ provenance/license).
- Sprint 2 Antigravity validation reports.
- Magna Enso trace: `STAR_MAP.md`, `FEATURE_TRACKER.md`, `DECISION_LOG.md`, `RISK_REGISTER.md`,
  `evidence/ENSO-0002_LIGHT_CURVE.md`.
- Sprint 3 approval package (14 files).

## Files Produced (design reports — all under ChatGPTReview/sprint-3-capability-governance-design/)

1. `CAPABILITY_TAXONOMY.md`
2. `CAPABILITY_POLICY_SCHEMA.md`
3. `DEFAULT_DENY_MODEL.md`
4. `DISABLEMENT_TIERS_MODEL.md`
5. `UNIFIED_APPROVAL_ENGINE_MODEL.md`
6. `POLICY_CHOKEPOINT_MAP.md`
7. `MEMORY_SKILL_DRAFT_ONLY_MODEL.md`
8. `SCHEDULER_REPORT_ONLY_MODEL.md`
9. `BROWSER_WEB_READ_ONLY_MODEL.md`
10. `TERMINAL_CODE_APPROVAL_REQUIRED_MODEL.md`
11. `MESSAGING_CLOUD_DISABLED_MODEL.md`
12. `PLUGIN_MCP_GOVERNANCE_MODEL.md`
13. `DELEGATION_RECURSION_CONTROL_MODEL.md`
14. `HERMES_SURFACE_GOVERNANCE_MATRIX.md`
15. `SPRINT_4_READINESS_GATES.md`
16. `SPRINT_3_LIGHT_CURVE.md` (this file)
17. `FINAL_RECOMMENDATION.md`

## Files Changed in magna-enso/

**None.** No runtime/source code, no `src/`, no `docs/`, no commits. All Sprint 3 output is local-only under
`ChatGPTReview/sprint-3-capability-governance-design/`.

## Commands Run

Documentation-only/read-only: directory listing, reading Sprint 2 reference reports, creating Markdown design
files. No build, no tests, no Hermes execution, no clone.

## Validation Results (real)

| Check | Result |
|---|---|
| 17 design reports created | PASS |
| No implementation/runtime code created | PASS (Markdown design only) |
| No `magna-enso/src/` or runtime files | PASS |
| No Hermes source copied | PASS (reports cite identifiers/paths + SHA only) |
| Hermes not run/built/cloned this sprint | PASS (pre-existing Sprint 2 scratch clone untouched) |
| Sprint 4 not started | PASS |
| EH-0005B remains PROPOSED | PASS |
| No commit / no push | PASS (baseline `94d63ed`) |

## Findings

The design resolves the Sprint 2 risk (no single complete chokepoint) via: a 20-category capability
taxonomy, a per-capability policy schema, a mandatory default-deny model, five disablement tiers (with
strong tiers for dangerous surfaces), a unified approval engine concept, a 13-boundary chokepoint map, and
per-surface MVP postures consolidated in a governance matrix. Sprint 4 readiness gates are defined and
mostly require human acceptance + Antigravity validation to turn green.

## Risks

Links: R-01 (reuse), R-02 (license/deps — full transitive review still future), R-04 (cloud), R-05 (exposure),
R-06 (policy bypass — primary risk addressed by chokepoint map + default-deny), R-07/R-08/R-09
(memory/skill draft-only), R-10 (scheduler report-only), R-13 (overengineering — bounded to spec).

## Final Status

**IN_REVIEW** — pending Antigravity validation and explicit human-owner acceptance.

## Human Approval

**Pending.** No self-approval. Antigravity validates next; the human owner is final authority (EH-0010).

## Next Steps

1. Antigravity validates the 17 Sprint 3 reports (default-deny coverage, bypass-resistance, no scope creep,
   design-only).
2. Grok second opinion; ChatGPT continuity update.
3. Human owner reviews and accepts (or requests changes) → then Sprint 3 is DONE.
4. Only then is Sprint 4 (clean governed fork) considered, separately, against the readiness gates.
