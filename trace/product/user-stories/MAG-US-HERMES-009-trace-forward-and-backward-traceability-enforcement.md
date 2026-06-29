# MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 4 — End-to-End TRACE Continuation
Capability Area: Governance Visibility / Task Awareness / Approval Flow
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want every remote task action to follow TRACE, so that I can trace from original request to final result and from each instruction to the next allowed action.

## User Value

The user can audit Magna work in both directions. Backward traceability explains what started the work, which instruction and worker were used, what changed, and who approved continuation. Forward traceability explains what may happen next, who may do it, what is forbidden, and when Magna must stop.

## User Flow

1. User starts a remote or governed runtime task.
2. Magna creates a TRACE envelope for the task.
3. Every worker action links to the originating task and instruction.
4. Every result links to evidence.
5. Every next step receives an allowed, blocked, or approval-required state.
6. Magna does not mark the task complete until trace evidence exists.

## Acceptance Criteria

- [ ] Every task has a TRACE envelope.
- [ ] Every worker action links to the originating task.
- [ ] Every result links to evidence.
- [ ] Every next step has an allowed, blocked, or approval-required state.
- [ ] No task can be marked complete without trace evidence.
- [ ] Backward traceability can answer what user request started the task, which task ID was created, which GitHub instruction was used, which worker ran, which command wrapper was used, what files changed, what evidence proves the result, and who approved continuation.
- [ ] Forward traceability can answer the next allowed action, who or what may perform it, what is forbidden, what evidence must be produced, and when Magna must stop and ask the user.

## Out of Scope

- Implementing TRACE storage or envelope mechanics.
- Creating technical traceability tasks.
- Replacing TRACE with Hermes runtime logs.
- Marking tasks complete without evidence.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: GitHub assessment and evidence update story.
- Product dependency: User notification and approval loop story.
- Product dependency: CLI worker dispatch and worker result capture stories.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- What is the minimum TRACE envelope view required for Product Owner review?
- Should the user see forward/backward traceability in the Command Center UI, GitHub evidence, or both?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that each remote task has durable forward and backward traceability and cannot be completed without evidence.
