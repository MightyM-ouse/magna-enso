# MAG-US-HERMES-010 — End-to-End Governed Task Continuation

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 4 — End-to-End TRACE Continuation
Capability Area: Command / Agents / Approval Flow / Task Awareness
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to continue a task after my approval or redirection, so that multi-step work can progress without losing context or traceability.

## User Value

The user can move from remote request to governed worker execution, evidence, notification, approval, continuation, and closure while remaining in control. Multi-step work can continue, but only inside the approved next envelope.

## User Flow

1. User starts a task remotely.
2. Magna classifies the request and dispatches a known worker task when allowed.
3. Magna captures the worker result.
4. Magna writes or proposes evidence in GitHub.
5. Magna notifies the user of the status and required decision.
6. User approves, rejects, clarifies, or redirects.
7. Magna continues only within the approved next envelope.
8. Full lifecycle remains TRACE-compliant.

## Acceptance Criteria

- [ ] User can start a task remotely.
- [ ] Magna can classify and dispatch a known worker task.
- [ ] Worker result is captured.
- [ ] Evidence is written to GitHub.
- [ ] User is notified.
- [ ] User can approve or redirect.
- [ ] Magna continues only within the approved next envelope.
- [ ] Full lifecycle remains TRACE-compliant.
- [ ] Magna stops when the next requested action is unknown, blocked, or outside approval.

## Out of Scope

- Full self-improving autonomy.
- Unrestricted terminal autonomy.
- Arbitrary worker invocation.
- Automatic merge to main, force push, branch deletion, software installation, or remote-access exposure.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: All Sprint 1, Sprint 2, and Sprint 3 stories in the Magna-Hermes Runtime Adoption epic.
- Product dependency: TRACE forward and backward traceability enforcement story.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- What is the first approved end-to-end demonstration scenario for Product Owner review?
- Should task continuation be available from both remote channel and ChatGPT, or one first?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm the complete governed loop from remote request to continuation while preserving user approval and TRACE evidence.
