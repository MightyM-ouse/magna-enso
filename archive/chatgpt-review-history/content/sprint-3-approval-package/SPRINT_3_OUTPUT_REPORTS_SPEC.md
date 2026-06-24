# SPRINT_3_OUTPUT_REPORTS_SPEC.md
# Magna Enso — Sprint 3 Output Reports Specification
# Type: Local-only approval package
# Date: 2026-06-17
# Status: SPEC for reports produced AFTER approval. None produced yet. Design-only.

---

## 0. Naming authority note (read first)

Two distinct name sets exist, intentionally:

- **Approval-package files** (the documents in `ChatGPTReview/sprint-3-approval-package/`, e.g.
  `DEFAULT_DENY_POLICY_MODEL.md`, `HERMES_SURFACE_GOVERNANCE_PLAN.md`) are **planning artifacts** —
  they propose and plan Sprint 3. Their filenames carry `_PLAN` / `_PROPOSAL` / `_CONCEPT` suffixes.
- **Sprint 3 execution-report names** (e.g. `DEFAULT_DENY_MODEL.md`, `MESSAGING_CLOUD_DISABLED_MODEL.md`)
  are the **deliverables Sprint 3 will produce when it runs**. They are a separate set.

The difference is **intentional**. **This file (`SPRINT_3_OUTPUT_REPORTS_SPEC.md`) is authoritative for the
Sprint 3 execution-report names** — the report set in §2 below governs what Sprint 3 execution produces.
Where other approval-package files mention an execution-report name, they defer to §2 here.

---

## 1. Where the reports live

Default: **local-only first** (drafted under `ChatGPTReview/sprint-3-capability-governance/`), finalized
design committed later as `magna-enso/docs/design/` + `docs/adr/` **only on a separate human decision**
(matches the Sprint Plan: Sprint 3 deliverables are `docs/design/CAPABILITY_GOVERNANCE_DESIGN.md` + ADRs).
No `docs/design/` is created now.

## 2. Report set (covers the 15 design deliverables)

| # | Report | Covers |
|---|---|---|
| 1 | `CAPABILITY_TAXONOMY.md` | Capability taxonomy (deliverable 1) |
| 2 | `CAPABILITY_POLICY_SCHEMA.md` | Policy schema sketch (2) |
| 3 | `DEFAULT_DENY_MODEL.md` | Default-deny governance model (3) |
| 4 | `DISABLEMENT_TIERS.md` | Disablement tiers (4) |
| 5 | `UNIFIED_APPROVAL_ENGINE.md` | Unified approval engine concept (5) |
| 6 | `POLICY_CHOKEPOINT_MAP.md` | Policy chokepoint map (6) |
| 7 | `MEMORY_SKILL_DRAFT_ONLY_MODEL.md` | Memory/skill draft-only (7) |
| 8 | `SCHEDULER_REPORT_ONLY_MODEL.md` | Scheduler report-only (8) |
| 9 | `BROWSER_READ_ONLY_MODEL.md` | Browser/web read-only (9) |
| 10 | `TERMINAL_APPROVAL_MODEL.md` | Terminal/code approval-required (10) |
| 11 | `MESSAGING_CLOUD_DISABLED_MODEL.md` | Messaging/cloud disabled-by-default (11) |
| 12 | `PLUGIN_MCP_ALLOWLIST_MODEL.md` | Plugin/MCP signed-allowlist or removal (12) |
| 13 | `OUTBOUND_DELIVERY_SHUTDOWN_MODEL.md` | Outbound delivery shutdown (13) |
| 14 | `DELEGATION_RECURSION_CONTROL.md` | Delegation recursion control (14) |
| 15 | `SPRINT_4_READINESS_GATES.md` | Sprint 4 readiness gates (15) |
| 16 | `SPRINT_3_LIGHT_CURVE.md` | Evidence package; human approval pending |

(Reports may be consolidated; all 15 topics + the Light Curve must be covered.)

## 3. Common standard (TRACE Documentation Standard)

Each report: metadata header, purpose, scope, the design, design rationale (facts vs. judgments),
confidence, and links to Sprint 2 findings (cite paths + SHA `33b1d144`). **No Hermes source pasted.**
**No executable code** — schema sketches are illustrative design artifacts only.

## 4. The Sprint 4 readiness gates (report 15) must answer

1. What exact Hermes modules are retained?
2. What exact Hermes modules are removed?
3. What capability states apply to every retained surface?
4. Where is default-deny enforced?
5. How is approval logged?
6. How are memory/skill writes staged?
7. How is the scheduler made report-only?
8. How are cloud/messaging/MCP/plugin surfaces disabled?
9. How are remote execution backends removed or blocked?
10. How is bypass-resistance validated?

Sprint 4 **cannot start** until these are answered and accepted.

## 5. Light Curve (report 16) requirements

Mode History: discovery → review. Inputs used (Sprint 2 reports + SHA), design reports produced, risks
(link R-01, R-02, R-04, R-05, R-06, R-07, R-08, R-09, R-10), Antigravity validation result, Final Status:
in_review, Human Approval: pending. **No self-approval.**

## 6. Acceptance flow

Design drafted (Claude, governance) with Codex feasibility input → Antigravity validates (bypass-resistance,
default-deny coverage, no scope creep) → Grok challenges → ChatGPT continuity → `SPRINT_3_LIGHT_CURVE.md`
written → **human owner accepts**. Only then is Sprint 3 DONE; Sprint 4 is considered separately.
