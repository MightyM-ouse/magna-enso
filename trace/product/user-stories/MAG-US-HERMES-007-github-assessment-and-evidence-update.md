# MAG-US-HERMES-007 — GitHub Assessment and Evidence Update

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 3 — Evidence and Approval Loop
Capability Area: Governance Visibility / Task Awareness
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to write task assessment and evidence to GitHub, so that project state remains durable, reviewable, and TRACE-compliant.

## User Value

The user can rely on GitHub as the durable project record for remote Magna work. Evidence captures what was requested, what instruction was used, what worker ran, what happened, what risks exist, and what decision is required next.

## User Flow

1. A remote or worker-backed Magna task reaches a result, pause, failure, or approval point.
2. Magna prepares a task assessment and evidence record.
3. Magna writes or proposes the evidence in GitHub.
4. Magna links the GitHub update to the task lifecycle.
5. User can review durable evidence before deciding the next step.

## Acceptance Criteria

- [ ] Magna writes or proposes a task evidence file.
- [ ] Evidence includes task ID, user request, instruction source, worker, action taken, result, risks, and next decision.
- [ ] GitHub update is linked to the task lifecycle.
- [ ] Unknown or risky cases include an assessment explaining why approval is needed.
- [ ] Evidence format supports later review package generation.
- [ ] The user can understand what happened and what decision is required from the evidence.

## Out of Scope

- Implementing GitHub write mechanics.
- Creating review package generation tasks.
- Automatically merging pull requests.
- Automatically deleting branches or force-pushing.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: Worker result capture story.
- Product dependency: TRACE evidence lifecycle.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Should evidence be written directly, proposed through PR, or saved in a local pending evidence state first?
- What minimum evidence fields are required before a task can be considered reviewable?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that evidence is durable, task-linked, understandable, and sufficient for Product Owner review and next-step decision.
