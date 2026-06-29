# GOV-005 — Corrections Consolidated Status

## Purpose

This artifact is the current rollup status for PR #17 after the CF-5 child hardening flow was merged into `claude/GOV-005-corrections`.

It separates historical validation evidence from current correction state so GOV-005 keeps both backward and forward traceability without presenting stale findings as current truth.

## Scope

- Parent correction PR: PR #17 — `[claude] GOV-005 corrections (CF-1..CF-6)`
- Parent branch: `claude/GOV-005-corrections`
- Parent base: `codex/GOV-005-multi-agent-governance`
- Current parent head before this consolidation: `db20c4ef2a4b1f7c3a4d32d07d9480f5287185aa`
- Child hardening PR: PR #28 — `[claude] GOV-005-CF5 task-specific ownership hardening`
- Child validation PR: PR #31 — `[antigravity] GOV-005-CF5 independent validation`

## Traceability Rule

Historical evidence remains valid for the commit it inspected. A later correction does not erase that evidence; it supersedes it for current decision-making only when there is explicit correction and validation evidence.

The current decision status must therefore be read from this rollup plus the latest branch head, not from any single historical report in isolation.

## Finding Rollup

| Finding | Historical Evidence | Correction Evidence | Validation Evidence | Current Status |
|---|---|---|---|---|
| CF-1 | Claude corrections matrix | PR #17 correction set | Governance validator and CI workflow | RESOLVED |
| CF-2 | Claude corrections matrix | PR #17 correction set | Schema/policy/registry review | RESOLVED |
| CF-3 | Claude corrections matrix | PR #17 correction set | Validator status-vocabulary checks | RESOLVED |
| CF-4 | Claude corrections matrix | PR #17 correction set | Negative status tests | RESOLVED |
| CF-5 | `trace/reviews/GOV-005-ANTIGRAVITY-VALIDATION-REPORT.md` against old head `61098c0` found a bypass | PR #28 at `3a694ed835e625bc529ad834035f8bd826609546` hardened task-specific ownership | PR #31 accepted the CF-5 hardening | RESOLVED_PENDING_PARENT_CI |
| CF-6 | Claude corrections matrix | PR #17 correction set | Provenance negative tests | RESOLVED |

## CF-5 Supersession Chain

1. Antigravity validated PR #17 at old head `61098c04f7b98016a7ce17efc20cfa1d44bf7f6b` and found CF-5 still had a union-of-ownership / broad allowlist bypass.
2. Claude implemented focused CF-5 hardening in PR #28 on branch `claude/GOV-005-cf5-hardening`.
3. Antigravity independently validated the PR #28 fix in PR #31 and returned verdict `ACCEPT`.
4. PR #28 was merged into `claude/GOV-005-corrections`, producing parent head `db20c4ef2a4b1f7c3a4d32d07d9480f5287185aa`.
5. The old Antigravity report remains historical evidence for old head `61098c0`; it no longer represents the current CF-5 implementation after PR #28.

## Current PR #17 Integration Status

The CF-5 implementation is fixed at child-task level and independently validated. The remaining PR #17 blocker is integration traceability and parent-task ownership: the parent correction task must explicitly carry the child task and validation artifacts that are now part of the consolidated branch diff.

This consolidation updates the active work registry so the parent `GOV-005-CLAUDE-CORRECTIONS` envelope can carry the integrated child artifacts without weakening task-specific ownership globally.

## Current Decision

PR #17 should remain draft until governance CI passes on the consolidated parent branch and ChatGPT/System Architect completes one final review.

Do not merge PR #17 until:

- the consolidated status is present,
- the parent correction envelope authorizes integrated child artifacts,
- stale evidence is marked as historical/superseded,
- governance CI is green on the current PR #17 head,
- Product Owner explicitly authorizes merge.
