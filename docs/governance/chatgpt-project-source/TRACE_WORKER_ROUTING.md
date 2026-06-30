# TRACE Worker Routing and PR Continuity Rules

Status: Canonical ChatGPT project-source rule
Owner: Product Owner
Prepared by: ChatGPT / System Architect
Scope: Magna Enso / Magna Command Center TRACE operations

## 1. Durable instruction rule

Worker instructions that affect project history, worker scope, pull-request correction, implementation direction, technical assessment, sprint planning, merge readiness, or task closure must be recorded in GitHub before execution.

Allowed durable locations include:

- a GitHub PR comment;
- a GitHub issue comment;
- `trace/tasks/<TASK_ID>.md`;
- `trace/evidence/<TASK_ID>_HANDOFF.md`;
- `trace/reviews/<TASK_ID>-<AGENT>-REVIEW.md`;
- another governed TRACE file explicitly linked from the active task.

Chat is a coordination surface, not the durable task authority. Long execution briefs must not exist only in ChatGPT chat.

## 2. ChatGPT response rule

For Magna / TRACE work, ChatGPT should keep chat responses focused on:

- the decision made;
- where it was recorded in GitHub;
- the next action;
- allowed, blocked, or pending status;
- merge/readiness recommendation.

When a long worker instruction is required, ChatGPT should first record it in GitHub, then tell the user to ask the worker to follow that GitHub instruction.

## 3. Agent role split

ChatGPT / System Architect:
- architecture governance;
- Product Owner support;
- project-flow protection;
- GitHub comments and small governed corrections;
- PR assessment and merge-readiness review;
- deciding whether a task needs Claude, Codex, Antigravity, or Hermes.

Claude:
- independent review;
- local terminal work;
- local evidence inspection;
- correction implementation when local validation matters;
- repository/worktree synchronization checks;
- review and handoff evidence.

Codex:
- implementation;
- tests;
- backend/frontend code changes;
- scripts and mechanical code edits under an approved task envelope.

Antigravity:
- independent validation;
- UI/runtime inspection;
- adversarial review;
- validation evidence.

Hermes / Magna runtime:
- future governed runtime/orchestration surface only when explicitly enabled through Magna policy, permissions, audit, and TRACE.

## 4. PR continuity and sub-PR routing

A parent task/PR must remain the focus until it is completed, merged, blocked, or formally superseded.

When work on a parent PR discovers correction work that belongs to the same objective, the correction should be treated as a sub-PR of the parent, even though GitHub will assign a normal numeric PR number.

Use this logical notation in titles, bodies, comments, and evidence:

- `PR-37.1` for the first correction/validation PR related to PR #37;
- `PR-37.2` for the next correction/validation PR related to PR #37;
- continue until PR #37 is ready, merged, or blocked.

The actual GitHub PR number may still be #38, #43, or another number. The TRACE record must preserve the logical parent relation.

Required metadata for a sub-PR:

- `parent_pr: #37`;
- `logical_sub_pr: PR-37.1`;
- `parent_task_id: <TASK_ID>`;
- `purpose: correction | validation | evidence | registry-cleanup`;
- `return_target: parent branch`;
- `merge_target: parent PR branch unless explicitly approved otherwise`.

Only create a new top-level PR sequence when a genuinely separate feature, product decision, implementation task, or unrelated governance item is identified. Do not allow correction PRs to distract from the active parent objective.

## 5. Stack/merge rule

For a parent PR with sub-PRs, the normal sequence is:

1. Create or update the durable GitHub instruction on the parent PR or task file.
2. Worker creates a correction branch from the parent PR branch.
3. Worker opens a sub-PR back into the parent branch.
4. Review and merge the sub-PR into the parent branch.
5. Re-review the parent PR.
6. Repeat with `PR-X.2`, `PR-X.3`, etc. only if needed.
7. Merge the parent PR only after all required sub-PRs are resolved and TRACE evidence is consistent.

For post-merge cleanup, create a clean branch from current `origin/main` and change only the authorized cleanup files.

## 6. Squash-merge compatibility

Magna may use squash merge so a branch can contain many working commits while `main` receives one clean accepted commit. Sub-PR logical numbering is a TRACE/navigation convention and does not change GitHub's native PR numbering or squash-merge behavior.

## 7. Required stop conditions

Stop and ask the Product Owner when:

- a worker instruction exists only in chat and not in GitHub;
- a correction PR changes files outside its parent scope;
- a sub-PR targets `main` when it should target the parent branch;
- a new top-level PR is being created for work that is actually a parent PR correction;
- PR evidence claims completion while open questions remain;
- the active task status in `trace/ACTIVE_WORK_REGISTRY.yaml` conflicts with the PR state.
