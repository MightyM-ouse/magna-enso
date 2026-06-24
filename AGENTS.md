# AGENTS.md - Magna Enso

This repository is the canonical source for Magna Enso. All workers use TRACE (Template,
Route, Assign, Check, Evidence), verify current GitHub state, and operate only through an
approved task envelope.

## Required startup and synchronization

Before making a current-state claim or issuing/acting on an execution instruction:

1. Read this file and the applicable worker adapter.
2. Read `trace/STAR_MAP.md`, `trace/ACTIVE_WORK_REGISTRY.yaml`, the active issue, task
   packet, pull request, and applicable Event Horizon decisions.
3. Load only the routes declared in `trace/CELESTIAL_INDEX.json`; broaden context with a
   recorded reason.
4. Confirm role and workflow in `trace/ROLE_REGISTRY.yaml` and `trace/WORKFLOWS.yaml`.
5. Compare default branch/HEAD, assigned branch and starting commit, task/PR status, CI,
   evidence, ownership, dependencies, shared paths, and known local-but-unpushed work.
6. Record exactly one verdict:
   - `SYNC_PASS`
   - `SYNC_BLOCKED`
   - `SYNC_UNVERIFIED_LOCAL_STATE`

Only `SYNC_PASS` permits execution. A discrepancy is reported and reconciled before a
worker prompt is issued or files are changed. GitHub state is not inferred from chat memory.

## Authority order

1. Product Owner decisions recorded in `trace/DECISION_LOG.md`.
2. Accepted requirements, architecture, technical specifications, and security policy.
3. Approved task envelope plus separately recorded amendments.
4. Current code, tests, configuration, and migrations.
5. Star Map, active-work and other registries, and curated evidence.
6. README files and historical/noncanonical archives.

Conflicts must be reported. Decisions are superseded, never silently deleted. Historical
archive content never overrides canonical sources.

## Instruction contract

Worker instructions follow: **precise outcome, bounded authority, independent method**.

A task defines outcome, acceptance criteria, evidence, constraints, ownership, authority,
and escalation boundaries. It does not prescribe a solution, file list, root cause, or
command sequence unless an accepted contract, security control, deterministic migration,
regulatory rule, or irreversible-risk boundary requires it. Workers investigate options,
choose the method, and record rationale and trade-offs.

Every task states that its instruction was prepared by ChatGPT/System Architect and
approved by the Product Owner. Every worker handoff is prepared for ChatGPT architectural
review and Product Owner decision.

## Parallel ownership

- Parallel agents use unique task IDs, branches, worktrees, starting commits, and PRs.
- Writable paths are exclusive while a task is active.
- Dependencies, shared paths, designated owners, and integration order are recorded in
  `trace/ACTIVE_WORK_REGISTRY.yaml`.
- Workers do not modify another task's branch, packet, worktree, evidence, or owned paths.
- Shared writable paths require a designated owner, sequential phase, separate amendment,
  or explicit reconciliation assignment.
- Stacked work identifies the exact dependency commit and does not represent it as accepted
  `main` state.

## Branch autonomy and Product Owner authority

An approved task packet authorizes the assigned worker to investigate, implement, validate,
correct, commit, push, and update a draft PR on its assigned branch without repeated
approval. The worker may not push to `main`, force-push, rewrite shared history, merge,
self-accept, close acceptance gates, delete branches, or change product scope.

The Product Owner retains scope, priority, functional acceptance, risk acceptance, merge,
and release authority. ChatGPT reviews completed work and issues `APPROVE_TO_MERGE`,
`CHANGES_REQUIRED`, or `BLOCKED`; only the Product Owner merges or explicitly authorizes
merge.

## Approval boundary

Routine task-branch work is not approval-gated. Stop before accessing unapproved personal
or system paths; using credentials, private repositories, paid services, or nonpublic data;
performing privileged/global/system changes; deleting user or unrelated data; creating
public or consequential external effects; materially changing architecture/scope; bypassing
policy; accepting risk; or merging.

Public task-required downloads and isolated project dependencies are permitted when the
task envelope covers them. Record source, purpose, version, destination, size/hash,
license/provenance, execution status, security checks, and resulting files or lockfiles.

Full rules: `docs/governance/MULTI_AGENT_EXECUTION_POLICY.md`.

## Immutable task authority

An approved task packet becomes immutable at `IN_PROGRESS`. Progress belongs in
checkpoints, issue comments, handoffs, PRs, and Light Curves. A scope/authority change uses
a separate amendment, Product Owner decision, and new synchronization pass. Do not edit the
active packet concurrently with its worker.

## TRACE and evidence

- **Template:** use the governed task template under `trace/templates/`.
- **Route:** load declared context only; justify expansion.
- **Assign:** stay within role, task envelope, and path ownership.
- **Check:** run required validation and preserve exact failures/skips.
- **Evidence:** create/update the task Light Curve and Markdown/JSON handoffs.

Meaningful work is incomplete without a reviewable PR and a JSON handoff conforming to
`trace/schemas/agent_handoff.schema.json`. Detailed evidence belongs in the repository;
chat output stays concise and points ChatGPT to the evidence paths.

## Security

- Never commit secrets, credentials, cookies, browser profiles, private keys, `.env`
  contents, unsafe personal data, or unredacted private paths.
- Run Gitleaks before push and in CI when available.
- Record provenance and license for reused source, dependencies, and material downloads.
- Store large/raw logs, traces, videos, coverage, and generated packages as approved
  artifacts, not source.
- Public repository visibility does not authorize public runtime or network exposure.
- Hermes, tools, memory writes, schedulers, providers, messaging, and external execution
  require an applicable approved envelope and policy gate.

## Worker adapters

`CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`, `HERMES.md`, and `CHATGPT.md` are thin role
adapters. They may narrow permissions but cannot override this file or Product Owner
authority.

## Current boundaries

- Sprint 4's inert Hermes provenance baseline is accepted.
- Sprint 5 implementation remains unaccepted until separately reviewed and merged.
- The canonical policy engine is not selected.
- Hermes capabilities remain inactive.
- SGN-01 remains blocked.
