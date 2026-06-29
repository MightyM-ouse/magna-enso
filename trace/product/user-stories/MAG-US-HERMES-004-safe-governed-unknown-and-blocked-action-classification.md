# MAG-US-HERMES-004 — Safe, Governed, Unknown, and Blocked Action Classification

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 1 — Control Foundation
Capability Area: Governance Visibility / Approval Flow / Task Awareness
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to classify each requested action by risk level, so that safe work can continue while risky or unknown work requires approval.

## User Value

The user gets a visible safety boundary for remote and runtime actions. Safe known work may continue, governed known work must match predefined instructions, approval-required work pauses for the user, and blocked or unknown work does not execute.

## User Flow

1. User sends or triggers a requested action.
2. Magna classifies the requested action before execution.
3. Magna assigns one of the agreed classes: SAFE_KNOWN, GOVERNED_KNOWN, APPROVAL_REQUIRED, or BLOCKED_OR_UNKNOWN.
4. Magna proceeds, pauses, or blocks according to the classification.
5. Magna shows the user the classification outcome and required next decision when applicable.

## Acceptance Criteria

- [ ] Every requested action receives a safety classification.
- [ ] SAFE_KNOWN actions may proceed automatically.
- [ ] GOVERNED_KNOWN actions require a matching predefined instruction.
- [ ] APPROVAL_REQUIRED actions pause for user confirmation.
- [ ] BLOCKED_OR_UNKNOWN actions do not execute.
- [ ] The user can see why an action was allowed, paused, or blocked.
- [ ] The classification is recorded as part of task evidence.

## Out of Scope

- Implementing the classification engine.
- Defining every possible command or action rule in this story.
- Allowing arbitrary shell commands.
- Merge, force-push, branch deletion, software installation, or automatic remote-access exposure.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: Known instruction matching story.
- Product dependency: Remote command intake story.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which example actions should be included in the first Product Owner approved classification table?
- Should the user see the classification before every action or only when an action pauses or blocks?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that all requested actions receive a visible classification and that approval-required, unknown, or blocked actions do not execute without permission.
