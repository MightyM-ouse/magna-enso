# DELEGATION_RECURSION_CONTROL_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 13 of 17 — Delegation & Recursion Control Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define governance for delegation/subagent spawning (C-14): **disabled in MVP**. Delegation multiplies
autonomy and tool-use scope and can recurse — a single approval could cascade into many ungoverned actions.

## 2. The threat

The Sprint 2 audit flagged delegation as "approval-required or disabled": `tools/delegate_tool.py`,
`run_agent.py::_dispatch_delegate_task`, and the agent-owned `delegate_task` in
`model_tools.py::_AGENT_LOOP_TOOLS`, also exposed via `acp_adapter/tools.py`. A spawned subagent inherits
tool access and can itself spawn — **recursion** — so capability and blast radius can grow without a
proportional number of human approvals.

## 3. Model (MVP)

```text
delegation / subagent spawn = DISABLED (T3 — not registered) in MVP
        │
   (post-MVP, if ever enabled)
        ▼
   approval_required per spawn
   + hard recursion depth limit (e.g. depth = 0/1)
   + child inherits NO capability the parent lacks (no privilege escalation)
   + child capabilities still default-deny + gated individually
   + every spawn + child action logged
```

## 4. Rules

1. MVP: delegation **disabled** (unregister `delegate_task`; route agent-owned/ACP paths to deny — P-04/P-07).
2. **No recursion in MVP** — subagents cannot spawn subagents.
3. If ever enabled post-MVP: `approval_required` per spawn, a **hard depth limit**, and **no privilege
   escalation** (a child can never hold a capability state less restrictive than the parent or than policy).
4. A delegated task does **not** carry a blanket approval — each child action is gated independently.
5. All spawns and child actions are logged with parent/child lineage.

## 5. Why disabled in MVP

Delegation is an autonomy multiplier. In an MVP focused on proving governance, the safe choice is to disable
it entirely — one fewer uncontrolled path — and revisit only after the single-action governance model is
proven and a recursion-control design exists.

## 6. Boundaries

Design only. Unregistration is a Sprint 4 fork action; any future delegation support is a separate sprint
with its own recursion-control implementation and approval.
