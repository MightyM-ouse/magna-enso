# UNIFIED_APPROVAL_ENGINE_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 5 of 17 — Unified Approval Engine Model (concept)
# Type: Design-only governance report. NO implementation.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Design the **concept** of one auditable approval path that every sensitive (`approval_required`) action and
every `draft_only` persistence routes through. Hermes today has *scattered* approval primitives
(`tools/approval.py`, `tools/write_approval.py`, ACP edit approval, gateway run-approval) — the design
unifies them into a single boundary. Concept only; built in Sprint 5+, surfaced in UI at Sprint 13.

## 2. Surfaces the single path must cover

terminal · code execution · browser actions · file transfer · memory writes · skill writes ·
scheduler execution · cloud/provider calls · messaging/outbound delivery · delegation.

(Plus any future `approval_required` capability — the engine is the *only* way such actions execute.)

## 3. Approval record fields

| Field | Meaning |
|---|---|
| `approval_id` | Unique id for this request |
| `requester` | Worker/role/agent that requested the action |
| `capability_id` | The capability invoked (`CAPABILITY_POLICY_SCHEMA.md`) |
| `proposed_action` | Exact action and parameters (human-readable) |
| `risk_level` | low / medium / high / critical |
| `affected_resources` | Files, hosts, accounts, data touched |
| `expected_side_effects` | What will change if approved |
| `rollback_possibility` | reversible / partially / irreversible |
| `expiration` | When the request/approval lapses (time-bounded) |
| `human_decision` | approve_once / deny / revoke |
| `audit_log_reference` | Pointer into the Event Horizon / evidence log |

## 4. Conceptual flow

```text
capability call → Polaris gate classifies state
     │
     ├─ active_safe / read_only / report_only → proceed within state (no approval)
     ├─ draft_only        → stage change → approval engine (to persist)
     └─ approval_required → approval engine
                               │
                               ▼
                   build approval record (fields above)
                               │
                               ▼
                   present to HUMAN OWNER  ── approve_once / deny / revoke
                               │
              approve_once ────┼──── deny ──► DENY + log
                               ▼
                   execute exactly once, within scope → log audit_log_reference
```

## 5. Design requirements (binding)

- **Single entry:** no sensitive action executes except through this engine. A second approval path is a
  design defect. (Directly answers the Sprint 2 "no single chokepoint" finding for the *approval* dimension.)
- **Per-action, scoped:** approval authorizes one action with a stated scope — not a standing "always allow".
- **Human-only approver:** the human owner approves; no worker self-approves (EH-0010). Antigravity/Claude
  may *recommend*, never approve.
- **Fully logged & reproducible:** every request + decision recorded; auditable after the fact.
- **Time-bounded & revocable:** approvals expire; standing approvals are discouraged in MVP; revocation supported.
- **Fail-closed:** engine unavailable/uncertain → deny.
- **Reversibility-aware:** irreversible actions get the strongest presentation; memory/skill go via draft staging.

## 6. Relationship to Hermes primitives

The fork should **route** Hermes' existing approval points into this engine rather than trusting them
individually: `tools/approval.py::check_all_command_guards` (terminal),
`tools/approval.py::check_execute_code_guard` (code), `tools/write_approval.py::stage_write` (memory/skill),
ACP edit approval (file mutation), and gateway `_handle_run_approval`. None of these may remain an
independent, bypassable approval path.

## 7. Boundaries

Concept and interface shape only. No queue, no UI, no code, nothing wired into a runtime. Implementation is
Sprint 5+, separately approved.
