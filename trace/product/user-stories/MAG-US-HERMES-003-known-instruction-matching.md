# MAG-US-HERMES-003 — Known Instruction Matching

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 1 — Control Foundation
Capability Area: Command / Governance Visibility / Approval Flow
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to check whether my remote command matches a known approved instruction, so that only predefined and governed workflows can proceed automatically.

## User Value

The user can trust that remote commands do not become open-ended automation. Magna proceeds only when a request matches a known governed instruction, and pauses unknown requests for clarification or approval.

## User Flow

1. User sends a remote command.
2. Magna compares the request against a known instruction registry.
3. Magna identifies whether the request matches a predefined instruction.
4. Magna informs the user whether the request was accepted, rejected, paused, or needs clarification.
5. Magna records the match result as part of task evidence.

## Acceptance Criteria

- [ ] Magna checks remote commands against a known instruction registry.
- [ ] Matching commands can proceed according to their safety class.
- [ ] Unknown commands are paused and escalated.
- [ ] The match result is recorded in task evidence.
- [ ] The user is informed whether the command was accepted, rejected, or needs clarification.
- [ ] A command cannot proceed automatically without a known instruction match and allowed safety class.

## Out of Scope

- Building the instruction registry implementation.
- Creating new instructions from remote messages automatically.
- Allowing unknown commands to run.
- Creating technical subtasks or sprint implementation tasks.

## Dependencies

- Product dependency: Known instruction registry concept.
- Product dependency: Remote command intake story.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- What should be the first approved instruction set for Product Owner review?
- Should Magna show the matched instruction name to the user before proceeding?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that known instructions are recognized, unknown commands are paused, and the user receives a clear match decision.
