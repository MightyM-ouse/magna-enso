# Product Story Index

Status: READY_FOR_REFINEMENT
Purpose: Product Owner review index for formal Magna product user stories.
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

---

## Epic

### EPIC: Magna-Hermes Runtime Adoption

As a Magna user, I want selected Hermes runtime capabilities to operate behind the Magna Enso experience, so that I can remotely initiate, monitor, approve, and continue governed agent work while preserving TRACE-based forward and backward traceability.

## Product Value

This epic allows Magna to become a practical command environment without rebuilding every runtime capability from scratch.

Hermes may provide runtime strengths such as terminal access, messaging gateway, memory, skills, profiles, scheduling, delegation, and tool execution.

Magna provides the governed user experience, safety boundaries, traceability, approval model, GitHub evidence, ChatGPT system-architect workflow, and Product Owner control.

## Core User Outcome

The user can start a governed task from Telegram or another approved remote channel. Magna receives it, checks whether the task matches known instructions, dispatches the correct CLI worker when allowed, captures the result, writes evidence or assessment to GitHub, notifies the user, and waits for approval when required.

## Non-Goals

- Do not replace Magna with Hermes.
- Do not allow unrestricted terminal autonomy.
- Do not allow arbitrary worker invocation.
- Do not bypass TRACE.
- Do not merge PRs, delete branches, force push, install software, or expose remote access automatically.
- Do not start with full self-improving autonomy.
- Do not treat Hermes profiles as security sandboxes.

## Success Criteria

- Magna-branded Hermes runtime can receive a remote command.
- Commands are classified as known-safe, governed, unknown, approval-required, or blocked.
- Approved CLI workers can be launched only through predefined wrappers.
- Worker output is captured and linked to a TRACE task ID.
- GitHub receives assessment/evidence updates.
- User receives notification and can approve or redirect next steps.
- Unknown/risky actions pause automatically.
- Every action can be traced backward to the user request and forward to the next allowed action.

---

## User Stories

| Story ID | Title | Sprint Group | Status | File |
|---|---|---|---|---|
| MAG-US-HERMES-001 | Magna-Branded Hermes Runtime Identity | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-001-magna-branded-hermes-runtime-identity.md` |
| MAG-US-HERMES-002 | Remote Command Intake from Telegram or Approved Channel | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-002-remote-command-intake-from-approved-channel.md` |
| MAG-US-HERMES-003 | Known Instruction Matching | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-003-known-instruction-matching.md` |
| MAG-US-HERMES-004 | Safe, Governed, Unknown, and Blocked Action Classification | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-004-safe-governed-unknown-and-blocked-action-classification.md` |
| MAG-US-HERMES-005 | CLI Worker Dispatch Through Approved Wrappers | Sprint 2 — Worker Dispatch | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-005-cli-worker-dispatch-through-approved-wrappers.md` |
| MAG-US-HERMES-006 | Worker Result Capture | Sprint 2 — Worker Dispatch | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-006-worker-result-capture.md` |
| MAG-US-HERMES-007 | GitHub Assessment and Evidence Update | Sprint 3 — Evidence and Approval Loop | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-007-github-assessment-and-evidence-update.md` |
| MAG-US-HERMES-008 | User Notification and Approval Loop | Sprint 3 — Evidence and Approval Loop | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-008-user-notification-and-approval-loop.md` |
| MAG-US-HERMES-009 | TRACE Forward and Backward Traceability Enforcement | Sprint 4 — End-to-End TRACE Continuation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-009-trace-forward-and-backward-traceability-enforcement.md` |
| MAG-US-HERMES-010 | End-to-End Governed Task Continuation | Sprint 4 — End-to-End TRACE Continuation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-010-end-to-end-governed-task-continuation.md` |

---

## Four-Sprint Grouping

This is a product-level grouping only. It must not be converted into technical implementation tasks until the Product Owner approves the formal user stories.

### Sprint 1 — Control Foundation

Goal: prove that Magna/Hermes can receive a command, classify it, and stop safely.

Stories:

- MAG-US-HERMES-001 — Magna-Branded Hermes Runtime Identity
- MAG-US-HERMES-002 — Remote Command Intake from Telegram or Approved Channel
- MAG-US-HERMES-003 — Known Instruction Matching
- MAG-US-HERMES-004 — Safe, Governed, Unknown, and Blocked Action Classification

Expected outcome:

Remote command intake works in a controlled mode. Magna can respond accepted, needs approval, unknown, or blocked. Risky execution is not allowed.

### Sprint 2 — Worker Dispatch

Goal: prove that Magna can start a specialist CLI worker safely through approved wrappers.

Stories:

- MAG-US-HERMES-005 — CLI Worker Dispatch Through Approved Wrappers
- MAG-US-HERMES-006 — Worker Result Capture

Expected outcome:

Magna can start a predefined Claude/Codex/Antigravity-style worker task, capture the outcome, and stop safely.

### Sprint 3 — Evidence and Approval Loop

Goal: prove that completed or paused work becomes reviewable and user-controlled.

Stories:

- MAG-US-HERMES-007 — GitHub Assessment and Evidence Update
- MAG-US-HERMES-008 — User Notification and Approval Loop

Expected outcome:

Magna can update GitHub with assessment/evidence and notify the user for the next decision.

### Sprint 4 — End-to-End TRACE Continuation

Goal: prove the complete governed remote task loop.

Stories:

- MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement
- MAG-US-HERMES-010 — End-to-End Governed Task Continuation

Expected outcome:

A full remote-controlled Magna task can run from user request to worker execution, evidence, notification, approval, continuation, and closure while preserving TRACE.

---

## Product Owner Review Notes

- These are formal product stories only.
- Sprint implementation tasks are not created yet.
- Technical subtasks are not created yet.
- Downstream design, architecture, frontend, backend, agent, validation, and governance work must be created only after Product Owner approval.
- PR #33 remains a branding dependency referenced by the source brief.
