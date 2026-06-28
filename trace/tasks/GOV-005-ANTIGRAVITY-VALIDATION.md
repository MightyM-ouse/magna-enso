# GOV-005-ANTIGRAVITY-VALIDATION - Independent Correction Validation

## Status

`AUTHORIZED_NOT_STARTED`

## Authority

- Product Owner: Vinay
- Instruction prepared by: ChatGPT / System Architect
- Product Owner authorization: GOV-005 approved validation sequence
- Assigned worker: Antigravity
- Role: independent validator
- Parent issue: `#12`
- Correction PR under review: `#17`
- Exact correction baseline: `61098c04f7b98016a7ce17efc20cfa1d44bf7f6b`
- Assigned branch: `antigravity/GOV-005-corrections-validation`
- Validation PR base: `claude/GOV-005-corrections`

Antigravity did not author GOV-005 or the Claude corrections and is the independent
validator. This task authorizes validation evidence only, not implementation correction,
acceptance, or merge.

## Required outcome

Independently determine whether PR #17 safely and completely resolves CF-1 through CF-6,
including whether the controls work under adversarial conditions rather than merely passing
their own positive examples.

Do not assume Claude's correction claims or green CI are sufficient. Inspect the actual
workflow, validator, schema, registry, ownership checker, handoffs, negative tests, CI run,
and branch relationships. Select the validation method independently.

## Required validation areas

1. **CI enforcement**
   - Confirm stacked and `main` PR triggers behave as claimed.
   - Confirm CI actually runs the substantive validator and ownership checker.
   - Confirm a deliberately invalid contract causes CI-equivalent validation failure.
   - Assess dependency pinning, provenance, and failure behavior.

2. **Status and synchronization**
   - Confirm one live status authority and truthful roles for immutable packet, Star Map,
     registry, and handoff snapshots.
   - Confirm commit-pointer semantics cannot be mistaken for live freshness.
   - Confirm no current record contradicts the correction baseline.

3. **Schema and provenance**
   - Confirm out-of-vocabulary status is rejected.
   - Confirm pending review cannot claim a completed reviewer.
   - Confirm completed review requires valid reviewer evidence.
   - Determine whether every governed JSON handoff is validated, not only one example.
   - Confirm the schema and validator agree.

4. **Ownership enforcement**
   - Confirm all 14 correction paths are authorized.
   - Test that runtime/product and another active task's owned paths are rejected.
   - Specifically test whether the union-of-ownership and broad governance allowlist permit
     one task to alter another task's task packet, review, handoff, evidence, or governance
     files. Treat such a bypass as a material finding.
   - Assess whether branch/task-specific ownership is required before merge.

5. **Scope and integrity**
   - Confirm immutable `trace/tasks/GOV-005.md`, merged Claude review evidence, GOV-006,
     runtime/product, ARCH-001, Sprint 5, Hermes, HELIX, and SGN-01 were untouched.
   - Confirm exact failures/skips and the initial failed CI attempt remain visible.
   - Confirm no secret, private path, binary dependency, or unapproved host change exists.

## Synchronization gate

Before validation:

1. Verify PR #17 is open/draft, targets `codex/GOV-005-multi-agent-governance`, and head is
   exactly `61098c04f7b98016a7ce17efc20cfa1d44bf7f6b`.
2. Verify Governance run `28130377771` completed successfully for that head.
3. Verify this assigned branch contains this packet and no conflicting Antigravity
   validation branch/PR or relevant unpushed work exists.
4. Record `SYNC_PASS`, `SYNC_BLOCKED`, or `SYNC_UNVERIFIED_LOCAL_STATE`.

Only `SYNC_PASS` permits validation. If PR #17 moves, stop and resynchronize rather than
reviewing a stale baseline.

## Ownership and boundaries

Antigravity may:

- inspect all PR #17 changes and related canonical governance evidence;
- run local/adversarial validation in an isolated environment;
- add validation artifacts under `trace/reviews/GOV-005-ANTIGRAVITY-*`;
- add Markdown/JSON handoffs under `trace/evidence/GOV-005-ANTIGRAVITY-*`;
- register only its own validation task entry; and
- commit/push only its assigned branch and open/update its draft validation PR.

Antigravity must not:

- correct the implementation it independently validates;
- modify PR #17, the GOV-005 implementation branch, or `main`;
- modify immutable task packets or historical Claude review/correction evidence;
- modify GOV-006, runtime/product code, ARCH-001, Sprint 5, Hermes, HELIX, or SGN-01;
- merge, self-approve, close Issue #12, or mark GOV-005 accepted.

No additional approval is required for routine validation inside this envelope. Stop for
credentials/private sources, paid services, privileged/global changes, destructive actions,
external effects, scope expansion, risk acceptance, or merge.

## Required evidence

Produce findings first, ordered by severity, and distinguish:

- confirmed correction;
- incomplete correction or bypass;
- nonblocking hardening;
- verified positive control;
- residual risk; and
- Product Owner decision.

Provide:

- CF-1 through CF-6 validation matrix;
- adversarial test record with commands, expected result, actual result, and exit status;
- CI/workflow evidence;
- changed-path and protected-boundary proof;
- Markdown and schema-valid JSON handoffs; and
- concise Issue/PR summary for ChatGPT review.

Preserve all failures and skipped checks. Detailed evidence belongs in the repository.

## Completion

Commit and push the assigned Antigravity branch and open a draft PR targeting
`claude/GOV-005-corrections`. Do not merge.

Return only synchronization verdict, validation verdict, severity-ordered findings,
CF-1..CF-6 disposition, branch/final commit, draft PR, validation evidence paths, residual
risks, and Product Owner decisions required.
