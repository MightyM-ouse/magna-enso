# SPRINT_3_SCOPE_AND_BOUNDARIES.md
# Magna Enso — Sprint 3 Scope and Boundaries
# Type: Local-only approval package
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 3 NOT started.

---

## 1. What Sprint 3 IS

A **capability-governance design sprint**. It produces the *design* (documents, models, schemas as
illustration) for how Magna Enso will control every Hermes-derived capability under a **default-deny**
model — **before** any fork or implementation. TRACE mode: Discovery / Review (design).

## 2. What Sprint 3 IS NOT

| Not this | Why |
|---|---|
| Implementation | No executable code is written. |
| A fork | Forking is Sprint 4, only after this design is accepted. |
| Runtime work | Nothing runs. |
| Hermes activation / build / run | Hermes is not built, run, installed, re-cloned, or modified. |
| UI work | The Capability Control UI is Sprint 13. |
| Scheduler implementation | Report-only scheduler is built in Sprint 9. |
| Approval-engine implementation | The unified approval engine is a **concept** here; built in Sprint 5+. |
| Sprint 4 | Clean governed fork baseline is separately gated. |

## 3. Hard boundaries (must hold for the whole sprint)

1. No code implementation (policy engine, UI, scheduler, runtime) — **design artifacts only**.
2. No modifying, cloning, building, running, or installing Hermes (or its dependencies).
3. No Hermes source copied into `magna-enso/`; reports cite identifiers/paths + the audited SHA only.
4. No commits, no pushes, no new branches (without separate explicit approval).
5. No Sprint 4 work; no promoting EH-0005B; no activating Hermes Agent.
6. Human owner is final authority (EH-0010); Antigravity validates before acceptance.

## 4. Design-only vs schemas (clarifying the gray area)

"Design-only" permits **illustrative, non-executable artifacts**: capability taxonomy tables, a capability
**policy schema sketch** (e.g. YAML/JSON shape with field definitions), state-machine diagrams in text, and
a chokepoint map. It does **not** permit a working policy engine, validators that run, or any code wired
into a runtime. Decision 2 lets the human owner confirm whether schema sketches are in scope (recommended:
yes, as design artifacts only).

## 5. Inputs (from Sprint 2)

Sprint 3 consumes the accepted Sprint 2 audit findings (code map, dispatch map, autonomy entry points,
external surface map, capability-gating feasibility, reuse recommendation) for Hermes @ `33b1d144`. It does
**not** re-audit or re-clone Hermes.

## 6. Out of scope (defer)

- Building any engine, gate, or UI (Sprint 5+).
- Deciding the final fork contents in code (Sprint 4 implements against this design).
- Performance, deployment, or integration concerns.

## 7. Definition of done (Sprint 3)

Sprint 3 is complete when the design reports in `SPRINT_3_OUTPUT_REPORTS_SPEC.md` exist and answer the
**Sprint 4 readiness gates** (`§H` of the brief), Antigravity has validated them, a `SPRINT_3_LIGHT_CURVE.md`
is written, and the human owner accepts. **Then the sprint stops** — it does not roll into Sprint 4.
