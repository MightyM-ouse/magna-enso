# HERMES_AUDIT_PLAN.md
# Magna Enso — Hermes Read-Only Audit Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN for execution AFTER human approval. Nothing executed yet.

---

## 1. Objective

Answer 14 questions about Hermes to decide its suitability as the Sprint 4 technical base, producing the
reports in `SPRINT_2_OUTPUT_REPORTS_SPEC.md`. Read-only; in the scratch workspace only.

## 2. Method (TRACE Investigation Mode)

For each question: route to the relevant files in the scratch clone → gather evidence (paths + commit SHA)
→ form findings with confidence → record in the matching report. No edits, no builds, no runs.

## 3. The 14 audit questions → where they land

| # | Question | Primary report | What "answered" looks like |
|---|---|---|---|
| 1 | What is Hermes' architecture? | `HERMES_CODE_MAP.md` | High-level component diagram (described in text), layering, entry points |
| 2 | What modules exist? | `HERMES_CODE_MAP.md` | Module inventory with one-line purpose each |
| 3 | Which modules are relevant to Magna Enso? | `MAGNA_ENSO_REUSE_RECOMMENDATION.md` | Relevance tag per module (keep / rebuild / exclude) |
| 4 | Which modules are risky? | `EXTERNAL_SURFACE_MAP.md` + reuse rec | Risk tag per module, linked to R-01…R-15 |
| 5 | Where are action-dispatch chokepoints? | `ACTION_DISPATCH_MAP.md` | The function(s) all actions flow through (gate candidates) |
| 6 | Where are memory writes? | `AUTONOMY_ENTRY_POINT_MAP.md` | All code paths that persist memory |
| 7 | Where are skill writes? | `AUTONOMY_ENTRY_POINT_MAP.md` | All code paths that register/activate skills |
| 8 | Where is scheduler/cron behavior? | `AUTONOMY_ENTRY_POINT_MAP.md` | Timed/triggered execution paths |
| 9 | Where are messaging gateways? | `EXTERNAL_SURFACE_MAP.md` | Inbound/outbound messaging surfaces |
| 10 | Where are terminal backends? | `EXTERNAL_SURFACE_MAP.md` | Shell/terminal execution surfaces |
| 11 | Where are browser/web tools? | `EXTERNAL_SURFACE_MAP.md` | Browser/web automation surfaces |
| 12 | Where are cloud/provider integrations? | `EXTERNAL_SURFACE_MAP.md` | Cloud/provider/API dependencies (R-04) |
| 13 | Can these be governed by Magna capability policy? | `CAPABILITY_GATING_FEASIBILITY.md` | Per-surface: gateable? at which chokepoint? gaps? |
| 14 | Is Hermes suitable as the Sprint 4 base? | `MAGNA_ENSO_REUSE_RECOMMENDATION.md` | Go / conditional-go / no-go, with rationale + confidence |

## 4. Provenance & license (run first)

Before the code map, record provenance and license — they can independently gate the whole effort:
- `HERMES_PROVENANCE.md` — source repo URL, exact commit SHA audited, upstream default branch, date.
- `LICENSE_AND_DEPENDENCY_REVIEW.md` — top-level license (confirm MIT or actual), dependency licenses,
  any copyleft/ToS concerns. **License verification is mandatory before Sprint 4** (Decision 9; R-02).

## 5. Capability-gating lens (the key feasibility test)

The central question for Magna Enso is #13: **can every dangerous surface be placed behind a single
policy gate?** The audit looks for **chokepoints** — narrow points all actions pass through. Many
chokepoints = easy to govern (default-deny is enforceable). Scattered, ungated entry points = harder
(higher R-06 policy-bypass risk). This finding drives the Sprint 3 governance design.

## 6. Evidence rules

- Cite file path + commit SHA for every claim.
- Quote only **minimal identifiers** (function/file names) — **never** paste Hermes source into reports
  or into `magna-enso/`.
- State **confidence** (high/medium/low) and **evidence for/against** for judgment calls.
- Separate facts from recommendations.

## 7. Stop condition

When all reports exist and Antigravity has validated them, write `SPRINT_2_LIGHT_CURVE.md` and **stop**.
Do not begin Sprint 3 design or Sprint 4 fork work. The reuse recommendation is **input** to those sprints,
not their start.
