# HUMAN_AUTHORITY_BOUNDARY_VALIDATION.md
# Magna Enso — Sprint 5 Human Authority and Approval Boundary Validation

## 1. Adversarial Challenge: Simulated vs. Authenticated Authority

A critical risk in any policy engine is that test stubs or mockups might be mistaken for real authenticated authority:

### Vulnerability Vector:
In Sprint 5, the test suite uses a test-only `HumanDecisionProvider` that programmatically returns `approve_once` to verify the gating logic. If this provider is left active in production configuration, or if the code fails to strictly segregate test configurations from execution runs, an untrusted worker or prompt-injected agent could leverage the test stub to bypass real human gating.

### Validation Finding & Mitigation:
- **Provider Absence:** The design strictly specifies that **no production/authenticated human-approval provider exists** in Sprint 5.
- **Fail-Closed Default:** The engine treats an unconfigured, default, or missing provider as an immediate `DENY`.
- **Harness Isolation:** The mock provider is confined to test fixtures (`tests/policy/`).
- **Required Correction:** The implementation must ensure that the test-only provider cannot be loaded or resolved if the execution environment is not explicitly configured as `TESTING`. Any load attempt in a non-test runtime environment must raise an uncatchable exception and default the gate to `DENY`.

## 2. Approval Binding and Parameter Scoping

For approvals to be secure, they must be tightly bound to the exact request. 

### Vulnerability Vector:
If an approval is granted for a general capability (e.g. `terminal_execution`) without binding it to the specific command or arguments, a malicious actor could request approval for a safe action (e.g. `ls`), intercept the approval, and then execute an unsafe command (e.g. `rm -rf /`) using the same authorization token.

### Validation Finding & Mitigation:
- **Rich Schema Binding:** The proposed approval record fields (`approval_id`, `requester`, `capability_id`, `proposed_action`, `risk_level`, `affected_resources`, `expected_side_effects`, `expiration`) ensure that approvals are **not** blanket permits.
- **Enforcement Rules:** The coordinator must match the incoming invocation against the *exact* fields recorded in the approval (`proposed_action` and `affected_resources`). If any parameter (such as a command argument or directory path) differs from the approved request, the match fails, and execution is blocked.
- **Single-Use Invariant:** Each approval is consumed exactly once and immediately expired, preventing replay attacks.

## 3. Concurrency and Race Conditions

### Vulnerability Vector:
If two capabilities attempt to consume the same approval record simultaneously in a multi-threaded or multi-process context, a race condition could allow both to succeed before the record is marked as "consumed" (double-allow).

### Validation Finding & Mitigation:
- **Serialization and Locking (D-8 / FAILURE_MODES §3c):** The design requires atomic operations. The check for "is consumed" and the write to "mark consumed" must happen inside a single critical section protected by a local file lock or thread lock.
- **Fail-Closed Contention:** If the lock cannot be acquired, the gate must not proceed. It must return `DENY` rather than risk an unlogged or double-authorized action.

## 4. Authority Escalation Vectors

Could config files, request payloads, worker roles, or test fixtures escalate authority?

- **Config Escalation:** The default-deny rules dictate that configuration settings can only make policy *more* restrictive. No config option is permitted to convert an `approval_required` capability to an auto-allow state.
- **Payload injection:** The evaluator is a pure function that does not read status or privileges from the request payload itself. It only reads the predefined, human-curated JSON policy store. Thus, prompt injection cannot alter the capability's policy boundaries.
- **Worker Self-Approval:** The system registry prevents any active worker or agent from self-approving. All approval decisions must arrive through the `HumanDecisionProvider` seam, which in production is authenticated to the human owner only.
