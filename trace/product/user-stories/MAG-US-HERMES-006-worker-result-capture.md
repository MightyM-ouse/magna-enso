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

1. Magna starts an approved worker task.
2. The worker produces output or reaches a pause, failure, timeout, or completion state.
3. Magna captures the relevant output and task result.
4. Magna separates worker claims from verified evidence.
5. Magna summarizes the result for the user.
6. User can review the result without manually searching terminal logs.

## Acceptance Criteria

- [ ] Worker stdout/stderr or equivalent output is captured.
- [ ] Changed files are identified where applicable.
- [ ] Worker result is summarized.
- [ ] Worker claims are separated from verified evidence.
- [ ] Failure, timeout, pause, or completion states are recorded.
- [ ] The user can see the result state clearly.
- [ ] The result links back to the originating task ID.

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
