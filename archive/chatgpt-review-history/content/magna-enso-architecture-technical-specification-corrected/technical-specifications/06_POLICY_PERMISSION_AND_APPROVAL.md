---
document: technical-specifications/06_POLICY_PERMISSION_AND_APPROVAL
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Policy engine, permission/authorization, approval; the comparative experiment & decision gate
current_vs_target: Enso controls verified at harness; runtime chokepoint completeness TARGET; NO engine chosen
date: 2026-06-21
evidence_sources: [05 of evidence-completion; package 08]
change_control: NO canonical policy engine selected. Governed; nothing deleted.
---

# Spec 06 — Policy, Permission, and Approval

## Human ToC
1. Purpose/Scope/Non-goals 2. Default-deny policy engine 3. Authorization 4. Approval & fingerprint
5. The comparative experiment (no selection) 6. Failure/recovery 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `policy_engine` → §2 (MAG-GOV-001) · `approval` → §4 (MAG-SEC-202) · `experiment` → §5 (ADR-R1)

## 1. Purpose/Scope/Non-goals
**Purpose:** govern every capability through one default-deny, fail-closed decision point. **Non-goals:**
choosing the canonical engine here; authenticated production approval UI (later sprint).

## 2. Default-deny policy engine (MAG-FR-003, MAG-SEC-001/008)
Decision: `(request, policy, ctx) → allow | deny | hold`. Missing policy/path/schema/provider/audit or any
error ⇒ DENY. Policy records are **JSON** (Enso harness: stdlib, strict schema, narrow value domain, NFC
normalization) (`05`). **Single-chokepoint completeness for real entry points is TARGET** — R-06 OPEN.

## 3. Authorization (MAG-GOV-001)
Risk classification + authorization context (verified in MCC) precede the policy decision. Identity-as-approver
is rejected for workers. Authorization identity model is part of ADR-R1.

## 4. Approval & canonical fingerprint (MAG-FR-004/005, MAG-SEC-006/007)
- `approval_required` ⇒ HOLD; only an authenticated human owner turns HOLD→ALLOW (production invariant). Enso
  ships **test-only** provider; **production absent ⇒ DENY**; Null/Deny is the default.
- **Canonical invocation fingerprint:** SHA-256 over canonical JSON of {approval_id+nonce, capability_id,
  invocation_path, proposed_action, complete normalized parameters, affected_resources, caller_context_id,
  policy_version/hash, expiry}. Single-use; any mismatch/mutation/duplicate/expiry/replay ⇒ DENY. Consumption
  in a serialized critical section. Expiry uses **monotonic** time; clock rollback ⇒ DENY; pending approvals
  not carried across restart.

## 5. The comparative experiment (ADR-R1) — **no engine selected**
Define one read-only, one local-write, one external/approval-required capability contract; route each through
adapters for **both** engines (MCC integrated controls; Enso strict policy); test parameter substitution,
replay, restart, audit failure, **direct-entry bypass**, authorization identity; compare evidence + coupling;
**Vinay decides** compose/adapt/replace. Decision gate per `13`.

## 6. Failure / recovery
Fail-closed everywhere; audit-before-allow; restart ⇒ default-deny; provider absent ⇒ DENY.

## 7. Acceptance / testing
Acceptance: every testable bypass class denied at harness; absence/structural/review checks for the rest;
P-01…P-13 chokepoint matrix labels testable-now vs deferred; **no claim of runtime protection**. Testing per
`14`.

## 8. Status / Open decisions
Status: Enso controls `IN_PROGRESS/IN_REVIEW`; chokepoint completeness `PLANNED`; **R-06 OPEN**. Open: ADR-R1;
authenticated provider design; harden ATM advisory boundaries.

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. **No engine chosen.** Governed; nothing deleted.
