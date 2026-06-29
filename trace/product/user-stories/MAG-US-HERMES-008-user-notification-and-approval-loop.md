# MAG-US-HERMES-008 — User Notification and Approval Loop

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 3 — Evidence and Approval Loop
Capability Area: Approval Flow / Task Awareness / Command
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to notify me when a task completes, pauses, or needs approval, so that I can decide the next step remotely or through ChatGPT.

## User Value

The user stays in control of remote and worker-backed work. Magna can report status and ask for decisions, but it does not continue approval-required work without the user’s explicit response.

## User Flow

1. A task completes, pauses, fails, or reaches an approval-required point.
2. Magna sends a clear notification to the user.
3. Notification includes short status, evidence reference, and required decision.
4. User approves, rejects, requests clarification, or redirects the next step.
5. Magna continues only when the next step is allowed and approved where required.

## Acceptance Criteria

- [ ] Magna sends a clear notification after task completion, pause, failure, or approval requirement.
- [ ] Notification includes short status, evidence link/reference, and decision needed.
- [ ] User can approve, reject, request clarification, or redirect next step.
- [ ] Magna does not continue approval-required work until approval is received.
- [ ] The user can understand the current task state from the notification.
- [ ] Approval, rejection, clarification, or redirection is recorded as part of the task lifecycle.

## Out of Scope

- Implementing notification transport mechanics.
- Defining every remote approval UI.
- Automatically continuing blocked or unknown work.
- Creating future schedulers or reminders.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: GitHub assessment and evidence update story.
- Product dependency: Action classification story.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which notification channel should be used first for approval decisions?
- Should approvals expire after a time window?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that notifications are clear, decision-oriented, linked to evidence, and prevent approval-required work from continuing without user approval.
