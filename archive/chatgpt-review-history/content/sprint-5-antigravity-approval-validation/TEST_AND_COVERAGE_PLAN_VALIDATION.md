# TEST_AND_COVERAGE_PLAN_VALIDATION.md
# Magna Enso — Sprint 5 Test and Coverage Plan Independent Validation

## 1. Test Category Separation

The `TEST_AND_VALIDATION_PLAN.md` file correctly segregates the testing requirements into four distinct, non-conflated categories. This prevents the common trap of pretending all security controls are covered by simple unit test checks:

1. **Executable Behavior Tests:** Verified via code execution (allow/deny outcomes, approval coordinator holds, single-use, timeout, JSON schema compliance).
2. **Absence Assertions:** Verified via static checks proving that forbidden surfaces (MCP loader, plugin loaders, API listener, background schedulers) are **not present** in the code workspace (T-6, T-11).
3. **Structural/Path Checks:** Verified via static code shape inspections (verifying a single chokepoint gate exists, verifying JSON stdlib parser usage, verifying provider boundary definitions).
4. **Independent Review Checks:** Verified by the human validator (Antigravity/human owner) verifying terms, lack of overclaims, and lack of tamper-proofing.

## 2. Test-First Implementation Sequence

The implementation plan enforces a **strict tests-first sequence** to ensure that gating and logging code are verified before any execution pathways are opened:

1. **Schema + store tests first:** Prove invalid policy JSONs are rejected and missing files cause fail-closed denials.
2. **Audit sink tests next:** Verify atomic logging, flush syncs, corruption detection (hash-chains), and malformed-tail recovery **before** writing allow paths. The engine must stay deny-only until the logging sink is fully functional.
3. **Gate tests:** Introduce allow states only after step 2 passes. Assert that if logging fails, ALLOWs are converted to DENYs.
4. **Provider tests:** Implement the mock `HumanDecisionProvider` stubs. Test that hold-and-ask logic functions, and that missing providers return DENY.
5. **Reversibility / draft tests:** Verify staging states.
6. **Bypass / negative tests:** Assert denial for all testable bypass classes.

## 3. P-01 through P-13 Chokepoint Coverage Matrix

The coverage matrix accurately represents the status of the 13 policy boundaries defined in the Sprint 3 chokepoint map. It honestly distinguishes between testable-now boundaries and deferred capabilities:

- **Harness-Testable (Green in Sprint 5):** 
  - `P-03` (Model tool dispatch) and `P-04` (Agent-owned tools) are modeled inside the test harness.
- **Absence Assertions (Inert in Sprint 5):** 
  - `P-02` (Registry), `P-06` (Gateway), `P-08` (Providers), `P-11` (Plugin), `P-12` (MCP), and `P-13` (Outbound) are verified as not present/imported.
- **Deferred (Red/Gray in Sprint 5):** 
  - `P-01` (Startup), `P-05` (Scheduler), `P-09` (Memory), and `P-10` (Skill registry) are out of scope and deferred.

This matrix ensures that Sprint 5 is accepted only as a harness-level validation. It guarantees that as each deferred capability is implemented in later sprints, its corresponding policy chokepoint must undergo full validation before it can be marked as complete.

## 4. Rollback and Recovery Validation

- **Process Restart:** Tests must assert that in-flight holds do not resolve to ALLOW on process restarts. They must return DENY or require a fresh simulated approval.
- **Replay/Reuse:** Tests must assert that consumed or expired approvals return DENY if replayed.
- **Rollback simplicity:** Discarding the `sprint/05-policy-engine` branch completely restores the clean main state. Removing the new `policy/` and `tests/policy/` folders removes all Sprint 5 changes, with no impact on the inert `vendor/hermes/` baseline.
