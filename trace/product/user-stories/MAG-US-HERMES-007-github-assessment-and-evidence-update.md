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

The user can rely on GitHub as the durable project record for Magna work. GitHub evidence is generated from the Magna internal TRACE envelope and captures the complete task story: what was requested, what instruction was used, what worker ran, what happened, what the verdict is, what risks exist, and what the recommended next actions are. GitHub is the canonical durable record; it does not replace Magna's live internal TRACE state — both are required.

## User Flow

1. A Magna task reaches a result, pause, failure, or approval point. The Magna TRACE envelope already records this state internally.
2. Magna prepares a task assessment and evidence record generated from or linked to the Magna TRACE envelope.
3. Evidence includes the detailed verdict and next-action suggestions (not only a status flag).
4. Magna writes or proposes the evidence in GitHub.
5. Magna links the GitHub evidence to the TRACE task ID.
6. User can review durable evidence before deciding the next step.
7. GitHub evidence serves as the canonical durable record; Magna live TRACE state remains the authoritative in-session state.

## Acceptance Criteria

- [ ] Magna writes or proposes a task evidence file.
- [ ] Evidence is generated from or explicitly linked to the Magna internal TRACE envelope.
- [ ] Evidence includes task ID, user request, instruction source, worker, action taken, result state, changed files, risks, and next decision.
- [ ] Evidence includes a detailed verdict explaining what was verified, what was not verified, and what requires further action.
- [ ] Evidence includes next-action suggestions: what the user or Product Owner may do next, what is allowed, what requires approval, and what is blocked.
- [ ] GitHub update is linked to the TRACE task ID so the evidence can be matched to the live task.
- [ ] Unknown or risky cases include an assessment explaining why approval is needed.
- [ ] Evidence format supports later review package generation.
- [ ] GitHub evidence is the durable record; it does not replace Magna's live internal TRACE state.
- [ ] The user can understand what happened, what the verdict is, and what decision is required from the evidence.

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
