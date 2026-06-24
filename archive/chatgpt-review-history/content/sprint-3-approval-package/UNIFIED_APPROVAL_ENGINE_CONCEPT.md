# UNIFIED_APPROVAL_ENGINE_CONCEPT.md
# Magna Enso — Unified Approval Engine Concept
# Type: Local-only approval package
# Date: 2026-06-17
# Status: CONCEPT for human approval. Design-only — NO implementation.

---

## 1. Purpose

Describe the **concept** of one auditable approval path that every sensitive capability routes through.
This is a design concept only; the engine is implemented later (Sprint 5+), surfaced in the UI at Sprint 13.

## 2. The problem it solves

If each surface (terminal, browser, memory, cloud, messaging…) implements its own approval logic, rules
drift, bugs multiply, and gaps appear. The Sprint 2 finding (no single chokepoint) is exactly this problem
in Hermes. A **unified** approval engine gives **one** rule set, **one** audit log, and **one** thing to
test for bypass-resistance.

## 3. Scope — one path covers all of these

The unified approval engine must cover, at minimum:

- terminal
- code execution
- browser actions
- file transfer
- memory writes
- skill writes
- scheduler execution
- cloud / provider calls
- messaging
- delegation

## 4. Conceptual flow

```text
capability request (any surface)
        │
        ▼
  Polaris gate ── classify (capability, paths, context) → capability state
        │
        ├─ active_safe / read_only / report_only → proceed within state limits (no approval)
        ├─ draft_only                            → stage change; require human acceptance to persist
        └─ approval_required / (disabled→deny)   → Unified Approval Engine
                                                      │
                                                      ▼
                                          create approval request (what / why / scope / risk)
                                                      │
                                                      ▼
                                          human owner decides  (approve once / deny / revoke)
                                                      │
                                                      ▼
                                          log decision (Event Horizon) + execute once if approved
```

## 5. Properties (design requirements)

- **Single entry:** no sensitive action executes without passing through this path (bypass = design defect).
- **Per-action, scoped approvals:** approval is for a specific action and scope, not a blanket "always allow."
- **Fully logged:** every request and decision is recorded (auditable, reproducible).
- **Human-only approver:** the human owner approves; no worker self-approves (EH-0010).
- **Revocable & time-bounded:** approvals can be revoked; standing approvals are discouraged in MVP.
- **Fail-closed:** if the engine is unavailable or uncertain, it denies.
- **Reversibility-aware:** irreversible actions get the strongest scrutiny; memory/skill go via draft staging.

## 6. What it is NOT (in Sprint 3)

Not code. No UI. No queue implementation. No wiring into any runtime. Sprint 3 defines the **concept,
interface shape, and requirements**; implementation is later and separately approved.

## 7. Relationship to other models

- Consumes capability **states** (`CAPABILITY_STATES_PROPOSAL.md`) and the **default-deny** decision.
- Is invoked from the **chokepoint map** (`POLICY_CHOKEPOINT_MAP_PLAN.md`) — every sensitive path routes here.
- Its audit log feeds TRACE evidence (Light Curves) and, later, the Capability Control UI (Observatory).
