# Multi-Agent Execution Policy

## Purpose

This policy governs repository work performed by ChatGPT, Codex, Claude, Antigravity,
and any later authorized Hermes worker. It enables parallel, outcome-oriented execution
without transferring Product Owner authority or allowing workers to conceal, overlap, or
self-approve work.

The operating principle is:

> Precise outcome, bounded authority, independent method.

## Authority model

- The Product Owner decides scope, priority, functional acceptance, risk acceptance,
  merge, and release.
- ChatGPT acts as System Architect: it synchronizes project state, prepares bounded tasks,
  coordinates ownership, reviews evidence, and issues merge-readiness recommendations.
- A worker may execute autonomously only inside an approved task envelope.
- Execution authority is not acceptance authority. No worker may approve or merge its own
  work.
- `main` remains protected and changes only through Product Owner-approved pull requests.

## Mandatory synchronization gate

Before ChatGPT issues an execution instruction, and again before a worker changes files,
the following remote state must be compared:

1. Default branch and current accepted commit.
2. Star Map and applicable decision, feature, risk, migration, and status registers.
3. Active GitHub issue and task packet.
4. Assigned branch, starting commit, pull request, and latest pushed commit.
5. Required checks, reviews, evidence, and unresolved conversations.
6. `trace/ACTIVE_WORK_REGISTRY.yaml`, including writable paths, dependencies, shared
   surfaces, and integration order.
7. Known local-but-unpushed work reported by any active worker.

The result must be exactly one of:

- `SYNC_PASS`: canonical and operational state agree; execution may proceed.
- `SYNC_BLOCKED`: a material inconsistency exists; no execution instruction is issued.
- `SYNC_UNVERIFIED_LOCAL_STATE`: GitHub is internally consistent, but relevant local work
  cannot be verified; execution stops until its owner publishes or accounts for it.

The synchronization record states the checked commit, sources, discrepancies, resolution,
and timestamp. Chat memory is never accepted as proof of current repository state.

## Outcome-oriented task design

A task packet defines:

- the required outcome and user value;
- acceptance criteria and evidence;
- protected boundaries and forbidden effects;
- the worker's authority envelope;
- dependencies and integration constraints;
- conditions that require escalation.

It should not prescribe an implementation, file list, root cause, or command sequence when
the worker can determine those safely through investigation. Exact methods are permitted
only for an accepted architecture contract, security control, deterministic migration,
regulatory requirement, or irreversible-risk boundary. The reason must be recorded.

Workers must inspect the current system, consider relevant alternatives, choose a method,
and record the rationale and trade-offs. Discovery may change the proposed method but may
not silently change the approved outcome or authority envelope.

## Parallel work and ownership

Parallel work is permitted when each active task has:

- a branch namespace matching the accountable worker or an explicitly approved neutral
  task namespace;
- a unique task ID, branch, worktree, starting commit, and pull request;
- one accountable worker;
- declared writable and read-only paths;
- declared dependencies and integration order;
- no uncoordinated writable-path overlap.

Path ownership is exclusive while a task is active. A shared writable path requires one of:

1. a single designated owner;
2. sequential phases;
3. a separate amendment or coordination artifact;
4. explicit Product Owner-approved reconciliation ownership.

Workers must not change another task's packet, evidence, branch, or worktree. A task that
depends on unmerged work records the exact branch and commit and is treated as a stacked
dependency, not as accepted `main` state.

## Bounded autonomous actions

An approved task packet authorizes the assigned worker, without repeated approval, to:

- investigate and choose a method within scope;
- edit approved repository paths in its isolated worktree;
- run task-relevant builds, tests, security scans, and local validation;
- make corrective iterations within the acceptance criteria;
- create normal commits and push only to its assigned branch;
- open and update a draft pull request;
- write required evidence, checkpoints, and handoffs;
- download public, task-required material into the assigned worktree; and
- install task-required dependencies into an isolated project environment when allowed by
  the task and provenance controls below.

Autonomy does not authorize force push, history rewrite, direct `main` push, merge,
self-acceptance, scope expansion, policy bypass, or changes outside assigned ownership.

## Actions requiring Product Owner approval

A worker must stop before:

- accessing personal or system files outside approved roots;
- using credentials, private repositories, paid services, or nonpublic data;
- performing administrator or privileged actions;
- changing global installations, operating-system settings, services, firewalls, or
  persistent host configuration;
- deleting or destructively modifying user data, unrelated work, or shared history;
- creating public listeners, tunnels, external messages, deployments, purchases, or other
  consequential external effects;
- adding an unapproved architectural dependency or materially changing product scope;
- accepting risk, merging to `main`, releasing, or closing acceptance gates; or
- acting when the synchronization result is not `SYNC_PASS`.

The worker reports the exact boundary, why it is necessary, alternatives considered, and
the least-privileged approval requested. It does not ask the Product Owner to approve
routine branch-local actions already covered by the task envelope.

## Downloads and dependencies

A public download is autonomous only when it is task-required, legal to use, stored within
the approved worktree or isolated project environment, below repository and task size
limits, and does not require credentials or privileged host changes.

The handoff must record for every material download:

- source URL and publisher;
- purpose and selection rationale;
- version, destination, and size;
- SHA-256 when a stable artifact is downloaded;
- license and provenance;
- whether it was executed or imported;
- security checks performed; and
- repository files, manifests, or lockfiles changed.

Executable downloads, install scripts, binary tools, or dependencies with material
runtime/license impact require explicit coverage in the task envelope. Package-manager
caches outside the worktree are permitted only as ordinary isolated-tool behavior; they
must not modify global configuration or expose credentials.

## Immutable execution authority and amendments

The approved task packet becomes immutable when its status enters `IN_PROGRESS`.
Workers record progress in checkpoints, Light Curves, handoffs, issue comments, and pull
requests, not by rewriting the active authority.

A scope or authority change requires a separate amendment containing:

- amendment ID and parent task;
- author and Product Owner decision;
- reason, changed boundaries, and effect on acceptance criteria;
- effective branch commit and required resynchronization.

The worker stops at a safe checkpoint, reaches `SYNC_PASS` against the amendment, and then
continues. Historical task and amendment records are never silently replaced.

## Handoff contract

Every meaningful worker result includes:

1. A concise chat summary for the Product Owner.
2. A repository Markdown handoff for human review.
3. A JSON handoff conforming to `trace/schemas/agent_handoff.schema.json`.

The handoff identifies the instruction as prepared by ChatGPT/System Architect and approved
by the Product Owner. Provenance distinguishes the **intended reviewer** from a **completed
review**: `intended_reviewer` names who will review, while `review_status` is `PENDING` until
an independent review actually occurs and `review_completed_by` is set only when it is
`COMPLETED`. A handoff must never assert a completed review before review evidence exists
(CF-6). It must include task/agent identity, branch and commits, files changed, downloads,
commands, validation, failures, deviations, decisions, architecture/security impact, residual
risk, pull request, and recommended next action. Exact failures and skipped checks remain
visible.

## Status authority and commit-field semantics

- **Canonical live task status** is `trace/ACTIVE_WORK_REGISTRY.yaml` (`active_tasks[].status`).
  The immutable task packet records the status frozen at publication (historical, not live);
  the Star Map is a human narrative summary that mirrors the live status; a handoff `task.status`
  is a point-in-time snapshot. All statuses use one governed vocabulary, declared once in
  `ACTIVE_WORK_REGISTRY.status_vocabulary` and enforced by the schema enum and validator (CF-3/CF-4).
- **Synchronization authority is the live GitHub branch head.** Recorded commit fields
  (`repository_state.final_commit`, registry `latest_known_commit`) are point-in-time pointers,
  are never required to equal the commit that contains them (impossible self-reference), and
  must not be read as freshness guarantees (CF-2).

## Governance enforcement (CI)

The governance validator `scripts/validate_multi_agent_governance.py` runs in CI on the main
PR and on stacked correction/review PRs, with a pinned dependency
(`scripts/governance-requirements.txt`).

**Task-specific changed-path ownership (CF-5, hardened).** `scripts/check_changed_path_ownership.py`
identifies the **one accountable active task** from the PR head branch and validates the change set
against **only that task's** envelope — its `writable_paths`, declared `shared_paths`, and any
explicit `correction_phase_modifies` files — plus the single self-registration file
`trace/ACTIVE_WORK_REGISTRY.yaml`. It does **not** accept a union of writable paths across tasks, and
broad directory allowances do not override explicit task ownership. The check **fails closed** when the
task identity is missing, ambiguous, unregistered, or not active (status `MERGED`/`CLOSED`/`REJECTED`),
and when a changed path falls outside the accountable task's envelope. Every changed governed handoff
file (`trace/evidence/*HANDOFF.json`) is schema-validated, rejecting out-of-vocabulary status and any
handoff changed outside the task envelope. This adds enforcement without changing `main` branch
protection.

## Review and integration

After a worker pushes its final task commit:

1. ChatGPT reruns synchronization and reviews scope, architecture, diff, tests, evidence,
   security, dependency changes, conflicts, and integration order.
2. Independent review is performed when the task or risk class requires it.
3. ChatGPT issues exactly one recommendation:
   - `APPROVE_TO_MERGE`
   - `CHANGES_REQUIRED`
   - `BLOCKED`
4. Only the Product Owner merges or explicitly authorizes merge into `main`.
5. After merge, canonical status and active-work records are reconciled before another
   dependent instruction is issued.

## Four-eyes rule

The independent reviewer uses a separate branch or read-only review context and must not
be the feature implementer. Review findings may be committed on a dedicated review branch.
Any correction to the implementation branch requires assigned ownership and remains
subject to the same evidence and Product Owner merge boundary.
