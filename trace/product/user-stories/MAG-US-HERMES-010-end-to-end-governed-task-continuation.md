# MAG-US-HERMES-010 — End-to-End Governed Task Continuation

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 4 — End-to-End TRACE Continuation
Capability Area: Command / Agents / Approval Flow / Task Awareness
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Magna to orchestrate a full governed task from my instruction to worker execution, evidence, verdict, next-action suggestion, and continuation, so that multi-step work can progress with full traceability and without losing context or requiring me to track state manually.

## Primary Flow (Epic 1)

Epic 1 prioritizes **local Magna-controlled orchestration first**. Remote Telegram continuation is a later activation-gated addition to the same flow.

The Epic 1 primary flow is:

```
1.  User starts Magna.
2.  User gives instruction to Magna.
3.  Magna understands and routes the instruction.
4.  Magna checks for a known instruction match.
5.  Magna classifies the action.
6.  Magna calls Claude or Codex according to approved worker policy.
7.  Claude or Codex performs the task.
8.  Worker output and evidence are written or proposed in GitHub.
9.  Magna reviews worker changes and evidence.
10. Magna verifies the task outcome.
11. Magna provides a short verdict summary in chat (later, activation-gated, also in Telegram).
12. Magna writes or proposes the complete verdict and next-action suggestions in GitHub.
13. Magna summarizes recommended next actions and waits for user approval, redirection, or stop.
```

## User Value

The user can give an instruction, watch Magna handle the governed workflow end-to-end, receive a verdict, see the recommended next actions, and decide what happens next. Multi-step work continues only inside the approved next envelope. The user never needs to manually track what the worker did, what changed, or what comes next — Magna manages, records, and reports all of that.

## User Flow

1. User starts Magna locally and gives an instruction.
2. Magna creates a TRACE envelope for the task.
3. Magna understands and routes the instruction to instruction matching.
4. Magna checks whether the instruction matches a known governed instruction.
5. Magna classifies the action (SAFE_KNOWN, GOVERNED_KNOWN, APPROVAL_REQUIRED, or BLOCKED_OR_UNKNOWN).
6. Magna selects the appropriate worker (Claude or Codex) according to approved worker policy.
7. Magna launches the worker through an approved wrapper with bounded scope.
8. Worker performs the task; output and evidence are captured by Magna.
9. Magna reviews worker changes and evidence against the task scope.
10. Magna verifies the task outcome (what was claimed vs. what is verified).
11. Magna records the verdict in the TRACE envelope.
12. Magna provides a short verdict summary in chat (the active session; later also Telegram when activation-gated).
13. Magna writes or proposes the complete verdict and next-action suggestions in GitHub evidence.
14. Magna records the next-action suggestions in the TRACE envelope.
15. Magna presents recommended next actions to the user and waits for approval, redirection, or stop.
16. User approves, rejects, clarifies, or redirects.
17. Magna continues only within the approved next envelope, or closes the task.
18. Full lifecycle remains TRACE-compliant from step 1 to step 17.

## Acceptance Criteria

- [ ] User can start a Magna task from a local instruction.
- [ ] Magna creates a TRACE envelope before any action proceeds.
- [ ] Magna matches the instruction against a known governed instruction.
- [ ] Magna classifies the action and records the classification in the TRACE envelope.
- [ ] Magna selects the appropriate worker according to approved worker policy.
- [ ] Worker is launched through an approved wrapper with bounded scope.
- [ ] Worker result is captured and a TRACE-linked result state is assigned.
- [ ] Magna reviews worker changes and evidence and records the review in the TRACE envelope.
- [ ] Magna verifies the task outcome (claimed vs. verified changes and evidence).
- [ ] Magna records the verdict in the TRACE envelope.
- [ ] Magna provides a short verdict summary in chat (the active session).
- [ ] Magna writes or proposes the complete verdict and next-action suggestions in GitHub evidence.
- [ ] GitHub evidence links back to the Magna TRACE task ID.
- [ ] Magna records next-action suggestions in the TRACE envelope.
- [ ] Magna presents recommended next actions to the user and waits for approval, redirection, or stop.
- [ ] User can approve, redirect, or stop.
- [ ] Magna continues only within the approved next envelope.
- [ ] Magna stops when the next requested action is unknown, blocked, or outside approval.
- [ ] Full lifecycle from instruction to closure remains TRACE-compliant.
- [ ] Chat verdict summary is concise and references the TRACE/evidence ID; it does not replace the GitHub evidence record.
- [ ] Full forward and backward traceability is visible in both Magna Command Center UI (live task/TRACE view) and GitHub (durable evidence).
- [ ] Chat and Telegram surfaces show short summaries with TRACE/evidence references only.
- [ ] Task continuation is supported from both local Magna/chat (Epic 1 default) and remote Telegram channel (once activation-gated).
- [ ] RETAIN_DISABLED_BY_DEFAULT capabilities are visible in the Magna Command Center UI with status, reason, activation gates, and enablement eligibility — and are not executed while disabled.

## Non-Default Capabilities (RETAIN_DISABLED_BY_DEFAULT)

The following capabilities are part of the Magna capability model but disabled by default in Magna version enso. They may be enabled later by explicit Product Owner or user action through Magna UI, subject to Magna permissions, policy gates, audit, and TRACE requirements:

- **Telegram-triggered task continuation** — remote continuation from Telegram is activation-gated; not part of Epic 1 default flow.
- **Scheduler/cron auto-execution** — automated continuation without user instruction is disabled by default.
- **Skills/self-improvement** — worker self-directed skill updates are disabled by default.
- **Memory write automation** — automatic memory writes without user approval are disabled by default.
- **Multi-level subagent delegation** — worker spawning sub-workers is disabled by default.
- **MCP/tool dynamic loading** — dynamic tool registration at runtime is disabled by default.
- **Browser actions** — automated browser control is disabled by default.
- **Remote execution backends** — cloud or SSH execution is disabled by default.
- **Multi-channel notification fanout** — notifications beyond the primary chat session are disabled by default.
- **Cloud provider activation** — remote model providers are disabled by default.

## Approved Demo Scenario (Epic 1)

The first approved end-to-end demonstration scenario for Product Owner review is:

> **Instruction:** "Review PR status for Magna Enso and prepare assessment."

Expected demo flow:

```
1.  User gives instruction in Magna local command/chat.
2.  Magna creates TRACE envelope.
3.  Magna parses instruction.
4.  Magna checks known instruction match.
5.  Magna classifies the action.
6.  Magna selects Claude or Codex based on approved worker policy.
7.  Worker performs the task.
8.  Worker output/evidence is written or proposed in GitHub.
9.  Magna reviews worker changes and evidence.
10. Magna verifies task outcome.
11. Magna records verdict in TRACE.
12. Magna provides short verdict summary in chat.
13. Magna writes/proposes complete verdict and next-action suggestions in GitHub.
14. Magna waits for user approval, redirection, or stop.
```

Telegram-triggered real execution remains blocked until R-06 is fixed and all messaging activation gates are complete. This demo scenario runs through the local Magna flow only.

## Task Continuation Channels

Task continuation is supported through both:

- **Local Magna / chat** (Epic 1 default): The primary continuation channel. Continuation occurs in the active Magna chat session.
- **Remote channel (Telegram)**: Allowed after all activation gates are satisfied (R-06, messaging re-authorization, Telegram User ID allowlist sender boundary, approved approval-channel design, TRACE/audit verified). This is not the Epic 1 default flow.

Epic 1 always prioritizes local Magna / chat continuation first. Remote continuation requires all authorization gates to be satisfied first.

## RETAIN_DISABLED_BY_DEFAULT Capability UI

RETAIN_DISABLED_BY_DEFAULT capabilities appear in the Magna Command Center UI even when disabled. The UI must:

- Show capability name.
- Show status: **Disabled by default**.
- Show the reason and associated risk.
- Show the required activation gates.
- Show whether the user can request enablement.
- Not allow activation unless all required gates are satisfied.
- Not execute a disabled capability.
- When a capability is later enabled, it must still pass Magna policy, audit, and TRACE requirements.

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

None — all open questions resolved by Product Owner on 2026-06-30.

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm the complete governed loop from remote request to continuation while preserving user approval and TRACE evidence.
