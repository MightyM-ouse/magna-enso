# CAPABILITY_GOVERNANCE_DESIGN_PLAN.md
# Magna Enso — Capability Governance Design Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN for execution AFTER approval. Design-only. Nothing implemented.

---

## 1. Objective

Produce the design for Magna Enso's capability-governance model — the runtime "Polaris" layer — so that
Sprint 4 can fork Hermes onto a default-deny, fully-gated foundation. **No code.**

## 2. The 15 design deliverables

| # | Deliverable | Output report (see reports spec) |
|---|---|---|
| 1 | Capability taxonomy | `CAPABILITY_TAXONOMY.md` |
| 2 | Capability policy schema (sketch) | `CAPABILITY_POLICY_SCHEMA.md` |
| 3 | Default-deny governance model | `DEFAULT_DENY_MODEL.md` |
| 4 | Disablement tiers | `DISABLEMENT_TIERS.md` |
| 5 | Unified approval engine concept | `UNIFIED_APPROVAL_ENGINE.md` |
| 6 | Policy chokepoint map | `POLICY_CHOKEPOINT_MAP.md` |
| 7 | Memory/skill draft-only model | `MEMORY_SKILL_DRAFT_ONLY_MODEL.md` |
| 8 | Scheduler report-only model | `SCHEDULER_REPORT_ONLY_MODEL.md` |
| 9 | Browser/web read-only model | `BROWSER_READ_ONLY_MODEL.md` |
| 10 | Terminal/code approval-required model | `TERMINAL_APPROVAL_MODEL.md` |
| 11 | Messaging/cloud disabled-by-default model | `MESSAGING_CLOUD_DISABLED_MODEL.md` |
| 12 | Plugin/MCP signed-allowlist or removal model | `PLUGIN_MCP_ALLOWLIST_MODEL.md` |
| 13 | Outbound delivery shutdown model | `OUTBOUND_DELIVERY_SHUTDOWN_MODEL.md` |
| 14 | Delegation recursion control | `DELEGATION_RECURSION_CONTROL.md` |
| 15 | Sprint 4 readiness gates | `SPRINT_4_READINESS_GATES.md` |

(These may be consolidated into fewer files during execution; the 15 topics must all be covered.)

> **Naming note (intentional).** The output-report names in the table above are **future Sprint 3
> execution deliverables** and are a different set from this approval package's own planning-artifact
> filenames (e.g. `DEFAULT_DENY_POLICY_MODEL.md`, `HERMES_SURFACE_GOVERNANCE_PLAN.md`). This difference is
> intentional. **`SPRINT_3_OUTPUT_REPORTS_SPEC.md` is authoritative for the Sprint 3 execution-report
> names**; if any name here and there differ, the spec wins.

## 3. Method

1. **Start from the Sprint 2 maps** (dispatch, autonomy entry points, external surface, gating feasibility)
   for Hermes @ `33b1d144`. Do not re-audit.
2. **Enumerate every capability and every execution path** that can reach it (the chokepoint map).
3. **Assign a capability state** (disabled / read_only / draft_only / report_only / approval_required /
   active_safe) to every surface — defaulting to deny.
4. **Define disablement tier** for anything `disabled` (process / module / registration / dispatch / config).
5. **Define the unified approval path** all sensitive actions route through (concept).
6. **Specify retain/remove** per Hermes module, with the capability state for everything retained.
7. **Define bypass-resistance validation** — how the design proves no path reaches a capability around the gate.
8. **Answer the Sprint 4 readiness gates.**

## 4. Design principles (binding)

- **Default-deny** is mandatory.
- **Single auditable chokepoint** for all sensitive actions; cover *all* paths (dispatch, startup, scheduler,
  gateway, provider, memory, skill, ACP, plugin, MCP).
- **States over booleans** — capabilities have states, not just on/off.
- **Removal beats disablement** for the most dangerous surfaces (remote execution backends, background
  self-improvement, direct script cron) where "disabled" could be re-enabled or bypassed.
- **Reversibility + evidence** — every sensitive action is logged; memory/skill writes are reversible drafts.
- **Human authority** — material actions require human approval; no self-approval.

## 5. Constraints

Design-only. No code, no Hermes build/run/clone, no Hermes source in `magna-enso/`, no commits/pushes, no
Sprint 4 work. Antigravity validates; human owner accepts.

## 6. Stop condition

When all 15 topics are designed, the readiness gates answered, Antigravity validation passed, and the
`SPRINT_3_LIGHT_CURVE.md` written → **stop** and present to the human owner. Sprint 4 is considered separately.
