# GIT_INITIALIZATION_DECISION.md
# Magna Enso — Git Initialization Decision
# Type: Local-only decision package (planning/governance)
# Prepared by: Claude (architecture/governance)
# Date: 2026-06-17
# Status: RECOMMENDATION for human owner — NOT an action. Git was NOT initialized by this package.

---

## 1. Purpose

Resolve open items **RG-03** (Git initialization timing / location / branch model) and **RG-06**
(keep `ChatGPTReview/` local-only and out of Git) before Sprint 2 begins. This document is advisory.
**No `git init`, no commit, no push was performed.** Human owner remains final authority (EH-0010).

## 2. Decision questions

1. Where is the Git repository root?
2. When do we initialize — now or defer?
3. What branch model?
4. What must `.gitignore` cover?
5. How do we keep `ChatGPTReview/` local-only?
6. How do we keep Sprint 2 blocked until separately approved?

(Each is detailed in its own report; this file gives the headline decisions.)

## 3. Recommended decisions

| # | Decision | Recommendation |
|---|---|---|
| 1 | **Repo root** | **`magna-enso/`** (the product repo), NOT the parent `Magna/` folder. |
| 2 | **Timing** | **Initialize now** (after this package is human-approved), **before Sprint 2** — with `.gitignore` in place first. |
| 3 | **Branch model** | `main` (protected) + `develop` + `sprint/NN-slug` + `audit/hermes-readonly`. See `BRANCH_MODEL_RECOMMENDATION.md`. |
| 4 | **.gitignore** | Defensive ignore (OS/editor/runtime artifacts + secrets) and documented exclusion rules. See `GITIGNORE_SCOPE_REVIEW.md`. |
| 5 | **ChatGPTReview/ local-only** | Keep it a **sibling** of `magna-enso/` (it already is). Repo-at-`magna-enso/` naturally excludes it. See `CHATGPTREVIEW_LOCAL_ONLY_GUARDRAIL.md`. |
| 6 | **Sprint 2 gate** | Git init does not start Sprint 2. Sprint 2 needs **separate explicit human approval**; Hermes clone goes to a separate scratch workspace, never into `magna-enso/`. |

## 4. Why `magna-enso/` and not parent `Magna/`

Current parent layout (`<MAGNA_LOCAL_ROOT>/`):

```text
Magna/
├── ChatGPTReview/     # local-only review memory (must NOT be tracked)
├── brand-assets/      # shared visual identity
├── magna-enso/        # the product repo  ← Git root here
├── planning/          # Sprint 0 planning package
└── trace/             # TRACE methodology reference (blueprint)
```

Initializing at `magna-enso/`:
- **Naturally excludes** `ChatGPTReview/` (it is one level up, outside the repo) — satisfies RG-06 structurally, not just by rule.
- Keeps the product repo's history clean and publishable, separate from local review memory and planning scaffolding.
- Matches the Sprint 0 Folder/Repo Strategy: **one product line = one repo**, future stages are tags on this repo.

Initializing at parent `Magna/` would pull `ChatGPTReview/` (and `planning/`, `trace/`, `brand-assets/`)
into tracking scope and **require** an explicit `.gitignore` exclusion of `ChatGPTReview/` before the first
commit — strictly riskier. **Not recommended.** (If ever chosen, see the mandatory exclusions in
`GITIGNORE_SCOPE_REVIEW.md` §4.)

## 5. Governance constraints carried into Git

When Git is eventually initialized (separate, human-approved step):
- **No auto-commit, no auto-push, no force-push** (EH-0008). The system never commits/pushes on its own.
- `main` is **protected**; merges require a human-reviewed review-package (Light Curve).
- The **existing Magna / HELIX repo is never modified** and is **not** nested inside this repo.
- **No Hermes source** is ever committed to `magna-enso/` (Sprint 2 clone lives in a scratch workspace).
- `ChatGPTReview/` is **never** tracked.

## 6. What this package does NOT do

- Does **not** run `git init`, `git add`, `git commit`, or `git push`.
- Does **not** create `.gitignore` inside `magna-enso/` (that is the approved next step).
- Does **not** start Sprint 2, clone Hermes, or modify the HELIX repo or review-memory files.

## 7. Recommended next action for the human owner

Approve repo root = `magna-enso/`, branch model, and `.gitignore` scope. Then a worker may, **on explicit
approval**, create `.gitignore` first and run `git init` at `magna-enso/` — with **no commit/push** until
you direct it. Log the choice as a new Event Horizon decision (suggested `EH-0012`).
