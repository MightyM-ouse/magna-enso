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

## User Value

The user can start governed Magna work remotely without opening the local UI first. The value is convenience with control: remote intake creates a task request and acknowledgement, but unsupported or ambiguous commands are not executed automatically.

## User Flow

1. User sends a message from Telegram or another approved channel.
2. Magna receives the message as a remote task request.
3. Magna parses the message into a proposed task request.
4. Magna assigns a unique task/session identifier.
5. Magna acknowledges receipt back to the user.
6. If the command is unsupported or ambiguous, Magna does not execute it and asks for clarification or reports that it is unsupported.

## Acceptance Criteria

- [ ] Magna can receive a remote message from an approved channel.
- [ ] The message is parsed into a task request.
- [ ] The request receives a unique task/session identifier.
- [ ] The request is acknowledged back to the user.
- [ ] Unsupported commands are not executed.
- [ ] Ambiguous commands are not executed and require clarification.
- [ ] The user can see whether the remote command was received, rejected, or needs clarification.

## Out of Scope

- Supporting every messaging provider.
- WhatsApp support unless separately approved.
- Executing arbitrary remote commands.
- Creating worker dispatch implementation tasks.
- Creating sprint implementation tasks or technical subtasks.

## Dependencies

- Product dependency: Approved remote channel decision, Telegram first per source brief.
- Product dependency: User identity / approved sender boundary.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which channel is approved first for Product Owner review: Telegram only, or Telegram plus another channel?
- What message wording should Magna use for acknowledgement, unsupported request, and clarification?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that a remote request can be received and acknowledged without allowing unsupported or ambiguous commands to execute.
