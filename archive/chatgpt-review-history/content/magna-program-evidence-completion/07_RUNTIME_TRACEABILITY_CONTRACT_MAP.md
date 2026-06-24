# Runtime Traceability Contract Map

## Proposed interoperability contracts

| Magna runtime fact | TRACE engineering artifact | Contract rule |
|---|---|---|
| `event_id`, timestamp, type, source, actor | Light Curve command/finding evidence | Append-only reference; TRACE stores digest + repository-relative evidence locator, not mutable runtime prose |
| correlation/request/task/orchestration IDs | Task packet ID and mode history | Stable cross-plane IDs; one plane cannot silently mint authority in the other |
| workflow/approval transition | Validation and approval record | Preserve actor, policy version, decision, before/after state, causal parent |
| replay frame/state digest | Validation result | Independent verifier recomputes from durable events; runtime cannot self-mark “verified” |
| provider call metadata | Privacy/review evidence | Provider/model/config digest, local/cloud classification, consent reference; never secrets/full sensitive payloads by default |
| test/build command result | Raw evidence file | Command, cwd, exit code, environment version, start/end time, output digest, pre/post Git state |

## Separation rules

- Runtime plane answers “what Magna did.” Engineering plane answers “how the repository was changed and independently validated.”
- Runtime databases/logs remain operational data; TRACE task packets, decisions, diffs, and acceptance remain repository/governance evidence.
- Runtime may propose evidence links but cannot update acceptance, supersede decisions, close risks, or certify release readiness.
- TRACE must not ingest secrets, raw `.env`, unrestricted user prompts, or personal content merely to improve traceability.
- Evidence verification should be performed by a separate process/identity with read-only access to runtime facts and no ability to mutate them.

## Minimum schema

`trace_id`, `plane`, `event_id`, `task_id`, `correlation_id`, `causation_id`, `actor`, `source`, `occurred_at`, `artifact_uri`, `content_digest`, `policy_version`, `privacy_class`, `replay_safe`, `verification_status`, `verified_by`, `verified_at`. `verification_status` defaults to `unverified`; Magna cannot set it to `verified` for its own output.

