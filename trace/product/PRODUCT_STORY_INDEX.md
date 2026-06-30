# Product Story Index

Status: READY_FOR_REFINEMENT
Purpose: Product Owner review index for formal Magna product user stories.
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

---

## Epic

### EPIC: Magna-Hermes Runtime Adoption

As a Magna user, I want Magna to orchestrate governed agent work from my instruction through worker execution, evidence, verdict, and next-action suggestion — with selected Hermes runtime capabilities operating behind the Magna Enso experience — so that I can initiate, monitor, approve, and continue governed work while preserving full TRACE-based traceability inside Magna and in GitHub.

## Product Value

This epic allows Magna to become a practical command environment without rebuilding every runtime capability from scratch.

Hermes may provide runtime strengths such as terminal access, messaging gateway, memory, skills, profiles, scheduling, delegation, and tool execution.

Magna provides the governed user experience, safety boundaries, traceability, approval model, GitHub evidence, ChatGPT system-architect workflow, and Product Owner control.

Advanced Hermes-derived capabilities that are not part of the default Epic 1 flow are **RETAIN_DISABLED_BY_DEFAULT** — they remain in the Magna capability model but are disabled by default and may be enabled later through explicit Magna UI action, subject to Magna permissions, policy gates, audit, and TRACE requirements.

## Capability Model: RETAIN_DISABLED_BY_DEFAULT

The following capabilities are retained in the Magna capability model but are **disabled by default** in Magna version enso. They are not part of default Epic 1 automatic execution. They may be enabled later only by explicit Product Owner or user action from Magna UI:

- WhatsApp messaging channel
- Scheduler/cron auto-execution
- Skills/self-improvement (background review, curator)
- Full memory write automation
- Multi-level subagent delegation
- MCP/tool dynamic loading
- Browser actions
- Remote execution backends (cloud, SSH)
- Multi-channel notification fanout
- Cloud provider activation
- Telegram-triggered remote execution (intake-only until authorization gates are met)

## RETAIN_DISABLED_BY_DEFAULT — Command Center UI Behavior

RETAIN_DISABLED_BY_DEFAULT capabilities appear in the Magna Command Center UI even when disabled. Required UI behavior:

- Show capability name.
- Show status: **Disabled by default**.
- Show the reason and associated risk.
- Show the required activation gates.
- Show whether the user can request enablement.
- Do not allow activation unless all required gates are satisfied.
- Do not execute a disabled capability under any circumstances.
- When a capability is later enabled, it must still pass Magna policy, audit, and TRACE requirements.

## Primary Flow (Epic 1 — Local Magna-Controlled Orchestration First)

Epic 1 prioritizes local Magna-controlled orchestration:

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

Telegram remote-triggered execution is activation-gated and requires R-06 fix, messaging re-authorization, Telegram User ID allowlist sender boundary (unknown user IDs are rejected or paused), and authenticated approval-channel design before real execution can proceed.

## Strong Internal TRACE Requirement

TRACE is enforced inside Magna itself (live internal state) as well as in GitHub (durable evidence record).

```
If it happened in Magna, it must be traceable in Magna.
If it matters for project history, it must also be durable in GitHub.
```

Every meaningful Magna action must create or update a TRACE event before the action can proceed. No worker dispatch, evidence write, verdict, next-action suggestion, continuation, or closure can occur without an active TRACE envelope. GitHub evidence links to the Magna TRACE task ID. Chat and Telegram summaries reference the TRACE/evidence ID.

## Non-Goals

- Do not replace Magna with Hermes.
- Do not allow unrestricted terminal autonomy.
- Do not allow arbitrary worker invocation.
- Do not bypass TRACE.
- Do not merge PRs, delete branches, force push, install software, or expose remote access automatically.
- Do not start with full self-improving autonomy.
- Do not treat Hermes profiles as security sandboxes.
- Do not allow RETAIN_DISABLED_BY_DEFAULT capabilities to activate without explicit Product Owner or user action.

## Success Criteria

- User can give a local instruction; Magna orchestrates the full governed workflow.
- Magna checks known instruction match and classifies every action before proceeding.
- Approved CLI workers can be launched only through predefined wrappers.
- Worker output is captured and assigned a TRACE-linked result state.
- Magna reviews worker changes and verifies task outcome.
- Magna provides a short verdict summary in chat and writes the complete verdict and next-action suggestions to GitHub.
- User receives the next-action suggestions and approves, redirects, or stops.
- Unknown/risky actions pause automatically.
- Every action is traceable inside Magna (live) and in GitHub (durable).
- Telegram intake is available activation-gated; it does not trigger execution until authorization gates are satisfied.
- RETAIN_DISABLED_BY_DEFAULT capabilities are not activated by default.

---

## User Stories

| Story ID | Title | Sprint Group | Status | File |
|---|---|---|---|---|
| MAG-US-HERMES-001 | Magna-Branded Hermes Runtime Identity | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-001-magna-branded-hermes-runtime-identity.md` |
| MAG-US-HERMES-002 | Remote Command Intake from Telegram or Approved Channel | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-002-remote-command-intake-from-approved-channel.md` |
| MAG-US-HERMES-003 | Known Instruction Matching | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-003-known-instruction-matching.md` |
| MAG-US-HERMES-004 | Safe, Governed, Unknown, and Blocked Action Classification | Sprint 1 — Control Foundation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-004-safe-governed-unknown-and-blocked-action-classification.md` |
| MAG-US-HERMES-005 | CLI Worker Dispatch Through Approved Wrappers | Sprint 2 — Worker Dispatch | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-005-cli-worker-dispatch-through-approved-wrappers.md` |
| MAG-US-HERMES-006 | Worker Result Capture | Sprint 2 — Worker Dispatch | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-006-worker-result-capture.md` |
| MAG-US-HERMES-007 | GitHub Assessment and Evidence Update | Sprint 3 — Evidence and Approval Loop | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-007-github-assessment-and-evidence-update.md` |
| MAG-US-HERMES-008 | User Notification and Approval Loop | Sprint 3 — Evidence and Approval Loop | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-008-user-notification-and-approval-loop.md` |
| MAG-US-HERMES-009 | TRACE Forward and Backward Traceability Enforcement | Sprint 4 — End-to-End TRACE Continuation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-009-trace-forward-and-backward-traceability-enforcement.md` |
| MAG-US-HERMES-010 | End-to-End Governed Task Continuation | Sprint 4 — End-to-End TRACE Continuation | READY_FOR_REFINEMENT | `trace/product/user-stories/MAG-US-HERMES-010-end-to-end-governed-task-continuation.md` |

---

## Four-Sprint Grouping

This is a product-level grouping only. It must not be converted into technical implementation tasks until the Product Owner approves the formal user stories.

### Sprint 1 — Control Foundation

Goal: prove that Magna/Hermes can receive a command, classify it, and stop safely.

Stories:

- MAG-US-HERMES-001 — Magna-Branded Hermes Runtime Identity
- MAG-US-HERMES-002 — Remote Command Intake from Telegram or Approved Channel
- MAG-US-HERMES-003 — Known Instruction Matching
- MAG-US-HERMES-004 — Safe, Governed, Unknown, and Blocked Action Classification

Expected outcome:

Local Magna instruction intake and remote command intake (Telegram, activation-gated) work in a controlled mode. Magna can respond accepted, needs approval, unknown, or blocked. Risky execution is not allowed. Telegram intake is intake-only until authorization gates are satisfied.

### Sprint 2 — Worker Dispatch

Goal: prove that Magna can start a specialist CLI worker safely through approved wrappers.

Stories:

- MAG-US-HERMES-005 — CLI Worker Dispatch Through Approved Wrappers
- MAG-US-HERMES-006 — Worker Result Capture

Expected outcome:

Magna can start a predefined Claude/Codex/Antigravity-style worker task, capture the outcome, and stop safely.

### Sprint 3 — Evidence and Approval Loop

Goal: prove that completed or paused work becomes reviewable and user-controlled.

Stories:

- MAG-US-HERMES-007 — GitHub Assessment and Evidence Update
- MAG-US-HERMES-008 — User Notification and Approval Loop

Expected outcome:

Magna can update GitHub with assessment/evidence and notify the user for the next decision.

### Sprint 4 — End-to-End TRACE Continuation

Goal: prove the complete governed remote task loop.

Stories:

- MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement
- MAG-US-HERMES-010 — End-to-End Governed Task Continuation

Expected outcome:

A full governed Magna task can run from user instruction to worker execution, evidence, Magna review, verdict, next-action suggestion, user approval, continuation, and closure while preserving TRACE inside Magna and in GitHub. Magna provides a short chat verdict summary and writes the complete verdict and next-action suggestions to GitHub. Remote Telegram continuation is activation-gated and not part of the default Epic 1 flow. RETAIN_DISABLED_BY_DEFAULT capabilities are not activated.

---

## Product Owner Review Notes

- These are formal product stories only. Status: READY_FOR_REFINEMENT.
- Sprint implementation tasks are not created yet.
- Technical subtasks are not created yet.
- Downstream design, architecture, frontend, backend, agent, validation, and governance work must be created only after Product Owner approval.
- PR #33 remains a branding dependency referenced by the source brief.
- Stories corrected per Product Owner CHANGES_REQUIRED comments on PR #35 (2026-06-30): RETAIN_DISABLED_BY_DEFAULT model applied, Telegram activation-gated, Epic 1 local-first flow added, strong internal TRACE requirement applied, verdict and next-action output split applied.
- Open question resolutions applied (2026-06-30): Telegram User ID allowlist sender boundary (OQ-1); approved Epic 1 demo scenario added to story 010 (OQ-2); both local-chat and remote-channel continuation supported, local first (OQ-3); minimum TRACE envelope view specified in story 009 (OQ-4); TRACE traceability in both Command Center UI and GitHub (OQ-5); RETAIN_DISABLED_BY_DEFAULT UI behavior specified (OQ-6); PR #33 treated as unresolved branding dependency in story 001 (OQ-7).
- PR #33: Unresolved branding dependency. Story 001 remains dependent on PR #33 acceptance. Do not assume merged until GitHub confirms.
