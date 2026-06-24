---
document: technical-specifications/09_TRACEABILITY_AND_EVIDENCE_CONTRACTS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Runtime traceability, TRACE engineering evidence, cross-plane contract, anti-self-certification
current_vs_target: Engineering plane partly current; runtime plane + cross-plane contract TARGET
date: 2026-06-21
evidence_sources: [06,07 of evidence-completion; package 09]
change_control: Planes stay separate. Governed; nothing deleted.
---

# Spec 09 — Traceability and Evidence Contracts

## Human ToC
1. Purpose/Scope/Non-goals 2. Engineering-plane evidence (MAG-TRC) 3. Runtime-plane facts 4. Cross-plane schema
5. Anti-self-certification 6. Privacy 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `engineering` → §2 · `runtime` → §3 · `schema` → §4 · `no_self_cert` → §5

## 1. Purpose/Scope/Non-goals
**Purpose:** dual-plane traceability with independent verification. **Non-goals:** Magna certifying its own
output; ingesting secrets to improve traceability.

## 2. Engineering-plane evidence (MAG-TRC-001/005)
Task packets, Light Curves, decisions, validation; raw command output + digests for reproducibility (target
standard; current evidence is partial — `06`). Reproducibility standard is ADR (OD-09.2).

## 3. Runtime-plane facts (MAG-TRC-002)
Runtime emits `event_id`, IDs, actor, source, timestamp + **digests**; may propose evidence links; **cannot**
update acceptance/supersede/close-risk/certify (`07`).

## 4. Cross-plane minimum schema (MAG-TRC-003, PROPOSED — `07`)
`trace_id, plane, event_id, task_id, correlation_id, causation_id, actor, source, occurred_at, artifact_uri,
content_digest, policy_version, privacy_class, replay_safe, verification_status, verified_by, verified_at`.
`verification_status` defaults `unverified`; **Magna cannot self-set `verified`.**

## 5. Anti-self-certification (MAG-TRC-004)
A **separate read-only verifier identity** recomputes from durable events. One plane cannot mint authority in
the other. Stable cross-plane IDs.

## 6. Privacy (MAG-TRC-006, MAG-SEC-004)
No secrets/raw `.env`/unrestricted prompts/personal content ingested; provider metadata as digest +
local/cloud class + consent reference. Privacy class carried per record.

## 7. Acceptance / testing
Acceptance: planes separate; verifier external; runtime cannot self-verify; no secret ingestion. Testing:
schema validation; self-certification-prevention test; privacy redaction test.

## 8. Status / Open decisions
Status: engineering plane `IMPLEMENTED_VALIDATED (template)` / effectiveness `IN_PROGRESS`; runtime + cross-
plane `PLANNED`. Open: OD-09.1 contract/verifier; OD-09.2 reproducibility standard; OD-09.3 TRACE UI build.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Schema PROPOSED. Planes separate. Governed; nothing deleted.
