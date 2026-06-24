# <TASK-ID> - <Outcome>

## Authority

- Product Owner: Vinay
- Instruction prepared by: ChatGPT / System Architect
- Instruction approval: `<approved reference and date>`
- Assigned worker: `<agent>`
- Role: `<role from ROLE_REGISTRY.yaml>`
- Issue: `<number>`
- Branch: `<unique task branch>`
- Starting commit: `<full main or stacked dependency SHA>`
- Pull request: `<number or pending>`

The approved packet authorizes autonomous execution inside the envelope below. It does not
authorize acceptance, merge, release, risk acceptance, or unlisted consequential effects.

## Synchronization record

- Verdict: `SYNC_PASS | SYNC_BLOCKED | SYNC_UNVERIFIED_LOCAL_STATE`
- Checked at: `<ISO-8601>`
- Accepted `main`: `<full SHA>`
- Task branch/head: `<full SHA>`
- Sources checked: `<issue, task, PR, Star Map, decisions, active-work registry, CI>`
- Known local/unpushed work: `<none or owner/status>`
- Discrepancies and resolution: `<none or exact record>`

Execution is forbidden unless the verdict is `SYNC_PASS`. The worker repeats this gate
before editing and records any newer state.

## Required outcome

Describe the result and user value. Do not prescribe the solution unless an accepted
contract or safety requirement makes the method mandatory.

## Acceptance criteria

1. `<observable result>`
2. `<quality/security result>`
3. `<evidence result>`

## Context and constraints

- Canonical sources: `<routes>`
- Protected boundaries: `<paths, runtime, data, architecture>`
- Dependencies: `<tasks/commits>`
- Integration order: `<before/after/concurrent>`

## Ownership

- Writable paths: `<glob list>`
- Read-only paths: `<glob list>`
- Shared surfaces: `<list and designated owner>`
- Forbidden paths: `<list>`

The worker may refine the writable file list after investigation only when the new path is
inside the approved outcome and no active ownership conflict exists. Record the reason in
the handoff. Scope or authority expansion requires an amendment.

## Autonomous authority

Within this envelope the worker may investigate, select the method, edit, test, correct,
commit, push the assigned branch, update a draft PR, and produce evidence. Public,
task-required downloads and isolated project dependencies are allowed only under the
provenance and security rules in the Multi-Agent Execution Policy.

## Approval-required boundaries

Stop before personal/system paths outside approved roots, credentials/private sources,
paid services, privileged/global host changes, destructive actions, public/external side
effects, material architecture/scope changes, policy bypass, risk acceptance, or merge.

## Method-selection expectation

Inspect the current implementation and evidence, identify reasonable options, select the
best method, and record rationale and trade-offs. Do not treat examples, preliminary file
names, or hypotheses as mandated solutions.

## Validation and evidence

- Required automated checks: `<list>`
- Security/provenance checks: `<list>`
- Independent review: `<required/not required and reason>`
- Light Curve: `trace/evidence/<TASK-ID>_LIGHT_CURVE.md`
- Markdown handoff: `trace/evidence/<TASK-ID>_HANDOFF.md`
- JSON handoff: `trace/evidence/<TASK-ID>_HANDOFF.json`

## Immutable execution rule

When status becomes `IN_PROGRESS`, this packet is immutable. Progress belongs in evidence
and checkpoints. Any authority change requires `<TASK-ID>-A<n>` amendment, Product Owner
decision, and a new synchronization pass.

## Completion response

Return only the task status, branch/final commit/PR, validation summary, evidence paths,
downloads/dependencies summary, deviations/risks, and decisions still required. Detailed
evidence belongs in the repository handoff and Light Curve for ChatGPT review.
