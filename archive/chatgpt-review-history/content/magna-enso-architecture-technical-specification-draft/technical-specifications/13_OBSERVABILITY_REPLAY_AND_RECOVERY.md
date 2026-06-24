---
document: technical-specifications/13_OBSERVABILITY_REPLAY_AND_RECOVERY
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Observability, replay, recovery, and error/failure handling
current_vs_target: MCC observability/replay verified; clean-Enso composition target
date: 2026-06-21
evidence_sources: [03,05 of evidence-completion; package 10]
change_control: Governed; nothing deleted.
---

# Spec 13 — Observability, Replay, and Recovery

## Human ToC
1. Purpose/Scope/Non-goals 2. Observability (MAG-OBS) 3. Replay & recovery 4. Error/failure handling
5. Permission 6. Acceptance/testing 7. Status/Open 8. Change-control

## AI navigation index
- `observability` → §2 · `replay` → §3 · `errors` → §4

## 1. Purpose/Scope/Non-goals
**Purpose:** durable visibility + deterministic recovery. **Non-goals:** observability granting control
("visible without granting control"); remote monitoring.

## 2. Observability (MAG-OPS-005)
Verified-current (`03`): durable events, runtime observability, WS dispatch, replay projections. Every decision
(allow/deny/hold/approve/reject) logged.

## 3. Replay & recovery (MAG-FR-015, MAG-NFR-003)
Append-only audit log = recovery source of truth; decisions/approvals reconstructed; malformed tail truncated/
quarantined; resting default-deny; pending approvals not carried across restart; monotonic expiry resets on
restart; clock rollback ⇒ DENY (`10`).

## 4. Error / failure handling
Every failure mode resolves to DENY (fail-closed): no policy/store/schema/provider/audit, evaluator error,
approval timeout, lock failure, insecure audit file. Never "allow because empty/unavailable/timed-out/errored."

## 5. Permission
Observability surfaces are read-only; they grant no control and require no elevated capability to view (within
the local owner's trusted zone).

## 6. Acceptance / testing
Acceptance: every failure branch denies; replay reconstructs deterministically; restart carries no pending
approval. Testing: failure-injection + replay/restart tests (`14`).

## 7. Status / Open decisions
Status: observability/replay `IMPLEMENTED_VALIDATED` (MCC); composition `PLANNED`. Open: OD-10.1 persistence/
audit composition; OD-10.3 tamper-evident store.

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Governed; nothing deleted.
