---
document: technical-specifications/04_COMMAND_COGNITION_AND_ROUTING
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Command interpretation, bounded cognition, routing (CSF→BRS pattern)
current_vs_target: Routing pattern verified-current (MCC); clean-Enso routing PLANNED
date: 2026-06-21
evidence_sources: [03,04 of evidence-completion; package 07]
change_control: Governed; nothing deleted.
---

# Spec 04 — Command, Cognition, and Routing

## Human ToC
1. Purpose/Scope/Non-goals 2. Command interpretation (MAG-FR-001) 3. Bounded cognition & routing (MAG-FR-002)
4. Reflex vs cognition 5. Failure/recovery 6. Permission/approval 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `interpret` → §2 (MAG-INT) · `routing` → §3 (MAG-COG) · `reflex` → §4 (MAG-GOV)

## 1. Purpose/Scope/Non-goals
**Purpose:** turn a command into a routed, governable intent. **Non-goals:** broad autonomous intelligence
(SGN-01 BLOCKED); model ownership of governance/architecture.

## 2. Command interpretation (MAG-FR-001)
Input: raw command. Output: structured intent (action, parameters, target). **Payload cannot escalate
privilege** — input-driven escalation ⇒ DENY. Data structure (PROPOSED): `{intent_id, action, params{},
targets[], origin}`.

## 3. Bounded cognition & routing (MAG-FR-002)
Verified-current pattern (`03`,`04`): `CSF → BRS` deterministic routing in `routes_local_model.py` +
`intent_router.py`. Target Enso reuses the **pattern** (refactored). Cognition **routes and proposes**; it does
not mint authority, change policy, or bypass the gate.

## 4. Reflex vs cognition (MAG-GOV)
Deterministic reflex/guardrails (default-deny, schema/permission checks) act **before** and **independent of**
cognition; cognition can **never** override reflex. (DIAG-08.)

## 5. Failure / recovery
Unparseable/ambiguous command ⇒ safe clarification or DENY (never guess into a privileged action). Router
error ⇒ DENY. Recovery: stateless per request; resting default-deny.

## 6. Permission / approval
Routing is not authorization. Every routed action still passes the gate; consequential actions require approval
(`06`).

## 7. Acceptance / testing
Acceptance: no routed action reaches a capability without the gate; privilege-escalation payloads denied.
Testing: routing unit tests + escalation deny-tests.

## 8. Status / Open decisions
Status: pattern `IMPLEMENTED_VALIDATED` (MCC); clean-Enso `PLANNED`. Open: OD-07.1 reuse vs reimplement router;
OD-07.2 reflex placement (gate-only vs defense-in-depth).

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks new structures. Governed; nothing deleted.
