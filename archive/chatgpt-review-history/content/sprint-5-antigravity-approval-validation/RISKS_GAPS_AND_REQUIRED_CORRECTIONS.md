# RISKS_GAPS_AND_REQUIRED_CORRECTIONS.md
# Magna Enso — Sprint 5 Risks, Gaps, and Required Corrections

This independent validation has identified several security gaps and architectural risks. These are classified by severity (CRITICAL, HIGH, MEDIUM, LOW, INFO) and categorized as either **Blocking** (must be corrected before starting/implementing Sprint 5) or **Non-Blocking / Recommended** (can be resolved during implementation or as trace maintenance).

---

## 1. Blocking Corrections (Required before implementation approval)

### Gap 1: Simulated Approval Leakage in Non-Testing Runtimes (T-4 / D-7)
- **Severity:** **HIGH**
- **Description:** If the test-only `HumanDecisionProvider` mockup is not strictly isolated to test runtimes, a development or production environment might load it, allowing simulated approvals to authorize real capabilities without human consent.
- **Required Correction:** The implementation code MUST enforce that the test-only decision provider cannot be loaded under any non-testing configuration. The code should check the environment (e.g. assert `TESTING=True` is set) and raise an uncatchable initialization exception if loaded in other runtimes, causing the gate to default-deny.

### Gap 2: Weak Parameter and Argument Binding in Approval Matching (T-9)
- **Severity:** **HIGH**
- **Description:** If the approval coordinator matches an active approval using only `approval_id` or `capability_id`, a compromised capability could request approval for a safe action (e.g. terminal command `ls`), intercept the approved token, and use it to run an unsafe action (e.g. `rm -rf /`).
- **Required Correction:** The policy matching engine MUST validate that the invocation matches the approved request's *exact parameters, arguments, and scope* (specifically the `proposed_action` and `affected_resources` fields). Any parameter mismatch must invalidate the approval and resolve the gate to `DENY`.

### Gap 3: Weak Audit Log File Permissions (T-10 / D-8)
- **Severity:** **MEDIUM**
- **Description:** If the audit JSONL file is created with default OS file permissions, other local users or unprivileged processes could read or overwrite the log, bypassing integrity checks.
- **Required Correction:** The file store loader MUST create the audit log file with strict read/write permissions (e.g., `0600` or `0640` in Unix environments, restricted solely to the execution owner process). Any failure to set secure permissions must abort initialization and result in `DENY` for all capability requests.

---

## 2. Non-Blocking / Recommended Corrections

### Gap 4: Clock Expiry Drift and Uncertainty (T-9 / F-11)
- **Severity:** **MEDIUM**
- **Description:** If the system clock is manipulated, reordered, or drifts backward, expired approvals could appear valid.
- **Recommended Correction:** The coordinator should check timestamps against monotonic times where possible, and any backward clock drift or clock uncertainty must immediately invalidate active hold tokens and expire approvals, resolving to `DENY`.

### Gap 5: Minor Feature Tracker Linked Decisions Inconsistency (OQ-2)
- **Severity:** **INFO**
- **Description:** The `ENSO-F-0501` card template lists outdated decisions `EH-0012` and `EH-0013` as links instead of the capability governance design decision `EH-0014`.
- **Recommended Correction:** In the final Sprint 5 FEATURE_TRACKER update, change the linked decisions to **`EH-0014`**.
