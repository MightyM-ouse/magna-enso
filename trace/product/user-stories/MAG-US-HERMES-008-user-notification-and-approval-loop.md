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

The user stays in control of remote and worker-backed work. Magna reports task status through a concise notification and waits for the user’s decision. The notification is a short summary surface only — it references the TRACE/evidence ID so the user can review the full durable record in GitHub before deciding. Magna does not continue approval-required work without the user’s explicit response.

## Notification Surface Rule

Notifications (in chat, and later Telegram) are a **short summary surface only**. They must:

- Be concise and decision-oriented.
- Include the TRACE/evidence ID or a direct reference to the GitHub evidence so the user knows where to find the full record.
- Not replace the detailed verdict or next-action suggestions, which belong in GitHub evidence (see MAG-US-HERMES-007).

The detailed verdict, evidence, changed-file summary, risk notes, and recommended next actions are written to GitHub. The chat or Telegram notification provides a short summary and a reference to that GitHub record.

## User Flow

1. A task completes, pauses, fails, or reaches an approval-required point.
2. Magna sends a concise notification to the user (in chat session first; later via Telegram when activation-gated).
3. Notification includes: short task status, TRACE/evidence ID or GitHub evidence reference, and the decision required.
4. User can review the full verdict and next-action suggestions in GitHub evidence before deciding.
5. User approves, rejects, requests clarification, or redirects the next step.
6. Magna records the user response in the TRACE envelope.
7. Magna continues only when the next step is allowed and approved where required.

## Acceptance Criteria

- [ ] Magna sends a concise notification after task completion, pause, failure, or approval requirement.
- [ ] Notification is a short summary only — it does not contain the full verdict or evidence.
- [ ] Notification includes TRACE/evidence ID or GitHub evidence reference so the user can access the full record.
- [ ] Notification includes the decision required.
- [ ] User can approve, reject, request clarification, or redirect next step.
- [ ] Magna does not continue approval-required work until approval is received.
- [ ] The user can understand the current task state from the notification and find the full evidence in GitHub.
- [ ] Approval, rejection, clarification, or redirection is recorded in the Magna TRACE envelope as part of the task lifecycle.
- [ ] Notification does not replace durable GitHub verdict and evidence (see MAG-US-HERMES-007).

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
