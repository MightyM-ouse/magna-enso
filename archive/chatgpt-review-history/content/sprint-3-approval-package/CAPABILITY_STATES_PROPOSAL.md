# CAPABILITY_STATES_PROPOSAL.md
# Magna Enso — Capability States Proposal
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PROPOSAL for human approval (Decision 3). Design-only.

---

## 1. Purpose

Propose the finite set of **capability states** every Magna Enso capability may hold. States replace coarse
on/off thinking and make "what is this capability allowed to do?" precise and auditable.

## 2. The six proposed states

| State | Meaning | External side effects? | Persists? | Human approval to act? |
|---|---|---|---|---|
| `disabled` | Capability is unavailable; should not start/register. | — | — | N/A (cannot run) |
| `read_only` | May observe/read; cannot mutate or trigger external side effects. | No | No | No (reads only) |
| `draft_only` | May propose/stage changes; cannot persist without human acceptance. | No | Only as a staged draft | Yes, to persist |
| `report_only` | May produce reports/metadata; cannot execute. | No | No | N/A (no execution) |
| `approval_required` | May execute only after explicit human approval. | Yes (gated) | Possibly | **Yes, per action** |
| `active_safe` | Safe to run without approval — no external or persistent side effects. | No | No | No |

## 3. How a state is chosen (decision rule)

```text
Does the capability have external side effects OR persist state OR take irreversible action?
  No  → active_safe (if it executes) or read_only (if it only reads)
  Yes → can the effect be staged for human acceptance?
          Yes → draft_only (for writes)  or  report_only (for "would-do" execution)
          No  → approval_required (gated per action)  OR  disabled/removed (if too risky for MVP)
```

Default before classification: **`disabled`** (default-deny). A capability is promoted to a less
restrictive state only by deliberate, logged decision.

## 4. State applied to Magna Enso surfaces (MVP, summary)

| Surface | Proposed state |
|---|---|
| Browser snapshot / read | `read_only` |
| Browser actions | `approval_required` (or `disabled`) |
| Memory writes | `draft_only` |
| Skill writes | `draft_only` |
| Scheduler | `report_only` |
| Terminal / code execution | `approval_required`, disabled by default |
| Messaging gateways | `disabled` (or removed) |
| Cloud / provider calls | `disabled` |
| Plugin / MCP loading | `disabled` unless signed allowlist |
| Curator / self-review | `report_only` |
| Background self-improvement | `disabled` / removed |
| Subagent delegation | `disabled` in MVP |

(Full surface mapping in `HERMES_SURFACE_GOVERNANCE_PLAN.md`.)

## 5. Properties every state must satisfy

- **Auditable:** the current state of every capability is inspectable and logged on change.
- **Default-deny:** unknown/unclassified capability ⇒ treated as `disabled`.
- **Reversible where it persists:** `draft_only` writes can be discarded; approvals are logged and revocable.
- **No silent promotion:** moving to a less restrictive state requires explicit human action (and a decision log entry).

## 6. Decision requested (Decision 3)

Approve this six-state set as the Magna Enso capability-state vocabulary, or amend. Recommendation:
**approve as proposed** — it cleanly expresses every posture the Sprint 2 findings require.
