# SPRINT_2_SCOPE_AND_BOUNDARIES.md
# Magna Enso — Sprint 2 Scope and Boundaries
# Type: Local-only approval package
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 2 NOT started.

---

## 1. What Sprint 2 IS

A **read-only investigation** (TRACE Investigation Mode) of the Hermes codebase as a **candidate**
technical base for the Magna Enso runtime. It maps architecture, provenance, license, risk surface,
and capability-gating feasibility, and produces a reuse recommendation for Sprint 4. **Reports only.**

"Read-only audit" means:
- A read-only local **clone** of Hermes is made **only** in a separate scratch workspace, **after explicit
  human approval** (per Charter / EH-0005A).
- The audit **reads** the code. It does not modify, fork, build, run, or integrate it.
- Findings live in Markdown reports — first local-only, committed later only if the human owner chooses.

## 2. What Sprint 2 IS NOT

| Not this | Why |
|---|---|
| Implementation | No runtime code is written in Sprint 2. |
| A fork | Forking/baseline creation is **Sprint 4**, and only after Sprint 3 governance design. |
| A rebrand | No copying-and-renaming of Hermes. |
| An integration | No wiring Hermes into Magna Enso. |
| Runtime work | No execution of Hermes capabilities. |
| Sprint 3/4 work | Governance design (S3) and clean fork (S4) are separate, later, separately-approved. |
| Hermes Agent activation | Hermes Agent (UI/E2E) stays **candidate** (EH-0005B PROPOSED); it does not run here. |

## 3. Hard boundaries (must hold for the whole sprint)

1. **No modification to Hermes** — the clone is read-only; nothing is edited, built, or run.
2. **No modification to existing Magna / HELIX repo.**
3. **No Hermes source inside `magna-enso/`** — not even snippets; quote only minimal identifiers in reports.
4. **No commits, no pushes** without separate explicit human approval.
5. **No new branches** unless explicitly approved (Decision 3).
6. **No runtime code, no integrations.**
7. **Scratch workspace is local-only and never committed.**
8. **Human owner is final authority** (EH-0010); Antigravity validates before acceptance.

## 4. Scope of inspection (in-bounds)

Reading and mapping, within the scratch clone, of: repository layout, module structure, dependency
manifests and licenses, action-dispatch chokepoints, memory/skill write paths, scheduler/cron behavior,
messaging gateways, terminal backends, browser/web tools, and cloud/provider integrations — strictly to
answer the 14 audit questions in `HERMES_AUDIT_PLAN.md`.

## 5. Out of scope (defer)

- Designing the Magna capability policy (that is Sprint 3).
- Choosing what to keep/rebuild in code (decided at Sprint 3/4 with this audit as input).
- Any performance testing, execution, or live behavior of Hermes.
- Any network calls Hermes might make (the audit reads code; it does not run it).

## 6. Definition of done (Sprint 2)

Sprint 2 is complete when the audit reports in `SPRINT_2_OUTPUT_REPORTS_SPEC.md` exist, Antigravity has
validated them, a `SPRINT_2_LIGHT_CURVE.md` is written, and the human owner reviews the reuse
recommendation. **Then the sprint stops** — it does not roll into Sprint 3/4.
