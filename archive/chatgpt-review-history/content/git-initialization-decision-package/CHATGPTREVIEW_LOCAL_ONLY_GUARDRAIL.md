# CHATGPTREVIEW_LOCAL_ONLY_GUARDRAIL.md
# Magna Enso — Keeping ChatGPTReview/ Local-Only
# Type: Local-only decision package (planning/governance)
# Date: 2026-06-17
# Status: GUARDRAIL DEFINITION — advisory. ChatGPTReview/ was NOT moved or modified.

---

## 1. Purpose

Define the guardrail that keeps `ChatGPTReview/` — the ChatGPT continuity / review-memory store — and
its sub-reports **local-only** and out of any Git history or remote (RG-06). Advisory only.

## 2. What ChatGPTReview/ contains

```text
Magna/ChatGPTReview/
├── AGENT_OUTPUT_REVIEW_SOURCE_DATA.md          # ChatGPT review-memory source data
├── AGENT_OUTPUT_REVIEW_TEMPLATE.md
├── AGENT_OUTPUT_REVIEW_USAGE_PROMPT.md
├── antigravity-sprint-1-trace-skeleton-review/ # Sprint 1 local validation reports (8 files)
└── git-initialization-decision-package/        # this package
```

It is **review memory and decision-support material**, not a Magna Enso runtime artifact. The repository
(`magna-enso/trace/`) remains the source of truth for project state; `ChatGPTReview/` is supporting memory.

## 3. The guardrail (layered)

1. **Structural (primary):** keep `ChatGPTReview/` as a **sibling** of `magna-enso/`, not inside it.
   With the Git root at `magna-enso/`, this folder is outside the repo tree and cannot be tracked. ✅ already true.
2. **Ignore-rule (secondary):** include `ChatGPTReview/` and `**/ChatGPTReview/` in `.gitignore`
   (see `GITIGNORE_SCOPE_REVIEW.md` §3) as belt-and-suspenders.
3. **Process (tertiary):** never `git add` anything under `ChatGPTReview/`; never copy its contents into
   `magna-enso/`; never reference it as a tracked path. Workers reference it only as an **external pointer**
   (as `STAR_MAP.md` and `ROLE_REGISTRY.yaml` already do).
4. **Parent-level fallback:** if Git is ever rooted at `Magna/`, the **mandatory** first step before any
   commit is adding `ChatGPTReview/` to `.gitignore`. Without that, do not commit.

## 4. Existing in-repo references are pointers only (safe)

These point *to* the external memory but do not embed or track it — keep them as-is:
- `magna-enso/trace/STAR_MAP.md` → "External review memory" section.
- `magna-enso/trace/ROLE_REGISTRY.yaml` → `orchestration_continuity.external_memory:
  ../../ChatGPTReview/AGENT_OUTPUT_REVIEW_SOURCE_DATA.md`.

> RG-04 note: these are **relative paths**. If the folder layout ever changes, update the relative
> path — but do not move `ChatGPTReview/` (out of scope and explicitly forbidden this task).

## 5. Must-never list

- ❌ Never commit/push any file under `ChatGPTReview/`.
- ❌ Never copy review-memory or review reports into `magna-enso/`.
- ❌ Never move `ChatGPTReview/` (forbidden by this task; would also break the relative pointers).
- ❌ Never modify the existing review-memory files as part of Git setup.

## 6. Confirmation for this task

`ChatGPTReview/` was **not moved** and its review-memory files were **not modified**. This package only
**added** a new sub-folder of advisory documents (`git-initialization-decision-package/`) inside
`ChatGPTReview/`, which is itself local-only and excluded by the same guardrail.
