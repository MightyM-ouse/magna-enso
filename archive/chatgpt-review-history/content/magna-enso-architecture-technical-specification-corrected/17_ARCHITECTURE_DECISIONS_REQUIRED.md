---
document: 17_ARCHITECTURE_DECISIONS_REQUIRED
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT — surfaces decisions; resolves none; grants no approval
scope: Consolidated decisions for Vinay + the four foundation/integration approval gates (Correction 13)
date: 2026-06-21
evidence_sources: [12,13 of evidence-completion; CORRECTION_REPORT.md; HELIX_VERSIONING_OPTIONS.md]
change_control: Vinay decides. Options only. Governed; nothing deleted.
---

# 17 — Architecture Decisions Required (corrected)

> Every item is **DECISION_REQUIRED**; this resolves none and grants no approval. Machine register:
> `registries/MAGNA_OPEN_DECISIONS.yaml`. The "new Enso repo creation gate" is **removed** and replaced by the
> four approval gates in §2 (Correction 13).

## Human table of contents
1. Decision register (ADR-R1…R12 + HELIX)
2. Foundation & integration approval gates (replaces repo-creation gate)
3. Change-control note

## AI navigation index
- `register` → §1 · `gates` → §2

## 1. Decision register

| ID | Decision | Options | Default if undecided | Evidence |
|---|---|---|---|---|
| ADR-R1 | Runtime/policy engine | compose MCC + Enso / select one / replace | **Run experiment first; no selection** | `05`,`08`,`15` |
| ADR-R2 | Repo-strategy + KENOSHA supersession | new Event Horizon ID; mark one-repo + "Kensho" SUPERSEDED | keep historical, mark superseded; do not delete | `04`, `12`#1 |
| ADR-R3 | TRACE dual-plane contract + verifier + blueprint pin | adopt schema + external verifier / defer | unverified default; no self-cert | `07 ec`, `09`, `TRACE_SOURCE_RESOLUTION` |
| ADR-R4 | BRS-01 acceptance | accept+freeze / keep AWAITING | **AWAITING_HUMAN_ACCEPTANCE** | `04 ec` |
| ADR-R5 | MEM-01 / NRV-01 scope + Pre-SGN↔evolution relation | define / defer | pending; relation DECISION_REQUIRED | `04 ec`, `PRESGN…MATRIX` |
| ADR-R6 | SGN-01 | stays blocked | **BLOCKED (unchanged, canonical scope)** | `04 ec` |
| ADR-R7 | CSF Ollama capability-truth drift | governed correction | record; correct via governance | `02 ec` |
| ADR-R8 | Enso pytest fix + independent Sprint 5 review | correct + review / leave | correct + review required | `05 ec` |
| ADR-R9 | Environment + release topology | define UAT/prod/DR / stay local | local/test only; rest PLANNED | `08 ec`, `13` |
| ADR-R10 | UX acceptance baseline | set a11y/responsive/perf targets | none accepted yet | `08 ec`, `12` |
| ADR-R11 | Sprint 5 isolated-branch disposition | keep / quarantine pending review | keep isolated, unaccepted | `01`, `05` |
| ADR-R12 | Cloud/data consent + dependency governance | formalize / defer | local-first, consent-gated default | `13`,`14` |
| ADR-HLX | HELIX preservation across separate repos | own repo / generated profile / contract package | **no repo decision; options only** | `HELIX_VERSIONING_OPTIONS.md` |

## 2. Foundation & integration approval gates (Correction 13 — replaces repo-creation gate)
This corrected package may become the **approved basis for backlog creation**, but it must **not** create/
number sprints, start implementation, accept Sprint 5 or BRS-01, start SGN-01, select a policy engine, or
activate Hermes. The relevant, **separate** human decisions are:

1. **Existing Enso foundation-baseline approval** — accept the current `magna-enso` state (`4d5c203`, harness
   IN_REVIEW) as the foundation baseline.
2. **Architecture-package integration approval** — integrate this package into `magna-enso` after review.
3. **Backlog-preparation approval** — turn requirements into a backlog (still no sprint numbers).
4. **Sprint-planning approval** — only then plan/number sprints.

Passing one gate does **not** imply the next. Recommended independent reviewer: a senior security/QA architect
with no authorship in Command Center, Enso Sprint 5, or this package.

## 3. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. No decision resolved; no engine chosen; SGN-01 BLOCKED. Governed; nothing deleted.
