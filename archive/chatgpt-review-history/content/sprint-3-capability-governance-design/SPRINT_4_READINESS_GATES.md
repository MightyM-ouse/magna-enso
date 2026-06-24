# SPRINT_4_READINESS_GATES.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 15 of 17 — Sprint 4 Readiness Gates
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define the gates that **must all pass** before Sprint 4 (clean governed Hermes fork baseline) may start.
Sprint 4 is **blocked** until every gate is green and the human owner accepts Sprint 3.

## 2. Readiness gates

| # | Gate | Met by | Status |
|---|---|---|---|
| G-01 | All **retained** surfaces mapped (with state + gate) | `HERMES_SURFACE_GOVERNANCE_MATRIX.md` §2 (Retain) | ✅ designed |
| G-02 | All **removed** surfaces listed | Matrix §3 (Remove/Disable) | ✅ designed |
| G-03 | Capability **state** assigned to every retained surface | Matrix col "MVP state" + `CAPABILITY_TAXONOMY.md` | ✅ designed |
| G-04 | **Default-deny** model accepted | `DEFAULT_DENY_MODEL.md` | ⛔ needs human acceptance |
| G-05 | **Unified approval** concept accepted | `UNIFIED_APPROVAL_ENGINE_MODEL.md` | ⛔ needs human acceptance |
| G-06 | **Policy chokepoints** accepted (all 13 boundaries gated/removed) | `POLICY_CHOKEPOINT_MAP.md` | ⛔ needs human acceptance |
| G-07 | **Disablement tiers** accepted (per surface) | `DISABLEMENT_TIERS_MODEL.md` | ⛔ needs human acceptance |
| G-08 | **Memory/skill draft-only** accepted | `MEMORY_SKILL_DRAFT_ONLY_MODEL.md` | ⛔ needs human acceptance |
| G-09 | **Scheduler report-only** accepted | `SCHEDULER_REPORT_ONLY_MODEL.md` | ⛔ needs human acceptance |
| G-10 | **Browser/web** model accepted | `BROWSER_WEB_READ_ONLY_MODEL.md` | ⛔ needs human acceptance |
| G-11 | **Plugin/MCP** model accepted | `PLUGIN_MCP_GOVERNANCE_MODEL.md` | ⛔ needs human acceptance |
| G-12 | **Outbound delivery shutdown** accepted | `MESSAGING_CLOUD_DISABLED_MODEL.md` | ⛔ needs human acceptance |
| G-13 | **Terminal/code approval-required** accepted | `TERMINAL_CODE_APPROVAL_REQUIRED_MODEL.md` | ⛔ needs human acceptance |
| G-14 | **Delegation disabled (MVP)** accepted | `DELEGATION_RECURSION_CONTROL_MODEL.md` | ⛔ needs human acceptance |
| G-15 | **Bypass-resistance** argued (no ungated path to any non-disabled capability) | `POLICY_CHOKEPOINT_MAP.md` §5 coverage | ✅ designed; ⛔ Antigravity to validate |
| G-16 | **Antigravity validates** Sprint 3 reports | (pending Sprint 3 validation) | ⛔ pending |
| G-17 | **Human owner accepts** Sprint 3 | (pending) | ⛔ pending |

## 3. The ten core questions Sprint 4 must be able to answer (from the approval package)

1. What exact Hermes modules are retained? → Matrix §3 (Retain).
2. What exact Hermes modules are removed? → Matrix §3 (Remove/Disable).
3. What capability states apply to every retained surface? → Matrix col "MVP state".
4. Where is default-deny enforced? → `POLICY_CHOKEPOINT_MAP.md` P-01…P-13 + `DEFAULT_DENY_MODEL.md`.
5. How is approval logged? → `UNIFIED_APPROVAL_ENGINE_MODEL.md` (approval record + audit_log_reference).
6. How are memory/skill writes staged? → `MEMORY_SKILL_DRAFT_ONLY_MODEL.md`.
7. How is the scheduler made report-only? → `SCHEDULER_REPORT_ONLY_MODEL.md`.
8. How are cloud/messaging/MCP/plugin surfaces disabled? → `MESSAGING_CLOUD_DISABLED_MODEL.md`, `PLUGIN_MCP_GOVERNANCE_MODEL.md`.
9. How are remote execution backends removed/blocked? → Matrix (remove, T1/T2) + `DISABLEMENT_TIERS_MODEL.md`.
10. How is bypass-resistance validated? → `POLICY_CHOKEPOINT_MAP.md` §5 + Antigravity validation (G-16).

## 4. What "model acceptance" means (RC-05)

For gates G-04…G-14, "accepted" means:

- Each governance model has been **reviewed and accepted as a design input** for Sprint 4.
- **Acceptance does NOT authorize implementation.** It confirms the *design* is agreed; it does not enable,
  build, fork, or run anything.
- **Sprint 4 still requires separate, explicit approval** to begin — accepting these models is necessary but
  not sufficient. A distinct human go-ahead (its own approval package + decision) starts Sprint 4.

In short: accepting a model = "this design is approved as the plan." Starting Sprint 4 = a separate decision.

## 5. Blocking rule

Sprint 4 **must not start** until G-04…G-17 are satisfied: every model accepted **as a design input** by the
human owner, Antigravity validation passed, and Sprint 3 formally accepted — **and** Sprint 4 itself is then
**separately approved**. Design completeness (G-01…G-03, G-15) is necessary but **not sufficient**; human
acceptance, independent validation, and a separate Sprint 4 go-ahead are the hard gates.

## 6. Boundaries

Design only. These gates govern *when* Sprint 4 may begin; they authorize nothing themselves.
