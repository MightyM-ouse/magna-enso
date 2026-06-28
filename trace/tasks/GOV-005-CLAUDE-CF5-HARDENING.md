# GOV-005-CF5 — Claude Task-Specific Ownership Hardening

Status: `PLANNED`
Issue: #26
Agent: Claude
Assigned branch: `claude/GOV-005-cf5-hardening`
Required base branch: `claude/GOV-005-corrections`
Target PR base: `codex/GOV-005-multi-agent-governance`
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before merge

## Purpose

Harden GOV-005 CF-5 so multi-agent governance validates changed paths against the specific active task identity, not a broad union of all active task permissions.

This is a focused correction task. It must not broaden GOV-005 scope, rewrite unrelated governance, or modify runtime/product behavior.

## Required synchronization before editing

Claude must perform and report these checks before any source edits:

1. Confirm repository: `MightyM-ouse/magna-enso`.
2. Confirm current local branch and remote state.
3. Fetch all relevant branches.
4. Confirm `claude/GOV-005-corrections` exists and is the required base.
5. Create or update only `claude/GOV-005-cf5-hardening` from `claude/GOV-005-corrections`.
6. Inspect open PRs #13, #17, and #24 history context only as evidence; do not modify them directly.
7. Confirm working tree is clean before edits.
8. Produce a short pre-implementation note in chat before changing files.

If synchronization fails or the base branch is not available, stop and report `SYNC_BLOCKED`.

## Problem to solve

Previous review found CF-5 remains incomplete because the ownership checker can still allow broad governance directories and appears to evaluate writable paths as a union of active task permissions.

The corrected behavior must be:

- identify one accountable task for the current change set,
- load only that task's allowed writable paths,
- reject paths outside that task's exact envelope,
- fail closed when task identity is missing, ambiguous, stale, or inconsistent,
- validate governed handoff files that changed in the PR,
- include adversarial tests proving cross-task edits are rejected.

## Outcome requirements

Claude must implement a minimal, focused correction that satisfies all of the following:

1. **Task-specific ownership**
   - Changed paths are checked against the writable paths for the active task only.
   - The validator must not accept a union of writable paths from multiple active tasks.
   - Broad directory allowances must not override explicit task ownership.

2. **Fail-closed identity detection**
   - Missing task identity fails.
   - Multiple candidate task identities fail unless an explicit, validated exception exists.
   - A task identity that is not active or not registered fails.
   - Branch/task mismatch fails unless explicitly allowed by the GOV-005 policy.

3. **Governed handoff validation**
   - Every changed governed handoff file must be validated, not only a hard-coded or original GOV-005 handoff.
   - Handoff validation must reject arbitrary status values if the schema or policy restricts them.
   - Handoff files changed outside the active task envelope must fail.

4. **Adversarial test coverage**
   Add or update tests proving:
   - task A cannot edit task B handoff/evidence paths,
   - a change set cannot pass by combining writable paths from multiple tasks,
   - broad governance directories do not bypass task-specific ownership,
   - missing/ambiguous task identity fails,
   - changed governed handoff files are all validated.

5. **Minimal surface**
   - Do not redesign GOV-005.
   - Do not change non-CF-5 policy behavior unless required to make CF-5 enforceable.
   - Do not touch runtime code, product code, ARCH-001, PAR-001 evidence, HERMES activation, SGN-01, or Sprint 5.

## Allowed paths

Claude may modify only paths required for CF-5 hardening within these areas:

```text
.github/workflows/governance-validation.yml
scripts/check_changed_path_ownership.py
scripts/validate_multi_agent_governance.py
scripts/governance-requirements.txt
docs/governance/MULTI_AGENT_EXECUTION_POLICY.md
trace/ACTIVE_WORK_REGISTRY.yaml
trace/ROLE_REGISTRY.yaml
trace/WORKFLOWS.yaml
trace/schemas/**
trace/tasks/GOV-005-CLAUDE-CF5-HARDENING.md
trace/evidence/GOV-005-CF5-*.md
trace/evidence/GOV-005-CF5-*.json
trace/reviews/GOV-005-CF5-*.md
tests/**
```

If another path appears necessary, stop and request Product Owner approval before editing it.

## Protected paths

Claude must not modify:

```text
backend/**
frontend/**
src/**
archive/**
vendor/**
trace/tasks/PAR-001-PARALLEL-TASK-PACKET-INDEX.md
trace/tasks/REPO-001-CODEX-INVENTORY.md
trace/tasks/ARCH-001A-CLAUDE-SOURCE-CLASSIFICATION.md
trace/tasks/ARCH-001V-ANTIGRAVITY-ARCHIVE-VALIDATION.md
trace/tasks/HERMES-001-SANDBOX-READINESS.md
trace/reviews/REPO-001-INVENTORY-REPORT.md
trace/reviews/HERMES-001-SANDBOX-READINESS.md
trace/reviews/ARCH-001-SOURCE-CLASSIFICATION.md
trace/reviews/ARCH-001-ARCHIVE-VALIDATION-REPORT.md
trace/evidence/REPO-001-*
trace/evidence/HERMES-001-*
trace/evidence/ARCH-001-*
docs/architecture/**
docs/technical-specifications/**
```

## Required implementation evidence

Claude must create or update:

```text
trace/evidence/GOV-005-CF5-HANDOFF.md
trace/evidence/GOV-005-CF5-HANDOFF.json
trace/reviews/GOV-005-CF5-CORRECTION-REPORT.md
```

The handoff must include:

- branch name,
- base branch and base SHA,
- final head SHA,
- changed files,
- tests run,
- governance validation result,
- CF-5 findings addressed,
- residual risks,
- Product Owner decisions required.

## Validation requirements

Claude must run the strongest available local validation. At minimum:

```text
python scripts/validate_multi_agent_governance.py
python scripts/check_changed_path_ownership.py
```

If scripts require arguments, Claude must inspect their help/source and run the appropriate PR/change-set validation mode.

Claude must also run the relevant test suite for the ownership checker and handoff validation. If no tests exist, Claude must add focused tests and run them.

## PR requirements

Claude must:

1. Commit only to `claude/GOV-005-cf5-hardening`.
2. Open a draft PR targeting `claude/GOV-005-corrections` unless a different base is explicitly required by repository state.
3. Mark the PR description with `CF-5 focused hardening`.
4. Do not merge.
5. Do not close issue #26.
6. Return a short final chat summary with:
   - branch,
   - final commit,
   - draft PR link,
   - validation result,
   - evidence paths,
   - residual risks.

## Stop conditions

Claude must stop and report `STOP_REQUIRED` if:

- the working tree is dirty before edits,
- the required base branch cannot be found,
- CF-5 changes require protected paths,
- validation cannot be run,
- changes would alter runtime/product behavior,
- another agent branch has moved in a way that changes the task base.

## Acceptance gate

This task is not accepted until:

1. Claude opens the draft PR.
2. Governance CI passes.
3. ChatGPT/System Architect reviews the changed files.
4. Antigravity performs a focused CF-5 validation.
5. Product Owner authorizes merge into the GOV-005 correction path.
