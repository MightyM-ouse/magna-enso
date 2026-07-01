# HERMES-STORIES-001 — Claude Correction Handoff

**Task:** HERMES-STORIES-001  
**Agent:** Claude  
**Role:** Product story correction reviewer  
**Correction branch:** `claude/HERMES-STORIES-001-corrections`  
**Target branch:** `product/hermes-runtime-adoption-stories`  
**Target PR:** #35  
**Date:** 2026-06-30  

---

## SYNC Verdict

**SYNC_PASS**

Correction branch checked out from `origin/product/hermes-runtime-adoption-stories`. Task HERMES-STORIES-001 registered `IN_PROGRESS`. Task HERMES-US-001 registered `PUSHED_FOR_REVIEW` to fix PR #35 governance CI. Hermes not activated. No runtime code modified. No sprint tasks created. Stories remain `READY_FOR_REFINEMENT`.

---

## Objective

Apply Product Owner CHANGES_REQUIRED corrections from PR #35 comments to Magna-Hermes runtime adoption product user stories. Fix PR #35 governance CI failure. Produce review report and handoff evidence.

---

## Files Produced

| File | Purpose |
|---|---|
| `trace/ACTIVE_WORK_REGISTRY.yaml` | Added HERMES-US-001 (fixes PR #35 governance CI) and HERMES-STORIES-001 entries |
| `trace/product/PRODUCT_STORY_INDEX.md` | Major update: capability model, primary flow, RETAIN_DISABLED_BY_DEFAULT, strong internal TRACE, success criteria, sprint outcomes |
| `trace/product/user-stories/MAG-US-HERMES-002-*.md` | Telegram activation-gated, authorization gates, WhatsApp as RETAIN_DISABLED_BY_DEFAULT |
| `trace/product/user-stories/MAG-US-HERMES-006-*.md` | TRACE-linked result state, result states enum, changed vs. claimed files |
| `trace/product/user-stories/MAG-US-HERMES-007-*.md` | TRACE envelope link, detailed verdict, next-action suggestions, durable-not-replacement |
| `trace/product/user-stories/MAG-US-HERMES-008-*.md` | Notification surface rule, TRACE/evidence ID reference, does-not-replace-GitHub |
| `trace/product/user-stories/MAG-US-HERMES-009-*.md` | Major rewrite: TRACE rule, 17 TRACE events, blocking requirement, backward/forward traceability |
| `trace/product/user-stories/MAG-US-HERMES-010-*.md` | Major expansion: 13-step primary flow, local-first, Magna review/verify/verdict/next-actions, RETAIN_DISABLED_BY_DEFAULT list |
| `trace/reviews/HERMES-STORIES-001-CLAUDE-REVIEW.md` | Full correction review report |
| `trace/evidence/HERMES-STORIES-001-CLAUDE-HANDOFF.md` | This file |

---

## Product Owner Decisions Applied

1. **RETAIN_DISABLED_BY_DEFAULT** — Advanced non-default capabilities are not permanently removed; they are disabled by default and may be enabled by explicit Product Owner or user action. Applied to story 002, story 010, and the story index.

2. **Verdict and next-action output split** — Chat/Telegram provides a short summary referencing the TRACE/evidence ID; GitHub provides the complete verdict, evidence, and next-action suggestions. Applied to stories 007, 008, 010, and the story index.

3. **Strong internal TRACE** — TRACE is enforced inside Magna (live internal state) and in GitHub (durable record). Every action must create/update a TRACE event before proceeding. No dispatch, write, verdict, or closure without active TRACE envelope. Applied to stories 006, 007, 008, 009, 010, and the story index.

4. **Epic 1 local-first primary flow** — 13-step local Magna-controlled orchestration is the primary flow; Telegram continuation is activation-gated. Applied to story 010 and the story index.

---

## PR #35 Governance CI

**Before corrections:** FAILING — `product/hermes-runtime-adoption-stories` had no registered task in the registry.

**After corrections:** **SUCCESS.** All corrections merged into `product/hermes-runtime-adoption-stories` via PR #38, PR #39, and PR #40. Registry now contains `HERMES-US-001` (product branch task) with `correction_phase_modifies` authorizing the review and handoff MD files. Governance validator passes on the current PR #35 head.

---

## Resolved Product Owner Questions

All open questions were answered by the Product Owner on 2026-06-30 and applied to the story files. No open questions remain.

| # | Resolution | Story |
|---|---|---|
| OQ-1 | Telegram sender boundary: **Telegram User ID allowlist**. Unknown IDs rejected or paused. Token-only not primary boundary. | 002 |
| OQ-2 | First approved demo scenario: **"Review PR status for Magna Enso and prepare assessment."** 14-step demo flow in story 010. | 010 |
| OQ-3 | Task continuation: **both local/chat (Epic 1 default) and remote Telegram (activation-gated)**. Local first. | 002, 010 |
| OQ-4 | Minimum TRACE envelope view: **specified in story 009** — 23 required fields, 8 audit questions. | 009 |
| OQ-5 | TRACE traceability visibility: **both** Magna Command Center UI (live) and GitHub (durable). Chat/Telegram summaries only. | 009, 010, index |
| OQ-6 | RETAIN_DISABLED_BY_DEFAULT in UI: **yes, visible when disabled** — shows name, status, reason, gates, enablement eligibility. | 010, index |
| OQ-7 | PR #33 branding: **unresolved dependency until GitHub confirms merge**. Story 001 remains dependent on acceptance. Reduced-motion fallback required. | 001, index |

---

## Final Verdict

**ACCEPT_WITH_CORRECTIONS — ready for Product Owner merge decision**

All Product Owner CHANGES_REQUIRED corrections applied. All open questions (OQ-1 through OQ-7) resolved and applied to story files. Governance validation: **SUCCESS** on current PR #35 head. Stories remain `READY_FOR_REFINEMENT`. No implementation tasks created. No stories marked final or design-ready. Product Owner merge decision required.

---

## Traceability

| Direction | Links |
|---|---|
| Backward | PR #35 Product Owner comments; `trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md`; `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md` |
| Forward | Product Owner merge decision on PR #35; final Product Owner approval of stories; downstream sprint planning (only after Product Owner approval) |

**Review report:** `trace/reviews/HERMES-STORIES-001-CLAUDE-REVIEW.md`
