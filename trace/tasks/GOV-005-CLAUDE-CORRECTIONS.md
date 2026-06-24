# GOV-005-CLAUDE-CORRECTIONS - Resolve Confirmed Governance Findings

## Status

`AUTHORIZED_NOT_STARTED`

## Authority

- Product Owner: Vinay
- Instruction prepared by: ChatGPT / System Architect
- Product Owner authorization: 2026-06-24
- Assigned worker: Claude
- Role for this task: correction implementer (not independent validator)
- Parent issue: `#12`
- Correction baseline: GOV-005 implementation branch after merged PR #16
- Correction branch: `claude/GOV-005-corrections`
- Correction PR base: `codex/GOV-005-multi-agent-governance`
- Independent validator after correction: Antigravity

Claude identified the findings during independent review. This separate task authorizes Claude
to implement corrections. Claude must not independently approve its own corrections.

## Required outcome

Resolve CF-1 through CF-5 from
`trace/reviews/GOV-005-CLAUDE-FOUR-EYES-REVIEW.md` and the additional ChatGPT-confirmed
handoff-provenance defect, producing a coherent and enforceable GOV-005 correction set.

Select the correction method independently after inspecting the current merged review
baseline. Preserve the accepted principles of immutable task authority, Product Owner merge
authority, bounded agent autonomy, repository-native instructions, and independent review.

## Findings in scope

1. **CF-1:** GOV-005 validation is not enforced by CI, and stacked task/review PRs do not
   receive equivalent governance validation.
2. **CF-2:** commit-pointer fields drift from the live branch head and currently imply
   stronger freshness than they can guarantee.
3. **CF-3:** live status disagrees across task packet, active registry, handoff, and Star Map.
4. **CF-4:** handoff task status is unconstrained and not cross-checked against the governed
   status vocabulary.
5. **CF-5:** GOV-005 handoff files are outside declared writable ownership.
6. **CF-6:** handoff provenance claims `reviewed_by: ChatGPT / System Architect` before the
   review actually occurs.

Also address the directly related nonblocking weaknesses where necessary:

- validator dependency/reproducibility;
- git-aware changed-path ownership enforcement;
- semantics for implementation/evidence commits that avoid impossible self-reference; and
- validation of stacked PRs without weakening protected-`main` controls.

## Acceptance criteria

1. CI runs the substantive GOV-005 validator and fails on a real contract violation.
2. Governance validation applies to PR #13 and relevant stacked correction/review PRs.
3. Required GOV-005 files are explicitly checked by CI.
4. The live GitHub branch head remains the synchronization authority; repository commit
   fields have truthful, testable semantics and do not claim impossible self-reference.
5. One canonical live task-status authority is defined. Immutable task status, Star Map
   summary, and handoff status have explicit roles/mapping.
6. Registry and handoff statuses use an enforced vocabulary.
7. Schema and validator reject an out-of-vocabulary task status.
8. All GOV-005 changed files are covered by declared ownership, and a git-aware check detects
   unauthorized changed paths.
9. Handoff provenance distinguishes intended reviewer from completed review. No artifact
   claims a review before evidence exists.
10. Existing Claude findings remain unchanged as historical review evidence.
11. No runtime, product, Sprint 5, policy-engine, Hermes activation, HELIX, SGN-01, or
    ARCH-001 implementation is changed.
12. Exact failures, skipped checks, dependencies, downloads, and residual risks are recorded.

## Synchronization and ownership

Before editing:

1. Verify PR #16 is merged and PR #13 is open/draft.
2. Verify the implementation branch head equals the commit containing this packet and is not
   behind `main`.
3. Verify no existing correction branch/PR or conflicting local work.
4. Record `SYNC_PASS`, `SYNC_BLOCKED`, or `SYNC_UNVERIFIED_LOCAL_STATE`.

Only `SYNC_PASS` permits execution. Create the assigned branch from the verified current
implementation head and register the correction task on that branch.

Claude may modify only the files needed to satisfy the findings, including:

- governance CI workflow and an appropriately scoped dependency declaration;
- GOV-005 validator and handoff schema;
- active-work registry and GOV-005 handoffs/status summaries;
- handoff/task templates and multi-agent policy where semantics require clarification;
- GOV-005 Light Curve;
- new Claude correction evidence/handoffs; and
- this correction task's active-work entry.

Do not modify the immutable original `trace/tasks/GOV-005.md`, the merged Claude review
report/handoffs, GOV-006 files, runtime/product code, ARCH-001, Sprint 5, Hermes activation,
HELIX, or SGN-01.

## Autonomous authority

Within this envelope Claude may investigate, select the solution, modify authorized files,
add a narrowly scoped governance dependency, run tests, make corrective iterations, commit,
push the assigned branch, and open/update a draft correction PR. Routine actions require no
additional approval.

Stop for credentials/private sources, paid services, privileged/global system changes,
destructive actions, access outside approved repository paths, consequential external
effects, material product-scope expansion, risk acceptance, or merge.

## Required evidence

Produce:

- a finding-to-correction matrix for CF-1 through CF-6;
- negative tests proving invalid status, ownership, provenance, or CI contract cases fail;
- exact local and GitHub CI results;
- dependency/download provenance when applicable;
- Markdown and schema-valid JSON correction handoffs; and
- a concise Issue/PR summary for ChatGPT and Product Owner review.

## Completion

Commit and push `claude/GOV-005-corrections` and open a draft PR targeting
`codex/GOV-005-multi-agent-governance`. Do not merge or self-approve.

Return only synchronization verdict, correction verdict, findings resolved/unresolved,
branch/final commit, draft PR, validation evidence, changed paths, residual risks, and
decisions required.
