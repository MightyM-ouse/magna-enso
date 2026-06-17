# DECISION_LOG.md — Event Horizon (Magna Enso)

> Material decisions cross the Event Horizon and become permanent project memory.
> Rule: if a decision matters beyond the current chat, it belongs here. Never delete; supersede instead.
> Template & field definitions: `../planning/MAGNA_ENSO_DECISION_LOG_TEMPLATE.md`.
> Status vocabulary: PROPOSED · ACCEPTED · REJECTED · SUPERSEDED · REVISITED.

## Decision Index

| Decision ID | Date | Decision | Status | Decided By |
|---|---|---|---|---|
| EH-0001 | 2026-06-17 | Official name is **Magna Enso** (first operational form of Magna). | ACCEPTED | Human owner |
| EH-0002 | 2026-06-17 | Parent folder `/Users/vinay/Projects/AI/Magna/` with `magna-helix/`, `magna-enso/`, `trace/`, `brand-assets/`, `planning/`. | ACCEPTED | Human owner |
| EH-0003 | 2026-06-17 | Future stages (Satori→Beyond) are **releases/tags**, not copied code folders. | ACCEPTED | Human owner |
| EH-0004 | 2026-06-17 | Magna Enso is a **new, separate** repo; the HELIX/Magna repo is never modified. | ACCEPTED | Human owner |
| EH-0005A | 2026-06-17 | Hermes codebase is the **candidate technical base** for Magna Enso, pending Sprint 2 read-only audit + Sprint 3 governance design. | ACCEPTED | Human owner |
| EH-0005B | 2026-06-17 | Hermes Agent may be **evaluated as a candidate UI/E2E testing & runtime-verification worker** in later sprints. | PROPOSED | Proposed by Claude |
| EH-0006 | 2026-06-17 | TRACE governs Enso from day one (AI Project Profile, regulated-leaning). | ACCEPTED | Human owner |
| EH-0007 | 2026-06-17 | Adopt TRACE astronomy naming standard (plain-name-first in public docs). | ACCEPTED | Human owner |
| EH-0008 | 2026-06-17 | Default posture: local-first, LAN-first, safe-by-default, human-approval-driven; no auto-commit/push, no autonomous execution, no public exposure, no cloud by default. | ACCEPTED | Human owner |
| EH-0009 | 2026-06-17 | Awareness/autonomy stages (Satori+) are sequenced **after** the Enso governance foundation. | ACCEPTED | Human owner |
| EH-0010 | 2026-06-17 | Human owner (Vinay) is final authority for all approvals, commits, releases, and risk acceptance. | ACCEPTED | Human owner |
| EH-0011 | 2026-06-17 | Sprint 0 planning package (9 documents) frozen; Sprint 1 authorized. | ACCEPTED | Human owner |
| EH-0012 | 2026-06-17 | Git repository root is `magna-enso/` (parent `Magna/` is **not** the Git root); `ChatGPTReview/` remains local-only and outside Git tracking; initial branch is `main`; no commit/push without explicit human approval; Sprint 2 remains separately gated. | ACCEPTED | Human owner |
| EH-0013 | 2026-06-17 | Sprint 2 Hermes read-only audit accepted; Hermes SHA `33b1d144590a211100f42aa911fd7f91ba031507` is conditionally suitable only for future governed fork consideration, not direct adoption, activation, build, run, fork, or implementation. Sprint 3 and Sprint 4 remain not started. | ACCEPTED | Human owner |

### EH-0012 — Git initialization at magna-enso/ (expanded)
- Date: 2026-06-17
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision:
  - Git repository root is **`magna-enso/`**.
  - Parent `Magna/` is **not** the Git root.
  - `ChatGPTReview/` remains **local-only** and outside Git tracking (sibling of the repo; also in `.gitignore`).
  - Initial branch is **`main`**.
  - **No commit/push** without explicit human approval.
  - **Sprint 2 remains separately gated** (Git init does not start Sprint 2).
- Reason: Rooting Git at `magna-enso/` keeps the review-memory store structurally outside the repo,
  keeps the product history clean/publishable, and matches the Sprint 0 Folder/Repo Strategy (one product
  line = one repo; future stages are tags). Resolves RG-03 and RG-06.
- Alternatives Considered: Git root at parent `Magna/` — rejected (would pull `ChatGPTReview/`, `planning/`,
  `trace/`, `brand-assets/`, and the separate HELIX repo into scope, requiring mandatory ignores before any commit).
- Impact: `magna-enso/` is now version-controlled (branch `main`, no commits yet). Closes RG-03; RG-06 mitigated structurally + by `.gitignore`.
- Links: `../../ChatGPTReview/git-initialization-decision-package/FINAL_RECOMMENDATION.md`, RG-03, RG-06.

### EH-0013 — Sprint 2 Hermes read-only audit accepted
- Date: 2026-06-17
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision:
  - Sprint 2 — Hermes Read-Only Audit is accepted for human review closeout.
  - Accepted Hermes audited SHA: `33b1d144590a211100f42aa911fd7f91ba031507`.
  - Hermes is **conditionally suitable only** for future governed fork consideration.
  - Hermes is **not approved** for direct adoption, activation, build, run, fork, or implementation.
  - EH-0005B remains **PROPOSED**.
  - Sprint 3 is **NOT STARTED**.
  - Sprint 4 is **NOT STARTED**.
- Reason: Codex completed the approved read-only audit, Antigravity validation completed with no blocking issues, and the two non-blocking report corrections were applied.
- Alternatives Considered: Direct adoption, activation, build/run, fork, or implementation — rejected as out of scope and not approved.
- Impact: ENSO-F-0201 is DONE. Next action is Sprint 3 approval preparation only, not Sprint 3 execution.
- Links: `trace/evidence/ENSO-0002_LIGHT_CURVE.md`, `../../ChatGPTReview/sprint-2-hermes-audit/`, `../../ChatGPTReview/sprint-2-antigravity-validation/`, R-01, R-02, R-06.

## Notes

- The expanded EH-0005A / EH-0005B entry cards (with reasons and alternatives) are in
  `../planning/MAGNA_ENSO_DECISION_LOG_TEMPLATE.md`.
- New decisions get the next `EH-<seq>` and are appended here. A reversed decision is `SUPERSEDED`
  by a new ID, never deleted.

## Pending / open (not yet decisions)

- Git initialization & branch model for `magna-enso/` — **RESOLVED** by EH-0012 (root `magna-enso/`,
  branch `main`, no commit/push yet).
- Initial commit timing & `develop`/sprint branches — **open**, awaiting separate human instruction.
- Sprint 2 (Hermes read-only audit) — **RESOLVED** by EH-0013; accepted as conditionally suitable only.
- Sprint 3 approval preparation — **open**, not execution.
