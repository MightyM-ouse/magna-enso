# UNIFIED_APPROVAL_ENGINE_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Unified Approval Engine Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that the Unified Approval Engine concept (UNIFIED_APPROVAL_ENGINE_MODEL.md)
covers all 10 required sensitive surface categories through one auditable path,
and that its design requirements are correct and complete.

---

## 2. Coverage of the 10 Required Surfaces

The 10 surfaces the engine must cover (per validation requirements):

| Required Surface | In Model §2? | Approval Record Field Coverage | Assessment |
|---|---|---|---|
| Terminal execution | YES (listed explicitly) | capability_id + affected_resources + side_effects + rollback | COVERED |
| Code execution | YES (listed explicitly) | Same fields | COVERED |
| Browser actions | YES (listed explicitly) | affected_resources (URLs, DOM elements) | COVERED |
| File transfer | YES (listed explicitly) | affected_resources (files, hosts) | COVERED |
| Memory writes | YES (listed explicitly — draft_only persistence path) | proposed_action + rollback_possibility | COVERED |
| Skill writes | YES (listed explicitly — draft_only persistence path) | proposed_action + rollback_possibility | COVERED |
| Scheduler execution | YES (listed explicitly — routes from report_only → approve → run) | proposed_action + expected_side_effects | COVERED |
| Cloud/provider calls | YES (listed explicitly) | affected_resources (external provider) + externality | COVERED |
| Messaging/outbound delivery | YES (listed explicitly) | affected_resources (recipients) + irreversible flag | COVERED |
| Delegation | YES (listed explicitly) | proposed_action (spawns subagent) + rollback_possibility=irreversible | COVERED |

Coverage: 10/10 required surfaces explicitly listed. PASS.

---

## 3. Design Requirements Assessment

§5 of UNIFIED_APPROVAL_ENGINE_MODEL.md specifies 7 binding design requirements:

| Requirement | Text | Antigravity Assessment |
|---|---|---|
| Single entry | "No sensitive action executes except through this engine. A second approval path is a design defect." | CORRECT AND CRITICAL — directly resolves Sprint 2 VA-08 (no unified approval engine). The "second path = design defect" framing is exactly right. |
| Per-action, scoped | "Approval authorizes one action with a stated scope — not a standing 'always allow'." | CORRECT — prevents blanket approvals from creating ungated windows of activity. |
| Human-only approver | "The human owner approves; no worker self-approves (EH-0010). Antigravity/Claude may recommend, never approve." | CORRECT — consistent with EH-0010 and Magna governance principles. |
| Fully logged + reproducible | "Every request + decision recorded; auditable after the fact." | CORRECT — audit_log_reference field in approval record. |
| Time-bounded + revocable | "Approvals expire; standing approvals are discouraged in MVP; revocation supported." | CORRECT — prevents stale approvals from remaining valid indefinitely. |
| Fail-closed | "Engine unavailable/uncertain → deny." | CORRECT — consistent with default-deny model. |
| Reversibility-aware | "Irreversible actions get the strongest presentation; memory/skill go via draft staging." | CORRECT — reversible field in policy schema drives presentation; draft-only is the correct memory/skill path. |

All 7 requirements: CORRECTLY STATED AND COMPLETE. PASS.

---

## 4. Approval Record Fields Assessment

The approval record has 9 fields:

| Field | Assessment |
|---|---|
| approval_id | CORRECT — stable unique id for audit trail |
| requester | CORRECT — which worker/role requested the action |
| capability_id | CORRECT — links to policy schema for full capability context |
| proposed_action | CORRECT — human-readable exact action and parameters |
| risk_level | CORRECT — drives human attention and urgency |
| affected_resources | CORRECT — files, hosts, accounts, data touched |
| expected_side_effects | CORRECT — what will change if approved |
| rollback_possibility | CORRECT — reversible / partially / irreversible |
| expiration | CORRECT — time-bounded; no standing approvals |
| human_decision | CORRECT — approve_once / deny / revoke (not approve_always) |
| audit_log_reference | CORRECT — pointer into Event Horizon / evidence log |

"approve_once" (not approve_always) is particularly important — it enforces the
per-action scoping requirement structurally, not just by policy.

---

## 5. Hermes Primitive Routing Assessment

§6 specifies that the fork should route existing Hermes approval primitives into the engine
rather than trusting them individually:

| Hermes Primitive | Routed Through Engine? | Notes |
|---|---|---|
| tools/approval.py::check_all_command_guards (terminal) | YES — must route into unified engine | Currently standalone; must not remain independent gate |
| tools/approval.py::check_execute_code_guard (code) | YES — must route into unified engine | Same; currently standalone |
| tools/write_approval.py::stage_write (memory/skill) | YES — must route into unified engine | Staging mechanism is reusable; approval decision must flow through engine |
| ACP edit approval (file mutation) | YES — must route into unified engine | ACP has its own approval path; must not remain independent |
| gateway::_handle_run_approval | YES — must route into unified engine | Gateway approval is listener-triggered; listener is off in MVP but this routing must be designed |

Assessment: The routing requirement is stated correctly. "None of these may remain an
independent, bypassable approval path" is the critical constraint for Sprint 4 fork
implementation. PASS.

---

## 6. Conceptual Flow Assessment

The conceptual flow (§4) correctly handles:
- active_safe / read_only / report_only → proceed within state (no approval needed)
- draft_only → stage change → approval engine (to persist)
- approval_required → approval engine → present to human → approve_once or deny → log

The flow correctly shows that draft_only still routes through the approval engine —
just at the persistence step rather than at the action step. This is the correct
distinction between draft-staging and immediate approval.

---

## 7. Unified Approval Engine Verdict

```
10/10 required surfaces covered:    PASS
7 binding design requirements:      All correct — PASS
Approval record fields:             Complete (11 fields) — PASS
Single-entry requirement:           CORRECTLY STATED — resolves Sprint 2 VA-08 — PASS
Human-only approver:                CONFIRMED — consistent with EH-0010 — PASS
Fail-closed:                        CORRECTLY SPECIFIED — PASS
Hermes primitive routing:           5 primitives correctly identified for routing — PASS
No implementation code:             CONFIRMED — concept only — PASS

UNIFIED APPROVAL ENGINE VALIDATION: PASS
Design is complete, correct, and addresses Sprint 2 VA-08 definitively.
```
