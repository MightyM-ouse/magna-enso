# HERMES_SURFACE_GOVERNANCE_PLAN.md
# Magna Enso — Hermes Surface Governance Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PROPOSAL for human approval. Design-only. Based on Sprint 2 audit (Hermes @ 33b1d144).

---

## 1. Purpose

Propose the **MVP governance posture** for each Hermes-derived surface, combining capability state +
disablement tier. This is the heart of the Sprint 3 design and the input to the Sprint 4 retain/remove
decision. Design-only; nothing is built, disabled, or removed in Sprint 3.

## 2. Proposed per-surface MVP posture

| Surface | Proposed MVP posture | State | Disablement tier (if disabled/removed) |
|---|---|---|---|
| Background review | **disabled / remove** | disabled | T1/T2 (remove) |
| Curator / self-review | **report_only** | report_only | — |
| Memory writes | **draft_only** | draft_only | — |
| Skill writes | **draft_only** | draft_only | — |
| External memory (sync) | **disabled / remove** (or forced staging) | disabled | T1/T2 |
| Cron scheduler | **report_only** | report_only | — |
| Direct script cron | **remove** | disabled | T1/T2 (remove) |
| Subagent delegation | **disabled in MVP** | disabled | T3 |
| Browser snapshot | **read_only** | read_only | — |
| Browser actions | **approval_required or disabled** | approval_required / disabled | T3 if disabled |
| Terminal / code | **approval_required, disabled by default** | approval_required | T4 + gate (off by default) |
| Remote execution backends | **remove or disabled** | disabled | T1/T2 (prefer remove) |
| Messaging gateways | **disabled / remove** | disabled | T1 |
| API server listener | **disabled** | disabled | T1 (not started) |
| Cloud providers | **disabled** | disabled | T2 |
| Plugin / MCP loading | **disabled unless signed allowlist** | disabled | T2/T3 |

## 3. Rationale highlights

- **Remove, don't just disable, the worst offenders.** Remote execution backends, direct script cron, and
  background self-improvement can re-enable or be reached by alternate paths if merely flagged off; removal
  (T1/T2) eliminates the door (Sprint 2: cron/direct script execution is high risk; background
  self-improvement must be disabled or removed).
- **Listeners and gateways off by construction.** API server listener and messaging gateways are
  process-disabled (T1) so nothing is reachable from the network by default (protects R-05 public exposure).
- **Cloud/providers default-deny.** Disabled at module level (T2) to prevent cloud/provider creep (R-04).
- **Plugin/MCP dynamic loading is high risk.** Disabled unless a **signed allowlist** exists; dynamic
  loading of unsigned code is never allowed in MVP.
- **Memory/skill are draft_only.** Writes are staged and require human acceptance — no silent mutation,
  reversible (R-07, R-08, R-09).
- **Scheduler is report_only.** It proposes; it never auto-executes (R-10).
- **Browser split:** reading/snapshots are `read_only`; actions are `approval_required` or disabled.
- **Terminal/code is the most carefully gated *retained* capability:** disabled by default, and every
  invocation is `approval_required` and logged.
- **Delegation recursion disabled in MVP** to prevent uncontrolled agent-spawns-agent loops.

## 4. Retain / remove framing for Sprint 4

This plan does **not** finalize code-level retain/remove (that is Sprint 4 implementing this design). It
provides the **posture** each surface must have, so Sprint 4 knows what to keep behind a gate, what to
disable at which tier, and what to remove outright.

## 5. Decisions this informs

Decisions 5–12 in the approval template (remove-vs-disable for plugin/MCP, remote backends, messaging;
cloud disabled; memory/skill draft-only; scheduler report-only; terminal approval-required; delegation
disabled). Recommendation: **adopt the postures in §2 as the MVP baseline.**
