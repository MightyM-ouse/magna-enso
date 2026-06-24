---
document: technical-specifications/01_SYSTEM_REQUIREMENTS_AND_NFRS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Functional + non-functional + performance/resource requirements for target Magna Enso
current_vs_target: TARGET (cites verified-current where applicable)
date: 2026-06-21
evidence_sources: [03,05,10 of evidence-completion; package 06,08]
change_control: Governed; PROPOSED marks anything not evidence-backed.
---

# Spec 01 — System Requirements and NFRs

## Human ToC
1. Purpose/Scope/Non-goals 2. Functional requirements (MAG-FR) 3. Non-functional (MAG-NFR)
4. Performance & resource 5. Acceptance & testing 6. Status/Open decisions 7. Change-control

## AI navigation index
- `functional` → §2 · `nfr` → §3 · `perf` → §4 · registry → `registries/MAGNA_REQUIREMENT_REGISTRY.yaml`

## 1. Purpose / Scope / Non-goals
**Purpose:** the requirement baseline for target Enso. **Scope:** single-user local-first runtime, governance,
evidence. **Non-goals:** SGN-01 (BLOCKED), multi-user, public deploy, active Hermes, autonomous memory.

## 2. Functional requirements (MAG-FR) — `Status: PLANNED unless noted`

| ID | Requirement | Arch ID | Source/reuse | Evidence |
|---|---|---|---|---|
| MAG-FR-001 | Interpret command → structured intent; no privilege from payload | MAG-INT-001 | REIMPLEMENT | `03` |
| MAG-FR-002 | Bounded cognitive routing (CSF→BRS pattern) | MAG-COG-001 | REUSE_AFTER_REFACTOR (MCC) | `03`,`04` |
| MAG-FR-003 | Single capability gate, default-deny | MAG-GOV-001 | EXTRACT (Enso) | `05` |
| MAG-FR-004 | approval_required ⇒ HOLD via HumanDecisionProvider; absent ⇒ DENY | MAG-GOV-001 | EXTRACT (Enso) | `05` |
| MAG-FR-005 | Canonical SHA-256 invocation fingerprint, single-use | MAG-SEC-202 | EXTRACT (Enso) | `05` |
| MAG-FR-006 | Durable event lineage (causal/correlation) | MAG-ORC-001 | REUSE (MCC) | `03`,`07` |
| MAG-FR-007 | Execute only permitted actions via workflow | MAG-ORC-001 | REUSE (MCC) | `03` |
| MAG-FR-008 | Orchestration runtime | MAG-ORC-001 | REUSE (MCC) | `03` |
| MAG-FR-009 | Provider-neutral model adapters | MAG-AGT-001 | REUSE_AFTER_REFACTOR | `03` |
| MAG-FR-010 | Tool/capability adapters behind the gate | MAG-TOL-001 | DECISION_REQUIRED | `05` |
| MAG-FR-011 | Identity truthful self-model surface | MAG-IDN-001 | REUSE (CSF) | `02 ec` |
| MAG-FR-012 | HELIX read-only doctrine integration | MAG-HLX-001 | PLANNED | `02 ec` |
| MAG-FR-013 | Cosmos ratification (propose→Vinay ratifies) | MAG-COS-001 | PLANNED | `02 ec` |
| MAG-FR-014 | Governed memory; draft persistence = approval | MAG-MEM-001 | PLANNED | `02 ec` |
| MAG-FR-015 | Replay/recover from append-only log | MAG-OBS-001 | compose | `05`,`03` |
| MAG-FR-016 | Frozen ten-tab shell surfaces | MAG-EXP-001 | REUSE_AFTER_REFACTOR | `03` |
| MAG-FR-017 | Reversibility / draft discard | MAG-MEM-001 | PLANNED | `05` |

## 3. Non-functional requirements (MAG-NFR)

| ID | Requirement | Arch ID |
|---|---|---|
| MAG-NFR-001 | Single-user, local-first | MAG-PRG-001/MAG-ENV-001 |
| MAG-NFR-002 | Fail-closed on any failure/ambiguity | MAG-GOV-001 |
| MAG-NFR-003 | Replay-safe deterministic recovery; resting state default-deny | MAG-OBS-001 |
| MAG-NFR-004 | Provider/worker replaceability | MAG-AGT-001 |
| MAG-NFR-005 | Performance budget (see §4) | MAG-OBS-001 |
| MAG-NFR-006 | Local resource constraints (see §4) | MAG-ENV-001 |
| MAG-NFR-007 | Modularity — no cognitive monolith | MAG-PRG-001 |
| MAG-NFR-008 | Minimal necessary context | MAG-SEC-202 |

## 4. Performance & resource (PROPOSED — no current budget evidence)
- PROPOSED: gate decision latency target (local) and shell interaction budget to be set during the experiment.
- Known signal: MCC frontend bundle warning **1.85 MB JS / ~500 KB gzip** (`08`) ⇒ MAG-UX-007 budget needed.
- Resource: runs within a single developer machine; no horizontal scaling assumed.

## 5. Acceptance & testing
Acceptance: each MAG-FR has an executable test or a labeled absence/structural/review check; NFRs have
measurable criteria where feasible (latency/bundle); fail-closed proven for every failure branch. Testing
strategy: `14_TESTING_AND_QUALITY_STRATEGY.md`.

## 6. Current status / Open decisions
Status: requirements `PLANNED` for the target architecture within the existing magna-enso repository; routing/orchestration/shell cite verified-current MCC.
Open: OD-01a ADR-R1 affects FR-003/004/005/010; OD-01b performance budgets unset (PROPOSED).

## 7. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks unevidenced budgets. Governed; nothing deleted.
