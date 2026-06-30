# MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 4 — End-to-End TRACE Continuation
Capability Area: Governance Visibility / Task Awareness / Approval Flow
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want every Magna action to create a TRACE event inside Magna itself and produce durable evidence in GitHub, so that I can always trace what happened, why, who did it, what was approved, and what the result was.

## TRACE Rule

```
If it happened in Magna, it must be traceable in Magna.
If it matters for project history, it must also be durable in GitHub.
```

TRACE is enforced **inside Magna** (live internal state), not only in GitHub evidence. GitHub evidence is the durable external record. Both are required. Neither replaces the other.

## User Value

The user can audit Magna work in both directions at any time — including in the future when investigating unexpected behavior, bugs, or results. Backward traceability explains what started the work, which user instruction caused it, which worker implemented it, which approval allowed it, and what evidence explains the current state. Forward traceability explains what is allowed next, what is forbidden, what requires approval, and when Magna must stop and ask the user.

Magna's internal TRACE state supports live recall, debugging, verdict generation, and next-action control. GitHub evidence provides the durable project record.

## TRACE Event Requirement

Every meaningful Magna action must create or update a TRACE event **before** the action can proceed. No worker dispatch, evidence write, verdict, next-action suggestion, continuation, or closure may occur without an active TRACE envelope for the task.

Required TRACE events (minimum):

- User instruction received
- Instruction parsed
- Known instruction matched or not matched
- Action classified (SAFE_KNOWN, GOVERNED_KNOWN, APPROVAL_REQUIRED, BLOCKED_OR_UNKNOWN)
- Worker selected
- Wrapper selected
- Worker execution started
- Worker output captured
- Changed files detected (verified separately from worker-claimed changes)
- Evidence prepared
- GitHub evidence written or proposed
- Magna verification started
- Magna verdict generated
- Next actions suggested
- User approval, redirection, or stop captured
- Continuation allowed or blocked
- Task closed

## User Flow

1. User starts a Magna task (locally or via remote intake).
2. Magna creates a TRACE envelope for the task before any other action.
3. Magna records a TRACE event for every meaningful action as the task progresses.
4. Every worker action links to the originating TRACE task ID and instruction.
5. Every result is recorded in the TRACE envelope with a result state.
6. Every next step receives an allowed, blocked, or approval-required state in the TRACE envelope.
7. When evidence is written to GitHub, it links back to the Magna TRACE task ID.
8. When a notification or chat summary is sent, it references the TRACE/evidence ID.
9. Magna does not mark the task complete until TRACE evidence exists internally and is linked to GitHub evidence.

## Acceptance Criteria

- [ ] Every task has a TRACE envelope created before any action proceeds.
- [ ] Every meaningful Magna action creates or updates a TRACE event before the action can proceed.
- [ ] No worker dispatch, evidence write, verdict, next-action suggestion, continuation, or closure can occur without an active TRACE envelope.
- [ ] TRACE events cover the full required list (see TRACE Event Requirement above).
- [ ] Every worker action links to the originating TRACE task ID.
- [ ] Every result is linked to a TRACE result state.
- [ ] Every next step has an allowed, blocked, or approval-required state in the TRACE envelope.
- [ ] No task can be marked complete without TRACE evidence internally and linked GitHub evidence.
- [ ] GitHub evidence links back to the Magna TRACE task ID.
- [ ] Chat and Telegram summaries reference the TRACE/evidence ID.
- [ ] TRACE supports future recall and debugging: what triggered a change, why it was done, which worker did it, which approval allowed it, and what evidence explains later behavior or defects.
- [ ] The minimum TRACE envelope view is available and exposes all required fields (trace_id, task_id, user_request, created_at, current_status, instruction_source, matched_instruction_id or unmatched_reason, action_classification, selected_worker, wrapper_id, branch/worktree context, files_changed, evidence_path, github_pr_or_issue_reference, worker_claims, verified_evidence, magna_verdict, next_recommended_actions, approval_status, approved_by or pending_user_decision, stop_condition, continuation_state, full event timeline).
- [ ] Forward and backward traceability is visible in both Magna Command Center UI (live) and GitHub (durable).
- [ ] Chat and Telegram surfaces show short summaries with TRACE/evidence references only — they do not show the full TRACE view.

## Minimum TRACE Envelope View

The minimum required TRACE envelope view for Product Owner review must expose the following fields:

| Field | Description |
|---|---|
| `trace_id` | Unique identifier for this TRACE instance |
| `task_id` | Associated Magna task ID |
| `user_request` | Original user instruction or remote command |
| `created_at` | Timestamp when TRACE envelope was created |
| `current_status` | Current result state of the task |
| `instruction_source` | Local Magna / chat, or remote channel (Telegram) |
| `matched_instruction_id` | Known instruction matched, or `unmatched_reason` if not matched |
| `action_classification` | SAFE_KNOWN / GOVERNED_KNOWN / APPROVAL_REQUIRED / BLOCKED_OR_UNKNOWN |
| `selected_worker` | Worker selected (Claude / Codex / other) |
| `wrapper_id` | Approved command wrapper used |
| `branch_or_worktree_context` | Branch or worktree where work occurred (where applicable) |
| `files_changed` | Files changed, verified independently from worker claims |
| `evidence_path` | Path to GitHub evidence file(s) |
| `github_pr_or_issue_reference` | GitHub PR or issue number linked to this task |
| `worker_claims` | What the worker reported as its output |
| `verified_evidence` | What Magna independently verified |
| `magna_verdict` | Magna's verdict on the task outcome |
| `next_recommended_actions` | Next actions suggested by Magna |
| `approval_status` | Approved / pending user decision / rejected |
| `approved_by_or_pending` | Who approved, or indication of pending user decision |
| `stop_condition` | Condition that caused or will cause Magna to stop and wait |
| `continuation_state` | What next step is allowed, blocked, or requires approval |
| `event_timeline` | Full ordered list of TRACE events from envelope creation to current state |

The view must be able to answer:
- What triggered this change?
- Why was it done?
- Who or which worker did it?
- What files changed?
- What evidence proves it?
- What approval allowed continuation?
- What next action is allowed or blocked?
- What could explain a later bug or unexpected behavior?

## Traceability Visibility

TRACE forward and backward traceability must be visible in **both**:

1. **Magna Command Center UI** — as a live task/TRACE view showing current state, event timeline, verdict, and next-action status.
2. **GitHub** — as durable evidence linked to the Magna TRACE task ID.

Chat and Telegram surfaces show **short summaries with TRACE/evidence references only**. They do not show the full TRACE view.

## Backward Traceability

Backward traceability must be able to answer:

- What user instruction or remote command started this task?
- Which TRACE task ID was created?
- Which known instruction was matched?
- Which action classification was assigned?
- Which worker was selected and why?
- Which command wrapper was used?
- What files were changed (verified, not only claimed)?
- What evidence proves the result?
- Who approved continuation?

## Forward Traceability

Forward traceability must be able to answer:

- What is the next allowed action?
- Who or what may perform it?
- What is forbidden?
- What evidence must be produced before proceeding?
- When must Magna stop and ask the user?

## Out of Scope

- Implementing TRACE storage or envelope mechanics.
- Creating technical traceability tasks.
- Replacing Magna TRACE with Hermes runtime logs.
- Marking tasks complete without TRACE evidence.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: GitHub assessment and evidence update story.
- Product dependency: User notification and approval loop story.
- Product dependency: CLI worker dispatch and worker result capture stories.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

None — all open questions resolved by Product Owner on 2026-06-30.

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that each remote task has durable forward and backward traceability and cannot be completed without evidence.
