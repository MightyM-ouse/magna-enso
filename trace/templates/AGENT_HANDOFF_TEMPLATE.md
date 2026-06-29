# <TASK-ID> Agent Handoff

## Provenance

- Instruction prepared by: ChatGPT / System Architect
- Instruction approved by: Product Owner
- Intended reviewer: ChatGPT / System Architect  <!-- CF-6: who WILL review -->
- Review status: `PENDING` | `COMPLETED`  <!-- PENDING until review evidence exists -->
- Review completed by: `<reviewer or null>`  <!-- null while PENDING -->
- Agent and role: `<agent> / <role>`

## Identity and state

| Field | Value |
|---|---|
| Task | `<TASK-ID>` |
| Status | `<one of the governed status_vocabulary values>` |
| Branch | `<branch>` |
| Starting commit | `<full SHA>` |
| Final commit (pre-handoff) | `<full SHA or null>`  <!-- CF-2: never the commit containing this handoff -->
| Synchronization authority | live GitHub branch head  <!-- CF-2: commit fields are point-in-time only -->
| Pull request | `<URL or null>` |
| Synchronization verdict | `SYNC_PASS` |

## Outcome

State what was achieved against each acceptance criterion. Distinguish implemented,
validated, proposed, skipped, and blocked work.

## Method and rationale

Summarize the repository observations, alternatives considered, selected method, and
trade-offs. Identify any accepted contract that constrained the method.

## Changes

List changed paths grouped by purpose. Record any path added after investigation and why it
remained within the approved envelope.

## Downloads and dependencies

| Source | Purpose | Version | Destination | Bytes/SHA-256 | License | Executed | Security checks | Resulting changes |
|---|---|---|---|---|---|---|---|---|

Use `None` when no material download or dependency was introduced.

## Validation

| Check | Command/tool | Result | Evidence |
|---|---|---|---|

Failed and skipped checks remain visible with the exact reason.

## Deviations and decisions

Record deviations from the expected outcome or envelope, amendments used, unresolved
questions, and Product Owner decisions required. Never hide corrective iterations.

## Architecture, security, and integration impact

Describe contract changes, security implications, migration/compatibility concerns,
shared-path interaction, integration order, and residual risk.

## Recommended next action

Provide one bounded next action. Do not claim acceptance or merge approval.

The companion JSON file must conform to `trace/schemas/agent_handoff.schema.json`.
