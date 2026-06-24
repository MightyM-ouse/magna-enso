---
document: technical-specifications/00_TECHNICAL_SPECIFICATION_INDEX
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Index and standard for the Magna Enso technical specifications (now incl. specs 18 & 19)
current_vs_target: Specs are TARGET unless they cite verified-current sources
date: 2026-06-21
evidence_sources: [package documents; magna-program-evidence-completion/*]
change_control: Governed; nothing deleted. PROPOSED marks all new APIs/schemas.
---

# Technical Specification Index (corrected)

> Target Magna Enso specs (built **into** `magna-enso`). `DRAFT_FOR_HUMAN_REVIEW`, not authorization. **No API
> path/schema asserted unless marked PROPOSED.** No sprint numbers. New in corrected: **18 state machines**,
> **19 failure/outcome taxonomy**.

## Human ToC
1. Spec standard 2. Spec register (00–19) 3. 30 topics → location 4. Requirement families 5. Open decisions 6. Change-control

## AI navigation index
- `standard` → §1 · `register` → §2 · `topics` → §3 · `families` → §4 (`registries/MAGNA_REQUIREMENT_REGISTRY.yaml`)

## 1. Spec standard (each spec defines)
Purpose · Scope · Non-goals · Architecture IDs (full, MAG-XXX-0NN) · Responsibilities · Inputs/Outputs ·
Interfaces & contracts · API/event (PROPOSED where new) · Data structures · State transitions (see `18`) ·
Permission · Human-approval · Failure behaviour (outcome taxonomy `19`) · Recovery · Security/privacy ·
Logging/observability · TRACE evidence · Acceptance · Testing · Current source/reuse · Status · Open decisions ·
Evidence references.

## 2. Spec register

| Spec | Title | Primary component IDs |
|---|---|---|
| 01 | System requirements & NFRs | MAG-PRG-001; MAG-NFR-* |
| 02 | Frontend & UX | MAG-EXP-001/002; MAG-UX-* |
| 03 | Backend & API | MAG-INT-001/002; MAG-ORC-* |
| 04 | Command, cognition & routing | MAG-INT-002; MAG-COG-001 |
| 05 | Event, workflow & orchestration | MAG-ORC-001/002/003 |
| 06 | Policy, permission & approval | MAG-GOV-001/002/003; MAG-SEC-201 |
| 07 | Identity, HELIX & Cosmos | MAG-IDN-001; MAG-HLX-001; MAG-COS-001 |
| 08 | Data, memory & persistence | MAG-MEM-001/002 |
| 09 | Traceability & evidence contracts | MAG-TRC-201/202; MAG-OBS-001 |
| 10 | Agent, model & tool adapters | MAG-AGT-001/002; MAG-TOL-001/002 |
| 11 | Security, privacy & secrets | MAG-SEC-201/202/203 |
| 12 | Configuration & environments | MAG-ENV-001 |
| 13 | Observability, replay & recovery | MAG-OBS-001 |
| 14 | Testing & quality strategy | MAG-TRC-201; MAG-GOV-001 |
| 15 | Release, backup & rollback | MAG-ENV-001; MAG-OPS-* |
| 16 | Implementation & reuse index | MAG-* (reuse) |
| 17 | Requirement traceability matrix (52/52) | MAG-FR/NFR/SEC/UX/TRC/OPS-* |
| **18** | **State machine specifications (audit-before-effect)** | MAG-GOV-001; MAG-SEC-202; MAG-OBS-001 |
| **19** | **Failure & outcome taxonomy (10 outcomes)** | MAG-GOV-001/002 |

## 3. The 30 required spec topics → location
FR(01)·NFR(01)·Frontend/UX(02)·Backend/API(03)·Command(04)·Cognition/routing(04)·Event bus(05)·Workflow(05)·
Orchestration(05)·Policy(06)·Authz/approval(06)·Identity/capability truth(07)·HELIX read-only(07)·Cosmos(07)·
Memory/context(08)·Persistence/schemas(08)·Runtime traceability(09)·TRACE engineering evidence(09)·Agents/
providers(10)·Tool/capability adapters(10)·Hermes boundary(10 + HERMES_DERIVED_CAPABILITY_PLAN)·Security/
privacy/secrets(11)·Config/environments(12)·Observability/replay/recovery(13)·Testing/quality(14)·Release/
backup/rollback(15)·Accessibility/responsiveness(02)·Reuse/migration(16)·Error/failure handling(19 + per-spec)·
Performance/resource(01 NFR + 13). **State models(18).**

## 4. Requirement ID families
`MAG-FR-*`, `MAG-NFR-*`, `MAG-SEC-*`, `MAG-UX-*` (requirement-only), `MAG-TRC-*`, `MAG-OPS-*`. UX **components**
use `MAG-EXP-*`. Registered in `registries/MAGNA_REQUIREMENT_REGISTRY.yaml`; traced in `17` +
`registries/MAGNA_TRACEABILITY_REGISTRY.yaml`.

## 5. Open decisions
- OD-TS.1 — Spec depth sufficiency for backlog after the C13 gates.
- OD-TS.2 — ADR-R1 must resolve before specs 05/06/08 finalize.

## 6. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks all new APIs/schemas. Governed; nothing deleted.
