---
document: technical-specifications/05_EVENT_WORKFLOW_AND_ORCHESTRATION
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Event bus, workflow engine, orchestration runtime
current_vs_target: Verified-current in MCC; reuse-after-refactor for the target architecture within the existing magna-enso repository
date: 2026-06-21
evidence_sources: [03,05 of evidence-completion; package 07,10]
change_control: Governed; nothing deleted. ADR-R1 affects composition.
---

# Spec 05 — Event, Workflow, and Orchestration

## Human ToC
1. Purpose/Scope/Non-goals 2. Event bus 3. Workflow engine 4. Orchestration runtime 5. Failure/recovery
6. Permission/approval 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `event_bus` → §2 (MAG-ORC-001) · `workflow` → §3 · `orchestration` → §4 · `recovery` → §5 (MAG-OBS-001)

## 1. Purpose/Scope/Non-goals
**Purpose:** durable, replay-safe execution substrate. **Non-goals:** autonomous goal generation; distributed
multi-host orchestration (local single-host).

## 2. Event bus (MAG-FR-006)
Verified-current (`03`): durable events with causal/correlation fields, WS delivery, replay. Interface
(PROPOSED ports): `publish(event)`, `subscribe(type)`, `replay(from)`. Data: `event_id, correlation_id,
causation_id, actor, source, occurred_at, type, payload_digest`.

## 3. Workflow engine (MAG-FR-007)
Executes only permitted actions; every consequential step passes the gate. State transitions: `pending →
authorized → running → completed | failed | denied`. Failure ⇒ DENY/halt step; no partial privileged effect
without a durable audit record.

## 4. Orchestration runtime (MAG-FR-008)
Coordinates multi-step workflows with lineage; restart ⇒ rebuild from log; no persistent "enabled" state
surviving restart as an open door (`10`).

## 5. Failure / recovery
Bus/engine error ⇒ fail-closed; malformed audit tail truncated/quarantined on startup; resting default-deny;
replay is recovery source of truth.

## 6. Permission / approval
Gate precedes every consequential step; `approval_required` steps HOLD (`06`). No step self-authorizes.

## 7. Acceptance / testing
Acceptance: no consequential step executes un-gated; replay reconstructs state deterministically; restart
carries no pending approval. Testing: integration + restart/replay + race/TOCTOU (best-effort) tests.

## 8. Status / Open decisions
Status: `IMPLEMENTED_VALIDATED` (MCC), reuse-after-refactor target. Open: ADR-R1 composition of MCC
orchestration with Enso governance core (DECISION_REQUIRED).

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks new ports. Governed; nothing deleted.
