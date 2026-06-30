# MAG-US-HERMES-006 — Worker Result Capture

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 2 — Worker Dispatch
Capability Area: Agents / Task Awareness / Governance Visibility
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to capture worker output and task results, so that I can review what happened without manually searching terminal logs.

## User Value

The user can understand what a worker did, what it claimed, what evidence exists, and whether the task completed, failed, timed out, or paused. This makes worker activity reviewable and prevents blind trust in terminal output.

## User Flow

1. Magna starts an approved worker task with an active TRACE envelope.
2. The worker produces output or reaches a pause, failure, timeout, completion, or blocked state.
3. Magna captures the relevant output and task result.
4. Magna assigns a TRACE-linked result state to the task (see result states below).
5. Magna separates worker claims from verified evidence.
6. Magna records changed files separately from claimed changes (what the worker reported vs. what Magna can verify).
7. Magna summarizes the result for the user, linked to the TRACE task ID and result state.
8. User can review the result without manually searching terminal logs.

## Result States

Every captured worker result must be assigned one of the following TRACE-linked result states:

- `COMPLETED` — worker finished within scope; output captured; evidence ready.
- `FAILED` — worker exited with error; output captured; failure reason recorded.
- `PAUSED_FOR_APPROVAL` — worker paused awaiting user or Product Owner decision.
- `BLOCKED` — worker could not proceed due to policy, classification, or missing prerequisite.
- `NEEDS_REVIEW` — worker output requires Magna or user review before next action.
- `TIMED_OUT` — worker exceeded time limit; partial output captured; task paused.

## Acceptance Criteria

- [ ] Worker stdout/stderr or equivalent output is captured.
- [ ] A TRACE-linked result state is assigned to the task (COMPLETED, FAILED, PAUSED_FOR_APPROVAL, BLOCKED, NEEDS_REVIEW, or TIMED_OUT).
- [ ] Changed files are listed separately from claimed changes (verified vs. worker-reported).
- [ ] Worker result is summarized.
- [ ] Worker claims are separated from verified evidence.
- [ ] Failure, timeout, blocked, needs-review, paused, or completion states are recorded.
- [ ] The user can see the result state clearly.
- [ ] The result links back to the originating TRACE task ID.
- [ ] No continuation or next action can be triggered without a valid result state recorded in the TRACE envelope.

## Out of Scope

- Implementing terminal capture mechanisms.
- Validating every worker claim in this story.
- Creating review packages.
- Continuing the task after result capture.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: CLI worker dispatch through approved wrappers story.
- Product dependency: TRACE task identity.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- What level of raw output should be shown to the user by default?
- Should sensitive output be redacted before display or only before persistence?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that worker output is captured, understandable, linked to task identity, and clearly separated from verified evidence.
