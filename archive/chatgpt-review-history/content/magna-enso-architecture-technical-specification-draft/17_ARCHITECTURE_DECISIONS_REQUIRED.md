---
document: 17_ARCHITECTURE_DECISIONS_REQUIRED
package: magna-enso-architecture-technical-specification-draft
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — surfaces decisions; resolves none; grants no approval
scope: Consolidated architecture decisions requiring Vinay, with options and recommended gate
current_vs_target: Decision register spanning current and target
date: 2026-06-21
evidence_sources: [12_REMAINING_CONTRADICTIONS_AND_QUESTIONS.md, 13_RECOMMENDED_FOUNDATION_GATE.md, 05_POLICY_ENGINE_COMPARATIVE_AUDIT.md]
change_control: Vinay decides. This document records options only; it does not select.
---

# 17 — Architecture Decisions Required

> Every item below is **DECISION_REQUIRED**. This document presents options and trade-offs; it **does not
> resolve any decision** and grants no approval. Machine register: `registries/MAGNA_OPEN_DECISIONS.yaml`.

## Human table of contents
1. Decision register (ADR-R1 … ADR-R12)
2. Recommended foundation gate (sequencing)
3. Cross-references
4. Change-control note

## AI navigation index
- `decision_register` → §1
- `foundation_gate` → §2 (`13` evidence)

## 1. Decision register

| ID | Decision | Options | Default if undecided | Evidence |
|---|---|---|---|---|
| ADR-R1 | Canonical runtime/policy engine | compose MCC primitives + Enso policy / select one / replace | **Run the experiment first; no selection** | `05`, `08`, `15` |
| ADR-R2 | Stage naming + repo-strategy supersession | new accepted EH IDs + mark legacy SUPERSEDED | keep historical, mark superseded; do not delete | `12`#1, `04` |
| ADR-R3 | TRACE dual-plane contract | adopt minimum schema + external verifier / defer | unverified default; no self-certification | `07`, `09` |
| ADR-R4 | BRS-01 acceptance/freeze | accept+freeze / keep AWAITING | **AWAITING_HUMAN_ACCEPTANCE** (do not accept here) | `04` |
| ADR-R5 | MEM-01 / NRV-01 acceptance scope | define + accept / defer | pending belt layers | `04`, `12`#4 |
| ADR-R6 | SGN-01 | stays blocked | **BLOCKED (unchanged)** | `04` |
| ADR-R7 | CSF Ollama capability-truth drift | governed correction | record drift; correct via governance | `02`, `12`#5 |
| ADR-R8 | Enso pytest correction + independent Sprint 5 review | correct + review / leave | correct + independent review required | `05`, `12`#6 |
| ADR-R9 | Environment + release topology | define integration/UAT/prod/DR / stay local | local/test only today; rest PLANNED | `08`, `13` |
| ADR-R10 | UX acceptance baseline | a11y/responsive/perf/visual-regression targets | none accepted yet | `08`, `12` |
| ADR-R11 | Sprint 5 branch disposition | keep isolated / quarantine pending review | keep isolated, unaccepted | `01` FND-01, `05` |
| ADR-R12 | Cloud/data consent + governance policy | formalize / defer | local-first, consent-gated default | `13`, `14` |

## 2. Recommended foundation gate (sequencing — evidence `13`)
Do **not** create the clean Magna project until all gates have explicit evidence + Vinay's recorded decision:
1. Authority → 2. Canonical truth → 3. Architecture (after ADR-R1 experiment) → 4. TRACE dual-plane →
5. UX → 6. Environment → 7. Backlog → 8. Validation → 9. Governance → 10. **Creation decision** (explicit;
passing earlier gates does **not** imply authorization). Recommended independent reviewer: a senior security/
QA architect with **no authorship** in Command Center, Enso Sprint 5, or this package.

## 3. Cross-references
Each OD-xx.y in documents `00`–`16` and the technical specs maps into the ADR-R register above and the machine
register `registries/MAGNA_OPEN_DECISIONS.yaml`.

## 4. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. No decision resolved here. Vinay decides; superseded options are marked, not deleted.
