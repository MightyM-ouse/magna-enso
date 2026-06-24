# AUDIT_DURABILITY_AND_RECOVERY_VALIDATION.md
# Magna Enso — Sprint 5 Audit Durability and Recovery Independent Validation

## 1. Audit Invariant: Ordering and Durability

The core invariant of the governance system is: **No ALLOW without a durable, flushed audit record.**

### Ordering Sequence:
The policy engine enforces a strict write sequence:
1. Matched capability request evaluated ⇒ provisional `ALLOW` or `HOLD`.
2. Structured audit record constructed (including timestamps, parameters, hashes).
3. Record appended to the JSONL log file.
4. Record flushed to disk using explicit flush and sync (`fsync`).
5. **Only upon successful sync** is the `ALLOW` returned to the gate to permit capability execution.

If the sync fails (disk full, write permission error, lock timeout), the process aborts, and the gate returns `DENY`.

## 2. Crash Windows Analysis

We adversarially map the behavior of the system across different crash windows:

### Scenario A: Crash *before* the audit record is durably written
- **State:** The capability evaluation was performed (possibly hold/allow), but the process crashed before the write completed or flushed.
- **Recovery:** Upon restart, the audit log contains no record of allowance. Since there is no record, default-deny holds. No capability was executed. The state remains clean and safe.

### Scenario B: Crash *after* the audit record is written, but *before* the ALLOW is returned
- **State:** The log contains a record indicating an approval was consumed and an ALLOW was authorized, but the caller crashed before it could actually execute the capability.
- **Recovery:** On restart, the log reconstruction reads that the approval was already consumed. The approval is exhausted and cannot be replayed. The caller is blocked and must request a fresh approval. This is fail-closed and prevents authorization leakages.

### Scenario C: Crash *during* the file write (partial append)
- **State:** The file contains a trailing, incomplete line (malformed JSONL tail).
- **Recovery:** On startup, the log loader detects the malformed tail, alerts the administrator, truncates/quarantines the invalid trailing bytes, and defaults to `DENY` for any in-flight decisions.

## 3. Concurrency, Serialization, and Reordered Logs

- **Race Conditions:** Under concurrent calls, if records are written out of order, the hash-chain will break. The design requires a single-writer lock around all writes. The append to JSONL and the update of the hash-chain head must be executed inside a single, synchronized critical section.
- **Lock Contention:** If the lock cannot be acquired or fails, the operation immediately aborts with `DENY`. No "best-effort" unlogged writes are allowed.

## 4. Hash-Chain Integrity and Limitations

The design incorporates a hash-chain where each record `N` contains a cryptographic hash of the entire content of record `N-1`.

### What the Hash-Chain Proves:
- It guarantees the **sequential integrity** of the log. An attacker cannot insert, delete, or reorder historical records without breaking the chain.
- It detects **accidental corruption** or simple offline file modifications.

### What the Hash-Chain does NOT Protect Against (Limitations):
- **Local Root Administrator Modification:** Since the keys and code used to calculate the hash-chain reside locally, a local administrator (or a worker running with root/filesystem write privileges) can modify the log file and recalculate the hash-chain from that point forward to match.
- **Log Erasure:** An administrator can delete the entire log file, forcing the engine to recover to a blank state. (Though this is detected as a clean restart, resetting all states to default-deny, it destroys historical audit records).

These limitations are honestly documented in D-8 and §3a. The log is **integrity-detecting, not tamper-proof**. Implementing a signed, remote, or tamper-evident audit store is deferred.
