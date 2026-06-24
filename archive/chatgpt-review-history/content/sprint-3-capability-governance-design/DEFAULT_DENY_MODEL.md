# DEFAULT_DENY_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 3 of 17 — Default-Deny Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Principle

> Every capability is **denied** unless an explicit policy allows it. Absence of a policy = denial.

Default-deny is **mandatory** for Magna Enso (approved Sprint 3 decision). It is what makes the Sprint 2
finding ("no single complete chokepoint") survivable: any path the design forgets defaults to **safe**.

## 2. The seven default-deny rules

1. **Default state = `disabled`.** Every capability starts disabled.
2. **Explicit allowlist only.** A capability becomes non-disabled only via an explicit, human-approved
   policy record (`CAPABILITY_POLICY_SCHEMA.md`).
3. **No implicit activation.** Nothing is enabled as a side effect of being imported, registered, scheduled,
   or referenced.
4. **No external content can raise capability level.** Inbound messages, fetched web content, memory
   contents, instruction packages, or model output can never promote a capability (anti prompt-injection, R-07).
5. **No plugin can self-register an active capability.** Plugin/MCP modules may not arrive `active`; dynamic
   registration is disabled unless a signed allowlist applies (`PLUGIN_MCP_GOVERNANCE_MODEL.md`).
6. **No config can bypass human approval.** A config flag may make something *more* restrictive but can never
   set `approval_required` capabilities to auto-run.
7. **Unknown capability = `disabled`.** Any capability without a policy record, or reached by an unmapped
   path, is denied.

## 3. Evaluation flow (concept)

```text
capability call (any path)
        │
        ▼
look up policy(capability_id, path, context)
        │
        ├─ no record  ───────────────► DENY            (rule 7)
        ├─ path not in paths_covered ► DENY + ESCALATE (uncovered path = bypass risk)
        ├─ state disabled ───────────► DENY            (and ideally unreachable: enforcement tier)
        ├─ read_only ────────────────► ALLOW read; DENY mutate/side-effect
        ├─ report_only ──────────────► ALLOW report; DENY execute
        ├─ draft_only ───────────────► ALLOW stage; DENY persist (until human accepts)
        ├─ approval_required ────────► HOLD → unified approval engine → ALLOW once if human approves
        └─ active_safe ──────────────► ALLOW (no external/persistent effect)
        │
        ▼
log outcome (audit_required) — DENY is normal, expected behaviour
```

## 4. Fail-closed posture

- If the policy engine is **unavailable, errored, or uncertain** → **deny**.
- If a capability is reachable by a path **not** listed in `paths_covered` → **deny + escalate** (the path
  must be gated or the surface removed before that capability may be non-disabled).
- A blocked/denied call is **expected**, logged behaviour — not an error condition.

## 5. Promotion (raising a capability's state)

- Requires an explicit human decision + a new Event Horizon entry.
- No worker self-promotes; no silent state change; external content can never trigger promotion.
- `blocked_until` conditions (e.g. `signed_allowlist`, `sprint_5_policy_engine`) must clear first.

## 6. Why this neutralizes the Sprint 2 risk

The audit found capabilities reachable via dispatch, agent-owned tools, cron, gateway, ACP, provider,
memory, skill, plugin, and MCP paths. Under default-deny, **every one of those paths resolves to DENY
unless an explicit, path-covered policy says otherwise** — so an ungoverned path is safe by default, not
dangerous. Combined with disablement tiers (remove/disable the worst paths entirely), this is defense in depth.

## 7. Boundaries

Design only. No engine implemented. Enforcement is Sprint 5; this report defines the rules that engine must obey.
