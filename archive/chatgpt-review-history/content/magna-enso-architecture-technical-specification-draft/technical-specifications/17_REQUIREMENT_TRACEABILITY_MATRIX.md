---
document: technical-specifications/17_REQUIREMENT_TRACEABILITY_MATRIX
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Traceability: objective → requirement → arch ID → spec → backlog candidate → source → test → TRACE evidence → acceptance
current_vs_target: Spans current and target; no sprint numbers assigned
date: 2026-06-21
evidence_sources: [package 01-18; technical-specifications 01-16; evidence-completion]
change_control: No sprint numbers assigned. Governed; nothing deleted.
---

# Spec 17 — Requirement Traceability Matrix

> Chain: **Product objective → Requirement → Architecture ID → Technical spec → Backlog candidate → Future
> sprint → Source module → Test → TRACE evidence → Human acceptance.** **No sprint numbers are assigned**
> (column shown as `UNASSIGNED`). Backlog candidates reference Enso feature IDs where one already exists.

## Human ToC
1. Objectives 2. Traceability matrix 3. Coverage notes 4. Open decisions 5. Change-control

## AI navigation index
- `objectives` → §1 · `matrix` → §2 · registry → `registries/MAGNA_REQUIREMENT_REGISTRY.yaml`

## 1. Product objectives
- OBJ-1 Govern every capability (default-deny, no bypass).
- OBJ-2 Keep human as final authority (approval, no self-approve, no self-certification).
- OBJ-3 Durable, replay-safe, independently verifiable evidence.
- OBJ-4 Local-first, private, reversible, provider-neutral.
- OBJ-5 Usable governed UX (frozen ten-tab shell).

## 2. Traceability matrix (representative; full set in registry)

| Objective | Req ID | Arch ID | Spec | Backlog candidate | Sprint | Source module | Test | TRACE evidence | Acceptance |
|---|---|---|---|---|---|---|---|---|---|
| OBJ-1 | MAG-FR-003 | MAG-GOV | 06 | ENSO-F-0501 (existing) | UNASSIGNED | `gate.CapabilityGate` (Enso) | gate deny-tests | Light Curve (target) | PENDING (R-06 OPEN) |
| OBJ-1 | MAG-SEC-001 | MAG-GOV | 06,11 | ENSO-F-0501 | UNASSIGNED | `evaluator.PolicyEvaluator` | default-deny tests | LC | PENDING |
| OBJ-1 | MAG-SEC-008 | MAG-SEC | 06,11 | DECISION (chokepoint) | UNASSIGNED | n/a (real entry points) | P-01..P-13 matrix | LC | OPEN (R-06) |
| OBJ-2 | MAG-FR-004 | MAG-GOV | 06 | ENSO-F-0502 (existing) | UNASSIGNED | `approval.ApprovalCoordinator` | approval HOLD/absent-deny | LC | PENDING |
| OBJ-2 | MAG-SEC-006 | MAG-SEC | 06 | ENSO-F-0502 | UNASSIGNED | HumanDecisionProvider contract | no-self-approve tests | LC | PENDING |
| OBJ-2 | MAG-TRC-004 | MAG-TRC | 09,14 | TRACE contract | UNASSIGNED | external verifier (target) | self-cert-prevention | LC | PENDING |
| OBJ-3 | MAG-FR-005 | MAG-SEC | 06 | ENSO-F-0501 | UNASSIGNED | `canonical.build_fingerprint` | fingerprint mutation deny | LC | PENDING |
| OBJ-3 | MAG-SEC-002 | MAG-SEC | 11 | ENSO-F-0501 | UNASSIGNED | `audit.SecureAuditSink` | audit-file security | LC | PENDING |
| OBJ-3 | MAG-FR-015 | MAG-OBS | 13 | ENSO-F-0601 (candidate) | UNASSIGNED | event_bus replay (MCC) | replay/restart | LC | PENDING |
| OBJ-3 | MAG-TRC-003 | MAG-TRC | 09 | TRACE contract | UNASSIGNED | cross-plane schema (PROPOSED) | schema validation | LC | PENDING |
| OBJ-4 | MAG-NFR-001 | MAG-ENV | 12 | env model | UNASSIGNED | config/env | isolation checks | LC | PENDING |
| OBJ-4 | MAG-FR-009 | MAG-AGT | 10 | provider adapters | UNASSIGNED | ollama/cloud adapters (MCC) | adapter gating | LC | PENDING |
| OBJ-4 | MAG-SEC-005 | MAG-SEC | 11,12 | consent | UNASSIGNED | cloud_review_service (MCC) | consent test | LC | PENDING |
| OBJ-5 | MAG-UX-001 | MAG-EXP | 02 | shell | UNASSIGNED | `App.tsx` (MCC) | shell/route tests | LC | PARTIAL (MCC validated) |
| OBJ-5 | MAG-UX-004 | MAG-UX | 02 | a11y baseline | UNASSIGNED | n/a (target) | a11y audit (target) | LC | OPEN |

## 3. Coverage notes
- Every requirement has an evidence reference or is marked PROPOSED/target.
- No requirement is marked accepted; acceptance is Vinay's (PENDING/OPEN).
- Existing Enso feature IDs reused where present (ENSO-F-0501/0502/0601…); others are candidates.

## 4. Open decisions
- OD-17.1 — Backlog candidate → sprint assignment is deferred until after the foundation gate (`13`).
- OD-17.2 — ADR-R1 resolution changes source-module bindings for governance/policy rows.

## 5. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. **No sprint numbers assigned.** Governed; nothing deleted.
