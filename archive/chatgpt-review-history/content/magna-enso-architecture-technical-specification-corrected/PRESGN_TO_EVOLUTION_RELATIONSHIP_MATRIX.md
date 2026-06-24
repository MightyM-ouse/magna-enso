---
document: PRESGN_TO_EVOLUTION_RELATIONSHIP_MATRIX
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Formal relationship between the Pre-SGN Stabilization Belt and the Enso→Beyond evolution stages
date: 2026-06-21
evidence_sources:
  - 04_PRESGN_STATUS_VERIFICATION.md; 02_CANONICAL_MAGNA_DIRECT_READ.md (evidence baseline)
  - planning/MAGNA_EVOLUTION_ROADMAP.md; MAGNA_ENSO_PROJECT_CHARTER.md
change_control: Governed; nothing deleted. Resolves Correction 4.
---

# Pre-SGN ↔ Evolution Relationship Matrix (Correction 4)

> **The Pre-SGN Stabilization Belt and the Enso→Beyond evolution are DIFFERENT frameworks** unless evidence
> explicitly maps them. The Belt is a **Command Center** readiness construct (HAB/ATM/CSF/BRS/MEM/NRV→SGN);
> the evolution stages are the **Magna product line** (Enso→Beyond, separate repos). No evidence in the
> accepted baseline maps Belt layers onto evolution-stage repositories. This matrix records that honestly and
> does **not** invent a mapping.

## Human table of contents
1. The two frameworks (kept distinct)
2. Allowed relationship values
3. Relationship matrix
4. SGN-01 scope statement
5. Open decisions
6. Change-control note

## 1. The two frameworks
- **Pre-SGN Stabilization Belt** — layers inside **Magna Command Center** that gate the eventual SGN-01 broad
  command-intelligence layer (evidence `04`). It is a *readiness belt*, not a release line.
- **Evolution stages** — the **Magna product line** Enso→Satori→Kenosha→Bodhi→Prabhava→Beyond, each a
  separate repository (human decision 4). It is a *capability/awareness maturity* line (roadmap).
- No accepted-evidence document states that a Belt layer *is* an evolution stage, or that SGN-01 governs the
  later stage repositories. Therefore most relationships are `CONCEPTUAL_ALIGNMENT`, `INDEPENDENT_FRAMEWORK`,
  or `DECISION_REQUIRED`.

## 2. Allowed relationship values
`DIRECT_PREREQUISITE` · `INHERITED_CAPABILITY` · `CONCEPTUAL_ALIGNMENT` · `INDEPENDENT_FRAMEWORK` · `UNKNOWN`
· `DECISION_REQUIRED`. (No other values used.)

## 3. Relationship matrix

| Pre-SGN Layer | Current Repository | Purpose (evidence `04`) | Evolution Stage Relation |
|---|---|---|---|
| HAB-01 (habitable surfaces / UI shell freeze) | magna-command-center | Ten-tab shell + route guardrails | `CONCEPTUAL_ALIGNMENT` — aligns with Enso "Govern/UX shell", but is a Command Center layer, not an Enso-stage deliverable |
| ATM-01 (permission/risk/authorization/approval) | magna-command-center | Permission metadata, approval controls | `CONCEPTUAL_ALIGNMENT` — same governance spirit as Enso default-deny; not the same artifact |
| CSF-01 (conscious self-model truth registry) | magna-command-center | Identity/capability-truth | `CONCEPTUAL_ALIGNMENT` — relates to Enso Identity; distinct framework |
| BRS-01 (routing layer) | magna-command-center | Bounded routing | `INDEPENDENT_FRAMEWORK` — a Command Center routing layer; reuse-candidate for Enso, not a stage gate. Stays AWAITING_HUMAN_ACCEPTANCE |
| MEM-01 (memory formation) | magna-command-center | Governed memory (pending) | `DECISION_REQUIRED` — may inform Enso/Kenosha memory governance; mapping not documented |
| NRV-01 (nervous-system visibility) | magna-command-center | Runtime observability | `DECISION_REQUIRED` — may inform Enso/Satori observability; mapping not documented |
| SGN-01 (broad command intelligence) | magna-command-center | Broad command intelligence | `INDEPENDENT_FRAMEWORK` + **BLOCKED** — within its **canonical Command Center scope**; **not** evidenced as governing later evolution repos |

## 4. SGN-01 scope statement
SGN-01 remains **BLOCKED within its canonical Command Center scope** (`04`). This package does **not** claim
that SGN-01 governs `magna-satori`, `magna-kenosha`, or any later evolution repository — no accepted evidence
establishes that. Whether the Belt is later adopted as a cross-stage gate is `DECISION_REQUIRED` (ADR-R5/ADR
new).

## 5. Open decisions
- OD-PE.1 — Whether the Pre-SGN Belt is adopted as a readiness gate for any evolution stage (DECISION_REQUIRED).
- OD-PE.2 — MEM-01 / NRV-01 relationship to Enso/Kenosha memory & observability (DECISION_REQUIRED; ADR-R5).
- OD-PE.3 — Whether SGN-01 has any role beyond Command Center scope (DECISION_REQUIRED; default: no).

## 6. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Frameworks kept distinct; no invented mapping. SGN-01 BLOCKED. Governed; nothing deleted.
