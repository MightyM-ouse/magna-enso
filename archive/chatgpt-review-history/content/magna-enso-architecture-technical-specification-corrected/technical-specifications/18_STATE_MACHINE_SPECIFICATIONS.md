---
document: technical-specifications/18_STATE_MACHINE_SPECIFICATIONS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Explicit state machines incl. audit-before-effect ordering; PROPOSED where not evidence-backed
date: 2026-06-21
evidence_sources: [05 of evidence-completion; package 07,08,10; spec 19]
change_control: ALLOW alone never triggers an effect. Governed; nothing deleted. Resolves Corrections 8 & 10.
---

# Spec 18 — State Machine Specifications (Corrections 8 & 10)

> Seven required state machines. Outcomes use the taxonomy in `19`. The **audit-before-effect** order
> (Correction 10) is enforced: an `ALLOW` decision **alone never triggers an effect** — a durable audit record
> must be written and confirmed first. State/transition names not backed by current evidence are **PROPOSED**.

## Human ToC
1. Audit-before-effect order 2. Capability decision 3. Approval lifecycle 4. Workflow lifecycle
5. Task lifecycle 6. Runtime evidence verification 7. Memory draft/persist/discard 8. Release promotion/rollback
9. Open decisions 10. Change-control

## 1. Audit-before-effect order (Correction 10) — `MAG-GOV-001`, `MAG-SEC-202`, `MAG-OBS-001`
Canonical order (no effect before AUDIT_CONFIRMED):

```mermaid
stateDiagram-v2
  [*] --> INTERPRETED: 1 interpret request (MAG-INT-001)
  INTERPRETED --> CAP_RESOLVED: 2 resolve capability (MAG-TOL-001)
  CAP_RESOLVED --> POLICY_EVALUATED: 3 evaluate policy (MAG-GOV-002)
  POLICY_EVALUATED --> DENY_POLICY: deny
  POLICY_EVALUATED --> APPROVAL: 4 approval required (MAG-GOV-003)
  APPROVAL --> DENY_POLICY: absent/deny/timeout (consequential)
  APPROVAL --> AUTHORIZED_PENDING_AUDIT: approve_once
  POLICY_EVALUATED --> AUTHORIZED_PENDING_AUDIT: allow (no approval needed)
  AUTHORIZED_PENDING_AUDIT --> AUDIT_CONFIRMED: 5-6 durable authz/audit record written + flushed (MAG-SEC-202)
  AUTHORIZED_PENDING_AUDIT --> UNAVAILABLE: audit sink down => deny-effect
  AUDIT_CONFIRMED --> EXECUTION_STARTED: 7 execute via governed adapter (MAG-TOL-001)
  EXECUTION_STARTED --> EXECUTION_COMPLETED: 8 record result
  EXECUTION_STARTED --> EXECUTION_FAILED: EXECUTION_ERROR
  EXECUTION_COMPLETED --> VALIDATED: 9 validate result
  EXECUTION_COMPLETED --> RECOVERY_REQUIRED: VALIDATION_FAILED
  VALIDATED --> EVIDENCE_EMITTED: 10 emit runtime evidence (MAG-OBS-001)
  EXECUTION_FAILED --> RECOVERY_REQUIRED
  EVIDENCE_EMITTED --> [*]
```

**Invariant:** transitions `AUTHORIZED_PENDING_AUDIT → EXECUTION_STARTED` are impossible without
`AUDIT_CONFIRMED`. An ALLOW with an unconfirmed audit write ⇒ `UNAVAILABLE` ⇒ no effect.

## 2. Capability decision state machine — `MAG-GOV-001`
`RECEIVED → VALIDATED | INVALID_REQUEST | NEEDS_CLARIFICATION → EVALUATED → {ALLOW, DENY_POLICY,
HOLD_FOR_APPROVAL}`. Read-only forbidden ⇒ `DENY_POLICY`; dependency down ⇒ `UNAVAILABLE` (see `19`).

## 3. Approval lifecycle — `MAG-GOV-003` (PROPOSED states)
`REQUESTED → PENDING(HOLD) → {APPROVED_ONCE, DENIED, EXPIRED, REVOKED}`; `APPROVED_ONCE → CONSUMED` (single-use,
fingerprint-checked in a serialized critical section); any mismatch/replay ⇒ `DENIED`. Expiry monotonic; restart
⇒ pending not carried (resets to default-deny). Absent production provider ⇒ `DENIED`.

## 4. Workflow lifecycle — `MAG-ORC-002`
`PENDING → AUTHORIZED → RUNNING → {COMPLETED, FAILED, DENIED, CANCELLED}`; each consequential step passes the
gate; `RUNNING` only after `AUDIT_CONFIRMED` for that step; failure ⇒ `RECOVERY_REQUIRED`.

## 5. Task lifecycle (TRACE Constellation) — `MAG-TRC-201` (engineering plane)
`SCOPED → IN_PROGRESS → EVIDENCE_DRAFT(Light Curve) → IN_REVIEW → {ACCEPTED, CHANGES_REQUESTED}`; acceptance is
human-only; mode history appended across worker handoffs (per TRACE adoption plan).

## 6. Runtime evidence verification — `MAG-TRC-202` (anti-self-certification)
`UNVERIFIED → SUBMITTED(read-only, digested) → INDEPENDENTLY_VERIFIED | VERIFICATION_FAILED`. **Magna cannot
self-set `INDEPENDENTLY_VERIFIED`** — a separate verifier identity recomputes from durable events. Default
`UNVERIFIED`.

## 7. Memory draft/persist/discard — `MAG-MEM-002`
`DRAFT → {PERSIST_REQUESTED → HOLD_FOR_APPROVAL → PERSISTED, DISCARDED}`. Persistence is an approval; no silent
mutation; discard is clean and reversible. (Sprint 8 governance.)

## 8. Release promotion/rollback — component `MAG-ENV-001`; requirements `MAG-OPS-002` (backup), `MAG-OPS-003` (rollback), `MAG-OPS-004` (release)
`BUILD → RC(UAT) → {ACCEPTED→PROMOTED(Local Production), REJECTED}`; rollback `PROMOTED → ROLLED_BACK(restore
snapshot + replay)`. **Tags are not releases**; promotion requires signed human acceptance; evidence retained
even on rollback.

## 9. Open decisions
- OD-18.1 — Final state names/fields are PROPOSED until ADR-R1 (engine composition) resolves.
- OD-18.2 — Whether workflow/step audit is per-step or per-workflow (default: per consequential step).

## 10. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. ALLOW alone ≠ effect. PROPOSED states marked. Governed; nothing deleted.
