# GOV-005-CLAUDE-REVIEW - Independent Four-Eyes Review

## Status

`AUTHORIZED_NOT_STARTED`

## Authority

- Product Owner: Vinay
- Instruction prepared by: ChatGPT / System Architect
- Product Owner approval: 2026-06-24
- Assigned worker: Claude
- Role: architecture specification and independent reviewer
- Parent issue: `#12`
- Review target: draft PR `#13`
- Review branch: `claude/GOV-005-four-eyes-review`
- Review PR base: `codex/GOV-005-multi-agent-governance`

This repository packet is the complete review instruction. The Product Owner launch message
only directs Claude to read and execute it.

## Required outcome

Independently determine whether GOV-005 is coherent, secure, enforceable, operationally
usable, and ready for Product Owner consideration. Review the actual repository state and
evidence without assuming the implementation or its validation claims are correct.

Assess whether the combined system reliably synchronizes status, supports non-overlapping
parallel work, grants useful bounded autonomy, preserves Product Owner authority, keeps
instructions outcome-oriented, controls downloads/system/external effects, prevents active
authority races, and produces dependable human- and machine-readable handoffs.

Select the review method independently. Investigate contradictions, bypasses, unsafe
permissions, ownership deadlocks, stale-state risks, schema/validator weaknesses,
unverifiable claims, and requirements that real workers could not follow consistently.

## Synchronization and branch

Before review:

1. Read `AGENTS.md`, `CLAUDE.md`, Issue #12, PR #13, this packet, the GOV-005 policy,
   registries, schemas, evidence, and applicable Event Horizon decisions.
2. Verify PR #13 is open/draft, Governance validation passes, and its head is not behind or
   inconsistent with its recorded base.
3. Verify no existing Claude review branch/PR or relevant unpushed local work conflicts.
4. Record `SYNC_PASS`, `SYNC_BLOCKED`, or `SYNC_UNVERIFIED_LOCAL_STATE`.

Only `SYNC_PASS` permits review execution. Create the assigned Claude branch from the
current verified PR #13 head. Register the review task in the active-work registry on that
branch with exact starting commit, owned paths, and integration order.

## Autonomous authority

Within this review envelope Claude may investigate, run validations and adversarial checks,
create review evidence, correct confirmed GOV-005 defects, update the review registry entry,
commit, push the assigned branch, and open/update a draft review PR targeting the GOV-005
implementation branch. Routine actions inside this envelope require no additional approval.

Approval remains required for credentials/private sources, paid services, privileged/global
system changes, destructive actions, access outside approved repository paths,
consequential external effects, material product-scope expansion, risk acceptance, or merge.

## Ownership and boundaries

Claude may:

- review all paths changed by PR #13;
- correct GOV-005 governance defects on its review branch;
- add review artifacts under `trace/reviews/GOV-005-CLAUDE-*`;
- add Claude handoffs under `trace/evidence/GOV-005-CLAUDE-*`; and
- update only its review entry in `trace/ACTIVE_WORK_REGISTRY.yaml`.

Claude must not:

- modify `trace/tasks/GOV-005.md` or this authorized review packet after execution starts;
- modify ARCH-001 content, runtime/product code, Sprint 5 implementation, policy-engine
  selection, Hermes activation, HELIX, or SGN-01;
- push to `main` or the GOV-005 implementation branch directly;
- merge, self-approve, close Issue #12, or mark GOV-005 accepted; or
- weaken a control merely to make validation pass.

Preserve every confirmed finding even when corrected.

## Required evidence

Produce findings-first review evidence ordered by severity and distinguish:

- confirmed defects;
- corrections made;
- nonblocking improvements;
- Product Owner judgment questions;
- controls verified as correct; and
- residual risks.

Provide:

- requirement-to-evidence assessment;
- correction record;
- exact validation results, including failures and skips;
- Markdown handoff using the repository template;
- schema-valid JSON handoff;
- concise Issue/PR summary with branch, commits, paths, validation, risks, and decisions.

Detailed evidence belongs in the repository. Chat output must remain concise and point
ChatGPT to the evidence paths.

## Completion

Commit and push the Claude review branch and open a draft PR targeting
`codex/GOV-005-multi-agent-governance`. Do not merge.

Return only synchronization verdict, review verdict, severity-ordered findings, corrections,
branch/final commit, review PR, validation summary, evidence/handoff paths, residual risks,
and Product Owner decisions required.
