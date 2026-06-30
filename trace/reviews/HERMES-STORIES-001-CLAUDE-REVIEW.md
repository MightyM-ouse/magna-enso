# HERMES-STORIES-001 — Claude Product Story Correction Review

**Reviewer:** Claude (product-story correction reviewer)  
**Correction branch:** `claude/HERMES-STORIES-001-corrections`  
**Target branch:** `product/hermes-runtime-adoption-stories`  
**Target PR:** #35 — Add Magna-Hermes runtime adoption product stories  
**Review date:** 2026-06-30  
**Authority:** Product Owner CHANGES_REQUIRED comments on PR #35

---

## 1. SYNC Verdict

**SYNC_PASS**

| Check | Result |
|---|---|
| Working directory | `/Users/vinay/Projects/AI/Magna/magna-enso` ✓ |
| Correction branch | `claude/HERMES-STORIES-001-corrections` (from `origin/product/hermes-runtime-adoption-stories`) ✓ |
| Target PR | #35 — `product/hermes-runtime-adoption-stories` ✓ |
| HERMES-US-001 status | `PUSHED_FOR_REVIEW`, `CHANGES_REQUIRED` per PR #35 comments ✓ |
| HERMES-STORIES-001 status | `IN_PROGRESS` ✓ |
| PR #35 governance CI | FAILING (branch not registered) — fixed by adding HERMES-US-001 entry to registry on this branch ✓ |
| Hermes activated | No ✓ |
| Runtime code modified | No ✓ |
| Sprint plan created | No ✓ |
| Stories marked final/design-ready | No ✓ |

---

## 2. Product Owner Decisions Applied

Three Product Owner comments on PR #35 define the required corrections:

**Comment 1 — RETAIN_DISABLED_BY_DEFAULT**  
Advanced Hermes-derived capabilities must not be described as permanently removed. They remain in the capability model, disabled by default, and may be enabled later by explicit Product Owner or user action from Magna UI, subject to Magna permissions, policy gates, audit, and TRACE requirements.

**Comment 2 — Verdict and Next-Actions Output Split**  
When Magna reviews a worker outcome, output is split into two surfaces:
- Chat/Telegram: short summary only, references TRACE/evidence ID
- GitHub: complete verdict, evidence, next-action suggestions — canonical durable record

**Comment 3 — Strong Internal TRACE**  
TRACE is enforced inside Magna (live internal state), not only in GitHub evidence. Every meaningful Magna action must create or update a TRACE event before the action can proceed. No worker dispatch, evidence write, verdict, continuation, or closure without an active TRACE envelope.

---

## 3. Files Changed

| File | Change type | Corrections applied |
|---|---|---|
| `trace/ACTIVE_WORK_REGISTRY.yaml` | Added 2 new task entries | Added HERMES-US-001 (product story branch, fixes PR #35 governance CI) and HERMES-STORIES-001 (this correction branch) |
| `trace/product/PRODUCT_STORY_INDEX.md` | Major update | Epic statement, capability model section, Primary Flow (13-step), RETAIN_DISABLED_BY_DEFAULT model, Strong Internal TRACE, Non-Goals, Success Criteria, Sprint 1 and Sprint 4 expected outcomes, PO review notes |
| `trace/product/user-stories/MAG-US-HERMES-002-*.md` | Medium update | Activation-gated classification, authorization gates, intake-only restriction, WhatsApp as RETAIN_DISABLED_BY_DEFAULT, out-of-scope real-execution statement |
| `trace/product/user-stories/MAG-US-HERMES-006-*.md` | Medium update | TRACE-linked result state, result states enum, changed files vs. claimed files separation |
| `trace/product/user-stories/MAG-US-HERMES-007-*.md` | Medium update | Evidence from/linked to TRACE envelope, detailed verdict and next-action suggestions, durable-not-replacement rule |
| `trace/product/user-stories/MAG-US-HERMES-008-*.md` | Medium update | Short summary surface rule, TRACE/evidence ID reference requirement, does-not-replace-GitHub rule |
| `trace/product/user-stories/MAG-US-HERMES-009-*.md` | Major rewrite | TRACE rule, internal-not-only-GitHub enforcement, TRACE Event Requirement list (17 events), rewritten user flow, expanded acceptance criteria, backward/forward traceability sections |
| `trace/product/user-stories/MAG-US-HERMES-010-*.md` | Major expansion | Primary Flow section (13-step), local-first orchestration, full user flow expansion, Magna review/verify/verdict/next-actions, RETAIN_DISABLED_BY_DEFAULT capability list, expanded acceptance criteria |

Stories not changed: MAG-US-HERMES-001, 003, 004, 005 — no corrections required by Product Owner comments.

---

## 4. Correction Detail by Story

### MAG-US-HERMES-002 — Telegram Activation-Gated

**Before:** Story described Telegram as an approved channel for remote command intake without noting that real execution is blocked until authorization gates are met. WhatsApp was described as "unless separately approved."

**After:**
- Added "Capability Classification" section explicitly stating Telegram is activation-gated.
- Listed five authorization gates that must be satisfied before real remote-triggered execution: R-06 fixed, messaging re-authorized, sender boundary exists, approval-channel design accepted, TRACE/audit verified.
- Changed WhatsApp to `RETAIN_DISABLED_BY_DEFAULT` (not "unless separately approved").
- Added "Non-Default Capabilities" section listing WhatsApp, multi-channel messaging, and automatic remote-triggered execution as RETAIN_DISABLED_BY_DEFAULT.
- Intake and acknowledgement remain available; execution does not proceed until gates are met.
- User flow step added: Magna queues request for local instruction matching and classification.

### MAG-US-HERMES-006 — Worker Result Capture

**Before:** Story captured worker output and result states but did not produce a TRACE-linked result state, did not specify result state vocabulary, and did not separate changed files from claimed changes.

**After:**
- User flow now assigns a TRACE-linked result state as an explicit step.
- Added "Result States" section with the full vocabulary: COMPLETED, FAILED, PAUSED_FOR_APPROVAL, BLOCKED, NEEDS_REVIEW, TIMED_OUT.
- Acceptance criteria now require: TRACE-linked result state, changed files listed separately from claimed changes, no continuation without a valid result state in the TRACE envelope.

### MAG-US-HERMES-007 — GitHub Evidence

**Before:** Evidence was described without explicitly linking it to the Magna TRACE envelope, without including verdict and next-action suggestions, and without clarifying that it is the durable record (not a replacement for Magna live state).

**After:**
- User value now states GitHub evidence is "generated from or linked to the Magna TRACE envelope."
- User value now clarifies: "GitHub is the canonical durable record; it does not replace Magna's live internal TRACE state — both are required."
- User flow adds: evidence includes detailed verdict and next-action suggestions.
- Acceptance criteria now require: evidence linked to TRACE envelope, includes detailed verdict, includes next-action suggestions, links to TRACE task ID, does not replace Magna live TRACE state.

### MAG-US-HERMES-008 — User Notification

**Before:** Notification was described with short status, evidence reference, and decision required. No rule stated it was a summary surface only or that it must reference a TRACE/evidence ID.

**After:**
- Added "Notification Surface Rule" section: notification is a short summary surface only; must include TRACE/evidence ID; must not replace GitHub durable record.
- User flow updated: notification explicitly references TRACE/evidence ID; user can review full verdict in GitHub before deciding.
- User response is recorded in TRACE envelope.
- Acceptance criteria: notification is short summary only, must include TRACE/evidence reference, does not replace GitHub durable record.

### MAG-US-HERMES-009 — TRACE Traceability

**Before:** Story described TRACE as a GitHub evidence and task-linking requirement. It did not require TRACE enforcement inside Magna itself, did not list required TRACE events, and did not block actions without a TRACE envelope.

**After:**
- User story rewritten to explicitly state "inside Magna itself and in GitHub."
- Added "TRACE Rule" block: "If it happened in Magna, it must be traceable in Magna. If it matters for project history, it must also be durable in GitHub."
- Added "TRACE Event Requirement" section: 17 required TRACE events listed; every event must be created or updated before the corresponding action proceeds.
- Added blocking rule: no worker dispatch, evidence write, verdict, next-action suggestion, continuation, or closure without an active TRACE envelope.
- Added requirement: chat/Telegram summaries reference TRACE/evidence ID.
- Added future-recall requirement: TRACE must support investigation of what triggered a change, why, who did it, which approval allowed it, and what evidence explains later behavior.
- Backward/forward traceability sections updated with specific questions.

### MAG-US-HERMES-010 — End-to-End Continuation

**Before:** Story described a remote-first user flow (user starts task remotely). It did not include the 13-step Product Owner primary flow, did not include Magna review/verify/verdict steps, did not include the output split, and did not list RETAIN_DISABLED_BY_DEFAULT capabilities.

**After:**
- User story rewritten to reflect local Magna-controlled orchestration as the primary flow.
- Added "Primary Flow (Epic 1)" section with the 13-step flow from Product Owner comment.
- User flow expanded to 18 steps covering: TRACE envelope creation, instruction routing, instruction match, classification, worker selection, worker execution, output capture, Magna review, Magna verify, verdict in TRACE, short chat summary, complete GitHub verdict with next-actions, next-actions in TRACE, user wait/approval/redirection.
- Acceptance criteria significantly expanded: covers Magna review, verification, TRACE verdict, short chat summary, complete GitHub verdict, TRACE next-actions, user wait/approval/stop, short summary references TRACE/evidence ID and does not replace GitHub evidence.
- Added "Non-Default Capabilities (RETAIN_DISABLED_BY_DEFAULT)" section listing 10 capabilities.

### PRODUCT_STORY_INDEX.md

**Before:** Epic statement described remote-first flow. Core user outcome described Telegram as the primary entry point. No capability model section, no RETAIN_DISABLED_BY_DEFAULT, no Strong Internal TRACE section.

**After:**
- Epic statement rewritten to reflect local-controlled orchestration with Hermes capabilities behind Magna.
- Added "Capability Model: RETAIN_DISABLED_BY_DEFAULT" section listing 11 non-default capabilities.
- Added "Primary Flow (Epic 1 — Local Magna-Controlled Orchestration First)" section with the 13-step flow.
- Added "Strong Internal TRACE Requirement" section with the TRACE rule.
- Non-Goals updated to include RETAIN_DISABLED_BY_DEFAULT prohibition.
- Success Criteria updated: local instruction, TRACE-linked result state, Magna review, short chat verdict + complete GitHub verdict with next-actions, Telegram activation-gated, RETAIN_DISABLED_BY_DEFAULT not activated.
- Sprint 1 expected outcome: added local instruction intake first; Telegram intake-only until authorization gates.
- Sprint 4 expected outcome: added Magna review, verdict, next-actions, TRACE inside Magna and GitHub, Telegram continuation activation-gated, RETAIN_DISABLED_BY_DEFAULT not activated.
- PO review notes updated to reference PR #35 corrections applied.

---

## 5. PR #35 Governance Validation

**Status before correction:** FAILING

**Cause:** `product/hermes-runtime-adoption-stories` branch had no registered task in `trace/ACTIVE_WORK_REGISTRY.yaml`. The governance CI validator (`check_changed_path_ownership.py`) requires every branch to have exactly one registered active task.

**Fix applied on this correction branch:** Added `HERMES-US-001` task entry to `trace/ACTIVE_WORK_REGISTRY.yaml` with:
- `branch: product/hermes-runtime-adoption-stories`
- `writable_paths: [trace/product/]`
- `status: PUSHED_FOR_REVIEW`

**How fix takes effect:** The governance CI for PR #35 will pass once either: (a) this correction branch is merged to main first (providing the registry entry on main), or (b) the registry entry is applied to the `product/hermes-runtime-adoption-stories` branch directly. The Product Owner must decide the merge order.

Also added `HERMES-STORIES-001` task entry for this correction branch so that this branch's own CI passes.

---

## 6. Stories Not Changed

MAG-US-HERMES-001, 003, 004, and 005 were not changed because no Product Owner comment targeted them. They are directionally correct as-is for the corrections required.

---

## 7. Remaining Open Questions

| # | Question | Story |
|---|---|---|
| OQ-1 | Which sender boundary mechanism is approved for Telegram? (user-ID allow list, token, other) | 002 |
| OQ-2 | What is the first approved demonstration scenario for the end-to-end flow? | 010 |
| OQ-3 | Should task continuation be available from both remote channel and ChatGPT, or one first? | 010 |
| OQ-4 | What is the minimum TRACE envelope view required for Product Owner review? | 009 |
| OQ-5 | Should the user see forward/backward traceability in Command Center UI, GitHub evidence, or both? | 009 |
| OQ-6 | Should RETAIN_DISABLED_BY_DEFAULT capabilities be listed in the Command Center UI even when disabled? | General |
| OQ-7 | PR #33 status — needed for MAG-US-HERMES-001 branding dependency | 001 |

---

## 8. Final Verdict

**ACCEPT_WITH_CORRECTIONS — ready for Product Owner review**

All Product Owner CHANGES_REQUIRED corrections from PR #35 comments have been applied:
- RETAIN_DISABLED_BY_DEFAULT model applied across story 002, story 010, and the story index.
- Telegram activation-gated with five explicit authorization gates.
- Epic 1 local-first 13-step primary flow added to story 010 and index.
- Strong Internal TRACE requirement applied to story 009 (major rewrite), story 006, 007, 008, 010, and index.
- Verdict and next-action output split applied to stories 007, 008, 010, and index.
- PR #35 governance validation fix included (HERMES-US-001 registry entry).

Status of all stories remains `READY_FOR_REFINEMENT`. No stories are marked final or design-ready. No sprint implementation tasks are created. No merge performed. Product Owner review and decision required.

---

## 9. Traceability

| Direction | Links |
|---|---|
| Backward | PR #35 Product Owner CHANGES_REQUIRED comments; `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`; `trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md` (Telegram activation-gated finding, RETAIN_DISABLED_BY_DEFAULT alignment) |
| Forward | Product Owner review of this correction branch; merging corrections into product story branch; remaining open questions resolved; final Product Owner approval of stories; downstream sprint planning |

**Handoff:** `trace/evidence/HERMES-STORIES-001-CLAUDE-HANDOFF.md`, `trace/evidence/HERMES-STORIES-001-CLAUDE-HANDOFF.json`
