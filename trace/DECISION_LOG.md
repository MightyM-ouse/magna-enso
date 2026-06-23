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
| EH-0014 | 2026-06-17 | Sprint 3 Capability Governance Design accepted as **design/report-only** (17 reports; Antigravity validated; RC-01…RC-05 applied). **No implementation, runtime, or policy-engine code approved; no Hermes fork/build/run/modification approved.** EH-0005B remains PROPOSED; Hermes Agent not activated. Sprint 4 remains **blocked** and requires a separate approval package. | ACCEPTED | Human owner |
| EH-0015 | 2026-06-20 | Sprint 4 Clean Governed Hermes Baseline Preparation accepted as an **inert, quarantined provenance baseline only** after Antigravity validation. No executable Hermes modules, runtime enforcement, policy engine, Hermes activation, or Sprint 5 authorization. EH-0005B remains PROPOSED; R-06 remains OPEN. | ACCEPTED | Human owner |
| EH-0016 | 2026-06-24 | GitHub is the canonical collaboration source; approved task packets may authorize commit/push to isolated task branches, with PR-only integration to protected `main`. | ACCEPTED | Human owner |
| EH-0017 | 2026-06-24 | Each Magna evolution stage uses a separate repository so any stage can be selected independently. Supersedes EH-0003. | ACCEPTED | Human owner |
| EH-0018 | 2026-06-24 | The canonical stage spelling is **KENOSHA**. Earlier `Kensho` references are superseded. | ACCEPTED | Human owner |
| EH-0019 | 2026-06-24 | The Enso source repository is public to enable repository rules on the current GitHub plan; runtime/network exposure remains local/LAN-only by default. | ACCEPTED | Human owner |

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

### EH-0014 — Sprint 3 Capability Governance Design accepted (design/report-only)
- Date: 2026-06-17
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision:
  - Sprint 3 — Capability Governance Design is accepted as **design/report-only** work.
  - 17 design reports completed; Antigravity validation completed (verdict ACCEPTED_FOR_HUMAN_REVIEW);
    corrections RC-01…RC-05 applied.
  - **No implementation, no runtime code, no policy-engine code is approved.**
  - **No Hermes fork, build, run, source modification, or direct adoption is approved.**
  - EH-0005B remains **PROPOSED**; Hermes Agent is **not activated**.
  - Sprint 4 remains **blocked / NOT STARTED** and requires a **separate approval package**.
- Reason: Claude produced the governance design from the Sprint 2 audit; Antigravity validated it; the five
  non-blocking corrections were applied. The design is accepted as the agreed plan — acceptance is a design
  input, not an authorization to implement.
- Alternatives Considered: Treat acceptance as authorizing Sprint 4 implementation — rejected; Sprint 4 is a
  separate, explicitly-gated decision.
- Impact: ENSO-F-0301 is DONE. Sprint 4 readiness gates require human acceptance (now given for the design) +
  a separate Sprint 4 go-ahead before any fork work.
- Links: `trace/evidence/ENSO-0003_LIGHT_CURVE.md`, `../../ChatGPTReview/sprint-3-capability-governance-design/`, `../../ChatGPTReview/sprint-3-antigravity-validation/`, R-04, R-05, R-06, R-07, R-08, R-09, R-10.

### EH-0015 — Sprint 4 inert governed Hermes baseline accepted
- Date: 2026-06-20
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision:
  - Sprint 4 — Clean Governed Hermes Baseline Preparation is accepted as an **inert, quarantined provenance baseline only**.
  - Accepted Hermes source SHA remains `33b1d144590a211100f42aa911fd7f91ba031507`.
  - Antigravity validation verdict is **ACCEPTED_FOR_HUMAN_REVIEW** with rating 9.8/10, no blocking issues, and no required corrections.
  - `vendor/hermes/` contains only inert upstream license/manifest references and Magna-owned retained-surface metadata; no executable Hermes module source is present.
  - This acceptance does **not** authorize runtime enforcement, policy-engine code, Hermes activation/run/build, additional source import, or Sprint 5 work.
  - R-06 remains **OPEN** because runtime enforcement does not exist.
  - EH-0005B remains **PROPOSED**; Hermes Agent remains not activated.
  - Sprint 5 remains **NOT STARTED** and requires separate human approval.
- Reason: The bounded Sprint 4 baseline passed provenance, SHA, quarantine, dangerous-surface exclusion, license/static review, retained-metadata, TRACE, and runtime-boundary validation with no blocking findings.
- Alternatives Considered: Treating the inert baseline as runtime enforcement or authorizing Sprint 5 automatically — rejected as outside scope and unsafe.
- Impact: ENSO-F-0401 is DONE. Commit remains pending separate explicit approval; no push or merge is authorized.
- Links: `trace/evidence/ENSO-0004_LIGHT_CURVE.md`, `../../ChatGPTReview/sprint-4-governed-hermes-baseline/`, `../../ChatGPTReview/sprint-4-antigravity-validation/`, R-01, R-02, R-04, R-05, R-06, R-11.

### EH-0016 - GitHub canonical multi-agent workflow
- Date: 2026-06-24
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision: GitHub issues, task packets, task branches, pull requests, repository evidence, and Actions artifacts form the operational collaboration record. Workers may commit and push only to an assigned branch when the task packet authorizes it. Protected `main`, no force push, no self-merge, independent review where required, and Product Owner merge authority remain mandatory.
- Supersession: Replaces only the absolute no-commit/no-push portions of EH-0008 and EH-0012. Their human authority and safety intent remain accepted.

### EH-0017 - Separate repository per evolution stage
- Date: 2026-06-24
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision: Enso, Satori, KENOSHA, Bodhi, Prabhava, and later stages use separate repositories. Shared assets require explicit versioned contracts.
- Supersession: EH-0003 is SUPERSEDED. Existing Enso history remains unchanged.

### EH-0018 - KENOSHA spelling
- Date: 2026-06-24
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision: `KENOSHA` is the canonical stage name. Historical evidence is not rewritten; active documents must use KENOSHA.

### EH-0019 - Public source, private runtime boundary
- Date: 2026-06-24
- Status: ACCEPTED
- Decided By: Human owner (Vinay)
- Decision: The GitHub source repository is public. This does not authorize public listeners, tunnels, cloud execution, external messaging, or public runtime endpoints. Public-source security, secret scanning, provenance, and evidence-redaction controls are mandatory.

## Notes

- The expanded EH-0005A / EH-0005B entry cards (with reasons and alternatives) are in
  `../planning/MAGNA_ENSO_DECISION_LOG_TEMPLATE.md`.
- New decisions get the next `EH-<seq>` and are appended here. A reversed decision is `SUPERSEDED`
  by a new ID, never deleted.

## Pending / open (not yet decisions)

- Git initialization & branch model for `magna-enso/` — **RESOLVED** by EH-0012 (root `magna-enso/`,
  branch `main`, no commit/push yet).
- GitHub branch model — **RESOLVED** by EH-0016; short-lived task branches and PR-only integration.
- Sprint 2 (Hermes read-only audit) — **RESOLVED** by EH-0013; accepted as conditionally suitable only.
- Sprint 3 (Capability Governance Design) — **RESOLVED** by EH-0014; accepted as design/report-only.
- Sprint 4 (clean governed Hermes baseline preparation) — **RESOLVED** by EH-0015; accepted as an inert,
  quarantined provenance baseline only.
- Sprint 5 (default-deny capability gate / policy engine) — **open / NOT STARTED**; requires separate explicit
  human approval. Sprint 4 acceptance does not authorize Sprint 5.
