# STAR_MAP.md — Project Status (Magna Enso)

> The Star Map is the current project state and next steps. Read it on entry; update it on exit.

## Current state

| Field | Value |
|---|---|
| Project | Magna Enso (first operational form of Magna) |
| Release target | `v1.0-enso` |
| Current sprint | **Between Sprint 3 and Sprint 4** |
| Sprint status | **Sprint 3 accepted (design-only); Sprint 4 not started / blocked** (human-approved 2026-06-17) |
| Overall stage | Governance design complete; no runtime code yet |
| Operating model | TRACE (AI Project Profile, regulated-leaning) |
| Final authority | Human owner (Vinay) |
| Git initialized | **Yes** — repo root `magna-enso/` (EH-0012, 2026-06-17) |
| Branch | **main** |
| Commit | Last accepted commit: `94d63ed` (Sprint 2 closeout) |
| `.gitignore` | present; `ChatGPTReview/` excluded (local-only) |
| Last accepted | Sprint 3 — Capability Governance Design (ENSO-F-0301 DONE, design-only), human-approved 2026-06-17 |

## What exists now

- TRACE operating instance under `trace/`: config, onboarding, this status file, context index,
  role registry, workflows, task-packet & evidence templates, decision log, feature tracker,
  risk register, validation checklist, and `evidence/`.
- Entry point `AGENTS.md` + thin bridges (`CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`).
- Repo `README.md`.
- Sprint 2 closeout evidence: `trace/evidence/ENSO-0002_LIGHT_CURVE.md`.
- Local-only Sprint 2 audit and validation reports under `../../ChatGPTReview/sprint-2-hermes-audit/`
  and `../../ChatGPTReview/sprint-2-antigravity-validation/`.

## What does NOT exist yet (by design)

- No runtime code (`src/`), no policy engine, no UI, no scheduler, no integrations.
- No Hermes source in `magna-enso/`.
- No Hermes direct adoption, activation, build, run, fork, or implementation approval.
- Sprint 3 produced **design/reports only** — no implementation, no runtime code, no policy-engine code.
- Sprint 4 is **NOT STARTED** and **blocked** — it requires a **separate approval package**.

## Sprint 1 acceptance

- **Sprint 1 accepted by the human owner on 2026-06-17.** Feature `ENSO-F-0101` is **DONE**.
- Evidence: `trace/evidence/ENSO-0001_LIGHT_CURVE.md` was created and **human-approved** (Light level).
- Antigravity recommended acceptance (review 9.2/10, implementation 9.6/10, no blocking issues);
  the human owner remains final authority (EH-0010).

## Sprint 2 acceptance

- **Sprint 2 accepted by the human owner on 2026-06-17.** Feature `ENSO-F-0201` is **DONE**.
- Hermes audited SHA: `33b1d144590a211100f42aa911fd7f91ba031507`.
- Evidence: `trace/evidence/ENSO-0002_LIGHT_CURVE.md` was created and **human-approved**.
- Codex read-only audit and Antigravity validation are complete; local-only report packages remain outside Git under `../../ChatGPTReview/`.
- Hermes is accepted as **conditionally suitable only** for future governed fork consideration.
- Hermes is **not approved** for direct adoption, activation, build, run, fork, or implementation.
- EH-0005B remains **PROPOSED**.

## Sprint 3 acceptance

- **Sprint 3 — Capability Governance Design accepted by the human owner on 2026-06-17 as design/report-only.**
  Feature `ENSO-F-0301` is **DONE**.
- Deliverables (all design-only): capability taxonomy (corrected), policy schema, default-deny model,
  disablement tiers, unified approval engine concept, policy chokepoint map, memory/skill draft-only,
  scheduler report-only, browser/web read-only, terminal/code approval-required, messaging/cloud disabled,
  plugin/MCP governance, delegation recursion control, Hermes surface governance matrix, Sprint 4 readiness gates.
- **Antigravity validation completed** (verdict ACCEPTED_FOR_HUMAN_REVIEW); **RC-01 through RC-05** corrections applied.
- Evidence: `trace/evidence/ENSO-0003_LIGHT_CURVE.md` (Full). Local-only packages:
  `../../ChatGPTReview/sprint-3-capability-governance-design/` and `../../ChatGPTReview/sprint-3-antigravity-validation/`.
- **No implementation / runtime code / policy-engine code approved.** No Hermes fork/build/run/modification
  approved. **EH-0005B remains PROPOSED**; Hermes Agent not activated.

## Next steps

1. **Sprint 4 — Clean governed Hermes fork baseline:** **NOT STARTED** and **blocked**. It requires a
   **separate Sprint 4 approval package** and explicit human approval against the Sprint 4 readiness gates.
2. Accepting the Sprint 3 design does **not** authorize implementation — Sprint 4 is a separate decision.
3. No commit/push without separate explicit human instruction.

## External review memory

ChatGPT (orchestration council / continuity review) maintains a separate review-memory source-data file
at `../../ChatGPTReview/AGENT_OUTPUT_REVIEW_SOURCE_DATA.md`. It is **review memory**, not a Magna Enso
runtime artifact, and is updated after each agent-output review. The repository (this `trace/` instance)
remains the source of truth for project state.

## Pointers (source of truth)

- Identity/governance: `../../planning/MAGNA_ENSO_PROJECT_CHARTER.md`
- Sprint plan: `../../planning/MAGNA_ENSO_SPRINT_PLAN.md`
- Decisions: `DECISION_LOG.md` · Features: `FEATURE_TRACKER.md` · Risks: `RISK_REGISTER.md`
