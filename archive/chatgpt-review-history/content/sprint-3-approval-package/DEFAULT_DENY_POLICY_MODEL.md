# DEFAULT_DENY_POLICY_MODEL.md
# Magna Enso — Default-Deny Policy Model
# Type: Local-only approval package
# Date: 2026-06-17
# Status: DESIGN PROPOSAL for human approval (Decision 4). Design-only; no engine implemented.

---

## 1. Principle

> No capability runs unless an explicit policy allows it. Absence of a policy = denial.

Default-deny is **mandatory** (recommended Decision 4 = Mandatory). It is the foundation that makes every
other control trustworthy: forgotten or newly-introduced capabilities are safe (denied) by construction.

## 2. Evaluation model (concept)

```text
capability call
   │
   ▼
[Polaris gate]  ── look up policy for (capability, path, context)
   │
   ├─ no policy found                → DENY  (default-deny)
   ├─ policy.state == disabled       → DENY  (and ideally never reached: see disablement tiers)
   ├─ policy.state == read_only      → ALLOW read; DENY mutate/side-effect
   ├─ policy.state == report_only    → ALLOW report; DENY execute
   ├─ policy.state == draft_only     → ALLOW stage; DENY persist (until human accepts)
   ├─ policy.state == approval_required → HOLD → request human approval → ALLOW once, logged
   └─ policy.state == active_safe    → ALLOW (no external/persistent effect)
   │
   ▼
log outcome (Event Horizon / Light Curve)
```

Every outcome — allow, deny, hold-for-approval — is **logged**. Deny is normal, expected behavior, not an error.

## 3. Policy schema (illustrative sketch — design artifact, not code)

```yaml
# magna-enso capability policy (SKETCH — Sprint 3 design artifact only)
capability: "terminal.exec"
surface: "terminal"
state: "approval_required"      # one of the six capability states
default: "deny"                 # explicit; absence of policy also denies
paths_covered:                  # ALL execution paths that can reach this capability
  - dispatch
  - startup
  - scheduler
  - gateway
  - provider
  - acp
  - plugin
  - mcp
approval:
  required: true
  approver: "human_owner"
  scope: "per_action"
  log: "event_horizon"
reversible: false
network_scope: "lan_local_only"
notes: "Disabled by default; each invocation gated and logged."
```

> This is a **shape**, to be refined in Sprint 3. It is not parsed or executed by anything in Sprint 3.

## 4. Coverage requirement (the non-negotiable)

Per the Sprint 2 finding (no single complete chokepoint), a policy is only valid if it declares the
**paths_covered** and those paths are **all** the ways the capability can be reached: dispatch, startup,
scheduler, gateway, provider, memory, skill, ACP, plugin, MCP. A capability reachable by an uncovered path
is, in effect, ungoverned. Bypass-resistance validation (Sprint 3 gate 10) checks exactly this.

## 5. Promotion & change control

- New/unknown capability ⇒ `disabled` until classified.
- Moving to a less restrictive state requires explicit human action + an Event Horizon entry.
- No worker may self-promote a capability; no silent state changes.

## 6. Relationship to disablement tiers

For `disabled` capabilities, default-deny at the gate is the *last* line. Stronger is to prevent the
capability from ever loading/registering (see `DISABLEMENT_TIERS_PROPOSAL.md`). Defense in depth: remove
where possible, disable at multiple tiers, and still deny at the gate.

## 7. Decision requested (Decision 4)

Approve **default-deny as mandatory** for Magna Enso. Recommendation: **Mandatory.**
