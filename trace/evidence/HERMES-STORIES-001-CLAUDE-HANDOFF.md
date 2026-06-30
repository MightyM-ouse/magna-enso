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
| `trace/evidence/HERMES-STORIES-001-CLAUDE-HANDOFF.json` | Machine-readable handoff |

---

## Product Owner Decisions Applied

1. **RETAIN_DISABLED_BY_DEFAULT** — Advanced non-default capabilities are not permanently removed; they are disabled by default and may be enabled by explicit Product Owner or user action. Applied to story 002, story 010, and the story index.

2. **Verdict and next-action output split** — Chat/Telegram provides a short summary referencing the TRACE/evidence ID; GitHub provides the complete verdict, evidence, and next-action suggestions. Applied to stories 007, 008, 010, and the story index.

3. **Strong internal TRACE** — TRACE is enforced inside Magna (live internal state) and in GitHub (durable record). Every action must create/update a TRACE event before proceeding. No dispatch, write, verdict, or closure without active TRACE envelope. Applied to stories 006, 007, 008, 009, 010, and the story index.

4. **Epic 1 local-first primary flow** — 13-step local Magna-controlled orchestration is the primary flow; Telegram continuation is activation-gated. Applied to story 010 and the story index.

---

## PR #35 Governance CI

**Before:** FAILING — `product/hermes-runtime-adoption-stories` had no registered task.

**After (on this correction branch):** Registry now contains `HERMES-US-001` entry for the product branch and `HERMES-STORIES-001` entry for this correction branch.

**Merge order:** Product Owner must decide whether to merge this correction branch to main first (providing registry entry on main), then rebase the product branch, or apply the registry entry directly to the product branch.

---

## Open Questions

| # | Question | Story |
|---|---|---|
| OQ-1 | Which sender boundary mechanism is approved for Telegram? | 002 |
| OQ-2 | What is the first approved demonstration scenario for end-to-end flow? | 010 |
| OQ-3 | Task continuation: both remote channel and ChatGPT, or one first? | 010 |
| OQ-4 | Minimum TRACE envelope view required for Product Owner review? | 009 |
| OQ-5 | Forward/backward traceability visible in Command Center UI, GitHub evidence, or both? | 009 |
| OQ-6 | Should RETAIN_DISABLED_BY_DEFAULT capabilities be listed in Command Center UI when disabled? | General |
| OQ-7 | PR #33 status — branding dependency for story 001 | 001 |

---

## Final Verdict

**ACCEPT_WITH_CORRECTIONS — ready for Product Owner review**

All Product Owner CHANGES_REQUIRED corrections applied. Stories remain `READY_FOR_REFINEMENT`. Product Owner review and decision required before any stories move to `DESIGN_READY` or `APPROVED`.

---

## Traceability

| Direction | Links |
|---|---|
| Backward | PR #35 Product Owner comments; `trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md`; `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md` |
| Forward | Product Owner review of `claude/HERMES-STORIES-001-corrections`; open questions resolution; final story approval; sprint planning |

**Review report:** `trace/reviews/HERMES-STORIES-001-CLAUDE-REVIEW.md`  
**Machine-readable:** `trace/evidence/HERMES-STORIES-001-CLAUDE-HANDOFF.json`
