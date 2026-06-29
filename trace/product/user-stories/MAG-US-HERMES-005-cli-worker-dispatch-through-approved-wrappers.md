# MAG-US-HERMES-005 — CLI Worker Dispatch Through Approved Wrappers

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 2 — Worker Dispatch
Capability Area: Agents / Command / Governance Visibility
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to start the correct CLI worker only through approved command wrappers, so that Claude, Codex, or Antigravity work is controlled and traceable.

## User Value

The user can benefit from specialist CLI workers without giving Magna unrestricted terminal autonomy. Worker launch remains bounded, visible, and tied to a task ID and approved instruction.

## User Flow

1. User submits a task that matches a governed known instruction.
2. Magna determines which specialist worker is appropriate for the task type.
3. Magna confirms that the worker can only be started through an approved wrapper.
4. Magna captures worker command details, task ID, start time, and bounded working context.
5. If the worker cannot start safely, Magna reports the failure and pauses.

## Acceptance Criteria

- [ ] Worker selection is based on task type and approved instruction.
- [ ] Only approved wrappers can be launched.
- [ ] Working directory is bounded.
- [ ] Worker command, arguments, start time, and task ID are captured.
- [ ] If the worker cannot start, Magna reports the failure and pauses.
- [ ] The user can identify which worker was selected and why.
- [ ] No arbitrary worker invocation is allowed.

## Out of Scope

- Implementing worker wrapper scripts.
- Creating Claude, Codex, or Antigravity execution task packets.
- Allowing arbitrary terminal execution.
- Starting workers without a matched instruction and permitted classification.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: Known instruction matching story.
- Product dependency: Action classification story.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which worker types are included in the first Product Owner approved wrapper list?
- Should Magna show the wrapper name to the user before worker dispatch?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that worker dispatch is visible, bounded, traceable, and limited to approved wrappers only.
