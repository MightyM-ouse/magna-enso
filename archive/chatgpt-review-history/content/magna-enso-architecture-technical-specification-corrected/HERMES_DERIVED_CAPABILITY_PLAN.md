---
document: HERMES_DERIVED_CAPABILITY_PLAN
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Hermes-derived Enso capability scope — adoption layers + capability table; activation remains 0/6
date: 2026-06-21
evidence_sources:
  - planning/MAGNA_ENSO_SPRINT_PLAN.md (Sprints 4-13); MAGNA_ENSO_PROJECT_CHARTER.md
  - 10_CORRECTED_STATUS_AND_PERCENTAGES.md; 11_REUSE_EVIDENCE_UPDATE.md (evidence baseline; 0/6 active)
  - _scratch/hermes-readonly-audit (read-only audit workspace, inspection only)
change_control: No Hermes capability is active. Governed; nothing deleted. Resolves Correction 11.
---

# Hermes-Derived Enso Capability Plan (Correction 11)

> **Current Hermes activation: 0 of 6 families.** Nothing below is active. "PLANNED for Enso" describes
> *intended governed scope from the approved sprint plan*, not activation. Activation requires policy,
> permission, evidence, reversibility, and human approval (human decision 8).

## Human table of contents
1. Four distinct adoption layers (do not conflate)
2. Capability table (from sprint plan + audit)
3. Activation gate (every capability)
4. Open decisions
5. Change-control note

## 1. Four distinct adoption layers
1. **Hermes source-code adoption** — taking Hermes code. Status: only a **clean governed fork baseline** is
   *planned* (Sprint 4), preserving provenance + SHA + MIT attribution; **no integration in current evidence**.
2. **Hermes feature/capability adoption** — adopting a *capability* (e.g. terminal) behind Magna governance.
   Status: PLANNED scope per sprint plan; **none active**.
3. **Magna-owned reimplementation inspired by Hermes** — rebuilding a capability cleanly under Magna policy.
   Status: PLANNED/DECISION_REQUIRED per capability.
4. **Capability activation** — turning a capability on at runtime. Status: **0/6; gated** (default-deny).

The 6-family activation denominator (evidence `10`): terminal, browser, messaging, agent, memory, tools.

## 2. Capability table (sprint plan + Hermes audit)

> Columns: business value · Enso target scope · source strategy · policy class · approval · privacy risk ·
> network risk · reversibility · TRACE evidence · activation gate · current status. All `current status =
> NOT ACTIVE`. Source strategy is PROPOSED pending Sprint 2/3 audit outcomes (ADR-R1-adjacent).

| Capability | Business value | Enso target scope (sprint) | Source strategy | Policy class | Approval | Privacy risk | Network risk | Reversibility | TRACE evidence | Activation gate | Current status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Terminal / code execution | Local automation | Local execution **capture** (S12); governed exec later | reimplement-or-governed-fork (PROPOSED) | approval_required | yes | high | low (local) | required | Light Curve (Full) | policy+evidence+human | NOT ACTIVE |
| Browser / web | Web tasks/search | default-mock web search reuse (MCC); governed browser later | reuse MCC mock + reimplement (PROPOSED) | approval_required | yes | high | high | required | Light Curve (Full) | policy+consent+human | NOT ACTIVE |
| Messaging / remote instruction | Remote ops | Remote **instruction package**, inert until approved (S11) | reimplement (PROPOSED) | approval_required | yes | high | high | required | Light Curve (Full) | policy+human; LAN-first | NOT ACTIVE |
| Agent / tool calling | Orchestration | Governed adapters behind the gate (S5+) | EXTRACT/DECISION_REQUIRED | approval_required | yes | med | med | required | Light Curve (Full) | policy+human | NOT ACTIVE |
| Memory / skill management | Continuity | Memory & skill **governance** (S8); no silent mutation | reimplement governed (PROPOSED) | approval_required | yes (draft=approval) | high | low | required (draft discard) | Light Curve (Full) | policy+human | NOT ACTIVE |
| General tools / plugins | Extensibility | Governed tool adapters (S5+) | DECISION_REQUIRED | approval_required | yes | med | med | required | Light Curve (Full) | policy+human | NOT ACTIVE |
| Scheduler (documented) | Timed proposals | **Report-only** scheduler (S9); proposes, never executes | reimplement governed (PROPOSED) | report_only | yes (to act) | low | low | n/a (no effect) | Light Curve (Standard) | policy+human to execute | NOT ACTIVE |
| Mobile / LAN access (documented) | Mobile control | **LAN-only** control, default-off (S10) | reimplement governed (PROPOSED) | approval_required | yes | med | high (LAN) | required | Light Curve (Full) | policy+human; no public listener | NOT ACTIVE |

(Scheduler and Mobile/LAN are explicitly documented in the sprint plan, so included with their documented
governed posture — report-only / LAN-only — not invented.)

## 3. Activation gate (applies to every capability)
A Hermes-derived (or any) capability may activate **only** when all hold: a policy record exists
(default-deny otherwise); permission/authorization resolves; durable evidence (Light Curve) is produced;
the action is reversible (or the irreversibility is explicitly accepted by the human); and the **human owner
approves**. Absent any one ⇒ remains inactive. (Human decision 8.)

## 4. Open decisions
- OD-HRM.1 — Per-capability source strategy (governed fork vs Magna reimplementation) — depends on Sprint 2/3
  audit/design outcomes; currently PROPOSED/DECISION_REQUIRED.
- OD-HRM.2 — Which families (if any) are in Enso v1.0 governed scope vs deferred to later stages.
- OD-HRM.3 — The authenticated approval channel for activation (later sprint; ADR-R-approval).

## 5. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. **0/6 active.** "PLANNED" ≠ active. Governed; nothing deleted.
