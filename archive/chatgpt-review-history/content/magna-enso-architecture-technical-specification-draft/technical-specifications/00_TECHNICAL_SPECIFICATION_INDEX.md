---
document: technical-specifications/00_TECHNICAL_SPECIFICATION_INDEX
package: magna-enso-architecture-technical-specification-draft
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Index and standard for the Magna Enso technical specifications
current_vs_target: Specs are TARGET for the clean Enso unless they cite verified-current sources
date: 2026-06-21
evidence_sources: [package documents 00-18, magna-program-evidence-completion/*]
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# Technical Specification Index (Magna Enso)

> These specifications describe the **target** Magna Enso (the current forward project). They are
> `DRAFT_FOR_HUMAN_REVIEW`, not authorization to build. **No API path or schema is asserted unless marked
> `PROPOSED`** (proposed) **or cited to a verified-current source.** No sprint numbers are assigned.

## Human table of contents
1. Spec standard (sections every spec contains)
2. Spec register (01–17 → covered topics)
3. The 30 required spec topics → where each lives
4. Requirement ID families
5. Open decisions
6. Change-control note

## AI navigation index
- `spec_standard` → §1
- `spec_register` → §2
- `topic_map` → §3
- `requirement_families` → §4 (`registries/MAGNA_REQUIREMENT_REGISTRY.yaml`)

## 1. Spec standard (each spec section defines)
Purpose · Scope · Non-goals · Architecture IDs · Responsibilities · Inputs/Outputs · Interfaces & contracts ·
API/event definitions (PROPOSED where new) · Data structures · State transitions · Permission requirements ·
Human-approval requirements · Failure behaviour · Recovery behaviour · Security & privacy · Logging &
observability · TRACE evidence requirements · Acceptance criteria · Testing requirements · Current source/reuse
candidate · Current status · Open decisions · Evidence references.

## 2. Spec register

| Spec | Title | Primary arch IDs |
|---|---|---|
| 01 | System requirements & NFRs | MAG-PRG, MAG-NFR-* |
| 02 | Frontend & UX | MAG-EXP, MAG-UX-* |
| 03 | Backend & API | MAG-INT, MAG-ORC |
| 04 | Command, cognition & routing | MAG-INT, MAG-COG |
| 05 | Event, workflow & orchestration | MAG-ORC |
| 06 | Policy, permission & approval | MAG-GOV, MAG-SEC |
| 07 | Identity, HELIX & Cosmos | MAG-IDN, MAG-HLX, MAG-COS |
| 08 | Data, memory & persistence | MAG-MEM |
| 09 | Traceability & evidence contracts | MAG-TRC, MAG-OBS |
| 10 | Agent, model & tool adapters | MAG-AGT, MAG-TOL |
| 11 | Security, privacy & secrets | MAG-SEC |
| 12 | Configuration & environments | MAG-ENV |
| 13 | Observability, replay & recovery | MAG-OBS |
| 14 | Testing & quality strategy | MAG-TRC, MAG-GOV |
| 15 | Release, backup & rollback | MAG-ENV, MAG-OPS-* |
| 16 | Implementation & reuse index | MAG-* (reuse) |
| 17 | Requirement traceability matrix | MAG-FR/NFR/SEC/UX/TRC/OPS-* |

## 3. The 30 required spec topics → where each lives
FR(01) · NFR(01) · Frontend/UX(02) · Backend/API(03) · Command interpretation(04) · Cognition/routing(04) ·
Event bus(05) · Workflow engine(05) · Orchestration runtime(05) · Policy engine(06) · Authz/approval(06) ·
Identity/capability truth(07) · HELIX read-only(07) · Cosmos ratification(07) · Memory/context(08) ·
Persistence/schemas(08) · Runtime traceability(09) · TRACE engineering evidence(09) · Agents/providers(10) ·
Tool/capability adapters(10) · Hermes boundary(10) · Security/privacy/secrets(11) · Config/environments(12) ·
Observability/replay/recovery(13) · Testing/quality(14) · Release/backup/rollback(15) · Accessibility/
responsiveness(02) · Reuse/migration(16) · Error/failure handling(13 + per-spec failure sections) ·
Performance/resource(01 NFR + 13).

## 4. Requirement ID families
`MAG-FR-*`, `MAG-NFR-*`, `MAG-SEC-*`, `MAG-UX-*`, `MAG-TRC-*`, `MAG-OPS-*`. Registered in
`registries/MAGNA_REQUIREMENT_REGISTRY.yaml`; traced in `17_REQUIREMENT_TRACEABILITY_MATRIX.md`.

## 5. Open decisions
- OD-TS.1 — Whether spec detail depth is sufficient to seed a backlog after the foundation gate (`13`).
- OD-TS.2 — ADR-R1 (engine) must resolve before specs 05/06/08 are finalized.

## 6. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Specs are target unless citing verified-current. PROPOSED marks all new APIs/schemas.
