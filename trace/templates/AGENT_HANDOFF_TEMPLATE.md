# <TASK-ID> Agent Handoff

## Provenance

- Instruction prepared by: ChatGPT / System Architect
- Instruction approved by: Product Owner
- Output prepared for: ChatGPT architectural review and Product Owner decision
- Agent and role: `<agent> / <role>`

## Identity and state

| Field | Value |
|---|---|
| Task | `<TASK-ID>` |
| Status | `<status>` |
| Branch | `<branch>` |
| Starting commit | `<full SHA>` |
| Final commit | `<full SHA>` |
| Pull request | `<URL>` |
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
