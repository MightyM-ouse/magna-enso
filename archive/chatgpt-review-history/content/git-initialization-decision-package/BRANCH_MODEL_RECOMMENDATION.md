# BRANCH_MODEL_RECOMMENDATION.md
# Magna Enso — Branch Model Recommendation
# Type: Local-only decision package (planning/governance)
# Date: 2026-06-17
# Status: RECOMMENDATION — no branches created, no Git initialized.

---

## 1. Purpose

Recommend the branch and tag model for the `magna-enso/` repository, consistent with the Sprint 0
Folder/Repo Strategy and the frozen governance principles. Advisory only.

## 2. Recommended branches

| Branch | Purpose | Rules |
|---|---|---|
| `main` | Stable, human-approved baseline. | **Protected.** No direct pushes. No force-push. Merges require a human-reviewed review-package (Light Curve). |
| `develop` | Integration of completed, evidenced sprint work. | Merged from `sprint/*` after evidence + human review. |
| `sprint/NN-slug` | One short-lived branch per sprint. | e.g. `sprint/02-hermes-readonly-audit`, `sprint/03-capability-governance-design`. Deleted after merge. |
| `audit/hermes-readonly` | Sprint 2 audit **notes only** (`docs/audit/`). | **Never** contains Hermes source. The Hermes clone lives in a separate scratch workspace outside the repo. |

> Note: `sprint/02-...` and `audit/hermes-readonly` are **created only when Sprint 2 is separately
> approved** — not now.

## 3. Recommended tags (releases)

Future Magna stages are **tags on this one repo**, never copied folders (EH-0003):

| Tag | Stage |
|---|---|
| `v1.0-enso` | Magna Enso (this release target) |
| `v1.0-enso-rcN` | Enso release candidates (Sprint 15) |
| `v2.0-satori` | Magna Satori |
| `v3.0-kensho` | Magna Kensho |
| `v4.0-bodhi` | Magna Bodhi |
| `v5.0-prabhava` | Magna Prabhava |
| `Beyond` (rolling) | Magna Beyond |

## 4. Mapping sprints → branches

```text
Sprint 1 (skeleton, DONE)        → would land on main as the initial governed baseline
Sprint 2 (Hermes audit)          → sprint/02-hermes-readonly-audit + audit/hermes-readonly (notes only)
Sprint 3 (governance design)     → sprint/03-capability-governance-design
Sprint 4 (clean governed fork)   → sprint/04-clean-governed-hermes-fork-baseline
...                              → sprint/NN-...
Release candidate (Sprint 15)    → tag v1.0-enso-rc1, then v1.0-enso
```

## 5. Protection & approval rules (carry the frozen governance)

- `main` protected: no direct commits, no force-push, no auto-merge.
- Every merge to `main` requires a **human-reviewed review-package** (diff + test logs + validation report).
- **No auto-commit / no auto-push** anywhere (EH-0008). The human owner approves every merge/release.
- Tags are created by the human owner (or under explicit human approval) at stabilization points.

## 6. First-baseline note

If the human owner initializes Git now, the recommended **first state** is:
- Branch `main` created, `.gitignore` present, working tree = the accepted Sprint 1 skeleton.
- **No commit is made by any worker automatically.** The human owner decides whether/when to make the
  initial commit (and that commit, if made, should reference Sprint 1 acceptance + `ENSO-0001_LIGHT_CURVE.md`).

## 7. Out of scope

No branches, tags, or commits are created by this package. Branch creation begins only with approved sprint work.
