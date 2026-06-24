# CLOCK_AND_RECOVERY_REVALIDATION.md
# Magna Enso — Sprint 5 Clock Handling and Recovery Targeted Security Revalidation

## 1. Validation Findings: Clock Handling and Recovery

The corrected approval package defines secure time-handling and recovery invariants in `FAILURE_MODES_AND_FAIL_CLOSED_BEHAVIOR.md` §3aa.

### Key Points Confirmed:
- **Process-Bound Monotonic Expiry:** For in-flight capability evaluations and approvals, expiration duration is tracked using process-bound monotonic time (`time.monotonic` in Python stdlib). This isolates expiry math from system-wide wall-clock adjustments.
- **Restart Invalidation:** A process restart resets the system's monotonic clock reference. Because monotonic values are process-bound, all pending approvals/HOLDs are discarded upon restart. Monotonic timestamps are never written to disk or expected to survive a restart. The system returns to a clean default-deny state, preventing replay attacks across process cycles.
- **Wall-clock as Evidence Only:** Wall-clock timestamps are written to the JSONL log records for human-readable audit purposes only. They are never used by the coordinator to calculate expiration.
- **Clock Rollback and Uncertainty Handling:** If monotonic timing becomes unavailable or exhibits inconsistent behavior, the coordinator invalidates the hold token and returns `DENY`.
- **Reconstruction Invariant:** On startup, approval states are rebuilt from the durable audit log. The log is the recovery source of truth, and any in-flight requests that did not commit an ALLOW record prior to the crash are resolved to `DENY`.
