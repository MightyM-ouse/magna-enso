# Policy Engine Comparative Audit

## Comparison

| Property | Command Center | Magna Enso Sprint 5 |
|---|---|---|
| Scope | Integrated runtime services and API surfaces | Standalone, inert decision harness |
| Default behavior | Deterministic risk-tier classifier; execution stays false in classification results | Missing policy/path/schema/provider/audit errors deny |
| Fail closed | Strong for known classifier/approval paths, but not a universal capability chokepoint | Explicit at evaluator/gate boundaries; real entry-point completeness unproved |
| Approval binding | Durable approval records, lifecycle transitions, auth context, workflow/orchestration lineage | SHA-256 fingerprint binds invocation, parameters, resources, caller, policy, nonce, expiry; single use |
| Persistence/restart | SQLite approval/event state and restart rehydration | Pending approvals intentionally memory-only and discarded on restart |
| Audit integrity | Redacted durable event archive/replay; no cryptographic chain in the inspected path | `0600`, owner/regular-file checks, lock/fsync, sequence + SHA-256 chain; detects but cannot prevent same-user tampering |
| Replay | Event-bus archive, correlation, replay, runtime reconstruction | Approval replay denied; audit records readable/verified; no runtime replay |
| Runtime coupling | High: FastAPI, SQLModel, workflows, auth, event bus | Low: standard-library package, no runtime dependencies |
| Test maturity | Current 701-test suite passes; policy/approval/auth/replay coverage included | 49 unittest cases pass; pytest collection is broken; no real runtime integration |
| Reuse value | Durable lifecycle, integration patterns, authorization and lineage | Strict schema/canonicalization, fingerprint binding, secure audit sink, compact fail-closed evaluator |

Direct symbols: Command Center `services/risk_policy_engine.evaluate_policy`, `core.approval_engine.ApprovalEngine`, `services.authorization_service.resolve_auth_context`, `core.audit_logger.store_envelope`, `core.event_bus.InProcessEventBus.replay`; Enso `schema.load_policy_records`, `canonical.build_fingerprint`, `evaluator.PolicyEvaluator.evaluate`, `approval.ApprovalCoordinator.consume`, `audit.SecureAuditSink`, `gate.CapabilityGate.authorize`.

## Missing controls

Command Center lacks evidence that every capability entry point passes through one canonical gate and lacks Enso-style invocation fingerprinting/hash-chained audit. Enso lacks authenticated human decision input, durable pending approvals, restart continuation, actual capability execution integration, an exhaustive entry-point inventory, and a passing standard pytest collection path.

## Canonical decision

Do not select a canonical engine yet. Required experiment: define one representative read-only, one local-write, and one external/approval-required capability contract; route each through adapters for both engines; test parameter substitution, replay, restart, audit failure, direct-entry bypass, and authorization identity; compare evidence and operational coupling. Vinay must then choose whether to compose, adapt, or replace. The first package’s recommendation to make Enso canonical was premature.

