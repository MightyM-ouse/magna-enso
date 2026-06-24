---
document: technical-specifications/17_REQUIREMENT_TRACEABILITY_MATRIX
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Full traceability for ALL 52 requirements (Correction 7); machine form in registries/MAGNA_TRACEABILITY_REGISTRY.yaml
current_vs_target: Spans current and target; no sprint numbers
date: 2026-06-21
evidence_sources: [package 01-18; technical-specifications 01-19; registries]
change_control: All 52 requirements present. No sprint numbers. Governed; nothing deleted.
---

# Spec 17 — Requirement Traceability Matrix (full, 52/52)

> Chain: **Objective → Requirement → Component ID → Spec → Interface → Backlog candidate → Sprint (UNASSIGNED)
> → Source/reuse → Test → TRACE evidence → Acceptance status → Open decision.** Machine-readable mirror:
> `registries/MAGNA_TRACEABILITY_REGISTRY.yaml`. **No requirement omitted; no sprint numbers assigned.**

## Objectives
OBJ-1 govern every capability · OBJ-2 human final authority · OBJ-3 durable verifiable evidence ·
OBJ-4 local-first/private/reversible/provider-neutral · OBJ-5 governed UX.

## Matrix (Obj · Req · Component · Spec · Interface · Backlog · Sprint · Source · Test · Evidence · Acceptance · OpenDec)

| Obj | Req | Component | Spec | IF | Backlog | Sprint | Source | Test | Evidence | Accept | OpenDec |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MAG-FR-001 | MAG-INT-002 | 04 | IF-GATE | command-interpreter | UNASSIGNED | reimplement | escalation deny | LC | NOT_SUBMITTED | — |
| 1 | MAG-FR-002 | MAG-COG-001 | 04 | IF-GATE | routing | UNASSIGNED | MCC intent_router | routing unit | LC | NOT_SUBMITTED | ADR-R1 |
| 1 | MAG-FR-003 | MAG-GOV-001 | 06 | IF-GATE | ENSO-F-0501 | UNASSIGNED | Enso gate | gate deny | LC(Full) | IN_REVIEW | ADR-R1 |
| 2 | MAG-FR-004 | MAG-GOV-003 | 06 | IF-APPROVAL | ENSO-F-0502 | UNASSIGNED | Enso approval | HOLD/absent-deny | LC(Full) | IN_REVIEW | — |
| 3 | MAG-FR-005 | MAG-SEC-201 | 06 | IF-FINGERPRINT | ENSO-F-0501 | UNASSIGNED | Enso canonical | fingerprint mutation | LC(Full) | IN_REVIEW | — |
| 3 | MAG-FR-006 | MAG-ORC-001 | 05 | IF-EVENT | ENSO-F-0601 | UNASSIGNED | MCC event_bus | lineage/replay | LC | NOT_SUBMITTED | ADR-R1 |
| 1 | MAG-FR-007 | MAG-ORC-002 | 05 | IF-GATE | workflow | UNASSIGNED | MCC workflow | gated-step | LC | NOT_SUBMITTED | — |
| 1 | MAG-FR-008 | MAG-ORC-003 | 05 | IF-EVENT | orchestration | UNASSIGNED | MCC orchestration | restart/replay | LC | NOT_SUBMITTED | — |
| 4 | MAG-FR-009 | MAG-AGT-001 | 10 | IF-PROVIDER | providers | UNASSIGNED | MCC ollama | adapter gating | LC | NOT_SUBMITTED | ADR-R1 |
| 1 | MAG-FR-010 | MAG-TOL-001 | 10 | IF-TOOL | tool-adapters | UNASSIGNED | decision | behind-gate | LC | NOT_SUBMITTED | ADR-R1 |
| 2 | MAG-FR-011 | MAG-IDN-001 | 07 | IF-HELIX | identity | UNASSIGNED | CSF registry | truth reconcile | LC | NOT_SUBMITTED | ADR-R7 |
| 2 | MAG-FR-012 | MAG-HLX-001 | 07 | IF-HELIX | helix-readonly | UNASSIGNED | decision | read-only assert | LC | NOT_SUBMITTED | OD-HLX.1 |
| 2 | MAG-FR-013 | MAG-COS-001 | 07 | IF-COSMOS | cosmos-ratify | UNASSIGNED | decision | ratify-required | LC | NOT_SUBMITTED | — |
| 3 | MAG-FR-014 | MAG-MEM-002 | 08 | IF-AUDIT | ENSO-F-0801 | UNASSIGNED | reimplement | no-silent-write | LC(Full) | NOT_SUBMITTED | ADR-R5 |
| 3 | MAG-FR-015 | MAG-OBS-001 | 13 | IF-EVENT | replay-recovery | UNASSIGNED | compose | replay/restart | LC | IN_REVIEW | ADR-R1 |
| 5 | MAG-FR-016 | MAG-EXP-001 | 02 | IF-GATE | shell | UNASSIGNED | MCC App.tsx | shell/route | LC | NOT_SUBMITTED | — |
| 4 | MAG-FR-017 | MAG-MEM-002 | 08 | IF-AUDIT | draft-discard | UNASSIGNED | reimplement | draft-discard | LC | NOT_SUBMITTED | — |
| 4 | MAG-NFR-001 | MAG-PRG-001 | 01 | IF-STAGE | local-first | UNASSIGNED | design | isolation | LC | NOT_SUBMITTED | — |
| 1 | MAG-NFR-002 | MAG-GOV-001 | 19 | IF-POLICY | fail-closed | UNASSIGNED | Enso | fail-closed branches | LC(Full) | IN_REVIEW | — |
| 3 | MAG-NFR-003 | MAG-OBS-001 | 13 | IF-EVENT | replay-safe | UNASSIGNED | compose | deterministic recovery | LC | IN_REVIEW | ADR-R1 |
| 4 | MAG-NFR-004 | MAG-AGT-001 | 10 | IF-PROVIDER | replaceability | UNASSIGNED | MCC | adapter swap | LC | NOT_SUBMITTED | — |
| 4 | MAG-NFR-005 | MAG-OBS-001 | 01 | IF-EVENT | perf-budget | UNASSIGNED | PROPOSED | latency budget | LC | NOT_SUBMITTED | OD-01b |
| 4 | MAG-NFR-006 | MAG-ENV-001 | 12 | IF-STAGE | resource | UNASSIGNED | PROPOSED | resource bounds | LC | NOT_SUBMITTED | OD-01b |
| 1 | MAG-NFR-007 | MAG-PRG-001 | 01 | IF-STAGE | modularity | UNASSIGNED | design | module-boundary | LC | NOT_SUBMITTED | — |
| 4 | MAG-NFR-008 | MAG-SEC-203 | 11 | IF-TRACE-XPLANE | min-context | UNASSIGNED | design | context-min | LC | NOT_SUBMITTED | — |
| 1 | MAG-SEC-001 | MAG-GOV-001 | 06 | IF-POLICY | ENSO-F-0501 | UNASSIGNED | Enso | default-deny | LC(Full) | IN_REVIEW | — |
| 3 | MAG-SEC-002 | MAG-SEC-202 | 11 | IF-AUDIT | ENSO-F-0501 | UNASSIGNED | Enso audit | audit-file security | LC(Full) | IN_REVIEW | — |
| 3 | MAG-SEC-003 | MAG-SEC-202 | 11 | IF-AUDIT | ENSO-F-0501 | UNASSIGNED | Enso audit | hash-chain detect | LC(Full) | IN_REVIEW | OD-14.1 |
| 4 | MAG-SEC-004 | MAG-SEC-203 | 11 | IF-TRACE-XPLANE | redaction | UNASSIGNED | reimplement | redaction | LC | NOT_SUBMITTED | — |
| 4 | MAG-SEC-005 | MAG-AGT-002 | 11 | IF-PROVIDER | consent | UNASSIGNED | MCC cloud_review | consent-gate | LC | NOT_SUBMITTED | ADR-R12 |
| 2 | MAG-SEC-006 | MAG-GOV-003 | 06 | IF-APPROVAL | ENSO-F-0502 | UNASSIGNED | Enso | no-self-approve | LC(Full) | IN_REVIEW | — |
| 3 | MAG-SEC-007 | MAG-SEC-201 | 06 | IF-FINGERPRINT | ENSO-F-0501 | UNASSIGNED | Enso | clock-rollback deny | LC(Full) | IN_REVIEW | — |
| 1 | MAG-SEC-008 | MAG-GOV-001 | 06 | IF-GATE | chokepoint | UNASSIGNED | n/a real entry | P-01..P-13 matrix | LC(Full) | NOT_SUBMITTED | R-06 OPEN |
| 5 | MAG-UX-001 | MAG-EXP-001 | 02 | IF-GATE | shell | UNASSIGNED | MCC | shell tests | LC | NOT_SUBMITTED | — |
| 5 | MAG-UX-002 | MAG-EXP-002 | 02 | IF-APPROVAL | approval-ux | UNASSIGNED | MCC | approval e2e | LC | NOT_SUBMITTED | — |
| 5 | MAG-UX-003 | MAG-EXP-002 | 02 | IF-GATE | states | UNASSIGNED | MCC | state coverage | LC | NOT_SUBMITTED | — |
| 5 | MAG-UX-004 | MAG-EXP-001 | 02 | IF-GATE | a11y | UNASSIGNED | PROPOSED | a11y audit | LC | NOT_SUBMITTED | ADR-R10 |
| 5 | MAG-UX-005 | MAG-EXP-001 | 02 | IF-GATE | responsive | UNASSIGNED | PROPOSED | breakpoint | LC | NOT_SUBMITTED | ADR-R10 |
| 4 | MAG-UX-006 | MAG-EXP-002 | 02 | IF-PROVIDER | offline | UNASSIGNED | MCC | degraded-mode | LC | NOT_SUBMITTED | — |
| 5 | MAG-UX-007 | MAG-EXP-001 | 02 | IF-GATE | perf-budget-ux | UNASSIGNED | PROPOSED | bundle budget | LC | NOT_SUBMITTED | ADR-R10 |
| 3 | MAG-TRC-001 | MAG-TRC-201 | 09 | IF-TRACE-XPLANE | eng-evidence | UNASSIGNED | TRACE template | artifact presence | LC | NOT_SUBMITTED | ADR-R3 |
| 3 | MAG-TRC-002 | MAG-TRC-202 | 09 | IF-TRACE-XPLANE | runtime-facts | UNASSIGNED | reimplement | digest emit | LC | NOT_SUBMITTED | ADR-R3 |
| 3 | MAG-TRC-003 | MAG-TRC-202 | 09 | IF-TRACE-XPLANE | xplane-schema | UNASSIGNED | PROPOSED | schema validate | LC | NOT_SUBMITTED | ADR-R3 |
| 2 | MAG-TRC-004 | MAG-TRC-202 | 09 | IF-TRACE-XPLANE | verifier | UNASSIGNED | reimplement | self-cert prevent | LC | NOT_SUBMITTED | ADR-R3 |
| 3 | MAG-TRC-005 | MAG-TRC-201 | 09 | IF-TRACE-XPLANE | reproducibility | UNASSIGNED | TRACE | raw-output digest | LC | NOT_SUBMITTED | OD-09.2 |
| 4 | MAG-TRC-006 | MAG-TRC-202 | 09 | IF-TRACE-XPLANE | privacy-class | UNASSIGNED | reimplement | privacy-class | LC | NOT_SUBMITTED | — |
| 4 | MAG-OPS-001 | MAG-ENV-001 | 12 | IF-STAGE | environments | UNASSIGNED | reimplement | env isolation | LC | NOT_SUBMITTED | ADR-R9 |
| 3 | MAG-OPS-002 | MAG-ENV-001 | 15 | IF-STAGE | backup | UNASSIGNED | design | backup/restore | LC | NOT_SUBMITTED | ADR-R9 |
| 4 | MAG-OPS-003 | MAG-ENV-001 | 15 | IF-STAGE | rollback | UNASSIGNED | design | rollback rehearsal | LC | NOT_SUBMITTED | ADR-R9 |
| 3 | MAG-OPS-004 | MAG-ENV-001 | 15 | IF-STAGE | release | UNASSIGNED | design | no-tag-as-release | LC | NOT_SUBMITTED | ADR-R9 |
| 3 | MAG-OPS-005 | MAG-OBS-001 | 13 | IF-EVENT | observability | UNASSIGNED | MCC | replay/recovery | LC | NOT_SUBMITTED | — |
| 4 | MAG-OPS-006 | MAG-SEC-203 | 12 | IF-PROVIDER | consent-policy | UNASSIGNED | design | dependency/consent | LC | NOT_SUBMITTED | ADR-R12 |

**Coverage:** 52 requirements, 52 rows, 0 omitted. LC = Light Curve (TRACE evidence; engineering-plane).

## Open decisions
- OD-17.1 — Backlog→sprint assignment deferred to the sprint-planning approval gate (`13` §4).
- OD-17.2 — ADR-R1 changes source bindings for governance/policy rows.

## Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. 52/52 traced. No sprint numbers. No acceptance granted. Governed; nothing deleted.
