# CANONICAL_SCOPE_VALIDATION.md
# Magna Enso — Sprint 5 Canonical Scope and Decisions Validation

## 1. Canonical Sprint 5 Scope Assessment

The proposed scope for Sprint 5 ("Policy Engine Foundation") matches the features defined in `planning/MAGNA_ENSO_SPRINT_PLAN.md` and `planning/MAGNA_ENSO_FEATURE_TRACKER_TEMPLATE.md` under features `ENSO-F-0501` and `ENSO-F-0502`.

### In-Scope Core Capabilities:
1. **Polaris Policy Engine Foundation:** Standalone Magna-owned policy evaluation core (`policy/`) written in Python standard library only.
2. **Default-Deny Gating (`ENSO-F-0501`):** Every capability call goes through a single gate; no matching policy resolves to `DENY`.
3. **State-Aware Evaluation:** Matched capability policy maps to one of six states: `disabled`, `active_safe`, `read_only`, `report_only`, `draft_only`, or `approval_required`.
4. **Approval-Request Flow (`ENSO-F-0502`):** Gating block on `approval_required` capabilities, requesting decision from `HumanDecisionProvider`, holding execution, consuming approval once, and enforcing timeout/denial.
5. **Durable Evidence & Audit Logging:** Structured append-only logging of every gate decision (allow, deny, hold, approve, reject) before action execution.
6. **Harness-Level Verification:** Standalone execution of the engine proven against a custom test harness (`tests/policy/`) rather than real capability surfaces (since none exist in the inert vendor baseline).

### Explicit Non-Goals:
- **No Remote Control:** No network listeners, WebSocket servers, or remote execution command interfaces (Sprint 11).
- **No Scheduler Execution:** No active background cron loop executing capabilities (Sprint 9).
- **No Observatory UI:** No visual interface or browser dashboard for approvals (Sprint 13).
- **No Auto-Execution:** The engine only returns a decision block; it does not execute side effects itself.
- **No Memory/Skill Subsystems:** Memory persistence and dynamic skill registry gating are deferred (Sprint 8).
- **No Hermes adoption, activation, or build/run:** The inert `vendor/hermes/` baseline remains quarantined and untouched.

## 2. Inconsistencies & Assumptions Check

### OQ-2: Linked Decisions Inconsistency
- **Inconsistency:** The feature card template for `ENSO-F-0501` lists `EH-0012` and `EH-0013` as linked decisions, which refer to git initialization and the read-only audit, rather than the capability governance design decision.
- **Resolution:** This is confirmed as a template placeholder. The actual governing design decision is **`EH-0014`** (governance design accepted). This minor inconsistency is noted and does not impact scope.

### OQ-3 / D-1: Runtime Gate Path Scope Assumption
- **Inconsistency:** The sprint plan states the deliverable is "integration into the runtime gate path," but the vendor baseline is metadata-only and inert. There is no runtime path to integrate into.
- **Resolution:** Addressed by **Decision D-1** (harness scope), defining Sprint 5's scope as standalone engine + gate interface + test harness. This validation confirms that gating against a test harness is the correct, low-risk sequence.

## 3. Decisions D-1 through D-8 Analysis

The approval package consolidates the critical architectural choices into eight pending decisions (D-1 through D-8) in `RISKS_OPEN_QUESTIONS_AND_DECISIONS.md`. This review assesses the completeness and quality of these choices:

| Decision ID | Decision Area | Options Evaluated | Validator Assessment & Rationale |
|---|---|---|---|
| **D-1** | Harness Scope | (a) Standalone harness (b) Wait for runtime | **(a) Recommended.** Building the engine and validating it in a clean test harness before integrating real surfaces prevents early coupling. |
| **D-2** | Approval Persistence | (a) In-memory + audit log (b) Persistent store | **(a) Recommended.** Simpler, lower attack surface. Ensures a process restart resets all in-flight approvals to a safe, default-deny state. |
| **D-3** | Runtime Policy Format | (a) JSON (stdlib) (b) YAML (needs PyYAML) | **(a) Recommended.** Avoids adding third-party dependencies (PyYAML) to the trusted core, minimizing supply-chain risk. |
| **D-4** | Language/Stack | (a) Python stdlib only (b) Allow dependencies | **(a) Recommended.** Zero external dependencies in the policy module matches the safety-by-default posture. |
| **D-5** | Risk R-06 Status | (a) Keep OPEN (b) Downgrade | **(a) Recommended.** The harness cannot prove real-world entry points are closed. R-06 must stay OPEN; validation must recur per capability. |
| **D-6** | Worker Assignment | (a) Codex lead, Antigravity validate | **(a) Recommended.** Proper division of labor (builder vs validator). |
| **D-7** | Human Boundary | (a) Test-only provider, absent prod | **(a) Recommended.** Clear boundary. Asserting simulated test approvals prevents false claims of production human authority. |
| **D-8** | Audit Durability | (a) Append-only JSONL, hash-chain | **(a) Recommended.** Honest model: provides integrity and crash recovery, but admits it does not protect against a local root admin. |

### Decision Quality Assessment:
The decisions are **complete, high-quality, and realistic**. They explicitly avoid overclaiming security boundaries (e.g. admitting audit logs are not write-protected against local admins, and that simulated test approvals are not human-authenticated).
