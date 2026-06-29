# Magna-Hermes Runtime Adoption Brief

Status: planning brief / Product Owner seed input  
Owner: Product Owner + ChatGPT system architect  
Repository: MightyM-ouse/magna-enso  
Related runtime source: https://github.com/NousResearch/hermes-agent  
Related command UI source: https://github.com/MightyM-ouse/magna-command-center  
Related Magna source: https://github.com/MightyM-ouse/magna-enso  
Related branding PR: #33 — Add MAG-US-001 animated Magna identity story

---

## 1. Purpose

This brief captures the agreed product direction for adopting selected Hermes runtime capabilities under the Magna Enso product experience.

This is not an implementation plan yet. It is the seed brief for the Product User Story chat to create formal product user stories and for later technical specification work.

The intended product direction is:

```text
Magna Enso remains the product identity, governance surface, command experience, and TRACE operating model.
Hermes is evaluated as a runtime capability provider underneath selected Magna functions.
TRACE remains mandatory for forward and backward traceability.
GitHub remains the durable source of planning, instruction, assessment, evidence, and review state.
The Product Owner remains final authority.
```

---

## 2. Epic

### EPIC: Magna-Hermes Runtime Adoption

As a Magna user, I want selected Hermes runtime capabilities to operate behind the Magna Enso experience, so that I can remotely initiate, monitor, approve, and continue governed agent work while preserving TRACE-based forward and backward traceability.

### Product value

This epic allows Magna to become a practical command environment without rebuilding every runtime capability from scratch.

Hermes may provide runtime strengths such as terminal access, messaging gateway, memory, skills, profiles, scheduling, delegation, and tool execution.

Magna provides the governed user experience, safety boundaries, traceability, approval model, GitHub evidence, ChatGPT system-architect workflow, and Product Owner control.

### Core user outcome

The user can start a governed task from Telegram or another approved remote channel. Magna receives it, checks whether the task matches known instructions, dispatches the correct CLI worker when allowed, captures the result, writes evidence or assessment to GitHub, notifies the user, and waits for approval when required.

### Non-goals

```text
- Do not replace Magna with Hermes.
- Do not allow unrestricted terminal autonomy.
- Do not allow arbitrary worker invocation.
- Do not bypass TRACE.
- Do not merge PRs, delete branches, force push, install software, or expose remote access automatically.
- Do not start with full self-improving autonomy.
- Do not treat Hermes profiles as security sandboxes.
```

### Success criteria

```text
- Magna-branded Hermes runtime can receive a remote command.
- Commands are classified as known-safe, governed, unknown, approval-required, or blocked.
- Approved CLI workers can be launched only through predefined wrappers.
- Worker output is captured and linked to a TRACE task ID.
- GitHub receives assessment/evidence updates.
- User receives notification and can approve or redirect next steps.
- Unknown/risky actions pause automatically.
- Every action can be traced backward to the user request and forward to the next allowed action.
```

---

## 3. Product story seeds

These are seeds only. The Product User Story chat must convert them into formal product story files using the repository's product story template and index.

### MAG-US-HERMES-001 — Magna-Branded Hermes Runtime Identity

As a Magna user, I want Hermes runtime interactions to appear under the Magna Enso identity, so that I experience one coherent Magna command environment instead of separate underlying tools.

Acceptance direction:

```text
- User-facing runtime messages use Magna/Magna Enso language.
- Internal evidence may record Hermes as the runtime provider.
- The distinction between Magna identity and Hermes runtime is documented.
- No existing Magna governance terminology is replaced by Hermes terminology.
```

### MAG-US-HERMES-002 — Remote Command Intake from Telegram or Approved Channel

As a Magna user, I want to send a task command from Telegram or another approved channel, so that I can initiate Magna work while away from the laptop.

Acceptance direction:

```text
- Magna can receive a remote message from an approved channel.
- The message is parsed into a task request.
- The request receives a unique task/session identifier.
- The request is acknowledged back to the user.
- Unsupported or ambiguous commands are not executed.
```

### MAG-US-HERMES-003 — Known Instruction Matching

As a Magna user, I want Magna to check whether my remote command matches a known approved instruction, so that only predefined and governed workflows can proceed automatically.

Acceptance direction:

```text
- Magna checks remote commands against a known instruction registry.
- Matching commands can proceed according to their safety class.
- Unknown commands are paused and escalated.
- The match result is recorded in task evidence.
- The user is informed whether the command was accepted, rejected, or needs clarification.
```

### MAG-US-HERMES-004 — Safe, Governed, Unknown, and Blocked Action Classification

As a Magna user, I want Magna to classify each requested action by risk level, so that safe work can continue while risky or unknown work requires approval.

Suggested classes:

```text
SAFE_KNOWN:
Read status, summarize logs, prepare evidence, send notification, run predefined validation.

GOVERNED_KNOWN:
Start Claude review, start Codex implementation, start Antigravity validation, create review package.

APPROVAL_REQUIRED:
Modify GitHub files, create branches, run non-trivial terminal commands, update memory/skills, schedule future work.

BLOCKED_OR_UNKNOWN:
Force push, merge to main, delete branches, install software, expose remote access, arbitrary shell command, unknown request.
```

Acceptance direction:

```text
- Every requested action receives a safety classification.
- Safe known actions may proceed automatically.
- Governed known actions require matching predefined instruction.
- Approval-required actions pause for user confirmation.
- Unknown or blocked actions do not execute.
```

### MAG-US-HERMES-005 — CLI Worker Dispatch Through Approved Wrappers

As a Magna user, I want Magna to start the correct CLI worker only through approved command wrappers, so that Claude, Codex, or Antigravity work is controlled and traceable.

Acceptance direction:

```text
- Worker selection is based on task type and approved instruction.
- Only approved wrappers can be launched.
- Working directory is bounded.
- Worker command, arguments, start time, and task ID are captured.
- If the worker cannot start, Magna reports the failure and pauses.
```

### MAG-US-HERMES-006 — Worker Result Capture

As a Magna user, I want Magna to capture worker output and task results, so that I can review what happened without manually searching terminal logs.

Acceptance direction:

```text
- Worker stdout/stderr or equivalent output is captured.
- Changed files are identified where applicable.
- Worker result is summarized.
- Worker claims are separated from verified evidence.
- Failure, timeout, pause, or completion states are recorded.
```

### MAG-US-HERMES-007 — GitHub Assessment and Evidence Update

As a Magna user, I want Magna to write task assessment and evidence to GitHub, so that project state remains durable, reviewable, and TRACE-compliant.

Acceptance direction:

```text
- Magna writes or proposes a task evidence file.
- Evidence includes task ID, user request, instruction source, worker, action taken, result, risks, and next decision.
- GitHub update is linked to the task lifecycle.
- Unknown/risky cases include an assessment explaining why approval is needed.
- Evidence format supports later review package generation.
```

### MAG-US-HERMES-008 — User Notification and Approval Loop

As a Magna user, I want Magna to notify me when a task completes, pauses, or needs approval, so that I can decide the next step remotely or through ChatGPT.

Acceptance direction:

```text
- Magna sends a clear notification after task completion, pause, failure, or approval requirement.
- Notification includes short status, evidence link/reference, and decision needed.
- User can approve, reject, request clarification, or redirect next step.
- Magna does not continue approval-required work until approval is received.
```

### MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement

As a Magna user, I want every remote task action to follow TRACE, so that I can trace from original request to final result and from each instruction to the next allowed action.

Backward traceability must answer:

```text
- What user request started this?
- Which task ID was created?
- Which GitHub instruction was used?
- Which worker ran?
- Which command wrapper was used?
- What files changed?
- What evidence proves the result?
- Who approved continuation?
```

Forward traceability must answer:

```text
- What is the next allowed action?
- Who or what may perform it?
- What is forbidden?
- What evidence must be produced?
- When must Magna stop and ask the user?
```

Acceptance direction:

```text
- Every task has a TRACE envelope.
- Every worker action links to the originating task.
- Every result links to evidence.
- Every next step has an allowed/blocked/approval-required state.
- No task can be marked complete without trace evidence.
```

### MAG-US-HERMES-010 — End-to-End Governed Task Continuation

As a Magna user, I want Magna to continue a task after my approval or redirection, so that multi-step work can progress without losing context or traceability.

Acceptance direction:

```text
- User can start a task remotely.
- Magna can classify and dispatch a known worker task.
- Worker result is captured.
- Evidence is written to GitHub.
- User is notified.
- User can approve or redirect.
- Magna continues only within the approved next envelope.
- Full lifecycle remains TRACE-compliant.
```

---

## 4. Four-sprint grouping

This is a product-level grouping only. It must not be converted into technical implementation tasks until the Product Owner approves the formal user stories.

### Sprint 1 — Control Foundation

Goal: prove that Magna/Hermes can receive a command, classify it, and stop safely.

Stories:

```text
MAG-US-HERMES-001 — Magna-Branded Hermes Runtime Identity
MAG-US-HERMES-002 — Remote Command Intake from Telegram or Approved Channel
MAG-US-HERMES-003 — Known Instruction Matching
MAG-US-HERMES-004 — Safe, Governed, Unknown, and Blocked Action Classification
```

Expected outcome:

```text
Remote command intake works in a controlled mode. Magna can respond accepted, needs approval, unknown, or blocked. Risky execution is not allowed.
```

### Sprint 2 — Worker Dispatch

Goal: prove that Magna can start a specialist CLI worker safely through approved wrappers.

Stories:

```text
MAG-US-HERMES-005 — CLI Worker Dispatch Through Approved Wrappers
MAG-US-HERMES-006 — Worker Result Capture
```

Expected outcome:

```text
Magna can start a predefined Claude/Codex/Antigravity-style worker task, capture the outcome, and stop safely.
```

### Sprint 3 — Evidence and Approval Loop

Goal: prove that completed or paused work becomes reviewable and user-controlled.

Stories:

```text
MAG-US-HERMES-007 — GitHub Assessment and Evidence Update
MAG-US-HERMES-008 — User Notification and Approval Loop
```

Expected outcome:

```text
Magna can update GitHub with assessment/evidence and notify the user for the next decision.
```

### Sprint 4 — End-to-End TRACE Continuation

Goal: prove the complete governed remote task loop.

Stories:

```text
MAG-US-HERMES-009 — TRACE Forward and Backward Traceability Enforcement
MAG-US-HERMES-010 — End-to-End Governed Task Continuation
```

Expected outcome:

```text
A full remote-controlled Magna task can run from user request to worker execution, evidence, notification, approval, continuation, and closure while preserving TRACE.
```

---

## 5. Future technical specification and integration assessment scope

After the formal product user stories are created and approved, prepare a technical specification and integration assessment for the first version of Magna, named:

```text
Magna version enso
```

The technical specification must assess integration between:

```text
https://github.com/NousResearch/hermes-agent
https://github.com/MightyM-ouse/magna-command-center
https://github.com/MightyM-ouse/magna-enso
```

The assessment must cover:

```text
- Hermes runtime capabilities to adopt, adapt, wrap, rebuild, reject, or defer.
- Messaging channel feasibility: Telegram first, WhatsApp later if practical.
- CLI worker orchestration: Claude, Codex, Antigravity.
- Approved wrapper model for terminal execution.
- TRACE task envelope and evidence lifecycle.
- GitHub assessment/evidence write strategy.
- Safety classification and approval model.
- Memory, skills, self-improvement, scheduler, and profile boundaries.
- Local-first constraints and laptop-on operating assumption.
- Magna Command Center UI fit.
- Magna Enso backend/orchestration fit.
- PR #33 animated Magna identity story and logo/brand asset dependency.
```

---

## 6. Branding dependency

PR #33 introduces the animated Magna identity story and related product story index.

This adoption epic must treat PR #33 as a branding dependency for Magna version enso:

```text
- User-facing runtime identity should be Magna/Magna Enso.
- Hermes may be recorded internally as runtime provider.
- Approved animated logo/presence behavior should be considered for app launch, loading, thinking, notification, and command-state surfaces.
- Reduced-motion fallback must be respected.
```

---

## 7. Instruction for Product User Story chat

The Product User Story chat must read this file before creating formal stories.

Instruction:

```text
Read trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md.
Create formal product user stories for the epic "Magna-Hermes Runtime Adoption".
Use the 1 epic, 10 user story seeds, and 4 sprint grouping exactly as the source structure.
Do not rely on chat memory.
Do not create sprint implementation tasks yet.
Do not create technical subtasks yet.
Save formal stories under trace/product/user-stories/ and update trace/product/PRODUCT_STORY_INDEX.md for Product Owner review.
```
