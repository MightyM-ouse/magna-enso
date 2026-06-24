# 05 — Policy Security and Bypass Review

This report documents an adversarial security review of both policy approaches: the integrated Command Center risk policy engine and the standalone Magna Enso Sprint 5 policy control harness.

## 1. Command Center Policy Engine Vulnerabilities

We conducted direct adversarial checks against the Command Center's [risk_policy_engine.py](file://<LOCAL_USER_HOME>/Projects/AI/magna-command-center/backend/app/services/risk_policy_engine.py) and discovered critical security vulnerabilities:

### A. Directory Traversal via Relative Paths (CRITICAL)
The path assessment function `_assess_path` contains a logical flaw: any path that does not start with a slash `/` is automatically classified as a relative path and assigned to `WorkspaceZone.APPROVED` inside the project root context.
Because the engine does not resolve paths to their canonical absolute forms (e.g. using `os.path.abspath` or `Path.resolve()`), relative paths that escape the project root (using `..` segments) bypass all folder restrictions.
* **Adversarial Proof:**
  - Path: `../../../../etc/passwd` -> Evaluated as: `Zone=APPROVED`, `Effective Tier: 1` (Auto Proceed), `Blocked: False`, `Approval Required: False`.
  - Path: `../../PrivateVault/secret.txt` -> Evaluated as: `Zone=APPROVED`, `Effective Tier: 1` (Auto Proceed), `Blocked: False`, `Approval Required: False`.
* **Impact:** An agent or compromised worker can read/modify files outside the workspace simply by referencing them via relative paths.

### B. Regex Bypass for Sensitive Targets
The engine relies on regular expressions to identify destructive operations and sensitive file access.
* **Adversarial Proof:**
  - Prompt: `cat .e'nv'` -> Evades the `.env` regex (`(?<!example)\.env(?:\.[A-Za-z0-9_-]+)?\b`), returning `Effective Tier: 1` (Auto Proceed) and `Blocked: False`.
  - Prompt: `unlink the system configurations` -> Evades the delete regex (`rm\s+-rf\|delete\|remove\|wipe\|erase\|trash\|purge`), returning `Effective Tier: 0` (Introspection/Safe) and `Blocked: False`.
* **Impact:** Sophisticated prompts can evade deterministic pattern-matching filters by using shell quoting, variable splits, or synonyms (e.g., `unlink` instead of `delete`).

### C. Loopback Trust Assumption
The authorization system automatically trusts all loopback requests without requiring a session token (returning a synthetic local operator context). If another process or unauthorized local user can interact with loopback, they gain full administrative access without authentication.

---

## 2. Magna Enso Policy Engine Vulnerabilities

The Enso Sprint 5 engine offers stronger isolation and parameter binding but introduces several structural risks:

### A. Same-User Audit Tampering (Tamper-Detecting, NOT Tamper-Proof)
The [audit.py](file://<MAGNA_LOCAL_ROOT>/magna-enso/policy/audit.py) module checks that the audit log file is owned by the process user and has `0600` permissions. It also uses a SHA-256 hash chain to verify record integrity.
* **Vulnerability:** While this prevents other regular OS users from reading/modifying the log, it provides no protection against code running as the *same* OS user. A compromised runner process or local script can write directly to the file, delete records, and recalculate the SHA-256 hash chain, making the edit look completely valid to the verifier.
* **Impact:** The log is tamper-detecting only under off-host verification; same-user tampering cannot be prevented locally.

### B. In-Memory Pending Approvals (Denial of Service on Restart)
Pending approvals are stored entirely in volatile RAM.
* **Vulnerability:** MONOTONIC clocks discard pending states on process restart. If the server restarts or crashes, all active user workflows awaiting approval are permanently lost.

### C. Inert Harness Bypass
Enso's policy engine is a standalone harness and does not execute capabilities.
* **Vulnerability:** If integrated, it lacks a unified runtime gateway. If developers call capability APIs directly without wrapping them in the `CapabilityGate` check, Enso is bypassed entirely.

---

## 3. Comparative Summary

| Scenario | Command Center | Magna Enso Sprint 5 |
| :--- | :--- | :--- |
| **Path Handling** | **Vulnerable** (relative paths bypass checks via directory traversal) | **Secure** (canonicalizes paths under approved roots) |
| **Regex Evading** | **Vulnerable** (simple string split/quoting evades regex) | **Secure** (uses canonical schemas and parameters) |
| **Replay/State Swap** | **Vulnerable** (no cryptographic binding of parameters) | **Secure** (SHA-256 fingerprint binds all request parameters) |
| **State on Restart** | **Durable** (persists state in SQLite) | **Vulnerable** (discards all pending approvals) |
| **Audit Log Integrity** | **Basic** (SQLite logs; no cryptographic chain) | **Hardened** (restrictive file check + SHA-256 chain) |

## 4. Required Security Integration Experiment

Do not select a canonical engine yet. To resolve these gaps, a controlled security experiment is recommended:
1. Define a benchmark suite containing:
   - Traversal paths (e.g. `../../PrivateVault`)
   - Split string evaders (e.g. `rm -r''f`)
   - Replay attempts and token reuse
   - Interrupted runs (process restart during HOLD state)
2. Implement adapters routing this suite through both engines.
3. Compare the outcomes: Command Center will likely fail on path and regex checks, while Enso will fail on rehydration/durability.
4. Vinay must choose whether to combine the durability of Command Center with the strict cryptographic validation of Enso.
