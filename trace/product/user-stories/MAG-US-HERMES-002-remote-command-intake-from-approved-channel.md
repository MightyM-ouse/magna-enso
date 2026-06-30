# MAG-US-HERMES-002 — Remote Command Intake from Telegram or Approved Channel

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 1 — Control Foundation
Capability Area: Command / Task Awareness
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want to send a task command from Telegram or another approved channel, so that I can initiate Magna work while away from the laptop.

## Capability Classification

Telegram remote command intake: **activation-gated**.

Real remote-triggered execution remains blocked until all of the following authorization gates are satisfied:

1. R-06 runtime policy chokepoint is fixed and verified.
2. Messaging gateway surface is explicitly re-authorized by Product Owner.
3. An approved sender boundary exists.
4. An authenticated approval-channel design is accepted.
5. TRACE evidence and audit for the messaging surface are verified.

Until those gates are satisfied, Telegram may only be used for intake reporting (receiving and acknowledging commands) and short status notifications. It does not trigger actual worker execution.

## User Value

The user can initiate governed Magna work remotely from an approved channel. The value is convenience with control: remote intake creates a task request and acknowledgement, but execution does not begin until Magna's local classification, instruction matching, and policy gates are satisfied. Telegram is the candidate first channel; it is activation-gated and intake-only until the authorization gates above are complete.

## User Flow

1. User sends a message from Telegram (candidate first channel, activation-gated) or another approved channel.
2. Magna receives the message as a remote task request (intake only; no execution yet).
3. Magna parses the message into a proposed task request.
4. Magna assigns a unique task/session identifier and creates a TRACE envelope.
5. Magna acknowledges receipt back to the user (short acknowledgement only).
6. Magna queues the request for local instruction matching and classification on the next local Magna session.
7. If the command is unsupported or ambiguous, Magna does not execute it and reports that it is unsupported or needs clarification.
8. Until all authorization gates are met, Magna does not trigger worker dispatch or execution from the remote channel.

## Acceptance Criteria

- [ ] Magna can receive a remote message from an approved channel (Telegram first, activation-gated).
- [ ] The message is parsed into a task request.
- [ ] The request receives a unique task/session identifier.
- [ ] A TRACE envelope is created for the task.
- [ ] The request is acknowledged back to the user with a short intake-only confirmation.
- [ ] Unsupported commands are not executed.
- [ ] Ambiguous commands are not executed and require clarification.
- [ ] The user can see whether the remote command was received, rejected, or needs clarification.
- [ ] Remote intake does not trigger worker execution until all authorization gates are satisfied (R-06 fixed, messaging re-authorized, sender boundary exists, approval-channel design accepted, TRACE/audit verified).
- [ ] The intake channel cannot be used to bypass Magna instruction matching, classification, or approval requirements.

## Non-Default Capabilities (RETAIN_DISABLED_BY_DEFAULT)

The following related capabilities are part of the Magna capability model but disabled by default in Magna version enso. They may be enabled later by explicit Product Owner or user action through Magna UI, subject to Magna permissions, policy gates, audit, and TRACE requirements:

- **WhatsApp** — additional messaging channel; disabled by default; not part of Epic 1.
- **Multi-channel messaging fanout** — disabled by default.
- **Automatic remote-triggered execution without local confirmation** — disabled by default.

## Out of Scope

- Supporting every messaging provider in Epic 1.
- Real remote-triggered worker execution until authorization gates are satisfied (see above).
- Bypassing Magna instruction matching or policy classification.
- Executing arbitrary remote commands.
- Creating worker dispatch implementation tasks.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: Approved remote channel decision; Telegram first, activation-gated.
- Product dependency: User identity and approved sender boundary (required authorization gate).
- Product dependency: R-06 runtime policy chokepoint fix (required authorization gate).
- Product dependency: Authenticated approval-channel design (required authorization gate).
- Architecture dependency: Not created yet.
- Governance dependency: Messaging gateway re-authorization decision required.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which channel is approved first: Telegram only, or Telegram plus another channel?
- What message wording should Magna use for intake acknowledgement, unsupported request, and clarification?
- What sender boundary mechanism is approved for Telegram? (user-ID allow list, token, or other)

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that a remote request can be received and acknowledged without allowing unsupported or ambiguous commands to execute, and that worker execution is not triggered until all authorization gates are satisfied.
