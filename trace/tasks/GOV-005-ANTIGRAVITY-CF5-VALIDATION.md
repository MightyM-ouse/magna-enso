# GOV-005-CF5 — Antigravity Independent Validation

Status: `PLANNED`
Issue: #26
Agent: Antigravity
Validation target PR: #28
Validation target branch: `claude/GOV-005-cf5-hardening`
Validation target base: `claude/GOV-005-corrections`
Target head expected at launch: `3a694ed835e625bc529ad834035f8bd826609546`
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before merge

## Purpose

Perform an independent validation of Claude's GOV-005 CF-5 hardening in PR #28.

This task is validation-only. Antigravity must not implement fixes unless explicitly authorized after reporting findings.

## Context

GOV-005 remains blocked until CF-5 is proven hardened.

Previous issue: ownership validation could allow broad governance directories or a union of active task writable paths. That meant one task could potentially modify another task's files.

Claude claims PR #28 fixes this by:

- identifying one accountable active task from the PR head branch,
- validating only that task's writable paths, shared paths, declared correction-phase paths, and self-registration file,
- removing union-of-all-active-task authorization,
- removing broad directory allowlist override,
- failing closed on missing, ambiguous, unregistered, or inactive task identity,
- validating every changed governed handoff JSON file,
- adding adversarial tests.

Antigravity must verify these claims independently.

## Required synchronization before analysis

Antigravity must perform and report these checks before validation:

1. Confirm repository: `MightyM-ouse/magna-enso`.
2. Fetch all relevant branches.
3. Confirm PR #28 exists and targets `claude/GOV-005-corrections`.
4. Confirm PR #28 head is `claude/GOV-005-cf5-hardening`.
5. Confirm target head SHA or report if it moved.
6. Confirm governance CI status for PR #28.
7. Confirm local working tree is clean before any local validation.
8. Do not merge PR #28.

If synchronization fails, stop and report `SYNC_BLOCKED`.

## Validation questions

Antigravity must answer these questions with evidence:

1. Does the checker validate against the active task only, not a union of all active tasks?
2. Can task A still modify task B evidence, handoff, task packet, or review files?
3. Do broad governance directories bypass task-specific ownership?
4. Does the checker fail closed when task identity is missing?
5. Does the checker fail closed when task identity is ambiguous?
6. Does the checker fail closed when task identity is unregistered or inactive?
7. Are all changed governed handoff JSON files validated, not only a hard-coded handoff?
8. Are arbitrary or out-of-vocabulary handoff statuses rejected?
9. Are correction-phase exceptions narrow and justified?
10. Do the tests prove the safety behavior, or are they superficial/self-fulfilling?

## Required inspection targets

At minimum, inspect:

```text
.github/workflows/governance-validation.yml
scripts/check_changed_path_ownership.py
tests/test_changed_path_ownership.py
trace/ACTIVE_WORK_REGISTRY.yaml
docs/governance/MULTI_AGENT_EXECUTION_POLICY.md
trace/evidence/GOV-005-CF5-HANDOFF.md
trace/evidence/GOV-005-CF5-HANDOFF.json
trace/reviews/GOV-005-CF5-CORRECTION-REPORT.md
trace/tasks/GOV-005-CLAUDE-CF5-HARDENING.md
```

## Required validation actions

Antigravity must run or simulate the strongest available validation. At minimum:

1. Review PR #28 changed files.
2. Review ownership checker logic.
3. Review adversarial tests.
4. Run governance validation if possible.
5. Run ownership checker tests if possible.
6. Create at least one independent adversarial scenario or reasoned check for each CF-5 risk.

Preferred commands, if compatible with repository state:

```text
python scripts/validate_multi_agent_governance.py
python scripts/check_changed_path_ownership.py --branch claude/GOV-005-cf5-hardening
python -m pytest tests/test_changed_path_ownership.py
```

If commands require different arguments, inspect script help/source and run the appropriate equivalent.

## Output requirements

Antigravity must create a validation report and handoff evidence.

Allowed output files only:

```text
trace/reviews/GOV-005-CF5-ANTIGRAVITY-VALIDATION.md
trace/evidence/GOV-005-CF5-ANTIGRAVITY-HANDOFF.md
trace/evidence/GOV-005-CF5-ANTIGRAVITY-HANDOFF.json
```

Do not modify Claude's implementation files, validators, workflows, policy, registry, tests, task packet, runtime, product code, ARCH-001, PAR-001, Hermes, or main.

## Verdict values

Use one of:

```text
ACCEPT
ACCEPT_WITH_NON_BLOCKING_NOTES
CHANGES_REQUIRED
REJECT
```

Use `CHANGES_REQUIRED` if any CF-5 safety property is not proven or if a bypass remains possible.

Do not call a blocking safety finding non-blocking.

## Report content

The validation report must include:

- validated PR number and head SHA,
- branch/base checked,
- files inspected,
- commands run and results,
- answers to each validation question,
- adversarial checks performed,
- verdict,
- blocking findings,
- non-blocking notes,
- residual risks,
- recommendation to ChatGPT/System Architect.

## PR requirements

Antigravity must:

1. Create/use branch `antigravity/GOV-005-cf5-validation`.
2. Base it on `claude/GOV-005-cf5-hardening` or another appropriate branch only if required for validation evidence.
3. Commit only validation output files listed above.
4. Open a draft PR targeting `claude/GOV-005-cf5-hardening`.
5. Do not merge.
6. Return short final chat summary with:
   - branch,
   - final commit,
   - draft PR link,
   - changed files,
   - validation commands,
   - verdict,
   - blocking findings if any.

## Stop conditions

Stop and report `STOP_REQUIRED` if:

- PR #28 cannot be found,
- PR #28 head moved unexpectedly and cannot be reconciled,
- local worktree is dirty before validation,
- validation requires modifying implementation files,
- Antigravity finds a safety bypass that requires immediate correction,
- validation commands cannot be run and no equivalent evidence can be produced.

## Acceptance gate

PR #28 must not be merged until:

1. Antigravity validation PR is opened.
2. Governance CI passes on Antigravity validation PR.
3. ChatGPT/System Architect reviews Antigravity findings.
4. Product Owner authorizes the next merge.
