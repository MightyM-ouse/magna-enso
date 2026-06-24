---
document: technical-specifications/16_IMPLEMENTATION_AND_REUSE_INDEX
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Source-module → reuse classification index across Command Center, Enso, TRACE, Hermes
current_vs_target: Classifies current sources for target reuse; selects nothing canonical
date: 2026-06-21
evidence_sources: [05,11 of evidence-completion]
change_control: No canonical engine selected. Governed; nothing deleted.
---

# Spec 16 — Implementation and Reuse Index

## Human ToC
1. Purpose/Scope/Non-goals 2. Reuse index (with fields) 3. Migration risk 4. Decision gate 5. Status/Open 6. Change-control

## AI navigation index
- `reuse_index` → §2 · machine form → `registries/MAGNA_COMPONENT_REGISTRY.yaml`

## 1. Purpose/Scope/Non-goals
**Purpose:** map known source modules to reuse classes with evidence. **Non-goals:** choosing the canonical
policy engine; wholesale copying.

## 2. Reuse index (summary; full register in component registry)

| Source module (symbol) | Origin | Class | Test status | Coupling | Provenance/License | Contract boundary |
|---|---|---|---|---|---|---|
| `risk_policy_engine.evaluate_policy` | MCC | DECISION_REQUIRED | 701-suite | high (FastAPI/SQLModel) | internal | governance port |
| `core.approval_engine.ApprovalEngine` | MCC | EXTRACT/DECISION_REQUIRED | 701-suite | high | internal | approval port |
| `core.event_bus.InProcessEventBus.replay` | MCC | EXTRACT_SHARED_COMPONENT | 701-suite | med | internal | event/replay port |
| `services.authorization_service.resolve_auth_context` | MCC | DECISION_REQUIRED | 701-suite | high | internal | authz port |
| `core.audit_logger.store_envelope` | MCC | DECISION_REQUIRED (vs Enso audit) | 701-suite | med | internal | audit port |
| ten-tab shell `App.tsx` + clients | MCC | REUSE_AFTER_REFACTOR | build PASS | med | internal | UI↔API contract |
| `schema.load_policy_records` | Enso | EXTRACT_SHARED_COMPONENT | 49 unittest (pytest broken) | low | internal | policy schema port |
| `canonical.build_fingerprint` | Enso | EXTRACT_SHARED_COMPONENT | 49 unittest | low | internal | fingerprint port |
| `approval.ApprovalCoordinator.consume` | Enso | EXTRACT_SHARED_COMPONENT | 49 unittest | low | internal | approval port |
| `audit.SecureAuditSink` | Enso | EXTRACT_SHARED_COMPONENT | 49 unittest | low | internal | audit sink port |
| `gate.CapabilityGate.authorize` | Enso | EXTRACT_SHARED_COMPONENT | 49 unittest | low | internal | gate port |
| TRACE artifacts/Observatory | TRACE | REUSE_UNCHANGED (sovereign) | 6 tests; UI build blocked | low | internal | TRACE contract |
| Hermes provenance metadata | Hermes | HISTORICAL_EVIDENCE_ONLY | n/a | n/a | external/license-audited | none (0/6 active) |

## 3. Migration risk
High-coupling MCC services carry medium migration risk (FastAPI/SQLModel entanglement); Enso components are
low-coupling stdlib (low risk) but harness-only; TRACE is sovereign (low). Adapters + contract tests preferred.

## 4. Decision gate
Governance-core reuse is `DECISION_REQUIRED` pending ADR-R1 experiment. **No canonical engine selected here.**

## 5. Status / Open decisions
Open: ADR-R1; ADR-R8 (Enso pytest); OD-15.x migration sequencing.

## 6. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. No engine chosen. Governed; nothing deleted.
