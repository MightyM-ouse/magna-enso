---
document: learning/TECHNICAL_SPECIFICATION_REVIEW_CHECKLIST_FOR_VINAY
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: A checklist Vinay can use to review the technical specifications (01-17)
current_vs_target: Review aid
date: 2026-06-21
evidence_sources: [technical-specifications 00-17, registries]
change_control: Governed; nothing deleted.
---

# Technical Specification Review Checklist for Vinay

> One pass per spec. Anything unchecked is a reason to send it back. **No spec may approve anything on your
> behalf.**

## Per-spec completeness (each spec 01-17)
- [ ] Has Purpose / Scope / **Non-goals**.
- [ ] Names its Architecture IDs and Requirement IDs.
- [ ] States inputs/outputs, interfaces/contracts, data structures, state transitions.
- [ ] States permission + **human-approval** requirements.
- [ ] States **failure** and **recovery** behaviour (fail-closed).
- [ ] States security/privacy + logging/observability + TRACE evidence requirements.
- [ ] States acceptance criteria + testing requirements.
- [ ] States current source/reuse candidate, current status, open decisions, evidence references.

## Honesty checks
- [ ] Every new API path or schema is marked **PROPOSED** (specs 03, 06, 08, 09).
- [ ] No spec claims runtime protection from harness tests (`14` honesty rule).
- [ ] Audit is described as integrity-detecting, **not** tamper-proof (`11`).
- [ ] **No canonical policy engine is chosen** — the experiment + gate are defined (`06`).
- [ ] Hermes boundary spec shows 0/6 active (`10`).

## Traceability
- [ ] Each requirement traces objective→arch ID→spec→source→test→evidence→acceptance (`17`).
- [ ] **No sprint numbers** assigned.
- [ ] Every requirement is evidenced or PROPOSED (`registries/MAGNA_REQUIREMENT_REGISTRY.yaml`).

## Decisions to make
- [ ] ADR-R1 (engine) — you understand it must be decided **after** the experiment.
- [ ] ADR-R4 (BRS-01), ADR-R5 (MEM/NRV), ADR-R8 (Enso pytest + independent review).
- [ ] ADR-R9/R10/R12 (environments, UX baseline, consent policy).

## Sign-off
- [ ] I (Vinay) accept / send back these specifications. (Your decision — this checklist does not decide.)

## Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Governed; nothing deleted.
