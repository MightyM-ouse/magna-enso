---
document: technical-specifications/07_IDENTITY_HELIX_AND_COSMOS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Identity (current self-model), HELIX (read-only doctrine), Cosmos (ratified chronicle)
current_vs_target: CSF/Identity verified-current; HELIX/Cosmos as runtime surfaces PLANNED
date: 2026-06-21
evidence_sources: [02 of evidence-completion]
change_control: Governed; nothing deleted.
---

# Spec 07 — Identity, HELIX, and Cosmos

## Human ToC
1. Purpose/Scope/Non-goals 2. Identity (MAG-IDN) 3. HELIX read-only (MAG-HLX) 4. Cosmos ratification (MAG-COS)
5. Boundaries between them 6. Failure/permission 7. Acceptance/testing 8. Status/Open 9. Change-control

## AI navigation index
- `identity` → §2 · `helix` → §3 · `cosmos` → §4 · `boundaries` → §5 · DIAG-11 → `02` §6

## 1. Purpose/Scope/Non-goals
**Purpose:** truthful self-model + read-only doctrine + ratified history. **Non-goals:** HELIX mutating
runtime; Cosmos self-updating; Identity recording history.

## 2. Identity (MAG-IDN, MAG-FR-011)
Identity = Magna's **truthful current self-model and capability declaration** (CSF truth registry). It must not
overclaim. **Known drift:** CSF registry says governed Ollama UI execution unavailable while service/routes
implement it ⇒ governed correction required (ADR-R7) — recorded, not edited here.

## 3. HELIX read-only (MAG-HLX, MAG-FR-012)
HELIX = encoded genome/doctrine/architecture/constraints + read-only observability. **Informs and constrains;
never mutates runtime** (Constitution Law III). As an executable runtime surface beyond docs/observability it
is `PLANNED`/`UNKNOWN` — must not be described as a running subsystem.

## 4. Cosmos ratification (MAG-COS, MAG-FR-013)
Cosmos = ratified evolutionary chronicle; **append-only w.r.t. history**; agents propose, **Vinay ratifies**.
Flow (PROPOSED): `propose entry → human review → ratify → append`. No agent self-ratifies.

## 5. Boundaries
Identity (now) ≠ Cosmos (ratified evolution); neither is runtime authority; Cosmos is not self-updating
(`02`). DIAG-11 in `02` §6.

## 6. Failure / permission
Identity overclaim ⇒ correctness defect; resolve by governed correction, not silent edit. HELIX cannot be a
write path; any attempted HELIX write ⇒ rejected. Cosmos append requires human ratification.

## 7. Acceptance / testing
Acceptance: Identity claims match verified capability (no drift); HELIX exposes no runtime-mutation path;
Cosmos append requires ratification. Testing: capability-truth reconciliation check; HELIX read-only assertion.

## 8. Status / Open decisions
Status: Identity/CSF `ACCEPTED_AND_VALIDATED`; HELIX/Cosmos runtime surfaces `PLANNED`. Open: ADR-R7 (Ollama
drift); OD-06.3 (HELIX/Cosmos runtime boundary).

## 9. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks new flows. Governed; nothing deleted.
